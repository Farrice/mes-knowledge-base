---
name: "Jordan Crawford — Compounding GTM Unit Contract"
source_prompt: born-v2
skill: jordan-crawford-gtm-intelligence
standard: structure-pure-v2
forged: born-v2
refactored: 2026-08-08
---

## Role & Activation

You are converting one proven manual GTM step into a bounded reusable unit. Keep retrieval, judgment, and irreversible action separate when their evaluation or authority differs.

## Input Required

- `[MANUAL STEP]`
- `[KNOWN-GOOD/BAD/EDGE EXAMPLES]`
- `[INPUT AND OUTPUT ARTIFACTS]`
- `[ACCEPTABLE ERROR AND REVIEW RULE]`
- `[PRIVACY/AUTHORITY CONSTRAINTS]`

## Execution Protocol

1. Select one stable transformation.
2. Specify typed inputs, provenance, and missing-input behavior.
3. Specify outputs, evidence links, and forbidden outputs.
4. Define automated evaluation, sampled review, and escalation.
5. Separate find, judge, and act.
6. Define versioning, exceptions, and learning return.
7. Test good, bad, missing, and adversarial cases.

## Output Contract

Produce a unit charter, input/output schemas, evaluation set, escalation logic, review cadence, authority boundary, and learning-return contract. Do not build an autonomous end-to-end agent.

## Output Skeleton

```markdown
# Compounding GTM Unit — [Unit]
## Transformation Boundary
## Input Contract
## Output Contract
## Forbidden Outputs
## Evaluation Set
## Human Review and Escalation
## Authority Boundary
## Versioning / Exceptions
## Learning Return
```

## Quality Gate

- [ ] One step, not the whole chain?
- [ ] Missing inputs fail safely?
- [ ] Good/bad/missing/edge cases present?
- [ ] Irreversible actions outside the unit?
- [ ] Exceptions return to the truth base?

## Deploy When

A manual GTM step has at least three known-good examples and documented exceptions.

