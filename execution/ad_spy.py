#!/usr/bin/env python3
"""
ad_spy.py — deterministic ingestion layer for the /ad-spy workflow.

Why this exists: Playwright does the actual scraping (read-only browsing of
the Meta Ad Library — no login, no state changes). What's genuinely fiddly
and worth making deterministic is everything AFTER the observation: runtime
math, longevity ranking, Notion property mapping/chunking, and dedup-by-URL
so re-running a brand doesn't create duplicate pages. This script owns none
of the scraping — it only ingests ad records the calling agent already
observed with its own eyes in the browser.

NEVER fabricates data. Every field either comes straight from the input
JSON (which must be hand-populated from actually-observed Playwright
output) or is deterministically computed (runtime_days, rank).

Usage:
    python3 execution/ad_spy.py ingest --brand "AG1" --file ads.json [--batch ad-spy-2026-07-24-ag1]
    python3 execution/ad_spy.py verify --batch ad-spy-2026-07-24-ag1

Input JSON schema (list of ad records):
[
  {
    "headline": "string — primary hook/headline text as observed",
    "body_copy": "string — full ad copy as observed (optional)",
    "cta": "string — CTA button text, e.g. 'Shop Now' (optional)",
    "start_date": "YYYY-MM-DD — the 'Started running on' date, REQUIRED",
    "platforms": ["Facebook", "Instagram"],  # as shown in the ad's platform icons
    "media_type": "Static Ad" | "Video Ad",
    "media_url": "string — direct media URL if captured (optional)",
    "ad_library_url": "string — permalink to the specific ad (optional but recommended)",
    "analysis": "string — why-it-survived breakdown (optional, written by the agent)"
  },
  ...
]
"""

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from notion_api import NotionAPI, DB_IDS  # noqa: E402

SOCIAL_INTEL_DB = "3a749875a8978104a867fc9aeb53f52c"  # NOTION_DB_SOCIAL_INTEL

VALID_PLATFORMS = {"Instagram", "TikTok", "YouTube", "LinkedIn", "X", "Facebook", "Ad Library"}
VALID_TYPES = {"Reel", "Short", "Video", "Post", "Carousel", "Static Ad", "Video Ad"}


def runtime_days(start_date: str, as_of: str | None = None) -> int:
    """Days between start_date (YYYY-MM-DD) and as_of (defaults to today).
    This is the core Riley Brown heuristic: runtime = public proxy for ROI."""
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(as_of, "%Y-%m-%d").date() if as_of else date.today()
    return (end - start).days


def rank_by_longevity(ads: list[dict]) -> list[dict]:
    """Sorts ads descending by runtime_days. Mutates each dict to add
    'runtime_days' and 'rank' (1-indexed, longest first). Ads missing a
    valid start_date are dropped to the bottom, unranked (rank=None), and
    flagged — never silently treated as rank-worthy without a real date."""
    dated, undated = [], []
    for ad in ads:
        sd = ad.get("start_date", "")
        try:
            ad["runtime_days"] = runtime_days(sd)
            dated.append(ad)
        except (ValueError, TypeError):
            ad["runtime_days"] = None
            ad["rank"] = None
            undated.append(ad)
    dated.sort(key=lambda a: a["runtime_days"], reverse=True)
    for i, ad in enumerate(dated, start=1):
        ad["rank"] = i
    return dated + undated


def _existing_post_urls(api: NotionAPI, batch: str | None = None) -> set:
    """Pulls Post URL values already in the DB so ingest() can skip dupes.
    Best-effort — on any query failure, returns empty set (ingest proceeds,
    worst case a re-run creates a duplicate page rather than silently
    dropping real data)."""
    urls = set()
    try:
        cursor = None
        while True:
            body = {"page_size": 100}
            if cursor:
                body["start_cursor"] = cursor
            res = api._request("POST", f"/databases/{SOCIAL_INTEL_DB}/query", body)
            for page in res.get("results", []):
                u = page.get("properties", {}).get("Post URL", {}).get("url")
                if u:
                    urls.add(u)
            if not res.get("has_more"):
                break
            cursor = res.get("next_cursor")
    except Exception:
        return set()
    return urls


def ingest(brand: str, ads_path: str, batch: str | None = None, top_n: int | None = None,
           dry_run: bool = False) -> list[dict]:
    """Ranks ads by longevity and creates one Notion page per ad (skipping
    exact Post URL dupes already in the DB). Returns the list of created
    page results (or the ranked ad list if dry_run)."""
    ads = json.loads(Path(ads_path).read_text())
    ranked = rank_by_longevity(ads)
    if top_n:
        ranked = ranked[:top_n]

    if dry_run:
        return ranked

    api = NotionAPI()
    existing = _existing_post_urls(api)
    today = date.today().isoformat()
    created = []

    for ad in ranked:
        lib_url = ad.get("ad_library_url", "")
        if lib_url and lib_url in existing:
            print(f"  SKIP (dupe Post URL): {ad.get('headline', '')[:60]}")
            continue

        media_type = ad.get("media_type", "Static Ad")
        if media_type not in VALID_TYPES:
            media_type = "Static Ad"

        platforms = [p for p in ad.get("platforms", ["Ad Library"]) if p in VALID_PLATFORMS] or ["Ad Library"]

        runtime = ad.get("runtime_days")
        rank = ad.get("rank")
        headline = ad.get("headline", "(no headline captured)")
        title = f"{brand} — {headline[:70]}" + (f" ({runtime}d, #{rank})" if runtime is not None else "")

        props = {
            "Name": api.title(title[:200]),
            "Platform": api.select("Ad Library"),
            "Type": api.select(media_type),
            "Creator": api.rich_text(brand),
            "Scraped": api.date(today),
        }
        if ad.get("start_date"):
            props["Running Since"] = api.date(ad["start_date"])
        if ad.get("headline"):
            props["Hook"] = api.rich_text(ad["headline"][:2000])
        if lib_url:
            props["Post URL"] = {"url": lib_url}
        if ad.get("analysis"):
            props["Analysis"] = api.rich_text(ad["analysis"][:2000])
        if batch:
            props["Batch"] = api.rich_text(batch)
        if ad.get("media_url"):
            props["Media"] = {"files": [{"name": "ad_media", "external": {"url": ad["media_url"]}}]}
        if rank == 1:
            props["Extract Candidate"] = api.checkbox(True)

        body_text = (
            f"Platforms: {', '.join(platforms)}\n"
            f"Running since: {ad.get('start_date', 'unknown')} "
            f"({runtime if runtime is not None else 'unknown'} days as of {today})\n"
            f"CTA: {ad.get('cta', 'not captured')}\n\n"
            f"Body copy:\n{ad.get('body_copy', '(not captured)')}\n\n"
            f"Analysis:\n{ad.get('analysis', '(not written)')}"
        )
        children = [
            api.heading2("Ad Detail"),
            api.para(body_text),
        ]

        result = api.create_page(SOCIAL_INTEL_DB, props, children=children)
        created.append(result)
        print(f"  CREATED: {title[:80]} -> {result.get('url', '?')}")

    return created


def verify(batch: str) -> list[dict]:
    """Queries the Social Intelligence DB for pages tagged with a given
    Batch value — used to confirm what actually landed in Notion (never
    trust the ingest() print log alone)."""
    api = NotionAPI()
    res = api.query_database(SOCIAL_INTEL_DB, filter={
        "property": "Batch",
        "rich_text": {"equals": batch},
    })
    return res.get("results", [])


def main():
    parser = argparse.ArgumentParser(description="ad_spy.py — /ad-spy Notion ingestion helper")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_ingest = sub.add_parser("ingest", help="Rank ads by longevity and push to Social Intelligence DB")
    p_ingest.add_argument("--brand", required=True)
    p_ingest.add_argument("--file", required=True, help="Path to JSON ad records")
    p_ingest.add_argument("--batch", default=None, help="Batch tag for later verify/dedup")
    p_ingest.add_argument("--top", type=int, default=None, help="Only ingest the top N by runtime")
    p_ingest.add_argument("--dry-run", action="store_true", help="Rank only, print, don't write to Notion")

    p_verify = sub.add_parser("verify", help="Query Notion back for a batch tag")
    p_verify.add_argument("--batch", required=True)

    p_rank = sub.add_parser("rank", help="Rank a local ad JSON file by longevity, no Notion writes")
    p_rank.add_argument("--file", required=True)

    args = parser.parse_args()

    if args.cmd == "ingest":
        result = ingest(args.brand, args.file, batch=args.batch, top_n=args.top, dry_run=args.dry_run)
        if args.dry_run:
            for ad in result:
                print(f"#{ad.get('rank')} — {ad.get('runtime_days')}d — {ad.get('headline', '')[:70]}")
        else:
            print(f"\n{len(result)} page(s) created in Social Intelligence DB.")
    elif args.cmd == "verify":
        pages = verify(args.batch)
        print(f"{len(pages)} page(s) found for batch '{args.batch}':")
        for pg in pages:
            name = "".join(t.get("plain_text", "") for t in pg.get("properties", {}).get("Name", {}).get("title", []))
            print(f"  - {name} ({pg.get('url', '?')})")
    elif args.cmd == "rank":
        ads = json.loads(Path(args.file).read_text())
        ranked = rank_by_longevity(ads)
        for ad in ranked:
            print(f"#{ad.get('rank')} — {ad.get('runtime_days')}d — {ad.get('headline', '')[:70]}")


if __name__ == "__main__":
    main()
