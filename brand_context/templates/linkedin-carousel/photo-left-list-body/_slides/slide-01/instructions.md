# Template: photo-left-list-body

source_ref: ../../../visual_refs/editorial/04-photo-left-list.png
canvas: 1080x1350 (4:5 LinkedIn carousel)
strategy: html-overlay (no AI generation anywhere in this template)
role: body

## Rationale

see rationale.md — form: a-framed-image · edit_mode: none (deliberate override of Form A's default
`edit-from-ref` — moves.md #8 "Evidence crop" forbids AI-generated evidence imagery in this zone).

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
    bbox: [0, 8.0, 54.0, 84.0]
    source: user-uploaded-asset
    notes: "the evidence-crop — a real screenshot of the product/landing page under teardown, uploaded per post; canonical-preview demo asset is a deterministic non-AI wireframe placeholder (_ai_bg/photo_main.png)"

elements:
  - name: masthead-left
    bbox: [7.78, 5.0, 25.0, 2.4]
    type: text
    content: "Creative Teardown"
    decision: slot
    notes: "content-pillar kicker, title-case bold — read literally from this ref, diverges from the sibling pool's tracked-uppercase masthead convention (see rationale.md §④)"

  - name: date-label
    bbox: [75.0, 5.0, 14.0, 2.4]
    type: text
    content: "03 Sep, 2026"
    decision: slot
    notes: "publish-date stamp + a static typographic arrow glyph (not a slot, not an icon asset) — a different semantic from the sibling pool's page-position field index"

  - name: evidence-crop
    bbox: [0, 8.0, 54.0, 84.0]
    type: photo
    content: "product-page screenshot under teardown"
    decision: slot
    notes: "bleed-left contained-rectangle (Form A); never AI-generated per moves.md #8 — real per-post upload in production"

  - name: headline
    bbox: [52.0, 14.5, 40.2, 15.7]
    type: text
    content: "three angles"
    decision: slot
    notes: "the dominant idea; brand display face, lowercase preserved exactly as authored in the ref"

  - name: subhead
    bbox: [52.0, 32.6, 40.2, 12.4]
    type: text
    content: "The same product can argue three different things. Only one of them is worth funding first."
    decision: slot
    notes: "graphite subtitle-register paragraph directly under the headline"

  - name: list-1
    bbox: [52.0, 48.6, 40.2, 11.5]
    type: text
    content: "Ingredient / Seventy-five things in one scoop. The claim they already own and everyone else copies."
    decision: slot
    notes: "bold ink label + graphite paragraph, repeated pattern shared with list-2/list-3"

  - name: list-2
    bbox: [52.0, 62.6, 40.2, 11.5]
    type: text
    content: "Outcome / What a person feels by week three. Honest, specific, and almost never in the ads."
    decision: slot

  - name: list-3
    bbox: [52.0, 76.7, 40.2, 11.5]
    type: text
    content: "Ritual / The morning glass. The format is the argument, and nobody has led with it."
    decision: slot

  - name: footer-row
    bbox: [7.78, 90.5, 84.44, 2.4]
    type: text
    content: "Farrice Cain · parallaxletter.substack.com · Supplement + performance brands · DM ANGLE"
    decision: slot
    notes: "4-slot flex space-between row (masthead pattern reused at the bottom edge); name/url/descriptor are static brand identity, CTA is the per-post-variable item"

chrome_observed:
  masthead_visible_in_ref: true
  pagination_dots_visible_in_ref: false
  page_indicator_visible_in_ref: false
```

## Visual summary

A two-column editorial body slide: a bounded, bleed-left "evidence crop" (a real product/landing-page
screenshot under teardown, moves.md #8) fills the left ~54% of the canvas on a line/border-toned field with a hairline
edge; the right column carries the argument in pure HTML type — a two-line lowercase display headline ("three
angles"), a graphite subhead, and three repeated label+paragraph items (Ingredient / Outcome / Ritual) in a
single flowing column. A full-width masthead row (content kicker + publish date) sits above both columns; a
4-item footer row (name, url, category descriptor, CTA) anchors the bottom. Use this template for a "Creative
Teardown"-style body slide that examines a real captured source next to a structured written breakdown.

## AI Image

```
generation_route: none
ref_input: none
```

No `[ai-image-zone]` block — the evidence-crop (`PHOTO_MAIN_PATH`) is deliberately NEVER AI-generated
(rationale.md §③/§④; moves.md #8 explicitly bans AI-generated imagery in this zone). In production the
operator uploads a real screenshot of the page under teardown. This build's canonical-preview demo asset
(`_ai_bg/photo_main.png`) is a deterministic, zero-AI-call wireframe placeholder (drawn once with Pillow —
outline rating dots, bar-shaped text placeholders, four thumbnail-shaped swatches, a bordered "subscribe"
block, and a centered "PASTE REAL SCREENSHOT HERE" watermark) so the rendered preview shows real, non-uniform
content in that zone without fabricating fake product data.

## Slots

- **KICKER** — content-pillar kicker (top-left). NOTE: deliberately NOT named `MASTHEAD_LEFT` —
  `render_template.py`'s `apply_masthead_tokens` hard-overrides that reserved name from
  `tokens.json > chrome.masthead.labels` unconditionally, which would silently replace this ref's
  literal "Creative Teardown" with the brand wordmark. See rationale.md §④.
  - bbox: 7.78% 5.0% 25% 2.4%
  - style: Helvetica Neue 700, 2.2cqw, title/sentence case (no uppercase transform), no tracking, ink
  - sample: "Creative Teardown"
  - user_editable: true

- **DATE_LABEL** — publish-date stamp (top-right, with a static `→` glyph)
  - bbox: 75% 5.0% 14% 2.4%, right-aligned
  - style: Helvetica Neue 700, 2.2cqw, ink
  - sample: "03 Sep, 2026"
  - user_editable: true

- **PHOTO_MAIN_PATH** — the evidence-crop image (a real per-post screenshot of the page under teardown)
  - bbox: 0% 8% 54% 84%
  - style: `object-fit:cover` on a `line`/`border_subtle` (`var(--brand-line)`) field — deliberately NOT the
    literal `paper` token; see rationale.md Q3 build note (paper sits too close to the canvas fill for the
    quality-gate's near-uniformity read) — hairline border (`var(--brand-line)`, moves.md #3's decision-line
    token) on top/right/bottom,
    no border-radius, no drop shadow (moves.md #8)
  - sample: `_ai_bg/photo_main.png` (deterministic non-AI wireframe placeholder — never a fabricated
    "real-looking" product screenshot)
  - user_editable: true

- **HEADLINE** — the dominant 2-line display statement (HTML-bearing: supports `<br>`/`<mark>`)
  - bbox: 59% 14.5% 33.2% ~15.7% (box-grows with content, inside the right-column flow)
  - style: brand display face, 9.8cqw, weight 700, line-height 1.0, letter-spacing -0.025em,
    `var(--brand-text-on-light)`, lowercase preserved as authored
  - sample: "three angles"
  - user_editable: true
  - max_chars: ~24 (auto-shrinks toward the 8cqw floor if longer)

- **SUBHEAD** — the supporting paragraph (HTML-bearing: supports `<br>`/`<mark>`/`<strong>`)
  - bbox: 59% 32.6% 33.2% ~12.4% (box-grows with content)
  - style: subtitle register, 3.4cqw, weight 400, line-height 1.3, `var(--brand-secondary)`
  - sample: "The same product can argue three different things. Only one of them is worth funding first."
  - user_editable: true

- **LIST_1_LABEL** — first list item's label (Ingredient)
  - bbox: 59% 48.6% 33.2% 3.2% (box-grows)
  - style: 3.6cqw, weight 700, ink
  - sample: "Ingredient"
  - user_editable: true

- **LIST_1_BODY** — first list item's paragraph (HTML-bearing: supports `<mark>`/`<strong>`)
  - bbox: 59% 52.5% 33.2% 7.6% (box-grows)
  - style: 3.4cqw, weight 400, `var(--brand-secondary)`, line-height 1.4
  - sample: "Seventy-five things in one scoop. The claim they already own and everyone else copies."
  - user_editable: true

- **LIST_2_LABEL** — second list item's label (Outcome)
  - bbox: 59% 62.6% 33.2% 3.2% (box-grows)
  - style: 3.6cqw, weight 700, ink
  - sample: "Outcome"
  - user_editable: true

- **LIST_2_BODY** — second list item's paragraph (HTML-bearing: supports `<mark>`/`<strong>`)
  - bbox: 59% 66.5% 33.2% 7.6% (box-grows)
  - style: 3.4cqw, weight 400, `var(--brand-secondary)`, line-height 1.4
  - sample: "What a person feels by week three. Honest, specific, and almost never in the ads."
  - user_editable: true

- **LIST_3_LABEL** — third list item's label (Ritual)
  - bbox: 59% 76.7% 33.2% 3.2% (box-grows)
  - style: 3.6cqw, weight 700, ink
  - sample: "Ritual"
  - user_editable: true

- **LIST_3_BODY** — third list item's paragraph (HTML-bearing: supports `<mark>`/`<strong>`)
  - bbox: 59% 80.6% 33.2% 7.6% (box-grows)
  - style: 3.4cqw, weight 400, `var(--brand-secondary)`, line-height 1.4
  - sample: "The morning glass. The format is the argument, and nobody has led with it."
  - user_editable: true

- **FOOTER_NAME** — author identity (bottom-left)
  - bbox: 7.78% 93% 18% 2.4%
  - style: 2.0cqw, weight 700, ink
  - sample: "Farrice Cain"

- **FOOTER_URL** — publication link
  - bbox: 30% 93% 24% 2.4%, centered
  - style: 2.0cqw, weight 400, `var(--brand-secondary)`
  - sample: "parallaxletter.substack.com"

- **FOOTER_DESCRIPTOR** — category descriptor (matches the brand's masthead descriptor identity)
  - bbox: 56% 93% 20% 2.4%, right-aligned
  - style: 2.0cqw, weight 400, `var(--brand-secondary)`
  - sample: "Supplement + performance brands"

- **FOOTER_CTA** — the post's call-to-action (bottom-right)
  - bbox: 80.2% 93% 12% 2.4%, right-aligned
  - style: 2.0cqw, weight 700, ink
  - sample: "DM ANGLE"
  - user_editable: true

## Fixed elements (not slot-editable)

- The flat `var(--brand-bg-light)` canvas fill — CSS only, no texture, no AI generation.
- The evidence-crop's material treatment (paper field, hairline border on 3 sides, no radius, no shadow,
  bleed-left to the canvas edge) — the CONTAINER is fixed template geometry; only its image content is a slot.
- The masthead's and footer's 3(→4)-slot flex layout (`justify-content:space-between`) — structural, not content.
- The right column's flow-column grouping (headline → subhead → the 3-item list cluster in one flex column
  with `gap`) — this is deliberate: these five text blocks are all per-post-variable length, so they are
  authored as ONE flow container (not five independently absolute-positioned boxes) to guarantee no block
  ever overlaps the next one regardless of how long any single post's copy runs (`html-craft.md` §1/§3.7 rule 1).
- The static `→` arrow glyph next to `DATE_LABEL` — a typographic character, not an icon asset or a slot.
- No `[ai-image-zone]` block anywhere in this template — see rationale.md §③/§④.
