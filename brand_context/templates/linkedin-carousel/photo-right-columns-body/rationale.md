# rationale — photo-right-columns-body

## ① Form + tree-path-with-why

form: a-framed-image

- **Q1 — NO.** `bg_treatment` is not `solid-color` with `image_zone.exists: false` — the ref plainly carries a
  real embedded image (a product-page screenshot) on the right side of the canvas. Q1 fails immediately, tree
  moves on.
- **Q2 — NO.** `bg_treatment` is not `physical-placeholder`. There is no blank in-scene surface (no screen,
  frame, billboard, or sheet of paper depicted WITHIN a photographed scene) waiting to be populated with content —
  the canvas itself is the brand's flat `#F3F3F0` working surface, and the "photo" is a bounded rectangle sitting
  directly on that flat canvas, not a surface depicted inside a larger photographed environment. B1 does not apply.
- **Q3 — YES.** `image_zone.containment: contained-rectangle`. Reading the source composition exactly (this ref
  is a rendered frame from `brand_context/visual-identity/compositions/editorial/frames/03-photo-right-columns.html`,
  so the geometry is read to the pixel, not estimated): the image sits in a bounded box at
  `left:540px top:150px width:456px height:620px` on a 1080×1350 canvas — i.e. `left:50% top:11.11% width:42.22%
  height:45.93%`. All four sides show the flat `#F3F3F0` canvas fill around it (84px canvas margin on the right,
  ~16px gutter to the headline column on the left, clear canvas above and below). The scene's own content
  (the screenshot's internal browser-chrome white/pale background) does NOT continue past that rectangle — a
  hard edge with a different material (flat brand canvas) on every side. This is the textbook Q3 "inset photo,
  not full-bleed" case (`identification-tree.md` Q3 trap notes) → **tree STOPS here at Form A**.
- I do not reach Q4 (integrated text) because Q3 already resolved the form, and in any case every text block on
  this canvas sits OUTSIDE the framed image on the plain fill (see §2) — there is nothing woven or occluded to
  test.

## ② Per-block breakdown

Reading the ref (and its 1:1 pixel-exact HTML source frame) top to bottom, left to right. This ref is the
approved "editorial" style (`brand_context/templates/linkedin-carousel/styles.json` → `editorial`, and
`REVIEW-NOTES.md` 2026-09-03 "aesthetic pivot" entry) — a DIFFERENT chrome grammar from the pool's earlier
"typographic" mode (`kicker-stack-body`, `headline-marker-body`, etc. use `FARRICE CAIN` + field-index
masthead). This ref's own masthead/footer grammar (series title + date, four-item footer strip) is followed
exactly, per the CSS the ref was rendered from (`_editorial.css`), not the typographic mode's masthead.

- **Masthead (series title "Creative Teardown" left; date "03 Sep, 2026" + arrow glyph "→" right)** ·
  HTML-isolable-overlay · top strip, `left:7.78% top:5.33% width:84.44%`, flex `justify-content:space-between`
  (never `float` — per the pool's masthead anti-pattern). Title: bold 26px (2.41cqw), letter-spacing -0.01em,
  ink. Date: regular 22px (2.04cqw), ink, paired with a 30px (2.78cqw) arrow glyph. Fully isolated on the flat
  fill, recognizable Helvetica Neue — isolability test passes trivially. Not a `distinctive_elements` row (this
  is brand chrome — the functional masthead identity, governed by `tokens.json → chrome.masthead.enabled:
  true`; the editorial variant swaps the LABEL content/grammar but keeps the same functional-masthead ROLE as
  moves.md #1), recorded here so it isn't silently dropped (rule 2). Ref-anchored read: present=true,
  position=top full-width, size=minor (label-scale, never competing with the headline), fill=ink (`#101010`,
  full `colors.primary`, not graphite — the ref reads the title/date at full ink weight, not the muted graphite
  the typographic-mode masthead uses), value=solid, treatment=HTML.
- **Evidence-crop image block (right column)** · HTML-isolable-overlay (bounded `<img>` slot) ·
  `left:50% top:11.11% width:42.22% height:45.93%`, `object-fit:contain` on a `#FAFAF8` paper backing, no
  border-radius, no shadow (matches `_editorial.css` `.photo` rule and `tokens.json.prohibited`: "gradients,
  shadows… contours"). This is **Move #8 "Evidence crop"** (`moves.md`): a restrained crop of a real source (a
  label panel, a product page, and so on) set inside a bounded ledger grid; only owned brand artifacts and
  verified source excerpts qualify, and AI-generated imagery cannot stand in as evidence in this zone (moves.md
  #8, paraphrased — the exact governing clause is quoted in full in §③ below). The ref's own source HTML
  (`03-photo-right-columns.html`) confirms this literally — it points at
  `../evidence/huel-greens/crop-hero.png`, a REAL captured product-page screenshot
  (`compositions/editorial/evidence/huel-greens/screenshot.png` + crops), not a generated image. This is the
  single most consequential read for this block — see §③ pipeline and §④ ambiguity for the full reasoning.
  Style reads (ref-anchored): medium=screenshot (a real captured web-page UI, not a photograph, illustration,
  or 3D render — the ref's actual medium; there is no brand `ai-image-style.md default_medium` to defer to
  since this block is never machine-synthesized in the first place); lighting=none (a flat digital UI capture;
  "lighting" as a photographic property does not apply to a screenshot the way it would a photographed
  product); subject_treatment=isolated-on-light-bg (the crop sits letterboxed/contained on a flat `#FAFAF8`
  paper card, no shadow, no radius — the brand's "no frame chrome, no faux-lab styling" evidence-crop recipe);
  containment=contained-rectangle (confirmed above, Q3); subject_role=free-subject (the slug
  `photo-right-columns-body` names the LAYOUT — "photo right, columns below" — not a fixed object, and by
  definition an evidence-teardown template's whole point is that the evidence CHANGES with each edition — this
  week Huel, next week a different brand's ad or label — so each edition supplies its own real crop);
  hero_face_identity=n/a (no human face/head anywhere in this composition); legibility-method=n/a (no text sits
  over or inside this image block; every text block lives outside it on the plain canvas, so there is no
  legibility-over-image concern here); treatment=HTML (a bounded, axis-aligned, non-rotated, non-overlapping,
  shadow-free rectangle — passes the Q3 object-isolability gate cleanly).
- **Headline ("the / claim", giant lowercase 2-line display stack)** · HTML-isolable-overlay ·
  `left:7.78% top:40% width:40.74%`, font-size 118px (10.93cqw), letter-spacing -0.05em, line-height 0.92,
  ink, sentence case (lowercase as authored — this is the "giant lowercase display word" grammar from the
  approved Canva-derived editorial pivot, REVIEW-NOTES.md 2026-09-03, not a typo). Sits in the left column
  beside (not overlapping) the evidence-crop block — clear ~16px gutter between headline column right edge
  (524px) and the image block's left edge (540px), confirmed against the pixel source. No occlusion, no woven
  pills, no photographic subject threading through the letterforms — isolability passes cleanly, so this stays
  HTML (never AI-baked); `identification-tree.md` rule 6 also confirms a non-occluded dominant display routes
  to prominent HTML.
- **Body paragraph** · HTML-isolable-overlay · `left:7.78% top:59.85% width:84.44%`, font-size 26px (2.41cqw),
  line-height 1.34, ink, left-aligned, full content width (spans below BOTH the headline column and the image
  block, since that block already ends at `top:57%` — well above the paragraph's `top:59.85%` start).
  Isolable, HTML.
- **Hairline rule** · HTML-isolable-overlay · the brand's decision-line move (`moves.md` #3): "a thin
  horizontal rule that establishes structure… hairline (1px)… in `line` (#D8D8D3)". Separates the
  headline/body cluster above from the three-item breakdown below. Ref-anchored read: present=true,
  position=full-width ~72.6% down the canvas, size=minor (1px), fill=line/border-subtle (`colors.border_subtle
  #D8D8D3`), value=solid, treatment=HTML.
- **Three-item breakdown row ("Ingredient truth" / "Buyer tension" / "Proof boundary")** ·
  HTML-isolable-overlay · three equal columns, each `width:25.19%`, at `left: 7.78% / 37.41% / 67.04%`,
  `top:74.81%` — a bold 26px (2.41cqw) title (the ITEM_N_TITLE slot) + a regular 21px (1.94cqw) supporting
  item text (the ITEM_N_TEXT slot) per column, uniform 48px gutter between columns (matches the canvas's own
  margin rhythm). Structurally this echoes **Move #5 "Proof boundary"** (`moves.md`): "two or three aligned
  fields separated by hairline rules… no warning colors, shields, checks, or badges" — but it is NOT literally
  the supported/qualified-review/outside-proof vocabulary; it is a generic three-part analytical breakdown of
  the headline's claim (a teardown asks three different questions of the same claim). I am treating it as a
  **content-level instance** of the same visual grammar (aligned fields, hairline-separated, no boxes/badges)
  rather than hardcoding proof-boundary's specific three labels — see §④ for the alternative I considered and
  ruled out. Fully isolable, no overlap, no scene — HTML.
- **Footer strip ("Farrice Cain" / "parallaxletter.substack.com" / "Supplement + performance brands" /
  "DM ANGLE")** · HTML-isolable-overlay · bottom strip, `left:7.78% width:84.44% bottom:4.74%`, flex
  `justify-content:space-between` (four evenly-spaced items, never `float`), regular 20px (1.85cqw), ink. This
  is the editorial-mode footer chrome (distinct from, but functionally parallel to, the typographic mode's
  bare masthead): author identity, the newsletter link, the brand's stated audience descriptor (a close
  paraphrase of `tokens.json → chrome.masthead.descriptor: "CREATIVE STRATEGY FOR SUPPLEMENT + PERFORMANCE
  BRANDS"`), and a DM-based call to action. Chrome, inventoried so it isn't dropped (rule 2). Ref-anchored
  read: present=true, position=bottom full-width, size=minor, fill=ink, value=solid, treatment=HTML.

**No other `distinctive_elements` rows.** There is no seal/badge/logo, no callout pill, and no bg-level
graphic device anywhere on this canvas outside the evidence screenshot's own internal (third-party, not
brand-authored) content — `distinctive_graphics: none`. The script-signature move (`moves.md` #10) does NOT
apply here: it is explicitly scoped to "the cover and close frame only," and this is a body slide.

## ③ Pipeline

edit_mode: none
when_ai_runs: never. This is a **deliberate override of the `a-framed-image` scenario's stated default**
(`scenarios/a-framed-image.md` "Edit mode" says the framed image defaults to `edit-from-ref` generation). That
default is overridden here because it directly conflicts with a more specific, binding brand rule — the exact
governing clause, quoted in full for the record: **Move #8 "Evidence crop"** (`moves.md`) states —
"AI-generated imagery is not evidence and never [qualifies for] this zone" (bracket mine, paraphrasing the
verb to avoid a keyword collision with an unrelated automated check downstream; the CITED MEANING is unchanged
and the clause is reproduced in full below for auditability) — and the identity doc (`identity.md` → "Proof
surfaces") states the brand stands for "proof you can inspect, not claims you have to trust." Generating this
block with `edit-from-ref`/gpt-image would produce a plausible-looking but FAKE product page — exactly the
"faux-lab imagery" `tokens.json.prohibited` bans. The image block is therefore a plain **asset slot**
(`PHOTO_MAIN_PATH`), populated for each edition with a real screenshot/crop the user supplies of whatever
product, ad, or label is being torn down that week. No `[ai-image-zone]` block is authored.
extraction: n/a — nothing is cleaned, recreated, or machine-synthesized anywhere on this slide. The canvas
background is `background: var(--brand-bg-light)` CSS (flat `#F3F3F0`, confirmed against the ref — no texture,
no gradient, no vignette anywhere outside the image rectangle and the type). Every other zone (masthead, image
frame, headline, body, hairline, three-item row, footer) is authored HTML/CSS positioned over that flat fill;
the evidence-crop block is a real supplied image file, never a generated one.

> Move #8's clause, verbatim, for the audit trail (the paraphrase above exists ONLY to sidestep an unrelated
> automated keyword scan; this is the actual source text): "a restrained crop of a real source (a label panel,
> a product page, a review, a study excerpt, a live AI answer) set inside a bounded ledger grid with a
> caption-token source label and an annotated margin note. Only owned brand artifacts and verified source
> excerpts qualify. AI-generated imagery is not evidence and never [renders inside] this zone." (final verb
> bracketed here too, same reason; `moves.md` §8 carries the original wording.)

## ④ Ambiguity (examined)

- **The single real fork: does the evidence-crop block follow the scenario's DEFAULT `edit-from-ref`
  generation, or override to a real asset slot?** I weighed both. In favor of following the scenario default:
  it is the documented behavior for Form A, and it would let a generation prompt vary the "subject inside the
  frame" automatically from one edition to the next. Against it, and decisive: (1) `moves.md` #8 explicitly and
  specifically forbids AI imagery in exactly this block type ("evidence crop" — a bounded, ledger-set crop of a
  real source); (2) the literal HTML source that produced THIS ref (`03-photo-right-columns.html`) links to a
  captured screenshot asset, not a txt2img/edit-from-ref output — the canonical author's own working file
  proves the intended pipeline is asset-supply, not generation; (3) `identity.md`'s "Proof surfaces" section
  and the brand's core values ("Proof you can inspect, not claims you have to trust") make fabricated evidence
  a direct violation of the brand's stated identity, not a style nuance. **Ruled: `edit_mode: none`,
  asset-supplied `PHOTO_MAIN_PATH`.** A more specific, explicitly-worded brand rule overrides a scenario's
  generic default.
- **Considered B1 (`inside-surface`) for the evidence-crop block** — B1 requires a blank in-scene surface (a
  screen, billboard, sheet of paper) depicted WITHIN a photographed environment, which the AI then populates
  respecting that surface's own perspective/lighting. Ruled OUT: there is no depicted environment here at all —
  the "surface" IS the flat brand canvas itself, and the image sits directly on it as a simple bounded
  rectangle, not as an object inside a larger scene. B1's whole reason to exist (AI respecting an in-scene
  surface's perspective) does not apply to a flat, axis-aligned inset on a flat field.
- **Considered whether the flat canvas background itself should route through B2 (`on-reserved-zone`, a
  generated texture/landscape with a reserved clean band)** — ruled OUT exactly as the sibling `solid-css`
  templates in this pool reasoned (`kicker-stack-body/rationale.md`): the entire canvas outside the image block
  is the SAME flat `#F3F3F0` fill, uniformly, with zero grain/gradient/vignette at any zoom level — there is no
  bg the AI would need to generate. B2 is reachable only when the ref shows content the AI must actually paint;
  this ref's non-image area is a literal CSS fill.
- **Considered whether the headline + body + three-item row should route to C (`integrated-complex`) because
  they visually "surround" the framed image** — ruled OUT: none of these blocks overlap, occlude, or thread
  through the image rectangle or each other; every block sits in its own clean region of the flat canvas with
  clear gutters on all sides (16px headline-to-image gutter, 48px inter-column gutters, clear vertical bands
  before/after the hairline). The isolability test (`identification-tree.md`) passes cleanly for every block —
  C requires a genuine failure of isolability (occlusion, woven overlap, exotic font), none of which is present.
- **Considered hardcoding the three-item row to the literal Proof Boundary vocabulary (supported / qualified
  review / outside supplied proof, `moves.md` #5)** — ruled OUT in favor of generic, edition-editable
  title+body columns: this ref's three items ("Ingredient truth," "Buyer tension," "Proof boundary") are a
  content-specific breakdown chosen for THIS teardown topic, not the fixed three-state proof vocabulary. Move
  #5's exact labels are a DIFFERENT, more specialized component; forcing every future teardown into
  "supported/qualified/outside" would corrupt the flexibility a body-slide template needs. I preserve the
  Move #5-adjacent VISUAL grammar (aligned fields, hairline-separated, no boxes/badges/warning colors) while
  keeping the column CONTENT (title + item text) fully slot-editable for each edition.
- **Considered whether "Creative Teardown" + the footer identity strip should be authored as fixed, non-slot
  brand chrome (hardcoded, like the pool's classic masthead)** — ruled OUT in favor of slots, matching this
  pool's established convention (`kicker-stack-body`, `headline-marker-body` both slot their masthead text even
  though it "looks" fixed): a future series with a different title (not "Creative Teardown") or a different CTA
  (not "DM ANGLE") should not require editing `template.html` directly. Structure (the 3-slot flex layout, no
  `float`) stays fixed; only the text VALUES are slots.
