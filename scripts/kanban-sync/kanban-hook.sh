#!/usr/bin/env bash
# kanban-hook.sh — post-tool-call hook for Hermes
#
# Drop this file at:
#   ~/.hermes/hooks/post-tool-call.sh
# (or wherever Hermes expects hooks)
#
# It detects kanban_* tool calls in the agent's tool-use stream and
# triggers kanban-sync.py --card <id> automatically.
#
# Hermes hook contract (verify in your Hermes docs):
#   - Reads JSON from stdin with the tool name and arguments
#   - Returns exit code 0 to continue
#   - Can run side effects
#
# If Hermes doesn't have a hook system, Aura can call this script
# directly after each kanban_* tool call.

set -euo pipefail

# Resolve symlinks so this works whether called directly or via /home/rocha/Proyectos/kryonix-dev/scripts/kanban-sync/kanban-hook.sh (Patched 2026-08-05)
SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)"
SYNC_SH="${SCRIPT_DIR}/kanban-sync.sh"

# Try to read JSON from stdin (Hermes hook pattern)
if [[ -t 0 ]]; then
    # No stdin — running manually
    echo "kanban-hook: no stdin (use directly: ${SYNC_SH} t_xxxxx)" >&2
    exit 0
fi

INPUT=$(cat)

# Extract tool name and arguments
TOOL_NAME=$(echo "$INPUT" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    print(data.get('tool', data.get('name', '')))
except Exception as e:
    print('', file=sys.stderr)
    sys.exit(0)
" 2>/dev/null || echo "")

# Only act on kanban_* tool calls
if [[ ! "$TOOL_NAME" =~ ^kanban_ ]]; then
    exit 0
fi

# Extract card_id from arguments
CARD_ID=$(echo "$INPUT" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    args = data.get('arguments', data.get('args', {}))
    print(args.get('card_id', args.get('id', '')))
except Exception:
    print('', file=sys.stderr)
    sys.exit(0)
" 2>/dev/null || echo "")

if [[ -z "$CARD_ID" ]] || [[ ! "$CARD_ID" =~ ^t_[a-z0-9]{6,}$ ]]; then
    # No card_id in args, or invalid format — do a full sync
    "$SYNC_SH" --quiet 2>&1 || true
    exit 0
fi

# Sync this specific card
"$SYNC_SH" --card "$CARD_ID" --quiet 2>&1 || true

exit 0
