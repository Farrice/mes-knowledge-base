---
description: Conduct the complete evidence-to-blueprint-to-draft-review fashion PDP rebuild while preserving approval, source, and live-theme boundaries.
---

# Workflow 07 — Fashion PDP Rebuild System

This is the front door for an AI-assisted Shopify apparel PDP rebuild. **BitBranding is the single owner.** The workflow composes Workflow 05 and Workflow 06 without collapsing their human checkpoint.

## Phase 0 — Fit and intent lock

Confirm Shopify + fashion fit, target product/template, current theme, business goal, customer problem, and whether the user wants planning only or an authorized draft-theme build. Route positioning gaps to Oren and voice gaps to the approved voice source, then return; do not create an expert stack by default.

## Phase 1 — Blueprint

Run `05-fashion-pdp-blueprint.md` and its v2 prompt. Deliver the evidence status, missing-facts questions, objection ledger, and module blueprint.

**Hard phase boundary:** wait for facts and human blueprint approval before implementation. If no external-write permission exists, continue only far enough to produce a connector-ready packet.

## Phase 2 — Draft build and review

Run `06-claude-pdp-build-loop.md` and its v2 prompt. Lock the duplicated draft target, re-read current state, produce or apply the smallest delta, inspect the rendered result, and repair from current state.

## Phase 3 — Proof and handoff

Return one run receipt:

- Source and evidence state.
- Blueprint approval state.
- External-write permission state.
- Draft theme target and rollback state.
- Applied and unapplied deltas.
- PASS/FAIL/PARTIAL/UNTESTED QA evidence.
- Publication state.
- Experiment plan and business outcomes still unproven.

## Output Schema

```markdown
# Fashion PDP Rebuild Run: [Product]
## Intent & Scope Lock
## Blueprint State
## Human Approval State
## Build State
## Defects & Repairs
## QA & Rollback
## Permission & Publication
## Business Proof
## Next Safe Action
```

## Stop conditions

Stop for missing material facts, absent blueprint approval, absent connector-write permission, ambiguous theme target, live-theme targeting, custom code outside the approved scope, paid apps, publication, or failed rollback/QA.

## Success definition

Success is a truthful, reviewable, team-editable draft or mutation packet with its defects and evidence visible. It is not “Claude said it succeeded,” an uploaded theme, or a predicted conversion rate.

## Quality Gate

- BitBranding remains the single owner and both component workflows ran in order.
- Missing facts, blueprint approval, and connector-write permission are explicit states.
- The draft target and rollback point are unambiguous; the live theme is excluded.
- Defects and repairs carry rendered or functional evidence.
- Implementation proof and business proof are separate.
- Exactly one next safe action is named.
