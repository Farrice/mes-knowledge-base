#!/bin/zsh
# Daily Zeitgeist Engine — 06:20 local headless run (2026-08-05).
# Deterministic scrape (zeitgeist_engine.py, --pulse-mode budget) → headless claude
# synthesis (brief JSON per .agent/zeitgeist-synthesis-prompt.md) → render_brief --gdoc
# → asset board. Invocation pattern mirrors execution/angle_map_listening_run.sh.
set -u
REPO="/Users/farricecain/Google Antigravity"
LOG="$REPO/.agent/zeitgeist-run.log"
CLAUDE="/Users/farricecain/.npm-global/bin/claude"
cd "$REPO" || exit 1
echo "=== $(date '+%F %T') zeitgeist run start ===" >> "$LOG"

# GOLDEN RULE: one writer per tree. Claim or skip — never run alongside a live session.
CLAIM=$(python3 execution/session_lock.py claim "zeitgeist daily run" 2>&1)
echo "$CLAIM" >> "$LOG"
if [[ "$CLAIM" != *"claimed:"* ]]; then
  echo "lock blocked — skipping today's run (one writer per tree)" >> "$LOG"
  exit 0
fi
TOKEN=$(echo "$CLAIM" | sed -n 's/.*claimed: \([a-z0-9]*\).*/\1/p')

# 1) Deterministic scrape — never raises; pulse budget skips gracefully.
ENGINE_OUT=$(python3 execution/zeitgeist_engine.py run 2>&1)
echo "$ENGINE_OUT" >> "$LOG"
PACKS=$(echo "$ENGINE_OUT" | tail -1 | python3 -c "import json,sys
try: print(' '.join(json.load(sys.stdin).get('packs',[])))
except Exception: print('')" 2>/dev/null)

# 2) Synthesis — only if the scrape produced packs.
if [[ -n "$PACKS" ]]; then
  "$CLAUDE" -p "Read and execute .agent/zeitgeist-synthesis-prompt.md for these signal packs: $PACKS. This is the scheduled daily zeitgeist run. No Chain, no finalize, no Notion, no Next Moves, no subagents — produce only the brief artifacts the prompt specifies." \
    --permission-mode acceptEdits >> "$LOG" 2>&1
  RC=$?
else
  echo "no packs produced (nothing due, or pulse budget skipped) — no synthesis" >> "$LOG"
  RC=0
fi

python3 execution/session_lock.py release "$TOKEN" >> "$LOG" 2>&1 || true
echo "=== $(date '+%F %T') zeitgeist run end rc=$RC ===" >> "$LOG"
exit $RC
