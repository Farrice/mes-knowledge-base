---
name: nick-st-pierre
description: "Generative-image ART DIRECTION as a discipline — the pre-generation layer, model-agnostic. Nick St. Pierre's method: layered construction (decide one layer at a time, lock the winner, then add the next), systematic aesthetic sweeps instead of rerolling (fixed control prompt, one variable moved, seed held), style-code library thinking (curated film-stock/lighting pairings, named looks, palettes, brand shorthand), reference-over-adjective direction (text carries medium/subject/environment; style and character move to images and moodboards), image-as-substrate (every still is a seed for a character, a style, a composite or a first frame), and contrast as the anti-slop lever. Use for: art directing an image or campaign before any generation, running an aesthetic sweep or look exploration, building or extending a style bank, writing a direction brief, diagnosing why a generation looks like AI slop, locking a character or a look across a set, or turning a vague visual idea into a specified frame. Trigger phrases: art direct this, direct the image, aesthetic sweep, look exploration, style bank, style codes, moodboard direction, lock the look, why does this look AI, image direction brief, additive prompting, layer this up, sweep the variable, cast the character."
---

# Nick St. Pierre — Image Art Direction

> **What this skill is for.** Not tool operation — the house already owns that
> (`banana-pro-director`, `gpt-image-2-director`, `tao-prompts-ai-video`). This is the layer
> *above*: deciding what the frame is, in what order, and how you know a version is better rather
> than merely different. It is model-agnostic on purpose.
>
> **Fidelity boundary.** Everything here is durable direction craft, validated against his
> 2025–2026 statements and prompts. Every Midjourney parameter, slot syntax and version-specific
> trick lives in `references/era-bound-mechanics.md` — dated, quarantined, "verify before use."
> Sources and dates: `references/source-notes.md`. Judgment and taste heuristics: `genius.md`.

---

## THE PREMISE

Two people with identical tools produce wildly different work. St. Pierre's whole practice is an
attempt to make that delta **legible and repeatable** rather than mysterious:

> "The delta between the AI content you typically see on X and what a true storyteller like Darren
> Aronofsky manages to produce with the same tools is truly insane." (2026-01-29)

The delta is direction. Direction is a **sequence of controlled decisions** made before and
between generations. Prompting is only where those decisions get typed.

**The one rule that generates all the others:** a result you cannot attribute to a decision is a
result you cannot repeat. So structure the work so that every difference has a cause.

---

## THE FIVE PILLARS

### Pillar 1 — Layered construction

Build the frame one decision-layer at a time. Hold everything above constant, decide the current
layer, **lock the winner**, then add the next layer. His own words on why the framework exists
(2023-03-02): *"to better understand the impact & interplay of variables in my prompts on the
overall composition of my images."*

**The layer ladder** (the order he actually worked in, Feb 2023 series, and the order that still
holds because it runs foundation → styling → mood):

| # | Layer | The decision |
|---|---|---|
| 0 | **Medium & subject** | What kind of image is this, of what? Keep it generic here — you are setting the stage, not detailing it. |
| 1 | **Emulsion / grade** | Film stock or rendering register. Sets colour science, grain, contrast, latitude before anything else. |
| 2 | **Light** | Source, direction, quality, time of day, weather. |
| 3 | **Shot & camera position** | Framing, angle, subject position in frame, lens behaviour. |
| 4 | **Wardrobe, colour, material** | What the subject is made of and wearing; palette. |
| 5 | **Atmosphere** | Particulate and air — mist, fog, steam, smoke, haze — with density chosen deliberately. |
| 6 | **Setting & time** | Where, and when in the day. |
| 7 | **Mood close** | One or two descriptors at the end. Never more. |

*"We'll be working our way up to more complex scenes as we go."* (2023-02-05)

**Lock the winner is not optional.** Mid-sweep, 2023-02-07: *"I liked Gucci and stuck with that
one as I started playing with the outfit."* Each layer inherits every decision above it. This is
what turns an exponential space (960 combinations) into a linear one (23 decisions).

**The modern construction order** — his own v6-era restatement (2023-12-30), which is the version
to use on any current model:

1. **Set the main scene.** *"Start w/ your basic idea. When possible, use generic representations
   of your subjects + a few scene details as needed. Avoid being overly specific here (think
   high-level)."*
2. **Describe the details.** *"Time to get specific… materials, ethnicity, age, clothing, colors,
   textures, shapes, hairstyles, emotions."* With multiple subjects: *"specify the position (left,
   right, middle) of the subject you're detailing & reference the same terminology used in your
   initial setup."*
3. **Describe the location.** *"prompts w/ many specific details about multiple subjects may get
   muddied by a very detailed setting description… If things get crazy, remove some of the
   specifics."*
4. **Explore styles & mediums.** *"This is your chance to set the vibe!!"* Medium goes at the
   start or the end. Be specific.

**Write it as sentences, not keyword salad.** Under *Things to avoid* (2023-12-30): *"Prompts that
are just comma-separated keywords."* Under *Ways to troubleshoot*: *"Play with your syntax/order ·
Remove 'vibey' terminology · Leverage position & repetition · Use more conversational phrasing."*

**The reduced spine, for when references carry the style** (2024-03-21):

```
{medium} of a {subject} {action/state of being} in a {setting/environment}.
The scene is {adjectives for mood/atmosphere}, emphasizing {specific elements/features}.
The {lighting} and {colors} palette adds to the {mood/theme}.
```

### Pillar 2 — Systematic aesthetic sweeps (not rerolling)

A sweep is a controlled experiment. A reroll is a coin flip.

**The protocol:**
1. Write a **control prompt** and freeze it. *"For easy comparison, all images in this thread are
   [street style] photo of [a woman], shot on [Film Type]."* (2023-02-04)
2. Move **exactly one slot**. *"It also helps to have simple prompts where you only change a
   single, specific variable."* (2023-02-08)
3. **Fix the random state** (seed, or the same reference) so the difference is the variable and
   not the dice.
4. Generate the full set **before judging any of it.** You are reading a response curve, not
   hunting a keeper.
5. **Announce every deviation.** *"I'll note when changes are made to this prompt."* (2023-02-06)
6. **Decide, lock, and write the winner into the bank** (Pillar 3). Then next layer.

**Sweep sizes that work:** 4–8 values per variable in a first pass; 2–3 finalists side by side for
the decision. He explicitly liked the two-up: *"finish off with some examples using the same
lighting (Off-Camera Flash), this time with 2 different film styles. I love this side-by-side
view."* (2023-02-05)

**When you genuinely want randomness, do it on purpose and at volume** — random style references
in big batches to *"explore style space 24x faster"* (2026-06-25). That is exploration, a separate
act from a sweep. Never confuse the two.

### Pillar 3 — Style-code library thinking

The point of a sweep is to leave behind **named, reusable looks**. Curation is the deliverable.

**Curated pairings.** He published film-stock ↔ lighting-condition pairings as matched sets
(2024-01-28: *"You can elevate pretty much any photo prompt by including a film stock with
complementary lighting conditions. I curated some pairings you can play with"*). Verbatim,
his eleven — this is real photographic vocabulary and transfers to any model:

| Stock | Paired condition | His prompt (abridged) |
|---|---|---|
| Cinestill 800T | night / mist / moody, soft | "Frogs on lily pads in a misty pond at night. Moody ambiance and soft lighting" |
| Cinestill 800T | window light, introspective | "A subject near a window in a reflective mood. Natural light and a soft, introspective feel" |
| Lomography Color Negative 800 | natural light, warm skin | "Close-up intimate portrait in natural light. Warm skin tones with a soft, dreamy quality" |
| Kodak T-Max P3200 | moonlight / dim, fine detail | "An owl perched on a tree branch, illuminated by the soft glow of the moon. Dimly lit scene with fine details" |
| Kodak Portra 800 | candlelight, deep shadow | "lit only by candlelight, creating deep shadows on their face. Warm tones and nuanced lighting" |
| Kodak Gold 200 | night flash, stark contrast | "An outdoor portrait at night using flash. Stark contrast between the subject and the dark background" |
| Polaroid Originals Color | daylight street, vintage | "Street style photo of a person on their daily commute through the city. Unique vintage effect" |
| Ilford Pan F Plus 50 | hard directional beam, fine grain | "waves crashing against rocks at night, illuminated by a lighthouse beam. A powerful scene" |
| Kodak Ektachrome E100 | dawn, somber, fine grain | "A soldier in uniform at dawn, the early light creating a somber mood highlighting the soldier's face" |
| Fuji Neopan Acros 100 | fog + single source, high contrast | "A lone figure walking down a foggy forest path, illuminated by a single light source. High contrast… mysterious atmosphere" |
| Fuji Provia 100F | daylight, vivid colour, fine grain | "Diverse textures and colors of a botanical garden… vivid color and fine grain" |

Note the **prompt shape** he uses for these: *scene sentence. Mood-and-light sentence, captured on
[stock].* Two sentences. No buzzwords.

**Personal codes.** Words he keeps because he knows what they do: *"I use 'mezzotint' in my prompts
a lot for deeper blacks."* (2024-01-30). A style bank is partly private vocabulary — terms whose
effect you have measured.

**Brand and design-movement shorthand.** *"Brand references like 'Pottery Barn' help define
style"* / *"Use specific design references like 'Scandinavian Bedroom' to help define the look"*
(2023-02-23). A well-known house style is a dense, decomposable compression — unlike an artist's
name, which he refuses (2024-03-21: *"I don't use artist names in my prompts. Never have."*).

**Palettes as direction.** He treats brand colour as a first-class control (2024-02-14, on
prompting against your own branded palettes). In the layered build, palette is a layer, not a
garnish.

**What goes in the bank, per entry:** name · what it does in one line · the exact prompt fragment
or reference image · the conditions it needs to work · what it is *not* for. Undated entries rot;
date them.

### Pillar 4 — Reference over adjective (the current centre of gravity)

His strongest and most recent statement of doctrine (2025-12-04) — read it whole in `genius.md`:

> "Visual preference isn't linguistic. We just see it and we know. **The eye knows what the mouth
> cannot say.** … The craft won't (and shouldn't) be about finding the right adjectives. It'll be
> **a collection of choices that shape your preferences and refine your tastes until the tool
> thinks like you do.**"

**Operationally:**
- **Text carries `{medium} {subject} {environment}`.** Style, character and palette move to
  images: references, moodboards, personalization, locked characters (2024-03-21).
- **The direction session's real output is the reference set**, not the prompt string. Prompts are
  disposable; the bank compounds.
- **Never judge a model — or your own work — on bare text-to-image output.** (2026-02-20: *"this
  is also a base model comparison, no style references, parameters, moodboards, etc, which all
  provide additional aesthetic control."*) That measures defaults, not direction.
- **A moodboard argues one direction.** It is an instrument of control, not a collage of maybes.

### Pillar 5 — Image as substrate

Every still is potentially a seed. Direct accordingly.

- **Cast, then shoot.** *"I'm currently in the process of casting some new models"* (2023-02-19).
  Lock a face first; then change **one variable class per shot** — wardrobe, camera, light, or
  location. *"I've found models that have a more unique/distinct look are more likely to result in
  consistent results"* — so cast **against the average** when you need consistency.
- **Composite direction.** *"if I combine my Character Prompt + Interior Prompt, I end up with a
  Cinematic Shot"* (2023-02-26). Banked prompt-objects compose. Build a character library and a
  set library and the shots fall out of the intersection.
- **Strip when references carry the load.** *"I removed a lot of variables… only keeping the shot
  type, subject, pose, location style, lighting, and descriptors. **The images fill in the
  rest.**"* (2023-02-26)
- **Blending physics that still bite:** source lighting must match across references, and you
  inherit the perspective of your sources (2023-02-26).
- **Motion is downstream of the frame.** *"Everything in this video was generated from a single
  frame, directing the character into different scenes over time with extensions"* (2025-06-25);
  a shot built from *"a sequence of six prompts"* (2025-06-23). Direct the still like a first
  frame, because it is one.

---

## THE ANTI-SLOP RULES

**1. Contrast is the lever.** (2024-01-30)

> "High contrast prompts always lead to such sick results… Contrast in lighting, colors, textures,
> art styles, genres, film stocks, perspective, etc. Lean into the contrast, see where it takes
> you."

Slop is the absence of tension — every element agreeing with every other element. Before
generating, name at least one deliberate collision: two of {light, palette, texture, medium,
genre, era, stock, perspective, subculture, scale}. His worked example stacked seven.

**2. Never name a quality; name its physical cause.** *"Adding in 'Cinematic Shot' doesn't seem to
hurt"* — but *"I've found aspect ratio and lighting to be the true drivers of cinematic looks"*
(2023-02-26). Frame shape and light do the work. "Luxurious" is weak; marble, brass, velvet, jewel
tones and a chandelier are strong.

**3. Banned: quality-assertion buzzwords and artist names.** *"Style buzzwords like 8k, vray, HDR,
etc"* (2023-12-30); *"Remove 'vibey' terminology"*; *"I don't use artist names in my prompts.
Never have"* (2024-03-21). They are undecomposable — you cannot sweep them, explain them, or bank
them.

**4. Pay the compensating token.** A direction word states intent; a second concrete token gives
the model what it needs to execute (all 2023-02-06):
- medium shot → add body language (`sitting`, `walking`, `texting`) or you get a medium close-up
- low/high angle → add `from below` / `from above`
- wide shot → *"add context for what's going on in the background"*
- emotion → be specific: *"more descriptive words like [overjoyed] produce better results than
  [happy]"*
- subject placement → `center view` / `side view`

**5. Triangulate an overloaded idea ("Combo Commands").** *"my term for using multiple variations
of a single idea to help Midjourney understand the intention of key phrases"* (2023-02-10). Say
the idea two or three neighbouring ways; the intended sense is the intersection. Benefits he
names: more consistent outputs, and colour assignment *"with minimal impact on other items in your
scene."*

**6. Resolve atmosphere physically.** Mist, fog, steam, smoke and haze differ in particle size,
density and visibility — *"Midjourney also does a pretty good job distinguishing between particle
sizes of similar conditions such as 'Misty' and 'Steamy'"* (2023-02-10). Same for light, where he
names three stackable approaches: **time of day** · **weather condition** · **light position**
(backlight, side light).

**7. Spend the specificity budget deliberately.** Three specific objects is his working ceiling
(*"I try to limit myself to 3 max"*, 2023-02-23); detailed subjects fight a detailed setting
(*"If things get crazy, remove some of the specifics"*, 2023-12-30). But never omit material —
*"It's important to include at least 1 or 2 texture references like metal, linen, wood, etc."*

**8. Know the failure envelope before you grind.** Faces degrade with camera distance
(2023-02-12). Blends inherit source perspective (2023-02-26). Some outputs come back soft and need
an upscale (2023-02-23). When you hit a known limit, **change the lever, don't reroll.**

---

## THE CRITIQUE PASS

Ten checks, in order, from `genius.md` — run them on any generation before it ships:

1. Is one variable responsible for the difference? (Else the comparison teaches nothing.)
2. Did the framing actually arrive, or is a compensating token missing?
3. What is in tension here? If nothing — it will read as slop however clean it is.
4. Is the light **named and placed** (source, direction, quality, time), or just "beautiful"?
5. Any quality-assertions or artist names? Replace with physical causes.
6. Are materials and textures stated? At least one or two.
7. Is the specificity budget over-spent — more than ~3 specific objects, or setting fighting
   subject?
8. Is the shot asking for face fidelity at a distance the model cannot hold?
9. Can this become a seed — clean, distinctive, consistent enough to anchor a character, a style,
   or a first frame?
10. **Would this have looked the same without me?** If yes, no direction happened.

---

## WORKFLOWS

| Workflow | Deliverable |
|---|---|
| `workflows/01-aesthetic-sweep.md` | A sweep plan and a decided look — control prompt, variable ladder, generation grid, side-by-side verdict, banked winner |
| `workflows/02-additive-prompt-build.md` | A fully constructed image direction, layer by layer, ending in a model-ready prompt + reference plan |
| `workflows/03-style-code-bank.md` | A named, dated style-code bank entry set — reusable looks with conditions and anti-conditions |

## EXECUTION PROMPTS

- `references/prompts-v2/01-aesthetic-sweep-plan.md` — the sweep plan and decision record
- `references/prompts-v2/02-image-direction-brief.md` — the layered direction brief and final prompt
- `references/prompts-v2/03-style-code-bank-entry.md` — style-bank entries from a completed sweep
- `references/prompts-v2/04-slop-diagnostic.md` — why this reads as AI, and the specific re-direction

## HANDOFFS (options, never a pipeline)

Direction decided here hands to the operators: `banana-pro-director` (photoreal people, character
locks), `gpt-image-2-director`, `tao-prompts-ai-video` / `pj-accetturo-ai-video` (motion),
`creative-direction` (`/mood-board`, `/art-direct`), `fantastic-posters` (catalogue styles).
**This skill decides; those skills operate.**

⚠️ **Values flag:** St. Pierre ran a sustained public campaign against Higgsfield in Feb 2026
(see `references/source-notes.md`, flag 7). The house router sends photoreal people to Higgsfield
Soul. Loading this expert and routing there is a knowing choice, not an oversight.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

4 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Nick St. Pierre — Aesthetic Sweep Plan & Decision Record** — `skills/nick-st-pierre/references/prompts-v2/01-aesthetic-sweep-plan.md`
- **Nick St. Pierre — Layered Image Direction Brief** — `skills/nick-st-pierre/references/prompts-v2/02-image-direction-brief.md`
- **Nick St. Pierre — Style-Code Bank Entries & Pairing Table** — `skills/nick-st-pierre/references/prompts-v2/03-style-code-bank-entry.md`
- **Nick St. Pierre — AI-Slop Diagnostic & Re-Direction** — `skills/nick-st-pierre/references/prompts-v2/04-slop-diagnostic.md`

<!-- END:execution-prompts -->
