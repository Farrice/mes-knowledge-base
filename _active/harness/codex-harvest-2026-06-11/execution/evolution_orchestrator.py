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
    0 6 * * * cd "/Users/farricecain/Codex Antigravity" && /usr/bin/python3 execution/evolution_orchestrator.py auto >> .agent/evolution_orchestrator.log 2>&1
"""

import sys
import json
import argparse
import hashlib
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
CANDIDATE_SNAPSHOT = ROOT / "evolution_store" / "queue" / "skill_evolution_candidates.json"

# Thresholds (tunable)
LOW_SCORE_THRESHOLD = 7.0       # finalize composite below this counts as "low"
LOW_SCORE_COUNT_TRIGGER = 2     # how many lows in 7d trigger Phase 2 queue
ROUTING_VIOLATION_TRIGGER = 3   # violations per binding to trigger binding review
WEEKLY_DAYS = 7
MONTHLY_DAYS = 30


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
    """Skills/components that have ground-truth benchmarks — eligible for auto-evolution."""
    grounded = set()
    if not GROUND_TRUTH_MANIFEST.exists():
        return grounded
    try:
        manifest = json.load(open(GROUND_TRUTH_MANIFEST))
        for sample in manifest.get("samples", []):
            if sample.get("skill"):
                grounded.add(sample["skill"])
    except Exception:
        pass
    return grounded


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


def _stable_queue_id(*parts: str) -> str:
    payload = "|".join(str(part).strip().lower() for part in parts if str(part).strip())
    return hashlib.sha1(payload.encode("utf-8")).hexdigest()[:16]


def queue_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    ids = set()
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get("id"):
                ids.add(str(row["id"]))
    return ids


def queue_phase2(skill: str, metrics: Dict[str, Any], reason: str, grounded: bool) -> bool:
    queue_id = _stable_queue_id("phase2", skill, reason)
    if queue_id in queue_ids(PHASE2_QUEUE):
        return False
    _append_jsonl(PHASE2_QUEUE, {
        "id": queue_id,
        "queued_at": datetime.now().isoformat(),
        "skill": skill,
        "reason": reason,
        "metrics": metrics,
        "auto_evolve_eligible": grounded,
        "action": ("queue_for_skill_evolution_run" if grounded
                   else "human_review_required_no_ground_truth"),
    })
    return True


def queue_binding_review(binding_id: str, violations: List[Dict[str, Any]]) -> None:
    _append_jsonl(BINDING_QUEUE, {
        "queued_at": datetime.now().isoformat(),
        "binding": binding_id,
        "violation_count": len(violations),
        "sample_violations": violations[:5],
        "action": "review_routing_enforcer.BINDINGS_for_this_id",
    })


def scan_skill_evolution_candidates(write: bool = True) -> Dict[str, Any]:
    try:
        from skill_evolution_candidates import build_snapshot, compact_status, write_outputs  # type: ignore

        snapshot = build_snapshot()
        if write:
            write_outputs(snapshot)
        return {
            "status": "ok",
            "summary": snapshot.get("summary", {}),
            "compact": compact_status(snapshot),
            "top_recommendation": snapshot.get("top_recommendation"),
        }
    except Exception as e:
        return {"status": "error", "error": str(e), "summary": {}, "compact": "candidate scan unavailable"}


# ─────────────────────────────────────────────────────────
# Daily cycle
# ─────────────────────────────────────────────────────────

def run_daily() -> Dict[str, Any]:
    """Read traces + routing logs from last 24h, queue actions, write report."""
    traces = load_traces(days=1)
    routing = load_routing_decisions(days=1)
    grounded = load_grounded_skills()
    candidate_scan = scan_skill_evolution_candidates(write=True)

    # Skill metrics — but use 7-day window for the low-count trigger
    week_traces = load_traces(days=7)
    week_metrics = aggregate_skill_metrics(week_traces)

    queued_phase2 = []
    for skill, m in week_metrics.items():
        if m["low_count"] >= LOW_SCORE_COUNT_TRIGGER:
            is_grounded = skill in grounded
            reason = f"{m['low_count']} scores <{LOW_SCORE_THRESHOLD} in 7d"
            queued = queue_phase2(skill, m, reason=reason, grounded=is_grounded)
            queued_phase2.append({"skill": skill, "metrics": m, "grounded": is_grounded, "queued": queued})

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
        f"**Skill Evolution Candidates**: {candidate_scan.get('compact', 'unavailable')}",
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

    report_lines += ["", "## Skill Evolution Candidate Snapshot"]
    if candidate_scan.get("status") == "ok":
        top = candidate_scan.get("top_recommendation") or {}
        summary = candidate_scan.get("summary") or {}
        report_lines.append(
            f"- Ready: {summary.get('ready', 0)} | Watchlist: {summary.get('watchlist', 0)} | Blocked: {summary.get('blocked', 0)}"
        )
        if top:
            report_lines.append(
                f"- Top: `{top.get('skill')}` ({top.get('state')}) - {top.get('reason')}"
            )
        else:
            report_lines.append("- Top: none")
    else:
        report_lines.append(f"- Candidate scan failed: {candidate_scan.get('error', 'unknown error')}")

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
        "skill_evolution_candidates": candidate_scan,
    }


# ─────────────────────────────────────────────────────────
# Weekly cycle
# ─────────────────────────────────────────────────────────

def run_weekly() -> Dict[str, Any]:
    """Snapshot 7-day baselines per skill; surface trend reversals."""
    traces = load_traces(days=WEEKLY_DAYS)
    metrics = aggregate_skill_metrics(traces)

    today = date.today().isoformat()
    snapshot_path = DAILY_REPORT_DIR / f"weekly_baseline_{today}.json"
    DAILY_REPORT_DIR.mkdir(parents=True, exist_ok=True)
    snapshot_path.write_text(json.dumps({
        "snapshot_date": today,
        "window_days": WEEKLY_DAYS,
        "metrics": metrics,
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

    state = _load_state()
    state["last_monthly"] = datetime.now().isoformat()
    _save_state(state)

    return result


# ─────────────────────────────────────────────────────────
# Auto cycle (decides what's due)
# ─────────────────────────────────────────────────────────

def run_auto() -> Dict[str, Any]:
    """Run all due cycles based on last-run state."""
    state = _load_state()
    out = {"ran": [], "skipped": []}

    if _is_due(state.get("last_daily"), 1):
        out["ran"].append({"daily": run_daily()})
    else:
        out["skipped"].append("daily")

    if _is_due(state.get("last_weekly"), WEEKLY_DAYS):
        out["ran"].append({"weekly": run_weekly()})
    else:
        out["skipped"].append("weekly")

    if _is_due(state.get("last_monthly"), MONTHLY_DAYS):
        out["ran"].append({"monthly": run_monthly()})
    else:
        out["skipped"].append("monthly")

    return out


# ─────────────────────────────────────────────────────────
# Inspection commands
# ─────────────────────────────────────────────────────────

def show_status() -> Dict[str, Any]:
    state = _load_state()
    grounded = load_grounded_skills()
    candidate_scan = scan_skill_evolution_candidates(write=False)
    return {
        "state": state,
        "grounded_skills_count": len(grounded),
        "grounded_skills": sorted(grounded),
        "skill_evolution_candidates": candidate_scan,
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
    if CANDIDATE_SNAPSHOT.exists():
        try:
            out["skill_evolution_candidates"] = json.loads(CANDIDATE_SNAPSHOT.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            out["skill_evolution_candidates"] = {"error": "snapshot is not valid JSON"}
    else:
        out["skill_evolution_candidates"] = scan_skill_evolution_candidates(write=False)
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
