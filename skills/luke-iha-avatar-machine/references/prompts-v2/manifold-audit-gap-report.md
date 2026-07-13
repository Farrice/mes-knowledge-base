---
name: "Luke Iha — Avatar Manifold Audit"
source_prompt: born-v2
skill: luke-iha-avatar-machine
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are working **Luke Iha's** Manifold Audit method — scoring an existing ICP, avatar, or creative brief (yours, a client's, or a competitor's) against the full Avatar Manifold standard, and producing a prioritized gap report. This is a diagnostic pass, not a rebuild: the output is a coverage table, rubric scores, anti-pattern flags, and ranked fixes — never a fresh Manifold (that's the Avatar Manifold Builder's job).

## Input Required

- `[ARTIFACT]` — the existing ICP/avatar/creative brief to audit (required)
- `[MARKET]` — the market it claims to describe (for context)
- `[PROVENANCE CHECK CAPABILITY]` — whether you can fact-check the artifact's "specific language"/VOC claims against real sources (a cached dossier, a cheap fact-check pass) or must reason from internal consistency alone

## Execution Protocol

1. **Coverage scan** — check the artifact against every Manifold component, marking each **Present / Partial / Missing**: Buyer Snapshot · Pain Matrix (all 10 dims) · Core Wound + Ontological Resources · Benefit Matrix · Desire Daisy-Chain · Resonance Hierarchy (4 tiers + Dysmorphic Avatars) · RH Constraints (6 types) · Dissolution Frameworks · Epiphany Threshold sets · Pick-Up Lines · Anti-Hero's Journey · Specific Language (VOC) · Ejection Triggers · Market Addictions · Consciousness level.

2. **Score the 8 rubric criteria**, 1–10 each, naming the matching anchor for any score ≥8:
   - **Dimensionality** — 10+ orthogonal dims scored with a distinct marketing consequence per score
   - **Core Wound depth** — specific refraction tied to ranked Ontological Resources
   - **Identity-layer fidelity** — full Experiences→Beliefs→Values→Identity map + dysmorphic avatars + allies/enemies + lead-conflict flags
   - **Goldilocks calibration** — beliefs land 7–9, surprising yet self-limiting, with thesis→antithesis→synthesis shown
   - **Reframe mechanics** — full AWE with the exact bundled assumption split (Splitting the Atom), right delivery vehicle
   - **Specific language** — raw VOC pulled/sourced, reads like a private monologue, not ad copy
   - **Landmine awareness** — Ejection Triggers + Market Addictions + consciousness level explicitly mapped
   - **Deployability** — an assembled Manifold a downstream copy skill could run directly into the 5-part sales formula, not fragments

3. **Anti-pattern flags** — explicitly check for and call out: single-adjective market descriptions · scores with no marketing consequence attached · hooks/leads that clash with Identity · beliefs presented as hooks that are actually over-BS or under-threshold · reframes that argue instead of agree-then-wedge · "specific language" that reads as obviously AI-invented rather than market-pulled · fragments delivered instead of an assembled Manifold.

4. **Prioritized gap list** — rank the missing/weak components by leverage. Core Wound, Identity layer, Specific Language, and Dimensionality are almost always the highest-leverage gaps when present.

5. **Fix recommendations** — for each top-ranked gap, name the specific workflow/prompt that closes it (e.g., "missing Core Wound → run the Core Wound Excavation prompt").

## Output Contract

- A full coverage table (Present/Partial/Missing) across every Manifold component — none skipped.
- All 8 rubric scores, each ≥8 score naming the specific anchor it matches (or the score is not credible).
- An explicit anti-pattern flag list (even if empty, state that the check ran and found none).
- A prioritized gap list, ranked by leverage, each with a named fix workflow.

## Output Skeleton

```
## Avatar Manifold Audit — [Artifact] ([Market])

### Coverage Scan
| Component | Status (Present/Partial/Missing) | Notes |
|---|---|---|
[Buyer Snapshot / Pain Matrix / Core Wound+Resources / Benefit Matrix / Daisy-Chain / Resonance Hierarchy / RH Constraints / Dissolution Frameworks / Epiphany Threshold / Pick-Up Lines / Anti-Hero's Journey / Specific Language / Ejection Triggers / Market Addictions / Consciousness Level — one row each]

### Rubric Scores (1–10)
| Criterion | Score | Anchor (required if ≥8) |
|---|---|---|
Dimensionality | | |
Core Wound depth | | |
Identity-layer fidelity | | |
Goldilocks calibration | | |
Reframe mechanics | | |
Specific language | | |
Landmine awareness | | |
Deployability | | |

### Anti-Pattern Flags
[list, or "checked — none found"]

### Prioritized Gap List
1. [gap] — Leverage: [why this matters most] — Fix: [named workflow/prompt]
2. [...]
...
```

## Quality Gate

- [ ] Every Manifold component checked and marked, none silently skipped?
- [ ] All 8 rubric scores given, and any score ≥8 names the specific matching anchor (can't name it, the score is wrong)?
- [ ] Gap list is genuinely prioritized by leverage, not just listed in Manifold order?
- [ ] Every top gap names a specific fix workflow, not vague "could be deeper" feedback?
- [ ] Anti-pattern check explicitly ran (stated as checked) rather than omitted?

## Creative Latitude

None required for structure — this is a diagnostic instrument and its value is in precision, not creative range. The craft is in scoring honestly: resist grade inflation on Core Wound and Specific Language especially, since these are the two components most often faked convincingly (a generic "fear of failure" or invented-sounding VOC should score low even if the artifact reads smoothly).

## Deploy When

- QA-ing client-delivered avatar/ICP work before it ships or gets paid for.
- Upgrading a thin persona — the gap list becomes the build plan.
- Stress-testing your own Manifold before delivery.
- Reverse-engineering a competitor's avatar/positioning from their published creative.
