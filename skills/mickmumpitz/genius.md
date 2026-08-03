# Mickmumpitz — Genius Context

> Determinism over prompting. Every "AI consistency problem" is a control problem, and control is
> bought by moving decisions **out of the sampler** and into artifacts you author: a dataset, a mask,
> a geometry, a path, a caption.

Extracted 2026-08-02 from five watched sources (2025-03-07 → 2026-07-17). Every claim below is
timestamp-anchored to one of them. Source ledger and fidelity flags: `references/source-notes.md`.
Tool names, model names, node graphs and version-specific settings are quarantined in
`references/era-bound-mechanics.md` — **nothing in this file depends on a line of that appendix.**

---

## Who (verified only)

German AI-filmmaking channel, ~182,000 subscribers as of 2026-08-02, site `mickmumpitz.ai`,
Patreon-funded, publishing free open-source character/VFX workflows since at least 2024. Ships a
finished short film with most major pipeline release (*Paper Jam*, 2025-03-07; *The Crystal Cat*,
2025-07-17) — the film is the proof, the workflow is the product.

**Nothing else about his background is in the sources.** No studio credits, no film-school history,
no client list, no real name. Do not assert any.

**What he adds that nobody else in the house does:** everyone else in the creative lane teaches
*direction* (St. Pierre, Clark, Flynn, Grace Liu) or *operation* (banana-pro-director, Tao). He is
the only one who teaches **determinism** — how to make the same character, the same camera move, the
same composition come out of the machine twice, on purpose, without asking nicely.

---

## The one-line thesis

> *"The important thing is if you want to control it, you can."*
> — AI VFX Pipeline masterclass, 2026-03-30, 04:01

Not "you must control everything." The claim is that control is **available at every level**, priced
in setup effort, and you choose the rung. That is the whole doctrine.

---

## The core claim

**Consistency is not a prompting skill. It is an authoring skill.**

Everything that must stay the same across shots gets **externalised into an artifact before
generation** — a trained character, a mask, a tracked camera, a blocked pose, a depth map, a captioned
dataset. The generator then has no room to disagree with you about it. What is left in the prompt is
only what you're genuinely willing to let vary.

The corollary is the diagnostic that runs through every source: **when the model gets something
wrong, the first move is never a better adjective. It is a better picture.**

---

## The Control Ladder

Every shot sits on a rung. The rung is chosen by what the shot actually needs, not by ambition — he
routinely picks a low rung and says so out loud. Cost rises down the list; so does determinism.

| Rung | What you author | What it locks | Cost |
|---|---|---|---|
| 0 | Text prompt only | Nothing. Vibes. | ~0 |
| 1 | Reference image(s) | Identity, style, look | minutes |
| 2 | Mask (black/white) | **Where** the change is allowed to happen | minutes |
| 3 | Structural ControlNet (edges / depth / pose) | Geometry, silhouette, human motion | minutes–hours |
| 4 | Camera tracking data | The camera move itself | hours |
| 5 | Authored 3D layout geometry | Space, proportion, eyelines, blocking, the whole shot | hours–days |
| 6 | Trained character model (LoRA) | The character, across every future shot and every model | ~1–2h train + dataset build |

Rung 6 is orthogonal to 0–5 and stacks with all of them. Rungs 0–5 control *a shot*; rung 6 controls
*a franchise*.

**"We could just let the AI figure it out based on a text prompt alone, or we could track the shot,
jump into Blender, and design the geometry of our scene."** (2026-03-30, 03:36) — both are named as
legitimate, in the same breath.

---

## The Four Building Blocks

> *"Remember, all you need is a black and white mask, a driving video — this is your modified plate
> combined with a ControlNet — reference images, and a detailed prompt. Once you understand these
> building blocks, a world of possibilities will open up for you."*
> — 2026-03-30, 04:04

Four **independent axes**. This is the compositional grammar of every controlled shot he makes, and
it is entirely model-agnostic:

| Block | Answers | Failure when it's wrong |
|---|---|---|
| **Mask** | *Where* am I allowed to change things? | Change bleeds into the wrong region, or the region you needed to change is frozen |
| **Driving plate + ControlNet** | What *structure* survives? | Geometry drifts, camera slides, subject floats |
| **Reference images** | What *identity/look* does the new content have? | Wrong style, wrong character, unintended bias (see Pattern 9) |
| **Prompt** | What is *happening*? | Model invents motion or subject you didn't ask for |

Diagnosing a bad shot means asking, in order: which of the four was under-specified? Not "which model
should I switch to."

---

## The 22 genius patterns

### A. The character-dataset method (the durable core)

**1. The dataset is the character; the model is disposable.**
You do not prompt a character into existence. You build a dataset that *defines* it, then bake that
dataset into whatever model is current. He does this explicitly and repeatedly — the same folder of
images and captions is trained into an image model, a bounding-box model, and a video model in one
sitting (2026-07-17, 02:43–02:45 and 30:29–31:57). The images and captions are the asset that
survives; the checkpoint is a rendering of it. *This is the single most durable idea in the corpus.*

**2. The five dataset rules** — the deepest craft he teaches, stated as a numbered list
(2026-07-17, 01:03–02:28). Verbatim mechanism per rule:

1. **The trigger word.** *"During training, everything that's not explicitly mentioned in the caption
   gets attached to this word. Your trigger word becomes your character."* Every un-captioned property
   in every image accretes onto that token. This is why rule 4 exists.
2. **Vary what you want to generalise.** *"If you train a LoRA only on close-up images of your
   character, the model starts to learn that your character only really exists in a close-up
   position."* The set's *coverage* becomes the character's *range of existence*. Same for lighting,
   poses, clothes.
3. **Decide what stays consistent and what you want to change later** — before you build the set.
   *"If your character is only supposed to wear one set of clothes, it's fine to train on the same set
   of clothes in each image."* Consistency is a budget you allocate, not a virtue you maximise.
4. **The caption decides whether you can change something later.** Twenty images in one outfit is fine
   *if* the outfit is captioned — *"the LoRA learns that these clothes are not attached to your trigger
   word."* Trade-off named honestly: *"the more detailed your caption, the more flexible you are later,
   but also the longer your prompt has to be because you have to recall all these elements."*
5. **A caption is a reverse prompt.** *"You always need to create these captions in the same style you
   would later create an image prompt for that image model."* Caption grammar must match target-model
   prompt grammar — long natural language for one model, structured JSON with bounding boxes for
   another. Mismatch here silently degrades everything downstream.

**3. The model-sheet shape.** What a complete dataset actually contains, verified on screen
(2025-10-07, 07:07–09:05; 2026-07-17, 05:39–05:48):
turnaround (front / three-quarter / side / three-quarter-back / back, same wardrobe, plain ground) ·
close-up portrait on white · T-pose · laying down · walking · sitting · emotion variants (per-expression
slider on the portrait) · wide shots · varied lighting conditions · varied environments · an
awkward/interaction prompt that tests articulation (*"failing to look at a frog"*). Close-ups AND
wides in the same set — rule 2 made concrete.

**4. The detail-anchor loop.** The drift-repair method, and the clearest demonstration of
show-don't-describe. Sequence (2026-07-17, 06:59–08:19):
generate set → train a test model → notice *which specific detail* drifted (*"I realized that her
necklace changed a lot"*) → author targeted images of exactly that detail — close-up, side view,
different lighting → **when generation still isn't matching, snip the detail out of the original input
image with a screenshot tool and feed it back as an additional reference** → add to dataset →
retrain. He repeats this for three characters' necklaces, piercings and makeup.
*You debug a character by photographing the part that broke.*

**5. The reference pair: body-scale + identity-scale.** *"Usually the T-pose and the full face is
giving you a lot of flexibility"* (2026-07-17, 06:38). Every generation gets one reference carrying
geometry/proportion and one carrying identity at usable resolution, because a single image almost
never carries both. When a third property matters, it gets its own reference (the necklace snip).
Corollary from the same source: if your input image is a close-up, everything below frame **will be
invented** unless you name it — *"clothes would usually be extracted from the full-body image, but
since we only have the upper body here, we should name the rest"* (04:59). He adds *"wearing chunky
sneakers"* / *"wearing black loafers"* purely to stop the model choosing for him.

**6. Face resolution is a physics problem, not a model problem.** *"In some shots when the face is
really small — for example in full-body T-poses — the face changes a little bit because the model
doesn't have enough resolution to generate"* (2026-07-17, 10:23). The fix is not a better model or a
stronger prompt: it is **selectively** re-detailing only the images where the face occupies too few
pixels, chosen by a pre-selection pass, *"because in some images the face is already filling up almost
the whole image."* Never blanket-apply a corrective; apply it exactly where the defect is.

**7. Multi-character separateness is a data problem, not a technique problem.** The naive move —
two trained characters in one prompt — merges them (*"it merged the character's appearance, so now Dave
also has kind of her hair"*, 2025-03-07, 02:11). Two generations of workaround failed to satisfy him
(regional masking: *"the proportions of the character changes and it's still not really as controllable
as I would want it to be"*, 02:32). The 2026 answer is data: **put all characters in one dataset AND
include images of them together in the same shot**, captioned with every trigger word plus where each
one is and how they interact — *"so the model can learn that these are separate entities"*
(2026-07-17, 17:29). Verbatim caption rule he types into the tagger:
*"If there are multiple characters in the same image, add their trigger words and describe where they
are in the image and how they are interacting."* Model capacity scales with cast size — he raises the
rank for three characters and says so.

**8. Last checkpoint ≠ best checkpoint.** *"The last one doesn't mean it will be the best one. So
download this one, but also download some of the other ones and test them out"* (2026-07-17, 15:41).
Training is a curve you **sample**, not an endpoint you wait for. He downloads several and picks by
eye; overtraining reads as *"a little overbaked, a little bit weird."* Save intermediate versions on a
fixed interval so there's something to sample.

**9. Every reference image is a vote — including the ones you didn't mean to cast.** The fireball
post-mortem (2026-03-30, 16:29–16:57): he wanted a flame, kept getting a literal ball. Cause:
*"I had this image right here in the reference images and it just looked too much like a ball, so I
guess it makes sense that the AI model would generate a ball — especially since that mask shape here is
also ball-shaped."* **The mask shape is a reference too.** Two silent votes for "ball" beat every word
in the prompt. Audit your inputs for accidental signal before you rewrite the prompt.

### B. Blocking and previs

**10. Block the camera in 3D before generating.** *"The next part of the process mirrors traditional
3D animation. We focus on the most important poses in each shot and animate them without interpolation
in a process called blocking"* (2025-03-07, 09:08). Import characters + environment, place the shot
camera, key only the important poses, no in-betweens. Then — separately — **light the layout for mood
before any AI touches it**: *"we spend some time perfecting the mood for our film, creating a late
evening atmosphere just after sunset"* (09:22). On screen at 09:05 and 09:25: the office layout with a
visible camera frustum, two rough characters posed, then the same frame lit warm and evening.

**11. The layout is a render target, not a picture.** You are not making the 3D look good; you are
making it **correct** — proportions, eyelines, spatial relationships, camera move. Everything else is
the render pass's job. He is blunt about how ugly the input is allowed to be:
*"The room is absolutely not looking perfect, but if you just want to have a basic scene where you can
pose your characters in, it is honestly enough"* (07:29) and, on a broken auto-rig,
*"there are still some broken parts in there — you could manually fix them, but honestly this is good
enough"* (07:34). *"We'll transform these ugly layouts into polished final renderings"* (09:33).
**"Good enough" is an engineering verdict he issues deliberately, on the layers whose only job is
geometry.**

**12. Blocking survives everything.** A shot list of blocked poses + camera moves is the one artifact
in the whole pipeline with zero dependence on the model, the year, or the tool. It hands off to a
renderer, a different renderer, or an actual camera.

**13. Two-pose interpolation as the animation unit.** *"We pretty much worked from one pose to the
next, interpolating the movement in between, and then editing everything together"* (2025-03-07,
23:05). The unit of production is not "a clip" — it is **a pose pair**. Author the start frame and the
end frame deterministically, then let the model own only the transit. Same source names the failure
mode this creates (models add mouth movement whenever they see a face) and the fix (negative-prompt
it).

**14. Choose the control representation with the widest domain.** He deliberately picked motion
trajectories over pose skeletons: *"With trajectory points you can animate anything you want — not just
humans, but also 2D animations, fantasy creatures, camera movements, or any subject that the open pose
format wouldn't work for"* (2025-07-17, 02:07). When two control formats both work for your current
shot, take the one that will still work for the shot after next.

### C. Controlled generation

**15. Structure early, freedom late.** Structural guidance decayed across the denoise:
*"At every step the ControlNet gets weaker and weaker, making sure that the composition of the image is
exactly the same as the original image — but the further we go with the image generation, the more
freedom [the model] gets to generate additional detail"* (2025-03-07, 12:12). Composition is decided in
the first steps; detail is earned in the last. Implementation is era-bound; **the principle is not.**

**16. The two-step preview shop.** Separate the *take* decision from the *quality* decision.
*"You can set the steps to something like two, and it will generate a sort of preview where you can
already make out the final movements pretty well — but of course it looks pretty bad. And then we can
quickly try out different seeds, choose the one where we like the movement, and then bump up the steps
to the final eight and render the final shot"* (2025-07-17, 12:42). Companion move: turn on live
latent previews *"and often you can tell from the first step on if it's working or not"* (2026-03-30,
11:56) — kill a bad generation at step one instead of paying ten minutes for it.
**Seed is a variable you shop, not a nuisance you endure** — and you shop it cheap.

**17. Derivation buys you compositing.** Because the generation was structurally derived from the
plate, it re-composites into the plate for free: *"in After Effects I actually used the original mask to
blend the generated footage with the original footage… it's super easy because it matches up
perfectly"* (2026-03-30, 16:09). A shot generated off a tracked, masked plate lands back in the timeline
frame-accurate. A shot generated off a vibe does not.

**18. The mask boundary is where you spend the trade-off.** Named explicitly with both directions on
the same shot (2026-03-30, 12:03–12:31): a tight cut-out mask preserved his identity but the lava
interaction at his shoes was bad; a full white mask fixed the integration but *"I look completely
different."* Verdict: *"the best approach would be to exclude my upper body and face from the mask, but
maybe add a bit of blur to the feet."* And the deliberate inverse on the fireball shot —
*"I included myself into the mask because I actually wanted some of these lighting effects on my body"*
(17:05). **Identity preservation and scene integration are in tension, the mask is the dial, and it
can be feathered.**

**19. When the model over-runs your intent, give it less freedom — not more prompt.** The explosion
shot ended on a fully black frame, so *"the model took this freedom and ran with it, creating this new
camera move between these cars, which is actually kind of cool, but I didn't want that."* Fix:
*"I created Canny outlines for this shot and blended them only in the edges, so that the model can
understand the camera movement"* (2026-03-30, 18:15). **Structural guidance placed exactly where the
drift is, and nowhere else.**

**20. Author the driving video as animation.** The superhero punch (2026-03-30, 17:30–17:58): he
hand-built the driving plate as a timed sequence — *"first my arm turns into this black area with the
open pose ControlNet, then it happens to my second arm, then it happens to my body, and then I punch
the ground. A black mask quickly turns the full frame black"* — and when the explosion came out too
small, *"I added these white lines here that spread outwards in the hopes of creating this, and it
actually worked kind of well."* The driving video is a **hand-authored piece of animation**, not a
preprocessing artifact. You can draw scale, timing and energy into it directly.

**21. Don't stack every control you own.** *"I gave [it] the inpainting area plus the ControlNet and
point data, but this seemed to be too much. The creature still moved along the path, but it was just an
unanimated image sliding over the video"* (2025-07-17, 06:26). Over-constraining doesn't over-determine,
it **kills motion**. He publishes the branch rule rather than a preference: *"use either the start frame
plus ControlNet technique for some natural character movement, or the inpainting technique for the best
consistency."* Two named recipes, one trade named.

### D. Process discipline

**22. Prompt-format propagation: write one gold prompt, let an LLM apply the grammar.**
*"It's really good to create a sort of preset and then tell a large language model: this is the format,
please adapt this format to the next scene"* (2026-07-17, 32:53). Also used to prompt-proof:
*"prompt-proof this video prompt. Focus on the description of effects like lava, fire and smoke. Do not
mention the camera movement — we already have that"* (2026-03-30, 11:13). Not *"have the AI write my
prompt"* — **have the AI apply my format, and forbid it from touching the axes I already control
deterministically.**

Supporting habits, all sourced:
- **Modular groups.** *"All of these groups are modular — you can just copy a group and change the
  prompt… it remembers that all of these groups are already calculated, so it will start right at the
  new group"* (2025-10-07, 07:48). The pipeline is a **library you extend and cache**, not a script you
  rerun.
- **Preview mode before commit.** Build the dataset in preview, refine, then flip to save
  (2026-07-17, 04:25). Folder-versioning trick: bump the character name's number to snapshot only the
  currently-displayed images into a fresh folder (2025-10-07, 09:57).
- **One naming spine.** Character name = trigger word = output folder = dataset name = job name.
  *"Make sure to use something that is unique"* (2025-10-07, 06:32).
- **Ordered graph.** *"We're working from left to right and top to bottom"* — stated in four of five
  sources. Pipelines are read in one direction, always.
- **State the cost.** *"We spent like $4 to train this, so we should grab everything we can, right?"*
  (2025-10-07, 18:25); *"don't forget to stop the pod so you don't burn through any more money."*
- **Give credit by name.** Nathan Shipley, Ostris, Kijai, Inner Reflections, MDMZ, whatdreamscost —
  named on screen with links in every source.

---

## Signature moves

1. **The T-pose + face pair** — every generation gets a body-scale reference and an identity-scale
   reference. Add a third only for a property that has already been observed to drift.
2. **The detail-anchor snip** — screenshot the drifting detail out of the original input, feed it back
   as an extra reference, then generate close-ups of it from more angles into the dataset.
3. **The group-shot injection** — teach a model that characters are separate entities by giving it
   images of them together, captioned with every trigger word plus position and interaction.
4. **The two-step preview shop** — cheap low-step pass to choose the take, expensive pass to finish it.
5. **Block before you generate** — key poses without interpolation, place the shot camera, light for
   mood, *then* render.
6. **The plate-derived composite** — mask back into the original footage; structural derivation makes
   the re-comp free.
7. **Decaying structure** — lock composition in early steps, hand detail back in late ones.
8. **Checkpoint sampling** — save on an interval, download several, judge by eye, expect the best one
   in the middle.
9. **Edge-only guidance** — when the model invents a camera move, blend structure into the frame edges
   only, so it reads the move and nothing else.
10. **Preview-mode datasets** — never write to the real folder until the set is what you want.

---

## The quality rubric — how he judges

**The honest-folder standard.** His highest claim about a result is not "look at this image," it is:
*"So this is no cherry-picking. These are all the images that came out of the model"* (2026-07-17,
21:21) — followed by scrolling the *entire* output folder including the ones that failed
(*"that is a prompt issue — now Emily is there two times in the shot. I fixed that, then it worked well
again"*). **A character is locked when the whole folder holds, not when one frame does.**

**Defects are named as objects, never as vibes.** From five sources: *"it still has a little bit of
that plastic AI look"* · *"her necklace changed a lot"* · *"look at that left pupil"* · *"the movement
is a bit more rigid, it doesn't look as natural"* · *"it's a bit floaty and the tail is not wiggling
enough"* · *"the lava is flowing really fast, that's a bit weird"* · *"how he's touching this curtain is
a bit awkward"* · *"that's an awkward kiss, eyes are closed"* · *"I don't know what's happening with
this one leg."* If you can't point at the defect, you haven't diagnosed it.

**The 80% trap.** *"I tried out so many variations for the driving video, and each of them worked like
80% well, but there was also always something weird going on"* (2026-03-30, 17:17). 80% is the plateau
where people ship. He treats it as the signal to go back and author more control, not to reroll.

**The integration test** (for anything composited into a plate): does the light interact? *"Look at
this short moment right here with the hand — it actually reflects on this aluminium steel, and there's
also a perfect shadow. It also adjusted the lighting on myself"* (2026-03-30, 14:53). Shadows, contact,
reflections, spill onto the original subject. Not "does it look cool" — *does the physics agree.*

**"Good enough" is a verdict, not a shrug** — issued deliberately on layers whose only job is geometry
(the rig, the greybox room, the layout), and never on the character or the final render.

**Failure is shown on camera.** *"Okay, this crocodile shot didn't work out exactly as planned"* —
then the diagnosis, then what would fix it. *"Don't expect it to work like this first try."*

---

## Voice profile

First-person live process narration, present tense, German-accented English, calm and quick. Sentences
run short and declarative: *"Let's just click run."* *"And this worked really well."* *"That's pretty
much it."* Habitual tells:

- **"honestly"** signals he is deliberately lowering a standard on a layer that doesn't need it —
  *"honestly this is good enough"*, *"it is honestly enough."*
- **Surprise stated plainly** when something works: *"I was surprised to see that it just instantly
  worked."* No hype vocabulary.
- **Costs named out loud**, in dollars and hours, mid-tutorial.
- **Credit given by name**, unprompted, to the people whose tools he's standing on.
- **Never oversells.** *"Don't expect it to work like this first try."* *"It definitely needs some time
  to get used to."*
- Optimism is expressed as **fun**, not as revolution: *"you can see how much fun it is."*

When channelling: narrate the build, name the defect, state the trade, give the cost, credit the
source, and never claim a result you didn't scroll the whole folder for.

---

## What NOT to do with this skill

- **Do not use it for taste.** He teaches control, not composition, palette or meaning. Look card,
  lighting language, shot grammar and "why is this flat" belong to `skills/dave-clark/`; image
  art direction belongs to `skills/nick-st-pierre/`; batch style operations to `skills/rory-flynn/`.
- **Do not treat the node graphs as the method.** They are era-bound, quarantined, and dated.
- **Do not port his tool stack as a recommendation.** He is a local-open-source specialist with a
  high-end GPU. The *method* is stack-agnostic; the *stack* is not a house standard.
