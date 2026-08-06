#!/usr/bin/env bash
# kanban-sync.sh — wrapper for kanban-sync.py
# Resolve symlink correctly: BASH_SOURCE[0] gives symlink path, readlink -f gives real file.
set -euo pipefail

# Resolve real path even when called via symlink
SCRIPT_PATH="$(readlink -f "${BASH_SOURCE[0]}")"
SCRIPT_DIR="$(cd "$(dirname "$SCRIPT_PATH")" && pwd)"
PY_SCRIPT="${SCRIPT_DIR}/kanban-sync.py"

if [[ ! -f "$PY_SCRIPT" ]]; then
    echo "ERROR: ${PY_SCRIPT} not found" >&2
    exit 2
fi

if ! command -v python3 >/dev/null 2>&1; then
    echo "ERROR: python3 not in PATH" >&2
    exit 2
fi

# Wrapper-level flags (intercept before passing to python)
case "${1:-}" in
    --version|-v)
        echo "kanban-sync wrapper v1 (python script v1.0)"
        exit 0
        ;;
    --help|-h)
        echo "kanban-sync — Hermes Kanban → kryonix-vault sync"
        echo ""
        echo "Wrapper for kanban-sync.py. Passes all flags through to python."
        echo "Use --help on the python script for full options:"
        echo "  kanban-sync --help"
        echo ""
        echo "Wrapper-specific flags:"
        echo "  --version, -v   Show wrapper version"
        echo "  --help, -h      Show this help"
        exit 0
        ;;
esac

exec python3 "$PY_SCRIPT" "$@"
