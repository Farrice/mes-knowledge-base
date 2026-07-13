---
name: "Algorithmic Art — Seed Variation Gallery"
source_prompt: born-v2
skill: algorithmic-art
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are extending an existing seeded algorithm the way a printmaker curates a series of pulls from the same plate: "the algorithm is consistent, but each seed reveals different facets of its potential." This is not a new artwork — it is the exploration layer on top of an already-built algorithmic piece, built for a user who wants specific variations surfaced rather than discovering them one seed-click at a time.

## Input Required

```
[EXISTING ARTIFACT] — the already-built single-file HTML artifact (algorithm, params object, UI) this gallery extends
[VARIATION COUNT / SEEDS] — how many seeds to highlight, or "generate 100 variations" (seeds 1-100) if the user wants the full sweep
[SPECIFIC SEEDS, if any] — explicit seed numbers the user wants included as presets
[DISPLAY MODE] — seed presets (buttons jumping to named seeds) and/or Gallery Mode (thumbnail grid of multiple seeds side-by-side)
```

## Execution Protocol

**Step 1 — Confirm this stays inside the same single artifact.** The base HTML file, its algorithm, and its Anthropic-branded shell (header, sidebar structure, seed controls, action buttons) are unchanged. Variation exploration is additive UI, not a new file and not a rebuilt algorithm.

**Step 2 — Seed presets.** If the user wants specific variations highlighted, add labeled buttons — e.g. "Variation 1: Seed 42," "Variation 2: Seed 127" — that jump directly to a chosen seed via the existing seed-update path (same reseed-and-reinitialize logic the Prev/Next/Random/Jump controls already use). Curate seeds worth naming: ones that visibly demonstrate different facets of the algorithm's range, not an arbitrary sequential run.

**Step 3 — Gallery Mode, if requested.** Render thumbnails of multiple seeds side by side within the same artifact — a grid view, not separate files. Each thumbnail should be generated from the same algorithm with a different seed value, at reduced size, click-through to load that seed at full size in the main canvas.

**Step 4 — Full sweep, if requested ("generate 100 variations").** Cycle seeds 1-100 through the existing algorithm. This is a batch exploration, not 100 separate artifacts — the mechanism is the same seeded-reinitialize loop, run across a range, surfaced either as a gallery grid or as a seed range the Prev/Next controls step through.

**Step 5 — Preserve reproducibility guarantees.** Every seed in every preset/thumbnail must reproduce identically on reload — the same `randomSeed`/`noiseSeed` discipline from the base artifact applies to every variation shown, no exceptions.

## Output Contract

An addition to the existing single-file HTML artifact (not a new file): seed preset buttons and/or a Gallery Mode thumbnail grid, wired into the existing seed-navigation logic. No change to the core algorithm, the params object's meaning, or the fixed Anthropic-branded shell. If the user asked for a written curation (why these seeds), a short paragraph or labeled list explaining what each highlighted seed demonstrates about the algorithm's range.

## Output Skeleton

```html
<!-- Added to the existing sidebar, inside or near the Seed control-section -->
<div class="control-section">
  <h3>Variations</h3>
  <!-- one preset button per curated seed -->
  <button class="button secondary" onclick="jumpToSeed([SEED_VALUE])">[VARIATION LABEL]: Seed [SEED_VALUE]</button>
  <!-- repeat per preset -->
  <!-- optional Gallery Mode toggle -->
  <button class="button tertiary" onclick="toggleGalleryMode()">Gallery Mode</button>
</div>
```

```
[If Gallery Mode requested: thumbnail grid container — one small canvas/render per shown seed, click-through loads that seed full-size in the main canvas-area]
```

```markdown
[Optional curation note — one line per highlighted seed, naming what it reveals about the algorithm's range]
```

## Quality Gate

- Do all preset/gallery seeds reuse the existing artifact's exact seeding mechanism (`randomSeed`/`noiseSeed` reinitialize), producing identical output on repeat load?
- Is this an addition to the single existing HTML file, not a second file or a rebuilt algorithm?
- Are the FIXED shell elements (header, base sidebar structure, Anthropic branding, core seed controls, action buttons) still present and unchanged?
- If seeds were curated (not just 1-100 sequential), does each one demonstrably show a different facet of the algorithm rather than near-duplicates?
- If Gallery Mode was built, does clicking a thumbnail actually load that seed into the main canvas?

## Creative Latitude

Seed curation is a taste call — the value of this deliverable is picking seeds that read as genuinely distinct expressions of the same underlying system (sparse vs. dense, calm vs. turbulent, symmetric vs. broken), not an arbitrary or evenly-spaced sample. Labeling is open: name variations by what they visually do ("Variation: Dense Convergence") rather than defaulting to generic numbering when the algorithm's behavior supports something more evocative.

## Deploy When

User already has (or is simultaneously building) an algorithmic art artifact and wants specific seed variations surfaced as presets, a side-by-side gallery/thumbnail view, or a full seed-range sweep — rather than exploring seeds one click at a time via the base Prev/Next/Random controls.
