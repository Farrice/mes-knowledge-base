# Workflow 03 — Controlled Shot Spec

**Produces:** a per-shot control specification built on the Four Building Blocks — mask, driving plate +
structural guidance, reference images, prompt — plus a generation-and-selection protocol, a
re-composite plan and a named failure prediction.

**Load first:** `genius.md` (the Four Building Blocks, patterns 15–21).

**Deploy when:** something must be added to, removed from, or replaced in existing footage or a rendered
layout · a generated element must sit in a moving plate · a character must land in a specific place in a
specific composition · "it looks pasted on" · "it works 80% and then something's always weird."

---

## The premise

> *"Remember, all you need is a black and white mask, a driving video — this is your modified plate
> combined with a ControlNet — reference images, and a detailed prompt. Once you understand these
> building blocks, a world of possibilities will open up for you."*
> — 2026-03-30, 04:04

Four **independent** axes. Every controlled shot is a decision on each one, and every failure is one of
them under-specified. Nothing here is a model choice.

| Block | Answers | Under-specified → |
|---|---|---|
| **Mask** | *Where* am I allowed to change things? | Change bleeds where it shouldn't, or freezes where it must move |
| **Driving plate + structure** | What *survives*? | Geometry drifts, camera slides, the element floats |
| **References** | What *identity/look* does the new content carry? | Wrong look, wrong character, unintended bias |
| **Prompt** | What is *happening*? | The model invents subject or motion you never asked for |

---

## Step 1 — Shot intent, in one sentence

What changes, and what must not. Both halves. *"Add a creature that enters frame and interacts with my
arm; my face, body and the camera move stay exactly as shot."*

If you can't say the "must not" half, you cannot draw the mask.

---

## Step 2 — The mask (WHERE)

The mask is the **primary creative control**, not a technicality. It is where the central trade-off is
spent.

**The trade, named:** identity preservation and scene integration pull against each other.
A tight mask around the new element preserves the original subject perfectly but the interaction at the
boundary — contact shadows, spill, splash, contact points — comes out weak. A mask that includes the
subject fixes the interaction and starts changing the subject. He hits exactly this and rules on it:

> *"The integration now looks much better, but I look completely different. So I think the best approach
> would be to exclude my upper body and face from the mask, but maybe add a bit of blur to the feet."*
> — 2026-03-30, 12:23

And the deliberate inverse, on a different shot:

> *"I actually included myself in the mask, because I actually wanted some of these lighting effects on
> my body."* — 17:05

Specify:
- **Region** — what's inside, what's outside, in plain language
- **Animation** — static, or moving with the element; if moving, along what path
- **Boundary treatment** — hard, or feathered where interaction matters
- **Deliberate inclusions** — anything you're putting *inside* the mask on purpose to receive light,
  shadow or contact from the new content
- **Shape check** — *the mask shape is a reference too.* A ball-shaped mask asks for a ball. If the mask
  silhouette resembles something you don't want, redraw it (Pattern 9).

---

## Step 3 — The driving plate + structural guidance (WHAT SURVIVES)

The driving plate is the original footage or layout render **modified to preserve what must survive**,
composited together with structural guidance for what gets regenerated.

Canonical construction, verified on screen (S2 02:45): the subject is preserved in full colour and
composited **on top of** structural outlines of the environment. The model then regenerates only the
guided region, and knows both what to keep and what the underlying structure is.

Choose structure per shot:

| Guidance | Locks | Choose when |
|---|---|---|
| **Edges/outlines** | Exact detail and geometry | Detail must survive intact — a building, a sign, a specific object |
| **Depth** | Spatial relationships, near/far | You want the space held but new detail invented. *"Generally a bit more flexible"* |
| **Pose** | Human articulation and rotation | A person's movement drives the shot. Also carries turn-around — a back view plus pose data keeps a replaced character consistent when it turns |
| **Tracking points** | The camera move itself | The camera moves and a generated element must sit in the world |
| **Path/trajectory** | Motion of a non-human subject | The subject isn't a person: a creature, an object, a camera, a 2D element. *"With trajectory points you can animate anything you want"* |
| **None** | Nothing | Clean plates, object removal, or when you want the model free |

**Two hard rules from source:**

1. **Don't stack every control you own.** *"I gave it the inpainting area plus the ControlNet and point
   data, but this seemed to be too much. The creature still moved along the path, but it was just an
   unanimated image sliding over the video."* Over-constraining **kills motion.** His published branch:
   *start frame + structural guidance* for natural movement, *inpainting* for best consistency — one or
   the other, and the trade is named.
2. **Structure exactly where the drift is, and nowhere else.** When the model over-ran his intent by
   inventing a camera move into an empty frame, the fix was not more prompt: *"I created Canny outlines
   for this shot and blended them only in the edges, so that the model can understand the camera
   movement."*

**The plate can be hand-authored as animation.** It is not a preprocessing artifact. Timed reveals,
progressive masking, drawn energy lines — all legitimate:

> *"First my arm turns into this black area with the open pose ControlNet, then it happens to my second
> arm, then it happens to my body, and then I punch the ground. A black mask quickly turns the full frame
> black… but the explosion was never big enough, so I added these white lines here that spread outwards
> in the hopes of creating this — and it actually worked kind of well."* — 2026-03-30, 17:30–17:56

If you want scale, timing or energy, **draw it into the plate.**

---

## Step 4 — References (IDENTITY)

- **Body-scale + identity-scale** as the default pair — one reference carrying geometry/proportion, one
  carrying identity at usable resolution.
- **Add a third only for an observed drift** — a specific detail that has already been seen to change.
  Snip it from the source rather than describing it.
- **Turn-around references** when the subject rotates: give the back view as well as the front, or the
  far side will be invented.
- **Every reference is a vote.** Audit the set for signal you didn't intend to send — silhouette,
  colour cast, framing, mood. Two accidental votes beat every word in the prompt.
- If a locked character from Workflow 01 exists, **use it instead of references** for identity and keep
  references for look only.

---

## Step 5 — The prompt (WHAT HAPPENS)

The prompt owns **only what the other three blocks don't.** That is the whole discipline, and it makes
prompts short and specific rather than long and hopeful.

- Describe the **action and the effects**, in natural language.
- Say **where the element is at the start** of the shot — a real, sourced tip: *"it can also help to
  describe where the creature is in the beginning of the video."*
- **Do not prompt what you already control deterministically.** His own instruction to the LLM he uses
  for prompt polish is exactly this: *"Prompt-proof this video prompt. Focus on the description of
  effects like lava, fire and smoke. Do not mention the camera movement — we already have that."*
- **Negative-prompt known model reflexes** where available — e.g. models adding mouth movement to any
  face they see.
- **Prompt-format propagation:** write one gold-standard prompt in the grammar the target model wants,
  then have an LLM apply that grammar to every subsequent shot. *"This is the format. Please adapt this
  format to the next scene."* Not delegating the writing — delegating the formatting.

---

## Step 6 — Generation & selection protocol

- **Two-step preview shop.** Run cheap, low-quality passes first to choose the **take** — the motion,
  the timing, the interpretation. Only then spend the expensive pass to finish it. *"You can set the
  steps to something like two… choose the one where we like the movement, and then bump up the steps to
  the final eight and render the final shot."*
- **Seed is a variable you shop, not a nuisance you endure** — and you shop it in the cheap pass.
- **Watch it generate.** Turn on live previews. *"Often you can tell from the first step on if it's
  working or not."* Kill bad runs early rather than paying for them.
- **Long shots are authored in segments**, with per-segment intent — behaviour can change across the
  shot on purpose.
- State the **budget**: how many takes, at what cost, before you stop.

---

## Step 7 — Re-composite plan

Because the generation was structurally derived from the plate, it comes back into the plate
frame-accurately. Use that.

> *"In After Effects I actually used the original mask to blend the generated footage with the original
> footage… it's super easy, because it matches up perfectly."* — 2026-03-30, 16:09

Specify: which regions come from the original, which from the generation, which mask does the blend,
and any edge treatment. Also note where the generation **beat** the plate — his own case: the model
generated new hair detail across a bad roto edge and merged the two seamlessly, so the "bad" edge was
better left generated than fixed.

---

## Step 8 — Failure prediction & quality gate

Predict the failure **before** generating. State which of the four blocks is most likely
under-specified for this shot, and what you'll do when it shows.

**Then check:**

- [ ] Shot intent names both what changes and what must not
- [ ] Mask region, animation, boundary treatment and deliberate inclusions are all specified
- [ ] The mask **silhouette** has been checked for accidental signal
- [ ] The identity/integration trade is **named and ruled on**, not left implicit
- [ ] Exactly one structural strategy is chosen; controls are **not** stacked
- [ ] Structural guidance is placed **where the drift is**, not everywhere
- [ ] References are audited for unintended votes
- [ ] The prompt does **not** re-specify anything the mask, plate or references already control
- [ ] Selection is a **cheap pass**; quality is a separate expensive pass
- [ ] A re-composite plan exists, naming which mask does the blend
- [ ] **The integration test is specified**: shadows, contact, reflections, spill onto the original
      subject — *does the physics agree*, not "does it look cool"
- [ ] Nothing in the spec names a model, node or version

**80% is not done.** *"Each of them worked like 80% well, but there was also always something weird
going on."* 80% means an axis is still un-authored. Go back to the four blocks and find which one.

**Execution prompt:** `references/prompts-v2/shot-control-spec.md` — honor its Output Contract.
**When the problem is a recurring character rather than a shot:** `workflows/01-character-lock-dataset.md`.
