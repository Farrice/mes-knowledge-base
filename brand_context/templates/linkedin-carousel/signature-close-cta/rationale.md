# rationale — signature-close-cta

## ① Form + tree-path-with-why

form: solid-css

Tree walk (first match wins):

- **Q1 — TRULY solid color, zero texture, no image? YES.** The entire canvas is one flat fill
  (`#F3F3F0`, matches `tokens.json colors.bg_light`/`named.canvas` exactly). There is no paper
  grain, no vignette, no gradient, no photo, no silhouette, no embedded crop anywhere on the
  frame — every mark on the slide is vector type (or a CSS rotate transform on vector type). This
  is not a "warm near-white that might be paper" trap case: the source composition file itself
  declares `background: #F3F3F0` as a literal CSS fill with nothing else painted underneath it.
  The tree **STOPS here** at `solid-css` — Q2 (blank in-scene surface), Q3 (contained image), Q4
  (integrated text needing an image/scene to integrate WITH) never get reached because they all
  presuppose an image_zone, and `image_zone.exists = false` for this ref.
- Confirms exactly the same form as this pool's sibling close/CTA frame (`statement-close-cta`)
  and its cover counterpart (`headline-subline-cover`) — this brand's whole "typographic"/"editorial"
  system is built on flat CSS canvases with zero AI generation; this ref is no exception, it simply
  swaps the ink-dark-recommendation surface for the light canvas + the new script-signature move.

## ② Per-block breakdown

- **Masthead-left "Creative Teardown"** · HTML-isolable-overlay · a small, flat, axis-aligned
  uppercase-adjacent label top-left, identical geometry class to the masthead label in every other
  template in this pool (`statement-close-cta`, `headline-subline-cover`). No occlusion, no
  perspective, no relief — the isolability test passes cleanly. Per-post variable: this is the
  *series title* for the post ("Creative Teardown"), read from `_editorial.css`'s own comment
  ("header: series title left, date + arrow right") — NOT the brand's fixed `FARRICE CAIN` identity
  masthead used elsewhere in this pool. This editorial style substitutes a per-series title here
  instead of the brand wordmark, so it is a **content slot**, not locked chrome.
- **Masthead-right "03 Sep, 2026 →"** · HTML-isolable-overlay · flat text + a small arrow glyph,
  right-aligned, same row as the series title. The date is per-post (publish date); the arrow is a
  fixed decorative glyph (never varies, no content reason to swap it).
- **Giant display word "dm angle"** · HTML-isolable-overlay · a huge (250px / 23.1cqw) flat,
  centered, lowercase Helvetica Neue 700 word, `text-align:center` inside a full-width zone. It sits
  on the flat canvas with nothing behind it to integrate with — no photographic subject, no scene,
  no perspective it must obey. The only thing that touches it is the script signature (see next
  row), and that touch is a flat CSS z-index overlap, not an occlusion by a rendered 3D/photographic
  object — so the isolability test still passes: HTML can reproduce this overlap exactly (two
  absolutely-positioned text layers, one rotated) without needing a generated image. This is the
  slide's primary per-post content axis — the recap/decision word from the carousel this frame
  closes.
  - `distinctive_elements` row: **giant display word "dm angle"** — present: true · position: center
    (vertically ~34–50% of canvas, horizontally centered) · size: dominant (spans edge-to-edge, the
    single loudest element on the frame) · fill: ink (`#101010`) · value: solid · treatment: **HTML**
    (per the decisive routing question — flat 2D type, not object-bound; no perspective/glow/occlusion
    by a photographed object to obey).
- **Script signature "Farrice Cain"** · HTML-isolable-overlay · a script-face word, rotated -7°,
  layered on top of the giant word in the brand's one unlocked accent (`colors.signature_accent`
  `#FF2D2D`). This is brand move #10 ("script signature") — the moves.md entry is explicit that this
  is authored as a CSS overlay (`transform: rotate(-7deg)`, absolute position, `white-space: nowrap`)
  in the source composition file (`compositions/editorial/frames/08-thanks-signature.html`), not a
  photographic bake. Per the decisive routing question: is this text bound to an object's
  geometry/lighting? No — the rotation is a flat 2D CSS transform, not a perspective/relief/glow
  effect tied to a rendered 3D surface; nothing photographic occludes it or is occluded by it. HTML
  wins on crispness and exact brand color (`--brand-*`) without ever re-generating an image. This is
  the brand's own identity signature (`tokens.json author.name` = "Farrice Cain") — it is FIXED
  content, not a per-post variable (every close frame in this style carries the same signature; it is
  a brand mark, not a swappable field, matching how `MASTHEAD_LEFT` is locked in `statement-close-cta`).
  - `distinctive_elements` row: **script signature overlay** — present: true · position: center
    (overlaid diagonally across the lower-middle of the giant word, left edge ~26% of canvas width) ·
    size: medium (spans roughly half the canvas width at 116px/10.7cqw — a strong secondary device,
    not the dominant element) · fill: signature-accent coral-red (`#FF2D2D`) · value: solid ·
    treatment: **HTML** (same reasoning as above — flat CSS rotate, no object-binding).
- **Footer strip (4 items)** · HTML-isolable-overlay · four small, evenly-spaced, flat plain-text
  items along one row at the base of the canvas (`justify-content:space-between`), identical
  isolability class to every other chrome row in this pool. Per-item:
  - "Farrice Cain" — fixed, the author's name (brand identity, matches `tokens.json author.name`).
  - "parallaxletter.substack.com" — fixed, the brand's owned publication URL.
  - "Supplement + performance brands" — fixed, a sentence-case shorthand of the brand's category
    descriptor (`tokens.json chrome.masthead.labels[2]`, here rendered in sentence case per THIS
    ref rather than the token's uppercase form — an editorial-style variant, not new content).
  - "DM ANGLE" — per-post, the resolved topic/thread tag this closing frame is wrapping up (mirrors
    how `RECOMMENDATION_NAME` behaves as a per-post slot in the sibling `statement-close-cta`).

No image/photo block exists on this ref at all — `image_zone.exists = false`. No embedded icons or
brand-badge marks either (the masthead/footer are plain type, not logotype); Step 2 (icon resolution)
does not apply and is skipped.

## ③ Pipeline

edit_mode: none — pure CSS/HTML, no AI generation whatsoever. There is no `[ai-image-zone]` block:
the background is `background: var(--brand-bg-light)` and every mark on the canvas (including the
rotated script signature) is native browser type rendering, which reproduces this ref's flat,
vector-crisp look more faithfully — and more cheaply — than any image-model round-trip would.
when_ai_runs: never.
extraction: n/a — nothing is extracted or cleaned; there is no source pixel content to isolate from
a background (the ref itself is already a flat CSS composition, confirmed by reading the sibling
source file `compositions/editorial/frames/08-thanks-signature.html` that generated it).

## ④ Ambiguity (examined)

- **Considered B2 (textured-bg/reserved-zone) — ruled out.** B2 requires an actual texture/landscape
  treatment with the text floating on a reserved clean sub-zone of it. This ref's background has
  zero texture anywhere (it's a single flat hex, not a "reserved calm zone of a busier field") — Q1 fires and
  stops the walk before B2 is ever reachable; there's no busier field this flat canvas could be a
  "clean zone within."
- **Considered C (integrated-text, AI-baked) for the signature/giant-word overlap — ruled out.** The
  signature visually crosses the giant word, which could look like "integrated/overlaid, no isolable
  container" at a glance. But the decisive routing question is about OBJECT-BOUND binding
  (perspective, glow, occlusion by a rendered surface/subject, relief/print texture) — this overlap
  is neither: it's two independently-positioned flat vector-text layers, one rotated via a plain CSS
  `transform`, stacked by `z-index`. HTML reproduces this pixel-for-pixel from the same source
  composition file that generated the ref, so there is no reason to hand it to an image model (which
  would also risk hallucinating the signature's exact letterforms/kerning on every re-render, where
  CSS renders it identically every time). Ruled out.
  - **Considered whether the giant word / signature carries a `subject_role` reading at all (n/a —
    there is no `image_zone`, so this field does not literally apply)** — worth reasoning through
    anyway by analogy: the giant word is `free-subject`-shaped, not a single fixed-identity object —
    the slug `signature-close-cta` describes the LAYOUT (a signature-bearing close/CTA frame), and the
    word's actual content ("dm angle") is exactly the kind of per-post recap word that should vary
    with the topic the carousel closes. This is moot for the FORM decision (no AI runs either way),
    but it settles that `HEADLINE_WORD` must be `user_editable: true`, never hardcoded as a fixed
    brand element.
- **Considered whether the footer's "Supplement + performance brands" line should be a per-post
  editable slot instead of fixed — ruled out (kept fixed).** It reads as the brand's category
  descriptor (a shorthand of `tokens.json chrome.masthead.labels[2]`) appearing consistently across
  this editorial style's frames (also present, same role, in the composition's other seven reference
  frames per a spot-check of the shared `_editorial.css` footer class), not a claim that changes
  frame-to-frame — it is chrome, treated as fixed, same class of decision as `MASTHEAD_LEFT` being
  locked in `statement-close-cta`.
