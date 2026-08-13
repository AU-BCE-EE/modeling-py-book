#!/bin/bash

# Regenerate xopp PNGs, then render book

set -e

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "== Exporting xopp PNGs =="
(cd "$repo_root/drawings" && ./xopp2png.sh)

echo
echo "== Rendering book =="

quarto render

