# Development Workspace

## Localização

O workspace de desenvolvimento oficial é:

```
/home/rocha/kryonix/
```

Com todos os repos clonados lado a lado:

| Repo | Caminho local |
|---|---|
| `kryonix` | `/home/rocha/kryonix/kryonix` |
| `kryonixos` | `/home/rocha/kryonix/kryonixos` |
| `kryonix-installer` | `/home/rocha/kryonix/kryonix-installer` |
| `kryonix-brain-lightrag` | `/home/rocha/kryonix/kryonix-brain-lightrag` |
| `kryonix-home` | `/home/rocha/kryonix/kryonix-home` |
| `kryonix-aura` | `/home/rocha/kryonix/kryonix-aura` |
| `kryonix-assets` | `/home/rocha/kryonix/kryonix-assets` |
| `kryonix-vault` | `/home/rocha/kryonix/kryonix-vault` |
| `kryonix-dev` | `/home/rocha/kryonix/kryonix-dev` |

## Meta-repo

O `kryonix-dev` é o meta-repositório oficial. Ele contém todos os repos como submodules em `repos/`.

```bash
cd /home/rocha/kryonix/kryonix-dev
git submodule update --init --recursive
```

## Desenvolvimento local com --override-input

Para testar mudanças locais no core com o downstream:

```bash
cd /home/rocha/kryonix/kryonixos
nix flake check --override-input kryonix path:/home/rocha/kryonix/kryonix
```

## Produção vs Desenvolvimento

| Ambiente | Caminho | Uso |
|---|---|---|
| DEV | `/home/rocha/kryonix/` | Edição, commit, PR |
| PROD | `/etc/kryonix` | Motor instalado |
| PROD | `/etc/kryonixos` | Downstream instalado |

## Scripts úteis

```bash
# Status de todos os repos
cd /home/rocha/kryonix/kryonix-dev
bash scripts/status-all.sh

# Pull em todos
bash scripts/pull-all.sh

# Validar flakes
bash scripts/validate-all.sh
```