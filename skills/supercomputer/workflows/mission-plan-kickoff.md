---
description: "Phase 0+1 of a Supercomputer mission — derive/load project state, decompose the request into a costed 5-10 step plan, get one explicit approval before any execution fires."
---

# Mission Plan & Kickoff — Opening Move of Every Supercomputer Mission

Dispatches `skills/supercomputer/references/prompts-v2/mission-plan-kickoff.md` (the engine —
read it first, this file is the workflow contract wrapping it). This is the mission's opening
turn: Phase 0 (Project State) and Phase 1 (Plan + Cost Gate) of the four-phase runbook in
`.agent/workflows/supercomputer.md`.

## Invocation

Fires automatically whenever `directives/supercomputer-mode.md` §1 trigger phrases match, or
explicitly via `/supercomputer "<mission request>"`. Never fired mid-mission — a request for a
NEW mission (new or existing project) only.

## Stages

1. **Derive the slug** — kebab-case, 3-6 words, no dates, checked against
   `python3 execution/anchor_memory.py list` for an existing project match before minting a new
   one.
2. **Initialize or load** — `anchor_memory.py init <slug> ...` (new) or
   `anchor_memory.py load <slug>` (existing); state the slug back to the user in one line.
3. **ASK vs INFER** — batch any required clarifying questions (brand name if unnamed, platform,
   audience, tone if 2+ valid reads, anything >$2 of spend) into ONE round, max 3 questions,
   BEFORE the plan block.
4. **Decompose** the request into 5-10 numbered steps; classify each `[free]` or route paid steps
   through `python3 execution/creative_router.py route --task "<step>" --json`.
5. **Cost** every paid step from `execution/cost_gate.py`'s SERVICES dict; sum the total.
6. **Present** the exact-format MISSION PLAN block (banner, steps, anchors flow, "Proceed? (y /
   adjust / cancel)") and wait for explicit approval before any Phase 2 execution fires.

## Output Schema

The deliverable is a single conversational turn, never a partial plan or a narrated summary of
one: (1) the one-line project-slug statement, (2) the literal MISSION PLAN banner block with
numbered steps — each paid step tagged `[$X.XX]` sourced from `cost_gate.py`'s SERVICES dict, never
an invented figure — an "Anchors flow" section listing every anchor with a non-empty `ref_for`,
and the total estimate line, (3) the literal "Proceed? (y / adjust / cancel)" close. Any
clarifying questions required by ASK vs INFER come before the plan block, batched in one round,
never scattered across multiple turns.

## Quality Gate

- Slug follows the derivation rules and was checked against `anchor_memory.py list` for an
  existing match before a new one was minted.
- Every paid step cites a `creative_router.py`-derived service name and a dollar figure sourced
  from `cost_gate.py`'s SERVICES dict — zero invented numbers.
- The "Anchors flow" section matches every "anchored to step `<N>`" annotation in the steps list
  one-for-one; nothing referenced there is missing from the steps list or vice versa.
- Step count is 5-10, each step a genuinely distinct deliverable, not padding to hit a number.
- Any $2+-impact or multi-valid-read decision was asked, not inferred, and batched in one round
  (max 3 questions) per `directives/supercomputer-mode.md` §3.
- Execution does not begin until the plan block's approval line receives an explicit "y" / "go" /
  "proceed" — "adjust" triggers a re-plan and re-show, not a silent continuation.
