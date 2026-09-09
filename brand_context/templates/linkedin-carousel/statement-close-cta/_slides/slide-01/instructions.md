# Template: statement-close-cta

source_ref: ../../../visual_refs/ref-04-premium-minimal-carousel.png
canvas: 1080x1350 (4:5 LinkedIn carousel)
strategy: html-overlay

## Rationale

See `rationale.md` for the full reasoning.

form: solid-css
edit_mode: none — pure CSS/HTML, no AI generation.

## Inventory

```yaml
bg_treatment:
  kind: solid-color
  has_baked_overlays: false
  needs_clean_ref: false

requires_photo_zone: false
zone_skip_reason: "no photo, silhouette, cutout, or scene content anywhere in the ref — the entire slide is flat CSS/typography on a solid ink fill (form = solid-css, tree Q1 = yes)"

elements:
  - name: masthead-left
    bbox: [8, 5, 45, 3]
    type: text
    content: "THE ANGLE MAP"
    decision: slot
    notes: "brand offer-mode masthead label, tokens.json chrome.masthead.offer_mode_labels[0]; caption token, stone, +0.16em tracking"

  - name: field-index
    bbox: [70, 5, 22, 3]
    type: text
    content: "04 / 04"
    decision: slot
    notes: "brand move #2 field index, current/total form; caption token, stone"

  - name: decision-line
    bbox: [8, 10, 84, 0.5]
    type: rule
    decision: fixed
    reason: "brand move #3 decision line — a structural hairline, not per-post content"

  - name: closing-headline
    bbox: [8, 25, 84, 30]
    type: text
    content: "Choose the argument before you multiply it."
    decision: slot
    notes: "display token, sentence case, paper on ink, 3 explicit line breaks — the primary per-post variation axis"

  - name: three-route-grammar
    bbox: [8, 61, 84, 12]
    type: graphic
    decision: slot
    notes: "brand move #4 — 3 rows (label + line + end-dot); the recommended row's label + weight are editable slots, the quiet rows are fixed structural chrome"

  - name: footer-caption
    bbox: [8, 85, 84, 3]
    type: text
    content: "THREE CAMPAIGN ANGLES · ONE LEAD RECOMMENDATION"
    decision: slot
    notes: "caption token, stone/graphite, functional label above the recommendation name"

  - name: recommendation-name
    bbox: [8, 89, 60, 5]
    type: text
    content: "DM ANGLE"
    decision: slot
    notes: "bold second-tier statement, paper on ink — the resolved recommendation name, second per-post variation axis"

chrome_observed:
  masthead_visible_in_ref: true
  pagination_dots_visible_in_ref: false
  page_indicator_visible_in_ref: true
```

## Visual summary

A pure-typographic closing/CTA frame on the brand's single "dark recommendation" surface: an
edge-to-edge ink (#101010) fill carrying a small offer-mode masthead + field index up top, a large
3-line display headline delivering the closing insight, the brand's three-route-grammar device
showing which of three campaign angles is the recommendation, and a footer pair (functional caption +
bold recommendation name) at the base. Use it as the final slide of an "Angle Map" — or any
route-comparison — carousel, where the whole point of the frame is to land the one decision.

## AI Image

generation_route: none
ref_input: n/a — no `[ai-image-zone]` block; the entire slide is CSS/HTML per `scenarios/solid-css.md`.

## Slots

- **MASTHEAD_LEFT** — brand offer-mode masthead label
  - bbox: 8% 5% 45% 3%
  - style: caption token, Helvetica Neue 700, +0.16em tracking, uppercase, stone/graphite on ink
  - sample: "THE ANGLE MAP"
  - user_editable: false (brand chrome — `tokens.json` `locked_fields` includes `chrome.masthead`)

- **PAGE_INDEX** — field index (current / total position in the sequence)
  - bbox: 70% 5% 22% 3%
  - style: caption token, stone, right-aligned
  - sample: "04 / 04"
  - user_editable: true

- **HEADLINE** — the closing statement / insight
  - bbox: 8% 25% 84% 30%
  - style: display token (104px @ reference canvas, line-height 1.0, letter-spacing -0.025em), sentence
    case, Helvetica Neue 700, paper (#FAFAF8) on ink, left-aligned; supports `<br>` for deliberate line
    breaks and `<mark>` for a single emphasis word
  - sample: "Choose the argument<br>before you<br>multiply it."
  - user_editable: true

- **ROUTE_01_LABEL** — quiet route, index only
  - bbox: within the three-route-grammar zone, row 1
  - style: caption token, stone
  - sample: "01"
  - user_editable: false

- **ROUTE_02_LABEL** — recommended route label
  - bbox: within the three-route-grammar zone, row 2
  - style: caption token, bold, paper, +0.16em tracking
  - sample: "02 LEAD"
  - user_editable: true

- **ROUTE_03_LABEL** — quiet route, index only
  - bbox: within the three-route-grammar zone, row 3
  - style: caption token, stone
  - sample: "03"
  - user_editable: false

- **FOOTER_CAPTION** — functional label above the recommendation name
  - bbox: 8% 85% 84% 3%
  - style: caption token, stone/graphite, uppercase, +0.16em tracking
  - sample: "THREE CAMPAIGN ANGLES · ONE LEAD RECOMMENDATION"
  - user_editable: true

- **RECOMMENDATION_NAME** — the resolved recommendation, spelled out
  - bbox: 8% 89% 60% 5%
  - style: bold, Helvetica Neue 700, paper on ink, sentence/caps per ref
  - sample: "DM ANGLE"
  - user_editable: true

## Strategy notes

- All zones are html-overlay. No ai-edit needed — `strategy: html-overlay`, `edit_mode: none`.
- Chrome injected: masthead (left + field-index right; no center slot used, matching this ref) + the
  decision-line hairline. No dot pagination (`tokens.json` `chrome.pagination: null`) — the field index
  IS the pagination for this brand.
- Background is solid ink via CSS — no `_ai_bg/bg.png` file, no image zone at all.
- The three-route-grammar block is authored as 3 flex rows (line + end-marker + label), NOT as three
  separate absolutely-positioned line elements guessed by eye — see `template.html` for the shared row
  markup.

## Fixed elements (not slot-editable)

- The ink (#101010) full-canvas fill — `tokens.json colors.bg_dark`, this brand's single "dark
  recommendation" move; never recolored per post.
- The decision-line hairline under the masthead.
- The two quiet-route rows' line weight (1px), color (`--brand-border-subtle`/line), and hollow
  end-circle style — only the recommended row's weight/fill/label vary.
- `MASTHEAD_LEFT` — brand offer-mode identity label (locked by `tokens.json`).

## Possible future variations

- Allow the quiet-route index labels ("01"/"03") to be renamed if a future carousel numbers its angles
  differently (e.g. lettered A/B/C).
- Allow the recommended-route row's ordinal position (top/middle/bottom of the 3) to vary if the lead
  angle isn't always the middle option.
