---
description: One social URL to a rich Notion page — metadata, embed, transcript, stats, source ledger
---

# /social-to-notion — Social URL to Notion Page

Take any supported social URL and land one rich Notion page: metadata, embedded video, full transcript, engagement stats, and a source ledger recording what tool fetched what. Glue between `execution/apify_client.py` / `execution/fetch-transcript.py` (acquisition) and `execution/notion_api.py` (delivery) — `execution/social_to_notion.py` does the work in one command.

## Usage

```
/social-to-notion [URL]
/social-to-notion https://youtu.be/abc123 --db content
/social-to-notion https://www.tiktok.com/@user/video/123 --tags trend,q3
/social-to-notion --watch-packet /path/video-intelligence.json --topics "AI Agents,Claude"
```

## When to Use

- A source video/post needs to become a real, queryable Notion record — not a pasted link
- Building the content/knowledge library from social sources (YouTube, TikTok, Instagram, Reddit)
- Feeding `/atomize`, `/watch-and-remix`, or the Knowledge Vault from a single external post
- Banking an already-watched exact video in the shared Riley Social Intelligence DB without fetching it twice

---

## Steps

### 1. Intent Check

Confirm before running:
- **URL** — which platform? (youtube.com/youtu.be, tiktok.com, instagram.com, reddit.com supported; linkedin.com and anything else are hard-skipped, see Step 4)
- **Destination DB** — `content` (default), `knowledge`, or `captures`. Ask if ambiguous — this determines which Notion database the page lands in and which properties it enforces.
- **Transcript needed?** Default yes; pass `--no-transcript` for pure-metadata posts (Instagram never has one anyway).

If `/watch` already produced a `watch-video-intelligence/v1` manifest for an exact public YouTube video, use packet mode. It owns the transcript, frames, OCR, timestamp alignment, and acquisition provenance; do not send that exact URL through `/scrape-creator`, which expands to a creator-wide scrape. Packet bridge v1 intentionally rejects non-YouTube and local-only sources rather than risk collapsing distinct URLs.

### 2. Run the Script

// turbo
```bash
python3 execution/social_to_notion.py "[URL]" --db [content|knowledge|captures] --tags "[tag1,tag2]"
```

For a dry run (no Notion write, prints the full payload as JSON) or when testing offline:
```bash
python3 execution/social_to_notion.py "[URL]" --dry-run --transcript-file [path]
```

Flags: `--db` (default `content`), `--dry-run`, `--transcript-file PATH`, `--tags a,b`, `--no-transcript`, `--limit N`.

For an existing `/watch` packet, the destination is always the shared **Social Intelligence** DB and the canonical Post URL is the dedup key:
```bash
python3 execution/social_to_notion.py --watch-packet "[manifest]" --topics "[topic1,topic2]"
```
Add `--inspection-receipt "[receipt]"` only after the frames were actually opened and reviewed. Otherwise the honest state remains `VISUAL_CAPTURED_UNREVIEWED`. Use `--dry-run` unless the user explicitly asked to save/harvest/bank the video.

Exit codes: `0` ok · `1` failure (bad Notion config, acquisition crash) · `2` skip (LinkedIn or unsupported host — this is expected behavior, not a bug).

### 3. Verify

- **Live run**: confirm the printed JSON has `"status": "ok"` and open the `notion_url` — check the embed renders, the transcript reads cleanly (chunked into paragraphs), and the Source Ledger bullets name the actual tool used (`fetch-transcript.py`, `apify:sc-tiktok-video`, etc.).
- **Dry run**: read the printed `notion_payload` — verify `properties` has the fields you expect populated (Name, Platform, Author, stats where known), `block_count` is sane, and `record.degraded` is empty or explains itself.
- **Watch packet**: verify the action is `created`, `updated`, or `unchanged`; `Evidence State` matches the receipt boundary; canonical YouTube URL variants collapse to one `Post URL`; and `Watch Fingerprint` changes when the packet, reviewed-frame receipt, or topics change.
- If `record.transcript` is `null` on a video source, check `record.degraded` for the reason before assuming failure — some skips are by design (Instagram has no transcript track).

### 4. Degradation Handling

The script **never crashes on a budget/fetch failure** — it degrades and tells you in `degraded[]` and the Notion page's "DEGRADED" callout block. On any `budget_exhausted` / `fallback: true` Apify response:
- The page still gets created with whatever was acquired (metadata-only, or transcript-only).
- Re-route per `directives/apify-usage-policy.md` — do not retry the same fallback response immediately.
- The script caps itself at **3 Apify calls per invocation** regardless of the monthly budget state — if you see `call_budget_exhausted`, that's this local cap, not the monthly one; re-run is fine.
- LinkedIn URLs and unknown hosts exit 2 by design — don't retry, don't force through Apify's generic `web` actor as a substitute (see the error message for the documented gap).

### 5. Finalize

The operator runs Step 6 finalize per CLAUDE.md — this workflow does not auto-finalize:
```bash
python3 execution/chain_runner.py finalize "[what landed in Notion]" \
    --expert n/a --skill n/a --workflow social-to-notion \
    --type Extraction --intent [1-10] --expert-score [1-10] --adversarial [1-10] --sub-agents 0 \
    --notes "Social URL to Notion | Factual Grounding: N/A | Verification: N/A"
```

---

## Stacking

- **Porting into the second-brain wiki**: `skills/simon-intellectual-library-os` for structured Notion library organization once pages accumulate.
- **Trend analysis pass on TikTok sources**: `skills/mike-foutia-marketing-tools` has a TikTok trend scraper prompt — run it against the same source set for pattern analysis, separate from this ingestion step.
- **Downstream remix**: once the transcript is in Notion, `/watch-and-remix` or `/atomize` can work from the same source URL for content derivatives.

## Error Handling

- Acquisition exception (not a graceful Apify degrade) → exit 1, message on stderr, nothing written to Notion.
- Packet dedup query failure, multiple exact-URL matches, a non-YouTube URL, or a local-only source with no public URL → exit 1 and **no schema or page write**. Refreshes preserve Riley's `Batch`, `Extract Candidate`, title, creator, and hook.
- Missing `NOTION_DB_<X>` env var for the chosen `--db` → exit 1, names the exact env var to set.
- Missing `NOTION_API_KEY` → exit 1 via `NotionAPI()` construction failure.
- Partial acquisition (e.g. transcript failed, metadata succeeded) is NOT an error — it's a degraded but valid page.
