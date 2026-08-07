#!/usr/bin/env python3
"""pending_decisions_hook.py — surface decisions waiting on Farrice, at session open.

WHY (2026-07-27): the harness accumulates things only a human can decide, and
NOTHING showed them to him at session open. Verified that day — all three
SessionStart hooks (divergence_alarm, concurrent_session_alarm, menu_parity)
were checked and none reads a pending-decision queue. The consequences were
measurable:

  - a born-intent anchor sat waiting on a one-word `--bless` for days while it
    held the verifier fleet red
  - 12 of 73 verifiers were failing since 2026-07-26, reported only to a log
  - `pending-review.md` removal proposals surface only inside /weekly-closeout

Self-heal now repairs everything mechanical (AUTO/EVIDENCE). What is left is,
by construction, exactly the set that needs his judgment — so it is the one
thing worth spending session-open attention on.

CONTRACT (matches divergence_alarm_hook.py, the house style for operator alarms)
  - plain text to stdout -> SessionStart additionalContext
  - `sys.exit(0)` ALWAYS. Never blocks, never fails a session open.
  - SILENCE WHEN CLEAN. No "0 pending" line — a hook that speaks every session
    stops being read, and then it is just another dead channel.
  - Every line is `⚠ TAG: <what> — <exact command>`; a finding with no command
    is a complaint, not a decision.
  - CACHED READS ONLY. No verifier runs, no git walks. Budget ~2s; SessionStart
    already carries divergence_alarm (p90 ~2s).
  - Caps output. At most MAX_LINES findings plus a roll-up.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HEALTH = ROOT / ".agent" / "health"
REPORT_CACHE = HEALTH / "self-heal-report.json"
HEAL_CACHE = HEALTH / "self-heal-latest.json"
PENDING_REVIEW = HEALTH / "pending-review.md"
PHASE2_QUEUE = ROOT / "evolution_store" / "queue" / "phase2_queue.jsonl"
REGISTRY = ROOT / "evolution_store" / "failure-registry.md"
FLEET_CACHE = HEALTH / "fleet.json"

MAX_LINES = 3
STALE_HOURS = 72   # beyond this the cache describes a world that has moved on


def _judgment_rows() -> tuple[list[dict], float | None]:
    """JUDGMENT findings from whichever self-heal cache is fresher."""
    rows, ts = [], None
    for p in (REPORT_CACHE, HEAL_CACHE):
        try:
            d = json.loads(p.read_text())
        except Exception:
            continue
        t = str(d.get("ts", ""))
        if ts is None or t > ts:
            rows, ts = d.get("rows") or [], t
    if not ts:
        return [], None
    try:
        age_h = (datetime.now() - datetime.fromisoformat(ts)).total_seconds() / 3600
    except ValueError:
        return [], None
    return [r for r in rows if r.get("cls") == "JUDGMENT"], age_h


def _pending_review_count() -> int:
    try:
        return PENDING_REVIEW.read_text(errors="replace").count("status: pending")
    except OSError:
        return 0


def _phase2_human_rows() -> int:
    n = 0
    try:
        with PHASE2_QUEUE.open() as f:
            for line in f:
                if "human_review_required" in line:
                    n += 1
    except OSError:
        pass
    return n


def _chronic_rules() -> int:
    """Prevention rules the learner recorded as CHRONIC — a fix that keeps
    failing is a standing decision, not a transient blip."""
    try:
        return REGISTRY.read_text(errors="replace").count("### [CHRONIC]:")
    except OSError:
        return 0


def _fleet_findings() -> int:
    """Count flagged findings from fleet verification (loop-integrity, core-surface)."""
    try:
        data = json.loads(FLEET_CACHE.read_text())
        by_classification = data.get("summary", {}).get("by_classification", {})
        return by_classification.get("FLAGGED", 0) + by_classification.get("UNDERLOADED", 0)
    except (OSError, json.JSONDecodeError):
        return 0


def main() -> None:
    lines: list[str] = []
    try:
        judgment, age_h = _judgment_rows()
        if age_h is not None and age_h > STALE_HOURS:
            lines.append(
                f"⚠ SELF-HEAL STALE: last scan was {age_h / 24:.0f}d ago — "
                "run `python3 execution/self_heal.py report` (a dark healer "
                "hides everything downstream of it).")
        elif judgment:
            shown = judgment[:MAX_LINES]
            for r in shown:
                what = str(r.get("what", ""))[:120]
                fix = str(r.get("fix", ""))[:90]
                lines.append(f"⚠ NEEDS YOU: {r.get('id')} — {what} → `{fix}`")
            if len(judgment) > MAX_LINES:
                lines.append(
                    f"⚠ +{len(judgment) - MAX_LINES} more waiting — "
                    "`python3 execution/self_heal.py report` for the full list.")
    except Exception:
        pass

    try:
        n = _chronic_rules()
        if n:
            lines.append(
                f"⚠ CHRONIC: {n} failure mode(s) whose automated fix keeps failing — "
                "read `evolution_store/failure-registry.md`; retrying them is wasted work.")
    except Exception:
        pass

    try:
        n = _pending_review_count()
        if n:
            lines.append(
                f"⚠ AWAITING YOUR YES: {n} removal proposal(s) — "
                "`.agent/health/pending-review.md`; nothing executes without it.")
    except Exception:
        pass

    try:
        n = _phase2_human_rows()
        if n:
            lines.append(
                f"⚠ EVOLUTION QUEUE: {n} skill(s) need ground truth before they can "
                "auto-evolve — `python3 execution/evolution_orchestrator.py status`.")
    except Exception:
        pass

    try:
        n = _fleet_findings()
        if n:
            lines.append(
                f"⚠ FLEET: {n} wiring issue(s) found — "
                "read `.agent/health/fleet-report.md` for details; `python3 execution/verify_fleet.py` to rescan.")
    except Exception:
        pass

    # Full-power watchdog (2026-08-06 lanes build): a hook that could not
    # resolve python ran degraded somewhere — surface it until the log is cleared.
    try:
        import time as _t
        beacon = ROOT / ".agent" / "hook-failures.log"
        if beacon.exists() and (_t.time() - beacon.stat().st_mtime) < 24 * 3600:
            n = len(beacon.read_text().splitlines())
            lines.append(
                f"⚠ HOOK DEGRADATION: {n} entr(ies) in .agent/hook-failures.log — a tree ran "
                "with degraded hooks → `python3 execution/worktree_lane.py doctor --fix`, then "
                "clear the log.")
    except Exception:
        pass

    # Silence when clean. This is the whole discipline.
    if lines:
        print("PENDING DECISIONS (deterministic, from pending_decisions_hook.py — "
              "self-heal already fixed everything mechanical; these need judgment):")
        for l in lines[:MAX_LINES + 3]:
            print(f"  {l}")

    sys.exit(0)


if __name__ == "__main__":
    main()
