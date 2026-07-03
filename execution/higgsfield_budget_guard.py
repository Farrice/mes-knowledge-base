#!/usr/bin/env python3
"""
Higgsfield credit guard for CLI and MCP generation.

Balanced posture:
  - Prompt-only ideation is free.
  - Per-call estimated spend above 3% of current credits requires --approved.
  - Session soft cap at 8% of current credits requires --approved.
  - Daily hard cap at 15% of current credits blocks unless --override-daily is passed.
  - 2 consecutive failures halt generation until reset-failures.
  - 1 automatic retry max.

Usage:
  python3 execution/higgsfield_budget_guard.py status
  python3 execution/higgsfield_budget_guard.py status --refresh
  python3 execution/higgsfield_budget_guard.py check --operation image_preview --count 3
  python3 execution/higgsfield_budget_guard.py check --operation marketing_studio_video --estimated-credits 42 --approved
  python3 execution/higgsfield_budget_guard.py log --operation image_preview --status success --estimated-credits 12 --actual-credits 10 --job-id abc
  python3 execution/higgsfield_budget_guard.py summary
  python3 execution/higgsfield_budget_guard.py reset-failures
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
TRACKER_PATH = Path(os.environ.get("HIGGSFIELD_USAGE_PATH", ROOT / ".agent" / "higgsfield-usage.json"))

SUCCESS_STATUSES = {"success", "selected", "displayed", "skipped"}
FAILURE_STATUSES = {"failure", "failed", "cancelled", "denied"}
ALL_STATUSES = sorted(SUCCESS_STATUSES | FAILURE_STATUSES)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def load() -> dict[str, Any]:
    if not TRACKER_PATH.exists():
        sys.exit(f"ERROR: tracker not found at {TRACKER_PATH}")
    with TRACKER_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def save(data: dict[str, Any]) -> None:
    with TRACKER_PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def reset_today_if_needed(data: dict[str, Any]) -> None:
    state = data["state"]
    today = today_str()
    if state.get("today_date") != today:
        state["today_date"] = today
        state["today_start_balance_credits"] = float(data["account"].get("current_balance_credits", 0.0))
        state["today_spent_credits"] = 0.0


def ensure_session(data: dict[str, Any]) -> None:
    state = data["state"]
    if not state.get("session_id"):
        state["session_id"] = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        state["session_start_balance_credits"] = float(data["account"].get("current_balance_credits", 0.0))
        state["session_spent_credits"] = 0.0


def prune_recent_calls(data: dict[str, Any]) -> None:
    cutoff = datetime.now(timezone.utc).timestamp() - 300
    fresh: list[str] = []
    for ts in data["state"].get("recent_call_timestamps", []):
        try:
            parsed = datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp()
        except (TypeError, ValueError):
            continue
        if parsed >= cutoff:
            fresh.append(ts)
    data["state"]["recent_call_timestamps"] = fresh


def refresh_account(data: dict[str, Any]) -> None:
    try:
        result = subprocess.run(
            ["higgsfield", "account", "status"],
            check=True,
            capture_output=True,
            text=True,
            timeout=20,
        )
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        sys.exit(f"ERROR: unable to refresh Higgsfield account status: {exc}")

    text = result.stdout.strip()
    match = re.search(r"^(.*?)\s+—\s+(.*?),\s+([0-9]+(?:\.[0-9]+)?)\s+credits", text)
    if not match:
        sys.exit(f"ERROR: could not parse account status: {text}")

    data["account"]["email"] = match.group(1).strip()
    data["account"]["plan"] = match.group(2).strip()
    data["account"]["current_balance_credits"] = float(match.group(3))
    data["account"]["last_refreshed_at"] = now_iso()


def estimate_credits(data: dict[str, Any], operation: str, count: int, explicit: float | None) -> float:
    if explicit is not None:
        return round(float(explicit), 4)

    estimates = data.get("estimates", {})
    if operation not in estimates:
        valid = ", ".join(sorted(estimates.keys()))
        sys.exit(f"ERROR: unknown operation '{operation}'. Use --estimated-credits or one of: {valid}")

    return round(float(estimates[operation]) * max(count, 1), 4)


def limit_values(data: dict[str, Any], balance: float) -> tuple[float, float, float]:
    limits = data["limits"]
    approval = round(balance * float(limits["approval_threshold_pct"]), 4)
    session = round(balance * float(limits["session_soft_cap_pct"]), 4)
    daily = round(balance * float(limits["daily_hard_cap_pct"]), 4)
    return approval, session, daily


def cmd_status(args: argparse.Namespace) -> int:
    data = load()
    if args.refresh:
        refresh_account(data)
    reset_today_if_needed(data)
    ensure_session(data)
    save(data)

    balance = float(data["account"].get("current_balance_credits", 0.0))
    approval, session_cap, daily_cap = limit_values(data, balance)

    print("HIGGSFIELD CREDIT GUARD")
    print(f"  Account: {data['account'].get('email') or 'unknown'}")
    print(f"  Plan: {data['account'].get('plan') or 'unknown'}")
    print(f"  Current balance: {balance:g} credits")
    print(f"  Approval threshold: {approval:g} credits per call")
    print(f"  Session soft cap: {session_cap:g} credits")
    print(f"  Daily hard cap: {daily_cap:g} credits")
    print(f"  Session spent: {float(data['state'].get('session_spent_credits', 0.0)):g} credits")
    print(f"  Today spent: {float(data['state'].get('today_spent_credits', 0.0)):g} credits")
    if data["state"].get("halt_reason"):
        print(f"  Halt: {data['state']['halt_reason']}")
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    data = load()
    if args.refresh:
        refresh_account(data)
    reset_today_if_needed(data)
    ensure_session(data)
    prune_recent_calls(data)

    balance = float(args.balance_credits if args.balance_credits is not None else data["account"].get("current_balance_credits", 0.0))
    estimated = estimate_credits(data, args.operation, args.count, args.estimated_credits)
    approval_threshold, session_cap, daily_cap = limit_values(data, balance)

    blocks: list[str] = []
    approvals: list[str] = []
    warns: list[str] = []
    state = data["state"]
    limits = data["limits"]

    if state.get("halt_reason"):
        blocks.append(f"HALTED: {state['halt_reason']}. Run reset-failures after fixing the issue.")

    if int(state.get("consecutive_failures", 0)) >= int(limits["max_consecutive_failures"]):
        blocks.append(f"BLOCKED: {state['consecutive_failures']} consecutive failures.")

    if len(state.get("recent_call_timestamps", [])) >= int(limits["max_calls_per_5min"]):
        blocks.append(f"BLOCKED: rate limit of {limits['max_calls_per_5min']} generation calls per 5 minutes.")

    if args.retry_count > int(limits["max_auto_retries"]):
        blocks.append(f"BLOCKED: retry count {args.retry_count} exceeds max automatic retry {limits['max_auto_retries']}.")

    if estimated == 0:
        warns.append("Prompt-only or display operation: no credit spend expected.")

    if estimated > approval_threshold and not args.approved:
        approvals.append(
            f"APPROVAL REQUIRED: estimated {estimated:g} credits exceeds per-call threshold "
            f"{approval_threshold:g} credits."
        )

    projected_session = float(state.get("session_spent_credits", 0.0)) + estimated
    if projected_session > session_cap and not args.approved:
        approvals.append(
            f"APPROVAL REQUIRED: session would reach {projected_session:g} credits "
            f"(soft cap {session_cap:g})."
        )

    projected_today = float(state.get("today_spent_credits", 0.0)) + estimated
    if projected_today > daily_cap and not args.override_daily:
        blocks.append(
            f"BLOCKED: today would reach {projected_today:g} credits "
            f"(daily hard cap {daily_cap:g})."
        )

    save(data)

    print("=" * 64)
    if blocks:
        print("HIGGSFIELD CREDIT GUARD: DENIED")
    elif approvals:
        print("HIGGSFIELD CREDIT GUARD: APPROVAL REQUIRED")
    else:
        print("HIGGSFIELD CREDIT GUARD: APPROVED")
    print("=" * 64)
    print(f"  Operation: {args.operation}")
    print(f"  Channel: {args.channel}")
    print(f"  Estimated: {estimated:g} credits")
    print(f"  Balance basis: {balance:g} credits")
    print(f"  Projected session: {projected_session:g} / {session_cap:g} credits")
    print(f"  Projected today: {projected_today:g} / {daily_cap:g} credits")
    for item in warns:
        print(f"  • {item}")
    for item in approvals:
        print(f"  • {item}")
    for item in blocks:
        print(f"  • {item}")

    if blocks:
        return 1
    if approvals:
        return 2
    return 0


def cmd_log(args: argparse.Namespace) -> int:
    data = load()
    if args.refresh_after:
        refresh_account(data)
    reset_today_if_needed(data)
    ensure_session(data)
    prune_recent_calls(data)

    estimated = estimate_credits(data, args.operation, args.count, args.estimated_credits)
    actual = float(args.actual_credits if args.actual_credits is not None else estimated)
    before = args.before_credits
    after = args.after_credits
    if before is not None and after is not None:
        actual = max(0.0, round(float(before) - float(after), 4))
        data["account"]["current_balance_credits"] = float(after)
    elif args.status in SUCCESS_STATUSES and actual > 0:
        data["account"]["current_balance_credits"] = max(
            0.0,
            round(float(data["account"].get("current_balance_credits", 0.0)) - actual, 4),
        )

    status = args.status
    if status in SUCCESS_STATUSES:
        data["state"]["consecutive_failures"] = 0
        data["state"]["halt_reason"] = None
        data["state"]["session_spent_credits"] = round(float(data["state"].get("session_spent_credits", 0.0)) + actual, 4)
        data["state"]["today_spent_credits"] = round(float(data["state"].get("today_spent_credits", 0.0)) + actual, 4)
        if actual > 0:
            data["state"]["recent_call_timestamps"].append(now_iso())
    elif status in FAILURE_STATUSES:
        data["state"]["consecutive_failures"] = int(data["state"].get("consecutive_failures", 0)) + 1
        if data["state"]["consecutive_failures"] >= int(data["limits"]["max_consecutive_failures"]):
            data["state"]["halt_reason"] = f"{data['state']['consecutive_failures']} consecutive Higgsfield failures"
    else:
        sys.exit(f"ERROR: unknown status '{status}'. Use one of: {', '.join(ALL_STATUSES)}")

    run = {
        "timestamp": now_iso(),
        "channel": args.channel,
        "operation": args.operation,
        "status": status,
        "estimated_credits": estimated,
        "actual_credits": round(actual, 4),
        "count": args.count,
        "job_id": args.job_id,
        "output_url": args.output_url,
        "mode": args.mode,
        "notes": args.notes,
    }
    data.setdefault("runs", []).append(run)
    save(data)

    print("HIGGSFIELD CREDIT GUARD: LOGGED")
    print(f"  Status: {status}")
    print(f"  Operation: {args.operation}")
    print(f"  Actual: {actual:g} credits")
    print(f"  Current balance estimate: {float(data['account'].get('current_balance_credits', 0.0)):g} credits")
    return 0


def cmd_summary(_: argparse.Namespace) -> int:
    data = load()
    reset_today_if_needed(data)
    ensure_session(data)

    runs = data.get("runs", [])
    by_operation: dict[str, float] = {}
    for run in runs:
        by_operation[run["operation"]] = by_operation.get(run["operation"], 0.0) + float(run.get("actual_credits", 0.0))

    print("HIGGSFIELD USAGE SUMMARY")
    print(f"  Current balance estimate: {float(data['account'].get('current_balance_credits', 0.0)):g} credits")
    print(f"  Session spent: {float(data['state'].get('session_spent_credits', 0.0)):g} credits")
    print(f"  Today spent: {float(data['state'].get('today_spent_credits', 0.0)):g} credits")
    print(f"  Total logged runs: {len(runs)}")
    if by_operation:
        print("  Spend by operation:")
        for operation, credits in sorted(by_operation.items()):
            print(f"    - {operation}: {credits:g} credits")
    return 0


def cmd_reset_failures(_: argparse.Namespace) -> int:
    data = load()
    data["state"]["consecutive_failures"] = 0
    data["state"]["halt_reason"] = None
    save(data)
    print("HIGGSFIELD CREDIT GUARD: failure circuit reset")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Higgsfield credit guard")
    sub = parser.add_subparsers(dest="command", required=True)

    p_status = sub.add_parser("status")
    p_status.add_argument("--refresh", action="store_true", help="Refresh account balance from `higgsfield account status`")
    p_status.set_defaults(func=cmd_status)

    p_check = sub.add_parser("check")
    p_check.add_argument("--operation", required=True)
    p_check.add_argument("--channel", choices=["cli", "mcp", "prompt"], default="cli")
    p_check.add_argument("--count", type=int, default=1)
    p_check.add_argument("--estimated-credits", type=float)
    p_check.add_argument("--balance-credits", type=float, help="Use this balance for mocked tests or offline checks")
    p_check.add_argument("--retry-count", type=int, default=0)
    p_check.add_argument("--approved", action="store_true", help="User approved approval-required spend")
    p_check.add_argument("--override-daily", action="store_true", help="Explicitly override daily hard cap")
    p_check.add_argument("--refresh", action="store_true", help="Refresh account balance before checking")
    p_check.set_defaults(func=cmd_check)

    p_log = sub.add_parser("log")
    p_log.add_argument("--operation", required=True)
    p_log.add_argument("--channel", choices=["cli", "mcp", "prompt"], default="cli")
    p_log.add_argument("--status", choices=ALL_STATUSES, required=True)
    p_log.add_argument("--count", type=int, default=1)
    p_log.add_argument("--estimated-credits", type=float)
    p_log.add_argument("--actual-credits", type=float)
    p_log.add_argument("--before-credits", type=float)
    p_log.add_argument("--after-credits", type=float)
    p_log.add_argument("--job-id")
    p_log.add_argument("--output-url")
    p_log.add_argument("--mode")
    p_log.add_argument("--notes")
    p_log.add_argument("--refresh-after", action="store_true")
    p_log.set_defaults(func=cmd_log)

    p_summary = sub.add_parser("summary")
    p_summary.set_defaults(func=cmd_summary)

    p_reset = sub.add_parser("reset-failures")
    p_reset.set_defaults(func=cmd_reset_failures)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
