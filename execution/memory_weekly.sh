#!/bin/sh
# Weekly memory pipeline — run by launchd (com.antigravity.distill-weekly).
#
# 2026-07-02 audit fix: distill-weekly used to run memory_distill.py alone,
# but nothing automated the L1→L2 ingest feeding it, so it distilled an empty
# window ("Loaded 0 recent episodic memories"). Order matters: ingest → embed
# → distill. Steps run independently — one failing must not starve the rest.
# memory_review.py stays HUMAN-gated (surfaced via system_health), never here.

ROOT="/Users/farricecain/Google Antigravity"
PY="$ROOT/.venv/bin/python3"

echo "=== memory_weekly $(date '+%Y-%m-%d %H:%M') ==="
"$PY" "$ROOT/execution/episodic_ingest.py" run --days 7
"$PY" "$ROOT/execution/memory_embed.py" backfill
"$PY" "$ROOT/execution/memory_distill.py" run --days 7
echo "=== memory_weekly done ==="
