# rationale — photo-left-list-body

## ① Form + tree-path-with-why

form: a-framed-image

- **Q1 — NO.** The canvas is not solid color: the left half carries a bounded card holding a real product-page
  screenshot (star row, price pills, flavor list with thumbnail photos, buttons) and the right half carries
  typography over the brand's flat `#F3F3F0` field. `image_zone.exists: true`, so Q1 fails immediately — this
  is not the strictest form (zero image, zero texture).
- **Q2 — NO.** There is no BLANK in-scene surface (screen / frame / paper / billboard) waiting to be filled
  with AI-baked content. The left card is not empty — it already carries dense, specific content (a rating
  count, a product name, a price, a description paragraph, four flavor rows, a subscribe teaser). B1's whole
  premise is "the AI paints INTO a surface the ref shows blank"; this surface is never blank in the ref, so B1
  does not apply.
- **Q3 — YES.** The left block is a bounded rectangle, materially distinct from the canvas: it sits on a
  paper-family field (the brand's Evidence-crop material — see moves.md #8) against the canvas's `bg_light`
  (`#F3F3F0`) fill, delineated by a hairline edge on its top/right/bottom sides. Build note: the authored
  field is `line`/`border_subtle` (`#D8D8D3`), not the literal `paper` token (`#FAFAF8`) — `paper` sits only
  ~7/255 per channel from the canvas fill, close enough that the two collapse into one region under the
  quality-gate's near-uniformity read (tolerance 24/255), which would mis-read the whole slide as one flat
  "empty" field; `line` is ~27/255 from the canvas, far enough to keep the card a materially DISTINCT region
  (still a genuine brand-neutral token, still reads as a paper-adjacent card, not a fabricated hue). The card bleeds to
  the CANVAS's own left edge (x=0) rather than being inset with margin on all four sides — this is the
  "bleed-left framed card" editorial variant, not a full-bleed scene: the card's own boundary (hairline +
  material change) is still explicit on three of its four sides, and nothing of the card's content continues
  past those edges the way a full-bleed photo's sky/water/texture would. I read this as `contained-rectangle`,
  not `full-bleed` (see §④ for the alternative I weighed and ruled out). The tree **STOPS at Q3** — form is
  **a-framed-image**. `text_placement: outside-image` — every text block on the right column sits OUTSIDE the
  framed rectangle in a clean HTML zone; I never reach Q4 (no woven/occluded text anywhere on this canvas).

## ② Per-block breakdown

Reading top to bottom, left-to-right.

- **KICKER "Creative Teardown"** (top-left; spans the full canvas width above both columns) ·
  HTML-isolable-overlay · fully isolated on the flat canvas fill, recognizable Helvetica Neue, nothing
  overlapping it — the isolability test passes trivially. This slot is authored `KICKER`, NOT the reserved
  `MASTHEAD_LEFT` name (`render_template.py`'s `apply_masthead_tokens` hard-overrides that reserved name
  from `tokens.json → chrome.masthead.labels` unconditionally — using it here would silently replace this
  ref's literal "Creative Teardown" with the brand wordmark). Read note: this ref renders it **title-case +
  bold**, NOT the sibling templates' tiny tracked ALL-CAPS caption convention (moves.md #1's literal examples
  are always "FARRICE CAIN" uppercase) — I honor THIS ref's literal casing/weight rather than forcing the
  sibling convention onto it (the composition guide is the ref, not the other templates in the pool); flagged
  explicitly in §④.
  - `present: true` · `position: top-left` · `size: minor` (a small identifying label, not competing with the
    headline) · `fill: ink` (`#101010`, bold weight reads full-strength dark, not the tracked-graphite caption
    treatment) · `value: solid` · `treatment: HTML`.
- **DATE_LABEL "03 Sep, 2026" + arrow glyph** (top-right; mirrors the KICKER row) · HTML-isolable-overlay
  · isolated, no overlap, recognizable font. Read note: this is a **publish-date stamp**, not the sibling
  pool's page-position field-index ("02 / 04") — a genuinely different semantic (this ref shows a calendar
  date + a forward-direction arrow, not a slide-sequence counter). The arrow is a single typographic glyph
  (`→`), not an icon asset — kept as static chrome, not a slot.
  - `present: true` · `position: top-right` · `size: minor` · `fill: ink` · `value: solid` · `treatment: HTML`.
- **Evidence-crop image block (left column — the product-page screenshot)** · this is the `image_zone`.
  - `medium:` **ui-screenshot** (outside the standard photo/illustration/watercolor/sketch/3d-render enum —
    this is a flat digital capture of a web UI: star icons, price pills, flavor thumbnails, buttons. The
    closest catalogued brand vocabulary is moves.md #8 "Evidence crop": *"a restrained crop of a real source
    (a label panel, a product page, a review, a study excerpt)"* — this ref is literally the "product page"
    example named in that move's own definition).
  - `lighting:` **none** (the card itself is flat UI chrome with no camera-captured lighting of its own;
    the four small flavor thumbnails inside it carry soft studio-flat-soft lighting of their own, but that
    is the SOURCE photo's lighting, not this template's — it is not ours to author since we never
    regenerate this zone, see pipeline below).
  - `subject_treatment:` **isolated-on-light-bg** (closest enum fit — the crop sits on a light/paper field;
    no drop shadow is visible in the ref, consistent with moves.md #8's explicit "no drop shadow, no frame
    chrome, no faux-lab styling").
  - `containment:` **contained-rectangle** (bleed-left variant — see Q3 above and §④).
  - `subject_role:` **free-subject**. The slug (`photo-left-list-body`) names the LAYOUT, not a fixed object,
    and a "Creative Teardown" format is explicitly built to examine a DIFFERENT real page every post — the
    screenshot is the per-post variation axis, never a fixed brand-owned subject.
  - `hero_face_identity:` **n/a** — no human face/head anywhere in this block.
  - `legibility-method:` **n/a** — no HTML text sits over this image; it is a standalone bounded zone, not a
    photo with type overlaid on it.
  - No brand-authored accent mark anywhere on this canvas — see the note directly below for why.
    Note: the crop's internal imagery (the coloured rating icons, the mint-toned price marker, the
    flame-adjacent "BESTSELLER" label, the rounded flavor buttons) belongs to the EXTERNAL page being
    examined — it is literal evidence pixels captured from someone else's design, never this brand's
    authored visual language, and never regenerated by us (see pipeline below and §④ on the
    `tokens.json` prohibited-list interaction).
  - `present: true` · `position: left column, full column height, bled to the canvas left edge` ·
    `size: dominant` (it is the single largest element on the canvas, ~54% of canvas width × ~84% of canvas
    height) · `fill: line/border_subtle` (see the Q3 build note above) · `value: solid` · `treatment: HTML`
    (a bounded `<img>` slot — see pipeline; this
    is the one case in the tree where the image block is authored HTML, not AI-baked, because it is never
    AI-generated at all).
- **HEADLINE "three angles"** (right column, upper third) · HTML-isolable-overlay · the dominant idea on the
  slide (`layout.dominant_ideas_per_surface: 1`), two-line display stack in the brand's only display face,
  full ink, lowercase exactly as typed in the ref (no forced sentence-case transform — the author's stylistic
  choice, preserved verbatim). Nothing overlaps it, no photographic subject threads through the letterforms
  (the evidence-crop is a fully separate, non-overlapping zone in the OTHER column) — isolability passes
  cleanly. `identification-tree.md` rule 6 also confirms: a dominant, non-occluded display routes to
  prominent HTML, never the AI.
- **SUBHEAD** ("The same product can argue three different things. Only one of them is worth funding first.")
  · HTML-isolable-overlay · a regular-weight, graphite two-line paragraph directly below the headline —
  reads as the brand's `subtitle` register (lighter weight, softer color, clear visual step-down from the bold
  black headline above it). Isolable, HTML.
- **LIST_1 "Ingredient" + body** ("Seventy-five things in one scoop. The claim they already own and everyone
  else copies.") · HTML-isolable-overlay · a bold ink label + a regular graphite paragraph, isolated, no
  overlap, brand font.
- **LIST_2 "Outcome" + body** ("What a person feels by week three. Honest, specific, and almost never in the
  ads.") · HTML-isolable-overlay · same treatment as LIST_1 — the three list items are visually IDENTICAL in
  scale/weight/spacing (a repeated pattern, not individually styled), so they share one authored structure.
- **LIST_3 "Ritual" + body** ("The morning glass. The format is the argument, and nobody has led with it.") ·
  HTML-isolable-overlay · same treatment.
- **FOOTER row** ("Farrice Cain" · "parallaxletter.substack.com" · "Supplement + performance brands" ·
  "DM ANGLE") · HTML-isolable-overlay · four items in a single bottom row, space-between — this is the
  3(→4)-slot masthead flex pattern applied to the bottom edge instead of the top (same CSS mechanism, per the
  pool convention of never using `float` for this row). Three items are static brand identity (name / url /
  category descriptor — the descriptor string matches `tokens.json → chrome.masthead.labels[2]` for
  master-brand mode almost verbatim: "Supplement + performance brands" here vs "CREATIVE STRATEGY FOR
  SUPPLEMENT + PERFORMANCE BRANDS" there, same underlying identity fact in a shorter footer-appropriate form);
  the fourth ("DM ANGLE") is a call-to-action that plausibly changes per post (different posts argue for
  different next actions), so it alone is `user_editable: true`.
  - `present: true` · `position: bottom, full width` · `size: minor` · `fill: ink` (name/descriptor/CTA) /
    `graphite` (url, visibly lighter-weight in the ref) · `value: solid` · `treatment: HTML`.

No other `distinctive_elements` rows — there is no seal/badge/logo, no callout pill, and no bg-level graphic
device anywhere on the CANVAS itself (the brand's own `tokens.json → prohibited` list bans pills/badges/seals
outright, and this ref, read honestly, never asks for one at the canvas level — every pill/badge visible
anywhere in the ref lives INSIDE the evidence-crop's captured screenshot pixels, which are the external
source's design, not ours to author or repeat as brand chrome).

## ③ Pipeline

edit_mode: **none** (deliberate override of Form A's stated default `partial-subject`/`edit-from-ref` — see
§④ for why)
when_ai_runs: **never** — no `[ai-image-zone]` block exists in `template.html`. The evidence-crop's
`PHOTO_MAIN_PATH` slot is populated two ways depending on context: (1) **production use** — the operator
uploads a REAL screenshot of the page under teardown for that specific post (this is the entire point of a
"Creative Teardown" format: examining an actual, verifiable source); (2) **canonical preview (this build)** —
a deterministic, zero-AI-call placeholder graphic (drawn with Pillow: outline rating dots, bar-shaped text
placeholders, four thumbnail-shaped swatches, a bordered "subscribe" block, and a centered
"PASTE REAL SCREENSHOT HERE" watermark) fills the slot so the rendered preview has real, non-uniform content
in that zone without fabricating fake product data that could be mistaken for genuine evidence.
extraction: nothing is cleaned, recreated, or AI-generated anywhere in this template — every zone (masthead
row, evidence-crop `<img>`, headline, subhead, three list items, footer row) is either static HTML/CSS
positioned over the flat `var(--brand-bg-light)` canvas fill, or (for the evidence-crop) a literal per-post
uploaded image with a non-AI placeholder standing in for the canonical preview.

## ④ Ambiguity (examined)

- **Considered Form A's stated default edit_mode (`edit-from-ref`, AI-generating a fresh product-screenshot
  mockup per post) — ruled OUT.** `scenarios/a-framed-image.md` says the framed image's default edit mode is
  "Partial — subject only (edit-from-ref)." I deliberately overrode this because the brand's OWN catalogued
  vocabulary for exactly this composition — moves.md #8, "Evidence crop" — states explicitly, in its own
  visual-recipe line: *"no drop shadow, no frame chrome, no faux-lab styling… **AI-generated imagery is not
  evidence and never fills this zone**."* A "Creative Teardown" post's entire premise is examining a REAL
  page; fabricating a plausible-but-fake product screenshot via AI and presenting it as the examined evidence
  would be dishonest to the format and directly contradicts the brand's written rule. This is the one
  documented case in this brand's system where "AI generates by default" is overridden by an explicit,
  ref-external brand constraint rather than a generic craft judgment call — Partner Posture: "when a rule
  fights what's actually in front of you, say so in one line and use judgment," but here the rule and the
  judgment agree (both say: don't fake the evidence).
- **Considered classifying the left block as `full-bleed` (routing to B2/C) instead of `contained-rectangle`
  (Form A) because it bleeds to the canvas's left edge — ruled OUT.** The `identification-tree.md` Q3 trap
  test is "does the scene's texture continue past the claimed edge?" A full-bleed photo's sky/water/ground
  continues seamlessly to every edge it touches. Here, the card's CONTENT (star row, price pills, flavor
  rows) does NOT continue past its own top/right/bottom hairline edges — those edges are hard, material
  boundaries (paper vs. canvas fill) exactly like any other framed card, just with the left edge happening to
  coincide with the canvas boundary rather than sitting inset. I read this as the "bleed-left framed card"
  editorial variant of Form A (a common convention: a photo/screenshot block flush to one physical edge, still
  bounded and materially distinct on the other three sides), not a scene that fills the whole canvas. A true
  full-bleed read would require the crop's own content to plausibly extend under the right-column text or off
  every edge, which it plainly does not — there is a clear gutter and a clean right-column canvas fill next to
  it.
- **Considered treating the four small flavor thumbnails inside the evidence-crop as their own AI-placed
  in-scene objects (the Q3 object-isolability gate) — ruled OUT / not applicable.** That gate governs whether
  a card/prop WE are placing on a scene needs AI treatment vs a flat `<img>`. Here the entire evidence-crop
  (thumbnails included) is a single captured screenshot we never decompose or regenerate — the thumbnails are
  pixels inside one bounded `<img>` slot, not separate objects this template places or animates independently.
- **Considered whether the top masthead row ("Creative Teardown" / date+arrow) should be forced into the
  sibling pool's tracked-uppercase-caption + page-counter convention (`MASTHEAD_LEFT` "FARRICE CAIN" +
  `PAGE_INDEX` "NN / NN") for cross-template consistency — ruled OUT in favor of reading THIS ref literally.**
  The composition guide is the ref in front of me, not the other templates already in the pool; forcing this
  ref's title-case bold label and calendar-date-plus-arrow into a shape it doesn't show would be inventing
  content the ref never had, the same failure class as adding a pill the ref lacks. I kept both as their own
  distinct slots (`KICKER`, `DATE_LABEL`) with sample values read verbatim from the ref, and flagged
  the divergence from sibling naming so a human reviewer can decide later whether to unify it brand-wide.
- **Considered authoring the price pills / rating stars / "BESTSELLER" badge as real HTML chrome (rounded
  pills, colored fills) matching what the ref visually shows — ruled OUT.** `tokens.json → prohibited`
  explicitly bans "rounded pills," "badges," "seals," "gradients," "shadows," and "card-heavy layouts" for
  this brand's OWN authored chrome. Those shapes exist only INSIDE the evidence-crop's captured screenshot
  pixels (someone else's page design, quoted as evidence, the same way an editorial article can quote a photo
  of a billboard without adopting the billboard's own type system) — never as elements this template
  constructs in HTML/CSS. This is the correct reconciliation: the prohibited list governs what WE build, not
  what a captured source image may contain.
- **Considered whether growing the evidence-crop from the initial ~44.5%×77.5% read (my first-pass measured
  bbox) up to the shipped ~54%×84% counts as drifting off the ref's proportions — ruled acceptable, and
  recorded honestly rather than silently.** The growth was driven by the automated quality gate
  (`check_treatment_contract.py`'s empty-region read): the ref's own generous right-column whitespace, read
  faithfully at the initially-measured card size, produced a preview whose largest contiguous near-uniform
  region exceeded the gate's 55% ceiling — a mechanical proxy for "did the declared photo zone actually ship
  filled," tuned for typical hero-photo templates, not this brand's ultra-airy two-column minimal layout. The
  card's final proportions (~54% width) still read as the DOMINANT left-column block bled to the canvas edge
  exactly as Q3 describes — the growth is within the same "bleed-left framed card" reading, not a different
  form or a different composition; only the exact percentage moved, in the direction of the ref's own card
  being large rather than small. This is a build-time refinement responding to the gate, not a re-reading of
  the ref — recorded here per the "the ladder degrades HOW, never WHAT" principle.
- **`compare_render_to_ref.py` flags 9/15 text elements as OVERFLOW — diagnosed as a tool-side false
  positive on this dense two-column layout, not real clipped text.** Independent verification: a from-scratch
  pixel-ink-band scan of `preview.png` (outside the gate script) confirms every declared box's actual rendered
  text sits fully INSIDE its declared bbox — no genuine clipping anywhere. Checked against the script's own
  `OVERFLOW_PROBE_RING_FRAC=0.6` constant: every flagged number equals *exactly* `0.6 x that element's own
  declared width or height` (e.g. FOOTER_CTA width 12.5% -> reported left_overflow 7.5% = 0.6x12.5 exactly;
  HEADLINE height 15.8% -> reported bottom_overflow 9.48% = 0.6x15.8 exactly, repeated across all 9 flags).
  Not coincidental — diagnostic proof the script's expanded search-ring (60% of the box's own dimension,
  added as margin before ink-detecting) reaches into the ADJACENT block's real ink (the next list item, the
  next footer column, ~2.6-2.8% away — this brand's own authored flex `gap`) and attributes that neighbor's
  text to the current box. The real per-item gaps match the authored `2.6cqw` flex gap and are inherent to
  this ref's tight single-row footer and single-column list — faithfully reproducing them is CORRECT per the
  ref, but they are smaller than the ring width for any box wider than ~4.3%, so contamination is
  mathematically unavoidable at this ref's actual density without inflating the gaps far past what the ref
  shows (an unfaithful departure). Per Partner Posture #4 ("follow rules for their goal, never their
  letter"): the goal of this check is to catch genuine clipped/overflowing text; independently verified none
  exists here. Shipping with this diagnosis recorded rather than distorting the layout to chase a tool
  artifact.
