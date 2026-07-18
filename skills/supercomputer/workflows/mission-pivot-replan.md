---
description: "Mid-mission redirect handling — acknowledge the delta, re-plan in the exact original format, re-cost honestly, get one fresh approval, and never lose anchors already earned from completed steps."
---

# Mission Pivot / Re-Plan — Handling a Mid-Mission Redirect

Dispatches `skills/supercomputer/references/prompts-v2/mission-pivot-replan.md` (the engine — read
it first, this file is the workflow contract wrapping it). Per `directives/supercomputer-mode.md`
§5, a pivot is not a failure state — it's normal mid-mission behavior. The discipline is in the
handling: precise acknowledgment, a written revised plan (not a prose description), honest
re-costing, one fresh approval, and anchors from completed steps preserved regardless of what
changes later.

## Invocation

Fires when the user issues a mid-mission redirect after a Mission Plan has already been approved
and Phase 2 execution is underway, or when the user wants to abort the mission entirely mid-flight.
Never fired for pre-plan adjustments (that's just re-showing the Phase 1 plan) and never for
post-mission follow-on requests (that's a new Mission Plan Kickoff).

## Stages

1. **Acknowledge precisely** — name what's scoped IN and what's scoped OUT; never accept a
   redirect silently.
2. **Re-plan in writing** — a revised MISSION PLAN block in the exact original format (banner,
   numbered steps, anchors flow, proceed line), not a prose summary of the change.
3. **Re-cost** — recompute the total (dropped-step cost removed, new-step cost added via
   `creative_router.py` + `cost_gate.py` SERVICES), never eyeballed.
4. **Preserve prior anchors** — anchors from already-completed steps stay in the revised "Anchors
   flow" section; a pivot on step 4 doesn't invalidate what steps 1-3 already anchored.
5. **Confirm before resuming** — one explicit "y" on the revised plan; never assume continuation.
6. **Log the pivot** — `python3 execution/anchor_memory.py log <slug> --phase "pivot" --action
   "user redirected from <original> to <new>"`.
7. **Full abort path** — leave `projects/<slug>/` state intact, log the abort action, exit with a
   one-line acknowledgment; no revised plan block, no deletion unless explicitly asked.

## Output Schema

For a partial pivot: (1) the acknowledgment line naming what's dropped and what's added, (2) the
revised MISSION PLAN block in the identical format to the original (including every
still-relevant prior anchor obligation carried into "Anchors flow"), (3) the re-approval prompt.
For a full abort: one acknowledgment line confirming state is preserved and the abort is logged —
no plan block. A pivot response that silently drops a prior anchor's `ref_for` obligation without
naming the change, or that resumes execution without a fresh "y", has not produced this
deliverable.

## Quality Gate

- The acknowledgment names the specific delta (dropped / added), not a vague "got it, adjusting."
- The revised plan uses the exact same block format as the original Mission Plan — never a prose
  stand-in for it.
- Anchors from already-completed steps are preserved in the revised "Anchors flow" section, none
  silently dropped.
- The re-cost was actually recomputed via `creative_router.py`/`cost_gate.py`, not estimated.
- Execution waited for an explicit "y" on the revised plan before resuming.
- For a full abort: state is left intact (not deleted) unless the user explicitly asked for
  deletion, and the abort is logged via `anchor_memory.py log`.
