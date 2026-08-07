---
name: thumbtack-continuity-audit
description: Trace one carried concept through a 4–12-line section and prescribe the smallest delete, reorder, or bridge repair.
produces: Sentence Dependency Map
routing: long-tail
menu_exempt: permanently internal semantic-dependency scalpel; no public command by approved architecture
source_rows: SL-051, SL-064, SL-065
prompt: references/prompts-v2/thumbtack-continuity-audit.md
---

# Thumbtack Continuity Audit

## Role

Test semantic dependency inside one short section. This is not a full flow, rhythm, voice, or body-copy review.

## Source and Ownership

- **Kyle:** thumbtack-and-string image and concept-continuation test, `SL-051`.
- **Co-authored recurrence:** `SL-064`.
- **Matthew:** later mechanism-consistency diagnosis, `SL-065`; do not relabel it Kyle-only.

## Input Required

1. One 4–12-line section with original line breaks.
2. The section's job and controlling Promise Card.
3. Audience, placement, and intended next section.
4. Definitions and evidence IDs for named mechanisms/concepts.

## Hard Stop / Refusal

Return `HOLD_THUMBTACK` when:

- no controlling concept can be named;
- the Promise Card itself is broken;
- fewer than 4 or more than 12 lines are supplied;
- the scope is a whole sales letter or full flow audit;
- an undefined mechanism makes continuity impossible to assess.

Route promise/mechanism failure upward before sentence repair.

## Procedure

### 1. Name the Thumbtack

Write the one concept the reader should still be carrying at the end. It must be supported and concrete enough to recognize.

### 2. Map Sentence Dependencies

For each line record:

- `inherits`: exact noun, claim, time frame, audience, or mechanism carried in;
- `advances`: what new work the line performs;
- `hands_off`: what the next line should inherit;
- `status`: `CONNECTED`, `BRIDGE_NEEDED`, `REORDER`, `DELETE`, or `ESCALATE`.

### 3. Find Broken Strings

Flag unannounced changes in:

- mechanism or object;
- audience or subject;
- time frame;
- promise/result;
- evidence type;
- section job.

### 4. Prescribe the Smallest Repair

Choose one:

- delete the stray line;
- reorder lines;
- add one evidence-bounded bridge;
- escalate an undefined concept or broken promise.

Do not smooth every sentence.

## Output Contract

```markdown
# Sentence Dependency Map

## Section Lock
- Job:
- Controlling promise:
- Thumbtack concept:

## Dependency Map
| Line | Inherits | Advances | Hands off | Status | Evidence |

## First Broken String
- Line:
- Change introduced:
- Why the reader cannot carry it:

## Minimal Repair
- DELETE | REORDER | BRIDGE | ESCALATE
- Exact action:
- Preserved lines:
- Recheck condition:

## Handoff
- Next owner:
- Open risk:
```

## Quality Gate

- [ ] Scope is one 4–12-line section.
- [ ] One supported thumbtack concept is named.
- [ ] Every line states what it inherits and hands off.
- [ ] The first broken string is exact, not “flow feels off.”
- [ ] Repair is the smallest delete, reorder, bridge, or escalation.
- [ ] No full-body rewrite or rhythm audit appears.
- [ ] Matthew-owned observations remain attributed.

## Handoff

Pass a repaired opener to workflow 04 for one recheck. Route full-copy flow to Matthew, rhythm-only work to the existing mechanics owner, and promise/mechanism failure upward. Stop after the handoff.

## Execution Prompt

Read and honor `../references/prompts-v2/thumbtack-continuity-audit.md`.
