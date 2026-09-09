# rationale — signature-cover

## ① Form + tree-path-with-why

form: solid-css

Tree walk (first match wins):

- **Q1 — TRULY solid color, zero texture, no image? YES.** Pixel-sampled the ref at nine points
  (all four corners, dead-center, and three empty regions between the header row / giant word /
  footer): every sample returned the identical RGB `(243, 243, 240)` with `std = 0` — a mathematically
  flat fill, not a "warm near-white that might secretly be paper" trap case. `(243,243,240)` matches
  `tokens.json colors.bg_light` / `colors.named.canvas` exactly. There is no paper grain, no vignette,
  no gradient, no photo, no silhouette, no embedded crop, no scan-line/dust artifact anywhere on the
  canvas — every mark on the slide is vector type (black ink, plus one rotated red script overlay).
  `image_zone.exists = false`. The tree **STOPS here**: Q2 (blank in-scene surface), Q3 (contained
  image), Q4 (integrated text needing something to integrate WITH) all presuppose an `image_zone` that
  doesn't exist on this ref.
- Confirmed against the ref's own source composition file (ground truth, found at
  `brand_context/visual-identity/compositions/editorial/frames/01-cover-signature.html` +
  `_editorial.css`, the exact file that rendered this PNG): `.frame { background: #F3F3F0; }` is a
  literal flat CSS fill with nothing else painted under it — no texture layer, no image tag anywhere
  in the DOM. Every element in the composition is native browser text (`<span>`, `<div>`), confirming
  the pixel read independently.
- This is the SAME visual system as this pool's sibling frames in progress (`signature-close-cta` —
  the "close" counterpart of this "cover" role, sharing the identical header/footer grammar and the
  same script-signature move) — this brand's whole editorial style is a flat CSS canvas with zero AI
  generation. This ref is the opening/cover frame of that style; it swaps the close frame's giant
  recap-word for the giant hook-word "teardown" and adds the category+date header row.

## ② Per-block breakdown

- **Header-left "Creative Teardown"** · HTML-isolable-overlay · a small, flat, axis-aligned bold label
  top-left (Helvetica Neue 700, 26px/2.41cqw, `letter-spacing:-0.01em`, sentence case — NOT the
  caption token's uppercase+tracked treatment). No occlusion, no perspective, no relief — passes the
  isolability test cleanly: it can be lifted into a plain HTML `<span>` without losing anything. This
  is the **series/category title** for the post, per the source file's own comment
  (`/* header: series title left, date + arrow right */` in `_editorial.css`) — it is NOT the brand's
  fixed `FARRICE CAIN` identity masthead used in the pool's `statement-close-cta` /
  `headline-subline-cover` templates (that masthead is a different, disabled-here component reading
  `tokens.json chrome.masthead.labels`). Because this editorial style substitutes a per-series title
  here instead of the brand wordmark, it is a **content slot** (`CATEGORY`), not locked chrome — kept
  `user_editable: true` since Farrice may reuse this exact cover layout for a different content pillar
  later (e.g. a different newsletter series name).
- **Header-right "03 Sep, 2026 →"** · HTML-isolable-overlay · flat text (Helvetica Neue 400, 22px/
  2.04cqw, `color:#101010`) plus a small arrow GLYPH (30px/2.78cqw, `line-height:1`), right-aligned on
  the same flex row as the category title (`display:flex; justify-content:space-between`). The date is
  per-post (the publish date of this specific carousel — `user_editable: true`, sample "03 Sep, 2026").
  The arrow is a **literal typographic character** ("→", U+2192) in the source DOM, not an SVG/logo
  asset — it needs no icon-provenance resolution (Step 2 is skipped) and never varies, so it's authored
  as fixed decorative chrome, not a slot.
  - `distinctive_elements` row: **header arrow glyph** — present: true · position: top-right · size:
    minor · fill: ink (`#101010`) · value: solid · treatment: **HTML** (a plain Unicode character in a
    `<span>`, not a resolved brand mark — no provenance lookup applies).
- **Giant display word "teardown"** · HTML-isolable-overlay · a huge (238px/22.04cqw ceiling, weight
  700, `line-height:0.86`, `letter-spacing:-0.065em`) flat, centered, ALL-LOWERCASE Helvetica Neue word
  spanning edge-to-edge (`left:0; width:100%; text-align:center`), positioned `top:455px` (33.7% of
  canvas height). It sits on the flat canvas with nothing behind it to integrate with — no
  photographic subject, no scene, no perspective/glow/relief it must obey. The only thing that touches
  it is the script signature (next row), and that touch is a flat CSS z-index overlap between two
  vector-text layers, not an occlusion by a rendered 3D/photographic object — the isolability test
  still passes: HTML reproduces this overlap exactly (two absolutely-positioned text nodes, one
  rotated) without a generated image, and does so pixel-identically on every re-render (an image model
  would risk re-hallucinating the exact word every time). This is the slide's **primary per-post
  content axis** — the one-word hook/topic this specific teardown post is about.
  - `distinctive_elements` row: **giant lowercase display word** — present: true · position: center
    (vertically ~33.7%–48% of canvas, horizontally full-bleed/centered) · size: **dominant** (the
    single loudest element on the frame, spans the full canvas width) · fill: ink (`#101010`) · value:
    **solid** · treatment: **HTML** (per the decisive routing question: flat 2D type, not object-bound
    — no perspective/glow/occlusion by a photographed object to obey).
  - `subject_role`: n/a (no image/photo primary subject on this ref — this rule applies to image blocks only).
- **Script signature "Farrice Cain"** · HTML-isolable-overlay · a script-face word (font stack
  `"Snell Roundhand", "Zapfino", cursive` — the macOS system script faces the source composition file
  itself specifies as the interim signature placeholder, pending Farrice's real handwritten SVG),
  116px/10.74cqw, weight 700, `transform: rotate(-7deg)`, `letter-spacing:-0.01em`, `white-space:nowrap`,
  positioned `left:240px (22.2%) top:540px (40%)`, layered on top of the giant word. Color is the
  brand's ONE unlocked accent, `tokens.json colors.signature_accent` (`#FF2D2D`) — this is brand move
  #10 ("Script signature", `moves.md`), explicitly authored as a CSS overlay in the source composition
  file, not a photographic bake. Per the decisive routing question: is this text bound to an object's
  geometry/lighting? **No** — the rotation is a flat 2D CSS `transform`, not a perspective/relief/glow
  effect tied to a rendered surface; nothing photographic occludes it or is occluded by it. HTML wins
  on crispness and exact brand color without ever re-generating an image. This is the brand's own
  identity signature (`tokens.json author.name` = "Farrice Cain") — **FIXED content, not a per-post
  variable** (every cover/close frame in this editorial style carries the identical signature per
  `moves.md` #10: "on the cover and close frame only" — it is a brand mark, never a swappable field).
  - `distinctive_elements` row: **script signature overlay** — present: true · position: center
    (overlaid diagonally across the lower-middle of the giant word, left edge ~22.2% of canvas width,
    spanning to ~79.7%) · size: **medium** (a strong secondary device — roughly 57% of canvas width at
    116px/10.74cqw — clearly subordinate to the dominant giant word, never competing with it for
    primacy) · fill: `signature_accent` coral-red (`#FF2D2D`, read directly off the ref's own red
    pixels — sampled `[255, 45, 45]`, an exact match) · value: **solid** · treatment: **HTML** (same
    reasoning as the giant word — flat CSS rotate transform, no object-binding). Because
    `render_template.py`'s brand-kit CSS-var injection does not carry an arbitrary `signature_accent`
    key (only the fixed `colors.{accent,primary,bg_*,text_*}` schema), the hex is declared ONCE as a
    local custom property (`--signature-accent: #FF2D2D` /* tokens.json colors.signature_accent —
    the brand's one sanctioned exception, script signature ONLY */) inside the template's own
    `<style>` block and consumed via `var(--signature-accent)` everywhere it's used — never inlined as
    a bare literal color value on the element itself.
- **Footer strip (4 items)** · HTML-isolable-overlay · four small, evenly-spaced, flat plain-text
  items along one row at the base of the canvas (Helvetica Neue 400, 20px/1.85cqw,
  `justify-content:space-between`, `bottom:64px` / 4.74% from the bottom edge). Same isolability class
  as every other flat chrome row on this ref — no scene, no occlusion, no exotic font. Per-item:
  - "Farrice Cain" (`AUTHOR_NAME`) — fixed, the author's identity, matches `tokens.json author.name`
    exactly. Not per-post.
  - "parallaxletter.substack.com" (`SITE_URL`) — fixed, the brand's owned publication URL. Not
    per-post.
  - "Supplement + performance brands" (`NICHE_LABEL`) — fixed, a sentence-case shorthand of the
    brand's category descriptor (compare `tokens.json chrome.masthead.labels[2]`:
    "CREATIVE STRATEGY FOR SUPPLEMENT + PERFORMANCE BRANDS", uppercase) — here rendered in sentence
    case and abbreviated, an editorial-style variant of the SAME brand content, not new content. Kept
    fixed because it names the brand's niche, which does not change post-to-post.
  - "DM ANGLE" (`CTA_LABEL`) — the brand's evergreen engagement CTA phrase for this series (source
    file authors it as a static literal string in the footer row, same as the other three items — it
    is not flagged anywhere as topic-dependent). Kept fixed for THIS cover template; `user_editable`
    left `true` at the field level only because it's plain text with no structural cost to changing it,
    but the DEFAULT/intended value never varies across posts.

No image/photo block exists on this ref — `image_zone.exists = false`. No embedded icons or
brand-badge marks (the header/footer are plain type, not logotype; the arrow is a Unicode glyph, not
an asset) — Step 2 (icon resolution) is skipped entirely, its trigger condition never fires.

## ③ Pipeline

edit_mode: none — pure CSS/HTML, zero AI generation. There is no `[ai-image-zone]` block: the
background is `background: var(--brand-bg-light)` and every mark on the canvas (including the rotated
script signature) is native browser type rendering, which reproduces this ref's flat, vector-crisp
look more faithfully — and at zero marginal cost — than any image-model round-trip would.
when_ai_runs: never.
extraction: n/a — nothing is extracted or cleaned; there is no source pixel content to isolate from a
background. The ref is already, at its origin, a flat CSS composition (confirmed directly against
`compositions/editorial/frames/01-cover-signature.html`, the file that rendered this exact PNG).

## ④ Ambiguity (examined)

- **Considered B2 (the reserved-zone / texture-background scenario) — ruled out.** B2 requires an
  actual texture/landscape backdrop with text floating on a reserved clean sub-zone of a BUSIER field.
  This ref's backdrop has zero texture anywhere — it is a single flat hex sampled identically at nine
  points across the canvas, not "a calm zone of a busier field." Q1 fires and stops the walk before B2
  is ever reachable; there is no busier field for this flat canvas to be a "reserved clean zone within."
- **Considered C (integrated-text, AI-baked) for the giant-word/signature overlap — ruled out.** At a
  glance, the red script crossing the black word could look like "integrated/overlaid, no isolable
  container" (Q4's territory). But the decisive routing question is specifically about OBJECT-BOUND
  binding — perspective, glow, occlusion by a rendered surface/subject, relief/print texture on a
  physical object. This overlap is none of those: it is two independently-positioned flat vector-text
  layers, one rotated via a plain CSS `transform: rotate(-7deg)`, stacked by z-index/DOM order. HTML
  reproduces this pixel-for-pixel from the exact same mechanism that generated the ref (confirmed
  against the source `.html`/`.css` files), so handing it to an image model would be strictly worse —
  it would risk hallucinating the signature's exact letterforms/kerning/rotation angle on every
  re-render, where CSS renders it identically, every time, for $0. Ruled out.
- **Considered whether the header's "Creative Teardown" and the footer's "Supplement + performance
  brands" should be treated as the brand's standard `chrome.masthead` component — ruled out.** Both
  read superficially like "brand chrome" (top-left label, descriptor text), but neither matches
  `tokens.json chrome.masthead.labels` verbatim (`FARRICE CAIN` / descriptor uppercase) — this ref's
  header shows a *series/category title* + *date*, and its footer shows a 4-item credit strip, both
  bespoke to this editorial style (confirmed against the source `_editorial.css`, which defines these
  as its own `.head`/`.foot` classes, entirely separate from any `.masthead`/`.dots` chrome component
  elsewhere in the brand system). Per the chrome auto-inject matrix, injecting the standard 3-slot
  `{{MASTHEAD_LEFT/CENTER/RIGHT}}` component here — on top of or instead of this ref's own header/footer
  — would add chrome the ref never shows. Built as bespoke content zones instead.
  - **Considered whether the whole header+giant-word+signature+footer stack could be read through
    the image-subject fixed-vs-free distinction (rule 7) — moot.** That distinction (a template's
    identity object vs a genuine per-post swap) only applies to an image/photo primary-subject block;
    there is no image block on this ref at all, so the rule doesn't engage. What it DOES settle, by
    analogy, is which TEXT block is the template's true
    per-post variation axis: the giant word ("teardown") is the one element whose *content itself* is
    the point of the post (what is being torn down), exactly the role a `free-subject` image would
    play on a photographic template — so it is the slot marked `user_editable: true` with the highest
    priority, never hardcoded.
  - **Considered whether "Supplement + performance brands" and "DM ANGLE" should be per-post editable
    instead of fixed-with-editable-field — settled as fixed-in-practice.** Both read as evergreen brand
    furniture (niche descriptor, standing CTA) that appears identically across this editorial style's
    other reference frames (a spot-check of the sibling composition files in the same
    `compositions/editorial/frames/` directory shows the same footer class/copy reused across frames);
    nothing in the source ties either string to THIS specific post's topic. Exposed as slots (so the
    field is technically editable, matching the convention that every rendered text zone gets a
    `## Slots` entry) but documented as brand-fixed defaults, not the variation axis.
