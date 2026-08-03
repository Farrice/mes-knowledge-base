# Workflow 01 — Character Lock Dataset

**Produces:** a complete character dataset specification — image manifest, caption spec, consistency
budget, bake plan and acceptance test — that anyone (or any tool, on any stack, in any year) can
execute to produce a character that comes out the same every time.

**Load first:** `genius.md` (patterns 1–8 are the whole workflow). Tool mechanics, if anyone asks for
them, are in `references/era-bound-mechanics.md` and are **not** part of the deliverable.

**Deploy when:** a character has to appear more than once · a style/character has to survive a campaign ·
"my character keeps changing" · an anime/mascot/founder-avatar needs locking · a cast has to appear
together in the same frame.

---

## Step 0 — Is this a dataset job at all?

The Control Ladder (genius.md) has six rungs. Rung 6 — a trained character — is the expensive one and
it is not always the right one.

- **One shot, one appearance** → don't build a dataset. Rungs 1–2 (reference image + mask) are enough.
- **A handful of shots, one session, one style** → an edit-model reference chain may hold. Try it first
  and *see whether the folder holds*.
- **The character recurs across shots, weeks, styles or media** → build the dataset. This workflow.
- **The character must appear in the same frame as another locked character** → build the dataset, and
  Step 4 (group shots) is mandatory, not optional.

Say which, in one line, before proceeding. A workflow that runs when it shouldn't is a cost, not a
deliverable.

---

## Step 1 — The consistency budget (dataset rule 3, done first)

Before a single image is generated, split every property of the character into three columns. This is
the decision the whole rest of the workflow executes.

| LOCKED — must never change | VARIABLE — must be changeable later | FREE — genuinely don't care |
|---|---|---|

Rules of the split, from source:
- **LOCKED properties get held constant across the whole set and are deliberately under-captioned**, so
  they accrete onto the trigger word. That is precisely how the trigger word becomes the character.
- **VARIABLE properties must be varied in the images AND named in every caption.** Varying without
  captioning is wasted; captioning without varying is fragile. Both, or it isn't variable.
- **FREE properties cost nothing** — but be honest, because anything you leave free and un-captioned
  quietly becomes part of the character.
- The trade is stated, not hidden: *"the more detailed your caption, the more flexible you are later,
  but also the longer your prompt has to be, because you have to recall all these elements."* A large
  VARIABLE column buys flexibility and charges you a long prompt forever.

Then name the **signature details** — the small, specific, high-drift objects that make this character
*this* character rather than a type. Jewellery, a piercing, a logo, a hair ornament, a scar, a
weapon, a specific weave. These get their own treatment in Step 3 and are the first thing the
acceptance test checks.

---

## Step 2 — The image manifest

A dataset is a **model sheet plus a range test**, not a gallery. Every entry is a shot spec with its
own reason for existing.

Mandatory spine (verified on screen, S3 07:07 / 08:58, S1 05:39):

| Block | Shots | Why it's there |
|---|---|---|
| **Turnaround** | front · three-quarter · side · three-quarter-back · back — identical wardrobe, plain neutral ground | Establishes silhouette and geometry from every angle |
| **Identity** | close-up portrait, neutral, plain ground | The face at usable resolution; also the identity reference for every later generation |
| **Expression** | 4–8 emotion variants of the portrait | So expression is not welded to the trigger word |
| **Body** | T-pose (or equivalent neutral articulation) | The body-scale reference for every later generation |
| **Range** | walking · sitting · laying down · one awkward or interactive action | Rule 2 — a set of close-ups teaches a character who only exists in close-up |
| **Scale** | at least 3 genuine wide shots where the figure is small in frame | Rule 2 again, in the axis people always forget |
| **Light** | ≥3 distinctly different lighting conditions | Or the character can only exist under one lamp |
| **World** | ≥3 different environments | Or the character can only exist in one room |

If your **only** input is a close-up, everything below the frame line **will be invented**. Name it
explicitly in the generation prompt — *"wearing black loafers"*, *"wearing chunky sneakers"* — or the
model chooses for you and the choice enters the dataset.

For each entry record: **ID · what's in frame · framing/scale · pose or action · lighting · ground or
environment · which references feed it · what it exists to teach.** The last column is the test — if
an image doesn't teach anything the others don't, cut it.

---

## Step 3 — Signature-detail anchors (the detail-anchor loop)

For every signature detail from Step 1, spec a dedicated close-up sub-set: **the detail alone, the
detail on the character close-up, the detail from a second angle, the detail under different light.**

And spec the repair loop, because this is a loop, not a step:

1. Bake a test version.
2. Generate a batch. **Do not judge the batch — judge each signature detail across the batch.**
3. For any detail that drifted: **snip it out of the original input image and feed it back as an
   additional reference** on the generations that produce that detail's images (S1 07:16 — he screen-
   snips the necklace, adds it as a third reference, and the result *"looks much better and much
   closer to the original"*).
4. Add the improved detail images to the dataset. Re-bake.

The move is always the same and it is the skill's signature: **when the model is wrong, give it a
better picture, not a better adjective.**

Also spec, per image, **which prompt inputs feed it** — several of his fixes come from *removing*
inherited context, not adding it (S1 08:01: shoes kept appearing in a necklace close-up because the
general clothing prompt was still wired in; the fix was to disconnect it, not to negative-prompt it).

---

## Step 4 — Cast handling (only when >1 locked character)

Two-characters-in-one-prompt merges them. Not a settings problem — a **data** problem, and one he
spent two published pipeline generations working around before solving it with data.

Spec, in addition to each character's own manifest:

- **Group shots** — every pair, plus the full cast, **both standing together and interacting.** These
  go in the *same* dataset folder as the individual sets.
- **The cast caption rule**, verbatim from the tagger he types into (S1 18:42):
  > *"If there are multiple characters in the same image, add their trigger words and describe where
  > they are in the image and how they are interacting."*
- **The identity map** — one line per character binding a plain visual description to its trigger word,
  so the captioner never has to guess which body is which. His own, verbatim: *"the blonde woman with
  a buzzcut is [trigger], the black man with a grey turtleneck is [trigger], the woman with curly hair
  is [trigger]."*
- **Capacity scales with cast size.** More characters need more model capacity — note it as a bake
  parameter, don't guess a number here (dated observations in the appendix).

Verbatim group-shot generation prompt, read off screen at S1 18:05 — the shape to copy:

> *"The three characters are standing together in an image close up photoshoot in an evening italian
> city. On the left side the young woman with a blonde buzzcut is wearing a long leather coat. In the
> middle stands the woman with the curly hair. On the right the black man is walking toward the camera.
> Keep the characters faces and styles consistent. Do not change clothes."*

Note what it does: names each character *by visual description and position*, gives each one an
action, and closes with two explicit hold-constant instructions.

---

## Step 5 — The caption spec

This is the step everyone skips and it is the one that decides whether the character is usable.

**A caption is a reverse prompt.** Write the caption spec in the exact grammar you will later write
prompts in for the target model. Long flowing natural language, or terse tag lists, or structured
objects with regions — whichever that model wants. Mismatch here degrades everything downstream and
you will never see why.

Specify:
- **Trigger word** — unique, made-up, non-colliding with real vocabulary. It is also the folder name,
  the dataset name and the job name. One naming spine.
- **Caption grammar** — sentence style, length, ordering, whether regions/boxes are carried.
- **Always name** — every VARIABLE property from Step 1, in every caption where it appears.
- **Never name** — every LOCKED property. Silence is what welds it to the trigger word.
- **Captioning rules** — the plain-language instructions handed to whatever writes the captions
  (identity map, the cast rule, any "don't mention X" exclusions). These are instructions to a language
  model, so write them as instructions: *"Don't mention the clothes"* works, and he uses exactly that.
- **Review pass** — captions and any region data are **read and corrected by a human** before baking.
  *"I really recommend taking the time and working through these images. It really helps when
  generating images later."*

---

## Step 6 — The bake plan (stack-agnostic)

Specify only what survives a stack change:

- **Bake targets** — which model families this character must exist in (still image / precise-placement
  / video / whatever ships next). The same dataset serves all of them; note per target only whether the
  **caption grammar differs**, because that is the one thing that does.
- **Sample the curve, don't wait for the end.** Save intermediate versions on a fixed interval, generate
  test samples on the same interval, and **download several checkpoints, not the last one.** The best is
  usually in the middle; the end is usually overbaked. Judge by eye against the acceptance test.
- **Sample prompts kept deliberately simple** — *"I try to keep them as simple as possible, to really
  see what kind of qualities get attached to my trigger word."* Complex sample prompts hide the very
  thing you're checking.
- **Prune before baking.** Drop images that are weird, off-model, or near-duplicates of each other.
  *"Take some time and look through them, and the ones that look slightly weird or off, just delete
  them."*
- **Curation state before commit** — build and review in preview, and only write the real dataset folder
  once the set is what you want.

---

## Step 7 — The acceptance test (the honest-folder standard)

A character is **locked** when the whole output folder holds — not when the best frame does.

Run a batch of at least 12 fresh prompts across the range the character has to work in — different
scales, environments, lighting and actions, plus one deliberately awkward pose or angle. Then:

- [ ] **Scroll the entire folder.** Report the failures with the successes. *"This is no cherry-picking.
      These are all the images that came out of the model."*
- [ ] **Every signature detail** from Step 1 is correct in every image where it should appear. Name each
      one and check it individually — this is where drift lives.
- [ ] **The face holds at wide scale**, not only in close-up. If it doesn't, the defect is resolution,
      not identity — re-detail *only* the images where the face occupies too few pixels.
- [ ] **Every VARIABLE property actually varies on command** — change it in a prompt and confirm it
      changed.
- [ ] **Every LOCKED property survives** a prompt that doesn't mention it.
- [ ] **Multi-cast:** no bleeding, no merged features, no duplicated character in a single frame, and
      each one lands where the prompt puts them.
- [ ] **Failures are named as objects, not vibes** — "the necklace changed", "the left pupil is broken",
      "she appears twice" — each with a stated cause and fix.

Anything at "80% works but something's always weird" is **not** locked. That is the plateau where people
ship. It means an axis is still un-authored — go back to Step 1 and find which column it belongs in.

**Execution prompt:** `references/prompts-v2/character-dataset-spec.md` — honor its Output Contract.
**Drift after locking:** `workflows/03-controlled-shot-spec.md` Step 2, or the drift diagnostic prompt
`references/prompts-v2/consistency-drift-diagnostic.md`.
