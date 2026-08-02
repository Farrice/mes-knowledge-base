# Workflow — The Style-Code Library (Brand-Consistent Asset System)

**Deliverable:** a **Style Library Spec** — one frozen backbone, a named set of style handles with
retrieval cards, a variable-head grammar, and the handoff signature. The thing a second person can pick
up and use to produce on-brand assets without asking you anything.

**Run this when:** a brand needs many images that look like each other, forever, produced by more than one
person, across tools that will change.

**Why it exists.** Consistency is usually attempted as *vigilance* — someone eyeballs every asset and
sends back the off-brand ones. Flynn's move converts it into **string concatenation**, which is
automatable, delegable, and survives staff turnover. The failure this prevents is his own, stated against
himself: *"I've got 40 or 50 of these things — how are you even going to keep track"* [MOOD @ 29:36, 2025].

**Tool-neutral by construction.** "Style handle" below means whatever the current generator offers —
moodboard, style reference, profile code, trained adapter. The library structure does not change when the
handle type does. Era-bound handle syntax is in `genius.md` Appendix A.

---

## Step 1 — Split the nine elements into backbone and head

The core move, and the reason the whole system works:

| **FREEZE — the backbone (aesthetic)** | **VARY — the head (content)** |
|---|---|
| Color Scheme | Shot / Photo Type |
| Technical Details (camera / lens / film) | Subject + Action |
| Lighting | Environment |
| Composition | |
| Textures | |
| Details / Modifiers | |

> "Everything that's in white over here on the left, that's what I'm just going to keep for every single
> prompt. I don't even need to change that. It's just really, all you need to do is change the shot type,
> the subject and the details… **the difference between close-up of a surfer with frost on his face versus
> close-up of a penguin on the beach — that's all that I changed in this prompt. Everything else on the
> back end stayed the same.** So really, that's how you can build out this visual signature and this
> visual identity that keeps you consistent so you can stay on brand." — [MJM @ 20:25–21:04, 2024]

**Mechanism.** Aesthetic identity lives almost entirely in the technical half of the element list;
narrative variety lives almost entirely in the content half. They are separable. Once separated, "on
brand" stops being a judgment call and becomes a fixed string. This is the durable idea behind every
style-handle feature ever shipped: **a persistent backbone.**

His own backbone, verbatim, from a live build:

> "minimalistic Icelandic landscape, black mountains, rolling ocean, dark atmosphere, muted colors,
> sharp resolution, color contrast" — [MJM @ 44:44, 2024]

Heads swapped on camera against it: surfer with frozen mustache → seal → walrus → surfboard covered in
frost. One world, four assets, one line changed.

## Step 2 — Source the backbone from an asset the brand already owns

Do not invent the backbone. Extract it. The brand's identity is already encoded in its best existing
image; your job is to make it composable.

> "Essentially it's reverse engineering an image and then basically we're using it for consistent brand
> relevance." — [MJM @ 21:45, 2024]

The pipeline, in model-independent steps:

1. **Pick winners, not favourites.** *"A lot of times we're picking winners… whatever images have worked
   in the past and we're iterating off of those"* [MJM @ 32:08, 2024].
2. **Get a machine reading** of the image via whatever captioning path the tool offers.
3. **Reject it as an answer.** *"To me, this kind of looks like crap. It looks like video games. It
   doesn't look like a real image"* [MJM @ 24:13, 2024]. Machine captions optimise for coverage, not
   direction — no lens language, no film stock, no compositional intent. It is input.
4. **Route through an LLM to impose the formula** — describe it *"like an award winning professional
   photographer and extreme technical detail,"* structure with the nine-slot formula, include specific
   camera / lens / settings, *"use short powerful keywords and phrases, do not use full sentences"*
   [MJM @ 24:41–25:22, 2024].
5. **Send the image back in** alongside the extracted text and tune the blend — the text extraction is
   lossy, and the reference closes the loop [MJM @ 27:01, 2024].
6. **Keep the technical half. Discard the content half.** That residue is the backbone.

**The rail, stated unprompted and twice:** *"I always say to disclaimer, use this on your own brands, your
own personal brands. **Please do not go and do this for every other brand, please**"* [MJM @ 21:52, 2024].

## Step 3 — Build handles at three tiers, and build a brake

A library is not a pile. It has structure [MOOD @ 01:35–02:38, 37:20, 2025]:

- **Tight** — the brand's core look. One or two. Overrides direction.
- **Broad** — house style with range, for campaigns that need room.
- **Micro (~5 images each)** — one isolated effect, built expressly to be stacked. Grain, chrome, film
  negative, a specific texture. *"Something that doesn't have to be 100 images — something that's maybe
  like five images but for a specific use… my favorite little stackable piece now."*
- **Brake** — at least one deliberately flat, unstylised handle whose job is to pull over-cooked output
  back toward plausibility [MOOD @ 03:44, 2025]. Almost nobody builds one. Build one.

Micro handles are the highest-value tier because they **compose**. A library of three tight handles is a
collection; a library with a micro tier is a system.

## Step 4 — Characterize every handle before it enters the library

Nothing enters the library uncharacterized. Run the sweep: `workflows/moodboard-sweep.md`.

Minimum bar per handle: a **null run** (what it does with no prompt), a **probe run** (what survives
direction), a tier, a working weight, and known stack partners. A handle with no characterization is not
a library entry — it's a folder someone will delete in six months.

## Step 5 — Write the retrieval card

The card is the deliverable. Its only test: **can somebody find the right handle under deadline without
asking you?**

His register for a behaviour note — concrete, sensory, no bare adjectives:

> "This is the Cenote, where it's going to be way more dark and mysterious and gritty textured…
> deep blacks, deep blues, deep greens." — [MOOD @ 34:02, 2025]

Every card carries a **"use for ___"** clause. That clause is what answers his own complaint —
*"am I going to remember to run this combination, and when am I going to use it?"* [MOOD @ 23:33, 2025].

## Step 6 — Write the variable-head grammar

Specify what a user is allowed to change and what they are not. Three slots open (shot type, subject +
action, environment), everything else locked. Include five worked heads so the pattern is unmistakable.

This is what turns the library from a reference document into an operating instruction.

## Step 7 — State the handoff signature

The library is finished when it can be stated as a type:

> "Now I can hand this off to someone else. **Any 2D vector image can go in and studio shots can come out.
> I've replaced myself.**" — [CONFIG @ 18:38, 2026]

> "Build this stuff not just for yourself, but for everyone else. **If only you can operate it, then it's
> not really a system.**" — [CONFIG @ 20:41, 2026]

Write the signature literally: *"Any <input type> goes in; <output type> comes out."* If you cannot write
that sentence, judgment is still stuck inside the pipe and the library isn't done.

## Step 8 — Version it against model change

> "Screw the models. Every model I've mentioned here, they're all going to change, but if you build
> structured systems, you can just swap tools in." — [CONFIG @ 20:30, 2026]

The library spec therefore records, separately and dated: **the backbone text** (durable), **the handle
inventory** (durable as intent, era-bound as artifacts), and **the current tool binding** (which generator,
which handle type, which weights — expected to expire). When the tool changes, only the third section is
rewritten. Never let a model name into the first two.

---

## Output schema

```
# Style Library Spec — <brand> — <date> — tool binding v<n>

## 1. Backbone (FROZEN, durable)
<verbatim backbone string>
Sourced from: <the winning asset it was extracted from>
Locked elements: color scheme · technical · lighting · composition · textures · modifiers

## 2. Variable head grammar (durable)
Open slots: shot/photo type · subject + action · environment
Locked: everything else
Worked heads: <5 examples>

## 3. Handle inventory
### <NAME> — tier: tight | broad | micro | brake
Behaviour: <concrete sensory note>
Working weight: <coefficient>
Stacks with: <> · Fights with: <>
Use for: <asset types>

## 4. Named recipes
R1 · <name> — <handles, order, weights> — for <asset type>

## 5. Handoff signature
Any <input> goes in; <output> comes out. Operator needs: <nothing / list>.

## 6. Tool binding (EXPIRES — dated)
Generator + version · handle mechanism · weight syntax · known failures
Reviewed: <date> · Next review trigger: <model release>

## 7. Rails
Own-brand only · no style-of-person · reverse-search commercial · AI disclosure
```

**Length:** 2–3 pages. Section 6 is the only one allowed to name a product.

## Quality gate

- [ ] Backbone is a single frozen string, sourced from a real owned asset, not invented.
- [ ] Backbone contains **no** subject, action or environment — only aesthetic.
- [ ] Variable-head grammar names exactly which slots are open, with 5 worked examples.
- [ ] Library has a micro tier **and** at least one brake handle.
- [ ] Every handle carries a null-run behaviour note, a tier, a weight, and a "use for ___" clause.
- [ ] Handoff signature is written as a literal type sentence.
- [ ] Sections 1–5 name **zero** products, parameters or menu paths; all of that is quarantined in
      Section 6 with a date and a review trigger.
- [ ] Rails present: own-brand only, no style-of-person, reverse-search, disclosure.

## Example output (abridged)

```
## 1. Backbone (FROZEN)
"muted oxidised palette, 50mm shallow depth of field, Portra 400, overcast
north light, off-centre framing with negative space, matte paper grain,
one warm practical in frame"
Sourced from: 2025 SS campaign hero (highest-CTR asset, 3 seasons running)

## 2. Variable head grammar
Open: shot/photo type · subject + action · environment. Locked: all else.
Worked heads:
  H1 "editorial full body, model walking away, empty loading dock"
  H2 "close-up product, hands fastening a strap, tiled stairwell"
  H3 "wide establishing, two figures crossing, rooftop at dusk"
  H4 "flat lay, folded garment stack, concrete bench"
  H5 "medium portrait, subject seated looking off-frame, bus shelter"

## 5. Handoff signature
Any owned product photo goes in; a 6-asset on-brand campaign set comes out.
Operator needs: the backbone string and this grammar. Nothing else.

## 6. Tool binding (EXPIRES) — reviewed 2026-08-02
<generator + version> · handles as <mechanism> · weights <range>
Next review trigger: next major model release, or 90 days, whichever first.
```

**Execution prompt:** `references/prompts-v2/brand-style-library-spec.md` — honor its Output Contract.
