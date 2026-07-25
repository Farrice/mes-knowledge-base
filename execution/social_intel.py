#!/usr/bin/env python3
"""
Social Intelligence Pipeline — scrape any creator's content from any platform
into the "Social Intelligence" Notion database (video, transcript, metrics).

Replicates (and surpasses) Riley Brown's flagship "scrape a creator -> Notion
database" workflow, built entirely on infrastructure we already own:
    - execution/apify_client.py  (Apify actors, budget-guarded, never raises)
    - execution/notion_api.py    (Notion writes, Notion-Version 2022-06-28 pinned)
    - yt-dlp                     (free YouTube captions — tried before any
                                   paid transcript actor)

Zero new spend beyond the existing Apify wallet. Zero new dependencies.

CLI:
    python3 execution/social_intel.py scrape <handle_or_url> \
        [--platform auto|instagram|tiktok|youtube] [--limit N] [--batch TAG] [--dry-run]
    python3 execution/social_intel.py status

Contract (fixed, do not re-derive):
    - Notion DB "Social Intelligence": id in NOTION_DB_SOCIAL_INTEL (.env).
      Properties: Name (title), Creator (rich_text), Platform (select),
      Type (select), Post URL (url), Media (files), Hook (rich_text),
      Views/Likes/Comments/Duration (s) (number), Posted/Scraped/Running
      Since (date), Analysis (rich_text), Batch (rich_text),
      Extract Candidate (checkbox).
    - Media uses EXTERNAL file URLs from the scrape — never downloads or
      uploads binaries.
    - Long transcripts: an excerpt lives in the Hook property; the FULL
      transcript is chunked into <=1900-char paragraph blocks in the page
      body (Notion's per-rich-text-object cap is 2000 chars).
    - Budget exhaustion is graceful: apify_client.run_actor NEVER raises —
      it returns {"status": "budget_exhausted", ...}. When that happens we
      print a clear message and write NOTHING partial to Notion. A single
      post failing mid-batch is skipped with a warning; the batch continues.
"""

import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).parent))
from apify_client import run_actor, load_env as apify_load_env, load_usage, budget_state  # noqa: E402
from notion_api import NotionAPI  # noqa: E402

BASE = Path(__file__).parent.parent
STATE_FILE = BASE / ".agent" / "social-intel-state.json"

PLATFORM_LABELS = {"instagram": "Instagram", "tiktok": "TikTok", "youtube": "YouTube"}


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------

def detect_platform(handle_or_url: str) -> str:
    low = handle_or_url.lower()
    if "tiktok.com" in low:
        return "tiktok"
    if "instagram.com" in low:
        return "instagram"
    if "youtube.com" in low or "youtu.be" in low:
        return "youtube"
    return ""


_VIDEO_URL_MARKERS = ("/watch", "youtu.be/", "/shorts/", "/video/", "/reel/", "/reels/", "/p/")


def _resolve_video_url_to_handle(url: str) -> str:
    """A single-video URL is not a creator reference. Resolve it to the
    uploader's handle via yt-dlp ($0) so the scrape targets the right
    creator — the 2026-07-25 mis-scrape put 'watch' through as a handle."""
    if shutil.which("yt-dlp"):
        try:
            out = subprocess.run(
                ["yt-dlp", "--skip-download", "--no-update", "--print", "uploader_id", url],
                capture_output=True, timeout=60, text=True,
            )
            handle = (out.stdout or "").strip().splitlines()[-1].lstrip("@") if out.stdout else ""
            if handle:
                print(f"NOTE: '{url}' is a single-video URL — resolved to creator "
                      f"'@{handle}'; scraping that creator's recent posts instead.")
                return handle
        except Exception:
            pass
    sys.exit(f"ERROR: '{url}' is a single-video URL, not a creator/channel reference, "
             f"and it could not be resolved to a handle. Pass the creator's handle or "
             f"profile URL instead.")


def clean_handle(raw: str) -> str:
    """Extract a bare handle from a URL, or strip a leading @ from a handle."""
    raw = raw.strip()
    if raw.startswith("http"):
        low = raw.lower()
        if any(m in low for m in _VIDEO_URL_MARKERS):
            return _resolve_video_url_to_handle(raw)
        path = urlparse(raw).path.strip("/")
        seg = path.split("/")[0] if path else ""
        return seg.lstrip("@") or raw
    return raw.lstrip("@")


def hook_from_text(text: str, max_len: int = 200) -> str:
    """First line of caption/transcript, truncated to a Hook-sized excerpt."""
    if not text:
        return ""
    text = text.strip()
    first = text.splitlines()[0].strip() if text else ""
    if not first:
        first = text[:max_len]
    if len(first) > max_len:
        cut = first[:max_len].rsplit(" ", 1)[0]
        first = (cut or first[:max_len]) + "…"
    return first


def _to_date(value) -> Optional[str]:
    """Normalize any actor-supplied date to a valid ISO date, else None.

    Actors return a zoo: ISO timestamps, 'YYYYMMDD', epoch numbers, and
    human strings like '8 Jul 2026' (yt actor, 2026-07-25). Never emit a
    non-ISO string — Notion rejects the whole page over it.
    """
    if not value:
        return None
    raw = str(value).strip()
    candidate = raw[:10]
    try:
        return datetime.strptime(candidate, "%Y-%m-%d").date().isoformat()
    except ValueError:
        pass
    if raw.isdigit():
        if len(raw) == 8:  # YYYYMMDD
            try:
                return datetime.strptime(raw, "%Y%m%d").date().isoformat()
            except ValueError:
                pass
        return _epoch_to_date(raw)
    for fmt in ("%d %b %Y", "%b %d, %Y", "%d %B %Y", "%B %d, %Y"):
        try:
            return datetime.strptime(raw, fmt).date().isoformat()
        except ValueError:
            continue
    return None


def _epoch_to_date(value) -> Optional[str]:
    if value is None:
        return None
    try:
        return datetime.fromtimestamp(int(value), tz=timezone.utc).date().isoformat()
    except Exception:
        return None


def _chunk(text: str, size: int = 1900) -> list:
    text = text or ""
    return [text[i:i + size] for i in range(0, len(text), size)] or [""]


def _best_thumbnail(thumbnails) -> Optional[str]:
    if not thumbnails:
        return None
    for t in thumbnails:
        url = (t or {}).get("url", "")
        if "maxresdefault" in url and url.endswith(".jpg"):
            return url
    return (thumbnails[-1] or {}).get("url")


def default_type_label(platform: str, duration_s=None, ig_type: str = "") -> str:
    if platform == "youtube":
        try:
            return "Short" if duration_s is not None and float(duration_s) <= 60 else "Video"
        except (TypeError, ValueError):
            return "Video"
    if platform == "tiktok":
        return "Reel"
    if platform == "instagram":
        if ig_type == "Sidecar":
            return "Carousel"
        if ig_type == "Video":
            return "Reel"
        return "Post"
    return "Post"


# ---------------------------------------------------------------------------
# YouTube — free caption path (yt-dlp) before any paid actor
# ---------------------------------------------------------------------------

def _vtt_to_text(vtt_content: str) -> str:
    """Collapse a YouTube rolling-caption VTT into plain, deduped text.

    YouTube auto-caption cues repeat the previous line and grow a new one
    word-by-word. Taking the LAST non-blank line of each cue and dropping
    consecutive duplicates reconstructs a clean transcript without the
    rolling overlap.
    """
    lines = vtt_content.splitlines()
    cues, current = [], []
    for raw in lines:
        line = raw.strip()
        if not line:
            if current:
                cues.append(current)
                current = []
            continue
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:") or "-->" in line:
            continue
        clean = re.sub(r"<[^>]+>", "", line).strip()
        if clean:
            current.append(clean)
    if current:
        cues.append(current)

    kept, prev = [], None
    for cue in cues:
        last = cue[-1] if cue else ""
        if last and last != prev:
            kept.append(last)
            prev = last
    return html.unescape(" ".join(kept)).strip()


def fetch_yt_transcript_ytdlp(video_url: str, video_id: str) -> Optional[str]:
    """Free transcript via yt-dlp's caption download. $0 cost. Returns None
    on any failure (no captions, network error, missing binary) — caller
    falls back to the paid sc-youtube-transcripts actor."""
    if not shutil.which("yt-dlp"):
        return None
    tmp_dir = Path(tempfile.mkdtemp(prefix="social_intel_yt_"))
    try:
        cmd = [
            "yt-dlp", "--skip-download", "--write-auto-sub", "--write-sub",
            "--sub-lang", "en", "--sub-format", "vtt", "--quiet", "--no-warnings",
            "-o", str(tmp_dir / "%(id)s.%(ext)s"), video_url,
        ]
        subprocess.run(cmd, capture_output=True, timeout=90, text=True)
        vtt_files = list(tmp_dir.glob(f"{video_id}*.vtt")) or list(tmp_dir.glob("*.vtt"))
        if not vtt_files:
            return None
        text = _vtt_to_text(vtt_files[0].read_text(encoding="utf-8", errors="ignore"))
        return text or None
    except Exception:
        return None
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def fetch_yt_transcript_fallback(video_url: str) -> Optional[str]:
    """Paid fallback (sc-youtube-transcripts) — only reached when yt-dlp
    has no captions. Kept well under the $0.25 per-run ceiling."""
    result = run_actor("sc-youtube-transcripts", {"videoUrls": [video_url]}, 1, max_cost=0.10)
    if result.get("status") != "ok" or not result.get("items"):
        return None
    item = result["items"][0]
    return item.get("transcript") or item.get("text") or None


# ---------------------------------------------------------------------------
# Per-platform scrape functions
# Each returns (posts: list[dict], raw_apify_result: dict)
# ---------------------------------------------------------------------------

def scrape_youtube(handle: str, limit: int):
    result = run_actor("youtube", {"youtubeHandles": [f"@{handle}"], "maxItems": limit}, limit)
    if result.get("status") != "ok":
        return [], result
    posts = []
    for item in result["items"][:limit]:
        video_id = item.get("id", "")
        posts.append({
            "platform": "youtube",
            "creator": (item.get("channel") or {}).get("name") or handle,
            "title": item.get("title") or "Untitled",
            "post_url": item.get("url") or (f"https://www.youtube.com/watch?v={video_id}" if video_id else ""),
            "media_url": _best_thumbnail(item.get("thumbnails")) or item.get("url"),
            "caption": item.get("description") or "",
            "views": item.get("views"),
            "likes": item.get("likes"),
            "comments": item.get("comments"),
            "duration_s": item.get("duration"),
            "posted_iso": _to_date(item.get("publishDate") or item.get("uploadDate")),
            "video_id": video_id,
        })
    return posts, result


def scrape_tiktok(handle: str, limit: int):
    result = run_actor("sc-tiktok", {"usernames": [handle], "maxItems": limit}, limit, max_cost=0.25)
    if result.get("status") != "ok":
        return [], result
    posts = []
    for item in result["items"][:limit]:
        video_meta = item.get("videoMeta") or {}
        author_meta = item.get("authorMeta") or {}
        caption = item.get("text") or item.get("caption") or item.get("desc") or ""
        video_url = item.get("webVideoUrl") or item.get("url") or item.get("shareUrl") or ""
        posts.append({
            "platform": "tiktok",
            "creator": author_meta.get("name") or item.get("author") or handle,
            "title": hook_from_text(caption) or "Untitled TikTok",
            "post_url": video_url,
            "media_url": video_meta.get("coverUrl") or item.get("cover") or video_url,
            "caption": caption,
            "views": item.get("playCount") or item.get("views"),
            "likes": item.get("diggCount") or item.get("likes"),
            "comments": item.get("commentCount") or item.get("comments"),
            "duration_s": video_meta.get("duration") or item.get("duration"),
            "posted_iso": _to_date(item.get("createTimeISO")) or _epoch_to_date(item.get("createTime")),
            "video_id": item.get("id") or item.get("videoId"),
        })
    return posts, result


def fetch_tiktok_transcripts(posts: list, max_cost: float = 0.25) -> dict:
    """Batched — one actor call for the whole post list to keep cost and
    call count down (the actor has no per-item pricing advantage to
    calling it N times)."""
    urls = [p["post_url"] for p in posts if p.get("post_url")]
    if not urls:
        return {}
    result = run_actor("sc-tiktok-transcripts", {"videos": urls}, len(urls), max_cost=max_cost)
    if result.get("status") != "ok":
        return {}
    mapping = {}
    for item in result.get("items", []):
        url = item.get("videoUrl") or item.get("url") or item.get("webVideoUrl")
        text = item.get("transcript") or item.get("text") or item.get("subtitle")
        if url and text:
            mapping[url] = text
    return mapping


def scrape_instagram(handle: str, limit: int):
    result = run_actor(
        "instagram",
        {
            "directUrls": [f"https://www.instagram.com/{handle}/"],
            "resultsType": "posts",
            "resultsLimit": limit,
            "onlyPostsNewerThan": "365 days",
        },
        limit,
    )
    if result.get("status") != "ok":
        return [], result
    posts = []
    for item in result["items"][:limit]:
        caption = item.get("caption") or ""
        ig_type = item.get("type") or ""
        images = item.get("images") or []
        media_url = item.get("videoUrl") or item.get("displayUrl") or (images[0] if images else None)
        posts.append({
            "platform": "instagram",
            "creator": item.get("ownerUsername") or handle,
            "title": hook_from_text(caption) or "Untitled Post",
            "post_url": item.get("url") or "",
            "media_url": media_url,
            "caption": caption,
            "views": item.get("videoViewCount") or item.get("videoPlayCount"),
            "likes": item.get("likesCount"),
            "comments": item.get("commentsCount"),
            "duration_s": item.get("videoDuration"),
            "posted_iso": _to_date(item.get("timestamp")),
            "ig_type": ig_type,
        })
    return posts, result
    # NOTE: no dedicated transcript actor exists for Instagram in the
    # contract — caption stands in for Hook/Analysis basis.


# ---------------------------------------------------------------------------
# Notion write layer
# ---------------------------------------------------------------------------

def build_properties(post: dict, batch: str) -> dict:
    props: dict = {
        "Name": NotionAPI.title((post.get("title") or "Untitled")[:200]),
        "Creator": NotionAPI.rich_text((post.get("creator") or "")[:1900]),
        "Platform": NotionAPI.select(PLATFORM_LABELS[post["platform"]]),
        "Type": NotionAPI.select(
            post.get("type_label")
            or default_type_label(post["platform"], post.get("duration_s"), post.get("ig_type", ""))
        ),
        "Scraped": NotionAPI.date(datetime.now(timezone.utc).date().isoformat()),
        "Batch": NotionAPI.rich_text(batch[:1900]),
        "Extract Candidate": NotionAPI.checkbox(False),
    }
    if post.get("post_url"):
        props["Post URL"] = {"url": post["post_url"]}
    if post.get("media_url"):
        props["Media"] = {"files": [{
            "name": (post.get("title") or "media")[:100],
            "type": "external",
            "external": {"url": post["media_url"]},
        }]}
    hook = post.get("hook") or hook_from_text(post.get("transcript") or post.get("caption") or "")
    if hook:
        props["Hook"] = NotionAPI.rich_text(hook[:1900])
    for src_key, notion_key in (
        ("views", "Views"), ("likes", "Likes"),
        ("comments", "Comments"), ("duration_s", "Duration (s)"),
    ):
        val = post.get(src_key)
        if val is not None:
            try:
                props[notion_key] = NotionAPI.number(float(val))
            except (TypeError, ValueError):
                pass
    if post.get("posted_iso"):
        props["Posted"] = NotionAPI.date(post["posted_iso"])
    return props


def build_body_blocks(post: dict) -> list:
    blocks = []
    caption = post.get("caption")
    if caption:
        blocks.append(NotionAPI.heading2("Caption / Description"))
        blocks.extend(NotionAPI.para(c) for c in _chunk(caption))
    transcript = post.get("transcript")
    if transcript:
        blocks.append(NotionAPI.heading2("Transcript"))
        blocks.extend(NotionAPI.para(c) for c in _chunk(transcript))
    blocks.append(NotionAPI.heading2("Source"))
    blocks.append(NotionAPI.para(
        f"Scraped via social_intel.py from {PLATFORM_LABELS.get(post['platform'], post['platform'])} "
        f"— {post.get('post_url', '(no url)')}"
    ))
    return blocks


def _update_state(batch: str, platform: str, count: int, status: str):
    try:
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATE_FILE.write_text(json.dumps({
            "last_batch": batch,
            "last_platform": platform,
            "last_count": count,
            "last_status": status,
            "last_run_at": datetime.now(timezone.utc).isoformat(),
        }, indent=2))
    except Exception:
        pass  # non-fatal — state tracking is best-effort


# ---------------------------------------------------------------------------
# CLI commands
# ---------------------------------------------------------------------------

def cmd_scrape(args):
    apify_load_env()
    db_id = os.environ.get("NOTION_DB_SOCIAL_INTEL", "")
    if not db_id:
        print("ERROR: NOTION_DB_SOCIAL_INTEL not set in .env")
        sys.exit(1)

    platform = args.platform
    if platform == "auto":
        platform = detect_platform(args.handle)
        if not platform:
            print(f"ERROR: could not auto-detect platform from '{args.handle}'. "
                  f"Pass --platform instagram|tiktok|youtube.")
            sys.exit(1)

    handle = clean_handle(args.handle)
    batch = args.batch or f"batch-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

    print(f"Scraping {platform} creator '{handle}' (limit={args.limit}, batch={batch})...")

    if platform == "youtube":
        posts, raw = scrape_youtube(handle, args.limit)
    elif platform == "tiktok":
        posts, raw = scrape_tiktok(handle, args.limit)
    elif platform == "instagram":
        posts, raw = scrape_instagram(handle, args.limit)
    else:
        print(f"ERROR: unsupported platform '{platform}'")
        sys.exit(1)

    if raw.get("status") != "ok":
        print(f"Scrape did not complete — status: {raw.get('status')}. {raw.get('message', '')}")
        print("Nothing written to Notion (no partial writes on a failed/budget-exhausted scrape).")
        _update_state(batch, platform, 0, raw.get("status", "error"))
        return

    if not posts:
        print("No posts returned. Nothing to write.")
        _update_state(batch, platform, 0, "empty")
        return

    # Transcripts — free path first, per-platform contract.
    if platform == "youtube":
        for post in posts:
            transcript = fetch_yt_transcript_ytdlp(post["post_url"], post.get("video_id", ""))
            if not transcript:
                transcript = fetch_yt_transcript_fallback(post["post_url"])
            post["transcript"] = transcript
            post["hook"] = hook_from_text(transcript or post.get("caption") or post["title"])
    elif platform == "tiktok":
        mapping = fetch_tiktok_transcripts(posts)
        for post in posts:
            post["transcript"] = mapping.get(post["post_url"])
            post["hook"] = hook_from_text(post["transcript"] or post.get("caption") or post["title"])
    else:  # instagram — no transcript actor in contract
        for post in posts:
            post["hook"] = hook_from_text(post.get("caption") or post["title"])

    if args.dry_run:
        print("\n--- DRY RUN: would create these Notion pages (no writes performed) ---")
        for p in posts:
            has_t = "transcript" if p.get("transcript") else "no transcript"
            print(f"  [{p['platform']}] {p['title'][:60]!r} — {has_t} — {p.get('post_url', '')}")
        print(f"\nApify cost incurred this run: ${raw.get('cost_dollars', 0):.4f}")
        _update_state(batch, platform, 0, "dry_run")
        return

    api = NotionAPI()
    created, failed = [], []
    for post in posts:
        try:
            props = build_properties(post, batch)
            blocks = build_body_blocks(post)
            result = api.create_page(db_id, props, children=blocks)
            created.append((post["title"], result["url"]))
        except Exception as e:  # noqa: BLE001 — individual failure must not kill the batch
            failed.append((post.get("title", "?"), str(e)))
            print(f"  WARNING: skipped '{post.get('title', '?')}' — {e}")

    print("\n--- Summary ---")
    for title, url in created:
        print(f"  {title[:55]:<57} {url}")
    if failed:
        print(f"\n{len(failed)} post(s) failed and were skipped (see warnings above).")
    print(f"\nCreated {len(created)}/{len(posts)} Notion page(s).")
    print(f"Apify cost this run: ${raw.get('cost_dollars', 0):.4f} (scrape) "
          f"+ any transcript-fallback cost noted above.")
    print(f"Notion DB: https://www.notion.so/{db_id.replace('-', '')}")

    _update_state(batch, platform, len(created), "ok")


def cmd_status(_args):
    apify_load_env()
    db_id = os.environ.get("NOTION_DB_SOCIAL_INTEL", "")
    usage = load_usage()
    state = budget_state(usage)
    last = {}
    if STATE_FILE.exists():
        try:
            last = json.loads(STATE_FILE.read_text())
        except Exception:
            last = {}
    print(json.dumps({
        "notion_db_id": db_id or None,
        "notion_db_url": f"https://www.notion.so/{db_id.replace('-', '')}" if db_id else None,
        "apify_budget_state": state,
        "apify_spent_dollars": round(usage["spent_dollars"], 4),
        "apify_remaining_dollars": round(usage["plan_dollars"] - usage["spent_dollars"], 4),
        "last_run": last or None,
    }, indent=2))


def main():
    apify_load_env()
    p = argparse.ArgumentParser(
        prog="social_intel.py",
        description="Scrape any creator's content into the Social Intelligence Notion DB.",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    ps = sub.add_parser("scrape", help="Scrape a creator and write posts to Notion")
    ps.add_argument("handle", help="Handle (e.g. @rileybrownai) or full profile/video URL")
    ps.add_argument("--platform", default="auto", choices=["auto", "instagram", "tiktok", "youtube"])
    ps.add_argument("--limit", type=int, default=5)
    ps.add_argument("--batch", default="")
    ps.add_argument("--dry-run", action="store_true")

    sub.add_parser("status", help="Show DB id, Apify budget, and last batch")

    args = p.parse_args()
    if args.cmd == "scrape":
        cmd_scrape(args)
    elif args.cmd == "status":
        cmd_status(args)


if __name__ == "__main__":
    main()
