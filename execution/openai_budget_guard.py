#!/usr/bin/env python3
"""openai_budget_guard.py — pre-flight / post-flight budget guard for OpenAI GPT Image.

Cap set by Farrice 2026-09-02: **$15.00 per calendar month**, hard block. Warn at $10.
Mirrors execution/fal_budget_guard.py in shape (check → run → log) but keyed to a
monthly cycle instead of a wallet, because OpenAI bills monthly with no prepaid wallet.

Covers every call to the Scrapes `viz-image-gen` GPT path
(`.claude/skills/viz-image-gen/scripts/generate_image_gpt.py`, invoked directly or via
`render_template.py`) and any future script that hits the OpenAI Images API.

Usage:
  python3 execution/openai_budget_guard.py check  --quality=<low|medium|high|auto> [--n=1] [--size=1024x1024]
  python3 execution/openai_budget_guard.py log    --quality=<...> [--n=1] [--size=...] --status=<success|failed> [--actual-cost=N]
  python3 execution/openai_budget_guard.py status
  python3 execution/openai_budget_guard.py reset-month      # admin only: Farrice's call

Exit codes: 0 = allowed · 1 = DENIED (monthly cap, per-call ceiling, daily cap, rate limit).

Pricing estimates are UNCONFIRMED against OpenAI's 2026 price list — they are the
gpt-image family's published 1024×1024 rates (low ≈ $0.011, medium ≈ $0.042, high ≈ $0.167)
with a 1.5× multiplier for 1536-pixel sizes. Pass `--actual-cost` on `log` whenever the
generator prints a real usage figure; actuals always overwrite estimates in the ledger.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRACKER_PATH = ROOT / ".agent" / "openai-usage.json"

LIMITS = {
    "monthly_block_usd": 15.00,
    "monthly_warn_usd": 10.00,
    "per_day_block_usd": 5.00,
    "per_call_block_usd": 1.00,
    "per_call_warn_usd": 0.30,
    "max_calls_per_5min": 6,
    "max_consecutive_failures": 2,
}

PRICING_USD = {  # per image, 1024x1024; UNCONFIRMED — see docstring
    "low": 0.011,
    "medium": 0.042,
    "high": 0.167,
    "auto": 0.167,  # assume the model picks high
}
SIZE_MULT = {"1024x1024": 1.0, "1536x1024": 1.5, "1024x1536": 1.5, "auto": 1.5}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def month_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m")


def _new_state() -> dict:
    return {
        "_schema": "openai-usage v1",
        "_doc": "OpenAI GPT Image spend. $15/month hard cap (Farrice 2026-09-02). "
                "See execution/openai_budget_guard.py and directives/openai-usage-policy.md.",
        "limits": LIMITS,
        "pricing_estimates_usd": PRICING_USD,
        "totals": {
            "cycle_month": month_str(),
            "month_spent_usd": 0.0,
            "month_calls": 0,
            "today_date": today_str(),
            "today_spent_usd": 0.0,
            "today_calls": 0,
            "lifetime_spent_usd": 0.0,
        },
        "state": {"recent_call_timestamps": [], "consecutive_failures": 0},
        "log": [],
    }


def load() -> dict:
    if not TRACKER_PATH.exists():
        TRACKER_PATH.parent.mkdir(parents=True, exist_ok=True)
        data = _new_state()
        save(data)
        return data
    with TRACKER_PATH.open() as f:
        return json.load(f)


def save(data: dict) -> None:
    with TRACKER_PATH.open("w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def roll_periods(data: dict) -> None:
    t = data["totals"]
    if t.get("cycle_month") != month_str():
        t["cycle_month"] = month_str()
        t["month_spent_usd"] = 0.0
        t["month_calls"] = 0
    if t.get("today_date") != today_str():
        t["today_date"] = today_str()
        t["today_spent_usd"] = 0.0
        t["today_calls"] = 0


def prune_recent(data: dict) -> None:
    cutoff = datetime.now(timezone.utc).timestamp() - 300
    fresh = []
    for ts in data["state"].get("recent_call_timestamps", []):
        try:
            if datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp() >= cutoff:
                fresh.append(ts)
        except ValueError:
            continue
    data["state"]["recent_call_timestamps"] = fresh


def estimate(quality: str, n: int, size: str) -> float:
    q = PRICING_USD.get(quality, PRICING_USD["high"])
    return round(q * SIZE_MULT.get(size, 1.5) * max(n, 1), 4)


def cmd_check(args) -> int:
    data = load()
    roll_periods(data)
    prune_recent(data)
    est = estimate(args.quality, args.n, args.size)
    t = data["totals"]
    lim = data.get("limits", LIMITS)
    problems, warnings = [], []

    if est > lim["per_call_block_usd"]:
        problems.append(f"per-call estimate ${est:.3f} > ceiling ${lim['per_call_block_usd']:.2f} (lower --quality or --n)")
    elif est > lim["per_call_warn_usd"]:
        warnings.append(f"per-call estimate ${est:.3f} above warn ${lim['per_call_warn_usd']:.2f}")
    if t["month_spent_usd"] + est > lim["monthly_block_usd"]:
        problems.append(f"monthly cap: ${t['month_spent_usd']:.2f} spent + ${est:.3f} > ${lim['monthly_block_usd']:.2f} for {t['cycle_month']}")
    elif t["month_spent_usd"] + est > lim["monthly_warn_usd"]:
        warnings.append(f"month at ${t['month_spent_usd'] + est:.2f} of ${lim['monthly_block_usd']:.2f}")
    if t["today_spent_usd"] + est > lim["per_day_block_usd"]:
        problems.append(f"daily cap: ${t['today_spent_usd']:.2f} + ${est:.3f} > ${lim['per_day_block_usd']:.2f}")
    if len(data["state"]["recent_call_timestamps"]) >= lim["max_calls_per_5min"]:
        problems.append(f"rate limit: {lim['max_calls_per_5min']} calls in 5 minutes")
    if data["state"].get("consecutive_failures", 0) >= lim["max_consecutive_failures"]:
        problems.append(f"{data['state']['consecutive_failures']} consecutive failures — fix the cause, then `log --status=success` or `reset-month`")

    save(data)
    if problems:
        print("❌ OPENAI BUDGET GUARD — DENIED")
        for p in problems:
            print(f"   • {p}")
        print(f"   Month {t['cycle_month']}: ${t['month_spent_usd']:.2f} / ${lim['monthly_block_usd']:.2f} · today ${t['today_spent_usd']:.2f} / ${lim['per_day_block_usd']:.2f}")
        return 1
    print(f"✅ OPENAI BUDGET GUARD — OK (est ${est:.3f}; quality={args.quality} n={args.n} size={args.size})")
    print(f"   Month {t['cycle_month']}: ${t['month_spent_usd']:.2f} / ${lim['monthly_block_usd']:.2f} · today ${t['today_spent_usd']:.2f} / ${lim['per_day_block_usd']:.2f}")
    for w in warnings:
        print(f"   ⚠ {w}")
    print("   After the call: python3 execution/openai_budget_guard.py log --quality=%s --n=%d --size=%s --status=success [--actual-cost=N]"
          % (args.quality, args.n, args.size))
    return 0


def cmd_log(args) -> int:
    data = load()
    roll_periods(data)
    prune_recent(data)
    cost = args.actual_cost if args.actual_cost is not None else estimate(args.quality, args.n, args.size)
    ok = args.status == "success"
    t = data["totals"]
    if ok:
        t["month_spent_usd"] = round(t["month_spent_usd"] + cost, 4)
        t["today_spent_usd"] = round(t["today_spent_usd"] + cost, 4)
        t["lifetime_spent_usd"] = round(t.get("lifetime_spent_usd", 0.0) + cost, 4)
        t["month_calls"] += 1
        t["today_calls"] += 1
        data["state"]["consecutive_failures"] = 0
    else:
        data["state"]["consecutive_failures"] = data["state"].get("consecutive_failures", 0) + 1
    data["state"]["recent_call_timestamps"].append(now_iso())
    data["log"].append({
        "ts": now_iso(), "quality": args.quality, "n": args.n, "size": args.size,
        "status": args.status, "cost_usd": round(cost, 4),
        "cost_source": "actual" if args.actual_cost is not None else "estimate",
        "note": args.note or "",
    })
    data["log"] = data["log"][-200:]
    save(data)
    print(f"📒 logged {args.status} ${cost:.3f} → month ${t['month_spent_usd']:.2f} / ${data['limits']['monthly_block_usd']:.2f}")
    return 0


def cmd_status(_args) -> int:
    data = load()
    roll_periods(data)
    save(data)
    t, lim = data["totals"], data["limits"]
    print(f"OpenAI GPT Image — month {t['cycle_month']}: ${t['month_spent_usd']:.2f} / ${lim['monthly_block_usd']:.2f} "
          f"({t['month_calls']} calls) · today ${t['today_spent_usd']:.2f} / ${lim['per_day_block_usd']:.2f} · lifetime ${t.get('lifetime_spent_usd', 0):.2f}")
    for e in data["log"][-5:]:
        print(f"  {e['ts']} {e['status']:8} ${e['cost_usd']:.3f} {e['quality']}/{e['n']}/{e['size']} ({e['cost_source']})")
    return 0


def cmd_reset_month(_args) -> int:
    data = load()
    data["totals"].update({"cycle_month": month_str(), "month_spent_usd": 0.0, "month_calls": 0})
    data["state"]["consecutive_failures"] = 0
    save(data)
    print("month counters reset (admin)")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="OpenAI GPT Image budget guard ($15/month cap).")
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("check", "log"):
        s = sub.add_parser(name)
        s.add_argument("--quality", default="high", choices=list(PRICING_USD))
        s.add_argument("--n", type=int, default=1)
        s.add_argument("--size", default="1024x1024", choices=list(SIZE_MULT))
        if name == "log":
            s.add_argument("--status", required=True, choices=["success", "failed"])
            s.add_argument("--actual-cost", type=float, default=None)
            s.add_argument("--note", default="")
    sub.add_parser("status")
    sub.add_parser("reset-month")
    args = p.parse_args()
    return {"check": cmd_check, "log": cmd_log, "status": cmd_status, "reset-month": cmd_reset_month}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
