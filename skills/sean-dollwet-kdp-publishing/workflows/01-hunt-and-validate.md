---
name: hunt-and-validate
description: Sean Dollwet's demand-first niche hunt. Sources topic candidates three ways, runs the BSR gate against live Amazon data, scans for the soft underbelly, and issues an evidence-backed GO/NO-GO verdict per topic BEFORE a word is written.
produces: GO/NO-GO demand verdict per topic with BSR evidence, attack-surface map, and content-pyramid placement
expert: Sean Dollwet
load_context: genius.md
---

# Hunt & Validate — the GO/NO-GO Demand Verdict

## Pre-Flight Gate

Run this FIRST, before any book idea, title, or outline exists. This is the inversion the whole doctrine rests on: "most people write the book first and hunt for buyers after" — you find proof buyers already exist, then build. (genius.md Patterns 1–3.)

Run this when:
- The user has a topic hunch, a hobby list, or a blank slate and wants to know what to publish.
- An existing book has stalled and you need to diagnose whether the TOPIC failed proof-of-concept (Pattern 2 red flag) vs. the book being weak.

Do NOT proceed to blueprint/production until a topic clears the BSR gate. Anti-patterns this kills (genius.md kill list): **write-first-validate-never**, following passion blind to demand, gambling on an unproven concept swap ("holiday learning picture book" when the market buys "Christmas story books"). If the user insists on an unvalidated pet topic, surface the anti-pattern in one line and offer to validate the nearest proven adjacent keyword.

## Skill Acquisition

Load before executing:
- `genius.md` — Patterns 1 (BSR gate), 2 (it's-not-the-topic-it's-the-book), 3 (copy demand / one-problem-one-audience), 8 (content pyramid + AI arbitrage), 11 (soft underbelly); Hidden Knowledge 7 (tool attribution), 11 (26-review signal), 13 ($300–400/mo median); Exemplars A (Money Tree A/B) and E (decluttering walkthrough); Quality Rubric items 1, 2, 9, 10.
- `references/window-thesis.md` — the soft-underbelly filter (two entry doors) and niche-dependent price ceilings.
- `references/prompt-chain.md` — Prompt 1 (the 50-topic brainstorm) and its "validate on Amazon, not in the model" human-judgment step.
- `references/price-sheet.md` — the 80,000 BSR ≈ $500/mo benchmark and the live royalty examples.

## Execution

### Step 1 — Source candidates (the trifecta)
Generate a wide candidate pool from three feeds, then dedupe:
1. **Brain dump.** Pull the user's interests, hobbies, and lived experience. The bar is low: you only need to know more than the reader, not more than everyone. Capture 10–20 raw threads.
2. **Amazon best-seller category browsing.** Walk Amazon → Books → Best Sellers by category and sub-category. Read what is *actually* selling right now; note recurring topics and sub-niches. This is market observation, not invention.
3. **AI 50-topic prompt.** Run Prompt 1 verbatim from `references/prompt-chain.md`: `Give me 50 profitable book topics I can write about for my Amazon KDP business.` Expect returns like "intermittent fasting for women over 40, air fryer, sourdough baking, anxiety workbook, ADHD productivity… how to stop overthinking."

Then narrow each survivor to the exact phrase a buyer would type. "Weight loss" → "intermittent fasting for women over 50." One problem, one audience (Pattern 3). Do NOT copy authority-figure/celebrity listings — they break every rule and still sell; you can't play their game.

### Step 2 — Run the BSR gate (the hard gate)
For each narrowed keyword, validate on Amazon, not in the model:
- Amazon → set category to **Books** → search the keyword → research in the **Paperback** format specifically.
- Read Best Sellers Rank inline. Tool lanes (time-or-money, Hidden Knowledge 7):
  - **Free:** DS Amazon Quick View (Chrome plugin) shows BSR + ASIN on the search grid, no tab-opening.
  - **Paid:** BookBeam (converts BSR → estimated royalties/catalog revenue) or KDSPY (a catalog's total monthly revenue). Note: on-screen numbers in Dollwet's own frames are often his Royalty Hero overlay's estimates.
- **The gate:** require **3+ distinct books from different authors below 80,000 BSR** on page one. One selling book is a fluke; three sub-80k books is a *pattern*. Benchmark: 80,000 BSR ≈ **$500/month** per format. Live confirmations from the source: BSR 189, 312, #1,013 — "way below 80,000… selling extremely well."
- The BSR cliff is real (Exemplar E): "Nobody Wants Your Sh*t" #4,016 ≈ **$282/day** and "Decluttering at the Speed of Life" #1,131 Audible ≈ **$545/day** sell hard, while "Declutter Without Losing Your Mind" #906,820 ≈ **$0/day** is dead. Cluster of sub-80k = proven. No cluster = kill the topic, pick another candidate.

### Step 3 — Read the bonus + underbelly signals
On a topic that clears the gate, grade the opening:
- **Low-reviews-on-page-one bonus (Hidden Knowledge 11).** Low review counts among ranked books = low ranking-friction; you won't need a big review pile to break in. Concrete signal: a book with only **26 reviews** sitting below 80,000 BSR is a green flag, not a warning.
- **Soft-underbelly scan (Pattern 11 / window-thesis two doors).** For each page-one incumbent, name a specific weak spot: **Door A —** top books under **300 reviews** ("the easiest target you can find"); **Door B —** obsolescence: outdated covers, generic titles, or content untouched in years. Even a 3,000-review book cracks "if the cover looks like it was designed in 2002, the title is super generic and the content hasn't been refreshed in years."
- **It's-not-the-topic-it's-the-book discrimination (Pattern 2).** Poor sellers inside a validated niche are a *green flag* — demand exists, competition is weak. Attribute their failure to cover / reviews / title, then plan to out-execute those exact weaknesses. Don't mistake ugly incumbents for dead demand.

### Step 4 — Fire the red-flag check
Before issuing GO, run the ranking-without-sales inversion (Pattern 2 corollary): search the topic's main keyword. If a book (or the user's own existing book) ranks **#1–2 for its own keyword and still isn't selling**, that is NOT a win — nobody searches or buys that concept. The topic failed proof-of-concept. Reposition to a proven adjacent keyword; never pour marketing at dead demand. Being first in an empty niche is usually *why* the niche was empty.

### Step 5 — Place on the content pyramid
Classify each GO topic (Pattern 8): **low-content** (journals/planners — easiest to make, most competition, least money), **medium-content** (coloring/activity), **high-content** (nonfiction/fiction — hardest, fewest competitors, most money). Default recommendation: **high-content**, because AI now erases its *creation* difficulty while leaving its *competition* moat intact — "the opportunity right now with high-content books is better than ever," and only high-content unlocks the audiobook stream.

### Step 6 — Issue the verdict
GO / NO-GO / CONDITIONAL per topic, each backed by the actual BSR evidence. Anchor expectations to the honest median: **$300–$400 per published book per month** (Hidden Knowledge 13) — never lead with the outlier income.

## Content Type Adaptations

| Content type | BSR gate | Signal weighting | Spec/positioning note |
|---|---|---|---|
| **High-content nonfiction** | 3+ paperback books <80k BSR; audiobook stream is a plus | Underbelly Door B (stale content) is the sharpest lever; AI arbitrage strongest here | Default recommendation; thin competition is the moat |
| **Low-content journals** | 3+ <80k, but expect crowding; demand the extra edge | Door A (low reviews) rarely available — market is saturated; lean on design/trend | Least money per Pattern 8; only if a clear underbelly exists |
| **Medium-content coloring/activity** | 3+ <80k; check price ceiling (coloring ~$9.99) | Aesthetic obsolescence (Door B) common — model page-one winners' trend | Model the trim; benchmark brand = Coco Wyo kawaii "Bold-Easy" |
| **Sprint vs standard** | Same gate regardless of eventual word count | N/A at validation | Word-count decision deferred to workflow 02 |

## Output Requirements

Deliver a **demand-validation report** containing:
- **Verdict table:** topic | verbatim target keyword | GO/NO-GO/CONDITIONAL | evidence (3+ competitor books with ASIN/BSR/author, paperback).
- **Per GO topic:** the BSR-cliff proof (winners vs. corpses), low-review bonus flag if present, an **attack-surface map** naming each incumbent's specific weak spot (review count / cover date / generic title / stale content), the ranking-without-sales check result, and content-pyramid placement.
- **Recommended #1 topic** with the reasoning trail and the honest $300–400/mo/book anchor.
- **Data gaps flagged honestly** — where BSR data wasn't retrievable, say so; never fabricate a rank, revenue figure, or search count.

`Execution prompt: references/prompts-v2/demand-validation-report.md`

## Quality Gate (pass/fail — references genius.md Rubric + anti-patterns)

- [ ] Every GO verdict cites **3+ real competitor books under 80,000 BSR** in **paperback**, with ASIN/BSR/author (Rubric 1). No evidence = fail.
- [ ] Thresholds are numeric and correct: 80k BSR ≈ $500/mo, <300 reviews, the 26-review bonus, $300–400/mo median (Rubric 2).
- [ ] The **ranking-without-sales** red flag was explicitly checked for any sparse-competition concept (Pattern 2).
- [ ] Each GO topic names ONE problem for ONE audience — no "everything for everyone" (Rubric 10).
- [ ] Each incumbent has a **named attack surface** (Rubric 9); ugly-but-selling niches are read as green flags, not kills.
- [ ] Content-pyramid placement stated, with high-content defaulted unless a specific reason overrides.
- [ ] Zero fabricated BSR/revenue/search numbers; honest median anchored, no outlier-income lead.
