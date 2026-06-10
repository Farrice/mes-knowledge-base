#!/usr/bin/env python3
"""
Unified pre-flight cost gate for the Antigravity Supercomputer.

Wraps every paid creative API behind one approve/deny gate so the agent
can show a single cost preview before rendering — Higgsfield's killer mechanic
ported into our stack.

Services covered:
  fal-poster              → delegates to fal_budget_guard.py (mode=poster)
  fal-edit                → delegates to fal_budget_guard.py (mode=edit)
  fal-rembg               → delegates to fal_budget_guard.py (mode=rembg)
  fal-kling               → delegates to fal_budget_guard.py (mode=kling)
  fal-seedance-720p       → delegates to fal_budget_guard.py (mode=seedance-720p)
  higgsfield-soul         → direct image gen via Higgsfield MCP
  higgsfield-cinema       → cinema-grade video via Higgsfield MCP
  higgsfield-nano         → Nano Banana Pro image via Higgsfield MCP
  higgsfield-virality     → virality predictor
  veo-3                   → Veo 3.1 video via Google Flow (Gemini Ultra quota)
  gemini-image            → Gemini Image (Ultra quota)
  gemini-text             → Gemini text (Ultra quota, effectively free)

Exit codes:
  0 = APPROVED (auto-fire OK)
  2 = NEEDS USER APPROVAL (cost > auto-approve threshold)
  1 = DENIED (hard-blocked: budget exhausted, daily cap, etc.)

Usage:
  python3 cost_gate.py check --service higgsfield-soul --request "product hero shot"
  python3 cost_gate.py log    --service higgsfield-soul --status success --actual-cost 0.08
  python3 cost_gate.py status
  python3 cost_gate.py reset-daily          # admin: clear today's spend record
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG_PATH = ROOT / ".agent" / "cost-gate-log.jsonl"
TRACKER_PATH = ROOT / ".agent" / "cost-gate-state.json"
FAL_GUARD = ROOT / "execution" / "fal_budget_guard.py"
APPROVALS_PATH = ROOT / ".agent" / "cost-gate-approvals.jsonl"
APPROVAL_TTL_MINUTES = 15

# ───────────────────────────────────────────────────────────────────
# SERVICE TABLE — the routing + cost source of truth
#
# TASTE-CALL ZONE (Farrice): tune these estimates against actual invoices
# once you've burned through a real Supercomputer session. The defaults
# are first-pass estimates from public pricing pages.
# ───────────────────────────────────────────────────────────────────
SERVICES = {
    # ─── Fal (delegate to existing guard, no duplicate tracking) ───
    "fal-poster":           {"type": "delegate", "guard_mode": "poster"},
    "fal-edit":             {"type": "delegate", "guard_mode": "edit"},
    "fal-rembg":            {"type": "delegate", "guard_mode": "rembg"},
    "fal-kling":            {"type": "delegate", "guard_mode": "kling"},
    "fal-seedance-480p":    {"type": "delegate", "guard_mode": "seedance-480p"},
    "fal-seedance-720p":    {"type": "delegate", "guard_mode": "seedance-720p"},

    # ─── Higgsfield MCP (we track here) ───
    "higgsfield-soul":      {"type": "paid", "est_usd": 0.10, "ceiling_usd": 0.50,
                             "desc": "Higgsfield Soul 2.0 image"},
    "higgsfield-cinema":    {"type": "paid", "est_usd": 1.50, "ceiling_usd": 3.00,
                             "desc": "Higgsfield Cinema Studio 3.5 video (~5-10s)"},
    "higgsfield-nano":      {"type": "paid", "est_usd": 0.05, "ceiling_usd": 0.20,
                             "desc": "Higgsfield Nano Banana Pro image"},
    "higgsfield-virality":  {"type": "paid", "est_usd": 0.01, "ceiling_usd": 0.05,
                             "desc": "Higgsfield virality predictor"},

    # ─── Google Ultra quota (Veo, Gemini) ───
    # Pay $0 per-call within Ultra subscription; count units against quota
    "veo-3":                {"type": "quota", "quota_units": 1, "quota_pool": "ultra-video",
                             "desc": "Veo 3.1 video via Google Flow"},
    "gemini-image":         {"type": "quota", "quota_units": 1, "quota_pool": "ultra-image",
                             "desc": "Gemini Image (Ultra)"},
    "gemini-text":          {"type": "quota", "quota_units": 0, "quota_pool": "ultra-text",
                             "desc": "Gemini text (Ultra, effectively unlimited)"},

    # ─── Unified research engine (execution/research.py) ───
    # Gemini Deep Research rides the Ultra text pool (≈$0 marginal). Perplexity is
    # paid fallback. The native floor is free and needs no service entry.
    "gemini-deep-research": {"type": "quota", "quota_units": 1, "quota_pool": "ultra-text",
                             "desc": "Gemini Deep Research (Ultra-covered accelerator)"},
    "perplexity-research":  {"type": "paid", "est_usd": 0.25, "ceiling_usd": 1.00,
                             "desc": "Perplexity sonar-deep-research (fallback accelerator)"},
}

# ───────────────────────────────────────────────────────────────────
# RISK-TOLERANCE ZONE (Farrice): tune these to your appetite.
# Default posture: pre-flight preview + manual approve, mirroring
# Higgsfield Supercomputer's killer mechanic.
# ───────────────────────────────────────────────────────────────────
AUTO_APPROVE_THRESHOLD_USD = 0.20   # below this: exit 0 (auto-fire)
DAILY_HARD_CAP_USD = 10.00           # cross this: exit 1 (deny)
SESSION_SOFT_CAP_USD = 5.00          # cross this: warn in output, still exit 2

# Quota pools (initial guesses; Google Ultra real limits TBD)
QUOTA_POOLS = {
    "ultra-video": {"daily_limit": 100, "warn_at": 80},   # Veo daily generations
    "ultra-image": {"daily_limit": 1000, "warn_at": 800},
    "ultra-text":  {"daily_limit": 100000, "warn_at": 90000},
}


# ───────────────────────────────────────────────────────────────────
# State persistence
# ───────────────────────────────────────────────────────────────────
def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def load_state() -> dict:
    if not TRACKER_PATH.exists():
        return _new_state()
    with TRACKER_PATH.open() as f:
        return json.load(f)


def _new_state() -> dict:
    return {
        "today_date": today_str(),
        "today_spent_usd": 0.0,
        "today_quota_used": {pool: 0 for pool in QUOTA_POOLS},
        "session_spent_usd": 0.0,
        "session_started_at": now_iso(),
        "lifetime_spent_usd": 0.0,
        "lifetime_calls": 0,
    }


def save_state(state: dict) -> None:
    TRACKER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with TRACKER_PATH.open("w") as f:
        json.dump(state, f, indent=2)
        f.write("\n")


def reset_today_if_needed(state: dict) -> None:
    if state["today_date"] != today_str():
        state["today_date"] = today_str()
        state["today_spent_usd"] = 0.0
        state["today_quota_used"] = {pool: 0 for pool in QUOTA_POOLS}


def append_log(entry: dict) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a") as f:
        f.write(json.dumps(entry) + "\n")


def _ingest_to_memory(entry: dict) -> None:
    """Sprint 1: mirror cost events to sovereign memory as episodic/decision.

    Non-fatal — failures here must never break the primary cost log.
    """
    try:
        try:
            from memory_store import store_memory_silent, _detect_workspace
        except ImportError:
            from execution.memory_store import store_memory_silent, _detect_workspace
        svc = entry.get("service", "unknown")
        status = entry.get("status", "unknown")
        actual = entry.get("actual_cost_usd", 0.0) or 0.0
        store_memory_silent(
            tier="episodic",
            category="decision",
            content=f"COST {status}: {svc} ${actual:.4f}",
            metadata={
                "source": "cost_gate",
                "service": svc,
                "type": entry.get("type"),
                "status": status,
                "estimated_cost_usd": entry.get("estimated_cost_usd"),
                "actual_cost_usd": actual,
                "output_path": entry.get("output_path", ""),
                "project": entry.get("project", ""),
                "workspace": _detect_workspace(),
            },
        )
    except Exception:
        pass


# ───────────────────────────────────────────────────────────────────
# CHECK
# ───────────────────────────────────────────────────────────────────
def _log_check_decision(service: str, exit_code: int, request: str = "") -> None:
    """Append every check decision to the ledger (event='check') so denials
    and bypass attempts are visible in weekly review. Non-fatal."""
    try:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(LOG_PATH, "a") as f:
            f.write(json.dumps({
                "ts": datetime.now(timezone.utc).isoformat(),
                "event": "check",
                "service": service,
                "decision": {0: "approved", 1: "denied", 2: "needs_approval"}.get(exit_code, str(exit_code)),
                "request": (request or "")[:200],
            }) + "\n")
    except Exception:
        pass


def cmd_check(args) -> int:
    code = _cmd_check_inner(args)
    _log_check_decision(args.service, code, getattr(args, "request", ""))
    return code


def _cmd_check_inner(args) -> int:
    service = args.service
    if service not in SERVICES:
        print(f"❌ Unknown service '{service}'. Valid: {sorted(SERVICES.keys())}", file=sys.stderr)
        return 1

    spec = SERVICES[service]

    # Delegate Fal calls to the existing guard
    if spec["type"] == "delegate":
        return _delegate_to_fal_guard(spec["guard_mode"], args)

    state = load_state()
    reset_today_if_needed(state)

    if spec["type"] == "paid":
        est = spec["est_usd"]
        ceiling = spec["ceiling_usd"]

        # Hard ceiling check
        if est > ceiling:
            _print_denied(service, est, f"estimate ${est:.3f} exceeds per-call ceiling ${ceiling:.2f}")
            return 1

        # Daily cap
        projected_day = state["today_spent_usd"] + est
        if projected_day > DAILY_HARD_CAP_USD:
            _print_denied(service, est,
                          f"projected daily spend ${projected_day:.2f} > cap ${DAILY_HARD_CAP_USD:.2f}")
            return 1

        # Auto-approve threshold
        if est <= AUTO_APPROVE_THRESHOLD_USD:
            _print_approved(service, est, state, auto=True)
            save_state(state)
            return 0

        # Above threshold: needs user approval
        _print_needs_approval(service, est, state)
        save_state(state)
        return 2

    if spec["type"] == "quota":
        units = spec["quota_units"]
        pool = spec["quota_pool"]
        pool_limit = QUOTA_POOLS.get(pool, {}).get("daily_limit", 0)
        pool_warn = QUOTA_POOLS.get(pool, {}).get("warn_at", 0)
        used = state["today_quota_used"].get(pool, 0)
        projected = used + units

        if pool_limit and projected > pool_limit:
            _print_denied(service, 0.0,
                          f"quota pool '{pool}' would hit {projected} (daily limit {pool_limit})")
            return 1

        # Quota items are $0 — always auto-approve
        _print_approved(service, 0.0, state, auto=True,
                        quota_note=f"pool={pool} used={projected}/{pool_limit}"
                                   + ("  ⚠️  near warn threshold" if projected >= pool_warn else ""))
        save_state(state)
        return 0

    print(f"❌ Service spec malformed for '{service}'", file=sys.stderr)
    return 1


def _delegate_to_fal_guard(guard_mode: str, args) -> int:
    """Pass through to fal_budget_guard.py with the appropriate mode."""
    cmd = ["python3", str(FAL_GUARD), "check", f"--mode={guard_mode}"]
    # Pass through quality/n for poster modes
    if args.quality:
        cmd.append(f"--quality={args.quality}")
    if args.n:
        cmd.append(f"--n={args.n}")
    if args.duration:
        cmd.append(f"--duration={args.duration}")
    if args.audio:
        cmd.append(f"--audio={args.audio}")
    if args.request:
        cmd.append(f"--brief={args.request}")
    result = subprocess.run(cmd, capture_output=False)
    return result.returncode


def _print_approved(service: str, est: float, state: dict, auto: bool, quota_note: str = "") -> None:
    label = "AUTO-APPROVED" if auto else "APPROVED"
    print("=" * 60)
    print(f"COST GATE: ✅ {label}  ({service}, est=${est:.4f})")
    print("=" * 60)
    if quota_note:
        print(f"  Quota: {quota_note}")
    print(f"  Today spent:   ${state['today_spent_usd']:.2f} / ${DAILY_HARD_CAP_USD:.2f}")
    print(f"  Session spent: ${state['session_spent_usd']:.2f}")
    print(f"\nAfter call: python3 execution/cost_gate.py log --service={service} --status=success [--actual-cost=N]")


def _print_needs_approval(service: str, est: float, state: dict) -> None:
    print("=" * 60)
    print(f"COST GATE: ⏸  USER APPROVAL NEEDED  ({service}, est=${est:.4f})")
    print("=" * 60)
    print(f"  Estimated cost: ${est:.4f}")
    print(f"  Auto-approve threshold: ${AUTO_APPROVE_THRESHOLD_USD:.2f}")
    print(f"  Today spent so far: ${state['today_spent_usd']:.2f} / ${DAILY_HARD_CAP_USD:.2f}")
    print(f"  Session spent so far: ${state['session_spent_usd']:.2f}")
    if state['session_spent_usd'] > SESSION_SOFT_CAP_USD:
        print(f"  ⚠️  Session over soft cap ${SESSION_SOFT_CAP_USD:.2f}")
    print("\nAsk user: 'Approve $X.XX for [thing being made]? (y/n)'")


def _print_denied(service: str, est: float, reason: str) -> None:
    print("=" * 60)
    print(f"COST GATE: ❌ DENIED  ({service}, est=${est:.4f})")
    print("=" * 60)
    print(f"  • {reason}")


# ───────────────────────────────────────────────────────────────────
# LOG
# ───────────────────────────────────────────────────────────────────
def cmd_log(args) -> int:
    service = args.service
    if service not in SERVICES:
        print(f"❌ Unknown service '{service}'", file=sys.stderr)
        return 1

    spec = SERVICES[service]

    if spec["type"] == "delegate":
        # Defer accounting to fal_budget_guard; just log a cross-reference here
        entry = {
            "ts": now_iso(),
            "service": service,
            "delegated_to": "fal_budget_guard",
            "status": args.status,
        }
        append_log(entry)
        _ingest_to_memory(entry)
        print(f"Logged: {service} delegated to fal_budget_guard ({args.status})")
        return 0

    state = load_state()
    reset_today_if_needed(state)

    actual = args.actual_cost if args.actual_cost is not None else (
        spec["est_usd"] if spec["type"] == "paid" else 0.0
    )

    if args.status == "success":
        if spec["type"] == "paid":
            state["today_spent_usd"] = round(state["today_spent_usd"] + actual, 4)
            state["session_spent_usd"] = round(state["session_spent_usd"] + actual, 4)
            state["lifetime_spent_usd"] = round(state["lifetime_spent_usd"] + actual, 4)
        elif spec["type"] == "quota":
            pool = spec["quota_pool"]
            units = spec["quota_units"]
            state["today_quota_used"][pool] = state["today_quota_used"].get(pool, 0) + units
        state["lifetime_calls"] += 1

    entry = {
        "ts": now_iso(),
        "service": service,
        "type": spec["type"],
        "request": args.request or "",
        "status": args.status,
        "estimated_cost_usd": spec.get("est_usd", 0.0),
        "actual_cost_usd": actual,
        "output_path": args.output_path or "",
        "project": args.project or "",
    }
    append_log(entry)
    _ingest_to_memory(entry)
    save_state(state)

    print(f"Logged: {service}, {args.status}, ${actual:.4f}")
    print(f"  Today: ${state['today_spent_usd']:.2f} / ${DAILY_HARD_CAP_USD:.2f}")
    return 0


# ───────────────────────────────────────────────────────────────────
# STATUS
# ───────────────────────────────────────────────────────────────────
def cmd_status(_args) -> int:
    state = load_state()
    reset_today_if_needed(state)
    save_state(state)
    print("─" * 64)
    print("ANTIGRAVITY COST GATE — STATUS")
    print("─" * 64)
    print(f"Today ({state['today_date']}):")
    print(f"  Paid spend:    ${state['today_spent_usd']:.2f} / ${DAILY_HARD_CAP_USD:.2f}")
    for pool, used in state["today_quota_used"].items():
        limit = QUOTA_POOLS.get(pool, {}).get("daily_limit", 0)
        print(f"  Quota {pool}: {used} / {limit}")
    print()
    print(f"Session (started {state['session_started_at']}):")
    print(f"  Spent:         ${state['session_spent_usd']:.2f}")
    print(f"  Soft cap:      ${SESSION_SOFT_CAP_USD:.2f}")
    print()
    print(f"Lifetime: ${state['lifetime_spent_usd']:.2f} across {state['lifetime_calls']} calls")
    print()
    print("Auto-approve threshold:", f"${AUTO_APPROVE_THRESHOLD_USD:.2f}")
    print("(Below threshold: auto-fire. Above: ask user.)")
    print()
    print("Service catalog:")
    for svc, spec in SERVICES.items():
        if spec["type"] == "delegate":
            print(f"  {svc:<24s} → fal_budget_guard ({spec['guard_mode']})")
        elif spec["type"] == "paid":
            print(f"  {svc:<24s} est=${spec['est_usd']:.3f}  ceil=${spec['ceiling_usd']:.2f}  ({spec['desc']})")
        else:
            print(f"  {svc:<24s} quota={spec['quota_units']}/{spec['quota_pool']}  ({spec['desc']})")
    return 0


def cmd_reset_daily(_args) -> int:
    state = load_state()
    state["today_date"] = today_str()
    state["today_spent_usd"] = 0.0
    state["today_quota_used"] = {pool: 0 for pool in QUOTA_POOLS}
    save_state(state)
    print("✅ Today's spend record cleared.")
    return 0


def cmd_reset_session(_args) -> int:
    state = load_state()
    state["session_spent_usd"] = 0.0
    state["session_started_at"] = now_iso()
    save_state(state)
    print("✅ Session spend cleared.")
    return 0


# ───────────────────────────────────────────────────────────────────
# APPROVE — user-granted token consumed by the PreToolUse cost hook
# ───────────────────────────────────────────────────────────────────
def cmd_approve(args) -> int:
    """Record a short-lived user approval for an above-threshold service.

    The PreToolUse hook (execution/hooks/cost_gate_hook.py) blocks paid calls
    whose check returns 2 (needs approval) unless an unexpired token exists.
    Run this ONLY after Farrice explicitly approves the spend.
    """
    from datetime import timedelta
    now = datetime.now(timezone.utc)
    minutes = args.minutes or APPROVAL_TTL_MINUTES
    entry = {
        "service": args.service,
        "ts": now.isoformat(),
        "expires_at": (now + timedelta(minutes=minutes)).isoformat(),
        "request": (args.request or "")[:200],
    }
    APPROVALS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(APPROVALS_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"✅ Approval recorded: {args.service} valid {minutes} min (until {entry['expires_at']})")
    return 0


def consume_approval(service: str) -> bool:
    """True if an unexpired, unconsumed approval token exists for service.
    Consumes it (marks used) by rewriting the file. Used by the cost hook."""
    if not APPROVALS_PATH.exists():
        return False
    now = datetime.now(timezone.utc).isoformat()
    lines, hit = [], False
    try:
        for line in APPROVALS_PATH.read_text().splitlines():
            if not line.strip():
                continue
            e = json.loads(line)
            if (not hit and not e.get("used")
                    and e.get("service") == service
                    and e.get("expires_at", "") > now):
                e["used"] = now
                hit = True
            lines.append(json.dumps(e))
        if hit:
            APPROVALS_PATH.write_text("\n".join(lines) + "\n")
    except Exception:
        return False
    return hit


# ───────────────────────────────────────────────────────────────────
# CLI
# ───────────────────────────────────────────────────────────────────
def main() -> int:
    p = argparse.ArgumentParser(description="Antigravity unified cost gate")
    sub = p.add_subparsers(dest="cmd", required=True)

    pc = sub.add_parser("check", help="Pre-flight: gate this call against budget rules")
    pc.add_argument("--service", required=True, help="Service id (see status for full list)")
    pc.add_argument("--request", default="", help="Free-text description of what's being made")
    pc.add_argument("--project", default="", help="Project slug for anchor-memory cross-ref")
    # Fal-delegate passthrough args
    pc.add_argument("--quality", choices=["low", "medium", "high"])
    pc.add_argument("--n", type=int)
    pc.add_argument("--duration", type=int)
    pc.add_argument("--audio", choices=["off", "on", "voice_control"])

    pl = sub.add_parser("log", help="Post-flight: record actual spend")
    pl.add_argument("--service", required=True)
    pl.add_argument("--status", required=True, choices=["success", "failed"])
    pl.add_argument("--actual-cost", type=float, default=None)
    pl.add_argument("--request", default="")
    pl.add_argument("--output-path", default="")
    pl.add_argument("--project", default="")

    pa = sub.add_parser("approve", help="Record user approval token (15-min TTL) for an above-threshold service")
    pa.add_argument("--service", required=True)
    pa.add_argument("--minutes", type=int, default=None, help=f"TTL (default {APPROVAL_TTL_MINUTES})")
    pa.add_argument("--request", default="", help="What was approved")

    sub.add_parser("status", help="Show current cost state")
    sub.add_parser("reset-daily", help="Clear today's spend record")
    sub.add_parser("reset-session", help="Clear session spend counter")

    args = p.parse_args()
    return {
        "check": cmd_check,
        "log": cmd_log,
        "approve": cmd_approve,
        "status": cmd_status,
        "reset-daily": cmd_reset_daily,
        "reset-session": cmd_reset_session,
    }[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
