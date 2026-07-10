#!/bin/bash
# Render an HTML file to PDF via headless Google Chrome at its @page size.
# Usage: ./render.sh path/to/file.html path/to/out.pdf
set -e
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
IN="$1"; OUT="$2"
ABS_IN="file://$(cd "$(dirname "$IN")" && pwd)/$(basename "$IN")"
"$CHROME" --headless --disable-gpu --no-sandbox \
  --no-pdf-header-footer \
  --print-to-pdf="$OUT" \
  --virtual-time-budget=8000 \
  "$ABS_IN" 2>/dev/null
echo "Rendered: $OUT"
