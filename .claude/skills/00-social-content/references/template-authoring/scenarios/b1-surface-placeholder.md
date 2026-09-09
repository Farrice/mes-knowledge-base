# Scenario B1 — surface in-scene (physical placeholder)

> Reached from `identification-tree.md` Q2 (`bg_treatment == physical-placeholder` — a blank screen / frame /
> paper / billboard inside the scene holds the content). `text_placement: inside-surface`. The text lives
> INSIDE the scene's surface, and the **AI places it** — it respects the surface's perspective and lighting
> the way a flat HTML layer cannot.

## Which object IS the surface? — the BOUNDED OBJECT the text sits ON, never the backdrop
The surface is the frame / screen / board / paper whose EDGES contain the text — point at it in the ref. The
wall / room / scene BEHIND that object is the backdrop, never the surface. On the §2 surface row in
`rationale.md`, record the surface's **`fill`** (light|dark + its colour) READ from the ref, plus the text's
polarity on it — and the `prompt_delta` names the surface BY its fill: *"KEEP the ref's WHITE framed board on
the dark wall; render {CONTENT} in dark text ON the board"*. A surface row with NO fill recorded is the run-06
ref-02 white-board miss: the dark backdrop got promoted to "the surface", the polarity inverted (light text on
dark instead of dark text on the white board), and the build came out as the negative of the ref.

## Multi-surface scenes (primary + satellites)
A B1 scene is not limited to ONE surface. It can hold a **primary surface plus satellites** — e.g. a CRT
screen as the hero surface surrounded by a ring of sticky-note surfaces, or a billboard flanked by smaller
signs. All of these are in-scene surfaces: **text on every one of them is AI-placed-in-surface** (the AI
renders it onto each, matching that surface's own perspective and lighting). The form stays B1 — satellites do
not change identification, they just add more on-surface content.

- In the `prompt_delta`, name each surface and the content it carries (primary first, then the satellites), so
  the AI knows which text goes where and keeps each within its own bounds.
- The "no HTML card / pill behind the text" rule applies to every surface — primary and satellite alike. Only
  an isolable element that sits *outside* all the surfaces may still be HTML.

## Edit mode — clean + reserve + REUSE the existing surface (NEVER total-recompose)
- `ai-prompt-craft.md` → **`edit-from-ref` that PRESERVES the ref's surface** (clean the baked overlays off it,
  reserve it, render the new content onto the SAME surface). The surface in the ref is the asset — **reuse it**,
  do not regenerate a lookalike. **`total-recompose` is FORBIDDEN for B1**: it repaints a new wall/screen and
  loses the ref's surface (the **ref-02** miss — a B1 declared total-recompose repainted a lookalike gallery
  wall instead of reusing the ref's). The delta says *"keep the existing <surface> and its perspective/lighting;
  render {CONTENT} onto it; change nothing else"* — a preservation delta, not an inspire-not-lock one.
- **Extraction must schedule the clean/reserve step.** A B1 ref carries baked text on the surface
  (`has_baked_overlays: true`); the pipeline MUST set `needs_clean_ref: true` so the surface is cleaned and
  reserved before the new content is rendered. `has_baked_overlays: true` + `needs_clean_ref: false` = no
  clean step scheduled = the ref-02 extraction miss.
- **No HTML card / pill behind the text.** The surface already exists in the AI scene (see `html-craft.md`
  §4). Any isolable caption that sits *outside* the surface may still be HTML.
- **Text the ref renders ON the surface is AI-on-surface — never blank-surface + flat HTML.** When the ref
  shows the content already rendered on the surface (with the surface's perspective / occlusion — a services
  list on the billboard slats partly occluded by a worker, a headline on a screen, labels on post-its), the
  build renders the new content the same way: AI onto the surface. Keeping the surface blank and floating flat
  HTML over it is the signboard miss — the text loses the perspective/occlusion that makes it read as printed
  ON the board. **A multi-item list is NO exception**: the list items ride the slats at the slats' own scale,
  recolored and occluded by the scene, exactly as the ref shows.

- **The AI bakes the SUPPLIED text — feed the content in, do not let the model invent.** The failure mode of a
  list on a surface is not "the AI renders text" — the image models render supplied text faithfully and legibly
  (route object-bound text to AI baking with confidence). The failure is the model **inventing its own items**
  when the prompt does not state them. The fix is to **feed the exact content into the bake prompt** — name each
  list item / line as the literal string to render onto its slat — and to carry a **negative prompt against
  invented or extra text** ("render ONLY these lines, NO other words, NO invented items, NO extra captions").
  Keep the **letter-fidelity check** (the rendered text matches the supplied strings, character for character).
  Do NOT switch the list to HTML slots to dodge the hallucination — that throws away the perspective/occlusion
  that makes it belong to the board.

- **`rationale.md` MUST agree.** A list template's §2 declares CONTENT as **AI-on-surface (surface-reuse)** with
  the supplied items named in the `prompt_delta` — NOT `decision: slot`. The gate's Check 3 (surface-reuse) DOES
  apply: an AI image zone must exist (pure-HTML slots with no AI zone = the surface was not reused → fail). The
  `prompt_delta` DESCRIBES the supplied text and forbids ONLY invented/extra text — a blanket no-text clause over
  a surface that must carry the list is the Check 4 contradiction (the model is told not to render the very text
  it must place).

## Generation moment
- **Every post** (surface-preserving edit; delta = the content that goes on the surface). Save the validated
  prompt at setup with the example content.

## Build
1. **On-surface content (single string OR a multi-item list)** — `[ai-image-zone:1]` block:
   `generation_route: edit-from-ref`, `prompt_delta` = "KEEP the ref's <surface> (its perspective, lighting, and
   bounds) — clean any baked text off it and render {CONTENT} onto the SAME surface; change nothing else in the
   scene." (Preservation delta — not "compose a new scene".) For a list, {CONTENT} is the **supplied items named
   verbatim** ("render these lines on the slats, top to bottom: <item 1> / <item 2> / …"), plus a **negative
   against invented/extra text** ("NO other words, NO invented items, NO extra captions"). §2 declares CONTENT
   AI-on-surface (surface-reuse).
2. If the slide needs an isolable element outside the surface (a kicker, a logo), add it as an HTML overlay
   with `data-slot`; otherwise the slide is AI-only.

## Try-3 fallback (from the quality gate)
If the AI repeatedly mis-renders the on-surface text (illegible / wrong content), the gate's ladder falls to
the **coordinated hybrid**: keep the surface blank in the scene and register an HTML text zone to the
surface's bounds (`background:transparent; box-shadow:none`), then to plain HTML if the hybrid also fails.
This is the deterministic fallback — no re-identification.

## Fidelity to the ref (REMONTA / INVENTA)
- **Containment is binding** (`identification-tree.md` rule 4): build the image zone to the ref's
  `image_zone.containment` — never invert contained↔full-bleed. Record `containment:` on the image block in
  `rationale.md` §2.
- **Legibility** for any text NOT on the surface (an isolable caption outside it) copies the ref's method —
  `legibility-method: ref-band | natural-composition`; a scrim/band is authored only when the ref shows one (the
  run-02 INVENTA miss). On-surface text gets no scrim by rule (the surface is the container).

## Extra QA criterion (beyond the common gate)
- **Surface bounds:** the text stayed within the in-scene surface (did not spill past the frame/screen edges)
  and reads as printed on the surface, not floating in front of it.
- **Treatment contract (Check B, `shared/quality-gate.md`):** when `rationale.md` says "reuse the in-scene
  surface", the output must be AI-placed-on-surface (an `[ai-image-zone]` exists) — pure HTML text with no AI
  zone means the surface was NOT reused (the body-statement miss) and fails Check B → re-roll. **This covers a
  multi-item list too**: the list is AI-on-surface, so an AI image zone must exist; additionally the list must
  satisfy (1) the `prompt_delta` NAMES the supplied items so the bake renders the user's content, not invented
  items, and (2) the `prompt_delta` carries a negative against invented/extra text (NOT a blanket no-text clause
  — Check 4 fails a blanket no-text clause over text the rationale routed to the AI).

> Before generation, the builder must pass **Check A** (`rationale.md` present + complete) — see
> `shared/quality-gate.md`. The B1 rationale's ④ ambiguity section should examine whether each surface (primary
> + satellites) is genuinely in-scene vs an isolable element that could be HTML.
