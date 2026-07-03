#!/usr/bin/env bash
set -euo pipefail

KDEV="${KDEV:-/home/rocha/kryonix/kryonix-dev}"
PROFILE="${1:-smoke}"
RUN_DATE="$(date +%F)"
RUN_ID="$(date +%H%M%S)"
VAULT="$KDEV/repos/kryonix-vault"
REPORT_DIR="$VAULT/99-Logs/test-runs/$RUN_DATE"
REPORT="$REPORT_DIR/$PROFILE-$RUN_ID.md"

mkdir -p "$REPORT_DIR"

status="PASS"

run_cmd() {
  local name="$1"
  local timeout_seconds="${2:-300}"
  shift 2

  echo "## $name" >> "$REPORT"
  echo '```txt' >> "$REPORT"

  if timeout "$timeout_seconds" "$@" >> "$REPORT" 2>&1; then
    echo '```' >> "$REPORT"
    echo "- $name: PASS" >> "$REPORT"
  else
    rc=$?
    echo '```' >> "$REPORT"
    echo "- $name: FAIL rc=$rc" >> "$REPORT"
    status="FAIL"
  fi

  echo "" >> "$REPORT"
}

sanitize_report() {
  sed -i -E \
    -e 's/\b(api[_-]?key|token|secret|password|passwd)\b[[:space:]]*[:=][[:space:]]*[^[:space:]]+/\1=<REDACTED>/Ig' \
    -e 's/\b(authorization)\b[[:space:]]*:[[:space:]]*bearer[[:space:]]+[A-Za-z0-9._~+\/=-]+/\1: bearer <REDACTED>/Ig' \
    "$REPORT"
}

{
  echo "# Kryonix Test Run"
  echo ""
  echo "- Profile: $PROFILE"
  echo "- Date: $(date -Is)"
  echo "- Host: $(hostname)"
  echo ""
} > "$REPORT"

case "$PROFILE" in
  smoke)
    run_cmd "meta status" 60 bash -lc "cd '$KDEV' && git status --short"
    run_cmd "submodule status" 60 bash -lc "cd '$KDEV' && git submodule status --recursive"
    ;;

  installer-critical)
    run_cmd "installer node test" 180 bash -lc "cd '$KDEV/repos/kryonix-installer/ui' && npm run test"
    ;;

  installer-e2e)
    run_cmd "installer e2e playwright" 300 bash -lc "cd '$KDEV/repos/kryonix-installer/ui' && npx playwright test"
    ;;

  nix-fast)
    run_cmd "flake show kryonix" 300 bash -lc "cd '$KDEV/repos/kryonix' && nix flake show --all-systems"
    ;;

  nix-full)
    if [ "${KRYONIX_ALLOW_HEAVY:-0}" != "1" ]; then
      echo "Profile nix-full requires KRYONIX_ALLOW_HEAVY=1" >&2
      exit 3
    fi
    run_cmd "flake check kryonix" 3600 bash -lc "cd '$KDEV/repos/kryonix' && nix flake check --keep-going -L --show-trace"
    ;;

  python)
    run_cmd "brain pytest" 300 bash -lc "cd '$KDEV/repos/kryonix-brain-lightrag' && pytest -q"
    ;;

  rust)
    run_cmd "home cargo test" 600 bash -lc "cd '$KDEV/repos/kryonix-home' && cargo test"
    ;;

  vault)
    run_cmd "vault scan" 120 bash -lc "cd '$VAULT' && kryonix vault scan"
    run_cmd "vault index" 120 bash -lc "cd '$VAULT' && kryonix vault index"
    ;;

  *)
    echo "Unknown profile: $PROFILE" >&2
    exit 2
    ;;
esac

sanitize_report

echo "" >> "$REPORT"
echo "Final status: $status" >> "$REPORT"

printf '{"profile":"%s","status":"%s","report_path":"%s"}\n' "$PROFILE" "$status" "$REPORT"

test "$status" = "PASS"
