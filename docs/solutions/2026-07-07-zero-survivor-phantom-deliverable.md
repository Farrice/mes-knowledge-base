---
name: Zero-Survivor Phantom Deliverable in Fan-Out Pipelines
problem_signature: fan-out workflow where all workers at a stage die still reports complete and returns a deliverable path that was never written
domain: system
tags: [swarm, fan-out, workflow, phantom-research, verification, degraded-mode]
date: 2026-07-07
status: active
session: swarm-apex-2026-07-07
---

## Problem

Fan-out pipelines filter dead workers with `.filter(Boolean)` before the next stage.
If a whole stage dies, a naive implementation falls through anyway, and downstream
synthesis fabricates a plausible answer plus a templated `deliverablePath` — the file
at that path was never written. Caller sees "PASS" with a path that 404s.

## Root Cause

`.filter(Boolean)` silently drops nulls with no signal the drop rate was 100%.
Downstream code that string-templates the output path
(`` `${outDirAbs}/heavy-report.md` ``) assumes the agent that was supposed to write it
succeeded — the path is a plan, not a receipt.

## Approach That Worked

1. After every filter, check `attempted > 0 && survivors === 0` and return early with
   `{ deliverablePath: null, failed: true, failureReason, taskTrace }` — guards at
   Diverge (152-165), Aggregate (185-198), Assemble (249-262).
2. Never fall back to the templated path when the writer agent returned null — the
   guard fires before that path is handed to the caller as a claim.
3. For partial death, don't fail the run — track a running `deadWorkers` counter and
   surface `{ degraded: true, deadWorkers }` in the final return. Degraded-but-real
   beats fully-failed and beats silently-fine.
4. Every survivor's output is logged into `taskTrace` with its real file path, so even
   a degraded run has a file-backed record.

## Dead Ends

- Trusting `result?.filePath || defaultPath` fallbacks — here a fallback path IS a
  fabricated claim that work exists.
- Failing loud only on total death, ignoring partial death visibility.

## Verification

Read the workflow end-to-end; confirmed all three stages guard before referencing an
unwritten file. Cross-checked a real receipt
(`.agent/run-receipts/2026-07-07T175051Z0000-swarm-research.md`, 15/15 agents, 0
errors) as a live pass-path proving completions there are real, not fabricated.

## Weaker-Model Trap

Treats `|| defaultPath` as harmless — "the agent probably wrote there." Backwards: a
guessed path that doesn't exist isn't degraded, it's a false completion claim. Must
ask "did EVERYTHING in this stage die?", not "did enough survive to look done?"

## Pointers

- `.agent/workflows/swarm-heavy.workflow.js` (guards: 152-165, 185-198, 249-262;
  degraded return: 277)
- `.agent/run-receipts/2026-07-07T175051Z0000-swarm-research.md`
- `_active/harness/swarm-apex-2026-07-07/PLAN.md` §"Deliverable-shape acceptance"
