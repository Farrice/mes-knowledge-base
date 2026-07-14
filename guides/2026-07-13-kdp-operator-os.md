---
date: 2026-07-13
session: kdp-operator-os
tier: operator-guide
status: enriched
---

# KDP Operator OS — What We Built 2026-07-13 and How to Use It

> Today's forge session took `sean-dollwet-kdp-publishing` from a v2 chat-export skill (3 workflows) to a v3.0 mastery-tier system: 10 workflows across 3 tiers, a 22-pattern genius file, 4 frame-verified references, 7 execution prompts, and a `/kdp-engine` front door — extracted by 5 parallel agents from 5 WATCHED videos (transcripts + 488 frames, every number frame-verified). The business goal it serves: $3–5k/mo in publishing revenue, which at the honest median of $300–400/mo per book means a portfolio of 8–12 books. Skill: `skills/sean-dollwet-kdp-publishing/` · pilot handoff: `.agent/handoffs/2026-07-13-kdp-book-one-pilot.md`.

---

## The mental model (read this once, everything else follows)

Four ideas run through all ten workflows:

1. **Demand before creation.** Never write first. A topic earns a book only when 3+ books from different authors sit under 80,000 BSR on page one (paperback) — one selling book is a fluke, three is a pattern. 80k BSR ≈ $500/month per format. The inversion is the whole doctrine: most people write the book and hunt for buyers after; you find proof buyers already exist, then build a better book on the proven topic.
2. **Quality is the moat; reviews close the door.** AI gives you the quality, speed gives you the reviews. Enter a weak niche with both — a book that out-executes incumbents on cover/title/content, plus a sprint to 50–100 honest reviews in 90 days — and there's no weak spot left to attack. The door closes behind you.
3. **Time-or-money at every step.** Every production step has a DIY-free lane and a priced outsource lane ($10–20 cover, $50–100 formatting, $1–2k ghostwriter, ~$200 ACX narration). Pick deliberately; never pretend organic is a free lunch — it costs time instead.
4. **$1,000/mo is the learning milestone; the rest is duplication.** Master one book to $1k/mo, then rinse and repeat across 2–5 niches. $1k → $10k → $100k is the same validated unit copied, not new tactics at each rung. Anchor every expectation to the $300–400/mo/book median — no jackpot math.

---

## 1. `/kdp-engine` — the front door (state-based routing)

### What it is

A router, not a workflow. It loads the Dollwet spine (SKILL.md + genius.md), asks where you actually are in the pipeline, and dispatches to the matching workflow. It never duplicates workflow content — it points.

### When to reach for it

Any KDP intent, always. Topic hunch, stalled book, proven book, "scaling," or "beat this niche" — say the state and it routes.

### When NOT to

If you already know the exact workflow (e.g. "run the book doctor on X"), invoke it directly — the router adds nothing.

### How to invoke — copy-paste examples

```
/kdp-engine I have a topic hunch: sourdough for beginners
```
→ Routes to workflow 01, runs the BSR gate, returns a GO/NO-GO verdict with evidence.

```
/kdp-engine my book is published but not selling
```
→ Routes to workflow 05 (book-doctor): 8-mistake checklist, ads-data read, fix-or-reposition verdict.

```
/kdp-engine
```
→ Bare invocation on the current pilot: the first mission is the **cold niche-hunt** — workflow 01 across 5–10 candidate topics at once, ranked verdict table, ONE recommended GO.

---

## 2. The ten workflows, by tier

### Tier 1 — Foundation (01→04, the core pipeline, in order)

| # | Workflow | Produces |
|---|---|---|
| 01 | hunt-and-validate | GO/NO-GO demand verdict per topic — BSR gate, soft-underbelly scan, red-flag check |
| 02 | book-blueprint | Outline (competitor-TOC + review-mining), engineered title/subtitle, book spec, cover direction |
| 03 | produce-manuscript | The 5-prompt chain into a humanized, copyright-eligible manuscript |
| 04 | launch-90 | 30-day honeymoon plan → 15-review gate → pricing → $3–5/day diagnostic ads → 90-day sprint to 50–100 reviews |

**Reach for Tier 1** on any new book, blank slate to live listing. It IS the business; everything else feeds or multiplies it. **Not** when a book already exists — jumping to 02/03 with an unvalidated topic is the exact write-first anti-pattern the system kills.

Workflow 01 is the sharpest thing in the skill. The gate is physical: every GO must cite 3+ real competitor books under 80,000 BSR with ASIN/BSR/author, in paperback. Then it grades the opening — Door A: top books under 300 reviews ("the easiest target you can find"); Door B: dated covers, generic titles, content untouched in years. A 26-review book below 80k BSR is a green flag (low ranking-friction), and ugly incumbents in a validated niche mean demand exists and competition is weak — it's not the topic, it's the book. The red-flag inversion also fires before any GO: a book ranking #1–2 for its own keyword while not selling means no demand exists. Being first in an empty niche is usually why the niche was empty.

Worked example from the workflow itself, the BSR cliff: "Nobody Wants Your Sh*t" at #4,016 ≈ $282/day and "Decluttering at the Speed of Life" at #1,131 Audible ≈ $545/day sell hard, while "Declutter Without Losing Your Mind" at #906,820 ≈ $0/day is dead. Cluster of sub-80k = proven; no cluster = kill the topic.

Key Tier 1 numbers you'll use constantly: title = exact searched keyword + flair, subtitle stacks 3–4 concrete benefits (title is irreversible post-publish); book spec 30,000 words standard (10,000–15,000 acceptable for a first book), ship in ≤1 week max; AI drafts ONE subchapter (~1,250 words) at a time and a human humanizes — raw AI paste is uncopyrightable and degrades after chapter 2–3; launch pricing ebook $0.99 / paperback $5.99–$6.99; minimum 15 reviews before any marketing (hard gate); ads start at $3–5/day as a diagnostic (high impressions + low clicks = fix cover/title/reviews, not demand).

### Tier 2 — Practitioner (05–08: fix, feed, and multiply)

| # | Workflow | Reach for it when | Skip it when |
|---|---|---|---|
| 05 | book-doctor | Published book, not selling — is it the topic or the book? | The book was never validated (rerun 01 first) |
| 06 | organic-engine | Proven book, wants free traffic — 7-type TikTok plan, 1 page = 1 video, clone the winner 10× | Book unproven; volume content on a dead topic is wasted time |
| 07 | outsource-desk | You want to buy a step instead of DIY — vendor briefs with real prices | Budget-zero validation stage; the free lanes exist for a reason |
| 08 | multiply-formats | Proven book — paperback → audiobook (ACX ~$200 one-time, ~$3.40/sale) → translations → bundles → wide | Nothing proven yet; multiplying an unproven book multiplies zero |

Tier 2's shared law: **proven first, then feed.** 05 diagnoses, 06 and 08 pour fuel on something already converting, 07 is a supporting desk callable from any route.

### Tier 3 — Scaling (09–10: portfolio and out-producing)

**09 portfolio-command** — reach for it once multiple books are live: per-book P&L state board plus a next-quarter allocation plan (scale / multiply / retire / plant a new flag) and an exit-readiness scorecard. The endgame is equity: Dollwet sold his first catalog for $820,000 on Empire Flippers. Skip it with one book — there's no portfolio to command.

**10 surpass-stack** — the beat-the-market quality layer, and the workflow with the strongest guardrail in the whole skill: **every handoff is an OPTION the operator picks per book, never a mandatory step.** It maps your OWN arsenal onto the pipeline — `/avatar-machine` on reader profiling, `/copy-engine` on title/listing copy, `nicolas-cole` value architecture on the manuscript, `/fantastic-posters` on the cover, `kallaway` on TikTok hooks — each with a stated "earns its cost when / native is enough when." Reach for it on competitive or premium niches (Door B) and taste-bearing flagships. Do NOT run it on validation-stage sprint books, soft Door-A targets, or pre-proof operators — firing all five handoffs on a sprint book violates the one-week ceiling, and the workflow itself will route you back to the native pipeline. Its payoff line is the door-close pairing: stacked quality only becomes a moat when paired with the 90-day review sprint (workflow 04).

---

## 3. The 7 execution prompts (honor the Output Contracts)

Under `references/prompts-v2/` sit 7 structure-pure v2 prompts — demand-validation-report, book-production-package, book-doctor-report, launch-and-multiplication-plan, organic-content-pack, outsource-brief-pack, portfolio-command-sheet. Each carries a deterministic Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, the session Reads it and honors its contract instead of improvising the shape — the prompt-menu hook surfaces them automatically whenever the skill loads. Your part: nothing, except noticing when an output doesn't match its contract and saying so.

## 4. The 4 references — two you'll open by hand

- **`references/prompt-chain.md`** — the verbatim 5-prompt production chain (topics → pain points → outline → titles → draft → cover) plus the competitor-TOC/review-mining method. This is the actual production line; workflow 03 runs it.
- **`references/price-sheet.md`** — every frame-verified number in one page: the outsource matrix, royalty math, launch pricing, book spec, platform facts (Amazon holds ~74–78% of the market, KDP costs $0 to join, print-on-demand), portfolio and exit math, review economics (Book Bounty ~$25/mo verified vs Book Reverb ~$6 bid-based unverified — never family, never direct swaps).
- `references/window-thesis.md` — the 12–18-month timing case (barrier DOWN × demand UP × competition SHRINKING) and the soft-underbelly filter.
- `references/organic-taxonomy.md` — the 7-type TikTok taxonomy, faceless-beats-face, wound-accusation hooks.

## 5. The Book One pilot (queued and pinned)

The mission approved at Checkpoint 1: prove the v3.0 system on a real book. It's pinned on thread `kdp-engine` — `/resume` surfaces it by name, and `.agent/handoffs/2026-07-13-kdp-book-one-pilot.md` holds the sequence: cold niche-hunt across 5–10 candidates (sourcing trifecta: your interests + Amazon Best Sellers browsing + the 50-topic AI prompt) → best GO → blueprint → sprint-book manuscript (10–15k words, validation stage, native pipeline, surpass-stack optional) → launch-90.

**Start with:** `/kdp-engine`

One hard requirement: the hunt needs **LIVE Amazon BSR data** — DS Amazon Quick View browsing or a Playwright session. Workflow 01's quality gate bans fabricated ranks outright; where data isn't retrievable, the report says so.

## 6. One line on the router fix

Also shipped today: deliverable missions that invoke workflows by slash command ("run /extract-forge …") are no longer hijacked by the control-intent classifier into /autopilot or /system-audit — golden-set-guarded (24/24 green), card at `docs/solutions/2026-07-13-control-router-hijacks-deliverable-missions.md`.

## 7. Honest edges

- **A-tier is pending your verdict.** The blind pass was a model-judged PASS (EVAL-036, heartbeat 6/6); the tier holds at that until you judge the sample yourself: `.tmp/blind-pass-sample-launch-90.md` against the corpus at `extractions/sean-dollwet-kdp-publishing/reference-corpus/`.
- **No live-market run yet.** Every number is frame-verified against the source videos, but the system hasn't touched real Amazon data or shipped a real book. The Book One pilot is the proof; expect rough edges and `/extract-approach` whatever they teach.
- **The BSR gate is only as good as its data.** Amazon estimates on screen in the source frames are often Dollwet's own Royalty Hero overlay — the workflows know this and cite tool lanes, but treat any third-party revenue estimate as an estimate.
- **The medians are the promise.** $300–400/mo/book, 8–12 books to $3–5k/mo, no guarantees — the skill leads with that on purpose. If a session ever leads with outlier income, that's a quality-gate failure, not enthusiasm.

*Created 2026-07-13 (KDP Operator OS forge session). Extend this guide as the pilot ships — don't let it sediment.*
