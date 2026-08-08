#!/bin/zsh
# Nightly mission sweep — 02:45 local (2026-08-07).
#
# Deterministic collect (session_sweep.py) → facts-only briefs (mission_brief.py)
# → headless claude synthesis into the NAMED SLOTS ONLY → rebuild with meaning
# → Briefing Room index. Invocation pattern mirrors execution/zeitgeist_run.sh.
#
# The two-pass shape is deliberate: briefs exist on disk after pass 1 even if the
# synthesis never runs, so a failed or skipped judge degrades to a facts-only
# board rather than to nothing.
#
# Called by ~/Library/LaunchAgents/com.antigravity.session-sweep.plist
set -u
REPO="/Users/farricecain/Google Antigravity"
LOG="$REPO/.agent/sweep/session-sweep.log"
RECEIPT="$REPO/.agent/health/session-sweep.json"
CLAUDE="${CLAUDE_BIN:-/Users/farricecain/.npm-global/bin/claude}"
SYNTH="$REPO/.agent/sweep/synthesis.json"
cd "$REPO" || exit 1
mkdir -p "$REPO/.agent/sweep" "$REPO/.agent/health"
echo "=== $(date '+%F %T') mission sweep start ===" >> "$LOG"

# GOLDEN RULE: one writer per tree. Claim or skip — never run alongside a live session.
CLAIM=$(python3 execution/session_lock.py claim "nightly mission sweep" 2>&1)
echo "$CLAIM" >> "$LOG"
if [[ "$CLAIM" != *"claimed:"* ]]; then
  echo "lock blocked — skipping tonight's sweep (one writer per tree)" >> "$LOG"
  # Still print a line: launchd's log mtime is the ONLY liveness evidence
  # detect_dead_launchd() reads, and a silent skip reads as a dead job.
  python3 -c "import json,datetime;print(json.dumps({'session_sweep':datetime.datetime.now().isoformat(),'status':'skipped','reason':'session lock held'}))"
  exit 0
fi
TOKEN=$(echo "$CLAIM" | sed -n 's/.*claimed: \([a-z0-9]*\).*/\1/p')

# 1) Deterministic collect. Writes .agent/sweep/sweep-<date>.json + latest.json.
SWEEP_OUT=$(python3 execution/session_sweep.py run --days 14 2>&1)
echo "$SWEEP_OUT" >> "$LOG"

# 2) Facts-only briefs. Every number/path/date is filled here and is now immutable.
python3 execution/mission_brief.py build --all --no-index >> "$LOG" 2>&1

# 3) Synthesis — the ONLY step allowed to write prose, and only into named slots.
#    Skipped cleanly when the CLI is missing so the box still has a fresh board.
RC=0
if [[ -x "$CLAUDE" ]]; then
  "$CLAUDE" -p "Run the nightly mission-brief synthesis.

1. Read .agent/sweep/latest.json — this is the FACT BUNDLE for every live thread.
2. Run: python3 execution/mission_brief.py slots — it prints the exact contract.
3. Write .agent/sweep/synthesis.json mapping each thread slug (plus 'mission-board')
   to ONLY these keys: lede, next_move, why, caveats, operator_read.

HARD RULES:
- Never state a number, path, date, count or filename. Those are already rendered
  from the bundle; restating one is how a synthesis pass introduces an error.
- 'lede' is 1-2 sentences on where the thread actually stands. Plain language.
- 'next_move' is one imperative sentence — the single next action.
- If a thread's records do not support a confident read, write a shorter honest
  lede. Do not speculate about intent or invent progress.
- Threads with no real signal: omit them from the file entirely.

No Chain, no finalize, no Notion, no Next Moves, no subagents — write only that one JSON file." \
    --permission-mode acceptEdits >> "$LOG" 2>&1
  RC=$?
else
  echo "claude CLI not found at $CLAUDE — facts-only board (synthesis skipped)" >> "$LOG"
fi

# 4) Rebuild with whatever synthesis landed, then refresh the Room index.
python3 execution/mission_brief.py build --all >> "$LOG" 2>&1

python3 execution/session_lock.py release "$TOKEN" >> "$LOG" 2>&1 || true

# 5) Receipt — the JSON file downstream reads, AND a stdout line so the launchd
#    log mtime moves. A job with a receipt but no stdout still reads as dead.
python3 - "$RC" "$SYNTH" <<'PY' | tee -a "$LOG"
import json, sys, datetime
from pathlib import Path
rc, synth = int(sys.argv[1]), Path(sys.argv[2])
bundle = {}
try:
    bundle = json.loads(Path(".agent/sweep/latest.json").read_text())
except Exception:
    pass
rec = {
    "session_sweep": datetime.datetime.now().isoformat(),
    "status": "ok" if rc == 0 else "synthesis_failed",
    "synthesis_rc": rc,
    "synthesized": synth.exists(),
    "counts": bundle.get("counts", {}),
    "degraded": bundle.get("degraded", []),
}
Path(".agent/health/session-sweep.json").write_text(json.dumps(rec, indent=2) + "\n")
print(json.dumps(rec))
PY

echo "=== $(date '+%F %T') mission sweep end rc=$RC ===" >> "$LOG"
exit 0
