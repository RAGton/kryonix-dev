#!/usr/bin/env bash
# bootstrap.sh — clona todos os repos do ecossistema Kryonix
set -euo pipefail

WORKSPACE="${1:-/home/rocha/kryonix}"
mkdir -p "$WORKSPACE"
cd "$WORKSPACE"

REPOS="
kryonix|https://github.com/RAGton/kryonix.git
kryonixos|https://github.com/RAGton/Kryonixos.git
kryonix-installer|https://github.com/RAGton/kryonix-installer.git
kryonix-brain-lightrag|https://github.com/RAGEnterprise/kryonix-brain-lightrag.git
kryonix-home|https://github.com/RAGton/KRYONIX-HOME.git
kryonix-aura|https://github.com/RAGton/kryonix-aura.git
kryonix-assets|https://github.com/RAGton/kryonix-assets.git
kryonix-vault|https://github.com/RAGton/kryonix-vault.git
kryonix-dev|https://github.com/RAGton/kryonix-dev.git
"

echo "=== Kryonix Workspace Bootstrap ==="
echo "Target: $WORKSPACE"
echo ""

while IFS='|' read -r name url; do
  [ -z "$name" ] && continue
  if [ -d "$name/.git" ]; then
    echo "OK: $name (já clonado)"
  else
    echo "Clonando $name..."
    git clone --depth 1 "$url" "$name" 2>&1 | tail -1
  fi
done <<< "$REPOS"

echo ""
echo "=== Workspace pronto em $WORKSPACE ==="
echo "Repos: $(find "$WORKSPACE" -maxdepth 1 -name '.git' -type d | wc -l)/9"
echo ""
echo "Para clonar submodules do kryonix-dev:"
echo "  cd $WORKSPACE/kryonix-dev && git submodule update --init --recursive"