---
name: multiply-formats
description: Evaluate print, audio, translation, bundle, and wide-distribution experiments only after observed Book One sales and net collection, with rights, quality, economics, and KDP Select compatibility gates.
produces: Proof-gated per-format experiment roadmap with economics, rights, quality, and distribution decisions
expert: Sean Dollwet
load_context: genius.md
---

# Multiply Formats — Distribution Surfaces After Proof

## Pre-Flight Gate

Run only after Book One records `SOLD` and `NET_COLLECTED`, with refund/cost context. A format is not an income stream before it earns. If these events do not exist, return `HOLD` and continue Book One learning.

## Execution

Evaluate each surface separately:

- **Paperback/hardcover** — print file, wrap geometry, proof copy, print cost, list price, rights, and reader need.
- **Audiobook** — narration rights, script adaptation, sample approval, production cost, distribution terms, and payback hypothesis.
- **Translation** — translator rights, native editorial review, cultural/claim accuracy, market demand, metadata, and disclosure.
- **Bundle** — reader coherence, duplicate-content risk, rights, and incremental value.
- **Wide distribution/direct download** — channel demand, support load, files, pricing, and KDP Select exclusivity conflict.

For each, record current cost evidence, expected range as `UNTESTED`, success metric, loss limit, and kill/continue rule. Select enrollment is never automatic.

## Output Requirements

- Book One proof receipt.
- Per-format `GO/HOLD/NO-GO` table.
- Rights, quality, economics, and Select compatibility per format.
- One recommended next experiment, budget/permission gate, and stop rule.

`Execution prompt: references/prompts-v2/launch-and-multiplication-plan.md`

## Quality Gate

- [ ] `SOLD` and `NET_COLLECTED` evidence exists.
- [ ] Every format has new rights and quality checks.
- [ ] Current costs are sourced; projections remain untested.
- [ ] KDP Select compatibility is explicit.
- [ ] Only one next-format hypothesis is recommended.
- [ ] Spend, distribution, and external actions wait for approval.
