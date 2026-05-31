---
description: Build the complete Avatar Manifold — a full multi-dimensional market-intelligence package (the flagship deliverable)
tier: 1
stacks_with: all luke-iha skills, dai-media, mcraney
---

# Avatar Manifold Builder ⭐

The flagship. Runs a single market through every framework in the system and concatenates the results into one comprehensive, reusable market-intelligence document — **the Avatar Manifold.** This is the sellable "in-depth package / creative brief" deliverable.

## Pre-Flight Gate
- **Market named?** You need a target market + (ideally) a product. If only a product, infer the market. If neither, ask once.
- **Sourcing — AUTO-FIRED, not optional.** At cold start this workflow EXECUTES real research (Phase 0 below) so Build-a-Buyer and the Specific-Language pack consume actual data, not assumptions. Only fall back to `[MODELED — replace with VOC]` if every research path degrades (budget denied + APIs down). Modeled output is the floor, not the default.
- **Scope check:** Full Manifold is long (3,000–8,000+ words). If the user wants a fast subset, route to the relevant single-framework workflow instead.
- Anti-pattern (genius.md): never deliver fragments or single-adjective descriptions. Plot before you write. **And: never plot from contextual guessing when the research tools are available — ground first.**

## PHASE 0 — GROUND (cold-start research, AUTO-FIRES; skip with `--no-ground`)

Fire real market intelligence BEFORE plotting — through the ONE deterministic chokepoint, so grounding REUSES a fresh per-market dossier at **$0** and only cold-starts (paid, cost-previewed) on a cache miss. The runner fires Gemini Deep Research (→ Perplexity fallback → recall-only degrade) + free Reddit/HN + Apify VOC in one pass:

```bash
// turbo
python3 execution/avatar_manifold_runner.py ground --slug <slug> --market "<market>" --product "<product>" --tier deep --mode max 2>&1 | tail -6
```
- **WARM** (`♻️`) → dossier reused, $0, proceed to plotting. **COLD** → cost-previewed, fires real research, writes `.tmp/copy-engine/<slug>/ground-dossier.md` + `deep-research.md` + `voc-pack.md`. **STALE** (`⏳`) → reused with a nudge; pass `--refresh` only if the market moved.
- **Budget-exhaustion is fail-closed**: the runner degrades to $0 (recall-only + `[MODELED]`), it never auto-escalates to a pricier pool.
- **Stream 2 — VOC** is built inside the same runner pass (free Reddit/HN public-JSON + optional Apify). For a deeper manual dig, `/buyer-sourcer` is the standalone equivalent; its deterministic floor check (≥15 source URLs, zero `[MODELED]`) is the quality bar.
- The Build-a-Buyer (stage 1) reads `deep-research.md`; the Specific-Language pack (stage 12) reads `voc-pack.md`. If a stream degraded, flag the dependent stages `[MODELED]` — never fabricate research.

**Seed rule:** stage 1 (Build-a-Buyer) reads `deep-research.md`; stage 12 (Specific-Language pack) reads `voc-pack.md`. If a stream degraded, flag the dependent stages `[MODELED]` — do NOT fabricate research.

## Skill Acquisition
Load `genius.md` (full) + `references/framework-library.md` (all sections) + `references/worked-manifold-exemplar.md` (output standard). Optionally `source-prompts/build-a-buyer-prompt.md` and `buyer-snapshot-prompt.md` for the buyer-profile stage. Have `.tmp/copy-engine/deep-research.md` + `voc-pack.md` open.

## Execution (canonical assembly order)
Run each stage, writing the section before moving on. Each stage names the sub-workflow that can deepen it.

1. **Build-a-Buyer Snapshot** — demographics, core problem, symptoms, emotional/social impact, hurtful soundbites (labeled by speaker), motivation triggers, future costs, magic-genie outcome, failed solutions, popular solutions + objections, ideal solution (edge of believability), things they won't do, market specifics (hinge/give-up/blame/objections). *(Use the preserved Build-a-Buyer prompt.)*
2. **Pain Matrix** — score all 10 dimensions 1–10, each with a marketing consequence. → `/pain-matrix`
3. **Core Wound + Ontological Resource Matrix** — ranked resources (relevance × inherent/earned × loss/gain), core-wound prediction, rub-salt message. → `/core-wound`
4. **Benefit Matrix** — the 10 axes for the solved state + imagery directives.
5. **Desire Daisy-Chain** — 3 chains (benefit→feeling→relationship→identity).
6. **Resonance Hierarchy** — full Experiences→Beliefs→Values→Identity with all subsections, incl. dysmorphic avatars + allies/enemies. → `/resonance-hierarchy`
7. **RH Constraints** — all 6 constraint types, ~5 each.
8. **Dissolution Frameworks** — dissolve each major constraint via AWE (named vehicle + bundled assumptions). → `/dissolution-forge`
9. **Epiphany Threshold sets** — 10 obvious / 10 over-BS / 10 Goldilocks (w/ reasoning). → `/epiphany-threshold`
10. **Market Pick-Up Lines** — 10 hooks mapped to pain dimensions. → `/market-pickup-lines`
11. **Anti-Hero's Journey (Pt 1)** — Garden of Eden → Slow Descent/False Idols → Fall of Man/PIG → Dark Night. → `/anti-hero-journey`
12. **Specific-Language pack** — pulled VOC soundbites by emotion/objection (or modeled + flagged).
13. **Landmines & segments** — Ejection Triggers · Market Addictions · Concentric Circles of Concern · consciousness level (Victim/Hybrid/Accountability).
14. **Suffering Archetype** — type the market (1 of 9) → 1-line tone directive. → `/suffering-archetype`

Then **concatenate** all sections under a titled header: `# AVATAR MANIFOLD — [Market]`.

## Content Type Adaptations
| Use case | Emphasis |
|---|---|
| Client creative brief (sellable) | Full Manifold + an executive summary up top + a "how to use this" page |
| Internal pre-copy intelligence | Full Manifold, lighter on prose, heavier on tables |
| Supplement / health offer | Core Wound + Interoceptive Mechanism + stigma handling |
| MMO / biz-opp | Market Addictions (the "$10K/month" fixation) + consciousness level + locus of control |
| Identity-driven (coaching, status) | Resonance Hierarchy + dysmorphic avatars carry the weight |

## Output Requirements
- Titled, sectioned, in canonical order. Tables for matrices, prose for stories.
- Every Pain/Benefit score paired with a consequence. Every soundbite labeled VOC or `[MODELED]`.
- End with: **"5-Part Sales Formula Map"** (which sections feed Lead / Background Story / Mechanism / Product Story / Close) + a one-line handoff note to `/manifold-to-copy`.

## Quality Gate
Score against the genius.md rubric (8 criteria). Composite must clear all 8 at ≥6, dimensionality + core-wound + deployability at ≥8. Auto-fail on: single-adjective descriptions, scores without consequences, invented "specific language" not flagged, Identity-clashing leads, fragments instead of an assembled Manifold, **and skipping Phase 0 research when the tools were available (modeled-by-default instead of modeled-by-necessity).**
