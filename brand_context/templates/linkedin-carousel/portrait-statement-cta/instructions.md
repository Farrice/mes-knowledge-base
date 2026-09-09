# Template: portrait-statement-cta

source_ref: ../../../visual_refs/editorial/07-portrait-close.png
canvas: 1080x1350 (4:5 LinkedIn carousel)
strategy: html-overlay (photo is a real static asset, no AI generation anywhere in this template)

## Rationale

See `rationale.md` for the full reasoning.

form: a-framed-image
edit_mode: none — the photo is Farrice's own real, unaltered studio portrait, placed verbatim (crop +
uniform scale only, CSS `object-fit`/`object-position`, zero pixel regeneration). `tokens.json >
portrait_policy` hard-prohibits AI touch on this class of asset (face regeneration, replacement,
inpainting, beauty filtering, AI upscaling, synthetic portraits). All text is HTML-overlay on the flat
canvas-grey background.

## Inventory

```yaml
bg_treatment:
  kind: solid-color
  has_baked_overlays: false
  needs_clean_ref: false

requires_photo_zone: true
photo_zones:
  - kind: embedded-photo
    bbox: [7.78, 11.11, 84.44, 41.48]
    source: user-uploaded-asset
    notes: "real, unaltered studio portrait of Farrice Cain (brand founder); NEVER AI-generated or
      re-rendered — tokens.json portrait_policy + brand move #9 'Original portrait' hard-prohibit
      synthetic/regenerated portraits. Contained rectangle, object-fit:cover, object-position:50% 30%,
      no radius, no shadow."

elements:
  - name: kicker
    bbox: [7.78, 5.33, 45, 3]
    type: text
    content: "Creative Teardown"
    decision: slot
    notes: "per-post category/series label — this ref's 'editorial' style header grammar (REVIEW-NOTES
      2026-09-03 pivot), distinct from the pool's typographic-style chrome.masthead; content varies by
      post, not brand-locked chrome"

  - name: date
    bbox: [60, 5.33, 32.22, 3]
    type: text
    content: "03 Sep, 2026"
    decision: slot
    notes: "post date, right-aligned, followed by a fixed decorative arrow glyph (→, static markup, not
      a slot)"

  - name: photo-main
    bbox: [7.78, 11.11, 84.44, 41.48]
    type: image
    content: "Farrice Cain, real studio portrait"
    decision: slot
    notes: "see photo_zones above; edit_mode none, real asset only"

  - name: headline
    bbox: [7.78, 57.04, 84.44, 15]
    type: text
    content: "choose the argument<br>before you multiply it."
    decision: slot
    notes: "giant lowercase display statement — the primary per-post variation axis (the post's core
      insight/argument); 92px/8.52cqw, letter-spacing -0.055em, line-height 0.94, matches the ref exactly"

  - name: subtitle
    bbox: [7.78, 74.81, 55.56, 7]
    type: text
    content: "Three campaign angles, one lead recommendation, before the next creative round. That is
      the whole job."
    decision: slot
    notes: "graphite body copy, left-aligned, two lines"

  - name: cta-mid
    bbox: [68, 74.96, 24.22, 3]
    type: text
    content: "DM ANGLE"
    decision: slot
    notes: "right-aligned bold tracked action label, ink, followed by a fixed decorative arrow glyph"

  - name: footer-strip
    bbox: [7.78, 93.0, 84.44, 3]
    type: text
    content: "Farrice Cain · parallaxletter.substack.com · Supplement + performance brands · DM ANGLE"
    decision: slot
    notes: "4-item flex row, evenly spaced. First two items (name, domain) are fixed brand identity;
      last two (descriptor, CTA repeat) are per-post editable"

chrome_observed:
  masthead_visible_in_ref: false
  pagination_dots_visible_in_ref: false
  page_indicator_visible_in_ref: false
```

## Visual summary

An editorial-style closing/CTA card: Farrice's real contained studio portrait up top (a fixed, never
AI-touched identity photo), a giant lowercase two-line bold statement below it delivering the post's
core argument, a graphite subtitle paired with a right-aligned tracked "DM ANGLE →" call-to-action on
the same row, a large open breathing band, and a four-item functional footer strip (author · domain ·
positioning · CTA repeat) anchoring the bottom edge. Use it as the closing/CTA slide of a teardown or
insight carousel where a real human face (the operator, not a stock photo) needs to carry the authority
of the recommendation.

## AI Image

generation_route: none
ref_input: n/a — no `[ai-image-zone]` block. The photo is a real static asset
(`assets/photo-main.jpg`, sourced verbatim from Farrice's own supplied studio portrait), never
AI-generated, at setup or per post. All other zones are plain CSS/HTML on a solid canvas-grey
background — no bg.png, no clean_ref pass.

## Slots

- **KICKER** — per-post category/series label
  - bbox: 7.78% 5.33% 45% 3%
  - style: Helvetica Neue 700, 2.41cqw, letter-spacing -0.01em, sentence case, ink on canvas
  - sample: "Creative Teardown"
  - user_editable: true

- **DATE** — post date (arrow glyph is fixed markup, not part of this slot)
  - bbox: 60% 5.33% 32.22% 3% (right-aligned)
  - style: Helvetica Neue 400, 2.04cqw, ink on canvas
  - sample: "03 Sep, 2026"
  - user_editable: true

- **PHOTO_MAIN_PATH** — Farrice's real, unaltered studio portrait
  - bbox: 7.78% 11.11% 84.44% 41.48%
  - style: contained rectangle, object-fit:cover, object-position:50% 30%, no radius, no shadow
  - sample: "assets/photo-main.jpg"
  - user_editable: true (a DIFFERENT real, unaltered photo of Farrice may be substituted by hand;
    AI-generated/regenerated photos are prohibited by `tokens.json > portrait_policy` — this slot must
    never be filled by an image-generation pipeline)

- **HEADLINE** — the closing statement / core argument
  - bbox: 7.78% 57.04% 84.44% 15%
  - style: display token custom scale (this ref's own editorial-grammar giant-word size, 92px/8.52cqw —
    clears the brand's own type_scale.display ceiling of 104px/9.63cqw), weight 700, letter-spacing
    -0.055em, line-height 0.94, lowercase/sentence case, Helvetica Neue, ink on canvas, left-aligned;
    supports `<br>` for the deliberate 2-line break and `<mark>` for a single emphasis word
  - sample: "choose the argument<br>before you multiply it."
  - user_editable: true

- **SUBTITLE** — supporting body copy
  - bbox: 7.78% 74.81% 55.56% 7%
  - style: Helvetica Neue 400, 2.22cqw, line-height 1.34, graphite (`--brand-secondary`), left-aligned
  - sample: "Three campaign angles, one lead recommendation, before the next creative round. That is the whole job."
  - user_editable: true

- **CTA_LABEL** — mid-canvas call-to-action (arrow glyph is fixed markup, not part of this slot)
  - bbox: 68% 74.96% 24.22% 3% (right-aligned)
  - style: Helvetica Neue 700, 2.22cqw, letter-spacing 0.16em, uppercase, ink on canvas
  - sample: "DM ANGLE"
  - user_editable: true

- **FOOTER_NAME** — author identity (fixed brand chrome)
  - bbox: within footer-strip zone, item 1 of 4
  - style: Helvetica Neue 400, 1.85cqw, ink on canvas
  - sample: "Farrice Cain"
  - user_editable: false (brand identity — not per-post content)

- **FOOTER_DOMAIN** — brand domain (fixed brand chrome)
  - bbox: within footer-strip zone, item 2 of 4
  - style: Helvetica Neue 400, 1.85cqw, ink on canvas
  - sample: "parallaxletter.substack.com"
  - user_editable: false (brand identity — not per-post content)

- **FOOTER_DESCRIPTOR** — positioning descriptor
  - bbox: within footer-strip zone, item 3 of 4
  - style: Helvetica Neue 400, 1.85cqw, ink on canvas
  - sample: "Supplement + performance brands"
  - user_editable: true (may be tailored per campaign/niche)

- **FOOTER_CTA** — CTA repeat
  - bbox: within footer-strip zone, item 4 of 4
  - style: Helvetica Neue 400, 1.85cqw, ink on canvas
  - sample: "DM ANGLE"
  - user_editable: true (mirrors CTA_LABEL)

## Strategy notes

- All zones are html-overlay. No ai-edit needed anywhere in this template — `strategy: html-overlay`,
  `edit_mode: none`.
- No chrome auto-inject: this ref's header row is the editorial-style per-post kicker/date grammar, not
  the pool's `chrome.masthead` — see `rationale.md` §4. No pagination dots (`tokens.json
  chrome.pagination: null`).
- Background is solid canvas-grey via CSS (`var(--brand-bg-light, #F3F3F0)`) — no `_ai_bg/` directory,
  no image zone other than the real photo asset.
- The photo is bound to `{{PHOTO_MAIN_PATH}}` (never a hardcoded `_ai_bg/…` path), per the renderer
  contract — its DEFAULT sample value points at `assets/photo-main.jpg`, the template's own copy of
  the real supplied portrait.
- Footer and mid-CTA both carry a static (non-slot) trailing arrow glyph `→`, matching the ref exactly.

## Fixed elements (not slot-editable)

- The `#F3F3F0` canvas-grey fill (`tokens.json colors.bg_light`) — never recolored per post.
- The photo's crop geometry (contained rectangle, `object-fit:cover`, `object-position:50% 30%`, no
  radius, no shadow) — the FRAMING is fixed; only the underlying photo FILE may be hand-swapped for a
  different real photo of Farrice.
- `FOOTER_NAME` ("Farrice Cain") and `FOOTER_DOMAIN` ("parallaxletter.substack.com") — brand identity,
  locked.
- The two decorative arrow glyphs (masthead date, mid-CTA) — always present, never removable per post.

## Known compromise (flagged for by-eye review, precedent: `headline-subline-cover`)

The ref's own footer sits at `bottom:64px` (≈4.74% from the canvas bottom edge) — inside both
`tokens.json canvas.safe_area.bottom` (108px/8%) and the LinkedIn platform's documented 160px dead
band (`html-craft.md` §2). This is the BRAND'S OWN approved reference frame (Farrice, 2026-09-03: "I
would rather this be the template"), authored deliberately as part of the "editorial style" pivot — ref
fidelity is preserved rather than pushing the footer up to satisfy the general safe-zone guidance. Flag
for by-eye confirmation if LinkedIn's own UI ever clips that low on this specific post format.

## Possible future variations

- Allow `KICKER` to read a different content-category label per post ("Case Study", "Framework", "The
  Angle Map") without changing the layout.
- If Farrice supplies additional real studio/environment photos later, `PHOTO_MAIN_PATH` can rotate
  through them by hand — still never AI-generated.
