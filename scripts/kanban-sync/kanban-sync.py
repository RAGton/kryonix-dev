#!/usr/bin/env python3
"""
kanban-sync.py — Mirror Hermes Kanban to kryonix-vault.

Reads the Hermes Kanban SQLite database and generates/updates a markdown
file per card in the kryonix-vault submodule. Keeps Vault in sync with
Kanban state, eliminating drift between execution (Kanban) and state
(Vault).

Usage:
  kanban-sync.py                          # sync all cards
  kanban-sync.py --card t_aa0e609b        # sync single card
  kanban-sync.py --dry-run                # show what would be written
  kanban-sync.py --check                  # only check for drift, don't write
  kanban-sync.py --prune                  # delete vault files for missing cards
  kanban-sync.py --vault-path <path>      # custom vault path
  kanban-sync.py --db <path>              # custom kanban SQLite path

Output structure in vault:
  09-Logs/Kryonix/Cards/<card_id>.md      # one file per card
  09-Logs/Kryonix/Cards/_INDEX.md         # summary of all cards
  09-Logs/Kryonix/Cards/kanban-state.json # machine-readable state
  09-Logs/Kryonix/.kanban-sync.log        # append-only sync log

Manual override: add `<!-- manual-override -->` at the top of a card's
file to prevent the script from overwriting manual edits (it will only
update the frontmatter timestamp).

Exit codes:
  0 — no drift / sync complete
  1 — drift detected
  2 — error (db not found, vault not found, etc)
"""

import argparse
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# Defaults — Gabriel's environment
DEFAULT_DB = os.path.expanduser("~/.hermes/kanban/boards/kryonix/kanban.db")
DEFAULT_VAULT = "/home/rocha/Proyectos/kryonix-dev/repos/kryonix-vault"
CARDS_SUBDIR = "09-Logs/Kryonix/Cards"
SYNC_LOG = "09-Logs/Kryonix/.kanban-sync.log"
DEFAULT_AUDIT_CONFIG = "09-Logs/Kryonix/.kanban-sync-audits.json"

# Card ID pattern: t_xxxxxxxx
CARD_ID_RE = re.compile(r"^t_[a-z0-9]{6,}$")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def epoch_to_iso(epoch) -> str:
    """Convert unix epoch (int seconds) to ISO 8601 UTC string. Empty/None returns ''."""
    if not epoch:
        return ""
    try:
        return datetime.fromtimestamp(int(epoch), timezone.utc).isoformat()
    except (ValueError, TypeError, OverflowError):
        return str(epoch)


def parse_existing_frontmatter(content: str) -> Optional[dict]:
    """Parse simple YAML frontmatter if present."""
    if not content.startswith("---\n"):
        return None
    end = content.find("\n---\n", 4)
    if end == -1:
        return None
    fm = content[4:end]
    result = {}
    for line in fm.split("\n"):
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            result[k.strip()] = v.strip()
    return result


def query_all_cards(conn) -> list[dict]:
    """Get all cards with metadata."""
    cur = conn.cursor()
    cur.execute("""
        SELECT id, status, title, priority, body,
                       created_at, started_at, completed_at,
                       result, last_failure_error,
                       created_by, assignee, current_run_id,
                       branch_name, workspace_path, idempotency_key
                FROM tasks
                ORDER BY
            CASE status
                WHEN 'running' THEN 1
                WHEN 'triage' THEN 2
                WHEN 'ready' THEN 3
                WHEN 'blocked' THEN 4
                WHEN 'todo' THEN 5
                WHEN 'scheduled' THEN 6
                WHEN 'done' THEN 7
                ELSE 8
            END,
            id
    """)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def query_card(conn, card_id: str) -> Optional[dict]:
    """Get a single card."""
    cur = conn.cursor()
    cur.execute("""
        SELECT id, status, title, priority, body,
               created_at, started_at, completed_at,
               result, last_failure_error,
               created_by, assignee, current_run_id,
               branch_name, workspace_path, idempotency_key
        FROM tasks WHERE id = ?
    """, (card_id,))
    row = cur.fetchone()
    if not row:
        return None
    cols = [d[0] for d in cur.description]
    return dict(zip(cols, row))


def query_events(conn, card_id: str, limit: int = 10) -> list[dict]:
    cur = conn.cursor()
    cur.execute("""
        SELECT kind, payload, created_at
        FROM task_events
        WHERE task_id = ?
        ORDER BY created_at DESC
        LIMIT ?
    """, (card_id, limit))
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def query_runs(conn, card_id: str, limit: int = 5) -> list[dict]:
    cur = conn.cursor()
    cur.execute("""
        SELECT id, status, outcome, started_at, ended_at
        FROM task_runs
        WHERE task_id = ?
        ORDER BY started_at DESC
        LIMIT ?
    """, (card_id, limit))
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def query_workspace_files(card_id: str) -> list[Path]:
    """List files in the workspace folder for this card."""
    ws_dir = Path(os.path.expanduser(
        f"~/.hermes/kanban/boards/kryonix/workspaces/{card_id}"
    ))
    if not ws_dir.exists():
        return []
    return sorted(ws_dir.rglob("*"))


def is_manual_override(content: str) -> bool:
    """Check if file has manual-override marker."""
    return "<!-- manual-override -->" in content[:500]


def load_audit_config(config_path: Path) -> dict:
    """
    Load audit config from JSON file.

    Expected format:
    {
      "audits": {
        "kanban-drift-2026-08-04": {
          "title": "...",
          "date": "YYYY-MM-DD",
          "state_file": "09-Logs/Kryonix/Audits/.../STATE.md",
          "cards": ["t_xxxxx", ...],
          "notes": "..."
        }
      }
    }
    """
    if not config_path.exists():
        return {"audits": {}}
    try:
        with open(config_path, encoding="utf-8") as f:
            data = json.load(f)
        if "audits" not in data:
            data["audits"] = {}
        return data
    except (json.JSONDecodeError, OSError) as e:
        print(
            f"WARN: failed to load audit config {config_path}: {e}",
            file=sys.stderr,
        )
        return {"audits": {}}


def find_audits_for_card(audit_config: dict, card_id: str) -> list[tuple[str, dict]]:
    """Find all audits that include the given card_id."""
    result = []
    for audit_id, audit_data in audit_config.get("audits", {}).items():
        if card_id in audit_data.get("cards", []):
            result.append((audit_id, audit_data))
    return result


def render_audit_section(audits: list[tuple[str, dict]]) -> str:
    """Render the audits section for a card."""
    if not audits:
        return ""

    lines = ["## Audits\n"]
    lines.append("This card is part of the following audit(s):\n")
    for audit_id, audit in audits:
        title = audit.get("title", audit_id)
        date = audit.get("date", "?")
        state_file = audit.get("state_file", "")
        notes = audit.get("notes", "")

        # Obsidian wikilink to the state file
        if state_file:
            # Make path relative to the Cards/ subdir
            # Cards/ → 09-Logs/Kryonix/Cards/
            # state_file → 09-Logs/Kryonix/Audits/kanban-drift-2026-08-04/STATE.md
            # So the relative path from Cards/ is ../Audits/.../STATE.md
            try:
                rel = os.path.relpath(state_file, CARDS_SUBDIR)
                link_target = rel.replace(".md", "")
            except ValueError:
                link_target = state_file
            lines.append(f"- `[{audit_id}]({rel})` — **{title}** ({date})")
        else:
            lines.append(f"- **{audit_id}** — {title} ({date})")

        if notes:
            lines.append(f"  - {notes}")

    lines.append("")
    return "\n".join(lines)


def render_card_markdown(
    card: dict,
    events: list,
    runs: list,
    workspace_files: list,
    previous: Optional[dict] = None,
    audits: Optional[list[tuple[str, dict]]] = None,
) -> str:
    """Render a card to markdown."""
    if audits is None:
        audits = []

    drift_block = ""
    if previous and previous.get("last_kanban_state") != card.get("status"):
        drift_block = (
            f"> [!warning] **DRIFT DETECTADO**\n"
            f"> Última sincronização: `{previous.get('last_sync_at', '?')}`\n"
            f"> Estado anterior: `{previous.get('last_kanban_state', '?')}`\n"
            f"> Estado atual: `{card.get('status', '?')}`\n\n"
        )

    body_section = ""
    if card.get("body"):
        body_text = card["body"].strip()
        # Don't escape — just include as markdown
        body_section = f"## Descrição\n\n{body_text}\n\n"

    result_section = ""
    if card.get("result"):
        result_section = f"## Result\n\n`{card['result']}`\n\n"

    failure_section = ""
    if card.get("last_failure_error"):
        err = card["last_failure_error"]
        # truncate to 500 chars to keep cards readable
        if len(err) > 500:
            err = err[:500] + "..."
        failure_section = f"## Last failure\n\n```\n{err}\n```\n\n"

    # Execução timestamps (started_at, completed_at)
    exec_section = ""
    started_iso = epoch_to_iso(card.get("started_at"))
    completed_iso = epoch_to_iso(card.get("completed_at"))
    if started_iso or completed_iso:
        exec_section = "## Execução timestamps\n\n"
        if started_iso:
            exec_section += f"- **Iniciado:** `{started_iso}`\n"
        if completed_iso:
            exec_section += f"- **Concluído:** `{completed_iso}`\n"
        exec_section += "\n"

    # Assignment (created_by + assignee) — only render if non-default
    assignment_section = ""
    created_by = card.get("created_by")
    assignee = card.get("assignee")
    if (created_by and created_by != "user") or (assignee and assignee != "default"):
        assignment_section = "## Assignment\n\n"
        if created_by:
            assignment_section += f"- **Criado por:** `{created_by}`\n"
        if assignee:
            assignment_section += f"- **Assignee:** `{assignee}`\n"
        assignment_section += "\n"

    # Current run (only if non-null)
    current_run_section = ""
    current_run_id = card.get("current_run_id")
    if current_run_id:
        current_run_section = f"## Current run\n\n`run_id: {current_run_id}`\n\n"

    # Branch (only if non-null)
    branch_section = ""
    branch_name = card.get("branch_name")
    if branch_name:
        branch_section = f"## Branch\n\n`{branch_name}`\n\n"

    # Workspace path (only if non-null)
    ws_path_section = ""
    ws_path = card.get("workspace_path")
    if ws_path:
        ws_path_section = f"## Workspace\n\n`{ws_path}`\n\n"

    # External ID (idempotency_key) — only if non-null
    external_id_section = ""
    idemp_key = card.get("idempotency_key")
    if idemp_key:
        external_id_section = f"## External ID\n\n`{idemp_key}`\n\n"

    audit_section = render_audit_section(audits)

    events_section = ""
    if events:
        events_section = "## Eventos recentes\n\n"
        events_section += "| Timestamp | Tipo | Payload |\n"
        events_section += "|-----------|------|---------|\n"
        for ev in events:
            ts = epoch_to_iso(ev.get("created_at"))
            kind = ev.get("kind", "?")
            payload = str(ev.get("payload", ""))
            # Escape pipe characters
            payload = payload.replace("|", "\\|").replace("\n", " ")
            if len(payload) > 200:
                payload = payload[:200] + "..."
            events_section += f"| `{ts}` | `{kind}` | {payload} |\n"
        events_section += "\n"

    runs_section = ""
    if runs:
        runs_section = "## Execuções recentes\n\n"
        runs_section += "| Run ID | Status | Outcome | Início | Fim |\n"
        runs_section += "|--------|--------|---------|--------|-----|\n"
        for r in runs:
            run_id = str(r.get("id", "?"))[:12]
            runs_section += (
                f"| `{run_id}` "
                f"| {r.get('status', '?')} "
                f"| {r.get('outcome', '?')} "
                f"| {epoch_to_iso(r.get('started_at'))} "
                f"| {epoch_to_iso(r.get('ended_at'))} |\n"
            )
        runs_section += "\n"

    workspace_section = ""
    if workspace_files:
        workspace_section = "## Workspace (no Kanban)\n\n"
        home = Path.home()
        for f in workspace_files[:15]:
            try:
                rel = f.relative_to(home / ".hermes/kanban/boards/kryonix/workspaces")
                workspace_section += f"- `{rel}`\n"
            except ValueError:
                workspace_section += f"- `{f}`\n"
        if len(workspace_files) > 15:
            workspace_section += f"- _... e mais {len(workspace_files) - 15} arquivos_\n"
        workspace_section += "\n"

    # Frontmatter — include audits as YAML list
    audits_yaml = ""
    if audits:
        audits_yaml = "audits:\n"
        for audit_id, _ in audits:
            audits_yaml += f"  - {audit_id}\n"
    else:
        audits_yaml = "audits: []\n"

    frontmatter = (
        f"---\n"
        f"card_id: {card.get('id', '')}\n"
        f"status: {card.get('status', '')}\n"
        f"type: {card.get('type', '')}\n"
        f"priority: {card.get('priority', '')}\n"
        f"created_at: {epoch_to_iso(card.get('created_at', ''))}\n"
        f"started_at: {epoch_to_iso(card.get('started_at', ''))}\n"
        f"completed_at: {epoch_to_iso(card.get('completed_at', ''))}\n"
        f"last_sync_at: {now_iso()}\n"
        f"last_kanban_state: {card.get('status', '')}\n"
        f"result: {card.get('result', '')}\n"
        f"auto_generated: true\n"
        f"{audits_yaml}"
        f"---\n\n"
    )

    return (
        f"{frontmatter}"
        f"# {card.get('title', 'Sem título')}\n\n"
        f"**Card:** `{card.get('id', '?')}` | "
        f"**Status:** `{card.get('status', '?')}`\n\n"
        f"{drift_block}"
        f"{body_section}"
        f"{result_section}"
        f"{failure_section}"
        f"{exec_section}"
        f"{assignment_section}"
        f"{current_run_section}"
        f"{branch_section}"
        f"{ws_path_section}"
        f"{external_id_section}"
        f"{audit_section}"
        f"{events_section}"
        f"{runs_section}"
        f"{workspace_section}"
        f"---\n\n"
        f"_Auto-gerado por `kanban-sync.py` em {now_iso()}. "
        f"Para parar de sobrescrever, adicione `<!-- manual-override -->` no topo. "
        f"Para editar metadados, edite o card no Kanban (este arquivo é derivado)._"
    )


def render_index(cards: list[dict]) -> str:
    """Render the _INDEX.md summary file."""
    by_status: dict[str, list[dict]] = {}
    for c in cards:
        by_status.setdefault(c.get("status", "unknown"), []).append(c)

    lines = [
        "---",
        f"generated_at: {now_iso()}",
        f"total_cards: {len(cards)}",
        "auto_generated: true",
        "---",
        "",
        "# Kanban Index — kryonix\n",
        f"Total: **{len(cards)} cards** | Sincronizado em {now_iso()}\n",
        "## Distribuição por status\n",
    ]

    status_order = ["running", "triage", "ready", "blocked", "todo", "scheduled", "done"]
    sorted_statuses = sorted(by_status.keys(), key=lambda s: (
        status_order.index(s) if s in status_order else 99
    ))

    for status in sorted_statuses:
        cards_in_status = by_status[status]
        lines.append(f"### `{status}` ({len(cards_in_status)})\n")
        for c in cards_in_status:
            title = c.get("title", "Sem título")[:80]
            card_id = c.get("id", "?")
            lines.append(f"- [`{card_id}`](./{card_id}.md) — {title}")
        lines.append("")

    lines.append("---")
    lines.append(f"_Auto-gerado por `kanban-sync.py`._")
    return "\n".join(lines)


def render_state_json(cards: list[dict]) -> str:
    """Render machine-readable state."""
    state = {
        "generated_at": now_iso(),
        "total": len(cards),
        "by_status": {},
        "cards": [],
    }
    for c in cards:
        s = c.get("status", "unknown")
        state["by_status"][s] = state["by_status"].get(s, 0) + 1
        state["cards"].append({
            "id": c.get("id"),
            "status": c.get("status"),
            "title": c.get("title"),
            "type": c.get("type"),
            "priority": c.get("priority"),
            "updated_at": c.get("updated_at"),
        })
    return json.dumps(state, indent=2, ensure_ascii=False)


def sync_card(
    conn, vault_path: Path, card: dict, audit_config: dict, dry_run: bool = False
) -> tuple[str, str]:
    """Sync a single card. Returns (status, message)."""
    card_id = card["id"]
    cards_dir = vault_path / CARDS_SUBDIR
    target = cards_dir / f"{card_id}.md"

    events = query_events(conn, card_id)
    runs = query_runs(conn, card_id)
    workspace_files = query_workspace_files(card_id)
    audits = find_audits_for_card(audit_config, card_id)

    previous = None
    manual = False
    if target.exists():
        try:
            content = target.read_text(encoding="utf-8")
            previous = parse_existing_frontmatter(content)
            manual = is_manual_override(content)
        except Exception as e:
            return ("error", f"{card_id}: failed to read existing: {e}")

    if manual:
        return ("skipped", f"{card_id}: manual-override active, skipping body rewrite")

    markdown = render_card_markdown(
        card, events, runs, workspace_files, previous, audits
    )

    if dry_run:
        audit_info = f" [+{len(audits)} audit(s)]" if audits else ""
        return ("dry", f"{card_id}{audit_info}: would write {target} ({len(markdown)} bytes)")

    try:
        cards_dir.mkdir(parents=True, exist_ok=True)
        target.write_text(markdown, encoding="utf-8")
    except Exception as e:
        return ("error", f"{card_id}: failed to write: {e}")

    drift = ""
    if previous and previous.get("last_kanban_state") != card.get("status"):
        drift = " [DRIFT]"
    audit_info = f" [+{len(audits)} audit(s)]" if audits else ""
    return ("ok", f"{card_id}{drift}{audit_info}: wrote {target} ({len(markdown)} bytes)")


def main():
    parser = argparse.ArgumentParser(
        description="Sync Hermes Kanban cards to kryonix-vault",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--card", help="Sync only this card ID")
    parser.add_argument(
        "--vault-path", default=DEFAULT_VAULT, help="Path to kryonix-vault"
    )
    parser.add_argument(
        "--db", default=DEFAULT_DB, help="Path to kanban SQLite"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Show what would be written"
    )
    parser.add_argument(
        "--check", action="store_true", help="Only check for drift, don't write"
    )
    parser.add_argument(
        "--prune", action="store_true", help="Delete vault files for missing cards"
    )
    parser.add_argument(
        "--config", help="Path to audit config JSON (default: <vault>/09-Logs/Kryonix/.kanban-sync-audits.json)"
    )
    parser.add_argument(
        "--validate-config", action="store_true", help="Validate audit config and exit"
    )
    parser.add_argument(
        "--quiet", action="store_true", help="Suppress per-card output"
    )
    args = parser.parse_args()

    db_path = Path(args.db)
    vault_path = Path(args.vault_path)

    if not db_path.exists():
        print(f"ERROR: Kanban DB not found: {db_path}", file=sys.stderr)
        sys.exit(2)
    if not vault_path.exists():
        print(f"ERROR: Vault not found: {vault_path}", file=sys.stderr)
        sys.exit(2)

    # Load audit config
    if args.config:
        config_path = Path(args.config)
    else:
        config_path = vault_path / DEFAULT_AUDIT_CONFIG
    audit_config = load_audit_config(config_path)

    if args.validate_config:
        # Validate and exit
        total_audits = len(audit_config.get("audits", {}))
        total_cards = sum(
            len(a.get("cards", []))
            for a in audit_config.get("audits", {}).values()
        )
        print(f"Config: {config_path}")
        print(f"Audits: {total_audits}")
        print(f"Cards in audits: {total_cards}")
        for audit_id, audit in audit_config.get("audits", {}).items():
            print(f"  - {audit_id}: {len(audit.get('cards', []))} cards")
            for c in audit.get("cards", []):
                print(f"      - {c}")
        sys.exit(0)

    # Open SQLite read-only
    try:
        conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    except sqlite3.OperationalError as e:
        print(f"ERROR: Cannot open Kanban DB: {e}", file=sys.stderr)
        sys.exit(2)

    try:
        # Get cards
        if args.card:
            card = query_card(conn, args.card)
            if not card:
                print(f"ERROR: Card {args.card} not found", file=sys.stderr)
                sys.exit(1)
            cards = [card]
        else:
            cards = query_all_cards(conn)

        if args.check:
            # Drift check
            drift_count = 0
            new_count = 0
            cards_dir = vault_path / CARDS_SUBDIR
            for card in cards:
                target = cards_dir / f"{card['id']}.md"
                if not target.exists():
                    print(f"NEW: {card['id']} ({card['status']}) — {card.get('title', '')[:60]}")
                    new_count += 1
                    continue
                try:
                    content = target.read_text(encoding="utf-8")
                    prev = parse_existing_frontmatter(content)
                except Exception:
                    continue
                if prev and prev.get("last_kanban_state") != card["status"]:
                    print(
                        f"DRIFT: {card['id']} "
                        f"prev={prev.get('last_kanban_state')} "
                        f"now={card['status']}"
                    )
                    drift_count += 1
            print(
                f"\nCheck: {len(cards)} cards, "
                f"{drift_count} drifted, {new_count} new"
            )
            sys.exit(1 if drift_count > 0 else 0)

        # Sync
        counts = {"ok": 0, "skipped": 0, "error": 0, "dry": 0}
        for card in cards:
            status, msg = sync_card(
                conn, vault_path, card, audit_config, dry_run=args.dry_run
            )
            counts[status] = counts.get(status, 0) + 1
            if not args.quiet:
                print(msg)

        # Write index + state files (only on full sync, not single card)
        if not args.card and not args.dry_run:
            cards_dir = vault_path / CARDS_SUBDIR
            try:
                (cards_dir / "_INDEX.md").write_text(
                    render_index(cards), encoding="utf-8"
                )
                (cards_dir / "kanban-state.json").write_text(
                    render_state_json(cards), encoding="utf-8"
                )
            except Exception as e:
                print(f"WARN: failed to write index: {e}", file=sys.stderr)

        # Optional prune
        if args.prune and not args.dry_run:
            cards_dir = vault_path / CARDS_SUBDIR
            if cards_dir.exists():
                card_ids = {c["id"] for c in cards}
                for f in cards_dir.glob("t_*.md"):
                    if f.stem not in card_ids:
                        f.unlink()
                        if not args.quiet:
                            print(f"pruned {f}")

        # Log
        if not args.dry_run:
            log_path = vault_path / SYNC_LOG
            log_path.parent.mkdir(parents=True, exist_ok=True)
            with open(log_path, "a", encoding="utf-8") as f:
                audits_in_use = sum(
                    1 for c in cards
                    if find_audits_for_card(audit_config, c["id"])
                )
                f.write(
                    f"{now_iso()} synced {counts['ok']} ok, "
                    f"{counts['skipped']} skipped, {counts['error']} errors, "
                    f"{len(cards)} total ({audits_in_use} with audits, "
                    f"dry={args.dry_run}, card={args.card})\n"
                )

        if not args.quiet:
            print(
                f"\nDone: {counts['ok']} ok, {counts['skipped']} skipped, "
                f"{counts['error']} errors ({len(cards)} total)"
            )
            if not args.dry_run:
                print(f"Index: {vault_path / CARDS_SUBDIR / '_INDEX.md'}")
                print(f"State: {vault_path / CARDS_SUBDIR / 'kanban-state.json'}")

        sys.exit(0 if counts.get("error", 0) == 0 else 1)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
