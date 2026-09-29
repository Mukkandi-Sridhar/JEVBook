#!/usr/bin/env bash
# Install the book's fonts (static instances, SIL OFL) so LaTeX, Matplotlib and Graphviz can find them.
set -e
DIR="$(cd "$(dirname "$0")/.." && pwd)/assets/fonts"
mkdir -p "$HOME/.local/share/fonts"
cp "$DIR"/*.ttf "$HOME/.local/share/fonts/"
fc-cache -f >/dev/null 2>&1 || true
echo "fonts installed"
