#!/bin/zsh
# Nightly mission sweep — 02:45 local (2026-08-07; librarian chain 2026-08-20).
#
# Deterministic collect (session_sweep.py, which chains the catalog merge) →
# facts-only briefs → judged passes via brief_synthesis.py (analyst slots +
# librarian triage; validated FAIL-CLOSED, previous synthesis restored on any
# failure — never silently discarded, the pre-2026-08-20 script moved it aside
# nightly which is why judged prose never survived) → rebuild with meaning →
# regenerate every surface (Room index, Homebase, Library).
#
# Called by ~/Library/LaunchAgents/com.antigravity.session-sweep.plist
set -u
REPO="/Users/farricecain/Google Antigravity"
LOG="$REPO/.agent/sweep/session-sweep.log"
RECEIPT="$REPO/.agent/health/session-sweep.json"
SYNTH="$REPO/.agent/sweep/synthesis.json"
cd "$REPO" || exit 1
mkdir -p "$REPO/.agent/sweep" "$REPO/.agent/health" "$REPO/.tmp"
echo "=== $(date '+%F %T') mission sweep start ===" >> "$LOG"

# GOLDEN RULE: one writer per tree. Claim or skip — never run alongside a live session.
CLAIM=$(python3 execution/session_lock.py claim "nightly mission sweep" 2>&1)
echo "$CLAIM" >> "$LOG"
if [[ "$CLAIM" != *"claimed:"* ]]; then
  echo "lock blocked — skipping tonight's sweep (one writer per tree)" >> "$LOG"
  python3 -c "import json,datetime;print(json.dumps({'session_sweep':datetime.datetime.now().isoformat(),'status':'skipped','reason':'session lock held'}))"
  exit 0
fi
TOKEN=$(echo "$CLAIM" | sed -n 's/.*claimed: \([a-z0-9]*\).*/\1/p')

# 1) Deterministic collect (also folds the census into the permanent catalog).
python3 execution/session_sweep.py run --days 14 >> "$LOG" 2>&1

# 2) Facts-only briefs — every number/path/date filled here, immutable.
python3 execution/mission_brief.py build --all --no-index >> "$LOG" 2>&1

# 3) Judged passes — analyst slots + librarian triage. brief_synthesis.py owns
#    the whole contract: batched claude -p, canonical validation, per-entry
#    pruning, and RESTORE-previous on failure. An expired CLI degrades to the
#    last valid synthesis (age is surfaced on the briefs), never to nothing.
python3 execution/brief_synthesis.py run >> "$LOG" 2>&1
RC=$?
python3 execution/brief_synthesis.py triage >> "$LOG" 2>&1 || true

# 4) Rebuild with whatever synthesis stands, then every surface.
python3 execution/mission_brief.py build --all >> "$LOG" 2>&1
python3 execution/homebase_board.py >> "$LOG" 2>&1 || true
python3 execution/catalog_board.py >> "$LOG" 2>&1 || true

python3 execution/session_lock.py release "$TOKEN" >> "$LOG" 2>&1 || true

# 5) Receipt + stdout line (launchd log mtime is the liveness evidence).
python3 - "$RC" "$SYNTH" <<'PY' | tee -a "$LOG"
import json, sys, datetime
from pathlib import Path
rc, synth = int(sys.argv[1]), Path(sys.argv[2])
bundle, receipt = {}, {}
try:
    bundle = json.loads(Path(".agent/sweep/latest.json").read_text())
except Exception:
    pass
try:
    receipt = json.loads(Path(".agent/sweep/synthesis-receipt.json").read_text())
except Exception:
    pass
rec = {
    "session_sweep": datetime.datetime.now().isoformat(),
    "status": "ok" if rc == 0 else "synthesis_degraded",
    "synthesis_rc": rc,
    "synthesized": synth.exists(),
    "synthesis_generated": receipt.get("generated"),
    "counts": bundle.get("counts", {}),
    "degraded": bundle.get("degraded", []),
}
Path(".agent/health/session-sweep.json").write_text(json.dumps(rec, indent=2) + "\n")
print(json.dumps(rec))
PY

echo "=== $(date '+%F %T') mission sweep end rc=$RC ===" >> "$LOG"
exit 0
