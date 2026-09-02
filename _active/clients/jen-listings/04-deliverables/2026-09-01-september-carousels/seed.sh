#!/bin/bash
# Assemble the Claude Design canvas from the working files (run from this folder).
set -e
SKILL="/private/tmp/claude-501/bundled-skills/2.1.255/18daca2b7179389694b4913fa493d7b1/design"
ARGS=()
for f in $(python3 -c "import json; print(' '.join(a['file'] for a in json.load(open('canvas.json'))['artboards']))"); do
  ARGS+=(--artboard "$f")
done
for img in img/*.jpg; do
  ARGS+=(--image "$img")
done
node "$SKILL/seed-canvas.mjs" --template "$SKILL/payload.template.html" \
  --out jen-september-carousels.html --title "Jen September Carousels" \
  "${ARGS[@]}" --canvas canvas.json
node "$SKILL/seed-canvas.mjs" --check jen-september-carousels.html | cut -c1-120
