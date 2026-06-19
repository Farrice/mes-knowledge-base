#!/usr/bin/env python3
"""
Revenue Tracker — Connects quality scores to business outcomes.

The missing link: the system tracks whether output is "good" but not whether
it makes money. This script adds outcome attribution to the feedback ratchet.

What it does:
    1. Tags Performance Log entries with revenue outcomes
    2. Tracks deliverable → outcome connections over time
    3. Calculates revenue-weighted quality scores
    4. Identifies which skills/experts actually generate ROI

Usage:
    from execution.revenue_tracker import (
        log_outcome, get_roi_report, tag_deliverable
    )

CLI:
    python execution/revenue_tracker.py log <deliverable> --revenue <amount> --outcome <description>
    python execution/revenue_tracker.py tag <notion_page_id> --revenue <amount> --outcome <description>
    python execution/revenue_tracker.py report [--skill <name>] [--expert <name>]
    python execution/revenue_tracker.py pipeline
"""

import os
import json
import argparse
from datetime import date, datetime, timedelta
from typing import Optional, Dict, List, Any
from pathlib import Path
from dotenv import load_dotenv

# Load .env
for env_path in [
    Path(__file__).parent.parent / 'jarvis-bot' / '.env',
    Path(__file__).parent.parent / '.env',
]:
    if env_path.exists():
        load_dotenv(env_path)

from notion_api import NotionAPI, NotionAPIError

PERFORMANCE_DB_ID = os.getenv(
    'NOTION_DB_PERFORMANCE',
    '31f49875a89781dbb599dee5e7961b5c'
)

# Local outcome tracking file (supplements Notion for speed)
OUTCOME_FILE = Path(__file__).parent.parent / '.agent' / 'revenue-outcomes.json'


def _load_outcomes() -> Dict[str, Any]:
    """Load local outcome tracking data."""
    if OUTCOME_FILE.exists():
        return json.loads(OUTCOME_FILE.read_text())
    return {"outcomes": [], "total_revenue": 0, "last_updated": None}


def _save_outcomes(data: Dict[str, Any]):
    """Save local outcome tracking data."""
    data["last_updated"] = datetime.now().isoformat()
    OUTCOME_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTCOME_FILE.write_text(json.dumps(data, indent=2))


def _find_pending_match(outcomes: List[Dict[str, Any]], deliverable: str) -> Optional[Dict[str, Any]]:
    """Find the pending stub that `deliverable` resolves, if any.

    Match order: exact deliverable string, then case-insensitive
    containment either way (stubs are truncated to 200 chars by
    auto_register_outcome, so the user's description often contains
    the stub or vice versa). Returns the entry dict (mutable reference
    into `outcomes`) or None.
    """
    want = deliverable.strip().lower()
    if not want:
        return None
    pending = [o for o in outcomes if o.get("outcome_type") == "pending"]
    for o in pending:
        if o.get("deliverable", "").strip().lower() == want:
            return o
    for o in pending:
        have = o.get("deliverable", "").strip().lower()
        if have and (want in have or have in want):
            return o
    return None


def log_outcome(
    deliverable: str,
    revenue: float = 0,
    outcome: str = "",
    expert: str = "",
    skill: str = "",
    client: str = "",
    outcome_type: str = "revenue",
    notion_page_id: str = "",
) -> Dict[str, Any]:
    """
    Log a revenue/business outcome tied to a deliverable.

    If a pending stub (auto-registered by chain_runner.finalize) matches
    the deliverable, it is RESOLVED IN PLACE — updated with the real
    outcome instead of appending a duplicate. This is what drains the
    "N deliverables awaiting revenue/outcome data" counter; before this
    fix the pending count could only grow.

    Args:
        deliverable: Description of the deliverable that generated this outcome
        revenue: Dollar amount generated (0 if non-monetary)
        outcome: Description of the outcome (e.g., "client signed", "3 sales")
        expert: Expert agent that produced the deliverable
        skill: Skill used
        client: Client name (if applicable)
        outcome_type: revenue | lead | conversion | feedback | engagement | dead
        notion_page_id: Optional Notion page ID to tag

    Returns:
        Dict with outcome data
    """
    data = _load_outcomes()
    matched = _find_pending_match(data["outcomes"], deliverable)

    if matched is not None:
        # Resolve the pending stub in place — preserve its provenance fields.
        matched.update({
            "revenue": revenue,
            "outcome": outcome,
            "outcome_type": outcome_type,
            "resolved_date": date.today().isoformat(),
        })
        if expert:
            matched["expert"] = expert
        if skill:
            matched["skill"] = skill
        if client:
            matched["client"] = client
        if notion_page_id:
            matched["notion_page_id"] = notion_page_id
        entry = matched
        resolved_stub = True
    else:
        entry = {
            "deliverable": deliverable,
            "revenue": revenue,
            "outcome": outcome,
            "expert": expert,
            "skill": skill,
            "client": client,
            "outcome_type": outcome_type,
            "date": date.today().isoformat(),
            "notion_page_id": notion_page_id,
        }
        data["outcomes"].append(entry)
        resolved_stub = False

    data["total_revenue"] = sum(o.get("revenue", 0) for o in data["outcomes"])
    _save_outcomes(data)

    # Tag Notion page if provided
    if notion_page_id:
        try:
            api = NotionAPI()
            # Add outcome as a comment or update properties
            # Note: this updates the page's properties if the schema supports it
            api.update_page(notion_page_id, {
                "Notes": api.rich_text(f"[OUTCOME] {outcome} | Revenue: ${revenue}")
            })
            entry["notion_tagged"] = True
        except Exception as e:
            entry["notion_tagged"] = False
            entry["notion_error"] = str(e)

    print(f"\n{'='*60}")
    print(f"  OUTCOME LOGGED" + ("  (resolved pending stub)" if resolved_stub else ""))
    print(f"{'='*60}")
    print(f"  Deliverable: {deliverable}")
    print(f"  Revenue:     ${revenue:,.2f}")
    print(f"  Outcome:     {outcome}")
    print(f"  Expert:      {expert}")
    print(f"  Skill:       {skill}")
    if client:
        print(f"  Client:      {client}")
    print(f"  Type:        {outcome_type}")
    print(f"  Total Revenue (All Time): ${data['total_revenue']:,.2f}")
    print(f"{'='*60}\n")

    return entry


DEFAULT_CHECK_IN_DAYS = 14


def auto_register_outcome(
    deliverable: str,
    expert: str = "",
    skill: str = "",
    workflow: str = "",
    task_type: str = "",
    composite: float = 0.0,
    notion_page_id: str = "",
    experiment_tag: str = "",
    expected_outcome: str = "",
    check_in_days: Optional[int] = None,
) -> Dict[str, Any]:
    """Upgrade 7 — Phase 2 auto-link hook.

    Called from chain_runner.finalize() on every PASSED deliverable in a
    revenue-relevant task_type. Creates a pending-outcome stub so the
    deliverable appears in `revenue_tracker pipeline` without manual
    follow-up. User later updates via `revenue_tracker log` with actual
    revenue + outcome description.

    Outcome-loop closure (2026-06-12): every stub now carries an
    expected_outcome (what success looks like, even if empty) and a
    check_in_date (defaults to +14 days). `revenue_tracker due` and the
    session-ledger staleness line surface overdue check-ins, so the
    outer loop has a deterministic clock instead of relying on memory.

    Idempotent: re-registering the same deliverable is a no-op.
    Non-fatal: any exception is swallowed — revenue tracking is never
    allowed to break the quality gate.
    """
    REVENUE_TASK_TYPES = {
        "Content", "Strategy", "Client Work", "Research",
        "Creative", "Analysis", "Extraction",
    }
    if task_type and task_type not in REVENUE_TASK_TYPES:
        return {"skipped": True, "reason": f"task_type '{task_type}' not revenue-relevant"}

    try:
        data = _load_outcomes()
        existing = [o for o in data["outcomes"] if o.get("deliverable") == deliverable]
        if existing:
            return {"skipped": True, "reason": "already registered", "entry": existing[-1]}

        days = check_in_days if check_in_days is not None else DEFAULT_CHECK_IN_DAYS
        entry = {
            "deliverable": deliverable,
            "revenue": 0.0,
            "outcome": "pending tracking",
            "expert": expert,
            "skill": skill,
            "workflow": workflow,
            "task_type": task_type,
            "composite_at_delivery": composite,
            "experiment_tag": experiment_tag,
            "notion_page_id": notion_page_id,
            "outcome_type": "pending",
            "date": date.today().isoformat(),
            "auto_registered": True,
            "expected_outcome": expected_outcome,
            "check_in_date": (date.today() + timedelta(days=days)).isoformat(),
        }
        data["outcomes"].append(entry)
        _save_outcomes(data)
        return {"registered": True, "entry": entry}
    except Exception as e:
        return {"skipped": True, "error": str(e)}


def get_due(include_legacy: bool = True, legacy_days: int = 30) -> Dict[str, Any]:
    """List pending outcomes whose check-in date has arrived.

    Two buckets:
      due     — entries with check_in_date <= today
      legacy  — entries with NO check_in_date (pre-2026-06-12 stubs)
                older than `legacy_days`, shown so old debt stays visible

    Prints prefilled `log` commands so closing each one is copy-paste.
    """
    data = _load_outcomes()
    today = date.today().isoformat()
    pending = [o for o in data.get("outcomes", []) if o.get("outcome_type") == "pending"]

    due = sorted(
        [o for o in pending if o.get("check_in_date") and o["check_in_date"] <= today],
        key=lambda o: o.get("check_in_date", ""),
    )
    legacy = []
    if include_legacy:
        cutoff = (date.today() - timedelta(days=legacy_days)).isoformat()
        legacy = sorted(
            [o for o in pending if not o.get("check_in_date") and o.get("date", "") <= cutoff],
            key=lambda o: o.get("date", ""),
        )

    print(f"\n{'='*60}")
    print(f"  OUTCOME CHECK-INS DUE — {today}")
    print(f"{'='*60}\n")
    if not due and not legacy:
        print("  Nothing due. Outer loop is current.")
    if due:
        print(f"  DUE ({len(due)}):")
        for o in due:
            exp = f" | expected: {o['expected_outcome']}" if o.get("expected_outcome") else ""
            print(f"   - [{o.get('check_in_date')}] {o['deliverable'][:70]}{exp}")
    if legacy:
        print(f"\n  LEGACY PENDING, no check-in date, older than {legacy_days}d ({len(legacy)}):")
        for o in legacy[:10]:
            print(f"   - [{o.get('date')}] {o['deliverable'][:70]}")
        if len(legacy) > 10:
            print(f"   ... and {len(legacy) - 10} more (run /weekly-closeout to drain)")
    if due or legacy:
        first = (due or legacy)[0]
        print("\n  Close one with:")
        print(f"  python3 execution/revenue_tracker.py log \"{first['deliverable'][:60]}\" "
              f"--revenue <$> --outcome \"<what happened, or 'dead: reason'>\"")
    print(f"\n{'='*60}\n")
    return {"due": due, "legacy": legacy, "due_count": len(due), "legacy_count": len(legacy)}


def get_roi_report(skill: str = "", expert: str = "") -> Dict[str, Any]:
    """
    Generate an ROI report showing which skills/experts generate revenue.

    Args:
        skill: Filter by skill name
        expert: Filter by expert name

    Returns:
        Dict with ROI analysis
    """
    data = _load_outcomes()
    outcomes = data.get("outcomes", [])

    # Filter
    if skill:
        outcomes = [o for o in outcomes if o.get("skill") == skill]
    if expert:
        outcomes = [o for o in outcomes if o.get("expert") == expert]

    # Aggregate by skill
    skill_revenue = {}
    expert_revenue = {}
    type_revenue = {}

    for o in outcomes:
        s = o.get("skill", "unknown")
        e = o.get("expert", "unknown")
        t = o.get("outcome_type", "unknown")
        r = o.get("revenue", 0)

        skill_revenue[s] = skill_revenue.get(s, 0) + r
        expert_revenue[e] = expert_revenue.get(e, 0) + r
        type_revenue[t] = type_revenue.get(t, 0) + r

    report = {
        "generated": date.today().isoformat(),
        "total_outcomes": len(outcomes),
        "total_revenue": sum(o.get("revenue", 0) for o in outcomes),
        "by_skill": dict(sorted(skill_revenue.items(), key=lambda x: x[1], reverse=True)),
        "by_expert": dict(sorted(expert_revenue.items(), key=lambda x: x[1], reverse=True)),
        "by_type": type_revenue,
        "recent": outcomes[-5:] if outcomes else [],
    }

    # Print report
    print(f"\n{'='*60}")
    print(f"  ROI REPORT")
    print(f"  Generated: {report['generated']}")
    print(f"{'='*60}")
    print(f"\n  Total Outcomes: {report['total_outcomes']}")
    print(f"  Total Revenue:  ${report['total_revenue']:,.2f}")

    if report["by_skill"]:
        print(f"\n  BY SKILL:")
        for s, r in report["by_skill"].items():
            print(f"    {s}: ${r:,.2f}")

    if report["by_expert"]:
        print(f"\n  BY EXPERT:")
        for e, r in report["by_expert"].items():
            print(f"    {e}: ${r:,.2f}")

    if report["by_type"]:
        print(f"\n  BY TYPE:")
        for t, r in report["by_type"].items():
            print(f"    {t}: ${r:,.2f}")

    if report["recent"]:
        print(f"\n  RECENT OUTCOMES:")
        for o in report["recent"]:
            print(f"    [{o['date']}] {o['deliverable']}: ${o.get('revenue', 0):,.2f} — {o.get('outcome', 'N/A')}")

    print(f"\n{'='*60}\n")
    return report


def get_pipeline() -> Dict[str, Any]:
    """
    Show active deliverables that should be tracked for outcomes.

    Scans recent Performance Log entries and flags any that don't have
    outcome data yet — these are the ones to follow up on.
    """
    data = _load_outcomes()
    tracked_deliverables = {o["deliverable"] for o in data.get("outcomes", [])}

    # Get recent performance log entries
    try:
        api = NotionAPI()
        results = api.query_database(PERFORMANCE_DB_ID, page_size=20)
        pages = results.get("results", [])
    except Exception:
        pages = []

    pipeline = []
    for page in pages:
        props = page.get("properties", {})
        title_prop = props.get("Output", {})
        title_parts = title_prop.get("title", [])
        title = title_parts[0].get("text", {}).get("content", "") if title_parts else "Unknown"

        # Check if this deliverable has outcome data
        if title not in tracked_deliverables:
            task_type_prop = props.get("Task Type", {})
            task_type = task_type_prop.get("select", {}).get("name", "Unknown") if task_type_prop.get("select") else "Unknown"

            pipeline.append({
                "deliverable": title[:80],
                "type": task_type,
                "page_id": page["id"],
                "needs_outcome": True,
            })

    print(f"\n{'='*60}")
    print(f"  REVENUE PIPELINE — Deliverables Awaiting Outcome Data")
    print(f"{'='*60}\n")

    if not pipeline:
        print("  All recent deliverables have outcome data. Nice.")
    else:
        for i, p in enumerate(pipeline, 1):
            print(f"  {i}. [{p['type']}] {p['deliverable']}")
        print(f"\n  {len(pipeline)} deliverables need outcome tracking.")
        print(f"  Use: python execution/revenue_tracker.py log \"<deliverable>\" --revenue <$> --outcome \"<what happened>\"")

    print(f"\n{'='*60}\n")
    return {"pipeline": pipeline, "count": len(pipeline)}


# ── CLI ─────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Revenue Tracker — Connect quality to outcomes")
    sub = parser.add_subparsers(dest="command")

    # log
    log_cmd = sub.add_parser("log", help="Log a revenue outcome")
    log_cmd.add_argument("deliverable", help="Description of the deliverable")
    log_cmd.add_argument("--revenue", type=float, default=0, help="Revenue generated ($)")
    log_cmd.add_argument("--outcome", default="", help="Outcome description")
    log_cmd.add_argument("--expert", default="", help="Expert name")
    log_cmd.add_argument("--skill", default="", help="Skill name")
    log_cmd.add_argument("--client", default="", help="Client name")
    log_cmd.add_argument("--type", default="revenue", help="Outcome type")
    log_cmd.add_argument("--notion-id", default="", help="Notion page ID to tag")

    # tag (shorthand for tagging a specific Notion page)
    tag_cmd = sub.add_parser("tag", help="Tag a Notion page with outcome data")
    tag_cmd.add_argument("notion_page_id", help="Notion page ID")
    tag_cmd.add_argument("--revenue", type=float, default=0, help="Revenue ($)")
    tag_cmd.add_argument("--outcome", default="", help="Outcome description")

    # report
    report_cmd = sub.add_parser("report", help="ROI report")
    report_cmd.add_argument("--skill", default="", help="Filter by skill")
    report_cmd.add_argument("--expert", default="", help="Filter by expert")

    # pipeline
    sub.add_parser("pipeline", help="Show deliverables needing outcome tracking")

    # due
    due_cmd = sub.add_parser("due", help="Show pending outcomes whose check-in date has arrived")
    due_cmd.add_argument("--no-legacy", action="store_true", help="Hide legacy pending entries without check-in dates")
    due_cmd.add_argument("--legacy-days", type=int, default=30, help="Age threshold for legacy pending entries (default 30)")

    args = parser.parse_args()

    if args.command == "log":
        log_outcome(
            args.deliverable, args.revenue, args.outcome,
            args.expert, args.skill, args.client, args.type, args.notion_id
        )
    elif args.command == "tag":
        log_outcome("(tagged)", args.revenue, args.outcome, notion_page_id=args.notion_page_id)
    elif args.command == "report":
        get_roi_report(args.skill, args.expert)
    elif args.command == "pipeline":
        get_pipeline()
    elif args.command == "due":
        get_due(include_legacy=not args.no_legacy, legacy_days=args.legacy_days)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
