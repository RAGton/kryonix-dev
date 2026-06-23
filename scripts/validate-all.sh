#!/usr/bin/env bash
# validate-all.sh — tenta nix flake check em cada repo que tem flake.nix
set -euo pipefail
DIR="$(cd "$(dirname "$0")/.." && pwd)"
for repo in "$DIR"/repos/*/; do
  name=$(basename "$repo")
  if [ -f "$repo/flake.nix" ]; then
    echo "=== $name ==="
    nix flake check "$repo" --keep-going 2>&1 | tail -5 || true
    echo ""
  else
    echo "=== $name === (sem flake.nix, pulando)"
  fi
done