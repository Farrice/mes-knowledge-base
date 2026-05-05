#!/bin/bash
# Daily Zeitgeist Brief runner — invoked by launchd at 7:03am LA daily.
# Runs the workflow via Claude Code in non-interactive mode and emails
# the brief to farrice.cain@gmail.com.

set -e

PROJECT_DIR="/Users/farricecain/Google Antigravity"
LOG_DIR="$PROJECT_DIR/.tmp/zeitgeist"
DATE=$(date +%Y-%m-%d)

mkdir -p "$LOG_DIR"

echo "[$(date)] Starting daily zeitgeist brief for $DATE" >> "$LOG_DIR/launchd-stdout.log"

cd "$PROJECT_DIR"

# Invoke Claude Code in non-interactive mode with the workflow command.
# --print runs once and exits. --dangerously-skip-permissions is needed
# because launchd has no TTY for permission prompts.
claude --print --dangerously-skip-permissions \
  "Run the workflow at .agent/workflows/daily-zeitgeist-brief.md for today's date $DATE. Execute all 11 phases. Use Gmail MCP create_draft if gws scope still missing; otherwise gws gmail +send (no --draft flag for autonomous send). Subject: 'Parallax Daily — [3-word punch]'. Archive to knowledge/zeitgeist-archive/$DATE.md. Append run record to .agent/zeitgeist-runs.jsonl with status, subject, gaps. Time-box research to 12-15 min." \
  >> "$LOG_DIR/launchd-stdout.log" 2>> "$LOG_DIR/launchd-stderr.log"

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
  echo "[$(date)] Brief delivered successfully" >> "$LOG_DIR/launchd-stdout.log"
else
  echo "[$(date)] Brief failed with exit code $EXIT_CODE" >> "$LOG_DIR/launchd-stderr.log"
  # Append failure to run log so morning audit catches it
  echo "{\"date\":\"$DATE\",\"status\":\"failed\",\"exit_code\":$EXIT_CODE}" \
    >> "$PROJECT_DIR/.agent/zeitgeist-runs.jsonl"
fi

exit $EXIT_CODE
