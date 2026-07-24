---
description: Scrape any creator's content from any platform into the Social Intelligence Notion DB, then analyze why each post works
---

# 📡 /scrape-creator — Social Intelligence Pipeline

> **Purpose**: Riley Brown's flagship workflow ("scrape any creator's content from any
> platform → Notion database with video, transcript, metrics") — replicated and
> surpassed on infrastructure we already own. $0 new spend: `execution/apify_client.py`
> (budget-guarded Apify actors) + `execution/notion_api.py` (2022-06-28 pinned) +
> yt-dlp (free YouTube captions, tried before any paid transcript actor).

## Usage

```bash
python3 execution/social_intel.py scrape <handle_or_url> \
    [--platform auto|instagram|tiktok|youtube] [--limit N] [--batch TAG] [--dry-run]

python3 execution/social_intel.py status
```

Examples:
```bash
python3 execution/social_intel.py scrape @rileybrownai --platform youtube --limit 5 --batch riley-2026-07-24
python3 execution/social_intel.py scrape https://www.tiktok.com/@fitnessguy --limit 10
python3 execution/social_intel.py scrape realestatewithjing --platform instagram --limit 10 --dry-run
```

`--platform auto` detects platform from a pasted URL; a bare handle (no URL) needs
`--platform` explicitly. `--dry-run` runs the scrape (Apify cost still applies) and
prints what *would* be written, without touching Notion.

## Flow

### 1. Scrape
// turbo
```bash
python3 execution/social_intel.py scrape "<handle_or_url>" --platform <auto|instagram|tiktok|youtube> --limit <N> --batch "<tag>"
```

Per post: one Notion page in the **Social Intelligence** DB
(`3a749875-a897-8104-a867-fc9aeb53f52c`) with metrics (Views/Likes/Comments/Duration),
dates (Posted/Scraped), Post URL, Media (external file URL — never downloaded/uploaded),
Hook (first line of caption/transcript), and the full transcript/caption chunked into
the page body. Budget exhaustion degrades gracefully — a clear message, zero partial
writes. A single post failing mid-batch is skipped with a warning; the rest of the
batch still lands.

### 2. Analysis layer (Claude, after scrape)
Read back the batch (`Batch` property = the tag from step 1) and write a per-post "why
it works" into the **Analysis** rich_text property — this is the surpass-Riley-Brown
move; his workflow stops at raw data in a table. Ground each verdict in an existing hook
lens rather than freehand opinion:
- `skills/kallaway-*` (content psychology, hook/pattern-interrupt lenses)
- `skills/diandra-escobar-linkedin-growth/` hook-architect workflows (`diandra-hook-architect`, `diandra-rehook-teardown`)
- Platform-specific: `sky-tan-format-engine` (short-form format), `jenny-hoyos-viral-os` (retention mechanics) for YouTube Shorts/TikTok

Optional deepeners, not required for every batch — reach for them when a post warrants
more than a one-line verdict.

### 3. Surpass move — graduate to extraction
Any scraped creator whose corpus turns out to be pattern-rich graduates straight to
`/extract` — the corpus is already banked (transcripts + captions live in the Notion
page bodies from step 1), so extraction starts from real material instead of a cold
YouTube/TikTok crawl. Mark the graduating posts' `Extract Candidate` checkbox before
handing off.

## Cost Notes

- Apify budget: `.agent/apify-usage.json`, $29/mo plan, soft-warn at 70%, hard-stop at
  90%. `python3 execution/social_intel.py status` shows current state + last batch.
- Per-run ceiling: pay_per_event actors (TikTok scrape/transcripts) default to a
  $0.25/run ceiling inside `apify_client.py`; YouTube's metrics pull is per_result
  pricing (~$0.005/video) and its transcript is free via yt-dlp unless captions are
  missing, in which case it falls back to the paid `sc-youtube-transcripts` actor
  capped at $0.10/run.
- Instagram has no dedicated transcript actor in the current contract — caption stands
  in for Hook/Analysis basis on IG posts.
- Extractions triggered downstream via `/extract` are never gated (Farrice's standing
  decision, 2026-06-09) — only the scrape itself burns Apify budget.
