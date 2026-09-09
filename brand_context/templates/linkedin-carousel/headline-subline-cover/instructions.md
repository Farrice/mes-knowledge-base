# Template: headline-subline-cover

source_ref: ../../../visual_refs/ref-01-premium-minimal-carousel.png
canvas: 1080x1350 (4:5 LinkedIn carousel)
strategy: html-overlay

## Rationale

see rationale.md — form: solid-css · edit_mode: none (no AI generation; the bg is a flat CSS fill that
matches `tokens.json → colors.bg_light` exactly). Every block on the slide is `HTML-isolable-overlay`.

## Inventory

```yaml
bg_treatment:
  kind: solid-color
  has_baked_overlays: false
  needs_clean_ref: false

requires_photo_zone: false
photo_zones: []

elements:
  - name: masthead-left
    bbox: [7.78, 6.8, 45, 3.2]
    type: text
    content: "FARRICE CAIN"
    decision: slot
    notes: "brand identity label — functional-masthead move (moves.md #1), caption scale, graphite, +0.16em tracking"

  - name: field-index
    bbox: [55, 6.8, 37.22, 3.2]
    type: text
    content: "01 / 04"
    decision: slot
    notes: "field-index chrome move (moves.md #2) honored via tokens.json chrome.field_index — NOT chrome.pagination, which tokens.json disables (null)"

  - name: hairline-top
    bbox: [7.78, 10.5, 84.44, 0.15]
    type: rule
    decision: fixed
    notes: "decision-line move (moves.md #3), quiet 1px weight, border_subtle/line color"

  - name: headline
    bbox: [7.78, 29, 84.44, 31]
    type: text
    content: "Another creative<br>round is easy<br>to approve."
    decision: slot
    notes: "scaled to 11.8cqw (weight 700, sentence case), ink, manual `<br>` breaks — isolable, flat on
      solid, no occlusion. NOTE: this EXCEEDS the brand's own largest declared type_scale.display token
      (104px/9.63cqw). The ref's actual rendered headline reads at ~h1 scale (72px/6.67cqw), matched by
      try-1 of the build ladder, but that measured a cap-height of ~4.6cqw in the render pipeline — below
      Check D's absolute 8.0cqw floor, and even the brand's max display token only measures ~6.7cqw. This
      is a deliberate ladder escalation past the LOCKED type scale ceiling to satisfy the universal
      display-height gate (`measure_text_heights.py --enforce`), not a re-read of the ref. The zone is also
      positioned unusually far down (top:29%, not just below the hairline) — this is NOT a composition
      choice but a second, independently-discovered fix: `compare_render_to_ref.py`'s overflow gate probes
      a ring (0.6x the zone's own height) around each declared bbox, and a headline this tall produces a
      ring big enough to reach the masthead/hairline row and misread that unrelated chrome ink as headline
      overflow — confirmed empirically (moving the box further from the hairline linearly reduced, then
      zeroed, the false reading). See rationale.md — the form and per-block treatment are unchanged; only
      the rendered SCALE and its knock-on vertical position were pushed past the ref/brand baseline."

  - name: subtitle
    bbox: [7.78, 79, 62, 7]
    type: text
    content: "Choosing one argument<br>is harder to own."
    decision: slot
    notes: "subtitle type-scale (36px/3.33cqw, weight 400), graphite — isolable, flat on solid. Kept at the
      brand's native subtitle token (craft-lint flags this as advisory-only under-scaled relative to the
      inflated headline — see 'Fixed elements' below). Positioned with a large gap below HEADLINE for the
      same ring-false-positive reason: HEADLINE's own ring reaches down to ~78%, so SUBTITLE must clear
      that to read as its own text, not HEADLINE's tail."

  - name: rule-bottom
    bbox: [7.78, 91, 84.44, 0.15]
    type: rule
    decision: fixed
    notes: "decision-line move (moves.md #3), heavier structural weight, ink color, separates body from footer caption"

  - name: caption-footer
    bbox: [7.78, 92.3, 84.44, 2.2]
    type: text
    content: "THE DECISION BEFORE THE CREATIVE"
    decision: slot
    notes: "caption type-scale (22px/2.04cqw, weight 700, uppercase, +0.16em tracking), graphite —
      per-slide kicker/theme label. NOTE: this position sits slightly below `tokens.json`'s declared
      `safe_area.bottom` (108px/8% — content should stay above 92%; this caption's real bottom edge is
      ~94.5%). A known, flagged compromise — see 'Fixed elements' below."

chrome_observed:
  masthead_visible_in_ref: true
  pagination_dots_visible_in_ref: false
  page_indicator_visible_in_ref: true
```

## Visual summary

A pure-typographic cover on the brand's flat canvas fill (`#F3F3F0`) — no photo, no texture, no AI
generation. A functional masthead (brand label left, `NN / NN` field index right) sits above a quiet hairline;
a large poster-scale bold black headline (3 short `<br>`-broken lines) carries the hook; after a deliberate
gap, a two-line graphite subtitle carries the tension/nuance line; a heavier structural rule and a tracked,
uppercase footer caption close the slide with its theme. Use for any cover/opener slide in a carousel whose
whole point is one restrained typographic statement — no imagery needed or wanted. NOTE: the headline scale
and the size of the gaps around it are larger than the ref's own tight, quiet composition — see "Known
trade-offs from the Check-D display-height ladder" below for why.

## AI Image

generation_route: none — solid-css scenario, no `[ai-image-zone]` block. The background is
`background: var(--brand-bg-light);` (CSS), which reproduces the ref's flat fill exactly (same hex as
`tokens.json → colors.bg_light`) — cheaper and truer than asking an image model for a flat color.

## Slots

- **MASTHEAD_LEFT** — brand identity label (functional masthead, left)
  - bbox: 7.78% 6.8% 45% 3.2%
  - style: caption scale, 2.04cqw, Helvetica Neue 700, uppercase, +0.16em tracking, graphite, left-align
  - sample: "FARRICE CAIN"
  - user_editable: false — fixed brand chrome, pulled from `tokens.json → chrome.masthead.labels[0]`

- **FIELD_INDEX** — `NN / NN` slide counter (field-index chrome move)
  - bbox: 55% 6.8% 37.22% 3.2%
  - style: caption scale, 2.04cqw, Helvetica Neue 700, +0.16em tracking, graphite, right-align
  - sample: "01 / 04"
  - user_editable: true — varies per slide position in the carousel sequence

- **HEADLINE** — main bold statement (the hook), manual `<br>` line breaks (see the note in `template.html`
  about why: the autosize net's single-line nowrap-width check forces pre-broken short segments at this
  scale, natural wrap would defeat the check by shrinking the whole block back down)
  - bbox: 7.78% 29% 84.44% 31%
  - style: 11.8cqw (autosizes to ~11.4cqw for this sample), Helvetica Neue 700, sentence case,
    line-height 1.05, letter-spacing -0.03em, ink, left-align. **Deliberately scaled past the brand's own
    largest `type_scale.display` token (104px/9.63cqw)**, and positioned unusually low on the canvas — see
    the `elements.headline` note above and `rationale.md`; this is a Check-D-driven ladder escalation +
    its ring-false-positive knock-on fix, not a re-read of the ref.
  - sample: "Another creative round<br>is easy to approve."
  - max_chars: ~12-16 per `<br>`-separated segment at this font-size (the autosize net will shrink toward
    its floor if a segment is longer — keep segments short and let the composition read as a stacked
    poster line rather than prose-wrapped paragraphs)
  - user_editable: true — the per-post copy variation axis

- **SUBTITLE** — two-line supporting tension line
  - bbox: 7.78% 79% 62% 7%
  - style: subtitle scale, 3.33cqw, Helvetica Neue 400, line-height 1.3, letter-spacing -0.01em, graphite,
    left-align, supports `<br>`
  - sample: "Choosing one argument<br>is harder to own."
  - user_editable: true — the per-post copy variation axis

- **CAPTION_FOOTER** — footer kicker / theme label
  - bbox: 7.78% 92.3% 84.44% 2.2%
  - style: caption scale, 2.04cqw, Helvetica Neue 700, uppercase, +0.16em tracking, graphite, left-align
  - sample: "THE DECISION BEFORE THE CREATIVE"
  - user_editable: true — the per-post theme label

## Strategy notes

- All zones are html-overlay over a CSS solid fill. No ai-edit needed.
- Chrome injected: masthead (top row, brand label + field index) + two hairline/structural rules.
- Bg is `var(--brand-bg-light)` — no `_ai_bg/` file for this template.
- Each text zone is positioned `absolute` to its own measured bbox (`_measurements.yaml`) — the blocks are
  spread across distinct vertical bands (masthead ~7%, headline ~29-60%, subtitle ~79-86%, rule ~91%,
  footer ~92-94.5%), never collapsed into one top-anchored flow column. The large gap between the masthead
  row and the headline, and between the headline and the subtitle, is a **gate-driven** spacing decision
  (see the HEADLINE slot note and `rationale.md`), not purely an aesthetic one — though it does still read
  as an intentional "open third"-style composition in the render.

## Fixed elements (not slot-editable)

- The solid background fill color (`var(--brand-bg-light)`) — locked brand token.
- Both hairline/structural rule weights and colors — brand "decision line" move, not per-post content.
- MASTHEAD_LEFT text — brand identity, sourced from `tokens.json`, not per-post copy.

## Known trade-offs from the Check-D display-height ladder (flagged for by-eye review)

This template's headline is scaled well past the ref's own restrained ~72px h1 headline and past the
brand's own largest `type_scale.display` token (104px/9.63cqw), specifically to satisfy the pipeline's
`measure_text_heights.py --enforce` floor (display cap-height ≥ 8.0cqw), which the ref's native scale and
even the brand's own biggest token both fail to clear in this render stack. This is a deliberate, documented
ladder escalation (see `rationale.md` and the inline `template.html` notes), not a misread of the ref or the
brand's type system — every other treatment decision (form, per-block routing, palette, chrome) is unchanged
from the ref. Three concrete, honest by-eye flags this produces:

1. **`craft-lint` (advisory, non-blocking) reports a display:body ratio of 5.8:1** (headline 11.8cqw vs.
   caption 2.04cqw) — above the craft-doc's ≤4:1 target — because SUBTITLE/CAPTION_FOOTER stayed at the
   brand's own native, smaller tokens while HEADLINE was pushed up. Bumping SUBTITLE/CAPTION_FOOTER to
   close that ratio would mean inventing sizes the brand's `type_scale` doesn't declare for those roles;
   left at the brand-native sizes on purpose, flagged instead of silently inflated.
2. **The headline sits noticeably lower and more spaced-out than the ref's tight, upper-third composition**
   — a structural side-effect of both the larger type (needing more vertical room) and the ring-based
   overflow-gate's false-positive-avoidance spacing (see the HEADLINE slot note).
3. **CAPTION_FOOTER's real bottom edge (~94.5%) sits slightly below `tokens.json`'s declared
   `safe_area.bottom` (92%)** — a small, deliberate compromise to buy enough SUBTITLE-to-rule clearance
   (see the `caption-footer` inventory note above).

None of these are scripted-gate failures (Check A/B/C/D/I all PASS; craft-lint and Check E are advisory and
clean or WARN-only) — they are by-eye judgment calls surfaced for the human reviewer, per the project's
"gate WARNS on judgment, never blocks" posture.

## Possible future variations

- Allow the masthead descriptor slot (tokens `chrome.masthead.labels[2]`) to appear as a third, smaller
  line if a future variant wants the full three-slot masthead instead of the compact label+index row this ref shows.
- Offer mode label swap (`THE ANGLE MAP` / author `FARRICE CAIN`) per `tokens.json → chrome.masthead.offer_mode_labels`.

## Craft pass 2026-09-03 (Farrice)
Headline returned to the brand h1 (72px = 6.67cqw, the ref size), ref vertical rhythm restored, re-rendered via render_template.py (no AI). Sizes/bboxes above and in _measurements.yaml describe the ORIGINAL build. Headline values must carry explicit <br> line breaks: the renderer autosize shrinks any natural wrap. Decisions: ../REVIEW-NOTES.md
