#!/bin/bash

# Regenerate xopp PNGs, then render book

set -e

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Export pngs from xopp files using a forked child process
echo "== Exporting xopp PNGs =="
(cd "$repo_root/drawings" && ./xopp2png.sh)

echo
# And render book also using forked child process
echo "== Rendering book =="
(cd "$repo_root" && quarto render)

