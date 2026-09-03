# rationale — kicker-stack-body

## ① Form + tree-path-with-why

form: solid-css

- **Q1 — YES.** `bg_treatment: solid-color`. Eyedropper-read across the ref (top-left corner, center, bottom
  edge) returns the same flat `#F3F3F0`-family off-white — zero grain, zero gradient, zero vignette, zero
  fading at the edges. This is exactly the canvas token (`tokens.json → colors.bg_light = "#F3F3F0"`, named
  `canvas`), which is the Premium Minimal system's literal paper-flat working surface — not a photographed or
  scanned paper (no dust, no fibre, no directional noise at any zoom level I can read). `image_zone.exists:
  false` — there is no photo, illustration, scene, or in-scene surface anywhere on the canvas; every mark on
  the slide is typography or a 1px rule. Both Q1 conditions hold, so the tree **STOPS at Q1** — solid-css is
  the first and only match; I never reach Q2 (no in-scene surface exists to ask about), Q3 (no image zone to
  test containment on), or Q4 (no scene to test integration against).
- Confirms against the Q1 trap notes: this is not a "textured near-white" false-solid (no paper grain, no
  scan artifacts, no corner gradient) and not a "warm-tone read as paper" trap (the fill is genuinely flat,
  not a photographed material) — it is a literal flat digital fill, the strictest form of solid-color.

## ② Per-block breakdown

Reading the ref top to bottom. Every block is `isolable: true` — nothing overlaps, nothing rides an object,
nothing needs perspective/occlusion/relief. There is no scene to integrate with, so every block routes to
plain HTML on the flat fill (the solid-css default per `scenarios/solid-css.md`).

- **Masthead-left "FARRICE CAIN"** · HTML-isolable-overlay · top-left, small caps, tracked — the brand's
  functional masthead move (`moves.md` #1: "a small uppercase identity label… never a decorative logo"). Not a
  distinctive element (it is brand chrome governed by `tokens.json → chrome.masthead`), so no `distinctive_elements`
  row — recorded here so the block isn't silently dropped (rule 2).
  - `present: true` · `position: top-left` · `size: minor` (small caption-scale label, not competing with the
    headline) · `fill: graphite` (moves.md #1 states the masthead label renders in `graphite`, i.e.
    `colors.secondary #555553`, even though at 700-weight/22px it visually reads close to dark) ·
    `value: solid` · `treatment: HTML`.
- **Field index "02 / 04" (top-right)** · HTML-isolable-overlay · the brand's field-index move (`moves.md` #2:
  "a two-digit index… in place of carousel dots"). Chrome, not a distinctive element. `chrome.pagination` is
  `null` in tokens.json (classic dot pagination disabled) but `chrome.field_index` is a live, separately
  declared chrome vocabulary item with its own example set (`["FIELD / 01", "NOTE / 02", "02"]`) — this ref's
  `"02 / 04"` is exactly that label-scale field-index format, so it is authored as chrome, not suppressed by
  the pagination-disabled flag (that flag governs dots, not the field index).
  - `present: true` · `position: top-right` · `size: minor` · `fill: graphite/stone` (label scale =
    `colors.secondary`; ref reads a small tracked numeral pairing, consistent with the caption token) ·
    `value: solid` · `treatment: HTML`.
- **Hairline rule (below masthead)** · HTML-isolable-overlay · the brand's decision-line move (`moves.md` #3:
  "a thin horizontal rule that establishes structure… hairline (1px)… in `line` (#D8D8D3)"). Structural, not
  content, but inventoried so it isn't dropped (rule 2 — every ref block gets a row).
  - `present: true` · `position: full-width, ~11% down the canvas, directly under the masthead row` ·
    `size: minor` (1px hairline) · `fill: line/border-subtle` (token `colors.border_subtle #D8D8D3`, named
    `line`) · `value: solid` (a crisp, non-faded hairline — not ghosted) · `treatment: HTML`.
- **Kicker 1 "SO THE TEAM ASKS FOR"** · HTML-isolable-overlay · a small tracked uppercase caption-scale label
  introducing the headline block (`type_scale.caption`: 22px, uppercase, +0.16em tracking, 700-weight,
  `colors.text_muted`/graphite). Fully isolated on the flat fill — the isolability test passes trivially
  (nothing to overlap, recognizable brand font).
- **Headline stack "More UGC. / More statics. / Another creator."** · HTML-isolable-overlay · the slide's one
  dominant idea (`layout.dominant_ideas_per_surface: 1`) — three short, escalating, sentence-case display
  lines in the brand's only display face (Helvetica Neue 700, tight tracking, close leading), full ink
  (`colors.text_on_light #101010`). This is the largest, heaviest element on the canvas and clearly the
  slide's headline. No occlusion, no woven pills, no photographic subject anywhere — the isolability test
  passes cleanly, so this stays HTML (never AI-baked); `identification-tree.md` rule 6 also confirms a
  "dominant display NOT occluded" routes to prominent HTML, never the AI.
- **Hairline rule (above "WHAT STAYED THE SAME")** · HTML-isolable-overlay · same decision-line move as above,
  now separating the escalation headline cluster from the closing statement cluster.
  - `present: true` · `position: full-width, ~69% down the canvas` · `size: minor` · `fill: line/border-subtle`
    · `value: solid` · `treatment: HTML`.
- **Kicker 2 "WHAT STAYED THE SAME"** · HTML-isolable-overlay · a second caption-scale label, the same visual
  role/style as Kicker 1, introducing the closing statement. Isolable, HTML.
- **Statement "The familiar category claim."** · HTML-isolable-overlay · a single sentence in a lighter,
  regular (non-bold) weight and a visibly softer gray than the headline ink — reads as the brand's `subtitle`
  token (36px, 1.3 line-height, `colors.secondary` graphite, NOT the bold display weight used above). It is
  the deliberate visual contrast to the bold headline block: the headline escalates (bold, black, 3 lines),
  the statement stays flat/unchanged (regular weight, graphite, 1 line) — a typographic argument, not just
  decoration. Isolable, HTML.

No `distinctive_elements` rows beyond the two hairline rules recorded above — there is no display word, no
seal/badge/logo, no callout pill, and no bg-level graphic device anywhere on this canvas. `image_zone`:
`exists: false` throughout, so none of the image-block STYLE reads (`medium` / `lighting` /
`subject_treatment` / `containment` / `subject_role` / `hero_face_identity` / `legibility-method`) apply — this
slide carries zero pixels of generated or photographic imagery.

## ③ Pipeline

edit_mode: none
when_ai_runs: never — no `[ai-image-zone]` block; no cutout subject is present over the solid either (no
subject at all), so the cutout-on-solid corollary in `scenarios/solid-css.md` does not apply.
extraction: n/a — nothing is cleaned or recreated. The background is `background: var(--brand-bg-light)` CSS,
period. Every zone (masthead, field index, two hairlines, two kickers, the headline stack, the closing
statement) is authored HTML/CSS positioned over that flat fill; no zone becomes an AI image.

## ④ Ambiguity (examined)

- **Considered B2 (`on-reserved-zone`) instead of solid-css** — B2 requires a *generated bg* (a full texture or
  landscape) with text floating on a reserved clean band within it. There is no generated texture here at all;
  the entire canvas IS the reserved band, uniformly, edge to edge. Ruled OUT: B2 is reachable only when the ref
  actually shows a bg the AI would need to generate (texture, landscape, scene); this ref has none — routing it
  to B2 would spend a generation call on a flat fill that CSS reproduces exactly and for free (the `solid-color`
  branch of the Background-route decision table explicitly exists for this case).
- **Considered whether the two hairline rules + field index constitute enough "structure" to push this toward
  a more complex form (e.g. treating the rule-divided sections as pseudo-"surfaces")** — ruled OUT: a hairline
  rule is a CSS border, not a physical in-scene surface (no screen/frame/paper/billboard exists in the ref for
  Q2's B1 test), and it carries no content of its own (it is decoration/structure, not a blank holder for
  text). B1 requires a genuine blank surface INSIDE a scene; there is no scene.
  the tree Q1 STOPS on solid-color + no image, before Q2–Q4 are ever asked.
- **Considered whether the headline's three escalating lines and the closing statement's contrasting weight
  might require AI-baked "integrated" text (Form C)** — ruled OUT: nothing overlaps the headline, no
  photographic subject or scene threads through the letterforms, and the font is the brand's own recognizable
  Helvetica Neue. The isolability test passes cleanly for every block; C is reserved for text that fails
  isolability (woven pills, subject occlusion, exotic fonts), none of which occurs here.
- **Considered whether the field-index value "02 / 04" should be a fixed chrome constant vs. a per-post
  variable slot** — resolved as `user_editable: true`: in a real carousel this value changes on every slide
  (it is the slide's position inside the sequence), so hardcoding it would ship every rendered slide reading
  "02 / 04" regardless of actual position. This is the correct per-post variation axis for THIS template (there
  is no photo/image variation axis — this is a pure-typography body slide), not an oversight of the "one
  variation axis is usually the image subject" default.
