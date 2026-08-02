# Workflow 02 — The Layered Build (Additive Prompting, modern form)

**Deliverable:** an *Image Direction* — the frame decided layer by layer, with each decision
stated and attributable, ending in a model-ready prompt in prose plus a reference plan (what the
text carries vs. what the images carry).

**Use when:** the look is decided (or inherited from a style bank) and the frame needs building.
"Direct this shot," "write the prompt for X," "turn this idea into a frame," "what should this
image be."

**Do NOT use when:** the aesthetic is genuinely undecided — sweep first (`01-aesthetic-sweep.md`).
Building on an undecided look means you will rebuild.

---

## Step 0 — Establish what the references already carry

Before writing a word, list every reference in play: style references, locked characters,
moodboards, palettes, banked style codes, personalization.

**The division of labour** (2024-03-21): text carries **`{medium} {subject} {environment}`**;
style, character and palette are carried by images wherever possible. *"Almost all other details
can be driven by image references now."*

**Never re-describe in text what a strong reference already shows.** When blending, he strips hard:
*"I removed a lot of variables… only keeping the shot type, subject, pose, location style,
lighting, and descriptors. The images fill in the rest."* (2023-02-26)

Write one line: **"Text carries ___. References carry ___."**

## Step 1 — Set the main scene (high-level)

*"Start w/ your basic idea. When possible, use generic representations of your subjects + a few
scene details as needed. Avoid being overly specific here (think high-level). You're simply
setting the stage."* (2023-12-30)

Also fix the **medium** now (at the start or the end of the prompt, never buried) and the **frame
shape**. Aspect ratio is a top-order decision, not a formatting afterthought — with lighting it is
one of the two *"true drivers of cinematic looks"* (2023-02-26).

## Step 2 — Decide light before you decide anything decorative

Name **source, direction, quality, time of day, weather**. Three stackable approaches
(2023-02-10): time of day · weather condition · light position (backlight, side light, rim,
split, silhouette, off-camera flash, spot, studio, natural).

Write it the way he writes it on current models (2025-11-20): *"dimly lit, with warm light from a
window on the left and the glow from the TV illuminating the creatures' faces."* **Named sources,
placed in the frame.** Never "beautiful lighting."

## Step 3 — Describe the details, with a budget

*"Time to get specific… materials, ethnicity, age, clothing, colors, textures, shapes, hairstyles,
emotions."* (2023-12-30)

Rules of the budget:
- **At least 1–2 texture/material references.** Non-negotiable (2023-02-23).
- **Roughly 3 specific objects maximum.** *"Adding too many specific furniture items can sometimes
  confuse it. I try to limit myself to 3 max."*
- **Multiple subjects need positions**: *"specify the position (left, right, middle) of the
  subject you're detailing & reference the same terminology used in your initial setup."*
  Repetition of the same noun is a feature, not a redundancy.
- **Emotions get specific words** — `overjoyed`, `heart-broken`, not `happy`, not `sad`.

## Step 4 — Pay the compensating tokens

Walk the frame and pay for each direction word (all 2023-02-06):

| You asked for | You must also supply |
|---|---|
| Medium shot | body language — `sitting`, `walking`, `texting` |
| Low angle | `from below` |
| High angle | `from above` |
| Wide / extreme wide | what is in the background |
| Emotion | a specific, non-generic emotion word |
| Subject placement | `center view` / `side view` / left / right |

## Step 5 — Set the atmosphere physically

Choose the particulate and its density on purpose: mist / fog / steam / smoke / haze differ in
particle size, density and visibility (2023-02-10). If one word is doing too much work,
**triangulate it** with a Combo Command — two or three neighbouring phrasings of the same idea so
the intended sense is their intersection.

## Step 6 — Place the setting and time; close with mood

Setting and time of day, then **one or two mood descriptors at the very end** — never a stack.
*"Adding 1 or 2 general descriptors at the [end] will help you define the look."* (2023-02-23)

Beware the muddying rule: *"prompts w/ many specific details about multiple subjects may get
muddied by a very detailed setting description… If things get crazy, remove some of the
specifics."* (2023-12-30)

## Step 7 — Add the deliberate collision

Name at least one tension you are introducing: light vs palette, texture vs subject, medium vs
content, genre vs setting, era vs subject, stock vs condition, scale vs perspective. If you cannot
name one, the frame is on the default aesthetic (2024-01-30).

## Step 8 — Write it as prose, then strip

Write in **conversational, naturally flowing sentences** — not comma-separated keywords
(2023-12-30). Then strip:

- every quality-assertion (`8k`, `HDR`, `vray`, `ultra-detailed`, bare `cinematic`)
- every artist name
- every "vibey" adjective that names a quality instead of its cause
- everything a reference image already carries

**Troubleshooting ladder if the result misses** (2023-12-30, verbatim): *"Play with your
syntax/order · Remove 'vibey' terminology · Leverage position & repetition · Use more
conversational phrasing."* Change the lever; do not reroll.

## Step 9 — Run the critique pass and state the seed potential

Run all ten checks from SKILL.md. Then answer: **what is this image a seed for?** A character
lock, a style reference, a composite half, a first frame — or nothing, in which case say so.

*Execution prompt: `references/prompts-v2/02-image-direction-brief.md` — honor its Output Contract.*

---

## Quality gate

- [ ] The text/reference division of labour is stated in one line before any prompt is written
- [ ] Medium and frame shape are decided at the top, not appended
- [ ] Light is named **and placed** (source + direction + quality + time), never "beautiful lighting"
- [ ] At least 1–2 materials/textures present; roughly ≤3 specific objects
- [ ] Every direction word has its compensating token
- [ ] One deliberate collision is named
- [ ] Prose sentences, not keyword salad; zero quality-assertions, zero artist names
- [ ] The critique pass is run and the seed potential is stated

---

## Example output (abridged)

**Text carries:** medium, subject, environment, light placement, one collision.
**References carry:** locked founder character, brand palette board, `WET-SLATE-800T` style code.

**Build log**
- L0 medium/subject — editorial portrait; founder at the loading bay of the co-packer
- L1 grade — `WET-SLATE-800T` (banked)
- L2 light — practical sodium lamp above and behind camera-right; open shade fill from the bay
  door camera-left; dusk
- L3 shot/camera — medium shot, slightly low angle, `from below`, subject `center view`, 4:5
- L4 wardrobe/material — worn canvas jacket, steel roller door, wet concrete
- L5 atmosphere — thin haze off the wet ground, low density (mist, not fog)
- L6 setting/time — industrial loading bay, dusk
- L7 mood close — grounded, unglamorous
- **Collision:** a night-tungsten grade on a subject the category always shoots in clean daylight

**Prompt**
> An editorial medium shot of a man in a worn canvas jacket standing in an industrial loading bay
> at dusk, shot slightly from below with the subject centered. A sodium lamp above and behind the
> camera on the right throws warm hard light across his shoulder; open shade from the open bay
> door fills the left side of his face. The steel roller door and wet concrete behind him hold
> the reflections, with a thin low mist coming off the ground. Captured on Cinestill 800T. The
> mood is grounded and unglamorous.

**Seed potential:** first frame for the founder-story cut; the wet-concrete plate is reusable as a
set reference.
