#!/usr/bin/env python3
"""
social_to_notion.py — Social URL -> rich Notion page, end to end.

CONTRACT: one command, any supported social URL in, one Notion page out —
metadata + embedded video + full transcript + engagement stats + a source
ledger (what was fetched, with what tool, and what degraded). This is the
glue the system was missing between apify_client.py / fetch-transcript.py
(acquisition) and notion_api.py (delivery).

Platform routing (by URL hostname):
    youtube.com / youtu.be -> fetch-transcript.py (youtube-transcript-api)
                              falling back to Apify sc-youtube-transcripts;
                              metadata via Apify `youtube` actor only if the
                              transcript path yielded none.
    tiktok.com             -> Apify sc-tiktok-video (metadata/stats) +
                              sc-tiktok-transcripts (transcript), unless
                              --no-transcript.
    instagram.com          -> Apify `instagram` (post/profile metadata).
    reddit.com              -> Apify `reddit`.
    linkedin.com            -> exit 2 (not in the approved actor whitelist).
    anything else            -> exit 2 (unsupported host).

Budget discipline: at most 3 Apify calls per invocation (hard local counter,
independent of apify_client.py's own $/month guard). Every Apify response is
checked for `.get("fallback")` / `status == "budget_exhausted"` (or any
other error/skip status) and the run degrades gracefully — never crashes,
never retries a fallback response.

Normalizes acquisition into one record dict:
    {platform, url, source_id, title, author, published,
     stats: {views, likes, comments, shares},
     transcript, embed_url, fetched_at, degraded: [...]}
Missing fields are always None — never invented.

--dry-run performs acquisition (network permitting) but NEVER calls Notion;
it prints the normalized record and the exact Notion payload (properties +
first block batch + total block count) as JSON. --transcript-file injects a
transcript from disk so dry-run is fully testable offline.

Usage:
    python3 execution/social_to_notion.py <url> [--db content|knowledge|captures]
        [--dry-run] [--transcript-file PATH] [--tags tag1,tag2]
        [--no-transcript] [--limit N]

Exit codes: 0 ok, 1 failure, 2 skip/unsupported (bad host, LinkedIn, etc.)
"""

import argparse
import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

BASE = Path(__file__).parent.parent
ENV_PATH = BASE / ".env"

MAX_APIFY_CALLS = 3

LINKEDIN_MESSAGE = (
    "LinkedIn scraping is not in the approved actor whitelist — see "
    "_active/knowledge/youtube-notion-replication/FULL-PICTURE.md § LinkedIn gap"
)


# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

def load_env(env_path: Optional[Path] = None):
    """Load .env into os.environ (setdefault — won't override existing)."""
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


# ---------------------------------------------------------------------------
# Module loaders (hyphenated filename, apify_client)
# ---------------------------------------------------------------------------

def _load_fetch_transcript_module():
    """fetch-transcript.py has a hyphen in its name — import via spec since
    a plain `import` statement can't reference it.

    Returns None (never raises, never exits the process) if the module
    can't be loaded — e.g. the optional `youtube-transcript-api` dependency
    is missing, which makes fetch-transcript.py call sys.exit(1) at import
    time. Callers must fall back gracefully (local regex extraction + Apify
    transcript actor) rather than crash the whole script over an optional dep.
    """
    # fetch-transcript.py prints an error + sys.exit(1) at *import time* if
    # youtube-transcript-api isn't installed. Check the dependency first so
    # we never trigger that noisy side effect (which would otherwise pollute
    # our stdout JSON output) — just fall back cleanly.
    if importlib.util.find_spec("youtube_transcript_api") is None:
        return None
    try:
        spec = importlib.util.spec_from_file_location(
            "fetch_transcript_mod", BASE / "execution" / "fetch-transcript.py"
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    except BaseException:
        return None


_VIDEO_ID_PATTERNS = [
    r'^[a-zA-Z0-9_-]{11}$',
    r'[?&]v=([a-zA-Z0-9_-]{11})',
    r'youtu\.be/([a-zA-Z0-9_-]{11})',
    r'youtube\.com/embed/([a-zA-Z0-9_-]{11})',
    r'youtube\.com/v/([a-zA-Z0-9_-]{11})',
]


def _extract_video_id_fallback(url_or_id: str) -> Optional[str]:
    """Local re-implementation of fetch-transcript.py's extract_video_id,
    used only when that module can't be imported (missing optional dep)."""
    import re
    if re.match(_VIDEO_ID_PATTERNS[0], url_or_id):
        return url_or_id
    for pattern in _VIDEO_ID_PATTERNS[1:]:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    return None


def _load_apify_client_module():
    spec = importlib.util.spec_from_file_location(
        "apify_client_mod", BASE / "execution" / "apify_client.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# Apify call budget
# ---------------------------------------------------------------------------

class ApifyBudget:
    """Hard local counter — at most MAX_APIFY_CALLS Apify calls per
    invocation of this script, independent of apify_client.py's own
    dollar-denominated monthly guard."""

    def __init__(self, apify_mod, max_calls: int = MAX_APIFY_CALLS):
        self.apify_mod = apify_mod
        self.max_calls = max_calls
        self.calls_made = 0

    def run(self, actor_key: str, run_input: dict, max_results: int) -> dict:
        if self.calls_made >= self.max_calls:
            return {
                "status": "call_budget_exhausted",
                "fallback": True,
                "message": (
                    f"social_to_notion.py local Apify call cap "
                    f"({self.max_calls}/invocation) reached before calling "
                    f"'{actor_key}'."
                ),
                "items": [],
            }
        self.calls_made += 1
        return self.apify_mod.run_actor(actor_key, run_input, max_results)


def is_degraded(result: dict) -> bool:
    """True if an Apify (or acquisition) response should be treated as a
    degraded/failed fetch rather than a usable result."""
    if not isinstance(result, dict):
        return True
    if result.get("fallback"):
        return True
    if result.get("status") not in ("ok", None):
        return True
    return False


# ---------------------------------------------------------------------------
# Normalized record
# ---------------------------------------------------------------------------

def new_record(platform: str, url: str) -> dict:
    return {
        "platform": platform,
        "url": url,
        "source_id": None,
        "title": None,
        "author": None,
        "published": None,
        "stats": {"views": None, "likes": None, "comments": None, "shares": None},
        "transcript": None,
        "embed_url": url,
        "fetched_at": now_iso(),
        "degraded": [],
        "ledger": [],  # [{tool, note}] — what was actually used
    }


def ledger_note(record: dict, tool: str, note: str):
    record["ledger"].append({"tool": tool, "note": note, "ts": now_iso()})


def _inject_transcript_file(record: dict, args):
    """--transcript-file always wins over any live fetch (offline-testable
    contract) — shared by every platform acquirer."""
    if not args.transcript_file:
        return
    try:
        record["transcript"] = Path(args.transcript_file).read_text(encoding="utf-8")
        ledger_note(record, "transcript-file", f"injected from {args.transcript_file}")
    except OSError as e:
        record["degraded"].append(f"failed to read --transcript-file: {e}")


def _dry_run_no_token_skip(record: dict, args, note: str) -> bool:
    """Returns True (and marks the record degraded-but-titled) if this is a
    dry run with no APIFY_TOKEN configured — Apify calls would just error,
    so skip them and let dry-run stay offline-friendly."""
    if args.dry_run and not os.environ.get("APIFY_TOKEN"):
        record["degraded"].append(f"dry-run: {note} (no APIFY_TOKEN)")
        record["title"] = record["title"] or record["url"]
        return True
    return False


def _fetch_single_item(record: dict, budget: ApifyBudget, actor_key: str,
                        run_input: dict, ledger_tool: str, ledger_desc: str) -> Optional[dict]:
    """Run one Apify actor expecting a single result item. Handles the
    degraded/zero-items/ledger bookkeeping shared by every metadata call —
    returns the item dict, or None (with `record` already updated) on any
    failure/degrade."""
    result = budget.run(actor_key, run_input, 1)
    if is_degraded(result):
        record["degraded"].append(
            f"Apify {actor_key} degraded: {result.get('message', result.get('status'))}"
        )
        return None
    items = result.get("items", [])
    if not items:
        record["degraded"].append(f"Apify {actor_key} returned zero items")
        return None
    ledger_note(record, ledger_tool, ledger_desc)
    return items[0]


# ---------------------------------------------------------------------------
# Platform: YouTube
# ---------------------------------------------------------------------------

def acquire_youtube(url: str, args, budget: ApifyBudget) -> dict:
    record = new_record("youtube", url)

    ft_mod = _load_fetch_transcript_module()
    if ft_mod is None:
        record["degraded"].append(
            "fetch-transcript.py unavailable (youtube-transcript-api not installed) — "
            "using local video-id regex fallback"
        )
        video_id = _extract_video_id_fallback(url)
    else:
        try:
            video_id = ft_mod.extract_video_id(url)
        except ValueError as e:
            record["degraded"].append(f"could not extract video id: {e}")
            video_id = None

    if video_id:
        record["source_id"] = video_id
        record["embed_url"] = f"https://www.youtube.com/embed/{video_id}"
    else:
        record["degraded"].append("could not extract a video id from the URL")

    _inject_transcript_file(record, args)
    if not record["transcript"] and not args.no_transcript and video_id and ft_mod is not None:
        try:
            record["transcript"] = ft_mod.fetch_transcript(video_id)
            ledger_note(record, "fetch-transcript.py", "youtube-transcript-api")
        except Exception as e:
            record["degraded"].append(f"youtube-transcript-api failed: {e}")
            # Fallback: Apify sc-youtube-transcripts
            t_item = _fetch_single_item(record, budget, "sc-youtube-transcripts",
                                         {"videoUrls": [url]}, "apify:sc-youtube-transcripts",
                                         "fallback transcript")
            if t_item:
                text = t_item.get("transcript") or t_item.get("text")
                if text:
                    record["transcript"] = text
                else:
                    record["degraded"].append("Apify sc-youtube-transcripts returned no transcript field")

    # Metadata: only hit Apify's `youtube` actor if we still have no title —
    # keep Apify calls minimal per the budget contract.
    if not record["title"] and not args.dry_run:
        item = _fetch_single_item(record, budget, "youtube",
                                   {"startUrls": [{"url": url}], "maxItems": 1},
                                   "apify:youtube", "metadata")
        if item:
            record["title"] = item.get("title")
            record["author"] = item.get("channelName") or item.get("author")
            record["published"] = item.get("date") or item.get("uploadDate")
            record["stats"]["views"] = item.get("viewCount") or item.get("views")
            record["stats"]["likes"] = item.get("likes")
            record["stats"]["comments"] = item.get("commentsCount") or item.get("comments")
    elif not record["title"] and args.dry_run and not args.transcript_file:
        record["degraded"].append("dry-run: metadata fetch skipped (no network / not attempted)")

    record["title"] = record["title"] or record["source_id"] or url

    return record


# ---------------------------------------------------------------------------
# Platform: TikTok
# ---------------------------------------------------------------------------

def acquire_tiktok(url: str, args, budget: ApifyBudget) -> dict:
    record = new_record("tiktok", url)
    _inject_transcript_file(record, args)

    if _dry_run_no_token_skip(record, args, "metadata/transcript fetch skipped"):
        return record

    item = _fetch_single_item(record, budget, "sc-tiktok-video", {"videos": [url]},
                               "apify:sc-tiktok-video", "metadata/stats")
    if item:
        record["source_id"] = item.get("id") or item.get("videoId")
        record["title"] = item.get("desc") or item.get("title") or item.get("text")
        author_meta = item.get("authorMeta")
        record["author"] = author_meta.get("name") if isinstance(author_meta, dict) else item.get("author")
        record["published"] = item.get("createTime") or item.get("createTimeISO")
        stats = item.get("stats") if isinstance(item.get("stats"), dict) else item
        record["stats"]["views"] = stats.get("playCount") or stats.get("views")
        record["stats"]["likes"] = stats.get("diggCount") or stats.get("likes")
        record["stats"]["comments"] = stats.get("commentCount") or stats.get("comments")
        record["stats"]["shares"] = stats.get("shareCount") or stats.get("shares")

    if not args.no_transcript and not record["transcript"]:
        t_item = _fetch_single_item(record, budget, "sc-tiktok-transcripts", {"videos": [url]},
                                     "apify:sc-tiktok-transcripts", "transcript")
        if t_item:
            text = t_item.get("transcript") or t_item.get("text")
            if text:
                record["transcript"] = text
            else:
                record["degraded"].append("Apify sc-tiktok-transcripts returned no transcript field")

    record["title"] = record["title"] or record["source_id"] or url
    return record


# ---------------------------------------------------------------------------
# Platform: Instagram
# ---------------------------------------------------------------------------

def acquire_instagram(url: str, args, budget: ApifyBudget) -> dict:
    record = new_record("instagram", url)
    _inject_transcript_file(record, args)

    if _dry_run_no_token_skip(record, args, "metadata fetch skipped"):
        return record

    item = _fetch_single_item(
        record, budget, "instagram",
        {"directUrls": [url], "resultsType": "posts", "resultsLimit": 1},
        "apify:instagram", "post/profile metadata",
    )
    if item:
        record["source_id"] = item.get("id") or item.get("shortCode")
        record["title"] = item.get("caption") or item.get("title")
        record["author"] = item.get("ownerUsername") or item.get("author")
        record["published"] = item.get("timestamp")
        record["stats"]["likes"] = item.get("likesCount")
        record["stats"]["comments"] = item.get("commentsCount")
        record["stats"]["views"] = item.get("videoViewCount") or item.get("videoPlayCount")

    record["degraded"].append("no transcript expected for instagram")
    record["title"] = record["title"] or record["source_id"] or url
    return record


# ---------------------------------------------------------------------------
# Platform: Reddit
# ---------------------------------------------------------------------------

def acquire_reddit(url: str, args, budget: ApifyBudget) -> dict:
    record = new_record("reddit", url)
    _inject_transcript_file(record, args)

    if _dry_run_no_token_skip(record, args, "metadata fetch skipped"):
        return record

    item = _fetch_single_item(
        record, budget, "reddit",
        {"startUrls": [{"url": url}], "maxItems": 1, "skipComments": True,
         "skipUserPosts": False, "skipCommunity": False},
        "apify:reddit", "post metadata",
    )
    if item:
        record["source_id"] = item.get("id")
        record["title"] = item.get("title")
        record["author"] = item.get("username") or item.get("author")
        record["published"] = item.get("createdAt") or item.get("date")
        record["stats"]["likes"] = item.get("upVotes") or item.get("score")
        record["stats"]["comments"] = item.get("numberOfComments")

    record["title"] = record["title"] or record["source_id"] or url
    return record


# ---------------------------------------------------------------------------
# Routing
# ---------------------------------------------------------------------------

def route_platform(url: str) -> Optional[str]:
    host = (urlparse(url).hostname or "").lower()
    host = host[4:] if host.startswith("www.") else host

    if host in ("youtube.com", "m.youtube.com") or host.endswith(".youtube.com") or host == "youtu.be":
        return "youtube"
    if host == "tiktok.com" or host.endswith(".tiktok.com"):
        return "tiktok"
    if host == "instagram.com" or host.endswith(".instagram.com"):
        return "instagram"
    if host == "reddit.com" or host.endswith(".reddit.com") or host == "redd.it":
        return "reddit"
    if host == "linkedin.com" or host.endswith(".linkedin.com"):
        return "linkedin"
    return None


ACQUIRERS = {
    "youtube": acquire_youtube,
    "tiktok": acquire_tiktok,
    "instagram": acquire_instagram,
    "reddit": acquire_reddit,
}


# ---------------------------------------------------------------------------
# Notion payload construction
# ---------------------------------------------------------------------------

def chunk_text(text: str, size: int = 1900) -> list:
    if not text:
        return []
    return [text[i:i + size] for i in range(0, len(text), size)]


def build_notion_payload(record: dict, notion_api, db_id: str, args) -> dict:
    """Returns {"properties": ..., "children": [...]} — the full block list
    (caller batches it into <=100-block create + append chunks)."""

    props_wanted = {
        "Name": {"title": {}},
        "Platform": {"select": {"options": [
            {"name": "youtube"}, {"name": "tiktok"},
            {"name": "instagram"}, {"name": "reddit"},
        ]}},
        "Author": {"rich_text": {}},
        "Source URL": {"rich_text": {}},
        "Views": {"number": {}},
        "Likes": {"number": {}},
        "Comments": {"number": {}},
        "Fetched": {"date": {}},
        "Tags": {"multi_select": {}},
    }
    available = notion_api._ensure_properties(db_id, props_wanted)

    properties = {}
    if "Name" in available:
        properties["Name"] = notion_api.title(record["title"] or record["url"])
    if "Platform" in available:
        properties["Platform"] = notion_api.select(record["platform"])
    if "Author" in available and record["author"]:
        properties["Author"] = notion_api.rich_text(str(record["author"]))
    if "Source URL" in available:
        properties["Source URL"] = notion_api.rich_text(record["url"])
    if "Views" in available and record["stats"]["views"] is not None:
        properties["Views"] = notion_api.number(record["stats"]["views"])
    if "Likes" in available and record["stats"]["likes"] is not None:
        properties["Likes"] = notion_api.number(record["stats"]["likes"])
    if "Comments" in available and record["stats"]["comments"] is not None:
        properties["Comments"] = notion_api.number(record["stats"]["comments"])
    if "Fetched" in available:
        properties["Fetched"] = notion_api.date(record["fetched_at"][:10])
    if "Tags" in available and args.tags:
        tags = [t.strip() for t in args.tags.split(",") if t.strip()]
        if tags:
            properties["Tags"] = notion_api.multi_select(tags)

    children = []

    # Embed block — NotionBlocks has no embed builder, construct inline.
    children.append({"object": "block", "type": "embed", "embed": {"url": record["url"]}})

    if record["degraded"]:
        children.append(notion_api.heading2("DEGRADED"))
        for reason in record["degraded"]:
            children.append(notion_api.para(f"DEGRADED: {reason}"))

    if record["transcript"]:
        children.append(notion_api.heading2("Transcript"))
        for chunk in chunk_text(record["transcript"]):
            children.append(notion_api.para(chunk))
    elif not args.no_transcript:
        children.append(notion_api.heading2("Transcript"))
        children.append(notion_api.para("(no transcript available)"))

    children.append(notion_api.heading2("Source Ledger"))
    children.append(notion_api.bullet(f"Platform: {record['platform']}"))
    children.append(notion_api.bullet(f"Fetched: {record['fetched_at']}"))
    for entry in record["ledger"]:
        children.append(notion_api.bullet(f"{entry['tool']}: {entry['note']}"))
    if not record["ledger"]:
        children.append(notion_api.bullet("No acquisition tool recorded"))
    for reason in record["degraded"]:
        children.append(notion_api.bullet(f"Degradation: {reason}"))

    return {"properties": properties, "children": children}


def create_notion_page(notion_api, db_id: str, payload: dict) -> str:
    """Create page with first <=90 blocks, then append the rest in batches
    of <=90 (Notion caps children at 100 blocks per API call)."""
    children = payload["children"]
    first_batch, rest = children[:90], children[90:]

    result = notion_api.create_page(db_id, payload["properties"], children=first_batch)
    page_id = result["id"]
    url = result["url"]

    for i in range(0, len(rest), 90):
        batch = rest[i:i + 90]
        notion_api._request("PATCH", f"/blocks/{page_id}/children", {"children": batch})

    return url


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        prog="social_to_notion.py",
        description="One command: social URL -> rich Notion page (metadata + embed + transcript + stats + ledger).",
    )
    parser.add_argument("url", help="Social URL (YouTube, TikTok, Instagram, Reddit)")
    parser.add_argument("--db", default="content", choices=["content", "knowledge", "captures"],
                        help="Target Notion database (default: content)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Acquire but never call Notion — print the payload as JSON")
    parser.add_argument("--transcript-file", default=None,
                        help="Inject a transcript from disk (enables fully offline testing)")
    parser.add_argument("--tags", default="", help="Comma-separated tags")
    parser.add_argument("--no-transcript", action="store_true",
                        help="Skip transcript acquisition entirely")
    parser.add_argument("--limit", type=int, default=1,
                        help="Result limit passed through to acquisition calls (default 1)")
    args = parser.parse_args()

    load_env()

    platform = route_platform(args.url)

    if platform == "linkedin":
        print(f"ERROR: {LINKEDIN_MESSAGE}", file=sys.stderr)
        sys.exit(2)

    if platform is None:
        host = urlparse(args.url).hostname or "(unparseable)"
        print(f"ERROR: unsupported host '{host}' — no acquisition route for this URL.", file=sys.stderr)
        sys.exit(2)

    apify_mod = _load_apify_client_module()
    budget = ApifyBudget(apify_mod)

    acquirer = ACQUIRERS[platform]
    try:
        record = acquirer(args.url, args, budget)
    except Exception as e:
        print(f"ERROR: acquisition failed for {platform}: {e}", file=sys.stderr)
        sys.exit(1)

    # notion_api is only needed once we're actually about to build/send a
    # payload — import lazily so --dry-run --transcript-file works with zero
    # network and no NOTION_API_KEY required for the acquisition side.
    try:
        from execution.notion_api import NotionAPI, DB_IDS
    except ImportError:
        sys.path.insert(0, str(BASE))
        from execution.notion_api import NotionAPI, DB_IDS

    if args.dry_run:
        # Build payload without ever touching Notion. Use a lightweight
        # stand-in for _ensure_properties so dry-run needs no API key/network.
        class _DryNotion:
            title = staticmethod(NotionAPI.title)
            rich_text = staticmethod(NotionAPI.rich_text)
            select = staticmethod(NotionAPI.select)
            multi_select = staticmethod(NotionAPI.multi_select)
            number = staticmethod(NotionAPI.number)
            date = staticmethod(NotionAPI.date)
            heading2 = staticmethod(NotionAPI.heading2)
            para = staticmethod(NotionAPI.para)
            bullet = staticmethod(NotionAPI.bullet)

            def _ensure_properties(self, database_id, required):
                # dry-run assumes every requested property is available so
                # the printed payload shows the full intended shape.
                return set(required.keys())

        dry_notion = _DryNotion()
        payload = build_notion_payload(record, dry_notion, DB_IDS.get(args.db, ""), args)

        output = {
            "record": record,
            "notion_payload": {
                "database": args.db,
                "properties": payload["properties"],
                "first_blocks": payload["children"][:90],
                "block_count": len(payload["children"]),
                "additional_batches": max(0, (len(payload["children"]) - 90 + 89) // 90) if len(payload["children"]) > 90 else 0,
            },
        }
        print(json.dumps(output, indent=2, default=str))
        sys.exit(0)

    db_id = DB_IDS.get(args.db, "")
    if not db_id:
        env_var = {
            "content": "NOTION_DB_CONTENT",
            "knowledge": "NOTION_DB_KNOWLEDGE",
            "captures": "NOTION_DB_CAPTURES",
        }.get(args.db, f"NOTION_DB_{args.db.upper()}")
        print(f"ERROR: no database id configured for --db {args.db}. Set {env_var} in .env.", file=sys.stderr)
        sys.exit(1)

    try:
        notion_api = NotionAPI()
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    payload = build_notion_payload(record, notion_api, db_id, args)

    try:
        page_url = create_notion_page(notion_api, db_id, payload)
    except Exception as e:
        print(f"ERROR: Notion page creation failed: {e}", file=sys.stderr)
        sys.exit(1)

    print(json.dumps({
        "status": "ok",
        "platform": platform,
        "title": record["title"],
        "notion_url": page_url,
        "transcript_chars": len(record["transcript"]) if record["transcript"] else 0,
        "degraded": record["degraded"],
    }, indent=2))
    sys.exit(0)


if __name__ == "__main__":
    main()
