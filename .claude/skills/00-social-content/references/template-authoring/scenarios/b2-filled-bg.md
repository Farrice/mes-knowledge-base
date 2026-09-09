# Scenario B2 — filled texture / landscape

> The DEFAULT form (`identification-tree.md` Q5 fallthrough). `text_placement: on-reserved-zone`. A full
> background (texture or landscape) with a **deliberate clean reserved zone**; the text floats on that zone,
> placed by **HTML** — the zone is known (the AI guaranteed it), not guessed.
>
> Canonical example: Visual Brain — reserved-zone bet validated by hand 2026-06-08.

## Edit mode
- **Background:** `ai-prompt-craft.md` → **reserved-zone prompting** so the AI generates the scene with a
  clean, low-detail band where the HTML text will land. If the bg also has a variable subject, combine with
  **Partial — subject only**.
- **Text:** `html-craft.md` → HTML on the reserved zone. Per-block isolability test: a headline on the clean
  band sits directly on it; a body block over busier detail uses the **pill** overlay (`html-craft.md` §4). A
  single B2 slide commonly MIXES both (headline = reserved-zone HTML, body = pill HTML).

## Generation moment
- **bg fixed** (fixed landscape/texture, no variable subject) → generate **1× at setup** (route
  `texture-extract` for pure texture, or `edit-from-ref` once for a landscape); `_ai_bg/bg.png` becomes a fixed
  asset (generated images ALWAYS land in `_ai_bg/`, never loose at the template root). Post-time swaps text
  only — **zero AI on the bg**.
- **bg + variable subject** → `edit-from-ref` every post with the reserved-zone + subject delta.

## Build
1. Background `<img>` or CSS, full-bleed. `data-slot` if it's a fillable zone. **When the whole slide IS one AI image** (the full-bleed composition, not a clean texture under HTML text), that `<img>` carries `data-slot="PHOTO_MAIN"` and IS the single editable AI layer — NO `composition-frame`/`card-zone-marker` wrapper around it, and NO second redundant `PHOTO_MAIN` zone. One `PHOTO_MAIN` per template, max (`shared/conventions/slots-and-html.md` §14).
2. Reserved-zone text: a flow zone positioned to the reserved band; headline directly on it, body in a pill
   if needed. `data-slot` per slot, triple-brace for HTML-bearing slots, breathing margin.
3. `[ai-image-zone]` block with the reserved-zone instruction folded into `prompt_delta`
   (mark `# validated-at-setup` once the gate passes).

**Optional scene photo (photo-absent ref):** When the ref has NO scene photo (the photo is a per-post
variation the template merely supports, not the ref's default), the ai-image-zone for the scene photo
MUST be declared `optional: true`. This signals the ssc-image-generator to skip generation when no
`PHOTO_SUBJECT` is provided — the template falls back to the fixed bg texture (`_ai_bg/bg.png`). Generating the
scene photo unconditionally produces a blank `photo_main.png` (the model receives no subject to place).
Rule: if the ref is photo-absent, `optional: true` is mandatory. If the ref has a photo, `optional: true`
is optional (but recommended unless every post must have one).

## Real-photo slot legibility contract (fix coral-on-coral)
`legibility-method: natural-composition` is only valid when the template **CONTROLS the composition** — the
calm/dark zone is generated via the `prompt_delta`. When the filled zone is a **real-photo slot**
(`generation_route: none` — e.g. a creator headshot fills it per post, `craft/html-craft.md` §7), the template
controls nothing about what fills the zone, so the ref's legibility scene becomes a **CONTRACT** satisfied one
of two ways:
- **(a) hybrid regeneration** — the `prompt_delta` recreates the ref's framing + the calm/dark zone AROUND the
  real face (the headshot rides as `--input-image`), `when_ai_runs: every post`; or
- **(b) fixed gradient + declared slot requirements** — reproduce the ref's gradient as a fixed template
  element AND declare the slot's framing/palette requirements in the slot spec, then MEASURE the reserved-zone
  contrast against the ACTUAL preview fill (not the assumed one).

A `color_role: *-on-dark` over a slot with NO darkness guarantee is invalid — the run-06 creator-portrait-cta
shipped coral text assuming a dark fill and rendered coral-on-coral. Cross-ref: `craft/html-craft.md` §7.

**When a HERO FACE fills the slot, it carries the BRAND identity (the `scene-restyle-with-real-face` ROTA).**
A face/head that is a hero element (any medium) uses the brand **headshot** when one exists — generate via
image-edit with the ref (scene/medium) + the headshot (identity) as two `--input-image`s, **resolving the
headshot to its real path in the build**, never a generic `PHOTO_SUBJECT` (the `creator-cover-cta` miss). No
headshot → AI invents the person in the ref's style (soft default). See `craft/ai-prompt-craft.md` "ROTA —
scene-restyle-with-real-face".

**When the hero is a FIXED OBJECT (the template identity — `subject_role: fixed-hero`), recolor the ref, never
swap it.** If the slug names the object (`chain-*`) and the ref shows ONE dominant subject, the per-post prompt
keeps the object and recolors its accent (no free `{PHOTO_SUBJECT}`) — the `chain-highlight-headline` miss read
this as a free subject and the chain became gears. See `craft/ai-prompt-craft.md` "Fixed-hero recolor vs
free-subject swap".

## Fidelity to the ref (REMONTA / INVENTA)
- **The reserved band is the ref's band.** Read `ref_vision_summary.text_elements[].position` and reserve THAT
  band (top / bottom / left / right) — the `prompt_delta` and the HTML text both target it. No inverting
  top↔bottom: text in a bottom band when the ref reserves the **top sky** is the ref-05 REMONTA miss
  (`identification-tree.md` rule 4).
- **Legibility copies the ref's method.** Record `legibility-method: ref-band | natural-composition` per block in
  `rationale.md` §2. If the ref resolves legibility by natural composition (no band), the `prompt_delta` GENERATES
  the calm/dark reserved zone in the scene and **NO `.bottom-scrim` div is authored** — stamping a solid band the
  ref lacks is the run-02 INVENTA miss. A band is reproduced only when the ref shows one
  (`craft/ai-prompt-craft.md` "Legibility method copies the ref").

## Extra QA criterion (beyond the common gate)
- **Reserved zone:** the text landed on the clean reserved band, and that band is actually clean — crop the
  band and measure uniformity + luminance + black-text contrast (the breathing-room measurement). If the
  generation did NOT reserve the zone, re-roll with the reserved-zone instruction reinforced (gate try 2).
- **Treatment contract (Check B, `shared/quality-gate.md`):** if `rationale.md` declares a filled raster zone
  (the hero photo/landscape, filled every post), the rendered preview must NOT be a near-uniform empty region
  — an empty grey placeholder fails Check B (the test-09-06 body-numbered failure) → fill it or hide the zone.

> Before generation, the builder must pass **Check A** (`rationale.md` present + complete) — see
> `shared/quality-gate.md`.
