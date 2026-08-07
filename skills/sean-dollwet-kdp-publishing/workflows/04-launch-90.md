---
name: launch-90
description: Prepare and run a policy-safe, organic-only Book One launch with current pricing, neutral optional review language, controlled content experiments, and a 90-day discovery-to-cash observation ledger.
produces: Upload-readiness receipt, organic launch experiment plan, review-integrity plan, pricing hypothesis, and 90-day measurement board
expert: Sean Dollwet
load_context: genius.md
---

# Launch 90 — Policy-Safe Organic Learning

## Pre-Flight Gate

Run after manuscript, cover, metadata, rights, AI disclosure, originality, claim, reader, format, and Previewer gates pass. The workflow may prepare upload assets, but it cannot publish without explicit upload permission.

Load `references/kdp-policy-and-evidence-boundary.md`, the Book One cockpit, compliance receipt, and `references/prompts-v2/launch-and-multiplication-plan.md`.

## Execution

### 1. Verify upload readiness

Confirm account readiness, rights, asset-level AI disclosure, metadata/cover/interior match, title length, categories/keywords, ebook format, print file if used, Kindle Previewer/link checks, pricing/royalty calculation, and KDP Select choice. Book One defaults to Select off.

Run `python3 execution/kdp_book_one.py preflight --project _active/publishing/kdp-book-one-pilot --json`. Stop at `READY_FOR_APPROVAL` until explicit upload permission exists.

### 2. Set a current pricing hypothesis

Use current KDP royalty/list-price rules, delivery/print costs, taxes, territory, category norms, perceived value, and the operator's zero-ad constraint. Record the initial hypothesis and what evidence would justify a change. Do not treat any creator price as universal.

### 3. Use only neutral review language

A reader may receive a free or discounted copy only with no required or influenced review. Invitations may say that feedback or an honest review is optional. Do not pay, award points, give gift cards, reciprocate, use close relationships, filter by positive sentiment, or require review proof.

### 4. Run organic experiments

Use workflow 06 to test audience-matched channels and formats. Each experiment names hypothesis, asset, channel, date, effort, reach signal, discovery evidence, attributed sale if any, and uncertainty. No ads in Book One.

### 5. Observe 90 days without algorithm claims

Track:

- Production: submitted and live timestamps.
- Market: listing discovered, sale, refund, and net collection events.
- Listing: availability, metadata issues, sample/preview, reader questions, and review integrity.
- Economics: gross royalty, costs, refunds, tax assumptions, and net cash.

Do not call the first 30 days a guaranteed boost or infer momentum from review count.

## Output Requirements

- Compliance and permission verdict.
- Pricing hypothesis and current rule source.
- Neutral review/feedback plan.
- Organic experiment backlog and attribution schema.
- 90-day observation board with production, market, and cash axes.
- Exact next checkpoint; no external action performed by the plan itself.

`Execution prompt: references/prompts-v2/launch-and-multiplication-plan.md`

## Quality Gate

- [ ] Upload assets pass current policy, rights, AI, metadata, format, and preview checks.
- [ ] No publication occurs without explicit permission.
- [ ] Review language is optional, uninfluenced, uncompensated, nonreciprocal, and not sentiment-filtered.
- [ ] Book One remains organic-only and Select-off unless separately approved.
- [ ] Pricing uses current platform economics and is labeled a hypothesis.
- [ ] No fixed review threshold or algorithm boost is asserted.
- [ ] Discovery, sale, refund, and net collection are recorded as separate events.
