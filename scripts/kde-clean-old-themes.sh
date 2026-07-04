#!/usr/bin/env bash
set -e

BACKUP_DIR="$HOME/kryonix-theme-cleanup-$(date +%Y%m%d-%H%M%S)"
echo "Criando backup em: $BACKUP_DIR"
mkdir -p "$BACKUP_DIR"

# Faz backup de todos os diretórios importantes primeiro
for dir in \
  "$HOME/.local/share/plasma/look-and-feel" \
  "$HOME/.local/share/plasma/desktoptheme" \
  "$HOME/.local/share/color-schemes" \
  "$HOME/.local/share/aurorae/themes" \
  "$HOME/.local/share/icons" \
  "$HOME/.config/Kvantum"
do
  if [ -e "$dir" ]; then
    mkdir -p "$BACKUP_DIR$(dirname "$dir")"
    cp -a "$dir" "$BACKUP_DIR$(dirname "$dir")/"
    echo "Backup salvo: $dir"
  fi
done

echo ""
echo "Iniciando limpeza de temas legados conflitantes..."
mkdir -p "$BACKUP_DIR/removed-user-themes"

# Move especificamente os temas conhecidos para fora da área ativa
for path in \
  "$HOME"/.local/share/plasma/look-and-feel/*BonaFides* \
  "$HOME"/.local/share/plasma/look-and-feel/*MacVentura* \
  "$HOME"/.local/share/plasma/look-and-feel/*Illusion* \
  "$HOME"/.local/share/plasma/look-and-feel/*kryonix* \
  "$HOME"/.local/share/plasma/desktoptheme/*BonaFides* \
  "$HOME"/.local/share/plasma/desktoptheme/*MacVentura* \
  "$HOME"/.local/share/plasma/desktoptheme/*Illusion* \
  "$HOME"/.local/share/plasma/desktoptheme/*kryonix* \
  "$HOME"/.local/share/color-schemes/*BonaFides* \
  "$HOME"/.local/share/color-schemes/*MacVentura* \
  "$HOME"/.local/share/color-schemes/*Illusion* \
  "$HOME"/.local/share/color-schemes/*kryonix*
do
  if [ -e "$path" ]; then
    mv "$path" "$BACKUP_DIR/removed-user-themes/"
    echo "Removido (movido para backup): $path"
  fi
done

echo ""
echo "Limpeza concluída! Apenas pacotes do NixOS (WhiteSur, Breeze) e temas não-conflitantes permaneceram."
echo "Execute 'kryonix switch all' e resete os painéis para aplicar as mudanças visuais limpas."
