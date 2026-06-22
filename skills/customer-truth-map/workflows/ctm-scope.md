---
description: Phase 1 (Steps 1–2) of the Customer Truth Map — narrow the customer, name 15–20 problems in their own voice tagged assumed vs evidenced, pick the 2–3 to research deeply, then build a sourced list of exactly where they talk with candor scores and a recommended capture tool per source.
---

# /ctm-scope — Narrow the Target & Map the Sources

Phase 1, Steps 1–2. Before a single quote is gathered, this workflow decides **who** the map is for (narrow enough to be useful), **which problems** are worth the dig, and **where** the customer actually talks in their own unprompted words. It produces the brief that `/ctm-gather` executes against — get this wrong and the whole map drifts. Uses enhanced prompts **P1** and **P2** from [../references/prompt-library.md](../references/prompt-library.md).

## Pre-Flight Gate

Load `../genius.md` if not hot. Answer before producing anything (Decision Framework, genius.md):

1. **One customer, one problem cluster?** Is the target narrow enough — the *"solo bookkeeper who just lost a big client"* test, not "small business owners"? The narrowest target makes the strongest map (genius.md, Hidden Knowledge). Serve several segments → build a separate map per customer; do not blur them into one.
2. **Do we already know this audience?** This is the non-negotiable first action below: front-load Recall + `memory_facade.py` so we build on what we hold and don't re-gather it.
3. **Unprompted over prompted?** The source list must prioritize where people talk when they *don't* feel observed (reviews, threads, DMs) over interview/survey answers — a survey question pre-decides the categories (genius.md, Core Thesis 4).

## Skill Acquisition

- **Always:** `../genius.md` (narrowness rule, unprompted>prompted, the honesty spine) + the two prompts: P1 (name the problems) and P2 (find where they talk) in [../references/prompt-library.md](../references/prompt-library.md).
- **Source-tool mapping:** [../references/tool-wiring.md](../references/tool-wiring.md) Layer 0 (grounding) + Layer 1 (the capture tools each source maps to) + the budget cheat-sheet.
- **Hands off to:** `./ctm-gather.md` (executes the source list).

## Execution

### Step 0 — Ground (REQUIRED first move, free)
We do not scrape what we may already hold. Run both before listing a single problem:
```bash
python3 execution/memory_facade.py "<customer + problem>" --top 10
```
Plus Recall: `mcp__recall__search { "query": "<customer + problem>" }` (and `get_document_content` on any strong hit). Report every store that was degraded or skipped — never silently drop one. Carry the returns into Step 1 as the grounding line for P1.

### Step 1 — Narrow the customer & name the problems (P1)
**Move.** Lock the target to the narrowest defensible definition, then have AI list **15–20 distinct problems, frustrations, or fears** the customer has, *"phrased the way the customer would say it to a friend, not in marketing language"* — then pick the 2–3 most worth researching deeply.

**Use enhanced P1:** prepend the grounding line — *"Here is what we already know about this customer (from memory + Recall): [paste Step-0 results]. Build on it, don't repeat it."* Require every item tagged **`[assumed]`** vs **`[evidenced: source]`**, so the list separates what we're guessing from what we've already heard.

**Diagnostic:** Is the target narrow enough to produce non-blurry patterns? Is each problem in the customer's voice, not marketing voice? Are evidenced items actually traced to a source, or quietly assumed?

**Worked thread — solo bookkeeper who just lost a big client** *(quotes below are `[illustrative]` structure only; real runs list the customer's actual phrasing, and only `[evidenced]` items carry a real harvested line):*
- `[evidenced: prior map / r/Bookkeeping]` *"I built my whole income on one client and now they're gone."* `[illustrative]`
- `[assumed]` *"I don't even know how to find new clients without feeling like a salesperson."*
- `[assumed]` *"What if the next one drops me too — am I always going to be this exposed?"*
- → **Picked for deep research:** client-concentration fear, the "how do I prospect without feeling pushy" friction. Depth on 2–3 beats a thin sweep (genius.md: *stop when the map stops surprising you*).

### Step 2 — Map exactly where they talk (P2)
**Move.** Have AI list the **specific** places this customer openly discusses these problems in their own words — subreddits, forums, Facebook groups, review sites, YouTube comment sections, niche communities — and, per source, what language/content to expect and how candid people are.

**Use enhanced P2:** require, for each source, **(a)** an exact URL/handle, **(b)** a candor score 1–5, **(c)** an *unprompted* (review/thread) vs *prompted* (Q&A/survey) flag, **(d)** the recommended capture tool from [../references/tool-wiring.md](../references/tool-wiring.md) (Apify reddit actor / NotebookLM / Playwright / WebFetch / manual). Then add our **own-data** sources — sales/discovery-call transcripts, support tickets/emails, DMs, reviews of your product *and competitors'* — because *"your past conversations are often the single best source"* (genius.md, Hidden Knowledge) and most people skip them.

**Diagnostic:** Are these specific places, not "the internet"? Is unprompted talk weighted above prompted? Is own-data on the list (it usually outranks Reddit)?

**Worked source table:**
| Source | URL/handle | Candor | Type | Capture tool |
|---|---|---|---|---|
| Own discovery-call transcripts | (files user provides) | 5 | unprompted | manual / Read |
| r/Bookkeeping | reddit.com/r/Bookkeeping | 4 | unprompted | Apify reddit actor |
| r/smallbusiness (losing-a-client threads) | reddit.com/r/smallbusiness | 4 | unprompted | Apify reddit actor / NotebookLM |
| Competitor software reviews (G2/Capterra) | g2.com/... | 3 | unprompted | WebFetch → Playwright if SPA |
| Bookkeeping Facebook groups | (login-gated) | 4 | unprompted | Playwright (read-only) / manual paste |

## Content-Type Adaptations

What "narrow" and "where they talk" look like by domain (full key: [../references/cross-domain-adaptations.md](../references/cross-domain-adaptations.md)):

| Domain | Narrowness move | Where they talk (unprompted) |
|---|---|---|
| **B2B SaaS** | one role + one trigger event (not "marketers" → "solo bookkeeper who just lost a big client") | competitor review sites, niche subreddits, role-specific Slack/Discord, your own sales calls |
| **Real estate / FTHB** | one buyer state ("first-time buyer scared of overpaying in the SFV") | r/FirstTimeHomeBuyer, local FB groups, agent DMs, listing-inquiry transcripts |
| **Consumer / DTC** | one occasion + one identity ("new parent buying their first stroller") | Amazon/retailer reviews, parenting forums, YouTube comments, support tickets |
| **Coaching / info-product** | one outcome at one stage ("invisible expert who can't articulate their value") | course-platform reviews, coaching subreddits, your DMs, discovery-call recordings |
| **Local service** | one job + one anxiety | Google/Yelp reviews, Nextdoor, neighborhood FB groups |

## Output Requirements

Return:
1. **Grounding receipt** — what memory + Recall already held about this customer; degraded/skipped stores reported.
2. **Narrowed customer definition** — one sentence, passing the bookkeeper sharpness test; a note if it had to be split into multiple maps.
3. **The problem list** — 15–20 problems in the customer's own voice, each tagged `[assumed]` or `[evidenced: source]`, with the **2–3 picked** for deep research flagged and a one-line reason.
4. **The source map** — the table above: each source with URL/handle, candor 1–5, unprompted/prompted flag, and recommended capture tool; own-data sources included and weighted.

This brief is the input to `./ctm-gather.md`.

## Quality Gate

Score against the `../genius.md` rubric (1–10; name the anchor for ≥8). The criteria this phase owns:
- **Narrowness** — target specific enough to produce non-blurry patterns; broad targets capped low.
- **Unprompted Sourcing** — source list weighted to unsolicited talk + own-data, not survey-shaped sources.
- **Verbatim Integrity (forward-looking)** — every `[evidenced]` tag is traced to a real source line; an `[evidenced]` tag with no traceable line is the same defect as a fabricated quote.

**Verbatim-Integrity veto.** Any problem presented as `[evidenced]` that is actually invented or paraphrased is an **automatic fail** — even at scoping, the honesty spine holds: real language only, or label it `[assumed]`. Real runs harvest verbatim quotes; this workflow never mints one to look more grounded.

**Self-check:** *Is the target narrow enough that one map serves it without blurring, and does every source point at where this customer talks unprompted?* If yes, hand to `/ctm-gather`. If no, re-narrow or re-source before gathering.
