---
description: "Riley Brown's competitor ad-spy — rank rivals' ads by how long they've been running (the longest-running ad is the winning ad), analyze why each survived, labeled as inference from durability not ROAS proof. $0 via Meta Ad Library."
---

# /riley-ad-spy — Longest-Running-Ad Competitor Intel

Riley's heuristic (Pattern 6): "the one metric that we can use... as a proxy for [ROI] is how long they've been running it. If you run an ad for nine months... presumably they're spending a lot of money keeping it alive for a good reason." And his agent's own epistemic honesty, on screen: "'Why it works' is clearly labeled as an inference from creative durability — not proof of ROAS or profitability." His stack used Foreplay; ours gets the same signal at **$0** via the Meta Ad Library.

## Pre-Flight Gate

Load `genius.md` first. Proceed if:
- You have a real competitor/brand to spy on (name or Facebook Page).
- You accept the honest limit: **the Ad Library exposes no likes/views/spend/ROI for commercial ads** — runtime is the only free proxy. If the client demands measured performance data, this can't provide it (say so).
- Playwright browser profile is free (single-instance lock — if held by another session, retry or report; never fabricate from memory).

## Skill Acquisition

- `genius.md` — Pattern 6 (longest-running heuristic), Hidden Knowledge #9 (verification gap)
- `references/source-quotes.md` — Exemplar 2 spy prompt; claims ledger (durability ≠ proof)
- Live infra: `.agent/workflows/ad-spy.md` (the full read-only Playwright + `ad_spy.py` procedure)

## Execution

1. **Run `/ad-spy`** on the competitor set — Riley scraped "quad.ai perplexity and chatgpt and replet... top five video ads from each one and the top five static ads... videos in English only." Follow `.agent/workflows/ad-spy.md`: navigate the Ad Library `active_status=active` URL (Tier 1 read-only), snapshot the results grid, extract per card: **Started running on [date]**, Library ID (→ permalink dedup key), platforms, headline/hook, full body copy, CTA, media type.
2. **Rank by longevity.** `execution/ad_spy.py rank --file <ads.json>` computes `runtime_days` and `rank` deterministically — don't eyeball date math. The top of the list is the ad the advertiser has paid for longest; treat it as the strongest signal, not a curiosity.
3. **Ingest to the Social Intelligence DB** (`ad_spy.py ingest`, `Platform=Ad Library`, `Running Since=start date`). **Leave Views/Likes/Comments blank** — never invent a metric Meta doesn't expose. `Extract Candidate` auto-checks the #1 longest-running ad.
4. **Analysis pass (per ad), labeled as inference.** Write a short "why it survived" into `Analysis`: offer, hook, mechanism/proof, CTA, and *why it likely survived* — tie to runtime and **flag it as inference** ("evergreen broad appeal" vs. "seasonal angle relaunched"), never as measured fact. Riley's on-screen honesty is the standard.
5. **Mid-run escalation, Riley-style.** If the analysis needs cross-ad synthesis, "turn up soul... extra high"; a straight scrape stays cheap ("you do not need to use a good model for this").
6. **Verify.** `ad_spy.py verify --batch <tag>` queries Notion back — report what actually landed, never a count from the ingest log.

## Content Type Adaptations

| Ad type | Adaptation |
|---|---|
| Static image | capture headline + body + CTA; media URL best-effort from DOM |
| Video ad | note it's video; runtime + hook line + CTA are the extractable signal |
| Carousel | captured as `Static Ad` with a "carousel" note in Analysis (no dedicated Type) |
| Political/issue | not the use case — those *do* show spend/reach; commercial ads don't |

## Output Requirements

- Ads ranked by `runtime_days` (deterministic), top N in Notion with a batch tag.
- Every "why it works" labeled **inference from durability, not ROAS proof.**
- No fabricated engagement/spend numbers — blanks where Meta shows nothing.
- Verified via `ad_spy.py verify`; #1 marked `Extract Candidate`.

Execution prompt: references/prompts-v2/competitor-ad-intel-report.md — honor its Output Contract.

## Quality Gate

Ranking is runtime-based and script-computed (not eyeballed)? · Every verdict flagged as inference, never proof? · Zero invented metrics? · The honest gap (no likes/spend) stated, not hidden? · Handoff options offered (`/creative-from-winners`, `/dara-static-engine`), never forced as pipeline steps?
