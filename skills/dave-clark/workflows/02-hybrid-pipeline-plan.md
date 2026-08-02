# Workflow 02 — Hybrid Pipeline Plan

**Produces:** a layer-by-layer production plan for a piece that has to survive real post — which layer comes
from where (camera, generator, 3D, library, hand), what must persist and how it's held outside the model, and
the delivery spec every layer has to hit.

**Use when:** the piece is longer than a clip, mixes live action with generated material, needs the same
character/environment/look across many shots, or has to clear a client's or platform's QC.

**Load first:** `genius.md` Part I (the 2025–26 architecture patterns). This workflow is built almost entirely
from the two most recent sources.

> **Model-independent by design.** This plan never specifies a generator. It specifies *what has to be true*
> of whatever generator is current. That is the point: the pipeline outlives the model.

---

## Step 0 — The question that reframes everything

Not *"can AI do this shot?"* but:

> **"Which layer of this shot is cheapest to get right, and from where?"** (Pattern 4)

Flat work is usually flat because someone forced plate, performance, environment, effect and grade all through
one generator. Clark's slate does the opposite — actors on set and on blue screen, generated backgrounds,
AI de-aging, hand-drawn source art, 3D-positioned cameras, *John Wick* stunt choreographers, a *Predator* VFX
supervisor. *"You don't have to use it, just like people don't have to use CGI, you don't have to use VFX."*
[FORBESLA]

## Step 1 — Decompose into layers, and source each one

For the piece (or the hero sequence), split into layers and assign a source to each. Typical set:

| Layer | Candidate sources | Decision driver |
|---|---|---|
| **Performance** | Live actor · self-acted + timbre conversion · generated | Is the *acting* — pauses, emphasis, eyeline — load-bearing? If yes it's human. (Pattern 12) |
| **Plate / subject** | Camera · generated · composited from multiple generations | Does identity have to hold across shots? |
| **Environment** | Location · blue screen + generated BG · 3D build · photogrammetry | Does the camera need to move through it repeatably? |
| **Effect** | Practical · generated · traditional VFX | Does it interact with a real object? |
| **Grade / finish** | Post | Always post. Never baked in upstream. |

Name a source for every layer. Any layer where you can't name one is where the plan will break.

## Step 2 — Identify what must persist, and put it outside the model

The single most important step. *"You can't prompt your way to the ends."* [FORBES26 2026]

List everything that has to be **identical** across more than a handful of shots — a face, a costume, a room,
a vehicle, a palette, a logo, a lighting scheme. For each one, name the **external anchor** that will hold it:

| Anchor type | What it holds | Precedent |
|---|---|---|
| **Trained/character-specific model** | Identity and style | *Hardcore 94* — character models trained on the original hand-drawn artwork [FORBES26] |
| **Layer separation** | Character vs background, so each can be held independently | *Hardcore 94* [FORBES26] |
| **3D scene** | Camera position, spatial continuity, repeatable blocking — positions fed back into image generation | *Hardcore 94* Unreal workflow [FORBES26] |
| **Locked plate / reference still** | Exact framing, exact face, exact resolution | Mask-the-fidelity-back-in (Pattern 10) |
| **Written bible / shot list** | Continuity of intent, order, coverage | Pattern 6 |
| **Custom glue code** | Getting generative tools to talk to 3D and post pipelines | *"custom workflows and Python code to make AI tools work with certain 3D products"* [NFS 2025] |

**Rule: if it has to persist and it only lives in a prompt, it will drift.** Ask a model to remember and it
will fail; hand it the answer every time and it can't. Length converts a prompting problem into an engineering
problem, and the conversion point is roughly where a clip becomes a scene.

## Step 3 — Set the delivery spec BEFORE anything is generated

None of these are recoverable downstream. Decide them now, and make every layer hit them.

- **Aspect ratio** — decided up front, not cropped to later. Extend the plate, never crop it. (Pattern 14)
- **Resolution** — including headroom for reframing and stabilisation.
- **Frame rate** — and whether you're generating high to retime. (Pattern 11)
- **Bit depth and colour space** — the studio-grade gate: *"you get something that's AI-generated to the same,
  or at least close to the same, type of color space as the live action scenes"*; 8-bit → 16-bit; clears
  Netflix/Amazon QC. [NFS 2025]
- **Gamma / working colour pipeline** — one, applied to every layer.

If any generated layer can't hit the spec at source, name the conversion step and where it happens.

## Step 4 — Provenance plan

*"In an industry built on ownership, guild rules and chain of title, a convincing image is not enough.
The frame must be explainable."* [FORBES26 2026]

Specify, before production starts:
- **What gets logged** — prompt iterations, technical settings, approvals per stage (the MUSE pattern).
- **What gets cleared** — IP conflicts flagged, cleared assets marked (the Copyright Guardian pattern).
- **What gets produced at wrap** — chain-of-title documentation.

Scale it to the stakes. A personal short needs a folder and a spreadsheet. A distributed film needs the
full trail. Either way, decide it now — provenance cannot be reconstructed afterwards.

## Step 5 — Crew and the human decisions

*"There's always going to have to be a human involved creatively."* [FORBESLA]

Name who holds each of these, even if it's all one person:
- **Direction** — the shot list and the selection.
- **Performance direction** — the read, the blocking.
- **Look** — the reference anchor and the grade.
- **Technical supervision** — the drift anchors and the delivery spec.

Promise's answer is AI-native artists paired with veteran technicians [FORBES26]. The pairing is the point:
the person who knows what a frame should look like and the person who knows how to make it survive post are
rarely the same person.

## Step 6 — Name the risks

For each layer, one line: **what breaks, and what the fallback is.** Clark is relentlessly non-defensive about
this — *"it's been a nightmare"*, *"it sucks right now"*, *"most of the stuff is bad"*. A pipeline plan with no
named failure modes is a wish.

**Execution prompt:** `references/prompts-v2/hybrid-pipeline-plan.md` — honor its Output Contract.

---

## Output shape

1. **Layer map** — every layer, its source, and why that source.
2. **Persistence register** — what must stay identical, and the external anchor holding each.
3. **Delivery spec** — aspect, resolution, frame rate, bit depth, colour space, gamma. Set once, applied to all.
4. **Provenance plan** — what's logged, what's cleared, what ships at wrap.
5. **Human decisions** — who holds direction, performance, look, technical supervision.
6. **Risk register** — per layer: what breaks, what the fallback is.

## Quality gate

- [ ] Every layer has a named source, and none defaults to "the generator" without a reason
- [ ] Every persistent element has an external anchor — nothing critical is held only in a prompt
- [ ] The delivery spec is set before generation and every layer is checked against it
- [ ] Colour space and bit depth are specified, not assumed
- [ ] The provenance plan is scaled to the actual stakes, not copy-pasted
- [ ] At least one named failure mode per layer, with a fallback
- [ ] **No generator, model version or product name is load-bearing anywhere in the plan** — if swapping the
      generator invalidates the plan, the plan is wrong
