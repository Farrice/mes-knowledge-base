# Template: two-photo-list-body

source_ref: ../../../visual_refs/editorial/05-two-photo-stack.png
canvas: 1080x1350 (4:5 LinkedIn carousel)
strategy: html-overlay
role: body
style: editorial (`styles.json` → "editorial", Farrice's default for teardowns)

## Rationale

see rationale.md — form: a-framed-image (two contained-rectangle photo zones) · edit_mode: none (pure HTML;
the two photo slots receive real per-post source captures, never AI-generated imagery — brand policy)

## Inventory

```yaml
ignore_screenshot_chrome: []

bg_treatment:
  kind: solid-color
  has_baked_overlays: false
  needs_clean_ref: false
  cleaned_bg_path: null

requires_photo_zone: true
photo_zones:
  - kind: embedded-photo
    bbox: [51.85, 11.11, 40.37, 37.04]
    source: user-uploaded-asset
    notes: "real per-post source capture (product page / ad crop) — never AI-generated; sample = a real
      Huel Daily Greens product-page crop Farrice captured via Playwright, evidence/huel-greens/crop-scoop.png"
  - kind: embedded-photo
    bbox: [51.85, 49.63, 40.37, 39.26]
    source: user-uploaded-asset
    notes: "same as above; sample = evidence/huel-greens/crop-bubbles.png"

elements:
  - name: title
    bbox: [7.78, 5.33, 35, 2.6]
    type: text
    content: "Creative Teardown"
    decision: slot
    notes: "header/series-title label, top-left; editorial style relocates author identity to the footer"

  - name: date-arrow
    bbox: [66, 5.33, 26.44, 2.8]
    type: text
    content: "03 Sep, 2026 →"
    decision: slot
    notes: "per-slide date stamp + plain Unicode arrow glyph, right-aligned, flex-paired with title"

  - name: headline
    bbox: [7.78, 12.59, 43, 20]
    type: text
    content: "what<br>changed"
    decision: slot
    notes: "giant lowercase display word (editorial style signature move), 112px/10.37cqw, ink"

  - name: body-intro
    bbox: [7.78, 32.59, 40.74, 15]
    type: text
    content: "Across three years of creative rounds the format changed every quarter. The argument underneath did not move once."
    decision: slot
    notes: "24px/2.22cqw ink paragraph"

  - name: item-1
    bbox: [7.78, 48.89, 40.74, 8]
    type: text
    content: "2024 · studio statics — Product on white, the ingredient count in the headline."
    decision: slot
    notes: "bold year+label line + regular description; first of three, 160px/11.85% rhythm"

  - name: item-2
    bbox: [7.78, 60.74, 40.74, 8]
    type: text
    content: "2025 · creator UGC — Same claim, now spoken by a stranger in a kitchen."
    decision: slot

  - name: item-3
    bbox: [7.78, 72.59, 40.74, 8]
    type: text
    content: "2026 · dynamic variants — Same claim, cut into a thousand modular frames."
    decision: slot

  - name: footer-strip
    bbox: [7.78, 93.26, 84.44, 2.2]
    type: text
    content: "Farrice Cain · parallaxletter.substack.com · Supplement + performance brands · DM ANGLE"
    decision: slot
    notes: "4-item flex row, justify-content:space-between; the brand's author-identity content relocated to the footer for the editorial style"

chrome_observed:
  masthead_visible_in_ref: false
  pagination_dots_visible_in_ref: false
  page_indicator_visible_in_ref: false
```

## Visual summary

A two-column editorial body slide on the brand's flat canvas fill. The left column stacks a header row (series
title left, date + arrow right), a giant lowercase 2-line headline, an intro paragraph, and three dated list
items on a consistent vertical rhythm. The right column holds two stacked, hard-edged, contained photographs —
real per-post evidence crops (a product-page screenshot, an ad capture), never AI-generated or stock imagery.
A 4-item footer strip closes the slide with the author identity, the newsletter URL, the niche descriptor, and
a CTA label. Use this template for a "Creative Teardown"-style body slide that walks through a dated
progression (a timeline, an evolution, a before/now/next argument) illustrated by two real supporting images.

## AI Image

```
generation_route: none
ref_input: assets/ref-canonical.png (audit trail only — never passed as --input-image; no generator runs)
```

No `[ai-image-zone]` block. `PHOTO_MAIN_PATH` and `PHOTO_SECOND_PATH` are plain `<img>` slots
(`photo_zones[].source: user-uploaded-asset` above) that receive a real per-post capture — a screenshot or
crop of whatever product, ad, or creative the "Creative Teardown" post is examining. This is a deliberate
brand-mandated departure from AI-generated photography (see `rationale.md` §③/§④): `REVIEW-NOTES.md`
("every photo zone holds a REAL source… stock imagery rejected on sight"), `moves.md` #8 ("AI-generated
imagery is not evidence and never fills this zone"), and `tokens.json → prohibited` ("stock supplement
imagery as generic credibility", "faux-lab imagery"). The canonical preview fills both slots with real
Huel Daily Greens product-page crops Farrice captured 2026-09-03 (`assets/photo-main-sample.png`,
`assets/photo-second-sample.png`, sourced from
`visual-identity/compositions/editorial/evidence/huel-greens/`). Zero AI image-generation calls; zero
OpenAI budget consumed.

## Slots

- **TITLE** — header/series-title label (top-left)
  - bbox: 7.78% 5.33% 35% 2.6%
  - style: 2.41cqw, weight 700, letter-spacing −0.01em, `var(--brand-text-on-light)`, sentence case
  - sample: "Creative Teardown"

- **DATE** — per-slide date stamp (top-right, paired with a fixed arrow glyph)
  - bbox: 66% 5.33% 26.44% 2.8%, right-aligned
  - style: 2.04cqw, weight 400, `var(--brand-text-on-light)`
  - sample: "03 Sep, 2026"
  - user_editable: true

- **HEADLINE** — giant lowercase 2-line display word (HTML-bearing: supports `<br>`)
  - bbox: 7.78% 12.59% 43% 20%
  - style: brand display face, 10.37cqw, weight 700, line-height 0.92, letter-spacing −0.05em,
    `var(--brand-text-on-light)`, lowercase, left-align
  - sample: "what<br>changed"

- **BODY** — intro paragraph (HTML-bearing: supports `<mark>`/`<em>`/`<strong>`)
  - bbox: 7.78% 32.59% 40.74% 15%
  - style: 2.22cqw, weight 400, line-height 1.34, `var(--brand-text-on-light)`, left-align
  - sample: "Across three years of creative rounds the format changed every quarter. The argument underneath did not move once."

- **ITEM_1_LABEL** — first dated list-item heading
  - bbox: 7.78% 48.89% 40.74% 2.6%
  - style: 2.41cqw, weight 700, letter-spacing −0.02em, `var(--brand-text-on-light)`
  - sample: "2024 · studio statics"

- **ITEM_1_BODY** — first list-item description (HTML-bearing)
  - bbox: 7.78% 51.9% 40.74% 4%
  - style: 1.94cqw, weight 400, line-height 1.3, `var(--brand-text-on-light)`
  - sample: "Product on white, the ingredient count in the headline."

- **ITEM_2_LABEL** — second dated list-item heading
  - bbox: 7.78% 60.74% 40.74% 2.6%
  - style: 2.41cqw, weight 700, letter-spacing −0.02em, `var(--brand-text-on-light)`
  - sample: "2025 · creator UGC"

- **ITEM_2_BODY** — second list-item description (HTML-bearing)
  - bbox: 7.78% 63.75% 40.74% 4%
  - style: 1.94cqw, weight 400, line-height 1.3, `var(--brand-text-on-light)`
  - sample: "Same claim, now spoken by a stranger in a kitchen."

- **ITEM_3_LABEL** — third dated list-item heading
  - bbox: 7.78% 72.59% 40.74% 2.6%
  - style: 2.41cqw, weight 700, letter-spacing −0.02em, `var(--brand-text-on-light)`
  - sample: "2026 · dynamic variants"

- **ITEM_3_BODY** — third list-item description (HTML-bearing)
  - bbox: 7.78% 75.6% 40.74% 4%
  - style: 1.94cqw, weight 400, line-height 1.3, `var(--brand-text-on-light)`
  - sample: "Same claim, cut into a thousand modular frames."

- **PHOTO_MAIN_PATH** — upper framed photograph (real evidence crop)
  - bbox: 51.85% 11.11% 40.37% 37.04%
  - style: `object-fit:cover`, no radius, no shadow (`_editorial.css .photo` — no decorative frame chrome)
  - sample: `assets/photo-main-sample.png` (real Huel Daily Greens product-page crop)
  - user_editable: true

- **PHOTO_SECOND_PATH** — lower framed photograph (real evidence crop)
  - bbox: 51.85% 49.63% 40.37% 39.26%
  - style: `object-fit:cover`, no radius, no shadow
  - sample: `assets/photo-second-sample.png` (real Huel Daily Greens macro crop)
  - user_editable: true

- **FOOTER_NAME** — author identity (footer, item 1 of 4)
  - style: 1.85cqw, weight 400, `var(--brand-text-on-light)`
  - sample: "Farrice Cain"

- **FOOTER_URL** — newsletter URL (footer, item 2 of 4)
  - style: 1.85cqw, weight 400, `var(--brand-text-on-light)`
  - sample: "parallaxletter.substack.com"

- **FOOTER_DESCRIPTOR** — niche descriptor (footer, item 3 of 4)
  - style: 1.85cqw, weight 400, `var(--brand-text-on-light)`
  - sample: "Supplement + performance brands"

- **FOOTER_CTA** — CTA label (footer, item 4 of 4)
  - style: 1.85cqw, weight 400, `var(--brand-text-on-light)`
  - sample: "DM ANGLE"
  - user_editable: true
  - bbox (footer row, all 4 slots): 7.78% 93.26% 84.44% 2.2%, flex `justify-content:space-between`

## Fixed elements (not slot-editable)

- The `#F3F3F0` canvas fill — CSS `background: var(--brand-bg-light);`, never a slot.
- The header row's 2-slot flex layout (left = title, right = date+arrow) and the footer row's 4-slot flex
  layout — the layouts are fixed; only the slot VALUES are editable.
- The arrow glyph "→" next to the date — fixed typographic content, not a data-slot.
- The photo frames' geometry (position, size, `object-fit:cover`, no radius/shadow) — fixed; only the image
  FILL (`PHOTO_MAIN_PATH` / `PHOTO_SECOND_PATH`) is editable.
- The list items' repeating 160px/11.85% vertical rhythm.

## Strategy notes

- All text zones are html-overlay. No ai-edit needed — `edit_mode: none`.
- No chrome injected from `tokens.json → chrome.masthead` (that move is NOT used on this editorial-style slide
  — the editorial style's own header/footer grammar replaces it, confirmed against all eight approved
  editorial reference frames, not a one-off).
- Bg is solid `var(--brand-bg-light)` via CSS — no `_ai_bg/bg.png` file for this template.
- Both photo slots are real-upload zones (`source: user-uploaded-asset`) — zero AI generation, zero API cost.

## Possible future variations

- Allow a 2- or 4-item list instead of the sampled 3 (each item is its own pair of slots; add/remove a pair
  and keep the 160px rhythm).
- Allow `BODY` to carry an `<mark>` accent word for a variant that wants one emphasized term in the intro.

## Craft notes

Every bbox/font-size number in this Template Card is read directly from the exact HTML/CSS source this ref
PNG was rendered from (`visual-identity/compositions/editorial/frames/05-two-photo-stack.html` +
`_editorial.css`, both authored and approved by Farrice 2026-09-03) — not estimated from pixel-scanning the
PNG alone (though an independent pixel scan of the rendered PNG cross-confirmed every measurement to within
rounding). The `HEADLINE` bbox width is trimmed to 43% (vs. the source's literal 44.44%/480px) as a defensive
margin so the authored bbox never geometrically touches the photo column's left edge (51.85%) — the actual
rendered glyphs ("changed") are well clear of that edge in every version, so this trim has zero visual effect.
