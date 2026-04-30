---
name: creative-direction
description: World-class creative direction — art direction, AI prompt engineering, storyboarding, mood boards, streetwear design, trailer storytelling, and visual brand systems. Covers Higgsfield, Kittl, Midjourney, and Flux platforms.
---

# Creative Direction

Elite creative direction skill covering the full spectrum from concept to production-ready output. Combines cinematography, graphic design, streetwear design, AI production, and narrative storytelling into a unified creative intelligence.

## When to Use

- Art direction for any visual concept (campaigns, brands, products, content)
- AI prompt generation for Higgsfield, Kittl, Midjourney, Flux
- Storyboarding and multi-shot sequence planning
- Mood board construction (5-layer system)
- Streetwear/apparel graphic design with production specs
- Applying trailer storytelling to any content format
- Creative review and critique (the Virgil Test)
- Brand visual identity systems
- Node-based production pipeline design (Kittl Flows, Higgsfield CS 3.0)

## Core Frameworks

### The Three Anchors (Concept Development)
Every strong concept has:
1. **Visual Hook** — The first thing that grabs attention
2. **Emotional Core** — The feeling that sustains engagement
3. **Cultural Anchor** — The reference point that creates meaning

### The 5-Layer Mood Board System
1. Color (hex codes + emotional reasoning)
2. Texture (material qualities + AI keywords)
3. Typography (pairings + hierarchy)
4. Photography/Image Direction (shot types, lighting, composition)
5. Cultural References (film, music, fashion, architecture, art)

### The 4-Act Trailer Structure
1. **The World** (0-30s) — Establish setting, tone, "normal"
2. **The Disruption** (30-60s) — Conflict, stakes, the change
3. **The Escalation** (60-90s) — Maximum intensity, emotional peak
4. **The Resolve** (90-120s) — Final hook, open loop, CTA

### The Virgil Abloh Method
- **3% Rule** — Change 3% of something existing; genius is knowing WHICH 3%
- **Readymade Principle** — Selection IS the creative act
- **DJ Philosophy** — Selection, sequencing, mixing of references
- **Quotation Mark Technique** — Transform labels into commentary

### Platform Selection Matrix
| Need | Platform |
|---|---|
| Cinematic video | Higgsfield CS 3.0 (Veo 3.1) |
| Photorealistic photos | Flux Pro |
| Artistic/stylized | Midjourney v6 |
| Graphic design | Kittl Image Board |
| Design-to-video | Kittl Video Board |
| Character consistency | Higgsfield + SoulID |
| Quick social | Kittl + Seedance 1.5 Pro |

### Render Backend Router (in-stack image generation)

Once the strategic call is made (concept, mood, style family), route to the right render backend:

| Brief shape | Backend | Why |
|---|---|---|
| Photoreal, cinematic, character-driven, scene-specific | `execution/generate_image.py` (Gemini Nano Banana 2) | Best at photoreal + scene composition; cheaper at scale |
| Stylized poster, typographic, vintage / Swiss / Ukiyo-e / brutalism / neon-noir / editorial | `skills/fantastic-posters/` (Fal + GPT Image 2) | 33 curated styles + auto-picker; GPT Image 2 stronger at typographic poster aesthetics |
| Ad creative / lookbook / lifestyle still | Either — Gemini for photoreal, fantastic-posters `streetwear-lookbook` style for editorial |
| Real estate listing poster | `skills/fantastic-posters/` `luxury-real-estate` or `luxury-estate-cover` styles | Native-fit styles purpose-built for the use case |
| Strategy brief / deliverable cover | `skills/fantastic-posters/` `corporate-report` / `swiss-minimal-typo` / `editorial-fashion` | Premium typographic covers |

**Rule of thumb**: if the brief mentions a *style family* by name (vintage, Swiss, brutalist, neon-noir, vapor, editorial, etc.) → fantastic-posters. If it mentions a *real scene* (a person doing something, a specific environment, a product photographed in context) → Gemini.

**Budget**: fantastic-posters runs on a $20 Fal wallet (refills at $5). Every call MUST go through `execution/fal_budget_guard.py check` first. Full policy: `directives/fal-usage-policy.md`. The guard blocks single calls > $1.00, daily spend > $4.00, cycle spend > $15.00, and rate-limits to 5 calls / 5 min.

## Workflows

| Workflow | File | Deliverable |
|---|---|---|
| Art Direction | `.agent/workflows/art-direct.md` | 3 concept directions + execution specs + prompts |
| AI Prompt Generation | `.agent/workflows/creative-prompt.md` | 3-variant platform-specific prompts |
| Storyboard | `.agent/workflows/storyboard.md` | Multi-shot sequence with connected prompts |
| Mood Board | `.agent/workflows/mood-board.md` | 5-layer strategic mood board brief |
| Design Spec | `.agent/workflows/design-spec.md` | Production-ready graphic design specs |
| Trailer Treatment | `.agent/workflows/trailer-treatment.md` | 4-act narrative framework for any content |
| Creative Review | `.agent/workflows/creative-review.md` | Virgil Test critique + specific improvements |

## Deep Reference

For complex or high-stakes creative work, load `genius.md` which contains the compressed encyclopedia across all 6 knowledge domains (visual language, creative direction, AI prompting, streetwear, trailer storytelling, node workflows).

For maximum depth, the full uncompressed knowledge bases and guides live in `knowledge/creative-direction/`.
