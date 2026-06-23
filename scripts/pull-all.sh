#!/usr/bin/env bash
# pull-all.sh — git pull --ff-only em todos os repos
set -euo pipefail
DIR="$(cd "$(dirname "$0")/.." && pwd)"
for repo in "$DIR"/repos/*/; do
  name=$(basename "$repo")
  echo "=== $name ==="
  git -C "$repo" pull --ff-only 2>&1 || echo "FAIL: $name"
  echo ""
done