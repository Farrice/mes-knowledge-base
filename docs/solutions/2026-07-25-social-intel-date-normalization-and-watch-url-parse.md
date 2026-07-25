# Solution Card — social_intel.py: video-URL misparse + non-ISO date rejection

**Date**: 2026-07-25 · **Domain**: system fix (/scrape-creator pipeline) · **Status**: SOLVED (both)

## Problem

Running `/scrape-creator` against individual YouTube **watch URLs** produced two failures:

1. **URL misparse (FIXED 2026-07-25, same session)**: `social_intel.py scrape "https://www.youtube.com/watch?v=..."`
   extracted `watch` as the creator handle → Apify scraped an unrelated channel's video
   (created junk Notion pages; 2 renamed "🗑️ [MIS-SCRAPE — SAFE TO DELETE]" in the Social
   Intelligence DB, 2026-07-25). The scraper is handle/channel-oriented; a `/watch?v=` URL is
   not a creator reference.
2. **Date rejection (fixed)**: the YouTube Apify actor returns human dates (`"8 Jul 2026"`).
   `_to_date()` blindly truncated to 10 chars (`"23 Jul 2026"` → `"23 Jul 202"`), Notion
   rejected the whole page over the invalid ISO date, and the post was skipped.

## Solution

- **Fix shipped** (`execution/social_intel.py::_to_date`): parse-and-validate instead of
  truncate — accepts ISO timestamps, `YYYYMMDD`, epoch digits, and human formats
  (`%d %b %Y`, `%b %d, %Y`, `%d %B %Y`, `%B %d, %Y`); returns None (omit Posted) rather than
  ever emitting a non-ISO string. Verified against all formats + garbage.
- **Workaround for single videos**: scrape the CHANNEL handle (`yt-dlp --print uploader_id` to
  get it) with a limit covering the target videos; if specific videos still fail, backfill via
  the module's own `build_properties`/`build_body_blocks` with yt-dlp metadata (free) — see
  `scratchpad backfill_briar.py` pattern from this session.

## Prevention (SHIPPED)

`clean_handle()` now detects single-video URL markers (`/watch`, `youtu.be/`, `/shorts/`,
`/video/`, `/reel(s)/`, `/p/`), resolves them to the uploader handle via yt-dlp ($0) with a
printed NOTE, and exits with a clear error if resolution fails. Tested: video URL →
`BriarCochranShortForm`; handles and profile URLs unaffected.

## Reusable lesson

Never pass actor-supplied strings into schema-validated APIs (Notion dates) without
normalization — validate at the boundary, omit on failure rather than sending malformed values.
