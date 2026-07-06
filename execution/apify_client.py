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
    python execution/apify_client.py verify                 # config check ($0)
    python execution/apify_client.py verify --live          # smoke-test new actors
    python execution/apify_client.py mcp-tools              # print MCP --tools list
    python execution/apify_client.py reddit "first time home buyer" --limit 50 --comments
    python execution/apify_client.py reddit --subreddit FirstTimeHomeBuyer --limit 30
    python execution/apify_client.py instagram realestatewithjing --limit 20
    python execution/apify_client.py tiktok firsttimebuyer --limit 50
    python execution/apify_client.py youtube "pilates day in life" --limit 5 --transcript
    python execution/apify_client.py amazon "yoga mat" --limit 30
    python execution/apify_client.py maps "coffee shop" --location "Los Angeles" --limit 30
    python execution/apify_client.py web "https://example.com"
    # --- social listening ---
    python execution/apify_client.py linkedin "AI ghostwriting" --limit 30
    python execution/apify_client.py linkedin-profile lara-acosta --limit 20
    python execution/apify_client.py twitter --query "personal branding" --limit 50
    python execution/apify_client.py twitter --handle naval --limit 30
    python execution/apify_client.py threads zuck --limit 25
    python execution/apify_client.py facebook "https://www.facebook.com/nike" --limit 25
    # --- generic passthrough for any wired actor (raw Apify input JSON) ---
    python execution/apify_client.py run twitter --input '{"searchTerms":["ai"],"maxItems":10}'

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

# Curated actor whitelist — SINGLE SOURCE OF TRUTH.
# `execution/apify_setup.sh` reads this list (via `apify_client.py mcp-tools`)
# to register the MCP server, so this dict and the MCP --tools flag can never
# drift. cost_per_result is a conservative estimate based on Apify Store
# pricing; the tracker logs actual cost after each run.
#
# "verified": True  = input schema confirmed by a live run.
# "verified": False = added 2026-07 (social-listening expansion). The MCP path
#     auto-loads each actor's real schema, so tools work regardless; the CLI
#     convenience input below is best-known and confirmed via `verify --live`.
ACTORS = {
    # --- core (verified live 2026-04) ---
    "reddit":    {"id": "trudax/reddit-scraper-lite",     "cost_per_result": 0.001,  "verified": True},
    "instagram": {"id": "apify/instagram-scraper",        "cost_per_result": 0.0005, "verified": True},
    "tiktok":    {"id": "clockworks/free-tiktok-scraper", "cost_per_result": 0.004,  "verified": True},
    "youtube":   {"id": "apidojo/youtube-scraper",        "cost_per_result": 0.005,  "verified": True},
    "amazon":    {"id": "junglee/amazon-scraper",         "cost_per_result": 0.0015, "verified": True},
    "maps":      {"id": "compass/crawler-google-places",  "cost_per_result": 0.007,  "verified": True},
    "web":       {"id": "apify/rag-web-browser",          "cost_per_result": 0.003,  "verified": True},
    # --- social-listening expansion (2026-07, pending first-run verification) ---
    "linkedin":         {"id": "harvestapi/linkedin-post-search",     "cost_per_result": 0.008,  "verified": False},
    "linkedin_profile": {"id": "harvestapi/linkedin-profile-scraper", "cost_per_result": 0.010,  "verified": False},
    "twitter":          {"id": "apidojo/tweet-scraper",               "cost_per_result": 0.0004, "verified": False},
    "threads":          {"id": "curious_coder/threads-scraper",       "cost_per_result": 0.003,  "verified": False},
    "facebook":         {"id": "apify/facebook-posts-scraper",        "cost_per_result": 0.003,  "verified": False},
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
# Social listening actors (added 2026-07 — verify input schema via `verify --live`)
# ---------------------------------------------------------------------------

def cmd_linkedin(args):
    """
    harvestapi/linkedin-post-search — search LinkedIn posts by keyword.
    No LinkedIn cookies required (HarvestAPI proxies). Best-known input below;
    if Apify returns 400, adjust and re-run `verify --live`. Via MCP the real
    schema is auto-loaded, so the tool works even if this convenience input drifts.
    """
    run_input = {"query": args.query, "maxItems": args.limit}
    print(json.dumps(run_actor("linkedin", run_input, args.limit), indent=2))


def cmd_linkedin_profile(args):
    """harvestapi/linkedin-profile-scraper — profile detail by handle or full URL."""
    handle = args.handle.lstrip("@")
    url = handle if handle.startswith("http") else f"https://www.linkedin.com/in/{handle}/"
    run_input = {"profiles": [url], "maxItems": args.limit}
    print(json.dumps(run_actor("linkedin_profile", run_input, args.limit), indent=2))


def cmd_twitter(args):
    """apidojo/tweet-scraper (X) — search by term OR pull a handle's timeline."""
    if not args.query and not args.handle:
        print(json.dumps({"status": "error", "fallback": True,
                          "message": "twitter needs --query or --handle.",
                          "items": []}, indent=2))
        return
    run_input = {"maxItems": args.limit, "sort": args.sort}
    if args.query:
        run_input["searchTerms"] = [args.query]
    if args.handle:
        run_input["twitterHandles"] = [args.handle.lstrip("@")]
    print(json.dumps(run_actor("twitter", run_input, args.limit), indent=2))


def cmd_threads(args):
    """curious_coder/threads-scraper — a Threads profile's recent posts."""
    handle = args.handle.lstrip("@")
    run_input = {
        "startUrls": [{"url": f"https://www.threads.net/@{handle}"}],
        "resultsLimit": args.limit,
    }
    print(json.dumps(run_actor("threads", run_input, args.limit), indent=2))


def cmd_facebook(args):
    """apify/facebook-posts-scraper — recent posts from a public page URL."""
    run_input = {"startUrls": [{"url": args.url}], "resultsLimit": args.limit}
    print(json.dumps(run_actor("facebook", run_input, args.limit), indent=2))


def cmd_run(args):
    """Generic passthrough: run any wired actor with raw Apify input JSON.

    Future-proofs new actors and lets an agent match the exact Apify schema
    when a convenience command doesn't cover a field.
    """
    try:
        run_input = json.loads(args.input)
    except json.JSONDecodeError as e:
        print(json.dumps({"status": "error", "fallback": True,
                          "message": f"--input is not valid JSON: {e}",
                          "items": []}, indent=2))
        return
    # Estimate a result cap for budget math from common limit fields.
    max_results = (run_input.get("maxItems") or run_input.get("resultsLimit")
                   or run_input.get("maxResults") or run_input.get("limit")
                   or args.limit)
    print(json.dumps(run_actor(args.actor, run_input, int(max_results)), indent=2))


# ---------------------------------------------------------------------------
# Introspection / verification (no or minimal API cost)
# ---------------------------------------------------------------------------

def cmd_mcp_tools(_args=None):
    """Print the comma-joined actor IDs for `claude mcp add ... --tools`.

    Single source of truth consumed by execution/apify_setup.sh.
    """
    print(",".join(a["id"] for a in ACTORS.values()))


def cmd_verify(args):
    """Config check ($0), plus optional live smoke-test of actors.

    `verify`         — token present? actors listed? MCP registered? budget state?
    `verify --live`  — run each UNVERIFIED actor with 1 result and report pass/fail.
    `verify --live --all` — smoke-test every actor (costs a few cents).
    """
    token = os.environ.get("APIFY_TOKEN", "")
    mcp_path = BASE / ".mcp.json"
    mcp_registered = False
    if mcp_path.exists():
        try:
            mcp_registered = "apify" in json.loads(mcp_path.read_text()).get("mcpServers", {})
        except (json.JSONDecodeError, AttributeError):
            mcp_registered = False
    usage = load_usage()

    report = {
        "token_present": bool(token),
        "actor_count": len(ACTORS),
        "actors": {k: {"id": v["id"], "verified": v["verified"]} for k, v in ACTORS.items()},
        "mcp_json_exists": mcp_path.exists(),
        "mcp_apify_registered": mcp_registered,
        "budget_state": budget_state(usage),
        "spent_dollars": round(usage["spent_dollars"], 4),
        "remaining_dollars": round(usage["plan_dollars"] - usage["spent_dollars"], 4),
        "next_steps": [],
    }
    if not token:
        report["next_steps"].append("Add APIFY_TOKEN to .env (get it at console.apify.com/account/integrations).")
    if not mcp_registered:
        report["next_steps"].append("Register MCP tools: bash execution/apify_setup.sh (then restart the session).")

    if args.live:
        if not token:
            report["live_test"] = "skipped — APIFY_TOKEN not set"
        else:
            targets = list(ACTORS) if args.all else [k for k, v in ACTORS.items() if not v["verified"]]
            probes = {
                "linkedin":         ("linkedin", {"query": "ai", "maxItems": 1}),
                "linkedin_profile": ("linkedin_profile", {"profiles": ["https://www.linkedin.com/in/williamhgates/"], "maxItems": 1}),
                "twitter":          ("twitter", {"searchTerms": ["ai"], "maxItems": 1, "sort": "Latest"}),
                "threads":          ("threads", {"startUrls": [{"url": "https://www.threads.net/@zuck"}], "resultsLimit": 1}),
                "facebook":         ("facebook", {"startUrls": [{"url": "https://www.facebook.com/nike"}], "resultsLimit": 1}),
                "reddit":           ("reddit", {"startUrls": [{"url": "https://www.reddit.com/r/test/"}], "maxItems": 1, "skipComments": True}),
                "instagram":        ("instagram", {"directUrls": ["https://www.instagram.com/instagram/"], "resultsType": "posts", "resultsLimit": 1}),
                "tiktok":           ("tiktok", {"hashtags": ["fyp"], "resultsPerPage": 1}),
                "youtube":          ("youtube", {"keywords": ["test"], "maxItems": 1}),
                "amazon":           ("amazon", {"categoryOrProductUrls": [{"url": "https://www.amazon.com/s?k=pen"}], "maxItemsPerStartUrl": 1}),
                "maps":             ("maps", {"searchStringsArray": ["cafe"], "locationQuery": "Los Angeles", "maxCrawledPlacesPerSearch": 1}),
                "web":              ("web", {"query": "https://example.com", "maxResults": 1}),
            }
            results = {}
            for key in targets:
                if key not in probes:
                    results[key] = {"status": "no-probe"}
                    continue
                actor_key, run_input = probes[key]
                resp = run_actor(actor_key, run_input, 1)
                results[key] = {
                    "status": resp.get("status"),
                    "result_count": resp.get("result_count", 0),
                    "message": resp.get("message", ""),
                }
            report["live_test"] = results
            report["next_steps"].append(
                "For any 'ok' actor above, flip \"verified\": True in the ACTORS dict.")

    print(json.dumps(report, indent=2))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    load_env()
    p = argparse.ArgumentParser(prog="apify_client.py")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("budget-status", help="Show current month budget")
    sub.add_parser("budget-reset", help="Manually reset budget (use sparingly)")
    sub.add_parser("mcp-tools", help="Print comma-joined actor IDs for MCP --tools")

    pv = sub.add_parser("verify", help="Config check ($0); --live smoke-tests actors")
    pv.add_argument("--live", action="store_true", help="Actually call actors (small cost)")
    pv.add_argument("--all", action="store_true", help="With --live: test every actor, not just unverified")

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

    pl = sub.add_parser("linkedin", help="LinkedIn post search by keyword")
    pl.add_argument("query")
    pl.add_argument("--limit", type=int, default=30)

    plp = sub.add_parser("linkedin-profile", help="LinkedIn profile detail")
    plp.add_argument("handle", help="handle (e.g. lara-acosta) or full profile URL")
    plp.add_argument("--limit", type=int, default=20)

    px = sub.add_parser("twitter", help="X/Twitter search or handle timeline")
    px.add_argument("--query", default="")
    px.add_argument("--handle", default="")
    px.add_argument("--limit", type=int, default=50)
    px.add_argument("--sort", default="Latest", choices=["Latest", "Top"])

    pth = sub.add_parser("threads", help="Threads profile recent posts")
    pth.add_argument("handle")
    pth.add_argument("--limit", type=int, default=25)

    pf = sub.add_parser("facebook", help="Facebook public page posts")
    pf.add_argument("url", help="full page URL, e.g. https://www.facebook.com/nike")
    pf.add_argument("--limit", type=int, default=25)

    prun = sub.add_parser("run", help="Run any wired actor with raw Apify input JSON")
    prun.add_argument("actor", choices=list(ACTORS.keys()))
    prun.add_argument("--input", required=True, help="Apify run input as a JSON string")
    prun.add_argument("--limit", type=int, default=25, help="Budget cap if input has no limit field")

    args = p.parse_args()

    handlers = {
        "budget-status":    cmd_budget_status,
        "budget-reset":     cmd_budget_reset,
        "mcp-tools":        cmd_mcp_tools,
        "verify":           cmd_verify,
        "reddit":           cmd_reddit,
        "instagram":        cmd_instagram,
        "tiktok":           cmd_tiktok,
        "youtube":          cmd_youtube,
        "amazon":           cmd_amazon,
        "maps":             cmd_maps,
        "web":              cmd_web,
        "linkedin":         cmd_linkedin,
        "linkedin-profile": cmd_linkedin_profile,
        "twitter":          cmd_twitter,
        "threads":          cmd_threads,
        "facebook":         cmd_facebook,
        "run":              cmd_run,
    }
    handlers[args.cmd](args)


if __name__ == "__main__":
    main()
