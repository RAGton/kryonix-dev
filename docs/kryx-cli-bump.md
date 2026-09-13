# kryx-cli bump — automação do ciclo de release

## Por que isto existe

O `kryx-cli` é o CLI Rust publicado (`RAGton/kryx-cli`) que embrulha
`nh os switch`, `nix flake update` e comandos relacionados. O repo
`RAGton/kryonix` consome o `kryx-cli` como flake input, pinado em uma
tag semver (`vX.Y.Z`). Quando uma nova versão do `kryx-cli` é
publicada, três lugares precisam ser atualizados em sequência:

1. `RAGton/kryx-cli` — tag publicada (`git tag -a vX.Y.Z` + `git push --tags`)
2. `RAGton/kryonix/flake.nix` — input `kryx-cli.url` apontando pra tag nova
3. `RAGton/kryonix-dev/repos/kryonix` — submodule pointer atualizado

Fazer isto manualmente a cada release é lento e propenso a erro. Este
diretório contém a automação.

## Os dois caminhos

### 1. Caminho GitHub Actions (modo produção)

Workflow: [`bump-kryx-cli.yml`](../../repos/kryonix/.github/workflows/bump-kryx-cli.yml)

**Setup único (você precisa fazer uma vez):**

```bash
# Em RAGton/kryx-cli, criar um PAT com scope 'repo' e adicioná-lo como
# secret KRYONIX_DISPATCH_TOKEN em RAGton/kryonix Settings → Secrets.

# Em RAGton/kryx-cli, criar .github/workflows/tag-notify.yml:
cat > .github/workflows/tag-notify.yml <<'YAML'
name: notify-kryonix
on:
  push:
    tags: ['v*.*.*']
jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger kryonix bump
        run: |
          TAG="${GITHUB_REF_NAME}"
          curl -X POST \
            -H "Authorization: token ${{ secrets.KRYONIX_DISPATCH_TOKEN }}" \
            -H "Accept: application/vnd.github+json" \
            https://api.github.com/repos/RAGton/kryonix/dispatches \
            -d "{\"event_type\":\"kryx-cli-tag\",\"client_payload\":{\"tag\":\"$TAG\"}}"
YAML
```

**Fluxo de release a partir daí:**

```bash
cd repos/kryx-cli
# faz as mudanças, commita, valida
cargo fmt && cargo clippy --all-targets -- -D warnings && cargo test --release
git tag -a vX.Y.Z -m "..."
git push origin main --follow-tags
# → automaticamente dispara workflow em RAGton/kryonix
# → automaticamente abre PR com flake.nix atualizado
# → você revisa e mergeia
# → consumers (inspiron, glacier) pegam na próxima atualização
```

**Nada de bump manual no `kryonix/flake.nix` — fica automático.**

### 2. Caminho script local (modo desenvolvimento)

Script: [`bump-kryx-cli.sh`](../../scripts/bump-kryx-cli.sh)

Usar quando:
- Está testando localmente antes de criar a tag.
- Quer aplicar o bump de várias tags de uma vez.
- O GitHub Actions está fora do ar / quer fallback offline.
- Quer auditar o que vai mudar antes de aplicar (`--dry-run`).

**Uso:**

```bash
cd /home/rocha/projetos/kryonix/kryonix-dev

# Dry-run: mostra o que mudaria sem aplicar
./scripts/bump-kryx-cli.sh --dry-run

# Aplicar de verdade, com push
./scripts/bump-kryx-cli.sh

# Forçar versão específica
./scripts/bump-kryx-cli.sh --version=v0.3.3

# Commitar mas não fazer push (você revisa antes)
./scripts/bump-kryx-cli.sh --no-push
```

**Garantias do script:**
- Idempotente: re-rodar sem mudanças necessárias sai com exit 0 e mensagem "já está em vX.Y.Z, nada a fazer".
- Working tree check: recusa bump se qualquer um dos três repos (`kryx-cli`, `kryonix`, `kryonix-dev`) tem mudanças não commitadas.
- Não usa `git add .`, `git reset --hard`, `git push --force` — apenas paths explícitos.
- Detecta a última tag via `git ls-remote --tags`, ordenação semver.

## Invariantes

1. **A tag é a fonte da verdade.** O `Cargo.toml` deve estar com `version = "X.Y.Z"` igual à tag. O `bump-kryx-cli.sh` mantém os dois em sincronia.
2. **PR review é obrigatório.** O workflow GitHub Actions abre PR mas nunca mergeia sozinho. Humanos revisam.
3. **Nunca pinar em rev (commit hash) sem tag.** Tags semver são o contrato. Pins em commit são aceitáveis para hot-fixes urgentes, mas devem virar tag depois.
4. **Submodule pointer sempre atualizado.** Após bumpar `kryonix/flake.nix`, o `kryonix-dev/repos/kryonix` precisa ser commitado também. O script e o workflow GitHub Actions já fazem isso.

## Histórico

| Data       | Versão | Mudança |
|------------|--------|---------|
| 2026-09-13 | v0.3.2 | Patch inicial: `update.rs` só stasha em mudanças não-lock, novos flags `--no-stash` + `--cleanup-stash`. Cria script + workflow automatizados. |

## Pendências

- [ ] Adicionar `tag-notify.yml` em `RAGton/kryx-cli` (workflow que dispara dispatch).
- [ ] Configurar PAT + secret `KRYONIX_DISPATCH_TOKEN` no repo `RAGton/kryonix`.
- [ ] Adicionar entrada semanal no systemd-user do Aura (`/etc/systemd/user/bump-kryx-cli.service` + `.timer`) para auditoria semanal via script local.
- [ ] Validar primeira execução ponta-a-ponta: criar tag fake `v0.3.3` em branch sandbox, ver se PR abre automático.