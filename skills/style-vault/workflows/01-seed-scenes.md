---
description: Turn a real ICP profile into a scene inventory — pain-state and desire-state scenes plus the fixed probe subject that anchors every later sweep
---

# 01 — Seed Scenes

**Deliverable:** a **scene inventory** — 3+ pain-state scenes, 3+ desire-state scenes, and one
**fixed probe subject**. Not prompts. Scenes. The prompt-writing happens in `02` through
St. Pierre's grammar.

**Run this when:** starting brand imagery for any brand/ICP pair that has no banked style, or
when an existing bank keeps producing images that look fine and land flat.

**Why it exists.** Every image skill in this house directs *how the frame looks*. None decides
*what is happening in it and which buyer emotion it serves*. Carter's contribution is the
bridge — he reads a brand brain into pain-based and desire-based scenes before touching style,
and states the consequence of skipping it: *"If you don't have that, you're just going to be
creating random images."*

---

## Pre-flight

**Do not interview Farrice for what is already on disk** (Partner Posture 2). Load in this order
and only ask about what genuinely isn't written down:

1. The ICP profile itself. Look for `_active/<brand>/` ICP files, then
   `python3 execution/memory_facade.py "<brand> ICP psychographics" --top 10`.
   Exemplar-grade reference: `icp-invisible-expert`.
2. `_active/farrice-brand/voice/VOICE-CARD.md` if the brand is Farrice's own.
3. Any existing vault entries for this brand: `python3 execution/style_vault.py list --brand <slug>`.

**Gate.** No ICP profile at identity level → **stop and build one first** (`icp-deep-canvasser`,
or `/ctm-*` for a customer truth map). A demographic profile produces demographic scenes.
Proceeding without one is the failure this workflow exists to prevent, and it is not
recoverable downstream by better art direction.

---

## Step 1 — Extract the two state lists

From the ICP profile, write two plain lists. Use the buyer's **researched words**, exactly — not
elevated paraphrase (binding: ICP Verbatim > Pageantry, 2026-07-30; paraphrasing a buyer's
language into elegant prose kills credibility silently).

- **Pain states** — where they are now, felt from the inside. Not problems; *states*.
- **Desire states** — not the outcome they'd name in a testimonial, but the moment they'd
  privately recognise as having arrived.

## Step 2 — Convert each state to a scene

A state is a feeling. A scene is a **physical situation a camera could be pointed at**. This
conversion is the whole craft of this workflow, and there are three rules.

**Rule 1 — A scene shows a state, not an activity.** "Working late at a laptop" is an activity;
every ICP in the world does it, so it carries nothing. "The laptop closed, still sitting at the
desk, coat still on" is a state — arrival, avoidance, or exhaustion, depending on the light.

**Rule 2 — It must read with the caption covered.** If the scene only means something once the
post explains it, the image is decoration. Cover the caption. What is the picture *about*?

**Rule 3 — Leave the negative space where the text will go.** Carter catches this in passing and
it is load-bearing: *"it starts to create nice negative space, which is really important
specifically when we're going to be adding text onto this."* Decide the text zone at the scene
stage, not in the layout. Name it: `upper-third`, `left-column`, `lower-band`, or `none`.

**Write each scene as one sentence** — subject, situation, and the one telling detail. No style
language whatsoever. Style is decided in `02`; mixing it in here means you can never tell whether
a weak result was a bad scene or a bad look.

| Field | Example shape |
|---|---|
| State served | pain: "I've done the work, nobody knows" |
| Scene | "A person alone in a lit room, work spread across the table, phone face-down and untouched" |
| Text zone | `upper-third` |
| Buyer verbatim it serves | "\<their exact words from the profile\>" |

## Step 3 — Choose the fixed probe subject

One scene from the inventory — or a neutral composite of the most *typical* one — becomes the
**probe subject** for the entire sweep in `02`.

Flynn's rule, and it voids the run if broken: *"pick one probe prompt and do not change it for
the entire sweep. Everything you learn is a difference, and a difference requires a fixed
baseline."*

Pick the scene you will produce **most often**, not the most interesting one. A probe optimised
for your rarest asset selects a style that fails on your daily work.

## Step 4 — Record it

Write the inventory to `_active/<brand>/05-assets/scene-inventory.md` (living doc — update in
place, no leading date). It is reused every time this brand needs a new style, so it is
infrastructure, not a session artifact.

---

## Output requirements

- 3+ pain scenes, 3+ desire scenes, each with state · scene sentence · text zone · buyer verbatim
- Exactly one fixed probe subject, with one line on why it is the most-produced scene
- Zero style language anywhere in the file
- A named gap list: which states had no usable verbatim in the profile

## Quality gate

1. Cover the caption on every scene — does it still mean something?
2. Is any scene an *activity* wearing a state's clothes?
3. Is the buyer's language verbatim, or has it been smoothed into your register?
4. Does the probe subject match what this brand actually ships most weeks?
5. Did any style word leak in? Cut it.

**Next:** `02-mine-and-audition.md`.
