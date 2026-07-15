---
name: Deep-Research-Swarm Verify Phase Never Fires
problem_signature: a workflow phase silently no-ops at every depth while its log message blames a different condition ("skipped (quick depth)" at depth=deep) — a guard filter whitelisting schema'd enum values matches zero of the free-form values agents actually emit, so the claims array is always empty
domain: system
tags: [deep-research-swarm, verification, silent-no-op, enum-drift, guard-expression, misleading-logs]
date: 2026-07-14
status: active
session: claude-skills-business-deep-research
---

# Solution Card: deep-research-swarm Verify phase never fired (silent no-op)

**Date**: 2026-07-14 · **Domain**: system / research harness · **Session**: claude-skills business deep research

## Problem
The adversarial Verify phase in `.agent/workflows/deep-research-swarm.workflow.js` never checked a single claim at any depth. Runs logged `Verify: skipped (quick depth)` even at `depth=deep`.

## Root cause
The claim filter whitelisted `finding_type ∈ ['statistic','data']`, but fan-out agents emit free-form types (`market_size`, `pricing_data`, `benchmark_data`, `market_share`…). Zero matches → empty claims array → the "skipped (quick depth)" branch message printed for a completely different reason than it stated. Classic silent-cap failure: the log message lied about why.

## Fix (one line)
```js
const claims = findings.filter((f) => /stat|data|size|pricing|revenue|market|benchmark/i.test(f.finding_type || '')).slice(0, checkN)
```
Applied to the canonical workflow and verified live in the Phase-2 SOP swarm run (`wf_8382df4f-239`): 8 claims checked by Opus verifiers, 2 unsourced claims quarantined at ingest.

## Detection rule for the future
When a workflow phase's log message names a condition ("quick depth") that contradicts known inputs (depth=deep), suspect the guard expression, not the config. Schema'd enums drift from free-form agent output — filter on regex families, or validate `finding_type` in the schema itself.

## Related
- Session variant with Conductor Ladder model tiers (Sonnet fan-out / Opus verify / Fable synthesis) worked well; consider promoting `model:` opts into the canonical script.
