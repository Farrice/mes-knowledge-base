# rationale — two-photo-list-body

## ① Form + tree-path-with-why

form: a-framed-image

- **Q1 — NO.** `bg_treatment: solid-color` is true in isolation (the canvas fill is a flat `#F3F3F0`, eyedropper-
  confirmed at nine sample points — top-left corner, mid-column, far-right margin, between the two photos, and
  bottom-right corner all return the identical `(243,243,240)` triple, zero gradient/grain) — but Q1 requires
  BOTH a flat fill AND `image_zone.exists: false`. This ref carries two real, hard-edged photographs in the
  right column, so `image_zone.exists: true` and Q1 fails on its second clause. The tree does not stop here.
- **Q2 — NO.** There is no blank in-scene surface (no screen/frame/paper/billboard depicted *inside* a photo)
  holding content — the two photo rectangles ARE the content, not placeholders inside a larger scene.
- **Q3 — YES.** `image_zone.containment: contained-rectangle`. Both photos are hard-edged rectangles with the
  canvas's own flat `#F3F3F0` fill visible on all four sides (confirmed by pixel-scanning: photo 1 spans
  x 51.85%–92.18%, y 11.11%–48.11%; photo 2 spans the same x-range, y 49.63%–88.85%; every pixel outside those
  two boxes in the right column reads the exact bg triple). Applying the **Q3 object-isolability test**
  (`identification-tree.md`): both photos are flat, axis-aligned, non-overlapping, with NO rotation, NO
  perspective, NO cast shadow, NO occlusion — they pass cleanly as bounded `<img>` slots, not in-scene props.
  The tree **STOPS at Q3** — Form A (framed image), with the important variant that there are **two** framed
  images stacked in the same right-hand column rather than one; `scenarios/a-framed-image.md` does not cap the
  count, and the Build section explicitly anticipates "two image slots → two blocks."
- Text placement: `outside-image`. Every text block (title, date, headline, body, three list items, footer)
  lives in the LEFT column — a clean, isolated HTML zone entirely separate from the photo rectangles. This is
  the textbook Form-A geometry: the image sits in a frame; text lives outside it.

## ② Per-block breakdown

Reading the ref top to bottom, left column first, then the right-column photos, then the footer. Every text
block passes the isolability test trivially — nothing overlaps a photo, nothing rides an object's geometry,
the font is the brand's own recognizable Helvetica Neue — so every text block is `HTML-isolable-overlay`.

- **Title "Creative Teardown" (top-left)** · HTML-isolable-overlay · a header/series-title label, NOT the
  brand's standard functional-masthead move (`moves.md` #1 puts "FARRICE CAIN" top-left in tracked uppercase
  graphite) — this editorial-style ref relocates the author identity to the FOOTER (see below) and uses the
  top-left slot for the *content-series title* instead, sentence case, ink, untracked, weight 700. This is a
  deliberate, source-confirmed grammar: the exact HTML/CSS this PNG was rendered from
  (`visual-identity/compositions/editorial/frames/05-two-photo-stack.html` + `_editorial.css`) declares
  `.head .title { font-weight:700; font-size:26px; letter-spacing:-0.01em; }` with content `"Creative
  Teardown"` — confirming this is the editorial style's header title, not a masthead mis-read.
  - `present: true` · `position: top-left` · `size: minor` (26px caption-adjacent, not competing with the
    112px headline) · `fill: ink` (`#101010`, the source CSS's default text color, no graphite override) ·
    `value: solid` · `treatment: HTML`.
- **Date + arrow "03 Sep, 2026 →" (top-right)** · HTML-isolable-overlay · a per-slide date stamp with a
  small directional arrow glyph (`.head .arrow{font-size:30px}`), flex-paired with the title via
  `justify-content:space-between` on the shared header row. The arrow is a plain Unicode glyph (`→`), not a
  brand mark/logo — no SVG asset resolution needed (`shared/icons.md` is for brand marks; a typographic arrow
  character is ordinary text content).
  - `present: true` · `position: top-right` · `size: minor` · `fill: ink` · `value: solid` · `treatment: HTML`.
- **Headline "what / changed" (giant lowercase, 2-line)** · HTML-isolable-overlay · the brand's editorial
  "giant lowercase display word" move (`REVIEW-NOTES.md` 2026-09-03 pivot: "giant lowercase display words…";
  `styles.json` editorial description: "giant lowercase display words"). Source CSS: `.h {font-weight:700;
  letter-spacing:-0.04em; line-height:0.92}` at `font-size:112px`. Sits cleanly on the flat canvas fill, no
  photographic subject anywhere near it, no woven pill or knockout — isolability passes trivially. This is
  also the `distinctive_elements` "dominant display" case (`identification-tree.md` rule 6): the display is
  large but **not occluded by anything**, so it routes `HTML` (prominent), never AI-baked.
  - `distinctive_elements` row: `element: "giant lowercase headline 'what changed'"` · `present: true` ·
    `position: upper-left, left column` · `size: dominant` (112px = 10.37cqw, the largest element on the
    canvas) · `fill: ink` · `value: solid` · `treatment: HTML`.
- **Body intro paragraph** · HTML-isolable-overlay · "Across three years of creative rounds the format changed
  every quarter. The argument underneath did not move once." Source: `.body{font-weight:400; line-height:1.34;
  color:#101010}` at an inline-overridden `font-size:24px` (2.22cqw) — ink, not graphite (the `.body.grey`
  modifier class exists in the shared CSS but is NOT applied to this particular paragraph in the source frame).
  Isolable, HTML, left-aligned in the same 440px/40.74%-wide column as the headline.
- **Three dated list items** (2024 · studio statics / 2025 · creator UGC / 2026 · dynamic variants), each a
  bold year+label line (`h4`, 26px/700/letter-spacing −0.02em) followed by a one-to-two-line regular
  description (`p`, 21px/400/line-height 1.3) · HTML-isolable-overlay · a repeating pattern, evenly spaced on
  a consistent 160px (11.85%) rhythm (items at top 660px/48.89%, 820px/60.74%, 980px/72.59% — confirmed by
  direct pixel-scan of the rendered PNG, which matches the source CSS `top` values exactly). Fully isolated,
  no scene, no overlap — HTML.
- **Two framed photographs (right column)** — see the dedicated image-block reads below.
- **Footer strip** (`Farrice Cain` · `parallaxletter.substack.com` · `Supplement + performance brands` ·
  `DM ANGLE`) · HTML-isolable-overlay · a 4-item flex row, `justify-content:space-between`, 20px/400/ink
  (`_editorial.css .foot`). This IS the brand's author-identity content (name + the newsletter URL + the
  niche descriptor, echoing `tokens.json → chrome.masthead.labels: ["FARRICE CAIN", "", "CREATIVE STRATEGY FOR
  SUPPLEMENT + PERFORMANCE BRANDS"]`) — relocated from the top (where the standard masthead move lives) to the
  bottom, which is this editorial style's own established grammar (confirmed identically across all eight
  approved editorial frames, not a one-off deviation on this ref alone). `DM ANGLE` is the carousel's
  recurring CTA label.
  - `present: true` · `position: bottom, full-width` · `size: minor` · `fill: ink` · `value: solid` ·
    `treatment: HTML`.

### Image blocks — the two framed photographs

- **PHOTO_MAIN (upper photo, a hand pouring supplement powder from a green scoop into a glass jar)**:
  `containment: contained-rectangle` (hard edge, canvas fill visible around it on all sides) ·
  `medium: photo` (a real, documentary product photograph — not an illustration or 3D render) ·
  `lighting: natural` (soft, even studio/product-photography light, no dramatic shadow) ·
  `subject_treatment: isolated-on-light-bg` (the product sits against a near-white backdrop within its own
  frame) · `subject_role: free-subject` (the slug `two-photo-list-body` names the LAYOUT — two stacked framed
  photos + a list — not a fixed object; a different "Creative Teardown" post examines a different
  product/brand's creative, so the specific subject genuinely varies per post) · `hero_face_identity: n/a`
  (no face in frame) · `legibility-method: n/a` (no text overlays this photo anywhere in the composition —
  all text lives in the separate left column, so no scrim/band decision applies).
- **PHOTO_SECOND (lower photo, a macro/abstract shot of green bubbles with an iridescent highlight)**: same
  `containment: contained-rectangle` · `medium: photo` · `lighting: natural` (macro product/ingredient
  photography, not dramatically lit) · `subject_treatment: full-bleed` (the texture fills its own frame edge
  to edge, no backdrop margin, unlike photo 1's isolated-on-white treatment — read per-photo, not assumed
  uniform) · `subject_role: free-subject` (same reasoning as above) · `hero_face_identity: n/a` ·
  `legibility-method: n/a`.

**Critical provenance fact that governs the pipeline (§③ below): these two photos are NOT ref-composition
placeholders for AI generation — they are literal, real captured crops.** The exact HTML/CSS source this PNG
renders from (`visual-identity/compositions/editorial/frames/05-two-photo-stack.html`) points its two
`<img>` tags at `../evidence/huel-greens/crop-scoop.png` and `../evidence/huel-greens/crop-bubbles.png` — real
crops Farrice captured via Playwright from `https://huel.com/products/huel-daily-greens` (see
`visual-identity/compositions/editorial/evidence/huel-greens/manifest.json`, timestamped 2026-09-03), not
stock photography and not an AI generation. This is not incidental — it is explicit, recorded brand policy:
`REVIEW-NOTES.md` (2026-09-03, "aesthetic pivot"): *"every photo zone holds a REAL source (Meta Ad Library
capture, Huel product page capture, his studio portrait) — stock imagery rejected on sight"*; `moves.md` #8
(Evidence crop): *"Only owned brand artifacts and verified source excerpts qualify… AI-generated imagery is
not evidence and never fills this zone"*; and `tokens.json → prohibited`: *"stock supplement imagery as
generic credibility"*, *"faux-lab imagery"*. This routes the pipeline decision in §③.

## ③ Pipeline

edit_mode: none
when_ai_runs: never — this template makes ZERO AI image-generation calls. No `[ai-image-zone]` block is
authored. `PHOTO_MAIN_PATH` and `PHOTO_SECOND_PATH` are plain HTML `<img>` slots that receive **real per-post
source captures** (a screenshot/crop of whatever product page, ad, or creative the "Creative Teardown" post is
examining) — architecturally this is `photo_zones[].source: user-uploaded-asset`, the third option the
Template Card schema already carries alongside `clean_ref` and `ai-gen-on-demand`
(`shared/conventions/slots-and-html.md` instructions.md anatomy). This is a deliberate, brand-mandated
departure from the builder's general AI-first default for imagery (never for TEXT — every text block above
still routes through the normal HTML-isolable path) — see §④ for the reasoning.
extraction: no AI cleanup or recreation of any kind. The canonical `assets/ref-canonical.png` is still saved
(mandatory, the audit trail) but is never passed as an `--input-image` to any generator, because none runs.
The two canonical preview images (`crop-scoop.png`, `crop-bubbles.png`) are copied verbatim from
`visual-identity/compositions/editorial/evidence/huel-greens/` into this template's own `assets/` folder as the
demo/sample fill for `PHOTO_MAIN_PATH` / `PHOTO_SECOND_PATH` — real captured product photography, not a
generated placeholder.

## ④ Ambiguity (examined)

- **The central tension: the builder's AI-first master rule vs. this brand's explicit no-AI-photography
  doctrine.** The default posture for any image zone in this system is "AI generates by default; HTML is the
  surgical exception" — and Form A's own scenario file defaults to `edit-from-ref` for the photo slot. I
  weighed generating the two photos via `edit-from-ref` (using `assets/ref-canonical.png` as `--input-image`,
  `{PHOTO_SUBJECT}` as the per-post delta) against leaving them as real-upload slots, and ruled OUT AI
  generation for THIS specific pair of zones: the brand's own `REVIEW-NOTES.md` (a LIVING doc, Farrice's
  literal words, dated the same day as this ref) states plainly that "every photo zone holds a REAL source…
  stock imagery rejected on sight," `moves.md` #8 states "AI-generated imagery is not evidence and never fills
  this zone," `tokens.json → prohibited` explicitly bans "stock supplement imagery as generic credibility" and
  "faux-lab imagery," and the `portrait_policy` block separately prohibits "face regeneration… synthetic
  portraits" for the brand's own portrait content. The whole point of a "Creative Teardown" post is showing a
  REAL competitor/example creative — an AI-hallucinated product photo would undermine the entire premise of
  the series (this is evidence, not illustration). The source HTML/CSS this exact ref renders from confirms
  the intended fill is a real captured crop, not a generation target. Given the brand's own explicit, recorded,
  and freshly-approved instruction directly contradicts the tool's generic default, I followed the brand's
  instruction (Partner Posture: "when a rule fights what's actually in front of you, use judgment") and treated
  both photo slots as real-upload zones with zero AI calls — $0 cost, zero OpenAI budget consumed, and no risk
  of shipping a synthetic "faux-lab" image the brand has explicitly rejected.
- **Considered whether this ref might instead be B2 (`on-reserved-zone`)** — ruled OUT: B2 requires a
  *generated* full bg/texture with text floating on a reserved clean band WITHIN that generated image. Here the
  bg is a flat, ungenerated CSS fill and the "images" are two separate, hard-edged, bounded rectangles with
  their own real content — not a texture the text floats over. This is squarely Form A's contained-rectangle
  case, doubled.
- **Considered whether the two photos should be treated as ONE `[ai-image-zone]` composite (a two-panel
  collage baked as a single image)** — ruled OUT: the object-isolability test (`identification-tree.md` Q3)
  passes independently for each photo (flat, axis-aligned, non-overlapping, no shared scene treatment between
  them — they are two unrelated crops from the same source page, stacked by LAYOUT, not composed together by
  the photographer). Two separate bounded `<img>` slots is the correct, more editable decomposition — a future
  post can swap one crop without touching the other.
- **Considered whether "Creative Teardown" (top-left) should be fixed brand chrome instead of an editable
  slot** — resolved as an editable `TITLE` slot, not hardcoded: this is the series/content-type title, and a
  future carousel in a different series (a different "Creative Teardown"-style franchise, e.g. a different
  recurring format) would carry a different title in that exact position. Locking it to the literal string
  "Creative Teardown" would make the template unusable for any other series sharing this layout.
- **Considered whether `FOOTER_NAME`/`FOOTER_URL` should be hardcoded fixed chrome rather than slots** —
  resolved as editable slots (consistent with the `kicker-stack-body` precedent in this same pool, which slots
  its `MASTHEAD_LEFT` identity label rather than hardcoding it) so a future rebrand or handle change does not
  require editing `template.html` directly; they are not flagged `user_editable: true` (that flag is reserved
  for the genuine per-post variation axes: the two photos, the date, and the CTA label) since they rarely
  change post-to-post.
