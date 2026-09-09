# Template conventions — AI image zones (`[ai-image-zone:N]` block)

> Slice of `template-conventions.md`. Read at **Step 3** (generate) / **Step 4** (write the `[ai-image-zone]` block).

## AI image zones — what they are and how to declare them

An **AI image zone** is a rectangle in the template that holds an entire AI-generated composition at render time. The template provides the rectangle (position + size); the AI prompt generates everything inside it (subject, sketch overlays, supporting cards/callouts, decorative bg patterns, framing borders).

### What belongs inside an AI image zone vs as HTML template chrome

| Belongs in the AI image (one slot) | Belongs in HTML (template chrome) |
|---|---|
| The slide's subject (robot, cabinet, character, product) | Text zones (headline, body, captions) — Mustache slots |
| Sketch/marker overlay drawn on the subject | Brand-wide chrome from `tokens.json` (dot-grid corner, masthead, pagination, logo stamp) |
| Annotation card/callout with pill + text lines that supports the subject | Page indicator pill in a fixed brand corner |
| Arrow/leader line connecting subject and annotation | Framed body-card border (when defined as brand-wide in tokens) |
| Decorative bg pattern *inside* the illustration zone (graph paper, dots) | Slide bg color (`var(--brand-bg-light)` / `--brand-bg-dark`) |
| Hairline border *bounding* the illustration zone | — |

**The boundary test (THREE-WAY — the binary above is incomplete):** for each element ask two questions:

1. **Does it vary per post?** No → **HTML brand chrome** (fixed, unchanged every slide: masthead, creator wordmark, decorative marks, page indicator).
2. **If it varies — is it a third-party tool/brand logo, or the photographic/illustrated subject?**
   - Third-party tool/brand logo of *whatever the post is about* → **`brand-badge`** (HTML, but per-post — see below).
   - The photographic/illustrated subject → **AI image content** (generated inside the image zone).

### Third category — `brand-badge` (the per-post logo slot)

A `brand-badge` holds the logo of the **tool/brand the post talks about**. It is NOT there because the template is "about" that tool — it is there because the slot receives the logo of whatever the post is about. So it is HTML (a crisp vector mark) yet it **varies per post** — it fails the old binary's "appears UNCHANGED" test while still being HTML, not AI content.

Three distinct logo roles — do not conflate:

| Role | Varies? | How declared |
|---|---|---|
| **creator brand chrome** (the creator's own wordmark/logo) | fixed | HTML chrome, from `tokens.json` |
| **decorative mark** (a brand-owned ornament) | fixed | HTML chrome / a `moves.md` move with an original asset |
| **`brand-badge`** (third-party tool/brand the post is about) | **per-post** | HTML slot `{{BRAND_LOGO_PATH}}`, resolved per post |

**Briefing / inventory annotation for a brand-badge:**
```yaml
- kind: brand-badge
  slot: BRAND_LOGO_PATH
  variability: per-post
  resolution: commons lookup (by the post's subject tool) → fetch_icon.py → plain text
  desc: "logo of the tool/brand the post talks about"
  example: "Claude → commons/ai/claude.svg"   # canonical SUBJECT only — NOT the fixed slot value
```

The `example` is the **canonical subject** used for the preview, never the locked value. A post about Notion fills `BRAND_LOGO_PATH` with `commons/productivity/notion.svg`; a post about GitHub fills it with `commons/social/github.svg`; etc.

**The slot MUST end in `_PATH`.** The renderer only inlines image paths that arrive through a Mustache slot if the slot name ends in `_PATH` (`embed_paths_as_data_uris` keys on that suffix and runs BEFORE Mustache fill; `_inline_relative_urls` only catches LITERAL paths in the raw HTML). A badge slot named `BRAND_LOGO` (no `_PATH`) renders BROKEN. The path value may be absolute, template-dir-relative (`assets/x.svg`), or brand_context-relative — all three resolve.

**Asset paths resolve SLIDE-RELATIVE — co-locate the asset and point the slot at the LOCAL copy, never at a project-root commons path.** The renderer resolves a `_PATH`/`src` value against the **template (slide) folder first**, then `brand_context`. A value like `.claude/skills/viz-image-gen/references/icons/commons/ai/claude.svg` (project-root-relative) resolves under NEITHER base from the slide folder → the `<img>` src is broken and the glyph never paints (the run-08 overlay-cover Claude logo). The rule is mechanical and slug-agnostic: when `shared/icons.md` resolves a mark from commons, it is **copied into `{template_dir}/assets/{name}.svg`** AND the slot value / `sample:` is the **slide-relative `assets/{name}.svg`** — the commons path is only the *source* of the copy, never the value that ships. This holds for every brand/logo/SVG asset: the value the template carries is the co-located local copy.

**An SVG that must take a brand-color TINT must be INLINED — never `<img>`.** An SVG loaded via `<img src="…svg">` is an isolated document: the host `color: var(--brand-accent)` does NOT cascade in, so `fill="currentColor"` paints the SVG's own default (black) instead of the brand colour (the run-08 overlay-cover starburst shell shipped black). Inlining it as a data-URI `<img>` does NOT fix this — it is still an isolated document. So:
- A **single-colour pictogram that takes a brand tint** (a `currentColor` shell, a tinted mark) is authored as **inline `<svg>`** in `template.html` (or via CSS `mask`/`background`), with `fill`/`stroke` = `var(--brand-*)`, so the colour cascades. The render bake also enforces this generically — a literal `<img src="…svg">` whose SVG uses `currentColor` is auto-spliced to inline `<svg>` at render time (`render_template.py > _inline_tinted_svgs`) — but the TEMPLATE should author it inline so the intent is explicit.
- A **pre-coloured / multi-colour brand logo** (the Claude glyph, a client wordmark) already carries its own colours: keep it an `<img src="{{…_PATH}}">` and render it **as-is** — never tint it, never `filter:` it (see `shared/icons.md` "Brand seal composition").
The discriminator is the asset: tint-via-currentColor → inline `<svg>`; baked colours → `<img>`.

**Placement — never a hardcoded mock, never over the subject:**
- **Default (crisp):** HTML overlay `<img src="{{BRAND_LOGO_PATH}}">` at the badge bbox; per post the path is resolved by the commons→fetch→text chain. Keeps the logo vector-crisp.
- **Position the overlay bbox in a CLEAR zone**, not where the scene's subject lands. A full-bleed image template has a focal subject (a seated figure's head, a face) — a centered badge bbox collides with it (the Claude badge landed on the figure's head on the agent-view cover). When the template carries a full-bleed `image_zone` with a likely-centered subject, place the badge in a margin/corner or the calm upper band — never dead-center over the focal area. State the safe zone in the Template Card.
- **In-scene integration (better composition):** when the badge must sit *within* the photographic scene (so any fixed overlay position would collide with the subject), pass the resolved `BRAND_LOGO_PATH` as an ADDITIONAL `--input-image` to the edit-from-ref generation and instruct the prompt to place it naturally relative to the subject (on the laptop lid, a wall, a held card). Trade-off: the model may redraw the mark (less crisp) — use only when overlay reads as "pasted on". This is the deliberate exception to "no logos in the photo" (that rule blocks *hallucinated* logos; a `brand-badge` is an explicit, provided input).

Never bake the canonical example (e.g. Claude) as a fixed `<img>` — that is the "mocked badge" failure: the template would show the same tool on every post.

### `[ai-image-zone:N]` comment block — format

Every AI image zone in `template.html` requires a matching `[ai-image-zone:N]` comment block at the top of the file (above `<style>`, inside one HTML comment). One block per zone, numbered from 1.

**Structural principle: the canonical ref IS the composition guide AND the generation input.** The block declares a `generation_route`; the prompt states ONLY the delta. There are three routes (see `ssc-template-builder.md` Step 3 for the full decision tree):

- **Route A — `edit-from-ref`** *(default — image-zone with a variable subject):* the ref (`assets/ref-canonical.png`) is passed as `--input-image`; `prompt_delta` describes only the per-post subject + the template's fixed style. Generated per post.
- **Route C — `texture-extract`** *(textured bg, no variable subject):* `_ai_bg/bg.png` is generated ONCE at template creation by stripping the ref to its background texture. Fixed template asset — NO per-post generation. The output lands in `_ai_bg/` like every generated image — never loose at the template root. The extract `prompt_delta` puts every captured `distinctive_graphics` device on the PRESERVE line and scopes "remove/clean" to text/content blocks only — a blanket "no marks" is FORBIDDEN when `distinctive_graphics ≠ none` (see `craft/ai-prompt-craft.md` rule 5).
- **Route B — pure CSS** *(solid-color bg, no image-zone):* needs no block at all.

**Route A — `edit-from-ref`:**
```
<!--
[ai-image-zone:1]
slot_path: PHOTO_MAIN_PATH                                # Mustache slot the rendered image fills
generation_route: edit-from-ref
ref_input: assets/ref-canonical.png                       # the template's saved ref → --input-image (scene/medium/composition)
# identity_input: visual-identity/headshots/simon-pic.jpg # OPTIONAL (scene-restyle-with-real-face ROTA) — a SECOND --input-image
#                                                          #   carrying IDENTITY (a brand headshot, RESOLVED to a real path in the build,
#                                                          #   never a literal placeholder). Present only when a hero FACE carries the brand
#                                                          #   person; the generator passes it second (ref FIRST, identity SECOND). See
#                                                          #   craft/ai-prompt-craft.md "ROTA — scene-restyle-with-real-face".
brand_style_source: visual-identity/ai-image-style.md     # brand IDENTITY grade (palette / accent / grain) + the default_* fallbacks
subject_role: free-subject                                # fixed-hero | free-subject (identification-tree.md rule 7).
                                                          #   free-subject → "Change the subject to: {PHOTO_SUBJECT}" (the slug names the LAYOUT).
                                                          #   fixed-hero  → the hero IS the template identity (the slug NAMES the object, ONE dominant
                                                          #     ref subject): RECOLOR the ref, never swap the object — see the fixed-hero prompt_delta below.
image_style:                                              # THIS template's STYLE, read from its ref by the builder (NOT brand-wide)
  medium: flat-illustration                               #   the ref's medium (photo | flat-illustration | watercolor | sketch | 3d-render)
  lighting: natural                                       #   the ref's lighting (dramatic | natural | studio-flat-soft | none) — omit/leave blank → grade default_lighting
  subject_treatment: full-bleed                           #   the ref's treatment (isolated-on-light-bg | full-bleed | inset-with-shadow | cutout) — omit → grade default_subject_treatment
render_register: flat-illustration / natural / full-bleed # BUILDER-WRITTEN — the style the builder actually READ + baked into the prompt opener (echo of
                                                          #   image_style). It is a RECORD for the post-render conference + the by-eye review, NOT a gate:
                                                          #   if the generated image's style ends up different, the conference WARNS (style is judgment,
                                                          #   never a trava — Gustavo's principle). Lets a reader confirm "the prompt inherited the ref's
                                                          #   style", which is the run-07 services-billboard failure (grade opener overrode the ref).
output_aspect: 4:5

# --- free-subject prompt_delta (the default — the slug names the LAYOUT, the subject varies per post) ---
prompt_delta: |
  Same composition and layout as the reference. Change the subject to: {PHOTO_SUBJECT}.
  Open in the ref's STYLE (this block's image_style — medium / lighting / treatment) and keep the brand IDENTITY (palette / accent / grain, from brand_style_source).
  Keep the subject <position — e.g. seated lower-center>.
  No text, no logos, no saturated color. Portrait 4:5.

variables:
  - name: subject
    slot: PHOTO_SUBJECT                                   # Mustache slot ssc-designer fills (free-subject ONLY)
    description: the per-post subject that carries the scene
    example_values:
      - "two founders seated reviewing documents"
      - "a solo founder in a tailored jacket reviewing printed pages"
[/ai-image-zone]
-->
```

**Fixed-hero `prompt_delta` (`subject_role: fixed-hero` — RECOLOR the ref, never swap the object).** When the
hero is the template identity (the slug names the object), the per-post prompt keeps the object and recolors it;
there is **no free `PHOTO_SUBJECT` slot** (`craft/ai-prompt-craft.md` "Fixed-hero recolor vs free-subject swap"):
```
prompt_delta: |
  Keep the EXACT subject from the reference — a metal chain with one accent link (the template's fixed hero).
  Recolor only the accent element → brand coral; keep the object's form, material, and identity.
  Vary only framing, camera angle, lighting, and the surrounding scene per post.
  Open in the ref's STYLE (image_style) and keep the brand IDENTITY (palette / accent / grain). No text, no logos. Portrait 4:5.
variables:
  - name: framing                                         # fixed-hero varies FRAMING, never the object category
    slot: SCENE_FRAMING
    example_values:
      - "the chain coiled on a soft-lit surface"
      - "a close crop of the single coral link"
```
> ❌ A `fixed-hero` with `"Change the subject to: {PHOTO_SUBJECT}"` and example values that are *different
> objects* ("neural node / AI chip / robotic hand") is the `chain-highlight-headline` defect — the chain
> (identity) became gears. The gate (r6g) hard-fails an object-hero regenerated into a different object.

**Route C — `texture-extract`:**
```
<!--
[ai-image-zone:bg]
generation_route: texture-extract
ref_input: assets/ref-canonical.png
output: _ai_bg/bg.png
generated: once-on-template-creation
[/ai-image-zone]
-->
```

### How the runtime uses these blocks

1. `ssc-designer` plans the slide and fills the Mustache slot values for the zone's `variables` (e.g., `AI_SUBJECT="filing cabinet"`, `ANNOTATION_LABEL="Memory"`).
2. `ssc-image-generator` parses every `[ai-image-zone:N]…[/ai-image-zone]` block in `template.html` via regex. For each:
   - Reads `generation_route` and branches:
     - `edit-from-ref` → load the **identity** cues (palette / accent / grain) from `brand_style_source` AND this block's **`image_style`** (medium / lighting / subject_treatment, the template's own style — falling back to the grade's `default_*` for any field the block omits), substitute every `{var}` in `prompt_delta`, then call the image API with `--input-image {template_dir}/{ref_input}` (the ref carries the composition; the delta carries the subject). The prompt is concatenated **identity → style → delta** (`ssc-image-generator.md` Step 5.8). GPT only — it is the script that supports `--input-image`.
     - `texture-extract` → NO per-post call; `_ai_bg/bg.png` already exists as a fixed template asset. Skip generation for this zone.
     - *(legacy, no `generation_route`)* a block with `composition_prompt` → substitute `{var}`s, concatenate `brand_style + composition_prompt_filled`, generate txt2img. Kept only for un-migrated templates.
   - Calls the image API at the `output_aspect` ratio; writes the result to a per-post asset path and populates `slot_path` (`PHOTO_MAIN_PATH`) in the render data.
3. `render_template.py` renders the template with the AI image filled into its slot via standard Mustache + data-URI inlining.

### Rules

- **One block per image slot.** Two image slots → two blocks (`:1`, `:2`).
- **No prompt content lives in `manifest.json`.** Manifest declares slots (input contract). Composition prompt lives where the layout lives — in `template.html`.
- **No prompt content lives in a sidecar `.prompt.md` file.** One template = one file. The comment block keeps prompt and HTML next to each other so they evolve together.
- **Identity is brand-wide; style is per-template; composition is the delta.** `palette` / `accent` / `grain` are the brand IDENTITY — they live in `visual-identity/ai-image-style.md` (the grade) and apply to every template. `medium` / `lighting` / `subject_treatment` are this template's STYLE — they live in this block's `image_style`, READ from the template's own ref (a cartoon ref ships a cartoon, a studio-lit ref ships studio light); the grade carries only `default_*` as the fallback when the ref is ambiguous. `composition` lives in `prompt_delta` (+ the ref via `--input-image`). So a default suave (the grade's `default_*`) is overridden by the example (the ref → this block's `image_style`), and the conference confirms — never duplicate the grade's identity here, and never let the grade's style dictate over the ref.
- **The hero image binds the `{{slot_path}}` placeholder, never a static `_ai_bg/…` path.** The `<img>` (or `background-image:url(...)` div) that holds the zone's generated image MUST bind the Mustache slot the block declares in `slot_path` — `<img src="{{PHOTO_MAIN_PATH}}">` / `style="background-image:url('{{PHOTO_MAIN_PATH}}')"`. At render time the placeholder is substituted with the POST's generated image; a hardcoded `src="_ai_bg/photo_main.png"` is NOT substituted, so every post would ship the TEMPLATE's demo background (the "post ships the template demo" defect). The literal `_ai_bg/…` file is the template's demo/preview asset only — never the binding the shipped template carries.
- **No hardcoded per-post subject.** Use `{var}` placeholders. If `prompt_delta` names the ref's actual subject ("two elderly men reading newspapers") instead of `{PHOTO_SUBJECT}`, the template is broken — every post generates the same image.
- **The delta is ONLY the delta.** `prompt_delta` never re-describes the composition (zones, proportions, focal points) — the ref carries it via `--input-image`. Re-describing the composition in text is the exact failure mode `edit-from-ref` exists to prevent.
- **`clean_ref` / texture-extract is Route C only.** Never use it to produce a variable subject — that is Route A (edit-from-ref).
- **Every template keeps `assets/ref-canonical.png`.** It is the composition anchor and the `--input-image`. Never deleted.

---
