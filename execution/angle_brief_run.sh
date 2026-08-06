#!/bin/zsh
# Angle Brief — Mon/Thu 07:00 local headless run (built 2026-08-06, Cody Schneider
# extraction session). Deterministic listening first (signal_scout.py — LISTENING-ONLY,
# never contacts anyone), then headless claude synthesis per
# _active/farrice-brand/04-deliverables/ANGLE-BRIEF-PROMPT.md → render_brief.py → briefs board.
# Invocation pattern mirrors execution/angle_map_listening_run.sh (proven 2026-08-05).
set -u
REPO="/Users/farricecain/Google Antigravity"
LOG="$REPO/.agent/angle-brief-run.log"
CLAUDE="/Users/farricecain/.npm-global/bin/claude"
cd "$REPO" || exit 1
echo "=== $(date '+%F %T') angle-brief run start ===" >> "$LOG"

# GOLDEN RULE: one writer per tree. Claim or skip — never run alongside a live session.
CLAIM=$(python3 execution/session_lock.py claim "angle-brief Mon/Thu run" 2>&1)
echo "$CLAIM" >> "$LOG"
if [[ "$CLAIM" != *"claimed:"* ]]; then
  echo "lock blocked — skipping this run (one writer per tree)" >> "$LOG"
  exit 0
fi
TOKEN=$(echo "$CLAIM" | sed -n 's/.*claimed: \([a-z0-9]*\).*/\1/p')

# 1) Deterministic listening refresh — budget-guarded in apify_client, never raises.
python3 execution/signal_scout.py >> "$LOG" 2>&1 \
  || echo "signal_scout failed — synthesis will use the newest existing roster" >> "$LOG"

# 2) Headless synthesis → HTML brief on the board.
"$CLAUDE" -p "Read and execute _active/farrice-brand/04-deliverables/ANGLE-BRIEF-PROMPT.md for today's date. This is the scheduled Angle Brief run (local, full-tool). Honor every boundary in that file. No publishing, outreach, or contact of any kind. No Chain, no finalize, no Notion, no Next Moves, no subagents." \
  --permission-mode acceptEdits >> "$LOG" 2>&1
RC=$?

python3 execution/session_lock.py release "$TOKEN" >> "$LOG" 2>&1 || true
echo "=== $(date '+%F %T') angle-brief run end rc=$RC ===" >> "$LOG"
exit $RC
