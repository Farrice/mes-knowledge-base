---
name: "Bilawal Sidhu: 3D-Grounded Camera & Spatial Control"
description: "The pre-generation spatial layer — greybox→reskin, camera as a drawn artifact instead of a typed hope, freeze-the-set continuity, and retrieve-don't-recall grounding, from an ex-Google spatial computing PM"
version: "1.0"
format: "completion-engine"
workflows: 2
---

# Bilawal Sidhu: 3D-Grounded Camera & Spatial Control

> Six years a senior product manager at Google on spatial computing and 3D maps — Immersive View, the
> ARCore Geospatial API, YouTube VR. Now a creator and analyst (2.1M-subscriber channel; *Map the World*,
> 36k+ subscribers) covering AI, AR/VR and spatial computing, with early access to world-model releases and
> on-record interviews with the teams building them. TED speaker and host of *The TED AI Show*.
>
> **What he adds that nobody else in the house does:** every other creative master here works in the 2D
> plane — prompt, image, shot, cut. Sidhu is the only one who treats **the scene as an object that exists
> before the render**, and the camera as something you *place* rather than describe. He is the answer to
> "the camera move isn't what I asked for" and "shot 4 doesn't look like it's in the same room as shot 3."

## The one-line thesis

> *"We are largely flying blind. We don't have the equivalent of a viewport — this 3D representation that
> allows us to see exactly what we had in mind before we actually hit that render button."*
> — 2026-02-18

## The core claim

**Every property of a shot is either asserted through an artifact you can point at, or left to the model's
imagination.** The craft is deciding which is which — and then holding only what 3D is cheap at while
buying everything 3D is expensive at.

Geometry, scale, camera path, timing and occlusion are expensive to prompt and cheap to arrange in space.
Volumetrics, light interaction, material richness and atmosphere are the reverse. Get that split backwards —
prompt your camera move while carefully modelling your fog — and you pay twice for nothing. Get it right and
a look change costs one cheap generation, a blocking change costs one cheap render, and neither disturbs
the other.

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---|---|---|
| 01 | [Greybox → Reskin Shot](workflows/01-greybox-reskin-shot.md) | Shot spec: HELD/BOUGHT split, control artifact, blocking sheet, reskin brief, ground-truth check | A camera move is load-bearing · a look needs deciding before production money · something must match · text-to-video keeps returning a different move |
| 02 | [Scene-First Blocking Plan](workflows/02-scene-first-blocking.md) | Spatial plan: persistence register, shot routing, grounding plan with named gaps, spatial-memory ledger | More than one shot in the same place · a real place must be right · long-form keeps decaying into unrelated clips |

## Quick Reference

- **Genius Context**: [genius.md](genius.md) — load before any workflow. 27 patterns in six groups,
  8 signature moves, the quality rubric, anti-patterns, voice profile, and a dated source key.
- **Era-bound mechanics**: [references/era-bound-mechanics.md](references/era-bound-mechanics.md) —
  every named tool, dated 2026-08-02, **verify before use**. Nothing in the method depends on it.
- **Source notes & fidelity ledger**: [references/source-notes.md](references/source-notes.md) — every
  source dated, every unverified receipt flagged, the honest depth assessment per section.

## Doctrine: model-independence

**The core method names no tool.** It survives every generator swap because none of it is about a
generator — it is about what artifact carries which property of the shot. Runway, Sora, Genie, Veo,
Seedance, World Labs, Postshot, XGrids and the rest live only in the era-bound appendix, dated. No
workflow and no execution prompt depends on a line of it.

**If swapping the model invalidates the spec, the spec was written wrong.**

## The nine ideas that carry

1. **Flying blind is the defect** — if nothing existed that you could have looked at before generating,
   the bad output wasn't bad luck.
2. **Split blocking from look** — the greybox holds geometry, motion, camera and timing; the reskin buys
   material, light and atmosphere. Two axes, two clocks.
3. **The camera is a drawn artifact** — a line on a screenshot, an arrowhead, numbered waypoints, real
   camera frustums. Annotation beats description whenever the instruction is spatial.
4. **The reproducibility gate** — how many times does this location appear? Once, generate it. More than
   once, freeze it first. Persistence is a cost you pay once or per take.
5. **Create once, image from anywhere** — continuity comes from not re-deciding, never from describing
   consistently.
6. **Retrieve, don't recall** — supply actual reference views along the path instead of trusting model
   memory of a place. Every direction you have no reference for is where invention happens.
7. **Ground truth as a measuring instrument** — render the intended move in something deterministic; grade
   the generation against it instead of eyeballing it.
8. **Explicit vs implicit, per shot** — does this need to be edited, matched, or repeated? That is the
   whole routing question. Neither side wins as a belief.
9. **Route by department, not leaderboard** — name which traditional craft role's job the shot is. The
   departments outlive the models.

## Signature moves (short list)

Scribble the trajectory · Greybox first, reskin second · Freeze the set before the takes · Ground-truth
render · Retrieve the place · Name the department · Paint the scene · Ask the model to draw its own arrows.

## Routing

- **A camera move that has to be exact, or a look to decide cheaply** → workflow 01
- **More than one shot in one place, or a real location that must be right** → workflow 02
- **Just the drawn camera artifact for one shot** → `references/prompts-v2/camera-path-brief.md`
- **Story, performance, edit rhythm, "why does this look flat"** → NOT this skill. `skills/dave-clark/`.
  Sidhu is upstream of that and orthogonal to it — Clark decides what the shot means, Sidhu decides where
  the camera is. They compose cleanly.
- **Prompt syntax, style codes, image art direction** → `skills/nick-st-pierre/`, `skills/rory-flynn/`.
- **Colour, grade, delivery specs, chain of title** → `skills/dave-clark/workflows/02-hybrid-pipeline-plan.md`.
- **Operating any specific 3D application** → NOT this skill and not any skill here. He names software; he
  never teaches it.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

3 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Bilawal Sidhu — Camera Path Annotation Brief** — `skills/bilawal-sidhu/references/prompts-v2/camera-path-brief.md`
- **Bilawal Sidhu — Greybox → Reskin Shot Spec** — `skills/bilawal-sidhu/references/prompts-v2/greybox-reskin-shot.md`
- **Bilawal Sidhu — Scene-First Spatial Plan** — `skills/bilawal-sidhu/references/prompts-v2/scene-first-blocking-plan.md`

<!-- END:execution-prompts -->
## Fidelity note

**Two workflows and three prompts, not five and twelve.** The corpus is lopsided, and the ledger says so.

The **spatial-control doctrine is course-deep** — argued from multiple angles across four 2026 video
essays (~1h 20m) with hands-on demonstration, quote-backed throughout `genius.md`.

The **greybox→reskin procedure is post-deep** — it exists in exactly one public artifact, a January 2025
post of three numbered steps plus three observations. There is no published step-by-step, no worked
example, no teaching of what makes a greybox good. Everything in workflow 01 beyond those six things is
tagged inline as **[SD]** Sidhu-derived or **[CG]** craft-general, and it is never presented as "his
framework," because he never published one.

Also excluded on purpose: **SpAItial** (named in the extraction brief; appears in no source examined —
World Labs does, repeatedly), "TED curator" (sources support speaker and podcast host), and every
self-reported view count and brand collaboration. He is not a film director and this skill never poses
him as one. Full ledger: [references/source-notes.md](references/source-notes.md).
