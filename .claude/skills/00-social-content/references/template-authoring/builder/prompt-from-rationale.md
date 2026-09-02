# Builder reference — prompt-from-rationale (Step 3 deep detail)

> Read at **Step 3**, after `scenarios/<form>.md`, when authoring the `prompt_delta`. The spine carries Check A + the scenario read + ref-save; this file carries the per-bullet prompt-from-rationale rules. Generate the `prompt_delta` FROM `rationale.md` §2 per-block treatment (`ai-prompt-craft.md` → "Faithful prompt-from-rationale"), not from a blanket template.

Generate per the scenario's edit mode (`ai-prompt-craft.md` has the exact prompts and the
`generate_image_gpt.py` invocation). The ref is ALWAYS the first `--input-image`; the prompt is ONLY the
delta. **Generate the `prompt_delta` FROM `rationale.md`'s §2 per-block treatment** (`ai-prompt-craft.md` →
"Faithful prompt-from-rationale"), not from a blanket template — the divergence between the two is exactly
what shipped the test-09-06 misses:
- The "no text" clause applies ONLY to blocks the rationale routed to **HTML**. A block the rationale declared
  **AI-integrated** (occluded headline, text-on-surface) must be **DESCRIBED** in the prompt — never forbidden
  by a blanket "No text, no lettering, no captions" (the ref-01 contradiction).
- `total-recompose` must NOT collapse isolable text (caption / CTA / byline / badge / label) into the AI zone
  — those stay HTML overlay (the ref-07 violation). Only genuinely-integrated text may be AI.
- For B1, use the surface-PRESERVING edit (clean + reserve + reuse), never `total-recompose` (the ref-02 miss).
- A reserved-zone % is ONE number shared by the `prompt_delta` and the HTML geometry (the ref-03 collision).
- **Medium, lighting AND treatment are the ref's, inherited — not the grade's opener prepended blindly.** Open
  the `prompt_delta` in the `medium` / `lighting` / `subject_treatment` you read into `rationale.md` §2: a
  `flat-illustration` + `natural` + `full-bleed` ref opens *"flat vector illustration, natural light, full-bleed
  scene, in <brand palette>, <brand grain>, …"*; a `photo` + `dramatic` + `isolated-on-light-bg` ref opens
  *"documentary photograph, dramatic light, subject isolated on light bg, <brand palette>, <brand grain>, …"*.
  Do NOT prepend `ai-image-style.md`'s style opener when it contradicts the ref (a documentary/studio-flat opener
  over a cartoon natural-light ref forces the wrong look — the run-07 `services-billboard` miss). The brand grade
  supplies only the IDENTITY — palette / accent / grain; medium / lighting / treatment come from the ref. When a
  ref's style field is ambiguous, fall back to the grade's `default_medium` / `default_lighting` /
  `default_subject_treatment` for that field (`ai-prompt-craft.md` → "Medium, lighting and treatment are the
  ref's"). The brand-mixed case (`default_medium: mixed`) ships no medium opener/negative of its own — the style
  enters here, per ref.
- Tonal words match the ref (a light/sand ref is never prompted "dark"; the ref-05 miss).
- The bg `prompt_delta` carries the ref's distinctive GRAPHIC device, not only palette + subject
  (`ref_vision_summary.image_zone.distinctive_graphics` → delta; `ai-prompt-craft.md` rule 5). Dropping ref-01's
  radial line-burst for a flat coral fill is the run-02 ESQUECE miss.
- Legibility over the photo COPIES the ref's method, recorded per block in `rationale.md` §2 as
  `legibility-method: ref-band | natural-composition`: ref has no band → the delta generates the dark/calm zone
  in the scene and NO `.bottom-scrim` div is authored; ref has a band → reproduce the solid band. Stamping a band
  the ref lacks is the run-02 INVENTA miss (see the scrim anti-pattern).
- Framing is binding: a `contained-rectangle` ref builds a contained image zone, a `full-bleed` ref builds
  full-bleed — never inverted (the run-02 REMONTA miss; `identification-tree.md` rule 4). The reserved band's
  position is the ref's (`text_elements[].position`), never re-chosen.
- **Element routing follows each `distinctive_elements` `treatment`** (`identification-tree.md` rule 6 +
  `ai-prompt-craft.md` "Element routing"). A **small brand mark** (badge/seal/logo) is `SVG-overlay` — it is
  NOT described in the `prompt_delta` at all (the AI drops small marks; the cover-hook Claude starburst
  vanished) — it is composited as an HTML/SVG overlay. A **non-occluded dominant display** is `HTML`, authored
  prominent (large `display` class) — NOT pushed into the AI image (the cover-hook "the one page" miss). A
  display **genuinely occluded by the subject** is `AI-baked` and its `prompt_delta` block MUST state explicit
  **DOMINANT / large scale** — quote the word, weight the scale early — never "lower-center integrated" with no
  scale (the cover-hook "system" ghost-size miss; `ai-prompt-craft.md` "Dominant-display scale").
- **Pill / callout fill is the ref's fill** read in `distinctive_elements.fill`: the HTML pill `background`
  uses the ref's colour (cover-hook's bottom pill is **white** in ref-01, not brand colour) — and its bbox
  matches the read `size`/`position`, never inflated full-width (the body-numbered miss).
- **Fixed-hero recolors the ref; free-subject swaps it** (`rationale.md` §2 `subject_role`, →
  `ai-prompt-craft.md` "Fixed-hero recolor vs free-subject swap"). When `subject_role: fixed-hero` (the slug
  names the object, ONE dominant ref subject), the `prompt_delta` **keeps the object and recolors the ref**
  (*"Keep the EXACT subject — a metal chain with one accent link; recolor the accent → brand coral; vary only
  framing/angle/lighting"*) with NO free `{PHOTO_SUBJECT}` slot. NEVER *"Change the subject to: {PHOTO_SUBJECT}"*
  with example values that are *different objects* on a fixed-hero — that is the `chain-highlight-headline`
  defect (the chain became gears). `free-subject` keeps the default "change the subject" opener.
- **A hero FACE uses the brand headshot, resolved IN THE BUILD** (`rationale.md` §2 `hero_face_identity`, →
  `ai-prompt-craft.md` "ROTA — scene-restyle-with-real-face"). When `hero_face_identity: brand-headshot`,
  generate via image-edit with TWO `--input-image`s — the ref (scene/medium) + the real headshot path
  (identity) — and the face carries the brand person restyled for the ref's medium. **The headshot resolves to
  its real path in the build** — never a literal string placeholder in the slot — and **`PHOTO_SUBJECT` is NOT
  a generic person description** when a headshot exists (both were the `creator-cover-cta` defect → random
  face). No headshot (`invented`) → the AI invents the person in the ref's style (the valid soft default; the
  identity slot may carry a TEXT marker `[fill with the brand headshot when one exists]`, never a hole).
