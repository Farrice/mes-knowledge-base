#!/usr/bin/env python3
"""monid_client.py — Cost-gating + tracking for Monid AI MCP server.

Monid is accessed primarily via:
  1. claude.ai connector (MCP at https://mcp.monid.ai/v1)
  2. Claude Code (MCP server in .mcp.json)
  3. Codex / CLI (MCP config)

This wrapper:
  - Tracks usage to .agent/monid-usage.json (per-call cost logging)
  - Enforces monthly budget + per-run caps via cost_gate integration
  - Provides CLI commands for budget status, resets, manual logging

Wired via cost_gate_hook.py (PreToolUse Bash hook) — any monid_client.py
invocation is gated before execution.

Cost model: pay-per-call (Monid returns actual cost in response).
Monthly budget: $25.00; per-run default cap: $5.00 (override with approval token).

Usage:
  python3 monid_client.py budget-status
  python3 monid_client.py log --query "trend check" --cost 0.02 --results 15
  python3 monid_client.py budget-reset  # admin: reset mid-month
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRACKER_PATH = ROOT / ".agent" / "monid-usage.json"

MONID_MONTHLY_BUDGET_USD = 25.00
MONID_SOFT_WARN_PERCENT = 0.70
MONID_HARD_STOP_PERCENT = 0.90


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def month_date() -> str:
    """Return YYYY-MM-01 for current calendar month."""
    d = datetime.now(timezone.utc)
    return d.strftime("%Y-%m") + "-01"


def load_tracker() -> dict:
    """Load usage tracker; auto-create if missing."""
    if not TRACKER_PATH.exists():
        return _new_tracker()
    try:
        return json.loads(TRACKER_PATH.read_text())
    except (json.JSONDecodeError, OSError):
        return _new_tracker()


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


def cmd_log(args) -> int:
    """Manual log entry (for testing, integration debugging)."""
    tracker = load_tracker()
    save_tracker(tracker)  # Reset if needed

    cost = float(args.cost or 0.0)
    query = args.query or "(no description)"
    results = int(args.results or 0)

    entry = {
        "ts": now_iso(),
        "query_preview": query[:100],
        "results": results,
        "cost": round(cost, 6),
    }
    tracker["log"].append(entry)
    tracker["month_calls"] += 1
    tracker["month_spent_usd"] = round(tracker["month_spent_usd"] + cost, 4)

    # Trim to last 200 entries
    if len(tracker["log"]) > 200:
        tracker["log"] = tracker["log"][-200:]

    save_tracker(tracker)
    print(f"✓ Logged: {query[:50]} (${cost:.4f})")
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
    elif args.command == "log":
        return cmd_log(args)
    elif args.command == "budget-reset":
        return cmd_budget_reset()
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
