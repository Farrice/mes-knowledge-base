# Scenario C — integrated text

> Reached from `identification-tree.md` Q4 (`text_placement: integrated-complex` — text fails the isolability
> test: it is cut into a complex scene, overlaid or behind an object, with no isolable container). The **AI
> places the text** — it fits it into the scene (overlap, occlusion, perspective) better than HTML.
>
> Canonical example: Nomba "Students. Freelancers." — text integrated into the scene, no container.

## Edit mode
- `ai-prompt-craft.md` → **Total — reskin-in-place** (`edit-from-ref`). The ref LOCKS the composition contract
  (framing + the integration manner — text threaded into the scene); the delta changes the scene/landscape +
  the integrated content. NOT "a new composition" — the composition contract is preserved, the landscape varies.
- Text is AI-rendered into the composition — NOT an HTML overlay. (An isolable kicker or badge that sits
  cleanly on top may still be HTML; the integrated text is not.)

## Generation moment
- **Every post** (full recompose; delta = content). Save the validated prompt at setup with the example
  content.

## Build
1. `[ai-image-zone:1]` block: `generation_route: edit-from-ref`, `prompt_delta` = "keep the reference's EXACT
   composition contract — framing (full-bleed) and the integration manner (text threaded into the scene);
   change the scene/landscape to {CONTENT} and the integrated text as shown; match the reference's
   lighting/tone/color temperature" (mark `# validated-at-setup`). **NEVER "compose a new scene"** — the
   contract is preserved, only the landscape + content vary. At build, reproduce the ref's scene (canonical vs gabarito).
2. Any isolable overlay element → HTML with `data-slot`; otherwise the slide is AI-only.

> **A full-bleed cover MUST have a native HTML headline slot — the hook has somewhere to render (the run-09/10
> `fullbleed-overlay-cover` defect).** A cover whose job is to land a HOOK headline over a full-bleed scene
> needs a **native headline zone authored into `template.html`** — a `data-slot="HEADLINE"` overlay zone. The
> run-09/10 cover shipped with NO headline slot, so the hook had nowhere to render and was lost; the
> orchestrator then patched a `.headline-zone` by hand outside the pool (which broke `_shared/`). Author the
> slot canonically instead:
> - A `.headline-zone` overlay div carrying `data-slot="HEADLINE"`, placed per the **§3.6 composition contract**
>   (`craft/html-craft.md`): declared bbox, ≥ 8% side margins, kicker reserved at top, footer pill as the
>   bottom anchor when the ref shows one.
> - The brand **display font** (the cover hero floor ≥ 9cqw, often 12cqw+ — `html-craft.md` §3), with the
>   `mark`→accent rule riding ONE meaning word (`html-craft.md` §3; never a local `mark { color }` override).
> - A **legibility scrim** so the hook reads over the busy scene: copy the ref's method
>   (`legibility-method: ref-band` → a band; `natural-composition` → the dark zone is GENERATED in the bg
>   `prompt_delta`, NO scrim div — the run-02 INVENTA rule still holds). A real-photo full-bleed gives no
>   luminance control, so a hook over one carries an authored scrim.
> - Because the full-bleed scene is an OPAQUE `edit-from-ref` rectangle, the headline slot MUST sit ABOVE it
>   (higher z-index), never buried under the photo zone — the run-09 `preview-cards-cover` / Check I
>   buried-headline rule. The hook is editable HTML type over the scene, not baked into the image.
> - `rationale.md` §2 declares the HEADLINE block `decision: HTML` (prominent display), so Check 11
>   (undeclared-slot) and Check B agree the slot was reasoned, not ad-hoc.
>
> **Headline-led C with the type in HTML (about-callout class).** When the "integration" is woven *typography*
> (label-pills over the headline, a knockout in a word) and the brand hard-rule keeps all type in HTML, the
> headline + pills are **HTML**, not baked into the AI (baking them is the about-callout miss — they burst the
> frame). Author the headline zone to the **§3.6 composition contract** (`craft/html-craft.md`): bbox target
> ≈ 58–65% of canvas, ≥ 8% side margins, kicker reserved at top, the **footer pill reinstated** as the bottom
> anchor (never SKIP), and typographic **variety** preserved (sentence-case + italic/heavy emphases + a
> medium-weight connector — not one flat "Anton heavy" slab). The per-post fit is §3.5 (auto-shrink); the
> overflow gate is r6g.

## The woven overlap is AI-baked OR a transparent cutout — NEVER an opaque image over HTML type (r8)

The whole point of Form C is that the AI *threads* the text into the scene. There is exactly one
way to keep the text as an **editable HTML layer** while an AI element overlaps it, and one
forbidden recipe:

- **NEVER place an HTML TEXT slot (a `data-slot`, the display/headline above all) UNDERNEATH an
  OPAQUE AI/photo image zone** (text at a lower z-index than an overlapping `data-zone="photo"`
  image). An `edit-from-ref` AI image is an **opaque rectangle** — GPT edit mode strips
  transparency (cross-ref the `gpt-edit-transparent` work). So an opaque image stacked on top
  BURIES the headline: it reads as an image (with seams), not as type, and in the Studio editor the
  user can't select the text to change it — it behaves like an image. This is the run-09
  `preview-cards-cover` miss (a `data-slot="HEADLINE"` at z-index 1 under a `PHOTO_MAIN` card
  cluster at z-index 10). The gate `check_buried_headline.py` (Check I) BLOCKS it.
- **The "AI element overlaps HTML type" (woven) composition is allowed ONLY** when the AI element
  is a **transparent-background cutout** that occludes only its own region — which depends on
  transparency actually being available (the cutout corollary in `craft/ai-prompt-craft.md`;
  declare it on the zone, e.g. `data-cutout`). If transparency is unavailable, the text MUST NOT be
  occluded by the image at all — place the headline **clear of the image's bounding box**, or keep
  the whole woven cluster **AI-baked** (the default Form-C treatment: the AI threads the type into
  the scene, no HTML text underneath the image).
- **If a blend mode is part of the contract, AUTHOR it.** When the rationale promises a
  `mix-blend-mode` (e.g. `multiply`) to blend the image into the page, it MUST actually be written
  into `template.html` — a declared-but-not-honored blend mode is a gap the gate treats as opaque
  (the run-09 rationale promised `multiply`; the template never wrote it).

## Try-3 fallback (from the quality gate)
If integrated text repeatedly renders illegible or garbled, the gate falls to the **coordinated hybrid**
(generate the scene leaving a clean zone, place the text as HTML on it) → then plain HTML. Deterministic, no
re-identification.

## Fidelity to the ref (REMONTA / INVENTA)
- **Containment is binding.** A ref read as `contained-rectangle` (a face/scene in a bounded rectangle) builds a
  contained image zone — never a full-bleed face. Blowing a contained portrait card up to a full-bleed face is
  the ref-07 REMONTA miss (`identification-tree.md` rule 4). Record `containment:` on the image block in
  `rationale.md` §2 and build to it.
- **Legibility copies the ref's method.** Record `legibility-method: ref-band | natural-composition` per block.
  A C composition usually resolves legibility by **natural composition** (the scene is dark/calm where the text
  sits) → the dark zone is GENERATED in the scene, **NO `.bottom-scrim` div is authored**. Stamp a band ONLY when
  the ref shows one (`craft/ai-prompt-craft.md` "Legibility method copies the ref"; the scrim anti-pattern in
  `agents/ssc-template-builder.md`).

## Extra QA criterion (beyond the common gate)
- **Legibility in-scene:** the integrated text is legible against the busy composition (contrast holds where
  it sits) and is not clipped by the canvas edge or an occluding object.
- **Treatment contract (Check B, `shared/quality-gate.md`):** a block `rationale.md` declares AI-integrated /
  occluded must come out integrated-in-the-image (an `[ai-image-zone]` exists), not a flat HTML box — a
  declared-integrated block that shipped as plain HTML fails Check B → re-roll.

> Before generation, the builder must pass **Check A** (`rationale.md` present + complete) — see
> `shared/quality-gate.md`. The C rationale's ④ ambiguity section should examine the B2-vs-C call (reserved
> zone vs no-isolable-container) that Q4 + the isolability test decide.
