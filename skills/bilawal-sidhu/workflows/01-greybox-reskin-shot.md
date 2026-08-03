# Workflow 01 — Greybox → Reskin Shot

**Produces:** a **Greybox Shot Spec** — a blocking sheet (what the untextured render must carry), a reskin
brief (the only things the prompt is allowed to decide), a ground-truth check, and an explicit split of what
is controlled versus what is deliberately bought from the model.

**Use when:** a shot has a camera move that matters · a look needs deciding before production money is
committed · text-to-video keeps returning a different move than the one you asked for · the shot has to
match something else · a piece is longer than one clip.

**Load first:** `genius.md` — Groups A and B are the spine. Group C if the shot will be controlled by
annotation rather than a 3D render.

> **Provenance, stated plainly.** Sidhu published this method as **three steps and three observations**
> (2025-01-06): kitbash a scene → render a greybox animation → reskin with a video model; plus notes that
> volumetric fog and light effects come out well, that materials, environment skybox and key light direction
> are promptable, and that it is fast look-dev even if you finish traditionally. **He never published a
> step-by-step.** Everything below beyond those six things is tagged: **[SD]** = Sidhu-derived from his
> stated practice elsewhere in the corpus, **[CG]** = craft-general previz/look-dev practice, not his.
> Never present this as "Bilawal Sidhu's greybox framework." See `references/source-notes.md`.
>
> **Model-independent by design.** No step names a tool. Named products live only in
> `references/era-bound-mechanics.md` and nothing here depends on them.

---

## Step 0 — Gate: does this shot want the method at all?

The method has real setup cost. Run it when at least one is true, and say which:

- **The camera move is load-bearing.** The shot fails if the move is approximately right.
- **Reproducibility is required.** This location, object or move appears more than once. *"If I need a
  perfectly reproducible set that I can shoot multiple takes on… [I] generate it once, and then I can shoot
  all the takes I want."* — Pattern 4.
- **The look is undecided and expensive to decide.** You are buying a decision, not a shot (Pattern 7).
- **Something must match** — a plate, a product, an existing render, another shot.

None of these true → say so and route to a direct generation lane. A one-off atmospheric shot with a
forgiving camera does not need a greybox and you should not build one.

---

## Step 1 — Split the shot into HELD and BOUGHT

The whole method is this split. Get it wrong and you pay twice for nothing (Pattern 9).

| | Default column | Why |
|---|---|---|
| **HELD** — carried by the greybox | geometry · spatial relationships · scale · camera path, speed and framing · timing and beat · occlusion order · continuity elements | expensive or impossible to get right by prompting; cheap to arrange in 3D |
| **BOUGHT** — left to the reskin | material and surface · light quality and colour · atmosphere and participating media · weathering, grime, wear · register (film / digital / archival) | expensive in 3D; the model's strongest ground |

**Write the split down before you build anything.** Two named rules:

1. **Nothing appears in both columns.** If you find yourself carefully modelling fog *and* prompting for
   fog, one of them is waste.
2. **Anything that has to be identical across shots is HELD, always.** No exceptions. That is Pattern 18 —
   continuity comes from not re-deciding, never from describing consistently. **[SD]**

State any element you are consciously leaving uncontrolled. Unspecified is not neutral; it is delegated.

---

## Step 2 — Choose the control artifact

Three ways to hold the HELD column. Pick by cost against how tight the control needs to be.

| Artifact | Control | Cost | Use when |
|---|---|---|---|
| **Greybox render** — kitbashed 3D, untextured, animated camera | highest: exact path, speed, timing, occlusion, scale | build a scene | the move is precise, or the shot must match | 
| **Annotated plan or still** — path drawn on a screenshot, plan view, map or concept frame | good: route, direction, beats, points of interest | minutes | the move is describable as a line over a place that already exists as an image (Pattern 10) |
| **Pose set** — camera frustums / reference views from an actual capture | high: real poses, real place | needs a capture | recreating a real location or a move you actually shot (Pattern 11) |

Kitbash rather than model. **The greybox does not need to be good. It needs to be correct in space.** Grey,
untextured, proxy geometry — its only job is to be unambiguous about where things are and where the camera
goes. **[CG]**

**If you chose the annotated plan:** use the vocabulary that has been shown to read — a continuous line for
the trajectory, an arrowhead for direction, numbered waypoints for order, a circle for the point of
interest (Pattern 11 table). And **plan the scaffolding's removal now**, not in the render: either strip the
annotation in a follow-up editing turn, or have the model place the arrows itself and then follow them
(Pattern 13).

---

## Step 3 — Block it

Decisions to make in the viewport, where you can see them, before any generation spend:

- **Camera.** Start pose, end pose, path shape, speed and where the speed changes. Height and whether it
  reads handheld, drone, dolly or crane. The path is the point of the whole exercise.
- **Scale.** The most common lie in generated video. Put a human-height proxy in the scene.
- **Occlusion order.** What passes in front of what, and when. This is the thing text prompts cannot say
  and greyboxes say for free.
- **Timing.** Where the beat lands. The clip length is a decision here, not a default.
- **Negative space.** What the camera reveals and when. **[CG]**

Then render grey, at the working resolution and the intended duration.

**Front-load these.** The known asymmetry of the method: changing the blocking after the reskin means
regenerating everything downstream. Blocking changes are the expensive ones — spend the time here.
(Recorded from the counter-cost raised in the original post's comment thread; see `genius.md` Pattern 6.)

---

## Step 4 — Write the reskin brief

The scene is already in the greybox. **The prompt is not a scene description; it is a lighting and
materials note** (Pattern 8). His three named controls, verbatim from source, plus what they each decide:

| Control | Decides | Write it as |
|---|---|---|
| **Key light direction** | modelling, shadow direction, where the eye goes | direction relative to camera and subject; hard or soft; one named source |
| **Environment / skybox** | ambient colour, fill, sky, overall time-of-day read | the condition, not an adjective — overcast noon, low sun behind, sodium streetlight, moonless |
| **Materials** | surface, age, reflectivity, how light is returned | per named surface in the shot, not globally |

Plus the fourth thing the reskin is for: **atmosphere.** Name the physical phenomenon, not the mood — fog,
haze, dust, spray, embers, caustics, god rays. His own praise vocabulary is entirely phenomena, never vibes
(see `genius.md`, quality rubric). **[SD]**

**Ban list for this brief:**
- Camera moves. They are in the greybox. Re-describing them invites the model to renegotiate.
- Composition and blocking. Same reason.
- Adjective stacking — "cinematic, moody, epic" decides nothing.
- Anything in your HELD column.

---

## Step 5 — Generate, then grade against ground truth

**The greybox is the answer key.** Compare the reskin against it, in this order (Pattern 15):

1. **Did it hold the camera path?** Same route, same speed profile, same start and end framing.
2. **Did it hold geometry and scale?** Nothing moved, grew, or disappeared. Occlusion order intact.
3. **Did it hold timing?** The beat still lands where you blocked it.
4. **Then, and only then, is the look worth judging.**

A drift in 1–3 is a **control failure** — fix the artifact, not the prompt. A miss in 4 is a **brief
failure** — fix the light, skybox or material language and regenerate, which is cheap precisely because the
blocking is untouched. Keeping those two diagnoses separate is the entire value of the split. **[SD]**

On rerolls: a single failure tells you very little about a stochastic generator. Distinguish *the model
can't* from *this draw didn't* before you redesign anything (Pattern 26).

---

## Step 6 — Say what the output actually is

Close by naming which of the two this run produced:

- **A shot** — it goes in the piece.
- **A look decision** — the greybox and the chosen reskin become the reference that a traditional pipeline
  (or a different model, or a human artist) now executes against. *"Even if you end up eventually [doing]
  this all the good old fashioned way, it's such a quick way to explore your creative possibilities, and
  dial in exactly what you want."* — Pattern 7.

The second is the more common and more valuable answer, and the one people forget to claim.

---

## Quality gate

- [ ] The HELD/BOUGHT split is written down, and nothing appears in both columns
- [ ] Every element required to be consistent across shots is in HELD
- [ ] The control artifact is named, and its removal-from-frame is planned if it is an in-frame annotation
- [ ] The reskin brief contains zero camera or composition language
- [ ] Light is specified as direction plus a named source; atmosphere as a named physical phenomenon
- [ ] The generation was graded against the greybox on path, geometry, scale and timing *before* look
- [ ] Any drift is labelled as a control failure or a brief failure, and the fix is applied to the right layer
- [ ] The output is declared as a shot or as a look decision
- [ ] No step of the delivered spec depends on a named product

**Execution prompt:** `references/prompts-v2/greybox-reskin-shot.md` — honor its Output Contract.
