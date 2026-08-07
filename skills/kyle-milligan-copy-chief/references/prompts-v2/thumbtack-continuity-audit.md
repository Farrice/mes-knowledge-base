---
name: "Kyle Milligan Method — Thumbtack Continuity Audit"
source_prompt: born-v2
skill: kyle-milligan-copy-chief
standard: structure-pure-v2
forged: born-v2
refactored: 2026-08-02
---

# Thumbtack Continuity Audit — Sentence Dependency Map

## Role & Activation

Operate Kyle's source-grounded thumbtack-and-string continuity test on one 4–12-line section. Trace one supported concept through adjacent lines and prescribe the smallest delete, reorder, bridge, or escalation. Do not expand into full flow, rhythm, or body-copy review.

## Input Required

1. `[SECTION_4_TO_12_LINES]` — original line breaks
2. `[SECTION_JOB]`
3. `[CONTROLLING_PROMISE_CARD]`
4. `[AUDIENCE_AND_PLACEMENT]`
5. `[INTENDED_NEXT_SECTION]`
6. `[CONCEPT_DEFINITIONS_AND_EVIDENCE_IDS]`

If the controlling promise is broken, no supported concept can be named, or the section falls outside 4–12 lines, return only `HOLD_THUMBTACK` and the upward handoff.

## Execution Protocol

### Phase 1 — Name the Thumbtack

Write the one concept the reader should still carry at the section's end.

### Phase 2 — Map Dependencies

For each line record:

- `inherits`: noun, claim, audience, mechanism, or time frame received;
- `advances`: new work performed;
- `hands_off`: exact concept the next line should receive;
- status: `CONNECTED`, `BRIDGE_NEEDED`, `REORDER`, `DELETE`, or `ESCALATE`.

### Phase 3 — Find the First Broken String

Flag the earliest unannounced change in mechanism/object, audience, time frame, promise/result, evidence type, or section job.

### Phase 4 — Minimal Repair

Choose one delete, reorder, evidence-bounded bridge, or escalation. Do not smooth every sentence.

## Output Contract

- One section/job/promise lock
- One named thumbtack concept
- One dependency row per supplied line
- One first-broken-string diagnosis
- One minimal repair and preservation set
- One handoff/recheck condition

## Output Skeleton

```markdown
# Sentence Dependency Map

## Section Lock
- Job: [...]
- Controlling promise: [...]
- Thumbtack concept: [...]

## Dependency Map
| Line | Inherits | Advances | Hands off | Status | Evidence |

## First Broken String
- Line: [...]
- Change introduced: [...]
- Why the reader cannot carry it: [...]

## Minimal Repair
- [DELETE | REORDER | BRIDGE | ESCALATE]
- Exact action: [...]
- Preserved lines: [...]
- Recheck condition: [...]

## Handoff
- Next owner: [one]
- Open risk: [one or none]
```

## Quality Gate

- [ ] Scope is exactly one 4–12-line section with one supported controlling concept.
- [ ] Every line states what it inherits, advances, and hands off.
- [ ] The first semantic break is exact rather than “flow feels off.”
- [ ] Repair is the smallest delete, reorder, bridge, or escalation.
- [ ] Promise/mechanism failure is routed upward instead of line-edited.
- [ ] Matthew-owned observations remain attributed and no full-copy audit appears.

## Creative Latitude

Use judgment in naming the true carried concept and in choosing whether deletion, order, or one surprising but evidence-bounded bridge preserves the most working material. The section limit and one-repair constraint are fixed.

## Deploy When

- Adjacent lines seem individually plausible but the section loses its object.
- A mechanism or audience shifts without an explicit bridge.
- One opening section needs semantic dependency—not full flow—repair.
