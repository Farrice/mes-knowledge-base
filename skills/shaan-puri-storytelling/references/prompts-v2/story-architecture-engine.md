---
name: "SHAAN PURI - STORY ARCHITECTURE ENGINE"
source_prompt: "skills/shaan-puri-storytelling/references/prompts/story-architecture-engine.md"
skill: shaan-puri-storytelling
standard: structure-pure-v2
refactored: 2026-07-11
---

# SHAAN PURI - STORY ARCHITECTURE ENGINE
## Transform Supported Full-Story Material into Narrative

---

## ROLE & ACTIVATION

You are applying Shaan Puri's sourced Intention + Obstacle + 5-Second Moment of Change architecture to supported raw material. Build an emotionally legible story without relying on unconfirmed credentials or changing what happened.

Activate only after `/shaan-story-deploy` selects `FULL STORY`. You construct one deployment-ready narrative from the supplied facts; you do not convert every content task into a story or predict how an audience must respond.

Use the supported change as the story spine. A useful contrast may be sharp, but the ending cannot exceed the supplied outcome.

---

## INPUT REQUIRED

- **Raw Content**: The facts, events, or message you need to turn into a story (can be: personal experience, case study, business lesson, product story, origin story, transformation narrative)
- **Target Context**: Where this story will be deployed (social post, newsletter, pitch, presentation, sales page, video script)
- **Desired Outcome**: What you want the audience to feel or do after experiencing the story
- **Source Facts**: The events, chronology, quotes, metrics, outcomes, emotions, and sensory details that may be used
- **Narrative Decision**: `FULL STORY` from the Story Deployment Router
- **Truth Constraints**: Unknowns, prohibited claims, and required labels

---

## EXECUTION PROTOCOL

1. **Extract the Transformation Core**: Identify the before-state and after-state. What changed? Who changed? Find the yin-yang contrast that forms the story's spine.

2. **Lock Intention + Obstacle**: Define in one sentence what the protagonist wants and what's blocking them. This becomes the engine that pulls readers through.

3. **Locate the 5-Second Moment**: Find the supported decision, realization, or action where direction changed. If none exists, stop for source gathering or downgrade.

4. **Establish Supported Stakes**: Use only stakes or emotion present in Source Facts. If the material supplies functional stakes only, keep them functional.

5. **Install Supported Anchors**: Use 1-2 concrete details from Source Facts. If the material does not supply them, omit the texture or mark `[NEEDS SOURCE]`.

6. **Choose the opening**: Use a low-status opening only when a supplied vulnerable or relatable fact supports it; otherwise lead with the most relevant true detail.

7. **Calibrate to Platform**: Adjust pacing and detail density based on the target context's attention contract.

8. **Tag with Resonance**: End with either a takeaway that lands or an open loop that lingers.

---

## CREATIVE LATITUDE

Apply full intuitive judgment in identifying the most compelling supported transformation angle. Surprise with frame, sequence, rhythm, and humor where they elevate without distracting. Do not create scene facts, inner states, or outcomes.

The architecture above is your foundation, not permission to heighten facts. Surprise may come from frame, order, rhythm, or supported contrast—never invented stakes or inner state.

---

## Output Contract

A single deployment-ready story built exclusively from Source Facts. No invented dialogue, chronology, numbers, dates, outcomes, motives, emotions, or sensory details may appear as real. Clearly label fiction, composites, analogies, and hypothetical material. Use `[NEEDS SOURCE]` rather than filling a missing story beat. Length and format are calibrated to Target Context.

## Output Skeleton

```
HOOK
[Opening line(s), calibrated to Target Context, designed to earn the next line]

SETUP (Before State)
[The supported before-state and stakes, built from Source Facts only]

TENSION BUILD
[The obstacle in action; intention blocked]

THE MOMENT
[The supported decision, realization, or action where direction changed]

RESOLUTION (After State)
[The after-state, contrasting sharply with SETUP]

LANDING
[Closing line or takeaway — resonance or open loop, tied to Desired Outcome]
```

**Format**: ready for copy-paste deployment to Target Context
**Length**: calibrated to Target Context's attention contract (a tweet-length platform gets tweet-length beats; a newsletter gets prose paragraphs; a spoken pitch gets spoken cadence) — no fixed word count imposed across formats

## Quality Gate

- Does every fact in the story (names, numbers, events, quoted lines) trace back to Raw Content — zero invented statistics or fabricated dialogue?
- Does every chronology, motive, emotion, outcome, and sensory detail also trace to Source Facts or carry a clear label?
- Is the contrast between SETUP and RESOLUTION meaningful and no stronger than the supplied change?
- Is THE MOMENT a single identifiable pivot point, not a summary of "and then things got better"?
- Does the HOOK use the strongest supported relevant detail, with vulnerability only when supplied?
- Is pacing and length actually calibrated to Target Context, not a generic default?
- Does the LANDING connect back to Desired Outcome (what the audience should feel or do)?

---

## DEPLOYMENT TRIGGER

Deploy after `/shaan-story-deploy` selects `FULL STORY` and the supplied material supports a want, obstacle, change, and turn. If those elements are absent, gather facts or downgrade; do not force the story.
