---
description: "Phase 4 closeout of a Supercomputer mission — individual per-deliverable finalize calls, honest actual-vs-planned cost reconciliation, and a specific next move, never a batched or generic wrap-up."
---

# Mission Completion Summary — Closing the Cost-Gate Contract

Dispatches `skills/supercomputer/references/prompts-v2/mission-completion-summary.md` (the engine
— read it first, this file is the workflow contract wrapping it). Per
`skills/supercomputer/genius.md`, the pre-flight cost preview is a trust mechanic — when the user
approved a costed plan, they entered a contract. This closeout is where the contract gets honored
or exposed as broken: real numbers, real per-deliverable scores, a real next move.

## Invocation

The final turn of every Supercomputer mission, fired only after Phase 3 (Anchor Propagation
Verification) has cleared. Never fired mid-mission and never a substitute for the individual
finalize calls it summarizes.

## Stages

1. **Finalize each deliverable individually** — one `chain_runner.py finalize` call per
   deliverable, never batched (explicit `SKILL.md` Anti-Pattern: "Each deliverable gets its own
   `chain_runner.py finalize` call. No exceptions.").
2. **Score each on the 4-dimension rubric** (CLAUDE.md Step 6). Composite <7 or any dimension <6 →
   retry the weakest section once, then re-finalize before it appears in the summary.
3. **Mark Factual Grounding N/A** in the finalize notes for pure-creative deliverables with no
   real-world claims, rather than scoring it.
4. **Pull the reconciled actual cost** — `python3 execution/cost_gate.py status` — against the
   Phase 1 planned estimate.
5. **Present the closing block** in the exact literal format: files produced, cost incurred
   (actual vs. planned), per-deliverable quality scores, anchor count, and one specific next move.

## Output Schema

The single closing "MISSION COMPLETE — `<slug>`" block, populated only with data actually produced
this mission: real file paths from `anchor_memory.py describe`, the real actual-vs-planned figures
from `cost_gate.py status`, and per-deliverable scores that match individual `chain_runner.py
finalize` calls actually made — zero invented paths, zero invented scores, zero rounded
stand-in cost figures. The "Suggested next move" line names one specific, executable follow-on
(a concrete `/supercomputer` invocation or a named action) — a generic "let me know what's next"
fails this schema.

## Quality Gate

- Every deliverable was finalized with its own individual `chain_runner.py finalize` call — zero
  batching, verifiable against the number of files-produced bullets.
- Every file path in "Files produced" corresponds to a real anchor or a real deliverable produced
  this session — none invented to round out the list.
- Any deliverable that scored composite <7 or a single dimension <6 was retried once before
  appearing here, and its listed score reflects the post-retry result, not the original.
- The cost line is sourced from `cost_gate.py status`, never estimated from memory or copied
  forward from the Phase 1 plan unchanged.
- "Suggested next move" is specific and executable, not a sign-off question.
