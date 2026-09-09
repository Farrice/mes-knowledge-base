# Template: photo-right-columns-body

source_ref: ../../../visual_refs/editorial/03-photo-right-columns.png
canvas: 1080x1350 (4:5 LinkedIn carousel)
strategy: mixed (html-overlay text + a real supplied evidence-crop asset — no AI generation anywhere)
role: body

## Rationale

see rationale.md — form: `a-framed-image` · edit_mode: `none`. A contained evidence-crop photo (right column,
Move #8 "Evidence crop") sits beside a giant lowercase display headline on the flat canvas; a body paragraph
and a hairline-separated three-item breakdown fill the lower two-thirds. The photo zone is a REAL supplied
asset per `moves.md` #8 ("AI-generated imagery is not evidence and never fills this zone") — never
`edit-from-ref`, overriding the `a-framed-image` scenario's generic AI-generation default. Full per-block
treatment + the per-element ref-anchored reads live in `rationale.md` §2; the override reasoning lives in §3–④.

## Inventory

```yaml
bg_treatment:
  kind: solid-color
  has_baked_overlays: false
  needs_clean_ref: false
  cleaned_bg_path: null

requires_photo_zone: true
photo_zones:
  - kind: embedded-photo
    bbox: [50, 11.11, 42.22, 45.93]
    source: user-uploaded-asset
    notes: "Move #8 evidence crop — a real product-page / ad / label screenshot supplied per post, contained
      rectangle, object-fit:contain on a paper backing, no radius, no shadow. Never AI-generated."

elements:
  - name: series-title
    bbox: [7.78, 5.33, 40, 3]
    type: text
    content: "Creative Teardown"
    decision: slot
    notes: "editorial-mode masthead left slot — series identity label, ink, sentence case"

  - name: date
    bbox: [55, 5.33, 29.44, 3]
    type: text
    content: "03 Sep, 2026"
    decision: slot
    notes: "editorial-mode masthead right slot, paired with a fixed arrow glyph (not a slot)"

  - name: photo-zone
    bbox: [50, 11.11, 42.22, 45.93]
    type: image
    decision: slot
    notes: "PHOTO_MAIN_PATH — real evidence crop, see photo_zones above"

  - name: headline
    bbox: [7.78, 40, 40.74, 17]
    type: text
    content: "the<br>claim"
    decision: slot
    notes: "giant lowercase 2-line display stack, ink, left column beside the photo"

  - name: body
    bbox: [7.78, 59.85, 84.44, 11.5]
    type: text
    content: "Seventy-five vitamins, minerals and whole-food sourced ingredients. One scoop. Foundational nutrition. Three phrases have carried the brand for a decade, and the creative team keeps re-lighting them."
    decision: slot
    notes: "full-width paragraph below the headline column and the photo zone"

  - name: hairline-rule
    bbox: [7.78, 72.59, 84.44, 0.1]
    type: rule
    content: null
    decision: skip
    reason: "structural decision-line move (moves.md #3), a 1px CSS border, not slot-editable content"

  - name: item-1
    bbox: [7.78, 74.81, 25.19, 8]
    type: text
    content: "Ingredient truth / What the formula can honestly carry, and what it cannot."
    decision: slot
    notes: "title + supporting line, column 1 of 3"

  - name: item-2
    bbox: [37.41, 74.81, 25.19, 8]
    type: text
    content: "Buyer tension / The fear the buyer holds before they read the label."
    decision: slot
    notes: "title + supporting line, column 2 of 3"

  - name: item-3
    bbox: [67.04, 74.81, 25.19, 8]
    type: text
    content: "Proof boundary / Where the evidence stops and the adjective begins."
    decision: slot
    notes: "title + supporting line, column 3 of 3"

  - name: footer-strip
    bbox: [7.78, 90.5, 84.44, 3]
    type: text
    content: "Farrice Cain / parallaxletter.substack.com / Supplement + performance brands / DM ANGLE"
    decision: slot
    notes: "4-item editorial footer chrome — author, link, audience descriptor, CTA"

chrome_observed:
  masthead_visible_in_ref: true
  pagination_dots_visible_in_ref: false
  page_indicator_visible_in_ref: false
```

## Visual summary

An evidence-teardown body slide on the brand's flat canvas fill: a real product/ad/label screenshot sits
contained in the right column (Move #8, never AI-generated — the brand's proof-you-can-inspect stance forbids
fabricated evidence), paired on the left with a giant lowercase 2-line verdict headline. A full-width paragraph
explains the claim below both columns, then a hairline rule opens onto a 3-column breakdown (title + supporting
line each) that interrogates the claim from three angles. A 4-item footer strip closes the slide with author
identity, the newsletter link, the audience descriptor, and a DM-based CTA. Use for any "creative teardown" body
slide that shows a real piece of evidence and argues a specific point about it.

## AI Image

```
generation_route: none
ref_input: none
```

No `[ai-image-zone]` block. `PHOTO_MAIN_PATH` binds a real, per-post supplied asset (a screenshot / crop of the
actual thing being torn down) — `rationale.md` §3 explains why this overrides the `a-framed-image` scenario's
default `edit-from-ref` generation (Move #8 forbids AI imagery in an evidence zone). The sample render uses the
same real crop the canonical ref itself was built from (`compositions/editorial/evidence/huel-greens/crop-hero.png`,
copied to `_ai_bg/photo_main.png`) — not a generated image.

## Slots

- **SERIES_TITLE** — masthead left, series identity label
  - bbox: 7.78% 5.33% 40% 3%
  - style: display face, 2.41cqw, weight 700, letter-spacing -0.01em, ink, left-aligned
  - sample: "Creative Teardown"
  - user_editable: true

- **DATE** — masthead right, publish date (paired with a fixed arrow glyph)
  - bbox: 55% 5.33% 29.44% 3%, right-aligned within the masthead row
  - style: display face, 2.04cqw, weight 400, ink
  - sample: "03 Sep, 2026"
  - user_editable: true

- **PHOTO_MAIN** — the evidence crop (real, per-post supplied image; binds `PHOTO_MAIN_PATH`)
  - bbox: 50% 11.11% 42.22% 45.93%
  - style: contained rectangle, `object-fit:contain`, paper backing (`var(--brand-text-on-dark)` ≈ `#FAFAF8`),
    no radius, no shadow
  - sample: `_ai_bg/photo_main.png` (a real Huel product-page screenshot crop)
  - user_editable: true

- **HEADLINE** — giant lowercase 2-line display verdict (HTML-bearing: supports `<br>`)
  - bbox: 7.78% 40% 40.74% 17% (fixed height, `overflow:hidden` — auto-shrink net applies)
  - style: display face, 10.93cqw, weight 700, line-height 0.92, letter-spacing -0.05em, ink, left-aligned,
    lowercase as authored (not CSS-forced)
  - sample: "the<br>claim"
  - user_editable: true

- **BODY** — full-width explanatory paragraph (HTML-bearing: supports `<mark>`/`<em>`/`<strong>`/`<br>`)
  - bbox: 7.78% 59.85% 84.44% 11.5% (fixed height, `overflow:hidden` — auto-shrink net applies)
  - style: body face, 2.41cqw, weight 400, line-height 1.34, ink, left-aligned
  - sample: "Seventy-five vitamins, minerals and whole-food sourced ingredients. One scoop. Foundational nutrition. Three phrases have carried the brand for a decade, and the creative team keeps re-lighting them."
  - user_editable: true

- **ITEM_1_TITLE** — breakdown column 1 title
  - bbox: within column 1 (7.78% 74.81% 25.19% —), stacked above ITEM_1_TEXT
  - style: display face, 2.41cqw, weight 700, letter-spacing -0.02em, ink
  - sample: "Ingredient truth"
  - user_editable: true

- **ITEM_1_TEXT** — breakdown column 1 supporting line (HTML-bearing: supports `<br>`)
  - bbox: within column 1, below ITEM_1_TITLE
  - style: body face, 1.94cqw, weight 400, line-height 1.3, ink
  - sample: "What the formula can honestly carry, and what it cannot."
  - user_editable: true

- **ITEM_2_TITLE** — breakdown column 2 title
  - bbox: within column 2 (37.41% 74.81% 25.19% —), stacked above ITEM_2_TEXT
  - style: display face, 2.41cqw, weight 700, letter-spacing -0.02em, ink
  - sample: "Buyer tension"
  - user_editable: true

- **ITEM_2_TEXT** — breakdown column 2 supporting line (HTML-bearing: supports `<br>`)
  - bbox: within column 2, below ITEM_2_TITLE
  - style: body face, 1.94cqw, weight 400, line-height 1.3, ink
  - sample: "The fear the buyer holds before they read the label."
  - user_editable: true

- **ITEM_3_TITLE** — breakdown column 3 title
  - bbox: within column 3 (67.04% 74.81% 25.19% —), stacked above ITEM_3_TEXT
  - style: display face, 2.41cqw, weight 700, letter-spacing -0.02em, ink
  - sample: "Proof boundary"
  - user_editable: true

- **ITEM_3_TEXT** — breakdown column 3 supporting line (HTML-bearing: supports `<br>`)
  - bbox: within column 3, below ITEM_3_TITLE
  - style: body face, 1.94cqw, weight 400, line-height 1.3, ink
  - sample: "Where the evidence stops and the adjective begins."
  - user_editable: true

- **FOOTER_NAME** — footer item 1, author identity
  - bbox: within the footer strip (7.78% 90.5% 84.44% 3%), leftmost of 4
  - style: body face, 1.85cqw, weight 400, ink
  - sample: "Farrice Cain"
  - user_editable: true

- **FOOTER_LINK** — footer item 2, newsletter link
  - bbox: within the footer strip, 2nd of 4
  - style: body face, 1.85cqw, weight 400, ink
  - sample: "parallaxletter.substack.com"
  - user_editable: true

- **FOOTER_TOPIC** — footer item 3, audience descriptor
  - bbox: within the footer strip, 3rd of 4
  - style: body face, 1.85cqw, weight 400, ink
  - sample: "Supplement + performance brands"
  - user_editable: true

- **FOOTER_CTA** — footer item 4, call to action
  - bbox: within the footer strip, rightmost of 4
  - style: body face, 1.85cqw, weight 400, ink
  - sample: "DM ANGLE"
  - user_editable: true

## Fixed elements (not slot-editable)

- The `#F3F3F0` canvas fill — CSS `background: var(--brand-bg-light);`, never a slot.
- The hairline rule (moves.md decision-line move) — CSS `border-top: 1px solid var(--brand-text-on-light);
  opacity: 0.15;`, structural, not content.
- The masthead's and footer's flex layout (`display:flex; justify-content:space-between;`, never `float`) —
  the layout pattern is fixed; only the slot VALUES are editable.
- The arrow glyph ("→") beside `DATE` — a fixed decorative character, not a slot.
- The photo zone's containment geometry (bounded rectangle, `object-fit:contain`, paper backing, no
  radius/shadow) — fixed template geometry; only the image FILE (`PHOTO_MAIN_PATH`) is editable.
- The three-item row's column structure (3 equal columns, uniform gutter) — fixed geometry; only the title/text
  VALUES per column are slots.

## Strategy notes

- Text zones are html-overlay. The photo zone is a real supplied asset, never AI-generated
  (`rationale.md` §3 — Move #8 "Evidence crop").
- Chrome injected: editorial-mode masthead (series title + date, per this ref's own grammar — NOT the pool's
  typographic-mode `FARRICE CAIN` + field-index masthead, per `styles.json`'s style split) + a 4-item footer
  strip (author / link / audience / CTA).
- Bg is solid `var(--brand-bg-light)` via CSS — no `_ai_bg/bg.png` file; `_ai_bg/photo_main.png` is the sample
  fill for the real evidence-crop slot only.

## Possible future variations

- Allow the three-item row to run with 2 items instead of 3 for a shorter breakdown (would need a template
  variant — the 3-equal-column geometry is currently fixed).
- Allow `HEADLINE` to run 1 line instead of 2 for a single-word verdict.
