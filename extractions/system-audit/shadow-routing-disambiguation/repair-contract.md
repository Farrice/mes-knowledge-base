# SHADOW Routing Disambiguation Repair Contract

Status: `WORKSPACE-LOCAL · BOUNDED`

## Symptom

An unrelated Signal Fidelity SHADOW repair prompt ranked
`/shadow-market-validation-report` first because the fuzzy workflow router
matched the ordinary word `SHADOW` inside that workflow's compound name.

## Root Cause

The control-intent classifier correctly returned no system-failure owner for the
original build prompt. Fuzzy workflow scoring then allowed one ambiguous token
to claim a specialized market-validation route without market, buyer, demand,
launch, niche, or validation context.

The later closeout classification was separate and correct: `verifier` plus
`repair` is explicit control-plane language and belongs to `/system-audit`.

## Smallest Repair

Require market-validation context before the fuzzy router may surface
`/shadow-market-validation-report`. Preserve:

- binding or governor ownership;
- real shadow-market, buyer-demand, niche, MVP, validation, and launch prompts;
- all Signal Fidelity files and SHADOW promotion boundaries.

## Regression Set

Negative controls cover Signal Fidelity SHADOW, generic SHADOW observation,
cold buyer-psychology SHADOW, SHADOW marketing, and visual light/shadow. Positive controls cover
three real market-validation phrasings. Explicit slash-alias behavior is a
separate pre-existing surface and is outside this repair.

## Boundary

No global mirror, Signal Fidelity change, workflow deletion, route promotion,
external write, or enforcement change is authorized. Leave this branch
unmerged after verification.
