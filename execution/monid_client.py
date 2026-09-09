#!/usr/bin/env python3
"""monid_client.py — Cost-gating + tracking for Monid AI MCP server.

Monid is accessed primarily via:
  1. claude.ai connector (MCP at https://mcp.monid.ai/v1)
  2. Claude Code (MCP server in .mcp.json)
  3. Codex / CLI (MCP config)

This wrapper:
  - Tracks usage to .agent/monid-usage.json (per-call cost logging)
  - Enforces monthly budget + per-run caps via cost_gate integration
  - Quotes every paid run before execution
  - Provides CLI commands for budget status, resets, manual logging

Shell-based `monid run` calls are intercepted by cost_gate_hook.py.
Connector/MCP calls must invoke this quote surface before the paid call.

Cost model: pay-per-call (Monid returns actual cost in response).
Local limits: $0.50 default task quote, approval above $0.50,
$3.00 absolute task cap, and $10.00 monthly hard stop.

Usage:
  python3 monid_client.py quote --task "ICP signal scan"
  python3 monid_client.py quote --task "multi-source scan" --estimated-cost 1.25
  python3 monid_client.py budget-status
  python3 monid_client.py log --query "trend check" --cost 0.02 --results 15
  python3 monid_client.py budget-reset  # admin: reset mid-month
"""

import argparse
import json
import math
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRACKER_PATH = Path(
    os.environ.get("MONID_TRACKER_PATH", ROOT / ".agent" / "monid-usage.json")
)

MONID_MONTHLY_BUDGET_USD = 10.00
MONID_SOFT_WARN_PERCENT = 0.75
MONID_HARD_STOP_PERCENT = 1.00
MONID_DEFAULT_TASK_CAP_USD = 0.50
MONID_APPROVAL_THRESHOLD_USD = 0.50
MONID_ABSOLUTE_TASK_CAP_USD = 3.00


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def month_date() -> str:
    """Return YYYY-MM-01 for current calendar month."""
    d = datetime.now(timezone.utc)
    return d.strftime("%Y-%m") + "-01"


def load_tracker() -> dict:
    """Load and normalize usage without writing during read-only checks."""
    if not TRACKER_PATH.exists():
        return _new_tracker()
    try:
        tracker = json.loads(TRACKER_PATH.read_text())
    except (json.JSONDecodeError, OSError):
        return _new_tracker()
    if tracker.get("month_date") != month_date():
        return _new_tracker()
    tracker["plan_dollars"] = MONID_MONTHLY_BUDGET_USD
    tracker.setdefault("month_spent_usd", 0.0)
    tracker.setdefault("month_calls", 0)
    tracker.setdefault("log", [])
    return tracker


def _new_tracker() -> dict:
    return {
        "plan_dollars": MONID_MONTHLY_BUDGET_USD,
        "month_date": month_date(),
        "month_spent_usd": 0.0,
        "month_calls": 0,
        "log": [],
    }


def save_tracker(tracker: dict) -> None:
    """Save tracker with auto-reset if month has changed."""
    # Auto-reset if month changed
    if tracker["month_date"] != month_date():
        tracker["month_date"] = month_date()
        tracker["month_spent_usd"] = 0.0
        tracker["month_calls"] = 0
        tracker["log"] = []

    tracker["plan_dollars"] = MONID_MONTHLY_BUDGET_USD
    TRACKER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with TRACKER_PATH.open("w") as f:
        json.dump(tracker, f, indent=2)
        f.write("\n")


def cmd_budget_status() -> int:
    """Print current month budget status."""
    tracker = load_tracker()
    spent = tracker["month_spent_usd"]
    budget = tracker["plan_dollars"]
    calls = tracker["month_calls"]

    pct = (spent / budget * 100) if budget else 0

    if pct >= MONID_HARD_STOP_PERCENT * 100:
        status_color = "🔴 RED"
    elif pct >= MONID_SOFT_WARN_PERCENT * 100:
        status_color = "🟡 YELLOW"
    else:
        status_color = "🟢 GREEN"

    print(f"\n{status_color} MONID BUDGET STATUS")
    print(f"  Spent:     ${spent:.2f} of ${budget:.2f} ({pct:.1f}%)")
    print(f"  Calls:     {calls}")
    print(f"  Month:     {tracker['month_date']}")

    if pct >= MONID_HARD_STOP_PERCENT * 100:
        print(f"\n  ⚠️  HARD STOP: New runs blocked. Reset (admin) or wait until {month_date()}")
        return 1
    elif pct >= MONID_SOFT_WARN_PERCENT * 100:
        print(f"\n  ⚠️  WARNING: {MONID_SOFT_WARN_PERCENT*100:.0f}% threshold reached. Approve expensive runs only.")
    else:
        print(f"\n  ✓ Plenty of headroom.")

    print()
    return 0


def evaluate_quote(estimated_cost: float) -> dict:
    """Return the local Monid budget decision without mutating usage state."""
    tracker = load_tracker()
    spent = float(tracker["month_spent_usd"])
    estimate = float(estimated_cost)
    projected = spent + estimate

    if not math.isfinite(estimate) or estimate < 0:
        return {
            "decision": "denied",
            "exit_code": 1,
            "reason": "estimated cost must be a finite non-negative number",
            "estimated_cost_usd": None,
            "task_default_usd": MONID_DEFAULT_TASK_CAP_USD,
            "approval_threshold_usd": MONID_APPROVAL_THRESHOLD_USD,
            "task_hard_cap_usd": MONID_ABSOLUTE_TASK_CAP_USD,
            "month_spent_usd": spent,
            "projected_month_usd": None,
            "monthly_hard_stop_usd": MONID_MONTHLY_BUDGET_USD,
        }
    if estimate > MONID_ABSOLUTE_TASK_CAP_USD:
        decision, code = "denied", 1
        reason = (
            f"estimate ${estimate:.2f} exceeds the ${MONID_ABSOLUTE_TASK_CAP_USD:.2f} "
            "absolute task cap"
        )
    elif projected > MONID_MONTHLY_BUDGET_USD:
        decision, code = "denied", 1
        reason = (
            f"projected monthly spend ${projected:.2f} exceeds the "
            f"${MONID_MONTHLY_BUDGET_USD:.2f} monthly hard stop"
        )
    elif estimate > MONID_APPROVAL_THRESHOLD_USD:
        decision, code = "approval_required", 2
        reason = (
            f"estimate exceeds the ${MONID_APPROVAL_THRESHOLD_USD:.2f} "
            "automatic task allowance"
        )
    else:
        decision, code = "approved", 0
        reason = "within the automatic task allowance and monthly budget"

    return {
        "decision": decision,
        "exit_code": code,
        "reason": reason,
        "estimated_cost_usd": round(estimate, 6),
        "task_default_usd": MONID_DEFAULT_TASK_CAP_USD,
        "approval_threshold_usd": MONID_APPROVAL_THRESHOLD_USD,
        "task_hard_cap_usd": MONID_ABSOLUTE_TASK_CAP_USD,
        "month_spent_usd": round(spent, 6),
        "projected_month_usd": round(projected, 6),
        "monthly_hard_stop_usd": MONID_MONTHLY_BUDGET_USD,
    }


def cmd_quote(args) -> int:
    """Quote a paid task before execution; never writes the tracker."""
    estimate = (
        MONID_DEFAULT_TASK_CAP_USD
        if args.estimated_cost is None
        else args.estimated_cost
    )
    quote = evaluate_quote(estimate)
    quote["task"] = args.task or "(no description)"

    if args.json:
        print(json.dumps(quote, sort_keys=True))
    else:
        label = {
            "approved": "APPROVED",
            "approval_required": "APPROVAL REQUIRED",
            "denied": "DENIED",
        }[quote["decision"]]
        print(f"MONID QUOTE: {label}")
        print(f"  Task: {quote['task']}")
        if quote["estimated_cost_usd"] is None:
            print("  Estimate: invalid")
        else:
            print(f"  Estimate: ${quote['estimated_cost_usd']:.2f}")
        projected_label = (
            "invalid"
            if quote["projected_month_usd"] is None
            else f"${quote['projected_month_usd']:.2f}"
        )
        print(
            f"  Month: ${quote['month_spent_usd']:.2f} spent; "
            f"{projected_label} projected / ${quote['monthly_hard_stop_usd']:.2f}"
        )
        print(f"  Reason: {quote['reason']}")
    return int(quote["exit_code"])


def cmd_log(args) -> int:
    """Manual log entry (for testing, integration debugging)."""
    tracker = load_tracker()
    cost = float(args.cost or 0.0)
    query = args.query or "(no description)"
    results = int(args.results or 0)

    if not math.isfinite(cost) or cost < 0:
        print("MONID LOG DENIED: cost must be a finite non-negative number", file=sys.stderr)
        return 1

    projected = float(tracker["month_spent_usd"]) + cost
    violations = []
    if cost > MONID_ABSOLUTE_TASK_CAP_USD:
        violations.append(
            f"actual task cost exceeded ${MONID_ABSOLUTE_TASK_CAP_USD:.2f} hard cap"
        )
    if projected > MONID_MONTHLY_BUDGET_USD:
        violations.append(
            f"actual monthly spend exceeded ${MONID_MONTHLY_BUDGET_USD:.2f} hard stop"
        )

    entry = {
        "ts": now_iso(),
        "query_preview": query[:100],
        "results": results,
        "cost": round(cost, 6),
        "budget_violation": bool(violations),
    }
    tracker["log"].append(entry)
    tracker["month_calls"] += 1
    tracker["month_spent_usd"] = round(tracker["month_spent_usd"] + cost, 4)

    # Trim to last 200 entries
    if len(tracker["log"]) > 200:
        tracker["log"] = tracker["log"][-200:]

    save_tracker(tracker)
    print(f"✓ Logged: {query[:50]} (${cost:.4f})")
    if violations:
        print("HARD-STOP VIOLATION: " + "; ".join(violations), file=sys.stderr)
        return 1
    return 0


def cmd_budget_reset() -> int:
    """Admin: reset month budget (use sparingly)."""
    print("⚠️  Resetting Monid monthly budget...")
    tracker = _new_tracker()
    save_tracker(tracker)
    print(f"✓ Reset to: ${tracker['plan_dollars']:.2f} / {tracker['month_date']}")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Monid AI cost-gating + tracking",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # budget-status
    subparsers.add_parser("budget-status", help="Print current month budget status")

    quote_parser = subparsers.add_parser("quote", help="Quote a paid task before execution")
    quote_parser.add_argument("--task", type=str, default="", help="Task description")
    quote_parser.add_argument(
        "--estimated-cost",
        type=float,
        default=None,
        help=f"Estimated USD cost (default {MONID_DEFAULT_TASK_CAP_USD:.2f})",
    )
    quote_parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")

    # log
    log_parser = subparsers.add_parser("log", help="Log a query result (testing)")
    log_parser.add_argument("--query", type=str, help="Query description")
    log_parser.add_argument("--cost", type=float, help="Actual cost (USD)")
    log_parser.add_argument("--results", type=int, help="Number of results")

    # budget-reset
    subparsers.add_parser("budget-reset", help="[ADMIN] Reset month budget")

    args = parser.parse_args()

    if args.command == "budget-status":
        return cmd_budget_status()
    elif args.command == "quote":
        return cmd_quote(args)
    elif args.command == "log":
        return cmd_log(args)
    elif args.command == "budget-reset":
        return cmd_budget_reset()
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
