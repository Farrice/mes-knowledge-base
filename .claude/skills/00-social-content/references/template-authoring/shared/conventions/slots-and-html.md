# Template conventions — file structure, template.html anatomy, slots

> Slice of `template-conventions.md`. Read at **Step 1** (Template Card) and **Step 4** (authoring `template.html`).

## File structure (1 template = 1 folder)

```
brand_context/templates/{pool}/{slug}/
├── ref.png             ← copy of the original ref (audit trail)
├── _ai_bg/bg.png       ← cleaned via gpt-image-2 (OR absent if bg is pure CSS). EVERY generated image
│                          lands under _ai_bg/ — never loose at the template root (a root bg.png breaks
│                          the Template Studio --emit-edit-slide); template.html refs point into _ai_bg/
├── template.html       ← the actual template (this file's conventions below)
├── instructions.md     ← per-template spec sheet (see below)
└── preview.png         ← render with sample text (shown at approval)
```

The `{pool}` is platform-specific (`linkedin-carousel`, `instagram-carousel`, etc).
The `{slug}` is a kebab-case name you choose based on the ref's visual signature (e.g., `accent-color-numbered-chapter`, `magazine-cover-with-creator-pill`, `paper-typography-body`). Avoid baking specific text from the ref into the slug — slugs describe the LAYOUT pattern, not the content.

---

## template.html — anatomy

The minimum viable template.html:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="../_shared/styles.css">
</head>
<body>
  <div class="slide" data-surface="light"><!-- data-surface = the slide's bg family: "light"|"dark"|"accent" -->
    <!-- BACKGROUND -->
    <!-- Use ONE of these patterns: -->
    <div class="bg" style="background-image: url('_ai_bg/bg.png'); background-size: cover; background-position: center;"></div>
    <!-- OR for CSS-only bg: -->
    <!-- <div class="bg" style="background: var(--brand-bg-light);"></div> -->

    <!-- CHROME (masthead at top) — only if the brand has chrome.masthead.labels configured -->
    <div class="masthead">
      <span class="masthead-slot left">{{MASTHEAD_LEFT}}</span>
      <span class="masthead-slot center">{{MASTHEAD_CENTER}}</span>
      <span class="masthead-slot right">{{MASTHEAD_RIGHT}}</span>
    </div>

    <!-- TEXT ZONES — one div per zone. position:absolute by bbox. -->
    <div class="zone"
         style="left:4%; top:13%; width:92%; height:22%;
                font-family: var(--brand-display);
                font-size: 28cqw;
                font-style: italic;
                font-weight: 700;
                color: var(--brand-text-on-light);
                text-align: center;">{{{HERO}}}</div>

    <div class="zone"
         style="left:10%; top:8%; width:80%; height:4%;
                font-family: var(--brand-display);
                font-size: 10cqw;
                font-weight: 900;
                color: var(--brand-text-on-light);
                text-align: center;">{{{SUBHEAD}}}</div>

    <!-- PILL (if present in ref) -->
    <div class="pill"
         style="left:42%; top:50%; width:16%; height:6%;
                background: var(--brand-accent);
                color: var(--brand-text-on-dark);
                font-family: var(--brand-body);
                font-weight: 700;
                font-size: 2.4cqw;">{{CLAUDE_BADGE}}</div>

    <!-- CHROME (pagination dots at bottom) — only if brand has chrome.pagination -->
    <div class="dots">
      {{#DOTS}}<span class="dot {{#ACTIVE}}is-active{{/ACTIVE}}"></span>{{/DOTS}}
    </div>
  </div>
</body>
</html>
```

### Key conventions

1. **Canvas is 1080×1350** (4:5 LinkedIn carousel). All `cqw` units are % of canvas width.
2. **Positioning is `position:absolute` + percentages.** Use bbox `[x, y, w, h]` directly in inline styles. No flex magic, no zone classes. This makes positions self-evident and editable by hand.
3. **Brand vars are CSS custom properties** loaded via `_shared/styles.css`:
   - `--brand-display`, `--brand-body`, `--brand-micro` — font families
   - `--brand-text-on-light`, `--brand-text-on-dark` — text colors
   - `--brand-accent`, `--brand-accent-secondary` — accent colors
   - `--brand-bg-light`, `--brand-bg-dark` — bg colors
4. **Sample text is the default in Mustache slots.** When the renderer doesn't get a value for `{{HERO}}`, render_template.py uses the sample defined in `instructions.md > slots > HERO.sample`. So previews look like the ref out of the box.
5. **One `.zone` div per text region.** Don't combine. If two pieces of text live in different bboxes, they get different divs.
6. **Inline styles for bbox + per-zone overrides** (font-size, alignment, opacity). CSS classes for type-role visuals (`.zone`, `.pill`, `.masthead`, `.dots`). Mixing both is fine — inline is the per-zone exception, CSS is the per-brand default.
7. **Font-size uses `cqw` (container-query width).** This scales the text proportionally to the canvas regardless of render resolution. Avoid `px` for typography.
8. **Opacity goes on the zone div** as `opacity: 0.3` inline when the ref shows faded/ghostly text (e.g., a large background word at low opacity that anchors the slide visually).
9. **Z-stacking for depth illusions:** when text needs to appear OVER a foreground subject in the bg (e.g., a large display word crossing a person photographed in the cleaned bg), use `z-index: 10` on that zone. Default zones are z-index 1. **An editable HTML TEXT slot must NEVER be placed UNDER an OPAQUE AI/photo image zone (a lower z-index than an overlapping `data-zone="photo"` image).** An `edit-from-ref` image is an opaque rectangle (GPT edit mode strips transparency), so it BURIES the text — the headline reads as an image and stops being click-selectable in the editor (the run-09 `preview-cards-cover` miss; gated by `check_buried_headline.py`). A text slot stays visually ON TOP (higher z-index) or in a CLEAR zone. The image-over-type "woven" overlap is allowed ONLY for a transparent-background cutout (the cutout corollary in `craft/ai-prompt-craft.md`) or a `mix-blend-mode` actually authored in the CSS (a declared-but-not-honored blend mode does not count) — otherwise keep the woven type AI-baked (`scenarios/c-integrated-text.md`).
10. **Triple-brace `{{{SLOT}}}` for HTML-bearing slots, double-brace for plain text.** Any slot that can carry inline markup — `<mark>` (accent word), `<br>` (line break), `<em>`/`<strong>` (emphasis) — uses **triple-brace** so the renderer passes the HTML through raw. Double-brace `{{SLOT}}` HTML-escapes the value, so `<mark>word</mark>` would render as the literal characters. Default headline / subhead / hero / body / CTA slots to triple-brace; keep plain-text-only slots (numerals, dates, handles, page indicators) on double-brace. The `mark` rule lives in `_shared/styles.css` — it is **surface-aware**: accent color on a light surface, inverting to the on-dark/paper color on accent/dark surfaces (driven by the slide's `data-surface`, see #12) so the marked word never goes accent-on-accent invisible — see `shared-styles-template.css`.
12. **`data-surface` on the slide root — the mark/contrast hook.** The root `.slide` MUST declare its background family via `data-surface`: `"light"` (paper / `--brand-bg-light` bg — the default), `"dark"` (`--brand-bg-dark` or a dark photo scrim), or `"accent"` (solid `--brand-accent` fill, e.g. an all-caps CTA). CSS can't read an inline `background:` value, so this attribute is what lets `_shared/styles.css` flip the surface-sensitive `mark` color (accent on light; on-dark/paper on accent+dark) without per-template hand-editing. Set it to match whatever the slide's `background` resolves to.
11. **Stable zone handles (`data-slot`) — required for the interactive editor.** Every editable zone div MUST carry `data-slot="<NAME>"` where `<NAME>` is the Mustache slot key the zone renders (strip `_PATH`/`_HTML`/`_SRC` suffixes for image zones: `PHOTO_MAIN_PATH` → `data-slot="PHOTO_MAIN"`). This is the contract that `render_template.py --tweaks` and the live-HTML editor key overrides by. Chrome zones (masthead, dots) also carry `data-slot`. Existing templates without this attribute can be migrated mechanically with `00-social-content/scripts/gates/migrate_data_slots.py`.
14. **Full-bleed AI composition = ONE editable `data-slot="PHOTO_MAIN"` full-bleed image.** When the whole slide IS a single AI-generated image (the entire canvas is the composition, with HTML text floating on reserved zones), author that image as **one full-bleed `<img>` carrying `data-slot="PHOTO_MAIN"`** — it is the editable hero/AI layer (Edit-with-AI / replace / magiclayer key off this slot). Two anti-patterns are banned: (a) wrapping the full-bleed AI `<img>` in a non-`data-slot` decorative wrapper (a `composition-frame` / `card-zone-marker` / any `frame`-class div) — the editor would read that wrapper as a non-editable FRAME shape and the image would stop being editable; (b) authoring a SECOND, redundant `data-slot="PHOTO_MAIN"` zone (typically an invisible `opacity:0` marker) that binds the SAME image path — it surfaces as a phantom empty slot in the editor. **One `PHOTO_MAIN` per template, max**, and it is the visible full-bleed image itself, not a wrapper around it. (The editor self-heals legacy templates that violate this — `preview_editor._collapse_fullbleed_ai` — but new templates must be authored the canonical way.) **The hero / post-subject AI image MUST bind its source to the `{{…_PATH}}` SLOT, never to a static asset path.** A post-subject element — whether an `<img src="{{PHOTO_MAIN_PATH}}">`, or a div whose `style="background-image:url('{{PHOTO_MAIN_PATH}}')"` — binds the **Mustache placeholder** that render-time substitution fills with the POST's image. Authoring it with a hardcoded relative path instead (`<img src="_ai_bg/photo_main.png">`, `background-image:url('_ai_bg/photo_main.png')`) is a defect: the placeholder is what gets substituted per post, so a static `src`/`url()` is NEVER substituted and every post renders the TEMPLATE's demo background instead of its own image (the "post ships the template demo" class). The static `_ai_bg/…` file is the template's *demo* asset only (it backs `assets/ref-canonical.png` / the approval preview) — it is never the binding the shipped template carries. The rule is mechanical: a `data-slot`-bearing post-subject image binds `{{<SLOT>_PATH}}`, not a literal `_ai_bg/…` path.
13. **Registration rule — an overlay that must REGISTER with live content never uses predicted canvas coordinates.** A mark that must align with a specific word / line / element of a live text slot (a circle around a word, an underline, a caret) is NEVER positioned by predicted absolute canvas `%` — the content reflows per post and the prediction misses. The overlay SHARES GEOMETRY with its anchor: make it a DOM child of (or sized by) the anchor's box, overshoot in `em` units, `preserveAspectRatio="none"` when the SVG must stretch with the box. If the anchor is AI-baked, render the mark in the SAME AI layer — or share the literal reserved numbers via `_measurements.yaml`. (The run-06 quote-circled miss: a hardcoded ellipse at predicted canvas coordinates missed the word "clarity".)

---

## instructions.md — anatomy

This is the **spec sheet** of the template. Both human-readable (user opens and understands the template) and machine-readable (render_template.py uses the slot definitions).

```markdown
# Template: <slug>

source_ref: ../../../visual_refs/<ref-name>.png
canvas: 1080x1350 (4:5 LinkedIn carousel)
strategy: html-overlay   # OR ai-edit-fallback OR mixed

## Inventory

The strict enumeration of what's visible in the ref. Validator (`validate_brand.py`)
reads this block to enforce Gates G1 (decision-reason) and G3 (photo-zone presence).
Write this BEFORE template.html — without enumeration, drift happens.

\`\`\`yaml
ignore_screenshot_chrome:
  - carousel-dot-indicators-at-very-bottom-edge (S1 rule)
  - browser-scrollbar-on-right
  - left-right-carousel-arrows

bg_treatment:
  kind: textured-paint  # See "Background route decision" section. Values:
                        #   scene-with-figures (Route 1) — people/products/photo backdrop
                        #   textured-paint     (Route 3) — analog texture CSS CAN'T reproduce
                        #   pure-typography    (Route 2) — text on simple bg CSS CAN reproduce
                        #   solid-color        (Route 2) — flat single color
  has_baked_overlays: true
  needs_clean_ref: true
  cleaned_bg_path: _ai_bg/bg.png

# G3 — set requires_photo_zone:true when ref has photo, silhouette, cutout,
# scene-with-figures, or full-bleed POV photo. If true, template.html MUST contain
# at least one element with class containing "photo-zone", id starting with "photo-",
# or data-zone="photo". If false AND ref carries photo elements, set zone_skip_reason
# with a non-banned reason (validator rejects cost/easier/faster/CSS-only/etc).
requires_photo_zone: true
photo_zones:
  - kind: silhouette-shadow  # OR: full-bleed-bg, cutout, embedded-photo, hero-overlay
    bbox: [10, 30, 80, 60]
    source: clean_ref         # OR: ai-gen-on-demand, user-uploaded-asset
    notes: "low-opacity silhouette of seated figure behind body text"

elements:
  - name: numeral-5
    bbox: [5, 8, 12, 11]
    type: pill
    shape: rounded-square  # NOT circle, NOT rectangle — observe carefully
    content: "5"
    decision: slot          # render via HTML overlay; NUMERAL slot
    notes: "white bg, coral text, ~1:1 aspect ratio"

  - name: italic-preamble
    bbox: [5, 24, 90, 8]
    type: text
    content: "<italic preamble sample>"
    decision: slot          # HERO_ITALIC slot
    style_observed:
      font_appears: italic-serif
      color: white
    brand_font_resolution:
      use: "Inter, italic"
      reason: "Brand declares no italic-serif; using Inter italic preserves editorial cadence without inventing a font"

  # Example of a skip-like decision — G1 requires >=20-char reason that is NOT
  # one of: cost / easier / faster / skip-photo / CSS-only / deterministic / save-API
  - name: decorative-grunge-splatter
    bbox: [80, 5, 18, 12]
    type: vector
    decision: skip
    reason: "User chose minimalist variant of the brand; decorative splatter is removed from all body slides per brand variant rules."

chrome_observed:
  masthead_visible_in_ref: false
  pagination_dots_visible_in_ref: false
  page_indicator_visible_in_ref: true
\`\`\`

## Visual summary

> **The `## Slots` block enumerates EVERY text slot the template.html declares — no gaps.** Every `data-slot` text zone in `template.html` gets exactly one `## Slots` entry; an un-enumerated slot is a Template-Card hole (the user opens `instructions.md` and a rendered zone is undocumented). When the slots are a numbered series (`LINE_1`, `LINE_2`, …), keep the numbering CONTIGUOUS to the slots that exist — if a zone is dropped or renamed (e.g. one line becomes a `CONNECTOR`), RENUMBER the remaining lines so the series has no gap (`LINE_1`, `LINE_2`, `LINE_3` — never `LINE_1`, `LINE_2`, `LINE_4` with `LINE_3` missing). The contract is mechanical: the set of `## Slots` entries equals the set of text `data-slot` handles in the HTML, and a numbered series is gap-free. (Gate: `run_template_qa.py` Step 4b.)

One paragraph: what does this template look like? When would I use it?

Example: "Coral solid bg with a numbered pill (top-left), display-italic + display-bold headline (upper-middle, left), body paragraph (middle), and a brand-accent CTA pill (bottom). Use for numbered insight slides in a series carousel."

## Slots

- **NUMERAL** — single digit, the slide index in a numbered series (e.g., "5")
  - bbox: 4% 8% 12% 10%
  - style: display-bold, 12cqw, white on coral
  - sample: "5"

- **HERO** — italic preamble
  - bbox: 4% 22% 92% 7%
  - style: display-italic, 8cqw, white on coral, left-align
  - sample: "<italic preamble sample>"

- **HEADLINE** — main bold display
  - bbox: 4% 30% 92% 11%
  - style: display-bold, 9cqw, white on coral, left-align
  - sample: "<bold headline sample>"
  - max_chars: 60 (auto-shrink to 7cqw if longer)

- **BODY** — body paragraph
  - bbox: 4% 47% 92% 22%
  - style: body, 2.4cqw, white on coral, left-align, supports `<br>` and `<strong>`
  - sample: "<body paragraph sample…>"

- **CALLOUT_PILL** — bottom CTA
  - bbox: 18% 88% 64% 8%
  - style: pill, brand-accent fill, white text, display-bold 2.8cqw
  - sample: "<CTA punchline sample>"

## Strategy notes

- All zones are html-overlay. No ai-edit needed.
- Chrome injected: masthead (top, 3 slots) + carousel dots (bottom).
- Bg is solid coral via CSS — no bg.png file.

## Fixed elements (not slot-editable)

- The coral bg color comes from the brand's accent color
- The numeral pill shape (circle) is hardcoded

## Possible future variations

- Allow user to override the pill fill color (currently locked to accent)
- Allow the body sample text to be paraphrased per slide
```

### Strategy field values

- **`html-overlay`** — all text zones render as HTML divs over bg.png (or CSS bg). Most common.
- **`ai-edit-fallback`** — html-overlay by default, but if user rejects the preview, re-render via `gpt-image-2 edit` on bg.png with the slot text baked in (for cases like text on a blackboard, where HTML overlay looks flat).
- **`mixed`** — some zones html-overlay, others ai-edit. Annotate per-zone in the slot description.

### Bbox notation

Always `x% y% w% h%` (4 numbers, % of canvas). Both in instructions.md (`bbox: 4% 22% 92% 7%`) and template.html inline style (`left:4%; top:22%; width:92%; height:7%`). Same numbers.

### When `_measurements.yaml` exists, it is the POSITION CONTRACT (fix the kraft top-anchored miss)

When a template carries a `_measurements.yaml` with per-block bboxes (masthead, line1, line2, body, wordmark…),
**each block is positioned `absolute` to its measured bbox** — that file is the contract for WHERE each block
sits, read from the ref, not a guess. The kraft miss collapsed the measured bboxes (masthead 2%, line1 10%,
line2 32%, body 60% width 70%, wordmark 97%) into a single `display:flex; flex-direction:column;
justify-content:flex-start` column → everything stacked at the TOP and the lower canvas went dead. The bbox
contract is what spreads the blocks down the canvas the way the ref does.

> **The rule (agnostic):** when `_measurements.yaml` exists, it is the position contract — author each block
> `absolute` to its bbox. A `flow` / auto-layout column is allowed ONLY if it lands each block within the
> tolerance of its measured bbox; a flow that top-anchors the stack (collapsing the vertical spread) violates
> the contract. (This is the per-zone *position*; **within** a zone, flow still owns the fine layout — see
> `craft/html-craft.md` §1. The two are compatible: the ZONE's position comes from the measured bbox; flow
> distributes content inside it.) The r6g Check-B dimension check flags a rendered block whose bbox drifts
> outside the `_measurements.yaml` tolerance.

---
