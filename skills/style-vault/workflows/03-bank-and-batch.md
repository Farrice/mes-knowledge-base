---
description: Permute a verified style across the scene inventory into a curated, indexed image bank the content pipeline consumes
---

# 03 — Bank and Batch

**Deliverable:** a curated, provenance-indexed **image bank** on the assets board, keyed to
brand × ICP × platform, sized to what will actually be used.

**Run this when:** a card is `verified` and you need on-brand images at volume.

**Why it exists.** Carter's real payoff is not the style — it is that the bank becomes a
*consumable*: *"I've got a carousel automation that's taking articles, building carousels
directly in code, using our image bank content, so we have unique designs going out every single
week."* The bank is infrastructure. A folder of nice images is not.

---

## Pre-flight

```bash
python3 execution/style_vault.py show <slug>
```

**Gate:** if the card reports GAP, stop and finish `02`. Batching an unverified style multiplies
an unproven look across a hundred assets, and the cost of finding out late is the whole batch.

---

## Step 1 — Build the permutation template

Take the verified style string and the scene inventory from `01`, and express the axes you
actually vary as brace groups:

```bash
python3 execution/style_vault.py permute \
  "{Editorial photo, Cut-paper collage} of {a founder mid-decision, a strategist reviewing work} \
   in {a quiet office at dusk, a bare room at midday}, {upper-third, left-column} left clear for text"
```

This is the port of Carter's curly-brace trick, and it is better here: seeded, diffable,
scriptable, and budget-checkable before it spends.

**Two disciplines on the axes:**

1. **Vary scene, never style.** The style is locked — that was the entire point of `02`. If a
   style word is in a brace group, you are running a second sweep with a batch's budget.
2. **Every axis must be one you will actually use.** Carter's own correction mid-video: he cuts a
   group because *"if I just want to make it a little bit less, I can just get rid of one of
   these."* Combinations multiply fast — four groups of three is 81 images. Generate the bank you
   will consume, not the bank the maths allows.

## Step 2 — Size and quote it

```bash
python3 execution/style_vault.py permute "<template>" --json    # read total_combinations
```

At `nano-banana-2`'s **$0.0062/image**, 140 images ≈ **$0.87**. State the number before running.
Sample down when the full product overshoots:

```bash
python3 execution/style_vault.py permute "<template>" --sample 60 --seed 3
```

The cost gate fires on paid invocation; a denial surfaces to Farrice and is never retried.

## Step 3 — Generate

**The floor applies at volume exactly as it does per-plate (retrofit 2026-08-10 — this step
predated the realism floor and carried none of it).** Before firing the batch:

1. **Lint the permutation template itself:** `python3 execution/style_vault.py lint "<template>"
   --strict` — brace groups vary the scene; the floor layers (capture, light, black point,
   atmosphere, imperfection, micro-surface) live in the constant part and must be present ONCE,
   outside the braces, or every image in the batch inherits their absence.
2. **Any document/label appearing anywhere in the batch runs the full 9-series first** — 9
   (real values), 9a (fetched specimen form), 9b (one SKU with the content it serves). A wrong
   table multiplied by a batch is a credibility failure at scale.
3. **Batch ≠ selection.** The permutation provides volume across *scenes*; it does not replace
   the 4-variant selection on any image that will lead an asset. Bank fills run permuted;
   hero/cover slots still go through `04`.

Route through `/generate` — `creative_router.py` lanes are binding, and the craft-map craft pass
applies to every generation, paid or free. Pass the style's reference image so the card does the
work the prompt no longer has to:

```bash
python3 execution/creative_router.py route --task "<brief>"
# then the routed wrapper, e.g.
python3 execution/generate_image.py "<permuted prompt>" --reference skills/generate/styles/<slug>/reference-1.png
```

Set `--run-id` and `--run-budget` for the batch when a ceiling was stated in the prompt. Never
raise a ceiling that came from Farrice.

## Step 4 — Curate

**Delete before indexing, not after.** The bank's value is that everything in it is usable
without a second look; one weak image in a folder of a hundred means every future use needs
review, which is the cost the bank existed to remove.

Four passes:

1. **World check** — cover the prompts and scroll the set. Does it read as one brand world, or
   as several? Anything not living in that world goes.
2. **Text-zone check** — the negative space decided in `01` actually landed clear. An image with
   nothing to overlay is not a content asset.
3. **Physics check** — most "looks AI" is a physics failure, not an aesthetic one. Light
   direction consistent with the source, hands and edges intact, materials behaving.
4. **Zoom check on every legible artifact** — `04`'s kill order applies per image: table rows
   read left-to-right (row-slip killed three variants across the proving session), headers
   unduplicated, every highlight agreeing with the named source. At bank scale this is the pass
   most tempting to skip and the one the buyer's zoom finds first.

## Step 5 — Index with provenance

```bash
python3 execution/generate_media.py index --file <output> --model <recipe-id> \
    --prompt "..." --cost N --project <brand-slug>
```

Provenance is sacred (standing verdict): every asset carries the prompt that made it and its
copy path. `--project <slug>` routes client work to `_active/<slug>/05-assets/generated/`.

Then refresh the surfaces:

```bash
python3 execution/asset_gallery.py        # board + Styles tab
python3 execution/style_vault.py index    # VAULT.md
```

## Step 6 — Close the loop on the card

Update `card.md` with what the batch taught you — scenes where the style underperformed at
volume, combinations that clashed, the real usable yield. **The card is a living doc; the batch
is a record.** This is the compounding step, and skipping it means the next batch relearns the
same lessons at the same price.

---

## LAYER 5 — THE BANK BUILD (Farrice, 2026-08-10; Carter's endgame at five-layer depth)

The bank is the system's real product: a deployable library per buyer-world, so content is
served from a compounding vault instead of one-off generations.

**Standing finding (2026-08-10, supplement-founder starter bank): establishing shots do not
survive batch generation.** 4 variants of one establishing composition returned four
near-identical renders — the model has one generic "moody desk" template at wide/symmetric
framing and a batch just re-rolls it. Working-mid and MACRO INSERT are the rungs proven at both
single-select and batch scale. **Default bank builds to working-mid + macro rungs only.** Only
attempt establishing with an explicit off-center/cropped/imperfect-framing instruction, treated
as its own prompt problem — never a bare re-roll of "the whole desk."

- **Permutation axes:** day-arc beat × emotional charge × shot rung — all three drawn from the
  segment's `scene-inventory.md` + `lived-world-codex.md`, never invented at build time.
- **The continuity dial, set per run:** *loose* (default — style constants hold, rooms free) ·
  *series* (2-3 recurring codex props threaded through the batch) · *canon* (a banked lead passed
  as image reference; same room recurs). Dial up only when the content series wants it — never
  as standing law.
- **Every batch prompt** still passes the full floor: `lint --strict` 8/8, calibrated numbers
  (codex "Calibrated ranges" or NO legible numbers), dark-mode rule for screens, 4 variants per
  concept, zoom kill-order at curation.
- **Output convention:** keepers land in `icp-worlds/<segment>/bank/` named
  `<beat>-<charge>-<rung>-NN.png`; index each to the assets board with prompt provenance.

## DECK DOCTRINE — cover carries the style, deck carries the brand (Farrice, 2026-08-10 — BINDING)

When a banked image becomes part of a multi-surface asset (carousel, deck, doc):

1. **The vault style styles the COVER ONLY.** The generated plate is one surface — the hook.
2. **Every other surface is set in the owning brand's design system**, loaded from its design
   contract — for Farrice that is
   `_active/farrice-brand/premium-minimal/package/02-DESIGN-CONTRACT.md` (tokens, type,
   grid, and sequence laws, verbatim — including *one dark interruption per sequence maximum*
   and *no serif type*). For a client, their brand contract.
3. **Never derive the deck's palette/type from the plate.** That was the first-draft failure:
   an improvised plate-derived system that violated the standing contract (serif headlines,
   off-token accent, three dark slides). Coherence comes from the brand system meeting one
   styled cover — not from the style leaking across every surface.
4. Type on the cover itself also obeys the brand contract; only the photograph carries the
   vault style.

Repeatable mechanics: deck = one HTML file on the contract's tokens → Playwright renders
per-slide PNGs (1080×1350) + a paged PDF. Working exemplar:
`_active/linkedin/03-launch/carousels/assets/carousel-01/deck.html`.

## Output requirements

- Permutation template, total combinations, and what was sampled or cut
- Stated cost before the run, actual cost after
- Curation counts: generated → kept, with the reason for the largest deletion group
- Indexed assets on the board with prompt provenance
- An updated `card.md` reflecting volume behaviour

## Quality gate

1. Did any style language leak into a brace group?
2. Was the bank sized to consumption or to the maths?
3. Cover the prompts — does the set read as one world?
4. Did the text zones survive at volume?
5. Is every kept image indexed with its prompt, or did some land as orphan files?
6. Does `card.md` now know something it didn't before the batch?
