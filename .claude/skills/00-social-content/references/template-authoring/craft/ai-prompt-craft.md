# AI-prompt craft — Layer 3 (the HOW WELL of AI generation)

> Pure knowledge, shared across scenarios. A scenario declares *which edit mode to invoke*; this file is *how
> to invoke it well*. Improving AI fidelity touches ONLY this file — never scenarios or identification.
>
> **The inversion (master rule):** AI generates by default (composition, text-fit, overlap, font). The ref is
> the composition guide AND the generation input — feed it as `--input-image` and prompt only the DELTA. Never
> re-describe the composition in prose; that is the exact failure `edit-from-ref` exists to prevent.

---

## Brand-context substitution — the ref is FORM, never CONTENT (RC-A, the run-08 leak)

> A MANDATORY step run AFTER the form is identified (`identification-tree.md` + `rationale.md` §1) and BEFORE
> authoring ANY `prompt_delta` / `distinctive_graphics` / block `fill` / text slot. It is the single rule that
> stops the reference image's literal **content** from surviving into the template.

**The failure it fixes.** The builder reads the ref correctly for FORM/composition — then lets the ref's literal
CONTENT leak through instead of re-deriving it from the BRAND context. "Preserve the surface structure"
**explicitly EXCLUDES** preserving the ref's palette, its people/objects, and its language. The ref describes
the REF; the template describes the BRAND. Three leak channels, each closed below — and the rule is **agnostic
to the ref**: it works for a Portuguese ref, a Chinese ref, a lime-green ref, a jiu-jitsu-dojo ref, identically,
because it never reads the ref's content as the answer — it reads only the ref's *form* and substitutes the
brand's content into it.

**1 — PALETTE: remap every colour to a brand token; never copy a colour from the ref.**
Every colour that lands in the rationale or the template is a **brand token** (`tokens.json` `colors` —
`accent` / `primary`(ink) / `bg_light`(paper) / `bg_*` / `text_*` …), authored as `var(--brand-*)` or a token
NAME, **never a literal ref hex**. The ref's colours are a description of the ref, not a palette to inherit —
a strict 3-colour brand (ink + paper + accent, no second accent) stays 3 colours even when the ref is lime-green
(the run-08 `list-on-object` miss kept the ref's `#b5e853` as the template palette). A block **`fill` is never
copied from the ref** — it maps to a token, **chosen for legibility against ITS background**: on a bright /
photographic zone a near-white headline is illegible, so the headline maps to the brand ink or accent with real
contrast, never near-white-on-near-white (the run-08 `fullbleed-photo-cover` headline `fill: white` copied from
the ref, against the brand "ink `#1f1816` for headlines" rule, on a bright dojo floor). **Where the brand has a
signature display move** for this composition — read it from the brand's `moves.md` / visual-identity (e.g. a
"giant accent display word over a full-bleed photo" move) — **apply the brand's move**, not the ref's colour
treatment. (Rule 4 below already makes the ref's *tonal/luminance* read faithful; this makes the *hue* the
brand's. The two compose: keep the ref's brightness contract, paint it in brand tokens.) The deterministic
catch is **Check E** (`check_palette_tokens.py`, `shared/quality-gate.md`): any non-token literal hex in the
rationale/template is flagged as a leak.

**2 — SUBJECT (free-subject): re-derive the subject from the BRAND's domain, never transcribe the ref's.**
For `subject_role: free-subject` (`identification-tree.md` rule 7), the subject description in
`distinctive_graphics` / `subject_treatment` / the `{PHOTO_SUBJECT}` example describes the **BRAND's** subject —
re-derived from the brand domain (`voice-profile.md` + `ai-image-style.md` + `typical_subjects`) — **not** the
ref's literal people/objects. The run-08 `fullbleed-photo-cover` carried the ref's literal jiu-jitsu
instructor + children even though it declared `free-subject`; the brand-context subject (the brand's own
domain) is what the example/treatment must describe. (`fixed-hero` is the exception only because the hero IS the
brand identity — it recolors the ref's object; it still never inherits the ref's *palette*, per rule 1.)

**3 — LANGUAGE / COPY: text slot values are placeholders regenerated in the BRAND's language.**
Text slot `sample:` values are **placeholders to be regenerated from brand context in the brand's language**,
independent of the ref's language — a Portuguese ref must NOT produce Portuguese slot copy when the brand
language is English (the run-08 Portuguese-ref leak transcribed the ref's literal strings). The slot carries a
brand-language placeholder; the ref's literal text is never transcribed verbatim. This is ref-language-agnostic:
a Chinese ref, a Portuguese ref, an Arabic ref all produce brand-language copy. **Surface-bound type on a
screen / terminal / code panel maps to the brand `mono` token** (`tokens.json` `fonts.mono`), not the ref's
typeface.

> One line: **read the ref's FORM, substitute the BRAND's content.** Palette → brand tokens · subject →
> brand domain · copy → brand language. The ref never supplies a colour, a person, or a word that ships.

---

## Faithful prompt-from-rationale (SPEC-A — the test-09-06 contradictions)

**The `prompt_delta` is GENERATED FROM `rationale.md`'s per-block treatment — not from a blanket template.**
The rationale already decided, per block, what is AI-integrated vs HTML-isolable. The prompt must honor that
decision faithfully, or the model negates the very plan the rationale made. Five rules, each a real
test-09-06 / run-02 failure:

1. **The "no text" clause applies ONLY to blocks the rationale assigned to HTML — NEVER to AI-integrated
   blocks.** If the rationale declared a headline/word AI-integrated (e.g. *occluded behind the subject*), the
   prompt must **DESCRIBE** that text so the model renders it; appending a blanket *"No text, no lettering, no
   captions"* tells the model to skip the very thing it was supposed to integrate, and it free-styles a
   wrong-font word or renders nothing (the **ref-01** contradiction). Forbid in the image ONLY the text the
   rationale routed to HTML. Phrase it scoped: *"the only rendered text is the integrated <headline>; no OTHER
   text, captions, or UI"* — not a blanket "no text".

2. **`total-recompose` must NOT collapse isolable text into the AI zone.** Only genuinely-integrated blocks
   (an occluded headline HTML can't do, text printed on an in-scene surface, a **woven typographic cluster** —
   another element overlaps/threads the letterforms: a pill over the headline, a knockout inside a word, a
   caret in the baseline; text-on-text has no isolable container even with NO photographic subject, qa ref-03
   Chazon) may be AI. Isolable
   caption / CTA / byline / badge / label / **dominant headline-or-display word (when NOT occluded by the
   subject)** / handle stay **HTML overlay** — the brand hard-rule (`ai-image-style.md`: *all type is
   HTML/overlay*) forbids baking them, and gpt-image renders large display type poorly so a non-occluded
   dominant word also belongs in prominent HTML (the **cover-hook "the one page"** miss — a dominant display
   pushed into the AI image instead of authored prominent in HTML). A `total-recompose` that bakes
   `DISPLAY_WORD` + `NAME_LABEL` + `CTA_BADGE` into one image is the **ref-07** violation. Split the treatment:
   describe ONLY the genuinely-integrated text in `prompt_delta`; leave the isolable text — including a
   non-occluded dominant display — to HTML slots. **The ONLY display that stays AI is one genuinely occluded by
   the photographic subject** (see "Dominant-display scale" below).

3. **A reserved-zone % is a SINGLE source shared by the prompt and the HTML.** When the prompt reserves "the
   upper N%" for HTML text, the HTML text zones must fit inside that same band. The prompt reserving 45% while
   the HTML occupies 60%+ guarantees a collision on every per-post subject swap (the **ref-03** collision).
   Pick ONE % , write it into both the `prompt_delta` reserved-zone instruction and the HTML zone geometry,
   and keep a luminance/clearance margin so a darker per-post subject doesn't turn the lower text into a
   contrast gamble. (Check B's reserved-zone-geometry check enforces this against `_measurements.yaml`.)

4. **Tonal words are read from the ref's ACTUAL luminance — they preserve the legibility contract.** The bg /
   texture-extract prompt's tonal description is a faithful read of the ref's real brightness (see
   `identification-tree.md` rule 3), never a "brand is dark" prior. A light/sand ref is prompted as light/warm
   paper — never "dark near-black" (the **ref-05** miss; and the **run-04 body-numbered** miss baked
   `#1d1c1c` over ref-04's bright teal water). The hard constraint is the **legibility contract**: the reserved
   text zone keeps the ref's luminance — a bright zone for dark text stays bright, never inverted into a dark
   zone for white text — because that contract is what makes the HTML text read on every per-post scene.

5. **The bg `prompt_delta` carries the ref's distinctive GRAPHIC devices — not only palette + subject (fix
   ESQUECE).** Rule 4 makes the *colour* faithful; this makes the *graphic device* faithful. The ref's signature
   non-text visual mark — a radial line-burst / engraving sunburst, a halftone field, a line-art motif, a
   pattern/texture, a framing rule, an emblem — is captured in `ref_vision_summary.image_zone.distinctive_graphics`
   (`identification-tree.md` Step 0) and **MUST be described in the bg `prompt_delta`**. A delta assembled from
   palette + subject + integration only, with the device left out, drops the signature and the bake comes back a
   flat fill (the **run-02 ESQUECE** miss: ref-01's orange radial line-burst behind the figures vanished —
   `photo-cover`'s delta said only *"warm coral-orange full-bleed background, fine paper-grain texture"*, so the
   burst was gone). Phrase the device faithfully and place it relative to the scene, e.g. *"a radial line-burst /
   engraving sunburst behind the figures, in the warm coral palette"*. When `distinctive_graphics: none`, there is
   nothing to carry — only then is palette + subject complete.

   **Texture-extract corollary (the run-06 airbrush-wash deletion).** The scope of `distinctive_graphics` is the
   WHOLE canvas, not just the image-zone slot (`identification-tree.md` Step 0). In a `texture-extract`
   `prompt_delta`, every captured device goes on the **PRESERVE** line; the "remove / clean" instruction scopes
   to the TEXT / CONTENT blocks only. A blanket *"no marks"* is **FORBIDDEN** whenever
   `distinctive_graphics ≠ none` — ref-03's orange airbrush washes were bg-level (outside the image-zone schema
   slot), the extract prompt said "no marks", and the brand device was deleted from the extracted bg.

6. **Medium, lighting AND treatment are the ref's — inherited into the prompt's opener, not the grade's opener
   prepended blindly (fix the run-07 services-billboard).** The brand's `ai-image-style.md` fixes the *identity*
   — palette, accent, grain — but NOT the **style**: the **medium** (photo / flat-illustration / watercolor /
   sketch / 3d-render), the **lighting** (dramatic / natural / studio-flat-soft / none), and the **subject
   treatment** (isolated-on-light-bg / full-bleed / inset-with-shadow / cutout). All three are READ per-template
   from the ref into `rationale.md` §2 (`medium:` / `lighting:` / `subject_treatment:` on the image-block line)
   and written into the `[ai-image-zone]` block's `image_style`; the `prompt_delta` **opens in that read style**:

   ```
   flat-illustration + natural + full-bleed ref → "flat vector illustration, natural light, full-bleed scene, in <brand palette>, <brand grain>, …"
   photo + dramatic + isolated ref              → "documentary photograph, dramatic light, subject isolated on light bg, <brand palette>, <brand grain>, …"
   ```

   Prepending the grade's documentary/studio-flat opener over a cartoon natural-light ref forces the wrong look
   and loses the example's language — the run-07 `services-billboard` shipped photoreal when ref-04 is a flat
   cartoon, because the brand grade crava'd a single "documentary photograph" opener + "no illustration" negative
   for the whole brand. The grade still supplies the palette / accent / grain cues — only the style (medium +
   lighting + treatment) follows the ref. **When a ref's style field is genuinely ambiguous**, fall back to the
   grade's `default_medium` / `default_lighting` / `default_subject_treatment` for that one field. **When the
   brand is `default_medium: mixed`**, there is no brand medium opener/negative to prepend at all — the style
   enters only here, from this ref. And never append a style-negative that contradicts the ref (no *"no
   illustration"* on a cartoon ref, no *"no dramatic shadows"* on a dramatically-lit ref). Check B's sibling —
   the **image-medium conference** (`check_image_medium.py`) — reads the §2 `medium` vs the prompt's medium terms
   and **WARNS** (does not block; style is judgment) when the prompt's medium inverts the ref's; the parallel
   lighting/treatment conference is a logged follow-up.

7. **The canonical reproduces the ref scene; the landscape is free only per-post (fix the run-04 INVENT, scoped
   by phase).** Two phases, two strictnesses. **At template build / validation** the prompt REPRODUCES the
   ref's scene so the canonical can be checked against the gabarito — an empty-chair ref stays an empty chair;
   never add a figure or prop the ref lacks (the run-04 body-numbered added a seated man to ref-04's empty
   chair). **At post time** the scene/landscape is the variable: a fully new landscape per post is legitimate,
   as long as it honours the composition contract (reserved zone clear + correctly-toned, integration manner
   intact). So "no-invent" binds the **canonical**, not the per-post scene — the landscape changes, the
   contract does not.

Check B (`shared/quality-gate.md`) verifies the deterministic subset post-generation; a mismatch feeds the
3-try ladder. (distinctive-graphics and reserved-band position stay soft in v1 — enforced by the by-eye golden
set — while scrim-vs-ref and containment-vs-ref are gate-checked; see the gate section.)

---

## Element routing — small mark = overlay, dominant display = HTML, occluded display = AI-at-scale (fix D2)

The `treatment` each `distinctive_elements` row carries (`identification-tree.md` rule 6) is HONOURED here when
the `prompt_delta` is built. Two classes the AI cannot hold, and the one display class it CAN:

**Small distinctive brand mark (badge / seal / logo, `size: minor`) → SVG/HTML overlay, NEVER in `prompt_delta`.**
gpt-image **drops** small marks. cover-hook asked the prompt for *"a small coral starburst seal with 'Claude'"*
and the AI rendered nothing there. So the mark is NOT described in the bg `prompt_delta` at all — it is
composited as an SVG/HTML overlay on top of the generated scene (an isolable badge that sits cleanly on top,
per `craft/html-craft.md`). The brand's OWN seal is a brand asset, not a per-post scene prop; route it `SVG-overlay`.
**Provenance:** the overlay asset is the REAL mark resolved via `shared/icons.md` (commons-first — Claude →
`commons/ai/claude.svg`); when no asset resolves, the mark is AI-generated in-scene (a resolved mark, when
available, rides as an extra `--input-image`). Never a hand-drawn HTML/CSS/inline-SVG approximation (the
run-06 cover-photo-hook 20-vertex polygon).

**Non-occluded dominant display → prominent HTML, NOT `prompt_delta`** (see "Faithful prompt-from-rationale"
rule 2). gpt-image renders large display poorly; a dominant word over the scene (not threaded through the
subject) is authored as a prominent HTML zone — large `display` class, the type-craft floors apply.

**Occluded dominant display → AI-baked, but the `prompt_delta` MUST state explicit DOMINANT / large scale.**
This is the ONE legitimate AI-integrated display (HTML can't thread a word behind a figure). cover-hook's
*"system"* is genuinely occluded by the seated figures — correctly kept in the AI — but it baked **ghost-small**
because the prompt said *"lower-center integrated"* with **no scale**, when ref-01 shows it LARGE behind the
figures. Make the scale explicit and weight it early (gpt-image weights earlier words more; see
`.claude/skills/viz-image-gen/references/prompt-patterns-gpt.md` → Core Prompt Structure + quoted-text rules).
Phrase the display block as a dominant element, quoted, with a scale cue, e.g.:

```
…the single large display word "system" (S-Y-S-T-E-M) is the DOMINANT element of the
composition — set in a heavy display face, the letterforms spanning most of the frame width,
the seated figures overlapping and threading in front of the lower half of the letters so the
word reads as integrated into the scene. Sharp text rendering, clean kerning.
```

- Quote the word and (for tricky words) spell it letter-by-letter — quoted strings hit ~99% accuracy vs ~70%
  unquoted (`prompt-patterns-gpt.md` → Text Rendering). NEVER "lower-center integrated" with no scale.
- Counter gpt-image's warm/dark bias when the scale word lands on a warm field (`prompt-patterns-gpt.md` →
  Known Quirks) so the dominant display doesn't ghost out tonally.
- If the AI-large display proves unreliable across run-04 re-rolls, the documented fallback (NOT built here) is
  the layered method — HTML display word + cutout figures composited on top (`prompt-patterns-gpt.md` → Layer
  Method). Note it in the report; do not build it.

**Overlay-asset path + SVG tint (the overlay side of the small-mark route — fix the run-08 overlay-cover).**
When a small mark is composited as an SVG/HTML overlay (above), two mechanical rules govern the overlay so the
mark actually paints — both slug-agnostic:
- **The overlay points at the SLIDE-RELATIVE local copy.** `shared/icons.md` copies the resolved asset to
  `{template_dir}/assets/{name}.svg`; the overlay `src` / slot value is **`assets/{name}.svg`**, never the
  project-root commons path (`.claude/.../commons/…`). The renderer resolves slide-relative first then
  `brand_context`; a project-root path resolves under neither → broken src, glyph never painted (the
  overlay-cover Claude logo).
- **A mark that must take a brand TINT is INLINED, never `<img>`.** An SVG via `<img src="…svg">` is an
  isolated document, so `color: var(--brand-accent)` + `fill="currentColor"` paints BLACK, not coral (the
  overlay-cover starburst shell). A tinted single-colour shell is authored **inline `<svg>`** (`fill =
  var(--brand-*)`); a pre-coloured logo stays `<img>` rendered as-is. See
  `shared/template-conventions.md` + `shared/icons.md`. (The render bake auto-splices a literal `currentColor`
  `<img>` as a backstop — `render_template.py > _inline_tinted_svgs` — but author it inline.)

**Pill fill is a ref read.** A callout/CTA pill's fill colour is READ from the ref and recorded in the
`distinctive_elements` row's `fill` (and `rationale.md` §2), then authored to match — cover-hook's bottom pill
came in brand colour when ref-01's pill is **white**. The HTML pill `background` uses the ref's fill, not a
default brand fill.

---

## Fixed-hero recolor vs free-subject swap (the hero subject — fix the chain miss)

`subject_role` (`identification-tree.md` rule 7, read into `rationale.md` §2) forks the per-post prompt **before**
the edit-mode table below. The two roles produce two different `prompt_delta` openers:

**`subject_role: fixed-hero` — the hero IS the template's identity → RECOLOR the ref, never regenerate the object.**
When the slug names the object (`chain-*`) and the ref shows ONE dominant subject that is the whole point of the
layout, the object is **fixed**. The per-post variation is framing / angle / lighting / scene — **not the object's
category**. So the `prompt_delta` *keeps the subject* and recolors the ref to the brand palette:

```
Keep the EXACT subject from the reference — {HERO_DESCRIPTION, e.g. a metal chain with one accent link}.
Recolor only: the accent element → brand coral ({--brand-accent}); keep the object's form, material, and identity.
Vary only framing, camera angle, lighting, and the surrounding scene per post.
Keep the reference's STYLE (medium / lighting / treatment) and the brand IDENTITY (palette / accent / grain).
No text, no logos. Portrait 4:5.
```

- **`{HERO_DESCRIPTION}` is the FIXED identity read from `distinctive_graphics`, not a `{PHOTO_SUBJECT}` slot.**
  Do NOT write *"Change the subject to: {PHOTO_SUBJECT}"* on a `fixed-hero` — that is the exact
  `chain-highlight-headline` defect (the chain's slot carried example values "neural node / AI chip / robotic
  hand", and the chain — the brand identity — became gears). The recolor is the `Partial — bg + color` posture
  applied to the SUBJECT: the object is preserved, only its accent colour and surroundings move.
- The fixed-hero's slot is **NOT** `user_editable: true` as a free subject. If a per-post slot exists at all it
  carries scene/framing variation, never a free object category. The example values in the
  `[ai-image-zone]` block describe **framings of the same object** ("the chain coiled", "the chain hanging
  vertically", "a close crop of the coral link"), never different objects.

**`subject_role: free-subject` — the hero is a genuine per-post slot → swap it.** The slug describes the layout
(`numbered-photo-rule`); `{PHOTO_SUBJECT}` is a real variation axis and the `Partial — subject only` opener
(*"Change the subject to: {SUBJECT}"*) below is correct. This is the unchanged default.

> One sentence: **`fixed-hero` recolors the ref's object (identity preserved); `free-subject` swaps it.** The
> read (rule 7) decides; the slug is the first hint. The gate (r6g) hard-fails an object-hero that regenerated
> into a different object than the ref.

---

## The 3 edit modes

**Every prompt is built on the edit-from-ref skeleton (`prompt-patterns-gpt.md` → Image Editing). Three lines —
and the Preserve/Match lines are NOT optional padding; they are what stops the model drifting to a generic dark
"documentary" scene (the run-02/run-04 divergence):**

```
Change:   the scene / landscape + the brand content (people, objects, text, palette) — MAY be a whole new landscape
Preserve: the COMPOSITION CONTRACT — framing (full-bleed/contained), reserved-zone position + its luminance,
          integration manner (text-behind-subject / on-surface / on-clean-zone), the arrangement the text depends on
Match:    the legibility/tonal contract — the reserved zone keeps the ref's luminance; never invert bright↔dark
```

**"Preserve" NEVER locks the landscape pixels — it locks the contract.** The scene/landscape lives on the
**Change** line and is free to be remade. What is invariant is the composition contract + the legibility
contract. (qa-kanban `visual-brain`: *"landscape changes per post; composition — POV, clear top, mid zone for
the pill — is fixed."*) The mechanical difference between partial and total is only **how much of the Change
line varies per post** — never whether the contract is preserved.

| Mode | Change line (free) | Scenarios | Contract preserved (locked) |
|---|---|---|---|
| **Partial — subject only** | swap the character/object | A, B2 | bg + full composition + reserved zone |
| **Partial — bg + color** | adapt palette (orange→blue) | any brand-color delta | composition + context |
| **Total — reskin-in-place** | the whole scene/landscape + integrated text | C, B1 | framing + integration manner + reserved zone — NOT "a new composition" |

All three are **`generation_route: edit-from-ref`** with the ref as the first `--input-image`. Total is NOT
"ignore the ref and compose freely" — it is "the whole landscape may change, the composition contract may not".

### Partial — subject only (the default)
```
Same composition and layout as the reference. Change the subject to: {SUBJECT}.
Keep the reference's STYLE — MEDIUM + LIGHTING + TREATMENT (read into rationale §2 `medium:` / `lighting:` /
  `subject_treatment:` and written to the block's `image_style` — e.g. flat vector illustration, natural light,
  full-bleed) and the brand IDENTITY — palette / accent / grain, from ai-image-style.md.
Keep the subject <position — e.g. seated lower-center>.
No text, no logos, no saturated color. Portrait 4:5.
```
- The ref is ALWAYS the first `--input-image`.
- The delta is ONLY the delta — never zones, proportions, or focal points.
- `{SUBJECT}` is a placeholder. Never hardcode the ref's actual subject ("two elderly men reading
  newspapers") — every post would generate the same image.

### Partial — bg + color
Used when the ref's background strays from the brand palette, OR when a per-post color adaptation is wanted.
```
Adapt the palette to [insert color here]. Keep the composition, layout, and context exactly.
```
- **Color is a variable, written `[insert color here]`** in the stored prompt — never a baked hex. At post
  time the generator fills it.
- **Recolor-at-setup (flag-only in v1):** when you read an off-palette ref at setup, you MAY recolor it once
  ("change the color to [brand], keep composition") and bake the recolored version into `ref-canonical` so
  future generations start from the correct color. This is a manual setup move you choose — the quality gate
  in v1 only **flags** palette stray, it does not auto-recolor. (Don't *reject* an off-palette ref; recolor or
  flag.)

### Total — reskin-in-place (C, B1)
The ref LOCKS the composition contract; the scene/landscape + integrated text change. This is NOT "a new
scene" — it is the SAME composition re-skinned. (qa-kanban ref-01 → template: full-bleed group, instructor
centered, giant display word occluded behind the central figure — all preserved; only the people, the
headline text, and the palette were swapped.)
```
Keep the reference's EXACT composition contract: framing (full-bleed), the arrangement the text depends on,
and the integration manner (the display text threaded behind the subject).
Change the scene/landscape to: {CONTENT}, and the integrated display text to "{HEADLINE}".
Match the reference's lighting, tone, and color temperature. Portrait 4:5.
```
- The ref LOCKS the composition contract (framing + integration manner + reserved zone); the landscape/scene
  on the Change line MAY be fully remade per post. Used when text is integrated into the scene (C) or sits
  inside an in-scene surface the AI must build with correct perspective (B1).
- At BUILD/validation, reproduce the ref's scene so the canonical checks against the gabarito (rule 6); the
  free per-post variation is the `{CONTENT}` slot — never "compose a new scene" at build.

---

## ROTA — `scene-restyle-with-real-face` (a hero face carries the BRAND identity, restyled for the medium)

> **Trigger: a human FACE / HEAD is a HERO element of the composition** — prominent, the eye lands on it — in
> ANY medium or style (editorial photo, 3D render, illustration, line-art, or even surreal: a giant head
> sculpted from stone in a desert). The trigger is **the face being hero**, NOT the template being "a creator /
> portrait cover". The medium/style is read from the ref like any other image zone (§ medium/lighting/treatment);
> the IDENTITY of the face is the thing this rota fixes.

**The rule:** when the brand has a **headshot**, the hero face **carries the brand person** (e.g. Simon),
*restyled for the ref's medium* — a photo ref → an editorial photo of them; a 3D-render ref → a 3D render of
them; a stone-sculpture ref → their face in stone. The headshot is the **identity** input; the ref is the
**style/medium + scene** input. **Never an invented face** when a headshot exists.

**Mechanic — image-edit / img2img guided by TWO inputs:**
- `--input-image` #1 = `assets/ref-canonical.png` → carries the **scene, framing, medium, lighting, vignette**.
- `--input-image` #2 = the brand headshot (`brand_context/visual-identity/headshots/*.jpg`) → carries the
  **identity** (it is the same person, restyled — not a reference for "a person like this").
- The `prompt_delta` reproduces the ref's environment + restyles the SAME person into the ref's medium. Seed
  (the prompt Gustavo proved by hand — adapt the scene words to the ref):

```
Restyle the person in the second image (KEEP their identity — same face, same person) into the scene and medium
of the first image: {MEDIUM, e.g. 3D render / oil illustration / stone sculpture}, {SCENE, e.g. seen from afar,
looking to the side, old cinematic camera, dark vignette}. Reproduce the reference's framing, lighting, and
mood. The background is a SCENE, not a flat colour. Portrait 4:5.
```

**Constrain the restyle so the IDENTITY survives the first generation (fix the run-08 portrait-cta — the
restyle invented the face).** Passing the headshot with a bare "keep identity" is not enough: when the restyle
strength is high, the medium/scene transfer overpowers the face and the model regenerates a *different* person
(portrait-cta restyled the scene so hard the real face was lost). The generation-side craft that keeps the face
(slug-agnostic, applies to every `scene-restyle-with-real-face` template):
- **Lower the edit strength / denoise on the identity input.** A scene-restyle is a *partial* edit, not a
  free recompose — keep the edit/denoise strength LOW enough that the headshot's facial structure survives
  (high strength = a new face). Restyle the medium and surroundings, not the bone structure.
- **State an explicit IDENTITY-LOCK in the `prompt_delta`, weighted EARLY** (gpt-image weights earlier words
  more): *"KEEP the exact identity of the person in the second image — same face, same facial structure, same
  features; restyle ONLY the medium and scene around them."* The identity clause leads; the medium/scene
  clause follows. Never let "3D render / oil painting / stone" outrank "same face".
- **Restyle the MEDIUM + SCENE, never the FACE GEOMETRY.** Phrase the medium transfer as a surface/material
  change (*"render their skin and hair in the {MEDIUM}'s surface"*), explicitly preserving proportions, eye
  spacing, nose/jaw shape — the things a viewer reads as "it's the same person".
- **When the restyle is heavy by nature** (a face → stone, a face → flat cartoon), prefer **compositing the
  real face** (img2img on the face region at low strength, or a face-region paste) over a full-frame restyle
  that the strength would otherwise overpower. The medium transfer runs on the scene; the face keeps the
  headshot's geometry.
> This is the GENERATION-side craft that makes the face survive in the first place. A parallel output
> face-MATCH gate catches a face that drifted anyway; this rule is what stops it drifting. The two compose —
> the gate is the backstop, the craft is the cause-side fix.

- **Carry the SCENE's provenance, not "never AI".** This is `ref-first → image-edit`: the scene is generated
  (`when_ai_runs: every post` if the scene varies; setup-only if fixed), the *identity* comes from the headshot.
  The slot contract declares the target framing and that **the background is a SCENE** (recreate the ref's
  environment), never a flat fill behind a floating head (the "rostão em fundo chapado" miss).

**The headshot RESOLVES IN THE BUILD when it exists — never deferred to post-time as a string placeholder.**
This is the hard part the `creator-cover-cta` build got wrong (the contract prose was right; the build dropped
it):
- When a headshot is available, the build **resolves it** — passes the real `headshots/*.jpg` path as
  `--input-image` #2 and generates with the brand person. It must NOT leave the identity slot as a literal
  string like `"(filled from brand-headshot: …simon-pic.jpg)"` (the `creator-cover-cta` `metadata.json:17`
  defect — the slot never resolved, so the generator fell back to a generic description).
- **`PHOTO_SUBJECT` MUST NOT be a generic person description when a headshot exists.** The
  `creator-cover-cta` build passed `PHOTO_SUBJECT: "a male creator, dark hair, confident expression, arms
  crossed"` — a generic invented person, which is what the generator actually consumed → a random face. With a
  headshot, the subject is *the brand person via the headshot input*, not a prose description of "a person".
- **The text marker is a TEXT placeholder in the slot, not a hole in the image.** When NO headshot exists yet,
  the identity slot carries a *text marker* (e.g. `[fill with the brand headshot when one exists]`) so a future
  headshot drops in — and **the image still generates normally with a generic person in the ref's style**
  (the soft default below). The marker documents the intent; it never blocks the render or leaves a gap.

**Default suave — no headshot → the AI invents the person in the ref's style (NOT a block).** When the brand has
no headshot, the rota still applies for the *scene/medium* (recreate the ref's environment + framing), and the
AI invents a person in that style. This is valid output — the brand identity simply does not enter until a
headshot exists. The ONLY hard rule is: **headshot exists → use it (no generic subject); headshot absent →
generic person is fine.**

> ⚠️ **Identity under heavy stylization is a by-eye call, not a deterministic check.** How recognizable the
> brand person stays through a heavy restyle (face → stone) is Gustavo's judgment on the re-gen — the rota
> *defines* that the hero face uses the headshot; the gate (r6g item 9) only catches the deterministic failure
> (slot left as a placeholder / `PHOTO_SUBJECT` generic when a headshot is declared).

---

## The generation moment — WHEN the AI runs (not partial vs total)

This is the cost lever. Three cases:

| Case | AI runs | Template stores | At post (handoff) |
|---|---|---|---|
| **bg fixed** (B2 texture, A frame) | **1× at setup** | static `bg.png` + reusable HTML | swap text in HTML only; **ZERO AI on bg** |
| **variable element** (subject/character) | **every post** | `ref-canonical` + **validated prompt** (delta = `{SUBJECT}`) | AI runs with the new subject inside the proven prompt |
| **full recompose** (C, B1) | **every post** | `ref-canonical` + **validated prompt** (delta = content) | AI recreates with new content in the proven prompt |

This is what reconciles the AI-first direction with cost: bg-fixed forms generate once at setup → no AI at
post time; recurring AI only fires when the subject genuinely varies.

---

## Test-and-save the validated prompt (setup, runs 1×)

For the **variable** and **full-recompose** cases, the prompt is proven at setup and never reinvented later:

1. At setup, generate **once** with the example content — fill `{SUBJECT}` with `image_zone.subject_hint`.
   The example subject is derived from the brand's tone (`voice-profile.md` + `ai-image-style.md`, already
   extracted at onboarding) — a serious brand gets a serious example, a young brand a young one. It is not a
   fixed generic and is not asked of the user.
2. The quality gate approves the render (`shared/quality-gate.md`).
3. The **prompt that passed is the one written** into the `[ai-image-zone]` block's `prompt_delta`. Mark it
   `# validated-at-setup` so a reader knows it cleared the gate.
4. At post handoff, `ssc-image-generator` **inherits** this prompt and fills only the delta (`{SUBJECT}` or
   content) — it never reassembles a prompt blind.

This single setup test produces two results at once: the example image (becomes the user-facing **preview**)
and the proven prompt (saved in the template).

> **Out of scope (v1):** versioning the validated prompt when the brand later changes palette/font (the
> recolor baked into `ref-canonical` would need redoing). Not handled in v1 — noted deliberately.

---

## Reserved-zone prompting (the hybrid, B2)

The hybrid (AI image + HTML text over it) only works with **deliberate coordination**: the AI must generate
the image with a clear, low-detail clean zone where the HTML text will land, so HTML fills a zone the image
*guaranteed* — no coordinate-guessing.

**The band is the ref's band — read its position, never re-choose it (fix REMONTA).** WHICH band gets reserved
(top / bottom / left / right) is anchored to `ref_vision_summary.text_elements[].position`
(`identification-tree.md` rule 4). The `prompt_delta` reserves THAT band and the HTML text lands in THAT band —
no inverting top↔bottom. The ref-05 miss was a build that reserved the **bottom** when the ref reserves the
**top sky**; the band is a fact you read, not a layout convenience.

```
…compose the scene so the <ref's reserved band — e.g. the top sky> is a calm, low-detail,
bright area with room for a headline — keep busy detail and the subject out of that band.
```
- Validated by hand 2026-06-08 on `ref-visual-brain-body`: the model reserved a bright low-detail top zone;
  an HTML headline + body-pill overlay landed correctly on it.
- Residual risk: **zone consistency** across N generations. The breathing-room gate (crop the reserved band,
  measure uniformity + luminance + black-text contrast) is what catches a generation that didn't reserve the
  zone — it then re-rolls with the reserved-zone instruction reinforced.

### Legibility method copies the ref — natural composition vs band (fix INVENTA)

How the text stays legible over the photo is a **read of the ref**, recorded per block in `rationale.md` §2 as
`legibility-method: ref-band | natural-composition` — see `agents/ssc-template-builder.md` (the scrim rule) and
`craft/html-craft.md` §4.

- **`natural-composition`** (the ref has NO band — legibility comes from the scene being calm/dark where the text
  sits): the bg `prompt_delta` instructs the AI to **generate that calm/dark zone in the scene** (reserved-zone /
  composition prompting, above), and **NO `.bottom-scrim` div is authored**. The legibility lives in the generated
  scene, matching the ref. Stamping a solid band the ref lacks is the **run-02 INVENTA** miss (creator-cta /
  numbered-fullbleed scrims over refs that resolve naturally).
- **`ref-band`** (the ref DOES show an intentional band / scrim / solid strip): reproduce it — the solid
  semi-opaque band guidance in the scrim rule applies HERE (and only here).

---

## In-scene per-post elements

Elements that change per post and sit *in* the scene (a character, an object overlapping/behind something)
are placed by the **AI**, not HTML pasted on top — the AI fits overlap and occlusion the way a flat HTML
layer cannot. (HTML overlays are for isolable text and badges that sit cleanly *on top* — see
`craft/html-craft.md`.)

---

## Cutout-on-solid corollary

When a subject sits over a solid-color bg (CSS bg + AI subject), generate the subject with its background
REMOVED (transparent) so the brand color shows through, then composite. Never let the subject carry a baked
background that hides the solid brand color. Pass `--background transparent` (or post-cut).

---

## Safe-zone margin (canvas edge rule — AIOS-190)

AI-integrated text must never sit at the very pixel-edge of the generated canvas. A tiny aspect-ratio
delta from GPT-image-1 (or any model that doesn't return exactly the requested ratio) combined with
`object-fit:cover; object-position:center` crops the very top or bottom pixels. Rule:

- **Do NOT place AI-integrated content within 8% of any canvas edge.** In `prompt_delta`, phrase as:
  *"in the upper area of the frame, leaving at least 8% margin from the top edge"* — never *"at the
  top of the canvas"*.
- **Use `object-position: center top` (not `center`) on the image container** whenever the AI-integrated
  composition has content near the top of the frame. This anchors the top of the image so any
  aspect-ratio mismatch crops at the bottom instead of the top.
- Top-heavy compositions (kicker at top, headline near top) always get `object-position: center top`.
  Vertically-centered compositions can use `object-position: center`.

### Anti-patterns (safe-zone)

- ❌ `"At the top of the canvas, short kicker text…"` — use `"In the upper area of the frame, leaving
  at least 8% margin from the top edge, short kicker text…"` instead.
- ❌ `object-position: center` on a full-canvas AI-integrated image zone that has top-area content —
  use `object-position: center top` to prevent aspect-ratio-mismatch clipping.
