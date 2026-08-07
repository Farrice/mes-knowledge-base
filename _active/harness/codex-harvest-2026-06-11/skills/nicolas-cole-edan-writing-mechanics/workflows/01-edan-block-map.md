---
description: "Classify a passage into Explanation, Description, Action, and Narration"
---

# EDAN Block Map

## Pre-Flight Gate

Use this workflow when the user provides a passage, draft, scene, thread, article section, script, newsletter, or model excerpt and wants to understand what is happening mechanically.

If the user only has an idea and no draft, use `/edan-opener-builder` or `/nonfiction-outline-architect` first.

## Skill Acquisition

Load:

- `skills/nicolas-cole-edan-writing-mechanics/genius.md`
- `skills/nicolas-cole-edan-writing-mechanics/references/genius-patterns.md`

## Execution

1. Identify the unit of analysis: sentence, paragraph, scene, section, or full piece.
2. Split the passage into clean numbered units.
3. Label each unit:
   - `E` = Explanation: context, backstory, logic, clarifying meaning.
   - `D` = Description: concrete detail that implies meaning.
   - `A` = Action: something happens, changes, moves, or reveals.
   - `N` = Narration: narrator/author belief, worldview, theme, judgment, or point of view.
4. For mixed units, choose the dominant function and note the secondary function.
5. Count the block ratio.
6. Name the current reader effect created by the mix.
7. Identify the missing or overused block.
8. Produce a rewrite recommendation without polishing yet.

## Content Type Adaptations

| Type | Mapping Focus |
|---|---|
| Fiction scene | Action consequence, description implication, narration scarcity |
| Memoir/personal essay | Explanation timing, narration point of view, description intimacy |
| Newsletter/article | Explanation overload, examples as action, narration as thesis |
| LinkedIn post | Claim-to-example ratio, POV lines, action proof |
| Client ghostwriting | Preserve voice markers while mapping function |
| Sales story/case study | Proof actions, concrete before/after, restrained narration |

## Output Requirements

Return:

1. EDAN map table: unit, excerpt/summary, block, why.
2. Block ratio.
3. Mechanical diagnosis.
4. Top 3 revision moves.
5. One suggested target block sequence.

## Quality Gate

Pass only if each label explains the functional job of the unit. Do not label based on topic alone. A sentence about an action can still be Explanation if it is only backstory.
