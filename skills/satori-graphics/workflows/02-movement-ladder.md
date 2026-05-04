---
description: Engineer movement at the right level (1-6) for any layout brief — directional cues to temporal flow
---

# /satori-movement-ladder — Movement & Flow Engineering

Pick the right level of movement for the brief and produce executable directives. Most designers default to Level 1 (literal arrows) when Level 2-6 would serve better. This workflow forces the level decision *first*, then engineers movement at that level.

## Pre-Flight Gate

**Use this when**:
- Designing flow / journey for any layout from scratch
- A draft layout feels static or aimless
- A draft layout feels chaotic and you suspect competing flows
- You're stuck between "do I add an arrow?" and "do I rely on hierarchy?"

**Do NOT use this when**:
- The layout has no leverage point yet (run `/satori-lift-audit` to identify L first)
- The brief itself is unclear (run `/satori-why-before-what`)
- The format is logo (movement doesn't apply at logo scale)

## Skill Acquisition

Load:
- `genius.md` — GP-04 (Movement Ladder), GP-06 (LIFT — eye dimension)
- `references/movement-flow-ladder.md` — full level taxonomy + selector table

## Execution

### Step 1: Establish the Movement Brief

Document:
- **Format**: poster / web hero / scroll / slide / social tile / reel frame / print spread / ad
- **Audience**: mass / professional / luxury / editorial / brand-conscious
- **Dwell expectation**: skim (<3 sec) / read (10-30 sec) / study (60+ sec) / experience (full attention)
- **Brief energy**: calm-corporate / editorial-engaging / dynamic-bold / luxury-experiential

### Step 2: Select the Movement Level (1-6)

Use the selector table from `references/movement-flow-ladder.md`. Default-by-context recommendations:

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

**Override the default only when the brief energy contradicts it.** Document your override reason in one sentence.

### Step 3: Engineer at the Selected Level

#### If Level 1 — Directional Cues
- Place ONE primary directional element (arrow, gaze, line)
- Origin: leverage point. Destination: secondary information or CTA.
- No secondary arrows; no competing directional cues
- Risk audit: does this read amateur for the audience? If yes, escalate to Level 2.

#### If Level 2 — Hierarchy-Driven Flow
- Establish 3-tier hierarchy: leverage (largest/highest contrast) → primary support → details
- Test: hide all type — does the visual weight still create a flow?
- No literal arrows; the composition itself is the arrow

#### If Level 3 — Multiple Flows
- Define ONE primary route from leverage to closing point
- Define 1-2 micro-routes that branch and reconnect
- Audit: are micro-routes lighter weight than primary? If equal weight, the layout has no primary
- Common move: central section pulls eye into a short loop before reconnecting

#### If Level 4 — Implied Motion
- Choose ONE motion source: repetition / progressive scaling / blur / gradient / directional pattern
- The motion direction must serve the leverage / journey
- Don't combine sources unless the brief calls for kinetic chaos

#### If Level 5 — Flow Disruption
- Place ONE disruption element on the main flow path
- Disruption tools: 45°-rotated block, scribble, half-cut text at edge, sudden contrast block
- Disruption must serve the leverage or the closing message — not just exist for novelty
- ONE disruption only; multiples compound to chaos

#### If Level 6 — Temporal Flow
- Define the four beats explicitly: **Punch → Slow → Pull → Release**
- Punch: full-bleed / dominant element (the impact)
- Slow: layered details (the linger)
- Pull: a directional or contrast move (the re-engagement)
- Release: white space / negative zone (the pause)
- Each beat gets a designated zone; transitions are spacing-driven
- Skip the Release at your peril — rhythm without resolution is exhausting

### Step 4: Stack Levels (Optional, Master Move)

Stacking allowed if you specify ONE primary level. Common stacks:
- Level 2 (hierarchy) + Level 5 (one disruption) = trustable + memorable
- Level 6 (temporal) absorbs Levels 2 + 4 within its beats

**Avoid stacking**:
- Level 1 + Level 5 (literal arrows + disruption = mixed messaging)
- Level 3 (multiple flows) + Level 5 (disruption) without clear primary

### Step 5: Output the Movement Spec

```markdown
# Movement Spec — [layout name]

**Format**: [...]
**Audience / dwell / energy**: [...]
**Selected level**: [1-6] — [name]
**Override?**: [yes/no — if yes, reason]

## Movement Mechanics
- Origin (leverage point): [...]
- Destination (closing point / CTA): [...]
- Path: [describe the journey]
- Tools deployed: [scale / contrast / arrow / disruption / etc.]

## Stacking (if applied)
- Primary level: [...]
- Secondary level: [...]
- Why they coexist: [one sentence]

## Disruption Budget
- Disruptions deployed: [0 or 1]
- Type: [rotated block / scribble / half-cut / contrast / etc.]
- Serves leverage or closing? [yes — explain]

## Risk Check
- Does the level fit the audience? [yes/no — explain]
- Does it scale to thumbnail? [yes/no — note]
- Is there exactly ONE primary flow? [yes/no — fix if no]

## Executable Directives
[Specific element-level changes — what to add, remove, resize, reposition]
```

## Content Type Adaptations

| Content type | Recommended levels | Common failure |
|---|---|---|
| **LinkedIn carousel** | 2 | Trying Level 1 (arrow on every slide = amateur) |
| **Listing reel frame** | 2-3 | Hero photo without weight hierarchy on the type overlay |
| **Streetwear poster** | 4-5 | Level 1 arrows kill streetwear feel; need disruption or implied motion |
| **Pitch deck** | 2-3 | Level 4 (implied motion) on a content slide = distracting |
| **Luxury ad** | 5-6 | Anything below Level 5 underdelivers the brief |
| **Real estate flyer** | 1-2 | Level 5 disruption on a corporate brokerage = wrong tone |
| **Newsletter visual** | 2 | Level 4 (gradient/motion) cheapens long-form reading |
| **Editorial spread** | 3-5 | Level 1 = boring; Level 6 = overengineered for static |

## Output Requirements

Spec must include:
1. Movement brief (format / audience / dwell / energy)
2. Selected level with explicit override reason if non-default
3. Movement mechanics (origin → path → destination)
4. Disruption budget enforced (0 or 1, never 2+)
5. Risk check (audience fit / thumbnail / single primary)
6. Executable directives at element level

## Quality Gate (Genius Rubric)

- [ ] **Single primary flow**: only one Level chosen as primary; secondaries clearly secondary
- [ ] **Disruption discipline**: ≤1 disruption per layout
- [ ] **Audience-fit**: chosen level matches audience expectation (not designer ego)
- [ ] **Thumbnail survival**: Level holds when scaled down (Levels 5-6 most at risk)
- [ ] **Executable**: directives can be implemented without re-asking

## Source Grounding

> *"99% of designers don't consider this temporal flow of time. But if you start to consider it on your designs, you'll begin to create better experiences for your audience."* — Satori, on Level 6
