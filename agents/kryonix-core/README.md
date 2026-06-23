# Kryonix Core — AI/Agent Context

Este diretório contém contexto de IA, agentes, prompts, skills e workflows migrados do repo `kryonix`.

## Origem

| Origem | Arquivos | Destino |
|---|---|---|
| `.ai/` | 37 | `agents/kryonix-core/ai/` |
| `.agents/` | 89 | `agents/kryonix-core/agents/` |
| `.claude/` | 15 | `agents/kryonix-core/claude/` |
| `.codex/` | 2 | `agents/kryonix-core/codex/` |
| `docs/ai/` | 33 | `agents/kryonix-core/docs-ai/` |

## Regra oficial

O repo `kryonix` é o core/motor limpo da distro e **não deve** conter contexto pesado de IA.

Todo contexto de desenvolvimento assistido, prompts, workflows, skills e automação multi-repo vive no meta-repo:

- **Repositório:** `RAGton/kryonix-dev`
- **Workspace local:** `/home/rocha/kryonix/kryonix-dev`