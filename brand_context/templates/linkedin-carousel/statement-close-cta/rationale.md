# rationale — statement-close-cta

## ① Form + tree-path-with-why

form: solid-css

- **Q1 — TRULY solid color, zero texture, no image? YES.** The entire 1080×1350 canvas is one flat
  fill, near-black (`#101010`, the brand's `bg_dark`/`ink` token). There is no gradient, no vignette,
  no paper grain, no photographic or illustrated content anywhere on the surface — every mark on the
  slide (masthead text, the closing headline, the three route-strokes, the footer caption, the
  recommendation label) is a flat CSS/typographic element sitting directly on that fill. `image_zone.exists
  = false`. The tree STOPS at Q1 — solid-css — and no scenario further down the list (B1 surface, A framed
  image, C integrated-text, B2 reserved-zone background) is reachable because none of their preconditions (a blank in-scene
  surface, a contained photo rectangle, a full-texture/landscape bg) are present.
- Ruled out in order for completeness: Q2 (blank in-scene surface) — no, there is no depicted
  screen/frame/paper inside a scene; the "surface" IS the canvas itself, not an object drawn on it. Q3
  (contained-rectangle image) — no, there is no image at all. Q4 (integrated-complex text with no isolable
  container) — no, every text/graphic block sits cleanly on the flat fill with nothing occluding it; each
  one passes the isolability test independently (see §2). Q5 fallthrough is moot because Q1 already matched.

## ② Per-block breakdown

- **Masthead-left "THE ANGLE MAP"** · HTML-isolable-overlay · brand chrome — `tokens.json →
  chrome.masthead.offer_mode_labels[0]`. Small uppercase Helvetica Neue 700, +0.16em tracking, top-left,
  reading `graphite`/`stone` on the dark fill. Fully isolated, no overlap, recognizable system font → HTML.
  Not per-post content; this is the brand's fixed offer-mode series label (`tokens.json` `locked_fields`
  includes `chrome.masthead`).
- **Field index "04 / 04"** (top-right) · HTML-isolable-overlay · brand move #2 (Field index), rendered here
  as `current/total` rather than the `FIELD/NN` example form — still the same functional device: a two-digit
  position marker in place of dots. Small caption-scale text, `stone`/`graphite`. Isolated, plain, no
  overlap → HTML. This IS per-post/per-slide content (which position in the sequence) so it is the one chrome
  slot that stays editable.
- **Decision line (hairline rule under masthead)** · HTML-isolable-overlay · brand move #3 (Decision line):
  a 1px horizontal rule in `line` (#D8D8D3), full content-width, sitting directly under the masthead row.
  Pure structural CSS, trivially isolable → HTML.
- **Distinctive element — closing headline "Choose the argument / before you / multiply it."**
  `present: true` · `position: upper-middle-left` (roughly the canvas's upper-middle third, left-aligned to
  the safe margin) · `size: dominant` (the single largest, most weighted element on the slide — three lines
  at display scale) · `fill: paper` (`#FAFAF8`, i.e. `text_on_dark`) · `value: solid` (full-strength white,
  not ghosted) · `treatment: HTML`. Sentence case, Helvetica Neue 700, tight tracking/leading exactly per
  `type_scale.display`. It sits on the flat ink fill with nothing overlapping or occluding it — the
  isolability test passes cleanly (no subject, no woven pill, no relief/texture to integrate with) — so per
  `identification-tree.md` rule 6 this is a "dominant display word NOT occluded" → routes **HTML**, prominent,
  never AI-baked. The three explicit line breaks in the ref ("argument" / "before you" / "multiply it.") are
  authored as real `<br>`s (triple-brace slot), not left to auto-wrap, because the ref shows a deliberate
  3-line composition, not a paragraph reflow.
- **Distinctive element — three-route grammar (the angle-comparison device)** · `present: true` ·
  `position: lower-middle` (a horizontal band roughly two-thirds down the canvas, between the headline and the
  footer) · `size: medium` (spans the full content width but occupies a modest vertical band — three thin
  rows, not a dominant graphic) · `fill: mixed` — the two quiet routes (01, 03) run in `line` gray
  (#D8D8D3) with a small hollow/outline circle at the line end; the recommended route (**02 LEAD**) runs
  heavier (visually ~6px vs ~1px) in `paper` white with a solid filled circle at its end and its label set in
  bold caps ("02 LEAD" vs plain "01"/"03") · `value: solid` for both weights (no ghosting) · `treatment: HTML`.
  This is brand move #4 ("Three-route grammar") verbatim: three parallel strokes differentiated by number,
  position and weight, the recommended one 6px/ink-equivalent (here: paper, because the whole surface is
  already the brand's "one bold dark move" — see below), the quiet ones 1–2px. It is pure CSS lines + small
  circle markers + caption-scale numeral/label text — no photographic or occluded content — so it is fully
  isolable → HTML. This device is legitimate here (not decorative route-lines-with-nothing-compared) because
  the slide genuinely IS the resolution of a 3-route comparison: it is slide 4/4 of "The Angle Map" sequence,
  declaring which of the three campaign angles is the lead recommendation.
- **Footer caption "THREE CAMPAIGN ANGLES · ONE LEAD RECOMMENDATION"** · HTML-isolable-overlay · caption-scale
  token, uppercase, +0.16em tracking, `stone`/`graphite`, left-aligned above the recommendation label. Plain,
  isolated, recognizable font → HTML.
- **Distinctive element — recommendation label "DM ANGLE"** · `present: true` · `position: lower-left,
  bottom edge` · `size: medium` (bold, larger than the footer caption but smaller than the headline — a
  second-tier emphasis) · `fill: paper` (white on the dark fill) · `value: solid` · `treatment: HTML`. This is
  the resolved answer to the route comparison above it — the actual NAME of the "02 LEAD" angle spelled out
  as a bold closing statement. It reads as this template's true swappable content field (the specific
  recommended-angle name changes carousel to carousel; the headline statement above it is the second variable
  axis). Bold Helvetica Neue, sentence/caps per ref, sits cleanly on the flat fill → HTML.
- **Whole-canvas dark fill = the brand's "Dark recommendation" move (#6).** `tokens.json` states this move is
  "an ink field with paper text, reserved for the consequential decision — maximum one per sequence." This
  slide IS that consequential decision (the closing/CTA frame revealing the lead recommendation), so the
  entire canvas going dark, edge-to-edge, is the correct and singular use of that move for this position in a
  carousel — not an invented flourish, but the ref's own composition read directly.

## ③ Pipeline

edit_mode: none
when_ai_runs: never — no `[ai-image-zone]` block is written; per `scenarios/solid-css.md` the background is
pure CSS (`background: var(--brand-bg-dark)`) and every mark on the slide is HTML/CSS text or CSS-drawn lines
and circles. No transparent-subject-over-solid exception applies (no subject anywhere in the ref).
extraction: nothing to extract/clean — there is no ref pixel content to preserve; the ref is read once for
composition (bbox/hierarchy) and then fully reproduced in HTML/CSS. All zones become HTML: masthead (2
slots), field index, decision line, headline, three-route grammar (3 rows + labels + dots), footer caption,
recommendation label.

## ④ Ambiguity (examined)

Two points were genuinely weighed before settling on solid-css with all-HTML routing:

1. **Could the three-route grammar be read as an "integrated/woven" composition (Q4 → C) instead of clean
   HTML?** Considered and ruled OUT. The Q4 woven-typography test (identification-tree.md, "the decisive
   routing question" + the woven-typography extension) asks whether another element threads through or
   overlaps the block's letterforms — a pill over a headline, a knockout inside a word, a caret in a
   baseline. Here nothing overlaps: the three lines sit in their own clear horizontal band below the
   headline, with their number/label text positioned cleanly above or beside each line, never crossing or
   overlapping the headline or each other. It fails every "woven" signal, so it stays isolable → HTML, not C.
2. **Is the near-black fill genuinely `solid-color`, or could it be a subtly textured/vignetted surface (the
   Q1 "textured near-white ≠ solid" trap, inverted for dark)?** Examined closely — no visible grain, no
   corner vignette, no gradient banding is present; the fill reads as a single flat hex value from edge to
   edge, matching `tokens.json colors.bg_dark = #101010` exactly. This is the genuine solid-color case the
   trap warns AGAINST wrongly demoting, not the "near-white paper-grain card" case the trap warns against
   wrongly promoting — so Q1 = yes stands.
3. **Should "DM ANGLE" be merged into the footer caption as one block, or kept as its own zone?** Ruled to
   keep it separate: the footer caption is small, tracked, functional-label scale (`caption` token) while "DM
   ANGLE" is bold and roughly double the caption's visual weight — a distinct hierarchy level (second bold
   move after the headline), not a continuation of the same sentence. Per `html-craft.md` §4 ("don't fuse a
   stack into one block"), they are authored as two stacked zones, not merged.
