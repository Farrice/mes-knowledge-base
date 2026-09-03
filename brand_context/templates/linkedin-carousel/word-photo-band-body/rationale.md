# rationale — word-photo-band-body

## ① Form + tree-path-with-why

form: a-framed-image

Tree walk, in order, looking ONLY at the ref:

- **Q1 (solid-css)? NO.** The canvas fill (`#F3F3F0`) is a flat, zero-texture solid — but `image_zone.exists ==
  true` (there is a real photographic/screenshot crop lower on the canvas), so Q1's second condition fails.
  Solid-color alone doesn't route here when a real image block is present.
- **Q2 (b1-surface-placeholder)? NO.** There is no blank in-scene surface (no screen/billboard/paper waiting
  to be filled) — the image block already carries finished, specific content (a real Meta Ad Library
  screenshot showing two active-ad detail cards). B1 requires a surface that is BLANK until the template fills
  it; this one arrives pre-filled as a captured asset.
- **Q3 (a-framed-image)? YES — STOP HERE.** The image sits in a single hard-edged rectangle (left 84px, top
  520px, width 912px, height 600px on the 1080×1350 canvas) with the canvas's own flat `#F3F3F0` fill visible
  on all four sides — a genuinely different material (paper-flat canvas vs. the screenshot's own white/UI
  chrome) bounds it, and the canvas's texture (there isn't any) does not continue into or past the rectangle.
  This is the discriminator for Form A: contained-rectangle, not full-bleed. The tree stops here.
- (Q4/Q5 not reached — Q3 already matched.)

## ② Per-block breakdown

- **Header title "Creative Teardown"** · HTML-isolable-overlay · sits in a clean top-left corner of the flat
  canvas fill, no overlap with anything, ordinary Helvetica Neue 700 at 26px — trivially rippable into a plain
  HTML span. Isolability test passes cleanly (not overlaid, no heavy effects, brand's own recognizable font).

- **Date + arrow "03 Sep, 2026 →"** · HTML-isolable-overlay · top-right, same header row, flex-justified against
  the title. The arrow is a plain Unicode glyph (`→`), not a brand mark or icon asset — rendered as ordinary
  text, no SVG/icon resolution needed. Isolable.

- **Headline "what they run"** · HTML-isolable-overlay · giant lowercase Helvetica Neue 700 at 144px
  (13.33cqw — well above the 8cqw display floor on its own, no gate tension), left-aligned, sitting directly on
  the flat canvas fill with NOTHING behind or through it — no photographic subject, no occlusion, no woven
  device crossing the letterforms. Passes the decisive routing question cleanly: not bound to any object's
  geometry/lighting, so HTML overlay wins on crispness and exact brand type. This is the giant-word "editorial"
  display move Farrice approved 2026-09-03 (see §④) — HTML renders it far more reliably than an AI bake would
  (gpt-image renders large display type poorly per `identification-tree.md` rule 6).

- **Subtitle paragraph (4-line body copy)** · HTML-isolable-overlay · sits under the headline in a narrower
  column (760px / 70.37% of the canvas width, not the full safe-margin width — a deliberate narrower reading
  column), flat canvas bg behind it, ordinary body weight. Isolable, no effects, no overlap.

- **Photo zone (the "photo band")** · treated as the image block, see below · the ONE piece of the slide that
  is NOT template-drawn — a real captured screenshot asset dropped into a contained rectangle. Isolable as a
  CONTAINER (Q3 object-isolability: flat, axis-aligned, non-overlapping, no rotation/perspective/cast shadow —
  a single rectangular `<img>` slot is the correct route, not an in-scene AI-placed object).

- **Source label ("Source · Meta Ad Library, "AG1", active ads, 03 Sep 2026")** · HTML-isolable-overlay · a
  single caption-scale line under the photo zone, uppercase via CSS `text-transform`, tracked +0.16em, sits on
  the flat canvas fill. Isolable — this is exactly the brand's caption/functional-label typographic role
  (`tokens.json → type_scale.caption`).

- **Footer strip (4 items: "Farrice Cain" · "parallaxletter.substack.com" · "Supplement + performance brands"
  · "DM ANGLE")** · HTML-isolable-overlay · a single flex row, space-between, bottom of the canvas, flat bg
  behind it, no overlap with anything above it. Isolable.

No distinctive_elements rows beyond the header arrow glyph (evaluated above as part of the date block, not a
separate seal/badge/pill — there is no logo, no brand mark, no callout pill, and no radial/graphic device
anywhere on this canvas). `distinctive_elements: none` beyond the plain text glyph.

**Image block — the STYLE reads:**
- `medium:` **screenshot / real UI capture** (not `photo`, not `flat-illustration` — the ref's image block is a
  genuine captured screenshot of the Meta Ad Library interface, containing an embedded product/lifestyle photo
  thumbnail inside its ad-preview panel; no single enum value in the spec covers "screenshot," so this is
  recorded literally rather than force-fit into `photo`).
- `lighting:` **none** — this is flat UI chrome, not a photographed scene; the small embedded ad-creative photo
  inside the screenshot carries its own natural/studio-soft lighting, but that is content OF the source
  capture, not something this template controls or generates.
- `subject_treatment:` closest enum is **inset-with-shadow**, but with an explicit caveat: the ref shows NO
  drop shadow and NO border radius — a hard flat-edged rectangle sitting directly on the canvas fill
  (`.photo { overflow:hidden; background:#D8D8D3; }` / `.photo img { object-fit:cover }` — no shadow, no
  radius declared). Recorded faithfully rather than silently defaulting to the "shadow" reading the enum name
  implies.
- `containment:` **contained-rectangle** (confirmed above in §①).
- `subject_role:` **free-subject.** The slug ("word-photo-band-body") names the LAYOUT — a giant word + a photo
  band — not a fixed object; the screenshot's actual content (which competitor, which ad, which platform) is
  exactly what changes every time this teardown format runs. The ref's specific "AG1 by Athletic Greens"
  screenshot is one EXAMPLE instance of the format, not the template's fixed identity.
- `hero_face_identity:` **n/a.** No human hero face is the subject of this template. A person incidentally
  appears inside the embedded ad-creative thumbnail (part of the captured screenshot's own content), but that
  is not a brand hero face this template routes or resolves.
- `legibility-method:` **natural-composition.** No block on this canvas relies on legibility-over-a-photo — the
  headline, subtitle, source label, and footer all sit on the flat canvas fill with nothing photographic
  behind them. No scrim/band device is authored anywhere.

## ③ Pipeline

edit_mode: none
when_ai_runs: never (this template performs no AI image generation)
extraction: none — the image block is NOT AI-generated. `brand_context/visual-identity/moves.md` move #8
("Evidence crop") states explicitly: *"AI-generated imagery is not evidence and never fills this zone."* This
overrides `scenarios/a-framed-image.md`'s generic default (`edit-from-ref`, subject-only) for this specific
template: the photo band's content must be a REAL captured source (a screenshot, a product-page crop, a real
photo) supplied per post, never synthesized. The canonical/sample asset for this build is the actual real
evidence capture already on disk — `brand_context/visual-identity/compositions/editorial/evidence/
ag1-adlibrary/crop-cards.png` — which is literally the SAME source image the approved reference frame itself
was built from (see `brand_context/visual-identity/compositions/editorial/frames/02-opener-photo-band.html`).
Using it as the sample gives perfect fidelity to the ref with zero AI cost and zero risk of the gate confusing
"filled" for a fabricated scene. Every other block on this slide is plain HTML/CSS — no AI generation anywhere
in this template.

## ④ Ambiguity (examined)

**Is this B1 (surface-in-scene) instead of A (framed-image)?** Considered and ruled out. B1 requires a BLANK
in-scene surface that the template fills with generated content respecting the surface's own
perspective/lighting (a billboard, a screen). This photo zone is a flat, non-perspective, non-tilted rectangle
holding a pre-finished real capture — there is no perspective or lighting relationship for an AI bake to
respect, and nothing here is "blank." Q3's containment test (a different material bounding all four sides,
canvas texture not continuing past the edge) matches Form A exactly, and B1's defining condition (blank surface
awaiting content) is absent. A is correct.

**Should the photo zone still get a generated `[ai-image-zone]` sample, the way `scenarios/a-framed-image.md`
defaults to (`edit-from-ref`, subject-only)?** Examined and rejected for THIS template specifically. The
scenario file's generic default assumes the framed image is stylized photography the AI can vary per post.
This ref's image zone is explicitly evidence (a real competitor ad-library screenshot), and the brand's own
move catalog (move #8, "Evidence crop") makes generating it synthetically a policy violation, not just a
stylistic choice — "AI-generated imagery is not evidence and never fills this zone" is unambiguous. So this
build deliberately diverges from the scenario file's generic edit-from-ref default; `edit_mode: none` is the
correct, deliberate reading for this specific ref/brand combination, not an oversight.

**Is the top header ("Creative Teardown" + date) the brand's standard `chrome.masthead` (identity label +
descriptor, per `tokens.json`)?** Examined and ruled NOT the same chrome device. `tokens.json →
chrome.masthead.labels` is `["FARRICE CAIN", "", "CREATIVE STRATEGY FOR SUPPLEMENT + PERFORMANCE BRANDS"]` —
brand identity + descriptor. This ref's header instead shows a per-post SERIES TITLE ("Creative Teardown") +
a DATE STAMP + an arrow — a document-header device, not the identity masthead. `brand_context/templates/
linkedin-carousel/styles.json` and `REVIEW-NOTES.md` (2026-09-03 "aesthetic pivot: the editorial style" entry)
confirm this is a deliberate, separately-approved chrome grammar for the "editorial" style bucket (distinct
from the "typographic" pool's masthead + field-index pattern used by `kicker-stack-body` etc.) — the brand's
own identity + descriptor instead appears in THIS template's FOOTER strip ("Farrice Cain" · "Supplement +
performance brands"), which functions as this style's masthead-equivalent, just relocated to the bottom of the
canvas per the approved editorial grammar. Both header and footer are authored as HTML chrome; neither is
force-fit into the standard 3-slot masthead component, since the content and position genuinely differ from
that component's contract.

**Does the source-label color (`#8C8C82`, stone) need its own CSS var, or does it fall back to
`--brand-secondary` (graphite, `#555553`) like the pool's existing captions do?** Examined. `render_template.py`
does not currently emit a dedicated CSS var for `tokens.json → colors.text_muted` / `colors.named.stone`
(`#8C8C82`) — only `--brand-secondary` (mapped to `colors.secondary`, graphite) exists. Rather than silently
substitute graphite for stone (a real, if small, tonal drift from the ref), this build hardcodes the literal
`#8C8C82` on that one zone with an inline comment tying it to the named brand token. This is a locked value
FROM `tokens.json` itself (not an invented or ref-leaked color), so it passes the palette-token gate
(`check_palette_tokens.py` accepts any hex within tolerance of a declared brand token) while staying faithful
to the ref's actual value instead of drifting to the nearest available CSS var.
