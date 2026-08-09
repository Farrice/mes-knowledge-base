---
name: "Cost per Right Answer"
produces: "Error-adjusted research method ledger with deterministic, model, and human escalation routes"
expert: "Jordan Crawford — Evidence-First GTM Intelligence"
load_context: "genius.md"
tier: 2
---

# Cost per Right Answer

## Pre-Flight Gate

Define the exact question and what a wrong answer costs. Read `references/research-tool-contract.md` and separate `PRIVATE_CONTEXT` from the minimum `PUBLIC_QUERY`. Paid or quota-heavy tools require an approved cost gate. If answer correctness cannot be evaluated, redesign the question first.

## Skill Acquisition

Load patterns 13, 14, and 15. Separate finding from judging and price the whole answer: retrieval, model use, human review, false positives, false negatives, latency, and rework.

## Input Required

- Research question and decision it changes
- Required confidence/freshness
- Candidate data sources and methods
- Tool, labor, latency, and error estimates
- Known-good evaluation cases

## Execution

1. Rewrite the question as a testable answer contract.
2. Build a known-good/known-bad evaluation set.
3. Route in order: existing internal evidence -> free public/first-party retrieval -> `execution/research.py` for public-safe questions -> approved paid/quota actor -> model judgment -> human review.
4. Keep retrieval receipts and judgment rationales separate.
5. Estimate total cost per accepted correct answer, including review and downstream error.
6. Choose the lowest-cost method that clears the confidence requirement.
7. Attach a Research Receipt and define escalation, failure, freshness, and review triggers. Empty, blocked, or failed engines are `NO RESEARCH EVENT`.

## Content Type Adaptations

| Question type | Adaptation |
|---|---|
| Existence/fact | Deterministic source first |
| Relevance/fit | Retrieve evidence, then model/human judgment |
| Sensitive claim | Authoritative source plus human checkpoint |
| High-volume classification | Sample evaluation before scaling |

## Output Requirements

Question contract, privacy partition, method ladder, evaluation set, cost/error table, chosen route, Research Receipt, fallback, and review trigger. Use `references/prompts-v2/cost-per-right-answer.md`.

## Quality Gate

- Cost includes review and errors, not only API price.
- Finding and judging are separate and auditable.
- A known-good evaluation set exists.
- Paid tools are not invoked without approval.
- Private context is not disclosed to an unspecified provider.
- Failed retrieval is recorded and never replaced with model memory.
- The answer changes a named decision; otherwise research is rejected as decoration.
