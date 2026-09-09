# Template conventions — background route, chrome, validation, anti-patterns, brand formats

> Slice of `template-conventions.md`. Read at **Step 2.5** (brand-context substitution / route) and the validation gates.

## Background route decision (apply BEFORE writing inventory)

**Pure CSS is the EXCEPTION, not the default. ANY sign of texture means it's NOT CSS anymore.**

This rule is the most-violated decision in the pipeline. Sub-Claude tends to look at a ref, see "mostly text, some bg noise", and decide CSS noise filters can replicate it. They almost never can — and even when they sort-of can, the result reads as digital sterile noise instead of the brand's analog/editorial signature.

The acceptance test for pure-CSS routes (`pure-typography`, `solid-color`) is **far stricter** than it sounds:

- ✅ **`solid-color` only when the bg is 100% one uniform color.** Eyedropper at 5 different spots returns identical hex. Zero gradient, zero noise, zero grain, zero edge fading. Examples: a flat coral wall, a clean white card with crisp edges, a solid black panel.
- ✅ **`pure-typography` only when the bg is solid OR a simple flat gradient with zero noise.** Like a Tailwind preset gradient. If you can see ANY grain when zoomed, it's not this route.
- ❌ **Paper-grain, scan lines, photocopy feel, dust marks, fading edges, halftone print, aged/torn paper, organic non-uniform noise → NEVER pure CSS.** No matter how clever the `feTurbulence` filter, CSS produces uniform DIGITAL noise. The brand's signature is the ANALOG directional artifacts. They look different. They feel different. CSS cannot replicate them.
- ❌ **Anything with people, products, scenes, photos, illustrations, screenshots → never pure CSS** (that's Route 1).

**Decision table.** Walk top-to-bottom; the FIRST matching row wins. Pure-CSS routes are at the bottom because they're rare.

| If the ref shows … | Then kind = | Route | clean_ref.py? |
|---|---|---|---|
| people, products, scene objects, building, brick wall, photo backdrop, silhouette | `scene-with-figures` | **1** | yes — clean the scene |
| paper-grain, scan lines, photocopy artifacts, dust marks, fading edges, halftone print, aged/torn paper, organic non-uniform noise — **any sign of texture** | `textured-paint` | **3** | **yes** — bg.png IS the texture |
| (rare) flat single color, no texture, no gradient, eyedropper confirms 100% uniform | `solid-color` | **2** | no — `background: var(--brand-bg)` |
| (very rare) clean flat color OR simple gradient, **zero noise/grain visible at any zoom level** | `pure-typography` | **2** | no — CSS only |

**The CSS-reproducibility test, sharpened.**

Don't ask "could CSS get close?". Ask:

> Is the bg 100% one solid color (or a simple gradient with literally zero noise)? Zoom into the ref at 200%. Do you see ANY pattern, ANY variation, ANY grain? If you see anything other than the same color, it's NOT a pure-CSS route.

**Default for ambiguity = `textured-paint`.** When you're not sure, you're wrong about it being CSS. Bias hard toward Route 3.

**Cost of choosing wrong:**
- Wrong CSS → wrong (your brand-signature texture is gone forever)
- Wrong textured-paint → $0.04 spent on a clean_ref call that produced a flat bg you could have done in CSS

The asymmetry says: when in doubt, choose textured-paint. The downside of false-textured is a few cents. The downside of false-CSS is the brand reads off-brand on every slide.

**Failure mode this prevents.** When refs carry paper-grain texture with silhouette photos behind body text and get classified as `pure-typography` ("the text is the main thing, bg is just texture, CSS noise will do it"), the templates ship as 100% CSS — brand-signature paper grain gone, silhouettes gone, output reads as a generic SaaS deck. The few cents saved on AI gen destroy the entire visual identity. **This is exactly what this section exists to prevent.**

---

## When the ref has a photo / person / scene (scene-template route)

1. **clean_ref.py** generates `_ai_bg/bg.png` (cleaned via gpt-image-2 edit, with your prompt).
2. template.html uses `background-image: url('_ai_bg/bg.png');`.
3. Text zones overlay on top of the bg.

Worked example for <ref-name> (the figures in the ref + <creator-tool pill> + system text):
- bg.png = the figures in the ref + brick wall, cleaned (your prompt removed "<a methodology name>" text, removed <creator-tool pill>, repainted orange accent → brand coral)
- HERO zone over the upper-half ("<a methodology name>" can be re-typed by user)
- CLAUDE_BADGE pill div positioned between the figures (16% × 6%, center)

## When the ref is pure typography on texture/color (no scene)

1. NO clean step. Skip clean_ref.py.
2. template.html uses CSS bg: `background: var(--brand-bg-light);` or layered gradient + noise.
3. Text zones overlay on the CSS bg.

Worked example for <ref-name> (coral wall, numbered pill, headline + body + CTA pill):
- bg = `background: var(--brand-accent);` (CSS solid)
- 5 zone divs for: numeral pill, hero italic, headline bold, body, CTA pill

## When the ref needs a complex bg you can't approximate in CSS (textured paper that pure SVG noise doesn't capture)

1. clean_ref.py with prompt that ASKS for the texture: "Generate a clean version of this paper-grain background. Remove all text. Preserve the warm cream tone and the subtle grain noise. Output 1080x1350."
2. template.html uses `background-image: url('_ai_bg/bg.png');` even though there are no scene subjects — the bg IS the texture.

---

## Chrome auto-inject (STRICT — honors tokens.json verbatim)

Chrome blocks (masthead row at top, pagination dots at bottom, optional brand wordmark) are CONDITIONAL based on the brand's `tokens.json > chrome` config AND the per-template `chrome_observed_in_ref` flag in the inventory.

**The matrix:**

| `tokens.chrome.masthead.enabled` | `chrome_observed.masthead_visible_in_ref` | Result in template.html |
|---|---|---|
| true | true | masthead `<div>` INCLUDED with `{{MASTHEAD_LEFT}}` / `{{MASTHEAD_CENTER}}` / `{{MASTHEAD_RIGHT}}` slots |
| true | false | masthead `<div>` ABSENT — this specific ref doesn't carry masthead even though brand has it globally |
| false | true | masthead `<div>` ABSENT — brand globally disabled it; ignore ref evidence |
| false | false | masthead `<div>` ABSENT |

Same matrix for `chrome.pagination` ↔ `chrome_observed.pagination_dots_visible_in_ref`.

**Critical rules:**

- **When chrome is disabled, the `<div>` is REMOVED from template.html — not emptied with placeholder text.** A `<div class="masthead"></div>` with empty content still occupies layout space and reads as a broken chrome bar. If chrome is off, the markup is GONE.
- **NEVER hardcode chrome content** like `<div class="masthead"><span>GROWITHALEX</span></div>`. Always use `{{MASTHEAD_*}}` Mustache placeholders that read from tokens at render time. Hardcoded chrome means changing the brand name requires editing every template.
- **The matrix overrides ref observation.** If `tokens.chrome.masthead.enabled:false`, the template MUST NOT render masthead — even if the ref is a screenshot that clearly shows a 3-slot masthead row at the top. The user opted out at brand level; that decision wins.
- **Carousel viewer UI ≠ slide chrome.** Carousel-viewer pagination dots, arrows, and scroll-bars at the very bottom edge of LinkedIn/Instagram screenshots are screenshot artifacts, NOT slide design. Set `chrome_observed.pagination_dots_visible_in_ref: false` for these — they were the viewer's UI, not the slide's content.

**Validator enforcement (Gate G6):** `validate_brand.py --template-dir <path>` checks:
- If `tokens.chrome.masthead.enabled:false` AND template.html contains `<div class="masthead">` (uncommented) → FAIL
- If `tokens.chrome.pagination:null` AND template.html contains `<div class="dots">` (uncommented) → FAIL
- If template hardcodes brand text inside masthead/pagination (no Mustache placeholders) → FAIL

If the user later wants a brand-wide chrome change, edit `tokens.json > chrome` ONCE; every template that uses Mustache placeholders picks it up at next render.

---

## Anti-patterns (these have all happened in production — do not repeat)

### Brand-fidelity violations

- ❌ **Adding a font that is NOT in tokens.json > fonts.** If the brand declares `Inter Tight + Inter`, you MUST NOT add Fraunces, Playfair, Geist, etc. — even if the visual ref appears to use one. The ref is from OTHER brands; the brand's font catalog is final. If the ref shows italic-serif but the brand only has `Inter`, use Inter italic (`font-style: italic` on the Inter family) — never substitute a serif. **Why:** adding a serif font to a brand whose tokens only declare sans-serif produces "almost-on-brand" output that reads as a different studio's work.

- ❌ **Copying elements between templates in the same pool.** Each template extracts from EXACTLY ONE ref (one builder per ref). If ref-A has a CTA pill and ref-B does not, template-B does NOT get a CTA pill — no matter how much it would "complete" the design. **Why:** copying a CTA pill from one template into another whose ref had no such pill silently invents chrome the brand never used.

- ❌ **Adding chrome from `tokens.json > chrome` when this ref doesn't show it.** The brand may have a 3-slot masthead declared globally, but a specific ref might NOT have one. Chrome auto-inject is OFF by default per template; opt-in by adding `<!-- chrome: masthead -->` and `<!-- chrome: dots -->` markers in template.html only when the ref clearly carries them.

- ❌ **Treating carousel-viewer UI as slide chrome.** The pagination-dot row at the very bottom edge of a LinkedIn/Instagram screenshot is **the viewer's UI, not the slide's design**. S1 rule (clean-prompt-patterns.md) says ignore. **Why:** rendering pagination dots the ref never had bakes the carousel viewer's progress indicator — accidentally captured in the user's screenshot — into the slide design.

- ❌ **Classifying paper-grain / scan / photocopy textures as `pure-typography`.** The texture IS the brand signature — CSS noise filters (`feTurbulence`, fractal, gradients) produce uniform digital noise, NOT the organic directional artifacts (scan lines, fading edges, dust marks) of an analog scan. Apply the CSS-reproducibility test in "Background route decision" above: if 5-10 lines of CSS can't get within 90% of the ref's bg, it's Route 3 (`textured-paint`), not Route 2. **Why:** classifying an editorial paper-grain ref as `pure-typography` + CSS noise loses the entire editorial-zine signature — it renders as generic gray noise on white.

- ❌ **Recreating photorealistic / AI-illustrated subjects using CSS or SVG shape primitives.** When the ref's main subject is a 3D-rendered character, a photorealistic product, an AI-generated illustration, or anything that fails the **Subject Reproducibility Test** (`ssc-template-builder.md > Step 0`: "could I recreate this with ≤10 shapes WITHOUT losing recognizability?"), the template MUST use an `<img>` slot — never `<svg>` paths or nested `<div>` rectangles. **Why:** recreating a photorealistic 3D-rendered subject (say, a robot in a business suit with red hand-drawn sketch annotations) out of grey `<div>` rectangles, circle eyes, and a line antenna destroys the brand-signature photorealism and drops the sketch overlay — the result is a child's drawing in place of the brand's editorial 3D aesthetic. Rule: if the subject's source is AI gen / photo / 3D render, the template carries a `<img src="{{PHOTO_*_PATH}}">` slot AND `manifest.json[id].ai_image_prompt` populated from `ai-image-style.md > prompt_template`. The render pipeline (HYBRID_AI v3 in `render_template.py`) fills the slot at render time.

- ❌ **Generating only PURE_CSS templates when `moves.md` catalogs photo moves.** If any move in `moves.md` has a `<!--meta-->` block with `image_bearing: true` (silhouette, cutout, photo-overlay, scene-backdrop, etc.), the template manifest MUST contain ≥1 ready template with a photo-zone slot. Documenting a move you can't render is worse than not declaring it — downstream agents (`ssc-designer`) filter templates by move support, find zero matches, and fall back to generic output. **Why:** when refs with photo/silhouette/cutout elements get compressed to PURE_CSS typographic templates because "deterministic is cheaper", a move like "Desaturated silhouette photography" declared in moves.md ends up with zero supporting templates — and output goes off-brand on every photo slide. **Gate G2** enforces this mechanically — but the rule applies even before the gate trips: if you find yourself thinking "I'll skip the photos to keep it CSS-only", STOP.

### Process violations

- ❌ **Marking an element `decision: skip` or `decision: simplify` with a cost/speed-driven reason.** Banned tokens (caught mechanically by Gate G1): `cost`, `cheap`, `expensive`, `easier`, `faster`, `quick`, `skip-photo`, `CSS-only`, `deterministic`, `save-API`, dollar/cent amounts. The element's decision drives whether your template captures the brand's signature or strips it. Cost is NOT a brand-fidelity reason. Acceptable reasons reference a brand-level rationale: "user chose minimalist variant", "element is screenshot chrome not slide design", "ref was corrupted in that region". Minimum reason length: 20 chars. **Why:** marking a silhouette photo behind body text as `decision: skip` with `reason: "deterministic is cheaper than clean_ref"` ships a template without the silhouette — the brand-signature feel is gone, and the few cents saved destroy the brand-fidelity payoff.

- ❌ **Writing template.html without first writing the `## Inventory` block in `instructions.md`.** Without enumeration, drift happens — you'll add things "that look like they belong" but aren't in the ref. The inventory is the contract: if an element isn't in the inventory, it CAN'T be in the template.html.

- ❌ **Rendering preview without composing a `_comparison.png` (ref + preview side-by-side).** Reading ref and preview separately misses obvious mismatches because the eye averages between reads. Compose the side-by-side, then read THAT.

### Hard-rule violations (visual)

- ❌ Building complex flex/grid layouts to "be responsive". The canvas is fixed 1080×1350. Use absolute positioning.
- ❌ Hardcoding hex colors in template.html. Always use `var(--brand-*)`. The brand kit substitutes at render.
- ❌ Defining new CSS classes per template. Use the shared ones (`.zone`, `.pill`, `.masthead`, `.dots`). If a template needs something the shared classes don't cover, propose adding to `_shared/styles.css` (one-time addition, then reused).
- ❌ Re-extracting fonts from the ref. Fonts come from brand_kit, period.
- ❌ Treating instructions.md as just docs. The render_template.py reads it for slot defaults and strategy routing.

---

## Validation gates (single validator runs all four)

One script enforces every mechanical gate:

```bash
# Per-template gates G1 (reason) + G3 (photo-zone contract)
uv run .claude/skills/mkt-visual-identity/scripts/validate_brand.py \
    --template-dir brand_context/templates/{pool}/{slug}/

# Brand-level gates G2 (moves vs templates) + G4 (moves.md meta sanity)
uv run .claude/skills/mkt-visual-identity/scripts/validate_brand.py \
    --brand-context brand_context/

# Combined pre-promotion check
uv run .claude/skills/mkt-visual-identity/scripts/validate_brand.py \
    --brand-context brand_context/ \
    --template-dir brand_context/templates/{pool}/{slug}/
```

**G1** reads the `## Inventory` YAML in `instructions.md`. Any element with `decision: skip` / `simplify` / `drop` / `omit` requires a `reason:` ≥20 chars that does NOT match the banned regex (`cost`, `cheap`, `easier`, `faster`, `quick`, `skip-photo`, `CSS-only`, `deterministic`, `save-API`, dollar/cent amounts).

**G3** also reads the `## Inventory` block, then matches `template.html` against three photo-zone patterns:
- `class` attribute containing `photo-zone`
- `id` attribute starting with `photo-`
- `data-zone="photo"`

If `requires_photo_zone: true`, ≥1 match is required. Inconsistencies also fail: `scene-with-figures` bg + `requires_photo_zone:false`; populated `photo_zones[]` with the flag off; photo elements in the ref + flag off + no `zone_skip_reason`.

**G4** parses `brand_context/visual-identity/moves.md` looking for `<!--meta ... -->` HTML comment blocks under each `## N. ...` section heading. Each block must parse as YAML and provide at minimum `name` (kebab-case slug) + `image_bearing` (bool). When `image_bearing: true`, `required_zone_types` must be a non-empty list of recognized tokens.

**G2** cross-checks: every `image_bearing: true` move must have ≥1 template (status `ready`, or `ready+draft` with `--include-draft`) whose `supports_zone_types` intersects the move's `required_zone_types`. The fallback for manifests without `supports_zone_types`: any template with `image_zone != "none"` is treated as supporting `photo-zone`.

The art-director QA gate calls the per-template invocation before composing the side-by-side preview. The brand-level invocation runs in Phase 5.5 (between Phase 5 template-builder loop and Phase 6 PDF regen). The failure mode where refs with photo/silhouette/cutout get compressed to PURE_CSS templates is now structurally blocked.

### ai-image-style.md format *(brand AI image contract)*

`{brand_context}/visual-identity/ai-image-style.md` captures the brand's AI image style ONCE per brand. Subsequent templates and `ssc-image-generator` content runs read this file to produce visually-consistent AI imagery across the brand.

Same pattern as `moves.md`: human-readable markdown with one `<!--meta-->` HTML comment block holding the machine-readable contract.

```markdown
# AI Image Style — <Brand Name>

<!--meta
default_medium: photorealistic-3d-render  # the brand's MOST-COMMON medium — a soft default, NOT a brand-fixed law.
                                          # OR: flat-illustration | watercolor | sketch | mixed.
                                          # Set `mixed` when the brand's refs span >1 medium (e.g. a photo cover
                                          # + a cartoon body). The medium each template ships is READ from THAT
                                          # template's ref; `default_medium` is the fallback only when the ref's
                                          # medium is genuinely ambiguous.
palette:                     # IDENTITY — brand-wide, applies to every template
  - "#FFFFFF (bg)"
  - "#888888 (subject base)"
  - "#E2473D (accent)"
grain: matte-flat            # IDENTITY — the brand's paper/surface feel (matte-flat | fine-film-grain | clean-digital | …).
                             # Promoted to its own key (was implicit in the prose) so the identity cues are read structurally.
text_policy: html-overlay    # ROUTING (not style, not identity) — "all type is HTML/overlay" on this brand; the anchor the
                             # treatment gate (check_treatment_contract.py Check 6) cites. Stays brand-wide. OR: ai-allowed
                             #   when this brand genuinely bakes integrated type.
default_lighting: studio-flat-soft   # FALLBACK only — the brand's most-common lighting. The lighting each template ships is READ
                                     # from THAT template's ref (its block's image_style.lighting); this is used only when the ref
                                     # is ambiguous. OR: dramatic | natural | none.
default_subject_treatment: isolated-on-light-bg   # FALLBACK only — same posture as default_lighting; per-template the treatment is
                                                  # read from the ref. OR: full-bleed | inset-with-shadow | cutout.
typical_subjects:            # IDENTITY (weak) — the brand's recurring subjects; informational
  - robot
  - tech-object
  - character
aspect_ratio: "1:1"   # most-used; per-template can override
prompt_template: "{subject}, <brand palette>, <brand grain>, square aspect"
                 # IDENTITY-ONLY template — the brand-wide cues that apply to EVERY image: palette + grain (+ aspect).
                 # The STYLE (medium / lighting / subject_treatment) is intentionally NOT here — it enters per-template from the
                 # ref, via the block's `image_style` (the builder reads it from the ref; the image-generator concatenates
                 # identity → style → delta). Do NOT hard-code a single medium's opener ("Photorealistic 3D-rendered …", a
                 # "studio-flat-soft" lighting clause) here — that would re-impose one style on every template (the run-07 cause).
annotation_overlay:
  enabled: true
  style: hand-drawn-sketch
  color: var(--brand-accent)
-->

## Style description

One paragraph describing the brand's AI image aesthetic in plain prose. What makes a slide image read as "on-brand"? What does the eye notice? Describe the IDENTITY the brand fixes (palette, accent, grain) first — that is the brand-wide floor. The STYLE (medium / lighting / treatment) varies per template, read from each ref; when the brand spans several (e.g. "covers are documentary photographs; explainer bodies are flat vector cartoons"), describe the range rather than forcing one.

## Generation guidelines

- Subject: always include `{subject}` placeholder when generating; fill per-slide.
- Brand IDENTITY cues (brand-wide): <fixed palette / accent / grain — these the brand DOES fix on every image>.
- STYLE (medium / lighting / subject_treatment): NOT fixed brand-wide. Each template's style is READ from its own ref into the block's `image_style` and may legitimately diverge (a cartoon ref ships a cartoon, a dramatically-lit ref ships dramatic light). The grade's `default_medium` / `default_lighting` / `default_subject_treatment` are the soft FALLBACK, used only when a ref is genuinely ambiguous. A field is fixed brand-wide ONLY when the brand is genuinely uniform on it.
- What to NEVER include: <e.g., depth-of-field, gradient backgrounds — palette/identity negatives>. Do NOT add a blanket STYLE-negative ("no illustration", "no photographs", "no dramatic shadows") when the brand spans more than one style — that negative would kill the templates whose ref legitimately is that style; style is the template's call, read from its ref.
- Annotation: apply the brand's hand-drawn sketch overlay AFTER AI gen completes. It's a MOVE (in `moves.md`), not part of the AI prompt.

## Per-template overrides

The brand fixes the IDENTITY — palette / accent / grain (and `text_policy`). The STYLE — `medium`, `lighting`, `subject_treatment` — is per-template, READ from the template's own ref into its `[ai-image-zone]` block's `image_style` (the builder writes it; see `ssc-template-builder.md` §2). `aspect_ratio` may also be overridden per template. When a template's ref diverges from a `default_*`, the template follows its ref and records why; the `default_*` keys are the fallback only when the ref is ambiguous. The identity fields (palette / accent / grain) stay brand-fixed.
```

**Who writes it:**
- `ssc-template-builder` Step 4 Case D-main — on FIRST encounter of an AI illustration ref. Inferred from vision analysis of that ref. Subsequent refs validate against it.
- User can hand-edit anytime. The skill never silently overwrites — divergent refs surface a popup.

**Who reads it:**
- `ssc-template-builder` (every template inherits the brand IDENTITY — palette / accent / grain; the **style** — medium / lighting / subject_treatment — each template ships is read from its OWN ref into its block's `image_style`, with the grade's `default_*` as the fallback when the ref is ambiguous)
- `ssc-image-generator` (content gen concatenates **identity** (palette / accent / grain, from this grade) → **style** (medium / lighting / treatment, from the template's `image_style`) → **delta** (the subject); the style comes from the template that runs, NOT this grade — see Step 5.8)
- `generate_brand_bible_pdf.py` (PDF includes an "AI image style" page in v2 regen — now an identity-only page; the per-template style is shown on each template, a follow-up)

**Why it exists:** without this artifact, every template + every content run re-infers the style from scratch — drift on every slide. With it, the brand has ONE source of truth for "what AI images on this brand look like".

### moves.md meta-block format

The brand's `moves.md` carries structured metadata inline — one `<!--meta-->` block per move section, right under the heading:

```markdown
## 1. Red Hand-Drawn Sketch Overlay *(THE signature move)*

<!--meta
name: red-hand-drawn-sketch-overlay
image_bearing: true
required_zone_types: [photo-zone, annotation-overlay]
keywords: [sketch, annotation, hand-drawn, arrow, circle]
-->

**Universal principle implemented:** functional decoration ...
```

Allowed `required_zone_types` tokens (kept in sync with the validator's whitelist):

| Token | Means |
|---|---|
| `photo-zone` | A slot for a real or AI-generated photo. |
| `silhouette-bg` | Background photo treated as silhouette (low-opacity, behind text). |
| `cutout` | Photo with bg removed, placed as a visual object. |
| `hero-overlay` | Hero slide with photo behind headline. |
| `illustration-overlay` | AI-generated illustration overlaid on the slide. |
| `annotation-overlay` | SVG annotation paths (sketches, arrows, circles) drawn on top. |
| `icon-zone` | Brand/tool/product logos rendered as SVG icons. |
| `text-zone` | Pure text content. |
| `pill` | Rounded callout pill. |
| `callout-card` | Framed inset card. |
| `page-indicator` | Carousel slide number indicator. |
| `masthead` | Top-edge editorial chrome row. |
| `dots` | Pagination dots row. |

A move is `image_bearing: true` when its rendering REQUIRES a non-text visual asset. Test: would the move still read correctly if the slide had ZERO photos / illustrations / screenshots? If yes → `image_bearing: false`. If no → `image_bearing: true`.
