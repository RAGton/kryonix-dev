#!/usr/bin/env bash
# bump-kryx-cli.sh — Idempotente. Sincroniza o input kryx-cli do kryonix
# com a última tag de RAGton/kryx-cli. Idempotente: re-rodar é no-op.
#
# Uso:
#   ./scripts/bump-kryx-cli.sh              # detecta e aplica
#   ./scripts/bump-kryx-cli.sh --dry-run    # só mostra o que faria
#   ./scripts/bump-kryx-cli.sh --version=vX.Y.Z  # força versão alvo
#   ./scripts/bump-kryx-cli.sh --no-push    # commita mas não faz push
#
# Pré-requisitos: rodar dentro do workspace kryonix-dev, com submodules
# kryx-cli e kryonix inicializados.
#
# Saídas (códigos):
#   0 = já estava em dia OU bump aplicado com sucesso
#   1 = erro genérico
#   2 = flag inválida
#   3 = tag alvo não existe no upstream
#   4 = working tree suja (refuse pra não mascarar mudanças)

set -euo pipefail

# ---------- paths ----------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEV_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
KRYX_CLI_DIR="$DEV_ROOT/repos/kryx-cli"
KRYONIX_DIR="$DEV_ROOT/repos/kryonix"
KRYX_CLI_FLAKE_NIX="$KRYONIX_DIR/flake.nix"
KRYX_CLI_CARGO_TOML="$KRYX_CLI_DIR/Cargo.toml"

# ---------- helpers ----------
log()  { printf '[bump] %s\n' "$*" >&2; }
err()  { printf '[bump][ERR] %s\n' "$*" >&2; exit "${2:-1}"; }

# ---------- parse args ----------
DRY_RUN=false
NO_PUSH=false
FORCE_VERSION=""
while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run)        DRY_RUN=true; shift ;;
    --no-push)        NO_PUSH=true; shift ;;
    --version=*)      FORCE_VERSION="${1#*=}"; shift ;;
    -h|--help)
      sed -n '2,20p' "$0"
      exit 0
      ;;
    *) err "flag inválida: $1" 2 ;;
  esac
done

# ---------- sanity ----------
# Aceita tanto .git/ quanto .git (arquivo de submodule apontando pro parent)
git_dir_ok() {
  [ -d "$1/.git" ] || [ -f "$1/.git" ]
}
git_dir_ok "$KRYX_CLI_DIR"  || err "submodule kryx-cli não inicializado em $KRYX_CLI_DIR"
git_dir_ok "$KRYONIX_DIR"   || err "submodule kryonix não inicializado em $KRYONIX_DIR"
[ -f "$KRYX_CLI_FLAKE_NIX" ] || err "flake.nix do kryonix não encontrado"
[ -f "$KRYX_CLI_CARGO_TOML" ] || err "Cargo.toml do kryx-cli não encontrado"

# ---------- descobrir versão alvo ----------
discover_latest_upstream_version() {
  git ls-remote --tags --sort=-v:refname \
    https://github.com/RAGton/kryx-cli.git 2>/dev/null \
    | awk '{print $2}' \
    | sed -n 's#^refs/tags/v##p' \
    | grep -E '^[0-9]+\.[0-9]+\.[0-9]+$' \
    | head -n1
}

discover_current_version_in_flake() {
  # Extrai a tag atual de `kryx-cli = { url = "github:RAGton/kryx-cli/vX.Y.Z";`
  awk -F'"' '/kryx-cli = \{/ {getline; print $2}' "$KRYX_CLI_FLAKE_NIX" \
    | sed -n 's#^github:RAGton/kryx-cli/v##p'
}

discover_current_version_in_cargo() {
  awk -F'"' '/^version *= */ {print $2; exit}' "$KRYX_CLI_CARGO_TOML"
}

TARGET="${FORCE_VERSION#v}"
TARGET="${TARGET:-$(discover_latest_upstream_version)}"
[ -n "$TARGET" ] || err "nenhuma tag vX.Y.Z encontrada no upstream" 3

CURRENT_FLAKE="$(discover_current_version_in_flake)"
CURRENT_CARGO="$(discover_current_version_in_cargo)"

log "alvo        : v$TARGET"
log "flake.nix   : v${CURRENT_FLAKE:-<vazio>}"
log "Cargo.toml  : v${CURRENT_CARGO:-<vazio>}"

# ---------- checagem de working tree ----------
require_clean_tree() {
  local dir="$1" label="$2"
  if ! git -C "$dir" diff --quiet HEAD 2>/dev/null \
     || [ -n "$(git -C "$dir" status --porcelain)" ]; then
    err "$label tem working tree suja; commit/stash primeiro (refuse bump pra não mascarar mudanças)" 4
  fi
}

require_clean_tree "$KRYX_CLI_DIR"  "kryx-cli"
require_clean_tree "$KRYONIX_DIR"   "kryonix"
require_clean_tree "$DEV_ROOT"      "kryonix-dev"

# ---------- sem mudanças necessárias? ----------
if [ "$CURRENT_FLAKE" = "$TARGET" ] && [ "$CURRENT_CARGO" = "$TARGET" ]; then
  log "já está em v$TARGET, nada a fazer"
  exit 0
fi

# ---------- aplicar patch ----------
apply_patch() {
  local file="$1" pattern="$2" replacement="$3"
  if grep -qF "$pattern" "$file"; then
    sed -i "s|$pattern|$replacement|" "$file"
  else
    err "padrão não encontrado em $file: $pattern"
  fi
}

log "aplicando bump em flake.nix + Cargo.toml"

# flake.nix: atualiza url e rev_pin (mantém comments existentes via busca simples)
apply_patch "$KRYX_CLI_FLAKE_NIX" \
  'github:RAGton/kryx-cli/v'"${CURRENT_FLAKE:-0.0.0}" \
  'github:RAGton/kryx-cli/v'"$TARGET"

# Cargo.toml
apply_patch "$KRYX_CLI_CARGO_TOML" \
  'version = "'"${CURRENT_CARGO:-0.0.0}"'"' \
  'version = "'"$TARGET"'"'

# ---------- commit ----------
run_or_dry() {
  if $DRY_RUN; then
    log "[dry-run] $*"
  else
    "$@"
  fi
}

COMMIT_MSG_KRYX="chore(kryx-cli): bump version ${CURRENT_CARGO:-0.0.0} -> ${TARGET}"
COMMIT_MSG_KRYONIX="chore(kryonix): bump kryx-cli input v${CURRENT_FLAKE:-0.0.0} -> v${TARGET}"
COMMIT_MSG_DEV="chore(dev): bump kryx-cli to ${TARGET} (automated by bump-kryx-cli.sh)"

log "commit em kryx-cli"
run_or_dry git -C "$KRYX_CLI_DIR" add Cargo.toml
run_or_dry git -C "$KRYX_CLI_DIR" commit -m "$COMMIT_MSG_KRYX"

log "commit em kryonix"
run_or_dry git -C "$KRYONIX_DIR" add flake.nix
run_or_dry git -C "$KRYONIX_DIR" commit -m "$COMMIT_MSG_KRYONIX"

log "atualizando submodule pointer no kryonix-dev"
run_or_dry git -C "$DEV_ROOT" add repos/kryx-cli
run_or_dry git -C "$DEV_ROOT" commit -m "$COMMIT_MSG_DEV"

# ---------- push ----------
if ! $NO_PUSH && ! $DRY_RUN; then
  log "push em kryx-cli"
  git -C "$KRYX_CLI_DIR" push origin HEAD:main
  log "push em kryonix"
  git -C "$KRYONIX_DIR" push origin HEAD:main
  log "push em kryonix-dev"
  git -C "$DEV_ROOT" push origin HEAD:main
elif $DRY_RUN; then
  log "[dry-run] git push (kryx-cli, kryonix, kryonix-dev)"
else
  log "--no-push: commits feitos localmente, push manual necessário"
fi

# ---------- retag (somente se a versão alvo foi detectada do upstream) ----------
if [ -z "$FORCE_VERSION" ] && ! $DRY_RUN; then
  log "tag v$TARGET já existe no upstream; nada a retaggar"
fi

log "OK: bump para v$TARGET concluído"
exit 0