#!/usr/bin/env python3
"""
Fal API budget guard for fantastic-posters skill (v2 — mode-aware).

Wallet model: $20 funded, refills when balance drops below $5 (rolling $15-20 budget).

Modes (each with its own per-call ceiling):
  - poster              | GPT Image 2 text-to-image     | ceiling $1.00
  - edit                | GPT Image 2 image-to-image    | ceiling $1.00
  - rembg               | fal-ai/imageutils/rembg       | ceiling $0.10  (chained transparency)
  - kling               | Kling v3 Pro video            | ceiling $2.00
  - seedance-480p       | Seedance 2.0 480p video       | ceiling $1.50
  - seedance-720p       | Seedance 2.0 720p video       | ceiling $3.00
  - seedance-1080p      | Seedance 2.0 1080p video      | HARD-BLOCKED (null ceiling)

Multi-layer safeguards:
  1. Per-call ceiling      — mode-specific (above)
  2. Per-day block         — $6.00 across all modes (raised from $4 to fit video)
  3. Per-cycle block       — $15.00 (preserves $5 refill buffer)
  4. Low-balance cap       — $0.50/call when wallet < $5
  5. Rate limit            — 5 calls / 5 min
  6. Failure circuit       — halt after 2 consecutive failures

Usage (poster — backward compatible):
  python3 fal_budget_guard.py check --quality=low --n=1
  python3 fal_budget_guard.py log --quality=low --n=1 --status=success

Usage (poster — explicit mode):
  python3 fal_budget_guard.py check --mode=poster --quality=high --n=1

Usage (Kling video):
  python3 fal_budget_guard.py check --mode=kling --duration=5 --audio=on
  python3 fal_budget_guard.py log --mode=kling --duration=5 --audio=on --status=success --actual-cost=0.84

Usage (Seedance video):
  python3 fal_budget_guard.py check --mode=seedance-720p --duration=8
  python3 fal_budget_guard.py log --mode=seedance-720p --duration=8 --status=success --actual-cost=2.42

Other commands:
  python3 fal_budget_guard.py status
  python3 fal_budget_guard.py refill-confirm   # call after Fal auto-refill
  python3 fal_budget_guard.py reset-failures   # clear consecutive failure halt
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRACKER_PATH = ROOT / ".agent" / "fal-usage.json"

POSTER_MODES = {"poster", "edit"}
UTILITY_MODES = {"rembg"}  # Chained image-utility calls (background removal, etc.)
VIDEO_MODES = {"kling", "seedance-480p", "seedance-720p", "seedance-1080p"}
# generic: recipe-driven calls from execution/generate_media.py (audio, recraft,
# any wrapper-less Fal model). Cost is computed upstream from the model recipe's
# pricing table and passed via --est-cost; ceiling $1.00/call — a model that
# needs more must graduate to its own named mode (deliberate friction).
GENERIC_MODES = {"generic"}
ALL_MODES = POSTER_MODES | UTILITY_MODES | VIDEO_MODES | GENERIC_MODES


STALE_THRESHOLD_DAYS = 30


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _days_since(iso_str: str) -> float | None:
    try:
        t = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return (datetime.now(timezone.utc) - t).total_seconds() / 86400
    except (ValueError, TypeError):
        return None


def stale_state_warning(data: dict) -> str | None:
    """Detect a tracker that hasn't recorded a real call/refill in a while.

    Root cause this guards against: the wallet balance / cycle totals below are only
    as fresh as the last `log` call. If generations happen through a path that never
    calls `log` (the exact gap this file was patched to close in generate.js /
    fal_video_kling.py / fal_video_seedance.py), the tracker silently rots — it will
    keep reporting a balance/cycle-spend that has nothing to do with reality. Rather
    than silently enforcing budget rules against frozen numbers, say so loudly.
    """
    log = data.get("log") or []
    last_ts = log[-1]["ts"] if log else data.get("wallet", {}).get("last_refill_confirmed_at")
    if not last_ts:
        return None
    age = _days_since(last_ts)
    if age is not None and age > STALE_THRESHOLD_DAYS:
        bal = data.get("wallet", {}).get("current_balance_estimate")
        bal_str = f"${bal:.2f}" if bal is not None else "unknown"
        return (
            f"STATE STALE — last recorded call/refill was {age:.0f} days ago ({last_ts}). "
            f"Balance estimate ({bal_str}) and cycle/day totals below are UNRELIABLE — verify "
            f"the actual wallet balance at fal.ai before trusting this gate's numbers, then run "
            f"`refill-confirm` (if a refill actually happened) to resync the cycle."
        )
    return None


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
        data["totals"]["today_spent_by_mode"] = {"poster": 0.0, "edit": 0.0, "rembg": 0.0, "kling": 0.0, "seedance": 0.0, "generic": 0.0}


def prune_old_timestamps(data: dict) -> None:
    """Keep only timestamps from the last 5 minutes for rate-limit check."""
    now = datetime.now(timezone.utc).timestamp()
    cutoff = now - 300
    fresh = []
    for ts in data["state"]["recent_call_timestamps"]:
        try:
            t = datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp()
            if t >= cutoff:
                fresh.append(ts)
        except (ValueError, TypeError):
            continue
    data["state"]["recent_call_timestamps"] = fresh


def mode_aggregate_key(mode: str) -> str:
    """Map specific mode to aggregate bucket: seedance-720p → 'seedance', kling → 'kling'."""
    if mode.startswith("seedance"):
        return "seedance"
    return mode  # poster, edit, rembg, kling


def estimate_cost(mode: str, *, quality: str | None = None, n: int = 1,
                  duration: int | None = None, audio: str | None = None,
                  est_cost: float | None = None) -> float:
    """Estimate cost in USD for a given call configuration.

    For poster/edit: requires quality (low/medium/high) and n.
    For kling: requires duration (3-15) and audio (off/on/voice_control).
    For seedance-*: requires duration (4-15). Resolution is encoded in mode.
    For generic: requires est_cost (computed upstream from the model recipe).
    """
    if mode in GENERIC_MODES:
        if est_cost is None:
            sys.exit("ERROR: mode=generic requires --est-cost (from the model recipe pricing table)")
        return round(est_cost, 4)

    data = load()
    pricing = data["pricing_estimates_usd"]

    if mode in POSTER_MODES:
        if quality is None:
            sys.exit(f"ERROR: mode={mode} requires --quality")
        price = pricing[mode].get(quality)
        if price is None:
            sys.exit(f"ERROR: unknown quality '{quality}' for mode={mode}. Use low|medium|high.")
        return round(price * n, 4)

    if mode == "rembg":
        # Flat per-call pricing — no quality tier. Quality flag (if passed) is ignored.
        per_call = pricing.get("rembg", {}).get("per_call", 0.005)
        return round(per_call * n, 4)

    if mode == "kling":
        if duration is None:
            sys.exit("ERROR: mode=kling requires --duration")
        audio = audio or "on"
        per_sec_map = pricing["kling_per_second"]
        key = {"off": "audio_off", "on": "audio_on", "voice_control": "voice_control"}.get(audio)
        if key is None:
            sys.exit(f"ERROR: unknown audio '{audio}'. Use off|on|voice_control.")
        return round(per_sec_map[key] * duration, 4)

    if mode in {"seedance-480p", "seedance-720p", "seedance-1080p"}:
        if duration is None:
            sys.exit(f"ERROR: mode={mode} requires --duration")
        res_key = mode.split("-")[1]  # 480p / 720p / 1080p
        per_sec = pricing["seedance_per_second"][res_key]
        return round(per_sec * duration, 4)

    sys.exit(f"ERROR: unknown mode '{mode}'. Valid: {sorted(ALL_MODES)}")


# ─────────────────────────────────────────────────────────────────
# CHECK — pre-flight gate
# ─────────────────────────────────────────────────────────────────
def cmd_check(args) -> int:
    data = load()
    reset_today_if_needed(data)
    prune_old_timestamps(data)

    mode = args.mode

    # Hard-block 1080p Seedance — no override path
    if mode == "seedance-1080p":
        print("=" * 60)
        print("FAL BUDGET GUARD: ❌ DENIED (HARD-BLOCKED)")
        print("=" * 60)
        print("  • mode=seedance-1080p is hard-blocked. Single 15s call costs ~$10.21 (50% of wallet).")
        print("  • Use --mode=seedance-720p instead (max ~$4.54 for 15s, ceiling $3.00 → ~10s max).")
        print("  • If you genuinely need 1080p, edit fal_budget_guard.py limits — runtime override is intentionally absent.")
        print("  • Policy: directives/fal-usage-policy.md")
        return 1

    estimated = estimate_cost(
        mode,
        quality=args.quality,
        n=args.n,
        duration=args.duration,
        audio=args.audio,
        est_cost=args.est_cost,
    )

    limits = data["limits"]
    state = data["state"]
    totals = data["totals"]
    wallet = data["wallet"]
    per_call_ceilings = limits["per_call_block_usd_by_mode"]
    mode_ceiling = per_call_ceilings.get(mode)
    if mode_ceiling is None:
        # Already handled 1080p above; this catches any future null entries.
        print(f"❌ DENIED: mode={mode} has no ceiling configured (hard-block).")
        return 1

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

    # 3. Per-call ceiling (mode-aware)
    if estimated > mode_ceiling:
        blocks.append(
            f"BLOCKED: estimated ${estimated:.3f} exceeds per-call ceiling for "
            f"mode={mode} (${mode_ceiling:.2f}). Lower duration/quality or pick a cheaper mode."
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
    stale = stale_state_warning(data)
    if stale:
        print("!" * 60)
        print(f"⚠️  {stale}")
        print("!" * 60)

    if blocks:
        print("=" * 60)
        print(f"FAL BUDGET GUARD: ❌ DENIED  (mode={mode}, est=${estimated:.4f})")
        print("=" * 60)
        for b in blocks:
            print(f"  • {b}")
        if warns:
            print("\nAlso noted:")
            for w in warns:
                print(f"  • {w}")
        print(f"\nMode ceiling for {mode}: ${mode_ceiling:.2f}")
        print(f"Cycle spent: ${totals['current_cycle_spent_usd']:.2f} / ${limits['per_cycle_block_usd']:.2f}")
        print(f"Today spent: ${totals['today_spent_usd']:.2f} / ${limits['per_day_block_usd']:.2f}")
        return 1

    print("=" * 60)
    print(f"FAL BUDGET GUARD: ✅ ALLOWED  (mode={mode}, est=${estimated:.4f})")
    print("=" * 60)
    if warns:
        for w in warns:
            print(f"  • {w}")
    print(f"Mode ceiling: ${mode_ceiling:.2f}")
    print(f"Cycle spent: ${totals['current_cycle_spent_usd']:.2f} / ${limits['per_cycle_block_usd']:.2f}")
    print(f"Today spent: ${totals['today_spent_usd']:.2f} / ${limits['per_day_block_usd']:.2f}")
    print(f"Wallet est:  ${wallet['current_balance_estimate']:.2f}")
    print(f"\nAfter the call, run:")
    print(f"  python3 execution/fal_budget_guard.py log --mode={mode} ...args... --status=success [--actual-cost=N]")
    return 0


# ─────────────────────────────────────────────────────────────────
# LOG — post-flight record
# ─────────────────────────────────────────────────────────────────
def cmd_log(args) -> int:
    data = load()
    reset_today_if_needed(data)
    prune_old_timestamps(data)

    mode = args.mode

    if mode == "seedance-1080p":
        # Should never reach log for blocked mode, but guard anyway
        print("ERROR: cannot log mode=seedance-1080p (hard-blocked, should not have run).")
        return 1

    estimated = estimate_cost(
        mode,
        quality=args.quality,
        n=args.n,
        duration=args.duration,
        audio=args.audio,
        est_cost=args.est_cost,
    )
    actual = args.actual_cost if args.actual_cost is not None else estimated

    state = data["state"]
    agg_key = mode_aggregate_key(mode)

    if args.status == "success":
        state["consecutive_failures"] = 0
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
        # Per-mode aggregates
        for bucket in ("today_spent_by_mode", "cycle_spent_by_mode", "lifetime_spent_by_mode"):
            data["totals"][bucket][agg_key] = round(data["totals"][bucket].get(agg_key, 0.0) + actual, 4)

    elif args.status == "failed":
        state["consecutive_failures"] += 1
        if args.fal_billed:
            data["totals"]["lifetime_spent_usd"] = round(data["totals"]["lifetime_spent_usd"] + actual, 4)
            data["totals"]["current_cycle_spent_usd"] = round(
                data["totals"]["current_cycle_spent_usd"] + actual, 4
            )
            data["totals"]["today_spent_usd"] = round(data["totals"]["today_spent_usd"] + actual, 4)
            data["wallet"]["current_balance_estimate"] = round(
                data["wallet"]["current_balance_estimate"] - actual, 4
            )
            for bucket in ("today_spent_by_mode", "cycle_spent_by_mode", "lifetime_spent_by_mode"):
                data["totals"][bucket][agg_key] = round(data["totals"][bucket].get(agg_key, 0.0) + actual, 4)
        if state["consecutive_failures"] >= data["limits"]["max_consecutive_failures"]:
            state["halt_reason"] = (
                f"{state['consecutive_failures']} consecutive failures at {now_iso()}"
            )

    state["recent_call_timestamps"].append(now_iso())

    # Append log
    entry = {
        "ts": now_iso(),
        "mode": mode,
        "brief": args.brief or "",
        "estimated_cost_usd": estimated,
        "actual_cost_usd": actual,
        "status": args.status,
        "fal_billed": args.fal_billed,
        "output_path": args.output_path or "",
    }
    if mode in POSTER_MODES:
        entry["quality"] = args.quality
        entry["n"] = args.n
        entry["style"] = args.style or ""
    elif mode == "rembg":
        entry["n"] = args.n
    elif mode == "kling":
        entry["duration"] = args.duration
        entry["audio"] = args.audio or "on"
    elif mode.startswith("seedance"):
        entry["duration"] = args.duration
        entry["resolution"] = mode.split("-")[1]
        entry["audio"] = args.audio or "on"
    elif mode in GENERIC_MODES:
        entry["model"] = args.model or ""

    data["log"].append(entry)
    save(data)

    print(f"Logged: mode={mode}, {args.status}, ${actual:.4f}")
    print(f"  Cycle total: ${data['totals']['current_cycle_spent_usd']:.2f} / ${data['limits']['per_cycle_block_usd']:.2f}")
    print(f"  Cycle by mode: {data['totals']['cycle_spent_by_mode']}")
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
    print("─" * 64)
    print("FAL BUDGET GUARD — STATUS  (v2 mode-aware)")
    print("─" * 64)
    stale = stale_state_warning(data)
    if stale:
        print("!" * 64)
        print(f"⚠️  {stale}")
        print("!" * 64)
        print()
    print(f"Wallet (estimated):  ${w['current_balance_estimate']:.2f} / ${w['funded_total']:.2f}")
    print(f"Refill threshold:    ${w['refill_threshold']:.2f}  (auto-refill: {w['auto_refill']})")
    print(f"Cycle started:       {w['cycle_started_at']}")
    print()
    print(f"Cycle spent:         ${t['current_cycle_spent_usd']:.2f} / ${l['per_cycle_block_usd']:.2f}  (warn at ${l['per_cycle_warn_usd']:.2f})")
    print(f"Today spent:         ${t['today_spent_usd']:.2f} / ${l['per_day_block_usd']:.2f}  (warn at ${l['per_day_warn_usd']:.2f})")
    print(f"Lifetime spent:      ${t['lifetime_spent_usd']:.2f}  ({t['lifetime_calls']} calls)")
    print()
    print("Per-call ceilings by mode:")
    for mode, ceiling in l["per_call_block_usd_by_mode"].items():
        cstr = f"${ceiling:.2f}" if ceiling is not None else "HARD-BLOCKED"
        print(f"  {mode:<20s} {cstr}")
    print()
    print("Cycle spent by mode:")
    for mode, spent in t.get("cycle_spent_by_mode", {}).items():
        print(f"  {mode:<20s} ${spent:.4f}")
    print()
    print(f"Low-balance cap:     ${l['low_balance_max_call_usd']:.2f}/call when balance < ${w['refill_threshold']:.2f}")
    print(f"Rate limit:          {l['max_calls_per_5min']} calls / 5 min")
    print(f"Consecutive fails:   {s['consecutive_failures']} / {l['max_consecutive_failures']}")
    if s.get("halt_reason"):
        print(f"⚠️  HALTED:           {s['halt_reason']}")
    print()
    if data["log"]:
        print(f"Last 5 calls:")
        for entry in data["log"][-5:]:
            ts = entry["ts"]
            mode = entry.get("mode", "poster")
            cost = entry.get("actual_cost_usd", 0)
            status = entry.get("status", "?")
            extra = ""
            if mode in POSTER_MODES:
                extra = f"q={entry.get('quality','?')} n={entry.get('n','?')}"
            elif mode == "kling":
                extra = f"d={entry.get('duration','?')}s audio={entry.get('audio','?')}"
            elif mode.startswith("seedance"):
                extra = f"d={entry.get('duration','?')}s {entry.get('resolution','?')}"
            print(f"  {ts}  {mode:<16s} {extra:<20s} ${cost:.4f}  {status}")
    else:
        print("No calls logged yet.")
    return 0


def cmd_refill_confirm(_args) -> int:
    data = load()
    data["wallet"]["current_balance_estimate"] = data["wallet"]["funded_total"]
    data["wallet"]["last_refill_confirmed_at"] = now_iso()
    data["wallet"]["cycle_started_at"] = now_iso()
    data["totals"]["current_cycle_calls"] = 0
    data["totals"]["current_cycle_spent_usd"] = 0.00
    data["totals"]["cycle_spent_by_mode"] = {"poster": 0.0, "edit": 0.0, "rembg": 0.0, "kling": 0.0, "seedance": 0.0}
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
def add_call_args(p: argparse.ArgumentParser) -> None:
    """Args common to check + log."""
    p.add_argument("--mode", default="poster", choices=sorted(ALL_MODES),
                   help="Generation mode. Default: poster (backward compatible).")
    p.add_argument("--quality", choices=["low", "medium", "high"],
                   help="For mode=poster|edit: quality tier.")
    p.add_argument("--n", type=int, default=1, help="For mode=poster|edit: number of images.")
    p.add_argument("--duration", type=int,
                   help="For mode=kling|seedance-*: video duration in seconds (kling 3-15, seedance 4-15).")
    p.add_argument("--audio", choices=["off", "on", "voice_control"],
                   help="For mode=kling: audio mode (off=no audio, on=audio, voice_control=audio+voice). Default: on.")
    p.add_argument("--est-cost", type=float, default=None, dest="est_cost",
                   help="For mode=generic: estimated cost in USD from the model recipe pricing table.")
    p.add_argument("--model", default="", help="For mode=generic: recipe id, for logging.")
    p.add_argument("--brief", default="", help="Free-text brief / prompt for logging.")


def main() -> int:
    p = argparse.ArgumentParser(description="Fal API budget guard for fantastic-posters (v2 mode-aware)")
    sub = p.add_subparsers(dest="cmd", required=True)

    pc = sub.add_parser("check", help="Pre-flight: gate this call against budget rules")
    add_call_args(pc)

    pl = sub.add_parser("log", help="Post-flight: record actual spend")
    add_call_args(pl)
    pl.add_argument("--status", required=True, choices=["success", "failed"])
    pl.add_argument("--actual-cost", type=float, default=None)
    pl.add_argument("--style", default="", help="(poster only) selected style id")
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
