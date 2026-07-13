---
name: "Satori Graphics — Logo Concept Brief"
source_prompt: born-v2
skill: satori-graphics
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running Satori's **verb-not-noun logo ideation** method. The amateur trap is starting from nouns (shield, arrow, mountain, initial) — generic ideas creep in immediately. The pro starts from verbs: what the brand *does*. Verbs unlock shape psychology; nouns lock you into cliché. You end "let's just sketch" wandering by forcing a one-sentence brief, a verb extraction, and a visual-primitive lock — *before* any concept direction is generated.

> "Things like shields, arrows, mountains, initials, and so on. And that's usually where generic ideas start to creep in… Instead, I'll try to define the brand in terms of verbs." — Satori
> "The Nike swoosh or the Apple logo. These logos do not tell you what these brands do or sell. They act as a memory hook." — Satori

## Input Required

- **[CLIENT BRIEF]** — the raw brief: values, persona, positioning paragraph
- **[INDUSTRY / CATEGORY]** — tech/SaaS, financial/insurance, wellness/lifestyle, industrial/construction, children/family, premium/luxury, social/community, or other
- **[NOUN-HEAVY CONSTRAINTS]** if the client has already fixated on an object ("we want a shield/mountain/arrow") — name it so it can be deliberately routed around, not silently obeyed

## Execution Protocol

### Step 1 — One-Sentence Brief Reduction (halt condition)

Reduce the entire brief — every value, persona, paragraph — to ONE clear sentence. Not polished, not clever: clear. Format: *"A [thing] that [verb] [audience] [outcome/feeling]."* Examples: cybersecurity → "A system that quietly protects your data in the background." Insurance → "A company that gives you calm about the unpredictable." Children's hospital → "A place that turns scary into safe for small humans." Verify: read it aloud — does it land? Show it to a non-designer — do they get it? If you cannot write it, halt and route to brief refinement; you cannot design the logo yet.

### Step 2 — Verb Extraction

List 10 verbs the brand performs for its audience, across categories: action (protects, accelerates, simplifies, connects), state (calms, anchors, steadies, elevates), transformation (translates, converts, transforms, evolves), relational (guides, partners, hosts, holds). From the 10, pick the strongest 1-2: a primary verb (the core action/state) and, optionally, a supporting verb (a secondary nuance). Validate against the one-sentence brief — if the verbs don't match, either the brief or the verbs are wrong.

### Step 3 — Visual Primitive Lock-In

Map the locked verb to its shape psychology:

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

Lock the primary primitive (which one carries the primary verb) and, optionally, a supporting primitive for the supporting verb. Validate against the brief — a "quiet" brief with a "sharp angles" primitive is a mismatch; resolve it before proceeding.

### Step 4 — Generate 3 Concept Directions

Each direction is a different *interpretation* of the same locked verb + primitive, not three random options:

1. **Literal** — the verb + primitive in its most direct shape interpretation.
2. **Metaphorical** — the verb + primitive expressed via a metaphor that opens memory encoding.
3. **Conceptual Inversion** — the verb + primitive expressed via what's absent, implied, or in negative space.

For each direction, document: concept name (one phrase), what it says without saying it (the implied meaning), visual-primitive deployment (how the locked primitive carries the concept), memory hook (what makes it stick — a metaphor, absence, swap, or controlled imbalance), and failure mode (what would weaken this direction in execution).

### Step 5 — Trap Audit (per direction)

| Trap | Audit question |
|---|---|
| Trying to tell the whole story | Does this try to convey product/industry/values all at once? If yes, simplify to anchor + psychology only. |
| Noun-locked thinking | Is this concept primarily an object? If yes, return to Step 2 and re-extract verbs. |
| Decoration without reason | Is there an element that doesn't serve verb/primitive? If yes, evict. |
| Generic visual | Could this be 100 other brands' logo with a color swap? If yes, push more specific. |

### Step 6 — Sketching / Generation Direction (not final)

Produce a concept brief, not a final logo. Per direction: a sketchable description a designer could draw in 5 minutes, an AI-image-generation prompt if applicable, and a 2-3 word visual-primitive descriptor for hand-off.

## Output Contract

A Logo Concept Brief: foundation (one-sentence brief, primary/supporting verb, primary/supporting primitive), exactly 3 concept directions (Literal / Metaphorical / Conceptual Inversion) each with concept name, implied meaning, primitive deployment, memory hook, failure mode, and sketchable description, plus a trap-audit table across all three, and a recommended next step.

## Output Skeleton

```markdown
# Logo Concept Brief — [brand name]

## Foundation
- One-sentence brief: "..."
- Primary verb: [...]
- Supporting verb: [...]
- Primary visual primitive: [...]
- Supporting primitive: [...]

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
| 1 | [✓/✗] | [✓/✗] | [✓/✗] | [✓/✗] |
| 2 | [✓/✗] | [✓/✗] | [✓/✗] | [✓/✗] |
| 3 | [✓/✗] | [✓/✗] | [✓/✗] | [✓/✗] |

## Recommended Next Workflow
[Logo Presentation Deck — or back to brief if foundation is shaky]
```

## Quality Gate

- One-sentence brief documented before any concept work began
- Zero concepts started from a noun — audit confirms verbs drove all three
- Visual primitive locked before any sketching direction
- Each direction names a specific memory hook (not "looks cool")
- The three directions are genuinely distinct, not three variations of one idea
- Trap audit is clean across all three concepts (or flagged and revised)

## Creative Latitude

The three-direction structure (Literal / Metaphorical / Inversion) is the floor; the actual verb chosen, the specificity of the shape psychology, and how far the Metaphorical and Inversion directions push past the obvious are where the concept lives or dies. Favor the verb that is true to the brand but *not* the first one that comes to mind — the second or third verb on the list-of-10 is often the sharper unlock. A concept that could belong to 100 other brands has failed regardless of how cleanly it passes the trap audit.

## Deploy When

Starting a logo project from scratch; a logo direction is wandering and needs re-anchoring; a client gave a noun-heavy brief; or an existing direction feels generic and you can't articulate why. Do not use for wordmark-only work (route to typography tooling) or when brand positioning itself is unsettled.
