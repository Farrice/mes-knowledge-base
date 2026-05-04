---
description: Engineer memorability — give the viewer something to resolve. The pause-to-figure-it-out IS the memory being formed.
---

# /satori-memory-encoding — Memory Hook Engineering

Designs become memorable when they require resolution. The pause is the encoding. This workflow engineers a memory hook into any design — logo, key visual, hero, listing thumbnail, ad, social tile.

## Pre-Flight Gate

**Use this when**:
- A design feels "too clean / too safe / too unoriginal"
- The brief explicitly demands memorability (logo, key visual, brand identity)
- A draft is technically correct but emotionally forgettable
- You're designing for an attention-saturated context (social feeds, busy ads)

**Do NOT use this when**:
- The brief calls for transparent / explanatory communication (instructions, wayfinding, legal copy) — memory hooks add friction inappropriate to instructional intent
- The audience needs immediate clarity (emergency comms, accessibility-first contexts)
- Decoration is masquerading as a memory hook (run `/satori-why-before-what` first to confirm intent)

## Skill Acquisition

Load:
- `genius.md` — GP-03 (Memory Encoding via Resolve-Something), HK-08 (Concept Pause = Memory Formation), HOF-02 (vinyl heart), HOF-03 (empty clothes), HOF-04 (Iron Grip)
- `references/source-quotes.md` — Satori's verbatim memory encoding material

## Execution

### Step 1: Audit Current Memorability

Run the **Resolve-Something Test** on the current design:

| Question | Answer |
|---|---|
| Does the design hand-deliver its meaning, or does it require resolution? | [hand / requires] |
| Is there a metaphor, swap, or absence? | [yes/no] |
| Is there at least one element slightly off-balance / off-symmetric? | [yes/no] |
| Would someone *pause* to figure it out, even briefly? | [yes/no] |
| If you closed your eyes 10 seconds later, what would you remember? | [specific element OR nothing] |

If the design is hand-delivering meaning with no resolve-something, it will not encode. Proceed to Step 2.

### Step 2: Choose a Memory-Hook Move

Memory encoding works through one of four moves. Pick ONE primary, optionally add a supporting:

#### Move A — Metaphor Substitution
Replace the literal arrangement with a metaphorical one.

**Examples**:
- Vinyl records arranged as a heart (HOF-02): music = emotion, records = romance. Conceptual twist lodges.
- Books stacked as a staircase: knowledge as climb.
- A keyboard with one key blooming: creativity emerging from routine.

**When to use**: Brand has emotional core (music, family, growth, creativity) that has a natural metaphor.

#### Move B — Absence as Presence
Show what's *not* there. Engineer meaning from negative space or implied form.

**Examples**:
- Empty clothes in a chair (HOF-03): body-shaped absence triggers depersonalization theme.
- A coffee cup ring on a manuscript: the writer who left.
- Footprints leading to nothing: the path interrupted.

**When to use**: Brand has emotional weight around loss, departure, longing, mystery, transition.

#### Move C — Conceptual Swap
Replace one element with another that encodes the brand's verb.

**Examples**:
- Thinker statue with off-switch instead of head: human creativity vs AI (HOF-01).
- A tie that's actually a road map: business as journey.
- A microscope showing a heart instead of cells: research with feeling.

**When to use**: Brand has a conceptual contradiction or paradox at its core (human-vs-tech, art-vs-science, professional-vs-personal).

#### Move D — Controlled Imbalance
Place one element slightly off-grid, off-rotation, or asymmetric — small enough to be deliberate, large enough to demand resolution.

**Examples**:
- Logo subtly blended at the corner of a hero image (HOF-01 lesson): not centered, not standard, but earns its placement.
- A typography line that drops 6° off horizontal across an otherwise rigid layout.
- One column 1.2× wider than the others on a multi-column grid.

**When to use**: Brand calls for sophistication / intrigue without overt metaphor; layout-level memory rather than image-level.

### Step 3: Validate Move Against Brief

The chosen memory-hook move must:
- **Serve the one-sentence brief**: not a random clever idea, but a specific clever idea
- **Honor the visual primitive**: a curve-primitive logo shouldn't sudden-angle for a memory hook
- **Pass predictive empathy**: the resolve-something shouldn't generate the wrong next-emotion (e.g., a horror metaphor for a children's brand)

If the move doesn't pass validation, return to Step 2 with a different move.

### Step 4: Engineer the Resolution Difficulty

The pause must be calibrated:
- **Too easy** (instant readability): no encoding happens; back to hand-delivery
- **Too hard** (viewer gives up): no encoding happens; viewer disengages
- **Goldilocks** (1-3 second pause to "get it"): memory forms

**Calibration tools**:
- **Brief context** can pre-resolve some difficulty (a tagline that hints at the metaphor)
- **Visual familiarity** of the elements can lower difficulty (familiar objects + unfamiliar arrangement = solvable)
- **Color / scale / contrast** can guide resolution (the "key" element gets emphasis)

**Pause-time test**: Show the design to a non-designer, time how long until they "get it." 1-3 seconds = ship. Longer = simplify the resolution. Shorter = make the move more substantial.

### Step 5: Test for Stickiness

After engineering, run the stickiness audit:

- **24-hour test**: If you saw this design once and someone asked you to describe it tomorrow, what would you say?
- **Element specificity**: Could you describe ONE specific element that lodged? (Not "the logo had circles" but "vinyl records as a heart.")
- **Metaphor portability**: Could the audience explain the metaphor to someone else without showing the design?

A passing memory hook generates specific descriptions and portable metaphors. A failing one generates "it was nice / clean / professional."

### Step 6: Output the Memory Hook Spec

```markdown
# Memory Encoding Spec — [design name]

## Current Memorability Audit
- Hand-delivers meaning?: [yes/no]
- Resolve-something present?: [yes/no]
- 10-sec recall: [specific element OR nothing]

## Chosen Move
- **Move type**: [A — Metaphor / B — Absence / C — Swap / D — Imbalance]
- **Specific implementation**: [...]

## Validation Against Foundation
- Serves one-sentence brief?: [yes/no — explain]
- Honors visual primitive?: [yes/no — explain]
- Passes predictive empathy?: [yes/no — confirm next-emotion alignment]

## Resolution Calibration
- Estimated pause time: [1-3 sec target]
- Familiarity tools: [familiar elements used to lower difficulty]
- Resolution guides: [color / scale / contrast cues]

## Stickiness Audit
- 24-hour predicted recall: [...]
- Element specificity: [the one detail that lodges]
- Metaphor portability: [yes/no]

## Executable Directives
[Specific element changes — what to add, remove, swap, reposition]
```

## Content Type Adaptations

| Content type | Recommended move | Common failure |
|---|---|---|
| **Logo** | C (Swap) or A (Metaphor) | Whole-story logos overload the resolve-something |
| **Hero key visual** | A (Metaphor) or B (Absence) | Too literal = no encoding |
| **Listing thumbnail** | D (Imbalance) | Trying for metaphor on small format degrades clarity |
| **Ad creative** | C (Swap) or A (Metaphor) | Stat-led ads have no resolve-something |
| **Social tile** | A or D — depending on platform | Square-feed conformity kills resolve-something |
| **Editorial spread** | A or B (Absence) | Decoration mistaken for memory encoding |
| **Pitch deck cover** | C (Swap) | Generic concept = forgettable deck |
| **Streetwear graphic** | A or C — bold metaphors | Symbol stacking without cohesion |
| **Newsletter visual** | B (Absence) or D (Imbalance) | Hand-delivery via topical illustration |
| **Brand identity card** | D (Imbalance) | Symmetric perfection kills lodging |

## Output Requirements

Spec must include:
1. Current memorability audit (with specific recall test)
2. Chosen move (one primary, optionally one supporting)
3. Validation against foundation (brief + primitive + empathy)
4. Resolution calibration (pause time targeted, tools deployed)
5. Stickiness audit (24-hour, specificity, portability)
6. Executable directives

## Quality Gate (Genius Rubric)

- [ ] **One primary move** chosen (not 3+ competing)
- [ ] **Move serves brief** — not random cleverness
- [ ] **Pause-time calibrated** — 1-3 sec target validated
- [ ] **Stickiness audit passes** — specific recall + portable metaphor
- [ ] **Predictive empathy intact** — memory hook doesn't generate wrong emotion
- [ ] **Visual primitive honored** — encoding move agrees with locked primitive

## Source Grounding

> *"This is the art of giving the viewer something to resolve — something slightly off-balance. Something that whispers a question instead of handing out an answer."* — Satori

> *"Two LPs and one album sleeve suddenly transformed into a metaphor. Music becomes emotion. Records become romance. And this single conceptual twist actually lodges itself into memory because your brain recognizes the intention and the meaning."* — Satori on metaphor substitution

> *"No person, no face, just a body-shaped absence. It instantly triggers a psychological reaction within the audience."* — Satori on absence as presence
