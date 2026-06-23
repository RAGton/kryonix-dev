# Multi-Repo Architecture

## Princípios

1. **Core é o motor.** `kryonix` contém módulos NixOS/HM reutilizáveis, lib, overlays, features opt-in e CLI base. Sem submodules.
2. **Produtos grandes em repos próprios.** Brain, Home, Aura, Assets, Installer — cada um com seu repo e ciclo de vida.
3. **Downstream é o usuário.** `kryonixos` contém hosts reais, hardware, usuários. Consome o core via flake input.
4. **Meta-repo para dev.** `kryonix-dev` agrupa tudo como submodules para desenvolvimento coordenado.

## Arquitetura

```
kryonix (core/motor)          → github:RAGton/kryonix
  ├── modules/                  Módulos reutilizáveis
  ├── lib/                      Helpers
  ├── overlays/                 Overlays de pacote
  ├── features/                 Features opt-in
  ├── packages/                 CLI, bar, monitors
  └── flake/                    Modularização

kryonixos (downstream)        → github:RAGton/Kryonixos
  ├── hosts/                    Hosts reais (inspiron, glacier)
  ├── users/                    Usuários (rocha, nina)
  └── flake.nix                 Consome inputs.kryonix

kryonix-installer              → github:RAGton/kryonix-installer
  ├── ISO build
  ├── Backend Axum (Rust)
  ├── UI React/Vite
  └── Disk planner, hardware probe

kryonix-brain-lightrag         → github:RAGEnterprise/kryonix-brain-lightrag
  ├── LightRAG engine
  ├── FastAPI server
  ├── CLI `rag`
  └── Autopilot

kryonix-home                   → github:RAGton/KRYONIX-HOME
  └── Rust CLI para organização de home

kryonix-aura                   → github:RAGton/kryonix-aura
  └── Agente e automação

kryonix-assets                 → github:RAGton/kryonix-assets
  └── Wallpapers, temas SDDM, branding

kryonix-vault                  → github:RAGton/kryonix-vault
  └── Documentação, notas, ADRs

kryonix-dev (meta-repo)        → github:RAGton/kryonix-dev
  └── Submodules de todos os repos + agents + docs + scripts
```

## Fluxo de desenvolvimento

```
1. Editar no repo específico (ex: kryonix)
2. Commit e push no repo específico
3. PR no repo específico
4. Merge → main no repo específico
5. Meta-repo: git submodule update --remote
6. Meta-repo: commit do update
```

## Regras

- Core NÃO tem submodules.
- Meta-repo PODE e DEVE ter submodules.
- `--override-input` para desenvolvimento local cruzado.
- `/etc/kryonix` e `/etc/kryonixos` são produção — não editar direto.