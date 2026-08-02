# Workflow — Photorealism Language

**Deliverable:** a **built prompt** with all nine Image Elements accounted for, a stated left-anchor
decision, a **Left-Anchor Swap ladder** (4 ordered variants), and a **finishing note** naming the
imperfection pass. Plus an explicit list of any element deliberately left to the model.

**Run this when:** the output looks like a render, a video game, a stock illustration, or "AI" — and the
instinct is to add the words *photorealistic, hyperrealistic, 8k, ultra detailed*. Those are words *about*
realism. This workflow replaces them with words *from* photography.

**Why it exists.** Flynn's diagnosis is that realism is not a dial you ask for; it is a **vocabulary you
write in**:

> "For us, typically the best way to trigger [the model] into a photorealistic mindset is to use
> photography terminology. That's what I've always found has worked the best." — [MJM @ 12:31, 2024]

The doctrine is 2024-era in origin and **has been carried forward deliberately** because it is
model-independent: it describes how generative latent spaces are organised, not how one product parses
flags. Nothing in this workflow names a model, a parameter or a syntax. Era-bound mechanics live in
`genius.md` Appendix A.

---

## Step 1 — Walk the nine non-negotiables

The list, verbatim from the Config 2026 stage [CONFIG @ 09:46, 2026]:

| Element | His gloss | Ask yourself |
|---|---|---|
| **Shot / Photo Type** | How it's captured | what genre of photograph is this? |
| **Subject + Action** | Who and what | what is happening, in verbs? |
| **Environment** | Where it is | what's actually around it? |
| **Color Scheme** | The colors | which three, and on which surfaces? |
| **Technical Details** | The aesthetic | camera, lens, film, focal behaviour |
| **Composition** | How it's constructed | framing, symmetry, crop, where the subject sits |
| **Lighting** | The tone | source, direction, quality, temperature |
| **Textures** | Surface. Depth. Feel. | what would you feel touching it? |
| **Details / Modifiers** | The subtle details | the one specific thing nobody would guess |

**The rule that makes this non-optional:**

> "Lighting is going to be represented in every photo no matter what. And when you're prompting, **if you
> don't add something like lighting, the model will provide it for you.** So if we can control these, we
> can really control everything." — [CONFIG @ 09:54, 2026]

Silence is not neutrality. Silence is delegation. Any element you skip is a slot the model fills from its
own priors — and that is precisely where drift between runs comes from.

**You may deliberately leave an element open.** Flynn does: *"you don't have to go really crazy"*
[CONFIG @ 10:31]. But it must be a *decision*, written down as one, not an oversight. The deliverable
lists them.

## Step 2 — Fill the formula

Verbatim from the same slide [CONFIG @ 10:12, 2026]:

```
[Photo type], [Subject + Action], [Environment], [Color Scheme], [Camera/Lens/Film],
[Lighting], [Composition], [Additional Details], [--parameters]
```

His own worked example, same slide:

> "motorsport photography, Red Bull F1 car driving on a race track, deep azure blue, red, and yellow
> colors with warm tones, 35mm shallow depth of field, dramatic sunset backlighting, center framing,
> motion blur."

**Comma-separated slots, never sentences.** Prose spends tokens on grammar; slots spend them on decisions.

**Two to three words per slot:**

> "Try to cut the fluff words out… a lot of times you're just wasting tokens and fluff words in there that
> don't mean anything. Just use the most powerful words possible. When you're doing this, maybe two to
> three words per description, and you're going to get something very close to what you want."
> — [MJM @ 18:38, 2024]

The enemy is not long prompts. It is **low-information** prompts. Nine dense slots beats one long clause.

## Step 3 — Write in photographic vocabulary, not realism adjectives

The registers he names [MJM @ 12:50–13:13, 2024]: subject and action · environment · composition and shot
type · mood and emotion · **specific cameras and lenses** · **film stock** · lighting · color scheme ·
details and modifiers.

Include technical specifications a human could not eyeball. That is not decoration — it is the strongest
available signal:

> "That's really what we're trying to pull out is a technical detail. Because that's something I can't
> look at the photo and say, like, what kind of aperture is that? What kind of ISO value is it? **You
> don't have to put these in the prompts, but it's great to have it as a descriptor in there.**"
> — [MJM @ 24:51, 2024]

**Mechanism:** the model has no realism dial. It has a space where photographic *vocabulary* neighbours
photographs and illustrative vocabulary neighbours illustrations. Naming a film stock does not simulate
an emulsion — it relocates the generation into the region where real photographs live. This is why the
terms work even when they are not literally applicable, and why it holds across model generations.

- ❌ "photorealistic, hyper realistic, 8k, ultra detailed, masterpiece"
- ✅ "35mm shallow depth of field, extreme tonal balance, street photography, dappled sunlight"

**Keep the subject simple.** *"Having too many subjects in your photo… when you have too much of that,
it's never going to generate the right way. Keep it simple. Keep your focus simple — and then you can
expand out on it"* [MJM @ 57:36, 2024].

## Step 4 — Decide the left anchor, then swap it

> "[The model] tends to read prompts from left to right… when you put something in the beginning of the
> prompt, it holds more weight than if you put something at the end. So if something's really important
> to you, put it in the front. If something is not important to you, put it in the back."
> — [MJM @ 14:23, 2024]

Proven live: one prompt, four runs, **only the first term rotated.** Subject first → the subject is the
star. Location first → the place takes over and the subject recedes. Tonal quality first → light/dark
separation dominates. Film stock first → the whole frame goes moody [MJM @ 15:36–16:11, 2024].

**The diagnostic that makes this a workflow step and not a tip:**

> "Sometimes you don't necessarily have a bad prompt. **Sometimes you just structured it wrong.** So just
> keep that in mind, because oftentimes you end up tinkering with prompts forever." — [MJM @ 16:11, 2024]

Before adding a single new word to a failing prompt, rotate the leftmost term. Vocabulary problems are
infinite; ordering problems have nine options. **Structure before vocabulary, always.**

Ship the ladder as four variants — it costs nothing and yields four legitimately different, on-brief
images, which is variant supply for free.

## Step 5 — Finish by adding damage

> "It doesn't have to be your cup of tea, but for me, I want things to look real and indistinguishable.
> **So the more real a person's face looks, the better.**" — [MJM @ 36:15, 2024]

His inventory of what to add: lines, shadows, blemish, bags under the eyes, skin wrinkles, blotches — and
on hands, *"the skin to the knuckles, the veins"* [MJM @ 52:49, 2024].

**The pipeline ends with a degradation step, not a cleanup step.** AI output fails realism from the
*smooth* side, always. Every model generation gets cleaner, so this corrective gets more necessary over
time, not less. Anyone whose last step is "upscale and sharpen" is walking the output away from real.

State the finishing note in the deliverable: what imperfection is being added, and where. Which tool
performs it is era-bound (Appendix A) and irrelevant to the brief.

## Step 6 — Rails before it ships

- **No "in the style of [living person]."** *"I don't think it's good if you're going to utilize it for
  commercial work, because if someone was getting you into litigation, going backwards… they went back to
  the end result, which was your prompt, and it said 'in the style of X person'"* [MJM @ 39:03, 2024].
  Decompose instead: *"go and learn it… what type of composition does he use? What type of color scheme?
  What type of equipment? And then you can build out those visual building blocks… but **you learned**"*
  [MJM @ 39:49, 2024]. The decomposition is also the better craft move — a name is one opaque token, its
  components are five tunable dials.
- **Reverse-image-search anything going commercial.** He demonstrates reproducing a famous magazine cover
  from text alone, no reference image, by looking up the original shoot's camera and aperture
  [MJM @ 37:39, 2024]. *"Just don't do anything that's close. Don't expose yourself there."*
- **Disclose AI use to clients.** *"It has to be an open discussion that you're utilizing AI in the work.
  You have to make sure everyone's comfortable with that"* [MJM @ 36:38, 2024].

---

## Output schema

```
# Photoreal Build — <subject> — <date>

## Element table
| Element | Decision | Deliberately open? |
(all nine rows, every one filled or explicitly marked open)

## Built prompt
<comma-separated slots, formula order, 2–3 words per slot>

## Left anchor
Chosen: <term> — because <what should dominate the frame>

## Swap ladder
V1 <anchor> | V2 <anchor> | V3 <anchor> | V4 <anchor>
(full prompt for each; only the leading term moves)

## Finishing note
Imperfection pass: <what damage gets added, where>

## Rails
Style-of-person: none · Reverse-search: <required / done> · Disclosure: <status>
```

**Length:** one page. If it's longer, the prompt is padded.

## Quality gate

- [ ] All nine elements addressed; any left open is **listed as a decision**, not silently missing.
- [ ] Prompt is comma-separated slots in formula order, not prose.
- [ ] 2–3 words per slot; no fluff words, no filler adjectives.
- [ ] Vocabulary is *from* photography (shot type, lens, film, light quality) — **zero** realism
      adjectives like "photorealistic / hyperrealistic / 8k / ultra-detailed / masterpiece."
- [ ] At least one technical specification a human couldn't eyeball (aperture, ISO, focal length, stock).
- [ ] Left anchor named with a reason, and the 4-variant swap ladder is present.
- [ ] Finishing note specifies an imperfection pass — not an upscale-and-sharpen.
- [ ] No "in the style of [living person]." Reverse-search flagged if commercial.
- [ ] No model name, parameter syntax or menu path taught as current.

## Example output (abridged)

```
## Element table
Shot/Photo Type   | editorial portrait, medium shot        |
Subject + Action  | barista pulling a shot, leaning in      |
Environment       | narrow shopfront, morning street behind |
Color Scheme      | warm brass, oxidised green, bone white  |
Technical Details | 50mm, f/1.8, Portra 400, ISO 800        |
Composition       | off-centre left, negative space right   |
Lighting          | single window source camera-left, hard  |
Textures          | steam, wet steel, flour dust on apron   |
Details/Modifiers | one loose apron string catching light   |
(none left open)

## Built prompt
editorial portrait, barista pulling a shot leaning into the machine, narrow
shopfront with morning street behind, warm brass and oxidised green and bone
white, 50mm f/1.8 Portra 400 ISO 800, single hard window source camera-left,
subject off-centre left with negative space right, steam and wet steel and
flour dust, one loose apron string catching the light

## Left anchor
"editorial portrait" — the register must dominate; the subject is
interchangeable across the campaign, the register is not.

## Swap ladder
V1 editorial portrait, … (register leads)
V2 barista pulling a shot, … (subject leads — expect tighter crop)
V3 single hard window source camera-left, … (light leads — expect contrast)
V4 Portra 400 ISO 800, … (stock leads — expect the whole frame to warm)

## Finishing note
Imperfection pass on face and hands: pore texture, forearm hair, steam-damp
skin sheen, knuckle skin. Do not smooth. Do not sharpen globally.
```

**Execution prompt:** `references/prompts-v2/photoreal-prompt-build.md` — honor its Output Contract.
