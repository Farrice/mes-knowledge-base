# Builder reference — `rationale.md` authoring spec (Step 0.5 deep detail)

> Read at **Step 0.5**, when writing `rationale.md`. The agent spine carries the 4-section skeleton + the blocking rule; this file carries the per-field READ spec for each section. Looking ONLY at the ref.

`rationale.md` has **exactly these 4 sections** (headers, in order). Each must be substantive; an empty or `n/a` section is FORBIDDEN and Check A will block generation.

```markdown
# rationale — {slug}

## ① Form + tree-path-with-why
form: <a-framed-image | b1-surface-placeholder | b2-filled-bg | c-integrated-text | solid-css>
<each tree decision you took WITH its reason — not "Q2 yes" but "Q2 yes → the CRT screen is a blank in-scene
surface holding the headline, so the tree STOPS here at B1">

## ② Per-block breakdown
<for EACH text/content block: `<block> · <treatment> · <mechanism/why>` where treatment is one of
AI-integrated | HTML-isolable-overlay | icon-chrome, and the why is the isolability test applied to THAT
block (per block, not per slide) — "Headline · AI-integrated · occluded behind the subject, HTML can't occlude".
For EACH **distinctive element** (a display word, a seal / badge / logo, a callout pill, a graphic device — NOT
chrome), ALSO record the PER-ELEMENT REF-ANCHORED read on its line (the `distinctive_elements` row from
`identification-tree.md` rule 5, auditable + gate-checkable):
  - `present: <true|false>` · `position: <quadrant/band>` · `size: minor|medium|dominant`
    · `fill: <colour>` · `value: solid|ghosted|tonal` — every field READ from THE ref, never inferred. (You
    receive exactly ONE ref, so there is no which-ref to misattribute — but the read errors remain:) inventing
    an absent element or inflating size is the **body-numbered** miss (a `minor` lower-left coral callout box
    stretched to a full-width mid-canvas strip). The authored bbox MUST match the read: a `minor` lower-left
    box is authored small and lower-left, never full-width.
  - `value: solid | ghosted | tonal` — READ the element's OPACITY/value from the ref, EXPLICITLY (it is a
    fidelity attribute, not an afterthought). `ghosted`/`tonal` = the element is faint / low-opacity /
    watermark-strength in the ref; the authored `opacity` on the zone MUST match it (a ghosted display word →
    `opacity:0.10–0.18`, never full strength). `solid` is the default ONLY when the ref shows full strength —
    never assumed when the read is silent. The **statement-scene** miss reasoned treatment/position/size/fill
    for a ghosted "setup" word but never declared its opacity, so the builder defaulted it solid and shipped a
    near-solid word the ref ghosts (`identification-tree.md` rule 5; the `opacity` hook is
    `shared/template-conventions.md` #8).
  - `treatment: HTML | SVG-overlay | AI-baked` — routed by `identification-tree.md` rule 6: a small brand mark
    (badge/seal/logo) → `SVG-overlay` (the AI drops it); a dominant display NOT occluded by the subject → `HTML`,
    prominent; a display genuinely OCCLUDED by the subject → `AI-baked`, prompted at DOMINANT scale. This feeds
    the prompt-from-rationale routing in Step 3.
For the image / photo / hero block, ALSO record these ref-reads on its line (auditable + gate-checkable). The
three STYLE reads (`medium` / `lighting` / `subject_treatment`) are the template's own style — READ from THIS
ref, each defaulting to the grade's `default_*` ONLY when the ref is genuinely ambiguous — and they are what
Step 4 WRITES into the `[ai-image-zone]` block's `image_style` (the load-bearing step — without it the
image-generator falls back to the grade and the per-template style is lost, the run-07 class of miss):
  - `medium: <photo | flat-illustration | watercolor | sketch | 3d-render | …>` — the medium THIS ref's image is
    in, READ from the ref (a cartoon ref reads `flat-illustration`, a documentary photo reads `photo`). This is
    the medium the build inherits — the prompt opens in it (Step 3 → `ai-prompt-craft.md` "Medium, lighting and
    treatment are the ref's"). By default the brand's `ai-image-style.md` `default_medium`; when THIS ref plainly
    diverges from it, follow the ref and say why on the line (e.g. "`medium: flat-illustration` — the brand
    default is `mixed`, this ref is a flat vector cartoon"). Only when the ref's medium is genuinely ambiguous do
    you fall back to `default_medium`.
  - `lighting: <dramatic | natural | studio-flat-soft | none>` — the lighting THIS ref's image shows, READ from
    the ref (a hard-shadowed ref reads `dramatic`, a soft even ref reads `studio-flat-soft`). Default = the
    grade's `default_lighting`; when THIS ref plainly diverges, follow the ref and say why. Fall back to
    `default_lighting` only when the ref's lighting is genuinely ambiguous.
  - `subject_treatment: <isolated-on-light-bg | full-bleed | inset-with-shadow | cutout>` — how THIS ref frames
    its subject, READ from the ref (a knocked-out subject on white reads `isolated-on-light-bg`, an
    edge-to-edge scene reads `full-bleed`). Default = the grade's `default_subject_treatment`; follow the ref
    when it diverges + say why; fall back to the default only when ambiguous. **The marca fixes the IDENTITY —
    palette / accent / grain; medium / lighting / subject_treatment are the ref's call (this template's style).**
  - `containment: contained-rectangle | full-bleed` — copied from `ref_vision_summary.image_zone.containment`;
    the build must match it (a contained ref → a contained image zone, never a full-bleed face — REMONTA).
    **INSET (contained) photo vs FULL-BLEED background photo route to different forms** (`identification-tree.md`
    Q3 routing): an inset/framed photo → Q3/Form A; a full-bleed bg photo → B2 or C, generated `edit-from-ref`
    on the scene, **never `texture-extract`** (texture-extracting a full-bleed scene deletes it — the
    numbered-text/photo miss).
  - `subject_role: fixed-hero | free-subject` — (`identification-tree.md` rule 7) is the hero subject the
    template's **IDENTITY** (the slug NAMES the object — `chain-*` — and the ref shows ONE dominant subject →
    `fixed-hero`) or a genuine per-post slot (the slug describes the LAYOUT → `free-subject`)? READ it; the slug
    is the first hint. `fixed-hero` → the per-post prompt **recolors the ref** (keep the object, recolor accent),
    no free `{PHOTO_SUBJECT}`; `free-subject` → "change the subject" is correct. The `chain-highlight-headline`
    miss read a fixed-hero (the chain) as free → the chain became gears. Routes the Step 3 prompt
    (`craft/ai-prompt-craft.md` "Fixed-hero recolor vs free-subject swap").
  - `hero_face_identity: brand-headshot | invented | n/a` — when a human **face/head is a HERO element** (any
    medium/style, `subject_treatment` notwithstanding — even surreal, e.g. a stone-sculpted head), does the
    brand have a headshot? `brand-headshot` (a headshot exists → the build RESOLVES it as the identity
    `--input-image`, the face carries the brand person restyled for the ref's medium — NEVER a generic
    `PHOTO_SUBJECT` person description) · `invented` (no headshot → the AI invents the person in the ref's style,
    the valid soft default) · `n/a` (no hero face). Routes the `scene-restyle-with-real-face` ROTA
    (`craft/ai-prompt-craft.md`). The `creator-cover-cta` miss: a headshot existed but the slot stayed a string
    placeholder and `PHOTO_SUBJECT` was generic → random face.
  - `legibility-method: ref-band | natural-composition` — for ANY block whose legibility relies on the photo
    behind it: `ref-band` only when the ref shows an intentional band/scrim/strip (then a solid scrim div is
    authored); `natural-composition` when the ref has no band (then the dark/calm zone is GENERATED in the scene
    via the `prompt_delta` and NO `.bottom-scrim` div is authored — INVENTA). See the scrim anti-pattern.>

## ③ Pipeline
edit_mode: <partial-subject | partial-bg-color | total-recompose | none>
when_ai_runs: <setup-only | every post>
extraction: <what the AI cleans/recreates + which zones become HTML>

## ④ Ambiguity (examined)
<PROOF you weighed the alternatives. Ruling one OUT with a reason is valid and good —
"No ambiguity — ruled out B1 because there's no blank in-scene surface; the texture is the bg, not a content
surface." Empty / "n/a" / a bare "none" is FORBIDDEN. The test is "did you show you looked at alternatives?",
NOT "did you find a problem?".>
```

The qa-kanban gabarito (`testbeds/qa-kanban/data.js`) is the QUALITY BAR for this artifact — read it once to
calibrate the LEVEL (the per-block `why`, the ambiguity flag like "the sticky notes are SATELLITE in-scene
surfaces…"); do NOT paste it as few-shot. Every `rationale.md` must reach that level for THIS ref.
