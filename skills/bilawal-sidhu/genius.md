# Bilawal Sidhu — Genius Context

> 3D-grounded camera and spatial control for generative video. The pre-generation layer where
> the camera stops being a hope you type and becomes a variable you set.
>
> Extracted 2026-08-02. Sources dated and keyed below; era-bound tool mechanics quarantined in
> `references/era-bound-mechanics.md`. Fidelity ledger: `references/source-notes.md`.

---

## Who he is (corroborated receipts only)

Six years at Google as a senior product manager on spatial computing and 3D maps — Immersive View,
the ARCore Geospatial API, YouTube VR [S8, S9]. Now a creator and analyst: a 2.1M-subscriber YouTube
channel and the *Map the World* Substack (36k+ subscribers) covering AI, AR/VR, robotics and spatial
computing [S10, channel page 2026-08-02]. TED speaker and host of *The TED AI Show* [S9]. Early
access to Google DeepMind's world-model work, including a recorded interview with the Genie 3
research co-lead and its product manager [S5]. Taught a *Generative AI Creation Masterclass* on Maven
(2 weeks, now retired; 4.7/5 across 23 reviews) [S8].

**What he is not, and must never be posed as:** a narrative film director. He does not teach story,
performance, or edit. His authority is spatial computing — how reality gets captured, represented and
navigated — applied to generative media. Route story and cinematography elsewhere (`skills/dave-clark/`).

**What he adds that nobody else in the house does:** every other creative master in this system works
in the 2D plane — prompt, image, shot, cut. Sidhu is the only one who treats **the scene as an object
that exists before the render**, and the camera as a thing you *place* rather than describe. He is the
house's answer to "the camera move isn't what I asked for" and "shot 4 doesn't look like it's in the
same room as shot 3."

---

## The one-line thesis

> *"We are largely flying blind. We don't have the equivalent of a viewport — this 3D representation
> that allows us to see exactly what we had in mind before we actually hit that render button."*
> — [S2 00:25]

Everything else follows from that sentence.

---

## The core axis: prompted hope vs. controlled variable

Every property of a shot is either **asserted through an artifact you can point at** or **left to the
model's imagination**. Sidhu's entire method is moving properties from the second column to the first.

| Property | Prompted hope | Controlled variable (his move) |
|---|---|---|
| Camera path | "slow drone push under the bridge, then rising left" | a red line drawn on the actual location [S4 00:09] |
| Camera pose | "low angle, wide" | rendered frustums from a real capture [S4 02:07] |
| Blocking, timing, geometry | described in prose | a greybox animation rendered from kitbashed 3D [S1] |
| The place | "downtown Austin" | the nearest Street View panoramas loaded into context [S6 05:21] |
| Environment continuity | re-prompted every shot | built once, imaged from any angle [S2 05:16] |
| Character continuity | re-prompted every shot | built once, reused [S2 05:16] |
| Look, light, atmosphere | *deliberately left generative* — this is the part you buy [S1] |

That last row matters as much as the others. He is not trying to control everything. He is trying to
control the things a model is bad at and buy the things it is good at. The greybox holds geometry,
motion and camera; the reskin buys volumetrics, light interaction and material. Confusing which is
which is the whole failure mode.

---

## Group A — The Viewport Doctrine (why 3D at all)

### Pattern 1 — Flying blind is the defect, not the difficulty

The complaint that "3D is hard" is aimed at the wrong cost. What you get for the setup cost is a
**source of truth you can look at before you spend a generation**.

> *"If you used any 3D application, you know exactly what I'm talking about. It is the visual anchor,
> the source of truth that gives you this interactive window into the world that you are creating. And
> I would posit that in the case of AI, that's exactly what we need, except we're co-creating this
> world."* — [S2 00:52]

Mechanism: generation is a sampling process. Without a viewport, every attempt is an independent draw
and your only feedback is the finished render — which arrives after the money and the minute are spent.
A viewport turns the loop from *sample → judge → resample* into *arrange → verify → render once*. The
setup cost is paid in exchange for killing the resample loop, which is where the real time goes.

**Diagnostic question this yields:** *What would I have looked at, before hitting generate, that would
have told me this was wrong?* If the answer is "nothing," you were flying blind and the bad output was
not bad luck.

### Pattern 2 — Nodes are the assembly language; don't mistake plumbing for filmmaking

> *"Nodes are like the assembly language of AI creation, but we need a higher order abstraction that
> feels a lot like it does to create on a sound stage."* — [S2 01:58]
>
> *"What we're doing is plumbing. But let's not call it filmmaking or content creation."* — [S2 01:36]
>
> *"Nodes are essentially a bridge to the future. They are not a destination. They're a good side dish,
> a good companion, but they can't be the main course."* — [S2 10:36]

Mechanism: a node graph gives you control over *the order of operations between models*. It gives you
zero control over *what is where in space*. That is a category confusion, and it's expensive because
node graphs feel like control — *"they give you the illusion of control, but you're still hitting the
generate button, waiting for the model to come back with something that you hope is close to what you
want"* [S2 00:01]. He is explicitly not anti-node — *"I grew up on After Effects and Nuke. I appreciate
when you need nodes"* [S2 01:13]. The rule is abstraction-level discipline: use nodes for plumbing,
never as the place where composition gets decided.

**The general form (this is the transferable part):** *the interface you use to make a decision should
match the kind of decision it is.* Spatial decisions want a spatial interface. Temporal decisions want a
timeline. He points at Unreal as the existing proof that all three can coexist — *"You've got node graphs
when you need them. You've got the timeline editor when you need them... And of course, you've got the
viewport"* [S2 04:15].

### Pattern 3 — Explicit vs. implicit, chosen per shot, not per belief

His strategic taxonomy [S3 06:39 onward]:

- **Explicit** — start from things that exist as addressable structure (meshes, splats, a scene graph),
  supercharge with AI. Property: *"everything AI does is still addressable. It's editable. You can change
  things"* [S3 08:39].
- **Implicit** — everything lives in model weights. Property: fast, atmospheric, emergent, and
  *"today it is actually hard to edit, constrain, and reason about hidden layers of meaning"* [S3 10:11].

He refuses the tribal version of this argument. On the "it's just 2D pixels" objection to world models:
*"Well, who cares? Because Genie 3 gives you multiple perspectives that you can interactively explore.
The 3D structure in this case is just represented by the weights of the model"* [S3 09:48]. And the
converse — he doesn't think implicit wins by default either.

**The operator's version:** this is a per-shot routing decision, made on one question — *does this shot
need to be edited, matched, or repeated?* If yes, explicit. If it needs to be atmospheric and felt once,
implicit is cheaper and usually better.

### Pattern 4 — The reproducibility gate: "can I shoot multiple takes on this set?"

The single most portable decision rule in the corpus.

> *"Let's say I'm doing some virtual production or lightweight interactive experiences. Walking around
> environments where I don't care about coherence — it's a cozy environment where I want you to feel
> enveloped by the vibe of the place and don't really care about the exact pixel-perfect execution...
> Genie is incredible. But if I need a perfectly reproducible set that I can shoot multiple takes on,
> yo, I'm probably going to pull a Gaussian splat out of Genie or just go to World Labs and generate it
> once. And then I can shoot all the takes I want."* — [S3 15:12]

Mechanism: **persistence is a cost you pay once or a cost you pay per take.** A stochastic generator
re-rolls the world on every attempt, so the set is a variable. Freezing the environment into an explicit
asset converts it into a constant — and only then do multiple takes of the same scene actually mean
anything, because only then are they takes *of the same thing*.

He names the failure state plainly: *"Genie is very much a slot machine right now"* [S3 15:34].

**The gate, as a question to ask before any multi-shot piece:** *how many times does this location have
to appear?* Once → generate it. More than once → freeze it first.

### Pattern 5 — Photorealism and cinematic realism are different targets

> *"What we're talking about allows you to take creative liberties, right? Because photorealism and
> cinematic realism are very different things."* — [S2 10:14]

Said in the context of contrasting creative work with robotics training data, where the requirement is
*"make this look super photorealistic and true to life."* Mechanism: the two goals impose opposite
constraints on the grounding layer. Robotics needs the anchor to be *accurate*. Film needs it to be
*consistent* — which permits the anchor to be a fantasy, a stylized map, or a historical reconstruction,
as long as it holds still. This is the permission slip for Pattern 12.

---

## Group B — The Greybox → Reskin Method (the signature move)

The full primary source is three steps and three notes, posted 2025-01-06 [S1]. Verbatim:

> *"Video-to-video AI combined with 3D tools is a surprisingly powerful & underrated combo. Here's my
> 3-step workflow:*
> *1. Build a scene by kitbashing 3d models*
> *2. Render out a greybox animation*
> *3. Use Runway Gen-3 to reskin & define the final look*
>
> *TL;DR it's an extremely fast workflow to make 3d animations and do look dev for your project."*

### Pattern 6 — Separate blocking from look, and iterate them on different clocks

This is the load-bearing idea and it is why the method survives every model change. The greybox render
carries **geometry, spatial relationships, motion, timing and camera**. The reskin pass carries
**material, light, atmosphere and register**. They are independent axes.

Mechanism: in a text-to-video attempt these two are entangled — change the look prompt and the camera
move changes too, because both are being sampled from the same latent draw. Splitting them means a look
change costs one cheap generation and a blocking change costs one cheap render, and neither disturbs the
other. Kitbashing (assembling from existing parts rather than modelling from scratch) is what keeps the
blocking side cheap enough for this to be worth it — the greybox does not need to be good, it needs to be
*correct in space*.

**The known asymmetry, flagged honestly:** a practitioner in the post's own comment thread noted the
counter-cost — iterating on the 3D base means regenerating downstream. Recorded here because it is the
real constraint on the method: *front-load blocking decisions, because they are the expensive ones to
change.* (Attribution: commenter on [S1], not Sidhu.)

### Pattern 7 — Reskin as a look-dev instrument, not only an output path

> *"Even if you end up eventually [doing] this all the good old fashioned way, it's such a quick way to
> explore your creative possibilities, and dial in exactly what you want."* — [S1]

Mechanism: this reframes the whole method from "a way to make finished video" to "a way to make the
look decision before committing production money." One greybox render supports unlimited look
explorations at generation cost, which is orders of magnitude below the cost of lighting and texturing
the same scene properly. The output of the exercise can legitimately be *a decision*, not a shot — and
the traditional pipeline then executes against a look that's already been chosen with the real camera
move and the real blocking.

**This is the highest-value use of the method for most projects, and the one people miss.**

### Pattern 8 — Prompt the light, not the object

The reskin prompt is not a scene description. The scene is already in the greybox. The prompt is a
lighting and materials note.

> *"You can really play with the materials and lighting in your prompt too — including the environment
> skybox and key light direction to drastically transform the look and feel."* — [S1]

Named controls, verbatim from source: **materials · environment skybox · key light direction.** That is
a lighting department's vocabulary, not a prompt engineer's. Mechanism: the greybox has already fixed
everything a prompt would otherwise waste its tokens (and its attention budget) fighting over. What
remains for the prompt to decide is exactly the set of things a gaffer and a look-dev artist decide.

### Pattern 9 — Buy what 3D is expensive at; hold what 3D is cheap at

> *"Gen-3 and Sora will do quite well with volumetric fog and lighting effects — love the aurora
> borealis and ground fog, where you see some nice light interactions."* — [S1]

He repeats the observation independently about interactive world models: atmospheric effects are
*"really hard to do in sort of traditional 3D where you have explicit 3D assets, especially in
real-time environments"* [S5 01:30], then names what he's watching for — caustics, god rays, plankton
and bubbles in an underwater scene [S5 02:16].

Mechanism: this is the trade the whole method is built on. Volumetrics, participating media, complex
light interaction and material richness are the expensive end of traditional 3D and the cheap end of
generative video. Geometry, spatial consistency and exact camera motion are the reverse. **The greybox
holds the cheap-in-3D things; the reskin buys the cheap-in-AI things.** Get the split backwards — try to
prompt your camera move while carefully modelling your fog — and you have paid twice for nothing.

---

## Group C — Camera as a Drawn Artifact

The 2026 evolution of the same doctrine. Where 2025 required a 3D render to control the camera, 2026
showed the control channel can be a **drawing**.

### Pattern 10 — Scribble the path; the model reads the line as a trajectory

> *"Last week, I scribbled a drone path on a Google Earth screenshot, and then I gave it to [the video
> model] and asked it to imagine the first-person drone view following that path. And somehow, it
> worked. Not perfectly, it hallucinated, but damn was it close. And critically, these video models now
> understand the assignment, that this little red line is the actual camera trajectory."* — [S4 00:02]

The specific intent behind that line, in his words: *"I wanted basically the drone to fly under the
bridge, up, and to the left towards this Google building"* [S4 01:25]. Try writing that as a text prompt
and predict what you get.

Mechanism: a drawn path is a **spatially registered instruction** — it says *where* in the image, which
text cannot. The model doesn't have to resolve "under the bridge, then up, then left" into a geometry
guess; the geometry is given and the model only has to interpolate views along it. He states the
motivation with no ceremony: *"who the hell wants to sit there and type a convoluted text prompt"*
[S4 03:17].

**The general principle: annotation beats description whenever the instruction is spatial.** This holds
for camera paths, points of interest, object placement, occlusion order, and shot order.

### Pattern 11 — The annotation vocabulary (what people drew, and what it controlled)

Catalogued from the wave of experiments he documents in [S4]:

| Mark | Controls | Source |
|---|---|---|
| A single continuous line | the camera trajectory | [S4 00:09] |
| An arrowhead on the line | direction of travel | [S4 04:47] |
| Numbered waypoints 1–2–3–4–5 | ordering / beats along the path | [S4 03:17] |
| Rendered camera frustums | actual poses from a real capture, not an approximation | [S4 02:07] |
| A circle or highlight on a subject | the point of interest to feature | [S4 05:08] |
| An annotated line drawn over *video* | a path through a real filmed street | [S4 05:31] |

The frustum case is the strongest and least imitated: he fed a Gaussian splat *plus every camera pose
from the actual capture path* — *"every single white camera frustum you see is the camera pose of the
actual path that I took"* — and got back a generation that took the same route, up the same staircase
[S4 02:07–02:30].

### Pattern 12 — Any coherent map works, including a fictional one

> *"You can actually have much more abstract map references... imagine taking any kind of cartographic
> map representation or even a stylized one and using that as a prompt. This could be very useful for
> historical reproductions or fantasy."* — [S4 04:47]

Mechanism: the model needs a *spatial substrate to register the path against*, not a true one. This
detaches the technique from satellite imagery entirely — a hand-drawn fantasy map, a floor plan, a
concept-art plan view, a level layout all work. Combined with Pattern 5 (cinematic realism ≠
photorealism), this is what makes the method usable on fiction and not just location work.

### Pattern 13 — Plan the scaffolding's removal

The annotation is visible in the output. That is a feature until it isn't.

> *"Of course, it's not perfect, and you do have this annoying red line, but since this model supports
> conversational multi-turn editing, you just say remove the red line, and it does it for you."*
> — [S4 01:46]

Mechanism: any control artifact placed *in the frame* becomes a rendered element. Two ways out — remove
it in a subsequent conversational turn, or (the more elegant version, which he credits to another
creator) **have the model place the annotation itself**: *"his innovation is you could just ask the model
to put the arrows in, and so then it'll follow it for you"* [S4 10:17]. That second version is worth
sitting with: the model draws its own control signal, then obeys it — which is a legible plan you can
inspect before the render, i.e. a viewport made of arrows.

---

## Group D — Grounding: retrieve, don't recall

### Pattern 14 — Spatial RAG: put the actual place in context

The most technically specific idea in the corpus, and the one with the longest shelf life.

> *"Rather than Google relying on this model having soaked up every single Street View panorama and
> being able to reproduce it on the fly, you can actually just give it the relevant set of panoramas and
> get a faithful, close to one-to-one rendition, rather than the approximate rendition that we're seeing
> today."* — [S4 06:24]
>
> *"Let's say there's a trajectory that you're going down, this system will retrieve the nearest panorama,
> constantly putting that into context. So the model knows what's physically around it, so it doesn't
> just make up."* — [S6 05:21]

He proves the failure mode by finding it: on the far side of a landmark, *"you don't have these houses in
the back. If they were doing an approach like this, they would factually be loading in those panoramas"*
[S6 05:43].

Mechanism: **model memory of a place is lossy and approximate; retrieved views of the place are exact.**
This is retrieval-augmented generation with a spatial index instead of a text one, and it generalizes far
past Street View. The operator's version: for any real location, character, product or set that has to be
*right*, gather the reference views along the intended path and supply them as context. Don't rely on the
model to remember; make it look.

### Pattern 15 — Build your own ground truth, then benchmark against it

> *"So you take this actual path, run it through Google Earth Studio, that's your ground truth, and then
> see how close [the] generation can get to that actual reference. Essentially a spatial benchmark."*
> — [S4 04:23]

Mechanism: this is a **deterministic renderer used as a measuring instrument.** Render the intended
camera path in something that cannot hallucinate; that render is the answer key. Now the generation has a
grade, not a vibe. He is describing this as something a lab should build, but it is directly stealable at
project scale: your greybox render *is* your ground truth, and comparing the reskin against it tells you
whether the model held your blocking or quietly invented its own.

The corollary honesty check, from him: on whether these generations correspond to the real world —
*"right now, it kind of doesn't. It's like close enough like most image-to-video generations"* [S4 04:00].
Anchored is not accurate. Know which one your deliverable needs.

### Pattern 16 — Anchored fantasy: the real world as substrate, not subject

> *"We can create fantastical, crazy visual effects that are actually anchored in the real world as it
> is."* — [S4 06:51]
>
> *"By bringing reality into latent space, you can now edit it and do things that would have been
> otherwise very hard or tedious to do in traditional tools."* — [S6 04:59]

Examples he ran: the Golden Gate Bridge underwater with a scuba diver, an entire city snow-covered, a
1900s aerial photograph flown around [S6 03:30–03:51]. Mechanism: the anchor supplies the credibility
(scale, geometry, familiar landmark relationships) and the generative layer supplies the impossibility.
Neither alone lands — pure generation lacks the "that's a real place" recognition, pure capture lacks the
event.

### Pattern 17 — You are the system's spatial memory (for now)

> *"These systems don't have spatial memory, and it's you as the human that's sort of managing the
> spatial context for it. In other words, you might go into [a world tool] and capture the environment
> from a couple different angles, and every time you do that generation, you might provide that image
> reference sort of as the ingredient — but I would posit that the system should do that for you."*
> — [S4/S2 07:27]

Mechanism: this converts an architecture complaint into a job description. Until the tools carry spatial
memory, **someone has to hold the register of where things are and which reference belongs to which
shot** — and that someone is the operator. Practically, that means a maintained artifact: a scene
inventory listing every persistent element, its reference views, and which shots consume it. Skipping it
doesn't remove the work; it just makes it happen badly and invisibly, one prompt at a time.

### Pattern 18 — Create once, image from anywhere

> *"You create your character once because you know that's the character that's going to be in all of
> your generations. You create your environment once and you can image it from any direction that you
> want. And then you can frame the shots exactly as you like — rather than typing in esoteric prompt
> incantations hoping that the camera angle comes close to what you had in mind, or drawing weird
> scribbles just to nudge things in the right direction."* — [S2 05:16]

Note that he includes *his own signature technique* in the list of workarounds. The scribble is a bridge;
the built scene is the destination. Mechanism: continuity is not something you achieve by describing the
same thing consistently — descriptions drift. It is something you achieve by **not re-deciding**. Build
once, then every shot is a camera position rather than a fresh act of creation.

This is what he identifies as the actual bottleneck on long-form: *"That is fundamentally what I think's
going to unlock these multi-minute creation[s]"* [S2 09:33], against the current state where *"most of the
professionally generated content that you're seeing is a bunch of these chaotic 1-to-2-minute
advertisements"* [S2 06:42].

---

## Group E — Capture: getting real environments in, first

For work where the environment should be a real place. His stated capture doctrine [S7].

### Pattern 19 — "Paint the scene" — coverage as a mental model

> *"I like to imagine every single image that you take, you're visually splatting the environment with
> paint, and that way you keep a recollection of what it is that you've actually imaged... and you could
> go about capturing the scene from all the possible angles that you require."* — [S7 01:30]

His stated method with a manual rig: *"start on the wall and start capturing the adjacent wall, and
basically again mentally keeping track of what images I have taken in a scene and visualizing how paint
from that perspective would fall on it, and then continuing to fill in the gaps as you go along"*
[S7 05:08].

Mechanism: reconstruction quality is a coverage problem before it is a hardware problem. Surfaces you
never pointed a lens at get invented. The paint metaphor makes an abstract sampling requirement into
something a person can track in their head while moving.

### Pattern 20 — Use the guided tool to build the intuition, then take it to the good camera

> *"The best practices on how to go about capturing the environment is out of scope for this particular
> video, but I'd encourage you to use something like [a real-time guided capture app] to build that
> intuition... so you get that augmented reality guidance there to know how you need to sample a scene,
> and then apply that to a DSLR."* — [S7 04:24]

Mechanism: a phone app with real-time coverage feedback is a **training instrument**, not just a lower
tier. It teaches the sampling pattern through immediate feedback; the DSLR then executes the learned
pattern at higher quality with no feedback at all. Deliberate practice on the cheap instrument, delivery
on the expensive one — the transferable shape here has nothing to do with 3D.

### Pattern 21 — Match the capture instrument to the reuse profile, not the quality ceiling

His stated decision rule [S7 11:40–13:09], compressed: if the camera also has to do other jobs
(shooting video, stills) and capture is occasional, a DSLR with a cheap wide lens is right — *"you don't
even need to worry about buying fancy glass because you're going to stop this thing down to f5 or f7
anyway... a $400, $500 lens on your existing camera body will get you started."* If you're capturing
spaces repeatedly and professionally, a dedicated rig with real-time feedback wins on **time**, not
image quality — *"you'll get real time feedback as you go about scanning... It'll tell you to slow
down, if you're moving too fast."*

Mechanism: he prices the decision in *predictability and time per capture*, not in resolution. The
constraint on repeated capture work is re-shoots and processing failures, and feedback during capture is
what kills those.

### Pattern 22 — Register and train are separate steps; use the best tool for each

> *"You figure out the pose or the 3D registration of the imagery and then export that into [the
> trainer]... That gives you the best of both worlds, because it's way faster at figuring out the 3D
> location of the images."* — [S7 05:31]

Mechanism: **solving where the cameras were** and **building the representation** are different problems
with different best-in-class tools. Anyone treating the pipeline as one monolithic "make me a 3D thing"
button leaves both quality and hours on the table. Generalizes to any multi-stage generative pipeline:
find the stage boundaries, and route each stage independently.

---

## Group F — Operating the models

### Pattern 23 — Route by task class, not by leaderboard

He is blunt that the best model overall is rarely the best model for a job. On one multimodal model:
*"[it] is just not that good at text-to-video or image-to-video"* — and then, in the same breath, what it
*is* for: *"where [it] does excel right now is visual effects and editing"* [S4 07:13].

His routing frame is the giveaway: he sorts by **which craft role's job this is**. *"The kind of tasks
that you would give to a visual effects compositing artist to do in Nuke or DaVinci Resolve or even
After Effects, those are the kind of things that I would lean on [it] for"* [S4 09:13]. Explicitly:
*"literally, [it] is sort of like a visual effects After Effects replacement. That's kind of how I've
been thinking about it"* [S4 08:27].

Task classes he names, with the traditional-craft equivalent: object addition and removal · crowd
reduction (*"make it have less people in it"*) · character/subject replacement · motion graphics on a
tracked surface · rotoscope-free occlusion repair · material and liquid changes [S4 08:49–09:56].

Mechanism: leaderboards rank *beauty on a generic sample*. Production needs *reliability on a specific
operation*. Naming the operation in the vocabulary of the department that used to do it gives you a
routing key that survives model turnover — the departments don't change, the models do.

### Pattern 24 — Previz cheap, finish expensive

> *"Right now these real-time video models are roughly a version or two behind the offline video models...
> But the fact that we've got interactivity here lets you frame a certain type of shot that you want, and
> then you can always upscale it in some of these other models."* — [S6 06:24]

And the same ladder against traditional tools: *"If I want to get a sense of what something looks like
before I do it the right way in Maya or Unreal Engine, [the interactive model] is incredible"* [S3 15:34].

Mechanism: **framing and finishing are different jobs with opposite requirements.** Framing wants
interactivity, latency and cheapness — you're making dozens of decisions. Finishing wants quality and
determinism — you're making one. Using a finishing tool to explore is how you burn a budget on
exploration; using an exploration tool to deliver is how you ship something soft.

### Pattern 25 — Chain the last frame

> *"One cool sort of interim hack... you can run a generation and then take the last frame and use that
> as conditioning for the next generation — kind of like your pseudo world extension."*
> — Genie 3 product manager, on [S5 17:08], surfaced by Sidhu's questioning

Mechanism: a duration limit is often a *context* limit rather than a hard wall. The last frame is a
compressed state handoff. Simple, and it works wherever a model accepts an image condition.

### Pattern 26 — Reroll, and don't conclude from one failure

> *"There is a lot to be said for re-rolling the prompt. If you're not getting the expected behavior,
> definitely try to reroll."* — [S5 01:09]

Reinforced by the research lead in the same session: *"don't think that because you prompted it one way
and it didn't work that that's all that's possible. If you persist with prompting, there's actually some
surprising things that can happen"* [S5 14:35].

Mechanism: with a stochastic generator, a single failure carries almost no information about capability.
Distinguish *the model can't* from *this draw didn't* — they demand opposite responses (redesign the
approach vs. press the button again), and confusing them is how people abandon working techniques.

### Pattern 27 — Probe for emergent affordances

His practice, repeatedly: construct a scene that *tests whether an unprogrammed relationship holds*. His
example — a first-person world with a GPS minimap held in frame: *"the top-down view and the perspective
view is perfectly synchronized as I was going through the world. It blew my mind that that actually
worked"* [S5 08:23]. Also observed: a second racing car appearing unprompted because the data
distribution implied one [S5 09:49].

Mechanism: models trained on enough of the world acquire relationships nobody specified. Those are free
capability if you go looking, and they are only found by **designing a probe** — a scene whose payoff
depends on the untested relationship. This is a research habit doing creative work: form the hypothesis,
build the minimal scene that would falsify it, run it.

---

## Signature moves (short list)

1. **Scribble the trajectory** — draw the camera path on a plan/screenshot of the actual location; hand
   the annotated image to the model instead of describing the move.
2. **Greybox first, reskin second** — kitbash → grey render → prompt only materials, skybox and key light.
3. **Freeze the set before the takes** — any location appearing more than once gets converted to a
   persistent asset before shot one.
4. **Ground truth render** — produce the same camera move in something deterministic; grade the
   generation against it instead of eyeballing.
5. **Retrieve the place** — supply actual reference views along the path rather than trusting model recall.
6. **Name the department** — route the shot by which traditional craft role's job it is, not by which
   model is winning this month.
7. **Paint the scene** — capture coverage tracked as paint falling on surfaces; fill the gaps before leaving.
8. **Ask the model to draw its own arrows** — have it place the control annotation, inspect the plan, then
   have it obey the plan.

---

## Quality rubric — how he separates good from bad

Distilled from what he praises and what he dismisses across the corpus.

**Fails:**
- The output is a draw, not a decision. *"You're still hitting the generate button, waiting for the model
  to come back with something that you hope is close to what you want"* [S2 00:01].
- The camera did something other than what was wanted, and there was no artifact that specified what was
  wanted. Nothing to point at means nothing to fix.
- The same location reads as a different place between shots — the set was never frozen (Pattern 4).
- The pipeline is a node graph and the composition decisions are happening inside it (Pattern 2).
- Real place, model memory. Approximate where the deliverable needed accurate (Pattern 14).
- Text prompt doing spatial work. If the instruction contains "then... then... toward...", it wanted to
  be a drawing (Pattern 10).
- Blocking and look entangled — a look change breaks the camera move (Pattern 6).

**Passes:**
- You could look at something before rendering that told you it was right.
- Every persistent element exists once and is referenced, not re-described.
- The generative layer is buying exactly what 3D is expensive at, and holding nothing 3D is cheap at.
- A wrong result can be traced to a specific artifact and that artifact can be edited.
- Scaffolding was planned for removal, not discovered in the render.
- The reference is retrieved and specific, not remembered and generic.

**What he actually says out loud when something is good:** he names the *physical phenomenon*, not the
vibe — caustics, god rays, plankton, ground fog, aurora, shadow catching, the reflection in the back,
the refraction holding up while an object rotates [S1; S4 09:13; S5 02:16; S6 01:14]. Praise at the level
of "looks amazing" appears nowhere.

---

## Anti-patterns (his explicit dismissals)

- **Convoluted text prompts for spatial intent** — *"who the hell wants to sit there and type a convoluted
  text prompt"* [S4 03:17].
- **Templates as a production strategy** — good for memes and short form, and *"the moment you start
  talking about doing something that's longer than 3 to 5 minutes, it gets really exhausting"* [S2 06:21].
- **Calling plumbing filmmaking** [S2 01:36].
- **Slot-machine acceptance** — treating an unpredictable generator as if it were a set [S3 15:34].
- **Tribal explicit-vs-implicit arguments** — he takes neither side and routes per shot [S3 09:48, 16:24].
- **Building scaffolding around a model's current limitations as your whole value** — *"every time we've
  seen startups that were building scaffolding around limitations of a certain model, the next iteration
  of the model just swallowed those startups up"* [S3 14:29]. Applies to workflows as much as companies:
  the method has to be about spatial control, not about this quarter's workaround.

---

## Voice profile (for channelling, not for imitation in Farrice's work)

- Opens on the concrete artifact, then generalizes. Never opens on theory.
- Shows the failure inside the win: *"Not perfectly, it hallucinated, but damn was it close"* [S4 00:02].
- Technically precise about mechanism, casual in register — "kitbashing," "greybox," "frustum," "spatial
  RAG," "register the imagery" sit next to "holy crap," "the homie," "yo."
- Credits other creators by name constantly; a large share of [S4] is other people's work presented as the
  point.
- Marks his own speculation as speculation: *"I don't think what Google showed today is doing this under
  the hood, but I suspect this is where it will go next"* [S6 04:59].
- States positions as positions: *"I would posit," "that's my take," "here's how I actually think about
  what's happening," "where I net out."*
- Self-aware about rhetoric: *"Maybe I was a little spicy at the start, but you know, you kind of have to
  do that for these type of videos"* [S2 10:14].

---

## Source key

| Key | Source | Date | Type |
|---|---|---|---|
| S1 | *"Video-to-video AI combined with 3D tools…"* — the greybox→reskin post (X `1876446735155015781`; full verbatim text recovered from the LinkedIn mirror `activity-7282893121984634883`) | 2025-01-06 (X timestamp 2025-01-07T01:52Z) | Post + demo video |
| S2 | *Nodes Aren't the Future of AI Creation. Here's What Is.* — YouTube `-k87m_sdhRI`, 11:43 | 2026-02-18 | Video essay |
| S3 | *World Models vs Game Engines: Who Wins?* — YouTube `iqSx2Xw7yQE`, 17:44 | 2026-02-13 | Video essay |
| S4 | *I Accidentally Started an AI Video Trend* — YouTube `ZfqLUVLRTj8`, 14:27 | 2026-06-05 | Video essay + demo |
| S5 | *I Tested Google's Genie 3… AI Game Engines Are HERE!* — YouTube `lALGud1Ynhc`, 23:52 | 2026-01-29 | Hands-on + interview |
| S6 | *Google Just Turned Street View Into a Video Game* — YouTube `bxv4IkobUPI`, 7:40 | 2026-05-19 | Hands-on |
| S7 | *The Most Realistic Way to Capture the World in 3D (Phone to Pro)* — YouTube `ctraRclNiZA`, 14:01 | 2026-01-23 | Tutorial |
| S8 | Maven — *Generative AI Creation Masterclass* course page (course retired) | 2024 cohort; page read 2026-08-02 | Curriculum + bio |
| S9 | TED speaker page — Bilawal Sidhu | read 2026-08-02 | Bio |
| S10 | *Map the World* Substack — spatialintelligence.ai | read 2026-08-02 | Publication |

Transcript quotes are from auto-generated captions reflowed from overlapping caption lines; wording is
faithful, punctuation is editorial. Timestamps are the caption timestamp of the passage's start.
