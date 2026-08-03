# Workflow 01 — Pre-Production Package

**Produces:** the document that exists *before* any generator opens — story spine, tension map,
shot list, a **reference-asset manifest** (which identity assets must be built, at what quality,
and which shot consumes each), and a generation budget you can quote.

**Use when:** starting any narrative AI piece longer than one clip; a previous attempt came back
with characters that changed face, locations that changed geometry, or a scene that didn't read as
one place; or you have to tell someone what this will cost before you start.

**Load first:** `genius.md` sections A–C. This workflow is the spine of the skill.

> **Tool-independent by design.** No model, product, price or setting appears in the output. It
> specifies what has to *exist* before generation, not what to press. Anything era-bound lives in
> `references/era-bound-mechanics.md`.

---

## Step 0 — The reframe

Not *"what's my prompt for shot one?"* but:

> **"What reference assets must exist on disk so that shot 7 belongs in the same film as shot 1?"**

Ward's whole method is an answer to one observed failure: *"If you just rely to going to the AI
video tools alone, you're going to see that there's just some severe lapses in continuity."*
[FILM26] 08:22. Continuity is something you *build*, in advance, as files.

## Step 1 — Idea, logline, tension shape

**Idea.** From observation, not from a generator. *"The best stories come from your own personal
experience and observations with the world."* [ANIME26] 03:16. His own worked example is a personal
place crossed with a tonal opposite — a high-speed chase set in an idyllic, slow-paced coastal town
[ANIME26] 01:36–01:55. If the input has no personal or observed seed, say so and propose where one
could come from; don't paper over it.

**Logline.** One sentence carrying **who** and **what the conflict is** — *"a simple sentence that
explains what your core idea is all about. It will give information about who the characters are and
what the conflict is."* [FILM26] 01:01. If you can't write it, the shot list will be decoration.

**Tension shape.** Draw the felt curve of the scene *before* listing shots. He reverse-engineers his
own: *"there was a level of [tension] that it started out with, and then we alleviated it, and then
we built up the tension as the scene progressed."* [ANIME26] 03:02. Three to five beats, each named
by its emotional state, not its action.

**Treatment — decide by headcount, not by ritual.** *"If you're working on a film by yourself, you
don't have to put together a treatment… but it can be helpful if you want to involve more people in
the process."* [FILM26] 01:39–01:47. Solo → skip it and say you're skipping it. Anyone else touching
this (collaborator, client, a second agent) → write it: characters, conflict, main beats.

## Step 2 — Cast the style, on purpose

Pick a **style anchor image** and say *why* in mechanism terms, the way he does — *"kind of this
anime manga style, but then it almost had elements of oil painting in it… a pretty cool fusion of
both classical Italian style and then also the anime aesthetic"* [ANIME26] 04:24–04:36. Not
adjectives. Name the two things being fused, or the one register being held.

**IP gate, here and only here.** *"Just be sure that any images and videos that you create do not
have any third-party IP"* — because *"that is problematic if you want to monetize your film in the
future"* [FILM26] 03:06–03:15. Inspiration libraries are full of frames from actual shows. Flag any
anchor that is recognisably somebody's property. This is free to fix now and fatal to fix later.

## Step 3 — The shot list (the floor — never optional)

*"You need to at the very least have a shot list, if not a storyboard… you can keep this list inside
a simple spreadsheet. You don't have to get super complicated with it."* [FILM26] 08:13–08:37.

One row per shot. Minimum columns: **# · beat · shot idea · location · characters present ·
composition load-bearing? (Y/N) · duration intent.**

**The composition question is the column that matters** (Pattern 7). Mark **Y** when the *frame
itself* carries the story — a reveal, an eyeline that must match, geography being established, a
composition the cut depends on. Mark **N** when only the *idea* of the shot matters: *"it was the
idea of the shot and not the individual composition being exactly right that would help me to tell
this specific story."* [ANIME26] 15:47–15:53. Y-shots get boarded in Workflow 02. N-shots get
written as a coverage brief. **The drawing is optional; the list is not.**

**Order of attack.** Mark which shot you'll build **first**, and make it the easiest one: *"I think
I want to start with what I believe to be the easiest part of the entire scene"* [ANIME26]
09:21–09:27. That clip becomes the reference anchor everything harder inherits from.

## Step 4 — The reference-asset manifest

The output nobody else produces, and the reason his pipelines hold. Every persistent identity in the
piece becomes a **built asset with a quality tier and a consuming shot list**.

| Asset type | What it must contain | Why |
|---|---|---|
| **Character sheet** — one per character | Front · side · back · face close-up, plus expressions; **exactly one identity per sheet** | *"so that we can get better consistency whenever we use AI image tools to generate our scenes"* [FILM26] 05:48. A sheet with two characters in it *"would be very confusing"* [ANIME26] 07:16 |
| **Location plate — at least two angles each** | The establishing angle *and* the reverse/second angle, built before you need it | *"Environmental consistency is a real challenge… having imagery that can define what the actual environment and scene is like is just really helpful for continuity"* [ANIME26] 07:51. His own bank carried two angles of the same alley [ANIME26] 08:40–08:47 |
| **Style anchor** | The picked image from Step 2 | Rides into every subsequent generation as the style reference |
| **Voice bed — one per speaking character** | ~15 seconds per emotional register (see Workflow 03) | Cast the voice once, condition everything on it |

**Quality tier is a decision, not a default.** Reference assets get maximum quality because the cost
amortises across the whole film — *"because this is going to be an asset that we use again and again
as a character reference, we want to have maximum resolution"* [FILM26] 06:35. Shot plates get only
what the next step consumes. Stylised motion can be generated low and up-ressed in finish. Write the
tier next to each asset, with the reason.

**Every asset lists the shot numbers that consume it.** An asset nothing consumes shouldn't be built;
a shot with an unbuilt asset is where continuity will break.

## Step 5 — Budget in generations, not hours

Ward quotes films out loud: *"it took seven generations, which each generation was $3 each. And so it
was ultimately about $21 to get to where we're wanting to go, which is more or less 80 bucks per
minute."* [ANIME26] 14:51–15:02. And he refuses to pretend: *"this is not a free creative medium."*
[ANIME26] 12:14.

State the arithmetic in the abstract so it survives price changes:

> **(iterations per usable second-of-screen) × (unit cost at the chosen quality tier) × (runtime)
> + reference-asset build + finish**

Give a range, name the iteration assumption you used, and name the one variable that would move the
number most. Do **not** invent current prices — pull them from the platform at plan time.

## Step 6 — Set the iteration expectation in writing

The plan survives a bad first take only if the plan said bad takes were coming. Put both lines in
the package:

- *"You're going to get really weird results, and that's all a part of the process."* [FILM26] 07:20
- *"In the same way that it's completely normal to be on a film set and do multiple takes of a scene."*
  [ANIME26] 12:32

And the diagnosis rule that protects you from rewriting a prompt that was never the problem:
**never conclude anything about a prompt from a single output** — *"if you're only getting one output
at a time, you may think that the problem is your prompt whenever the actual problem is just you
didn't generate enough images."* [FILM26] 07:44.

## Step 7 — Lay it out where you can see it

Not a node graph. *"I actually do not prefer to utilize that workflow… because it can get messy and
slow very quickly."* [FILM26] 10:08. A flat wall: intended frame on top, delivered plate directly
beneath — *"organize the final shots below your storyboard. So it's all just in one place."*
[FILM26] 13:13. State the layout in the package so whoever executes it builds the same wall.

---

## Quality gate

- [ ] Logline is one sentence and carries both **who** and **the conflict**
- [ ] Tension shape is named in emotional states, not actions, before any shot is listed
- [ ] Treatment decision is explicit and justified by headcount
- [ ] Style anchor is described as a mechanism/fusion, not adjectives, and passed the IP gate
- [ ] Shot list exists, and **every** row carries a composition-load-bearing Y/N call
- [ ] The first shot to build is named and is the easiest beat in the scene
- [ ] Every character has a sheet spec; every location has **≥2 angles**; every speaking character has a voice bed
- [ ] Every reference asset carries a quality tier **with its reason**, and the shot numbers that consume it
- [ ] Budget is stated as iterations × unit cost × runtime, with the assumption named and no invented prices
- [ ] No model name, product name, price or setting anywhere in the output

**Execution prompt:** `references/prompts-v2/preproduction-package.md` — honor its Output Contract.
