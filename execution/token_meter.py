#!/usr/bin/env python3
"""
token_meter.py — a deterministic, retroactive token & cost ledger for Claude Code sessions.

The harness (Claude Code) makes the API calls, not this repo — but it writes every
assistant turn's real `usage` into per-session JSONL transcripts under
~/.claude/projects/<project-slug>/ — including nested subagent transcripts at
<project-slug>/<parentSession>/subagents/agent-*.jsonl (~35% of real spend). This tool
recursively parses all of them (deduped by requestId) and computes
**cache-aware cost** (cache reads at 0.1x input, 5m cache writes at 1.25x, 1h writes at 2x,
output at the model's output rate) exactly the way the Anthropic Console bills. Nothing here
depends on Claude remembering to log anything — it reads what actually happened.

Answers: "what do I typically spend per session?" and "what would that have cost on Fable 5?"

Pricing source: the `claude-api` skill catalog (cached 2026-06-24). Update PRICES below when it
changes. Cache economics: `shared/prompt-caching.md` (reads ~0.1x, 5m write 1.25x, 1h write 2x).

Usage:
  python3 execution/token_meter.py summary                 # totals + typical (median/mean) session
  python3 execution/token_meter.py sessions [--limit 20]   # per-session table, newest first
  python3 execution/token_meter.py session <id-prefix>     # one session, per-model detail
  python3 execution/token_meter.py project-at --model fable-5   # reprice ALL usage at one model
  python3 execution/token_meter.py snapshot                # write .agent/token-usage.* ledger
Common flags: --since YYYY-MM-DD  --all  --project <slug>  --json
"""
import argparse
import json
import os
import statistics
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

# ── Pricing: USD per 1,000,000 tokens (input, output). Source: claude-api skill (2026-06-24).
PRICES = {
    "fable-5":    (10.0, 50.0),
    "mythos-5":   (10.0, 50.0),
    "mythos-preview": (10.0, 50.0),
    "opus-4-8":   (5.0, 25.0),
    "opus-4-7":   (5.0, 25.0),
    "opus-4-6":   (5.0, 25.0),
    "opus-4-5":   (5.0, 25.0),
    "opus-4-1":   (15.0, 75.0),
    "opus-4-0":   (15.0, 75.0),
    "opus-3":     (15.0, 75.0),
    "3-opus":     (15.0, 75.0),
    "sonnet-5":   (3.0, 15.0),   # intro $2/$10 through 2026-08-31; standard used here
    "sonnet-4-6": (3.0, 15.0),
    "sonnet-4-5": (3.0, 15.0),
    "sonnet-4":   (3.0, 15.0),
    "sonnet-3-7": (3.0, 15.0),
    "3-7-sonnet": (3.0, 15.0),
    "3-5-sonnet": (3.0, 15.0),
    "3-sonnet":   (3.0, 15.0),
    "haiku-4-5":  (1.0, 5.0),
    "haiku-3-5":  (1.0, 5.0),
    "3-5-haiku":  (1.0, 5.0),
    "haiku-3":    (1.0, 5.0),
    "3-haiku":    (1.0, 5.0),
}
# Match order matters: most-specific / longest keys first so "opus-4-8" wins before a bare "opus".
_PRICE_KEYS = sorted(PRICES, key=len, reverse=True)

CACHE_READ_MULT = 0.10   # cache read = 0.1x input rate
CACHE_5M_MULT = 1.25     # 5-minute cache write = 1.25x input rate
CACHE_1H_MULT = 2.00     # 1-hour cache write = 2x input rate

PROJECTS_DIR = Path.home() / ".claude" / "projects"
THIS_PROJECT = "-Users-farricecain-Google-Antigravity"
LEDGER_DIR = Path(__file__).resolve().parent.parent / ".agent"


def rates_for(model: str):
    """Return (in_per_1m, out_per_1m) for a model id, or None if unpriceable/synthetic."""
    if not model or model.startswith("<"):   # "<synthetic>" etc. — no real spend
        return None
    m = model.lower()
    for key in _PRICE_KEYS:
        if key in m:
            return PRICES[key]
    return None  # unknown model — flagged, not silently priced


def message_cost(rec, override_model=None):
    """Cache-aware USD cost for one usage record. override_model reprices at a target model."""
    rates = rates_for(override_model) if override_model else rates_for(rec["model"])
    if rates is None:
        return 0.0
    in_rate, out_rate = rates[0] / 1_000_000, rates[1] / 1_000_000
    return (
        rec["input"] * in_rate
        + rec["cache_read"] * in_rate * CACHE_READ_MULT
        + rec["cache_w5m"] * in_rate * CACHE_5M_MULT
        + rec["cache_w1h"] * in_rate * CACHE_1H_MULT
        + rec["output"] * out_rate
    )


def iter_records(paths, since=None):
    """Yield deduped per-assistant-message usage records from transcript JSONL files.

    Dedup key = requestId (one API response = one billable call), falling back to the log
    entry uuid. This prevents double-counting when a transcript re-logs a message on
    resume/rewind. Non-assistant lines and lines without usage are skipped.
    """
    seen = set()
    for path in paths:
        try:
            fh = open(path, encoding="utf-8")
        except OSError:
            continue
        with fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    o = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if o.get("type") != "assistant":
                    continue
                msg = o.get("message") or {}
                usage = msg.get("usage")
                if not isinstance(usage, dict):
                    continue
                dedup = o.get("requestId") or o.get("uuid")
                if dedup and dedup in seen:
                    continue
                if dedup:
                    seen.add(dedup)
                ts = o.get("timestamp") or ""
                if since and ts[:10] < since:
                    continue
                cc = usage.get("cache_creation") or {}
                # 5m/1h breakdown when present; else treat all creation as 5m (1.25x).
                w5 = cc.get("ephemeral_5m_input_tokens")
                w1 = cc.get("ephemeral_1h_input_tokens")
                if w5 is None and w1 is None:
                    w5 = usage.get("cache_creation_input_tokens", 0) or 0
                    w1 = 0
                yield {
                    "session": o.get("sessionId") or Path(path).stem,
                    "ts": ts,
                    "model": msg.get("model") or "",
                    "sidechain": bool(o.get("isSidechain")),
                    "input": usage.get("input_tokens", 0) or 0,
                    "output": usage.get("output_tokens", 0) or 0,
                    "cache_read": usage.get("cache_read_input_tokens", 0) or 0,
                    "cache_w5m": w5 or 0,
                    "cache_w1h": w1 or 0,
                }


def resolve_paths(args):
    # Recurse so nested SUBAGENT transcripts are included. They live 4 levels deep at
    # <slug>/<parentSessionId>/subagents/agent-*.jsonl — they carry the PARENT sessionId and
    # isSidechain:true, so they roll up to the spawning session and populate the subagent-cost
    # split. requestId dedup guarantees no double-count with top-level files (verified overlap=0).
    # A flat glob here silently omitted ~35% of real spend.
    if args.all:
        return sorted(PROJECTS_DIR.glob("*/**/*.jsonl"))
    slug = args.project or THIS_PROJECT
    return sorted((PROJECTS_DIR / slug).rglob("*.jsonl"))


def blank_agg():
    return {"msgs": 0, "input": 0, "output": 0, "cache_read": 0, "cache_w5m": 0,
            "cache_w1h": 0, "cost": 0.0, "models": defaultdict(int)}


def fold(agg, rec):
    agg["msgs"] += 1
    for k in ("input", "output", "cache_read", "cache_w5m", "cache_w1h"):
        agg[k] += rec[k]
    agg["cost"] += message_cost(rec)
    agg["models"][rec["model"] or "unknown"] += 1


def total_tokens(a):
    return a["input"] + a["output"] + a["cache_read"] + a["cache_w5m"] + a["cache_w1h"]


def fmt_tok(n):
    return f"{n/1_000_000:.2f}M" if n >= 1_000_000 else (f"{n/1_000:.0f}k" if n >= 1000 else str(n))


def build(args):
    """Return (per_session dict, records list) for the resolved scope."""
    paths = resolve_paths(args)
    sessions = defaultdict(blank_agg)
    records = []
    for rec in iter_records(paths, since=args.since):
        records.append(rec)
        s = sessions[rec["session"]]
        fold(s, rec)
        s.setdefault("first_ts", rec["ts"])
        s["last_ts"] = rec["ts"]
        s.setdefault("sidechain_cost", 0.0)
        if rec["sidechain"]:
            s["sidechain_cost"] += message_cost(rec)
    return sessions, records


# ────────────────────────────────────────────────────────── commands

def cmd_summary(args):
    sessions, records = build(args)
    if not records:
        print("No usage found for the selected scope/date range.")
        return
    grand = blank_agg()
    main_cost = sub_cost = 0.0
    per_model = defaultdict(lambda: {"msgs": 0, "cost": 0.0})
    for r in records:
        fold(grand, r)
        c = message_cost(r)
        if r["sidechain"]:
            sub_cost += c
        else:
            main_cost += c
        pm = per_model[r["model"] or "unknown"]
        pm["msgs"] += 1
        pm["cost"] += c
    costs = sorted(s["cost"] for s in sessions.values())
    scope = "ALL projects" if args.all else (args.project or THIS_PROJECT)
    dates = sorted(r["ts"][:10] for r in records if r["ts"])
    payload = {
        "scope": scope,
        "date_range": [dates[0], dates[-1]] if dates else None,
        "sessions": len(sessions),
        "assistant_messages": grand["msgs"],
        "tokens": {k: grand[k] for k in ("input", "output", "cache_read", "cache_w5m", "cache_w1h")},
        "total_tokens": total_tokens(grand),
        "actual_cost_usd": round(grand["cost"], 2),
        "main_thread_cost_usd": round(main_cost, 2),
        "subagent_cost_usd": round(sub_cost, 2),
        "per_session_cost_usd": {
            "median": round(statistics.median(costs), 3),
            "mean": round(statistics.mean(costs), 3),
            "p90": round(costs[int(len(costs) * 0.9)] if costs else 0, 3),
            "max": round(max(costs), 3),
        },
        "by_model": {m: {"messages": v["msgs"], "cost_usd": round(v["cost"], 2)}
                     for m, v in sorted(per_model.items(), key=lambda kv: -kv[1]["cost"])},
        "unpriced_models": sorted({r["model"] for r in records if rates_for(r["model"]) is None}),
    }
    if args.json:
        print(json.dumps(payload, indent=2))
        return
    p = payload
    print(f"\n  TOKEN & COST SUMMARY — {scope}")
    print(f"  {'='*58}")
    if p["date_range"]:
        print(f"  Range: {p['date_range'][0]} → {p['date_range'][1]}   Sessions: {p['sessions']}   Msgs: {p['assistant_messages']}")
    t = p["tokens"]
    print(f"  Tokens  in:{fmt_tok(t['input'])}  out:{fmt_tok(t['output'])}  "
          f"cacheRead:{fmt_tok(t['cache_read'])}  cacheWrite:{fmt_tok(t['cache_w5m']+t['cache_w1h'])}"
          f"  (total {fmt_tok(p['total_tokens'])})")
    print(f"  {'-'*58}")
    print(f"  ACTUAL COST:      ${p['actual_cost_usd']:.2f}")
    print(f"    main thread:    ${p['main_thread_cost_usd']:.2f}")
    print(f"    subagents:      ${p['subagent_cost_usd']:.2f}")
    ps = p["per_session_cost_usd"]
    print(f"  Per session:  median ${ps['median']:.2f}  mean ${ps['mean']:.2f}  p90 ${ps['p90']:.2f}  max ${ps['max']:.2f}")
    print(f"  {'-'*58}")
    print("  By model:")
    for m, v in p["by_model"].items():
        print(f"    {m:22} {v['messages']:>5} msgs   ${v['cost_usd']:.2f}")
    if p["unpriced_models"]:
        print(f"  ⚠ unpriced (cost=0): {', '.join(p['unpriced_models'])}")
    print(f"  {'='*58}")
    print("  Tip: `project-at --model fable-5` reprices all of this at Fable 5 rates.\n")


def cmd_sessions(args):
    sessions, _ = build(args)
    rows = sorted(sessions.items(), key=lambda kv: kv[1].get("last_ts", ""), reverse=True)
    if args.limit:
        rows = rows[: args.limit]
    if args.json:
        print(json.dumps([
            {"session": sid[:8], "last_ts": a.get("last_ts", "")[:19], "msgs": a["msgs"],
             "total_tokens": total_tokens(a), "cost_usd": round(a["cost"], 3),
             "models": dict(a["models"])}
            for sid, a in rows], indent=2))
        return
    print(f"\n  {'date':10} {'session':9} {'msgs':>5} {'tokens':>9} {'cost':>9}  models")
    print(f"  {'-'*74}")
    for sid, a in rows:
        models = ",".join(sorted({m.replace("claude-", "") for m in a["models"]}))
        print(f"  {a.get('last_ts','')[:10]:10} {sid[:8]:9} {a['msgs']:>5} "
              f"{fmt_tok(total_tokens(a)):>9} {'$'+format(a['cost'],'.2f'):>9}  {models[:34]}")
    print()


def cmd_session(args):
    sessions, records = build(args)
    match = [s for s in sessions if s.startswith(args.id)]
    if not match:
        print(f"No session matching '{args.id}'. Try `sessions` to list.")
        return
    sid = match[0]
    recs = [r for r in records if r["session"] == sid]
    per_model = defaultdict(blank_agg)
    for r in recs:
        fold(per_model[r["model"] or "unknown"], r)
    a = sessions[sid]
    if args.json:
        print(json.dumps({"session": sid, "msgs": a["msgs"], "cost_usd": round(a["cost"], 3),
                          "subagent_cost_usd": round(a.get("sidechain_cost", 0), 3),
                          "by_model": {m: round(v["cost"], 3) for m, v in per_model.items()}}, indent=2))
        return
    print(f"\n  SESSION {sid}")
    print(f"  {a.get('first_ts','')[:19]} → {a.get('last_ts','')[:19]}   {a['msgs']} messages")
    print(f"  Cost ${a['cost']:.2f}  (subagents ${a.get('sidechain_cost',0):.2f})   tokens {fmt_tok(total_tokens(a))}")
    for m, v in sorted(per_model.items(), key=lambda kv: -kv[1]["cost"]):
        print(f"    {m:22} {v['msgs']:>4} msgs  in:{fmt_tok(v['input'])} out:{fmt_tok(v['output'])} "
              f"cacheRead:{fmt_tok(v['cache_read'])}  ${v['cost']:.2f}")
    print()


def cmd_project_at(args):
    """Reprice ALL usage in scope as if every message had run on --model."""
    target = args.model
    if rates_for(target) is None:
        print(f"Unknown target model '{target}'. Known: {', '.join(sorted(set(_PRICE_KEYS)))}")
        return
    _, records = build(args)
    if not records:
        print("No usage in scope.")
        return
    actual = sum(message_cost(r) for r in records)
    projected = sum(message_cost(r, override_model=target) for r in records)
    by_sess_proj = defaultdict(float)
    for r in records:
        by_sess_proj[r["session"]] += message_cost(r, override_model=target)
    sess_costs = sorted(by_sess_proj.values())
    payload = {
        "scope": "ALL" if args.all else (args.project or THIS_PROJECT),
        "messages": len(records),
        "actual_cost_usd": round(actual, 2),
        "projected_model": target,
        "projected_cost_usd": round(projected, 2),
        "multiplier_vs_actual": round(projected / actual, 2) if actual else None,
        "projected_per_session": {
            "median": round(statistics.median(sess_costs), 3),
            "mean": round(statistics.mean(sess_costs), 3),
        },
    }
    if args.json:
        print(json.dumps(payload, indent=2))
        return
    print(f"\n  REPRICE AT {target.upper()} — {payload['scope']}  ({payload['messages']} messages)")
    print(f"  {'-'*54}")
    print(f"  Actual (as-run):     ${payload['actual_cost_usd']:.2f}")
    print(f"  If all {target}:  ${payload['projected_cost_usd']:.2f}"
          + (f"   ({payload['multiplier_vs_actual']}x)" if payload["multiplier_vs_actual"] else ""))
    pp = payload["projected_per_session"]
    print(f"  Projected per session: median ${pp['median']:.2f}  mean ${pp['mean']:.2f}\n")


def cmd_snapshot(args):
    """Write a persistent local ledger to .agent/ so cost history survives without re-parsing."""
    sessions, records = build(args)
    LEDGER_DIR.mkdir(exist_ok=True)
    rows_path = LEDGER_DIR / "token-usage.jsonl"
    with open(rows_path, "w", encoding="utf-8") as f:
        for sid, a in sorted(sessions.items(), key=lambda kv: kv[1].get("last_ts", "")):
            f.write(json.dumps({
                "session": sid, "last_ts": a.get("last_ts", ""), "msgs": a["msgs"],
                "input": a["input"], "output": a["output"], "cache_read": a["cache_read"],
                "cache_write": a["cache_w5m"] + a["cache_w1h"],
                "cost_usd": round(a["cost"], 4),
                "subagent_cost_usd": round(a.get("sidechain_cost", 0), 4),
                "models": dict(a["models"]),
            }) + "\n")
    grand = sum(a["cost"] for a in sessions.values())
    summ = {
        "generated_ts_note": "stamp externally; Date.now unavailable in some runtimes",
        "scope": "ALL" if args.all else (args.project or THIS_PROJECT),
        "sessions": len(sessions), "messages": len(records),
        "actual_cost_usd": round(grand, 2),
        "fable5_projection_usd": round(sum(message_cost(r, "fable-5") for r in records), 2),
        "opus48_projection_usd": round(sum(message_cost(r, "opus-4-8") for r in records), 2),
    }
    (LEDGER_DIR / "token-usage-summary.json").write_text(json.dumps(summ, indent=2))
    print(f"Wrote {rows_path} ({len(sessions)} sessions) + token-usage-summary.json")
    print(f"  actual ${summ['actual_cost_usd']}  |  all-Fable5 ${summ['fable5_projection_usd']}  |  all-Opus4.8 ${summ['opus48_projection_usd']}")


def main():
    ap = argparse.ArgumentParser(description="Deterministic token & cost ledger for Claude Code sessions")
    ap.add_argument("command", choices=["summary", "sessions", "session", "project-at", "snapshot"])
    ap.add_argument("id", nargs="?", help="session id prefix (for `session`)")
    ap.add_argument("--since", help="only messages on/after YYYY-MM-DD")
    ap.add_argument("--all", action="store_true", help="scan every project dir, not just this repo")
    ap.add_argument("--project", help="project slug under ~/.claude/projects (default: this repo)")
    ap.add_argument("--model", help="target model for `project-at` (e.g. fable-5, opus-4-8)")
    ap.add_argument("--limit", type=int, default=25, help="rows for `sessions`")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.command == "summary":
        cmd_summary(args)
    elif args.command == "sessions":
        cmd_sessions(args)
    elif args.command == "session":
        if not args.id:
            ap.error("`session` needs an id prefix")
        cmd_session(args)
    elif args.command == "project-at":
        if not args.model:
            ap.error("`project-at` needs --model")
        cmd_project_at(args)
    elif args.command == "snapshot":
        cmd_snapshot(args)


if __name__ == "__main__":
    main()
