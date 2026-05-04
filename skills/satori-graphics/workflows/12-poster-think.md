---
description: 4-input pre-flight brief for fantastic-posters — verb + primitive + memory hook + imperfections. Tight 1-page handoff.
---

# /satori-poster-think — Pre-flight Brief for fantastic-posters

`fantastic-posters` produces poster artwork via Fal API. This workflow runs the four decisions Satori would force *before* generation — verb, visual primitive, memory hook, imperfections — and hands off a tight 1-page brief. Nothing more. The previous 9-step version of this workflow created overhead without speed advantage; this version is the corrective.

## Pre-Flight Gate

**Use this when**:
- About to call `/fantastic-posters` and want a single-pass concept lock first
- Generating a poster series that needs conceptual coherence across pieces
- A previous AI-generated poster came back generic and you want a thinking layer next time

**Do NOT use this when**:
- The brief is exploratory and you want fast iteration (skip; just call `/fantastic-posters` direct)
- You already know the verb + primitive + memory move (skip; you don't need the workflow, you need the production)
- The poster is purely typographic (use Kittl)

## Stacks With

- **`fantastic-posters`** — primary stacking partner; this workflow is the pre-flight, fantastic-posters is the production

## Skill Acquisition

Load:
- `genius.md` — GP-07 (Verb-Not-Noun), GP-09 (Visual Primitive Lock-In), GP-03 (Memory Encoding), GP-11 (Anti-AI-Slop)

That's it. No reference files needed. The four decisions are well-grounded in genius.md and don't require deeper context.

## Execution — 4 Inputs Only

### Input 1: Verb
What does this poster *do* to the viewer? One verb.

Examples (not prescriptive — pick what fits the brief):
- anchors / disrupts / invites / honors / ignites / glitches / pauses / haunts

If you can't pick one verb, the brief isn't ready. Stop. Refine the brief.

### Input 2: Visual Primitive
Map the verb to its shape psychology. From genius.md GP-09:
- Vertical lines → strength, stability, structure
- Horizontal lines → calm, peace, reliability
- Curves / circles → friendly, organic, inclusive
- Sharp angles → robust, technical, modern
- Asymmetry → dynamic, energetic
- Hand-drawn / imperfect → human, crafted, warm

Pick one primary primitive. Optionally pick one supporting.

### Input 3: Memory Hook Move
One of four (genius.md GP-03):
- **A — Metaphor substitution** (familiar object × unexpected metaphor)
- **B — Absence as presence** (negative space carries meaning)
- **C — Conceptual swap** (familiar element replaced with unexpected)
- **D — Controlled imbalance** (small off-grid / off-rotation / asymmetric move)

Pick one. Write a one-sentence concrete implementation. **If you cannot write a concrete implementation specific to this brief, do not invent one — leave it blank and flag for revisit.** A speculative memory hook is worse than no memory hook.

### Input 4: Imperfections (3-5)
From genius.md GP-11. Pick 3-5 specific moves that will be in the prompt or applied post-generation:
- Asymmetric crop
- Texture overlay (specify: grain / paper / risograph)
- Color punctuation (one accent color in ONE location)
- Off-rotation element (2-7°)
- Element creep (one element overlapping another)
- Subtle blend (logo or motif at low opacity)
- Hand-drawn line / annotation

## Output — 1 Page

```markdown
# Poster Brief — [poster name]

**Surface(s)**: [aspect ratios needed]
**Brand context**: [1-2 lines — what should NOT be repeated visually from prior pieces]

## The Four Decisions
- **Verb**: [...]
- **Visual primitive**: [...] (supporting: [...])
- **Memory hook**: [Move A/B/C/D] — [concrete one-sentence implementation; or BLANK if speculative]
- **Imperfections**: 1) [...]  2) [...]  3) [...]  [4) ...]  [5) ...]

## Generation Prompt for fantastic-posters
[3-6 sentence English prompt that encodes verb energy + primitive + memory hook + imperfections + style refs]

## Forbidden (based on brand context)
- [...]
- [...]

## Post-Generation Audit Chain
1. `/satori-flip-test` (technical structural)
2. `/satori-anti-ai-slop` (verify imperfections survived generation)
3. `/satori-memory-encoding` (verify hook landed) — only if Input 3 had a concrete implementation
```

## Content Type Adaptations

| Poster context | Verb examples | Primitive |
|---|---|---|
| **Capsule launch (streetwear)** | anchors / ignites / disrupts | Asymmetric / sharp angles |
| **Event poster (club / show)** | ignites / pulses / gathers | Asymmetric + hand-drawn |
| **Brand-statement poster** | declares / honors / clarifies | Vertical lines / symmetry |
| **Merch tee print** | claims / signals / honors | Geometric (clarity at small print) |
| **Wheatpaste large format** | confronts / disrupts / invites | Sharp angles + asymmetric |
| **Editorial poster** | excavates / pauses / haunts | Curves / hand-drawn |
| **Premium / luxury** | refines / distinguishes / quiets | Symmetry + restraint |

## Output Requirements

Brief must:
1. Fit on one screen — if it's longer than ~50 lines, you over-thought it
2. Have all 4 inputs filled OR explicitly blanked (no speculative content)
3. Include a generation prompt ready for fantastic-posters (no further translation needed)
4. Include forbidden elements from brand context
5. Reference the post-generation audit chain

## Quality Gate

- [ ] **One verb** locked (not 2+)
- [ ] **Primitive** named with shape psychology rationale
- [ ] **Memory hook** is concrete OR explicitly blank (no speculation)
- [ ] **3-5 imperfections** specified at element level
- [ ] **Generation prompt** is 3-6 sentences (not 200-line spec)
- [ ] **Forbidden** documented (so the AI doesn't repeat prior shipped work)

## Source Grounding

This workflow is the minimum viable pre-flight Satori would run — and nothing more. The 9-step version that previously occupied this slot inflated decisions into busywork; this version cuts to the four that genuinely shape the output.

> *"You, the human designer, are supposed to ruin that template style perfection. And I don't mean in some kind of chaotic way, more like in a bring it to life way."* — Satori on imperfection

> *"Things like shields, arrows, mountains, initials, and so on. And that's usually where generic ideas start to creep in… Instead, I'll try to define the brand in terms of verbs."* — Satori on verb-not-noun

## Memory Note

For my.bpm posters, refer to auto-memory `mybpm-streetwear-brand.md` for brand context (EDM streetwear, PLUR culture, mybpm.store). The verb / primitive / memory hook examples in this workflow are deliberately generic — fill them with brief-specific content, do not borrow speculative examples.

## What Changed (vs Prior Version)

The prior `/satori-poster-think` was 9 steps with speculative my.bpm-specific memory-hook examples (vinyl-pulse-grooves, fingerprint-wristband, glow-stick-waveform) and a grid-by-aspect-ratio table that wasn't grounded in source material. Adversarial review found that the workflow added overhead without speed advantage over running the four decisions mentally and calling `/fantastic-posters` directly. This version is the corrective — 4 inputs, 1-page output, no speculative examples, no over-prescribed grid choices.
