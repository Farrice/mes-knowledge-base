# Template: signature-close-cta

source_ref: ../../../visual_refs/editorial/08-thanks-signature.png
canvas: 1080x1350 (4:5 LinkedIn carousel)
strategy: html-overlay

## Rationale

see rationale.md — form: solid-css · edit_mode: none (no AI generation; the bg is a flat CSS fill
matching `tokens.json colors.bg_light` exactly). Every block is `HTML-isolable-overlay`, including the
rotated script signature — the overlap with the giant word is a plain CSS `transform` + z-index stack,
not a photographic occlusion.

## Inventory

```yaml
bg_treatment:
  kind: solid-color
  has_baked_overlays: false
  needs_clean_ref: false

requires_photo_zone: false
zone_skip_reason: "no photo, silhouette, cutout, or scene content anywhere in the ref — the entire slide
  is flat CSS/typography on a solid canvas fill (form = solid-css, tree Q1 = yes); confirmed against the
  source composition file that generated this ref (compositions/editorial/frames/08-thanks-signature.html),
  which authors the whole frame as plain HTML/CSS with no image element at all"

elements:
  - name: series-title
    bbox: [7.78, 5.33, 45, 3]
    type: text
    content: "Creative Teardown"
    decision: slot
    notes: "per-post series/thread title, sentence case, Helvetica Neue 700, ink, -0.01em tracking —
      this editorial style's own masthead pattern (series title left / date+arrow right), distinct from
      the brand's locked FARRICE CAIN identity masthead used by the typographic style's templates. Slot
      is named SERIES_TITLE (NOT MASTHEAD_LEFT) — render_template.py force-overrides an exact
      'MASTHEAD_LEFT' slot with tokens.json chrome.masthead.labels[0] unconditionally; this row is
      per-post content, not the brand's fixed identity masthead, so it must use a non-colliding name."

  - name: masthead-date
    bbox: [55, 5.33, 30, 3]
    type: text
    content: "03 Sep, 2026"
    decision: slot
    notes: "per-post publish date, right-aligned, regular weight, ink; paired with a fixed arrow glyph"

  - name: masthead-arrow
    bbox: [95, 5.33, 4, 3]
    type: glyph
    decision: fixed
    reason: "a fixed decorative → glyph closing the header row — never per-post content"

  - name: headline-word
    bbox: [1, 27.4, 98, 30]
    type: text
    content: "dm angle"
    decision: slot
    notes: "the giant lowercase display word (ref: 250px/23.15cqw; authored ceiling trimmed to
      22.5cqw — weight 700, letter-spacing -0.065em, line-height 0.86, centered via flex). The
      ref's own measured box was top:34.44% height:15.93% (vertical center 42.4%) — the AUTHORED
      zone here is grown to height:30% around that SAME center (top:27.4%) to clear
      dead_space.py's text_height_fraction >= 0.25 floor, and inset left:1%/width:98% (from
      left:0/width:100%) so the rendered ink clears compare_render_to_ref.py's 1.5%
      canvas-safe-margin — the ref's own edge-to-edge fit measured 0.065% past it at the ref's
      exact 23.15cqw; 22.5cqw is the smallest trim that clears the margin, still ~19.5-20cqw
      measured cap-height (Check D floor 8cqw, tolerance floor 17.6cqw). This is the primary
      per-post variation axis: the recap/decision word the carousel closes on."

  - name: author-signature
    bbox: [25.93, 41.19, 50, 10]
    type: text
    content: "Farrice Cain"
    decision: fixed
    reason: "brand move #10 (script signature) — the author's own identity mark, overlaid diagonally
      across the giant word in the one unlocked signature accent; fixed brand content, sourced from
      tokens.json author.name, never per-post"

  - name: footer-author
    bbox: [7.78, 95.26, 20, 2]
    type: text
    content: "Farrice Cain"
    decision: fixed
    reason: "brand identity, matches tokens.json author.name"

  - name: footer-url
    bbox: [30, 95.26, 26, 2]
    type: text
    content: "parallaxletter.substack.com"
    decision: fixed
    reason: "the brand's owned publication URL — chrome, not per-post content"

  - name: footer-category
    bbox: [58, 95.26, 24, 2]
    type: text
    content: "Supplement + performance brands"
    decision: fixed
    reason: "sentence-case shorthand of tokens.json chrome.masthead.labels[2], the brand's category
      descriptor — chrome, not per-post content"

  - name: footer-topic
    bbox: [84, 95.26, 12, 2]
    type: text
    content: "DM ANGLE"
    decision: slot
    notes: "per-post resolved topic/thread tag this closing frame wraps up — same role as
      RECOMMENDATION_NAME in the sibling statement-close-cta template"

chrome_observed:
  masthead_visible_in_ref: true
  pagination_dots_visible_in_ref: false
  page_indicator_visible_in_ref: false
```

## Visual summary

A pure-typographic closing/CTA frame on this editorial style's flat canvas (`#F3F3F0`) — no photo, no
texture, no AI generation. A small header row (per-post series title left, date + fixed arrow right) sits
above a giant, edge-to-edge lowercase display word carrying the closing recap/decision, crossed diagonally
by the brand's red script signature (move #10) — the one human, hand-made mark on an otherwise edited
system. A four-item footer strip (author, URL, category, resolved topic tag) closes the base. Use it as the
final "thanks / sign-off" slide of a carousel, wherever the brand's own signature should visibly close the
piece.

## AI Image

generation_route: none — solid-css scenario, no `[ai-image-zone]` block. Background is
`background: var(--brand-bg-light);` (CSS), reproducing the ref's flat fill exactly
(`tokens.json colors.bg_light` = `#F3F3F0`).

## Slots

- **SERIES_TITLE** — per-post series/thread title (named to avoid the reserved `MASTHEAD_LEFT`
  auto-injection — see the `series-title` inventory note above)
  - bbox: 7.78% 5.33% 45% 3%
  - style: Helvetica Neue 700, 2.41cqw, letter-spacing -0.01em, ink, left-align
  - sample: "Creative Teardown"
  - user_editable: true

- **MASTHEAD_DATE** — per-post publish date
  - bbox: 55% 5.33% 30% 3%
  - style: Helvetica Neue 400, 2.04cqw, ink, right-align (paired with a fixed → glyph)
  - sample: "03 Sep, 2026"
  - user_editable: true

- **HEADLINE_WORD** — the giant closing/recap word
  - bbox: 1% 27.4% 98% 30% (zone grown/inset around the ref's measured vertical center 42.4% —
    see the `headline-word` inventory note above)
  - style: display token, 22.5cqw ceiling (ref: 23.15cqw, trimmed for the canvas-safe-margin —
    see the inventory note; autosize still shrinks further to fit width on longer per-post
    values, floor 9cqw per `html-craft.md` §3), Helvetica Neue 700, letter-spacing -0.065em,
    line-height 0.86, lowercase/sentence-adjacent per ref, ink, centered, `white-space:nowrap`
    single line
  - sample: "dm angle"
  - user_editable: true — the per-post variation axis

- **FOOTER_TOPIC** — resolved topic/thread tag
  - bbox: 84% 95.26% 12% 2%
  - style: Helvetica Neue 400, 1.85cqw, ink, right-align
  - sample: "DM ANGLE"
  - user_editable: true

## Fixed elements (not slot-editable)

- The flat `#F3F3F0` (`--brand-bg-light`) canvas fill.
- `MASTHEAD_ARROW` — fixed "→" glyph closing the header row.
- `AUTHOR_SIGNATURE` — "Farrice Cain" in the script placeholder face (Snell Roundhand / Zapfino,
  pending the real handwriting SVG per `moves.md` #10), rotated -7°, in `colors.signature_accent`
  (`#FF2D2D`) — the brand's own identity mark, never per-post.
- `FOOTER_AUTHOR` ("Farrice Cain"), `FOOTER_URL` ("parallaxletter.substack.com"),
  `FOOTER_CATEGORY` ("Supplement + performance brands") — brand chrome sourced from
  `tokens.json author.name` / the brand's owned URL / the category descriptor.

## Strategy notes

- All zones are html-overlay. No ai-edit needed — `strategy: html-overlay`, `edit_mode: none`.
- Chrome injected: the header row (series title + date/arrow) and the footer strip. No `NN/NN` field
  index or pagination dots — this ref does not show one (`chrome_observed.page_indicator_visible_in_ref:
  false`), matching the brand's editorial-style close frames which lead with the signature, not a counter.
- Each zone is positioned `absolute` to its own measured bbox (`_measurements.yaml`) — the blocks are
  spread across distinct, widely-separated bands (header ~5%, giant word ~34-50%, signature overlaid
  ~41-51%, footer ~95%), never collapsed into one top-anchored flow column.
- `AUTHOR_SIGNATURE` is positioned exactly as the source composition authored it (`left`/`top` only, no
  explicit `width` — shrink-to-fit around its fixed content, matching
  `compositions/editorial/frames/08-thanks-signature.html`), rotated with `transform: rotate(-7deg)`.

## Known trade-off from the dead-space gate (flagged for by-eye review)

`dead_space.py`'s `text_height_fraction` floor (>= 0.25 of canvas height, union of the measured
text zones) is not cleared by this ref's own geometry alone (a giant single-line word + a thin
footer strip, both intentionally small vertical spans on a deliberately open canvas — this
close/CTA frame is, by design, more open than a typical body slide). Rather than inventing new
on-canvas content to fill the gate, `HEADLINE_WORD`'s zone height was grown from the ref-measured
15.93% to 30%, kept centered on the SAME vertical midpoint via flex centering — the rendered giant
word does not move; only its invisible bounding box grew. This mirrors the same class of trade-off
already documented in `headline-subline-cover`'s Check-D ladder note: a scripted numeric floor,
not this ref's own restrained composition, drives the adjustment. No other geometry changed.

## Possible future variations

- Swap the script placeholder face for the real handwriting SVG once `visual-identity/logos/signature.svg`
  lands (per `moves.md` #10) — `AUTHOR_SIGNATURE` would become an `<img>` slot instead of styled text.
- Allow a per-carousel `NN/NN` field index to be reintroduced on the header row if a future close frame
  wants the counter alongside the signature.
