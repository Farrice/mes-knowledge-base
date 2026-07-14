---
name: joey-cinema-os
description: "Joey (Noisy Group / Control World) — cinema-grade AI production OS. The consistency layer for AI image/video: story/world bibles as model context, face-lock + 3-panel character sheets engineered against identity drift, zero-lighting reference plates, block-structured Seedance video prompts, credit-costed shot plans, and the product-grade transfer (product/garment identity locks via the KY technical-flats method). Orchestrates the three installed production skills (banana-pro-director, cinema-worldbuilder-pro, story-bible-builder) and wires them into Higgsfield MCP / Fal surfaces. Use for: persistent characters or brand worlds, product-grade AI visuals, AI video consistency, character sheets, scene plates, Seedance prompts, AI music videos / branded films, drift or prompt-bloat repair."
---

# Joey Cinema OS — Persistent-World AI Production

**The one-line genius:** consistency is an asset discipline, not a model feature — move every load-bearing decision out of the prompt and into locked upstream artifacts, so each generation is a cheap read of expensive, permanent context.

**Load order:** this file → `genius.md` (judgment layer) → the production skill(s) for the layer you're working: `skills/story-bible-builder/SKILL.md` (canon), `skills/banana-pro-director/SKILL.md` (stills), `skills/cinema-worldbuilder-pro/SKILL.md` (video). The three carry LOCKED verbatim grammar (flat-grade close, cinema stack, Capture Realism, night register, FOV ladder) — never paraphrase their blocks; load and use them.

## The Pipeline (strict order)

```
CANON  → story-bible-builder      (once per world — who, voice, era, "never" clauses)
STILLS → banana-pro-director      (per asset — face lock → outfit base → 3-panel sheet → scene plates)
MOTION → cinema-worldbuilder-pro  (per shot — block-structured Seedance prompts, @tags, costed runtime)
```

Don't skip steps. Don't combine steps. Unbuilt character in a video ask → kick back to stills. Multi-scene world with no bible → build canon first (or proceed with drift named).

## Workflows

### Tier 1 — Foundation

| Workflow | Command | What it produces |
|---|---|---|
| `workflows/pipeline.md` | `/jcin-pipeline` | End-to-end mission conductor: bible → asset locks → scene plates → costed shot plan → shot prompts, checkpointed |
| `workflows/world-canon.md` | `/jcin-world-canon` | Story/world/brand bible built via story-bible-builder, saved to the owning project, install-ready |
| `workflows/character-lock.md` | `/jcin-character-lock` | Full character identity pipeline: face lock → outfit base → 3-panel sheet (strict Mode 0→1→2A order) |
| `workflows/scene-shot.md` | `/jcin-scene-shot` | Scene plate (Mode 3 cinema-prose) + matching block-structured Seedance shot prompt, mode-matched grammar |

### Tier 2 — Practitioner

| Workflow | Command | What it produces |
|---|---|---|
| `workflows/product-lock.md` | `/jcin-product-lock` | Product-grade identity lock for products/garments/vehicles: hero lock → turnaround sheet → in-context plates (KY technical-flats method, colors-to-avoid palette) |
| `workflows/outfit-engine.md` | `/jcin-outfit-engine` | Outfit builds and swaps: Mode 1A/1B fork, Mode 5 two-ref swap, technical-flat ingestion |
| `workflows/prompt-doctor.md` | `/jcin-prompt-doctor` | Drift/bloat diagnosis + repair: reset ritual, write-the-visible rewrite, lock audit ("never" clauses, anchors, position) |
| `workflows/shot-plan.md` | `/jcin-shot-plan` | Credit-costed shot plan: beats, durations, per-shot mode, take budget, total credit estimate BEFORE generation |
| `workflows/voice-lock.md` | `/jcin-voice-lock` | Voice/persona consistency payloads: bible Speech/Movement/Stillness descriptors formatted for Sound Bed / Subject Lock slots |

### Tier 3 — Stacking

| Workflow | Command | What it produces |
|---|---|---|
| `workflows/story-15s.md` | `/jcin-story-15s` | 3-shot/15-second micro-story: grab → payoff → unresolved questions, one costed prompt with timestamped beats |
| `workflows/ad-world.md` | `/jcin-ad-world` | Branded-world ad system: locked product + locked avatars + scene-plate library feeding static and video ad production |
| `workflows/studio-bridge.md` | `/jcin-studio-bridge` | Wiring run: routes fantastic-studio stages 04-05 / creative_router intents into this pipeline; Higgsfield MCP paste-and-attach loop |

## Stacking Guide

| Partner | Stack |
|---|---|
| **Stanton / Ben Watkins / Hawley** | Story spine → `/jcin-world-canon` premise/thesis + `/jcin-story-15s` beat design (narrative layer above the visual pipeline) |
| **Dara Denney / Omar Eddaoudi** | `/jcin-product-lock` + `/jcin-ad-world` → identity that holds across static AND video ad variants |
| **Fantastic Studio (`/fantastic-studio`)** | Stages 04 (model route) / 05 (prompt compile): photoreal people + Seedance lanes compile through banana-pro / worldbuilder grammar; concept/divergence/critique stages stay upstream |
| **Tao Prompts** | Tao's multi-shot decoupling + Joey's reference locks = long-form film pipeline |
| **Meg Heckman / MyBPM** | KY technical-flats method → merch/apparel visualization with construction-true garments |
| **Voice OS** | Bible voice descriptors are the character-side analog of VOICE-CARD — never let them collide with Farrice's own voice layer; separate documents |

## Surfaces & Gates

- **Higgsfield MCP** (native surface): `@tag` element grammar works; outputs → `show_reference_elements` / character slots. **Fal wrappers**: no @tags — strip to prose descriptors; seedance-1080p is HARD-BLOCKED by the budget guard.
- All three production skills are prompt-only ("the skill's job ends at the code block") — cost gates fire at execution, unchanged (`higgsfield_budget_guard.py`, `fal_budget_guard.py`).
- **Disambiguation:** Joey's "GPT-2" = Higgsfield GPT-2 (face-fidelity king, credit-heavy) ≠ `gpt-image-2-director`'s OpenAI GPT Image 2 (layout/typography king, weak faces).

## Quick Reference

- Bell curve: past ~3 failed iterations → reset the prompt, re-add minimum.
- One face per identity reference, as large as the format allows.
- Plates flat (18% gray, zero lighting info) whenever the asset seeds video.
- Degrees not millimeters; timestamps not vibes; km/h not "fast"; muscle not mood.
- Names/brands/ages never in prompt output. Duration declared, plan costed, then generate.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

8 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Joey — Character Identity Lock Package** — `skills/joey-cinema-os/references/prompts-v2/character-identity-lock.md`
- **Joey — 15-Second 3-Shot Story** — `skills/joey-cinema-os/references/prompts-v2/micro-story-15s.md`
- **Joey — Product Identity Lock Package** — `skills/joey-cinema-os/references/prompts-v2/product-identity-lock.md`
- **Joey — Prompt Diagnosis & Repair** — `skills/joey-cinema-os/references/prompts-v2/prompt-repair.md`
- **Joey — Cinematic Scene Plate** — `skills/joey-cinema-os/references/prompts-v2/scene-plate.md`
- **Joey — Seedance Shot Prompt** — `skills/joey-cinema-os/references/prompts-v2/seedance-shot.md`
- **Joey — Credit-Costed Shot Plan** — `skills/joey-cinema-os/references/prompts-v2/shot-plan.md`
- **Joey — Story/World/Brand Bible** — `skills/joey-cinema-os/references/prompts-v2/world-bible.md`

<!-- END:execution-prompts -->
