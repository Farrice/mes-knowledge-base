# Template: headline-marker-body

source_ref: ../../../visual_refs/ref-03-premium-minimal-carousel.png
canvas: 1080x1350 (4:5 LinkedIn carousel)
strategy: html-overlay (pure CSS, no AI generation)

## Rationale

see rationale.md — form: `solid-css` · edit_mode: `none`. Flat `#F3F3F0` field, zero texture, zero image; every
element (masthead, divider, headline, route/track marker diagram, footer caption) is authored HTML/CSS. The
full per-block treatment + the per-element ref-anchored reads live in `rationale.md` §2.

## Inventory

```yaml
bg_treatment:
  kind: solid-color
  has_baked_overlays: false
  needs_clean_ref: false

requires_photo_zone: false
zone_skip_reason: "ref has no photographic or illustrated content anywhere on the canvas — pixel-band analysis confirms a genuinely flat, zero-texture #F3F3F0 field; there is nothing to photo-zone"

elements:
  - name: masthead-left
    bbox: [7.78, 5.0, 40, 3]
    type: text
    content: "FARRICE CAIN"
    decision: slot
    notes: "ink, uppercase, tracked caption — brand identity label"

  - name: page-index
    bbox: [50, 5.0, 34.44, 3]
    type: text
    content: "03 / 04"
    decision: slot
    notes: "graphite, uppercase, tracked caption — carousel field index (matches tokens.json chrome.field_index)"

  - name: divider-hairline
    bbox: [7.78, 9.4, 84.44, 0.1]
    type: rule
    decision: fixed
    reason: "1px structural rule, matches rules.hairline_px:1 — not per-post content, chrome"

  - name: headline
    bbox: [7.78, 21.0, 92, 26]
    type: text
    content: "The format changed. The campaign argument did not."
    decision: slot
    notes: "bold display statement (natural wrap, no forced breaks — see ## Slots), ink, left-aligned — the dominant idea on the slide"

  - name: route-diagram
    bbox: [7.78, 60, 84.7, 13]
    type: vector+text
    decision: slot
    notes: "3-row route/track marker (01 / 02 LEAD / 03) — one bold ink row (the LEAD recommendation), two tonal graphite rows; matches tokens.json rules.maximum_dark_interruptions_per_sequence:1 and modes.offer.primary_content ('three campaign arguments, one lead recommendation')"

  - name: footer-caption
    bbox: [7.78, 88.7, 60, 2.5]
    type: text
    content: "A NEW HOOK IS NOT ALWAYS A NEW ANGLE"
    decision: slot
    notes: "graphite, uppercase, tracked caption — supporting insight line"

chrome_observed:
  masthead_visible_in_ref: true
  pagination_dots_visible_in_ref: false
  page_indicator_visible_in_ref: true
```

## Visual summary

A pure-typography carousel body slide on the brand's flat cream field — no photo, no texture, no AI generation
at all. A tracked masthead (brand identity + field index) sits above a hairline rule; a bold 3-line Helvetica
Neue statement carries the slide as its single dominant idea; a 3-row "route" diagram beneath it marks one of
three numbered options as the LEAD recommendation (thin graphite rows for the two not chosen, one thick ink
row + filled dot for the one that is); a small tracked caption anchors the bottom. Use for body/argument slides
in an editorial carousel sequence where a single statement needs a supporting "which option wins" marker.

## AI Image

generation_route: none — `solid-css` scenario, no `[ai-image-zone]` block. Background is `var(--brand-bg-light)`
CSS, confirmed against the ref by pixel-band analysis (zero non-text/non-line pixels outside the identified
content bands). No `ref_input`, no per-post image variables — nothing in this template is AI-generated.

## Slots

- **MASTHEAD_LEFT** — brand identity label
  - bbox: 7.78% 5.0% 40% 3%
  - style: caption (Helvetica Neue 700, 2.04cqw, uppercase, +0.16em tracking), ink, left-aligned
  - sample: "FARRICE CAIN"

- **MASTHEAD_CENTER** — reserved center masthead slot (empty on this ref; kept for pool masthead-pattern consistency)
  - bbox: center third of the masthead row
  - style: caption, same family, centered
  - sample: ""

- **PAGE_INDEX** — carousel field index / page counter
  - bbox: 50% 5.0% 34.44% 3% (right-aligned within)
  - style: caption, graphite, right-aligned, +0.16em tracking
  - sample: "03 / 04"
  - user_editable: true

- **HEADLINE** — main bold statement
  - bbox: 7.78% 21% 92% 26% (box-grows with content)
  - style: display (Helvetica Neue 700), 9.8cqw, line-height 1.0, letter-spacing -0.025em (from the shared
    `.display` class — matches brand `type_scale.display`, LOCKED letter-spacing field), ink, left-aligned;
    natural wrap (no manual `<br>` in the sample — the display scale needed to clear the 8cqw display-height
    floor wraps a full-sentence headline to more, shorter lines than the ref's exact 3-line break; supports
    `<br>` if a future value wants a deliberate break)
  - sample: "The format changed.<br>The campaign argument<br>did not."
  - user_editable: true
  - max_chars: ~70 (auto-shrinks toward the 8cqw floor if longer)

- **ROUTE_1_LABEL** — route row 1 label (not the lead)
  - bbox: within the route zone, row 1, right-aligned above its line
  - style: caption, graphite at 0.18 opacity (tonal), right-aligned
  - sample: "01"
  - user_editable: true

- **ROUTE_2_LABEL** — route row 2 label (the LEAD row)
  - bbox: within the route zone, row 2, right-aligned above its line
  - style: caption, ink, full opacity (solid — the one dark interruption), right-aligned
  - sample: "02 LEAD"
  - user_editable: true

- **ROUTE_3_LABEL** — route row 3 label (not the lead)
  - bbox: within the route zone, row 3, right-aligned above its line
  - style: caption, graphite at 0.18 opacity (tonal), right-aligned
  - sample: "03"
  - user_editable: true

- **FOOTER_CAPTION** — supporting insight line
  - bbox: 7.78% 88.7% 60% 2.5%
  - style: caption, graphite, left-aligned, +0.16em tracking
  - sample: "A NEW HOOK IS NOT ALWAYS A NEW ANGLE"
  - user_editable: true

## Fixed elements

- The divider hairline (1px, below the masthead) — chrome, matches `rules.hairline_px:1`, not slot-editable.
- The route diagram's STRUCTURE (3 rows, one bold ink row with a thick 6px line + filled dot, two tonal
  graphite rows with thin 1.5px lines + hollow dots) — the visual grammar is fixed template geometry (matches
  `rules.recommended_route_px:6`, `rules.quiet_route_px:[1,2]`, `rules.maximum_dark_interruptions_per_sequence:1`);
  only the row LABELS are slot-editable, not which row is bold (row 2 is fixed as the marked row, matching the ref).
  Fixed structure; only its labels are slots.
- Flat `var(--brand-bg-light)` background — not slot-editable, no AI generation.
- `data-surface="light"` on the slide root.

## Craft pass 2026-09-03 (Farrice)
Headline returned to the brand h1 (72px = 6.67cqw, the ref size), ref vertical rhythm restored, re-rendered via render_template.py (no AI). Sizes/bboxes above and in _measurements.yaml describe the ORIGINAL build. Headline values must carry explicit <br> line breaks: the renderer autosize shrinks any natural wrap. Decisions: ../REVIEW-NOTES.md
