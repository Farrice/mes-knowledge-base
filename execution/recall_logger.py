#!/usr/bin/env python3
"""
Recall Logger — Observability for Tier 1.5 grounding decisions.

Purpose: The Recall grounding protocol is "silent skip on 6 failure modes"
(disconnected, <2 cards, low relevance, >5s timeout, --no-ground, non-grounding
domain). That silence means a core architectural feature cannot be measured —
if Recall degrades or the relevance gate is wrong, nobody knows.

This logger gives Claude one trivial CLI to call after each grounding decision
(fire OR skip), turning silent infrastructure into observable infrastructure.

Two subcommands:

    log     — Append a grounding decision to the JSONL trace.
    report  — Compute weekly correlation: does grounding correlate with higher
              Expert Standard scores in chain_runner finalize() entries?

Storage:
    evolution_store/traces/recall_grounding.jsonl

Why a separate trace file (not routing_decisions.jsonl): different schemas,
different cadence, different correlation analyses. Keep them clean.

Usage from Claude (per recall-grounding-protocol.md):

    # After firing grounding successfully
    python3 execution/recall_logger.py log \\
        --status fired --domain content --query "Lara Acosta LinkedIn hook" \\
        --cards-returned 3 --signal high --expert lara-acosta

    # After skipping (any of 6 reasons)
    python3 execution/recall_logger.py log \\
        --status skipped --reason low_signal --domain content \\
        --query "Lara Acosta LinkedIn hook" --cards-returned 1

    # On failure
    python3 execution/recall_logger.py log \\
        --status failed --reason timeout --domain content \\
        --query "Lara Acosta LinkedIn hook"
"""

import sys
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
from collections import defaultdict

TRACE_DIR = Path(__file__).parent.parent / "evolution_store" / "traces"
RECALL_LOG = TRACE_DIR / "recall_grounding.jsonl"
CHAIN_TRACE_DIR = Path(__file__).parent.parent / "evolution_store" / "v2_traces"

VALID_STATUSES = {"fired", "skipped", "failed"}
VALID_SKIP_REASONS = {
    "disconnected",       # Recall MCP unavailable
    "no_signal",          # 0 cards returned
    "low_signal",         # <2 cards or low relevance
    "timeout",            # >5s response
    "no_ground_flag",     # User invoked --no-ground
    "non_grounding_domain",  # Domain not in grounding-relevant set
    "other",              # Catch-all (must include note)
}
VALID_SIGNALS = {"high", "medium", "low", "none"}


def log_decision(
    status: str,
    domain: str = "",
    query: str = "",
    expert: str = "",
    reason: str = "",
    cards_returned: Optional[int] = None,
    signal: str = "",
    note: str = "",
    session_id: str = "",
) -> bool:
    """Append a single grounding decision to the JSONL trace. Returns True on success."""
    if status not in VALID_STATUSES:
        return False
    if status == "skipped" and reason and reason not in VALID_SKIP_REASONS:
        # Allow but flag — don't reject
        pass
    try:
        TRACE_DIR.mkdir(parents=True, exist_ok=True)
        entry = {
            "timestamp": datetime.now().isoformat(),
            "status": status,
            "domain": domain,
            "expert": expert,
            "query": query[:300],
            "reason": reason,
            "cards_returned": cards_returned,
            "signal": signal,
            "note": note,
            "session_id": session_id,
        }
        with open(RECALL_LOG, "a") as f:
            f.write(json.dumps(entry) + "\n")
        return True
    except Exception:
        return False


def _load_recent_grounding(days: int = 7) -> List[Dict[str, Any]]:
    """Load recall grounding entries from the last N days."""
    if not RECALL_LOG.exists():
        return []
    cutoff = datetime.now() - timedelta(days=days)
    entries = []
    with open(RECALL_LOG) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
                ts = datetime.fromisoformat(entry["timestamp"])
                if ts >= cutoff:
                    entries.append(entry)
            except Exception:
                continue
    return entries


def _load_recent_chain_traces(days: int = 7) -> List[Dict[str, Any]]:
    """Load chain_runner finalize traces from the last N days."""
    if not CHAIN_TRACE_DIR.exists():
        return []
    cutoff = datetime.now() - timedelta(days=days)
    traces = []
    for tf in CHAIN_TRACE_DIR.glob("trace_*.json"):
        try:
            mtime = datetime.fromtimestamp(tf.stat().st_mtime)
            if mtime < cutoff:
                continue
            with open(tf) as f:
                trace = json.load(f)
                traces.append(trace)
        except Exception:
            continue
    return traces


def correlation_report(days: int = 7) -> Dict[str, Any]:
    """
    Test the Tier 1.5 design hypothesis: does grounding correlate with
    higher Expert Standard scores?

    Approach: For each finalize trace in the window, find any Recall grounding
    decisions logged within the same hour (rough proxy for "same session").
    Compare Expert Standard scores between fired-grounding sessions and
    skipped/failed sessions.

    This is rough — proper correlation requires session_id linkage, which
    requires the protocol to thread session_id through. For now, hourly
    proximity is the cheapest signal that beats nothing.
    """
    grounding = _load_recent_grounding(days)
    traces = _load_recent_chain_traces(days)

    report: Dict[str, Any] = {
        "window_days": days,
        "grounding_total": len(grounding),
        "chain_traces_total": len(traces),
    }

    # Tally grounding outcomes
    status_counts: Dict[str, int] = defaultdict(int)
    skip_reasons: Dict[str, int] = defaultdict(int)
    domain_fires: Dict[str, int] = defaultdict(int)
    for g in grounding:
        status_counts[g["status"]] += 1
        if g["status"] == "skipped" and g.get("reason"):
            skip_reasons[g["reason"]] += 1
        if g["status"] == "fired" and g.get("domain"):
            domain_fires[g["domain"]] += 1

    report["status_breakdown"] = dict(status_counts)
    report["skip_reasons"] = dict(skip_reasons)
    report["domain_fires"] = dict(domain_fires)

    if not traces:
        report["correlation"] = "no_chain_traces"
        return report

    # Rough hourly correlation
    fired_scores: List[float] = []
    skipped_scores: List[float] = []
    no_grounding_scores: List[float] = []

    grounding_by_hour: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for g in grounding:
        try:
            hour_key = datetime.fromisoformat(g["timestamp"]).strftime("%Y-%m-%d %H")
            grounding_by_hour[hour_key].append(g)
        except Exception:
            continue

    for trace in traces:
        ts_raw = trace.get("timestamp")
        if not ts_raw:
            continue
        try:
            hour_key = datetime.fromisoformat(ts_raw).strftime("%Y-%m-%d %H")
        except Exception:
            continue
        es = trace.get("expert_score") or trace.get("expert_standard")
        if es is None:
            continue
        nearby = grounding_by_hour.get(hour_key, [])
        if any(g["status"] == "fired" for g in nearby):
            fired_scores.append(float(es))
        elif any(g["status"] in ("skipped", "failed") for g in nearby):
            skipped_scores.append(float(es))
        else:
            no_grounding_scores.append(float(es))

    def _avg(xs):
        return round(sum(xs) / len(xs), 2) if xs else None

    report["correlation"] = {
        "fired_grounding_avg_expert_standard": _avg(fired_scores),
        "fired_grounding_n": len(fired_scores),
        "skipped_grounding_avg_expert_standard": _avg(skipped_scores),
        "skipped_grounding_n": len(skipped_scores),
        "no_grounding_avg_expert_standard": _avg(no_grounding_scores),
        "no_grounding_n": len(no_grounding_scores),
    }

    if fired_scores and (skipped_scores or no_grounding_scores):
        baseline = _avg((skipped_scores or []) + (no_grounding_scores or []))
        fired_avg = _avg(fired_scores)
        if baseline and fired_avg:
            delta = round(fired_avg - baseline, 2)
            report["correlation"]["lift_vs_baseline"] = delta
            report["correlation"]["interpretation"] = (
                "POSITIVE — grounding correlates with higher Expert Standard"
                if delta > 0.3
                else "NEUTRAL — no clear lift from grounding (within noise)"
                if abs(delta) <= 0.3
                else "NEGATIVE — fired-grounding sessions score LOWER (investigate signal gate)"
            )

    return report


def main():
    parser = argparse.ArgumentParser(description="Recall Logger — observability for Tier 1.5 grounding")
    sub = parser.add_subparsers(dest="command")

    log = sub.add_parser("log", help="Append a grounding decision to the trace")
    log.add_argument("--status", required=True, choices=sorted(VALID_STATUSES))
    log.add_argument("--domain", default="", help="Grounding-relevant domain (content, copy, brand, etc.)")
    log.add_argument("--expert", default="", help="Expert name if known (e.g., lara-acosta)")
    log.add_argument("--query", default="", help="The Recall query that was constructed")
    log.add_argument("--reason", default="", help="Skip/fail reason (no_signal, low_signal, timeout, etc.)")
    log.add_argument("--cards-returned", type=int, default=None, help="Number of cards Recall returned")
    log.add_argument("--signal", default="", choices=[""] + sorted(VALID_SIGNALS), help="Relevance signal level")
    log.add_argument("--note", default="", help="Freeform note (especially for reason=other)")
    log.add_argument("--session-id", default="", help="Optional session id for tighter correlation")

    rep = sub.add_parser("report", help="Weekly correlation: does grounding lift Expert Standard?")
    rep.add_argument("--days", type=int, default=7)

    args = parser.parse_args()

    if args.command == "log":
        ok = log_decision(
            status=args.status,
            domain=args.domain,
            query=args.query,
            expert=args.expert,
            reason=args.reason,
            cards_returned=args.cards_returned,
            signal=args.signal,
            note=args.note,
            session_id=args.session_id,
        )
        sys.exit(0 if ok else 1)

    if args.command == "report":
        report = correlation_report(days=args.days)
        print(json.dumps(report, indent=2))
        sys.exit(0)

    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
