# Template: evidence-crop-body

source_ref: ../../../visual_refs/editorial/06-evidence-crop.png
canvas: 1080x1350 (4:5 LinkedIn carousel)
strategy: html-overlay
role: body

## Rationale

see rationale.md — form: a-framed-image · edit_mode: none (the evidence crop is a REAL per-post source
capture, never AI-generated — `moves.md` #8 hard rule)

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
    bbox: [7.8, 11.19, 84.4, 41.48]
    source: user-uploaded-asset
    notes: "the evidence crop — a real captured source (ad screenshot, label panel, product page, review,
      study excerpt). moves.md #8: 'AI-generated imagery is not evidence and never fills this zone.' Sample
      for the canonical preview is the REAL Huel Daily Greens product-page capture this ref frame itself
      uses (compositions/editorial/evidence/huel-greens/crop-claim.png, a genuine Playwright capture — see
      that folder's manifest.json), copied to assets/evidence-sample.png."

elements:
  - name: masthead-series-title
    bbox: [7.8, 5.3, 40, 3]
    type: text
    content: "Creative Teardown"
    decision: slot
    notes: "editorial-style series header (left), ../REVIEW-NOTES.md aesthetic pivot; ink, bold, tight tracking"

  - name: masthead-date-arrow
    bbox: [50, 5.3, 34.4, 3]
    type: text
    content: "03 Sep, 2026 ->"
    decision: slot
    notes: "post date + directional arrow glyph (right); ink, regular weight; per-post variable"

  - name: hairline-rule-1
    bbox: [7.8, 11.1, 84.4, 0.1]
    type: rule
    content: null
    decision: skip
    reason: "structural decision-line move (moves.md #3), a 1px CSS border, not slot-editable content"

  - name: evidence-crop-image
    bbox: [7.8, 11.19, 84.4, 41.48]
    type: photo
    content: "<real source capture, per post>"
    decision: slot
    notes: "contained rectangle on paper, object-fit:contain (never crops the source), no radius, no shadow
      (tokens.json prohibits both); moves.md #8 Evidence crop move"

  - name: hairline-rule-2
    bbox: [7.8, 52.67, 84.4, 0.1]
    type: rule
    content: null
    decision: skip
    reason: "structural decision-line move (moves.md #3), a 1px CSS border, not slot-editable content"

  - name: evidence-label
    bbox: [7.8, 53.9, 84.4, 3]
    type: text
    content: "Evidence · huel.com, Daily Greens product page, 03 Sep 2026"
    decision: slot
    notes: "moves.md #8's required source-label annotation; caption token, graphite, uppercase via CSS
      text-transform"

  - name: verdict-headline
    bbox: [7.8, 60.74, 44.4, 16]
    type: text
    content: "the miss"
    decision: slot
    notes: "the dominant idea; large lowercase display word, brand's only display face, full ink, not
      occluded by anything — stays prominent HTML per identification-tree.md rule 6"

  - name: analysis-body
    bbox: [7.8, 71.11, 70.4, 15]
    type: text
    content: "A ten-year claim about ingredient count, when the buyer's fear is whether they will still be drinking it in March. The adjective got funded. The argument did not."
    decision: slot
    notes: "the analysis paragraph; regular weight, ink, brand body token"

  - name: footer-strip
    bbox: [7.8, 93, 84.4, 3]
    type: text
    content: "Farrice Cain | parallaxletter.substack.com | Supplement + performance brands | DM ANGLE"
    decision: slot
    notes: "4-slot identity/CTA strip, tokens.json modes.master_brand.offer_reference (restrained footer,
      final frame only); ink, regular weight, evenly spaced"

chrome_observed:
  masthead_visible_in_ref: true
  pagination_dots_visible_in_ref: false
  page_indicator_visible_in_ref: false
```

## Visual summary

A body slide for the "Creative Teardown" editorial series: a real evidence capture (a competitor's ad, product
page, review, or study excerpt) sits contained on brand paper between two hairline rules, labeled with its
source — then a large lowercase verdict word ("the miss") and a short analysis paragraph make the argument
underneath, closed by a 4-item identity/CTA footer strip. The evidence crop is NEVER AI-generated (brand hard
rule, `moves.md` #8) — it is a real per-post upload. Use this template for any teardown post that critiques a
specific piece of real marketing copy against a real screenshot of it.

## AI Image

```
generation_route: none
ref_input: assets/ref-canonical.png
```

No `[ai-image-zone]` block — `edit_mode: none` per `rationale.md` §③ (a hard brand rule, not a cost/judgment
call: `moves.md` #8 "AI-generated imagery is not evidence and never fills this zone"). `PHOTO_MAIN_PATH` is a
plain `<img>` slot bound to a real, per-post user-supplied capture (`source: user-uploaded-asset`). The
canonical-preview sample value is a REAL capture (`assets/evidence-sample.png`, copied from the brand's own
Huel Daily Greens Playwright screenshot — see `## Inventory > photo_zones` above), not a synthetic mockup.

## Slots

- **SERIES_TITLE** — the content series name (masthead, left)
  - bbox: 7.8% 5.3% 40% 3%
  - style: display face, 2.41cqw, weight 700, −0.01em tracking, `var(--brand-text-on-light)` (ink)
  - sample: "Creative Teardown"

- **POST_DATE** — the post's publish date (masthead, right, before the arrow glyph)
  - bbox: 50% 5.3% 34.4% 3%, right-aligned
  - style: display face, 2.04cqw, weight 400, `var(--brand-text-on-light)` (ink)
  - sample: "03 Sep, 2026"
  - user_editable: true

- **PHOTO_MAIN** (renders via `PHOTO_MAIN_PATH`) — the real evidence crop
  - bbox: 7.8% 11.19% 84.4% 41.48%
  - style: contained rectangle on paper (`var(--brand-text-on-dark, #FAFAF8)`), `object-fit:contain`, no
    radius, no shadow
  - sample: `assets/evidence-sample.png` (real Huel Daily Greens product-page capture)
  - user_editable: true

- **EVIDENCE_LABEL** — the source/caption line under the crop
  - bbox: 7.8% 53.9% 84.4% 3%
  - style: caption token, 1.85cqw, uppercase (CSS `text-transform`), +0.16em tracking, weight 700,
    `var(--brand-secondary)` (graphite)
  - sample: "Evidence · huel.com, Daily Greens product page, 03 Sep 2026"
  - user_editable: true

- **VERDICT_WORD** — the dominant lowercase display headline (HTML-bearing: supports `<br>`)
  - bbox: 7.8% 60.74% 44.4% 16%
  - style: brand display face, 10.37cqw, weight 700, line-height 0.92, letter-spacing −0.05em,
    `var(--brand-text-on-light)` (ink), lowercase, left-align
  - sample: "the miss"
  - user_editable: true

- **ANALYSIS_BODY** — the argument paragraph (HTML-bearing: supports `<mark>`/`<em>`/`<strong>`)
  - bbox: 7.8% 71.11% 70.4% 15%
  - style: body token, 2.41cqw, weight 400, line-height 1.34, `var(--brand-text-on-light)` (ink), left-align
  - sample: "A ten-year claim about ingredient count, when the buyer's fear is whether they will still be drinking it in March. The adjective got funded. The argument did not."
  - user_editable: true

- **FOOTER_NAME** — author identity (footer, item 1)
  - bbox: within the footer strip (7.8% 93% 84.4% 3%)
  - style: display face, 1.85cqw, weight 400, `var(--brand-text-on-light)` (ink)
  - sample: "Farrice Cain"

- **FOOTER_HANDLE** — the newsletter/handle (footer, item 2)
  - style: same as FOOTER_NAME
  - sample: "parallaxletter.substack.com"

- **FOOTER_NICHE** — the niche descriptor (footer, item 3)
  - style: same as FOOTER_NAME
  - sample: "Supplement + performance brands"

- **FOOTER_CTA** — the closing call-to-action (footer, item 4)
  - style: same as FOOTER_NAME
  - sample: "DM ANGLE"
  - user_editable: true

## Fixed elements (not slot-editable)

- The `#F3F3F0` canvas fill — CSS `background: var(--brand-bg-light);`, never a slot.
- The two hairline rules (moves.md decision-line move) — CSS `border-top`, structural, not content.
- The masthead's 2-slot flex layout and the footer's 4-slot flex layout — the layout pattern is fixed; only
  the slot VALUES are editable.
- `FOOTER_NAME` / `FOOTER_HANDLE` / `FOOTER_NICHE` are slotted for maintainability but are brand-identity
  constants (author name, handle, niche) — not expected to vary per post, unlike `FOOTER_CTA`.

## Strategy notes

- All text zones are html-overlay. `PHOTO_MAIN` is a plain HTML `<img>` slot, never AI-generated —
  `edit_mode: none`.
- Chrome injected: editorial masthead (2-slot, series title left + date/arrow right) and footer (4-slot
  identity/CTA strip) — both per this ref's own evidence and Farrice's explicit approval of the editorial
  style pivot (`../REVIEW-NOTES.md`). No pagination dots (`tokens.json → chrome.pagination: null`) and no
  field index (this ref doesn't carry one).
- Bg is solid `var(--brand-bg-light)` via CSS — no `_ai_bg/bg.png` file for this template.

## Possible future variations

- Allow `EVIDENCE_LABEL` to carry a structured multi-part format (source · page · date) as separate spans if a
  future post needs to re-order them.
- Allow `VERDICT_WORD` to run 2 short words instead of 1 (the slot already supports `<br>`; the auto-shrink fit
  mechanic handles the extra line within the 16%-height zone).
