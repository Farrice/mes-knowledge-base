---
description: Filled 1900×10000-px vertical logo presentation — concept → iterations → color → context. Anti-bias structure that compares concepts on strength.
---

# /satori-logo-presentation — Standardized Logo Presentation

Produce the structured client presentation that removes aesthetic confound from concept comparison. Every concept gets the same 1900×10000-px vertical layout. Clients compare *idea strength*, not *presentation polish*.

## Pre-Flight Gate

**Use this when**:
- Presenting 2-4 logo concepts to a client
- Building a logo project's deliverable structure for the first time
- Replacing ad-hoc concept slides with a defensible standardized format

**Do NOT use this when**:
- Presenting a single locked direction (use a simple concept rationale instead)
- The client has explicitly requested a custom presentation format (honor their constraint, document deviation)
- Concepts haven't been generated yet (run `/satori-logo-concept` first)

## Skill Acquisition

Load:
- `genius.md` — GP-10 (Logo as Memory Hook), HK-04 (Presentation Standardization as Anti-Bias)
- `references/source-quotes.md` — Satori's verbatim presentation philosophy

## Execution

### Step 1: Confirm Inputs

Verify you have:
- 2-4 logo concepts (each with one-sentence brief, locked verb + primitive, sketchable description)
- Client name and project context
- Concepts at minimum-viable visual fidelity (not napkin sketch — at least vector outline)

If concepts aren't ready, route to `/satori-logo-concept` first.

### Step 2: Build the Standardized Frame

**Canvas**: 1900 × 10000 px vertical (Satori's default).
**Optional adjustment**: 1080 × N for mobile-first delivery; 1920 × N for ultra-wide projector.

**The frame is identical for every concept presented to this client.** Variations across concepts come ONLY from concept content — never from frame structure.

### Step 3: Section Order (Standard Structure)

Each concept gets these sections in this order:

1. **Concept name + tagline** (top hero, ~600 px height)
   - Concept name (one phrase, e.g., "The Threshold")
   - One-sentence concept tagline ("A doorway-as-protection mark")
2. **The mark — black-on-white** (~1500 px)
   - Primary mark, large, centered
   - No decoration, no shadow, no context — just the mark
3. **The mark — white-on-black** (~1500 px)
   - Inverted version
   - Tests transferability across light/dark
4. **The thinking** (~1200 px)
   - Why this concept (one paragraph, max 80 words)
   - Verb anchor: which verb does this carry?
   - Visual primitive: which primitive carries the verb?
   - Memory hook: what makes it stick?
5. **The iterations** (~1500 px)
   - 3-5 sketches showing the path from initial idea to refined mark
   - Annotated: what changed between iterations and why
6. **Color exploration** (~1000 px)
   - 2-3 color treatments
   - Each annotated: what feeling each treatment carries
7. **In context** (~1500 px)
   - Mockup 1: business card or email signature (intimate scale)
   - Mockup 2: storefront sign or large display (presence scale)
   - Mockup 3: app icon or favicon (thumbnail scale — transferability test)
8. **The decision sentence** (~400 px footer)
   - One-sentence summary of why this concept deserves selection

### Step 4: Maintain Identity Across Concepts

The CRITICAL discipline: every concept presented for this client uses the **identical** frame.

| Concept 1 | Concept 2 | Concept 3 |
|---|---|---|
| 1900×10000 | 1900×10000 | 1900×10000 |
| Same section order | Same section order | Same section order |
| Same hero height | Same hero height | Same hero height |
| Same mockup choices | Same mockup choices | Same mockup choices |
| Same typography for annotations | Same typography for annotations | Same typography for annotations |

Why: this prevents the client from picking the *prettier-presented* concept. They must compare actual concept strength.

### Step 5: Write the Thinking Sections

For each concept's "The Thinking" section, write a concept rationale of ≤80 words.

**Required components**:
- Concept name + one-line distillation
- Verb anchor (one verb, the primary)
- Visual primitive (one primitive, the primary)
- Memory hook (one sentence — what makes it stick)

**Format**:
```
[Concept name]

This mark is built on a single verb: [verb]. The visual primitive is [primitive], chosen because [reason — one short clause].

What makes it lodge in memory: [memory hook description].
```

**Anti-pattern**: Don't write a sales pitch. Don't oversell. The concept either holds on its mechanics or it doesn't — your rationale just makes the mechanics legible.

### Step 6: Decision Section (Final Page)

After the per-concept pages, add a final summary page:

- **Brief recap** (the one-sentence brief shared across all concepts)
- **Comparison table**: concept name + verb + primitive + memory hook (so client can compare on the actual axes)
- **Recommended direction** (designer's pick + 1-sentence reason)
- **Next steps**: refinement window, decision deadline, file delivery format

The recommended direction is your **judgment**, not your only option. The client can override.

### Step 7: Output the Presentation Spec

Produce the build-ready spec for a designer to assemble in Figma / InDesign / Illustrator:

```markdown
# Logo Presentation Spec — [client name]

## Frame
- Canvas: 1900 × 10000 px vertical
- Identical across all [N] concepts

## Section Order (per concept)
[1] Concept name + tagline (~600 px)
[2] Mark — black on white (~1500 px)
[3] Mark — white on black (~1500 px)
[4] The thinking (~1200 px)
[5] The iterations (~1500 px)
[6] Color exploration (~1000 px)
[7] In context — 3 mockups (~1500 px)
[8] Decision sentence (~400 px footer)

## Per-Concept Content

### Concept 1 — [name]
- Tagline: [...]
- Verb anchor: [...]
- Primitive: [...]
- Memory hook: [...]
- Thinking text (≤80 words): [...]
- Iteration count: [...]
- Color treatments: [...]
- Mockup choices: [...]

### Concept 2 — [name]
[same structure]

### Concept 3 — [name]
[same structure]

## Final Decision Page
- Brief recap: [...]
- Comparison table: [...]
- Recommended direction: [...] — [reason]
- Next steps: [...]

## Designer Instructions
[Specific implementation notes — fonts, spacing, mockup sourcing, color modes]
```

## Content Type Adaptations

| Project tier | Concept count | Mockup choices |
|---|---|---|
| **Standard logo** | 3 concepts | Business card / sign / app icon |
| **Premium / brand-system** | 3-4 concepts | Add: print collateral, web header, vehicle wrap (depending on industry) |
| **Personal brand** | 2-3 concepts | LinkedIn avatar / email signature / Substack header |
| **Startup pre-launch** | 3 concepts | App icon / pitch deck cover / merch tee |
| **Real estate agent brand** | 2-3 concepts | Yard sign / business card / Instagram avatar |
| **Local business** | 2-3 concepts | Storefront sign / receipt / Google Maps icon |
| **Streetwear / merch** | 3-4 concepts | Tee print / hang tag / Instagram avatar |

## Output Requirements

Spec must include:
1. Confirmed inputs (concepts ready, fidelity adequate)
2. Standardized frame (1900×10000 default; deviations documented)
3. Section order applied identically to every concept
4. Per-concept content (name + tagline + thinking + iterations + color + mockups + decision)
5. Final decision page (recap + comparison + recommendation + next steps)
6. Designer implementation instructions

## Quality Gate (Genius Rubric)

- [ ] **Identical frame across concepts** — no concept gets fancier treatment
- [ ] **Thinking text ≤80 words** — no sales pitches; mechanics legible
- [ ] **3 mockup scales** — intimate / presence / thumbnail (transferability built in)
- [ ] **Verb + primitive** documented per concept
- [ ] **Recommended direction** present (you're paid for judgment, not just options)
- [ ] **Next steps** documented (decision deadline, refinement window)

## Source Grounding

> *"Every concept we present with a client uses the exact same layout and structure… each client will have its own presentation, but that presentation will stay the same for each concept. And so, if we present three or four ideas, they're not competing based on how they're shown because they're actually competing based on the strength of the idea itself."* — Satori
