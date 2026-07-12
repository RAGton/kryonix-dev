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
    ├── kryonix-vault/     ← Obsidian Vault (documentação, ADRs, logs)
    ├── ragos/             ← plataforma diskless NixOS (servidor, cliente, ragc)
    └── ragos-installer/   ← instalador oficial do ecossistema RAGOS
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
| `repos/ragos` | Plataforma RAGOS | Servidor e clientes diskless NixOS, inventário, PXE e `ragc` |
| `repos/ragos-installer` | Instalador RAGOS | ISO, backend, UI e pipeline de instalação do servidor RAGOS |

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

## Uso obrigatório do Vault

O repositório `repos/kryonix-vault` é a camada oficial de **memória persistente, contexto operacional e rastreabilidade** do ecossistema Kryonix.

Todo agente que trabalha neste workspace deve usar o Vault para melhorar a qualidade das entregas, evitar retrabalho, preservar decisões e impedir "vibe coding" sem contexto.

### Regra principal

- **Antes** de executar mudanças relevantes, o agente deve **consultar** o Vault.
- **Depois** de executar mudanças relevantes, o agente deve **registrar** no Vault o que foi feito, por quê, quais validações foram executadas e quais pendências ficaram.

### O Vault deve ser usado para

- registrar decisões técnicas;
- guardar contexto de arquitetura;
- documentar migrações entre repositórios;
- registrar auditorias de workspace;
- registrar validações e evidências;
- preservar plano, execução e resultado de tarefas importantes;
- melhorar continuidade entre sessões de Aura, Codex, Claude e outros agentes.

### O Vault não deve conter

- secrets;
- tokens;
- API keys reais;
- `.env` real;
- cache de LLM;
- `.claude` cache pesado;
- `__pycache__`;
- `.venv`;
- builds;
- artefatos temporários;
- bancos/runtime;
- dados de `/var/lib/kryonix`.

### Protocolo obrigatório antes de tarefas relevantes

Antes de alterar código, arquitetura, módulos, profiles, installer, Brain, Aura ou fluxo multi-repo, o agente deve consultar:

```bash
repos/kryonix-vault/AGENTS.md
repos/kryonix-vault/VAULT_INDEX.md
repos/kryonix-vault/02-Areas/Kryonix/
repos/kryonix-vault/09-Logs/
```

Também deve procurar registros anteriores relacionados à tarefa:

```bash
cd repos/kryonix-vault
rg -n "<tema-da-tarefa>" 01-MOCs 02-Areas 03-Projetos 09-Logs AGENTS.md VAULT_INDEX.md
```

### Protocolo obrigatório depois de tarefas relevantes

Ao concluir uma tarefa relevante, criar ou atualizar uma nota no Vault com:

```md
# <Título da tarefa>

Data: YYYY-MM-DD
Agente: Aura/Codex/Claude/etc
Repos afetados:

- repo 1
- repo 2

## Objetivo

## Contexto consultado

## Mudanças realizadas

## Commits e branches

## Validações executadas

## Evidências

## Pendências

## Próximo passo recomendado
```

Local recomendado:

```txt
repos/kryonix-vault/09-Logs/Kryonix/
```

Para decisões arquiteturais duradouras, também atualizar ou criar notas em:

```txt
repos/kryonix-vault/02-Areas/Kryonix/canonical/
```

### Fluxo correto ao modificar o Vault

O Vault é um submodule. Portanto, alterações nele exigem dois commits:

1. Commit no próprio Vault:

```bash
cd repos/kryonix-vault
git add <arquivos>
git commit -m "docs(vault): <descrição>"
git push origin main
```

2. Atualização do pointer no `kryonix-dev`:

```bash
cd ../..
git add repos/kryonix-vault
git commit -m "chore(dev): update vault submodule pointer"
git push origin main
```

### Regra de qualidade para agentes

Nenhuma entrega relevante deve terminar sem:

- status final dos repos afetados;
- lista de arquivos alterados;
- commits gerados;
- validações executadas;
- pendências explícitas;
- registro no Vault quando houver decisão, migração, arquitetura ou mudança multi-repo.

Se a tarefa não tiver registro no Vault, ela não está totalmente concluída.

---

## Política anti-vibe coding

O agente deve evitar alterações baseadas apenas em intuição.

Antes de modificar arquivos importantes, deve:

1. identificar o repo correto;
2. consultar o contexto no Vault;
3. verificar o estado Git;
4. listar arquivos que serão alterados;
5. explicar o plano;
6. executar mudanças pequenas e reversíveis;
7. validar;
8. commitar com mensagem clara;
9. atualizar o submodule pointer no `kryonix-dev`, quando aplicável;
10. registrar a decisão no Vault quando a tarefa for relevante.

### Comandos proibidos sem autorização explícita

```bash
git add .
git reset --hard
git clean -fdx
git push --force
git branch -D
rm -rf
nix flake update
nixos-rebuild switch
kryonix switch
```

### Comandos preferidos

```bash
git status -sb
git diff --stat
git diff -- <arquivo>
git add <arquivo-específico>
git commit -m "tipo(escopo): mensagem"
git push origin main
```

### Regra de ouro

O agente deve produzir entregas auditáveis, não apenas mudanças que "parecem funcionar".

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
---

## Uso do MCP de Testes

Use o MCP `kryonix-test` para rodar testes locais do Kryonix.

**Regras:**
1. Antes de testar, chame `list_test_profiles`.
2. Para testes locais, use `run_test_profile`.
3. Não rode comandos shell diretos se existir profile MCP equivalente.
4. Leia apenas o JSON resumido retornado.
5. Só chame `get_last_test_report` quando houver falha.
6. Só chame `get_last_failures` para diagnóstico compacto.
7. Não leia logs completos sem necessidade.
8. Nunca peça secrets.
9. Nunca tente rodar comando arbitrário fora da allowlist.
10. Para `nix-full`, peça confirmação humana e use somente se `KRYONIX_ALLOW_HEAVY=1` estiver configurado no ambiente.
11. Após alterações no installer, rode `installer-critical`.
12. Após mudanças no Vault, rode `vault`.
13. Após mudanças Python/Brain, rode `python`.
14. Após mudanças Rust/Home, rode `rust`.
15. Após mudanças Nix, rode `nix-fast`; `nix-full` só com aprovação.
