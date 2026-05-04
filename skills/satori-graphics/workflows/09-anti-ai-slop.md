---
description: Human-imperfection injection plan — 3+ micro-decisions that distinguish a layout from AI default templates
---

# /satori-anti-ai-slop — Human Imperfection Deployment

AI layouts in 2026 are too perfect — symmetrical, evenly spaced, polished. The human moat is "ruin the perfection in a bring-it-to-life way." This workflow injects 3+ deliberate human-imperfections into any AI-generated or AI-assisted layout heading toward delivery.

## Pre-Flight Gate

**Use this when**:
- A layout was AI-generated (Midjourney, DALL-E, Nano Banana, Skywork, Canva AI)
- A layout was human-made but feels template / generic
- Final layout is heading to delivery and needs the human-quality differentiator
- The brief explicitly demands a human, hand-crafted feel

**Do NOT use this when**:
- The brief calls for clinical / systematic / corporate sterility (medical UI, financial dashboards, government forms) — anti-slop moves degrade trust there
- The design is for accessibility-first contexts where imperfections create cognitive load
- The audience is AI-aware and explicitly wants AI aesthetic (some tech / Web3 / AI-tool brands)
- The asymmetry would compromise legibility or function

## Skill Acquisition

Load:
- `genius.md` — GP-11 (Anti-AI-Slop via Human Imperfection), HK-01 (What Designers Actually Sell), HK-07 (Speed Doesn't Fix Weak Thinking)
- `references/source-quotes.md` — Satori's verbatim anti-AI material

## Execution

### Step 1: Diagnose the AI Tells

Examine the design. Document which AI tells are present:

| AI tell | Symptom | Severity |
|---|---|---|
| **Perfect symmetry** | Center-aligned everything; mirror-balance dominates | High |
| **Even spacing** | All gaps identical; no rhythm variation | High |
| **Default template feel** | Looks like 100 other layouts | High |
| **Evenly distributed elements** | Equal weight across all quadrants | Medium |
| **Stock-photo cleanliness** | Imagery feels untouched, generic | High |
| **Generic palette** | "Professional blue" / "modern gray" without specificity | Medium |
| **Vector-perfect curves** | No hand-feel; mathematically smooth | Medium |
| **Rigid grid adherence** | No breakage; everything in cells | High |
| **Headline-deck-body-CTA stacking** | Default information hierarchy with no creative interpretation | High |
| **Standard aspect ratios** | All elements at default 1:1 / 16:9 / golden ratio | Low |

Score: count of high-severity tells. 3+ = significant slop signal; needs strong intervention.

### Step 2: Lock the Anti-Slop Quota

Decide how many human-imperfections you'll inject. Default by context:

| Context | Imperfection quota |
|---|---|
| Editorial / streetwear / artistic | 5-7 |
| Brand work / hero key visual | 4-5 |
| Product / e-commerce hero | 3-4 |
| Standard ad creative | 3 |
| Corporate / financial | 2-3 (within trust constraints) |
| Tech / SaaS landing | 3-4 |
| Children / family / hospitality | 4-5 (warmth requires hand-feel) |

Minimum: 3. Below 3, the AI-tell signal still dominates.

### Step 3: Choose Imperfection Moves

Select from the human-imperfection library. Each move is a "bring-it-to-life" decision, not chaos:

#### Compositional moves (re-arrange existing elements)
1. **Element creep** — One element creeps over another (bottle creeping over typography, photo edge crossing into the gutter)
2. **Subtle blend** — A logo or motif subtly blended at low opacity across the background
3. **Connecting line** — A hand-drawn or thin line running between distant elements
4. **Controlled crop** — Defy symmetry with an asymmetric crop on a key image
5. **Asymmetric breathing** — More white space on one side than the other (with reason)
6. **Off-rotation** — A glyph or motif at slightly-off rotation (2-7°)

#### Surface moves (texture / treatment)
7. **Tapered gradient** — A gradient that fades off-axis or stops short of an edge
8. **Hand-drawn element** — One drawn line, scribble, or annotation injected into a clean composition
9. **Texture overlay** — A subtle grain, paper, or risograph texture across the layout
10. **Imperfect alignment** — One element 4-8 px off the grid baseline (deliberate, not accidental)

#### Compositional rhythm moves
11. **Rhythm break** — One paragraph one-line; one image full-bleed; one section breathes
12. **Type-size variance** — A non-standard size jump within type hierarchy (instead of 14/24/48, use 14/22/52)
13. **Color punctuation** — One color used in only ONE place (the spot of red in an otherwise neutral layout)
14. **Negative-space asymmetry** — Empty space concentrated on one side, content weighted on the other

#### Imperfection-by-restraint moves
15. **Subtraction** — Remove one element the AI insisted on (decorative line, secondary CTA, tertiary info)
16. **Single-job element** — Replace a multi-job element with one that does one job well
17. **Resist the "balanced corner"** — Leave the balancing corner empty when AI wants symmetry

### Step 4: Validate Each Imperfection Pays Rent

Run each imperfection through the rent test (cross-reference `/satori-why-before-what`):
- **Concept reason**: serves the central idea
- **Hierarchy reason**: guides eye to leverage point
- **Psychology reason**: engineers a specific emotional response

Imperfection without rent = chaos, not character. Reject the move and pick another.

### Step 5: Sequence the Imperfections

Distribute imperfections across the layout — don't cluster them. AI tells live evenly distributed; human moves should also distribute, but **with clusters of intentionality** at the leverage point.

**Distribution rule**: 
- ONE imperfection at or adjacent to the leverage point (anchors the human feel)
- ONE imperfection in a secondary zone (carries the feel through the journey)
- ONE+ imperfection elsewhere (texture-level human signal)

### Step 6: Stress-Test Against Sterile Baseline

Mentally compare:
- **AI baseline**: the original, perfect, symmetric version
- **Anti-slop version**: with imperfections injected

The anti-slop version must:
- Still pass legibility / function tests
- Still pass LIFT (`/satori-lift-audit`)
- Pass predictive empathy (correct next-emotion)
- Feel **more alive**, not chaotic

If it feels chaotic, you over-shot. Reduce imperfection count.

### Step 7: Output the Anti-Slop Spec

```markdown
# Anti-AI-Slop Spec — [layout name]

## AI Tell Diagnosis
- High-severity tells present: [list]
- Total slop signal: [n tells]

## Imperfection Quota
- Context: [...]
- Quota: [n imperfections]

## Injected Moves

### Move 1 — [name]
- Type: [Compositional / Surface / Rhythm / Restraint]
- Specific implementation: [...]
- Rent reason: [Concept / Hierarchy / Psychology + one sentence]
- Location: [near leverage / secondary / texture]

### Move 2 — [name]
[same structure]

### Move 3 — [name]
[same structure]

[continue per quota]

## Distribution Audit
- ONE at leverage point: [✓/✗]
- ONE in secondary zone: [✓/✗]
- ONE+ in texture zones: [✓/✗]

## Stress Test
- Legibility intact: [yes/no]
- LIFT still passes: [yes/no]
- Predictive empathy intact: [yes/no]
- Feels alive vs chaotic: [alive / chaotic]

## Executable Directives
[Specific element-level changes]

## Anti-Pattern Check
- [ ] No imperfections fail rent test
- [ ] No clustering of imperfections (all in one zone)
- [ ] No imperfection compromises legibility
- [ ] At least 3 imperfections injected
- [ ] Imperfections honor visual primitive
```

## Content Type Adaptations

| Content type | Imperfection emphasis | Common failure |
|---|---|---|
| **Streetwear poster** | Asymmetric crop + texture overlay + controlled imbalance | Imperfection clustering at one corner |
| **Real estate listing** | Subtle hand-drawn annotation + asymmetric breathing | Imperfections compromise legibility of price |
| **Newsletter header** | Type-size variance + color punctuation | Decorative scribble that pays no rent |
| **Brand pitch deck** | Off-rotation glyph + element creep | Excessive imperfection on a single slide |
| **Ad creative** | Element creep + subtle blend + tapered gradient | AI tells re-emerge after "polish" pass |
| **Children's brand** | Hand-drawn element + texture overlay | Imperfection feels child-like (cute) instead of warm-crafted |
| **Premium product hero** | Subtle blend + asymmetric breathing + restraint | Over-imperfection cheapens premium feel |
| **Tech / SaaS landing** | Color punctuation + rhythm break + type-size variance | Hand-drawn element breaks tech feel |

## Output Requirements

Spec must include:
1. AI tell diagnosis (with severity)
2. Quota locked (3+ minimum)
3. Each imperfection with type / implementation / rent reason / location
4. Distribution audit (leverage / secondary / texture)
5. Stress test (legibility / LIFT / empathy / alive vs chaotic)
6. Executable directives at element level
7. Anti-pattern checklist

## Quality Gate (Genius Rubric)

- [ ] **3+ imperfections** injected (minimum)
- [ ] **Each imperfection pays rent** (concept / hierarchy / psychology)
- [ ] **Distribution intentional** (not clustered)
- [ ] **Legibility intact**
- [ ] **LIFT still passes** post-injection
- [ ] **Visual primitive honored** (imperfections don't contradict locked primitive)

## Source Grounding

> *"AI layouts in 2025 are almost just too perfect for their own good… everything starts looking like a default template, which to be fair, that's exactly what it is."* — Satori

> *"You, the human designer, are supposed to ruin that template style perfection. And I don't mean in some kind of chaotic way, more like in a bring it to life way."* — Satori

> *"AI can give you the clean version every time, but only you can give the human version. The version with intent, with targeted emotion, and with enough subtle imperfection to actually feel alive."* — Satori

> *"The brands or businesses that hire actual human designers do so for their thinking and their psychological experience in the design space."* — Satori on what designers actually sell
