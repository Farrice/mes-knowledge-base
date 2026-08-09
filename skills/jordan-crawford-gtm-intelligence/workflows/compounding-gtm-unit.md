---
name: "Compounding GTM Unit"
produces: "One reusable GTM unit with explicit input, output, evaluation, human decision, review trigger, and learning return"
expert: "Jordan Crawford — Evidence-First GTM Intelligence"
load_context: "genius.md"
tier: 3
---

# Compounding GTM Unit

## Pre-Flight Gate

Require at least three known-good manual examples and documented exceptions. Unitize one stable step only. External writes, enrichment spend, and irreversible actions remain outside the unit unless separately approved.

## Skill Acquisition

Load patterns 14 and 15 plus `references/cross-domain-patterns.md`. Retrieval, judgment, and action are separate units when their evaluation or authority differs.

## Input Required

- Manual step and why it matters
- Known-good and known-bad examples
- Input/output artifacts
- Evaluation rule and acceptable error
- Exceptions, privacy, authority, and review constraints

## Execution

1. Draw the current manual boundary and identify one repeatable transformation.
2. Specify typed inputs, required provenance, and missing-input behavior.
3. Specify output schema, evidence links, and forbidden outputs.
4. Define automated checks, sampled human review, and hard escalation triggers.
5. Separate find, judge, and act where their truth or permission models differ.
6. Define versioning, exception capture, and the learning return to the dossier.
7. Test against known-good, known-bad, missing-data, and adversarial cases before recommending automation.

## Content Type Adaptations

| Unit | Adaptation |
|---|---|
| Evidence retrieval | Deterministic receipts and freshness |
| Fit judgment | Evidence bundle + confidence + dissent |
| PVP generation | Proof constraints and receiver review |
| External action | Separate approval-gated executor; never implicit |

## Output Requirements

Unit charter, schemas, evaluation set, escalation logic, review cadence, authority boundary, and learning-return contract. Use `references/prompts-v2/compounding-gtm-unit.md`.

## Quality Gate

- The unit is smaller than the end-to-end workflow.
- Known-good, known-bad, missing, and edge cases exist.
- Missing evidence cannot become fabricated output.
- Human review and irreversible-action boundaries are explicit.
- Exceptions improve the shared truth base rather than disappearing.

