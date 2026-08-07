---
name: book-doctor
description: Diagnose an underperforming KDP book by separating demand, discovery, listing, sample, content, policy, and economics defects using observed evidence rather than static rank or review rules.
produces: Evidence-backed defect diagnosis, cheapest-first test sequence, and reposition/repair/hold verdict
expert: Sean Dollwet
load_context: genius.md
---

# Book Doctor — Diagnose the Bottleneck You Can Prove

## Pre-Flight Gate

Run on a live or upload-ready book with evidence. Do not diagnose from rank alone, wait for a mythical algorithm window, or prescribe ads without permission. Load the listing, proof ledger, market dossier, claim/rights receipts, and current policy boundary.

## Execution

1. **Demand** — refresh the dated market scan and reader-problem evidence. A sparse query is ambiguous until corroborated.
2. **Discovery** — inspect query/indexing evidence, availability, categories, keywords, and any observable impressions.
3. **Click** — compare cover/title/subtitle/category fit at thumbnail and search-result level.
4. **Detail page** — inspect description, sample, metadata consistency, price, formats, and unsupported claims.
5. **Content** — review opening quality, promise delivery, factual support, repetition, formatting, accessibility, and reader feedback.
6. **Policy/rights** — check AI disclosure, licenses, trademarks, review plan, Select conflicts, and account notices.
7. **Economics** — separate gross royalty, costs, refunds, taxes, and net; do not use BSR-to-income estimates as receipts.
8. **Test** — choose the cheapest change that isolates the highest-confidence defect. Change one hypothesis at a time.

Issue one verdict: `REPOSITION`, `REPAIR`, `HOLD`, or `SCALE TEST`. A scale test requires observed profitable conversion and separate spend approval.

## Output Requirements

- Evidence inventory and missing data.
- Ranked defect list with observed signal and confidence.
- This-book versus relevant-incumbent comparison without copying.
- One-hypothesis test sequence, success metric, and stop rule.
- Verdict and next action.

`Execution prompt: references/prompts-v2/book-doctor-report.md`

## Quality Gate

- [ ] Every defect traces to observed evidence or is labeled a hypothesis.
- [ ] Demand, discovery, click, page, content, policy, and economics are separated.
- [ ] No static BSR, review count, price, or launch window is treated as universal.
- [ ] Rights and account notices can override conversion work.
- [ ] One variable changes per test.
- [ ] Spend and external actions require separate approval.
