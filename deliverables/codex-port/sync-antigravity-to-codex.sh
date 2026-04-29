#!/usr/bin/env bash
set -euo pipefail

SRC="/Users/farricecain/Google Antigravity"
CODEX_HOME="/Users/farricecain/.codex"

mkdir -p "$CODEX_HOME/skills" "$CODEX_HOME/vendor_imports/antigravity-system"

rsync -a --exclude 'pdf/' "$SRC/skills/" "$CODEX_HOME/skills/"
rsync -a "$SRC/skills/pdf/" "$CODEX_HOME/skills/antigravity-pdf/"
rsync -a "$SRC/deliverables/codex-port/antigravity-harness/" "$CODEX_HOME/skills/antigravity-harness/"

rsync -a \
  --exclude 'node_modules/' \
  --exclude '.git/' \
  --exclude '.env' \
  --exclude '.DS_Store' \
  "$SRC/" "$CODEX_HOME/vendor_imports/antigravity-system/"

echo "Antigravity harness synced into Codex."
