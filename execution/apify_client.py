#!/usr/bin/env python3
"""
Apify Client — scraping/social-listening for Antigravity workflows.

CLI wrapper for Apify actors with built-in budget guard. Mirrors
execution/perplexity_client.py pattern.

KEY CONTRACT (read this before editing):
This wrapper NEVER raises on budget exhaustion. It always returns a
structured JSON response. When the monthly cap is hit it returns
{"status": "budget_exhausted", "fallback": true, ...} and the calling
workflow is expected to route to Perplexity / Tavily / web search instead.
This is what makes Apify integration safe — workflows degrade, they don't
break.

Usage:
    python execution/apify_client.py budget-status
    python execution/apify_client.py reddit "first time home buyer" --limit 50 --comments
    python execution/apify_client.py reddit --subreddit FirstTimeHomeBuyer --limit 30
    python execution/apify_client.py instagram realestatewithjing --limit 20
    python execution/apify_client.py tiktok firsttimebuyer --limit 50
    python execution/apify_client.py youtube "pilates day in life" --limit 5 --transcript
    python execution/apify_client.py amazon "yoga mat" --limit 30
    python execution/apify_client.py maps "coffee shop" --location "Los Angeles" --limit 30
    python execution/apify_client.py web "https://example.com"

Budget policy: directives/apify-usage-policy.md
Ledger file:   .agent/apify-usage.json
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests

# ---------------------------------------------------------------------------
# Paths & Constants
# ---------------------------------------------------------------------------

BASE = Path(__file__).parent.parent
ENV_PATH = BASE / ".env"
USAGE_FILE = BASE / ".agent" / "apify-usage.json"
WARN_FLAG = BASE / ".agent" / "apify-budget-warning.flag"

PLAN_DOLLARS = 29.00
SOFT_WARN_PCT = 0.70   # 70% → yellow, prefer cheap actors
HARD_STOP_PCT = 0.90   # 90% → red, refuse new runs

# Curated actor whitelist — must match --tools in .mcp.json.
# cost_per_result is a conservative estimate based on Apify Store pricing
# (April 2026). Real cost may differ slightly; tracker logs actual after each run.
ACTORS = {
    "reddit":    {"id": "trudax/reddit-scraper-lite",     "cost_per_result": 0.001},
    "instagram": {"id": "apify/instagram-scraper",        "cost_per_result": 0.0005},
    "tiktok":    {"id": "clockworks/free-tiktok-scraper", "cost_per_result": 0.004},
    "youtube":   {"id": "apidojo/youtube-scraper",        "cost_per_result": 0.005},
    "amazon":    {"id": "junglee/amazon-scraper",         "cost_per_result": 0.0015},
    "maps":      {"id": "compass/crawler-google-places",  "cost_per_result": 0.007},
    "web":       {"id": "apify/rag-web-browser",          "cost_per_result": 0.003},
}

API_URL_TEMPLATE = "https://api.apify.com/v2/acts/{actor_id}/run-sync-get-dataset-items"


# ---------------------------------------------------------------------------
# Environment & Usage File
# ---------------------------------------------------------------------------

def load_env(env_path: Optional[Path] = None):
    """Load .env file into os.environ (setdefault — won't overwrite existing)."""
    path = env_path or ENV_PATH
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def current_month() -> str:
    return datetime.now().strftime("%Y-%m")


def new_usage() -> dict:
    return {
        "month": current_month(),
        "plan_dollars": PLAN_DOLLARS,
        "soft_warn_pct": SOFT_WARN_PCT,
        "hard_stop_pct": HARD_STOP_PCT,
        "spent_dollars": 0.0,
        "runs": [],
    }


def load_usage() -> dict:
    """Load usage file. Auto-creates on first run. Auto-resets on month change."""
    if not USAGE_FILE.exists():
        USAGE_FILE.parent.mkdir(parents=True, exist_ok=True)
        save_usage(new_usage())
        return new_usage()
    try:
        data = json.loads(USAGE_FILE.read_text())
    except json.JSONDecodeError:
        return new_usage()
    if data.get("month") != current_month():
        return new_usage()
    return data


def save_usage(data: dict):
    USAGE_FILE.parent.mkdir(parents=True, exist_ok=True)
    USAGE_FILE.write_text(json.dumps(data, indent=2))


def budget_state(usage: dict) -> str:
    """Returns 'green', 'yellow', or 'red'."""
    pct = usage["spent_dollars"] / usage["plan_dollars"]
    if pct >= HARD_STOP_PCT:
        return "red"
    if pct >= SOFT_WARN_PCT:
        return "yellow"
    return "green"


def fallback_response(reason: str) -> dict:
    return {
        "status": "budget_exhausted",
        "fallback": True,
        "message": reason,
        "alternative": "Use Perplexity (perplexity_client.py) or web search instead.",
        "items": [],
    }


# ---------------------------------------------------------------------------
# Actor Runner
# ---------------------------------------------------------------------------

def run_actor(actor_key: str, run_input: dict, max_results: int) -> dict:
    """
    Runs an Apify actor with budget guard.
    NEVER raises on budget exhaustion — returns {"fallback": True}.
    """
    if actor_key not in ACTORS:
        return {
            "status": "error",
            "fallback": True,
            "message": f"Unknown actor: {actor_key}",
            "items": [],
        }

    usage = load_usage()
    state = budget_state(usage)

    estimated = ACTORS[actor_key]["cost_per_result"] * max_results
    projected_spent = usage["spent_dollars"] + estimated
    projected_pct = projected_spent / usage["plan_dollars"]

    # Hard stop — would this push us past 90%?
    if state == "red" or projected_pct >= HARD_STOP_PCT:
        WARN_FLAG.write_text(f"red:{now_iso()}")
        return fallback_response(
            f"Apify monthly cap (${PLAN_DOLLARS:.2f}) would be exceeded. "
            f"Current: ${usage['spent_dollars']:.2f}, projected: ${projected_spent:.2f}."
        )

    # Yellow — set warn flag, still allow
    if state == "yellow":
        WARN_FLAG.write_text(f"yellow:{now_iso()}")
        sys.stderr.write(
            f"WARNING: Apify budget at "
            f"{usage['spent_dollars'] / usage['plan_dollars'] * 100:.0f}% "
            f"(${usage['spent_dollars']:.2f}/${PLAN_DOLLARS:.2f}). "
            f"Prefer cheap actors (reddit, instagram, web).\n"
        )
    else:
        if WARN_FLAG.exists():
            WARN_FLAG.unlink()

    token = os.environ.get("APIFY_TOKEN", "")
    if not token:
        return {
            "status": "error",
            "fallback": True,
            "message": "APIFY_TOKEN not set in environment. Add it to .env.",
            "items": [],
        }

    actor_id = ACTORS[actor_key]["id"].replace("/", "~")
    url = API_URL_TEMPLATE.format(actor_id=actor_id)

    try:
        response = requests.post(
            url,
            params={"token": token, "timeout": 90, "memory": 1024},
            json=run_input,
            timeout=180,
        )
        response.raise_for_status()
        items = response.json()
    except requests.RequestException as e:
        return {
            "status": "error",
            "fallback": True,
            "message": f"Apify API error: {e}",
            "items": [],
        }

    actual_count = len(items) if isinstance(items, list) else 0
    actual_cost = ACTORS[actor_key]["cost_per_result"] * actual_count

    # Log to usage file
    usage["spent_dollars"] = round(usage["spent_dollars"] + actual_cost, 4)
    usage["runs"].append({
        "ts": now_iso(),
        "actor": actor_key,
        "results": actual_count,
        "cost": round(actual_cost, 4),
    })
    if len(usage["runs"]) > 200:
        usage["runs"] = usage["runs"][-200:]
    save_usage(usage)

    return {
        "status": "ok",
        "fallback": False,
        "actor": actor_key,
        "result_count": actual_count,
        "cost_dollars": round(actual_cost, 4),
        "spent_total": usage["spent_dollars"],
        "remaining_dollars": round(PLAN_DOLLARS - usage["spent_dollars"], 4),
        "items": items if isinstance(items, list) else [],
    }


# ---------------------------------------------------------------------------
# CLI Commands
# ---------------------------------------------------------------------------

def cmd_budget_status(_args=None):
    usage = load_usage()
    pct = usage["spent_dollars"] / usage["plan_dollars"] * 100
    state = budget_state(usage)
    print(json.dumps({
        "month": usage["month"],
        "plan_dollars": usage["plan_dollars"],
        "spent_dollars": round(usage["spent_dollars"], 4),
        "remaining_dollars": round(usage["plan_dollars"] - usage["spent_dollars"], 4),
        "percent_used": round(pct, 1),
        "state": state,
        "soft_warn_at": round(usage["plan_dollars"] * SOFT_WARN_PCT, 2),
        "hard_stop_at": round(usage["plan_dollars"] * HARD_STOP_PCT, 2),
        "run_count": len(usage["runs"]),
        "last_runs": usage["runs"][-5:],
    }, indent=2))


def cmd_budget_reset(_args=None):
    save_usage(new_usage())
    if WARN_FLAG.exists():
        WARN_FLAG.unlink()
    print(json.dumps({"status": "reset", "month": current_month()}))


def cmd_reddit(args):
    """
    trudax/reddit-scraper-lite uses startUrls (search URLs or subreddit URLs).
    There is no separate "searches" field — queries become search URLs.
    """
    start_urls = []
    if args.query:
        from urllib.parse import quote_plus
        q = quote_plus(args.query)
        start_urls.append({"url": f"https://www.reddit.com/search/?q={q}&type=link&sort=relevance"})
    if args.subreddit:
        start_urls.append({"url": f"https://www.reddit.com/r/{args.subreddit}/"})
    if not start_urls:
        print(json.dumps({"status": "error", "fallback": True,
                          "message": "Reddit needs --subreddit or a query.",
                          "items": []}, indent=2))
        return
    run_input = {
        "startUrls": start_urls,
        "maxItems": args.limit,
        "scrollTimeout": 40,
        "skipComments": not args.comments,
        "skipUserPosts": False,
        "skipCommunity": False,
    }
    print(json.dumps(run_actor("reddit", run_input, args.limit), indent=2))


def cmd_instagram(args):
    handle = args.handle.lstrip("@")
    run_input = {
        "directUrls": [f"https://www.instagram.com/{handle}/"],
        "resultsType": "posts",
        "resultsLimit": args.limit,
        # Without this, the scraper paginates from account creation forward
        # and returns 2010-era posts. Force recency window so we get current posts.
        "onlyPostsNewerThan": "365 days",
    }
    print(json.dumps(run_actor("instagram", run_input, args.limit), indent=2))


def cmd_tiktok(args):
    run_input = {"hashtags": [args.hashtag], "resultsPerPage": args.limit}
    print(json.dumps(run_actor("tiktok", run_input, args.limit), indent=2))


def cmd_youtube(args):
    # apidojo/youtube-scraper expects `keywords` (array), `startUrls`, or
    # `youtubeHandles`. The previous "searchQueries" field caused 400 errors.
    # maxItems is the result cap, not maxResults.
    run_input = {
        "keywords": [args.query],
        "maxItems": args.limit,
    }
    if args.transcript:
        run_input["downloadSubtitles"] = True
        run_input["subtitlesLanguage"] = "en"
    print(json.dumps(run_actor("youtube", run_input, args.limit), indent=2))


def cmd_amazon(args):
    url = "https://www.amazon.com/gp/bestsellers" if args.best_sellers \
        else f"https://www.amazon.com/s?k={args.query.replace(' ', '+')}"
    run_input = {
        "categoryOrProductUrls": [{"url": url}],
        "maxItemsPerStartUrl": args.limit,
    }
    print(json.dumps(run_actor("amazon", run_input, args.limit), indent=2))


def cmd_maps(args):
    run_input = {
        "searchStringsArray": [args.query],
        "locationQuery": args.location,
        "maxCrawledPlacesPerSearch": args.limit,
    }
    print(json.dumps(run_actor("maps", run_input, args.limit), indent=2))


def cmd_web(args):
    run_input = {"query": args.url, "maxResults": 1}
    print(json.dumps(run_actor("web", run_input, 1), indent=2))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    load_env()
    p = argparse.ArgumentParser(prog="apify_client.py")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("budget-status", help="Show current month budget")
    sub.add_parser("budget-reset", help="Manually reset budget (use sparingly)")

    pr = sub.add_parser("reddit", help="Reddit posts/comments")
    pr.add_argument("query", nargs="?", default="")
    pr.add_argument("--subreddit", default="")
    pr.add_argument("--limit", type=int, default=50)
    pr.add_argument("--comments", action="store_true")

    pi = sub.add_parser("instagram", help="Instagram profile/posts")
    pi.add_argument("handle")
    pi.add_argument("--limit", type=int, default=20)

    pt = sub.add_parser("tiktok", help="TikTok hashtag scrape")
    pt.add_argument("hashtag")
    pt.add_argument("--limit", type=int, default=50)

    py = sub.add_parser("youtube", help="YouTube search + transcripts")
    py.add_argument("query")
    py.add_argument("--limit", type=int, default=10)
    py.add_argument("--transcript", action="store_true")

    pa = sub.add_parser("amazon", help="Amazon products / Best Sellers")
    pa.add_argument("query", nargs="?", default="")
    pa.add_argument("--limit", type=int, default=30)
    pa.add_argument("--best-sellers", action="store_true", dest="best_sellers")

    pm = sub.add_parser("maps", help="Google Maps places")
    pm.add_argument("query")
    pm.add_argument("--location", default="")
    pm.add_argument("--limit", type=int, default=30)

    pw = sub.add_parser("web", help="Generic JS-rendered web fetch")
    pw.add_argument("url")

    args = p.parse_args()

    handlers = {
        "budget-status": cmd_budget_status,
        "budget-reset":  cmd_budget_reset,
        "reddit":        cmd_reddit,
        "instagram":     cmd_instagram,
        "tiktok":        cmd_tiktok,
        "youtube":       cmd_youtube,
        "amazon":        cmd_amazon,
        "maps":          cmd_maps,
        "web":           cmd_web,
    }
    handlers[args.cmd](args)


if __name__ == "__main__":
    main()
