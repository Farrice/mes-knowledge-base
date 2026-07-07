#!/usr/bin/env python3
"""session_end_hook.py — SessionEnd deterministic backstop for the closeout spine.

WHY: /end-session persisting a handoff was never itself physically enforced —
a session could ship real artifacts and simply be closed by exiting Claude
Code, losing the closeout intelligence capture, sovereign-memory record, COS
journal entry, and session-state archive that `end_session_closeout.py`
provides. This hook makes closeout no longer memory-dependent on the operator:
if a session produced artifacts and the closeout spine never ran, this fires
it once in degraded mode on the way out.

Skip conditions (exit 0 silently):
    - No ledger for this session (nothing tracked, e.g. a stateless surface).
    - The ledger already shows closeout_ran (set by session_ledger_hook.py
      posttool when it sees `CLOSEOUT SPINE COMPLETE` / an
      end_session_closeout.py invocation in Bash output, or by THIS hook
      after a degraded run — re-entry guard for double SessionEnd fires).
    - The ledger shows no produced artifacts (pure conversational session).

Otherwise: runs `end_session_closeout.py run --degraded` (90s timeout),
marks closeout_ran in the ledger, and appends one line to
.agent/sessions/observe-log.jsonl for visibility.

FAIL-SAFE: any exception anywhere -> exit 0. A broken backstop must never
block session end. Wired via .claude/settings.json -> hooks.SessionEnd.
"""

import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SESSIONS_DIR = REPO_ROOT / ".agent" / "sessions"
OBSERVE_LOG = SESSIONS_DIR / "observe-log.jsonl"


def _now() -> str:
    return datetime.now().isoformat()


def _ledger_path(session_id: str) -> Path:
    safe = re.sub(r"[^A-Za-z0-9_-]", "_", session_id or "unknown")[:64]
    return SESSIONS_DIR / f"ledger-{safe}.json"


def main() -> None:
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
    except Exception:
        sys.exit(0)

    try:
        session_id = payload.get("session_id", "unknown")
        reason = payload.get("reason", "")

        ledger_path = _ledger_path(session_id)
        if not ledger_path.exists():
            sys.exit(0)

        try:
            ledger = json.loads(ledger_path.read_text())
        except Exception:
            sys.exit(0)

        if ledger.get("closeout_ran"):
            sys.exit(0)

        produced = bool(ledger.get("produced")) or bool(ledger.get("produced_paths"))
        if not produced:
            sys.exit(0)

        try:
            subprocess.run(
                [sys.executable, str(REPO_ROOT / "execution" / "end_session_closeout.py"),
                 "run", "--degraded"],
                capture_output=True, text=True, timeout=90, cwd=str(REPO_ROOT),
            )
        except Exception:
            pass

        # Re-entry guard: mark closeout_ran in this session's own ledger so a
        # second SessionEnd fire for the same session skips. The posttool
        # detection in session_ledger_hook.py only covers spine runs made via
        # the Bash tool inside the session — it can't see this hook's run.
        try:
            ledger["closeout_ran"] = True
            ledger_path.write_text(json.dumps(ledger, indent=1))
        except Exception:
            pass

        try:
            SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
            with open(OBSERVE_LOG, "a") as f:
                f.write(json.dumps({
                    "event": "session_end_auto_closeout",
                    "session_id": session_id,
                    "ts": _now(),
                    "reason": reason,
                }) + "\n")
        except Exception:
            pass
    except Exception:
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
