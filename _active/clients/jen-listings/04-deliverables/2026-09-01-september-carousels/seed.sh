#!/bin/bash
# Assemble the Claude Design canvas from the working files (run from this folder).
set -e
SKILL="/private/tmp/claude-501/bundled-skills/2.1.255/18daca2b7179389694b4913fa493d7b1/design"
ARGS=()
for f in Main C1S2 C1S3 C1S4 C1S5 C1S6 C1S7 C2S1 C2S2 C2S3 C2S4 C2S5 C2S6 C2S7 C3S1 C3S2 C3S3 C3S4 C3S5 C3S6 C3S7 DD1 DD2 DD3 DD4 DD5 DD6 DD7 DA1 DA2 DA3 DA4 DB1 DB2 DB3 DB4; do
  ARGS+=(--artboard "$f.dc.html")
done
for img in img/*.jpg; do
  ARGS+=(--image "$img")
done
node "$SKILL/seed-canvas.mjs" --template "$SKILL/payload.template.html" \
  --out jen-september-carousels.html --title "Jen September Carousels" \
  "${ARGS[@]}" --canvas canvas.json
node "$SKILL/seed-canvas.mjs" --check jen-september-carousels.html | cut -c1-120
