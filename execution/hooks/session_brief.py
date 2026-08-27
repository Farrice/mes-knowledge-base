#!/usr/bin/env python3
"""session_brief.py — SessionStart digest (Farrice, 2026-08-20).

Goal + scar (rule contract): the eight SessionStart hooks each printed a full
block (missions list, pending decisions, git integrity, campaign, lanes) —
~60 lines of scroll at every session open. Farrice: "I don't need to see all
this." The detail already lives on the pulse board and in each script's CLI —
the startup dump duplicated it.

This wrapper runs the noisy hooks, captures their output, and emits AT MOST
ONE LINE per domain: the script's own first meaningful line (they all lead
with a summary header), plus a pointer to the full view when more was said.
Alarms still surface — compressed, never swallowed. Compass doctrine: nudges
get out of the way.

Never blocks, always exits 0. A child that dies or hangs (15s cap) is reported
in one line, not silently dropped.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PY = str(ROOT / ".venv" / "bin" / "python3")
if not Path(PY).exists():
    PY = sys.executable

# (label, argv, detail-hint) — order preserved from the old hook order.
CHILDREN = [
    ("git", [PY, str(ROOT / "execution" / "hooks" / "divergence_alarm_hook.py")],
     "python3 execution/hooks/divergence_alarm_hook.py"),
    ("menu", [PY, str(ROOT / "execution" / "hooks" / "menu_parity_hook.py"), "sessionstart"],
     "python3 execution/hooks/menu_parity_hook.py sessionstart"),
    ("decisions", [PY, str(ROOT / "execution" / "hooks" / "pending_decisions_hook.py")],
     "python3 execution/self_heal.py report"),
    ("campaign", [PY, str(ROOT / "execution" / "hooks" / "campaign_beacon.py")],
     "_active/linkedin/CAMPAIGN.md"),
    ("missions", [PY, str(ROOT / "execution" / "pulse_dashboard.py"), "--open", "--alarm"],
     "python3 execution/pulse_dashboard.py --open"),
    ("voice", [PY, str(ROOT / "execution" / "voice_ratchet.py"), "nudge"],
     "python3 execution/voice_ratchet.py nudge"),
    ("library", [PY, str(ROOT / "execution" / "work_catalog.py"), "nudge"],
     "http://127.0.0.1:8765/library"),
    # Second-brain read path (2026-08-21): the one line that keeps memory
    # health visible — before this, the review-queue alarm lived only in a
    # launchd log and went unseen 26 straight days.
    ("memory", [PY, str(ROOT / "execution" / "memory_pulse.py")],
     "python3 execution/memory_pulse.py --full"),
    # Standing-council outcome loop (the Mailroom, 2026-08-27): silent when
    # clean; one line when calibration predictions or decision memories are
    # sitting open. Before this, pending rows had no watcher.
    ("council", [PY, str(ROOT / "execution" / "council_pulse.py")],
     "python3 execution/council_pulse.py --full"),
]

MAX_LINE = 160


BOILERPLATE = re.compile(r"\s*\((deterministic|from)[^)]*\)")


def first_meaningful(text: str) -> tuple[str, int]:
    lines = [BOILERPLATE.sub("", ln.strip()) for ln in text.splitlines() if ln.strip()]
    if not lines:
        return "", 0
    head = lines[0]
    # A pure header ("GIT INTEGRITY:") says nothing — fold in the first content line.
    if head.endswith(":") and len(lines) > 1:
        head = f"{head} {lines[1]}"
    return head, len(lines)


def main() -> int:
    stdin_data = sys.stdin.read() if not sys.stdin.isatty() else ""
    out = []
    for label, argv, hint in CHILDREN:
        try:
            proc = subprocess.run(
                argv, input=stdin_data, capture_output=True, text=True,
                timeout=15, cwd=str(ROOT),
            )
            head, total = first_meaningful(proc.stdout)
        except subprocess.TimeoutExpired:
            out.append(f"• {label}: hook timed out (15s) — run {hint} manually")
            continue
        except Exception as exc:  # never let the digest kill session start
            out.append(f"• {label}: hook failed ({exc.__class__.__name__}) — {hint}")
            continue
        if not head:
            continue
        if len(head) > MAX_LINE:
            head = head[: MAX_LINE - 1] + "…"
        more = f"  (+{total - 1} more — {hint})" if total > 1 else ""
        out.append(f"• {label}: {head}{more}")
    if out:
        print("SESSION BRIEF (one line per domain; detail lives behind each pointer):")
        print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
