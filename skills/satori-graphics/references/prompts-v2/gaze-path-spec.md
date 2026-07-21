---
name: "Satori Graphics — Gaze-Path Spec"
source_prompt: born-v2
skill: satori-graphics
standard: structure-pure-v2
---

## Role & Activation

You are wiring **directional hierarchy** — Satori's path of importance — along a committed layout spine. Hierarchy decides what's seen first; direction decides where the eye goes next. The triad: line of sight · flow of shapes · balance of weight. The benchmark move is the Dazed cover: the amber-lit face wins first fixation, the gaze delivers the eye to a masthead that is deliberately black — engineered paths beat salience defaults.

> "The goal isn't to create movement. It's actually to create a path of importance. Each directional cue should serve the hierarchy by leading from the most dominant focal point to the next in order of relevance." — Satori

## Input Required

- **[SPINE]** — the committed HOOK → SECONDARY → FINISHER (halt if absent)
- **[FIRST-FIXATION GUARANTEE]** — what makes the hook win (size / light / isolation)
- **[DIRECTIONAL ASSETS]** — faces/figures, product angles, background shapes, light sources available (or the photography still to be selected)
- **[SURFACE + TONE]** — editorial/poster/landing/ad/UI; whether literal cues (arrows) are tolerated

## Execution Protocol

### Step 1 — Confirm Spine + First Fixation
Restate the spine. If nothing guarantees the hook wins first, fix hierarchy before wiring direction.

### Step 2 — Inventory What Can Point
Faces/eyes (strongest), body posture, product angles, background shape angles, light gradients, shadows, pattern direction. For unselected photography: define shot-direction requirements — the right image is the one pointing where the journey goes.

### Step 3 — Wire Each Leg
For hook→secondary and secondary→finisher, assign ≥1 carrier: gaze line (frame the next element where the face points; never let a face point off-canvas at nothing) · angled shapes funneling inward (outward angles leak attention) · curves/diagonals for momentum · light/shadow falloff leading to the next beat. Any cue pointing at a non-anchor is a hijack: quiet or evict.

### Step 4 — Salience-Default Check (the Dazed move)
Per anchor: is it loud because the path needs it, or by habit? Where a gaze/angle already delivers the eye, the receiving element may go QUIETER — buying contrast budget for zones that need it. Log every refused default.

### Step 5 — Thumbnail Trace
Verify the wired path reads at ~120px.

## Output Contract

A Gaze-Path Spec: spine + first-fixation guarantee, directional-asset inventory, per-leg wiring table (`LEG → CARRIER(S) → SPECIFIC MOVE`), hijack list, refused salience defaults with reasons, thumbnail verdict — plus shot-direction requirements when photography is unselected. Executable without narration.

## Output Skeleton

```markdown
# Gaze-Path Spec — [layout name]

## Spine
HOOK: [...] (first-fixation via [...]) → SECONDARY: [...] → FINISHER: [...]

## Directional Assets
- [asset]: points [direction]

## Wiring
| Leg | Carrier(s) | Specific move |
|---|---|---|
| Hook → Secondary | [...] | [...] |
| Secondary → Finisher | [...] | [...] |

## Hijacks
- [cue]: QUIET / EVICT — [it pointed at non-anchor X]

## Refused Salience Defaults
- [element]: kept quiet because [path already delivers]

## Photography Requirements (if unselected)
- [shot must point/angle toward ...]

## Thumbnail Verdict
PASS / FAIL → [fix]
```

## Quality Gate

- Every leg carries a named carrier
- No face/figure points off-canvas at nothing
- Every cue serves an anchor; hijacks handled
- ≥1 salience default consciously examined
- Arrow-free unless the brief tolerates literal cues
- Path verified at thumbnail

## Creative Latitude

The Dazed move is the ceiling: the boldest wiring quietly REMOVES emphasis from an anchor because the path already guarantees arrival. Light and shadow are the least-used carriers — reaching for them before shapes is where sophisticated work separates.

## Deploy When

Spine committed and the layout holds faces/figures/angles that can carry direction; imagery selection by pointing direction; arrow-free premium surfaces; viewers reading a design "out of order." Not before a spine exists, and not when the movement mechanics themselves (levels 1–6) are the question.
