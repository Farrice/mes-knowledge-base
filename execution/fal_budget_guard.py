#!/usr/bin/env python3
"""
Fal API budget guard for fantastic-posters skill.

Wallet model: $20 funded, refills when balance drops below $5 (rolling $15-20 budget).
Multi-layer safeguards prevent runaway spend:
  1. Per-call ceiling      — block any single call estimated > $1.00
  2. Per-day ceiling       — block once today's spend hits $4.00
  3. Per-cycle ceiling     — block once cycle spend hits $15.00 (preserves $5 refill buffer)
  4. Low-balance mode      — when balance < $5, only allow calls < $0.50
  5. Rate limit            — max 5 calls per 5 minutes (catches accidental loops)
  6. Failure circuit       — halt after 2 consecutive failures (probably config error)

Usage:
  python3 fal_budget_guard.py check --quality=low --n=1 [--brief="..."]
  python3 fal_budget_guard.py log --quality=low --n=1 --status=success [--actual-cost=0.011]
  python3 fal_budget_guard.py status
  python3 fal_budget_guard.py refill-confirm   # call after you fund the Fal wallet
  python3 fal_budget_guard.py reset-failures   # clear consecutive failure counter
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRACKER_PATH = ROOT / ".agent" / "fal-usage.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def load() -> dict:
    if not TRACKER_PATH.exists():
        sys.exit(f"ERROR: tracker not found at {TRACKER_PATH}")
    with TRACKER_PATH.open() as f:
        return json.load(f)


def save(data: dict) -> None:
    with TRACKER_PATH.open("w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def reset_today_if_needed(data: dict) -> None:
    if data["totals"]["today_date"] != today_str():
        data["totals"]["today_date"] = today_str()
        data["totals"]["today_calls"] = 0
        data["totals"]["today_spent_usd"] = 0.00


def estimate_cost(quality: str, n: int) -> float:
    data = load()
    price = data["pricing_estimates_usd"].get(quality)
    if price is None:
        sys.exit(f"ERROR: unknown quality '{quality}'. Use low|medium|high.")
    return round(price * n, 4)


def prune_old_timestamps(data: dict) -> None:
    """Keep only timestamps from the last 5 minutes for rate-limit check."""
    now = datetime.now(timezone.utc).timestamp()
    cutoff = now - 300  # 5 minutes
    fresh = []
    for ts in data["state"]["recent_call_timestamps"]:
        try:
            t = datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp()
            if t >= cutoff:
                fresh.append(ts)
        except (ValueError, TypeError):
            continue
    data["state"]["recent_call_timestamps"] = fresh


# ─────────────────────────────────────────────────────────────────
# CHECK — pre-flight gate
# ─────────────────────────────────────────────────────────────────
def cmd_check(args) -> int:
    data = load()
    reset_today_if_needed(data)
    prune_old_timestamps(data)

    estimated = estimate_cost(args.quality, args.n)
    limits = data["limits"]
    state = data["state"]
    totals = data["totals"]
    wallet = data["wallet"]

    blocks = []
    warns = []

    # 0. Halt circuit
    if state.get("halt_reason"):
        blocks.append(f"HALTED: {state['halt_reason']}. Run `reset-failures` after fixing config.")

    # 1. Consecutive failures
    if state["consecutive_failures"] >= limits["max_consecutive_failures"]:
        blocks.append(
            f"BLOCKED: {state['consecutive_failures']} consecutive failures. "
            f"Likely config error. Run `reset-failures` after diagnosing."
        )

    # 2. Rate limit
    if len(state["recent_call_timestamps"]) >= limits["max_calls_per_5min"]:
        blocks.append(
            f"BLOCKED: rate limit ({limits['max_calls_per_5min']} calls / 5 min). "
            f"Wait or investigate loop."
        )

    # 3. Per-call ceiling
    if estimated > limits["per_call_block_usd"]:
        blocks.append(
            f"BLOCKED: estimated ${estimated:.3f} exceeds per-call ceiling "
            f"${limits['per_call_block_usd']:.2f}. Lower quality or reduce --n."
        )
    elif estimated > limits["per_call_warn_usd"]:
        warns.append(f"WARN: single call ~${estimated:.3f} (>${limits['per_call_warn_usd']:.2f}).")

    # 4. Daily cap
    projected_today = totals["today_spent_usd"] + estimated
    if projected_today > limits["per_day_block_usd"]:
        blocks.append(
            f"BLOCKED: today's spend would hit ${projected_today:.2f} "
            f"(daily cap ${limits['per_day_block_usd']:.2f})."
        )
    elif projected_today > limits["per_day_warn_usd"]:
        warns.append(
            f"WARN: today's spend would hit ${projected_today:.2f} "
            f"(daily warn ${limits['per_day_warn_usd']:.2f})."
        )

    # 5. Cycle cap
    projected_cycle = totals["current_cycle_spent_usd"] + estimated
    if projected_cycle > limits["per_cycle_block_usd"]:
        blocks.append(
            f"BLOCKED: cycle spend would hit ${projected_cycle:.2f} "
            f"(cycle cap ${limits['per_cycle_block_usd']:.2f}, preserves "
            f"${wallet['refill_threshold']:.0f} refill buffer)."
        )
    elif projected_cycle > limits["per_cycle_warn_usd"]:
        warns.append(
            f"WARN: cycle spend would hit ${projected_cycle:.2f} "
            f"(cycle warn ${limits['per_cycle_warn_usd']:.2f})."
        )

    # 6. Low balance mode
    if wallet["current_balance_estimate"] < wallet["refill_threshold"]:
        if estimated > limits["low_balance_max_call_usd"]:
            blocks.append(
                f"BLOCKED: low-balance mode (est. ${wallet['current_balance_estimate']:.2f} "
                f"< ${wallet['refill_threshold']:.0f}). Single call must be "
                f"≤ ${limits['low_balance_max_call_usd']:.2f}; this is ${estimated:.3f}."
            )
        else:
            warns.append(
                f"NOTE: low-balance mode active (~${wallet['current_balance_estimate']:.2f}). "
                f"Refill expected from Fal."
            )

    # ─── Verdict ───
    if blocks:
        print("=" * 60)
        print("FAL BUDGET GUARD: ❌ DENIED")
        print("=" * 60)
        for b in blocks:
            print(f"  • {b}")
        if warns:
            print("\nAlso noted:")
            for w in warns:
                print(f"  • {w}")
        print(f"\nEstimated cost of this call: ${estimated:.4f}")
        print(f"Cycle spent: ${totals['current_cycle_spent_usd']:.2f} / ${limits['per_cycle_block_usd']:.2f}")
        print(f"Today spent: ${totals['today_spent_usd']:.2f} / ${limits['per_day_block_usd']:.2f}")
        return 1

    print("=" * 60)
    print(f"FAL BUDGET GUARD: ✅ ALLOWED — est. ${estimated:.4f}")
    print("=" * 60)
    if warns:
        for w in warns:
            print(f"  • {w}")
    print(f"Cycle spent: ${totals['current_cycle_spent_usd']:.2f} / ${limits['per_cycle_block_usd']:.2f}")
    print(f"Today spent: ${totals['today_spent_usd']:.2f} / ${limits['per_day_block_usd']:.2f}")
    print(f"Wallet est: ${wallet['current_balance_estimate']:.2f}")
    print(f"\nAfter `node generate.js`, run:")
    print(f"  python3 execution/fal_budget_guard.py log --quality={args.quality} --n={args.n} --status=success")
    return 0


# ─────────────────────────────────────────────────────────────────
# LOG — post-flight record
# ─────────────────────────────────────────────────────────────────
def cmd_log(args) -> int:
    data = load()
    reset_today_if_needed(data)
    prune_old_timestamps(data)

    estimated = estimate_cost(args.quality, args.n)
    actual = args.actual_cost if args.actual_cost is not None else estimated

    # Update state
    state = data["state"]
    if args.status == "success":
        state["consecutive_failures"] = 0
        # Bill it
        data["totals"]["lifetime_calls"] += 1
        data["totals"]["lifetime_spent_usd"] = round(data["totals"]["lifetime_spent_usd"] + actual, 4)
        data["totals"]["current_cycle_calls"] += 1
        data["totals"]["current_cycle_spent_usd"] = round(
            data["totals"]["current_cycle_spent_usd"] + actual, 4
        )
        data["totals"]["today_calls"] += 1
        data["totals"]["today_spent_usd"] = round(data["totals"]["today_spent_usd"] + actual, 4)
        data["wallet"]["current_balance_estimate"] = round(
            data["wallet"]["current_balance_estimate"] - actual, 4
        )
    elif args.status == "failed":
        state["consecutive_failures"] += 1
        if args.fal_billed:
            # Even on failure, if Fal billed us, count it
            data["totals"]["lifetime_spent_usd"] = round(data["totals"]["lifetime_spent_usd"] + actual, 4)
            data["totals"]["current_cycle_spent_usd"] = round(
                data["totals"]["current_cycle_spent_usd"] + actual, 4
            )
            data["totals"]["today_spent_usd"] = round(data["totals"]["today_spent_usd"] + actual, 4)
            data["wallet"]["current_balance_estimate"] = round(
                data["wallet"]["current_balance_estimate"] - actual, 4
            )
        if state["consecutive_failures"] >= data["limits"]["max_consecutive_failures"]:
            state["halt_reason"] = (
                f"{state['consecutive_failures']} consecutive failures at {now_iso()}"
            )

    state["recent_call_timestamps"].append(now_iso())

    # Append log
    data["log"].append({
        "ts": now_iso(),
        "brief": args.brief or "",
        "style": args.style or "auto",
        "quality": args.quality,
        "n": args.n,
        "estimated_cost_usd": estimated,
        "actual_cost_usd": actual,
        "status": args.status,
        "fal_billed": args.fal_billed,
        "output_path": args.output_path or "",
    })

    save(data)
    print(f"Logged: {args.status}, ${actual:.4f}, cycle total ${data['totals']['current_cycle_spent_usd']:.2f}")
    if state.get("halt_reason"):
        print(f"⚠️  HALTED: {state['halt_reason']}")
    return 0


# ─────────────────────────────────────────────────────────────────
# STATUS
# ─────────────────────────────────────────────────────────────────
def cmd_status(_args) -> int:
    data = load()
    reset_today_if_needed(data)
    save(data)
    w = data["wallet"]
    t = data["totals"]
    l = data["limits"]
    s = data["state"]
    print("─" * 60)
    print("FAL BUDGET GUARD — STATUS")
    print("─" * 60)
    print(f"Wallet (estimated):  ${w['current_balance_estimate']:.2f} / ${w['funded_total']:.2f}")
    print(f"Refill threshold:    ${w['refill_threshold']:.2f}  (auto-refill: {w['auto_refill']})")
    print(f"Cycle started:       {w['cycle_started_at']}")
    print()
    print(f"Cycle spent:         ${t['current_cycle_spent_usd']:.2f} / ${l['per_cycle_block_usd']:.2f}  (warn at ${l['per_cycle_warn_usd']:.2f})")
    print(f"Today spent:         ${t['today_spent_usd']:.2f} / ${l['per_day_block_usd']:.2f}  (warn at ${l['per_day_warn_usd']:.2f})")
    print(f"Lifetime spent:      ${t['lifetime_spent_usd']:.2f}  ({t['lifetime_calls']} calls)")
    print()
    print(f"Per-call block:      ${l['per_call_block_usd']:.2f}  (warn at ${l['per_call_warn_usd']:.2f})")
    print(f"Low-balance cap:     ${l['low_balance_max_call_usd']:.2f}/call when balance < ${w['refill_threshold']:.2f}")
    print(f"Rate limit:          {l['max_calls_per_5min']} calls / 5 min")
    print(f"Consecutive fails:   {s['consecutive_failures']} / {l['max_consecutive_failures']}")
    if s.get("halt_reason"):
        print(f"⚠️  HALTED:           {s['halt_reason']}")
    print()
    if data["log"]:
        print(f"Last 3 calls:")
        for entry in data["log"][-3:]:
            print(f"  {entry['ts']}  {entry['quality']:6s} n={entry['n']}  ${entry['actual_cost_usd']:.4f}  {entry['status']}")
    else:
        print("No calls logged yet.")
    return 0


# ─────────────────────────────────────────────────────────────────
# REFILL CONFIRM — call after Fal auto-refill happens
# ─────────────────────────────────────────────────────────────────
def cmd_refill_confirm(_args) -> int:
    data = load()
    data["wallet"]["current_balance_estimate"] = data["wallet"]["funded_total"]
    data["wallet"]["last_refill_confirmed_at"] = now_iso()
    data["wallet"]["cycle_started_at"] = now_iso()
    data["totals"]["current_cycle_calls"] = 0
    data["totals"]["current_cycle_spent_usd"] = 0.00
    save(data)
    print(f"✅ Refill confirmed. Cycle reset. Wallet: ${data['wallet']['funded_total']:.2f}")
    return 0


def cmd_reset_failures(_args) -> int:
    data = load()
    data["state"]["consecutive_failures"] = 0
    data["state"]["halt_reason"] = None
    data["state"]["halt_until"] = None
    save(data)
    print("✅ Failure counter reset. Halt cleared.")
    return 0


# ─────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────
def main() -> int:
    p = argparse.ArgumentParser(description="Fal API budget guard for fantastic-posters")
    sub = p.add_subparsers(dest="cmd", required=True)

    pc = sub.add_parser("check", help="Pre-flight: gate this call against budget rules")
    pc.add_argument("--quality", required=True, choices=["low", "medium", "high"])
    pc.add_argument("--n", type=int, default=1)
    pc.add_argument("--brief", default="")

    pl = sub.add_parser("log", help="Post-flight: record actual spend")
    pl.add_argument("--quality", required=True, choices=["low", "medium", "high"])
    pl.add_argument("--n", type=int, default=1)
    pl.add_argument("--status", required=True, choices=["success", "failed"])
    pl.add_argument("--actual-cost", type=float, default=None)
    pl.add_argument("--brief", default="")
    pl.add_argument("--style", default="")
    pl.add_argument("--output-path", default="")
    pl.add_argument("--fal-billed", action="store_true",
                    help="If failed but Fal billed us anyway, set this to count the spend.")

    sub.add_parser("status", help="Show current budget state")
    sub.add_parser("refill-confirm", help="Confirm Fal auto-refill happened; reset cycle counters")
    sub.add_parser("reset-failures", help="Clear consecutive-failure counter and halt state")

    args = p.parse_args()
    return {
        "check": cmd_check,
        "log": cmd_log,
        "status": cmd_status,
        "refill-confirm": cmd_refill_confirm,
        "reset-failures": cmd_reset_failures,
    }[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
