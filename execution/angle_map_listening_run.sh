#!/bin/zsh
# Angle Map Listening Engine — daily 05:30 local headless run (v4 fusion, 2026-07-31).
# Local-first replaces the cloud routine: cloud runs were proxy-blocked (zero Reddit
# reads 2026-07-30); local runs carry .env (API_KEY, PERPLEXITY_API_KEY) + full tools.
# Invocation pattern matches execution/mission_runner.py (claude -p + acceptEdits).
# AUTH FIX 2026-08-27: use CLAUDE_CODE_SIMPLE=1 + ANTHROPIC_API_KEY to bypass OAuth/Keychain
# issues in headless launchd context. OAuth token refresh was failing after 4 days.
set -u
REPO="/Users/farricecain/Google Antigravity"
LOG="$REPO/_active/knowledge/health-performance-ip-library/06-system/listening-run.log"
CLAUDE="/Users/farricecain/.npm-global/bin/claude"
cd "$REPO" || exit 1
mkdir -p "$(dirname "$LOG")"
echo "=== $(date '+%F %T') listening run start ===" >> "$LOG"

# Load .env for ANTHROPIC_API_KEY and other secrets
if [[ -f "$REPO/.env" ]]; then
  set -a
  source "$REPO/.env"
  set +a
fi

# GOLDEN RULE: one writer per tree. Claim or skip — never run alongside a live session.
CLAIM=$(python3 execution/session_lock.py claim "angle-map-listening daily run" 2>&1)
echo "$CLAIM" >> "$LOG"
if [[ "$CLAIM" != *"claimed:"* ]]; then
  echo "lock blocked — skipping today's run (one writer per tree)" >> "$LOG"
  exit 0
fi
TOKEN=$(echo "$CLAIM" | sed -n 's/.*claimed: \([a-z0-9]*\).*/\1/p')

# Run in CLAUDE_CODE_SIMPLE mode (API key auth) to avoid OAuth/Keychain issues
export CLAUDE_CODE_SIMPLE=1
"$CLAUDE" -p "Read and execute _active/knowledge/health-performance-ip-library/AUTOMATION_PROMPT.md for today's date. This is the scheduled Angle Map Listening Engine daily run (local, full-tool). Honor every gate, boundary, and budget in that file. No publishing, outreach, or contact of any kind. Subagent brief if any are used: no Chain, no finalize, no Notion, no Next Moves, return only the artifact." \
  --permission-mode acceptEdits >> "$LOG" 2>&1
RC=$?

python3 execution/session_lock.py release "$TOKEN" >> "$LOG" 2>&1 || true
echo "=== $(date '+%F %T') listening run end rc=$RC ===" >> "$LOG"
exit $RC
