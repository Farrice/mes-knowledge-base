#!/usr/bin/env python3
"""menu_parity_hook.py — PostToolUse advisory (Write|Edit on skill workflows).

WHY: a workflow written into skills/<skill>/workflows/ is not fireable until a
wrapper + shim exist. That minting used to be a manual step and manual steps
lose to velocity — 728 workflows accumulated unfireable before heartbeat check 7
existed to notice. This is the fastest of the four parity surfaces: it tells you
at write time, while the intent is still in your head.

FAST BY CONSTRUCTION: no arsenal_index import. That module globs ~5k files;
this hook must stay under ~100ms, so it does ONE stat call for a same-stem
shim. It is a nudge, not an authority — the end-session spine and the nightly
sweep run the real check and do the actual minting.

DEBOUNCED: one notice per skill per session, tracked in
.agent/sessions/menu-parity-seen.json. Forging 12 workflows in a row should
produce one line, not twelve — a hook that spams is a hook that gets ignored.

NEVER blocks, never exits nonzero, silent when the shim already exists.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

PROJECT = Path(os.environ.get("CLAUDE_PROJECT_DIR")
               or Path(__file__).resolve().parents[2])
SEEN_PATH = PROJECT / ".agent" / "sessions" / "menu-parity-seen.json"
SKILL_WF_RE = re.compile(r"skills/([^/]+)/workflows/([^/]+)\.md$")
# Same exemption vocabulary as skill_auditor check 7 — a named opt-out is a
# decision, and decisions are respected here too.
EXEMPT_RE = re.compile(r"^\s*(?:menu_exempt\s*:|status\s*:\s*superseded\b|superseded_by\s*:)",
                       re.I | re.M)
VARIANT_RE = re.compile(r"\.variant\.|\.pre-evolution\.|backup", re.I)


def _already_flagged(session: str, skill: str) -> bool:
    """True if this session already got a notice for this skill (and records it)."""
    try:
        state = json.loads(SEEN_PATH.read_text(encoding="utf-8"))
    except Exception:
        state = {}
    if not isinstance(state, dict):
        state = {}
    flagged = state.get(session) or []
    if skill in flagged:
        return True
    flagged.append(skill)
    state[session] = flagged[-200:]
    # Keep only the most recent sessions so the file cannot grow without bound.
    if len(state) > 40:
        state = dict(list(state.items())[-40:])
    try:
        SEEN_PATH.parent.mkdir(parents=True, exist_ok=True)
        SEEN_PATH.write_text(json.dumps(state), encoding="utf-8")
    except Exception:
        pass
    return False


def session_start() -> None:
    """One line at kickoff: what the nightly sweep minted, and what still drifts.

    Reads only the last line of the sweep report — never rebuilds the index, so
    it costs nothing at session start. Silent when the last sweep was clean.
    """
    report = PROJECT / ".agent" / "sessions" / "menu-parity.jsonl"
    try:
        lines = [ln for ln in report.read_text(encoding="utf-8").splitlines() if ln.strip()]
        rec = json.loads(lines[-1])
    except Exception:
        return
    minted, drift = int(rec.get("minted", 0)), int(rec.get("remaining_drift", 0))
    if not minted and not drift:
        return
    bits = []
    if minted:
        bits.append(f"{minted} workflow(s) minted overnight and now fireable")
    if drift:
        bits.append(f"{drift} still unreachable "
                    f"(`python3 execution/mint_menu_wrappers.py --scope all --apply`)")
    print(f"ARSENAL (deterministic, from menu_parity_hook.py): {' · '.join(bits)}. "
          f"Browse what you have: `/arsenal <task>`.")


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "sessionstart":
        session_start()
        return
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return
    if payload.get("tool_name") not in ("Write", "Edit"):
        return
    path = (payload.get("tool_input") or {}).get("file_path", "")
    m = SKILL_WF_RE.search(str(path).replace("\\", "/"))
    if not m:
        return
    skill, stem = m.group(1), m.group(2)
    if VARIANT_RE.search(stem):
        return

    if (PROJECT / ".claude" / "commands" / f"{stem}.md").exists():
        return  # already fireable under its own name

    try:
        head = Path(path).read_text(encoding="utf-8", errors="replace")[:600]
        if EXEMPT_RE.search(head):
            return  # named exemption — a decision, not drift
    except Exception:
        pass

    if _already_flagged(str(payload.get("session_id") or "nosession"), skill):
        return

    print(
        f"MENU PARITY (deterministic, from menu_parity_hook.py): new workflow(s) in "
        f"`{skill}` are not fireable yet — built is not the same as reachable. "
        f"No action needed now: the end-session spine mints wrappers + shims "
        f"automatically at close, and the nightly sweep catches anything it misses. "
        f"To make them fireable immediately: "
        f"`python3 execution/mint_menu_wrappers.py --scope skill {skill} --apply`"
    )


if __name__ == "__main__":
    main()
