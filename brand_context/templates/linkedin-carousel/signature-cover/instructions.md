# Template: signature-cover

source_ref: ../../../visual_refs/editorial/01-cover-signature.png
canvas: 1080x1350 (4:5 LinkedIn carousel)
strategy: html-overlay

## Rationale

See `rationale.md` for the full per-block reasoning. At-a-glance:

form: solid-css
edit_mode: none — pure CSS/HTML, zero AI generation for any post rendered from this template.

## Inventory

```yaml
ignore_screenshot_chrome: []

bg_treatment:
  kind: solid-color   # eyedropped at 9 points across the canvas — identical RGB(243,243,240)
                       # everywhere, std=0. Matches tokens.json colors.bg_light / named.canvas
                       # exactly. Confirmed against the ref's own source composition file
                       # (compositions/editorial/frames/01-cover-signature.html): a literal
                       # `background: #F3F3F0` CSS fill, nothing painted under it.
  has_baked_overlays: false
  needs_clean_ref: false
  cleaned_bg_path: null

requires_photo_zone: false   # no photo/silhouette/cutout/scene element anywhere on the ref —
                              # the whole canvas is flat fill + vector type.

elements:
  - name: category-label
    bbox: [7.78, 5.33, 35, 3.0]
    type: text
    content: "Creative Teardown"
    decision: slot          # CATEGORY slot — the series/category title, per-post variable
    notes: "top-left, Helvetica Neue 700 26px/2.41cqw, letter-spacing -0.01em, sentence case"

  - name: date-label
    bbox: [70, 5.33, 17, 3.0]
    type: text
    content: "03 Sep, 2026"
    decision: slot          # DATE slot — publish date, per-post variable
    notes: "top-right, same row as category (flex space-between), Helvetica Neue 400 22px/2.04cqw"

  - name: header-arrow
    bbox: [89.5, 5.33, 3, 3.0]
    type: glyph
    content: "→"
    decision: fixed
    notes: "literal Unicode arrow glyph (U+2192) in the source DOM, not an SVG/logo asset — never varies, no content reason to swap it, no icon-provenance resolution needed"

  - name: headline-word
    bbox: [0, 33.7, 100, 15.5]
    type: text
    content: "teardown"
    decision: slot          # HEADLINE_WORD slot — the PRIMARY per-post variation axis
    notes: "giant lowercase Helvetica Neue 700, 238px/22.04cqw ceiling, line-height 0.86, letter-spacing -0.065em, full-width centered. box-grows: no fixed height, wraps rather than clips."

  - name: script-signature
    bbox: [22.22, 40, 57.18, 10.3]
    type: text
    content: "Farrice Cain"
    decision: fixed
    notes: "brand move #10 (script signature) — Snell Roundhand/Zapfino cursive, 116px/10.74cqw, rotate(-7deg), color = tokens.json colors.signature_accent (#FF2D2D), the one unlocked accent. Fixed brand mark, present on cover + close frames only, never a per-post variable."

  - name: footer-author
    bbox: [7.78, 93.5, 10, 2.2]
    type: text
    content: "Farrice Cain"
    decision: fixed
    notes: "matches tokens.json author.name — brand identity, not per-post"

  - name: footer-url
    bbox: [22.0, 93.5, 23, 2.2]
    type: text
    content: "parallaxletter.substack.com"
    decision: fixed
    notes: "the brand's owned publication URL — not per-post"

  - name: footer-niche
    bbox: [49, 93.5, 30, 2.2]
    type: text
    content: "Supplement + performance brands"
    decision: fixed
    notes: "sentence-case shorthand of tokens.json chrome.masthead.labels[2] (uppercase form) — same brand content, editorial-style casing variant, not new content"

  - name: footer-cta
    bbox: [82.5, 93.5, 10.5, 2.2]
    type: text
    content: "DM ANGLE"
    decision: fixed
    notes: "the series' standing engagement CTA — static in the source composition, not tied to this post's topic"

chrome_observed:
  masthead_visible_in_ref: false   # this ref's header row is a bespoke CATEGORY+DATE composition,
                                    # NOT the brand's standard tokens.json chrome.masthead 3-slot
                                    # component (which reads "FARRICE CAIN" / a descriptor) — see
                                    # rationale.md §④. Built as its own zone, not the shared masthead.
  pagination_dots_visible_in_ref: false
```

## Visual summary

A pure-CSS editorial cover: a flat canvas-color (`#F3F3F0`) background carries a small
category-title + date header row (top), one giant all-lowercase black display word as the hook
(center, ~34–48% of canvas height), Farrice's red script signature rotated across the lower half of
that word, and a four-item credit footer (author · owned URL · niche · CTA) along the base. No AI
generation, no photography, no texture — every mark is native browser type, two of them layered with a
CSS rotation. Use this as the opening/cover frame of the "Creative Teardown" (or any single-hook-word)
carousel series; its close-frame counterpart is the sibling `signature-close-cta` template.

## AI Image

None. This template is pure CSS/HTML — no `[ai-image-zone]` block exists and no post rendered from
this template ever calls an image generator. See `rationale.md` §③ Pipeline.

## Slots

- **CATEGORY** — series/category title, top-left
  - bbox: 7.78% 5.33% 35% 3.0%
  - style: Helvetica Neue 700, 2.41cqw, letter-spacing -0.01em, ink, sentence case
  - sample: "Creative Teardown"
  - user_editable: true

- **DATE** — publish date, top-right
  - bbox: 70% 5.33% 17% 3.0%
  - style: Helvetica Neue 400, 2.04cqw, ink
  - sample: "03 Sep, 2026"
  - user_editable: true

- **HEADLINE_WORD** — the giant one-word hook (PRIMARY per-post variation axis)
  - bbox: 0% 33.7% 100% 15.5%
  - style: Helvetica Neue 700, 22.04cqw ceiling (auto-shrinks for longer words), line-height 0.86, letter-spacing -0.065em, all-lowercase, centered, ink
  - sample: "teardown"
  - user_editable: true
  - max_chars: ~14 at full ceiling size before the autosize net starts stepping the font down (longer words still fit — they render smaller, never clip)

- **SIGNATURE** — the author's script signature, overlaid on the giant word
  - bbox: 22.22% 40% 57.18% 10.3%
  - style: "Snell Roundhand"/"Zapfino" cursive, 10.74cqw, rotate(-7deg), `var(--signature-accent)` (#FF2D2D)
  - sample: "Farrice Cain"
  - user_editable: false — fixed brand mark (moves.md #10); never varies per post

- **AUTHOR_NAME** — footer item 1
  - bbox: 7.78% 93.5% 10% 2.2%
  - style: Helvetica Neue 400, 1.85cqw, ink
  - sample: "Farrice Cain"
  - user_editable: false — brand identity, fixed

- **SITE_URL** — footer item 2
  - bbox: 22.0% 93.5% 23% 2.2%
  - style: Helvetica Neue 400, 1.85cqw, ink
  - sample: "parallaxletter.substack.com"
  - user_editable: false — brand-owned URL, fixed

- **NICHE_LABEL** — footer item 3
  - bbox: 49% 93.5% 30% 2.2%
  - style: Helvetica Neue 400, 1.85cqw, ink
  - sample: "Supplement + performance brands"
  - user_editable: false — brand niche descriptor, fixed

- **CTA_LABEL** — footer item 4
  - bbox: 82.5% 93.5% 10.5% 2.2%
  - style: Helvetica Neue 400, 1.85cqw, ink
  - sample: "DM ANGLE"
  - user_editable: false — standing series CTA, fixed by default (technically editable text, not intended to vary)

## Strategy notes

- All zones are html-overlay. No ai-edit needed anywhere in this template.
- No chrome auto-inject: the standard `{{MASTHEAD_*}}` / `{{DOTS}}` components are NOT used —
  `tokens.json chrome.masthead` labels ("FARRICE CAIN" / descriptor) don't match what this ref shows
  (a bespoke CATEGORY+DATE header and a 4-item footer credit strip), so both are authored as their own
  bespoke zones instead of the shared masthead/dots partials.
- Bg is solid `var(--brand-bg-light)` via CSS — no `_ai_bg/` directory, no `bg.png` file.
- The one color in this template that is NOT part of the renderer's brand-kit CSS-var schema
  (`--signature-accent`, `tokens.json colors.signature_accent`) is declared as a local custom property
  inside `template.html`'s own `<style>` block — see the comment there for why `var(--brand-accent)`
  cannot be used (it resolves to ink on this brand, not the signature coral).

## Fixed elements (not slot-editable)

- The canvas background color (`var(--brand-bg-light)`, `#F3F3F0`).
- The header arrow glyph ("→") — a literal Unicode character, always present, never swapped.
- The script signature's font stack, rotation (-7deg), and color (`var(--signature-accent)`,
  `#FF2D2D`) — brand move #10, cover/close frames only.
- The footer's four-item layout (author / URL / niche / CTA) and each item's default text — exposed as
  slots for maintainability but intended to stay at their brand-fixed defaults across every post using
  this template.
- The lowercase transform on the giant headline word — the design language is always-lowercase
  regardless of what case the slot value is typed in.

## Possible future variations

- Swap the signature's system-font placeholder for Farrice's real handwritten signature SVG once it
  lands at `visual-identity/logos/signature.svg` (per moves.md #10's stated migration path).
- Allow `NICHE_LABEL` / `CTA_LABEL` to vary per campaign if Farrice ever runs a sub-brand or guest
  co-signed edition of this series.
