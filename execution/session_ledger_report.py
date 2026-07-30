#!/usr/bin/env python3
"""session_ledger_report.py — deterministic reader for the finalize-debt
observe log (loop-repair #3ii, Farrice all-12 GO 2026-07-24).

The Stop-hook has logged would-block events since 2026-06-14 with zero
consumers. This report is the consumer: it collapses multi-Stop-per-session
noise into per-session facts and a weekly trend, so the LEDGER_ENFORCE
decision can be made on evidence. Bucketing rules live in code, never in
model judgment (AI-memory-dependent observability is banned).

Usage:
    python3 execution/session_ledger_report.py            # print report
    python3 execution/session_ledger_report.py --write    # also write .agent/sessions/session-ledger-report.md
"""

import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LOG = REPO_ROOT / ".agent" / "sessions" / "observe-log.jsonl"
OUT = REPO_ROOT / ".agent" / "sessions" / "session-ledger-report.md"


def summary() -> dict:
    """Machine-readable rollup; imported by health_metrics.py."""
    if not LOG.exists():
        return {}
    events = []
    for line in LOG.read_text().splitlines():
        try:
            events.append(json.loads(line))
        except Exception:
            continue
    if not events:
        return {}
    sessions = defaultdict(list)
    for e in events:
        sessions[e.get("session_id", "?")].append(e)
    weekly = Counter()
    debt_types = Counter()
    zero_spawn_sessions = 0
    for sid, evs in sessions.items():
        ts = evs[-1].get("ts", "")
        try:
            week = datetime.fromisoformat(ts).strftime("%G-W%V")
        except Exception:
            week = "unknown"
        weekly[week] += 1
        for d in evs[-1].get("debts", []):
            debt_types[d.get("type", "?")] += 1
        if evs[-1].get("subagent_spawns", 0) == 0:
            zero_spawn_sessions += 1
    n_sessions = len(sessions)
    return {
        "events": len(events),
        "debted_sessions": n_sessions,
        "noise_factor": round(len(events) / max(1, n_sessions), 1),
        "weekly_debted_sessions": dict(sorted(weekly.items())),
        "debt_types": dict(debt_types.most_common(5)),
        "zero_spawn_sessions": zero_spawn_sessions,
    }


def render(s: dict) -> str:
    if not s:
        return "# Session-Ledger Report\n\n(no observe-log data)\n"
    lines = [
        "# Session-Ledger Report (finalize-debt observe mode)",
        f"Generated {datetime.now().isoformat(timespec='seconds')} · source: .agent/sessions/observe-log.jsonl",
        "",
        f"- **{s['events']} would-block events** collapse to **{s['debted_sessions']} debted sessions** "
        f"(noise factor {s['noise_factor']}x — multi-Stop firings per session; enforcement today would "
        f"block ~{s['noise_factor']}x per honest session).",
        f"- Sessions ending with zero measured subagent spawns: {s['zero_spawn_sessions']}.",
        "- Top open-debt types (last event per session): "
        + ", ".join(f"{k} ({v})" for k, v in s["debt_types"].items()),
        "",
        "## Debted sessions per ISO week",
        "",
        "| week | sessions |",
        "|---|---|",
    ]
    lines += [f"| {w} | {c} |" for w, c in s["weekly_debted_sessions"].items()]
    lines += [
        "",
        "## Decision guidance (deterministic, not advice)",
        "",
        "- Flip `LEDGER_ENFORCE=1` only when the weekly debted-session count is a number you would",
        "  accept being hard-blocked that many times per week — the noise factor above is the",
        "  false-positive multiplier to fix (dedupe Stop firings) BEFORE enforcement.",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    s = summary()
    text = render(s)
    print(text)
    if "--write" in sys.argv:
        OUT.write_text(text)
        print(f"[written] {OUT.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
