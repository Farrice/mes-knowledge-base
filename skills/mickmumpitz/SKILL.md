---
name: "Mickmumpitz: Deterministic Character & Shot Control"
description: "Determinism over prompting — the character-dataset method, camera blocking before generation, and the four building blocks of a controlled shot. The house's only skill for making the same thing come out of the machine twice on purpose."
version: "1.0"
format: "completion-engine"
workflows: 3
---

# Mickmumpitz: Deterministic Character & Shot Control

> German AI-filmmaking practitioner. ~182,000 subscribers, `mickmumpitz.ai`, Patreon-funded, publishing
> free open-source ComfyUI and Blender character/VFX pipelines and shipping a finished short film with
> each major release (*Paper Jam*, 2025; *The Crystal Cat*, 2025). Actively shipping through July 2026.
>
> **What he adds that nobody else in the house does:** everyone else in the creative lane teaches
> *direction* (Clark, St. Pierre, Flynn, Grace Liu) or *operation* (banana-pro-director, Tao). He is the
> only one who teaches **determinism** — how to make the same character, the same camera move, the same
> composition come out of the machine twice, on purpose, without asking nicely.

## The one-line thesis

> *"The important thing is if you want to control it, you can."*
> — AI VFX Pipeline masterclass, 2026-03-30, 04:01

Not *"you must control everything."* Control is available at every level, priced in setup effort, and you
choose the rung the shot actually needs.

## The core claim

**Consistency is not a prompting skill. It is an authoring skill.**

Everything that must stay the same across shots gets **externalised into an artifact before generation** —
a captioned dataset, a mask, a tracked camera, a blocked pose, a geometry. The generator then has no room
to disagree with you about it. What is left in the prompt is only what you're genuinely willing to let
vary.

The corollary, and the diagnostic that runs through every source:
**when the model gets something wrong, the first move is never a better adjective. It is a better picture.**

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---|---|---|
| 01 | [Character Lock Dataset](workflows/01-character-lock-dataset.md) | Consistency budget, image manifest, signature-detail anchors, caption spec, bake plan, acceptance test | A character must appear more than once — across shots, weeks, styles or media |
| 02 | [Camera Blocking & Previs](workflows/02-camera-blocking-previs.md) | Rung calls, layout inventory, camera reports, pose keys, lighting pass, export manifest | More than two shots must read as the same place, or characters must interact in frame |
| 03 | [Controlled Shot Spec](workflows/03-controlled-shot-spec.md) | Mask · driving plate + structure · references · prompt, plus selection protocol, re-composite plan and failure prediction | Something must be added to, removed from or replaced in existing footage or a layout |

## Quick Reference

- **Genius Context**: [genius.md](genius.md) — load before any workflow. Carries the Control Ladder, the
  Four Building Blocks, 22 patterns, 10 signature moves, the quality rubric and the voice profile.
- **Source notes & fidelity ledger**: [references/source-notes.md](references/source-notes.md) — five
  sources dated, every claim timestamped, every unverified claim flagged.

## Doctrine: model-independence

**Everything in the core method is model-independent**, and the corpus proves it rather than asserting
it. Across five sources spanning sixteen months the *method* never changed — dataset → captions → bake →
controlled generation — while the model roster turned over twice. Four of the five "current best" models
named in 2025 were not the recommendation by 2026. The five dataset rules were identical throughout.

**Tool-specific mechanics are quarantined in
[references/era-bound-mechanics.md](references/era-bound-mechanics.md) — "verify before use", dated
2025-03 → 2026-07.** No workflow and no execution prompt in this skill depends on a single line of that
appendix. If swapping the stack invalidates an output, the output was wrong.

## The Control Ladder

Every shot sits on a rung. The rung is chosen by what the shot needs, not by ambition — he routinely picks
a low rung and says so out loud. Cost and determinism both rise down the list.

| Rung | You author | It locks |
|---|---|---|
| 0 | Text prompt only | Nothing |
| 1 | Reference image(s) | Identity, style, look |
| 2 | Mask | **Where** change is allowed |
| 3 | Structural guidance (edges / depth / pose) | Geometry, silhouette, articulation |
| 4 | Camera tracking | The camera move |
| 5 | 3D layout geometry | Space, proportion, eyelines, blocking |
| 6 | Trained character | The character, across every future shot and every model |

Rungs 0–5 control *a shot*. Rung 6 is orthogonal, stacks with all of them, and controls *a franchise*.

## The Four Building Blocks

> *"All you need is a black and white mask, a driving video — this is your modified plate combined with a
> ControlNet — reference images, and a detailed prompt."* — 2026-03-30, 04:04

**Mask** = WHERE · **Driving plate + structure** = WHAT SURVIVES · **References** = IDENTITY ·
**Prompt** = WHAT HAPPENS. Four independent axes. Every failure is one of them under-specified — never a
model choice.

## The five dataset rules

The deepest craft in the corpus, stated by him as a numbered list (2026-07-17, 01:03–02:28):

1. **The trigger word** — everything not explicitly named in a caption accretes onto it. *"Your trigger
   word becomes your character."*
2. **Vary what you want to generalise** — train only on close-ups and the character only exists in
   close-up. Same for lighting, pose and wardrobe.
3. **Decide what stays consistent and what must change later** — before building the set. Consistency is
   a budget you allocate, not a virtue you maximise.
4. **The caption decides what you can change later** — a detailed caption buys flexibility and charges a
   long prompt forever.
5. **A caption is a reverse prompt** — write captions in the exact grammar you will later write prompts
   in for that model. Mismatch here degrades everything downstream, invisibly.

## Signature moves (short list)

The T-pose + face reference pair · The detail-anchor snip · The group-shot injection · The two-step
preview shop · Block before you generate · The plate-derived composite · Decaying structure · Checkpoint
sampling · Edge-only guidance · Preview-mode datasets.

## The quality rubric

**The honest-folder standard.** *"This is no cherry-picking. These are all the images that came out of the
model."* A character is locked when the whole folder holds, not when one frame does — and the failures get
scrolled alongside the successes.

**Defects are named as objects, never as vibes** — *"her necklace changed a lot"*, *"look at that left
pupil"*, *"the tail is not wiggling enough"*. **80% is a symptom, not a result.** The integration test is
physics — shadows, contact, reflections, spill — not "does it look cool." And **"good enough" is a verdict
issued deliberately**, on the layers whose only job is geometry.

## Routing

- **A character that must appear more than once** → workflow 01
- **A sequence that must read as one place, or characters interacting in frame** → workflow 02
- **Adding to, removing from or replacing something in a plate** → workflow 03
- **"It changed and I don't know what changed" / 80% and something's always weird** →
  `references/prompts-v2/consistency-drift-diagnostic.md`
- **Taste, look, palette, "why is this flat"** → NOT this skill. `skills/dave-clark/` (cinematic
  direction) · `skills/nick-st-pierre/` (image art direction) · `skills/rory-flynn/` (image operations).
  He teaches control, not composition, and no taste vocabulary has been invented for him.
- **Tool operation on the house's own paid stack** → `/banana-pro`, `/art-direct`, `creative_router.py`.
  His stack is local open-source with a high-end GPU; the *method* is stack-agnostic, the *stack* is not a
  house standard.
- **Ad-shaped AI video** → `skills/pj-accetturo-ai-video/`.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

4 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Mickmumpitz — Character Lock Dataset Spec** — `skills/mickmumpitz/references/prompts-v2/character-dataset-spec.md`
- **Mickmumpitz — Consistency Drift Diagnostic** — `skills/mickmumpitz/references/prompts-v2/consistency-drift-diagnostic.md`
- **Mickmumpitz — Previs & Camera Blocking Plan** — `skills/mickmumpitz/references/prompts-v2/previs-blocking-plan.md`
- **Mickmumpitz — Controlled Shot Spec** — `skills/mickmumpitz/references/prompts-v2/shot-control-spec.md`

<!-- END:execution-prompts -->
## Fidelity note

**HIGH.** Five long-form sources (121 minutes, 2025-03-07 → 2026-07-17), all **watched** — full captions
plus 37 frames read at every moment a workflow, dataset, layout or result was shown. The corpus verifies
visually rather than rhetorically: he shows the input, the failure, the diagnosis and the fix on screen.

Two honesty notes. **The Control Ladder is this extraction's synthesis** — he names every rung across the
sources but never arranges them; it is labelled a house frame, not put in his mouth. The Four Building
Blocks, by contrast, are his own words verbatim. And the dossier's claim of a **"Consistent Character
Creator v4" is contradicted by source** — the on-screen file reads `CCC_3-0` and the 2026 successor is
unnamed; no version number is cited anywhere in this skill. Nothing about his real name, background,
credits or client list appears in the sources, so nothing is asserted. Full ledger:
[references/source-notes.md](references/source-notes.md).
