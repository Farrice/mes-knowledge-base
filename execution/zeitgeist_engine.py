#!/usr/bin/env python3
"""
zeitgeist_engine.py — deterministic scrape layer of the daily zeitgeist brief (Layer 3).

Reads .agent/zeitgeist-lanes.json, decides which lanes are due today (rotation via
.agent/zeitgeist-state.json), runs each lane's pulls through apify_client.py with
--pulse-mode ($5/mo sub-ledger, graceful skip), and writes a trimmed signal pack to
.tmp/zeitgeist/<date>-<lane>-signals.json for the synthesis pass (headless claude,
see .agent/zeitgeist-synthesis-prompt.md and execution/zeitgeist_run.sh).

Never raises on budget exhaustion — pulse_skipped / fallback pulls are recorded in the
pack and the engine exits 0. A pack with zero live pulls is still written (the synthesis
pass then skips brief production for that lane).

Usage:
    python3 execution/zeitgeist_engine.py run [--lane NAME] [--force]
    python3 execution/zeitgeist_engine.py status
"""
import argparse
import json
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANES_FILE = ROOT / ".agent" / "zeitgeist-lanes.json"
STATE_FILE = ROOT / ".agent" / "zeitgeist-state.json"
OUT_DIR = ROOT / ".tmp" / "zeitgeist"
APIFY = ROOT / "execution" / "apify_client.py"

# Fields worth carrying into the synthesis pack, per actor family. Everything else is
# dropped — packs must stay small enough to hand a headless synthesis run whole.
KEEP_FIELDS = {
    "twitter": ["text", "id", "type"],
    "threads-search": ["post_text", "author_username", "like_count", "reply_count",
                       "repost_count", "post_url", "posted_at"],
    "linkedin-search": ["firstName", "lastName", "summary", "linkedinUrl", "location"],
    "linkedin-posts": ["text", "url", "posted_at", "stats", "post_type"],
    "reddit": ["title", "body", "communityName", "upVotes", "numberOfComments", "url"],
    "youtube": ["title", "text", "viewCountInt", "url", "channelName", "date"],
    "facebook-ads": ["page_name", "ad_archive_id", "is_active", "snapshot"],
}
MAX_ITEMS_PER_PULL = 15
MAX_TEXT_CHARS = 500


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_json(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def trim_item(actor, item):
    keep = KEEP_FIELDS.get(actor)
    if not keep or not isinstance(item, dict):
        slim = item if isinstance(item, dict) else {"value": item}
    else:
        slim = {k: item.get(k) for k in keep if item.get(k) is not None}
    for k, v in list(slim.items()):
        if isinstance(v, str) and len(v) > MAX_TEXT_CHARS:
            slim[k] = v[:MAX_TEXT_CHARS] + "…"
    return slim


def run_pull(pull):
    cmd = [sys.executable, str(APIFY), pull["actor"], pull["arg"],
           "--limit", str(pull.get("limit", 20)), "--pulse-mode"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300, cwd=ROOT)
        data = json.loads(r.stdout) if r.stdout.strip() else {}
    except (subprocess.TimeoutExpired, json.JSONDecodeError) as e:
        return {"actor": pull["actor"], "arg": pull["arg"], "status": "error",
                "message": str(e)[:200], "items": []}
    items = data.get("items") or []
    return {
        "actor": pull["actor"],
        "arg": pull["arg"],
        "status": data.get("status", "error"),
        "cost_dollars": data.get("cost_dollars"),
        "result_count": data.get("result_count", len(items)),
        "message": None if data.get("status") == "ok" else str(data.get("message"))[:200],
        "items": [trim_item(pull["actor"], it) for it in items[:MAX_ITEMS_PER_PULL]],
    }


def lanes_due(lanes, state, force=False, only=None):
    today = date.today()
    due = []
    for name, lane in lanes.items():
        if only and name != only:
            continue
        if force or only:
            due.append(name)
            continue
        last = state.get("last_run", {}).get(name)
        if not last:
            due.append(name)
            continue
        days_since = (today - date.fromisoformat(last)).days
        if days_since >= lane.get("cadence_days", 1):
            due.append(name)
    return due


def cmd_run(args):
    lanes = load_json(LANES_FILE, {}).get("lanes", {})
    if not lanes:
        print(f"[zeitgeist] no lanes configured at {LANES_FILE}")
        return 0
    state = load_json(STATE_FILE, {})
    due = lanes_due(lanes, state, force=args.force, only=args.lane)
    if not due:
        print("[zeitgeist] no lanes due today — nothing to do")
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    packs = []
    for name in due:
        lane = lanes[name]
        pulls = [run_pull(p) for p in lane.get("pulls", [])]
        live = [p for p in pulls if p["status"] == "ok" and p["items"]]
        cost = round(sum(p.get("cost_dollars") or 0 for p in pulls), 4)
        pack = {
            "lane": name,
            "title": lane.get("title", name),
            "brief_lens": lane.get("brief_lens", ""),
            "date": today,
            "generated_at": now_iso(),
            "run_cost_usd": cost,
            "stack": sorted({p["actor"] for p in live}),
            "pulls": pulls,
            "live_pull_count": len(live),
        }
        pack_path = OUT_DIR / f"{today}-{name}-signals.json"
        pack_path.write_text(json.dumps(pack, indent=2, ensure_ascii=False), encoding="utf-8")
        packs.append(str(pack_path))
        state.setdefault("last_run", {})[name] = today
        state.setdefault("history", []).append(
            {"ts": now_iso(), "lane": name, "cost": cost, "live_pulls": len(live)})
        state["history"] = state["history"][-200:]
        print(f"[zeitgeist] {name}: {len(live)}/{len(pulls)} pulls live, ${cost:.4f} → {pack_path}")

    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")
    print(json.dumps({"packs": packs}))
    return 0


def cmd_status(args):
    state = load_json(STATE_FILE, {})
    lanes = load_json(LANES_FILE, {}).get("lanes", {})
    print("lane                       cadence  last_run    due?")
    today = date.today()
    for name, lane in lanes.items():
        last = state.get("last_run", {}).get(name, "never")
        due = "YES" if name in lanes_due(lanes, state) else "no"
        print(f"{name:26} {lane.get('cadence_days', 1)}d       {last:11} {due}")
    hist = state.get("history", [])[-10:]
    if hist:
        print("\nrecent runs:")
        for h in hist:
            print(f"  {h['ts'][:16]} {h['lane']} ${h['cost']:.4f} ({h['live_pulls']} live pulls)")
    subprocess.run([sys.executable, str(APIFY), "pulse-budget-status"], cwd=ROOT)
    return 0


def main():
    ap = argparse.ArgumentParser(prog="zeitgeist_engine.py")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pr = sub.add_parser("run", help="scrape due lanes into signal packs")
    pr.add_argument("--lane", help="run one lane regardless of rotation")
    pr.add_argument("--force", action="store_true", help="run all lanes regardless of rotation")
    sub.add_parser("status", help="rotation state + recent runs + pulse budget")
    args = ap.parse_args()
    sys.exit(cmd_run(args) if args.cmd == "run" else cmd_status(args))


if __name__ == "__main__":
    main()
