---
name: first-four-lines-audit
description: Gate an opening at its first four lines with an advance, repair, or restart verdict and the first exact failure.
produces: ADVANCE, REPAIR, or EXIT/RESTART verdict
routing: long-tail
menu_exempt: pending detached behavior proof and Verification approval
source_rows: SL-045
prompt: references/prompts-v2/first-four-lines-audit.md
---

# First-Four-Lines Audit

## Role

Decide whether the opening has earned another line. This is an early continuation gate, not Matthew's full Hook/Flow/Close/Voice audit.

## Source and Ownership

- **Kyle:** first-line and continuation questions at `SL-045`.
- **Adjacent source exclusion:** contest-entry count in `SL-046` is self-reported and cannot become role proof.
- **Context reinforcement:** `SL-044` is co-authored.

## Input Required

1. At least four actual opening lines, preserving their line breaks.
2. Product Truth Packet and intended Promise Card.
3. Audience, awareness, placement, voice owner, and desired action.
4. Evidence IDs for factual clauses.
5. Intended next section/job.

## Hard Stop / Refusal

Return `HOLD_FIRST_FOUR` when:

- fewer than four lines are supplied;
- audience, offer, intended promise, or placement is unknown;
- the Product Truth Packet is missing;
- an idea-level or promise-level failure is already known;
- the request is actually a full-copy audit.

Do not fabricate unseen lines or grade a fragment as if it were complete.

## Procedure

### 1. Map Each Line's Job

For lines 1–4, identify:

- intended beat/job;
- concept inherited from the previous line;
- new information advanced;
- factual claim and evidence ID;
- reader question opened or resolved.

### 2. Run the Continuation Questions

At each line ask:

- Why is this here now?
- Why should this speaker/source be heard?
- What is in it for this reader?
- What promise is becoming clear?
- What specific reason remains to read the next line?

### 3. Find the First Failure

Stop at the earliest line that fails. Classify it:

- `CONTEXT`;
- `PROMISE`;
- `RELEVANCE`;
- `CREDIBILITY`;
- `DEMONSTRATION`;
- `CONTINUITY`;
- `UNDEFINED_CONCEPT`;
- `VOICE_OR_FORMAT`.

### 4. Issue One Verdict

- `ADVANCE` — all four lines earn continuation and evidence maps cleanly.
- `REPAIR` — promise passes; one local defect has a bounded repair.
- `EXIT/RESTART` — idea/promise/context failure makes line repair wasteful.

Prescribe only the first repair. Do not rewrite the whole opening unless the caller explicitly invokes the builder next.

## Output Contract

```markdown
# First-Four-Lines Verdict

## Context Lock
- Audience:
- Promise:
- Placement:
- Desired action:

## Line Job Map
| Line | Job | Inherits | Advances | Evidence | Continue? |

## Verdict
- ADVANCE | REPAIR | EXIT/RESTART
- First failing line:
- Failure class:
- Reader-level reason:
- Preserve:
- First exact repair:

## Handoff
- Next owner:
- Prohibited lower-level work:
- Recheck condition:
- Open risk:
```

## Quality Gate

- [ ] Four actual lines were assessed in order.
- [ ] Every line has a job, concept handoff, and evidence status.
- [ ] The first failure—not the loudest failure—controls the verdict.
- [ ] An idea-level failure is not disguised as line-level repair.
- [ ] `REPAIR` contains one exact action; `ADVANCE` contains no gratuitous rewrite.
- [ ] Feedback diagnoses the artifact, not the writer.
- [ ] The next owner is one workflow or existing skill.

## Handoff

- `ADVANCE` → existing body-copy owner.
- Opening architecture failure → `03-four-beat-opening-builder.md`.
- Promise failure → `02-unique-promise-spine.md`.
- One undefined-concept or continuity failure → workflow 07 or 05.
- Unknown/missing move → `08-negative-space-copy-chief.md`.

## Execution Prompt

Read and honor `../references/prompts-v2/first-four-lines-audit.md`.
