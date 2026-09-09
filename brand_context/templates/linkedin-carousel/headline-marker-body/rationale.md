# rationale — headline-marker-body

## ① Form + tree-path-with-why

form: solid-css

Q1 (`bg_treatment == solid-color` AND `image_zone.exists == false`) → **yes**. Pixel-band analysis of the ref
(threshold <235 against the measured bg value 243/243/240 ≈ `#F3F3F0`) turns up exactly zero non-text/non-line
pixels outside the identified content bands (masthead, divider, headline, route diagram, footer) — no paper
grain, no gradient, no vignette, no noise field. This rules out the Q1 trap ("textured near-white ≠ solid"):
the field genuinely IS a flat CSS-fillable color, not a paper texture reading pale. It is also not a warm
photographic scene (the Q1 corollary trap) — there is no depicted content (no sky, ground, horizon, object) at
all, only typography and vector line-work on a flat field.

Because Q1 answers yes, the tree **stops here** — solid-css. I did not need to reach Q2 (no blank in-scene
surface — there is no scene), Q3 (no image at all, so no containment question applies), or Q4 (the text blocks
are NOT integrated/occluded — every block, including the route diagram, sits cleanly on the flat field with no
photographic subject and no woven overlap between blocks; each is independently isolable). This confirms
solid-css rather than falling through to B2 by default: solid-css requires TRUE zero-image, which this ref
satisfies exactly, so B2's "reserved zone over a textured background" scenario is not the right read — there is no
texture to fill.

## ② Per-block breakdown

- **Masthead-left "FARRICE CAIN"** · HTML-isolable-overlay · chrome, matches `tokens.json`
  `chrome.masthead.labels[0]`; small uppercase identity label, top-left, isolable, ordinary Helvetica Neue 700
  caps — no effects, trivially HTML. Measured band: y 5.6%–6.8%, x 7.9%–25.6% (left-aligned, inside the 84px
  safe area).

- **Masthead-right field index "03 / 04"** · HTML-isolable-overlay · chrome, matches `tokens.json`
  `chrome.field_index` (two-digit field index instead of dots — "03 / 04" is the fraction variant of that same
  functional label). Isolable, uppercase Helvetica Neue 700, tracked. Measured band: y 5.6%–6.8%, x
  85.0%–92.1% (right-aligned, inside the safe area).
  - `distinctive_elements` row: element: "field-index '03 / 04'" · present: true · position: top-right ·
    size: minor · fill: graphite (`#555553`, matches `colors.named.graphite`) · value: solid · treatment: HTML.

- **Divider hairline** · HTML-isolable-overlay · chrome, a single 1px rule directly below the masthead row
  (matches `rules.hairline_px: 1`), full measured width x 7.8%–92.1%, y ≈9.4%. Color reads as `border_subtle`
  (`#D8D8D3`). Trivial CSS `border-top` — isolable.

- **Headline (3-line bold statement)** · HTML-isolable-overlay · "The format changed. / The campaign argument /
  did not." — bold Helvetica Neue, sentence case, tight leading, left-aligned, sitting on the flat field with
  no overlap, no occlusion, no exotic font. Passes the isolability test cleanly (rip it into a clean HTML block,
  nothing lost). Measured bands: line 1 y 25.9%–31.6%, line 2 y 32.7%–38.4%, line 3 y 39.6%–44.1%, all
  left-aligned starting x 7.9%–7.96% (safe-area edge). Color: ink (`#101010`) on the light canvas — full
  contrast.
  - `distinctive_elements` row: element: "3-line bold display headline" · present: true · position: upper-mid
    (roughly y 26%–44%) · size: dominant (the largest, highest-weight text block on the canvas — the single
    "dominant idea" per `layout.dominant_ideas_per_surface: 1`) · fill: ink · value: solid · treatment: HTML.

- **Route/track diagram ("01" / "02 LEAD" / "03")** · HTML-isolable-overlay · this is the slide's distinctive
  GRAPHIC device and the mechanism the slug ("headline-marker-body") names as "marker" — three stacked
  full-width horizontal rows, each pairing a thin/bold line with a small right-aligned label and an end-of-line
  circle marker. Measured: row 1 label "01" y 61.6%–62.3% x 90.3%–91.5% (graphite, thin), row 1 line y
  63.3%–64.0% (thin hairline, full width 7.8%–92.6%, hollow circle at the right end); row 2 label "02 LEAD" y
  65.4%–66.2% x 85.6%–91.8% (ink, bold — the ONE marked row); row 2 line y 67.0%–68.0% (thick/bold, ink, solid-fill
  circle at the right end — this is the `rules.recommended_route_px: 6` "recommended route" weight and
  matches `rules.maximum_dark_interruptions_per_sequence: 1`, i.e. exactly one bold/dark row permitted per
  sequence, which is what the ref shows); row 3 label "03" y 69.3%–70.0% x 90.3%–91.7% (graphite, thin), row 3
  line y 71.0%–71.7% (thin hairline, hollow circle). This reads as the brand's `route_grammar` device
  ("route lines as decoration when no choice is compared" is prohibited by `tokens.json`, but here genuine
  choices ARE compared — the headline text itself says "the campaign argument did not [change]" and the three
  rows read as three campaign-argument options with one marked LEAD, matching the `modes.offer.primary_content`
  spec: "three campaign arguments, one lead recommendation"). Isolable — no photographic subject, no woven
  overlap between rows, pure vector line-work reproducible with CSS borders + border-radius circles.
  - `distinctive_elements` row: element: "3-row route/track diagram (01 / 02 LEAD / 03)" · present: true ·
    position: lower-third-center (y ≈61%–72%, full width) · size: medium (full canvas width but a compact
    vertical band, not canvas-dominant) · fill: mixed — graphite/border-subtle for rows 1 & 3, ink for row 2
    (the one "dark interruption") · value: solid · treatment: **HTML** (simple line + circle primitives — NOT
    a brand mark/logo, so `SVG-overlay`'s asset-resolution requirement does not apply; CSS `border-top` +
    `border-radius:50%` circles reproduce it faithfully).

- **Footer caption "A NEW HOOK IS NOT ALWAYS A NEW ANGLE"** · HTML-isolable-overlay · small uppercase tracked
  caption, bottom-left, isolable, no effects. Measured band: y 89.3%–90.4%, x 7.8%–53.4% (left-aligned, roughly
  half-width). Reads as the `type_scale.caption` role (functional label, uppercase, +0.16em tracking).
  - `distinctive_elements` row: element: "footer caption line" · present: true · position: bottom-left ·
    size: minor · fill: graphite (`#555553`) · value: solid · treatment: HTML.

**No image_zone** (`exists: false` — confirmed by the Q1 pixel-band read, no photographic or illustrated content
anywhere on the canvas). **No embedded_icons** — the masthead is text-only per `tokens.json`
`chrome.masthead.style`: "never a decorative logo"; there is no logo/badge/seal anywhere in the ref. No
`SVG-overlay` or `AI-baked` treatments apply to any element — every block on this canvas is HTML.

## ③ Pipeline

edit_mode: none
when_ai_runs: never — no `[ai-image-zone]` block. This is a pure HTML/CSS build (per `scenarios/solid-css.md`):
background is `var(--brand-bg-light)` (matches the measured `#F3F3F0`), all text and the route diagram are
HTML/CSS zones over it.
extraction: n/a — there is no generated visual to clean or extract from; every element (masthead, divider, headline,
route diagram, footer) is authored directly as HTML/CSS with the measured bboxes as its position contract.

## ④ Ambiguity (examined)

- **Considered B2 (textured bg + reserved zone) instead of solid-css.** Ruled out: B2 requires an actual
  texture/landscape background that the text floats over; this ref has no texture at all — the pixel-band read confirms a
  genuinely flat, zero-noise field. Reaching B2 here would be inventing a texture the ref doesn't have, the
  inverse of the "don't invent a reserved zone" trap. Q1 answering yes correctly stops the walk before B2 is
  ever reached.
- **Considered routing the route/track diagram to `SVG-overlay` instead of `HTML`.** Ruled out: `SVG-overlay`
  in `identification-tree.md` rule 6 is reserved for a small BRAND mark (badge/seal/logo) that the AI generator
  would drop and that needs asset-provenance resolution via `shared/icons.md`. The route diagram is not a
  brand mark — it's a generic vector diagram (lines + circles), which is licensed as an HTML/CSS primitive
  exactly like the "generic pictograms" carve-out in `shared/icons.md` ("Shape fidelity" — primitives licensed
  only for generic marks, never known brand marks; this is generic, not a known brand mark, so HTML wins).
- **Considered Form C (integrated-complex) for the route diagram**, on the theory that a marked "LEAD" row
  might be read as text woven with a graphic device (the Q4 tie-breaker rule about woven typography). Ruled
  out: nothing here overlaps or threads through anything else — each row's label sits cleanly above its own
  line, the bold row is not overlapping the thin rows, and no photographic subject or knockout effect is
  present anywhere. This is the "clean over the field" branch of the Q4 tie-breaker, not the "woven" branch —
  isolable, stays HTML.
- **Considered whether the top-right "03 / 04" is `chrome.pagination`** (which `tokens.json` sets to `null`,
  i.e. disabled) rather than `chrome.field_index` (which IS configured, with examples like "02" and the note
  "page numbers as a two-digit field index instead of dots"). Read it as `field_index`: the ref's mark is
  typographic text ("03 / 04"), not a dot/pill pagination indicator, so it follows the enabled `field_index`
  chrome rule rather than the disabled `pagination` rule — authored, not skipped.
- **No AI ambiguity to weigh** — with `image_zone.exists: false` there is no medium/lighting/subject_treatment/
  subject_role, face-identity, or legibility-method judgment call to make; the entire pipeline is `edit_mode:
  none`.
