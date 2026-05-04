---
description: Concept-direction-first logo ideation — one-sentence brief reduction → verb extraction → visual primitive lock → 3 concept directions
---

# /satori-logo-concept — Logo Concept Ideation

End the "let's just sketch" wandering. Produce 3 concept directions with locked visual primitives, derived from verbs (not nouns), validated against a one-sentence brief.

## Pre-Flight Gate

**Use this when**:
- Starting a logo project from scratch
- A logo direction is wandering and needs to be re-anchored
- A client gave a noun-heavy brief ("we want a shield / mountain / arrow")
- An existing logo direction feels generic and you can't articulate why

**Do NOT use this when**:
- Refining an existing logo (use logo refinement workflows or `/satori-flip-test` for technical issues)
- The "logo" is actually a wordmark only (use Kittl typography skill)
- Brand strategy is unsettled — fix positioning first via Greg Hoffman / Dai Media

## Skill Acquisition

Load:
- `genius.md` — GP-07 (Verb-Not-Noun), GP-08 (One-Sentence Brief), GP-09 (Concept-Direction-First / Visual Primitive Lock-In), GP-10 (Logo as Memory Hook)
- `references/source-quotes.md` — Satori's logo verbatim material

## Execution

### Step 1: One-Sentence Brief Reduction

Reduce the entire client brief — every value, persona, paragraph — to ONE clear sentence. Not polished. Not clever. Clear.

**Format**: *"A [thing] that [verb] [audience] [outcome/feeling]."*

**Examples**:
- Cybersecurity → *"A system that quietly protects your data in the background."*
- Insurance → *"A company that gives you calm about the unpredictable."*
- Operating system → *"A platform that keeps you secure and reliable."*
- Children's hospital → *"A place that turns scary into safe for small humans."*

**Verification**:
- Read aloud. Does it land?
- Show to a non-designer. Do they get it?
- If you can't write it, you cannot design the logo. Halt and route to brief refinement.

### Step 2: Verb Extraction

List 10 verbs the brand performs for its audience.

**Verb categories to consider**:
- Action verbs (protects, accelerates, simplifies, connects)
- State verbs (calms, anchors, steadies, elevates)
- Transformation verbs (translates, converts, transforms, evolves)
- Relational verbs (guides, partners, hosts, holds)

From the 10, pick the strongest 1-2 verbs:
- **Primary verb**: the core action / state the brand delivers
- **Supporting verb** (optional): a secondary quality that nuances the primary

**Validation**: Do these verbs match the one-sentence brief? If not, the brief is wrong OR the verbs are wrong.

### Step 3: Visual Primitive Lock-In

Map each verb to its shape psychology. Use the genius.md GP-09 cheat sheet:

| Visual primitive | Psychology |
|---|---|
| Vertical lines | Strength, stability, structure, security |
| Horizontal lines | Calm, peace, reliability, breadth |
| Curves / circles | Friendly, organic, inclusive, soft |
| Sharp angles | Robust, aggressive, technical, modern |
| Asymmetry | Dynamic, modern, energetic |
| Symmetry | Trustworthy, classical, premium |
| Hand-drawn / imperfect | Human, crafted, real, warm |
| Geometric / precise | Systematic, technological, clinical |

**Lock the primary primitive**: which one carries the primary verb?

**Lock a supporting primitive (optional)**: which carries the supporting verb?

**Validation**: Locked primitives must agree with one-sentence brief. If "quiet" is the brief but the primitive is "sharp angles," there's a mismatch.

### Step 4: Generate 3 Concept Directions

Each concept direction is a different *interpretation* of the same locked verb + primitive — not three random options.

**Concept Direction 1 — Literal**: The verb + primitive expressed in the most direct shape interpretation.
- Example: Cybersecurity (verb: protects, primitive: vertical lines) → Vertical bar shielding a smaller form

**Concept Direction 2 — Metaphorical**: The verb + primitive expressed via a metaphor that opens memory encoding.
- Example: Cybersecurity → Vertical lines forming a doorway/threshold (the "passing through" metaphor)

**Concept Direction 3 — Conceptual Inversion**: The verb + primitive expressed via what's *absent*, *implied*, or *negative space*.
- Example: Cybersecurity → A shape made entirely of negative space between vertical bars (the "invisible protection" interpretation)

For each direction, document:
- **Concept name** (one phrase)
- **What it says without saying it** (the implied meaning)
- **Visual primitive deployment** (how the locked primitive carries the concept)
- **Memory hook** (what makes it stick — see GP-10)
- **Failure mode** (what would weaken this direction in execution)

### Step 5: Avoid the Amateur Traps

For each concept, run the trap audit:

| Trap | Audit question |
|---|---|
| **Trying to tell the whole story** | Does this logo try to convey product / industry / values all at once? If yes, simplify to anchor + psychology only. |
| **Noun-locked thinking** | Is this concept primarily an object (shield, arrow, mountain)? If yes, return to Step 2 — re-extract verbs. |
| **Decoration without reason** | Is there an element that doesn't serve verb / primitive? If yes, evict. |
| **Generic visual** | Could this be 100 other brands' logo with a color swap? If yes, the concept is too neutral — push more specific. |

### Step 6: Sketching / Generation Direction (Not Final)

This workflow produces the **concept brief**, not the final logo. Output should be sketchable / promptable but not pixel-final.

For each concept, provide:
- A sketchable description a designer could draw in 5 minutes
- An AI-image-generation prompt (if AI sketching is part of the workflow)
- A 2-3 word visual primitive descriptor (for hand-off to designer / AI)

### Step 7: Output the Logo Concept Brief

```markdown
# Logo Concept Brief — [brand name]

## Foundation
- **One-sentence brief**: "..."
- **Primary verb**: [...]
- **Supporting verb**: [...]
- **Primary visual primitive**: [...]
- **Supporting primitive**: [...]

## Concept Direction 1 — Literal — "[name]"
- What it says without saying it: [...]
- Visual primitive deployment: [...]
- Memory hook: [...]
- Failure mode: [...]
- Sketchable description: [...]
- AI prompt (optional): [...]

## Concept Direction 2 — Metaphorical — "[name]"
[same structure]

## Concept Direction 3 — Conceptual Inversion — "[name]"
[same structure]

## Trap Audit
| Concept | Whole-story? | Noun-locked? | Decoration? | Generic? |
|---|---|---|---|---|
| 1 | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 2 | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3 | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |

## Recommended next workflow
[/satori-logo-presentation to format these for client] OR [back to brief if foundation is shaky]
```

## Content Type Adaptations

| Logo type | Verb emphasis | Primitive emphasis | Common trap |
|---|---|---|---|
| **Tech / SaaS** | Verbs of process (simplifies, automates, transforms) | Geometric / precise | Trying to "look like a tech logo" → genericism |
| **Financial / insurance** | State verbs (steadies, holds, protects) | Vertical / horizontal lines | Noun-locked (shield/lock) without verb anchor |
| **Wellness / lifestyle** | Relational verbs (guides, supports, honors) | Curves / hand-drawn | Over-organic looks unprofessional |
| **Industrial / construction** | Action verbs (builds, constructs, endures) | Sharp angles / vertical | "Bold and strong" cliché — needs specific verb |
| **Children / family** | Transformation verbs (turns scary into safe) | Curves / hand-drawn | Cute trap — sacrifices anchor for friendliness |
| **Premium / luxury** | State verbs (elevates, refines, distinguishes) | Symmetry / precise serifs | Trying to be classic AND modern simultaneously |
| **Social / community** | Relational verbs (connects, hosts, gathers) | Asymmetry / curves | Over-friendly = trust loss |

## Output Requirements

Brief must include:
1. One-sentence brief documented (no concept work without foundation)
2. Verb extraction (10 candidates → 1-2 locked)
3. Visual primitive lock (mapped to verb psychology)
4. 3 concept directions (Literal / Metaphorical / Inversion) each with full structure
5. Trap audit completed for each concept
6. Sketchable / promptable description per concept
7. Recommended next workflow

## Quality Gate (Genius Rubric)

- [ ] **One-sentence brief** documented and verifiable
- [ ] **Verbs not nouns** drove the concepts (audit: how many concepts started from a noun? Should be 0)
- [ ] **Visual primitive locked** before any sketching direction
- [ ] **Memory hook articulated** per concept (not "looks cool" — specific resolve-something or shape psychology)
- [ ] **3 distinct directions** (not 3 variations of the same concept)
- [ ] **Trap audit clean** (no concept fails on whole-story / noun-lock / decoration / genericism)

## Source Grounding

> *"Things like shields, arrows, mountains, initials, and so on. And that's usually where generic ideas start to creep in… Instead, I'll try to define the brand in terms of verbs."* — Satori on verb-not-noun

> *"Before getting too deep into sketching, I'd like to reduce the entire brief or the brand down into one clear sentence."* — Satori on one-sentence brief

> *"The Nike swoosh or the Apple logo. These logos do not tell you what these brands do or sell. They act as a memory hook."* — Satori on logo as anchor
