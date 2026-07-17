# AURA CODING STANDARDS

> Manifesto operacional de engenharia para a Aura no ecossistema Kryonix.
>
> Status: canônico para planejamento e revisão futura.
> Escopo: arquitetura, organização de código, legibilidade, padrões de projeto e disciplina de commits.

---

## 1. Princípio central

A Aura não deve inventar arquitetura do zero quando já existem padrões maduros na indústria.

A estrutura de pastas, os limites de módulo e os contratos entre camadas devem nascer de evidência:

1. código atual do Kryonix;
2. requisitos reais do domínio;
3. padrões aceitos pela comunidade;
4. referências de repositórios profissionais;
5. documentação oficial das tecnologias usadas;
6. experimentos pequenos e reversíveis.

Arquitetura boa não é estética de pasta: é redução de acoplamento, clareza de responsabilidade e facilidade de manutenção.

---

## 2. Experiência real e convenções

Antes de propor uma estrutura nova, a Aura deve observar padrões reais usados em projetos sólidos.

Referências conceituais aceitas:

- arquitetura hexagonal / ports and adapters;
- separação entre domínio, aplicação, infraestrutura e interface;
- boundaries claros entre backend, frontend, NixOS modules, runtime e documentação;
- organização por capacidade quando o domínio pede, não por modismo;
- padrões de comunidade em Rust, React, NixOS, Axum, Tokio e Serde.

No Kryonix, isso significa:

- Rust backend não deve carregar regras visuais do React;
- React não deve conhecer segredo, socket de runtime, `/etc/shadow`, Unix socket do Incus ou detalhes de systemd;
- NixOS modules declaram estado e capabilities;
- `kryxd` executa/expõe contratos seguros;
- Vault e `docs/ia-reference/` guardam raciocínio, prompts, planos e memória arquitetural;
- código-fonte guarda implementação revisável.

---

## 3. Design Patterns como linguagem, não decoração

Design Patterns não existem para deixar o código “chique”.

Eles existem para tornar a intenção imediatamente reconhecível para:

- Gabriel no futuro;
- outros mantenedores;
- agentes revisores;
- ferramentas de teste e auditoria.

Um pattern só deve entrar quando reduzir ambiguidade ou acoplamento.

Exemplos bons:

- `Port` para abstrair Incus, PAM, storage ou provider externo;
- `Adapter` para Unix socket, CLI legado ou API HTTP;
- `Repository` apenas quando houver persistência real e contrato claro;
- `Command` para ações mutáveis auditáveis;
- `Policy` para RBAC, capabilities e guardrails;
- `DTO` separado de modelo de domínio quando exposto para frontend.

Exemplos ruins:

- criar `services/`, `managers/`, `helpers/` gigantes sem limite claro;
- empurrar regra de negócio para componente React;
- criar camada por moda sem teste e sem contrato;
- usar pattern para esconder código acoplado.

---

## 4. Proibição de código espaguete — ou “quiabo”

Código acoplado, escorregadio e difícil de revisar é proibido.

Sinais de quiabo:

- módulo que faz UI, auth, storage e rede ao mesmo tempo;
- função com efeitos colaterais invisíveis;
- frontend chamando runtime privilegiado direto;
- backend imprimindo segredo ou aceitando mutação sem role;
- commit misturando bugfix, feature, refactor, documentação e migração;
- `git add .` em workspace sujo;
- regra importante escondida em prompt, não em teste/contrato.

Regra da Aura:

```txt
uma mudança = um motivo = uma validação = um rollback possível
```

---

## 5. Separação de camadas no Kryonix

### 5.1 Frontend React / KVE

Responsabilidades:

- renderizar estado;
- chamar API do `kryxd`;
- apresentar ações com feedback claro;
- esconder opções não suportadas por capabilities;
- nunca persistir segredo sensível.

Não responsabilidades:

- autenticar contra PAM diretamente;
- acessar `/etc`, Unix sockets, Incus socket, systemd ou chaves;
- decidir capabilities por hardcode visual;
- simular produção sem etiqueta clara de mock/dev.

### 5.2 Backend Rust / `kryxd`

Responsabilidades:

- expor API tipada e versionada;
- aplicar RBAC e sessão;
- isolar acesso a Incus, PAM, systemd, storage e runtime;
- nunca vazar segredo;
- registrar erros de forma redigida;
- manter contratos compatíveis com UI.

### 5.3 NixOS / Flakes

Responsabilidades:

- declarar capabilities reais;
- compor módulos por host/perfil;
- expor estado canônico para o runtime;
- não colocar segredo no Nix Store;
- permitir rollback por geração.

### 5.4 Vault e `docs/ia-reference/`

Responsabilidades:

- guardar raciocínio arquitetural;
- inventários, prompts, specs, padrões e decisões;
- separar conhecimento de IA do código de produção;
- preservar contexto para retomada pós-formatação.

---

## 6. Commits e fluxo de trabalho

A Aura deve manter commits pequenos, revisáveis e com escopo único.

Proibido por padrão:

```bash
git add .
git reset --hard
git clean -fd
git push --force
```

Permitido quando aprovado e escopado:

```bash
git add caminho/arquivo1 caminho/arquivo2
git commit -m "type(scope): descrição clara"
git push -u origin HEAD
```

Em workspaces sujos, a Aura deve:

1. identificar mudanças preexistentes;
2. assumir que pertencem ao usuário;
3. não sobrescrever;
4. não misturar escopos;
5. stagear paths explícitos;
6. reportar o que ficou fora.

---

## 7. Padrão para novas features

Antes de implementar:

1. descobrir código atual;
2. identificar contrato existente;
3. consultar documentação oficial quando necessário;
4. desenhar menor mudança correta;
5. separar frontend/backend/Nix/docs;
6. validar com build/teste real;
7. registrar riscos e rollback.

Formato de decisão:

```txt
Contexto
Objetivo
Não objetivos
Contrato afetado
Arquitetura proposta
Alternativas consideradas
Riscos
Validação
Rollback
```

---

## 8. Segurança como requisito arquitetural

Nenhuma arquitetura é boa se expõe segredo.

A Aura deve proteger:

- senhas;
- tokens;
- cookies;
- chaves privadas;
- arquivos `.env` reais;
- Unix sockets privilegiados;
- paths sensíveis;
- logs de autenticação.

Para login local real, o caminho recomendado é PAM via backend Rust com fase dedicada, testes e política de roles. O frontend nunca deve validar senha Linux diretamente.

---

## 9. Critério de qualidade final

Um patch está aceitável quando:

- o motivo é claro;
- o diff é revisável;
- os contratos estão explícitos;
- não há segredo exposto;
- há validação real;
- há rollback possível;
- a mudança respeita a separação de camadas;
- Gabriel consegue entender o porquê sem reconstruir toda a conversa.

O objetivo não é ter a pasta mais bonita.

O objetivo é ter uma plataforma que sobreviva a crescimento, manutenção, incidentes e retomadas futuras.
