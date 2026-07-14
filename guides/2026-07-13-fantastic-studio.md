---
date: 2026-07-13
session: operator-guide backfill (guides fleet)
tier: operator-guide
status: enriched
---

# Fantastic Studio — What We Built and How to Use It

> `fantastic-posters` grew a brain on 2026-07-04 and became the **Fantastic Studio (v2)**: a concept-first, multi-model, self-critiquing image pipeline behind one front door, `/fantastic-studio`. This guide is the entry point; the full spec lives at `skills/fantastic-posters/workflows/00-studio.md`, the brain at `skills/fantastic-posters/genius.md`, and the base skill (38 styles, `generate.js` flags, video bridge) at `skills/fantastic-posters/SKILL.md`.

## ⚡ If you only read 10 lines

- Doctrine: **never hand a bare prompt to a generator** when the output must be remarkable — run the Studio.
- Front door: `/fantastic-studio [brief, asset path, or a /satori-design-think Production Brief]` → a routed generation plan.
- 8 stages, each also standalone: reference-ground → art-direct → divergence → model-route → prompt-compile → generate-run → critique-refine → format-pack.
- One rule: **Satori decides, the router picks the instrument, the studio critiques its own work.**
- Route before rendering: `python3 execution/creative_router.py route --task "<direction>"` — people/real scenes go to Higgsfield Soul, NOT this skill.
- Paid generation is cost-gated and **human-triggered**: `python3 execution/cost_gate.py check --service <id>` → approve → run. Never auto-fired.
- `seedance-1080p` is hard-blocked at script level. Video pre-flight: `python3 execution/fal_budget_guard.py check --mode=<kling|seedance-720p|...> --duration=<N>`.
- Image cost: `--quality=low` ~$0.011 (drafts) · `medium` ~$0.04 (client review) · `high` ~$0.17 (final).
- Skip the Studio only for one-off quick drafts or a `--template` replicate of a proven layout.
- Proven live: MyBPM "Still Synced" — 3 orthogonal directions across 2 models for $0.15 (`_active/mybpm-merch-os-run-1/04-deliverables/10-studio-job-still-synced.md`).

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/fantastic-studio` | Full 8-stage run → routed generation plan | Any client-facing or brand-defining visual |
| `/fantastic-reference-ground` | Real high-taste lineage anchor | Output keeps defaulting to model taste |
| `/fantastic-art-direct` | Art-direction spec (ingests a satori Production Brief) | You have `/satori-design-think` output, or need the generic killed |
| `/fantastic-divergence` | N *orthogonally distinct* directions | You need variety, not the same idea in three tints |
| `/fantastic-model-route` | Per-direction model assignment | Directions are set; instruments aren't |
| `/fantastic-prompt-compile` | Model-specific prompts (+ Fal `--brief` JSON) | Specs are locked, ready to translate |
| `/fantastic-generate-run` | Cost-gated, human-triggered runbook | Time to spend money |
| `/fantastic-critique-refine` | Virgil × LIFT × type × anti-slop critique → `--mask` edits | First output is good, not remarkable |
| `/fantastic-format-pack` | One concept → feed/story/hero/print/cutout/motion | A winner needs to ship everywhere |

## The mental model

**Two ideas make everything else obvious.**

1. **The bare path is the failure mode.** The old skill was "brief → pickStyle → render": keyword-matched templates, `--n=3` as colour-nudge redundancy, one model. It rendered; it didn't think. The Studio front-loads the thinking — concept before pixels — so that when money is spent, it's spent on directions that were already art-directed, diverged, and routed. The divergence stage exists specifically because the old redundancy failure (three near-identical outputs) burned budget without buying options.

2. **Three separated jobs.** Satori (`/satori-design-think`) is the brain — it decides the hidden truth, hierarchy, color, feeling. The router (`creative_router.py`) picks the instrument per direction. The Studio critiques its own work before you see it (stage 7 turns "fine" into "remarkable" via `--mask` edits). Collapsing any two of these back into one step recreates the generic output the v2 rebuild fixed.

## The lane split (which engine gets the brief)

This is where money gets wasted, so pre-flight EVERY visual brief through the router:

```bash
python3 execution/creative_router.py route --task "<brief>" --json
```

| Brief looks like | Route |
|---|---|
| Posters, typographic, style-family work (Swiss, vintage, brutalism, editorial…) | **Fantastic Studio** → Fal GPT Image 2 (`generate.js`) |
| Photoreal **people** — a real scene, someone doing something in an environment | **Higgsfield Soul** (router sends portrait/person/character there) |
| Cheap iteration / drafts | Nano |
| Motion | Kling / Seedance / Cinema (budget-guarded) |
| **Consistency across a series** — same character, world, or product over many assets | **Joey Cinema OS** (`/jcin-pipeline`; product-grade client visuals → `/jcin-product-lock`) |

The receipts behind the people-rule: 12 Resonance posters generated through fantastic-posters' editorial-fashion style were rated 0/10 ("group fitness classroom meeting, not a room full of life and energy") — $1.69 burned. Poster generators bake in posed, magazine-cover framing; real-scene energy needs Soul. The Studio and Joey Cinema compose freely (no forced wiring): Studio for the one remarkable asset, Joey Cinema when the job is keeping asset #14 consistent with asset #1.

## /fantastic-studio — the front door

**What it is.** An orchestrator that runs stages 1–8 and emits a routed generation plan. It is the *thinking/plan layer* — nothing paid fires from it directly.

**When to reach for it.** Anything client-facing or brand-defining. The tell: you're about to type a prompt into a generator and hoping.

**When NOT to.** A one-off quick draft (`node generate.js "<brief>"` with the style picker is fine), or a `--template` replicate of a proven layout — the reference carries the layout; the Studio adds nothing there.

**How to invoke.**

```
/fantastic-studio [brief, asset path, or a /satori-design-think Production Brief]
```

The satori handoff is the strongest input: `/satori-design-think` produces a Production Brief (hidden truth, LIFT hierarchy, hex tokens, feeling, memory hook, anti-slop) and `/fantastic-art-direct` ingests it directly.

**Worked example.** MyBPM Week-1 "Still Synced" (2026-07-04): three strangers-not-tints directions across two models for $0.15 total — a Swiss EKG poster (ship-grade), a Higgsfield Soul photoreal portrait, a riso flyer. Images in `skills/fantastic-posters/out/`.

## Cost discipline (physical, not advisory)

- **Every paid generation**: `python3 execution/cost_gate.py check --service <id>` → Farrice approves → run → log. The Studio's generate-run stage produces a runbook you execute by hand; it never auto-fires spend.
- **Video** adds `fal_budget_guard.py` pre-flight (mandatory): kling $2.00/call ceiling · seedance-720p $3.00 · seedance-480p $1.50 · **seedance-1080p refused at script level** (~$10 per 15s call).
- `generate.js` prompts for confirmation at ≥5 images or `--quality=high` regardless of `--yes`.
- Useful cheap moves: `--variants=4` (4 siblings, 1 API call) vs `--n=3` (3 separate calls with diversity nudge); `--rembg` transparency adds ~$0.005/image.

## Composition table (options, not pipeline steps)

| Stacks with | What it adds | Earns its cost when |
|---|---|---|
| `/satori-design-think` | The design brain — Production Brief the Studio executes | Brand-defining work; anything where "why this look" must be defensible |
| `creative_router.py` | Instrument selection + cost-gate pre-flight printout | Always — it's a $0 pre-flight |
| Joey Cinema OS (`/jcin-*`) | Character/world/product consistency across a series | Multi-asset campaigns, client product visuals |
| Poster-to-video bridge | Studio output as video input frame (`workflows/poster-to-video.md`) | A winning still deserves motion |
| Subagent fan-out | One subagent per brief via the Agent tool | 10+ briefs (real-client batches) |

## Honest edges

- Logo placement is imperfect even with the edit endpoint — review rendered logos before delivering. Titles past ~6 words risk typos.
- No upscaling, no PSD layering in-skill: Topaz/Real-ESRGAN for print, Canva Magic Layers for splitting.
- The Studio has one live proof run (MyBPM). The stage-by-stage standalone commands are less exercised than the full front door.
- The 38-style picker still exists underneath — it's the right tool for quick drafts, and the wrong one for anything with people in it. When in doubt, the router decides, not you.
