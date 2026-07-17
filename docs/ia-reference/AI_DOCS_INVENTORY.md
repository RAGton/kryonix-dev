# AI Docs Reference Inventory

Data: 2026-07-17
Status: SAFE_CENTRALIZATION_COPY

## Escopo

Este inventário centraliza cópias de documentos de IA/prompts/agentes encontrados em `repos/kryonix/`, `repos/kryxd/` e `repos/kryonix-aura/`.

## Vault Guard

Nenhum arquivo dentro de `repos/kryonix-vault/` foi lido, movido, copiado ou alterado por esta rotina.

## Por que cópia, não remoção de origem

A purificação destrutiva foi adiada porque:

- `repos/kryonix` está em uma branch suja com muitas alterações preexistentes fora deste escopo;
- `AGENTS.md` e `CLAUDE.md` podem ser regras operacionais ativas do repositório;
- remover/mover documentos rastreados dentro de submódulos exigiria novos commits/pushes nos submódulos, com risco de misturar escopos;
- o objetivo pré-formatação é preservar conhecimento e reduzir risco, não reescrever histórico de documentação em árvore suja.

Próxima fase recomendada: abrir uma PR dedicada de `docs: move AI planning docs to meta repo` a partir de árvore limpa, removendo as origens com `git mv`/`git rm` por lote revisável.

## Resumo

- Total de arquivos copiados: 237
- `kryonix`: 236
- `kryxd`: 1

## Arquivos centralizados

| Repo | Origem | Cópia central | Bytes | SHA256-16 | Tracked na origem |
|---|---|---|---:|---|---|
| `kryonix` | `.github/prompts/fix-launcher.prompt.md` | `docs/ia-reference/imported/kryonix/.github/prompts/fix-launcher.prompt.md` | 932 | `1b424f5c9f95e73d` | `True` |
| `kryonix` | `.github/prompts/implement-host.prompt.md` | `docs/ia-reference/imported/kryonix/.github/prompts/implement-host.prompt.md` | 771 | `32bb7a6e3a6b425f` | `True` |
| `kryonix` | `.github/prompts/write-release.prompt.md` | `docs/ia-reference/imported/kryonix/.github/prompts/write-release.prompt.md` | 652 | `e038246e890bcce8` | `True` |
| `kryonix` | `AGENTS.md` | `docs/ia-reference/imported/kryonix/AGENTS.md` | 739 | `4fdaa4347f944fbf` | `True` |
| `kryonix` | `CLAUDE.md` | `docs/ia-reference/imported/kryonix/CLAUDE.md` | 2325 | `91eae2084a1ebb0c` | `True` |
| `kryonix` | `CONTRIBUTING_AGENTS.md` | `docs/ia-reference/imported/kryonix/CONTRIBUTING_AGENTS.md` | 2415 | `b0c4a97d00ceab82` | `True` |
| `kryonix` | `desktop/kde/kryonix-blue-glass/mascot/kryonix-mascot-prompt.md` | `docs/ia-reference/imported/kryonix/desktop/kde/kryonix-blue-glass/mascot/kryonix-mascot-prompt.md` | 1020 | `d529f4643742cd22` | `True` |
| `kryonix` | `docs/agents/AGENT_SYSTEM_INVENTORY.md` | `docs/ia-reference/imported/kryonix/docs/agents/AGENT_SYSTEM_INVENTORY.md` | 4858 | `af3c929b206d4750` | `True` |
| `kryonix` | `docs/agents/CONTEXT_ARCHITECTURE.md` | `docs/ia-reference/imported/kryonix/docs/agents/CONTEXT_ARCHITECTURE.md` | 2032 | `8534b91dd1c14d78` | `True` |
| `kryonix` | `docs/agents/README.md` | `docs/ia-reference/imported/kryonix/docs/agents/README.md` | 1015 | `4370453f760910b0` | `True` |
| `kryonix` | `docs/agents/VIBECODE_GOVERNANCE.md` | `docs/ia-reference/imported/kryonix/docs/agents/VIBECODE_GOVERNANCE.md` | 1637 | `35dfdcb632930726` | `True` |
| `kryonix` | `docs/agents/agente-update.md` | `docs/ia-reference/imported/kryonix/docs/agents/agente-update.md` | 20510 | `5e35346606868a25` | `True` |
| `kryonix` | `docs/archive/fix/PLANO_REVISADO_FIX_SDDM.md` | `docs/ia-reference/imported/kryonix/docs/archive/fix/PLANO_REVISADO_FIX_SDDM.md` | 10113 | `ad917db6fbd9a78d` | `True` |
| `kryonix` | `docs/archive/fix/PROMPT_FIX_BLACKSCREEN_POSLOGIN.md` | `docs/ia-reference/imported/kryonix/docs/archive/fix/PROMPT_FIX_BLACKSCREEN_POSLOGIN.md` | 6474 | `65b36fad2999923d` | `True` |
| `kryonix` | `docs/archive/fix/PROMPT_FIX_HYPRLAND_CONF_BINDS.md` | `docs/ia-reference/imported/kryonix/docs/archive/fix/PROMPT_FIX_HYPRLAND_CONF_BINDS.md` | 8307 | `63002cfdbe4f13a5` | `True` |
| `kryonix` | `docs/archive/fix/PROMPT_FIX_HYPRLAND_SDDM.md` | `docs/ia-reference/imported/kryonix/docs/archive/fix/PROMPT_FIX_HYPRLAND_SDDM.md` | 6966 | `e8c0dcbcec9ff12e` | `True` |
| `kryonix` | `docs/archive/fix/PROMPT_FIX_SDDM_QTMULTIMEDIA_CAELESTIA.md` | `docs/ia-reference/imported/kryonix/docs/archive/fix/PROMPT_FIX_SDDM_QTMULTIMEDIA_CAELESTIA.md` | 6771 | `7bee29c7f079125b` | `True` |
| `kryonix` | `docs/archive/fix/PROMPT_PLYMOUTH.md` | `docs/ia-reference/imported/kryonix/docs/archive/fix/PROMPT_PLYMOUTH.md` | 5254 | `39e9b6452aeeddec` | `True` |
| `kryonix` | `docs/archive/fix/PROMPT_SDDM_HUD.md` | `docs/ia-reference/imported/kryonix/docs/archive/fix/PROMPT_SDDM_HUD.md` | 7203 | `b8371aae6bc10d55` | `True` |
| `kryonix` | `docs/archive/fix/PROMPT_TEMA_SCIFI_HUD.md` | `docs/ia-reference/imported/kryonix/docs/archive/fix/PROMPT_TEMA_SCIFI_HUD.md` | 19296 | `8315f588490fc39b` | `True` |
| `kryonix` | `docs/archive/fix/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/fix/SKILL.md` | 7670 | `3b315493621371c1` | `True` |
| `kryonix` | `docs/archive/fix/black-screen-recovery.md` | `docs/ia-reference/imported/kryonix/docs/archive/fix/black-screen-recovery.md` | 3806 | `8dae80b7966ea04f` | `True` |
| `kryonix` | `docs/archive/fix/display-manager-hyprland.md` | `docs/ia-reference/imported/kryonix/docs/archive/fix/display-manager-hyprland.md` | 4582 | `6d7304dc4cbe584d` | `True` |
| `kryonix` | `docs/archive/fix/mkforce-conflicts.md` | `docs/ia-reference/imported/kryonix/docs/archive/fix/mkforce-conflicts.md` | 3099 | `0af7080314ea2d58` | `True` |
| `kryonix` | `docs/archive/kryonix-plasma-tiling-claude-spec/00_PROMPT_CLAUDE.md` | `docs/ia-reference/imported/kryonix/docs/archive/kryonix-plasma-tiling-claude-spec/00_PROMPT_CLAUDE.md` | 6695 | `09d379d64e1e6eb4` | `True` |
| `kryonix` | `docs/archive/legacy_agents/context/ACTIVE_WORK.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_agents/context/ACTIVE_WORK.md` | 1088 | `8c85935c509b8847` | `True` |
| `kryonix` | `docs/archive/legacy_agents/context/CONSTRAINTS.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_agents/context/CONSTRAINTS.md` | 375 | `23b259075534a0c6` | `True` |
| `kryonix` | `docs/archive/legacy_agents/context/CURRENT_STATE.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_agents/context/CURRENT_STATE.md` | 2521 | `1a0a0be1cc5c4a5b` | `True` |
| `kryonix` | `docs/archive/legacy_agents/context/DECISIONS.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_agents/context/DECISIONS.md` | 2053 | `2122265ee93639f0` | `True` |
| `kryonix` | `docs/archive/legacy_agents/context/README.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_agents/context/README.md` | 692 | `3fad3e7de6388002` | `True` |
| `kryonix` | `docs/archive/legacy_agents/context/REPO_MAP.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_agents/context/REPO_MAP.md` | 891 | `df7662336f7cfe62` | `True` |
| `kryonix` | `docs/archive/legacy_ai/CHECKPOINTS.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/CHECKPOINTS.md` | 355 | `0b56473cf4df8080` | `True` |
| `kryonix` | `docs/archive/legacy_ai/INDEX.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/INDEX.md` | 1327 | `a3c4da77882b32cb` | `True` |
| `kryonix` | `docs/archive/legacy_ai/KRYONIX_CONTEXT_MEMORY_FULL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/KRYONIX_CONTEXT_MEMORY_FULL.md` | 23176 | `73398106afd3ac71` | `True` |
| `kryonix` | `docs/archive/legacy_ai/LOCAL_LLM_STRATEGY.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/LOCAL_LLM_STRATEGY.md` | 1763 | `0103246649c162d2` | `True` |
| `kryonix` | `docs/archive/legacy_ai/RAG_GOVERNANCE.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/RAG_GOVERNANCE.md` | 2272 | `cd5f5924297baf2e` | `True` |
| `kryonix` | `docs/archive/legacy_ai/README.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/README.md` | 1348 | `f54de6fb5b1b7df4` | `True` |
| `kryonix` | `docs/archive/legacy_ai/STATE.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/STATE.md` | 1134 | `843053c972082441` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/00-Inbox/IMPLEMENTAR_EM_OUTROS_PROJETOS.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/00-Inbox/IMPLEMENTAR_EM_OUTROS_PROJETOS.md` | 4605 | `3ea5d2254cc4660d` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/00-Inbox/Inbox.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/00-Inbox/Inbox.md` | 412 | `1477c4e06b858e1c` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-Canonical/Agents.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-Canonical/Agents.md` | 818 | `3d446a89b2213710` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-Canonical/Architecture.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-Canonical/Architecture.md` | 1997 | `bc5604484d1403ba` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-Canonical/Install.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-Canonical/Install.md` | 1365 | `56551086350159d8` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-Canonical/Main.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-Canonical/Main.md` | 1151 | `f979653e6e39440a` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-Canonical/Operations.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-Canonical/Operations.md` | 1536 | `ab48e3490a0b7edf` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-Canonical/Roadmap.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-Canonical/Roadmap.md` | 6250 | `38d4c5ad3ac770c0` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-Canonical/Security.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-Canonical/Security.md` | 1757 | `39c9201325540c03` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-Canonical/Testing.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-Canonical/Testing.md` | 2767 | `3bf796f3122f6874` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-Canonical/Troubleshooting.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-Canonical/Troubleshooting.md` | 2526 | `f34ec3343d600d33` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-Canonical/Usage.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-Canonical/Usage.md` | 2181 | `6fad47aefd55a18e` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - Backend e APIs.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - Backend e APIs.md` | 662 | `425145a6162c4465` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - Cerebro Supremo de IA.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - Cerebro Supremo de IA.md` | 2172 | `58ca96db279a29d6` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - Dados e Algoritmos.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - Dados e Algoritmos.md` | 441 | `1c512371ffeebad6` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - DevOps e SRE.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - DevOps e SRE.md` | 440 | `97b2fbd7bf67dad2` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - Engenharia de Software.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - Engenharia de Software.md` | 900 | `1fb5088c53d0f262` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - IA e Agentes.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - IA e Agentes.md` | 802 | `01fe099cf4fad050` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - Linux e Sistemas.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - Linux e Sistemas.md` | 581 | `54da35bd902d7d50` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - NixOS e Infra Declarativa.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - NixOS e Infra Declarativa.md` | 708 | `23fb21c61a86a8b5` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - Produto e SaaS.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - Produto e SaaS.md` | 465 | `75e6337917ba8fc8` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - Segurança.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/01-MOCs/Mapa - Segurança.md` | 558 | `c9abd15b14f74cbe` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Backend e APIs/API Vendavel.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Backend e APIs/API Vendavel.md` | 394 | `b1b0bac31c4459bb` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Backend e APIs/Arquitetura Backend Profissional.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Backend e APIs/Arquitetura Backend Profissional.md` | 425 | `fc12249498411f9d` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Backend e APIs/Autenticacao e Autorizacao.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Backend e APIs/Autenticacao e Autorizacao.md` | 483 | `9987ea7bf36181f7` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Backend e APIs/Idempotencia e Jobs.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Backend e APIs/Idempotencia e Jobs.md` | 388 | `f97c9948768fd38d` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Backend e APIs/OpenAPI e Contratos.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Backend e APIs/OpenAPI e Contratos.md` | 260 | `b4085e7c2d4e50cd` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Dados e Algoritmos/Arvores.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Dados e Algoritmos/Arvores.md` | 228 | `79e2818cbea49b99` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Dados e Algoritmos/Big-O.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Dados e Algoritmos/Big-O.md` | 305 | `f8eedcf2639e1120` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Dados e Algoritmos/Filas e Heaps.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Dados e Algoritmos/Filas e Heaps.md` | 213 | `3247d9eb050be137` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Dados e Algoritmos/Grafos.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Dados e Algoritmos/Grafos.md` | 223 | `9ea93194c224230e` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Dados e Algoritmos/Hash Tables.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Dados e Algoritmos/Hash Tables.md` | 227 | `f75b9b675c5c00c0` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/DevOps e SRE/CI CD.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/DevOps e SRE/CI CD.md` | 246 | `b8d60b7f87f15020` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/DevOps e SRE/Deploy Rollback Aware.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/DevOps e SRE/Deploy Rollback Aware.md` | 275 | `7328aabb230486fc` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/DevOps e SRE/Observabilidade.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/DevOps e SRE/Observabilidade.md` | 278 | `d70fcab96ff40e7b` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/DevOps e SRE/Runbooks.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/DevOps e SRE/Runbooks.md` | 271 | `fa555f1bf3c22234` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Engenharia de Software/Arquitetura Limpa.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Engenharia de Software/Arquitetura Limpa.md` | 366 | `ed10f2dc25a5b120` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Engenharia de Software/Clean Code.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Engenharia de Software/Clean Code.md` | 513 | `173b3d2ea54ff1d3` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Engenharia de Software/Design Patterns Uteis.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Engenharia de Software/Design Patterns Uteis.md` | 598 | `654cdfb238263842` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Engenharia de Software/Refatoracao Segura.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Engenharia de Software/Refatoracao Segura.md` | 392 | `05ce89a103888475` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Engenharia de Software/Testes Automatizados.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Engenharia de Software/Testes Automatizados.md` | 312 | `e6df1c2c07102583` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/IA e Agentes/Codex Workflow.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/IA e Agentes/Codex Workflow.md` | 487 | `ebda1e4c0dacf852` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/IA e Agentes/Estrategia de Custo de Tokens.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/IA e Agentes/Estrategia de Custo de Tokens.md` | 695 | `b23f9faa9e4fd9ed` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/IA e Agentes/Graph + Vector Hybrid Search.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/IA e Agentes/Graph + Vector Hybrid Search.md` | 351 | `6b12bad3701d2cdb` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/IA e Agentes/LLM como Amplificador.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/IA e Agentes/LLM como Amplificador.md` | 668 | `1beb8668b3a77aad` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/IA e Agentes/MCP Architecture.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/IA e Agentes/MCP Architecture.md` | 2541 | `9e3315093034df04` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/IA e Agentes/Protocolo de Consulta do Vault por IA.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/IA e Agentes/Protocolo de Consulta do Vault por IA.md` | 1791 | `df4323ab9edb52bd` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/IA e Agentes/RAG Pipeline Interno.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/IA e Agentes/RAG Pipeline Interno.md` | 3216 | `f467f7b1fc77414c` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/IA e Agentes/Skills Reutilizaveis.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/IA e Agentes/Skills Reutilizaveis.md` | 456 | `ec35c72fa0c12f26` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Linux e Sistemas/Debugging Linux.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Linux e Sistemas/Debugging Linux.md` | 315 | `26f3397215fa029c` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Linux e Sistemas/Filesystem e Permissoes.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Linux e Sistemas/Filesystem e Permissoes.md` | 270 | `a2a2eec039970c70` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Linux e Sistemas/Processos e Memoria.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Linux e Sistemas/Processos e Memoria.md` | 316 | `c3503183959322ef` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Linux e Sistemas/Rede no Linux.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Linux e Sistemas/Rede no Linux.md` | 241 | `90e29b7623713430` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Linux e Sistemas/systemd.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Linux e Sistemas/systemd.md` | 439 | `bf06af722d00e070` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/NixOS/Deploy e Rollback.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/NixOS/Deploy e Rollback.md` | 285 | `3e80f1f257020025` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/NixOS/Flakes.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/NixOS/Flakes.md` | 339 | `6588c4f2b826417e` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/NixOS/Modulos NixOS.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/NixOS/Modulos NixOS.md` | 2949 | `83d984227a364cb8` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/NixOS/Nix Language.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/NixOS/Nix Language.md` | 250 | `be501d4dfbace22f` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/NixOS/Secrets.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/NixOS/Secrets.md` | 2525 | `957ca88c74c712ba` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/NixOS/devShells.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/NixOS/devShells.md` | 262 | `e5b241fcc27e5973` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Produto e SaaS/API como Produto.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Produto e SaaS/API como Produto.md` | 268 | `e71f4bb3b5bceab5` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Produto e SaaS/MVP Vendavel.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Produto e SaaS/MVP Vendavel.md` | 324 | `da45306667d338b7` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Produto e SaaS/Pricing e Custos.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Produto e SaaS/Pricing e Custos.md` | 242 | `f137097ddf0c0fe0` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Seguranca/Hardening de Servicos.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Seguranca/Hardening de Servicos.md` | 308 | `56b8afdcec172755` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Seguranca/OWASP API Top 10.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Seguranca/OWASP API Top 10.md` | 446 | `f12be24c1e06d26f` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Seguranca/Secrets e Credenciais.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Seguranca/Secrets e Credenciais.md` | 331 | `c5f620197d468e63` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Areas/Seguranca/Seguranca para Agentes de IA.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Areas/Seguranca/Seguranca para Agentes de IA.md` | 333 | `314fec606ab18800` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Systems/Brain.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Systems/Brain.md` | 1234 | `8233073737081b64` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Systems/Glacier.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Systems/Glacier.md` | 2075 | `5f5ce222081cc179` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Systems/Inspiron.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Systems/Inspiron.md` | 1640 | `6dfaeb904d7ab363` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Systems/LightRAG.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Systems/LightRAG.md` | 1238 | `079207a2370e6466` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Systems/MCP.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Systems/MCP.md` | 1751 | `272fd43e4e7f5bf7` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Systems/Ollama.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Systems/Ollama.md` | 957 | `905a2a745170516a` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/02-Systems/Vault.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/02-Systems/Vault.md` | 1661 | `bb59f4872d087b79` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/03-Projetos/Kryonix Installer.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/03-Projetos/Kryonix Installer.md` | 3093 | `dd91b701d81d91cf` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/03-Projetos/Kryonix System.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/03-Projetos/Kryonix System.md` | 3142 | `b44312bb25009841` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/03-Projetos/Kryonix VE.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/03-Projetos/Kryonix VE.md` | 1286 | `b5d2e6e9206438c2` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/03-Projetos/RAGOS Installer.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/03-Projetos/RAGOS Installer.md` | 3066 | `3f49fcd78a945d3f` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/03-Projetos/RAGOS.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/03-Projetos/RAGOS.md` | 3118 | `07a3489ffb6cb8b3` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/03-Projetos/Ragos VE.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/03-Projetos/Ragos VE.md` | 1283 | `d45c97a0aed11eba` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/03-Projetos/_Template - Projeto.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/03-Projetos/_Template - Projeto.md` | 376 | `ca66d81b8978a1f0` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/03-Runbooks/Docs Audit.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/03-Runbooks/Docs Audit.md` | 698 | `a39e5f10d3e05851` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/03-Runbooks/Doctor Full.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/03-Runbooks/Doctor Full.md` | 704 | `9988dd0db8d422bf` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/04-Recursos/Templates/Template - ADR.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/04-Recursos/Templates/Template - ADR.md` | 276 | `ca42d8c95cab95b0` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/04-Recursos/Templates/Template - Issue Codex.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/04-Recursos/Templates/Template - Issue Codex.md` | 524 | `645ddf2f75d9c42b` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/04-Recursos/Templates/Template - Nota Tecnica.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/04-Recursos/Templates/Template - Nota Tecnica.md` | 230 | `8411b7f4c85e6043` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/04-Recursos/Templates/Template - Projeto.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/04-Recursos/Templates/Template - Projeto.md` | 290 | `3e3c71fcdc9c33ef` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Evidence/README.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Evidence/README.md` | 392 | `4daab863f9a68f5f` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/analise-banco-dados/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/analise-banco-dados/SKILL.md` | 1827 | `af56cfda00167337` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/analise-custo-ia/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/analise-custo-ia/SKILL.md` | 1812 | `fca87cdd3887cb4c` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/analise-logs/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/analise-logs/SKILL.md` | 1807 | `31075e309d37da94` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/analise-performance/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/analise-performance/SKILL.md` | 1810 | `21b6a3d8f764f0b7` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/arquitetura-backend/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/arquitetura-backend/SKILL.md` | 1819 | `b615e8db631172d2` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/auditoria-secrets/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/auditoria-secrets/SKILL.md` | 1814 | `65fa5f0339c603f5` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/debug-producao/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/debug-producao/SKILL.md` | 1808 | `998b86fc1406c256` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/decomposicao-codex/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/decomposicao-codex/SKILL.md` | 1814 | `de5d8121e4662d9b` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/design-estrutura-dados/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/design-estrutura-dados/SKILL.md` | 1834 | `7cba9b28542f659c` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/documentacao-tecnica/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/documentacao-tecnica/SKILL.md` | 1809 | `4ed6757ebbae9024` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/estudo-guiado/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/estudo-guiado/SKILL.md` | 1793 | `584b4f7c7f824aeb` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/geracao-api/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/geracao-api/SKILL.md` | 1803 | `9114bbb2a8cc3919` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/geracao-testes/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/geracao-testes/SKILL.md` | 1810 | `62bd875a78ddc271` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/hardening-nixos/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/hardening-nixos/SKILL.md` | 1821 | `0f3f7b30ed374795` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/planejamento-mvp/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/planejamento-mvp/SKILL.md` | 1813 | `737dd36175b41648` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/refatoracao-segura/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/refatoracao-segura/SKILL.md` | 1804 | `c56e34fba7a548f7` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/revisao-ci-cd/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/revisao-ci-cd/SKILL.md` | 1796 | `c8f0ab4b15c0f7e9` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/revisao-clean-code/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/revisao-clean-code/SKILL.md` | 1810 | `f78257ec34d7ba07` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/revisao-pr/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/revisao-pr/SKILL.md` | 1791 | `c6527f6422134e9a` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/05-Skills/revisao-seguranca-api/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/05-Skills/revisao-seguranca-api/SKILL.md` | 1828 | `0383d52258b97f11` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Analise de Logs.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Analise de Logs.md` | 399 | `50eca4ac31256f51` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Auditoria de Secrets.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Auditoria de Secrets.md` | 407 | `26fa84f3ca63ba66` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Configurar Repo para Codex.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Configurar Repo para Codex.md` | 478 | `7439f39aee2e3f34` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Criar Backend API Vendavel.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Criar Backend API Vendavel.md` | 429 | `d2a8bd714d291263` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Criar Issue para Codex.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Criar Issue para Codex.md` | 398 | `a635003ad37b5d43` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Criar Projeto Novo.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Criar Projeto Novo.md` | 734 | `73d858660de6337d` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Debug de Producao.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Debug de Producao.md` | 406 | `56081f7c03041c76` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Reduzir Custo de IA.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Reduzir Custo de IA.md` | 440 | `c83170ff5b2495a1` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Refatorar Sem Quebrar.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Refatorar Sem Quebrar.md` | 371 | `7921ed774c61d331` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Revisar Codigo Gerado por IA.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Revisar Codigo Gerado por IA.md` | 491 | `dcfcf9b091415075` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Transformar Ideia em MVP.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Transformar Ideia em MVP.md` | 451 | `8a28a6935e45c571` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Validar Seguranca Antes do Deploy.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/06-Playbooks/Playbook - Validar Seguranca Antes do Deploy.md` | 401 | `f3f22131a2b077a8` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/07-Prompts/PROMPT_AGENT_BACKEND_API.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/07-Prompts/PROMPT_AGENT_BACKEND_API.md` | 865 | `60cab3fd0d2a0ddd` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/07-Prompts/PROMPT_AGENT_INFRA_LINUX.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/07-Prompts/PROMPT_AGENT_INFRA_LINUX.md` | 1171 | `1712ce0ce05d33e1` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/07-Prompts/PROMPT_AGENT_SITE_MODERNO.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/07-Prompts/PROMPT_AGENT_SITE_MODERNO.md` | 892 | `6335c875bacd2aaf` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/07-Prompts/PROMPT_IA_CONSUMIR_OBSIDIAN.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/07-Prompts/PROMPT_IA_CONSUMIR_OBSIDIAN.md` | 1588 | `fe311027873e5a43` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/07-Prompts/PROMPT_SUPREMO_DEEP_RESEARCH.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/07-Prompts/PROMPT_SUPREMO_DEEP_RESEARCH.md` | 2316 | `fc425ffc9219e9bc` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Arquitetura de Sistema.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Arquitetura de Sistema.md` | 608 | `a15d420d6e974a02` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Auditoria de Custo de IA.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Auditoria de Custo de IA.md` | 479 | `643cb63b31d494fe` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Criacao de Flake.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Criacao de Flake.md` | 330 | `7305d75cced41d7a` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Debug de Producao.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Debug de Producao.md` | 483 | `f061b3596791e21e` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Issue para Codex.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Issue para Codex.md` | 492 | `7b520e55a95633bd` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Pesquisa Tecnica Profunda.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Pesquisa Tecnica Profunda.md` | 661 | `734164d64a2462c3` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Revisao NixOS.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Revisao NixOS.md` | 453 | `5f76fc7114e2f7ad` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Revisao de Codigo.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Revisao de Codigo.md` | 451 | `404e376d66281055` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Revisao de Seguranca.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/07-Prompts/Prompt - Revisao de Seguranca.md` | 496 | `bbdfbab0b840ad47` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/08-Referencias/Checklist de Avaliacao de Codigo Externo.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/08-Referencias/Checklist de Avaliacao de Codigo Externo.md` | 2498 | `3c18bbf2d06e269f` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/08-Referencias/Fontes Oficiais.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/08-Referencias/Fontes Oficiais.md` | 567 | `31a3994093ffae6a` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/08-Referencias/Politica de Curadoria de Fontes e Codigo.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/08-Referencias/Politica de Curadoria de Fontes e Codigo.md` | 3321 | `3b30562f216aa5de` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/08-Referencias/Radar de Documentacao Engenharia.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/08-Referencias/Radar de Documentacao Engenharia.md` | 3363 | `4999aca39b1661d8` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/09-Logs/Backlog de Estudos.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/09-Logs/Backlog de Estudos.md` | 407 | `bed4c5996831ac0b` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/09-Logs/Decisoes Recentes.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/09-Logs/Decisoes Recentes.md` | 262 | `ea5c15c973d8fc94` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/09-Logs/Revisao Semanal.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/09-Logs/Revisao Semanal.md` | 337 | `1f3ab72d06c92c84` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/90-Archive/AGENTS_LEGACY.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/90-Archive/AGENTS_LEGACY.md` | 7602 | `21333429124d2fc4` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/90-Archive/VAULT_INDEX_LEGACY.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/90-Archive/VAULT_INDEX_LEGACY.md` | 2347 | `ed93f7734f9ef270` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/AGENTS.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/AGENTS.md` | 7612 | `656a62cdbf36092d` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/IMPLEMENTAR_EM_OUTROS_PROJETOS.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/IMPLEMENTAR_EM_OUTROS_PROJETOS.md` | 4615 | `b2e9cb3a8ec8a86a` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/PROMPT_MASTER.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/PROMPT_MASTER.md` | 6323 | `6fc171f7aa6be287` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/README.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/README.md` | 1458 | `4675fe884786271d` | `True` |
| `kryonix` | `docs/archive/legacy_ai/kryonix-vault/VAULT_INDEX.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/kryonix-vault/VAULT_INDEX.md` | 2312 | `e1f0fe6577a810ae` | `True` |
| `kryonix` | `docs/archive/legacy_ai/prompts/2026-neo4j-rag-cag-hardening.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/prompts/2026-neo4j-rag-cag-hardening.md` | 2108 | `7c423220969c8b80` | `True` |
| `kryonix` | `docs/archive/legacy_ai/prompts/README.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/prompts/README.md` | 459 | `c223914b8177934a` | `True` |
| `kryonix` | `docs/archive/legacy_ai/prompts/codex-deep-refactor.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/prompts/codex-deep-refactor.md` | 494 | `e97d93a7dc3283f6` | `True` |
| `kryonix` | `docs/archive/legacy_ai/prompts/codex-glacier.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/prompts/codex-glacier.md` | 542 | `d6eca5d06947d7c3` | `True` |
| `kryonix` | `docs/archive/legacy_ai/prompts/copilot-core.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/prompts/copilot-core.md` | 492 | `2fe47136627e0c13` | `True` |
| `kryonix` | `docs/archive/legacy_ai/prompts/copilot-kryonix-cli.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/prompts/copilot-kryonix-cli.md` | 559 | `a3a18052e337bcc7` | `True` |
| `kryonix` | `docs/archive/legacy_ai/reports/brain-rust-current-state.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/reports/brain-rust-current-state.md` | 2844 | `4c18dd9ccba98e03` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/README.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/README.md` | 403 | `d3f063d418e32a11` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/brain/cag-routing.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/brain/cag-routing.md` | 599 | `92d5dfcdd7ced95e` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/brain/nixos-local-sources.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/brain/nixos-local-sources.md` | 752 | `dbcbd2d48e145ee4` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/branding/ASSETS.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/branding/ASSETS.md` | 277 | `c9359021848530e9` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/branding/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/branding/SKILL.md` | 759 | `aef297b377086741` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/commands/rebuild-nixos.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/commands/rebuild-nixos.md` | 442 | `12cc521a50445a8d` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/docs/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/docs/SKILL.md` | 776 | `2613c35d164881b5` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/docs/STYLE.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/docs/STYLE.md` | 280 | `6c306840cc755557` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/hosts/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/hosts/SKILL.md` | 848 | `77f90cf34cbfb07e` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/hosts/glacier.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/hosts/glacier.md` | 524 | `e6ffa347b4e350bb` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/hosts/inspiron.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/hosts/inspiron.md` | 448 | `5a9a4dbd15e5c372` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/kryonix-cli/CHECKLIST.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/kryonix-cli/CHECKLIST.md` | 519 | `9dceb125abb981a3` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/kryonix-cli/EXAMPLES.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/kryonix-cli/EXAMPLES.md` | 402 | `62bb441b0d9eb079` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/kryonix-cli/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/kryonix-cli/SKILL.md` | 1334 | `3d541275c5fc8cfd` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/operations/CHECKLIST.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/operations/CHECKLIST.md` | 420 | `f75ffa9bfc7722b5` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/operations/EXAMPLES.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/operations/EXAMPLES.md` | 408 | `da2bc6e82884bf29` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/operations/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/operations/SKILL.md` | 998 | `df807669a2ab2cdc` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/virtualization/SKILL.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/virtualization/SKILL.md` | 938 | `083d4f01d2ba1f4c` | `True` |
| `kryonix` | `docs/archive/legacy_ai/skills/virtualization/STORAGE.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/skills/virtualization/STORAGE.md` | 371 | `c9d07e83eb00191d` | `True` |
| `kryonix` | `docs/archive/legacy_ai/templates/checklist-template.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/templates/checklist-template.md` | 227 | `ed409d7fc0b75d72` | `True` |
| `kryonix` | `docs/archive/legacy_ai/templates/prompt-template.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/templates/prompt-template.md` | 318 | `3a671e3b07faab83` | `True` |
| `kryonix` | `docs/archive/legacy_ai/templates/skill-template.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_ai/templates/skill-template.md` | 202 | `da569eb6274a2caa` | `True` |
| `kryonix` | `docs/archive/legacy_docs/AGENTS_INCREMENT_GRAPH_RAG_CAG.md` | `docs/ia-reference/imported/kryonix/docs/archive/legacy_docs/AGENTS_INCREMENT_GRAPH_RAG_CAG.md` | 9491 | `b1f574cedba681d6` | `True` |
| `kryonix` | `docs/archive/promptkryonix.md` | `docs/ia-reference/imported/kryonix/docs/archive/promptkryonix.md` | 4093 | `fe4a411ff5d9e95b` | `True` |
| `kryonix` | `docs/aura/KORA_RETIREMENT_STUDY.md` | `docs/ia-reference/imported/kryonix/docs/aura/KORA_RETIREMENT_STUDY.md` | 4667 | `7bde2eed2c4d4757` | `True` |
| `kryonix` | `docs/brain/AUTOPILOT.md` | `docs/ia-reference/imported/kryonix/docs/brain/AUTOPILOT.md` | 3795 | `d70d5a506c01380a` | `True` |
| `kryonix` | `docs/brain/CAG_ARCHITECTURE.md` | `docs/ia-reference/imported/kryonix/docs/brain/CAG_ARCHITECTURE.md` | 907 | `94fdbb3bd9f7a0c1` | `True` |
| `kryonix` | `docs/brain/GRAPH_RAG_ARCHITECTURE.md` | `docs/ia-reference/imported/kryonix/docs/brain/GRAPH_RAG_ARCHITECTURE.md` | 1834 | `27f58ae7f22f972c` | `True` |
| `kryonix` | `docs/brain/INGESTION_PIPELINE.md` | `docs/ia-reference/imported/kryonix/docs/brain/INGESTION_PIPELINE.md` | 998 | `1f7ddf48a6af226f` | `True` |
| `kryonix` | `docs/brain/MEMORY.md` | `docs/ia-reference/imported/kryonix/docs/brain/MEMORY.md` | 995 | `b879f9ab51d53a30` | `True` |
| `kryonix` | `docs/brain/NEO4J.md` | `docs/ia-reference/imported/kryonix/docs/brain/NEO4J.md` | 1249 | `5070ee12a2bd88e9` | `True` |
| `kryonix` | `docs/brain/NEO4J_SCHEMA.md` | `docs/ia-reference/imported/kryonix/docs/brain/NEO4J_SCHEMA.md` | 8762 | `d26a02a2f471e848` | `True` |
| `kryonix` | `docs/brain/OBSIDIAN_NEO4J_MODEL.md` | `docs/ia-reference/imported/kryonix/docs/brain/OBSIDIAN_NEO4J_MODEL.md` | 1611 | `be9b9dab3d540925` | `True` |
| `kryonix` | `docs/brain/RAG_ARCHITECTURE.md` | `docs/ia-reference/imported/kryonix/docs/brain/RAG_ARCHITECTURE.md` | 1080 | `e6da2a317cfd54d0` | `True` |
| `kryonix` | `docs/brain/RAG_CAG_GRAPHRAG.md` | `docs/ia-reference/imported/kryonix/docs/brain/RAG_CAG_GRAPHRAG.md` | 1435 | `82b36719290d2ea8` | `True` |
| `kryonix` | `docs/brain/README.md` | `docs/ia-reference/imported/kryonix/docs/brain/README.md` | 1205 | `c7db126e4f443e69` | `True` |
| `kryonix` | `docs/brain/REASONING_MEMORY.md` | `docs/ia-reference/imported/kryonix/docs/brain/REASONING_MEMORY.md` | 751 | `5359d83a68bc12ac` | `True` |
| `kryonix` | `docs/brain/REMOTE_CLIENT_INSPIRON.md` | `docs/ia-reference/imported/kryonix/docs/brain/REMOTE_CLIENT_INSPIRON.md` | 3264 | `d519cf6f458c0116` | `True` |
| `kryonix` | `docs/brain/STATE_LAYOUT.md` | `docs/ia-reference/imported/kryonix/docs/brain/STATE_LAYOUT.md` | 1554 | `b71441243b6c58d6` | `True` |
| `kryonix` | `docs/brain/kryonix-rag-pipeline.md` | `docs/ia-reference/imported/kryonix/docs/brain/kryonix-rag-pipeline.md` | 1665 | `11cf706adf84324a` | `True` |
| `kryonix` | `docs/brain/lightrag.md` | `docs/ia-reference/imported/kryonix/docs/brain/lightrag.md` | 1172 | `2d7b5457cf99cef9` | `True` |
| `kryonix` | `docs/brain/mcp.md` | `docs/ia-reference/imported/kryonix/docs/brain/mcp.md` | 2415 | `1920fd23295ebb1a` | `True` |
| `kryonix` | `docs/brain/vault.md` | `docs/ia-reference/imported/kryonix/docs/brain/vault.md` | 1911 | `9a0a57c2210d6725` | `True` |
| `kryxd` | `.agents/skills/kryonix-notebooklm/SKILL.md` | `docs/ia-reference/imported/kryxd/.agents/skills/kryonix-notebooklm/SKILL.md` | 6500 | `e8411057ceee147f` | `True` |

## Observação

Arquivos de dependências (`node_modules`), builds (`dist`, `target`) e o Vault real foram ignorados.
