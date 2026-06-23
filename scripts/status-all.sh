#!/usr/bin/env bash
# status-all.sh — mostra status git de todos os repos
set -euo pipefail
DIR="$(cd "$(dirname "$0")/.." && pwd)"
for repo in "$DIR"/repos/*/; do
  name=$(basename "$repo")
  echo "=== $name ==="
  git -C "$repo" status --short 2>/dev/null || echo "(no git)"
  echo ""
done