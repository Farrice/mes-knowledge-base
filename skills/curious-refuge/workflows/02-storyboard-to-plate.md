# Workflow 02 — Storyboard → Plate → Coverage Chain

**Produces:** a **shot conversion sheet** — per shot: board-or-brief call, the three-channel
reference assignment (composition · identity · style), the direction written in transferable camera
language, the coverage-vs-specify decision, the chaining plan, and the accept/salvage criteria the
result gets judged against.

**Use when:** the shot list exists and it's time to make pictures move; or generations keep coming
back "wrong" and nobody can say *which part* is wrong.

**Load first:** `genius.md` sections B–E.

> **Tool-independent by design.** This sheet names *which reference owns which channel* and *what
> the shot has to do*. It hands off to whatever image and motion tooling is current. Prompt syntax
> and model names live in `references/era-bound-mechanics.md` and never enter this output.

---

## Step 0 — Board it, or brief it

The honest state of the doctrine, both halves quoted:

- April 2026: *"A storyboard is a rough visual approximation of what you want the composition to look
  like… with simple sketches, it allows you to have more creative flexibility, and your brain doesn't
  get so locked in on some of the supporting details that will be found whenever you create
  photorealistic imagery."* [FILM26] 08:41–09:12
- June 2026: *"You actually don't need to do that anymore. AI tools are so intelligent now that you
  can describe what you want to see"* — because *"it was the idea of the shot and not the individual
  composition being exactly right that would help me to tell this specific story."* [ANIME26]
  09:46–09:53, 15:47

**The rule that reconciles them:**

> **Board the shot when the composition is load-bearing. Brief it when only the idea of the shot is.**

Take the Y/N call from the Workflow 01 shot list. For **Y** shots, board rough — and board rough *on
purpose*: the sketch's job is to keep your own decision-space open. A photoreal frame is an answer; a
sketch is a question. Generate photoreal too early and you start art-directing the model's accidents
(the lamp it invented, the extra it added) instead of deciding the shot.

**Note the vocabulary trap:** *dynamic* is his word for the **character sheet** (*"a dynamic
character sheet"* [ANIME26] 06:03) — many angles, many expressions. His storyboards are deliberately
the opposite: static, rough, cheap. Don't collapse the two.

## Step 1 — Assign the three channels

Every shot decomposes into three channels, and **each gets its own named reference**:

| Channel | Owned by | What drifts if unassigned |
|---|---|---|
| **Composition** | the board frame (Y shots) or the written shot idea (N shots) | framing, blocking, camera height, what's in frame |
| **Identity** | the character sheet — one sheet per character | faces, wardrobe, build, age |
| **Style** | the style anchor image | palette, render register, grade, medium |
| *(Location, where it matters)* | the location plate for that angle | geometry, architecture, time of day |

His move, verbatim: *"use the composition from image number one, which is our storyboard, and keep
the character as at character number one."* [FILM26] 11:40–11:50.

**This is the diagnostic layer.** When a result is wrong, the sheet lets you say *which channel
drifted* — and a channel that drifted is a reference-assignment problem, not an adjective problem.
Unassigned channel = model-chosen = drift you didn't authorise.

## Step 2 — Write the direction in transferable language

Write each shot the way it would survive being handed to a human crew, a generator, or a 3D scene:
**camera behaviour · subject action · light source and direction · what stays out of frame.**

His house ordering for motion is **CCR — camera, character, rig**: *"we always like using the CCR
method here at Curious Refuge. That's camera, character, and then rig."* [CINE26] 13:12–13:16.

Two reasons to write it this way rather than in adjectives:

1. Constraints are direction too. His own prompt closes by pinning the camera down: *"the camera
   stays on the man. We don't want the camera to be moving around the scene."* [VOICE26] 03:12–03:17.
2. It's forward-compatible. *"The future of AI filmmaking is very much going to be a 3D informed
   process"* [CINE26] 07:45 — and in a world-model tool he **places** the camera (position, focal
   length, aspect) rather than describing it [CINE26] 03:32–03:48. Blocking, focal length, eyeline
   and camera position transfer to that lane. Adjectives don't.

## Step 3 — Specify, or brief for coverage

*"You could break down shot by shot exactly what you want to see, or you can have the AI system give
you coverage that will help you to tell the overall story that you're looking to tell."* [ANIME26]
11:01–11:12.

- **Specify** (shot-by-shot) when composition is load-bearing, when an eyeline or geography has to
  match, or when the beat is the point of the scene.
- **Brief for coverage** when you want a *sequence* — a place established, a mood held, cuts you
  don't need to author. Write it as a scene brief with an explicit emotional target, the way he does:
  a location, who is where, *"have multiple cuts as we see guests enjoying the hotel"*, the style
  constraint, and then the state — *"he's at peace. So we want the entire vibe to be very very
  tranquil."* [ANIME26] 11:14–11:40.

Mark the choice per shot on the sheet. A film that specifies everything is slow and expensive; a film
that briefs everything has no authored frames in it.

## Step 4 — Plan the chain

Sequences hold together when the **edit carries continuity forward**, not when each shot is
individually perfect.

- Build the **easiest beat first** [ANIME26] 09:21 — it becomes the anchor.
- Cut ~15 seconds of approved footage, then feed **that cut** in as the reference for the next
  generation: *"Continue the scene using the uploaded reference footage, and keep the character of
  the woman as the woman and the man as the man."* [ANIME26] 15:28–15:34.
- Choose what the reference window carries. It's a budget: one continuous beat for **continuity**, or
  chopped context cards for **breadth** — *"you can break up those clips into 1 second chunks in that
  15 second video clip to give the AI system as much context as possible."* [ANIME26] 17:20–17:27.
  Ward expects the window to grow; the *choice* survives whatever the number becomes.

State the chain as an ordered list: which clip anchors which generation, and what the reference
window is carrying at each link.

## Step 5 — Accept, salvage, or reject

Batch first — **never judge a prompt on one output**: *"if you're only getting one output at a time,
you may think that the problem is your prompt whenever the actual problem is just you didn't generate
enough images."* [FILM26] 07:44.

Then triage at the **shot level, not the generation level**:

- **Accept** — passes the rubric checks you assigned this shot.
- **Salvage** — *"just because an entire generation fails does not mean there's not something you
  could salvage from there… go in and cut it out and use it as a select."* [ANIME26] 13:03–13:17.
  A generation with an invented tower in the background is still a keeper if *"all we really need of
  that shot is just about a half of a second."* [FILM26] 15:44. **Half a second counts.**
- **Reject and re-assign** — and name the channel that drifted, not the adjective you'll change.

Assign each shot its accept criteria in advance, drawn from the rubric in `genius.md`: identity
holds · world and time-of-day continuity · edges not over-sharpened · realism not sanded off · the
physical action reads correctly · text in frame is right · it reads high-budget.

---

## Quality gate

- [ ] Every shot carries an explicit **board-or-brief** call traceable to the composition question
- [ ] Boards, where used, are described as rough sketches — never photoreal pre-viz
- [ ] **All three channels are assigned by name** for every shot; none silently delegated
- [ ] Direction is written as camera behaviour + action + light + constraint (CCR order for motion) — no adjective-only shots
- [ ] Specify-vs-coverage is marked per shot, and coverage briefs carry an explicit emotional target
- [ ] The chain is ordered, starts from the easiest beat, and says what each reference window carries
- [ ] Batch-before-judging is stated; no shot is judged on a single output
- [ ] Every shot has accept criteria assigned in advance, and a salvage instruction
- [ ] Rejections name the drifting **channel**, not a prompt tweak
- [ ] No model name, product name, price, resolution or setting anywhere in the output

**Execution prompt:** `references/prompts-v2/shot-conversion-sheet.md` — honor its Output Contract.
