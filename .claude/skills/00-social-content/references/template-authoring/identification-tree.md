# Identification tree — Layer 1 (the WHAT)

> `ssc-template-builder` rebuild (AIOS-190). This is the FIRST thing the builder reads. It picks the **form**
> by reading the reference (a present fact), then reads ONLY the matching `scenarios/<form>.md`. Reading one
> scenario instead of all five is what slims the prompt.
>
> **Principle:** the form comes from READING the ref, never from predicting the result. The default is **AI
> generates**; HTML is the surgical exception. The quality gate corrects after.

---

## Step 0 — capture `ref_vision_summary` (quick read, NOT measurement)

Read THE ref directly (the builder receives exactly one). This is a fast read — you are NOT extracting bbox
percentages or calm/focal zones. The ref itself carries the composition; it is reused as the image input
later. Capture only:

```yaml
ref_vision_summary:
  bg_treatment: scene-full-bleed | textured-paint | solid-color | physical-placeholder
    # physical-placeholder = the scene contains a blank surface (billboard, screen, frame, paper)
    # that holds the slide's content
  text_placement: outside-image | inside-surface | on-reserved-zone | integrated-complex
    # RENAMED from text_composition_type. 4 values, one per scenario (see the map below).
  text_elements:
    - role: headline | body | numeral | caption
      position: top | center | bottom | left | right   # approximate — NOT %. BINDING for the
                                                        # reserved band: the HTML text zone lands in
                                                        # the SAME band the ref reserves (rule 4 below).
                                                        # No inverting top↔bottom (the REMONTA miss).
      color: light | dark                               # readable against its background
      isolable: true | false                            # the per-block isolability test (see below)
  distinctive_elements:                                 # NEW — the per-element ref-anchored read (rule 5).
    # One row per DISTINCTIVE element: a display word, a seal/badge/logo, a callout pill,
    # a graphic device. NOT chrome (masthead/pagination). Each field is READ from THE ref,
    # never inferred — inventing or inflating an element is the body-numbered miss (a minor
    # lower-left callout pill authored full-width). See rule 5.
    - element: "<short name, e.g. coral-callout-pill | display-word 'system' | Claude starburst seal>"
      present: true | false                             # does the ref ACTUALLY have it (READ, never guessed)
      position: top-left | lower-left | center | ...    # quadrant / band (approximate)
      size: minor | medium | dominant                   # coarse band, NOT a guessed bbox %. `dominant` = the
                                                        # element commands the canvas (e.g. a display word
                                                        # behind the figures); `minor` = a small mark / pill
      fill: "<the element's fill colour, e.g. white | coral | dark>"  # READ from the ref (the pill came in
                                                        # brand colour when ref-01's bottom pill is white)
      value: solid | ghosted | tonal                    # READ the element's OPACITY/VALUE from the ref. `solid`
                                                        # = full-strength (the default). `ghosted` = low-opacity /
                                                        # watermark / faded — the element reads FAINT against its
                                                        # bg (a large ghosted display word, a watermark). `tonal`
                                                        # = present at a reduced tint, not full strength. When
                                                        # ghosted/tonal, the authored opacity MUST match (e.g.
                                                        # `opacity:0.12`) — defaulting it solid ships the wrong
                                                        # element (the run-08 statement-scene "setup" word read
                                                        # as solid near-black, authored full-opacity, when the ref
                                                        # ghosts it). See rule 5.
      treatment: HTML | SVG-overlay | AI-baked          # routes per rule 6 below (feeds rationale §2)
  image_zone:
    exists: true | false
    containment: contained-rectangle | full-bleed       # NEW — the discriminator that isolates Form A
    medium: photo | flat-illustration | watercolor | sketch | 3d-render | …  # the ref's MEDIUM, READ (a cartoon
                                                        # reads flat-illustration). The builder's §2 STYLE read;
                                                        # grade `default_medium` is the fallback when ambiguous.
    lighting: dramatic | natural | studio-flat-soft | none   # the ref's LIGHTING, READ (hard shadows → dramatic,
                                                        # soft even → studio-flat-soft). Per-template STYLE, NOT
                                                        # brand-fixed; grade `default_lighting` is the fallback.
    subject_treatment: isolated-on-light-bg | full-bleed | inset-with-shadow | cutout  # how the ref FRAMES the
                                                        # subject, READ. Per-template STYLE; grade
                                                        # `default_subject_treatment` is the fallback when ambiguous.
    subject_hint: "short description of the ref's subject"
    subject_role: fixed-hero | free-subject   # NEW (rule 7) — is the hero subject the template's IDENTITY
                                              # (slug names it + ONE dominant ref subject → fixed-hero, the
                                              # per-post prompt RECOLORS the ref) or a per-post slot (the slug
                                              # describes the layout → free-subject, "change the subject" is
                                              # correct)? Read it; the slug is the first hint. Routes the edit
                                              # mode (ai-prompt-craft.md "Fixed-hero recolor vs free-subject swap").
    distinctive_graphics: "<faithful short description, or none>"
      # the signature NON-TEXT visual device(s) ANYWHERE on the canvas — the SCOPE is the WHOLE
      # canvas, bg-level devices included, even though the field lives under image_zone for schema
      # continuity: a radial line-burst / engraving sunburst, a halftone field, an airbrush/spray
      # wash, a line-art motif, a pattern/texture, a framing rule, an emblem. A bg-level device
      # MUST be captured here too — run-06: ref-03's orange airbrush washes lived OUTSIDE the
      # image_zone slot, were never captured, and a blanket "no marks" deleted them. A short
      # faithful description (ref-01: "orange radial line-burst behind the figures"), NOT just the
      # palette enum. The bg prompt_delta MUST carry these (see craft/ai-prompt-craft.md rule 5) —
      # dropping them is the ESQUECE miss (palette kept, device lost). `none` only when the WHOLE
      # canvas genuinely has no distinctive device.
    ref_path: "<the ref's path>"
  embedded_icons:                                        # SMALL marks only — never the hero
    - kind: brand-logo | app-icon | pictogram | brand-badge
      position: top-left | top-right | center | ...      # approximate
  chrome:
    masthead: <visible in ref?>      # record it, but FOLLOW tokens.json (disabled → don't inject)
    pagination: <visible in ref?>    # same
```

**Rules:** honor `tokens.json > chrome.*` (disabled there → do not inject even if the ref shows it). The hero
scene is ONE image zone — never rebuild an AI scene out of HTML `<div>`/`<svg>`/CSS layers.

---

## The decisive routing question (OVERRIDES any default-to-HTML tendency)

Before the form tree and inside every per-block text decision, ask ONE question — it routes the substrate
(who renders the text), case-agnostic:

> **Is this text bound to an object's geometry/lighting — does it have to obey perspective, glow, occlusion, or
> relief to belong?**
>
> - **YES → AI bakes it.** Belonging requires the object's own physics: the skew/perspective of a tilted
>   surface, a screen's glow on the glyphs, a subject occluding letters, the recolor of a slat behind the words,
>   the deboss/grain of a printed surface. HTML can only float a flat rectangle in front — it cannot put type
>   *on* a tilted billboard or *behind* a person. **The image models render supplied text faithfully and
>   legibly; route object-bound text to AI baking with confidence** — the fix for a past hallucination is to
>   FEED the correct text into the prompt (plus a letter-fidelity check and a negative against invented/extra
>   text), never to retreat to HTML.
> - **NO — the text sits on a flat reserved field** (a clean surface, a calm low-detail band, a solid colour
>   third) **→ HTML overlay.** Nothing to integrate with; HTML wins on crispness, editability, exact brand type,
>   and per-post swaps without re-generating the image.
> - **MIXED scene → HYBRID:** the AI bakes the scene (and any text that must ride an object) AND **reserves a
>   clean band** for the HTML; the bake prompt must explicitly leave that calm/margin zone so the overlay lands
>   on emptiness, not on busy texture.

**This rule OVERRIDES any tendency to default to HTML.** Where a prior pass pushed HTML onto text that sits on
an object, it routes back to AI-baked.

**Signals that text is OBJECT-BOUND** (→ AI-bake): text on a signboard / billboard slat · text on a screen /
glass / CRT phosphor · text on a post-it / physical label / sticker · a headline woven with a full-bleed
subject (letterforms threaded behind / in front of a figure) · text in relief, embossed, or printed on a
textured surface. A multi-item list on slats is object-bound like any other on-surface text — the items ride
the slats; feed them into the bake, never retreat to flat HTML.

---

## The ordered tree — first match wins, STOP at the first match

The **order of the questions IS the tie-break rule.** Walk top to bottom; the first `yes` is the form.

```
1. TRULY solid color — zero texture AND no image at all?    → solid-css         (scenarios/solid-css.md)
2. Is there a blank SURFACE inside the scene                → b1-surface        (scenarios/b1-surface-placeholder.md)
   (screen / frame / paper / billboard) holding content?
3. Is the image contained in a rectangle (not full-bleed)? → a-framed-image    (scenarios/a-framed-image.md)
4. Is the text integrated / overlaid on the scene with     → c-integrated-text (scenarios/c-integrated-text.md)
   no isolable container (fails the isolability test)?
5. Default: full texture / landscape, text floats on a     → b2-filled-bg      (scenarios/b2-filled-bg.md)
   reserved clean zone.
```

Q1 reads `bg_treatment == solid-color` + `image_zone.exists == false`. Both conditions are required:
the background must be a flat fill with **zero texture** AND **no image**.

> **Q1 trap — textured near-white ≠ solid.** A light or near-white background is NOT automatically solid.
> If it carries *any* texture — paper grain, grid/dot lines, a subtle corner gradient or vignette, a faint
> noise field — it is `textured-paint`, not `solid-color`, and Q1 must answer **no**. It routes onward (a
> textured fill with no surface, no framed rectangle, and isolable text typically lands at C). On a fast read,
> a pale paper-grain card reads as "white = solid" — resist that; check for texture before calling Q1 `yes`.
>
> **Q1 trap (corollary) — a warm / muted TONE is not evidence of paper.** Paper is a *material* (grain, fibre,
> dust, fading) — not a colour temperature. A warm, sandy, hazy or muted PHOTOGRAPHIC scene (a desert, a beach,
> a dusk landscape, a sepia interior) is a **`scene-full-bleed`**, never `textured-paint`/kraft, even though its
> palette overlaps a kraft tone. The discriminator is *depicted content*: does the field show a SCENE (sky,
> ground, water, a horizon, an object) or only a flat surface texture? A scene → it carries a subject and stays
> a photo/illustration (it routes through Q3/Q5 as an image zone, and any bg generated for it is `edit-from-ref`
> on the scene — **never `texture-extract`**, which would strip the landscape to a blank kraft sheet). "Warm =
> paper" is the numbered-text-rule class of miss (a full-bleed warm landscape read as kraft and texture-extracted
> → the scene vanished into a flat tan field). Read the *material*, not the *temperature*.

Q2 reads `bg_treatment == physical-placeholder` (a blank in-scene surface).
Q3 reads `image_zone.containment == contained-rectangle`.
Q4 reads `text_placement == integrated-complex` (decided by the isolability test, below).
Q5 is the fallthrough (`on-reserved-zone`).

**The tree has EXACTLY five forms.** The walk ENDS at one of the five — NEVER synthesize a hybrid form at the
fallthrough ("solid-css extended" was invented at the Q5 fallthrough in run-06; forbidden). A ref that doesn't
feel like a clean fit still routes to one of the five (Q5 is the catch-all); the discomfort goes in
`rationale.md` §④ as examined ambiguity, never into an invented sixth form.

> **Q3 trap — a bright / calm / hazy zone of a full-bleed scene is NOT a background.** `contained-rectangle`
> requires a HARD photographic edge with a **DIFFERENT MATERIAL** (paper, a solid fill) visible on all four
> sides of the image. The test: *does the scene's texture (water, sky, haze) continue past the claimed edge?*
> Same-texture continuation = `full-bleed`, and Q3 answers **no**. A calm zone of the scene is a candidate
> reserved band (B2) or integration area (C) — never a "background" that contains the rest. (The run-06
> numbered-photo-callout miss: ref-04's full-bleed teal water read as "contained-rectangle + kraft paper" —
> the model's THIRD escape hatch on that ref, after the invented scrim and the inverted tone. A read that
> invents a material the ref doesn't show is a wrong read.)

> **Q3 routing — INSET (contained) photo vs FULL-BLEED background photo are different forms.** Q3 is the gate
> for the **inset** case ONLY: a photo *contained/framed* inside a bounded rectangle, with a different material
> (paper / fill) around it on all four sides → **Q3 yes → Form A** (the image sits in a frame; text goes
> OUTSIDE it in a clean HTML zone). A **full-bleed background photo** (a scene that bleeds edge-to-edge and the
> text floats *over* it) is **NOT** Q3 — it falls through to **B2** (`on-reserved-zone`, text on a reserved
> clean band of the scene) or **C** (`integrated-complex`, text woven into the scene). The discriminator is the
> SAME hard-edge test as the trap above: a different material visible on all four sides = inset/contained (A);
> the scene's own texture continuing to every edge = full-bleed (B2/C). **A full-bleed background photo is a
> SCENE generated `edit-from-ref` (Route A — the ref drives the composition) — never stripped to bg texture via
> `texture-extract` (Route C).** Route C is for a *fixed surface texture with no subject* (kraft, paper grain);
> a full-bleed scene HAS a subject and a composition the text depends on, so texture-extracting it deletes the
> scene (the numbered-text / numbered-photo class of miss — a full-bleed photo bg routed to kraft/texture). The
> two-line takeaway: **inset photo → Q3/Form A · full-bleed bg photo → B2 or C, scene route, never
> texture-extract.**

> **Q3 object-isolability — an IMAGE block earns a bounded HTML `<img>` only when it is genuinely isolable.**
> Routing an image block to a contained HTML `<img>` slot requires ALL of: flat, axis-aligned, non-overlapping,
> and free of scene treatment (no rotation, no perspective, no cast shadow, no occlusion). Cards / props lying
> on a surface with rotation + overlap + cast shadows are **in-scene objects** → AI-placed (see
> `craft/ai-prompt-craft.md` "In-scene per-post elements"), never flattened into axis-aligned `<img>` slots
> (the run-06 index-card-cover miss: ref-03's fanned, overlapping, shadowed cards flattened into 3 axis-aligned
> `<img>` slots — the scene treatment IS the look). Echoed in `scenarios/a-framed-image.md` Build.

> **Q4 tie-breaker — a big display word over a single-hue field (fix the C-vs-B2 flip).** When the deciding
> block is a **large display word sitting over a single-colour / single-hue field** (e.g. ref-01's *"system"*
> on the flat coral), Q4 is under-determined: read as occluded → **C**, read as a clean reserved band → **B2**,
> with no tie-break — so the *same* ref came out split-HTML (B2) in one run and total-recompose-AI (C) in
> another (the D2a form instability). Resolve it deterministically by the isolability of THAT display word
> alone:
> - the display word is **genuinely occluded by the photographic subject** (a figure threads in front of /
>   behind the letterforms, so HTML can't reproduce the layering) → **Q4 yes → C**, and the word routes
>   `AI-baked` at dominant scale (rule 6).
> - the display word is **NOT occluded** (it sits cleanly over the single-hue field, rippable into HTML) →
>   **Q4 no → fall through to B2**, and the word routes `HTML`, prominent (rule 6). HTML is the default for a
>   non-occluded display — never route a clean dominant word to the AI.
>
> The single test — *"is THIS display word threaded through the subject, yes or no?"* — gives the same answer
> every run, so the same ref reads to the same form. (ref-01: *"system"* IS threaded behind the seated figures
> → C, AI-baked-dominant. Confirm against ref-01's `rationale.md` in pre-flight.)
>
> The same test extends to **WOVEN typography**: a block threaded by OTHER ELEMENTS — a callout pill over the
> letterforms, a highlight knockout inside a word, a caret in the baseline, tilted labels crossing the type —
> is "occluded" in exactly the same sense, with NO photographic subject required. Woven → Q4 yes → **C**
> (qa ref-03 Chazon); clean over the field → B2.
>
> **A brand `text_policy` does NOT demote a Q4-yes woven composition into B2 (fix the run-08 highlight-pills
> flattening).** `text_policy` (`ai-image-style.md`) is a **rendering-substrate** decision — *is type baked by
> the AI or laid as HTML* — NOT a **form** decision. A Q4-yes woven/overlapping/icon-anchored cluster STAYS
> **Form C**; `text_policy: html-overlay` only chooses HOW Form C is rendered, it does not flip the form to B2.
> The run-08 highlight-pills miss used `text_policy: html-overlay` to route a woven tilted-pills-over-headline
> ref to B2, and the B2 path produced **flat isolated chips** — the tilt, the icon-anchor, and the
> headline-overlap (the entire point of the composition) were lost. The precedence is fixed:
> - **`text_policy: ai-allowed`** (or unset) → Form C is AI-integrated: the woven pills + headline are baked
>   together by the AI (the default Form-C treatment).
> - **`text_policy: html-overlay`** → Form C is rendered in HTML, but the **HTML MUST REPRODUCE the woven
>   composition** — the pill **tilt** (CSS `rotate`), the **icon-anchor** (icons pinned to the pills), and the
>   **headline overlap** (z-index stacking with real overlap, pills sitting OVER the letterforms). It is NOT a
>   licence to flatten the cluster into axis-aligned isolated chips in a tidy row. If the HTML cannot reproduce
>   the tilt + anchor + overlap, the cluster is AI-integrated regardless of `text_policy` (HTML that drops the
>   composition is worse than baking it). Either way the FORM stays C and the **woven look is preserved** — a
>   `text_policy` never buys a flattened B2.

---

## The form → scenario map

| Form | `text_placement` | What the AI returns | Where text goes | Who places the text |
|---|---|---|---|---|
| **A — framed** | `outside-image` | image inside a contained rectangle | outside the image, clean HTML zone | **HTML** (bounded zone — safe) |
| **B1 — surface in-scene** | `inside-surface` | scene with a blank screen/frame/paper | inside the scene's surface | **AI** (respects perspective; HTML misses) |
| **B2 — filled texture/landscape** | `on-reserved-zone` | full bg + a deliberate clean zone | over the bg, in the reserved zone | **HTML** (known zone, not guessed) |
| **C — integrated text** | `integrated-complex` | complex composition, text in the scene | overlaid / behind an object | **AI** (fits it better) |
| **solid** | (n/a) | nothing (no generation) | over solid color | **HTML / CSS** |

---

## The text-isolability test (routes text WITHIN a scenario: HTML vs AI-placed)

Runs **per text block, not per slide.** A single slide can mix treatments — e.g. a headline floating on the
scene (AI / reserved clear zone) + a body inside a pill (HTML overlay). The scenario fixes the *form*; within
it each text block runs this test separately, and sets its own `isolable` field in `ref_vision_summary`.

Negative rule (easier to apply):

```
A text block goes to HTML IF it is:
  - fully in an isolated spot (not overlaid on the scene), AND
  - without heavy effects, AND
  - in a recognizable font (one the AI reproduces).
Otherwise (overlaid / heavy effects / exotic font) → the AI places the text.
```

Mental test: *"Can I rip this text out and drop it into clean HTML without losing the look?"* — Yes → HTML
(`isolable: true`). No → AI (`isolable: false`). Checkable at ref-read time; it is part of identification,
not output prediction.

**A block ALSO fails isolability when it is part of a WOVEN typographic composition — subject-occlusion is ONE
failure mode, not THE definition.** When another element overlaps or threads the block's letterforms — a
callout pill sitting over the headline, a highlight knockout inside a word, a caret in the baseline, tilted
labels crossing the type — the block has no isolable container even when there is **NO photographic subject
anywhere**. Text-on-text overlap → `isolable: false` → Q4 yes → **C**, and the whole woven cluster routes
AI-integrated (qa ref-03 Chazon: label-pills overlapping the headline, a green knockout on "brands", a caret
in the baseline — woven, AI-integrated).

**Why this matters most (the real gain over the old Step 0):** today's `overlay-float` is ambiguous — it
lumps text floating on a *reserved clear zone* (B2, e.g. the Visual Brain headline) together with text *cut
into a complex scene with no container* (C, e.g. Nomba "Students. Freelancers."). Q4 + the isolability test
SPLIT them: isolable → **B2 `on-reserved-zone`** (HTML on the guaranteed clean zone); not isolable →
**C `integrated-complex`** (AI places it). That split is why the old step mis-identified.

---

## Two hard identification rules (SPEC-A — the test-09-06 mis-IDs)

**1. A content-bearing surface ⇒ C or B1 — NEVER invent a clean reserved zone (no fabricated B2).**
B2 is reachable ONLY when the ref *actually has* a clean, low-detail band that text floats on. If the ref's
content lives ON surfaces that ARE the message — cards carrying the pillars, a screen/wall holding the
statement — that is **C** (integrated) or **B1** (in-scene surface), never B2. Do NOT "see" a reserved zone
the ref lacks and then generate a background to satisfy the invention (the **ref-03** miss: content cards
forced to B2 by inventing a clean upper band the ref never had). The test: *"point to the genuinely blank,
low-detail band in THIS ref."* If you can't, it is **not B2** — fall to C (or B1 if the content sits on an
in-scene surface). A reserved zone is a fact you READ, never one you assume.

**2. Inventory EVERY ref block — none collapses into thin chrome or is dropped.**
Every text/content block visible in the ref must end up as either an HTML slot or an AI-zone element — listed
in §2 of `rationale.md` with its treatment. A block that is neither inventoried as a slot nor described in the
AI zone can be *neither* AI nor HTML: it silently vanishes (the **ref-01** caption-pill, **ref-02** surface,
**ref-03** content cards — all dropped). Walk the ref block by block; if a block carries meaning (a caption
pill, a label, a byline, a content card), it gets a row. "Thin chrome" is reserved for genuine brand chrome
(masthead, pagination, wordmark) that `tokens.json` governs — never a content block you'd rather not handle.

**3. Read the ref's TONE accurately — the bg/texture prompt inherits it.**
`bg_treatment` carries the ref's actual tonality, and the bg or texture-extract prompt must describe THAT, not
an invented one. A near-white / sand / cream ref is **light** — its texture-extract prompt must say light/warm
paper, never "dark near-black #1d1c1c" (the **ref-05** miss: a light/sand ref described as a dark
tree-landscape, so the extracted `bg.png` came out dark and off-ref). The tonal words in the prompt are a
faithful read of the ref, exactly like the per-block treatment — see `craft/ai-prompt-craft.md` "Faithful
prompt-from-rationale".

**4. Framing and text-zone position are BINDING reads of the ref — never inverted (fix REMONTA).**
The built template must honor the ref's framing and the band it reserves; the builder may not re-frame or move
the text to a different band.
- **Containment is binding.** `image_zone.containment` is a fact READ from the ref, and the build must match
  it: a ref read as `contained-rectangle` builds a **contained** image zone (a bounded rectangle, not edge-to-edge);
  a ref read as `full-bleed` builds **full-bleed**. The builder may NOT invert it — blowing a contained portrait
  card up to a full-bleed face is the **ref-07** REMONTA miss. Record the containment in `rationale.md` §2 for the
  image block, and build to it.
- **The reserved-zone band is anchored to the ref.** For B2 (and any reserved-zone form), the band the ref
  reserves — recorded in `ref_vision_summary.text_elements[].position` (top / bottom / left / right) — is WHERE
  the HTML text lands. The `prompt_delta`'s reserved-zone instruction and the HTML text geometry both target THAT
  band. No inverting top↔bottom: putting the text in a bottom band when the ref reserves the **top sky** is the
  **ref-05** REMONTA miss. The reserved band is a fact you READ (rule 1 here), and its **position** is read the
  same way — never re-chosen for layout convenience. See `scenarios/b2-filled-bg.md` and
  `craft/ai-prompt-craft.md` "Reserved-zone prompting".

---

**5. Each distinctive element is read PER-ELEMENT and REF-ANCHORED — presence + position + size + fill + VALUE/opacity (fix the inflated read + the ghosted-element miss).**
A distinctive element (a display word, a seal / badge / logo, a callout pill, a graphic device) is NOT covered
by the coarse `bg_treatment` enum — it gets its OWN row in `distinctive_elements`, and every field is READ from
THE ref, never inferred. (The builder receives exactly one ref — there is no sibling set, so no which-ref to
misattribute; the read errors that remain are presence and size.) The field that goes wrong is **size**: the
body-numbered pill — a `minor` coral callout box, lower-left in the ref — was **inflated** to a full-width
mid-canvas strip (bbox width 80%). The cure is mechanical: before writing the row, point at the element in the
ref, read its `position`, read its coarse `size` band, read its `fill`, **and read its `value` (opacity/tonal
strength)**. The authored bbox MUST match that read — a `minor` lower-left box is authored small and lower-left,
never stretched full-width. This GENERALIZES the existing "don't invent a pill the ref lacks" anti-pattern
(rule 2): there the sin was *adding* an absent element; here it is *inflating or relocating* a present one to
the wrong size, wrong position. Both are read errors — fixed by reading the ref per element.

**VALUE/OPACITY is a fidelity attribute, not an afterthought (fix the run-08 statement-scene ghosted "setup").**
When the ref's distinctive element is **ghosted / low-opacity / tonal** — a faint watermark display word, a
faded background numeral, a low-tint device — its `value` MUST be read and recorded EXPLICITLY (`value:
ghosted | tonal`), exactly like position and size. The statement-scene miss reasoned treatment + position +
size + fill for the oversized "setup" word but **never declared its opacity**, so the builder defaulted it
**solid** and shipped a near-solid word the ref ghosts faintly. The cure is mechanical: a ghosted/tonal element
is read `value: ghosted|tonal` and the authored `opacity` matches it (a ghosted word → `opacity:0.10–0.18`,
not full strength). `solid` is the default ONLY when the ref shows the element at full strength — never assumed
when the read is silent. The convention hook (`opacity` on the zone div) already exists in
`shared/template-conventions.md` #8; this rule makes CAPTURING the value at read-time mandatory so the hook
actually gets used.

**6. Element ROUTING — small mark = overlay, dominant display = HTML, occluded display = AI-at-dominant-scale.**
The `treatment` field in each `distinctive_elements` row is decided by WHICH class the element is, because the
AI cannot hold every class. Route by:
- **Small distinctive brand mark** (badge / seal / logo, `size: minor`) → **`SVG-overlay`. NEVER AI-baked.**
  gpt-image **drops** small marks — the cover-hook prompt asked for *"a small coral starburst seal with
  'Claude'"* and the AI rendered nothing there. The mark is composited as an SVG/HTML overlay on top of the
  generated scene, where it cannot be dropped. **The overlay's SVG is the REAL asset**, resolved via
  `shared/icons.md` (commons-first — Claude → `commons/ai/claude.svg`); when no asset resolves, the mark is
  AI-generated in-scene (a resolved mark, when available, rides as an extra `--input-image`). NEVER hand-drawn
  as HTML/CSS/inline-SVG primitives — the run-06 cover-photo-hook 20-vertex polygon "starburst" is the defect
  this forbids.
- **Dominant display word NOT occluded by the photographic subject** → **`HTML` (prominent).** gpt-image renders
  large display type poorly; a dominant headline that sits cleanly over the scene (not threaded through a figure)
  belongs in prominent HTML, not buried small in the AI image.
- **Display word genuinely OCCLUDED by the photographic subject** → **`AI-baked`**, the only legitimate
  AI-integrated display (HTML can't thread a word behind a figure). But the bg `prompt_delta` MUST state an
  **explicit DOMINANT / large scale** — cover-hook's *"system"* came ghost-small because the prompt said
  *"lower-center integrated"* with no scale, when ref-01 shows it LARGE behind the figures (see
  `craft/ai-prompt-craft.md` "Dominant-display scale"). Record the routing in `rationale.md` §2 as the element's
  `treatment`; the prompt-from-rationale step (`agents/ssc-template-builder.md`) honours it.
- A non-occluded dominant display sent to the AI, OR a small mark baked into the AI, OR an AI-integrated display
  prompted with no explicit scale, are the cover-hook D2 misses — see the anti-patterns in
  `agents/ssc-template-builder.md` and `craft/ai-prompt-craft.md`.

**7. The hero subject is FIXED IDENTITY or FREE per-post — read which, the slug is the first hint (fix the chain miss).**
The image zone's subject is one of two kinds, and the read decides whether the per-post prompt **recolors a
fixed object** or **swaps a free one**:
- **`subject_role: fixed-hero`** — the hero subject **IS the template's identity**: the slug NAMES it
  (`chain-*`, `gear-*`, `lock-*`) AND the ref shows ONE dominant subject that is the whole point of the layout.
  Then the subject is **fixed** — every post keeps THAT object and varies only framing / angle / lighting /
  scene; the per-post prompt **recolors the ref** (e.g. the ref's green link → brand coral), it does **NOT**
  regenerate the object from a free `{PHOTO_SUBJECT}`. The `chain-highlight-headline` miss is exactly this read
  inverted: the chain (named in the slug, one dominant ref subject) was read as a free per-post axis, so the
  prompt said *"Change the subject to: {PHOTO_SUBJECT}"* with example values "neural node / AI chip / robotic
  hand" → the chain became gears. A `fixed-hero` reads its `distinctive_graphics` as the identity to preserve.
- **`subject_role: free-subject`** — the hero is a **slot that genuinely varies per post** (a photo of whatever
  the post is about): the slug describes the LAYOUT, not the object (`numbered-photo-rule`, `creator-cover`),
  and the ref's subject is one *example*, not the fixed identity. Then `{PHOTO_SUBJECT}` is a real variation
  axis and "change the subject" is correct.
- **The slug is the FIRST hint, not the proof.** A slug that names a concrete object (`chain`, `gear`) flags
  `fixed-hero`; a slug that names a layout (`numbered`, `cover`, `statement`) flags `free-subject`. Confirm
  against the ref: ONE dominant subject that the composition is *built around* → `fixed-hero`; a subject that
  is plainly a placeholder for per-post content → `free-subject`. Record `subject_role:` on the image block in
  `rationale.md` §2; it routes the edit mode (`craft/ai-prompt-craft.md` "Fixed-hero recolor vs free-subject
  swap") and is checked by the gate (objeto-herói regenerated ≠ ref → r6g). When genuinely ambiguous, prefer
  `fixed-hero` if the slug names the object — recoloring the ref is the safe default (it can't lose the
  identity), and a wrong `fixed-hero` only over-constrains one post, while a wrong `free-subject` deletes the
  brand object on every post.

**8. The ref is FORM, not CONTENT — read structure, substitute the BRAND's content (RC-A, run-08).**
Everything rules 1–7 read off the ref is **structure**: the form, the framing, the band position, the medium,
which block is occluded, whether the hero is fixed or free. The ref's literal **content** — its palette, its
people/objects, its language — is NEVER inherited; it is re-derived from the brand. After identification, the
builder runs the **brand-context substitution** (`agents/ssc-template-builder.md` Step 2.5;
`craft/ai-prompt-craft.md` "Brand-context substitution") BEFORE authoring anything:
- **PALETTE** → brand tokens (`tokens.json`), never the ref's colour (the run-08 `list-on-object` lime
  `#b5e853` kept as palette; a `fill` copied from the ref). Caught by Check E (`check_palette_tokens.py`).
- **SUBJECT** (`free-subject`) → the brand's domain, never the ref's literal people/objects (the run-08
  `fullbleed-photo-cover` jiu-jitsu instructor + children). `fixed-hero` recolors the ref's object (rule 7) but
  still never inherits its palette.
- **LANGUAGE / COPY** → text slots are brand-language placeholders, never the ref's transcribed strings (a
  Portuguese ref → Portuguese slots when the brand is English). This is ref-language-agnostic (a Chinese ref
  too). Surface-bound type on a screen/terminal maps to the brand `mono` token.

## Migration note — this tree is a DIFF of the old Step 0, not a rewrite

For maintainers comparing to `ref_vision_summary` in the pre-190 agent:

- **Reused as-is:** `bg_treatment`, `image_zone`, `embedded_icons`, `chrome`, `text_elements`. They work.
- **Renamed:** `text_composition_type` → `text_placement`. The old 3 values map into the new 4:
  - `physical-placeholder` → `inside-surface` (B1)
  - `lateral-split` → `outside-image` (A)
  - `overlay-float` → **SPLIT** into `on-reserved-zone` (B2) vs `integrated-complex` (C) via Q4 + isolability.
- **New:** `image_zone.containment` (`contained-rectangle | full-bleed`) — separates Form A from a full-bleed
  scene; and the per-block `isolable` flag.

(B1 was already covered by `bg_treatment: physical-placeholder` + the placeholder text type; it only lacked a
dedicated scenario file to route to. Now it has one.)

---

## After identification

1. Write the form + the tree path you took + the per-block AI-vs-HTML decisions into the Template Card
   rationale (the builder's structured output — feeds the by-eye QA review).
2. Read `scenarios/<form>.md`. It tells you which **edit mode** to invoke (`craft/ai-prompt-craft.md`), which
   **HTML craft** to read (`craft/html-craft.md`) if text is HTML-placed, and its extra QA criterion.
3. Run the build; the quality gate (`shared/quality-gate.md`) checks the render.
