# Template: word-photo-band-body

source_ref: ../../../visual_refs/editorial/02-opener-photo-band.png
canvas: 1080x1350 (4:5 LinkedIn carousel)
strategy: html-overlay
role: body
style_bucket: editorial (see ../styles.json)

## Rationale

see rationale.md — form: a-framed-image · edit_mode: none (all HTML/CSS; the photo zone holds a real,
non-generated evidence capture per moves.md move #8 "Evidence crop" — AI-generated imagery never fills it)

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
    bbox: [7.78, 38.52, 84.44, 44.44]
    source: user-uploaded-asset   # real screenshot/crop supplied per post — NEVER AI-generated (move #8)
    notes: "single contained rectangle holding a real captured screenshot (e.g. a Meta Ad Library crop
      showing one or more active-ad detail cards). Sample asset for this build is a real capture
      (assets/photo-sample-evidence.png), not synthesized."

elements:
  - name: header-title
    bbox: [7.78, 5.33, 40, 3]
    type: text
    content: "Creative Teardown"
    decision: slot
    notes: "series/document title, top-left of the header row; Helvetica Neue 700 26px"

  - name: header-date
    bbox: [55, 5.33, 37.22, 3]
    type: text
    content: "03 Sep, 2026 →"
    decision: slot
    notes: "date stamp + trailing unicode arrow glyph, right-aligned in the header row; not a brand icon
      asset — the arrow is plain text"

  - name: headline
    bbox: [7.78, 11.85, 84.44, 14]
    type: text
    content: "what they run"
    decision: slot
    notes: "the giant lowercase editorial display word/phrase — the slide's one dominant idea; Helvetica
      Neue 700, 144px (13.33cqw), letter-spacing -0.055em, line-height 0.92"

  - name: subtitle
    bbox: [7.78, 25.19, 70.37, 11]
    type: text
    content: "Eighty-seven percent of the active ads are dynamic variants of one modular frame. Ten percent are creator testimonials. Three percent are statics. Every one repeats the same claim in a new costume."
    decision: slot
    notes: "body-weight supporting paragraph in a narrower reading column (760px, not full safe-width)"

  - name: source-label
    bbox: [7.78, 84.89, 84.44, 2.5]
    type: text
    content: 'Source · Meta Ad Library, "AG1", active ads, 03 Sep 2026'
    decision: slot
    notes: "caption-scale citation line under the photo band; uppercase via CSS text-transform, +0.16em
      tracking, stone color (#8C8C82, tokens.json colors.text_muted — no CSS var emitted for this token
      yet, so hardcoded per-zone; see rationale.md §4)"

  - name: footer-strip
    bbox: [7.78, 93.48, 84.44, 3]
    type: text
    content: "Farrice Cain / parallaxletter.substack.com / Supplement + performance brands / DM ANGLE"
    decision: slot
    notes: "4-item flex row (space-between), this style's masthead-equivalent identity strip, relocated to
      the footer per the approved editorial grammar (rationale.md §4); ink color, 20px regular weight"

chrome_observed:
  masthead_visible_in_ref: false   # NOT the standard tokens.json chrome.masthead — see rationale.md §4
  pagination_dots_visible_in_ref: false
  page_indicator_visible_in_ref: false
```

## Visual summary

A single-image editorial "opener" body slide: a flat canvas-grey fill carries a document-style header (a
series title top-left, a date + arrow top-right), a giant lowercase Helvetica Neue headline, a narrower
supporting paragraph, one large real evidence photo band in a contained rectangle, a small tracked source
citation, and a four-item footer identity strip. No AI generation anywhere — the photo band is always a real
captured source (a screenshot, a product-page crop), never synthesized, per the brand's "Evidence crop" move.
Use this template to open a teardown/evidence carousel: one big claim in words, one real picture that proves it.

## AI Image

```
generation_route: none
ref_input: none
```

No `[ai-image-zone]` block. `edit_mode: none` per `rationale.md` §③ — this template performs no AI image
generation at all. The photo band is populated by a real, user-supplied capture (`PHOTO_MAIN_PATH`); the
canonical/sample value for this build (`assets/photo-sample-evidence.png`) is itself a real evidence capture
(a Meta Ad Library crop), copied from `brand_context/visual-identity/compositions/editorial/evidence/
ag1-adlibrary/crop-cards.png` — the same source asset the approved reference frame was built from.

## Slots

- **HEADER_TITLE** — series/document title (top-left of the header row)
  - bbox: 7.78% 5.33% 40% 3%
  - style: brand display face, 2.41cqw, weight 700, letter-spacing -0.01em, `var(--brand-text-on-light)`,
    left-align
  - sample: "Creative Teardown"

- **HEADER_DATE** — date stamp + arrow (top-right of the header row, HTML-bearing: carries the arrow glyph)
  - bbox: 55% 5.33% 37.22% 3%, right-aligned
  - style: brand display face, 2.04cqw, weight 400, `var(--brand-text-on-light)`, arrow glyph at 2.78cqw
  - sample: "03 Sep, 2026 <span class=\"arrow\">→</span>"

- **HEADLINE** — giant lowercase display word/phrase, the slide's one dominant idea
  - bbox: 7.78% 11.85% 84.44% 14%
  - style: brand display face, 13.33cqw, weight 700, line-height 0.92, letter-spacing -0.055em,
    `var(--brand-text-on-light)`, sentence/lowercase-as-written, left-align
  - sample: "what they run"
  - user_editable: true

- **SUBTITLE** — supporting paragraph (HTML-bearing: supports `<mark>`/`<em>`/`<strong>`)
  - bbox: 7.78% 25.19% 70.37% 11%
  - style: brand body face, 2.41cqw, weight 400, line-height 1.34, `var(--brand-text-on-light)`, left-align
  - sample: "Eighty-seven percent of the active ads are dynamic variants of one modular frame. Ten percent are creator testimonials. Three percent are statics. Every one repeats the same claim in a new costume."

- **PHOTO_MAIN_PATH** — the real evidence capture (screenshot / product-page crop / photo)
  - bbox: 7.78% 38.52% 84.44% 44.44%
  - style: `object-fit: cover`, `object-position: 0 0` (top-left anchored, matches the approved ref frame),
    no border-radius, no shadow — a hard flat edge on the canvas fill
  - sample: `assets/photo-sample-evidence.png` (real capture, not AI-generated)
  - user_editable: true

- **SOURCE_LABEL** — caption-scale citation line (HTML-bearing: supports `<mark>`/`<em>`/`<strong>`)
  - bbox: 7.78% 84.89% 84.44% 2.5%
  - style: caption token, 1.85cqw, uppercase (CSS `text-transform`), +0.16em tracking, weight 700,
    `#8C8C82` (tokens.json `colors.text_muted` / `named.stone` — no CSS var emitted yet, see rationale.md §4)
  - sample: 'Source · Meta Ad Library, "AG1", active ads, 03 Sep 2026'

- **FOOTER_NAME** — footer item 1 (fixed brand identity)
  - bbox: within `footer-strip` flex row, left item
  - style: brand display face, 1.85cqw, weight 400, `var(--brand-text-on-light)`
  - sample: "Farrice Cain"

- **FOOTER_SITE** — footer item 2
  - style: brand display face, 1.85cqw, weight 400, `var(--brand-text-on-light)`
  - sample: "parallaxletter.substack.com"

- **FOOTER_DESC** — footer item 3
  - style: brand display face, 1.85cqw, weight 400, `var(--brand-text-on-light)`
  - sample: "Supplement + performance brands"

- **FOOTER_CTA** — footer item 4 (right-aligned)
  - style: brand display face, 1.85cqw, weight 700, `var(--brand-text-on-light)`
  - sample: "DM ANGLE"

## Fixed elements (not slot-editable)

- The `#F3F3F0` canvas fill — CSS `background: var(--brand-bg-light);`, never a slot.
- The header row's flex layout (title left, date+arrow right, `justify-content:space-between`) — fixed
  structure; only the two text VALUES are editable.
- The footer row's 4-item flex layout (`justify-content:space-between`) — fixed structure; the four text
  VALUES are technically slots (for maintainability, matching the pool's `MASTHEAD_LEFT`/`FIELD_INDEX`
  precedent in `kicker-stack-body`) but this identity strip is not meant to vary post-to-post in normal use.
- The photo zone's flat-edge, no-radius, no-shadow framing — fixed CSS treatment (`overflow:hidden`,
  `object-fit:cover`), never a per-post style choice.

## Strategy notes

- All zones are html-overlay. No ai-edit needed — `edit_mode: none`.
- No standard `chrome.masthead`/`chrome.pagination` injection — this style's own header/footer chrome replaces
  it for the `editorial` bucket (see `rationale.md` §4 + `../styles.json`).
- Bg is solid `var(--brand-bg-light)` via CSS — no `_ai_bg/bg.png` file for this template.
- The photo zone binds `{{PHOTO_MAIN_PATH}}` (never a hardcoded `_ai_bg/…` or `assets/…` literal path) so a
  real per-post capture always overrides the demo sample at render time.

## Possible future variations

- Allow the photo band to hold 2+ separate contained rectangles (side-by-side) instead of a single wide crop,
  for posts where the per-post evidence is naturally two distinct screenshots rather than one pre-composed crop.
- Allow `SOURCE_LABEL` to omit the trailing date when the citation doesn't need one.
