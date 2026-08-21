#!/usr/bin/env python3
"""
Surface Router — queryable web-surface routing registry.

The machine copy of `directives/browser-automation-routing.md`. Ask it which
tool chain actually works on a given surface, in what order, at what cost, and
which wall you will hit if you reach for the light tool first.

Prose canon stays in the directive; this file is the queryable copy. Update
both together.

Apify hops resolve actor id + pricing live from `execution/apify_client.py`
ACTORS — actor IDs are NEVER duplicated here.

Usage:
    python3 execution/surface_router.py route "reddit thread comments"
    python3 execution/surface_router.py route "https://www.amazon.com/dp/B00XYZ"
    python3 execution/surface_router.py list
    python3 execution/surface_router.py inventory
"""

import argparse
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
APIFY_USAGE = BASE / ".agent" / "apify-usage.json"

# ─────────────────────────────────────────────────────────
# SURFACE REGISTRY
# Each hop: tool · how · cost · notes (+ optional actor key resolved live)
# ─────────────────────────────────────────────────────────

SURFACES = {
    "reddit-thread": {
        "name": "Reddit thread / comments",
        "keywords": ["reddit", "subreddit", "thread", "comments", "r/", "comment tree", "sentiment mining"],
        "domains": ["reddit.com", "old.reddit.com", "redd.it"],
        "tool_chain": [
            {"tool": "Playwright", "how": "browser_navigate to the thread URL, then browser_evaluate an in-page "
                                         "fetch('<thread>/.json?limit=500') and walk the comment tree "
                                         "(data.children[].data.body, recurse .replies)",
             "cost": "$0", "notes": "VERIFIED LIVE 2026-08-21. Same-origin fetch carries the browser's own headers, "
                                    "so the JSON endpoint answers where a bare HTTP client is 403'd."},
            {"tool": "Apify", "actor": "reddit", "how": "apify_client.py reddit --search/--urls for scaled multi-thread mining",
             "cost": "per_result (see live ACTORS row)", "notes": "Use when 50+ threads or structured bulk is needed, not for one thread."},
        ],
        "known_failure": "WebFetch and the Claude-browser MCP are BLOCKED on reddit.com (bot wall / 403). "
                         "Raw HTTP to the .json endpoint is blocked too — it only works from inside a real browser context.",
        "escalation": "One failed hop max: do not retry WebFetch. Go straight to Playwright + in-page fetch.",
        "solution_card": "docs/solutions/2026-08-21-reddit-json-via-playwright-in-page-fetch.md",
    },
    "x-twitter-post": {
        "name": "X / Twitter public post",
        "keywords": ["x.com", "twitter", "tweet", "status", "x post", "thread on x"],
        "domains": ["x.com", "twitter.com", "t.co"],
        "tool_chain": [
            {"tool": "WebSearch", "how": "surface direct status URLs; snippets often preview the opening text",
             "cost": "$0", "notes": "Cheapest way to find which posts are long-form text vs video."},
            {"tool": "Playwright", "how": "browser_navigate the STATUS URL (never the profile), then snapshot — "
                                          "full tweet text lands in the accessibility tree",
             "cost": "$0", "notes": "Single public status pages render logged-out; the profile timeline does not."},
            {"tool": "Apify", "actor": "twitter", "how": "apify_client.py twitter --search for timeline/search at scale",
             "cost": "per_result (see live ACTORS row)",
             "notes": "Vendor pads empty results with 'mock data' notice items — filter any item mentioning "
                      "KaitoEasyAPI / mock data before synthesis."},
        ],
        "known_failure": "WebFetch on any x.com URL returns HTTP 402, always. Playwright on the PROFILE page returns a "
                         "login-gated skeleton with an infinite spinner.",
        "escalation": "402 or spinner → Playwright on individual status URLs; scale need → Apify twitter actor.",
        "solution_card": "docs/solutions/2026-07-21-x-corpus-via-playwright-public-snapshot.md",
    },
    "linkedin-post": {
        "name": "LinkedIn post / profile content",
        "keywords": ["linkedin", "linkedin post", "authwall", "activity-", "engagers", "reactions", "post comments"],
        "domains": ["linkedin.com", "lnkd.in"],
        "tool_chain": [
            {"tool": "WebSearch + WebFetch", "how": "site:linkedin.com/posts/<handle> to harvest permalinks, then WebFetch "
                                                    "each candidate with an explicit 'if authwall, say AUTHWALL' prompt",
             "cost": "$0", "notes": "~50% of post permalinks render full body logged-out. Fetch-test every one — which "
                                    "permalinks render is NOT predictable. Feed and profile pages stay gated."},
            {"tool": "Apify", "actor": "linkedin-posts", "how": "apify_client.py linkedin-posts --username <handle> --limit N",
             "cost": "pay_per_event, ~$2.00/1k posts observed 2026-08-05 (100 posts → $0.20)",
             "notes": "Real schema is username + limit (1-100/page); unknown fields are silently ignored and still bill a full page."},
            {"tool": "Apify", "actor": "linkedin-post-reactions", "how": "engager roster for a post URL",
             "cost": "pay_per_event, $0.25 ceiling", "notes": "LISTENING-ONLY. Sends stay human (Farrice, 2026-08-06)."},
            {"tool": "Apify", "actor": "linkedin-post-comments", "how": "comment text + authors (ICP verbatim)",
             "cost": "pay_per_event, $0.25 ceiling", "notes": "Full scout run observed 2026-08-06 at $0.50 total."},
        ],
        "known_failure": "Authwall on feed, profile, and ~50% of post permalinks. Logged-out Playwright usually hits the "
                         "same authwall, so it is not a reliable escalation.",
        "escalation": "AUTHWALL on a permalink → try the next permalink (not the same one), then Apify actors for structured pulls.",
        "solution_card": "docs/solutions/2026-07-21-linkedin-authwall-corpus-via-public-post-permalinks.md",
    },
    "instagram": {
        "name": "Instagram post / reel (captions, frames)",
        "keywords": ["instagram", "ig", "reel", "reels", "caption", "og:description"],
        "domains": ["instagram.com", "instagr.am"],
        "tool_chain": [
            {"tool": "Playwright", "how": "navigate the profile, then one browser_evaluate loop doing same-origin "
                                          "fetch() of each post URL and regexing <meta name=\"description\"> for the full caption",
             "cost": "$0", "notes": "20 captions in one tool call. HTML-entity-encoded — decode before quoting."},
            {"tool": "Playwright", "how": "canvas seek-capture for frames (play muted → pause → seek → drawImage → toDataURL)",
             "cost": "$0", "notes": "Burned-in captions ARE the transcript for short-form. browser_evaluate's filename "
                                    "param must be inside the workspace root (/tmp is rejected)."},
            {"tool": "Apify", "actor": "instagram", "how": "apify_client.py instagram for profiles/posts/hashtags at scale",
             "cost": "per_result (see live ACTORS row)", "notes": "No dedicated IG transcript actor — caption stands in."},
        ],
        "known_failure": "DOWNLOADS BLOCKED: yt-dlp anonymous returns 'Instagram sent an empty media response'; "
                         "--cookies-from-browser chrome HANGS indefinitely while Chrome is open (not transient — do not retry).",
        "escalation": "Never chase the download. Captions via og:description first, frames via canvas second. "
                      "Private accounts need real auth — declare unavailable rather than guessing.",
        "solution_card": "docs/solutions/2026-07-25-instagram-voice-scrape-without-downloads.md",
    },
    "tiktok": {
        "name": "TikTok video / profile / hashtag",
        "keywords": ["tiktok", "tik tok", "fyp", "hashtag scan", "tiktok transcript"],
        "domains": ["tiktok.com", "vm.tiktok.com"],
        "tool_chain": [
            {"tool": "Apify", "actor": "sc-tiktok", "how": "apify_client.py sc-tiktok --search/--profile/--hashtag",
             "cost": "pay_per_event, $0.25/run ceiling", "notes": "Scrape Creators actors are the registered path for TikTok — "
                                                                  "consistent structured data, no login."},
            {"tool": "Apify", "actor": "sc-tiktok-transcripts", "how": "transcripts where available",
             "cost": "pay_per_event, $0.25/run ceiling", "notes": "Direct voice beats interpreted summary for research."},
            {"tool": "Playwright", "how": "navigate + scroll + evaluate for a handful of public videos",
             "cost": "$0", "notes": "Infinite-scroll feed; fine for a few items, slow past ~20."},
        ],
        "known_failure": "WebFetch returns the JS shell. Bulk scrolling in Playwright is slow and rate-limited.",
        "escalation": "Volume or transcripts → Apify sc-* actors (pre-check budget for >50 posts).",
        "solution_card": None,
    },
    "youtube": {
        "name": "YouTube video (transcript / metadata / comments)",
        "keywords": ["youtube", "yt", "video transcript", "captions", "youtube comments", "channel"],
        "domains": ["youtube.com", "youtu.be"],
        "tool_chain": [
            {"tool": "execution/fetch-transcript.py", "how": "python3 execution/fetch-transcript.py <url> — yt-dlp captions",
             "cost": "$0", "notes": "FREE path first, always. Captions exist for the large majority of videos."},
            {"tool": "execution/fetch-video-context.py", "how": "python3 execution/fetch-video-context.py <url> for full video context "
                                                               "(frames + transcript + metadata)",
             "cost": "$0", "notes": "Watch-the-source standard: transcript-only extraction caps at 5/10."},
            {"tool": "Apify", "actor": "sc-youtube-transcripts", "how": "fallback only when captions are missing",
             "cost": "pay_per_event, ~$0.10/run cap", "notes": "Never the first hop — yt-dlp is free."},
            {"tool": "Apify", "actor": "sc-youtube-comments", "how": "comment mining",
             "cost": "pay_per_event, $0.25 ceiling", "notes": "Comment corpora are ICP-verbatim gold."},
        ],
        "known_failure": "WebFetch on a watch URL returns page chrome, not the transcript. Paying for a transcript that "
                         "yt-dlp would have given free is the recurring waste here.",
        "escalation": "Captions missing → sc-youtube-transcripts. Metadata only → youtube actor (per_result).",
        "solution_card": None,
    },
    "meta-ad-library": {
        "name": "Meta / Facebook Ad Library",
        "keywords": ["ad library", "meta ads", "facebook ads", "ad spy", "competitor ads", "longest running ad"],
        "domains": ["facebook.com/ads/library", "www.facebook.com/ads/library"],
        "tool_chain": [
            {"tool": "Playwright", "how": "read-only navigate + snapshot + evaluate on the Ad Library search URL "
                                          "(execution/ad_spy.py wraps this)",
             "cost": "$0", "notes": "Tier 1, no login, no state change."},
            {"tool": "Apify", "actor": "facebook-ads", "how": "apify_client.py facebook-ads for bulk historical pulls",
             "cost": "pay_per_event, ~$0.75/1k ads", "notes": "Input is urls as [{'url': ...}] request objects; minimum 10 "
                                                              "charged results; needs memory_mb 512."},
        ],
        "known_failure": "NO LONGEVITY SORT EXISTS. The Ad Library exposes no likes/views/spend/ROI for commercial ads, and "
                         "no 'sort by longest running' control. Raw HTTP is 403 bot-blocked — a real browser context is required.",
        "escalation": "Infer longevity from 'Started running on' date + active status, computed client-side. "
                      "Leave Views/Likes/Comments blank — never fabricate performance numbers.",
        "solution_card": "docs/solutions/2026-07-24-replicate-creator-tool-stack-at-zero-cost.md",
    },
    "amazon-reviews": {
        "name": "Amazon product reviews",
        "keywords": ["amazon reviews", "product reviews", "review mining", "verified purchase", "star rating"],
        "domains": ["amazon.com/product-reviews", "amazon.com/dp"],
        "tool_chain": [
            {"tool": "Apify", "actor": "amazon", "how": "apify_client.py amazon — the registered path for products/reviews",
             "cost": "per_result (see live ACTORS row)", "notes": "Pre-check budget for >100 products."},
        ],
        "known_failure": "The full review list is LOGIN-WALLED to plain fetchers: WebFetch and raw HTTP return a sign-in "
                         "interstitial or a captcha. Playwright logged-out sees only the handful of reviews rendered on the PDP.",
        "escalation": "If the amazon actor is not registered or the budget is red, DECLARE THE SURFACE UNAVAILABLE and say so — "
                      "do not paraphrase reviews from memory or from a search snippet.",
        "solution_card": None,
    },
    "amazon-bestsellers": {
        "name": "Amazon bestseller / category lists",
        "keywords": ["bestseller", "best sellers", "amazon category", "top 100", "movers and shakers", "amazon ranking"],
        "domains": ["amazon.com/Best-Sellers", "amazon.com/gp/bestsellers"],
        "tool_chain": [
            {"tool": "Playwright", "how": "navigate the bestseller URL + evaluate the DOM (rank, title, price, ASIN)",
             "cost": "$0", "notes": "VERIFIED: bestseller lists are server-rendered and NOT login-walled — the DOM path works."},
            {"tool": "Apify", "actor": "amazon", "how": "structured bulk across many categories",
             "cost": "per_result (see live ACTORS row)", "notes": "Only when the list count justifies the spend."},
        ],
        "known_failure": "WebFetch often returns a partially-rendered shell; the ranks are there but truncated.",
        "escalation": "Shell or truncation → Playwright DOM read. Do not escalate to Apify for a single list.",
        "solution_card": None,
    },
    "ssr-marketing-site": {
        "name": "SSR marketing site (Webflow / Framer / Next.js) — hero, pricing, public copy",
        "keywords": ["marketing site", "landing page", "pricing page", "homepage", "webflow", "framer", "next.js", "sales page"],
        "domains": [],
        "tool_chain": [
            {"tool": "WebFetch", "how": "fetch the URL directly",
             "cost": "$0", "notes": "MOST modern marketing sites server-render hero and pricing for SEO. "
                                    "Calibration test 2026-04-30 — try this FIRST."},
            {"tool": "Playwright", "how": "navigate + evaluate, only when WebFetch returns near-empty content",
             "cost": "$0 (3-8s latency)", "notes": "Escalate on evidence of emptiness, not on the framework name."},
        ],
        "known_failure": "The recurring error is OVER-escalation: assuming 'JS framework = needs Playwright' and paying "
                         "3-8s of latency for content WebFetch would have returned in under a second.",
        "escalation": "Only escalate when the fetched content is genuinely missing or visibly degraded.",
        "solution_card": None,
    },
    "spa-app-interior": {
        "name": "True client-rendered SPA (dashboard, app interior, no SSR)",
        "keywords": ["spa", "dashboard", "app interior", "client-rendered", "single page app", "web app ui", "analytics dashboard"],
        "domains": [],
        "tool_chain": [
            {"tool": "Playwright", "how": "browser_navigate + browser_evaluate against the rendered DOM; "
                                          "browser_wait_for on the element that signals hydration",
             "cost": "$0", "notes": "Login-gated interiors need a persistent profile per browser-automation-safety.md."},
            {"tool": "Apify", "actor": "web", "how": "apify/rag-web-browser for scaled JS-rendered fetches",
             "cost": "per_result (see live ACTORS row)", "notes": "Only at 50+ URLs."},
        ],
        "known_failure": "WebFetch returns the empty shell HTML — and the model then hallucinates a summary from it. "
                         "This is the single most expensive failure in the whole routing table.",
        "escalation": "Empty shell → Playwright immediately. Never summarize a shell.",
        "solution_card": None,
    },
    "longform-article": {
        "name": "Long-form article / blog post / public PDF",
        "keywords": ["article", "blog post", "read this", "essay", "seo page", "public pdf", "summarize this page"],
        "domains": [],
        "tool_chain": [
            {"tool": "WebFetch", "how": "fetch the URL and read",
             "cost": "$0", "notes": "Fastest and cheapest. Playwright on a static blog post is pure overkill."},
            {"tool": "Perplexity ask", "how": "when the page is gone or paywalled and a cited paraphrase suffices",
             "cost": "metered (perplexity budget)", "notes": "Secondhand — never use it where verbatim quotes are the deliverable."},
        ],
        "known_failure": "Paywalls and cookie interstitials return consent HTML instead of the article body.",
        "escalation": "Consent wall → Playwright (decline non-essential cookies) → Perplexity as last resort.",
        "solution_card": None,
    },
    "generic-search": {
        "name": "Generic web search / fact lookup",
        "keywords": ["search", "find", "look up", "fact check", "who is", "what is", "latest news", "stat"],
        "domains": [],
        "tool_chain": [
            {"tool": "WebSearch", "how": "free search first — always",
             "cost": "$0", "notes": "Free tools before metered ones is the standing order."},
            {"tool": "Perplexity ask / search", "how": "single-claim verification with citations",
             "cost": "metered ($30/mo plan)", "notes": "Fallback, not default."},
            {"tool": "execution/research.py", "how": "receipt-carrying research for anything larger than one claim",
             "cost": "varies", "notes": "NEVER answer research from training memory."},
        ],
        "known_failure": "Spinning up a browser for one fact; or answering from memory and calling it research.",
        "escalation": "WebSearch thin → Perplexity → Gemini Deep Research for true multi-source synthesis.",
        "solution_card": None,
    },
}

NO_ROUTE = {
    "status": "no_route_known",
    "fallback": True,
    "alternative": "write a mining brief naming the surface; check docs/solutions/; consider WebSearch first",
}


# ─────────────────────────────────────────────────────────
# APIFY: live import, never duplicated
# ─────────────────────────────────────────────────────────

def apify_actors():
    """Import ACTORS live from apify_client. Returns (actors_dict, error_msg)."""
    try:
        import sys
        sys.path.insert(0, str(BASE / "execution"))
        from apify_client import ACTORS  # type: ignore
        return dict(ACTORS), None
    except Exception as exc:
        return {}, f"apify_client not importable ({exc.__class__.__name__}: {exc})"


def apify_budget():
    """Read budget state from the ledger. Honest about a missing/unreadable file."""
    if not APIFY_USAGE.exists():
        return {"status": "unknown", "message": f"no ledger at {APIFY_USAGE}"}
    try:
        data = json.loads(APIFY_USAGE.read_text())
    except Exception as exc:
        return {"status": "unknown", "message": f"ledger unreadable ({exc})"}
    plan = float(data.get("plan_dollars", 29.0))
    spent = float(data.get("spent_dollars", 0.0))
    pct = (spent / plan) if plan else 0.0
    warn = float(data.get("soft_warn_pct", 0.70))
    stop = float(data.get("hard_stop_pct", 0.90))
    state = "red" if pct >= stop else ("yellow" if pct >= warn else "green")
    return {"status": state, "spent": round(spent, 4), "plan": plan,
            "percent": round(pct * 100, 1), "month": data.get("month", "?")}


# ─────────────────────────────────────────────────────────
# MATCHING — keyword + stemmer scoring (tool_router.py algorithm)
# ─────────────────────────────────────────────────────────

def _stem(word):
    for suffix in ("ing", "tion", "ness", "ally", "ment", "ive", "ity", "ly", "ed", "er", "es", "s"):
        if len(word) > len(suffix) + 3 and word.endswith(suffix):
            return word[: -len(suffix)]
    return word


def match_surface(query):
    """Score every surface; return (key, score, matched_terms) or (None, 0, [])."""
    q = query.lower().strip()
    words = re.findall(r"[a-z0-9./_-]+", q)
    stems = [_stem(w) for w in words]

    best_key, best_score, best_matched = None, 0, []
    for key, surf in SURFACES.items():
        score, matched = 0, []

        for dom in surf["domains"]:
            if dom in q:
                score += 10 * len(dom.split("."))
                matched.append(dom)

        for kw in surf["keywords"]:
            if kw in q:
                score += len(kw.split()) * 3
                matched.append(kw)
                continue
            kw_stems = [_stem(w) for w in kw.split()]
            overlap = sum(1 for ks in kw_stems
                          if any(ks == s or (len(s) > 3 and (ks in s or s in ks)) for s in stems))
            if overlap >= max(1, len(kw_stems) * 0.6):
                score += overlap
                matched.append(f"{kw}~")

        if key.replace("-", " ") in q:
            score += 5
            matched.append(key)

        if score > best_score:
            best_key, best_score, best_matched = key, score, matched

    # Threshold: 3 keeps a stray one-stem brush from inventing a route.
    if best_score < 3:
        return None, 0, []
    return best_key, best_score, best_matched


# ─────────────────────────────────────────────────────────
# OUTPUT
# ─────────────────────────────────────────────────────────

def build_envelope(query):
    key, score, matched = match_surface(query)
    if key is None:
        env = dict(NO_ROUTE)
        env["query"] = query
        env["message"] = f"No registered surface matches \"{query}\"."
        return env

    surf = SURFACES[key]
    actors, actor_err = apify_actors()

    chain = []
    for i, hop in enumerate(surf["tool_chain"], 1):
        row = {"step": i, "tool": hop["tool"], "how": hop["how"],
               "cost": hop["cost"], "notes": hop["notes"]}
        if "actor" in hop:
            row["actor_key"] = hop["actor"]
            live = actors.get(hop["actor"])
            if live:
                row["actor_id"] = live.get("id")
                row["pricing"] = live.get("pricing")
                if live.get("cost_per_result") is not None:
                    row["cost_per_result"] = live["cost_per_result"]
            else:
                row["actor_id"] = actor_err or f"actor '{hop['actor']}' not in ACTORS"
        chain.append(row)

    return {
        "status": "routed",
        "fallback": False,
        "query": query,
        "surface": key,
        "surface_name": surf["name"],
        "match_score": score,
        "matched_terms": matched[:6],
        "tool_chain": chain,
        "known_failure": surf["known_failure"],
        "escalation": surf["escalation"],
        "solution_card": surf["solution_card"],
        "apify_budget": apify_budget(),
        "apify_import": actor_err or "ok",
    }


def print_envelope(env):
    if env["status"] == "no_route_known":
        print(f"Query: \"{env['query']}\"\n")
        print("  status:      no_route_known")
        print("  fallback:    true")
        print(f"  message:     {env['message']}")
        print(f"  alternative: {env['alternative']}")
        return

    print(f"Query: \"{env['query']}\"")
    print(f"Surface: {env['surface_name']}  [{env['surface']}]  "
          f"(score {env['match_score']}; matched: {', '.join(env['matched_terms'])})\n")

    print("Tool chain (in order):")
    for hop in env["tool_chain"]:
        print(f"  {hop['step']}. {hop['tool']}  —  {hop['cost']}")
        print(f"     how:   {hop['how']}")
        if "actor_key" in hop:
            extra = f" · {hop.get('pricing', '?')}"
            if "cost_per_result" in hop:
                extra += f" · ${hop['cost_per_result']}/result"
            print(f"     actor: {hop['actor_key']} → {hop.get('actor_id')}{extra}")
        print(f"     note:  {hop['notes']}")
    print()

    print(f"KNOWN FAILURE: {env['known_failure']}")
    print(f"ESCALATION:    {env['escalation']}")
    print(f"SOLUTION CARD: {env['solution_card'] or '(none on disk)'}")

    b = env["apify_budget"]
    if b["status"] in ("green", "yellow", "red"):
        print(f"APIFY BUDGET:  {b['status'].upper()} — ${b['spent']:.2f} / ${b['plan']:.2f} "
              f"({b['percent']}%) for {b['month']}")
    else:
        print(f"APIFY BUDGET:  unknown — {b['message']}")
    if env["apify_import"] != "ok":
        print(f"APIFY IMPORT:  {env['apify_import']}")


def cmd_list():
    print(f"{'key':22s} {'hops':5s} surface")
    print("-" * 78)
    for key, surf in SURFACES.items():
        card = " ·card" if surf["solution_card"] else ""
        print(f"{key:22s} {len(surf['tool_chain']):>3d}   {surf['name']}{card}")
    print(f"\n{len(SURFACES)} surfaces registered. "
          "Prose canon: directives/browser-automation-routing.md")


def cmd_inventory():
    actors, actor_err = apify_actors()
    for key, surf in SURFACES.items():
        print(f"\n=== {key} — {surf['name']}")
        print(f"  keywords: {', '.join(surf['keywords'])}")
        print(f"  domains:  {', '.join(surf['domains']) or '(no domain anchor — matched by keyword)'}")
        for i, hop in enumerate(surf["tool_chain"], 1):
            line = f"  {i}. {hop['tool']} [{hop['cost']}]"
            if "actor" in hop:
                live = actors.get(hop["actor"])
                line += f" actor={hop['actor']}→{live.get('id') if live else (actor_err or 'UNREGISTERED')}"
            print(line)
            print(f"     {hop['how']}")
            print(f"     {hop['notes']}")
        print(f"  known_failure: {surf['known_failure']}")
        print(f"  escalation:    {surf['escalation']}")
        print(f"  solution_card: {surf['solution_card'] or '-'}")
    b = apify_budget()
    print(f"\napify budget: {b}")
    if actor_err:
        print(f"apify import: {actor_err}")


def main():
    parser = argparse.ArgumentParser(description="Surface Router — web-surface routing registry")
    sub = parser.add_subparsers(dest="command")

    route_p = sub.add_parser("route", help="Route a surface name or URL")
    route_p.add_argument("query", help="Surface description or URL")
    route_p.add_argument("--json", action="store_true", help="Emit the raw envelope")

    sub.add_parser("list", help="One line per registered surface")
    sub.add_parser("inventory", help="Full dump")

    args = parser.parse_args()

    if args.command == "route":
        env = build_envelope(args.query)
        if args.json:
            print(json.dumps(env, indent=2))
        else:
            print_envelope(env)
    elif args.command == "list":
        cmd_list()
    elif args.command == "inventory":
        cmd_inventory()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
