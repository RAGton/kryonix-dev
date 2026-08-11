# NEXT SPRINT — Kryonix (2026-08-01+)

Pendências para a próxima sessão, em ordem de prioridade:

- Resolver buraco negro do PPPoE no InstallPlanV2
  (UI coleta senha mas V2 perde o usuário — decisão de produto pendente:
  V2 gera NixOS, ou delega ao Flake base?)
- Executar cargo clippy via `nix-shell -p llvmPackages.libclang`
  no backend kryxd (libclang ausente no sandbox)
- Refatorar SystemFeatures.jsx (segundo maior componente da UI,
  mesmo playbook Network.jsx: SSoT → hooks → decomposição)