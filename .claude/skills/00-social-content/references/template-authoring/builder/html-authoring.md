# Builder reference — universal HTML authoring rules (Step 4 deep detail)

> Read at **Step 4**, when writing `template.html`. The craft for making HTML *alive* is `craft/html-craft.md`; the slot/anatomy schema is `shared/conventions/slots-and-html.md`. This file carries the universal authoring rules + the `[ai-image-zone]` write-back detail.

Universal HTML rules (the craft for making it *alive* is in `html-craft.md`):
- **`data-slot` on every editable zone**, set to the exact Mustache key with trailing `_PATH`/`_HTML`/`_SRC`
  stripped. The handle `render_template.py --tweaks` and the Content Studio editor key overrides by.
- **Triple-brace `{{{SLOT}}}` for HTML-bearing slots** (headline/title/subhead/body/CTA — carry `<mark>`,
  `<br>`, `<em>`, `<strong>`). Double-brace `{{SLOT}}` only for plain-text-only slots (numerals/dates/handles).
- **Image slots end in `_PATH`** (the suffix that inlines the image).
- **Display/headline zones get the `display`/`headline`/`kicker` class** (or `data-role="display"`) so they
  inherit the brand display font with the SANS fallback tail — never let a display zone fall to a serif.
- Add the `[ai-image-zone:N]` block above `<style>` reflecting the route from Step 3 (ref_input + delta).
  **WRITE the structured `image_style: {medium, lighting, subject_treatment}` into the block** — the three STYLE
  reads from `rationale.md` §2 (the ref's, not the grade's). This is the LOAD-BEARING step: the image-generator
  reads `image_style` per-template (Step 5.8) and concatenates identity → style → delta; if you omit it, the
  generator falls back to the grade's `default_*` and this template's style is lost (the run-07 class). For any
  field the ref left genuinely ambiguous, leave it blank/omit it and the generator inherits the grade
  `default_*` for that one field — never copy the grade in just to fill it (that re-imposes the grade). Format
  per `template-conventions.md` `[ai-image-zone]` → Route A.
- **WRITE `subject_role` + `render_register` into the `[ai-image-zone]` block.** `subject_role`
  (`fixed-hero | free-subject`, from §2) selects which `prompt_delta` shape you author — fixed-hero recolors the
  ref (no free `{PHOTO_SUBJECT}`), free-subject swaps (`template-conventions.md` → the two `prompt_delta`
  variants). `render_register` is a one-line **echo of the style you read + baked into the prompt opener**
  (e.g. `flat-illustration / natural / full-bleed`) — a RECORD for the post-render conference, NOT a gate: if
  the image's style ends up different the conference WARNS (style is judgment, never a trava — Gustavo's
  principle), it does not block. It lets a reader confirm the prompt inherited the ref's style (the run-07
  services-billboard failure was the grade opener overriding the ref).
- **Never** rebuild the hero scene as HTML/SVG/CSS — it lives inside the image zone.
- **Type-craft floors (SPEC-B, `html-craft.md` §3):** display ≥ 9cqw, body ≥ 3.2cqw; display line-height ~0.95,
  letter-spacing −0.02…−0.035em (the shared defaults set these). Lay the text stack out as ONE flow column
  (no per-block `top:%`) so there is no hollow middle. **Never** locally override `mark { color }` — let the
  shared surface-aware rule drive the coral accent.
- **Headline composition contract (`html-craft.md` §3.6)** — a headline-led slide declares the headline's
  **bbox target ≈ 58–65% of canvas**, ≥ 8% side margins, kicker reserved at top, and the **footer pill
  reinstated as the bottom anchor** (never SKIP a footer the ref shows — it centers the composition). Keep
  typographic **variety** (sentence-case + italic/heavy emphases + a medium-weight connector — not one flat
  "Anton heavy" slab). The per-post **fit** is `html-craft.md` §3.5 (auto-shrink; the authored size is the
  ceiling) — referenced, NOT restated here; overflow *detection* is the r6g gate. (about-callout miss: headline
  baked into the AI, burst the frame; in HTML it needs this contract.)
- **Isolability — `text-on-scene-no-box` is the default (`html-craft.md` §4).** Text over a scene gets NO
  box/border/chip unless the ref shows a real material edge (survives erasing the text). "Callout/highlight" is
  text WEIGHT/COLOUR, not an invented coral box (the numbered-photo phantom-rectangle miss). Preserve a
  paragraph STACK — N left-aligned paragraphs are N stacked zones, never merged + a final line promoted to a
  pill.
- **When `_measurements.yaml` exists it is the POSITION CONTRACT (`template-conventions.md`).** Author each
  block `absolute` to its measured bbox; a flow column is allowed only if each block lands within its bbox
  tolerance. Collapsing spread-out measured blocks into one top-anchored `justify-content:flex-start` column is
  the kraft miss.
- **A hero FACE carries the brand identity, resolved IN THE BUILD (`html-craft.md` §7 + the
  `scene-restyle-with-real-face` ROTA).** ANY hero face/head (any medium), not only "creator covers": author a
  `user_editable: true` `PHOTO_*_PATH` slot, declare `brand-headshot` in `bg_substitution_methods`, and **when a
  headshot exists, RESOLVE it to its real path in the build** (the identity `--input-image`) — never leave the
  slot a literal string placeholder, and never pass a generic `PHOTO_SUBJECT` person description (both were the
  `creator-cover-cta` defect). No headshot → AI invents the person in the ref's style (soft default; the slot
  may carry a TEXT marker, never a hole).
- **Brand seal = ONE glyph in its OWN colour, never `filter:invert`/`brightness(0)` (`shared/icons.md`).**
  Render a provided coloured logo as-is; two layers (shell+logo) only when the ref shows two shapes; if it must
  read on dark, put it on its own light card — never filter the colour away (the one-page miss).
