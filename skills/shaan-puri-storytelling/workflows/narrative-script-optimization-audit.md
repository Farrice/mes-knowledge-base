---
slug: narrative-script-optimization-audit
name: "Narrative Script & Content Optimization Audit"
description: "Diagnose and rebuild a supplied narrative or script using source-grounded Shaan Puri mechanics and a strict factual-integrity invariant."
produces: "A polished, humor-infused narrative script or article"
expert: "Shaan Puri Storytelling Mastery"
load_context: "genius.md"
---

# Shaan Puri Storytelling Mastery — Narrative Script & Content Optimization Audit

## Role
You are applying Shaan Puri's sourced story architecture to a supplied draft or fact packet. Diagnose why it feels flat, corporate, confusing, or poorly paced, then rebuild it without changing what happened.

## Skill Acquisition

1. If invoked through `/shaan-story-deploy`, inherit its `FULL STORY` or `STORY FRAGMENT` decision and truth constraints.
2. If invoked directly, read `references/story-deployment-map.md` first. Refuse or downgrade when story does not fit.
3. Read `genius.md`, especially Decision Framework, Voice DNA, Patterns 1–7, audience buy-in pacing, and the Factual Integrity Invariant.
4. Execute `references/prompts-v2/narrative-script-optimization-audit.md` for the exact deliverable shape.

## Input Required
1. **Raw Content/Draft**: The facts, events, or current underperforming draft.
2. **Target Platform**: (e.g., Twitter/X Thread, YouTube Script, Newsletter, LinkedIn Post).
3. **The "Jenny"**: Describe the one supported audience situation or label it as a working hypothesis.
4. **Desired Outcome**: What should the audience FEEL and DO after reading?
5. **Tone Parameters**: Formality level (Low-status/Conversational is default) and Humor level (Light/Moderate/Heavy).
6. **Source Facts and Paths**: The details, quotes, chronology, metrics, and evidence the rewrite may use.
7. **Narrative Dosage**: `FULL STORY` or `STORY FRAGMENT`.
8. **Truth Constraints**: Unknowns, prohibited claims, and required labels.

If target platform, audience, desired outcome, tone, or voice is absent, preserve it as unknown. When truth and scope are still clear, use a neutral platform-agnostic working default and label the output a provisional asset. Missing presentation context blocks a claim of channel-specific deployment readiness; it does not block a factual local draft or authorize invented audience detail.

> **Pre-Flight Gate**: Run `genius.md` § Decision Framework. List the protected facts and voice markers before rewriting. Missing story texture becomes `[NEEDS SOURCE]`, never invented detail.


## Workflow

### Phase 1: The Diagnostic Surgery
Perform a "Content Audit" to identify why the current version isn't landing.
*   **Identify Failure Mode**: Flag Frame Failure, Voice Drift, unsupported narrative pressure, or a missing direct-explanation spine.
*   **Extract Buried Value**: Find the one genuinely interesting fact or moment hidden in the fluff.
*   **The Jenny Filter**: Use supplied audience evidence or a labeled working hypothesis. Do not invent a bedroom, private emotion, or reading context.
*   **Frame Generation**: Produce three truthful frames. Select for objective, audience fit, and evidence support—not maximum emotionality.

### Phase 2: Branch on narrative dosage

For `FULL STORY`, rebuild around a supported intention, obstacle, change, and turn. Use a yin-yang contrast, pivot, low-status opening, emotion, or sensory anchor only when the Source Facts support that move.

For `STORY FRAGMENT`, preserve the direct evidence or explanation spine. Add exactly one approved frame, sourced moment, labeled analogy, or pacing move. Do not add a protagonist arc or full transformation structure.

### Phase 3: Optional voice and humor pass

Apply humor, parenthetical asides, levity, or spoken texture only when the requested voice, risk class, and supplied material support it. Humor has no fixed percentage. Never invent inner monologue, minimize a serious fact, or make evidence feel more certain.

### Phase 4: Platform-Specific Calibration
Finalize the structure based on the **Attention Contract** of the target platform.
*   **For Video**: Calibrate the opening and beats to the supplied duration. Use story architecture only for `FULL STORY`; a fragment or direct explainer keeps its factual spine.
*   **For Threads/Articles**: Improve skimmability and pacing. Use nested stories only when multiple supported stories exist and the dosage permits them.

## Content-Type Adaptations

| Context | Adaptation |
|---|---|
| Founder, customer, or origin material | Require traceable events, chronology, outcomes, and quotes; use source gaps instead of narrative completion |
| Evidence-sensitive explanation | Keep evidence primary and use only the router-approved fragment |
| Internal or technical communication | If direct decision logic is primary, return to `NO STORY` and preserve only frame, hierarchy, or plain-language compression |
| Video | Pair supported spoken beats with visual notes; never invent B-roll as evidence of an event |
| Text or social | Calibrate value density and line length to audience buy-in rather than a universal length rule |

## Output Contract
The user receives a single document—deployment-ready when presentation inputs are complete, or explicitly labeled provisional when they are not—containing:
1. **The Diagnosis**: What is weak, what must be preserved, and which dosage is active.
2. **Three truthful opening frames**: Ranked by objective, audience fit, and evidence support.
3. **The Final Asset**: A full narrative only for `FULL STORY`; otherwise a direct asset with one bounded fragment.
4. **Production Notes**: Platform and format guidance, with hypothetical visuals labeled and unsupported texture omitted.

Execution prompt: `references/prompts-v2/narrative-script-optimization-audit.md` — honor its Output Contract.

## Quality Gate
*   **The Full-Story Test**: When dosage is `FULL STORY`, are the intention, obstacle, change, and turn supported?
*   **The Fragment Test**: When dosage is `STORY FRAGMENT`, does the direct spine remain primary with only one approved story move?
*   **The Voice Test**: Are humor, emotion, and audience details supported or clearly labeled—not mandatory decorations?
*   **The Audience Check**: Does the asset fit the supplied audience evidence or an explicit working hypothesis?
*   **The Dosage Test**: Does the result honor `FULL STORY` or preserve the direct spine under `STORY FRAGMENT`?
*   **The Fact-Trace Test**: Can every dialogue line, event, metric, outcome, emotion, and sensory detail trace to the source facts?
*   **The Readiness Test**: If presentation context is incomplete, are the working defaults labeled and the missing deployment inputs named?


> **Anti-Pattern Check**: Review `genius.md` § Anti-Patterns, Voice DNA, and Factual Integrity Invariant before delivery.
