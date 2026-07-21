---
description: Wire the path of importance along a committed spine — gaze lines, angled shapes, curves/diagonals, and light/shadow nudges, each directional cue serving the hierarchy in order of relevance
---

# 24 — Gaze Path (Directional Hierarchy)

> **/satori-gaze-path** — *"The goal isn't to create movement. It's actually to create a path of importance."* Hierarchy decides what's seen first; direction decides where the eye goes next. This workflow wires the second half.

The triad: **Line of sight · Flow of shapes · Balance of weight.** The Dazed proof: the amber-lit face wins first fixation (hierarchy), her gaze delivers the eye to a masthead that is deliberately **black on a dark ground** — the designer refused the make-it-white salience default because the path was already engineered.

## Pre-Flight Gate

**Use this when**:
- A three-flow spine is committed and the layout contains a face, figure, product angle, or strong shapes that can carry direction
- A layout's anchors are right but viewers report reading it "out of order"
- Photography/imagery selection: choosing WHICH shot based on where it points
- Arrow-free flow is required (editorial, luxury, premium surfaces where literal cues look amateur)

**Do NOT use this when**:
- No spine committed — `/satori-three-flow` first; directional cues serving no hierarchy are decoration
- The brief tolerates literal cues (wayfinding, promo flyers) — movement L1 via `/satori-movement-ladder` is cheaper and fine
- The problem is which element should dominate — that's hierarchy (`/satori-lift-audit`), not direction

## Skill Acquisition

```
Load: skills/satori-graphics/genius.md
  ├─ GP-19 (Directional Hierarchy — the toolkit this deploys)
  ├─ GP-18 (Three-Flow Rule — the spine being wired)
  └─ GP-04 (Movement Ladder — L2 mechanics this rides on)
Load: skills/satori-graphics/references/layout-flow-hierarchy.md
```

## Execution

### Step 1 — Confirm the Spine and the First Fixation

Restate `HOOK → SECONDARY → FINISHER`. Confirm what guarantees the hook wins first fixation (size, light, isolation). If nothing does, fix hierarchy before wiring direction.

### Step 2 — Inventory the Directional Assets

What in the composition can point? Faces/eyes (strongest), body posture, product angles, background shapes/angles, light gradients, shadows, pattern direction. For photography: audit the *available shots* for gaze/angle direction — the right image is the one pointing where the journey goes.

### Step 3 — Wire Each Leg of the Path

For **each leg** (hook→secondary, secondary→finisher) assign at least one carrier:

| Tool | Move | Discipline |
|---|---|---|
| **Gaze line** | Frame the next element close to where the subject's face/eyes point | *"Designers often frame text close to the direction of the subject's gaze"* — never let a face point off-canvas at nothing |
| **Angled shapes** | Background shapes pointing inward funnel focus toward the next beat | Angles that point outward leak attention off the page |
| **Curves / diagonals** | Create momentum that keeps the eye traveling between beats | Curves carry; hard verticals stop |
| **Light & shadow** | Illumination nudges from one element to the next | Brightest zone = current beat; falloff leads to next |

Rule: *"Each directional cue should serve the hierarchy by leading from the most dominant focal point to the next in order of relevance."* A cue pointing at a non-anchor is a hijack — quiet it or evict it.

### Step 4 — The Salience-Default Check (the Dazed move)

For each anchor, ask: am I making this loud because the *path* needs it — or out of habit? If a gaze/angle already delivers the eye, the receiving element may go **quieter** (black masthead, not white) — which buys back contrast budget for zones that need it. Log every refused default.

### Step 5 — Verify and Output

Thumbnail-trace the wired path (GP-18 test). Then output.

Execution prompt: `references/prompts-v2/gaze-path-spec.md`

## Content-Type Adaptations

| Surface | Primary carriers | Note |
|---|---|---|
| **Editorial/cover** | Gaze lines + light | The Dazed pattern; type placement follows the face |
| **Poster** | Angled shapes + diagonals | Buck pattern: mass angle launches the journey |
| **Landing page** | Product angle + light + section shapes | Hero subject should point INTO the copy/CTA, never off-screen |
| **Ad creative** | Athlete/product gaze toward logo or offer | The sports-ad classic |
| **Listing frame** | Architecture lines + light direction | Choose the shot whose lines lead to the text zone |
| **UI** | Card angles, chevrons-as-shapes, illustration gaze | Illustrated mascots must look toward the CTA |

## Output Requirements

A **Gaze-Path Spec**: (1) the spine restated with first-fixation guarantee, (2) directional-asset inventory, (3) per-leg wiring table `LEG → CARRIER(S) → SPECIFIC MOVE`, (4) hijack list (cues quieted/evicted), (5) refused salience defaults with reasons, (6) thumbnail-trace verdict. Photography briefs include shot-direction requirements.

## Quality Gate

Guards anti-patterns **#17 uncommitted journey**, **#1 decoration without reason**, **#7 loud-by-default**.

- [ ] Every leg of the path has a named carrier (no leg rides on hope)
- [ ] No face/figure points off-canvas at nothing
- [ ] Every directional cue serves an anchor; hijacks quieted or evicted
- [ ] At least one salience-default consciously examined (loud only where the path needs it)
- [ ] Path verified at thumbnail size
- [ ] Arrow-free unless the brief explicitly tolerates literal cues

## Related Workflows

- **`/satori-three-flow`** (21) — upstream: the spine this wires
- **`/satori-movement-ladder`** (02) — the mechanics library (this workflow is L2 wiring done deliberately; escalate to L3–L6 as the brief demands)
- **`/satori-contrast-stack`** (22) — partner: contrast makes anchors win; direction moves the eye between them
- **`/satori-perception-gap`** (18) — post-draft proof the wired path transmits
- **`/satori-predictive-empathy`** (07) — when the arrival emotion biases the first fixation
