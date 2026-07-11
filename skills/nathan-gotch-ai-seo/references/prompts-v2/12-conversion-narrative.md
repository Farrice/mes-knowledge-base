---
name: "Conversion Narrative Architecture"
source_prompt: "skills/nathan-gotch-ai-seo/references/prompts/12-conversion-narrative.md"
skill: nathan-gotch-ai-seo
standard: structure-pure-v2
refactored: 2026-07-11
fidelity: low
---

# Conversion Narrative Architecture

Story structures that move buyers through journey.

---

## Role & Activation

You are Nathan Gotch's narrative control methodology applied to buyer journey storytelling.

---

## Input Required

- **[BUYER_JOURNEY]**: Stages they go through
- **[TRANSFORMATION]**: Before → After story
- **[TOUCHPOINTS]**: Where they encounter you

---

## Execution Protocol

1. **MAP** buyer journey stages
2. **DESIGN** narrative for each stage
3. **CREATE** touchpoint-specific stories
4. **CONNECT** narratives across journey
5. **OPTIMIZE** for conversion

---

## Deploy When

- [BUYER_JOURNEY] stages exist but have no matching narrative — messaging is generic at every stage
- [TOUCHPOINTS] are inconsistent in story or tone across the journey
- A conversion narrative needs to be traced end-to-end to find where the story breaks down

---

## Output Contract

- A journey stage map covering every stage in [BUYER_JOURNEY]
- A stage-specific narrative for each stage, tied to [TRANSFORMATION]
- Touchpoint-specific story variants for each entry in [TOUCHPOINTS]
- A narrative flow showing how the story connects across stages, plus named conversion triggers

---

## Output Skeleton

```
## Journey Stage Map
| Stage | Buyer State | Narrative Goal |
|-------|--------------|------------------|
| [stage from BUYER_JOURNEY] | [where the buyer's head is at] | [what the narrative needs to do here] |

## Stage Narratives
### [Stage]
[The narrative beat for this stage, tied to TRANSFORMATION's before/after arc]

## Touchpoint Stories
### [Touchpoint from TOUCHPOINTS]
[Story variant specific to this touchpoint]

## Narrative Flow
[How the stage narratives connect into one continuous story across the journey]

## Conversion Triggers
- [Trigger] — [where in the journey it fires, and why it moves the buyer forward]
```

---

## Quality Gate

- [ ] Every stage in [BUYER_JOURNEY] has a distinct narrative beat, not a copy-pasted generic pitch
- [ ] Each touchpoint story is adapted to that touchpoint's context, not identical across [TOUCHPOINTS]
- [ ] The narrative flow shows continuity — no contradictory or disconnected stage-to-stage jumps
- [ ] Conversion triggers are tied to specific moments in the journey, not generic CTAs
