#!/usr/bin/env python3
"""swarm_meter.py — deterministic per-run token/dollar meter for subagent swarms.

Tracks estimated and actual spend for a "swarm" of subagent seats (Claude Task/
Agent dispatches, or Codex child sessions) against a declared budget. Pure
stdlib, no network calls, no raising on bad input — every failure path prints
`STOP <REASON>: <message>` and exits 1 (2 is reserved for argparse usage
errors).

State lives under $SWARM_METER_HOME (default: repo `.agent/`):
    swarm-runs/<run_id>.json   — one file per open/closed run
    swarm-usage.json           — schema, limits, pricing, active-run pointer, log

CLI:
    open      --budget --run --harness claude|codex
    price     --seat --brief|--brief-bytes [--out-tokens] [--label] [--run]
    charge    --run --label --in --out
    round     --run
    status    [--run]
    reconcile --run --harness claude|codex [--subagents-dir] [--sessions-dir] [--parent]
    close     --run [--partial] [--dissent N]

Importable API (used in-process by execution/hooks/swarm_meter_hook.py so the
PreToolUse hook never pays subprocess overhead per Agent dispatch):
    load_usage(), save_usage(), load_run(), save_run(),
    do_open(), do_price(), do_charge(), do_round(), do_reconcile(), do_close(),
    set_active_run(), SwarmMeterError
"""

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HOME = REPO_ROOT / ".agent"

RUN_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")

MAX_SEATS = 4
MAX_ROUNDS = 3
MAX_BRIEF_BYTES = 6144
WARN_RATIO = 0.7

# $ per MTok {in, out}. gpt-6-astra pricing is UNCONFIRMED (no verified public
# rate card as of 2026-09) — flagged, not blocked; the factual veto is a ship
# floor for claims, not a reason to refuse a deterministic estimate.
PRICING = {
    "opus": {"in": 5, "out": 25},
    "sonnet": {"in": 3, "out": 15},
    "haiku": {"in": 1, "out": 5},
    "gpt-6-astra": {"in": 5, "out": 25, "unconfirmed": True},
}


class SwarmMeterError(Exception):
    def __init__(self, reason, message):
        self.reason = reason
        self.message = message
        super().__init__(f"{reason}: {message}")


# ---------------------------------------------------------------- plumbing --

def _home() -> Path:
    h = os.environ.get("SWARM_METER_HOME")
    return Path(h) if h else DEFAULT_HOME


def _runs_dir() -> Path:
    return _home() / "swarm-runs"


def _usage_path() -> Path:
    return _home() / "swarm-usage.json"


def _run_path(run_id: str) -> Path:
    if not RUN_ID_RE.match(run_id or ""):
        raise SwarmMeterError("INVALID_RUN_ID", f"{run_id!r} has unsafe characters")
    return _runs_dir() / f"{run_id}.json"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _save_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, default=str))


def load_usage() -> dict:
    p = _usage_path()
    if not p.exists():
        usage = {
            "_schema": "swarm-usage-v1",
            "limits": {
                "max_seats": MAX_SEATS,
                "max_rounds": MAX_ROUNDS,
                "max_brief_bytes": MAX_BRIEF_BYTES,
                "warn_ratio": WARN_RATIO,
            },
            "pricing_usd_per_mtok": PRICING,
            "state": {"active_run": None},
            "log": [],
        }
        _save_json(p, usage)
        return usage
    try:
        return json.loads(p.read_text())
    except Exception as e:
        raise SwarmMeterError("USAGE_CORRUPT", f"{p}: {e}")


def save_usage(usage: dict) -> None:
    _save_json(_usage_path(), usage)


def set_active_run(run_id) -> None:
    usage = load_usage()
    usage.setdefault("state", {})["active_run"] = run_id
    save_usage(usage)


def load_run(run_id: str) -> dict:
    p = _run_path(run_id)
    if not p.exists():
        raise SwarmMeterError("RUN_NOT_FOUND", f"no run '{run_id}' at {p}")
    try:
        return json.loads(p.read_text())
    except Exception as e:
        raise SwarmMeterError("RUN_CORRUPT", f"{p}: {e}")


def save_run(run: dict) -> None:
    _save_json(_run_path(run["run_id"]), run)


def _seat_cost(seat: dict) -> float:
    return seat["actual_usd"] if seat.get("actual_usd") is not None else seat.get("est_usd", 0.0)


def _find_seat(run: dict, label: str):
    candidates = [s for s in run["seats"] if s["label"] == label]
    if not candidates:
        return None
    for s in candidates:
        if s.get("actual_usd") is None:
            return s
    return candidates[-1]


def _price_estimate(seat_type: str, brief_bytes: int, out_tokens: int) -> float:
    p = PRICING[seat_type]
    return ((brief_bytes / 4) + 3000) * p["in"] / 1e6 + out_tokens * p["out"] / 1e6


# --------------------------------------------------------------- core ops --

def do_open(run_id: str, harness: str, budget) -> dict:
    if harness not in ("claude", "codex"):
        raise SwarmMeterError("BAD_HARNESS", f"harness must be claude|codex, got {harness!r}")
    budget = float(budget)
    run = {
        "run_id": run_id,
        "harness": harness,
        "budget_usd": budget,
        "warn_usd": round(budget * WARN_RATIO, 4),
        "spent_est_usd": 0.0,
        "spent_actual_usd": 0.0,
        "seats": [],
        "rounds": 0,
        "max_seats": MAX_SEATS,
        "max_rounds": MAX_ROUNDS,
        "max_brief_bytes": MAX_BRIEF_BYTES,
        "opened_ts": _now_iso(),
        "closed_ts": None,
        "status": "OPEN",
    }
    save_run(run)
    set_active_run(run_id)
    return run


def do_price(run_id: str, seat_type: str, brief_bytes: int, out_tokens: int = 1200, label=None) -> dict:
    if seat_type not in PRICING:
        raise SwarmMeterError("UNKNOWN_SEAT", f"{seat_type!r} not in {sorted(PRICING)}")
    run = load_run(run_id)
    if brief_bytes > run["max_brief_bytes"]:
        raise SwarmMeterError("BRIEF_TOO_BIG", f"{brief_bytes} bytes > max {run['max_brief_bytes']}")
    if len(run["seats"]) >= run["max_seats"]:
        raise SwarmMeterError("SEAT_CAP", f"{len(run['seats'])} seats already reserved >= max {run['max_seats']}")

    est_usd = _price_estimate(seat_type, brief_bytes, out_tokens)
    current_total = sum(_seat_cost(s) for s in run["seats"])
    projected = current_total + est_usd
    if projected > run["budget_usd"]:
        raise SwarmMeterError(
            "OVER_BUDGET", f"projected ${projected:.4f} > budget ${run['budget_usd']:.2f}")

    label = label or f"{seat_type}-seat{len(run['seats']) + 1}"
    seat_record = {
        "label": label,
        "seat": seat_type,
        "brief_bytes": brief_bytes,
        "est_usd": round(est_usd, 4),
        "actual_usd": None,
        "in_tokens": None,
        "out_tokens": None,
    }
    run["seats"].append(seat_record)
    run["spent_est_usd"] = round(run.get("spent_est_usd", 0.0) + est_usd, 4)
    save_run(run)

    return {
        "run_id": run_id,
        "seat": seat_type,
        "label": label,
        "est_usd": est_usd,
        "projected": projected,
        "budget": run["budget_usd"],
        "warn_usd": run["warn_usd"],
        "warn": projected > run["warn_usd"],
        "unconfirmed": bool(PRICING[seat_type].get("unconfirmed")),
    }


def do_charge(run_id: str, label: str, in_tokens: int, out_tokens: int) -> dict:
    run = load_run(run_id)
    seat = _find_seat(run, label)
    if seat is None:
        raise SwarmMeterError("LABEL_NOT_FOUND", f"no seat labeled {label!r} on run '{run_id}'")
    p = PRICING[seat["seat"]]
    actual = in_tokens * p["in"] / 1e6 + out_tokens * p["out"] / 1e6
    prior_est = seat.get("est_usd", 0.0)
    seat["actual_usd"] = round(actual, 4)
    seat["in_tokens"] = in_tokens
    seat["out_tokens"] = out_tokens
    run["spent_actual_usd"] = round(
        sum(s["actual_usd"] for s in run["seats"] if s.get("actual_usd") is not None), 4)
    save_run(run)
    return {"run_id": run_id, "seat": seat["seat"], "label": label, "actual_usd": actual, "prior_est": prior_est}


def do_round(run_id: str) -> dict:
    run = load_run(run_id)
    if run["rounds"] + 1 > run["max_rounds"]:
        raise SwarmMeterError("ROUND_CAP", f"round {run['rounds'] + 1} exceeds max {run['max_rounds']}")
    run["rounds"] += 1
    save_run(run)
    return {"rounds": run["rounds"], "max_rounds": run["max_rounds"]}


def _reconcile_claude(run: dict, run_id: str, subagents_dir) -> list:
    pattern_dir = subagents_dir or str(Path.home() / ".claude" / "projects" / "*" / "*" / "subagents")
    meta_files = sorted(glob.glob(os.path.join(pattern_dir, "agent-*.meta.json")))
    matched_ids = set()
    lines = []
    prefix = f"[swarm:{run_id}]"
    for meta_path in meta_files:
        meta_p = Path(meta_path)
        try:
            meta = json.loads(meta_p.read_text())
        except Exception:
            continue
        desc = meta.get("description") or ""
        if not desc.startswith(prefix):
            continue
        label = desc[len(prefix):].strip()
        name = meta_p.name
        base = name[: -len(".meta.json")] if name.endswith(".meta.json") else meta_p.stem
        jsonl_path = meta_p.parent / f"{base}.jsonl"
        totals = {"input_tokens": 0, "cache_creation_input_tokens": 0,
                  "cache_read_input_tokens": 0, "output_tokens": 0}
        if jsonl_path.exists():
            for raw_line in jsonl_path.read_text().splitlines():
                raw_line = raw_line.strip()
                if not raw_line:
                    continue
                try:
                    obj = json.loads(raw_line)
                except Exception:
                    continue
                usage = ((obj.get("message") or {}).get("usage")) or {}
                for k in totals:
                    totals[k] += usage.get(k, 0) or 0
        seat = _find_seat(run, label)
        if seat is None:
            continue
        p = PRICING[seat["seat"]]
        actual = (
            totals["input_tokens"] * p["in"]
            + totals["cache_read_input_tokens"] * p["in"] * 0.10
            + totals["cache_creation_input_tokens"] * p["in"] * 1.25
        ) / 1e6 + totals["output_tokens"] * p["out"] / 1e6
        prior_est = seat.get("est_usd", 0.0)
        seat["actual_usd"] = round(actual, 4)
        seat["in_tokens"] = (totals["input_tokens"] + totals["cache_creation_input_tokens"]
                              + totals["cache_read_input_tokens"])
        seat["out_tokens"] = totals["output_tokens"]
        matched_ids.add(id(seat))
        lines.append(f"RECONCILE {label} est=${prior_est:.4f} -> actual=${actual:.4f}")
    for s in run["seats"]:
        if id(s) not in matched_ids and s.get("actual_usd") is None:
            lines.append(f"RECONCILE {s['label']} UNMEASURED (no transcript found)")
    return lines


def _reconcile_codex(run: dict, sessions_dir, parent) -> list:
    if not parent:
        raise SwarmMeterError("MISSING_PARENT", "codex reconcile requires --parent <thread_id>")
    root = sessions_dir or str(Path.home() / ".codex" / "sessions")
    rollout_files = sorted(glob.glob(os.path.join(root, "**", "*.jsonl"), recursive=True))
    unclaimed = [s for s in run["seats"] if s.get("actual_usd") is None]
    idx = 0
    lines = []
    for rp in rollout_files:
        try:
            raw_lines = Path(rp).read_text().splitlines()
        except Exception:
            continue
        if not raw_lines:
            continue
        try:
            first = json.loads(raw_lines[0])
        except Exception:
            continue
        if first.get("type") != "session_meta":
            continue
        if (first.get("payload") or {}).get("parent_thread_id") != parent:
            continue
        last_usage = None
        for raw_line in raw_lines:
            try:
                obj = json.loads(raw_line)
            except Exception:
                continue
            if obj.get("type") == "event_msg":
                p2 = obj.get("payload") or {}
                if p2.get("type") == "token_count":
                    info = (p2.get("info") or {}).get("total_token_usage")
                    if info:
                        last_usage = info
        if last_usage is None or idx >= len(unclaimed):
            continue
        seat = unclaimed[idx]
        idx += 1
        p = PRICING[seat["seat"]]
        input_tokens = last_usage.get("input_tokens", 0) or 0
        cached = last_usage.get("cached_input_tokens", 0) or 0
        output_tokens = last_usage.get("output_tokens", 0) or 0
        actual = (input_tokens * p["in"] + cached * p["in"] * 0.10) / 1e6 + output_tokens * p["out"] / 1e6
        prior_est = seat.get("est_usd", 0.0)
        seat["actual_usd"] = round(actual, 4)
        seat["in_tokens"] = input_tokens + cached
        seat["out_tokens"] = output_tokens
        lines.append(f"RECONCILE {seat['label']} est=${prior_est:.4f} -> actual=${actual:.4f}")
    for s in run["seats"]:
        if s.get("actual_usd") is None:
            lines.append(f"RECONCILE {s['label']} UNMEASURED (no transcript found)")
    return lines


def do_reconcile(run_id: str, harness: str, subagents_dir=None, sessions_dir=None, parent=None) -> dict:
    run = load_run(run_id)
    if harness == "claude":
        lines = _reconcile_claude(run, run_id, subagents_dir)
    elif harness == "codex":
        lines = _reconcile_codex(run, sessions_dir, parent)
    else:
        raise SwarmMeterError("BAD_HARNESS", f"harness must be claude|codex, got {harness!r}")
    run["spent_actual_usd"] = round(
        sum(s["actual_usd"] for s in run["seats"] if s.get("actual_usd") is not None), 4)
    save_run(run)
    return {"lines": lines, "run": run}


def do_close(run_id: str, partial: bool = False, dissent: int = 0) -> dict:
    run = load_run(run_id)
    seats = run["seats"]
    all_actual = all(s.get("actual_usd") is not None for s in seats) if seats else True
    if all_actual:
        cost = sum(s["actual_usd"] for s in seats)
        basis = "actual"
    else:
        cost = sum(_seat_cost(s) for s in seats)
        basis = "est"
    status = "PARTIAL" if (partial and not all_actual) else "CLOSED"
    run["status"] = status
    run["closed_ts"] = _now_iso()
    save_run(run)

    usage = load_usage()
    state = usage.setdefault("state", {})
    if state.get("active_run") == run_id:
        state["active_run"] = None
    usage.setdefault("log", []).append({
        "run_id": run_id,
        "harness": run.get("harness"),
        "closed_ts": run["closed_ts"],
        "status": status,
        "cost_usd": round(cost, 4),
        "basis": basis,
        "seats": len(seats),
        "rounds": run["rounds"],
        "dissent": dissent,
    })
    save_usage(usage)
    return {"run_id": run_id, "seats": len(seats), "rounds": run["rounds"], "cost": cost,
            "basis": basis, "dissent": dissent, "status": status}


def _resolve_run_id(explicit_run) -> str:
    if explicit_run:
        return explicit_run
    usage = load_usage()
    active = (usage.get("state") or {}).get("active_run")
    if not active:
        raise SwarmMeterError("NO_ACTIVE_RUN", "no --run given and no active run set")
    return active


# --------------------------------------------------------------------- CLI --

def cmd_open(args):
    run = do_open(args.run, args.harness, args.budget)
    print(f"OPEN {run['run_id']} harness={run['harness']} budget=${run['budget_usd']:.2f} "
          f"warn=${run['warn_usd']:.2f}")


def cmd_price(args):
    run_id = _resolve_run_id(args.run)
    if args.brief:
        p = Path(args.brief)
        if not p.exists():
            raise SwarmMeterError("BRIEF_NOT_FOUND", str(p))
        brief_bytes = p.stat().st_size
    else:
        brief_bytes = args.brief_bytes
    result = do_price(run_id, args.seat, brief_bytes, out_tokens=args.out_tokens, label=args.label)
    note = " [UNCONFIRMED PRICING]" if result["unconfirmed"] else ""
    print(f"PRICE {result['seat']} {result['label']} est=${result['est_usd']:.2f} "
          f"run_total=${result['projected']:.2f}/${result['budget']:.2f}{note}")
    if result["warn"]:
        print(f"WARN projected ${result['projected']:.2f} exceeds warn threshold "
              f"${result['warn_usd']:.2f} (budget ${result['budget']:.2f})")


def cmd_charge(args):
    result = do_charge(args.run, args.label, args.in_tokens, args.out_tokens)
    print(f"CHARGE {result['seat']} {result['label']} actual=${result['actual_usd']:.2f} "
          f"(est was ${result['prior_est']:.2f})")


def cmd_round(args):
    result = do_round(args.run)
    print(f"ROUND {result['rounds']}/{result['max_rounds']}")


def cmd_status(args):
    if args.run:
        run = load_run(args.run)
        print(json.dumps(run, indent=2))
        return
    usage = load_usage()
    active = (usage.get("state") or {}).get("active_run")
    if active:
        print(json.dumps(load_run(active), indent=2))
    else:
        print(json.dumps(usage, indent=2))


def cmd_reconcile(args):
    result = do_reconcile(args.run, args.harness, subagents_dir=args.subagents_dir,
                           sessions_dir=args.sessions_dir, parent=args.parent)
    if result["lines"]:
        for line in result["lines"]:
            print(line)
    else:
        print(f"RECONCILE {args.run}: no matching transcripts found")


def cmd_close(args):
    result = do_close(args.run, partial=args.partial, dissent=args.dissent)
    print(f"Swarm: {result['run_id']} seats={result['seats']} rounds={result['rounds']} "
          f"cost=${result['cost']:.2f} ({result['basis']}) dissent={result['dissent']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="swarm_meter.py", description="Deterministic per-run token/dollar meter for subagent swarms.")
    sub = parser.add_subparsers(dest="cmd")

    p_open = sub.add_parser("open")
    p_open.add_argument("--budget", type=float, required=True)
    p_open.add_argument("--run", required=True)
    p_open.add_argument("--harness", choices=["claude", "codex"], required=True)
    p_open.set_defaults(func=cmd_open)

    p_price = sub.add_parser("price")
    p_price.add_argument("--seat", choices=sorted(PRICING), required=True)
    g = p_price.add_mutually_exclusive_group(required=True)
    g.add_argument("--brief")
    g.add_argument("--brief-bytes", type=int)
    p_price.add_argument("--out-tokens", type=int, default=1200)
    p_price.add_argument("--label", default=None)
    p_price.add_argument("--run", default=None)
    p_price.set_defaults(func=cmd_price)

    p_charge = sub.add_parser("charge")
    p_charge.add_argument("--run", required=True)
    p_charge.add_argument("--label", required=True)
    p_charge.add_argument("--in", dest="in_tokens", type=int, required=True)
    p_charge.add_argument("--out", dest="out_tokens", type=int, required=True)
    p_charge.set_defaults(func=cmd_charge)

    p_round = sub.add_parser("round")
    p_round.add_argument("--run", required=True)
    p_round.set_defaults(func=cmd_round)

    p_status = sub.add_parser("status")
    p_status.add_argument("--run", default=None)
    p_status.set_defaults(func=cmd_status)

    p_recon = sub.add_parser("reconcile")
    p_recon.add_argument("--run", required=True)
    p_recon.add_argument("--harness", choices=["claude", "codex"], required=True)
    p_recon.add_argument("--subagents-dir", default=None)
    p_recon.add_argument("--sessions-dir", default=None)
    p_recon.add_argument("--parent", default=None)
    p_recon.set_defaults(func=cmd_reconcile)

    p_close = sub.add_parser("close")
    p_close.add_argument("--run", required=True)
    p_close.add_argument("--partial", action="store_true")
    p_close.add_argument("--dissent", type=int, default=0)
    p_close.set_defaults(func=cmd_close)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    if not getattr(args, "cmd", None):
        parser.print_usage()
        sys.exit(2)
    try:
        args.func(args)
    except SwarmMeterError as e:
        print(f"STOP {e.reason}: {e.message}")
        sys.exit(1)
    except SystemExit:
        raise
    except Exception as e:
        print(f"STOP INTERNAL_ERROR: {type(e).__name__}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
