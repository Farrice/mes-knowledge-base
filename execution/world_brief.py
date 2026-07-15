#!/usr/bin/env python3
"""world_brief.py — World Pulse research loop for the Chief of Staff OS.

Farrice avoids social media by design; the morning brief is his tap-in channel
to the world. This script writes `.agent/cos/world/YYYY-MM-DD.md`: 5-8 sourced
items across the active interests in `.agent/cos/interests.json`, each with a
one-line "why it matters" grounded in his live goals (`.agent/cos/goals.json`).

Research path (honest-receipt discipline, per execution/research.py):
  1. cost_gate.py check for every paid research service FIRST. Anything that
     needs approval is NOT called — no exceptions, no retries.
  2. The $0 Tavily floor leg of the unified research engine
     (execution/native_floor.tavily_search) does the actual gathering.
  3. If nothing sourced comes back, the file is written with
     `status: DEGRADED (<reason>)` and ZERO items. An empty honest file beats
     invented items — fabricating a news item is the one unforgivable failure.

Subcommands:
    generate [--force] [--max-items N]   Write today's world file
    verify                               Exit 0 iff today's file is honest+complete
    latest                               Print today's file path if present
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EXEC = REPO_ROOT / "execution"
COS = REPO_ROOT / ".agent" / "cos"
WORLD = COS / "world"
INTERESTS_PATH = COS / "interests.json"
GOALS_PATH = COS / "goals.json"

sys.path.insert(0, str(EXEC))

MIN_ITEMS = 5
DEFAULT_MAX_ITEMS = 8
MAX_LINES = 90

# Paid services that MUST clear the cost gate before any call. The default
# engine here is the $0 Tavily floor, so a blocked gate never blocks the file —
# it only forecloses the paid-accelerator upgrade path.
PAID_SERVICES = ["gemini-deep-research", "perplexity-research"]

# interest id -> (goal id to ground the "why" in, [why-line templates]).
# Templates may use {target} (shortened goal target from goals.json) and
# {topic} (the item's interest label). Grounded, never generic: every line
# names the live goal it feeds. Unknown interest ids fall back to the active
# revenue goal.
WHY_MAP = {
    "marketing": ("revenue-5k-incumbency", [
        "Positioning moves like this are the raw material for '{target}' — steal the frame before pitching health brands.",
        "Directly sellable to the Path A pipeline ('{target}') — a live example beats a framework in outreach.",
    ]),
    "copywriting": ("revenue-5k-incumbency", [
        "Copy craft feeding '{target}' — claim-safe brands pay for exactly this kind of conversion mechanics.",
        "A hook/proof pattern to test in the next client draft — the '{target}' work is won on copy, not credentials.",
    ]),
    "creative-strategy": ("revenue-5k-incumbency", [
        "Creative-strategy signal for '{target}' — this is the TrendScale/Josh-tier skill he charges for.",
        "Campaign thinking that upgrades the service behind '{target}' without repositioning (Incumbency Rule intact).",
    ]),
    "content-strategy": ("revenue-scale-20-30k", [
        "Feeds the authority flywheel behind '{target}' — distribution shifts decide where his content compounds.",
        "LinkedIn/newsletter terrain intel for '{target}' — he publishes there; the ground rules just moved.",
    ]),
    "ai-agentic-tooling": ("revenue-5k-incumbency", [
        "His unfair advantage — AI proficiency not yet converted to revenue ('{target}'); tooling shifts are margin.",
        "Harness-relevant: what the frontier ships this week decides what Antigravity should absorb vs ignore.",
    ]),
    "anime": ("father-presence", [
        "Personal recharge + storytelling craft — the interiority tricks in {topic} feed Parallax; zero business required.",
        "Joy input, not work input — protects the '{target}' side of the ledger; maybe a future JJ co-watch.",
    ]),
}
FALLBACK_WHY = "Signal in a declared interest area ({topic}) — logged because it touches the active goal '{target}'."


def _today() -> str:
    return datetime.now().date().isoformat()


def today_path() -> Path:
    return WORLD / f"{_today()}.md"


def load_interests() -> tuple:
    """Return (active_interests, max_items)."""
    try:
        data = json.loads(INTERESTS_PATH.read_text())
        active = [i for i in data.get("interests", []) if i.get("active", True)]
        return active, int(data.get("max_items", DEFAULT_MAX_ITEMS))
    except Exception:
        return [], DEFAULT_MAX_ITEMS


def load_goals() -> dict:
    """Active goals keyed by id."""
    try:
        goals = json.loads(GOALS_PATH.read_text()).get("goals", [])
        return {g["id"]: g for g in goals if g.get("status") == "active"}
    except Exception:
        return {}


def gate_check(service: str) -> tuple:
    """Run the cost gate pre-flight. Returns (allowed: bool, summary: str).
    Any non-zero exit (needs-approval, denied, script error) = NOT allowed."""
    try:
        proc = subprocess.run(
            [sys.executable, str(EXEC / "cost_gate.py"), "check", "--service", service],
            capture_output=True, text=True, timeout=30, cwd=REPO_ROOT,
        )
        allowed = proc.returncode == 0
        m = re.search(r"COST GATE: (.+?)\s*\(", proc.stdout or "")
        return allowed, (m.group(1).strip() if m else f"exit {proc.returncode}")
    except Exception as e:
        return False, f"gate check failed ({type(e).__name__})"


def _short_target(goal: dict, limit: int = 70) -> str:
    t = (goal or {}).get("target", "")
    t = re.sub(r"\s+", " ", t).strip()
    return t[: limit - 1] + "…" if len(t) > limit else t


def build_why(interest_id: str, label: str, goals: dict, variant: int) -> str:
    goal_id, templates = WHY_MAP.get(interest_id, ("", []))
    goal = goals.get(goal_id)
    if not goal:  # mapped goal retired/missing -> ground in any active revenue goal
        goal = goals.get("revenue-5k-incumbency") or (next(iter(goals.values())) if goals else {})
    if not templates:
        templates = [FALLBACK_WHY]
    tpl = templates[variant % len(templates)]
    return tpl.format(target=_short_target(goal), topic=label)


def gather_items(interests: list, goals: dict, max_items: int) -> tuple:
    """Round-robin the active interests through the $0 Tavily floor leg.
    Returns (items, reason_if_empty). Items only ever come from real search
    results — a result without an http(s) URL is dropped, never patched."""
    try:
        from native_floor import tavily_search, load_env_vars
    except Exception as e:
        return [], f"research engine unavailable ({type(e).__name__})"

    env = load_env_vars()
    if not env.get("TAVILY_API_KEY"):
        return [], "no TAVILY_API_KEY (floor leg dark)"

    month_year = datetime.now().strftime("%B %Y")
    per_interest: list = []  # list of lists (ranked results per interest)
    for interest in interests:
        hints = interest.get("query_hints") or [interest.get("label", interest.get("id", ""))]
        query = f"{hints[0]} {month_year}"
        results = []
        seen = set()
        # Recency bar (Farrice 2026-07-14): news index, last 14 days only —
        # a "pulse" that surfaces 2025 content is noise, not signal.
        for res in tavily_search(query, max_results=5, env=env,
                                 days=14, topic="news"):
            url = (res.get("url") or "").strip()
            title = re.sub(r"\s+", " ", (res.get("title") or "").strip())
            content = re.sub(r"\s+", " ", (res.get("content") or "").strip())
            if not url.startswith(("http://", "https://")):
                continue
            if len(title) < 15 and len(content) < 60:
                continue  # too thin to be an honest headline
            if url in seen:
                continue
            seen.add(url)
            results.append({
                "interest_id": interest.get("id", ""),
                "label": interest.get("label", interest.get("id", "")),
                "headline": (title or content[:100])[:110],
                "url": url,
            })
        per_interest.append(results)

    # Round-robin so every interest gets a seat before any gets two.
    items, counts = [], {}
    for rank in range(3):
        for results in per_interest:
            if len(items) >= max_items:
                break
            if rank < len(results):
                r = results[rank]
                r["why"] = build_why(r["interest_id"], r["label"], goals,
                                     counts.get(r["interest_id"], 0))
                counts[r["interest_id"]] = counts.get(r["interest_id"], 0) + 1
                items.append(r)
    if not items:
        return [], "search returned zero sourced results"
    return items, ""


def render_file(items: list, status: str, gates: list, max_items: int) -> str:
    today = _today()
    lines = [
        f"# World Pulse — {today}",
        "",
        f"status: {status}",
        f"generated: {datetime.now().isoformat(timespec='seconds')}",
        f"engine: tavily-floor ($0) · gates: {', '.join(gates)}",
        "",
    ]
    if not items:
        lines.append("No sourced items today. This file is honestly empty — no item is ever")
        lines.append("fabricated to fill space. Retry: `python3 execution/world_brief.py generate --force`")
        lines.append("")
    for i, item in enumerate(items[:max_items], 1):
        lines.append(f"## {i}. [{item['label']}] {item['headline']}")
        lines.append(f"**Source:** {item['url']}")
        lines.append(f"**Why it matters:** {item['why']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def cmd_generate(force: bool, max_items_override: int) -> int:
    WORLD.mkdir(parents=True, exist_ok=True)
    out = today_path()
    if out.exists() and not force:
        print(f"World file already exists: {out} (use --force to regenerate)")
        return 0

    interests, max_items = load_interests()
    if max_items_override:
        max_items = max_items_override
    goals = load_goals()

    # Cost-gate pre-flight on every paid service. This engine only uses the $0
    # Tavily floor, but the check is the contract: if a paid accelerator is
    # ever wired in here, a non-zero gate means it is NOT called.
    gates, paid_allowed = [], {}
    for svc in PAID_SERVICES:
        allowed, summary = gate_check(svc)
        paid_allowed[svc] = allowed
        gates.append(f"{svc}={'allowed' if allowed else 'BLOCKED (' + summary + ')'}")

    if not interests:
        text = render_file([], "DEGRADED (no active interests in interests.json)", gates, max_items)
        out.write_text(text)
        print(f"World file written DEGRADED (no interests): {out}")
        return 0

    items, empty_reason = gather_items(interests, goals, max_items)
    if len(items) >= MIN_ITEMS:
        status = "OK"
    elif items:
        status = f"DEGRADED (only {len(items)} sourced items — floor thin, nothing fabricated to fill)"
    else:
        status = f"DEGRADED (research gate: {empty_reason})"

    text = render_file(items, status, gates, max_items)
    # Hard ceiling: trim items (never pad) if the file would exceed MAX_LINES.
    while len(text.splitlines()) >= MAX_LINES and items:
        items = items[:-1]
        text = render_file(items, status, gates, max_items)
    out.write_text(text)
    print(f"World file written: {out} ({len(items)} items, {status})")
    return 0


def cmd_verify() -> int:
    out = today_path()
    if not out.exists():
        print(f"FAIL: no world file for today ({out})")
        return 1
    text = out.read_text()
    n_lines = len(text.splitlines())
    if n_lines >= MAX_LINES:
        print(f"FAIL: {out.name} is {n_lines} lines (must be <{MAX_LINES})")
        return 1
    status_m = re.search(r"^status: (.+)$", text, re.MULTILINE)
    status = status_m.group(1).strip() if status_m else ""
    degraded = status.startswith("DEGRADED")

    items = re.findall(r"^## \d+\. .+$", text, re.MULTILINE)
    sourced = re.findall(r"^\*\*Source:\*\* https?://\S+", text, re.MULTILINE)
    if degraded:
        print(f"PASS (DEGRADED): {out.name} — {status} · {len(items)} items · {n_lines} lines")
        return 0
    if len(items) < MIN_ITEMS:
        print(f"FAIL: {len(items)} items (need >={MIN_ITEMS}) and status is not DEGRADED")
        return 1
    if len(sourced) < len(items):
        print(f"FAIL: {len(items)} items but only {len(sourced)} http(s) sources — every item must be sourced")
        return 1
    print(f"PASS: {out.name} — {len(items)} items, all sourced, {n_lines} lines")
    return 0


def cmd_latest() -> int:
    out = today_path()
    if out.exists():
        print(out)
        return 0
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_gen = sub.add_parser("generate", help="write today's world pulse file")
    p_gen.add_argument("--force", action="store_true")
    p_gen.add_argument("--max-items", type=int, default=0)
    sub.add_parser("verify", help="exit 0 iff today's file is honest and complete")
    sub.add_parser("latest", help="print today's file path if present")
    args = parser.parse_args()

    if args.cmd == "generate":
        return cmd_generate(args.force, args.max_items)
    if args.cmd == "verify":
        return cmd_verify()
    if args.cmd == "latest":
        return cmd_latest()
    return 1


if __name__ == "__main__":
    sys.exit(main())
