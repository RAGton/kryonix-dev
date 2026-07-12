#!/bin/bash
sed -i 's/"KrohnkiteFocusRight" = "Meta+L";/"KrohnkiteFocusRight" = "none";/' repos/kryonix/desktop/kde/keybinds.nix
sed -i 's/"Lock Session" = "Meta+Escape";/"Lock Session" = "Ctrl+Esc";/' repos/kryonix/desktop/kde/keybinds.nix
sed -i 's/"Log Out" = "Shift+Escape";/"Log Out" = "Ctrl+Alt+Del";/' repos/kryonix/desktop/kde/keybinds.nix
