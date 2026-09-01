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
- Reference-first moodboard orchestration: discovery/brief → three visual territories → blind choice → proving surface → selected-direction handoff
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

### The Connected Moodboard System
1. **Intent and evidence lock** — one objective, decision, audience, felt target, constraint set, and proof state
2. **Reference acquisition** — inspectable visual sources with bounded roles and rights/provenance
3. **Three visual territories** — genuinely different worlds, not palette variations
4. **Five-layer executor keys** — color, material, typography, image direction, and cultural lineage beneath each actual board
5. **Comparative proving surface** — the same real surface rendered through A/B/C
6. **Blind taste decision** — Choose / Keep / Kill before the rationale or recommendation is revealed
7. **Selected-direction handoff** — one locked world passed to DESIGN.md, art direction, storyboarding, or production

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

### Render Backend Router (in-stack image + video generation)

Once the strategic call is made (concept, mood, style family), route to the right render backend:

| Brief shape | Backend | Why |
|---|---|---|
| Photoreal, cinematic, character-driven, scene-specific | `execution/generate_image.py` (Gemini Nano Banana 2) | Best at photoreal + scene composition; cheaper at scale |
| Stylized poster, typographic, vintage / Swiss / Ukiyo-e / brutalism / neon-noir / editorial | `skills/fantastic-posters/` (Fal + GPT Image 2) | 33 curated styles + auto-picker; GPT Image 2 stronger at typographic poster aesthetics |
| Ad creative / lookbook / lifestyle still | Either — Gemini for photoreal, fantastic-posters `streetwear-lookbook` style for editorial |
| Real estate listing poster | `skills/fantastic-posters/` `luxury-real-estate` or `luxury-estate-cover` styles | Native-fit styles purpose-built for the use case |
| Strategy brief / deliverable cover | `skills/fantastic-posters/` `corporate-report` / `swiss-minimal-typo` / `editorial-fashion` | Premium typographic covers |
| **Image edit** (brand swap, copy variant, ref-anchored regen) | `skills/fantastic-posters/` `gen.sh --refs=...` | GPT Image 2 edit endpoint; handled by existing generate.js |
| **Video — multi-shot narrative trailer** | `skills/fantastic-posters/` `fal_video_kling.py` (Kling v3 Pro) | Only model with `multi_prompt` for distinct scene cuts; supports custom element references |
| **Video — cinematic single-shot, lipsync-grade audio, start→end transition** | `skills/fantastic-posters/` `fal_video_seedance.py` (Seedance 2.0 720p) | Premium synchronized audio + frame interpolation |
| **Video — short ambient motion, social trailer** | `skills/fantastic-posters/` `fal_video_kling.py` (5s, audio on, $0.84) | Cheapest path that still feels cinematic |
| **Video — full live-action / cinematic narrative ≥15s** | Higgsfield CS 3.0 (Veo 3.1) | Out of fantastic-posters scope; superior for true cinematic work |

**Bridge pattern**: posters generated by `gen.sh` become natural input frames for `fal_video_*` wrappers. Generate the still first, lock the winner, then animate. Always pre-flight via `python3 execution/fal_budget_guard.py check --mode=<...>`.

**Rule of thumb**: if the brief mentions a *style family* by name (vintage, Swiss, brutalist, neon-noir, vapor, editorial, etc.) → fantastic-posters. If it mentions a *real scene* (a person doing something, a specific environment, a product photographed in context) → Gemini.

**Budget (mode-aware as of 2026-04-30)**: fantastic-posters runs on a $20 Fal wallet (refills at $5). Every call MUST go through `execution/fal_budget_guard.py check --mode=<...>` first. Full policy: `directives/fal-usage-policy.md`. Per-call ceilings: poster $1.00, edit $1.00, kling $2.00, seedance-480p $1.50, seedance-720p $3.00, seedance-1080p HARD-BLOCKED. Daily cap $6.00, cycle cap $15.00, rate-limit 5 calls / 5 min, halt after 2 consecutive failures.

## Workflows

| Workflow | File | Deliverable |
|---|---|---|
| Art Direction | `.agent/workflows/art-direct.md` | 3 concept directions + execution specs + prompts |
| AI Prompt Generation | `.agent/workflows/creative-prompt.md` | 3-variant platform-specific prompts |
| Storyboard | `.agent/workflows/storyboard.md` | Multi-shot sequence with connected prompts |
| Mood Board | `.agent/workflows/mood-board.md` | Three reference-locked visual boards + comparative proving surface + blind taste decision + selected-direction handoff |
| Design Spec | `.agent/workflows/design-spec.md` | Production-ready graphic design specs |
| Trailer Treatment | `.agent/workflows/trailer-treatment.md` | 4-act narrative framework for any content |
| Creative Review | `.agent/workflows/creative-review.md` | Virgil Test critique + specific improvements |

## Deep Reference

For complex or high-stakes creative work, load `genius.md` which contains the compressed encyclopedia across all 6 knowledge domains (visual language, creative direction, AI prompting, streetwear, trailer storytelling, node workflows).

For maximum depth, the full uncompressed knowledge bases and guides live in `knowledge/creative-direction/`.

The connected runtime contract and repair boundary live at
`docs/mission-artifacts/mood-board-orchestrator-repair/CONTRACT.md`. The
five-layer method remains the executor grammar under each board; it is no longer
treated as a complete moodboard deliverable by itself.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

7 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Creative Direction — AI Prompt Generation (3-Variant, Platform-Specific)** — `skills/creative-direction/references/prompts-v2/ai-prompt-generation.md`
- **Creative Direction — Art Direction (3 Concept Directions)** — `skills/creative-direction/references/prompts-v2/art-direction.md`
- **Creative Direction — Creative Review (The Virgil Test Critique)** — `skills/creative-direction/references/prompts-v2/creative-review.md`
- **Creative Direction — Design Specification (Apparel / Logo / Poster / Packaging)** — `skills/creative-direction/references/prompts-v2/design-specification.md`
- **Moodboard Decision System — [Objective]** — `skills/creative-direction/references/prompts-v2/mood-board.md`
- **Creative Direction — Storyboard (Multi-Shot Sequence)** — `skills/creative-direction/references/prompts-v2/storyboard.md`
- **Creative Direction — Trailer Treatment (4-Act Narrative Framework)** — `skills/creative-direction/references/prompts-v2/trailer-treatment.md`

<!-- END:execution-prompts -->
