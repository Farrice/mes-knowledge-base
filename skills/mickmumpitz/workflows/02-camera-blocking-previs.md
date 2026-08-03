# Workflow 02 — Camera Blocking & Previs

**Produces:** a blocking plan — layout inventory, per-shot camera report, pose keys, lighting-for-mood
pass, export manifest and a per-shot Control Ladder rung — that determines the spatial content of every
shot *before* anything is generated.

**Load first:** `genius.md` (patterns 10–14, plus the Control Ladder).

**Deploy when:** more than two shots need to read as the same place · characters must interact in one
frame with correct proportions · a camera move must repeat or be recreated · a sequence keeps coming out
as unrelated postcards · someone said "just prompt the camera angle" and it didn't hold.

---

## The premise

> *"The next part of the process mirrors traditional 3D animation. We focus on the most important poses
> in each shot and animate them without interpolation, in a process called blocking."*
> — 2025-03-07, 09:08

Camera position, character proportion, eyeline, spatial continuity and blocking are **not prompt
parameters.** They are geometry. You author them once, in a space, and every shot inherits them for free.
The generator then becomes what he treats it as: **a renderer on top of a deterministic layout.**

The corollary, and the reason this is affordable: **the layout is a render target, not a picture.** It
is judged on correctness, never on beauty. *"The room is absolutely not looking perfect, but if you just
want to have a basic scene where you can pose your characters in, it is honestly enough."*

---

## Step 1 — Pick the rung, per shot

Do not put the whole sequence on rung 5. Cost is real and he routinely spends less.

| Rung | Author | Use when |
|---|---|---|
| 0–1 | Prompt / reference only | Establishing shot, no continuity load, nothing has to match |
| 2 | Mask | One element changes, everything else is already right |
| 3 | Structural guidance (edges / depth / pose) from existing footage or a rough source | The composition already exists somewhere and only the look changes |
| 4 | Camera tracking | The camera move must be preserved or recreated exactly |
| 5 | Full 3D layout | Multiple characters interact · proportions must hold · a designed camera move · the same space recurs across shots |

Output a one-line rung call **per shot with its reason.** A sequence with every shot on rung 5 is
usually an unexamined sequence.

---

## Step 2 — Layout inventory

What has to exist in the space, and at what fidelity. Fidelity is assigned deliberately and most of it
is low.

| Element | Fidelity needed | Why |
|---|---|---|
| Characters | Proportion-correct, roughly posable. Broken geometry is acceptable | They exist to occupy space and hold eyelines, not to be rendered |
| Set/environment | Correct scale, correct sightlines, correct spatial relationships | *"Absolutely not looking perfect… honestly enough"* |
| Props that block or are handled | Present, correct size and position | Anything a character touches or that occludes the camera |
| Everything else | Omit | It isn't in the render |

State per element where it comes from (generated, modelled, kit-bashed, photographed, greyboxed) and
**explicitly mark which elements are allowed to be ugly.** Naming the "good enough" tier is part of the
deliverable — it is what keeps this workflow cheap enough to actually run.

---

## Step 3 — The camera report, per shot

Each shot gets a camera report, in the vocabulary you'd hand a DP, plus the two things that only exist
because this is a layout:

- **Size** — wide / medium / close / extreme close
- **Camera position and height** — where in the space, at what height, relative to what
- **Lens character** — wide/normal/long, and what that does to the space (not a focal-length number
  unless one is genuinely known)
- **Movement** — static / push / pull / track / handheld, over how many frames
- **Screen direction and eyelines** — who looks where, which way the geometry faces
- **Subject action** — what happens, in one clause
- **Duration intent** — how long this is meant to be on screen
- **Coverage relationship** — which other shot(s) this must cut with, and what has to match for the cut
  to read as one place

---

## Step 4 — Pose keys (blocking proper)

For each shot, key **only the important poses. No in-betweens.**

- Number the keys and say what each one *is* — the beat, not the position.
- Mark which key is the **start frame** and which is the **end frame** of any generated motion.
- **The unit of production is the pose pair, not the clip.** You author both ends deterministically and
  let the model own only the transit between them (*"we pretty much worked from one pose to the next,
  interpolating the movement in between"*).
- Mark any pose that is an **interaction** — contact, handoff, eyeline exchange. These are the poses
  that fail if the layout is wrong, and the ones that justify rung 5 in the first place.
- Rigs are allowed to be imperfect. *"There are still some broken parts in there — you could manually
  fix them, but honestly this is good enough."*

---

## Step 5 — Light the layout for mood

A separate, deliberate pass, done **in the layout, before generation** — not left to the prompt.

> *"After creating all the necessary poses and camera angles, we can focus on lighting the scene. We
> spend some time perfecting the mood for our film, creating a late evening atmosphere just after
> sunset."* — 2025-03-07, 09:20

Specify, per scene: **key source and direction · time of day / condition · contrast intent · what
motivates each source in the fiction.** This is the one place where the layout stops being purely
functional, and it is worth the time because it is the only mood decision the generator will inherit
for free across every shot in the space.

> **Boundary.** This skill can tell you to light the layout and hold it across shots. It does not carry
> a lighting vocabulary. For the *content* of the look — light behaviour, black point, palette,
> atmosphere, capture register — load `skills/dave-clark/` and write the look card there.

---

## Step 6 — Export manifest

What actually leaves the layout and becomes an input. Per shot, list which of these are exported:

| Export | Locks | Note |
|---|---|---|
| Rendered layout frame(s) | Composition, pose, framing | The base plate for structural guidance |
| Depth pass | Spatial relationships, near/far | *"More flexible, giving the model more freedom to generate new detail"* |
| Edge/outline pass | Exact detail and geometry | Use when detail must survive intact |
| Element/ID masks | Which region is which | Cheaper and more reliable than segmenting after the fact |
| Camera tracking data | The camera move | Needed whenever a generated element must sit in a moving plate |
| Pose data | Human articulation | Only when a person's movement drives the shot |
| Start / end frames | The pose pair | The transit unit from Step 4 |

Two rules from source:

1. **Export the minimum that locks what must be locked.** *"Like 95% of the time I only use the tile
   ControlNet — that's usually enough."* More controls do not mean more control (Pattern 21: stacking
   everything produced *"an unanimated image sliding over the video"*).
2. **Structure early, freedom late.** Where the tooling permits, structural guidance should be strongest
   at the start of generation and decay — composition locked in the first steps, detail earned in the
   last. Implementation is era-bound; the instruction is not.

---

## Step 7 — Quality gate

- [ ] Every shot carries a **rung call with a reason** — and they are not all the same rung
- [ ] Every shot is a **camera report**, not a mood description
- [ ] **Coverage relationships are named** — which shots must cut together, and what must match
- [ ] Pose keys are **beats**, in-betweens are absent, and start/end pairs are marked
- [ ] **Interaction poses are marked** — the ones that justify the layout at all
- [ ] Lighting is a **layout decision** with source, direction and motivation, not a prompt adjective
- [ ] The export manifest lists **the minimum** per shot, and nothing is exported "just in case"
- [ ] Elements allowed to be ugly are **explicitly named** — if none are, the plan is too expensive to run
- [ ] Nothing in the plan depends on a named model, node or version

**Execution prompt:** `references/prompts-v2/previs-blocking-plan.md` — honor its Output Contract.
**Then:** `workflows/03-controlled-shot-spec.md` converts each shot into its four building blocks.
