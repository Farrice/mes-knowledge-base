#!/usr/bin/env python3
"""
Routing Intelligence — Observation layer for expert routing decisions.

Logs routing decisions and user feedback. Generates analytics dashboards.
Does NOT modify routing behavior — this is observation only.
The user reads the dashboard, sees patterns, and makes their own decisions.

Usage:
    python execution/routing_intelligence.py log \
        --request "Write a sales page" --score 4 --domain "1-copywriting" \
        --experts "Cardinal Mason" --tier 2 --mode output

    python execution/routing_intelligence.py feedback \
        --routing-id "rt_20260308_143022_a7f3" --rating positive

    python execution/routing_intelligence.py scoreboard
    python execution/routing_intelligence.py utilization
    python execution/routing_intelligence.py unused
    python execution/routing_intelligence.py domain-dist
    python execution/routing_intelligence.py top-combos
    python execution/routing_intelligence.py underperforming
    python execution/routing_intelligence.py last-id
"""
import argparse
import json
import os
import secrets
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).parent.parent
DATA_FILE = ROOT / ".agent" / "routing-intelligence.json"
AGENTS_DIR = ROOT / "agents"


# ---------------------------------------------------------------------------
# Data I/O
# ---------------------------------------------------------------------------

def _empty_data() -> dict:
    """Return a fresh empty data structure."""
    month = datetime.now(timezone.utc).strftime("%Y-%m")
    return {
        "schema_version": "1.0",
        "current_month": month,
        "routing_decisions": [],
        "feedback_log": [],
        "monthly_summary": {
            month: _empty_month_summary()
        },
    }


def _empty_month_summary() -> dict:
    return {
        "total_routings": 0,
        "total_feedback": 0,
        "positive_count": 0,
        "negative_count": 0,
        "mixed_count": 0,
        "domain_counts": {},
        "expert_counts": {},
        "tier_counts": {"0": 0, "1": 0, "2": 0, "3": 0},
        "mode_counts": {"output": 0, "expertise": 0, "hybrid": 0},
        "ensemble_count": 0,
    }


def _read_data() -> dict:
    """Read JSON data file, return empty structure if missing or corrupt."""
    if not DATA_FILE.exists():
        return _empty_data()
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, Exception):
        return _empty_data()


def _write_data(data: dict):
    """Write JSON data, create .agent/ directory if needed."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(data, indent=4, ensure_ascii=False), encoding="utf-8")


def _ensure_current_month(data: dict) -> dict:
    """Handle month rollover — archive stale month, reset for current."""
    now_month = datetime.now(timezone.utc).strftime("%Y-%m")
    if data.get("current_month") == now_month:
        return data

    old_month = data.get("current_month", now_month)

    # Aggregate current routing_decisions into monthly_summary if not already there
    if old_month not in data.get("monthly_summary", {}):
        data.setdefault("monthly_summary", {})[old_month] = _empty_month_summary()

    # Recount from routing_decisions for the old month (in case summary drifted)
    summary = data["monthly_summary"][old_month]
    for rd in data.get("routing_decisions", []):
        summary["total_routings"] += 1
        domain = rd.get("domain_detected", "unknown")
        summary["domain_counts"][domain] = summary["domain_counts"].get(domain, 0) + 1
        for expert in rd.get("experts_deployed", []):
            summary["expert_counts"][expert] = summary["expert_counts"].get(expert, 0) + 1
        tier = str(rd.get("tier_loaded", 0))
        summary["tier_counts"][tier] = summary["tier_counts"].get(tier, 0) + 1
        mode = rd.get("mode", "output")
        summary["mode_counts"][mode] = summary["mode_counts"].get(mode, 0) + 1
        if rd.get("ensemble"):
            summary["ensemble_count"] += 1

    for fb in data.get("feedback_log", []):
        summary["total_feedback"] += 1
        rating = fb.get("rating", "mixed")
        summary[f"{rating}_count"] = summary.get(f"{rating}_count", 0) + 1

    # Reset for new month
    data["current_month"] = now_month
    data["routing_decisions"] = []
    data["feedback_log"] = []
    data["monthly_summary"].setdefault(now_month, _empty_month_summary())

    return data


# ---------------------------------------------------------------------------
# ID generators
# ---------------------------------------------------------------------------

def _generate_routing_id() -> str:
    return f"rt_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_{secrets.token_hex(2)}"


def _generate_feedback_id() -> str:
    return f"fb_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_{secrets.token_hex(2)}"


# ---------------------------------------------------------------------------
# Agent discovery
# ---------------------------------------------------------------------------

def _get_all_agent_slugs() -> List[str]:
    """Get all agent slugs from agents/ directory (skip _framework, hidden dirs)."""
    agents = []
    if not AGENTS_DIR.exists():
        return agents
    for item in sorted(os.listdir(AGENTS_DIR)):
        if item.startswith("_") or item.startswith("."):
            continue
        if (AGENTS_DIR / item).is_dir():
            agents.append(item)
    return agents


def _slug_to_display(slug: str) -> str:
    """Convert agent slug to display name: 'cardinal-mason' -> 'Cardinal Mason'."""
    return slug.replace("-", " ").title()


# ---------------------------------------------------------------------------
# Core logging functions
# ---------------------------------------------------------------------------

def log_routing_decision(
    request_summary: str,
    intent_score: int,
    domain_detected: str,
    experts_deployed: List[str],
    tier_loaded: int,
    mode: str,
    workflow_used: str = "",
    ensemble: bool = False,
    compound_pairing: str = "",
    session_id: str = "",
) -> str:
    """Log a routing decision. Returns the generated routing_id."""
    data = _read_data()
    data = _ensure_current_month(data)

    routing_id = _generate_routing_id()
    month = data["current_month"]

    record = {
        "routing_id": routing_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "session_id": session_id,
        "request_summary": request_summary[:200],
        "intent_score": intent_score,
        "domain_detected": domain_detected,
        "experts_deployed": experts_deployed,
        "tier_loaded": tier_loaded,
        "mode": mode,
        "workflow_used": workflow_used,
        "ensemble": ensemble,
        "compound_pairing": compound_pairing or None,
        "feedback": None,
    }

    data["routing_decisions"].append(record)

    # Update monthly summary inline
    summary = data["monthly_summary"][month]
    summary["total_routings"] += 1
    summary["domain_counts"][domain_detected] = summary["domain_counts"].get(domain_detected, 0) + 1
    for expert in experts_deployed:
        summary["expert_counts"][expert] = summary["expert_counts"].get(expert, 0) + 1
    tier_key = str(tier_loaded)
    summary["tier_counts"][tier_key] = summary["tier_counts"].get(tier_key, 0) + 1
    summary["mode_counts"][mode] = summary["mode_counts"].get(mode, 0) + 1
    if ensemble:
        summary["ensemble_count"] += 1

    _write_data(data)
    return routing_id


def log_feedback(
    routing_id: str,
    rating: str,
    session_id: str = "",
    correction: str = "",
    notes: str = "",
) -> str:
    """Log user feedback on a routing decision. Returns feedback_id."""
    data = _read_data()
    data = _ensure_current_month(data)

    feedback_id = _generate_feedback_id()
    month = data["current_month"]

    record = {
        "feedback_id": feedback_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "session_id": session_id,
        "routing_id": routing_id,
        "rating": rating,
        "correction": correction or None,
        "notes": notes or None,
    }

    data["feedback_log"].append(record)

    # Link feedback to routing decision
    for rd in data["routing_decisions"]:
        if rd["routing_id"] == routing_id:
            rd["feedback"] = feedback_id
            break

    # Update monthly summary
    summary = data["monthly_summary"][month]
    summary["total_feedback"] += 1
    count_key = f"{rating}_count"
    summary[count_key] = summary.get(count_key, 0) + 1

    _write_data(data)
    return feedback_id


def get_last_routing_id() -> Optional[str]:
    """Return the routing_id of the most recent routing decision."""
    data = _read_data()
    decisions = data.get("routing_decisions", [])
    if not decisions:
        return None
    return decisions[-1]["routing_id"]


# ---------------------------------------------------------------------------
# Analytics functions
# ---------------------------------------------------------------------------

def _get_current_summary(data: dict) -> dict:
    """Get the current month's summary."""
    month = data.get("current_month", datetime.now(timezone.utc).strftime("%Y-%m"))
    return data.get("monthly_summary", {}).get(month, _empty_month_summary())


def _get_all_time_summary(data: dict) -> dict:
    """Aggregate all months into a combined summary."""
    combined = _empty_month_summary()
    for month, summary in data.get("monthly_summary", {}).items():
        combined["total_routings"] += summary.get("total_routings", 0)
        combined["total_feedback"] += summary.get("total_feedback", 0)
        combined["positive_count"] += summary.get("positive_count", 0)
        combined["negative_count"] += summary.get("negative_count", 0)
        combined["mixed_count"] += summary.get("mixed_count", 0)
        combined["ensemble_count"] += summary.get("ensemble_count", 0)
        for domain, count in summary.get("domain_counts", {}).items():
            combined["domain_counts"][domain] = combined["domain_counts"].get(domain, 0) + count
        for expert, count in summary.get("expert_counts", {}).items():
            combined["expert_counts"][expert] = combined["expert_counts"].get(expert, 0) + count
        for tier, count in summary.get("tier_counts", {}).items():
            combined["tier_counts"][tier] = combined["tier_counts"].get(tier, 0) + count
        for mode, count in summary.get("mode_counts", {}).items():
            combined["mode_counts"][mode] = combined["mode_counts"].get(mode, 0) + count
    return combined


def expert_utilization(data: dict) -> str:
    """Per-expert deployment counts with feedback breakdown."""
    summary = _get_current_summary(data)
    decisions = data.get("routing_decisions", [])
    feedback_log = data.get("feedback_log", [])

    # Build feedback map: routing_id -> rating
    feedback_map = {fb["routing_id"]: fb["rating"] for fb in feedback_log}

    # Build per-expert feedback counts
    expert_feedback = {}
    for rd in decisions:
        for expert in rd.get("experts_deployed", []):
            if expert not in expert_feedback:
                expert_feedback[expert] = {"positive": 0, "negative": 0, "mixed": 0}
            rating = feedback_map.get(rd["routing_id"])
            if rating:
                expert_feedback[expert][rating] = expert_feedback[expert].get(rating, 0) + 1

    expert_counts = summary.get("expert_counts", {})
    if not expert_counts:
        return "No expert deployments recorded yet.\n"

    # Sort by deployment count descending
    sorted_experts = sorted(expert_counts.items(), key=lambda x: x[1], reverse=True)

    lines = ["| Expert | Deployments | Positive | Negative | Mixed |",
             "|--------|-------------|----------|----------|-------|"]
    for expert, count in sorted_experts:
        fb = expert_feedback.get(expert, {"positive": 0, "negative": 0, "mixed": 0})
        lines.append(f"| {expert} | {count} | {fb['positive']} | {fb['negative']} | {fb['mixed']} |")

    return "\n".join(lines) + "\n"


def domain_distribution(data: dict) -> str:
    """Per-domain request counts."""
    summary = _get_current_summary(data)
    domain_counts = summary.get("domain_counts", {})
    if not domain_counts:
        return "No domain data recorded yet.\n"

    total = sum(domain_counts.values())
    sorted_domains = sorted(domain_counts.items(), key=lambda x: x[1], reverse=True)

    lines = ["| Domain | Requests | % of Total |",
             "|--------|----------|------------|"]
    for domain, count in sorted_domains:
        pct = round(count / total * 100) if total else 0
        lines.append(f"| {domain} | {count} | {pct}% |")

    return "\n".join(lines) + "\n"


def unused_experts(data: dict) -> str:
    """Cross-reference agents/ directory against expert_counts."""
    all_time = _get_all_time_summary(data)
    used_experts = set(all_time.get("expert_counts", {}).keys())
    used_normalized = {name.lower().replace(" ", "-") for name in used_experts}

    all_slugs = _get_all_agent_slugs()
    unused = []
    for slug in all_slugs:
        if slug not in used_normalized and _slug_to_display(slug).lower().replace(" ", "-") not in used_normalized:
            # Check if any used expert name matches this slug loosely
            matched = False
            for used_name in used_experts:
                if slug.replace("-", "") in used_name.lower().replace(" ", "").replace("-", ""):
                    matched = True
                    break
            if not matched:
                unused.append(slug)

    if not unused:
        return "All agents have been deployed at least once. Nice coverage!\n"

    lines = [f"**{len(unused)} agents** with zero deployments (all-time):\n"]
    for slug in unused[:30]:
        lines.append(f"- `{slug}` ({_slug_to_display(slug)})")
    if len(unused) > 30:
        lines.append(f"- ... and {len(unused) - 30} more")

    return "\n".join(lines) + "\n"


def top_combinations(data: dict) -> str:
    """Ensemble pairings sorted by positive feedback ratio."""
    decisions = data.get("routing_decisions", [])
    feedback_log = data.get("feedback_log", [])
    feedback_map = {fb["routing_id"]: fb["rating"] for fb in feedback_log}

    ensembles = {}
    for rd in decisions:
        if not rd.get("ensemble"):
            continue
        pairing = rd.get("compound_pairing") or " + ".join(rd.get("experts_deployed", []))
        if pairing not in ensembles:
            ensembles[pairing] = {"uses": 0, "positive": 0, "negative": 0, "mixed": 0}
        ensembles[pairing]["uses"] += 1
        rating = feedback_map.get(rd["routing_id"])
        if rating:
            ensembles[pairing][rating] += 1

    if not ensembles:
        return "No ensemble routings recorded yet.\n"

    sorted_ensembles = sorted(ensembles.items(), key=lambda x: x[1]["positive"], reverse=True)

    lines = ["| Pairing | Uses | Positive | Negative | Mixed |",
             "|---------|------|----------|----------|-------|"]
    for pairing, stats in sorted_ensembles:
        lines.append(f"| {pairing} | {stats['uses']} | {stats['positive']} | {stats['negative']} | {stats['mixed']} |")

    return "\n".join(lines) + "\n"


def underperforming_routes(data: dict) -> str:
    """Routes with negative feedback and their corrections."""
    decisions = data.get("routing_decisions", [])
    feedback_log = data.get("feedback_log", [])

    # Find negative feedback with corrections
    negative_fbs = [fb for fb in feedback_log if fb.get("rating") == "negative"]
    if not negative_fbs:
        return "No negative feedback recorded. Either everything's working well, or feedback isn't being captured yet.\n"

    # Map routing_id to decision
    rd_map = {rd["routing_id"]: rd for rd in decisions}

    lines = ["| Expert(s) | Domain | Correction | Notes |",
             "|-----------|--------|------------|-------|"]
    for fb in negative_fbs:
        rd = rd_map.get(fb["routing_id"], {})
        experts = ", ".join(rd.get("experts_deployed", ["unknown"]))
        domain = rd.get("domain_detected", "unknown")
        correction = fb.get("correction") or "—"
        notes = fb.get("notes") or "—"
        lines.append(f"| {experts} | {domain} | {correction} | {notes} |")

    return "\n".join(lines) + "\n"


def generate_scoreboard() -> str:
    """Full Markdown analytics dashboard."""
    data = _read_data()
    data = _ensure_current_month(data)

    summary = _get_current_summary(data)
    month = data.get("current_month", "unknown")

    total_r = summary.get("total_routings", 0)
    total_f = summary.get("total_feedback", 0)
    pos = summary.get("positive_count", 0)
    neg = summary.get("negative_count", 0)
    mix = summary.get("mixed_count", 0)
    ens = summary.get("ensemble_count", 0)

    if total_r == 0:
        return (
            "# Routing Intelligence Dashboard\n\n"
            f"**Period**: {month}\n\n"
            "No routing data yet. Data will accumulate as you use the system.\n\n"
            "The intelligence layer logs every expert routing decision and your feedback.\n"
            "Use `/rate` after expert outputs to start building your scoreboard.\n"
        )

    pos_rate = round(pos / total_f * 100) if total_f else 0
    ens_rate = round(ens / total_r * 100) if total_r else 0

    # Calculate avg intent score
    scores = [rd.get("intent_score", 0) for rd in data.get("routing_decisions", [])]
    avg_score = round(sum(scores) / len(scores), 1) if scores else 0

    lines = [
        f"# Routing Intelligence Dashboard",
        f"**Generated**: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"**Period**: {month} (current month)\n",
        "## Overview\n",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Total Routings | {total_r} |",
        f"| Total Feedback | {total_f} |",
        f"| Positive Rate | {pos_rate}% ({pos}/{total_f}) |",
        f"| Negative | {neg} |",
        f"| Mixed | {mix} |",
        f"| Ensemble Rate | {ens_rate}% ({ens}/{total_r}) |",
        f"| Avg Intent Score | {avg_score} |",
        "",
        "## Expert Utilization\n",
        expert_utilization(data),
        "## Domain Distribution\n",
        domain_distribution(data),
        "## Top-Performing Ensembles\n",
        top_combinations(data),
        "## Underperforming Routes\n",
        underperforming_routes(data),
        "## Unused Experts\n",
        unused_experts(data),
    ]

    # Suggestions section
    suggestions = _generate_suggestions(data)
    if suggestions:
        lines.append("## Suggestions\n")
        for s in suggestions:
            lines.append(f"- {s}")
        lines.append("")

    return "\n".join(lines)


def _generate_suggestions(data: dict) -> List[str]:
    """Generate actionable suggestions based on patterns."""
    suggestions = []
    summary = _get_current_summary(data)
    decisions = data.get("routing_decisions", [])
    feedback_log = data.get("feedback_log", [])
    feedback_map = {fb["routing_id"]: fb for fb in feedback_log}

    # Suggestion: experts with high positive rate
    expert_counts = summary.get("expert_counts", {})
    for expert, count in expert_counts.items():
        pos_count = 0
        total_fb = 0
        for rd in decisions:
            if expert in rd.get("experts_deployed", []):
                fb = feedback_map.get(rd["routing_id"])
                if fb:
                    total_fb += 1
                    if fb["rating"] == "positive":
                        pos_count += 1
        if total_fb >= 3 and pos_count / total_fb >= 0.8:
            suggestions.append(f"**Strong performer**: {expert} has {pos_count}/{total_fb} positive feedback. Consider using more frequently.")

    # Suggestion: repeated negative corrections pointing to same expert
    corrections = {}
    for fb in feedback_log:
        if fb.get("correction"):
            corrections[fb["correction"]] = corrections.get(fb["correction"], 0) + 1
    for correction, count in corrections.items():
        if count >= 2:
            suggestions.append(f"**Recurring correction**: \"{correction}\" appeared {count} times. Consider adjusting default routing.")

    # Suggestion: low feedback rate
    total_r = summary.get("total_routings", 0)
    total_f = summary.get("total_feedback", 0)
    if total_r >= 10 and total_f / total_r < 0.3:
        suggestions.append(f"**Low feedback rate**: Only {total_f}/{total_r} routings have feedback ({round(total_f/total_r*100)}%). Use `/rate` more often to improve insights.")

    return suggestions


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Routing Intelligence — observation layer for expert routing decisions"
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # log
    log_p = subparsers.add_parser("log", help="Log a routing decision")
    log_p.add_argument("--request", required=True, help="Request summary (max 200 chars)")
    log_p.add_argument("--score", type=int, required=True, help="Intent score 1-5")
    log_p.add_argument("--domain", required=True, help="Domain detected (e.g. 1-copywriting)")
    log_p.add_argument("--experts", required=True, help="Comma-separated expert names")
    log_p.add_argument("--tier", type=int, required=True, help="Tier loaded 0-3")
    log_p.add_argument("--mode", required=True, choices=["output", "expertise", "hybrid"])
    log_p.add_argument("--workflow", default="", help="Workflow/skill path used")
    log_p.add_argument("--ensemble", action="store_true", help="Multi-expert synthesis")
    log_p.add_argument("--pairing", default="", help="Named compound pairing")
    log_p.add_argument("--session", default="", help="Session ID")

    # feedback
    fb_p = subparsers.add_parser("feedback", help="Log user feedback on a routing")
    fb_p.add_argument("--routing-id", required=True, help="Routing decision ID to rate")
    fb_p.add_argument("--rating", required=True, choices=["positive", "negative", "mixed"])
    fb_p.add_argument("--session", default="", help="Session ID")
    fb_p.add_argument("--correction", default="", help="Who should have been used instead")
    fb_p.add_argument("--notes", default="", help="Free text notes")

    # scoreboard
    subparsers.add_parser("scoreboard", help="Generate full analytics dashboard")

    # utilization
    subparsers.add_parser("utilization", help="Expert utilization report")

    # unused
    subparsers.add_parser("unused", help="List unused experts")

    # domain-dist
    subparsers.add_parser("domain-dist", help="Domain distribution report")

    # top-combos
    subparsers.add_parser("top-combos", help="Top-performing ensembles")

    # underperforming
    subparsers.add_parser("underperforming", help="Routes with negative feedback")

    # last-id
    subparsers.add_parser("last-id", help="Print the most recent routing ID")

    args = parser.parse_args()

    if args.command == "log":
        experts = [e.strip() for e in args.experts.split(",")]
        rid = log_routing_decision(
            request_summary=args.request,
            intent_score=args.score,
            domain_detected=args.domain,
            experts_deployed=experts,
            tier_loaded=args.tier,
            mode=args.mode,
            workflow_used=args.workflow,
            ensemble=args.ensemble,
            compound_pairing=args.pairing,
            session_id=args.session,
        )
        print(rid)

    elif args.command == "feedback":
        fid = log_feedback(
            routing_id=args.routing_id,
            rating=args.rating,
            session_id=args.session,
            correction=args.correction,
            notes=args.notes,
        )
        print(fid)

    elif args.command == "scoreboard":
        print(generate_scoreboard())

    elif args.command == "utilization":
        data = _read_data()
        print(expert_utilization(data))

    elif args.command == "unused":
        data = _read_data()
        print(unused_experts(data))

    elif args.command == "domain-dist":
        data = _read_data()
        print(domain_distribution(data))

    elif args.command == "top-combos":
        data = _read_data()
        print(top_combinations(data))

    elif args.command == "underperforming":
        data = _read_data()
        print(underperforming_routes(data))

    elif args.command == "last-id":
        rid = get_last_routing_id()
        if rid:
            print(rid)
        else:
            print("No routing decisions logged yet.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
