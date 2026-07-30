#!/usr/bin/env python3
"""
Evolution Orchestrator — Closes the Phase 1-4 loop (Fix 4 / 2026-04-25).

The audit (_active/system-audit/audit-2026-04-24.md) found that Phase 1-4
scripts existed (log_performance, skill_benchmark, pattern_propagation,
gap_analysis) but no orchestrator ran them as a continuous cycle. Evolution
was logging without learning. This module fixes that.

What it does:
    1. DAILY: read v2_traces from last 24h
       → compute per-skill metrics (count, avg score, regression count)
       → flag skills with 2+ scores <7 in 7-day window for Phase 2 review
       → read routing_decisions.jsonl from Fix 2
       → flag routing patterns with 3+ violations for binding review
       → write delta to evolution_store/traces/daily_evolution_<DATE>.md

    2. WEEKLY: snapshot rolling baselines per skill, write trend report

    3. MONTHLY: run gap_analysis (Phase 4)

GUARDRAIL (per audit Fix 4 design):
    Auto-evolution scoped ONLY to skills with ground-truth benchmarks.
    For skills without ground truth, log observations but DO NOT auto-modify.
    This respects best-practice principle #5: self-improvement only in
    verifiable domains.

Usage:
    python3 execution/evolution_orchestrator.py daily       # Run daily cycle
    python3 execution/evolution_orchestrator.py weekly      # Run weekly cycle
    python3 execution/evolution_orchestrator.py monthly     # Run monthly cycle
    python3 execution/evolution_orchestrator.py status      # Show last-run state
    python3 execution/evolution_orchestrator.py auto        # Run all due cycles based on state
    python3 execution/evolution_orchestrator.py queue       # Show Phase 2/binding queues

Cron suggestion (one entry, runs daily, decides what's due):
    0 6 * * * cd /Users/farricecain/Google\ Antigravity && /usr/bin/python3 execution/evolution_orchestrator.py auto >> .agent/evolution_orchestrator.log 2>&1
"""

import sys
import json
import re
import subprocess
import argparse
from pathlib import Path
from datetime import datetime, timedelta, date
from typing import Dict, List, Any, Optional
from collections import defaultdict

ROOT = Path(__file__).parent.parent
TRACE_DIR = ROOT / "evolution_store" / "v2_traces"
ROUTING_LOG = ROOT / "evolution_store" / "traces" / "routing_decisions.jsonl"
GROUND_TRUTH_MANIFEST = ROOT / "evolution_store" / "ground_truth" / "manifest.json"
ORCHESTRATOR_STATE = ROOT / "evolution_store" / "orchestrator_state.json"
DAILY_REPORT_DIR = ROOT / "evolution_store" / "traces"
PHASE2_QUEUE = ROOT / "evolution_store" / "queue" / "phase2_queue.jsonl"
BINDING_QUEUE = ROOT / "evolution_store" / "queue" / "binding_review_queue.jsonl"

# Routing-learning loop (Wave 3, 2026-07) — closes the MoE-style
# suggest->load->outcome feedback captured by skill_router_hook.py +
# execution/hooks/session_ledger_hook.py into per-skill rank weights.
ROUTING_INTEL_PATH = ROOT / ".agent" / "routing-intelligence.json"
SUB_AGENT_MISSES = ROOT / "evolution_store" / "sub_agent_misses.jsonl"
SKILL_WEIGHTS_PATH = ROOT / ".agent" / "skill-weights.json"
SYNONYM_CANDIDATES_PATH = ROOT / ".agent" / "synonym-candidates.md"
# Quality→routing cursor (Wave 1, Harness Apex 2026-07-07): last v2-trace id
# already folded into skill weights, so each finalize nudges exactly once.
QUALITY_CURSOR_PATH = ROOT / ".agent" / "routing-quality-cursor.json"

WEIGHT_NUDGE = 0.05
WEIGHT_DECAY = 0.02   # pulls weights back toward 1.0 each nightly run
WEIGHT_MIN = 0.5
WEIGHT_MAX = 2.0

# Thresholds (tunable)
LOW_SCORE_THRESHOLD = 7.0       # finalize composite below this counts as "low"
LOW_SCORE_COUNT_TRIGGER = 2     # how many lows in 7d trigger Phase 2 queue
ROUTING_VIOLATION_TRIGGER = 3   # violations per binding to trigger binding review
WEEKLY_DAYS = 7
MONTHLY_DAYS = 30

# Catch-up threshold (Fix, 2026-07-06 audit): StartCalendarInterval launchd
# jobs are silently skipped when the machine is asleep at the scheduled
# minute — observed 7 missed days in June 2026, no catch-up. If the daily
# cycle is this stale by the time ANY `auto` invocation happens (whenever
# the machine next wakes/checks in), it runs immediately and is tagged
# catchup:true in the log rather than silently waiting for tomorrow's slot.
CATCHUP_STALE_HOURS = 36


# ─────────────────────────────────────────────────────────
# State management
# ─────────────────────────────────────────────────────────

def _load_state() -> Dict[str, Any]:
    if not ORCHESTRATOR_STATE.exists():
        return {"last_daily": None, "last_weekly": None, "last_monthly": None}
    try:
        return json.load(open(ORCHESTRATOR_STATE))
    except Exception:
        return {"last_daily": None, "last_weekly": None, "last_monthly": None}


def _save_state(state: Dict[str, Any]) -> None:
    ORCHESTRATOR_STATE.parent.mkdir(parents=True, exist_ok=True)
    with open(ORCHESTRATOR_STATE, "w") as f:
        json.dump(state, f, indent=2)


def _is_due(last_run_iso: Optional[str], days_between: int) -> bool:
    if not last_run_iso:
        return True
    try:
        last = datetime.fromisoformat(last_run_iso)
        return datetime.now() - last >= timedelta(days=days_between)
    except Exception:
        return True


# ─────────────────────────────────────────────────────────
# Ground truth scoping
# ─────────────────────────────────────────────────────────

def load_grounded_skills() -> set:
    """Skills/components that have ground-truth benchmarks — eligible for auto-evolution.

    Apex W0.3 (2026-07-29): DERIVED from two sources, filtered to skills that
    exist on disk — never hand-synced. The old manifest-only read meant the
    2026-07-24 calibration ratification (18 skills, human-calibrated eval rows)
    never reached this gate: the phase2 queue sat 100% blocked at "no ground
    truth" while the ground truth existed one file away. 3 of the manifest's 5
    entries were also phantom dirs; the existence filter retires them silently.
    """
    grounded = set()
    skills_root = ROOT / "skills"

    def _add(name: str) -> None:
        name = (name or "").strip().removeprefix("skills/")
        if name and name not in ("n/a", "TBD") and (skills_root / name).is_dir():
            grounded.add(name)

    try:
        if GROUND_TRUTH_MANIFEST.exists():
            manifest = json.load(open(GROUND_TRUTH_MANIFEST))
            for sample in manifest.get("samples", []):
                _add(sample.get("skill", ""))
    except Exception:
        pass
    try:
        eval_set = GROUND_TRUTH_MANIFEST.parent / "eval_set_v1.jsonl"
        if eval_set.exists():
            for line in eval_set.read_text().splitlines():
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                except ValueError:
                    continue
                if row.get("calibrated_by_human"):
                    _add(row.get("domain", ""))
                    _add(row.get("skill", ""))
    except Exception:
        pass
    return grounded


# ─────────────────────────────────────────────────────────
# Routing-learning cycle (Wave 3, 2026-07)
# ─────────────────────────────────────────────────────────

def _load_skill_weights() -> Dict[str, float]:
    if not SKILL_WEIGHTS_PATH.exists():
        return {}
    try:
        return json.load(open(SKILL_WEIGHTS_PATH))
    except Exception:
        return {}


def _save_skill_weights(weights: Dict[str, float]) -> None:
    SKILL_WEIGHTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(SKILL_WEIGHTS_PATH, "w") as f:
        json.dump(weights, f, indent=2, sort_keys=True)


def _clamp_weight(w: float) -> float:
    return max(WEIGHT_MIN, min(WEIGHT_MAX, w))


def run_routing_learning() -> Dict[str, Any]:
    """Nightly MoE-style weight nudge.

    Reads the suggest->load->outcome feedback that skill_router_hook.py logs
    (routing_decisions) and execution/hooks/session_ledger_hook.py logs
    (feedback_log: auto_match/auto_miss, keyed by routing_id, with
    `correction` always carrying the expert skill that actually loaded) from
    .agent/routing-intelligence.json, plus qualifying-workflow misses from
    evolution_store/sub_agent_misses.jsonl. Computes per-skill weight
    nudges and writes them to .agent/skill-weights.json — a file SEPARATE
    from the skill index (.agent/skill-index.json) on purpose, so any
    SKILL.md edit that triggers an index rebuild never clobbers what's been
    learned. find_skill.rank() applies these as a multiplier at query time.

    Direction of the nudge:
      - auto_match: the suggested skill was the one that actually loaded ->
        +WEIGHT_NUDGE (reinforce — it was correctly ranked).
      - auto_miss: the skill that actually loaded was NOT among the
        suggestions -> +WEIGHT_NUDGE for that skill (it was under-ranked and
        deserved to surface), -WEIGHT_NUDGE for each skill that WAS
        suggested but wrong (over-ranked for that query).
    All weights decay toward 1.0 by WEIGHT_DECAY first, so an un-reinforced
    nudge relaxes over time rather than accumulating forever. Clamped to
    [WEIGHT_MIN, WEIGHT_MAX].

    Wave 1 (Harness Apex, 2026-07-07) adds a QUALITY signal alongside the
    followed/not-followed signal: chain_runner finalize composites from
    evolution_store/v2_traces nudge the finalized skill up (>=8) or down
    (<7) at the same WEIGHT_NUDGE magnitude, cursor-tracked so each
    finalize counts exactly once (.agent/routing-quality-cursor.json).

    NEVER touches execution/find_skill.py's SYNONYMS map or the skill index
    — those stay human-owned. Recent sub_agent_misses.jsonl entries with a
    `skill` field are instead appended as human-readable candidates to
    .agent/synonym-candidates.md for manual review.
    """
    result: Dict[str, Any] = {"cycle": "routing_learning", "nudged": {}, "candidates_appended": 0}

    try:
        intel = json.loads(ROUTING_INTEL_PATH.read_text()) if ROUTING_INTEL_PATH.exists() else {}
    except Exception:
        intel = {}
    decisions = {d.get("routing_id"): d for d in intel.get("routing_decisions", [])}
    feedback = intel.get("feedback_log", [])

    weights = _load_skill_weights()

    # Decay toward 1.0 first so unrewarded weights relax over time.
    for skill, w in list(weights.items()):
        try:
            w = float(w)
        except Exception:
            weights[skill] = 1.0
            continue
        if w > 1.0:
            weights[skill] = _clamp_weight(max(1.0, w - WEIGHT_DECAY))
        elif w < 1.0:
            weights[skill] = _clamp_weight(min(1.0, w + WEIGHT_DECAY))

    def _nudge(skill: str, delta: float) -> None:
        if not skill:
            return
        weights[skill] = _clamp_weight(weights.get(skill, 1.0) + delta)
        result["nudged"][skill] = round(weights[skill], 3)

    for fb in feedback:
        rating = fb.get("rating")
        if rating not in ("auto_match", "auto_miss"):
            continue
        rd = decisions.get(fb.get("routing_id"), {})
        loaded_skill = fb.get("correction") or ""
        suggested = rd.get("experts_deployed", []) or []
        if rating == "auto_match":
            _nudge(loaded_skill, WEIGHT_NUDGE)
        else:  # auto_miss
            _nudge(loaded_skill, WEIGHT_NUDGE)  # under-ranked, deserved better
            for s in suggested:
                if s and s != loaded_skill:
                    _nudge(s, -WEIGHT_NUDGE)     # over-ranked for this query

    # ── Quality→routing loop (Wave 1, Harness Apex 2026-07-07) ──────────
    # Until now the loop only learned "was the suggestion followed"
    # (auto_match/auto_miss) — never "did it work." chain_runner finalize
    # already writes a per-route local record (evolution_store/v2_traces,
    # operation=chain_finalize, component=skill dir, quality.composite).
    # Fold it in: composite >=8 nudges the skill up, <7 nudges it down —
    # same WEIGHT_NUDGE magnitude, same [WEIGHT_MIN, WEIGHT_MAX] clamp.
    # A cursor (.agent/routing-quality-cursor.json) guarantees each finalize
    # is counted exactly once; only components that are real skills/ dirs
    # feed weights (task_type fallbacks like "Content" are skipped).
    quality_counted = 0
    try:
        cursor = ""
        try:
            cursor = json.loads(QUALITY_CURSOR_PATH.read_text()).get("last_trace_id", "")
        except Exception:
            cursor = ""
        if not cursor:
            # First run: seed one week back so history doesn't stampede weights.
            cursor = (datetime.now() - timedelta(days=WEEKLY_DAYS)).strftime("%Y%m%d_%H%M%S")
        max_seen = cursor
        for tf in sorted(TRACE_DIR.glob("trace_*.json")):
            trace_id = tf.stem[len("trace_"):len("trace_") + 15]  # YYYYMMDD_HHMMSS
            if trace_id <= cursor:
                continue
            try:
                trace = json.loads(tf.read_text())
            except Exception:
                continue
            if trace_id > max_seen:
                max_seen = trace_id
            if trace.get("operation") != "chain_finalize":
                continue
            skill = (trace.get("component") or "").strip()
            if not skill or not (ROOT / "skills" / skill).is_dir():
                continue
            try:
                composite = float((trace.get("quality") or {}).get("composite", 0.0))
            except Exception:
                continue
            if composite >= 8.0:
                _nudge(skill, WEIGHT_NUDGE)
                quality_counted += 1
            elif 0.0 < composite < LOW_SCORE_THRESHOLD:
                _nudge(skill, -WEIGHT_NUDGE)
                quality_counted += 1
        QUALITY_CURSOR_PATH.parent.mkdir(parents=True, exist_ok=True)
        QUALITY_CURSOR_PATH.write_text(json.dumps({"last_trace_id": max_seen}, indent=2))
    except Exception as e:
        result["quality_loop_error"] = str(e)
    result["quality_finalizes_counted"] = quality_counted

    try:
        _save_skill_weights(weights)
    except Exception as e:
        result["weights_write_error"] = str(e)

    # Synonym candidates — human-review queue only, never auto-applied.
    candidates_appended = 0
    try:
        if SUB_AGENT_MISSES.exists():
            recent_cutoff = datetime.now() - timedelta(days=1)
            new_lines = []
            with open(SUB_AGENT_MISSES) as f:
                for line in f:
                    try:
                        m = json.loads(line)
                    except Exception:
                        continue
                    ts = m.get("timestamp", "")
                    try:
                        if datetime.fromisoformat(ts) < recent_cutoff:
                            continue
                    except Exception:
                        continue
                    skill = m.get("skill") or m.get("expert") or ""
                    workflow = m.get("workflow", "")
                    if not skill:
                        continue
                    new_lines.append(f"- `{workflow}` -> `{skill}` (manual load, {ts})")
            if new_lines:
                if not SYNONYM_CANDIDATES_PATH.exists():
                    SYNONYM_CANDIDATES_PATH.parent.mkdir(parents=True, exist_ok=True)
                    SYNONYM_CANDIDATES_PATH.write_text(
                        "# Synonym Candidates\n\n"
                        "Human-review queue only. evolution_orchestrator.run_routing_learning() "
                        "appends candidate query-term -> skill pairs here from workflows that ran "
                        "with zero measured sub-agent spawns (evolution_store/sub_agent_misses.jsonl). "
                        "NEVER auto-applied to execution/find_skill.py's SYNONYMS map — a human "
                        "decides whether the phrasing generalizes before adding it.\n"
                    )
                with open(SYNONYM_CANDIDATES_PATH, "a") as f:
                    f.write(f"\n## {date.today().isoformat()}\n\n" + "\n".join(new_lines) + "\n")
                candidates_appended = len(new_lines)
    except Exception as e:
        result["candidates_error"] = str(e)
    result["candidates_appended"] = candidates_appended

    # Cheap deterministic backstop (Wave 4, 2026-07-06): if the weekly cycle
    # missed its slot (same sleep/StartCalendarInterval failure mode fixed
    # for the daily cycle above), refresh the standalone router report card
    # here anyway so it's never silently stale for more than a day past due.
    try:
        result["router_report_card_backstop"] = write_router_report_card(force=False)
    except Exception as e:
        result["router_report_card_error"] = str(e)

    return result


# ─────────────────────────────────────────────────────────
# Router Report Card (Wave 4, 2026-07-06)
#
# A ~one-page weekly glance at the router learning loop Wave 3 wired up
# (skill_router_hook -> .agent/routing-intelligence.json ->
# session_ledger_hook auto_match/auto_miss reconciliation ->
# run_routing_learning() weight nudges + synonym candidates). Farrice's
# stated #1 concern is the loop going dark silently, so section (e) below
# exists purely as a canary: it checks whether ANY routing decision landed
# in the trailing window, independent of whether there's enough reconciled
# feedback yet to trend a match rate.
# ─────────────────────────────────────────────────────────

ROUTER_REPORT_CARD_PATH = ROOT / ".agent" / "router-report-card.md"
GAP_LOG_PATH = ROOT / ".agent" / "gap-log.md"
ROUTER_MIN_DECISIONS_TO_TREND = 5   # below this, report the raw split, not a headline %


def _naive_ts(ts: str) -> Optional[datetime]:
    """Parse an ISO timestamp and strip tzinfo so it compares against the naive
    datetime.now() used everywhere else in this module. routing-intelligence.json
    timestamps are tz-aware (+00:00); evolution_store trace timestamps are not —
    this normalizes both."""
    if not ts:
        return None
    try:
        t = datetime.fromisoformat(ts)
        return t.replace(tzinfo=None) if t.tzinfo else t
    except Exception:
        return None


def _gap_log_counts(days: int) -> Dict[str, Any]:
    """Count gap-log entries. Section headers follow `## YYYY-MM-DD — slug`.
    If every section is dated, count is windowed to the last `days`; if any
    section lacks a parseable date, falls back to the total count rather than
    silently undercounting."""
    if not GAP_LOG_PATH.exists():
        return {"total": 0, "windowed": 0, "all_dated": True}
    text = GAP_LOG_PATH.read_text()
    total_sections = len(re.findall(r"^## ", text, flags=re.MULTILINE))
    dated = re.findall(r"^## (\d{4}-\d{2}-\d{2})", text, flags=re.MULTILINE)
    if total_sections == 0 or len(dated) < total_sections:
        return {"total": total_sections, "windowed": total_sections, "all_dated": False}
    cutoff = date.today() - timedelta(days=days)
    windowed = sum(1 for d in dated if date.fromisoformat(d) >= cutoff)
    return {"total": len(dated), "windowed": windowed, "all_dated": True}


def _synonym_candidate_count() -> int:
    """Each pending candidate is a `- \\`workflow\\` -> \\`skill\\`` bullet line."""
    if not SYNONYM_CANDIDATES_PATH.exists():
        return 0
    text = SYNONYM_CANDIDATES_PATH.read_text()
    return len(re.findall(r"^- `", text, flags=re.MULTILINE))


def build_router_report_card() -> str:
    """Build the one-page router report card as a markdown string (no I/O)."""
    now = datetime.now()
    generated = now.strftime("%Y-%m-%d %H:%M")
    cutoff = now - timedelta(days=WEEKLY_DAYS)

    try:
        intel = json.loads(ROUTING_INTEL_PATH.read_text()) if ROUTING_INTEL_PATH.exists() else {}
    except Exception:
        intel = {}
    routing_decisions = intel.get("routing_decisions", [])
    feedback_log = intel.get("feedback_log", [])

    recent_decisions = [r for r in routing_decisions if (_naive_ts(r.get("timestamp", "")) or datetime.min) >= cutoff]
    recent_feedback = [f for f in feedback_log if (_naive_ts(f.get("timestamp", "")) or datetime.min) >= cutoff]

    auto_match = sum(1 for f in recent_feedback if f.get("rating") == "auto_match")
    auto_miss = sum(1 for f in recent_feedback if f.get("rating") == "auto_miss")
    total_rated = auto_match + auto_miss

    lines = [
        f"# Router Report Card — {generated}",
        "",
        "Weekly glance at the router learning loop: "
        "`skill_router_hook` (suggest) -> `routing-intelligence.json` (log) -> "
        "`session_ledger_hook` (reconcile auto_match/auto_miss) -> "
        "`run_routing_learning()` (nudge weights + surface synonym candidates).",
        "",
        f"## (a) Suggested-vs-Loaded Match Rate ({WEEKLY_DAYS}d)",
    ]
    if total_rated == 0:
        lines.append(f"- 0 reconciled decisions in the last {WEEKLY_DAYS}d — too early to trend.")
    elif total_rated < ROUTER_MIN_DECISIONS_TO_TREND:
        rate = round(100 * auto_match / total_rated, 1)
        lines.append(
            f"- {total_rated} decision(s) reconciled — too early to trend confidently "
            f"(auto_match {auto_match} / auto_miss {auto_miss}, {rate}% match)."
        )
    else:
        rate = round(100 * auto_match / total_rated, 1)
        lines.append(
            f"- {total_rated} decisions reconciled: **{rate}% match rate** "
            f"(auto_match {auto_match}, auto_miss {auto_miss})."
        )

    lines += ["", "## (b) Skill Weight Movers (vs 1.0 baseline)"]
    weights = _load_skill_weights()
    if not SKILL_WEIGHTS_PATH.exists() or not weights:
        lines.append("- (no `.agent/skill-weights.json` yet — no weight nudges recorded)")
    else:
        ranked_desc = sorted(weights.items(), key=lambda kv: kv[1], reverse=True)
        ranked_asc = sorted(weights.items(), key=lambda kv: kv[1])
        gainers = [(s, w) for s, w in ranked_desc if w > 1.0][:5]
        losers = [(s, w) for s, w in ranked_asc if w < 1.0][:5]
        lines.append("**Top gainers:**")
        if gainers:
            for s, w in gainers:
                lines.append(f"- `{s}` -> {round(w, 3)} ({round(w - 1.0, 3):+})")
        else:
            lines.append("- (none above baseline)")
        lines.append("")
        lines.append("**Top losers:**")
        if losers:
            for s, w in losers:
                lines.append(f"- `{s}` -> {round(w, 3)} ({round(w - 1.0, 3):+})")
        else:
            lines.append("- (none below baseline)")

    lines += ["", "## (c) Abstention / Gap Count"]
    gap = _gap_log_counts(WEEKLY_DAYS)
    if gap["total"] == 0:
        lines.append("- 0 gaps on record.")
    elif gap["all_dated"]:
        lines.append(f"- {gap['windowed']} gap(s) logged in the last {WEEKLY_DAYS}d ({gap['total']} total on record).")
    else:
        lines.append(f"- {gap['total']} gap(s) on record (not all entries dated — showing total, not a {WEEKLY_DAYS}d window).")

    lines += ["", "## (d) Pending Synonym Candidates"]
    candidate_count = _synonym_candidate_count()
    lines.append(f"- {candidate_count} candidate(s) awaiting human review -> `.agent/synonym-candidates.md`")

    lines += ["", "## (e) Health Check — Is the Loop Alive?"]
    if len(recent_decisions) == 0:
        lines.append(
            f"- **WARNING: 0 routing decisions logged in the last {WEEKLY_DAYS}d.** "
            "The suggest->load->outcome loop may be dark — check `skill_router_hook.py` wiring "
            "and `.agent/routing-intelligence.json` writes."
        )
    else:
        lines.append(f"- {len(recent_decisions)} routing decision(s) logged in the last {WEEKLY_DAYS}d — loop is live.")

    return "\n".join(lines) + "\n"


def write_router_report_card(force: bool = False) -> Dict[str, Any]:
    """Write the standalone .agent/router-report-card.md.

    force=True (weekly cycle): always regenerate — this is the authoritative
    weekly refresh.
    force=False (daily cheap-mode backstop, called from run_routing_learning):
    only regenerate if the file is missing or older than one WEEKLY_DAYS
    window, so a missed weekly run doesn't leave Farrice staring at a stale
    card — mirrors the CATCHUP_STALE_HOURS philosophy already applied to the
    daily cycle in run_auto().
    """
    if not force and ROUTER_REPORT_CARD_PATH.exists():
        try:
            age_hours = (
                datetime.now() - datetime.fromtimestamp(ROUTER_REPORT_CARD_PATH.stat().st_mtime)
            ).total_seconds() / 3600.0
            if age_hours < WEEKLY_DAYS * 24:
                return {"written": False, "reason": "fresh", "age_hours": round(age_hours, 1)}
        except Exception:
            pass
    card = build_router_report_card()
    ROUTER_REPORT_CARD_PATH.parent.mkdir(parents=True, exist_ok=True)
    ROUTER_REPORT_CARD_PATH.write_text(card)
    return {"written": True, "path": str(ROUTER_REPORT_CARD_PATH)}


# ─────────────────────────────────────────────────────────
# Trace ingestion
# ─────────────────────────────────────────────────────────

def load_traces(days: int) -> List[Dict[str, Any]]:
    """Load v2 trace files modified within the window."""
    if not TRACE_DIR.exists():
        return []
    cutoff = datetime.now() - timedelta(days=days)
    traces = []
    for tf in TRACE_DIR.glob("trace_*.json"):
        try:
            mtime = datetime.fromtimestamp(tf.stat().st_mtime)
            if mtime < cutoff:
                continue
            with open(tf) as f:
                traces.append(json.load(f))
        except Exception:
            continue
    return traces


def load_routing_decisions(days: int) -> List[Dict[str, Any]]:
    if not ROUTING_LOG.exists():
        return []
    cutoff = datetime.now() - timedelta(days=days)
    out = []
    with open(ROUTING_LOG) as f:
        for line in f:
            try:
                e = json.loads(line)
                ts = datetime.fromisoformat(e["timestamp"])
                if ts >= cutoff:
                    out.append(e)
            except Exception:
                continue
    return out


# ─────────────────────────────────────────────────────────
# Per-skill aggregation
# ─────────────────────────────────────────────────────────

def aggregate_skill_metrics(traces: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Per-skill: count, mean composite, low_count, last_score, trend hint."""
    bucket: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for t in traces:
        skill = t.get("component") or t.get("skill") or t.get("expert") or ""
        if not skill:
            continue
        q = t.get("quality") or {}
        comp = q.get("composite")
        if comp is None:
            continue
        ts = t.get("timestamp")
        bucket[skill].append({"composite": float(comp), "timestamp": ts})

    metrics = {}
    for skill, entries in bucket.items():
        entries_sorted = sorted(entries, key=lambda x: x.get("timestamp") or "")
        scores = [e["composite"] for e in entries_sorted]
        low_count = sum(1 for s in scores if s < LOW_SCORE_THRESHOLD)
        # Simple trend: compare first half avg vs second half avg
        if len(scores) >= 4:
            mid = len(scores) // 2
            first_avg = sum(scores[:mid]) / mid
            second_avg = sum(scores[mid:]) / (len(scores) - mid)
            delta = round(second_avg - first_avg, 2)
            trend = "improving" if delta > 0.3 else "degrading" if delta < -0.3 else "stable"
        else:
            trend = "insufficient_data"
            delta = 0.0
        metrics[skill] = {
            "count": len(scores),
            "mean": round(sum(scores) / len(scores), 2),
            "min": min(scores),
            "max": max(scores),
            "low_count": low_count,
            "last_score": scores[-1],
            "trend": trend,
            "trend_delta": delta,
        }
    return metrics


# ─────────────────────────────────────────────────────────
# Queue writers
# ─────────────────────────────────────────────────────────

def _append_jsonl(path: Path, entry: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(entry) + "\n")


def queue_phase2(skill: str, metrics: Dict[str, Any], reason: str, grounded: bool) -> None:
    # Dedupe (2026-07-24, phase-2 card #1 finding): the daily cycle re-queued
    # the same low-score signal every day (oren: 2 scores -> 15 rows), which
    # inflates the consumer's queue-pressure ranking. One row per skill per 7d.
    try:
        cutoff = (datetime.now() - timedelta(days=7)).isoformat()
        if PHASE2_QUEUE.exists():
            for line in PHASE2_QUEUE.read_text().splitlines():
                if not line.strip():
                    continue
                row = json.loads(line)
                if row.get("skill") == skill and row.get("queued_at", "") >= cutoff:
                    return
    except Exception:
        pass
    _append_jsonl(PHASE2_QUEUE, {
        "queued_at": datetime.now().isoformat(),
        "skill": skill,
        "reason": reason,
        "metrics": metrics,
        "auto_evolve_eligible": grounded,
        "action": ("queue_for_skill_evolution_run" if grounded
                   else "human_review_required_no_ground_truth"),
    })


def queue_binding_review(binding_id: str, violations: List[Dict[str, Any]]) -> None:
    _append_jsonl(BINDING_QUEUE, {
        "queued_at": datetime.now().isoformat(),
        "binding": binding_id,
        "violation_count": len(violations),
        "sample_violations": violations[:5],
        "action": "review_routing_enforcer.BINDINGS_for_this_id",
    })


# ─────────────────────────────────────────────────────────
# Daily cycle
# ─────────────────────────────────────────────────────────

def run_daily() -> Dict[str, Any]:
    """Read traces + routing logs from last 24h, queue actions, write report."""
    traces = load_traces(days=1)
    routing = load_routing_decisions(days=1)
    grounded = load_grounded_skills()

    # Skill metrics — but use 7-day window for the low-count trigger
    week_traces = load_traces(days=7)
    week_metrics = aggregate_skill_metrics(week_traces)

    queued_phase2 = []
    for skill, m in week_metrics.items():
        if m["low_count"] >= LOW_SCORE_COUNT_TRIGGER:
            is_grounded = skill in grounded
            queue_phase2(skill, m, reason=f"{m['low_count']} scores <{LOW_SCORE_THRESHOLD} in 7d", grounded=is_grounded)
            queued_phase2.append({"skill": skill, "metrics": m, "grounded": is_grounded})

    # Routing violations — group by binding
    violation_buckets: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for r in routing:
        if not r.get("valid"):
            bid = r.get("binding_matched") or "unknown"
            violation_buckets[bid].append(r)

    queued_bindings = []
    for bid, vs in violation_buckets.items():
        if len(vs) >= ROUTING_VIOLATION_TRIGGER:
            queue_binding_review(bid, vs)
            queued_bindings.append({"binding": bid, "count": len(vs)})

    # Daily report
    today = date.today().isoformat()
    report_path = DAILY_REPORT_DIR / f"daily_evolution_{today}.md"
    DAILY_REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_lines = [
        f"# Daily Evolution Report — {today}",
        "",
        f"**Traces (24h)**: {len(traces)} | **Routing decisions (24h)**: {len(routing)}",
        f"**Grounded skills (eligible for auto-evolution)**: {len(grounded)}",
        "",
        "## Phase 2 Queue (skills with ≥2 scores <7 in 7d)",
    ]
    if queued_phase2:
        for item in queued_phase2:
            tag = "AUTO-EVOLVE" if item["grounded"] else "HUMAN REVIEW (no ground truth)"
            report_lines.append(
                f"- `{item['skill']}` — mean {item['metrics']['mean']}, "
                f"low_count {item['metrics']['low_count']}, trend {item['metrics']['trend']} "
                f"→ **{tag}**"
            )
    else:
        report_lines.append("- (none)")

    report_lines += ["", "## Routing Violations (binding-grouped, 24h)"]
    if queued_bindings:
        for item in queued_bindings:
            report_lines.append(f"- `{item['binding']}` — {item['count']} violations → **REVIEW BINDINGS**")
    else:
        report_lines.append("- (none)")

    report_lines += [
        "",
        "## Skills observed (24h)",
        "",
        "| Skill | Count | Mean | Trend |",
        "|---|---|---|---|",
    ]
    today_metrics = aggregate_skill_metrics(traces)
    for skill in sorted(today_metrics.keys()):
        m = today_metrics[skill]
        report_lines.append(f"| {skill} | {m['count']} | {m['mean']} | {m['trend']} ({m['trend_delta']:+}) |")

    # Platform constitution drift (observe-only — must never break evolution)
    try:
        import subprocess
        proc = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parent / "platform_compiler.py"), "check", "--json"],
            capture_output=True, text=True, timeout=30,
        )
        platform_drift = json.loads(proc.stdout or "{}")
    except Exception as exc:
        platform_drift = {"drifted": [], "error": str(exc)}

    report_lines += ["", "## Platform Constitution Drift"]
    if platform_drift.get("drifted"):
        for f in platform_drift["drifted"]:
            report_lines.append(
                f"- `{f}` changed since last bless — review siblings, then `python3 execution/platform_compiler.py sync`"
            )
    elif platform_drift.get("error"):
        report_lines.append(f"- (check unavailable: {platform_drift['error']})")
    else:
        report_lines.append("- (in sync)")

    # Portability + surface-budget lint (observe-only — must never break evolution).
    # Covers the 2026-06-12 additions: core-roster surface budget, roster
    # integrity, plus all pre-existing portability invariants.
    try:
        import subprocess
        proc = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parent / "platform_compiler.py"), "lint", "--json"],
            capture_output=True, text=True, timeout=60,
        )
        lint_result = json.loads(proc.stdout or "{}")
    except Exception as exc:
        lint_result = {"failures": [], "error": str(exc)}

    report_lines += ["", "## Portability & Surface Lint"]
    if lint_result.get("failures"):
        for f in lint_result["failures"]:
            report_lines.append(f"- {f}")
    elif lint_result.get("error"):
        report_lines.append(f"- (lint unavailable: {lint_result['error']})")
    else:
        report_lines.append("- (clean)")

    # Constitution-core compile drift (Wave 2, 2026-07-06) — observe-only: never
    # mutates constitutions in the daily run, just reports whether the marked
    # passages in CLAUDE.md/GEMINI.md/AGENTS.md still match
    # directives/constitution-core/. Human runs `compile --write` to reconcile.
    try:
        import subprocess
        proc = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parent / "platform_compiler.py"), "compile", "--check"],
            capture_output=True, text=True, timeout=30,
        )
        compile_ok = proc.returncode == 0
        compile_output = (proc.stdout or proc.stderr or "").strip()
    except Exception as exc:
        compile_ok = None
        compile_output = str(exc)

    report_lines += ["", "## Constitution Compile Drift (observe-only)"]
    if compile_ok is None:
        report_lines.append(f"- (compile check unavailable: {compile_output})")
    elif compile_ok:
        report_lines.append("- (in sync — marked blocks match directives/constitution-core/)")
    else:
        report_lines.append(f"- DIVERGENT — review, then `python3 execution/platform_compiler.py compile --write`: {compile_output}")

    # Routing-learning pass (Wave 3, 2026-07) — observe-only-safe: a failure
    # here must never break the rest of the daily cycle.
    try:
        routing_learning = run_routing_learning()
    except Exception as exc:
        routing_learning = {"cycle": "routing_learning", "error": str(exc), "nudged": {}, "candidates_appended": 0}

    report_lines += ["", "## Routing Learning (skill-weight nudges)"]
    if routing_learning.get("error"):
        report_lines.append(f"- (routing-learning unavailable: {routing_learning['error']})")
    elif routing_learning.get("nudged"):
        for skill, w in sorted(routing_learning["nudged"].items()):
            report_lines.append(f"- `{skill}` -> weight {w}")
    else:
        report_lines.append("- (no feedback to learn from yet)")
    if routing_learning.get("candidates_appended"):
        report_lines.append(
            f"- {routing_learning['candidates_appended']} synonym candidate(s) appended to "
            ".agent/synonym-candidates.md for human review"
        )

    # Candidate-snapshot refresh (2026-07-21 verifier-fleet triage): nothing
    # else schedules `skill_evolution_candidates.py scan --write`, so the
    # freshness contract (verify_skill_evolution_candidate_freshness) went
    # stale daily. Same fail-soft rule as routing-learning: a failure here
    # must never break the rest of the daily cycle.
    try:
        _scan = subprocess.run(
            [sys.executable, str(ROOT / "execution" / "skill_evolution_candidates.py"),
             "scan", "--write"],
            capture_output=True, text=True, timeout=300, cwd=ROOT)
        report_lines += ["", "## Candidate Snapshot",
                         "- refreshed via scan --write" if _scan.returncode == 0
                         else f"- refresh FAILED (exit {_scan.returncode}): {_scan.stdout[-160:]}{_scan.stderr[-160:]}"]
    except Exception as exc:
        report_lines += ["", "## Candidate Snapshot", f"- refresh unavailable: {exc}"]

    report_path.write_text("\n".join(report_lines) + "\n")

    # Update state
    state = _load_state()
    state["last_daily"] = datetime.now().isoformat()
    _save_state(state)

    return {
        "cycle": "daily",
        "report_path": str(report_path),
        "traces_24h": len(traces),
        "routing_decisions_24h": len(routing),
        "queued_phase2": len(queued_phase2),
        "queued_binding_reviews": len(queued_bindings),
        "auto_evolve_eligible": sum(1 for q in queued_phase2 if q["grounded"]),
        "human_review_required": sum(1 for q in queued_phase2 if not q["grounded"]),
        "routing_learning": routing_learning,
    }


# ─────────────────────────────────────────────────────────
# Weekly cycle
# ─────────────────────────────────────────────────────────

def run_weekly() -> Dict[str, Any]:
    """Snapshot 7-day baselines per skill; surface trend reversals."""
    traces = load_traces(days=WEEKLY_DAYS)
    metrics = aggregate_skill_metrics(traces)

    # Router Report Card (Wave 4, 2026-07-06) — appended into the same
    # dated snapshot file the weekly cycle already produces (there is no
    # separate weekly markdown report to match), plus a standalone,
    # always-overwritten .agent/router-report-card.md so there's one
    # stable path Farrice can glance at without hunting a dated filename.
    try:
        router_card = build_router_report_card()
        card_write = write_router_report_card(force=True)
    except Exception as e:
        router_card = f"# Router Report Card\n\n- (generation failed: {e})\n"
        card_write = {"written": False, "error": str(e)}

    today = date.today().isoformat()
    snapshot_path = DAILY_REPORT_DIR / f"weekly_baseline_{today}.json"
    DAILY_REPORT_DIR.mkdir(parents=True, exist_ok=True)
    snapshot_path.write_text(json.dumps({
        "snapshot_date": today,
        "window_days": WEEKLY_DAYS,
        "metrics": metrics,
        "router_report_card": router_card,
    }, indent=2))

    degrading = [s for s, m in metrics.items() if m["trend"] == "degrading"]
    improving = [s for s, m in metrics.items() if m["trend"] == "improving"]

    state = _load_state()
    state["last_weekly"] = datetime.now().isoformat()
    _save_state(state)

    return {
        "cycle": "weekly",
        "snapshot_path": str(snapshot_path),
        "skills_tracked": len(metrics),
        "degrading_count": len(degrading),
        "degrading_skills": degrading[:10],
        "improving_count": len(improving),
        "improving_skills": improving[:10],
        "router_report_card_path": card_write.get("path", str(ROUTER_REPORT_CARD_PATH)),
    }


# ─────────────────────────────────────────────────────────
# Monthly cycle (Phase 4 — gap analysis)
# ─────────────────────────────────────────────────────────

def run_monthly() -> Dict[str, Any]:
    """Run Phase 4 gap analysis if available."""
    result = {"cycle": "monthly"}
    try:
        sys.path.insert(0, str(ROOT / "execution"))
        # Local import — gap_analysis exists per the existing execution/ layer
        try:
            from gap_analysis import run_gap_analysis  # type: ignore
            gap = run_gap_analysis()
            result["gap_analysis"] = gap if isinstance(gap, dict) else {"raw": str(gap)[:500]}
            result["status"] = "ok"
        except ImportError:
            result["status"] = "gap_analysis_unavailable"
        except Exception as e:
            result["status"] = "gap_analysis_error"
            result["error"] = str(e)
    except Exception as e:
        result["status"] = "import_error"
        result["error"] = str(e)

    # Phase-2 consumer (loop-repair #4, Farrice all-12 GO 2026-07-24): the
    # queue's fix-arm. One card per monthly cycle, top candidate by queue
    # pressure; auto_evolve_eligible rows run headless (T1), everything else
    # parks for Farrice (T2) — human-optional review is a standing refusal.
    try:
        result["phase2_card"] = _emit_phase2_card()
    except Exception as e:
        result["phase2_card"] = {"status": "error", "error": str(e)}

    state = _load_state()
    state["last_monthly"] = datetime.now().isoformat()
    _save_state(state)

    return result


def _emit_phase2_card() -> Dict[str, Any]:
    """Emit ONE mission card for the highest-pressure phase2_queue skill.
    Skips if a phase2 card is already pending/parked (never stack cards)."""
    queue_dir = ROOT / ".agent" / "mission-queue"
    for sub in ("pending", "parked"):
        if list((queue_dir / sub).glob("card-phase2-*.md")):
            return {"status": "skipped", "reason": f"phase2 card already in {sub}/"}
    # One card per monthly cycle also means: a card COMPLETED recently blocks
    # re-emission (done/ counts for 21d) — without this, finishing a card
    # same-day would let a second one fire outside the monthly cadence.
    import time as _time
    for done_card in (queue_dir / "done").glob("card-phase2-*.md"):
        if (_time.time() - done_card.stat().st_mtime) < 21 * 86400:
            return {"status": "skipped", "reason": f"{done_card.name} completed <21d ago"}
    if not PHASE2_QUEUE.exists():
        return {"status": "skipped", "reason": "no queue"}
    rows = [json.loads(l) for l in PHASE2_QUEUE.read_text().splitlines() if l.strip()]
    if not rows:
        return {"status": "skipped", "reason": "queue empty"}
    by_skill: Dict[str, list] = {}
    for r in rows:
        by_skill.setdefault(r.get("skill", "?"), []).append(r)
    # Pressure = auto-eligible first, then most-queued, then most recent.
    def pressure(item):
        skill, rs = item
        return (any(r.get("auto_evolve_eligible") for r in rs), len(rs),
                max(r.get("queued_at", "") for r in rs))
    skill, rs = max(by_skill.items(), key=pressure)
    auto_ok = any(r.get("auto_evolve_eligible") for r in rs)
    tier = "T1" if auto_ok else "T2"
    latest = max(rs, key=lambda r: r.get("queued_at", ""))
    today = date.today().isoformat()
    card = queue_dir / "pending" / f"card-phase2-{today}.md"
    card.parent.mkdir(parents=True, exist_ok=True)
    card.write_text(f"""# Mission Card — Phase-2 skill evolution: {skill} ({today})
Tier: {tier}
Produced: {today} (evolution_orchestrator monthly Phase-2 consumer — loop-repair #4)

## Objective
Run `/skill-evolution` on `{skill}` — queued {len(rs)}x in phase2_queue
(latest reason: {latest.get('reason', '?')}; metrics: {json.dumps(latest.get('metrics', {}))[:200]}).
Ratchet semantics are BINDING: keep the edit only on measured score improvement,
revert on regression (alex-suzuki precedent, commit dcc8f69d7). On completion,
remove this skill's rows from `evolution_store/queue/phase2_queue.jsonl`.
{"" if auto_ok else "Human review required (not grounded) — Farrice runs or nods this; the runner parks it."}

## Constraints
- One skill per card; never batch the queue.
- Claim `session_lock.py` before editing skill files; clean `git status` after.
- Log the outcome to the evolution trace; re-queue only on new low scores.
""")
    return {"status": "emitted", "card": card.name, "skill": skill,
            "tier": tier, "queued_count": len(rs)}


# ─────────────────────────────────────────────────────────
# Auto cycle (decides what's due)
# ─────────────────────────────────────────────────────────

def _hours_since(last_run_iso: Optional[str]) -> Optional[float]:
    if not last_run_iso:
        return None
    try:
        last = datetime.fromisoformat(last_run_iso)
        return (datetime.now() - last).total_seconds() / 3600.0
    except Exception:
        return None


def _ran_same_calendar_day(last_run_iso: Optional[str]) -> bool:
    if not last_run_iso:
        return False
    try:
        return datetime.fromisoformat(last_run_iso).date() == date.today()
    except Exception:
        return False


def _skip_reason(cycle: str, last_run_iso: Optional[str], days_between: int) -> Dict[str, Any]:
    """Build a self-describing skip record instead of a bare cycle name.

    Distinguishes 'already ran earlier today, this is a second invocation
    the same day' (routine — e.g. a second same-day trigger) from 'genuinely
    not due yet' (e.g. weekly waiting mid-week) — a bare ["daily", ...] list
    with no timestamp made a healthy second-invocation skip indistinguishable
    from a failed run when read back from the log (2026-07-06 audit finding).
    """
    entry: Dict[str, Any] = {"cycle": cycle, "last_run": last_run_iso}
    if not last_run_iso:
        entry["reason"] = "never_run"
        return entry
    hours = _hours_since(last_run_iso)
    if days_between <= 1 and _ran_same_calendar_day(last_run_iso):
        entry["reason"] = "already_ran_today"
    else:
        entry["reason"] = "not_due_yet"
    if hours is not None:
        days_elapsed = hours / 24.0
        entry["days_remaining"] = max(0.0, round(days_between - days_elapsed, 2))
    return entry


def run_auto() -> Dict[str, Any]:
    """Run all due cycles based on last-run state.

    Includes catch-up handling (2026-07-06 fix): StartCalendarInterval
    launchd jobs are missed entirely when the machine is asleep at the
    scheduled minute (7 missed days observed in June 2026, no catch-up
    previously). If the daily cycle is stale by more than
    CATCHUP_STALE_HOURS by the time this runs, it fires immediately and is
    tagged catchup:true. Guarded against double-running daily twice in the
    same calendar day (e.g. a stray second invocation later the same day
    after an earlier successful run) via _ran_same_calendar_day.

    Each cycle is wrapped independently so one cycle throwing never
    prevents the others from running, from updating their own state, or
    from being reflected in this invocation's returned/printed record —
    previously an uncaught exception in one cycle meant main() never
    reached its print() call and the whole invocation vanished from the
    log with no trace.
    """
    state = _load_state()
    out: Dict[str, Any] = {"run_at": datetime.now().isoformat(), "ran": [], "skipped": []}
    errors: List[Dict[str, Any]] = []

    # --- daily ---
    last_daily = state.get("last_daily")
    if _ran_same_calendar_day(last_daily):
        out["skipped"].append(_skip_reason("daily", last_daily, 1))
    elif _is_due(last_daily, 1):
        hours = _hours_since(last_daily)
        try:
            daily_result = run_daily()
            entry: Dict[str, Any] = {"daily": daily_result}
            if hours is not None and hours >= CATCHUP_STALE_HOURS:
                entry["catchup"] = True
                entry["hours_since_last_run"] = round(hours, 1)
            out["ran"].append(entry)
        except Exception as exc:
            errors.append({"cycle": "daily", "error": str(exc)})
    else:
        out["skipped"].append(_skip_reason("daily", last_daily, 1))

    # --- weekly ---
    last_weekly = state.get("last_weekly")
    if _is_due(last_weekly, WEEKLY_DAYS):
        try:
            out["ran"].append({"weekly": run_weekly()})
        except Exception as exc:
            errors.append({"cycle": "weekly", "error": str(exc)})
    else:
        out["skipped"].append(_skip_reason("weekly", last_weekly, WEEKLY_DAYS))

    # --- monthly ---
    last_monthly = state.get("last_monthly")
    if _is_due(last_monthly, MONTHLY_DAYS):
        try:
            out["ran"].append({"monthly": run_monthly()})
        except Exception as exc:
            errors.append({"cycle": "monthly", "error": str(exc)})
    else:
        out["skipped"].append(_skip_reason("monthly", last_monthly, MONTHLY_DAYS))

    if errors:
        out["errors"] = errors

    return out


# ─────────────────────────────────────────────────────────
# Inspection commands
# ─────────────────────────────────────────────────────────

def show_status() -> Dict[str, Any]:
    state = _load_state()
    grounded = load_grounded_skills()
    return {
        "state": state,
        "grounded_skills_count": len(grounded),
        "grounded_skills": sorted(grounded),
        "thresholds": {
            "low_score_threshold": LOW_SCORE_THRESHOLD,
            "low_score_count_trigger": LOW_SCORE_COUNT_TRIGGER,
            "routing_violation_trigger": ROUTING_VIOLATION_TRIGGER,
        },
    }


def show_queues() -> Dict[str, Any]:
    out: Dict[str, Any] = {"phase2_queue": [], "binding_queue": []}
    if PHASE2_QUEUE.exists():
        with open(PHASE2_QUEUE) as f:
            out["phase2_queue"] = [json.loads(l) for l in f if l.strip()]
    if BINDING_QUEUE.exists():
        with open(BINDING_QUEUE) as f:
            out["binding_queue"] = [json.loads(l) for l in f if l.strip()]
    out["phase2_count"] = len(out["phase2_queue"])
    out["binding_count"] = len(out["binding_queue"])
    return out


def main():
    parser = argparse.ArgumentParser(description="Evolution Orchestrator — closes the Phase 1-4 loop")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("daily")
    sub.add_parser("weekly")
    sub.add_parser("monthly")
    sub.add_parser("auto", help="Run all due cycles based on state")
    sub.add_parser("status")
    sub.add_parser("queue")

    args = parser.parse_args()

    if args.command == "daily":
        print(json.dumps(run_daily(), indent=2))
    elif args.command == "weekly":
        print(json.dumps(run_weekly(), indent=2))
    elif args.command == "monthly":
        print(json.dumps(run_monthly(), indent=2))
    elif args.command == "auto":
        print(json.dumps(run_auto(), indent=2))
    elif args.command == "status":
        print(json.dumps(show_status(), indent=2))
    elif args.command == "queue":
        print(json.dumps(show_queues(), indent=2))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
