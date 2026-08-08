#!/bin/bash
# session_sweep_run.sh — nightly deterministic session sweep + mission-board digest.
#
# Runs in headless mode (claude -p) to synthesize facts into mission briefs.
# Follows zeitgeist_run.sh pattern: session_lock claim → run → release.
#
# Called by: ~/Library/LaunchAgents/com.antigravity.session-sweep.plist
# Usage: /bin/bash execution/session_sweep_run.sh

set -e

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
EXEC="$ROOT/execution"
LOCK_MISSION="nightly-session-sweep"
LOG="$ROOT/.agent/sweep/session-sweep.log"

mkdir -p "$(dirname "$LOG")"

{
    echo "=== session-sweep run @ $(date) ==="

    # Try to claim lock; exit cleanly if unavailable
    if ! python3 "$EXEC/session_lock.py" claim "$LOCK_MISSION" 2>/dev/null; then
        echo "[$(date)] lock blocked — skipping"
        echo "[$(date)] lock blocked — skipping" >&2
        exit 0
    fi

    trap "python3 '$EXEC/session_lock.py' release '$LOCK_MISSION' 2>/dev/null || true" EXIT

    cd "$ROOT"

    # Run sweep
    echo "[$(date)] collecting sessions..."
    python3 "$EXEC/session_sweep.py" run --days 14 --json > /tmp/sweep.json 2>&1 || {
        echo "[$(date)] sweep collection failed" >&2
        exit 0
    }

    # Build briefs (includes mission-board digest)
    echo "[$(date)] building mission briefs..."
    python3 "$EXEC/mission_brief.py" build --all 2>&1 | tail -5

    # Update library
    echo "[$(date)] updating library..."
    python3 "$EXEC/brief_library.py" generate 2>&1 | tail -2

    echo "[$(date)] complete"
    echo "[$(date)] complete" >&2

    # Print JSON to stdout (launchd captures it as evidence)
    python3 -c "import json; print(json.dumps({'ts': '$(date -u +%Y-%m-%dT%H:%M:%SZ)', 'status': 'ok', 'mission': '$LOCK_MISSION'}))"

} 2>&1 | tee -a "$LOG"
