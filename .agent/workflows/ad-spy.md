---
description: "$0 competitor ad-spy — Meta Ad Library via read-only Playwright, ranked by ad runtime (Riley Brown's longest-running-ad-wins heuristic), ingested to the Social Intelligence Notion DB."
---

# /ad-spy — Competitor Ad Intelligence ($0, No Foreplay)

> Replicates Riley Brown's Foreplay workflow with free infrastructure. Core heuristic: **the longest-running ad is the winning ad.** Meta doesn't let advertisers keep paying for a losing ad — nobody burns budget on a creative for 9 months unless it's converting. Runtime is the public, unpaywalled proxy for ROI that Foreplay charges $59-149/mo to surface. This workflow gets the same signal at $0.

## Usage

```
/ad-spy <brand or advertiser name> [--vertical supplement|fitness|saas|dtc|...] [--country US] [--top N]
```

Examples: `/ad-spy AG1 --vertical supplement`, `/ad-spy "Momentous" --top 10`

Feeds Farrice's $2,500 10-day sprint offer (supplement/performance brand ICP, see `project_proof-to-market-path-a.md`) — start with the brand's #1 competitor before pitching, then hand the client the same read on themselves.

---

## Step 1 — Meta Ad Library (PRIMARY, $0)

Read-only browsing per `directives/browser-automation-safety.md` — this is Tier 1 (navigate, snapshot, evaluate; no login, no state changes, no forms submitted). Use the Playwright MCP tools (`mcp__playwright__browser_navigate`, `browser_snapshot`, `browser_evaluate`, `browser_take_screenshot`).

**1a. Navigate to the advertiser's active-ad set:**

```
https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=<BRAND>&search_type=keyword_unordered&media_type=all
```

- `active_status=active` — only currently-running ads (the ones still being paid for = the signal we want). Optionally re-run with `active_status=all` to see recently-stopped ads too (useful for spotting a creative that just got retired — still informative, just not "currently winning").
- `country=US` doubles as a rough English-only filter (Meta doesn't expose a direct language param on this endpoint) — swap for the client's actual target market if not US.
- `q=<BRAND>` — try the brand name first; if results are thin, retry with the parent company name (e.g., a DTC brand under a larger holding co) and with `search_type=page` if you have the exact Facebook Page name.

**1b. Take a `browser_snapshot`** (accessibility tree, not a screenshot — it exposes structured text more reliably than pixels) of the results grid.

**1c. For each ad card, extract:**
- **"Started running on [date]"** or **"Started running on [date] · Total active time [N days]"** — the field the whole ranking depends on. If Meta shows a date range instead (some placements), use the start date.
- **Library ID** (e.g., `Library ID: 1234567890`) — build the permalink `https://www.facebook.com/ads/library/?id=<LIBRARY_ID>` for the `ad_library_url` field; this is what dedup in `ad_spy.py` keys off.
- **Platforms** shown as small icons on the card (Facebook, Instagram, Messenger, Audience Network) — map to the Notion `Platform` multi-select values that exist (Facebook, Instagram; anything else logs as "Ad Library" only).
- **Primary text / headline** (the hook — first 1-2 lines shown before "See more")
- **Full body copy** — click "See ad details" or expand "See more" if truncated; use `browser_click` (still Tier 1 — expanding text is not a state change to any account) then re-snapshot.
- **CTA button text** (Shop Now, Learn More, Sign Up, etc.)
- **Media type** — static image → `Static Ad`; video → `Video Ad`; carousel → capture as `Static Ad` and note "carousel" in the analysis text.
- **Media URL** if directly visible in the DOM (`browser_evaluate` to pull `img[src]` / `video[src]` from the ad card) — best-effort, not always exposed without opening the ad detail modal.

**What the Ad Library does NOT expose** (unlike organic post scraping): no view counts, no likes, no comments, no spend, no impressions — Meta only surfaces spend/reach ranges for political/issue ads, not commercial ones. Leave `Views`/`Likes`/`Comments` blank in Notion rather than inventing a number. This is the one real gap versus Foreplay (which infers spend from other signals) — runtime is still the strongest free proxy available.

**1d. Scroll / paginate** (`browser_evaluate` scroll-to-bottom, then re-snapshot) until you've covered all active ads or hit a reasonable ceiling (~20-30 for a first pass).

## Step 2 — Rank by Longevity

The whole point. For each ad: `runtime_days = today - start_date`. Sort descending. The top of the list is the ad Meta's advertiser has kept paying for the longest — treat it as the strongest signal in the set, not a curiosity.

Use `execution/ad_spy.py rank --file <ads.json>` to do this deterministically once you've hand-populated a JSON file from what you observed (see schema in the script's docstring) — don't eyeball date math, the script computes `runtime_days` and assigns `rank` for you.

## Step 3 — Ingest to Notion (Social Intelligence DB)

DB: **Social Intelligence** (`3a749875-a897-8104-a867-fc9aeb53f52c`, env `NOTION_DB_SOCIAL_INTEL`) via `execution/notion_api.py` (pins `Notion-Version: 2022-06-28` — never the JS client).

```bash
python3 execution/ad_spy.py ingest --brand "<Brand>" --file <ads.json> --batch "ad-spy-$(date +%Y-%m-%d)-<brand-slug>" --top 5
```

Property mapping (existing schema, no new properties needed):
- `Name` (title) — `"<Brand> — <headline> (<N>d, #<rank>)"`
- `Platform` (select) — `Ad Library`
- `Type` (select) — `Static Ad` / `Video Ad`
- `Running Since` (date) — the observed start date
- `Scraped` (date) — today
- `Creator` (rich_text) — brand name
- `Hook` (rich_text) — headline
- `Post URL` (url) — the Library ID permalink (dedup key — re-running the same brand skips exact URL matches already in the DB)
- `Analysis` (rich_text, ≤2000 chars) + full breakdown in the page **body** as blocks (long text never truncated silently — `ad_spy.py` writes platforms/runtime/CTA/body-copy/analysis into `heading2`/`para` body blocks per `notion_api.py`'s 2000-char-per-run chunking)
- `Batch` (rich_text) — the batch tag, so `ad_spy.py verify --batch <tag>` can query results back
- `Extract Candidate` (checkbox) — auto-checked on the #1 longest-running ad only, as a signal (not a claim about performance data we don't have) to route it toward Step 5

**Verify before trusting the run**: `python3 execution/ad_spy.py verify --batch <tag>` — queries Notion back and prints what actually landed. Never report a page count from the ingest log alone.

## Step 4 — Analysis Pass (per ad)

For each ranked ad, write a short "why it survived" breakdown into `analysis`, grounded only in what was observed:
- **Offer**: what's actually being sold/promised in the copy (not inferred beyond the text)
- **Hook**: the specific opening line/frame and why it likely stops the scroll
- **Mechanism/proof**: any specificity, numbers, testimonial, or claim used to earn belief
- **CTA**: what action it asks for and how hard/soft the ask is
- **Why it likely survived**: tie back to runtime — is it evergreen (broad appeal, low creative fatigue) or seasonal-but-repeated (same angle relaunched)? Flag this as an inference, not observed fact — Meta doesn't expose *why* an ad keeps running, only *that* it does.

## Step 5 — Handoff (Options, Never Pipeline Steps)

Per `feedback_no-forced-wiring-hubs-compose-freely.md` — these are things to consider next, not automatic next steps:
- **`/dara-static-engine`** — feed the winning ad's offer/hook/mechanism as creative-strategy input for a new static-ad build in the same space, not a copy of the competitor's ad.
- **Fantastic Studio** (`/fantastic-studio`, `skills/fantastic-posters/`) — if the winning ad is visual-led, use it as reference grounding for `fantastic-reference-ground` before generating original creative (cost-gated per `directives/fal-usage-policy.md`; never hand a bare prompt to a generator).
- **`/competitor-intel`** — if the ad-spy pull surfaces a broader positioning question (not just a single winning creative), escalate to the full competitor-intelligence system.

## Cost Notes

| Route | Cost | When |
|---|---|---|
| Meta Ad Library via Playwright (PRIMARY) | $0 | Always try first — public, no login, no rate-limit wall observed for read-only browsing at reasonable pace |
| Apify fallback | ~$0.25/run ceiling (per `directives/apify-usage-policy.md`, `$29/mo` plan) | Only if Playwright is blocked/unavailable. **Not currently wired**: no facebook/meta-ads actor exists in `execution/apify_client.py`'s `ACTORS` dict as of this build. A candidate is `curious_coder/facebook-ads-library-scraper` (unverified pricing/availability — check Apify Store before adding). To use it: add an entry to `ACTORS` in `execution/apify_client.py` with `pricing: "per_result"` and a conservative `cost_per_result`, then call `run_actor("meta-ads", {...}, max_results=N, max_cost=0.25)`. Do not run this untested actor without Farrice's go-ahead given the ACTORS-dict gap — the cost-gate hook only guards actors already registered. |

Extractions of this kind are ungated per CLAUDE.md (`/extract` family is never gated) — but this is a research/intel workflow, not an extraction, so it doesn't inherit that exemption; the table above is the actual gate.

## Known Limits (Honest, Not Hedged)

- No engagement metrics (views/likes/comments/spend) — Ad Library doesn't expose them for commercial ads. Runtime is the only free performance proxy; treat "why it's winning" analysis as inference from copy, not measured data.
- No language filter param — `country=US` is a proxy, not a guarantee; spot-check results.
- Shared Playwright browser profile (`mcp-chrome-86fe5ea`) is a **single-instance lock** — if another Claude Code session on the same machine is holding it, `browser_navigate` fails with "Browser is already in use." Retry after a short wait; if persistently locked, report it rather than fabricating data from memory/training.
- Carousel ads: captured as `Static Ad` with a body-text note; no dedicated Notion `Type` for carousels yet.
