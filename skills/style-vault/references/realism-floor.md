# The Realism Floor

**Status:** the floor for every image generation in this house, not just the vault.
**Set by:** Farrice's 8/10 verdict on the COA plate, 2026-08-10 — *"we nailed the realism… make sure
this is embedded so the floor is here no matter what work we're doing."*

**Mechanical, not remembered:**

```bash
python3 execution/style_vault.py lint "<prompt>" --strict
```

Verified both directions 2026-08-10: the winning COA prompt scores **8/8**; the door prompt that
Farrice rejected scores **0/8 + 4 banned terms**.

---

## The eight layers

Each is a physical **cause**. Every layer you don't name is one the model fills with its own
averaged default — and averaged defaults are what "AI slop" means.

| Layer | What it means | Failure it prevents |
|---|---|---|
| **capture** | Camera, lens, aperture, stock/format, support | Digitally immaculate, therefore never photographed (Clark #5) |
| **light** | One nameable source with a direction | Soft global illumination from nowhere (Clark #3) |
| **black_point** | Shadows landing on real black | Mid-grey end to end; reads as render |
| **atmosphere** | Something physically in the mid-ground | Clean air collapses planes into a poster (Clark #4) |
| **imperfection** | Marks of the object's own history | Perfection is the tell |
| **provenance** | A specific thing, not a described abstraction | *"That piece of paper looks so fake it looks lazy"* |
| **material_response** | Materials behaving as that material behaves | Most "looks AI" is a **physics** failure, not an aesthetic one |
| **micro_surface** | The high-frequency detail models average away | Plastic, waxy, smoothed |

Plus the ban: no `8k`, `cinematic`, `hyperrealistic`, `masterpiece`, `stunning`, `beautiful`,
`award-winning`, `octane`, `vray`. Undecomposable — you cannot sweep, explain, or bank them.

**And the rule that isn't a layer: generate ≥4 and select.** Clark's most common cause of flat is
"one generation deep," and it is a *selection* problem. One image per concept is a first take.

---

## What takes it from 8 to 10 (researched 2026-08-10)

The four layers above get you a photograph. These four get you a *published* one.

### 1. Subsurface scattering — name it, because the model won't

2026 benchmarks put proper subsurface-scattering simulation at roughly **23%** of generators. It
is the single largest cause of the "wax figure" read: real materials let light penetrate and
re-emerge with a warm internal glow. Without it, everything looks like painted plastic.

**Materials that need it named:** skin, ice cream and dairy, wax, marble, jade, thin paper held
against light, leaves, fruit flesh, milk, alabaster, fingernails, ears.

> On the COA plate this was the unnamed win — the melt read as dairy partly by luck. Name it and
> it stops being luck: *"light penetrating the melt and re-emerging warm at the thin edge."*

### 2. Specular behaviour and catchlights

Generators produce reflections that are slightly too perfect, or place them contradicting the
scene's own lighting. **One misplaced or absent catchlight breaks believability on its own.**

**Name:** where the specular sits, that it agrees with the named source, and its *shape* — a
scrim gives a soft rectangle, a bare bulb a hard point, a window a mullioned grid. Wet surfaces
carry sharp speculars; brushed steel carries anisotropic streaks along the grain direction.

### 3. Luminance-dependent sensor noise — not "fine grain"

Real noise is **not uniform**. It lives in the shadows and thins toward the highlights. "Fine
grain" asks for an even blanket, which is itself a tell.

> Write: *"luminance-dependent grain — coarse in the shadow side of the bench, near-absent in the
> lit paper."*

Related: real capture carries lens character (falloff, slight field curvature, longitudinal CA at
wide apertures) and coherent optics. Immaculate optics read as CGI.

### 4. Split the passes — stop asking one generation to do three jobs

**This is the ceiling we hit at 8/10**, and it's confirmed industry practice for 2026: *for
content requiring precise text, the reliable workflow is generating the image without text and
adding text in post.* The garbled body copy on the COA is not a prompt failure — no current model
holds a full page of small text.

A real editorial shot is three departments. Ours should be three passes:

| Pass | Job | Where |
|---|---|---|
| **Plate** | The photograph: light, materials, physics, capture | Generation, ≥4 variants, select |
| **Art department** | Real typography, real document, real label | Composited in — the actual typeset COA over the plate |
| **Grade** | Black point, warmth, series consistency | A post layer, **once, set-level** — never per-frame |

Clark's own framing: look is a post layer, not a generation layer. Asking the model to grade
*and* shoot *and* set type is why prompts get long and results plateau.

### 5. Coverage (Clark #6) — the one nobody does for stills

Every shot being a new setup means nothing reads as a *scene*. For a carousel, shoot the same
set from three distances — wide establishing, the working crop, one macro detail — so the deck
reads as a place you're standing in rather than three unrelated postcards.

---

## The ninth layer — CONTEXTUAL CORRECTNESS (Farrice, 2026-08-10; the 9→10 layer)

> *"The table can't be random. I would zoom in and look… a misread would kill all credibility
> of the actual image."*

The eight layers above make the frame read as photographed. This one makes it survive a zoom.
**Any document, label, chart or instrument in frame renders its REAL contents** — sourced from
the deliverable it accompanies, never invented:

1. **Source of truth is the artifact's own copy.** For a teardown carousel, the document's rows
   are the teardown's published numbers (Transparent Labs: 8.0 g L-citrulline malate, 4.0 g
   beta-alanine, 2.5 g betaine — the same numbers slide 4 states). The zoom must AGREE with the
   copy beside it.
2. **Write the exact rows into the prompt** — column headers and cell values, verbatim. Current
   models hold table-density text when given the literal strings; they garble only what they're
   left to invent.
3. **Standard specs are allowed to be standard.** Microbial limits, NMT/NLT thresholds — use the
   real USP-style values. Generic-but-correct beats invented-but-specific.
4. **Verify on the output, not the prompt.** Zoom the selected variant and read every legible
   row before shipping. A wrong number in a legible cell is a factual-veto matter — the image is
   asserting a fact.

This layer is a judgment gate, not a regex — `lint` cannot check it. It lives here, in the
workflow quality gates, and on every card whose style contains a document.

### 9a — DOCUMENT AUTHENTICITY RESEARCH (Farrice, 2026-08-10 — the step that makes 9 executable)

Correct *numbers* in a wrong *form* still reads as generated. The first fact-correct COA carried
the teardown's real doses but structured heavy metals as one generic row ("Heavy Metals NMT 10
ppm") plus a lone Lead row — and a founder who orders COAs monthly clocks that instantly. The
domain knowledge in my head is not the specimen.

**Before writing any document spec into a prompt:**

1. **Fetch a real specimen of the document type.** Priority order: the subject brand's own
   published document (Transparent Labs publishes its COAs) → the category's standard form
   (USP-style lab reports) → a competitor's published equivalent. Web-check; never write a
   document's structure from model memory.
2. **Mirror four things from the specimen, not just values:** the row inventory (heavy metals =
   per-element: Arsenic, Cadmium, Lead, Mercury), the **column set** (real COAs carry a METHOD
   column — HPLC, ICP-MS, USP <2021>/<2022>), the **units** (µg/serving, cfu/g), and the
   **result formats** — real labs write "Below LOQ" and "Absent", not "<10 ppm" on every row.
3. **Log the specimen source** (URL or file) in the sweep log — a document spec without a named
   specimen is unresearched, and gate 9 fails it.
4. Substantive values still come from the deliverable's own copy (layer 9); the specimen
   supplies the FORM those values sit in.

## The order to fix in

Grade path → **physics** → **capture** → look. Drift in the first three is a control failure: fix
the artifact, never the adjective. A miss in look is a brief failure.

**And the closer, always:** would this have looked the same without me?

## Sources

- [Why AI Images Still Look Fake — Vofy](https://www.vofy.art/blog/why-ai-images-look-fake-photorealistic-solutions)
- [How to Make AI Images Look Like Real Photos (2026) — Imagera](https://imagera.ai/blog/how-to-make-ai-images-look-real-2026)
- [Why AI Generated Images Look Fake: The Technical Truth — Rewarx](https://www.rewarx.com/blogs/why-ai-generated-images-look-fake)
- [The Ultimate Guide to AI-Generated Product Photography (2026) — Rainfrog](https://www.rainfrog.ai/blog/the-ultimate-guide-to-ai-generated-product-photography-for-e-commerce-2026)
- [The State of AI Image Generation in 2026 — Lovino](https://lovino.ai/blog/state-of-ai-image-generation-2026)
- House: `skills/dave-clark/genius.md` (eight causes of flat) · `skills/nick-st-pierre/SKILL.md`
  (anti-slop rules) · `skills/grace-liu/SKILL.md` (direction discipline)
