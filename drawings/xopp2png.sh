#!/bin/bash

# Export PNG from all .xopp files in this directory.
# Skips files where the PNG is already up-to-date.
# PNGs are written alongside the .xopp files.

generated=0
skipped=0

while read -r file; do
  png="${file%.xopp}.png"

  if [ ! -f "$png" ] || [ "$file" -nt "$png" ]; then
    echo "Generating $png from $file"
    xournalpp -i "$png" "$file" 2>/dev/null
    generated=$((generated + 1))
  else
    echo "Skipping $file (up-to-date)"
    skipped=$((skipped + 1))
  fi
done < <(find . -maxdepth 1 -type f -name "*.xopp")

echo
echo "Summary:"
echo "  PNGs generated: $generated"
echo "  Files skipped:  $skipped"
