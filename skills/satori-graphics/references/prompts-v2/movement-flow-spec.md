---
name: "Satori Graphics — Movement & Flow Spec"
source_prompt: born-v2
skill: satori-graphics
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are engineering movement using Satori's **Movement & Flow Ladder** — a 6-level hierarchy from literal directional cues to temporal (musical) rhythm. Most designers default to Level 1 when Level 2-6 would serve the brief better; your job is to force the level decision *first*, then engineer movement at that level deliberately.

> "99% of designers don't consider this temporal flow of time. But if you start to consider it on your designs, you'll begin to create better experiences for your audience." — Satori

## Input Required

- **[FORMAT]** — poster / web hero / scroll / slide / social tile / reel frame / print spread / ad
- **[AUDIENCE]** — mass / professional / luxury / editorial / brand-conscious
- **[DWELL EXPECTATION]** — skim (<3 sec) / read (10-30 sec) / study (60+ sec) / experience (full attention)
- **[BRIEF ENERGY]** — calm-corporate / editorial-engaging / dynamic-bold / luxury-experiential
- **[LEVERAGE POINT]** — the design's established focal element (movement cannot be engineered without a leverage point already identified — if none exists, halt and route to a LIFT audit or composition-foundations pass first)

## Execution Protocol

### Step 1 — Establish the Movement Brief

Document format, audience, dwell expectation, brief energy from the inputs above.

### Step 2 — Select the Movement Level (1-6)

Use context defaults, then override only when the brief energy contradicts it (document the override reason in one sentence):

| Context | Default level |
|---|---|
| Wayfinding / mass-audience | 1 |
| LinkedIn carousel / social tile | 2 |
| Magazine editorial spread | 3-4 |
| Streetwear / brand-forward poster | 4-5 |
| Luxury campaign / Apple-tier page | 6 |
| Real estate listing reel | 2-3 |
| Newsletter article header | 2 |
| Brand pitch deck | 2-3 |

### Step 3 — Engineer at the Selected Level

- **Level 1 — Directional Cues**: one primary directional element (arrow/gaze/line) only; origin = leverage point, destination = secondary info or CTA; no competing cues. If this reads amateur for the audience, escalate to Level 2.
- **Level 2 — Hierarchy-Driven Flow**: 3-tier hierarchy (leverage → primary support → details) via size/contrast alone; test by hiding all type — does visual weight still create flow? No literal arrows.
- **Level 3 — Multiple Flows**: one primary route from leverage to closing point + 1-2 lighter-weight micro-routes that branch and reconnect. If micro-routes match primary's weight, there is no primary — fix.
- **Level 4 — Implied Motion**: one motion source only (repetition / progressive scaling / blur / gradient / directional pattern), direction must serve the leverage/journey; don't combine sources unless the brief calls for kinetic chaos.
- **Level 5 — Flow Disruption**: exactly one disruption element on the main path (45°-rotated block, scribble, half-cut text at edge, sudden contrast block); it must serve leverage or the closing message, never exist for novelty alone.
- **Level 6 — Temporal Flow**: define four beats explicitly — Punch (full-bleed/dominant impact) → Slow (layered-detail linger) → Pull (directional/contrast re-engagement) → Release (white-space pause). Each beat gets a designated zone; transitions are spacing-driven. Never skip Release — rhythm without resolution exhausts the viewer.

### Step 4 — Stack Levels (Optional, Master Move)

Stacking is allowed only if one primary level is specified. Sound stacks: Level 2 + one Level 5 disruption ("trustable + memorable"); Level 6 absorbing Levels 2+4 within its beats. Avoid: Level 1 + Level 5 (mixed messaging), Level 3 + Level 5 without a clear primary.

### Step 5 — Risk Check

Does the level fit the audience (not designer ego)? Does it scale to thumbnail? Is there exactly ONE primary flow?

## Output Contract

A Movement Spec: movement brief, selected level with explicit override reasoning if non-default, movement mechanics (origin → path → destination), stacking rationale if applied, disruption budget enforced at 0 or 1 (never 2+), risk check, and element-level executable directives.

## Output Skeleton

```markdown
# Movement Spec — [layout name]

**Format**: [...]
**Audience / dwell / energy**: [...]
**Selected level**: [1-6] — [name]
**Override?**: [yes/no — if yes, one-sentence reason]

## Movement Mechanics
- Origin (leverage point): [...]
- Destination (closing point / CTA): [...]
- Path: [...]
- Tools deployed: [...]

## Stacking (if applied)
- Primary level: [...]
- Secondary level: [...]
- Why they coexist: [one sentence]

## Disruption Budget
- Disruptions deployed: [0 or 1]
- Type: [...]
- Serves leverage or closing? [yes — explain]

## Risk Check
- Audience fit: [yes/no — explain]
- Thumbnail survival: [yes/no]
- Single primary flow: [yes/no — fix if no]

## Executable Directives
[element-level: add / remove / resize / reposition]
```

## Quality Gate

- Exactly one Level chosen as primary; any secondary is explicitly subordinate
- Disruption discipline held — ≤1 disruption per layout
- Chosen level matches audience expectation, not designer preference
- Level 5-6 choices confirmed to survive thumbnail scale
- Directives are executable without re-asking

## Creative Latitude

The level ladder is a decision framework, not a formula — the creative work is in *which* motion source, *which* disruption, *what* the four Level-6 beats actually contain for this specific brief. Push toward the level that genuinely fits the brief energy even when it's the harder-to-execute one (Level 5-6 over the safe default Level 1-2), and be willing to name when stacking creates a genuinely new rhythm rather than defaulting to the two "sound" stacks listed.

## Deploy When

Designing flow/journey for any layout from scratch; a draft layout feels static or aimless; a draft feels chaotic from competing flows; or you're stuck between "add an arrow?" and "rely on hierarchy?" Do not use before a leverage point exists (run a LIFT audit first) or when the format is a logo.
