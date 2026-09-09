# Icons — embedded-mark resolution (shared)

> Read this when `ref_vision_summary.embedded_icons` is non-empty **OR any `distinctive_elements` row routes
> `SVG-overlay` / `brand-badge`**. It resolves the SMALL marks in a template (brand logos, app icons,
> pictograms, per-post brand-badges) — **never the hero image** (the hero is an AI image zone, see the
> scenarios). Neither trigger fires → skip entirely.

## Step 1 — MANDATORY local-commons search FIRST (before any fetch or generation)

For every brand / tool / product mark named in `embedded_icons`, FIRST glob the local commons library,
matching the name **case-insensitively**:

```bash
.claude/skills/viz-image-gen/references/icons/commons/**/*.svg
# e.g. "Claude" → commons/ai/claude*.svg / claude-sunburst.svg
```

- **Found → use it directly.** Copy to `{template_dir}/assets/{slug}.svg`, and **point the element at the
  SLIDE-RELATIVE local copy `assets/{slug}.svg`** — never at the project-root commons path
  (`.claude/.../commons/…`), which resolves under neither the slide folder nor `brand_context` and renders
  broken (the run-08 overlay-cover Claude logo). The commons path is the SOURCE of the copy, never the value
  that ships. Embed via `<img>` for a **pre-coloured** mark; embed as **inline `<svg>`** for a mark that must
  take a brand tint via `currentColor` (see "Brand seal composition" below). Do NOT call `fetch_icon.py`, do
  NOT generate an SVG, do NOT approximate the mark with inline primitives.
- **Not found → only THEN** advance to the table below.

Drawing a look-alike (an inline starburst instead of `commons/ai/claude*.svg`) when the real mark exists in
commons is a defect — it was the hero-display-cutout failure.

## Step 2 — only for marks local search did NOT resolve (first match wins)

| Subject | Case | Action |
|---|---|---|
| Client's own logo / headshot (`{brand_context}/visual-identity/{logos\|headshots}/`) | **A** | copy to `{template_dir}/assets/{slug}.{ext}` |
| Known third-party brand mark NOT in commons (OpenAI, GitHub, Notion…) | **B** | `uv run .claude/skills/viz-image-gen/scripts/fetch_icon.py --brand "<name>" --output {template_dir}/assets/{slug}.svg` |
| Generated app-icon / small custom icon | **D-mini** | simple txt2img (NO ref input) via `generate_image_gpt.py`, palette from tokens.json → `{template_dir}/assets/{slug}.png`, embed `<img>` |
| Simple pictogram (geometric, ≤10 shapes, generic line/bar/shape — NOT a known brand mark) | **inline-SVG** | `<svg>` primitives in `template.html`, `stroke/fill = var(--brand-*)` |

Point the relevant element at its `asset_path:`.

## Shape fidelity (inline-SVG case)
When an element declares a `shape` (starburst, scalloped, seal, hexagon, ribbon…), the SVG MUST realize that
exact geometry — a ~12-bump starburst is a real petal/bump path, NOT `border-radius:50%`. Never simplify a
declared non-circular shape into a circle. **This case applies ONLY to generic pictograms — never to a known
brand mark.** A brand mark that commons + fetch did not resolve is AI-generated in-scene, never approximated
with primitives (the run-06 cover-photo-hook 20-vertex polygon "starburst" in place of the real Claude mark).

## Third-party logo scope (Case B)
A fetched third-party mark lands ONLY in an explicit overlay `<img>`/icon slot the briefing declares — never
in a brand-chrome position (masthead, wordmark, decorative accent) and never merged into the brand's `moves`.
A brand's own decorative mark comes from `moves.md`, not from a third-party logo that merely looks similar. If
a mark could be either, flag it rather than promoting it to chrome.

## `brand-badge` — per-post third-party logo (NEVER hardcode the ref's example)
If the ref's third-party mark is there because the slide names a tool/brand *the post talks about* (not the
creator's own chrome, not a fixed ornament), it is a **`brand-badge`** — a per-post slot, not a static
`<img>`. See `shared/template-conventions.md > Third category — brand-badge`:

- Slot `{{BRAND_LOGO_PATH}}`; `variability: per-post`; resolution = commons lookup (by the post's subject
  tool) → `fetch_icon.py` → plain text.
- The mark in the ref (e.g. Claude) is the **canonical example for the preview ONLY** — never the locked
  value. Fill `{{BRAND_LOGO_PATH}}` with the example for the preview render, but keep the slot per-post in the
  Template Card + `[ai-image-zone]`/slots.
- Placement: HTML overlay `<img src="{{BRAND_LOGO_PATH}}">` by default (crisp). For in-scene marks that would
  collide with the subject, pass the resolved `BRAND_LOGO_PATH` as an extra `--input-image` to the
  edit-from-ref generation and let the prompt place it. The slot MUST end in `_PATH`.
- Baking the example (`assets/claude.svg`) as a fixed `<img>` is the "mocked badge" defect — every post would
  show the same tool.

## Brand seal composition — ONE provenance glyph, rendered with its OWN colour (fix the one-page miss)

A **brand / product seal** (the proof-of-provenance mark — e.g. the Claude glyph) is **one glyph rendered on
its own**, with an explicit composition contract. The one-page miss stacked TWO real SVGs (a starburst shell +
the logo inside it) and then killed the logo's colour with a CSS filter — both are forbidden by default.

**Read the seal from the ref, then author it to a contract:**
- **How many shapes does the ref's seal actually show?** ONE mark (just the glyph, maybe on a plain card) →
  author ONE `<img>`, nothing behind it. **Compose a shell + logo (two layers) ONLY when the ref shows the two
  shapes separately** (a distinct decorative shell AND a distinct logo sitting in it). Do not invent a starburst
  shell behind a glyph the ref shows alone — that is the one-page "2 selos empilhados" defect.
- **The seal's contract** (declare each in the Template Card / the element's row):
  - `card`: the background behind the glyph if the ref shows one (e.g. a white rounded card) — `background:#fff;
    border-radius:NNcqw;` — or none.
  - `position` + `size`: the bbox, read from the ref (`distinctive_elements` size/position), not inflated.
  - `fill`: **explicit and NATIVE** — the glyph renders in **its own brand colour** (the Claude mark is
    `#D97757` coral). State the fill; never let it inherit or get filtered away.
  - `tint vs baked → `<svg>` vs `<img>`:` a **single-colour decorative shell** behind/around the glyph that
    must read in the brand accent (a `currentColor` starburst) is authored as **inline `<svg>`** with
    `fill=var(--brand-accent)` — NOT `<img src="shell.svg">`, because an `<img>`-loaded SVG is an isolated
    document and the host `color` never cascades in, so a `currentColor` shell paints BLACK (the run-08
    overlay-cover starburst). The **pre-coloured glyph itself** stays `<img src="assets/{slug}.svg">`,
    slide-relative, rendered as-is. (The render bake auto-splices a literal `currentColor` `<img>` to inline
    `<svg>` as a backstop — but author it inline so the tint intent is explicit.)
  - `wordmark`: if the ref shows the name ("Claude") next to the glyph, author it as a **text slot**
    (`{{SEAL_WORDMARK}}` / a `data-slot`), not as part of the image.

**❌ NEVER `filter: invert(...)` / `brightness(0)` / `grayscale(...)` on a COLOURED logo.** These force a
multi-colour brand mark to flat white/black and **destroy its brand colour** — the exact one-page defect
(`filter: brightness(0) invert(1)` on `{{BRAND_LOGO_PATH}}` turned the coral Claude glyph solid white). A
provided logo asset already carries its correct colours; render it **as-is**. If the seal must read on a dark
surface, put it on its **own card** (a white/light rounded card behind the glyph) — never filter the glyph.
The only legitimate use of a colour filter is on a SINGLE-colour pictogram you own and intend to tint via
`var(--brand-*)`, never on a third-party / multi-colour brand logo.

> The inegociável (gate-enforced, r6g + PRIO 6 conference): never two seals stacked when the ref shows one;
> never a filter that kills the brand colour. Everything else (card or no card, exact size) the **ref decides**
> — the policy is "read the seal from the example", not a fixed card+wordmark law.
