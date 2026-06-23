# Kryonix Dev — Meta-Repository

Desenvolvimento da distro Kryonix. Workspace multi-repo oficial.

## Repositórios

| Repo | Caminho | Descrição |
|---|---|---|
| **kryonix** | `repos/kryonix` | Core/motor da distro (módulos, lib, overlays, CLI) |
| **kryonixos** | `repos/kryonixos` | Downstream com hosts reais (inspiron, glacier) |
| **kryonix-installer** | `repos/kryonix-installer` | ISO build, instalador, TUI, web-kiosk |
| **kryonix-brain-lightrag** | `repos/kryonix-brain-lightrag` | RAG engine, LightRAG, FastAPI, CLI `rag` |
| **kryonix-home** | `repos/kryonix-home` | Organizador de home directory (Rust CLI) |
| **kryonix-aura** | `repos/kryonix-aura` | Agente Aura e camada de automação |
| **kryonix-assets** | `repos/kryonix-assets` | Wallpapers, temas SDDM, branding |
| **kryonix-vault** | `repos/kryonix-vault` | Obsidian Vault com documentação operacional |

## Uso

```bash
# Clonar com submodules
git clone --recursive https://github.com/RAGton/kryonix-dev.git
cd kryonix-dev

# Atualizar todos os submodules
git submodule update --init --recursive

# Status de todos os repos
./scripts/status-all.sh

# Sincronizar todos (pull --ff-only)
./scripts/pull-all.sh

# Validar flake de todos os repos
./scripts/validate-all.sh
```

## Estrutura

```
kryonix-dev/
├── README.md
├── .gitmodules
├── repos/              # Todos os repos como submodules
├── agents/             # Contexto de IA e agentes
│   ├── aura/
│   ├── codex/
│   ├── claude/
│   └── prompts/
├── docs/               # Documentação do workspace
└── scripts/            # Scripts de produtividade
```

## Regras

- Core `kryonix` NÃO tem submodules.
- `kryonix-dev` PODE e DEVE ter submodules (é o meta-repo).
- Desenvolvimento local usa `--override-input` para apontar para `repos/`.
- Cada repo tem commit/push próprios — nada de commits multi-repo.
- Produção em `/etc/kryonix` e `/etc/kryonixos`.