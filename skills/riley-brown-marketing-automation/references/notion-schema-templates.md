# Notion Schema — Social Intelligence DB

**Read this first:** Riley creates a throwaway Notion database per scrape ("put the notion database just in the archive... just for testing purposes" — `[primary]`). We do **not** replicate that. All Riley scrape/ad-spy output lands in **one shared, persistent DB**: **Social Intelligence** (`3a749875-a897-8104-a867-fc9aeb53f52c`, env `NOTION_DB_SOCIAL_INTEL`), written via `execution/notion_api.py` (pins `Notion-Version: 2022-06-28`). Canonical schema lives in `directives/notion-databases.md` — this file mirrors it and maps Riley's on-screen fields onto ours.

> Earlier drafts invented five bespoke databases (Creator Videos, Competitor Ads, Creator Profiles, Content Calendar, Ad Audits) with invented formulas ("Engagement Score = likes + 2×comments + 5×shares") Riley never specified. Those are removed. Riley ranks by "most engagement that are not sponsored" and by ad *duration* — no weighting formula is on record.

---

## The One Schema (Social Intelligence)

| Property | Type | Populated by | Notes |
|---|---|---|---|
| **Name** | title | both | `/scrape-creator`: post title/hook · `/ad-spy`: `"<Brand> — <headline> (<N>d, #<rank>)"` |
| **Creator** | rich_text | both | handle or brand name |
| **Platform** | select | both | Instagram / TikTok / YouTube / LinkedIn / X / Facebook / **Ad Library** |
| **Type** | select | both | Reel / Short / Video / Post / Carousel / **Static Ad** / **Video Ad** |
| **Post URL** | url | both | dedup key — re-running a brand/creator skips exact-URL matches |
| **Media** | files (external URLs) | both | never downloaded/uploaded — external file URL only |
| **Hook** | rich_text | both | first line of caption/transcript, or ad headline |
| **Views / Likes / Comments** | number | scrape only | **left blank for ads** — Meta Ad Library exposes none of these for commercial ads; never fabricate |
| **Duration (s)** | number | scrape | video length in seconds |
| **Posted** | date | scrape | original post date |
| **Running Since** | date | **ad-spy** | the observed "Started running on" date — the field the longest-running ranking depends on |
| **Scraped** | date | both | today |
| **Analysis** | rich_text (≤2000) | both | the "why it works" / "why it survived" verdict — full breakdown goes in the page **body** blocks (2000-char property cap; `notion_api.py` chunks long text into `heading2`/`para` blocks) |
| **Batch** | rich_text | both | run tag (e.g. `riley-2026-07-24`, `ad-spy-2026-07-24-ag1`) — lets `verify --batch <tag>` query results back |
| **Watch Fingerprint** | rich_text | `/watch` bridge | content-bound sync identity; keeps receipt/topic upgrades idempotent without overwriting Riley's `Batch` |
| **Evidence State** | select | `/watch` bridge | `TRANSCRIPT_ONLY` / `VISUAL_CAPTURED_UNREVIEWED` / `PARTIAL_VISUAL_VERIFIED` / `VISUAL_VERIFIED`; the Notion writer never upgrades this on its own |
| **Topics** | multi_select | `/watch` bridge | normalized, deduplicated caller/packet topics; no competing taxonomy engine |
| **Extract Candidate** | checkbox | both | marks a pattern-rich creator / #1 longest-running ad for graduation to `/extract` |

---

## How Riley's On-Screen Fields Map to Ours

- Riley's ad schema (`[visual]`, frame_0087): **Ad (thumbnail) / CTA / Competitor** → our `Media` / (CTA goes in `Analysis` body) / `Creator`. Clean 3-column structure; ours folds it into the shared DB.
- Riley's "why it works" text field, *labeled as inference from durability* → our `Analysis` property, with the same epistemic honesty required (see `/ad-spy` Step 4).
- Riley's creator DB read-back ("10 source videos downloaded, 10 transcripts succeeded") → our per-post pages with transcript/caption chunked into the page body.
- Riley's sponsored-exclusion audit trail → recorded in the `Analysis`/body of graduated posts and in the batch note (we don't add a separate `Is Sponsored` property; the analysis pass states which posts were excluded and why).

---

## Doctrine (from Riley, honored in our schema)

1. **The DB is staging; the skill is the durable asset.** Don't over-engineer per-scrape schemas. One shared DB + `Batch` tags + `Extract Candidate` is enough.
2. **Never invent a metric the source doesn't expose.** Ads have no likes/views/spend — leave blank.
3. **Rank honestly.** Creators by non-sponsored engagement; ads by runtime (an inference proxy, not ROAS proof).
4. **Bake "return a link" in.** Every write returns the Notion page/DB URL for instant review (Riley's "always provides a link" move).
5. **Verify before trusting a run.** `python3 execution/ad_spy.py verify --batch <tag>` queries Notion back — never report a count from the ingest log alone.
6. **Reuse evidence packets.** Exact videos flow `/watch` packet → `social_to_notion.py --watch-packet` → this same DB. Do not send them through creator scraping or download them twice.
