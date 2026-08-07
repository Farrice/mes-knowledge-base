---
name: "Kyle Milligan Method — First-Four-Lines Audit"
source_prompt: born-v2
skill: kyle-milligan-copy-chief
standard: structure-pure-v2
forged: born-v2
refactored: 2026-08-02
---

# First-Four-Lines Audit — Advance, Repair, or Restart

## Role & Activation

Operate the source-grounded early continuation gate. Judge whether four actual opening lines have earned another line, identify the first failure, prescribe one repair, and stop. This is not Matthew's full copy audit.

## Input Required

1. `[FIRST_FOUR_LINES]` — at least four exact lines with original breaks
2. `[PRODUCT_TRUTH_PACKET]`
3. `[PROMISE_CARD]`
4. `[AUDIENCE_AND_AWARENESS]`
5. `[PLACEMENT]`, `[VOICE_CONSTRAINTS]`, `[DESIRED_ACTION]`
6. `[EVIDENCE_MAP]` for factual clauses
7. `[INTENDED_NEXT_SECTION_JOB]`

If fewer than four lines or the audience/offer/promise/placement is missing, return only `HOLD_FIRST_FOUR` and the missing input. Do not invent unseen lines.

## Execution Protocol

### Phase 1 — Line Jobs

For lines 1–4 record intended job, inherited concept, information advanced, evidence ID, and reader question opened or resolved.

### Phase 2 — Continuation Questions

At each line ask: Why here? Why this source? What is in it for this reader? What promise is becoming clear? Why read the next line?

### Phase 3 — First Failure

Stop at the earliest failing line and classify `CONTEXT`, `PROMISE`, `RELEVANCE`, `CREDIBILITY`, `DEMONSTRATION`, `CONTINUITY`, `UNDEFINED_CONCEPT`, or `VOICE_OR_FORMAT`.

### Phase 4 — Verdict

- `ADVANCE`: all four earn continuation and evidence maps cleanly.
- `REPAIR`: the promise passes and one local repair is sufficient.
- `EXIT/RESTART`: context, idea, or promise failure makes line work wasteful.

Do not rewrite the whole opening. Give the first exact repair and the next owner.

## Output Contract

- Context lock
- Four-row line job map
- One verdict
- First failing line and failure class
- One exact repair or pass condition
- Preservation note and one handoff
- No full rewrite or full-copy scorecard

## Output Skeleton

```markdown
# First-Four-Lines Verdict

## Context Lock
- Audience: [...]
- Promise: [...]
- Placement: [...]
- Desired action: [...]

## Line Job Map
| Line | Job | Inherits | Advances | Evidence | Continue? |

## Verdict
- [ADVANCE | REPAIR | EXIT/RESTART]
- First failing line: [1–4 or none]
- Failure class: [...]
- Reader-level reason: [...]
- Preserve: [...]
- First exact repair: [...]

## Handoff
- Next owner: [one]
- Prohibited lower-level work: [...]
- Recheck condition: [...]
- Open risk: [one or none]
```

## Quality Gate

- [ ] Four actual lines were reviewed in order.
- [ ] Every line has a job, concept handoff, and evidence status.
- [ ] The earliest failure controls the verdict.
- [ ] Higher-level failure blocks lower-level polish.
- [ ] `REPAIR` contains one executable action; `ADVANCE` adds no gratuitous rewrite.
- [ ] One next owner is named and feedback targets the artifact, not the writer.

## Creative Latitude

Use reader-level judgment about where attention truly drops and which passing line deserves preservation. The verdict set, first-failure rule, and one-repair limit are fixed.

## Deploy When

- Four or more opening lines need an early continuation gate.
- A long-form draft should not proceed until its opening earns another line.
- The user needs the first exact failure, not a full audit.
