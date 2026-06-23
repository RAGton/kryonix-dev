# Kryonix Dev — Agent Workspace

Bem-vindo ao workspace de desenvolvimento da distro Kryonix.

Este repositório é o **ambiente oficial de desenvolvimento + contexto de IA**.  
O core limpo da distro vive em `repos/kryonix`.

---

## Estrutura

```
kryonix-dev/
├── AGENTS.md              ← você está aqui
├── agents/                ← contexto de IA
│   └── kryonix-core/      ← .ai, .agents, .claude, .codex, docs/ai migrados do core
├── docs/                  ← documentação do workspace
├── scripts/               ← bootstrap, status-all, pull-all, validate-all
└── repos/                 ← submodules oficiais da distro
    ├── kryonix/           ← core/motor limpo (módulos, lib, overlays, CLI)
    ├── kryonixos/         ← hosts reais (inspiron, glacier, usuários)
    ├── kryonix-installer/ ← ISO, instalador, TUI, web-kiosk
    ├── kryonix-brain-lightrag/ ← RAG engine, LightRAG, FastAPI
    ├── kryonix-home/      ← organizador de home directory (Rust)
    ├── kryonix-aura/      ← agente Aura e automação
    ├── kryonix-assets/    ← wallpapers, temas SDDM, branding
    └── kryonix-vault/     ← Obsidian Vault (documentação, ADRs, logs)
```

---

## Papel de cada repo

| Repo | Função | O que contém |
|---|---|---|
| `repos/kryonix` | Core/motor da distro | Módulos NixOS/HM, lib, overlays, features opt-in, CLI base |
| `repos/kryonixos` | Downstream real | Hosts (inspiron, glacier), usuários (rocha, nina), hardware |
| `repos/kryonix-installer` | Instalador | ISO build, backend Axum (Rust), UI React/Vite, TUI |
| `repos/kryonix-brain-lightrag` | IA/Brain | LightRAG, FastAPI, CLI `rag`, autopilot |
| `repos/kryonix-home` | Home organizer | Rust CLI para organizar diretório home |
| `repos/kryonix-aura` | Agente Aura | Scripts de automação e agente |
| `repos/kryonix-assets` | Branding | Wallpapers, temas SDDM, avatars |
| `repos/kryonix-vault` | Memória | Notas Obsidian, MOCs, ADRs, logs, documentação |

---

## Regras para agentes

### 1. Workspace oficial

Sempre trabalhar dentro de `/home/rocha/kryonix/kryonix-dev`.

**Nunca desenvolver diretamente em `/etc/kryonix` ou `/etc/kryonixos`** — esses são produção/deploy.

### 2. Cada repo tem seu ciclo

Não commitar em múltiplos repos no mesmo commit.  
Cada alteração vai para o repo específico, depois atualiza o submodule pointer no `kryonix-dev`.

Fluxo correto:

```bash
cd repos/kryonix          # ou outro repo
# fazer alterações
git add <arquivos>
git commit -m "tipo(escopo): mensagem"
git push origin main

cd ..                     # volta pro kryonix-dev
git add repos/kryonix     # atualiza o pointer
git commit -m "chore(dev): update kryonix submodule pointer"
git push origin main
```

### 3. Core não tem submodules

O repo `repos/kryonix` **não deve conter submodules Git**.  
Dependências externas são consumidas via flake inputs.

### 4. Não usar `git add .`

Sempre adicionar arquivos explicitamente.

### 5. Sempre validar antes de commitar

Para o core:

```bash
cd repos/kryonix
nix flake check --keep-going
```

Para o installer:

```bash
cd repos/kryonix-installer
cargo fmt --check
cargo clippy -- -D warnings
```

---

## Onde encontrar contexto de IA

| Conteúdo | Caminho |
|---|---|
| Prompts, skills, workflows (migrados do core) | `agents/kryonix-core/` |
| Documentação do workspace | `docs/` |
| Scripts de produtividade | `scripts/` |
| Documentos canônicos e decisões | `repos/kryonix-vault/` |

---

## Links rápidos

- Repositórios no GitHub: https://github.com/RAGton/kryonix-dev
- Core: `repos/kryonix`
- Downstream: `repos/kryonixos`
- Installer: `repos/kryonix-installer`
- Vault (Obsidian): `repos/kryonix-vault`