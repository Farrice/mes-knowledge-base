---
name: "Satori Graphics — Logo Presentation Deck Spec"
source_prompt: born-v2
skill: satori-graphics
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are building Satori's **standardized logo presentation** — a structure engineered to remove aesthetic confound from concept comparison. Every concept presented to a given client gets the identical frame, so the client compares *idea strength*, not *presentation polish*. This is presentation-standardization-as-anti-bias (HK-04): a defensible structure a designer can build in Figma/InDesign/Illustrator without re-asking.

> "Every concept we present with a client uses the exact same layout and structure… each client will have its own presentation, but that presentation will stay the same for each concept. And so, if we present three or four ideas, they're not competing based on how they're shown because they're actually competing based on the strength of the idea itself." — Satori

## Input Required

- **[LOGO CONCEPTS]** — 2-4 concepts, each with a one-sentence brief, locked verb + primitive, and sketchable description (output of the Logo Concept Brief prompt; at minimum vector-outline fidelity, not napkin sketches)
- **[CLIENT NAME / PROJECT CONTEXT]**
- **[PROJECT TIER]** — standard logo / premium brand-system / personal brand / startup pre-launch / real-estate agent brand / local business / streetwear-merch (drives mockup selection)

## Execution Protocol

### Step 1 — Confirm Inputs

Verify 2-4 concepts exist at minimum-viable fidelity. If not ready, halt and route to the Logo Concept Brief prompt first.

### Step 2 — Build the Standardized Frame

Canvas: **1900 × 10000 px vertical** (default). Optional adjustments: 1080 × N for mobile-first delivery, 1920 × N for ultra-wide projector. **The frame is identical for every concept shown to this client** — variation comes only from concept content, never from frame structure.

### Step 3 — Section Order (fixed, identical per concept)

1. Concept name + tagline (top hero, ~600px)
2. The mark — black-on-white (~1500px): primary mark, large, centered, no decoration/shadow/context
3. The mark — white-on-black (~1500px): inverted, tests light/dark transferability
4. The thinking (~1200px): why this concept, one paragraph max 80 words — verb anchor, visual primitive, memory hook
5. The iterations (~1500px): 3-5 sketches from initial idea to refined mark, annotated with what changed and why
6. Color exploration (~1000px): 2-3 treatments, each annotated with the feeling it carries
7. In context (~1500px): three mockup scales — intimate (business card/email signature), presence (storefront sign/large display), thumbnail (app icon/favicon — the transferability test)
8. The decision sentence (~400px footer): one sentence on why this concept deserves selection

### Step 4 — Maintain Identity Across Concepts

Confirm every concept uses identical: canvas size, section order, hero height, mockup choices, annotation typography. This prevents the client from picking the prettier-presented concept instead of the stronger idea.

### Step 5 — Write the Thinking Sections (≤80 words each)

Format: *"[Concept name]. This mark is built on a single verb: [verb]. The visual primitive is [primitive], chosen because [reason — short clause]. What makes it lodge in memory: [memory hook description]."* Anti-pattern: no sales pitch, no overselling — the mechanics either hold or they don't; the rationale just makes them legible.

### Step 6 — Decision Section (final page)

Brief recap (shared one-sentence brief), comparison table (concept name + verb + primitive + memory hook — comparable axes), recommended direction (designer's judgment + one-sentence reason — the client can override, but a recommendation is what's being paid for), and next steps (refinement window, decision deadline, file delivery format).

### Step 7 — Mockup Selection by Project Tier

| Project tier | Concept count | Mockup choices |
|---|---|---|
| Standard logo | 3 | Business card / sign / app icon |
| Premium / brand-system | 3-4 | + print collateral, web header, vehicle wrap (industry-dependent) |
| Personal brand | 2-3 | LinkedIn avatar / email signature / Substack header |
| Startup pre-launch | 3 | App icon / pitch deck cover / merch tee |
| Real estate agent brand | 2-3 | Yard sign / business card / Instagram avatar |
| Local business | 2-3 | Storefront sign / receipt / Google Maps icon |
| Streetwear / merch | 3-4 | Tee print / hang tag / Instagram avatar |

## Output Contract

A Logo Presentation Spec: confirmed inputs, standardized frame (canvas + identical-across-concepts confirmation), section order applied identically, per-concept content filled for all 8 sections, a final decision page (recap + comparison + recommendation + next steps), and designer implementation instructions (fonts, spacing, mockup sourcing, color modes).

## Output Skeleton

```markdown
# Logo Presentation Spec — [client name]

## Frame
- Canvas: 1900 × 10000 px vertical
- Identical across all [N] concepts

## Section Order (per concept)
[1] Concept name + tagline (~600px)
[2] Mark — black on white (~1500px)
[3] Mark — white on black (~1500px)
[4] The thinking (~1200px)
[5] The iterations (~1500px)
[6] Color exploration (~1000px)
[7] In context — 3 mockups (~1500px)
[8] Decision sentence (~400px footer)

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
[fonts, spacing, mockup sourcing, color modes]
```

## Quality Gate

- Identical frame across every concept — no concept gets fancier treatment
- Every "thinking" text is ≤80 words with no sales-pitch language
- Three mockup scales present for every concept — intimate / presence / thumbnail
- Verb + primitive documented per concept
- A recommended direction is present (not just options dumped on the client)
- Decision deadline and refinement window are documented

## Creative Latitude

The frame is rigid by design — the latitude lives in the thinking-text prose (make the mechanics legible without selling), the iteration narrative (show real evolution, not backfilled justification), and the honesty of the recommendation. A recommendation that hedges between two concepts is a failed recommendation; name the winner and defend it on mechanics.

## Deploy When

Presenting 2-4 logo concepts to a client; building a logo project's deliverable structure for the first time; or replacing ad-hoc concept slides with a defensible standardized format. Do not use for a single locked direction, or before concepts have been generated (run the Logo Concept Brief prompt first).
