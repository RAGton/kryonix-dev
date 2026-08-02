# Kryonix — README Template

> **Template canônico** para READMEs dos sub-repositórios do meta-repo `kryonix-dev`.
>
> Aplicar este template em **todo repo** que ainda não segue o padrão. Não é
> obrigatório reescrever READMEs já bons — apenas aplicar quando o repo for
> tocado pela primeira vez ou quando a auditoria detectar drift estrutural.

---

## Estrutura canônica

Um README do ecossistema Kryonix deve ter, **na ordem**:

1. **1 H1** com o nome do repo
2. **Tagline** em blockquote (uma linha, papel do repo no ecossistema)
3. **3 badges Shields.io** (Compatibilidade, Status, Última atualização)
4. **Descrição** (2-4 frases: o que é, pra que serve)
5. **Status** (estável / experimental / wip, com frase explicando)
6. **Compatibilidade** (tabela com NixOS, Kryonix meta, Rust, Node)
7. **Instalação** (comandos reais de build/install)
8. **Uso** (exemplo mínimo)
9. **Repos relacionados** (cross-links com `../<repo>/`)
10. **Contribuição** (1-2 frases)
11. **Licença**
12. **Changelog** (2-3 bullets com data)

---

## Template (copiar e preencher)

````markdown
# <Nome do Repo>

> <Tagline curta em uma linha, descrevendo o papel do repo no ecossistema>

[![Compatibilidade: NixOS <versão>](https://img.shields.io/badge/NixOS-<versão>-blueviolet)](#compatibilidade)
[![Status: <estável|experimental|wip>](https://img.shields.io/badge/status-<estável|experimental|wip>-<green|orange|red>)](#status)
[![Última atualização: YYYY-MM-DD](https://img.shields.io/badge/updated-YYYY--MM--DD-lightgrey)](#changelog)

## Descrição

<2-4 frases: o que é, pra que serve, por que existe. Foco no valor pro usuário
final, não em features internas. Mencionar o papel no ecossistema Kryonix.>

## Status

<estável|experimental|wip>: <uma frase explicando o estado atual>.

## Compatibilidade

| Componente       | Versão suportada       |
|------------------|------------------------|
| NixOS            | <versão>               |
| Kryonix (meta)   | <commit/tag>           |
| Rust (se houver) | <toolchain>            |
| Node.js (se houver) | <versão>            |

## Instalação

```bash
# <comandos reais de build/install deste repo>
```

<Se o repo não tem install/build, omitir esta seção mas mencionar onde vive
o artefato (ex: "Imagens publicadas em ...").>

## Uso

<Exemplo mínimo de uso. Se for uma lib, mostrar 1 import. Se for binário,
mostrar 1 chamada.>

## Repos relacionados

Este repo integra com:

- [`<repo-irmao>`](../<repo-irmao>/): <relação>
- [`<repo-irmao>`](../<repo-irmao>/): <relação>

Veja [`AGENTS.md`](../../AGENTS.md) do meta-repo pra entender como tudo se
encaixa no workspace.

## Contribuição

<1-2 frases: como contribuir. Se tem workflow específico (ex: Nix flakes),
mencionar. Referenciar `AGENTS.md` do meta-repo pra regras de gate humano.>

## Licença

<MIT|Apache-2.0|GPL-3.0|proprietária>

## Changelog

- **YYYY-MM-DD**: <última mudança relevante>
- **YYYY-MM-DD**: <mudança anterior>
````

---

## Regras duras

1. **Nunca** usar mais de **1 H1**. Sub-seções usam `##` (H2).
2. **Sempre** ter **pelo menos uma das seções**: Descrição, Instalação ou Uso.
3. **Sempre** linkar pelo menos **1 repo relacionado** (cross-link).
4. **Sempre** atualizar a seção **Changelog** em commits que mudem o repo.
5. **Nunca** incluir URLs externas quebradas, badges offline, ou imagens
   hospedadas em domínios não-confiáveis.

## Quando aplicar o template

| Evento | Ação |
|---|---|
| **Novo repo adicionado ao meta-repo** | Aplicar template desde o início |
| **Auditoria detecta drift** (≥3 H1, sem seção canônica, zero cross-links) | Aplicar template (re-escrita completa ou patch cirúrgico) |
| **Refactor estrutural do repo** | Aproveitar pra migrar pro template |
| **Doc-patch trivial** (typo, link quebrado) | NÃO reescrever — só corrigir |

## Como auditar uniformidade

```bash
# Contar H1s por repo (deve ser 1)
for repo in kryonix kryonixos kryxd kryx-cli kryonix-brain-lightrag             kryonix-home kryonix-aura kryonix-assets kryonix-vault; do
    n=$(grep -c '^# ' repos/$repo/README.md)
    echo "$repo: $n H1 (esperado: 1)"
done

# Verificar cross-links (cada repo deve linkar ≥1 outro)
for repo in kryonix kryonixos kryxd kryx-cli kryonix-brain-lightrag             kryonix-home kryonix-aura kryonix-assets kryonix-vault; do
    n=$(grep -c '../kryonix\|../kryonixos\|../kryxd\|../kryx-cli' repos/$repo/README.md)
    echo "$repo: $n cross-links (esperado: >=1)"
done
```

## Histórico

- **2026-08-02**: Template criado (Aura, KCR `docs(meta)`).
- Auditoria inicial detectou: 0/9 READMEs com cross-links, 3/9 com ≥3 H1,
  4/9 sem seção "Última atualização".

---

> Manter este arquivo sincronizado com a evolução do meta-repo.
> Mudanças devem ser revisadas por humano (L2+) antes de aplicar nos repos.
