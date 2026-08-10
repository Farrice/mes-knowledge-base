---
description: THE imagery run — one verified cover plate from a brief, at the v6-03 standard, every time. The extraction of the 2026-08-10 six-round session into a single repeatable loop.
---

# 04 — Cover Plate

**Deliverable:** ONE selected, zoom-verified cover plate (plus its kept alternates), indexed with
provenance. Nothing else. Content, decks and captions are Farrice's; this workflow's whole job is
that the image comes out at the proven standard on every run.

**Cost per run:** ~120 OpenArt credits (4 variants, gpt-image-2, quality high, 1k). State it
before firing.

**Why this workflow exists.** It is the distillation of the six-round Transparent Labs session
(2026-08-10) that went 4/10 → shipped. Every step below exists because skipping it produced a
rejected round. Run the steps in order; none is optional.

---

## Inputs (all three, before anything fires)

1. **The content the image will sit on** — either shape:
   - **Evidence-bearing deliverable** (teardown, audit, case study): the image argues *its*
     argument; the 9b read anchors to the exact SKU/claim the copy quotes.
   - **Post / topic** (the original mission — ICP-resonant imagery for whatever he's posting):
     open the brand's **scene inventory** (`_active/<brand>/05-assets/scene-inventory.md`, built
     by `01-seed-scenes.md`) and select the scene whose STATE matches the post's claim — pain
     scene for a pain post, desire scene for an arrival post. The scene supplies the situation;
     the post supplies the specific real-world anchor (a named thing, a number, a document, a
     moment) that 9b then verifies. **No inventory for this brand → run `01` first.** A plate
     generated without an ICP-anchored scene is decoration, however crafted.
2. **The brand + platform key** — `python3 execution/style_vault.py list --brand <x> --platform <y>`
   to pull the matching card. No matching card → run `02-mine-and-audition.md` first; do not
   freehand a look.
3. **The card** — `python3 execution/style_vault.py show <slug>`. Its conditions/anti-conditions
   gate whether this style fits this job at all (e.g. `evidential-still-life` is an indictment
   format — wrong for warm/aspirational work).

## Step 1 — The coherence read (layer 9b — BEFORE any visual thinking)

Read the deliverable's copy and answer in writing, in the sweep log:

- **Which exact SKU does the quoted evidence belong to?** (Read it — don't assume. The v5 scar:
  reviews were the whey isolate's, the document said pre-workout.)
- What is that SKU's name, flavor, form, serving size?
- What object plays that SKU's own story? (The antagonist is the product's claim, not a generic
  prop.)

Cross-check both directions before proceeding: cover the image-to-be — does the document alone
name what the copy quotes? Cover the document — does the imagined image match what the evidence
describes? Mismatch = full stop.

## Step 2 — Specimen research (layer 9a)

If the frame contains any document, label, chart or instrument:

- **Fetch a real specimen** of that document type (subject brand's own published one → category
  standard → competitor's). Web-check; never from model memory.
- Mirror its **form**: row inventory, METHOD column, units, result formats ("Below LOQ",
  "Absent"), closing lines (accredited-lab, approved-by).
- Pull the SKU's **real published values** (label facts, published test results) for the cells.
- **Log the specimen source URL** in the sweep log. No named specimen = gate 9a fails.

## Step 2b — THE SHOT LADDER (added 2026-08-10 — the heartstring layer)

Every banked world produces at three distances (Clark's coverage, applied to stills):

| Rung | What fills the frame | Job |
|---|---|---|
| **Establishing** | The whole room/world | "This is my world" — orientation, banked first |
| **Working mid** | One element in its context | "That's my Tuesday" — the scene inventory's rows |
| **MACRO INSERT** | ONE insider artifact, frame-filling, shallow DOF | **"He gets me"** — the recognition gut-punch |

The macro insert draws from the segment's **Lived-World Codex**
(`_active/linkedin/05-assets/icp-worlds/<segment>/lived-world-codex.md`) — a researched
inventory of insider artifacts, each carrying an emotional charge and a macro-shot spec. Select
by matching the POST's claim to the artifact's charge (dread post → dread artifact).

**The recognition test governs the rung:** *would an outsider think to include this?* If yes,
it is decoration at any craft level — cut it. Recognition lives in what only the insider knows:
not the coffee, the dried shaker ring; not the spreadsheet, the tab named after the problem.
An establishing shot orients; only the insider detail makes the buyer feel SEEN.

## Step 3 — Build the prompt

Start from the card's `prompt.md` skeleton (e.g.
`skills/generate/styles/evidential-still-life/prompt.md`) and fill its brackets. The document
block is written as **literal strings** — headers, every row, every cell. The model garbles only
what it is left to invent.

Then the floor, from the card if it carries them, else authored fresh: capture (camera, lens,
aperture, stock, support) · one named light source everything agrees with · real black point ·
mid-ground atmosphere · marks of history · material physics (wet paper cockles) · subsurface
scattering named on any translucent material · specular shape/placement · luminance-dependent
grain (not uniform "fine grain").

## Step 4 — Lint (deterministic, no judgment)

```bash
python3 execution/style_vault.py lint "<full prompt>" --strict
```

**8/8 and exit 0, or fix and re-lint.** Never fire a prompt that fails the floor.

## Step 5 — Generate: 4 variants, one call

OpenArt MCP, `gpt-image-2`, `text2image`, `imageCount: 4`, `quality: high`, `resolutionTier: 1k`,
aspect per platform (4:5 LinkedIn), `autoEnhancePrompt: false` (the craft pass already happened —
a second polish would overwrite it).

One image per concept is a first take, not a run (Clark #1: flat is a *selection* failure).

## Step 6 — The zoom verdict (where two of six rounds died)

Open every variant at full size and read it. Kill order:

1. **Row/pair integrity** — read every legible table row LEFT TO RIGHT. A value column that
   slips one row pairs Mercury with "cfu/g"; this killed v6-01 and v5-04. Any wrong pairing =
   killed, no rescue.
2. **Header integrity** — occlusion by the antagonist is natural; doubled letters are not
   (killed v4-01).
3. **Physics** — materials behaving as themselves; every highlight agreeing with the one source.
4. **Composition** — text zone actually clear for the overlay; black point real.

Select ONE. Keep passing alternates in `deliverables/generations/<project>/`; delete kills.

## Step 7 — Deliver + close the loop

```bash
python3 execution/generate_media.py index --file <selected> --model gpt-image-2 \
    --prompt "<prompt>" --cost 1.20 --project <brand-slug>
```

Update the card with anything the run taught (new refusal, drift pattern, text-load ceiling).
The card is living; the run is a record.

**Optional, only when asked:** the deck pipeline — `deck.html` on the brand's design-contract
tokens → Playwright per-slide PNGs + paged PDF (working exemplar:
`_active/linkedin/03-launch/carousels/assets/carousel-01/`). Deck doctrine applies: the plate
styles the cover ONLY; the brand system carries every other surface. **Not part of this
workflow's deliverable** — Farrice does the content work (his call, 2026-08-10).

---

## Quality gate (all seven, in order)

1. 9b answered in writing before any visual work?
2. Specimen fetched and its source logged?
3. Document written as literal strings, values from the SKU's real published facts?
4. Lint 8/8, exit 0?
5. Four variants, one call, judged as a set?
6. Every legible row read left-to-right at zoom on the SELECTED variant?
7. Indexed with provenance, card updated?

**The closer, always:** would this have looked the same without me?
