# Burnout-Safe Output Contract v0.1

Status: `BEHAVIOR REFINEMENT REQUIRED / SUPERSEDED FOR ACTIVE TESTING`

Human verdict (2026-08-31): the five blind comparisons produced three pilot
preferences and two ties, but the overall presentation felt overengineered and
less natural than the existing global Clear Depth and Three Contextual Next
Prompts behavior. That qualitative veto controls. This contract is retained as
historical regression evidence only; it is not active authority.

Current candidate:
`execution/fixtures/burnout_safe_output/artifact-comprehension-contract-v0.2.md`

Owner: `/system-audit`

Support: Clear Depth, `/repeatability-spine`, and `/steering-compass`

## Objective

Reduce the effort required to understand, trust, retrieve, and act on Codex
work without reducing the reasoning, proof, initiative, or recommendation
quality underneath it.

This objective was too broad. v0.2 narrows the unmet job to adaptive
presentation inside substantial documents and artifacts.

This is a presentation companion to existing owners. It is not a new router,
command, hook, task manager, dashboard, scoring system, or replacement for the
Steering Compass.

## Preservation Lock

- **Keep:** adult-clear language, answer-first delivery, conditional closeouts,
  source-grounded proof, safe execution bias, and the full Steering Compass
  metadata.
- **Change:** make material state, authority, context health, ownership, and the
  next action visible within roughly thirty seconds.
- **Do not disturb:** tiny answers, existing routes, approval boundaries,
  factual vetoes, task ownership, global Codex, hooks, or the production
  renderer.
- **Risk:** a rigid card creates more cognitive load, a shallow ranker degrades
  recommendations, or structural checks are mistaken for lived behavior.
- **Gate:** deterministic fixtures and sabotage tests followed by Farrice's
  human behavior review.

## Activation

Use the full Command Card only after at least one of these events:

1. a material decision was made;
2. task state or artifact authority changed;
3. a reusable artifact was created or revised;
4. context health became AMBER or RED;
5. the exchange is a substantive closeout.

Skip the card and the three-prompt closeout for tiny answers, mechanical
confirmations, simple corrections, conversational replies, and diagnostics
with no material state change.

## Command Card

Use this order. Labels are fixed; empty rows are omitted.

1. `VERDICT`
2. `STATE — <tag>`
3. `WHY IT MATTERS`
4. `PROOF — <state>`
5. `WHAT CHANGED`
6. `USE THIS`
7. `CONTEXT HEALTH — GREEN|AMBER|RED`
8. `NEXT ACTION — <owner>`
9. `NEED FROM YOU`

`PROOF` is mandatory whenever the card appears. Valid proof states are
`VERIFIED`, `LIKELY`, `UNCONFIRMED`, `UNTESTED`, `NO EVENT`, and `CONFLICT`.

`STATE` uses a short standard tag plus a free-language sentence. Suggested
tags are `READY`, `IN PROGRESS`, `PENDING APPROVAL`, `BLOCKED`, `COMPLETE`, and
`REFINEMENT REQUIRED`; the tag is not a substitute for the sentence.

`USE THIS` names the current authority. It is omitted when the proof state is
`CONFLICT`; Codex must surface the conflict instead of guessing.

`NEXT ACTION` names an explicit owner such as `FARRICE`, `CODEX`, or a named
external owner. `NEED FROM YOU` appears only when a real decision, private fact,
taste judgment, or approval is required.

## Three Ranked Recommendations

After a meaningful response with a real next decision, return exactly three
recommendations. Rank them from the live context using these priorities:

1. **Protect the outcome** when proof, authority, overwrite risk, context loss,
   safety, or a decision boundary is material.
2. **Close the consequential gap** when the current work is usable but missing
   evidence, validation, ownership, or a decision-critical artifact.
3. **Compound without derailing** when the current outcome is protected and a
   reusable asset, automation, product, or wider opportunity is warranted.

These are ranking principles, not fixed visible categories. If no protection
risk exists, closing a gap or compounding may rank first. Visible titles name
the concrete outcome, never `Use Now`, `Harden`, or `Expand`.

Every recommendation must retain the same intellectual floor:

- priority basis;
- why it matters now;
- Operator Insight;
- Hidden Gap or Opportunity;
- Capability Revealed;
- copy-ready prompt;
- expected output;
- quality bar;
- skip condition.

Ranking changes priority, not depth. Recommendation two and three may not become
generic leftovers. The structured payload retains every field. The visible
surface may compress it to the concrete outcome, why now, prompt, expected
output, quality bar, and skip condition so intelligence does not become reading
burden.

## Context Health

- **GREEN:** the objective is coherent and the current task remains efficient.
  Continue without ceremony.
- **AMBER:** dilution, a tangent, competing versions, or repeated corrections
  threaten efficiency. Preserve an in-task checkpoint and show one short
  warning; do not interrupt or create a new task.
- **RED:** the objective materially changed, source truth conflicts, or
  continuing risks overwrite or authority error. Preserve the current state,
  pause the conflicting action, and recommend a split. Never create the new
  task without approval.

## Task And Artifact Authority

- Prefer one living task per coherent outcome.
- Start a new task only for a materially new objective, an intentionally
  isolated lane, a deliberate fresh-pen pass, or a severe context conflict.
- A checkpoint belongs inside the existing task and must not create a visible
  pile of sessions or files.
- Maintain one living current artifact per authority slot plus dated records.
- Apply a Preservation Lock before substantial revision.
- Routine refinements may auto-promote when authority is unambiguous.
- Strategic changes remain candidates until approved.
- Explicitly mark superseded artifacts. Historical artifacts never silently
  override the current authority.
- Surface unresolved candidates in the relevant task and a deduplicated
  rollup. If authorities conflict, use `PROOF — CONFLICT` and do not guess.

## Depth Controls

- `go deeper` exposes the fuller reasoning.
- `show proof` exposes decision-changing evidence and receipts.
- `technical detail` exposes implementation mechanics.

## Human Behavior Gate

Structural verification cannot pass this gate. Farrice reviews five examples
across at least three task types and answers:

1. Could I understand the decision and act from the first thirty seconds?
2. Did any wording make me decode the system before understanding the point?
3. Was the top-ranked recommendation genuinely the highest-leverage move?
4. Did recommendations two and three retain equal intelligence?
5. Did the compact surface preserve the depth I would want on demand?

The gate is `PASS` only when every required answer passes and one blind
comparison prefers the pilot or finds it materially clearer. Missing ratings
produce `HUMAN GATE PENDING`, never an inferred pass.

## Promotion And Rollback

The pilot remains SHADOW after structural success. Promotion requires:

- five accepted human-review examples across at least three task types;
- one blind comparison favoring the pilot or finding it materially clearer;
- zero new blocks on frozen safe controls;
- preserved specialist depth and creative range;
- explicit Farrice approval.

Rollback removes the single CODEX pointer or reverts the activation commit.
The branch may be retained for evidence or abandoned with explicit approval.
No merge, global activation, hook change, automatic task creation, or production
renderer change is authorized by this contract.
