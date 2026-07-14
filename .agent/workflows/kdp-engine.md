---
description: "Front door for Amazon KDP publishing (Sean Dollwet) — validate demand before creating, then route to the right pipeline stage: hunt → blueprint → produce → launch → doctor → multiply → portfolio → surpass."
---

# KDP Engine (Sean Dollwet)

Front door for the whole KDP publishing system. Loads the Dollwet spine, then dispatches to the skill workflow that matches where the operator actually is. This is a ROUTER — it does not duplicate workflow content; it points.

## Load First

```
Read: skills/sean-dollwet-kdp-publishing/SKILL.md   (the 10-workflow map + Quick Reference)
Read: skills/sean-dollwet-kdp-publishing/genius.md   (22 patterns, 13 hidden-knowledge items, exemplars, rubric)
```

## The Doctrine (5 lines)

1. **Demand before creation.** Never write first. Find 3+ books under 80,000 BSR on the topic, then build — proof buyers exist beats hoping they do.
2. **Quality is the moat; reviews close the door.** AI gives the quality, speed gives the reviews — enter with both and the door closes behind you before later entrants can dislodge you.
3. **Time-or-money at every step.** Every production choice is a stated trade: DIY to save money, outsource to save time. Never sell organic as a free lunch.
4. **$1,000/mo is the learning milestone; the rest is duplication.** $1k → $10k → $100k is one validated unit rinsed and repeated across 2–5 niches — not new tactics at each rung.
5. **Honest expectations.** $300–400/mo median per book, no guarantees. A $3–5k/mo business is 8–12 books, not one jackpot.

## Usage

```
/kdp-engine [where you are: a topic hunch, a stalled book, a proven book, "scaling", or "beat this niche"]
```

## Pipeline Router

Match the operator's state, load the workflow, run it, gate it. Each route: what it needs in / what comes back.

- **New niche / blank slate / topic hunch** → **workflow 01 → 02 → 03 → 04**, in order.
  - `01-hunt-and-validate` — in: topic candidates or interests. out: GO/NO-GO verdict per topic with BSR evidence + attack-surface map.
  - `02-book-blueprint` — in: a GO topic. out: outline (competitor-TOC + review-mining), engineered title/subtitle, spec, cover direction.
  - `03-produce-manuscript` — in: the blueprint. out: a humanized, copyright-eligible manuscript (5-prompt chain + generate→humanize loop).
  - `04-launch-90` — in: a finished, uploaded book. out: 30-day honeymoon plan → 15-review gate → pricing → $3–5/day diagnostic ads → 90-day sprint to 50–100 reviews.
- **Stalled book (published, not selling)** → **workflow 05** `book-doctor` — in: the live listing + any ads data. out: diagnosis against the 8-mistake checklist + out-product audit + fix-or-reposition verdict (is it the topic or the book?).
- **Proven book (converting, wants more)** → **workflow 06 and/or 08**.
  - `06-organic-engine` — in: a proven book. out: a 7-type TikTok content plan (1-page=1-video, clone-the-winner, repurpose waterfall).
  - `08-multiply-formats` — in: a proven book. out: format roadmap (paperback → audiobook ACX → translations → bundles → wide).
- **Scaling (multiple books, wants a real business)** → **workflow 09** `portfolio-command` — in: all live books. out: portfolio state board (per-book P&L) + next-quarter allocation (scale / multiply / retire / plant a new flag) + exit-readiness scorecard.
- **Competitive / premium niche (out-produce the best book)** → **layer workflow 10** `surpass-stack` on top of 02/03 — in: a competitive-niche book + the operator's own skill arsenal. out: a per-stage plan of OPTIONAL cross-skill handoffs (avatar / copy / ghostwriting / cover / content-psychology). These are options the operator picks, never mandatory steps.

Supporting desk, callable from any route: **workflow 07** `outsource-desk` — the time-or-money matrix + vendor briefs with real prices for any step the operator wants to buy instead of DIY.

## First Mission — the cold niche-hunt (Book One pilot)

For an operator starting from zero (the stated Book One pilot): don't validate a single pet topic — **run `01-hunt-and-validate` across 5–10 candidate topics at once** and pick the best GO. Sourcing trifecta (workflow 01): the operator's own interests/experience + Amazon Best Sellers category browsing + the AI 50-topic prompt. Then run the BSR gate on each, scan the soft underbelly (Door A: <300 reviews; Door B: dated covers/generic titles/stale content), and hand back a ranked verdict table with ONE recommended topic and its evidence trail. That GO becomes the input to workflow 02. Anchor expectations to $300–400/mo/book, no guarantees.

## Related

Skill: `skills/sean-dollwet-kdp-publishing/` (SKILL.md · genius.md · references/{window-thesis, prompt-chain, price-sheet, organic-taxonomy}.md · 10 workflows)
Optional cross-skill stack (workflow 10): `/avatar-machine` · `/copy-engine` · `nicolas-cole` · `/fantastic-posters` · `kallaway`
