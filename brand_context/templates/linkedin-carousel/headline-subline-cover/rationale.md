# rationale — headline-subline-cover

## ① Form + tree-path-with-why

form: solid-css

Q1 — bg_treatment is `solid-color`: the entire 1080×1350 canvas is one flat fill, `#F3F3F0`, matching
`tokens.json → colors.bg_light` (`named.canvas`) exactly. Zero texture — no paper grain, no vignette, no
noise, no gradient corner-darkening. `image_zone.exists == false` — there is no photo, illustration, or any
non-vector imagery anywhere on the canvas; every mark on the slide is vector type or a hairline/rule. Both Q1
conditions are satisfied → **Q1 yes → STOP at solid-css.** The tree does not proceed to Q2 (no in-scene
surface exists to hold content — there is no "scene" at all), Q3 (no image, so no containment question), or
Q4 (every text block sits cleanly on the flat field with nothing occluding it — see §2, all pass the
isolability test) — the walk correctly terminates at the first match.

## ② Per-block breakdown

- **Masthead-left "FARRICE CAIN"** · HTML-isolable-overlay · small uppercase brand label, flat on solid bg,
  no effects, standard tracked caps — passes isolability trivially. Governed by `tokens.json →
  chrome.masthead.labels[0]`, not a content block (chrome).
- **Masthead-right "01 / 04"** · HTML-isolable-overlay · this is the **field-index** chrome move (#2 in
  `moves.md`), NOT the disabled `chrome.pagination` (`tokens.json → chrome.pagination: null`) and NOT
  `chrome.masthead`'s right slot (which in master-brand mode carries the descriptor line, absent here). It is
  the two-digit `NN / NN` counter pattern `tokens.json → chrome.field_index` describes, positioned in the
  masthead row. Isolable, flat text, no effects.
- **Top hairline rule** (below the masthead) · HTML-isolable-overlay · a 1px `border_subtle`/`line`
  (`#D8D8D3`) horizontal rule — the quiet weight of the "decision line" move (#3). Simple CSS border, no
  scene to integrate with.
  - `distinctive_elements` row: `element: "top hairline rule"` · `present: true` · `position: top (~11%
    down, directly under the masthead)` · `size: minor` · `fill: line (#D8D8D3)` · `value: solid` ·
    `treatment: HTML`
- **Headline "Another creative round / is easy to approve."** · HTML-isolable-overlay · h1-scale (~72px
  token), Helvetica Neue 700, sentence case, tight leading (~1.0–1.05), full ink black (`#101010`), two lines,
  flush-left, generous line gap. Sits on the flat field with nothing behind or through it — no occlusion, no
  woven pill, no exotic font (Helvetica Neue is the brand's one recognized display face) → isolability test
  passes cleanly → **HTML**.
- **Subtitle "Choosing one argument / is harder to own."** · HTML-isolable-overlay · subtitle-scale (~36px
  token), Helvetica Neue 400, graphite (`#555553`), two lines, flush-left directly under the headline with a
  visible gap. Same isolability read as the headline — flat, unoccluded, brand font → **HTML**.
- **Bottom structural rule** (above the caption) · HTML-isolable-overlay · a heavier, darker horizontal rule
  than the top hairline — reads as the `structural_px`/heavier weight of the "decision line" move (#3), full
  content-width, ink-colored. Simple CSS border/div, isolable.
  - `distinctive_elements` row: `element: "bottom structural rule"` · `present: true` · `position:
    lower-third (~85% down, directly above the footer caption)` · `size: minor` (a thin full-width line, not
    a block/field) · `fill: ink (#101010)` · `value: solid` · `treatment: HTML`
- **Footer caption "THE DECISION BEFORE THE CREATIVE"** · HTML-isolable-overlay · caption-scale (~22px
  token), uppercase, +0.16em tracking, weight 700, graphite/stone tone, flush-left below the bottom rule. This
  is genuine per-slide content (the thematic kicker line for THIS carousel, not reusable chrome) — inventoried
  as its own text slot, not folded into chrome. Flat, isolable → **HTML**.

No image block, no seal/badge/logo, no callout pill, no display word — `image_zone.exists: false`,
`embedded_icons: []`. There is nothing in this ref that requires AI generation.

## ③ Pipeline

edit_mode: none
when_ai_runs: never — no `[ai-image-zone]` block. Background is `var(--brand-bg-light)` via CSS, exactly
matching the ref's flat fill; asking the AI for a flat color fill would be more expensive and less exact than
the CSS token.
extraction: nothing to extract or clean. All eight blocks above (masthead-left, masthead-right/field-index,
top hairline, headline, subtitle, bottom rule, footer caption) become HTML text/CSS zones over the solid CSS
background — no AI zones exist on this slide.

## ④ Ambiguity (examined)

- **Considered B2 (the on-reserved-zone scenario — full-bleed texture/landscape background with text on a
  reserved clean band).** Ruled out: B2 requires an actual full-bleed texture
  or landscape bg with a text block floating on a reserved clean band WITHIN that texture. This ref has no
  texture whatsoever — the fill is a single flat hex matching the brand's own `bg_light` token exactly, with
  no grain, gradient, or noise anywhere. There is nothing to "reserve a zone" within; the whole canvas is
  already the reserved zone. Q1 fires first and correctly, so B2 is never reached.
- **Considered C (`c-integrated-text`, integrated-complex).** Ruled out: the isolability test on every text
  block (headline, subtitle, both rules, both masthead slots, footer caption) passes cleanly — none is
  occluded by a subject (there is no subject), none is woven through another element (no callout pill
  overlapping the headline, no highlight knockout, no tilted label crossing the type). Every block can be
  ripped out and dropped into clean HTML without losing the look.
- **Considered whether the bottom rule + footer caption invoke the "dark recommendation" move (#6, an ink
  FIELD with paper text, max 1 per sequence).** Ruled out: move #6 is a full inversion — a solid dark
  background field with light text on it. What's present here is a thin ink-colored RULE (a line, not a
  solid ink field) separating the body from a caption, still on the light `bg_light` canvas throughout. This is
  the "decision line" move (#3) at its heavier weight, not move #6's dark-field inversion — no dark
  interruption is used on this slide at all, so `rules.maximum_dark_interruptions_per_sequence = 1` is
  trivially respected (zero used here).
- **Considered whether "01 / 04" is `chrome.pagination`.** Ruled out explicitly: `tokens.json` sets
  `chrome.pagination: null` (disabled) — the rule "honor tokens.json chrome.* even if the ref shows it" means
  a dots-style pagination indicator would NOT be injected. But "01 / 04" is not a dots indicator; it matches
  the separately-defined, ENABLED `chrome.field_index` pattern (examples `"02"`, `"FIELD / 01"`) exactly, so
  it is honored under that key instead of being dropped.
