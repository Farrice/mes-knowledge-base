# Quality gate — the automatic judge (shared)

> The gate common to every scenario. Same mechanics as the existing pipeline gates (contrast gate,
> text-verification gate) applied to more criteria. It **blocks and re-rolls itself** — it is not a warning.
> A bad slide never reaches the user.
>
> Thresholds resolved with Gustavo 2026-06-08. Acceptance overall is by-eye on the golden set; this gate is
> the automatic floor underneath that.

---

## Check A — the rationale gate (BEFORE generation, not part of this gate's re-rolls)

Before generation runs at all (builder Step 3, top), the builder MUST pass **Check A**:
`00-social-content/scripts/gates/check_rationale.py --rationale {template_dir}/rationale.md`. It verifies
`rationale.md` exists and all 4 sections (Form+tree-with-why · Per-block breakdown · Pipeline · Ambiguity)
are present and non-empty (the ambiguity section may NOT be `n/a`/empty). Non-zero → generation is LOCKED;
the builder writes the rationale first. Check A verifies **presence + completeness only** — it does not judge
reasoning quality (that is the gabarito bar + the by-eye golden set). It is a hard scripted lock, not advisory.

## Check B — the treatment-contract (AT the gate, post-generation)

After generation, alongside the scripted criteria below, run **Check B**:
`00-social-content/scripts/gates/check_treatment_contract.py --rationale {template_dir}/rationale.md
--template-html {template_dir}/template.html --preview {template_dir}/preview.png
--measurements {template_dir}/_measurements.yaml`. It binds the **category** the rationale declared per block
(and the reserved-zone geometry), NOT the pixels/position. Seven checks:

- a block declared **AI-integrated** must come out integrated-in-the-image (an `[ai-image-zone]` exists), not
  a flat HTML box; an **HTML-overlay** block must ship a content `data-slot`;
- a declared **filled raster zone** (photo/cutout/hero, filled every post) must render filled — a near-uniform
  empty region ≥ threshold = the grey-placeholder failure (test-09-06 **body-numbered**);
- a **B1 "reuse the in-scene surface"** rationale must place the text on the surface (AI-placed) — pure HTML
  text with no AI zone = the **body-statement** miss;
- **(SPEC-A) the `prompt_delta` must not forbid text wholesale** when the rationale declared AI-integrated
  text — a blanket "no text/captions" negates the integrated text (**ref-01**);
- **(SPEC-A) a B1 must not be `total-recompose`** — that regenerates the surface instead of reusing it (**ref-02**);
- **(SPEC-A) no isolable caption/CTA/byline/badge/label declared AI-integrated** — baked text the brand
  hard-rule keeps in HTML (**ref-07**);
- **(SPEC-A) reserved-zone geometry** — the prompt's reserved upper band and the HTML text extent
  (`_measurements.yaml`) must agree, else the text collides with the scene below the band (**ref-03**).

A Check B mismatch (exit 2) feeds the SAME 3-try ladder below. The ladder degrades only HOW the slide is
executed — `rationale.md` does NOT change. If the ladder exhausts with Check B still unsatisfied →
`needs-user-decision` (the declared decision wasn't executable = a human case). A full per-block
pixel-region comparator remains a documented follow-up.

## Check C — the font-resolved gate (AT the gate, post-bake)

The single decisive plumbing bug from test-09-06: the pool's `_shared/styles.css` carries the brand
`@font-face` with **relative** urls, and the bake runs against `about:blank` (no base URL), so an
un-inlined sheet leaves the brand display family **unresolved** → every HTML headline falls back to
system sans. A PNG diff doesn't catch it (the layout looks fine); only `document.fonts.check` does.

`render_template.py` now inlines the shared sheet's `@font-face` urls to base64 and, after
`document.fonts.ready`, evaluates `document.fonts.check('400 100px "<brand-display>"')`, writing the
verdict to a sidecar `<output>.fontcheck.json`. The gate runs **Check C**:
`00-social-content/scripts/gates/check_fonts_resolved.py --render-output {template_dir}/preview.png`
(exit 0 = resolved, exit 2 = fallback → BLOCK). Equivalently, bake the gate render with
`render_template.py --require-font` to hard-fail at bake time. A Check C failure feeds the SAME 3-try
ladder below (a re-bake on a fixed sheet, not a re-identification).

## Image-medium conference — the soft sibling (AT the gate, post-generation — WARNS, never blocks)

The marca fixes the IDENTITY — palette / accent / grain; the STYLE (medium / lighting / subject_treatment) is read per-template from each ref (`agents/ssc-template-builder.md` §2; `craft/ai-prompt-craft.md` "Medium, lighting and treatment are the ref's") and written to the block's `image_style`. The conference covers the **medium** today (a parallel lighting/treatment conference is a logged follow-up — fuzzier text read, deferred so it does not become a new pedra). It confirms the prompt kept the ref's medium:
`00-social-content/scripts/gates/check_image_medium.py --rationale {template_dir}/rationale.md
--template-html {template_dir}/template.html`. It reads the §2 `medium:` (falling back to the brand `ai-image-style.md` `default_medium` when §2 is silent) and compares it to the `prompt_delta`'s medium terms. When the prompt **inverts** the ref's medium (a cartoon ref prompted "documentary photograph" — the run-07 `services-billboard` miss) it prints a `[warn]` and **exits 0**.

This is a CONFERENCE, not a gate: medium is a **judgment** call, so it **WARNS and surfaces it for the human** — exactly the posture the palette check already takes (flag-only, never auto-recolor). It does **NOT** feed the 3-try ladder and does **NOT** block. A `default_medium: mixed` brand never warns (it legitimately ships any medium). The deterministic text read (declared vs prompted medium) ships now; a **visual cartoon-vs-photo classifier** on the rendered preview is a logged follow-up (read the pixels, the costlier read — deferred like Check B's full per-block pixel comparator).

## Check D — the display-height gate (AT the gate, post-bake — SPEC-B)

After SPEC-C made the brand display font load, the remaining flatness is real type craft — and the most
common miss is a timid, under-scaled headline (the r04/r05/r06 "big-head/starved-body" only LOOKS big because
the body is starved). **Check D** makes the display height blocking:
`mkt-visual-identity/scripts/measure_text_heights.py --image {template_dir}/preview.png
--compare-to {template_dir}/assets/ref-canonical.png --enforce`. It FAILS (exit 2) when the preview's display
row is **< 8cqw** OR (with `--compare-to`) **more than 15% smaller** than the ref's display height. On fail,
grow the headline + tighten line-height/tracking (never bump weight — `html-craft.md` §3) and re-bake. Feeds
the SAME 3-try ladder.

## Check E — the palette-token gate (AT the gate, post-generation — the brand-substitution leak catch)

The deterministic catch for **RC-A leak channel 1** (the run-08 palette leak): the builder reads the ref for
FORM, then lets the ref's literal **palette** survive into the rationale/template instead of remapping it to
brand tokens (`craft/ai-prompt-craft.md` → "Brand-context substitution"). Check E flags any **literal hex that
is NOT a brand token** (`tokens.json` `colors`, per-channel tolerance) appearing in `rationale.md` or
`template.html` — the run-08 `list-on-object` lime `#b5e853` kept as the palette, the `fullbleed-photo-cover`
headline `fill: white` (`#ffffff`) copied from the ref:
`00-social-content/scripts/gates/check_palette_tokens.py --tokens {brand_context}/visual-identity/tokens.json
--rationale {template_dir}/rationale.md --template-html {template_dir}/template.html`. The right authoring is
`var(--brand-*)` / a token NAME — never a baked literal hex (`template-conventions.md`).

It is **accent-agnostic** (the palette comes from the brand's own `tokens.json`, never a hardcoded hue) and
mirrors the **palette flag-only posture**: **advisory by default** (exit 0, WARNS — surfaces the leak for the
human; the fix is upstream, remap the colour to a token, never auto-recolor), `--enforce` to make a leak BLOCK
(exit 2) and feed the 3-try ladder where a pool wants a hard palette floor. It does NOT judge whether the remap
is tasteful (by-eye) and does NOT replace `measure_text_contrast.py` (legibility-against-background) — it
answers only "is every literal hex a brand token?". The subject + language leak channels are by-eye / the
brand-substitution step (Step 2.5); the palette channel is the one that is deterministically catchable.
## Craft-LINT — the type-craft layer above the overflow gate (RC-B — WARNS, never blocks by default)

The overflow gate (`compare_render_to_ref.py`) only sees text spilling the CANVAS; the autosize net only
shrinks text that overflows its OWN box. A whole class of misses is *ugly-but-fits* or *cross-zone collision*
— a body stranded as a footnote under a giant display, airy line-height ("espaçamentos muito altos"), negative
tracking colliding multi-line condensed glyphs, a display stack running into the image zone below. None is a
pixel-overflow event, so neither gate fires. **Craft-LINT** measures these from the authored CSS:
`00-social-content/scripts/gates/check_craft_lint.py --template-html {template_dir}/template.html`. It reads the
per-zone `cqw` font-sizes / line-heights / letter-spacing / line count / height cap and flags: display:body
ratio out of range, body below the cqw floor, excessive line-height/whitespace, negative tracking on
multi-line condensed display, and a too-tall un-capped display stack (the five `html-craft.md` §3.7 rules).

It is **ADVISORY** (warns + surfaces for the human, exit 0 — the same "gate WARNS on judgment" posture as the
palette flag and the image-medium conference); it does **NOT** feed the 3-try ladder by default. Pass
`--enforce` to make it block (exit 2) and feed the ladder. NO slug is hardcoded — every threshold is general
craft, so it catches the *class* wherever it recurs.

## HONOR checks (RC-C — the contract was RESOLVED but not HONORED)

The gates above verify a contract was NAMED / RESOLVED; these three verify the **OUTPUT honors
it**. RC-C (run-08): a contract resolves and passes presence, but the shipped pixels don't honor
it — resolution ≠ preservation. NO slug is hardcoded; each read is general to any template.

### Check F — FACE-MATCH (a resolved hero face must MATCH the brand headshot)

`check_treatment_contract.py` Check 13 catches the PRESENCE failures (placeholder identity slot /
generic `PHOTO_SUBJECT`) but explicitly punts on "whether the identity survived heavy
stylization". **Check F closes that gap:** when a hero-face slot resolved to a brand headshot AND
the path is real, assert the preview's hero FACE matches the headshot identity. The run-08
`portrait-cta` miss: the headshot (`simon-pic.jpg`) WAS resolved and passed to the edit with
"keep identity", but the restyle overpowered it → an AI-invented face shipped. Check 13 passes
(path resolved, subject not generic); FACE-MATCH fails.
`00-social-content/scripts/gates/check_face_match.py --preview {template_dir}/preview.png
--headshot {brand_context}/visual-identity/headshots/<headshot> --rationale {template_dir}/rationale.md`.
It uses OpenCV Haar face detection + a deterministic identity score (Sobel-gradient facial
STRUCTURE correlation, grayscale image correlation, HSV tone histogram — structure weighted most;
NOT a learned embedding — **documented limitation**: a very heavy legitimate restyle can also
score low). The gate is applicable only when the rationale routes a hero face WITH a brand
headshot (a `hero_face_identity: invented` read suppresses it); it degrades to *indeterminate*
(never fails) when no face is detected or no headshot is found. Identity-under-stylization is a
**judgment** call → **ADVISORY by default** (exit 0, WARN — the "gate WARNS on judgment" posture);
`--enforce` makes a mismatch BLOCK (exit 2) and feed the 3-try ladder.

### Check G — SEAL-GLYPH-PRESENT (a contracted seal glyph must visibly RENDER)

`check_treatment_contract.py` Check 14 verifies the seal ASSET isn't destroyed by CSS, and the
provenance gates verify a logo was RESOLVED — none verifies the glyph LANDED. The run-08
`overlay-cover` miss: the Claude logo asset existed in commons (provenance passed), but the badge
authored `<img src="{{BRAND_LOGO_PATH}}">` whose path resolved to a `.claude/skills/...` location
that did not exist relative to the template dir (the asset sat at `assets/claude.svg`) → an empty
starburst shipped. **Check G** asserts the glyph the badge points at actually renders:
`00-social-content/scripts/gates/check_seal_glyph.py --template-html {template_dir}/template.html
--preview {template_dir}/preview.png --rationale {template_dir}/rationale.md`. For every badge/seal
region that CONTRACTS a glyph, it runs (1) a HARD deterministic read — the glyph `<img src>`
(`{{SLOT}}` placeholders substituted from the slide `metadata.json`) must resolve to an existing
file relative to the template dir — and (2) an advisory pixel read of the inner glyph sub-region
(not near-empty/single-color). Read (1) is **deterministic** (a broken glyph path is not a
judgment call), so it **BLOCKS by default** (exit 2) and feeds the ladder, mirroring the
seal-provenance hard-fail; `--no-enforce` downgrades to advisory.

### Check H — FORM-VS-REF SIGNATURE (don't trust the rationale's self-declared form)

`check_treatment_contract.py` binds the OUTPUT to the treatment the RATIONALE declared — so a
rationale that MIS-READS the ref and self-declares a flat form passes (the gates check the output
against the wrong form). The run-08 `highlight-pills` miss: the ref's defining signature is
tilted / overlapping / icon-bearing pills WOVEN through the headline (a Form C composition), but
the rationale argued its way to B2 and the output shipped FLAT axis-aligned isolated chips off in
the margin. **Check H** reads the REF's signature directly, not the rationale's:
`00-social-content/scripts/gates/check_form_vs_ref.py --template-html {template_dir}/template.html
--ref {template_dir}/assets/ref-canonical.png`. It detects a WOVEN ref (multiple small VIVID
device pills in the headline band, reading tilted/overlapping — vividness, NOT the brand accent
hue, since the RAW ref is read before any remap) vs a FLAT-ISOLATED output (pill/callout
containers, none rotated/tilted). REF=woven AND OUTPUT=flat → flag. Form routing is a **judgment**
call → **ADVISORY by default** (exit 0, WARN); `--enforce` BLOCKS (exit 2) + feeds the ladder. It
fires only when the output declares pill containers AND the ref reads woven (a vivid-bg ref with
no output pills can never trip it).

## Check I — the BURIED-HEADLINE gate (AT the gate, post-bake — r8; BLOCKS by default)

The single decisive composition bug from run-09 (`preview-cards-cover`): the builder authored an
HTML display HEADLINE (a real editable `data-slot="HEADLINE"` text node) at a LOW z-index and put
an OPAQUE AI image zone (`data-slot="PHOTO_MAIN" data-zone="photo"`) at a HIGHER z-index ON TOP of
it — a "woven Form-C via z-index" recipe meant to let the image overlap the letterforms. But an
`edit-from-ref` AI image is an **OPAQUE rectangle** (GPT edit mode strips transparency — see the
`gpt-edit-transparent` work), so the image BURIES the headline in the bake (it reads as an image,
not type, with visible seams) AND occludes it in the Studio editor (the user can't click-select the
text to change font-size — the headline behaves like an image). The rationale even promised
`mix-blend-mode: multiply` but the template.html never authored it — a **declared-but-not-honored** gap.

**The general rule (NO slug, NO per-template constant): an HTML TEXT data-slot must NEVER sit
UNDERNEATH an OPAQUE AI/photo image zone whose bbox intersects it.** A text slot stays visually on
top / in a clear zone and remains an editable text layer. The "AI element overlaps HTML type"
(woven) composition is allowed ONLY when the AI element is a **transparent-background cutout** (it
occludes only its own region) — which depends on transparency being available (cross-ref the
`gpt-edit-transparent` work) — or a HONORED `mix-blend-mode` actually authored in the CSS. A
declared blend mode that is not authored does NOT earn the exception. If transparency is
unavailable, the text MUST NOT be occluded by the image at all (place the headline clear of the
image's bounding box).

`00-social-content/scripts/gates/check_buried_headline.py --template-html {template_dir}/template.html`
reads ONLY template.html (pure z-index + bbox geometry — no pixels, no model). It FLAGS (exit 2)
when a TEXT `data-slot` (a `display`/headline zone most of all) has a STRICTLY LOWER effective
z-index than an OVERLAPPING photo / AI-image slot (`data-zone="photo"`, a `photo-zone`/`photo-`
selector, or an `<img>`-bearing image zone) that is OPAQUE (no `data-cutout`/`data-transparent`
marker, no authored non-`normal` `mix-blend-mode`). A buried editable text slot is **not a judgment
call** → it **BLOCKS by default** and feeds the SAME 3-try ladder below (try-2 reinforces "lift the
headline above the image / clear the image bbox"; the ladder degrades toward the clean pattern —
text z-index above the image, or the coordinated hybrid). The clean reference pattern
(`numbered-statement-body` / `fullbleed-overlay-cover`: a full-bleed photo at z-index 0 with text
zones at z-index 10/20 ON TOP — `template-conventions.md` #9) PASSES.

## The 3-try ladder — VARY the strategy (never the same prompt 3×)

| Try | Strategy |
|---|---|
| **1** | Normal scenario edit (the scenario's declared edit mode). |
| **2** | **Reinforce the specific instruction that failed** — e.g. "text clipped at the bottom → increase bottom margin"; "reserved zone wasn't clean → restate the reserved-zone instruction". |
| **3** | **Change strategy, deterministically: coordinated hybrid → plain HTML.** Generate the scene leaving a clean zone and place the text as HTML on it (the coordinated hybrid); if that still fails, fall to plain HTML. **No re-identification** — the form is fixed; only the rendering strategy falls back. |
| — | After 3 failures → log and mark **`needs-user-decision`**. Never present a failed slide. |

> Design note (AIOS-190): try 3 does NOT re-run the identification tree on the result. The form read from the
> ref stands; the ladder only degrades the rendering strategy toward the safest path.

---

## Common criteria (all scenarios)

- **Breathing room** — 30–50px margin at the canvas edges by default. Without it text glues to the margin.
- **Proportion / dead space** — text must not sit crammed at the top leaving half the canvas empty.
  **Measured by script** (`dead_space.py`): FAIL when `text_height_fraction < 0.25` **AND**
  `empty_fraction > 0.55`. Either alone passes (a minimal centered cover is fine).
  **Advisory-only for C / B1 (AIOS-190).** The script measures HTML/bbox text zones + the
  largest near-uniform pixel region; it **cannot see text baked into the AI image**, so a clean
  full-canvas C (integrated text) or B1 (in-scene surface) on a uniform background would
  false-fail (the filled canvas reads as empty). Pass `--form C` (or `--form B1`) and a would-be
  FAIL is downgraded to **ADVISORY** (a non-blocking note, exit 0) — it surfaces but does NOT
  trigger the re-roll ladder. A full vision-read of baked text is out of scope for v1.
- **Palette** — **flag-only in v1.** If the generated output strays far from the brand palette, the gate
  **warns** (surfaces it for the human); it does NOT auto-recolor. Recolor stays an optional setup-time move
  (`ai-prompt-craft.md`, partial bg+color) the builder MAY apply when it reads an off-palette ref — never an
  automatic gate re-roll. (Never *reject* an off-palette ref; recolor or flag.) The deterministic sibling of
  this flag is **Check E** (`check_palette_tokens.py`, below): the rendered-output stray is by-eye/visual,
  while Check E reads the **authored** rationale/template for a literal off-token hex (the run-08 ref-palette
  leak) — same flag-only posture, a different read (text, not pixels).
- **Contrast** — text legible. **Measured by script** (`measure_text_contrast.py`, WCAG AA), not by the AI
  judging itself.
- **No overflow / clip** — text didn't spill past its zone or the canvas edge.
- **Baked-letter correctness** — if any text was baked into the AI image, the letters are correct
  (vision check; reuse the existing text-verification gate's verbatim ladder).
- **Not "dead"** — composition has life (real type hierarchy, scale, breathing room — see `html-craft.md`).

## Per-scenario appendix (the scenario's extra criterion)

- **A** — the image stayed contained without invading the text zone.
- **B1** — the text respected the in-scene surface bounds (didn't spill past the frame/screen).
- **B2** — the text landed on the reserved zone, and the band is actually clean (crop the band, measure
  uniformity + luminance + black-text contrast — the breathing-room measurement).
- **C** — the integrated text is legible against the busy scene and not clipped.
- **solid** — text contrast holds on the solid (script).

---

## Robustness — at least one criterion measured by SCRIPT, not the AI

Avoids self-praise. Two script measurements back the gate:

1. **Contrast** — `mkt-visual-identity/scripts/measure_text_contrast.py`
   `--preview preview.png --measurements _measurements.yaml` (deterministic WCAG ratio per text element).
2. **Dead space** — `00-social-content/scripts/gates/dead_space.py`
   `--preview preview.png [--measurements _measurements.yaml]` (largest near-uniform region + text-band
   height; the thresholds above).
3. **Rationale gate (Check A)** — `00-social-content/scripts/gates/check_rationale.py` (presence + completeness of
   the 4-section `rationale.md`; runs BEFORE generation — see Check A above).
4. **Treatment-contract (Check B)** — `00-social-content/scripts/gates/check_treatment_contract.py` (output
   matches the per-block treatment the rationale declared; runs AT the gate — see Check B above).
5. **Font-resolved (Check C)** — `00-social-content/scripts/gates/check_fonts_resolved.py`
   `--render-output preview.png` (the brand display `@font-face` actually loaded in the bake; reads the
   `<output>.fontcheck.json` sidecar render_template.py emits — see Check C above).
6. **Display-height (Check D)** — `mkt-visual-identity/scripts/measure_text_heights.py --image preview.png
   --compare-to assets/ref-canonical.png --enforce` (the display row is ≥ 8cqw AND within −15% of the ref —
   blocks the timid-headline miss; see Check D above).
7. **Render-vs-ref overflow/clip + line-count (Check B(a))** — `mkt-visual-identity/scripts/compare_render_to_ref.py
   --preview preview.png --measurements _measurements.yaml --ref assets/ref-canonical.png` (every fixed-dimension
   text box, `display` included, contains its text — no scroll-overflow/clip; per-element line count agrees with
   the ref). Exit non-zero → feeds the 3-try ladder. This is the run-07 HTML-overflow gate (about-callout / chain
   caption); `--ref` optional (overflow read runs without it).
8. **Palette-token (Check E)** — `00-social-content/scripts/gates/check_palette_tokens.py
   --tokens {brand_context}/visual-identity/tokens.json --rationale rationale.md --template-html template.html`
   (every literal hex in the rationale/template is a brand token — the RC-A run-08 palette-leak catch; see
   Check E above). **Advisory by default** (exit 0, WARNS — like the palette-stray flag); `--enforce` makes a
   leak BLOCK + feed the ladder. Listed here as a scripted floor; its posture is flag-only like the palette flag.
9. **Seal-glyph-present (Check G)** — `00-social-content/scripts/gates/check_seal_glyph.py
   --template-html template.html --preview preview.png --rationale rationale.md` (a contracted
   seal/badge glyph's `<img src>` resolves to an existing file AND renders into the badge — the
   RC-C `overlay-cover` empty-Claude-starburst catch; see Check G). **BLOCKS by default** (the
   asset-resolves read is deterministic); `--no-enforce` for inspection.
10. **Buried-headline (Check I)** — `00-social-content/scripts/gates/check_buried_headline.py
    --template-html template.html` (no editable TEXT data-slot sits under an OPAQUE AI/photo image
    zone with a lower z-index — the run-09 `preview-cards-cover` headline-as-image / not-editable
    catch; see Check I). **BLOCKS by default** (a buried editable text slot is deterministic, not a
    judgment call) + feeds the ladder. Pure geometry — reads template.html only, no pixels.

Plus three **advisory HONOR/judgment checks** (warn, never block by default; `--enforce` to make
them block + feed the ladder): **Face-match (Check F)** —
`00-social-content/scripts/gates/check_face_match.py --preview preview.png --headshot
{brand_context}/visual-identity/headshots/<headshot> --rationale rationale.md` (a resolved hero
face matches the brand headshot identity — the RC-C `portrait-cta` invented-face catch; deterministic
similarity, documented limitation; see Check F) — and **Form-vs-ref signature (Check H)** —
`00-social-content/scripts/gates/check_form_vs_ref.py --template-html template.html --ref
assets/ref-canonical.png` (a WOVEN ref shipped as FLAT isolated chips — the RC-C `highlight-pills`
mis-route, read off the REF not the rationale's self-declared form; see Check H). Listed apart from
the scripted floors 1–9 because identity-under-stylization and form routing are judgment calls.

Plus two **advisory conferences** (warn, never block by default): **Image-medium** —
`00-social-content/scripts/gates/check_image_medium.py --rationale rationale.md --template-html template.html`
(the prompt's medium vs the ref's recorded medium; exit 0 always — see the conference above) — and
**Craft-LINT** — `00-social-content/scripts/gates/check_craft_lint.py --template-html template.html` (the five
`html-craft.md` §3.7 type-craft rules: display:body ratio, body floor, line-height/whitespace, multi-line
condensed tracking, too-tall display stack; advisory by default, `--enforce` to block — see Craft-LINT above).
Listed apart from 1–7 because they are advisory, not scripted floors.

**`_measurements.yaml` for the AI-first builder.** The contrast and dead-space scripts read text bboxes from
`_measurements.yaml` (schema: `elements: [{id, bbox_pct:[l,t,w,h], color_role, type, font_size_cqw}]`). The
AI-first builder no longer measures bboxes for *placement* — but the **HTML text zones still have known
bbox %** (they're authored HTML with `data-slot`). Emit a minimal `_measurements.yaml` from those authored
zones **for the gate only**. AI-placed text (B1 surface, C integrated) has no HTML bbox → it is gated by the
dead-space measurement (empty-only WARN path) + the baked-letter vision check, not contrast-by-bbox.

**Gates stay separate in v1** (deterministic contrast · heuristic dead-space · vision text-fidelity) — run in
sequence, so it's clear which one failed. The form comes from reading the ref (a present fact); the gate
evaluates the concrete *result* and re-rolls per the ladder — it does not re-identify the form.

---

## Out of scope (v1)

- **Auto-recolor** on palette stray (flag-only — see above).
- **Versioning the validated prompt** when the brand later changes palette/font (the recolor baked into
  `ref-canonical` would need redoing). Noted deliberately; not handled in v1.
