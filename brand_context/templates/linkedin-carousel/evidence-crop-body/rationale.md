# rationale — evidence-crop-body

## ① Form + tree-path-with-why

form: a-framed-image

- **Q1 — NO.** `bg_treatment` is not solid-color for the whole canvas — an image (the evidence crop) exists
  on it (`image_zone.exists: true`). Even though the CANVAS fill outside the crop is the flat brand paper/canvas
  color (`#F3F3F0`-family, zero texture at any zoom I can read), Q1 requires `image_zone.exists == false`, and
  it is `true` here. Q1 fails on the second condition alone — move to Q2.
- **Q2 — NO.** `bg_treatment` is not `physical-placeholder`. The evidence crop is not a BLANK in-scene surface
  (no screen/billboard/frame sitting empty inside a larger depicted scene, waiting for content) — it is a
  bounded rectangle on the flat canvas that already HOLDS a real, fully-rendered source capture (a webpage
  screenshot: star rating, product name, price pills, description paragraph). There is no scene around it for
  the rectangle to be "inside" — the rectangle sits directly on the flat paper/canvas fill, framed by two
  hairline rules. This is the Q2 trap in reverse: a rectangle that already CARRIES content is not a blank
  physical placeholder, so Q2 answers no — move to Q3.
- **Q3 — YES.** `image_zone.containment: contained-rectangle`. The evidence crop is a hard-edged rectangle
  (measured against the source frame markup: `left:84px; top:151px; width:912px; height:560px` on a 1080×1350
  canvas) sitting on a DIFFERENT material — the flat brand paper (`#FAFAF8`) inside the flat canvas
  (`#F3F3F0`) — bounded top and bottom by 1px hairline rules (`#D8D8D3`). The crop's own texture (a white
  webpage screenshot with green stars, black type, a mint price-pill) does NOT continue past its edges — outside
  the rectangle is uniform flat paper/canvas, on all sides. This passes the Q3 hard-edge test cleanly (not the
  "calm zone of a full-bleed scene" trap — there is no scene, the crop is a discrete inset object). The tree
  **STOPS at Q3 — form is A (framed image)**. I never reach Q4 (Q3 already matched) or the B2 fallthrough.
- Confirms against the Q3 object-isolability corollary: the crop is flat, axis-aligned, non-overlapping, no
  rotation, no cast shadow, no perspective — it earns a genuine bounded `<img>` slot, not an AI-placed in-scene
  object treatment.

## ② Per-block breakdown

Reading the ref top to bottom. This ref is a rendered HTML reference frame authored by Farrice's own editorial
system (`brand_context/visual-identity/compositions/editorial/frames/06-evidence-crop.html`, styled by
`_editorial.css`) — the exact source markup, CSS, and even the real evidence asset it uses
(`compositions/editorial/evidence/huel-greens/crop-claim.png`, a genuine Playwright capture of
`huel.com/products/huel-daily-greens`, see that folder's `manifest.json`) are on disk. I read the ref pixels
AND cross-checked every position/color/size claim below against that source markup — this is a stronger-than-
usual read (no measurement guesswork), but every field below is still what the REF shows, not an assumption.

- **Masthead row "Creative Teardown" (left) + "03 Sep, 2026 →" (right)** · HTML-isolable-overlay · a two-slot
  flex row at the very top (`top:72px` = 5.3% down), left = the content-series title (bold 700, 26px/2.41cqw,
  −0.01em tracking, ink `#101010`), right = the post date + a small directional arrow glyph (regular 400,
  22px/2.04cqw date; 30px/2.78cqw arrow), both ink, `display:flex; justify-content:space-between;
  align-items:baseline`. Nothing overlaps, nothing rides a scene, brand's own recognizable Helvetica Neue — the
  isolability test passes cleanly. This is a template-specific editorial header, NOT the brand's generic
  `tokens.json → chrome.masthead` wordmark row (see §④ ambiguity — it is still chrome, just a different
  approved chrome grammar for this content series). Read as chrome: present, top full-width row, minor scale
  (small caption/title-scale text, does not compete with the display headline lower on the canvas), fill ink
  (#101010, var(--brand-text-on-light)), value solid, treatment HTML.
- **Hairline rule 1 (below masthead)** · HTML-isolable-overlay · the brand's decision-line move (`moves.md`
  #3: "a thin horizontal rule that establishes structure"). Full-width (7.8%–92.2%), `top:150px` = 11.1% down,
  1px, `line` token (`#D8D8D3`). Structural, inventoried so it isn't dropped (rule 2).
- **Evidence image (the crop)** · the image block. See the dedicated STYLE reads below. `present: true` in the
  general sense the whole block IS the image zone; not a `distinctive_elements` row (it's the primary content
  block, not a decorative device), but every image-block field the spec requires is captured below.
- **Hairline rule 2 (below the image)** · HTML-isolable-overlay · same decision-line move, `top:711px` = 52.7%
  down, same style as rule 1. Closes the "evidence" ledger box the image sits in.
- **Source/caption label** (reads "Evidence, huel.com, Daily Greens product page, 03 Sep 2026") · HTML-isolable-overlay
  · sits directly under hairline 2 (`top:728px` = 53.9%), the brand's caption token
  rendered exactly to spec (`type_scale.caption`: 20px/1.85cqw, +0.16em tracking, uppercase via
  `text-transform`, weight 700, graphite `#555553`/`var(--brand-secondary)`). This is `moves.md` move #8's
  "source label in caption token, graphite" — the evidence-crop move's own required annotation, naming exactly
  what the crop can carry (URL, page, date). Fully isolated below the rule, no overlap, brand font — isolable,
  HTML. Read as chrome-adjacent content: present, position left-aligned directly below the image's lower rule,
  minor scale, fill graphite (#555553, var(--brand-secondary)), value solid, treatment HTML.
- **Headline "the miss" (the VERDICT_WORD slot, the verdict word)** · HTML-isolable-overlay · the dominant idea on this half of the slide: a large,
  lowercase, bold display word (`top:820px` = 60.7%, 112px/10.37cqw, weight 700, −0.05em tracking, line-height
  0.92, ink). It sits on the flat canvas fill, well clear of the image block above it — nothing occludes it,
  no photographic subject, no woven pill, brand's own Helvetica Neue. The isolability test passes cleanly, and
  `identification-tree.md` rule 6 independently confirms: a dominant display word NOT occluded by a
  photographic subject routes to prominent HTML, never the AI. 10.37cqw is comfortably above the 8cqw display
  floor (`shared/quality-gate.md` Check D) and is the ref's OWN size (not inflated to satisfy the gate — the
  ref's own 112px/1080 canvas width already clears the floor).
- **Body paragraph** ("A ten-year claim about ingredient count…") · HTML-isolable-overlay · a 4-line regular-
  weight paragraph (`top:960px` = 71.1%, 26px/2.41cqw, line-height 1.34, ink, 760px/70.4% column width) directly
  below the headline. Isolated on the flat fill, brand font, no overlap — isolable, HTML.
- **Footer strip** (four items: author name "Farrice Cain", handle "parallaxletter.substack.com", niche
  descriptor "Supplement + performance brands", CTA "DM ANGLE") · HTML-isolable-overlay · a 4-item flex row
  pinned to the bottom (`bottom:64px` = 4.7% up from the edge → ~93.5% down), evenly spaced
  (`justify-content:space-between`), regular weight, 20px/1.85cqw, ink. This is the brand's "restrained
  footer… final frame only" offer reference (`tokens.json → modes.master_brand.offer_reference`) rendered as a
  4-slot identity/CTA strip: author name, the substack handle, the niche descriptor, and a DM call-to-action.
  Fully isolated, brand font — isolable, HTML. Read as chrome: present, position bottom full-width row, minor
  scale, fill ink (#101010, var(--brand-text-on-light)), value solid, treatment HTML.

**No `distinctive_elements` rows beyond the two hairline rules recorded above.** There is no display word
riding a scene, no seal/badge/logo, no callout pill, and no bg-level graphic device anywhere on this canvas —
consistent with `tokens.json → prohibited` (`"rounded pills", "badges", "seals", "ornamental icons",
"gradients", "shadows"` are all explicitly banned brand-wide, and none appear in this ref either).

### Image-block STYLE reads (the evidence crop)

- `medium:` **screenshot** (a real captured webpage UI — star-rating icons, a product headline, two price
  pills, a description paragraph, all in the SOURCE website's own type, not the brand's Helvetica Neue). This
  genuinely diverges from the standard `photo | flat-illustration | watercolor | sketch | 3d-render` enum — the
  closest fit is "photo of a screen" but it is more precisely a raw UI capture (a Playwright screenshot). I
  record the divergence here rather than force-fitting `photo`, per the "when the ref plainly diverges, follow
  the ref and say why" instruction. See §④ for why this reads determines the whole pipeline.
- `lighting:` **none** — there is no photographic lighting; it is a flat 2D UI capture (screen pixels, not a
  lit physical scene).
- `subject_treatment:` **inset-on-paper, object-fit:contain, no crop distortion.** The source markup (`.photo`
  div with an inline override `object-fit:contain; background:#FAFAF8`) shows the crop is NOT cropped/cover-
  filled to the box — it is scaled to fit WITHIN the box at its native aspect ratio, letterboxed on brand paper
  if needed, with a hairline border top and bottom, no radius, no shadow (shadows are brand-prohibited). This
  is `moves.md` move #8's own visual recipe verbatim: "crop sits on paper inside hairline rules… no drop
  shadow, no frame chrome, no faux-lab styling."
- `containment:` **contained-rectangle** (established at Q3 above; matches `identification-tree.md` rule 4 —
  the build must match this containment, never blow it up to full-bleed).
- `subject_role:` **free-subject.** This is the one element that is genuinely different on every single
  published post, and the entire reason this template exists: each "Creative Teardown" entry examines a
  DIFFERENT real source (a different product page, ad screenshot, review, or study excerpt). The slug
  (`evidence-crop-body`) names the LAYOUT ("evidence crop", matching `moves.md` move #8's own name), not one
  fixed recurring object — confirming `free-subject` per rule 7's own slug heuristic (a layout-named slug, not
  an object-named slug like `chain-*`).
- `hero_face_identity:` **n/a** — no face in this image block.
- `legibility-method:` **n/a** — no text overlays the photo directly (the caption sits below it, on paper,
  past the second hairline); there is no legibility-over-photo concern to resolve either way.

## ③ Pipeline

edit_mode: **none — this is the one field where the default AI-first posture is overridden by an explicit
brand hard rule, not a judgment call.**

`brand_context/visual-identity/moves.md` move #8 ("Evidence crop", the move this exact ref implements) states
verbatim: *"Only owned brand artifacts and verified source excerpts qualify… AI-generated imagery is not
evidence and never fills this zone."* This is a brand-level prohibition on the SPECIFIC zone this template
builds, not a general anti-AI stance (every other block on this canvas is plain HTML text, and other templates
in this brand's system DO use AI generation elsewhere). So the evidence-crop image zone is authored as a plain
`<img data-slot="PHOTO_MAIN" src="{{PHOTO_MAIN_PATH}}">` bound to a REAL, per-post user-supplied capture — never
an `[ai-image-zone]` block, never `edit-from-ref`, never `texture-extract`. `PHOTO_MAIN_PATH` is
`user_editable: true` (the one truly variable element — different on every published post) with
`source: user-uploaded-asset`
(`shared/conventions/routing-and-validation.md`'s own inventory schema explicitly names this exact case).

when_ai_runs: **never**, for this zone. (No other zone on this canvas is a candidate for AI generation either —
every text block is isolable HTML per §2.)

extraction: **none — no cleaning, no generation.** For the CANONICAL PREVIEW sample (this build's own demo
render), I use the REAL asset that this exact reference frame was built from:
`brand_context/visual-identity/compositions/editorial/evidence/huel-greens/crop-claim.png` — a genuine
Playwright capture of `huel.com/products/huel-daily-greens` (`manifest.json` in that folder records the URL,
capture backend, and timestamp). This is not a synthetic "looks like evidence" placeholder; it IS evidence,
exactly as move #8 requires, and it is the same asset the approved ref itself displays. I copy it into this
template's `assets/` folder (co-located per the asset-provenance convention) and pass it as the sample
`PHOTO_MAIN_PATH` value — zero AI image-generation calls, $0 cost, full compliance.

## ④ Ambiguity (examined)

- **Considered generating a synthetic "evidence-style" mockup via AI (`edit-from-ref`) for the preview, to stay
  consistent with the "AI generates by default" posture stated in the builder's role.** Ruled OUT, hard: the
  brand's own design system explicitly and specifically forbids this for this exact zone (`moves.md` #8, quoted
  above), and `shared/conventions/routing-and-validation.md`'s photo-zone inventory schema explicitly supports
  `source: user-uploaded-asset` as a first-class, non-AI photo-zone kind — this is not an edge case the system
  fails to anticipate, it is a named, supported route. The role's "AI-first, HTML is the surgical exception"
  framing governs the *text-vs-image substrate* decision (does a block render as HTML or does the AI bake it);
  it does not override an explicit brand prohibition on WHERE the pixels of a specific photo zone come from.
  Generating a fake product-review screenshot here would also risk shipping something that reads as a real
  (but fabricated) claim about a real brand (Huel) — a second, independent reason to keep this zone real-source
  only. This is the single most consequential read in this rationale — it decides the entire §3 pipeline.
- **Considered whether the masthead row ("Creative Teardown" + date + arrow) should be forced into the brand's
  generic `tokens.json → chrome.masthead` shape (`"FARRICE CAIN" / descriptor`).** Ruled OUT: this ref is one of
  eight reference frames Farrice explicitly commissioned and approved 2026-09-03 as "the template" for a new
  editorial aesthetic pivot (`../REVIEW-NOTES.md`, "aesthetic pivot: the editorial style" entry) — the frame's
  own CSS (`_editorial.css → .head`) defines a DIFFERENT, deliberate chrome grammar for this content series:
  series title left, date + arrow right. Forcing the generic masthead shape onto this ref would silently
  discard Farrice's own explicit design decision in favor of an older, superseded pattern. I follow the ref
  (and the source markup that generated it) faithfully here — recorded as HTML-isolable-overlay chrome in §2 —
  rather than force-fitting the older token.
- **Considered whether the evidence image, being a UI screenshot rather than a photograph, might actually be
  `bg_treatment: physical-placeholder` (Q2, form B1) instead of a framed image (Q3, form A).** Ruled OUT: B1
  requires a BLANK in-scene surface (an empty screen/frame/billboard inside a depicted scene) that content gets
  placed ONTO, respecting the surface's own perspective/lighting. Here there is no larger scene at all — the
  crop sits directly on the flat canvas fill as a standalone bounded rectangle, and it already carries its own
  complete, self-contained content (it does not need the template to draw anything ONTO it). This is squarely
  the Q3 "contained rectangle, different material on all sides" case, not a B1 in-scene surface.
- **Considered whether the footer's "DM ANGLE" item is fixed brand chrome (like the author name and handle) or
  a per-post-variable call-to-action.** Resolved as `user_editable: true`: unlike the author name/handle/niche
  descriptor (which are literally always the same across every post — they identify Farrice, not this post),
  a closing CTA is plausibly reworded post to post ("DM ANGLE" vs. a different prompt) even though this specific
  ref happens to show one recurring value. This mirrors the kicker-stack-body sibling's precedent for
  `FIELD_INDEX` — a value that recurs across the reviewed ref but is structurally a per-post variable, not an
  identity constant.
