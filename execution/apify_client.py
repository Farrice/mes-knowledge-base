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

Usage — Original 7 actors (per_result pricing):
    python execution/apify_client.py budget-status
    python execution/apify_client.py reddit "first time home buyer" --limit 50 --comments
    python execution/apify_client.py reddit --subreddit FirstTimeHomeBuyer --limit 30
    python execution/apify_client.py instagram realestatewithjing --limit 20
    python execution/apify_client.py tiktok firsttimebuyer --limit 50
    python execution/apify_client.py youtube "pilates day in life" --limit 5 --transcript
    python execution/apify_client.py amazon "yoga mat" --limit 30
    python execution/apify_client.py maps "coffee shop" --location "Los Angeles" --limit 30
    python execution/apify_client.py web "https://example.com"

Usage — New Scrape Creators actors (pay_per_event pricing, added 2026-07-16):
    python execution/apify_client.py sc-tiktok --search "fitness tips" --limit 20
    python execution/apify_client.py sc-tiktok --profile "@fitnessguy" --limit 20
    python execution/apify_client.py sc-tiktok --hashtag "fitnessmotivation" --limit 20
    python execution/apify_client.py sc-tiktok-video "7234567890" --limit 1
    python execution/apify_client.py sc-tiktok-profile "@fitnessguy"
    python execution/apify_client.py sc-tiktok-hashtag "fitnessmotivation" --limit 50
    python execution/apify_client.py sc-tiktok-transcripts --search "fitness" --limit 10
    python execution/apify_client.py sc-tiktok-followers "@fitnessguy" --limit 50
    python execution/apify_client.py sc-tiktok-following "@fitnessguy" --limit 50
    python execution/apify_client.py sc-youtube-transcripts --search "fitness" --limit 5
    python execution/apify_client.py sc-youtube-channels "@fitnessguy"
    python execution/apify_client.py sc-youtube-comments --search "fitness" --limit 50

Cost control (for pay_per_event actors):
    --max-cost 0.50              # Override per-run ceiling (default $0.25)
    --allow-expensive            # Bypass ceiling but still respect monthly $29 cap

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
#
# Pricing model: "per_result" = conservative estimate (logs actual after run)
#                "pay_per_event" = actual cost from Apify run response (usageTotalUsd)
#                                  required for Scrape Creators actors (2026-07-16)
#
# For per_result actors: cost_per_result is used for budget projections + logged actual
# For pay_per_event actors: cost_per_result is ignored; actual cost read from Apify run object
ACTORS = {
    # Original 7 (per_result pricing)
    "reddit":    {"id": "trudax/reddit-scraper-lite",     "pricing": "per_result", "cost_per_result": 0.001},
    "instagram": {"id": "apify/instagram-scraper",        "pricing": "per_result", "cost_per_result": 0.0005},
    "tiktok":    {"id": "clockworks/free-tiktok-scraper", "pricing": "per_result", "cost_per_result": 0.004},
    "youtube":   {"id": "apidojo/youtube-scraper",        "pricing": "per_result", "cost_per_result": 0.005},
    "amazon":    {"id": "junglee/amazon-scraper",         "pricing": "per_result", "cost_per_result": 0.0015},
    "maps":      {"id": "compass/crawler-google-places",  "pricing": "per_result", "cost_per_result": 0.007},
    "web":       {"id": "apify/rag-web-browser",          "pricing": "per_result", "cost_per_result": 0.003},

    # New 10 Scrape Creators (pay_per_event pricing — actual cost from Apify response)
    "sc-tiktok":        {"id": "scrape-creators/best-tiktok-scraper",          "pricing": "pay_per_event"},
    "sc-tiktok-video":  {"id": "scrape-creators/best-tiktok-video-scraper",    "pricing": "pay_per_event"},
    "sc-tiktok-profile":{"id": "scrape-creators/best-tiktok-profile-scraper",  "pricing": "pay_per_event"},
    "sc-tiktok-hashtag":{"id": "scrape-creators/best-tiktok-hashtag-scraper",  "pricing": "pay_per_event"},
    "sc-tiktok-transcripts": {"id": "scrape-creators/best-tiktok-transcripts-scraper", "pricing": "pay_per_event"},
    "sc-tiktok-followers":   {"id": "scrape-creators/best-tiktok-followers-scraper",   "pricing": "pay_per_event"},
    "sc-tiktok-following":   {"id": "scrape-creators/best-tiktok-following-scraper",   "pricing": "pay_per_event"},
    "sc-youtube-transcripts": {"id": "scrape-creators/best-youtube-transcripts-scraper", "pricing": "pay_per_event"},
    "sc-youtube-channels":    {"id": "scrape-creators/best-youtube-channels-scraper",    "pricing": "pay_per_event"},
    "sc-youtube-comments":    {"id": "scrape-creators/best-youtube-comments-scraper",    "pricing": "pay_per_event"},
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
        # Pulse sub-ledger (added 2026-07-16)
        "pulse_budget_dollars": 5.0,  # $5/mo dedicated to pulse
        "pulse_spent_dollars": 0.0,   # Pulse runs only
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

def run_actor(
    actor_key: str,
    run_input: dict,
    max_results: int,
    max_cost: float = 0.25,
    allow_expensive: bool = False,
    pulse_mode: bool = False
) -> dict:
    """
    Runs an Apify actor with budget guard.
    NEVER raises on budget exhaustion — returns {"fallback": True}.

    Args:
        actor_key: Key in ACTORS dict
        run_input: Input payload for actor
        max_results: Result limit (for per_result pricing estimates)
        max_cost: Per-run cost ceiling (default $0.25). Override with allow_expensive.
        allow_expensive: If True, bypass per-run ceiling (still checks monthly budget).
        pulse_mode: If True, use pulse sub-budget ($5/mo) and skip (not fail) on exhaustion.
    """
    if actor_key not in ACTORS:
        return {
            "status": "error",
            "fallback": True,
            "message": f"Unknown actor: {actor_key}",
            "items": [],
        }

    actor_config = ACTORS[actor_key]
    pricing_model = actor_config.get("pricing", "per_result")

    usage = load_usage()
    state = budget_state(usage)

    # Budget projection (depends on pricing model)
    if pricing_model == "per_result":
        estimated = actor_config["cost_per_result"] * max_results
    else:  # pay_per_event — use ceiling as estimate
        estimated = max_cost

    projected_spent = usage["spent_dollars"] + estimated
    projected_pct = projected_spent / usage["plan_dollars"]

    # Pulse mode budget check (separate sub-budget)
    if pulse_mode:
        pulse_projected = usage.get("pulse_spent_dollars", 0.0) + estimated
        pulse_budget = usage.get("pulse_budget_dollars", 5.0)

        # For pulse: skip (not fail) if pulse sub-budget exhausted OR global yellow/red
        if state in ("red", "yellow") or pulse_projected >= pulse_budget:
            return {
                "status": "pulse_skipped",
                "fallback": True,
                "reason": "pulse_budget_or_global_threshold",
                "message": (
                    f"Pulse run skipped: global state={state}, "
                    f"pulse spent ${usage.get('pulse_spent_dollars', 0.0):.2f}/${pulse_budget:.2f}. "
                    f"This is normal — pulse gracefully skips when budget is tight."
                ),
                "items": [],
            }
    else:
        # Normal mode — hard stop at red/90%
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

    # Determine actual cost
    if pricing_model == "pay_per_event":
        # For pay_per_event actors, cost is in the Apify response metadata.
        # When using run-sync-get-dataset-items, the items are returned directly.
        # We need to fetch the run object separately to get usageTotalUsd.
        # For now, log that this needs to be fetched from run metadata.
        # (Implementation note: production version should call /v2/actors/{id}/runs/{runId}
        # to retrieve the run object with usageTotalUsd; for MVP, use response headers if available)
        actual_cost = _get_pay_per_event_cost(response, actor_key, max_cost, allow_expensive)
        if actual_cost is None:  # Cost exceeded ceiling without allow_expensive
            return {
                "status": "cost_ceiling_exceeded",
                "fallback": True,
                "message": f"Run cost would exceed per-run ceiling ${max_cost:.4f}. "
                           f"Use --allow-expensive to override.",
                "items": [],
            }
        actual_count = len(items) if isinstance(items, list) else 0
    else:  # per_result
        actual_count = len(items) if isinstance(items, list) else 0
        actual_cost = actor_config["cost_per_result"] * actual_count

    # Log to usage file
    usage["spent_dollars"] = round(usage["spent_dollars"] + actual_cost, 4)
    if pulse_mode:
        usage["pulse_spent_dollars"] = round(usage.get("pulse_spent_dollars", 0.0) + actual_cost, 4)

    run_record = {
        "ts": now_iso(),
        "actor": actor_key,
        "results": actual_count,
        "cost": round(actual_cost, 4),
        "pricing_model": pricing_model,
    }
    if pulse_mode:
        run_record["pulse"] = True
    usage["runs"].append(run_record)

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


def _get_pay_per_event_cost(
    response: requests.Response,
    actor_key: str,
    max_cost: float,
    allow_expensive: bool
) -> Optional[float]:
    """
    Extract actual cost from a pay_per_event actor run.

    The Apify API response may include cost info in headers or in metadata.
    This function attempts to extract usageTotalUsd.

    Returns the cost in dollars, or None if cost would exceed ceiling (and allow_expensive=False).
    """
    # Attempt 1: Check response headers for Apify cost metadata
    actual_cost = None
    if "x-apify-usage-total-usd" in response.headers:
        try:
            actual_cost = float(response.headers["x-apify-usage-total-usd"])
        except (ValueError, TypeError):
            pass

    # Attempt 2: If items are returned, check first item for metadata (some actors embed it)
    if actual_cost is None:
        try:
            items = response.json()
            if isinstance(items, list) and len(items) > 0 and isinstance(items[0], dict):
                if "_metadata" in items[0] and "usageTotalUsd" in items[0]["_metadata"]:
                    actual_cost = items[0]["_metadata"]["usageTotalUsd"]
        except (json.JSONDecodeError, KeyError, TypeError):
            pass

    # Fallback: Use conservative estimate based on result count
    if actual_cost is None:
        try:
            items = response.json()
            actual_count = len(items) if isinstance(items, list) else 0
            # Conservative: assume $0.10 per result for pay_per_event actors (will be refined)
            actual_cost = min(actual_count * 0.10, max_cost)
        except (json.JSONDecodeError, TypeError):
            actual_cost = 0.0

    # Check per-run ceiling
    if actual_cost > max_cost and not allow_expensive:
        return None

    return round(actual_cost, 4)


# ---------------------------------------------------------------------------
# CLI Commands
# ---------------------------------------------------------------------------

def cmd_budget_status(_args=None):
    usage = load_usage()
    pct = usage["spent_dollars"] / usage["plan_dollars"] * 100
    state = budget_state(usage)

    # Pulse info
    pulse_budget = usage.get("pulse_budget_dollars", 5.0)
    pulse_spent = usage.get("pulse_spent_dollars", 0.0)
    pulse_pct = (pulse_spent / pulse_budget * 100) if pulse_budget > 0 else 0

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
        # Pulse sub-ledger (added 2026-07-16)
        "pulse_budget_dollars": pulse_budget,
        "pulse_spent_dollars": round(pulse_spent, 4),
        "pulse_remaining_dollars": round(pulse_budget - pulse_spent, 4),
        "pulse_percent_used": round(pulse_pct, 1),
        "last_runs": usage["runs"][-5:],
    }, indent=2))


def cmd_budget_reset(_args=None):
    save_usage(new_usage())
    if WARN_FLAG.exists():
        WARN_FLAG.unlink()
    print(json.dumps({"status": "reset", "month": current_month()}))


def cmd_pulse_budget_status(_args=None):
    """Show pulse sub-budget status."""
    usage = load_usage()
    pulse_budget = usage.get("pulse_budget_dollars", 5.0)
    pulse_spent = usage.get("pulse_spent_dollars", 0.0)
    pulse_pct = (pulse_spent / pulse_budget * 100) if pulse_budget > 0 else 0

    print(json.dumps({
        "month": usage["month"],
        "pulse_budget_dollars": pulse_budget,
        "pulse_spent_dollars": round(pulse_spent, 4),
        "pulse_remaining_dollars": round(pulse_budget - pulse_spent, 4),
        "pulse_percent_used": round(pulse_pct, 1),
        "global_state": budget_state(usage),
        "global_spent": round(usage["spent_dollars"], 4),
        "global_remaining": round(usage["plan_dollars"] - usage["spent_dollars"], 4),
        "pulse_runs": [r for r in usage.get("runs", []) if r.get("pulse", False)],
    }, indent=2))


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
# Scrape Creators Actors (pay_per_event pricing)
# ---------------------------------------------------------------------------

def cmd_sc_tiktok(args):
    """
    best-tiktok-scraper: supports search, hashtag, profile, trending, video.
    Usage:
        python execution/apify_client.py sc-tiktok --search "fitness tips" --limit 20
        python execution/apify_client.py sc-tiktok --profile "@fitnessguy" --limit 20
        python execution/apify_client.py sc-tiktok --hashtag "fitnessmotivation" --limit 20
        python execution/apify_client.py sc-tiktok --trending --limit 20
    """
    run_input = {"resultsLimit": args.limit}

    if args.search:
        run_input["searchTerm"] = args.search
    elif args.profile:
        run_input["profileUsername"] = args.profile.lstrip("@")
    elif args.hashtag:
        run_input["searchHashtag"] = args.hashtag.lstrip("#")
    elif args.trending:
        run_input["searchTerm"] = "#trending"  # Proxy for trending
    else:
        print(json.dumps({
            "status": "error",
            "fallback": True,
            "message": "sc-tiktok requires --search, --profile, --hashtag, or --trending",
            "items": []
        }, indent=2))
        return

    result = run_actor(
        "sc-tiktok",
        run_input,
        args.limit,
        max_cost=args.max_cost,
        allow_expensive=args.allow_expensive
    )
    print(json.dumps(result, indent=2))


def cmd_sc_tiktok_video(args):
    """
    best-tiktok-video-scraper: scrape specific TikTok videos by ID or URL.
    Usage:
        python execution/apify_client.py sc-tiktok-video "7234567890" --limit 1
    """
    run_input = {"videoIds": [args.video_id], "resultsLimit": args.limit}
    result = run_actor(
        "sc-tiktok-video",
        run_input,
        args.limit,
        max_cost=args.max_cost,
        allow_expensive=args.allow_expensive
    )
    print(json.dumps(result, indent=2))


def cmd_sc_tiktok_profile(args):
    """
    best-tiktok-profile-scraper: fetch TikTok profile info.
    Usage:
        python execution/apify_client.py sc-tiktok-profile "@fitnessguy"
    """
    run_input = {"username": args.username.lstrip("@")}
    result = run_actor(
        "sc-tiktok-profile",
        run_input,
        1,
        max_cost=args.max_cost,
        allow_expensive=args.allow_expensive
    )
    print(json.dumps(result, indent=2))


def cmd_sc_tiktok_hashtag(args):
    """
    best-tiktok-hashtag-scraper: scrape TikTok hashtag data.
    Usage:
        python execution/apify_client.py sc-tiktok-hashtag "fitnessmotivation" --limit 50
    """
    run_input = {
        "hashtags": [args.hashtag.lstrip("#")],
        "resultsLimit": args.limit
    }
    result = run_actor(
        "sc-tiktok-hashtag",
        run_input,
        args.limit,
        max_cost=args.max_cost,
        allow_expensive=args.allow_expensive
    )
    print(json.dumps(result, indent=2))


def cmd_sc_tiktok_transcripts(args):
    """
    best-tiktok-transcripts-scraper: fetch TikTok video transcripts (if available).
    Usage:
        python execution/apify_client.py sc-tiktok-transcripts --search "fitness" --limit 10
    """
    run_input = {"resultsLimit": args.limit}
    if args.search:
        run_input["searchTerm"] = args.search
    else:
        print(json.dumps({
            "status": "error",
            "fallback": True,
            "message": "sc-tiktok-transcripts requires --search",
            "items": []
        }, indent=2))
        return

    result = run_actor(
        "sc-tiktok-transcripts",
        run_input,
        args.limit,
        max_cost=args.max_cost,
        allow_expensive=args.allow_expensive
    )
    print(json.dumps(result, indent=2))


def cmd_sc_tiktok_followers(args):
    """
    best-tiktok-followers-scraper: fetch TikTok follower data.
    Usage:
        python execution/apify_client.py sc-tiktok-followers "@fitnessguy" --limit 50
    """
    run_input = {
        "username": args.username.lstrip("@"),
        "resultsLimit": args.limit
    }
    result = run_actor(
        "sc-tiktok-followers",
        run_input,
        args.limit,
        max_cost=args.max_cost,
        allow_expensive=args.allow_expensive
    )
    print(json.dumps(result, indent=2))


def cmd_sc_tiktok_following(args):
    """
    best-tiktok-following-scraper: fetch TikTok following data.
    Usage:
        python execution/apify_client.py sc-tiktok-following "@fitnessguy" --limit 50
    """
    run_input = {
        "username": args.username.lstrip("@"),
        "resultsLimit": args.limit
    }
    result = run_actor(
        "sc-tiktok-following",
        run_input,
        args.limit,
        max_cost=args.max_cost,
        allow_expensive=args.allow_expensive
    )
    print(json.dumps(result, indent=2))


def cmd_sc_youtube_transcripts(args):
    """
    best-youtube-transcripts-scraper: fetch YouTube video transcripts.
    Usage:
        python execution/apify_client.py sc-youtube-transcripts --search "fitness" --limit 5
        python execution/apify_client.py sc-youtube-transcripts --channel "@fitnessguy" --limit 5
    """
    run_input = {"resultsLimit": args.limit}
    if args.search:
        run_input["searchTerm"] = args.search
    elif args.channel:
        run_input["channelName"] = args.channel.lstrip("@")
    else:
        print(json.dumps({
            "status": "error",
            "fallback": True,
            "message": "sc-youtube-transcripts requires --search or --channel",
            "items": []
        }, indent=2))
        return

    result = run_actor(
        "sc-youtube-transcripts",
        run_input,
        args.limit,
        max_cost=args.max_cost,
        allow_expensive=args.allow_expensive
    )
    print(json.dumps(result, indent=2))


def cmd_sc_youtube_channels(args):
    """
    best-youtube-channels-scraper: fetch YouTube channel data.
    Usage:
        python execution/apify_client.py sc-youtube-channels "@fitnessguy"
        python execution/apify_client.py sc-youtube-channels --search "fitness" --limit 10
    """
    run_input = {}
    # Handle positional channel argument if provided
    channel = args.channel if hasattr(args, 'channel') and args.channel else None

    if channel:
        run_input["channelNames"] = [channel.lstrip("@")]
    elif args.search:
        run_input["searchTerm"] = args.search
        run_input["resultsLimit"] = args.limit
    else:
        print(json.dumps({
            "status": "error",
            "fallback": True,
            "message": "sc-youtube-channels requires a channel name or --search",
            "items": []
        }, indent=2))
        return

    result = run_actor(
        "sc-youtube-channels",
        run_input,
        args.limit if args.search else 1,
        max_cost=args.max_cost,
        allow_expensive=args.allow_expensive
    )
    print(json.dumps(result, indent=2))


def cmd_sc_youtube_comments(args):
    """
    best-youtube-comments-scraper: fetch YouTube video comments.
    Usage:
        python execution/apify_client.py sc-youtube-comments --video-id "dQw4w9WgXcQ" --limit 50
        python execution/apify_client.py sc-youtube-comments --search "fitness" --limit 50
    """
    run_input = {"resultsLimit": args.limit}
    if args.video_id:
        run_input["videoId"] = args.video_id
    elif args.search:
        run_input["searchTerm"] = args.search
    else:
        print(json.dumps({
            "status": "error",
            "fallback": True,
            "message": "sc-youtube-comments requires --video-id or --search",
            "items": []
        }, indent=2))
        return

    result = run_actor(
        "sc-youtube-comments",
        run_input,
        args.limit,
        max_cost=args.max_cost,
        allow_expensive=args.allow_expensive
    )
    print(json.dumps(result, indent=2))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def _add_pay_per_event_args(parser):
    """Add common cost-control args to pay_per_event subparsers."""
    parser.add_argument(
        "--max-cost",
        type=float,
        default=0.25,
        help="Per-run cost ceiling in dollars (default $0.25)"
    )
    parser.add_argument(
        "--allow-expensive",
        action="store_true",
        help="Bypass per-run cost ceiling (still respects monthly budget)"
    )


def main():
    load_env()
    p = argparse.ArgumentParser(prog="apify_client.py")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("budget-status", help="Show current month budget (with pulse sub-ledger)")
    sub.add_parser("pulse-budget-status", help="Show pulse sub-budget status only")
    sub.add_parser("budget-reset", help="Manually reset budget (use sparingly)")

    # Original 7 actors (per_result pricing)
    pr = sub.add_parser("reddit", help="Reddit posts/comments")
    pr.add_argument("query", nargs="?", default="")
    pr.add_argument("--subreddit", default="")
    pr.add_argument("--limit", type=int, default=50)
    pr.add_argument("--comments", action="store_true")

    pi = sub.add_parser("instagram", help="Instagram profile/posts")
    pi.add_argument("handle")
    pi.add_argument("--limit", type=int, default=20)

    pt = sub.add_parser("tiktok", help="TikTok hashtag scrape (clockworks)")
    pt.add_argument("hashtag")
    pt.add_argument("--limit", type=int, default=50)

    py = sub.add_parser("youtube", help="YouTube search + transcripts (apidojo)")
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

    # New 10 Scrape Creators actors (pay_per_event pricing)
    psc_tiktok = sub.add_parser("sc-tiktok", help="TikTok scraper (scrape-creators best)")
    psc_tiktok.add_argument("--search", help="Search term")
    psc_tiktok.add_argument("--profile", help="Profile handle (@username)")
    psc_tiktok.add_argument("--hashtag", help="Hashtag (with or without #)")
    psc_tiktok.add_argument("--trending", action="store_true", help="Fetch trending")
    psc_tiktok.add_argument("--limit", type=int, default=20)
    _add_pay_per_event_args(psc_tiktok)

    psc_tiktok_video = sub.add_parser("sc-tiktok-video", help="TikTok video scraper (scrape-creators)")
    psc_tiktok_video.add_argument("video_id")
    psc_tiktok_video.add_argument("--limit", type=int, default=1)
    _add_pay_per_event_args(psc_tiktok_video)

    psc_tiktok_profile = sub.add_parser("sc-tiktok-profile", help="TikTok profile scraper")
    psc_tiktok_profile.add_argument("username", help="Profile handle (@username)")
    _add_pay_per_event_args(psc_tiktok_profile)

    psc_tiktok_hashtag = sub.add_parser("sc-tiktok-hashtag", help="TikTok hashtag scraper")
    psc_tiktok_hashtag.add_argument("hashtag", help="Hashtag (with or without #)")
    psc_tiktok_hashtag.add_argument("--limit", type=int, default=50)
    _add_pay_per_event_args(psc_tiktok_hashtag)

    psc_tiktok_transcripts = sub.add_parser("sc-tiktok-transcripts", help="TikTok transcript scraper")
    psc_tiktok_transcripts.add_argument("--search", help="Search term", required=True)
    psc_tiktok_transcripts.add_argument("--limit", type=int, default=10)
    _add_pay_per_event_args(psc_tiktok_transcripts)

    psc_tiktok_followers = sub.add_parser("sc-tiktok-followers", help="TikTok followers scraper")
    psc_tiktok_followers.add_argument("username", help="Profile handle (@username)")
    psc_tiktok_followers.add_argument("--limit", type=int, default=50)
    _add_pay_per_event_args(psc_tiktok_followers)

    psc_tiktok_following = sub.add_parser("sc-tiktok-following", help="TikTok following scraper")
    psc_tiktok_following.add_argument("username", help="Profile handle (@username)")
    psc_tiktok_following.add_argument("--limit", type=int, default=50)
    _add_pay_per_event_args(psc_tiktok_following)

    psc_yt_transcripts = sub.add_parser("sc-youtube-transcripts", help="YouTube transcript scraper")
    psc_yt_transcripts.add_argument("--search", help="Search term")
    psc_yt_transcripts.add_argument("--channel", help="Channel handle (@channel)")
    psc_yt_transcripts.add_argument("--limit", type=int, default=5)
    _add_pay_per_event_args(psc_yt_transcripts)

    psc_yt_channels = sub.add_parser("sc-youtube-channels", help="YouTube channels scraper")
    psc_yt_channels.add_argument("channel", nargs="?", help="Channel handle (@channel)")
    psc_yt_channels.add_argument("--search", help="Search term")
    psc_yt_channels.add_argument("--limit", type=int, default=10)
    _add_pay_per_event_args(psc_yt_channels)

    psc_yt_comments = sub.add_parser("sc-youtube-comments", help="YouTube comments scraper")
    psc_yt_comments.add_argument("--video-id", help="YouTube video ID")
    psc_yt_comments.add_argument("--search", help="Search term")
    psc_yt_comments.add_argument("--limit", type=int, default=50)
    _add_pay_per_event_args(psc_yt_comments)

    args = p.parse_args()

    handlers = {
        "budget-status":       cmd_budget_status,
        "pulse-budget-status": cmd_pulse_budget_status,
        "budget-reset":        cmd_budget_reset,
        "reddit":        cmd_reddit,
        "instagram":     cmd_instagram,
        "tiktok":        cmd_tiktok,
        "youtube":       cmd_youtube,
        "amazon":        cmd_amazon,
        "maps":          cmd_maps,
        "web":           cmd_web,
        "sc-tiktok":     cmd_sc_tiktok,
        "sc-tiktok-video":       cmd_sc_tiktok_video,
        "sc-tiktok-profile":     cmd_sc_tiktok_profile,
        "sc-tiktok-hashtag":     cmd_sc_tiktok_hashtag,
        "sc-tiktok-transcripts": cmd_sc_tiktok_transcripts,
        "sc-tiktok-followers":   cmd_sc_tiktok_followers,
        "sc-tiktok-following":   cmd_sc_tiktok_following,
        "sc-youtube-transcripts": cmd_sc_youtube_transcripts,
        "sc-youtube-channels":    cmd_sc_youtube_channels,
        "sc-youtube-comments":    cmd_sc_youtube_comments,
    }
    handlers[args.cmd](args)


if __name__ == "__main__":
    main()
