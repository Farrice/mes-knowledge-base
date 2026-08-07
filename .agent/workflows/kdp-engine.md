---
description: "Front door for Amazon KDP and AI ebooks without slop — conduct a first pen-name nonfiction book from zero through market research, editorial, cover, policy, organic launch, and honest proof; or route an existing book to the right Sean Dollwet stage."
---

# KDP Engine (Sean Dollwet)

Front door for the whole KDP publishing system. For a first book, it starts the persistent Book One conductor. For an existing book, it dispatches only the stage that matches the operator's current evidence.

## Load First

```
Read: skills/sean-dollwet-kdp-publishing/SKILL.md
Read: skills/sean-dollwet-kdp-publishing/references/kdp-policy-and-evidence-boundary.md
```

## The Doctrine (5 lines)

1. **Demand before drafting.** Use current, dated marketplace evidence and reader-problem language; no single rank threshold proves a market.
2. **One world-class book before a factory.** Approve the niche, outline, gold chapter, cover, and upload separately.
3. **Official policy outranks creator tactics.** Rights, AI disclosure, metadata, review integrity, formats, Previewer, and Select compatibility are gates.
4. **Pace never lowers quality.** Day 7 may escalate to Day 14; Day 14 may remain open through Day 30.
5. **Proof stays separated.** `DRAFTED`, `LIVE`, `SOLD`, and `NET_COLLECTED` are different events. Revenue claims remain `UNTESTED` until receipts exist.

## Usage

```
/kdp-engine [where you are: a topic hunch, a stalled book, a proven book, "scaling", or "beat this niche"]
```

## Pipeline Router

Match the operator's state, load the workflow, run it, gate it. Each route: what it needs in / what comes back.

- **First book / blank slate / AI ebook without slop / no ads** → **workflow 00** `book-one-pilot`, which conducts 01 → 04 with a persistent cockpit, approvals, and compliance gates.
- **New niche inside an existing operation** → **workflow 01 → 02 → 03 → 04**, in order.
  - `01-hunt-and-validate` — in: topic candidates or interests. out: dated GO/HOLD/NO-GO verdict with multiple demand signals and attack-surface map.
  - `02-book-blueprint` — in: a GO topic. out: outline (competitor-TOC + review-mining), engineered title/subtitle, spec, cover direction.
  - `03-produce-manuscript` — in: the approved blueprint and gold-chapter standard. out: sourced, human-authored, AI-disclosed, reader-tested manuscript package.
  - `04-launch-90` — in: an approved live book. out: policy-safe organic experiments and 90-day observation plan; no paid ads in Book One.
- **Stalled book (published, not selling)** → **workflow 05** `book-doctor` — in: the live listing + any ads data. out: diagnosis against the 8-mistake checklist + out-product audit + fix-or-reposition verdict (is it the topic or the book?).
- **Proven book (converting, wants more)** → **workflow 06 and/or 08**.
  - `06-organic-engine` — in: a proven book. out: a 7-type TikTok content plan (1-page=1-video, clone-the-winner, repurpose waterfall).
  - `08-multiply-formats` — in: a proven book. out: format roadmap (paperback → audiobook ACX → translations → bundles → wide).
- **Scaling (multiple books, wants a real business)** → **workflow 09** `portfolio-command` — in: all live books. out: portfolio state board (per-book P&L) + next-quarter allocation (scale / multiply / retire / plant a new flag) + exit-readiness scorecard.
- **Competitive / premium niche (out-produce the best book)** → **layer workflow 10** `surpass-stack` on top of 02/03 — in: a competitive-niche book + the operator's own skill arsenal. out: a per-stage plan of OPTIONAL cross-skill handoffs (avatar / copy / ghostwriting / cover / content-psychology). These are options the operator picks, never mandatory steps.

Supporting desk, callable from any route: **workflow 07** `outsource-desk` — the time-or-money matrix + vendor briefs with real prices for any step the operator wants to buy instead of DIY.

## First Mission — the cold niche-hunt (Book One pilot)

For an operator starting from zero, run `00-book-one-pilot`. Initialize the cockpit, complete the deep interview, exclude unreviewed high-stakes lanes, and scan 5–10 current topics. Record marketplace, format, date, query, visible competitor evidence, reader-problem corroboration, uncertainty, and source paths. Recommend one topic, but do not draft until the niche checkpoint is approved. Income remains `NO EVENT` and `UNTESTED`.

## Related

Skill: `skills/sean-dollwet-kdp-publishing/` (SKILL.md · policy boundary · Book One conductor · 10 stage workflows)
Optional cross-skill stack (workflow 10): `/avatar-machine` · `/copy-engine` · `nicolas-cole` · `/fantastic-posters` · `kallaway`
