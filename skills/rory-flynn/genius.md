# Rory Flynn — Genius Patterns

Founder, Systematiq AI. Figma Config 2026 Maker Stage. Client work shown on stage: BarkBox, SharkNinja.
Came up running a 90-client email-and-paid-media agency shipping ~900 emails a month, which is where the
whole worldview comes from: he is not an artist who learned operations, he is an operator who learned
images because the throughput problem would not go away.

Source keys: **[CONFIG]** Figma Config 2026 talk (2026 — **the spine**) · **[MOOD]** Midjourney Fast Hours
moodboards episode (2025) · **[MJM]** Midjourney Masterclass (2024, v6 era — **historical**).
Full ledger and fidelity flags: `references/source-notes.md`.

> **SOURCE-WEIGHTING RULE (binding, Farrice 2026-08-02).** The 2026 Config talk is the spine of this
> skill. The 2024 masterclass and the 2023 LinkedIn cheat sheet contain **era-bound parameter mechanics**
> — Discord slash-commands, specific weight ranges, named upscalers, model-version failure modes. Those
> are **not taught as current** anywhere in the main body. What is carried forward from the older sources
> is only what survives a model swap: the photography-language doctrine, the frozen-backbone consistency
> system, the deconstruct→formula discipline, the ethics rails. Every era-bound mechanic lives in
> **Appendix A — Era-Bound Mechanics (verify before use)**, dated, and is to be verified against the
> current tool before it is ever executed. This is his own instruction applied to his own corpus:
> *"screw the models… if you build structured systems, you can just swap tools in."*

---

## The one-line thesis

Everyone can now make one beautiful image. Almost nobody can make the nine-hundredth on-brand image this
month without the quality falling apart. **He builds the machine that closes that gap, and he builds it so
that the machine survives every model swap.**

> "The truth is everyone can do this now. They can create cool things, but they do it in a vacuum. The real
> question is can they do it at scale?" — [CONFIG @ 04:06]

---

## PART I — THE DIAGNOSIS (why systems at all)

### Pattern 1 — Creative inflation

The named disease. Not "we need better images." The demand curve for creative is permanently outrunning
the supply curve, structurally, because channels and formats and variants multiply faster than headcount.

> "It's like this never-ending need for new creative. We have to do this stuff for multiple channels and
> multiple formats, all the variants. All this demand leads to a lot of creative fatigue. So we have to
> start to build systems to keep up with that." — [CONFIG @ 04:21]

**Mechanism.** Once you name the problem as *inflation* rather than *quality*, the correct response stops
being "hire a better designer" and becomes "raise throughput per unit of taste." Every downstream pattern
is a throughput move that refuses to trade away control. His own statement of the target: *"more creative
at a faster pace, at a higher quality, with more control"* [CONFIG @ 04:42] — four dials, none sacrificed.

**Why it compounds.** The diagnosis also explains what NOT to build. He is uninterested in one-off magic.
If a technique cannot be run a second time by somebody else, it does not treat the disease.

### Pattern 2 — Solve small; the small problem is the leverage

> "You try to solve way too big of problems when the small problems are right in front of us." — [CONFIG @ 14:58]

BarkBox's actual bottleneck wasn't "AI strategy." It was one recurring composite photo of a subscription
box, needed every month, across multiple partnerships, with contents that change every time. Studio shoot,
asset wrangling, turnaround — "so this one little piece becomes a big problem" [CONFIG @ 15:32].

**Mechanism.** Small problems are recurring problems, and recurring problems are the only ones that pay
back a system. A big problem is usually a bundle of small recurring ones plus a lot of one-offs; solving
the bundle head-on produces a system that fits nothing. And the small solved problem *spreads*: "that one
workflow for just creating a singular asset now has started to bleed into every piece of the organization"
[CONFIG @ 19:31] — retouching, environment fixes, product fixes, compositing, localization, video.

### Pattern 3 — AI is only three things

The tool-agnostic invariant. He refuses to teach tools.

> "You don't need to know every tool. You just need to know that AI is only like three things and you can
> figure this stuff out. It's **context**, what you provide it, it's **direction**, it's how you brief it,
> and then it's **iteration**, what you do and iterate once you get something back." — [CONFIG @ 05:22]

**Mechanism.** Every technique he teaches is one of the three wearing a different hat. Reference images,
scale refs and feeder images are *context*. Prompt formulas, system prompts and Keep/Change are *direction*.
Weighting, permutations, remix-strong and the sweep are *iteration*. When a new tool lands, you don't learn
it — you ask which of the three it moves, and slot it in.

### Pattern 4 — Screw the models

> "Be flexible and, you know, screw the models. Every model I've mentioned here, they're all going to
> change, but if you build structured systems, you can just swap tools in." — [CONFIG @ 20:30]

**Mechanism.** The durable asset is the graph and the rules, not the generator. This is why his system
prompts describe *roles and formats* rather than model-specific syntax, and why his workflows put the
model at a swappable node. Anyone whose knowledge is "here are the magic words for model X" is holding a
depreciating asset. **Corollary for anyone building on him: never encode a model name into a rule.**

### Pattern 5 — If only you can operate it, it isn't a system

The handoff test, and the sharpest line in the talk.

> "Build this stuff not just for yourself, but for everyone else. **If only you can operate it, then it's
> not really a system.** If it's built for everyone, then they can take it and run with it." — [CONFIG @ 20:41]

The pass condition is stated as a shape, not a feeling:

> "Now I can hand this off to someone else. **Any 2D vector image can go in and studio shots can come out.
> I've replaced myself.** We can go work on the next problem." — [CONFIG @ 18:38]

**Mechanism.** A workflow is finished when its interface is a *type* (any 2D vector) and its output is a
*type* (studio shots), with no operator judgment left inside the pipe. Judgment moves to the inputs and to
the final selection — never to the middle. This is also the anti-hoarding rule: an expert who keeps the
judgment inside the pipe has built job security, not infrastructure.

### Pattern 6 — Track the hours or the whole thing is theatre

> "We did 114 projects in November with AI. And on the low end… still 30 percent reduction in time spent…
> On the high end, it was an 85 percent reduction in hours spent. We're really focused on tracking this
> meticulously because at the end of the day, **if it doesn't save time and it doesn't save money, like
> what the hell is the point?**" — [MJM @ 39:34–41:02] *(self-reported figures)*

**Mechanism.** Measurement is what stops an AI practice from becoming a hobby with a client list. Note the
shape of the claim: a range across a real project count, with the low end stated first. That is what an
honest operator's number looks like.

---

## PART II — DECONSTRUCTION (the skill he ranks first)

### Pattern 7 — Deconstruction is the parent skill

Of his three core skills — deconstruction, system prompts, workflow dev — he names the first as primary.

> "It's probably my favorite one here. It's basically reverse engineering… if we can deconstruct
> something, we can start to reveal patterns and those will show us how to build formulas and templates so
> we always know what and how to prompt anything." — [CONFIG @ 08:30, 09:08]

**Mechanism.** Deconstruction converts a *sample* into a *formula*, and a formula is the only thing that
scales. You cannot batch an intuition. The chain is always: take a piece of media → break it into core
components → notice which components recur → the recurring set IS the template → the template is what a
machine can fill.

**The move applies recursively.** He deconstructs a photo (→ Image Elements). He deconstructs *editing*
(→ Keep/Change). He deconstructs a brand's visual identity (→ asset hacking). Same operation, three levels.

### Pattern 8 — The nine Image Elements (the non-negotiables)

Read verbatim off the Config slide [CONFIG @ 09:46]:

| Element | His gloss |
|---|---|
| **Shot / Photo Type** | How it's captured |
| **Subject + Action** | Who and what |
| **Environment** | Where it is |
| **Color Scheme** | The colors |
| **Technical Details** | The aesthetic |
| **Composition** | How it's constructed |
| **Lighting** | The tone |
| **Textures** | Surface. Depth. Feel. |
| **Details / Modifiers** | The subtle details |

> "I call these like the non-negotiables. They'll be represented just about every photo ever taken. So
> without them, you don't really have an image." — [CONFIG @ 09:48]

**The mechanism, and it is the single most useful sentence in the corpus:**

> "Lighting is going to be represented in every photo no matter what. And when you're prompting, **if you
> don't add something like lighting, the model will provide it for you.** So if we can control these, we
> can really control everything." — [CONFIG @ 09:54]

Every element is present in the output whether or not you specified it. Silence is not neutrality —
silence is a delegation. Each unspecified element is a slot the model fills from its own priors, which is
exactly where run-to-run drift and off-brand output come from. **Unspecified = model-chosen = drift.**

**Anti-example:** "a woman drinking coffee in a cafe, photorealistic" — seven of nine slots delegated.
The output will be *some* photo. It will not be *your* photo, and the next one won't match it.

**Excellence example (his own, off the same slide deck):** "motorsport photography, Red Bull F1 car driving
on a race track, deep azure blue, red, and yellow colors with warm tones, 35mm shallow depth of field,
dramatic sunset backlighting, center framing, motion blur." — nine slots, nine decisions.

**Corollary — the elements are visual building blocks.** The slide pairs the list with a stack graphic
labelled "Visual Building Blocks." → camera icon. "When you think about them like little visual building
blocks, you can stack them together and then this becomes a prompt formula that either you can fill in or
a machine can fill in" [CONFIG @ 10:04]. The list is not a checklist for humans. It is an interface for
automation.

### Pattern 9 — The Simple Prompt Formula

Verbatim from the slide [CONFIG @ 10:12]:

```
[Photo type], [Subject + Action], [Environment], [Color Scheme], [Camera/Lens/Film],
[Lighting], [Composition], [Additional Details], [--parameters]
```

His worked example, same slide: *"motorsport photography, Red Bull F1 car driving on a race track, deep
azure blue, red, and yellow colors with warm tones, 35mm shallow depth of field, dramatic sunset
backlighting, center framing, motion blur."*

> "It's just sort of like a random collection of words here, no rhyme or reason to it, but they all have a
> little weight to them so that when we run it, we get an image and exactly what we're looking for."
> — [CONFIG @ 10:16]

**Mechanism.** Comma-separated slots, not sentences. Prose burns tokens on grammar; slots spend them on
decisions. And crucially: *"you don't have to go really crazy because you're doing the things that are
most important to create an image"* [CONFIG @ 10:31]. The formula is a floor for completeness, not a
license for length.

**The longer variant exists and is a different tool.** In [MJM @ 16:38–18:30] he shows a granular version
that splits subject into *subject position* (laying down / facing left), *subject focus* (foreground /
midground / background, in or out of focus), and wardrobe detail, plus environment focus, emotion, tone,
time of day, textures, image type. His framing of when to reach for it:

> "You do not have to use everything here, but if you want to have a very singular vision and you want to
> have that executed, you can break it down this granularly… think about when you're building a scene or
> telling a story, this is kind of like a screenplay writer would give this to a director. You're giving
> them every little piece so they can just go and capture the shot." — [MJM @ 16:41, 17:41]

### Pattern 10 — Left-to-right weighting, and the diagnosis it enables

> "Midjourney tends to read their prompts from left to right… when you put something in the beginning of
> the prompt, it holds more weight than if you put something at the end. So if something's really important
> to you, put it in the front. If something is not important to you, put it in the back." — [MJM @ 14:23]

He proves it live: one prompt, four runs, **only the first term rotated.** Land Rover first → the car is
the star. "Vibrant Cusco, Peru" first → the city takes over and the car recedes. "Extreme tonal balance"
first → the light/dark separation dominates. "Berger Pancro 400" first → the whole frame goes moody
[MJM @ 15:36–16:11].

**The payoff line, which is a diagnostic tool and not a tip:**

> "Sometimes you don't necessarily have a bad prompt. **Sometimes you just structured it wrong.** So just
> keep that in mind, because oftentimes you end up tinkering with prompts forever." — [MJM @ 16:11]

**Mechanism.** Most prompt-tinkering is an ordering problem misdiagnosed as a vocabulary problem, and
vocabulary problems are infinite while ordering problems have nine slots. Before you add a word, rotate
the leftmost term. The Left-Anchor Swap is also a *generative* move: four positions × one prompt is four
distinct legitimate images, which is variant supply for free.

---

## PART III — PHOTOREALISM AS A LANGUAGE

### Pattern 11 — Photography terminology is the photorealism trigger

> "For us, typically **the best way to trigger Midjourney into a photorealistic mindset is to use
> photography terminology.** That's what I've always found has worked the best. Keeping it very consistent
> in that sense and also priming it to be more photorealistic." — [MJM @ 12:31]

The named registers: subject and action, environment, composition and shot type, mood and emotion,
**specific cameras and lenses**, **film stock**, lighting, color scheme, details and modifiers
[MJM @ 12:50–13:13].

**Mechanism.** A generator has no "realism" dial. It has a latent space in which the neighbourhood of
photographic *vocabulary* is populated by photographs, and the neighbourhood of illustrative vocabulary is
populated by illustrations. Naming a film stock does not simulate that emulsion; it relocates the
generation into the region of the space where real photographs live. This is why the terms work even when
they are not literally applicable.

He makes exactly that point about specs a human could never eyeball:

> "That's really what we're trying to pull out is a technical detail. Because that's something I can't
> look at the photo and say, like, you know, what kind of aperture is that? What kind of ISO value is it?
> **You don't have to put these in the prompts, but it's great to have it as a descriptor in there.**"
> — [MJM @ 24:51]

**Anti-example:** "photorealistic, hyper realistic, 8k, ultra detailed" — words *about* realism.
**Excellence:** "35mm shallow depth of field, Berger Pancro 400, extreme tonal balance, street photography"
— words *from* photography.

### Pattern 12 — Clear and direct in, clear and direct out

> "Clear and direct prompts equal clear and direct output. Ambiguous prompts equal ambiguous output —
> meaning the less detail you put in your prompt, the more Midjourney takes over and takes its creative
> liberty. So if you just put like 'dog in a park,' you'll get a dog in a park, but you might not have
> control over anything else." — [MJM @ 11:52]

Same mechanism as Pattern 8, stated as a conservation law: **control is conserved.** Every decision you
don't make is a decision the model makes. There is no third option where the slot stays empty.

### Pattern 13 — Two to three words per description; cut the fluff

> "Try to cut the fluff words out… a lot of times you're just wasting tokens and fluff words in there that
> don't mean anything. Just use the most powerful words possible. When you're doing this, maybe **two to
> three words per description**, and you're going to get something very close to what you want."
> — [MJM @ 18:38]

Reinforced in his own system prompt, which instructs the LLM to "use powerful language" and to produce
prompts "detailed + expressive" [CONFIG slide @ 12:22], and in the third-party summary of his cheat sheet:
avoid full sentences, prefer "enormous" over "big."

**Mechanism.** Nine slots × two-to-three high-specificity words is a dense, complete prompt. Nine slots ×
a clause each is a diffuse one. Density per slot beats length overall — the enemy is not long prompts,
it's *low-information* prompts.

### Pattern 14 — Polished reads as fake; the last step must ADD damage

The durable principle, stated as a preference and defended as a standard:

> "It doesn't have to be your cup of tea, but for me, I want things to look real and indistinguishable.
> **So the more real a person's face looks, the better.**" — [MJM @ 36:15–36:24, 2024]

What he adds, in his own inventory: lines, shadows, blemish, bags under the eye, skin wrinkles, blotches
— and on hands, the tell everyone forgets: *"those hands look so polished, but I add this and we add hair
and we add all that, we have the skin to the knuckles, we add the veins. Like that looks so much
different"* [MJM @ 52:49, 2024].

**Mechanism.** AI output fails realism from the *smooth* side, never the rough side. The viewer's fake
detector is calibrated on skin texture, pore noise, knuckle hair, veins, asymmetry, blown highlights —
the artifacts of a real sensor meeting real light. **A photorealism pipeline therefore ends with a
degradation step, not a cleanup step.** Anyone whose final step is "upscale and sharpen" is walking the
output *away* from real.

This is model-independent and gets more true, not less, as generators improve: every generation of model
gets *cleaner*, so the corrective gets more necessary. Which specific tool performs the pass is era-bound
and belongs in Appendix A.

### Pattern 15 — Failure modes are a routing table, not a complaint

The durable half: every generator has a set of things it will not do consistently, those things are
knowable, and knowing them converts "the model is bad" into "this shot takes a different path."

> "Those are things I wouldn't say stay away from — just be cognizant of." — [MJM @ 57:33, 2024]

His structural observation is the part that survives every model release:

> "It's a lot of things that typical artists have problems with, right? Artists have a really hard time
> drawing hands and have a really hard time drawing eyes." — [MJM @ 57:19, 2024]

**Mechanism.** Generator failures cluster where *human representation* is hardest — articulated
extremities, specular reflection, recursive geometry, crowd coherence — because those are the regions of
the training distribution that are both rare and unforgiving. That's a property of the problem, not of a
release. So the operating move is permanent even though the specific list churns: **maintain a current
failure inventory for whatever model you're on, and route those shots to a different path** (different
model, local repair, hand comp, or don't shoot it).

The one durable *composition* rule he gives alongside it:

> "Having too many subjects in your photo… when you have too much of that, it's never going to generate
> the right way. **Keep it simple. Keep your focus simple** — and then you can expand out on it."
> — [MJM @ 57:36–58:00, 2024]

Which specific subjects fail on which model in which year is era-bound. See Appendix A.

---

## PART IV — BRAND CONSISTENCY (the frozen backbone)

### Pattern 16 — Freeze the backbone, vary the head

The most transferable single move in the corpus, and the actual answer to "how do I keep 200 images on brand."

Take the nine elements and split them in two. **Freeze**: color scheme, camera/lens/film, lighting,
composition, additional details — the aesthetic. **Vary**: photo type, subject + action, environment —
the content.

> "Everything that's in white over here on the left, that's what I'm just going to keep for every single
> prompt. I don't even need to change that. It's just really, all you need to do is change the shot type,
> the subject and the details… **the difference between close-up of a surfer with frost on his face
> versus close-up of a penguin on the beach — that's all that I changed in this prompt. Everything else on
> the back end stayed the same.** So really, that's how you can build out this visual signature and this
> visual identity that keeps you consistent so you can stay on brand." — [MJM @ 20:25–21:04]

Restated for the asset-hacking case: *"that color scheme, the lens, the camera lens and film, the lighting,
the composition, the additional details — those stay the same, and now we can just change the photo type,
the subject and action, and the environment. That'll all keep that same look and branded feel"*
[MJM @ 28:22].

**Mechanism.** Aesthetic identity lives almost entirely in the *technical* half of the element list, and
narrative variety lives almost entirely in the *content* half. They are separable. Once separated, brand
consistency stops being a matter of vigilance and becomes a string-concatenation problem — which is to
say, automatable. This is what makes a style code, an `sref`, a moodboard and a system prompt all
interchangeable implementations of one idea: **a persistent backbone.**

**Excellence example (his, verbatim backbone):** "minimalistic Icelandic landscape, black mountains,
rolling ocean, dark atmosphere, muted colors, sharp resolution, color contrast." Heads swapped live on
camera: close-up surfer with frozen mustache → seal → walrus → surfboard covered in frost. Same world,
four assets, one line changed [MJM @ 43:42–46:33].

### Pattern 17 — Asset hacking

Reverse-engineer an image you own into building blocks, then regenerate outward to infinity.

> "Essentially it's reverse engineering an image and then basically we're using it for consistent brand
> relevance." — [MJM @ 21:45]

The pipeline, stated in model-independent steps, as demonstrated on a Red Bull F1 image
[MJM @ 22:02–29:19, 2024 — *the shape is durable; the button-presses are in Appendix A*]:

1. **Organize the brand assets.** Pick the ones that already carry the identity. In ad work specifically:
   *"a lot of times we're picking winners… whatever images have worked in the past and we're iterating off
   of those"* [MJM @ 32:08].
2. **Get a machine reading of the image** — whatever the current tool's image-captioning path is.
3. **Reject that reading as an answer.** See Pattern 18. It is input, not output.
4. **Route the image through an LLM** with an instruction to describe it *"like an award winning
   professional photographer and extreme technical detail,"* to structure the output with his prompt
   formula, to include specific camera, lens and camera settings, and to *"use short powerful keywords
   and phrases, do not use full sentences"* [MJM @ 24:41–25:22].
5. **Optionally blend** the best machine reading into the LLM prompt: *"sometimes you get a really good
   synthesized prompt out of that. Sometimes you don't need it"* [MJM @ 25:29].
6. **Send the image back in alongside the new text prompt**, and tune the balance between the two. His
   reasoning is explicitly LLM-shaped: *"if you've utilized ChatGPT before, typically it works better if
   you give it data first and then you generate off of it, because it has some context to work off of"*
   [MJM @ 27:01]. The text extraction is lossy; the reference closes the loop.
7. **Iterate on the head only** (Pattern 16): panning shot Red Bull racing car → Red Bull skier → Red Bull
   motorcycle → Red Bull mountain biker.

**The hard ethical rail, stated unprompted and twice:**

> "I always say to disclaimer, use this on your own brands, your own personal brands, whatnot.
> **Please do not go and do this for every other brand, please.**" — [MJM @ 21:52]

**Mechanism.** The brand's identity is *already encoded* in its best existing asset. Extracting it into
text makes it composable; text is the only representation you can batch, template and hand off.

### Pattern 18 — A machine caption is raw material, never an answer

> "If you're looking at this and saying, cool, maybe there are some cool images here — but to me, this
> kind of looks like crap. It looks like video games. It doesn't look like a real image. So for me,
> utilizing this in my brand in any way, shape or form, I just wouldn't use it." — [MJM @ 24:13, 2024]

And the reason he routes it through an LLM instead:

> "I would not be able to do this with just my eyes, and **[the auto-caption] is not going to put out
> something like this because it's kind of all over the place.**" — [MJM @ 26:14, 2024]

**Mechanism.** Machine-read image captions optimize for *coverage*, not *direction*. They name what's
present without ranking it or forcing it into a controllable structure, which is why they read as
video-game-ish: no lens language, no film stock, no compositional intent. The LLM's job in the chain is
not description — it's **imposing the formula.** Two different machines, two different jobs; conflating
them is the common failure. This holds regardless of which captioner is current: any system that outputs
an unstructured reading needs a structuring pass before it can drive production.

### Pattern 19 — Don't say "in the style of [name]" — learn it instead

> "I typically don't like to use 'in the style of' prompts… I don't think it's good if you're going to
> utilize it for commercial work, because if someone was getting you into litigation, going backwards…
> they went back to the end result, which was your prompt, and it said 'in the style of X person.'"
> — [MJM @ 39:03–39:43]

The replacement, which is the strictly better craft move anyway:

> "Instead of doing that, actually go and learn it. If you like Wes Anderson's composition style, go to
> ChatGPT and say, what type of composition does he use? What type of color scheme does he use? What type
> of equipment does he use? And then you can build out those visual building blocks and you can create in
> his style, but **you learned.**" — [MJM @ 39:49–40:13]

**Mechanism.** A name is an opaque, unadjustable, legally-attributable token. Its decomposition — symmetry,
centered framing, specific palette, particular focal lengths — is transparent, tunable, and yours. You
give up nothing but the shortcut, and you gain every dial. This is Pattern 7 (deconstruction) applied to
a person instead of a photo.

**Adjacent rail:** reverse-image-search everything going commercial. He demonstrates reproducing a famous
1980s National Geographic cover from a text prompt alone — no image reference — by looking up the shoot's
camera and aperture and plugging them in [MJM @ 37:39–38:30]. *"Just know that this can happen… all you
have to do is then go iterate it and you don't have to have that same image. Just don't do anything that's
close. Don't expose yourself there"* [MJM @ 38:56].

---

## PART V — MOODBOARDS AS AN OPERATION

Everything below is from [MOOD], an unrehearsed working session — which is why it carries the actual
working method rather than the taught version of it.

### Pattern 20 — A moodboard is a token you minted yourself

The line that reframes the whole feature:

> "It's like you're creating your own tokens now — you're creating your own tokens with a moodboard."
> — [MOOD @ 38:01]

His framing of why that matters, and it is the most strategic thing in the episode:

> "The more context, the more you think and the more energy you put into the input, the better the output.
> The problem is it's so labor intensive to do the typing… references, style codes, moodboards — some of
> these things **give it more information without requiring more energy and time on our output.**"
> — [MOOD @ 38:16, 39:51]

**Mechanism.** A board is compression. Concepts that would cost 40 words of unreliable description
(a specific grain, a specific goo, a specific chrome) become a single referenceable handle that transmits
*more* signal at *lower* input cost. That is the actual economics of style codes: not consistency for its
own sake, but bandwidth per keystroke. And unlike a text description, the board doesn't drift when the
model's reading of the words shifts.

### Pattern 21 — Three tiers of board: tight, broad, micro

The full arc of his own thinking, verbatim, because the reasoning is the pattern:

> "When I started doing moodboards I wanted this really tight aesthetic — I was trying to create an `sref`
> code. And then I'm like, well that doesn't work for everything, because it takes a lot of time to build
> the database to that. I'm like, what if I go more broad? So it's kind of like this mashed-up aesthetic.
> And then it's like, oh that's cool, but then it's also like, well maybe I just want certain elements
> that I want to mix and match. So then you go back to creating these little tiny small things."
> — [MOOD @ 01:35–01:59]

| Tier | Size | Job | His examples |
|---|---|---|---|
| **Tight** | large, curated | reproduce one exact aesthetic; an `sref` substitute | the aesthetic he originally chased |
| **Broad** | large, mixed | a house style with range; "a lot of different aesthetics in it" [MOOD @ 32:40] | Japanese movie poster, Atoll |
| **Micro** | **~5 images** | one isolated effect, built to be stacked | film negative, iPhone, grunge textures, film grain, chrome, goo |

> "Something that doesn't have to be 100 images — something that's maybe like five images but for a
> specific use, like that film negative one. To me that's my favorite little stackable piece now."
> — [MOOD @ 37:20]

**Mechanism.** The tiers exist because *burden* differs. Explicitly:

> "Not every moodboard needs to carry the same amount of burden… one could be a little bit more of a
> 'hey this is a nice little seasoning to put on your bland chicken,' and you can stack this with one of
> these other moodboards that provides more of the tastiness." — [MOOD @ 02:20]

A micro board that does one thing well is more valuable than a broad board that does everything vaguely,
because the micro board *composes*. This is the difference between building a style library and building
a style collection.

### Pattern 22 — Stacking, and stacking opposites

> "So I've been liking the Cenote and this ethereal one together — very very well. So it's like more of a
> super gritty dark high-contrasty with a very ethereal sort of soft. **It's like blending two opposites
> together — that's how I like the opposites.** Like putting my black and white one with my super colorful
> one. I like doing the juxtaposition there because you get some really cool stuff." — [MOOD @ 20:39–21:06]

And the corrective use, which is the most practical single trick in the episode:

> "I was getting these really crazy images that I wanted, but they were so overdone in terms of texture.
> And then I applied like my little iPhone moodboard to it and it **brought it right back down to reality,
> exactly where I wanted it to be.**" — [MOOD @ 03:44]

**Mechanism.** Boards are not just additive flavour; they are **vectors with direction**, and a board can
be used as a *brake*. An "iPhone" board (flat, snapshot, unstylised) pulls a hyper-stylised generation back
toward plausibility. Once you see boards as vectors, opposition-stacking stops being novelty and becomes
range control: two opposed vectors produce a result neither could reach alone, and one weak vector opposed
to a strong one produces calibrated restraint.

### Pattern 23 — Weighting is the tell that separates users from operators

> "It surprises me how many people don't know about the weighting of the references. They know that
> there's an image or a style thing and they have a general idea how it works, but they don't really know
> to weight it. And most of them don't know about permutations." — [MOOD @ 06:16–06:33]

> "Do you know what `sref` is, how comfortable are you with it, do you know how to weight it? And most of
> the time if it's 'I'm super comfortable' and then I get to 'I don't know how to weight it' — I'm like,
> okay, sure, **then you don't really know, because you're not able to control it.**" — [MOOD @ 07:21–07:35]

**The durable claim: every reference mechanism has a weight, and the weight is where the control lives.**
That is true of style references, moodboards, personalization profiles, image-vs-text balance and
character references, in every generator, in every year — because they are all implemented as a blend
between two signals, and a blend has a coefficient. The named surfaces change; the existence of the
coefficient does not.

He also names a second-order case most people never reach — weighting *reference systems against each
other*, not just against the prompt:

> "You can weight your global profiles versus the moodboards too, so you get a little bit heavier on the
> global profile and personalization versus the moodboards." — [MOOD @ 16:38]

**Mechanism.** Reference *presence* is a binary; reference *weight* is a continuum, and essentially all
the useful territory is in the middle. An operator who can only turn a reference on and off has two
settings and will conclude the feature "doesn't work." An operator who knows the dial has the full range.
And because batch-sweeping a weight usually costs one submission rather than N, **the correct default is
to sweep the weight rather than guess it.**

**Corollary, and it is the competence test:** "I know the feature" is not a claim. "I know its dial, its
range, and its default" is. Apply it to yourself on every new tool.

Specific ranges, parameter syntax and the permutation-brace mechanic are era-bound — Appendix A.

### Pattern 24 — The null-prompt characterization run

How you find out what a board actually is, before you trust it in production:

> "If you're testing moodboards — whether you're doing this yourself or you're using [someone else's] —
> **type in an empty character like a period or a slash and just run it.** And just dig into what that
> default is going to be. And then that might give you a better sense of what to expect."
> — [MOOD @ 35:02–35:25]

Then the second probe, deliberately neutral and pointed at your actual use case:

> "I usually do that along with — I try to think of the things that I'm going to create most often, which
> could be maybe photorealism-based, so maybe I'll throw in something very simple like 'editorial photo,'
> 'editorial photography,' 'lifestyle photography,' and just kind of see where it takes me."
> — [MOOD @ 35:29–35:43]

**Mechanism.** With a real prompt attached, you cannot tell what came from the board and what came from
your words — the two signals are confounded. A null or near-null prompt isolates the board's own prior.
This is a controlled experiment, and it is the reason his boards are named and reusable while most
people's are a folder of vibes. **Anyone deploying a purchased or inherited style asset without running
this is flying blind on someone else's taste.**

### Pattern 25 — The solo → stack ladder (the sweep proper)

The full comparison run, narrated as he scrolls it:

> "So this I just ran global. Then we ran a different moodboard. Then we ran these together. So this is
> just kind of showing you what happens to **stacking versus running a moodboard solo** — then I just kind
> of went and stacked one at a time." — [MOOD @ 23:13–23:33]

Ladder, in order: **global profile alone → each board solo → global + one board → one-at-a-time additions →
diff and name what each rung contributed.** One prompt held constant across every rung. His own example of
a rung worth keeping: *"global profile, global plus Kaleidoscope, global plus Kaleidoscope and Motion —
I think that's a good stack"* … *"I've run that enough to know that you get some pretty cool results out
of that"* [MOOD @ 24:53–25:05].

**The honest constraint he raises against himself, and it is load-bearing:**

> "I don't like whenever it gets more than global and like a moodboard or two — it just quickly becomes
> like, well, am I going to remember to run this combination, and when am I going to use it?"
> — [MOOD @ 23:33–23:47]

And: *"I've got 40 or 50 of these things — how are you even going to keep track of what we're running here"*
[MOOD @ 29:36].

**Mechanism.** The sweep is only useful if its results are *written down as named, retrievable recipes.*
An unrecorded sweep is entertainment. The deliverable of a sweep is not the images — it's the card that
says *this combination, at these weights, for this kind of asset.* That constraint is exactly why a
style-code **library** (Pattern 27) exists at all, and it is the discipline most people skip.

### Pattern 26 — Go deep on the one

> "Don't get lost in going too far in too many directions that you forget to go deep enough in one. And
> I think that's maybe the lesson I'm trying to convey here — **dig into things that you really like, push
> it, because that's how you go from the good to the great.**" — [MOOD @ 33:19–33:36]

The mechanical follow-through, in tool-neutral terms: once a frame hits, **re-roll variations off that
exact frame at high deviation**, repeatedly, rather than re-rolling the prompt — *"getting [a strong
variation] on top of something you already like tends to get me something really cool"*
[MOOD @ 26:26–26:35]. And he explicitly separates exploration from production: *"now I have to go and run
these actually individually instead of just bashing everything together"* [MOOD @ 26:44]. The
button-names for these operations are era-bound (Appendix A); the move — *branch from the winner, not
from the prompt* — is not.

**Mechanism.** Breadth finds the direction; depth finds the asset. Bashing produces candidates, not
deliverables. The transition from bash-mode to depth-mode is a *decision*, and naming it prevents the
most common failure in generative work: shipping the first interesting thing instead of the best version
of the right thing. **This is the counterweight to everything else in Part V** — the same session that
celebrates infinite stacking says, out loud, that infinite stacking is how you never finish.

### Pattern 27 — The library is the asset (and the naming is the work)

Multiple *kinds* of style asset coexist and compose — boards, style-reference images, personalization
profiles. He runs *"about six moodboards, four profile codes, two `sref` images, and then style version on
top of that"* in a single prompt [MOOD @ 08:03, 2025]. The takeaway is not the specific asset types (those
are era-bound) but that **a mature library has several classes of handle and they layer.** His own
published collection is ~24–26 named boards with hand-built profile codes derived from curated image sets.

Boards are referred to **by name** — Cenote, goo, bionic, Kaleidoscope, Motion, shape FX, iPhone, film
negative, Japanese movie poster, chrome, collage — and each name carries a known behaviour:

> "This is the Cenote, where it's going to be way more dark and mysterious and gritty textured…
> deep blacks, deep blues, deep greens." — [MOOD @ 34:02–34:12]

**Mechanism.** A style asset with no name and no characterization is unusable by anyone including its
author six weeks later. Naming plus a one-line behaviour note plus known-good stack partners is what
converts a pile of boards into a library you can *retrieve from under deadline* — which is the only
condition that matters. Note also that boards are personal: *"if I'm trying to use mine I need something
very smooth and soft and clean — my personalization codes just don't work, it's just never going to do it
for me, but I know you have some in there that are for that purpose"* [MOOD @ 27:42]. A library is
therefore also a map of what your own defaults *can't* do.

---

## PART VI — THE MACHINE (system prompts + workflow graphs)

### Pattern 28 — Keep / Change: the entire edit-model grammar

> "If you think about it that way, **editing is keep this, change that.** It doesn't have to be any more
> complicated than that." — [CONFIG @ 10:52]

The formula, verbatim: `Keep: [things to keep]; Change: [things to change]`. His worked version:
*"Keep this exact product visible, preserve the fine details. Change: [whatever that might be]"*
[CONFIG @ 11:13]. The simplest possible case shown on stage: keep the bottle, change the background.

> "Now that we have a prompt formula — that keep-change little structure — that doesn't have to be for one
> image, that can be for a thousand images." — [CONFIG @ 11:33]

**Mechanism.** Edit models fail in exactly one direction: they drift on the thing you needed preserved,
because you only told them what to add. Naming the invariant *first and explicitly* is what pins it. And
because "keep" is constant across a whole campaign (the product) while "change" is the variable, the
grammar is natively batchable — it's the frozen backbone (Pattern 16) expressed for image-to-image.

### Pattern 29 — The system prompt is a brief for the LLM: six slots

> "The system prompt is basically just a brief for the LLM. You're telling it who it's acting as, what
> it's going to receive, what it's going to do with what it receives, how it should output, and then maybe
> some things of like what not to do." — [CONFIG @ 12:07]

The six-slot anatomy rail, read verbatim off the slide [CONFIG @ 12:22]:

| Slot | Definition on the slide | Example given |
|---|---|---|
| **Act As** | Who / how to respond | Photographer |
| **Input / Output** | What you get / how to output | Structured prompts |
| **Core Focus** | Place specific attention | Enhancing inputs |
| **Rules** | Direct instructions | Prompt details |
| **Format** | Output structure | Prompt format |
| **Limits** | Restrictions / limitations | Only the prompt |

And the complete production system prompt from the same slide, transcribed in full — the densest single
artifact in the corpus:

> **ACT AS:** Professional magazine photographer with a specialty in creating art directed prompts for ai
> image generators.
> **INPUT:** You will be provided with a text prompt and an image of a product. Take the user text prompt
> into high account when creating new prompts.
> **OUTPUT:** Your task is to generate (#) prompts — diverse + visceral for image generation.
> **CORE FOCUS:** Follow the rules formatting below to craft the prompts taking the users input and
> slightly altering to optimize for enhanced visuals.
> **RULES:** Follow the exact format below to craft each prompt. Always start the prompt with:
> *"Keep: This exact product visible and preserve the fine details. Change: [new image description]"*.
> Each prompt needs to end with an `*`. Each prompt should be between 120–175 words. Use powerful
> language — all prompts should be detailed + expressive.
> **FORMAT:** Format as a list: `[prompt1]*` `[prompt2]*`. Example prompt: *"Keep: This exact product
> visible and preserve the fine details. Change: Cyclist mid-training, AG1 bottle thrust at camera with
> wide-angle vertical crop, powerful sweat-soaked expression blurred in background, dramatic mountain
> horizon glowing behind with sharp contrast.*"
> **LIMITS:** No additional context, commentary, thoughts, analysis. JUST provide the raw prompts.
> DO NOT alter/change/suggest a new product.

Read what that prompt is actually doing: it hard-codes Keep/Change into the RULES slot, hard-codes a
terminator character so a downstream node can split the output, hard-codes a word band, carries one
verbatim exemplar, and closes every escape hatch in LIMITS. **Every slot is doing machine work, not
politeness work.**

> "You write it once, the model follows it, takes you out of the loop." — [CONFIG @ 11:57]

**Mechanism.** Deconstruction (Pattern 7) tells you the formula; the system prompt is how you *hand the
formula to a machine* so you stop being the one applying it. Note the terminator `*` — that single
character is what makes the LLM's prose output *parseable* by the next node. Format constraints in a
system prompt are not tidiness; they are the API contract between two nodes.

### Pattern 30 — Change the input, not the system

> "Once you have workflows that are pretty much standardized, you don't have to change much. **You only
> have to change the input.** So this entire system stays exactly the same. So instead of a Kodak Lancia,
> maybe I want a Polaroid F40. All I'm doing is changing the input. System takes over. It runs. I get new
> output. And when these workflows are built scalable and structured appropriately, **95% of the time they
> don't have to change.**" — [CONFIG @ 07:44–08:08]

**Mechanism.** The 95% figure is the whole design target. If a workflow needs editing every time it runs,
it isn't a workflow — it's a habit with extra steps. The test of a good graph is how much of it survives a
completely different input, and the way to get there is to push every variable to the edges (input nodes)
and keep every rule in the middle (system prompts).

### Pattern 31 — The text-iterator fan-out: one to N with two changes

The batch move, and it is deliberately anticlimactic:

> "Same structure here. We're only going to make a few changes. The system prompt section — instead of
> saying 'can you write one prompt for me,' let's just say 'write four.' And then we add this thing called
> the **text iterator**, which will split those four prompts into individual inputs. That gets sent to the
> image generator node, and all four will generate at once. So it's going to be one output — this could be
> four, this could be 400, whatever you want." — [CONFIG @ 14:20–14:45]

The slide labels the second change *"the only addition"* [CONFIG @ 14:32].

**Mechanism.** Scale is a *parameter*, not an architecture. If going from one to four assets requires a
different graph, the graph was wrong. This is why the terminator character in the system prompt matters —
the split is only trivial because the output was engineered to be splittable. **Design the parse target
before you need the batch.**

### Pattern 32 — The feeder image

> "We use Weave to composite the boxes digitally and then add the lighting depth and shadows to give it
> the 3D feel. **That becomes a feeder image for everything else we're doing.**" — [CONFIG @ 15:41]

> "So we can take that reference image and go create whatever we need. If we need stuff for banner ads, if
> we need stuff that looks like UGC, if we need stuff that looks like something just goofy for social —
> **that one image feeds everything else. So solving that one problem really helps.**" — [CONFIG @ 16:34]

**Mechanism.** Consistency is cheapest to enforce *upstream*. One canonical rendering, built carefully
once, is a stronger consistency anchor than any amount of prompt discipline applied independently to
fifty downstream generations — because every downstream asset inherits from the same parent rather than
converging on a description. It also relocates the expensive judgment to a single reviewable artifact:
approve the feeder, and the campaign is pre-approved.

### Pattern 33 — Manual where manual is better

The BarkBox graph is explicitly hybrid: element inputs (box art, toys, treats) → **manual composite by
hand in a compositor node** → flatten → *one* system prompt that adds lighting, depth and shadow → outputs.

> "We still manually composite everything with a compositor node within Weave. We'll flatten it and then
> we'll regenerate it with the lighting depth and shadow to give it the 3D feel… The compositor, we can
> still drag things around manually, control it the way you want to. And then it's all run by one system
> prompt." — [CONFIG @ 16:01–16:29]

**Mechanism.** Layout is a *decision*; lighting integration is a *rendering task*. He gives the model the
rendering and keeps the decision. This is the discipline that keeps a pipeline from becoming a slot
machine: every step asks whether a human is faster and more certain, and if the answer is yes, the human
does it. Note also how small the model's job ends up being — one system prompt, one transformation.

### Pattern 34 — The scale ref (fixing what the model cannot infer)

The named failure and its fix, from the BarkBox 2D→3D→studio-shot pipeline:

> "We have a lot of failure. A lot of times there's no context for how big something is. So we have to
> feed the details to give it an understanding of how big the toy is against the dogs. **Because if not,
> everything starts to get unproportional.** So all we're doing is giving the size of the toy against the
> size of the dogs. It creates this reference image. **This reference image becomes our new feeder image**
> to create the assets that we need." — [CONFIG @ 18:05–18:35]

The generated intermediate, read off the slide [CONFIG @ 18:28], is titled
`REFERENCE DIAGRAM: PROPORTION STUDY FOR NANO BANANA` — a technical-drawing-style plate on a dimensioned
3D grid, with a plush toy and small / medium / large dogs drawn to scale with approximate heights labelled.
The system-prompt node driving it reads *"Builds scale Ref / Using math + 3D depth."* The user-prompt node
supplies toy size and comparison sizes. Outputs on the right are labelled *"Better Outputs."*

**Mechanism.** Generative models have no unit system. They have no idea whether a plush toy is four inches
or four feet, so every shot re-guesses and every shot disagrees. The fix is not more adjectives — it's to
**manufacture the missing prior as an image**, in the visual language of a spec sheet, and hand it back as
context. This is the highest-leverage single trick in the Config talk and it generalizes cleanly:
whenever the model is failing at something it *cannot know*, generate an intermediate artifact that
encodes the knowledge, and make that artifact the reference. Scale is one case. Materials, seam logic,
layout grids and brand-colour chips are the same case.

### Pattern 35 — Quality control at every step, because you already work this way

> "You're not used to prompt and pray. That's not something that I was ever used to. You're used to
> building things in steps, piece by piece — **quality control at every step of the way.** If I wasn't
> going to just go from that first starting image to these last images: I want to create the body of the
> car. I want to apply the design to the car. I want to then take multiple angles of the car, and then I
> want to use that as a reference image to create all different variations of that car in real-life
> circumstances." — [CONFIG @ 07:09–07:37]

**Mechanism.** "Prompt and pray" is a single-step process with a single inspection point at the end, so
every defect is discovered after all the compute is spent and every fix is a full re-roll. A staged graph
puts an inspection point after every transformation, which means defects are caught where they're cheap
and where the cause is unambiguous. He frames it as familiar on purpose — designers *already* work in
stages; the node graph is just that habit in a new medium.

---

## SIGNATURE MOVES (the repeatable tactical set)

1. **The Non-Negotiables Sweep.** Before running any prompt, walk the nine Image Elements and ask which
   ones you have left silent. Every silent one is a decision handed to the model. Fill or accept.
2. **Frozen Backbone / Variable Head.** Split the nine into aesthetic (freeze) and content (vary).
   Concatenate. That's your brand-consistent asset system, and it's one string operation.
3. **Left-Anchor Swap.** Before adding words to a failing prompt, rotate which term sits first. Four runs,
   four legitimately different images, zero new vocabulary. Structure before vocabulary, always.
4. **Keep / Change.** Every image-to-image instruction opens by naming the invariant, explicitly, first.
   `Keep: [invariant]. Change: [delta].`
5. **The Null-Prompt Sweep.** Characterize any style asset — board, `sref`, profile code, inherited or
   purchased — with a period or slash as the entire prompt, then with one neutral photographic probe
   ("editorial photography"). Only then trust it in production.
6. **The Solo → Stack Ladder.** One prompt held constant. Global alone → each asset solo → pairs → one at
   a time. Diff, then **write the winning combinations down as named recipes** or the sweep never happened.
7. **Micro-Board Seasoning.** Build ~5-image single-effect boards (grain, chrome, negative, texture,
   iPhone) whose only job is to be stacked onto something else. Composability beats completeness.
8. **The Opposition Stack.** Pair opposites deliberately — gritty × ethereal, mono × saturated — and keep
   one deliberately flat board on hand as a **brake** for over-stylised output.
9. **Sweep the Weight, Don't Guess It.** Every reference mechanism has a coefficient. Batch the range in
   one submission using whatever the current tool's permutation facility is. Knowing a feature without
   knowing its dial, range and default isn't knowing it.
10. **The Feeder Image.** Build one canonical composite carefully; every downstream asset references it
    rather than re-describing it. Approve once, inherit everywhere.
11. **The Scale Ref.** When the model cannot know something (proportion, seam logic, material, layout),
    generate a spec-sheet-style reference diagram that encodes it, and make that diagram the reference.
12. **The Text-Iterator Fan-Out.** Ask the LLM for N instead of 1, terminate each item with a parse
    character, split, fan out. Scale is a parameter.
13. **Go Deep On The One.** When a frame hits, stop bashing: vary-strong and remix-strong the winner
    repeatedly. Breadth finds direction; depth finds the asset.
14. **The Imperfection Pass.** End photoreal pipelines with a step that *adds* damage — pores, blemishes,
    knuckle skin, veins, grain. Never end on cleanup.
15. **The Handoff Test.** State the workflow as a type signature: "any X goes in, Y comes out." If you
    can't, judgment is still stuck in the middle of the pipe.

---

## QUALITY RUBRIC — how he separates good from bad

**On an image**

- Does it read as a *photograph*, or as a render? His `/describe` verdict is the standard: *"this kind of
  looks like crap. It looks like video games. It doesn't look like a real image."*
- Is the skin too clean? Are the hands too polished? Polished = fake. The tell is smoothness.
- Would a detail-oriented eye find something wrong? He assumes yes and ships anyway when the economics
  justify it: *"Is it 100% accurate? No. A detailed eye will find something wrong with this every single
  time"* [CONFIG @ 03:18]. **Fidelity is a budget line, not an absolute.**
- Is it close enough to a real existing photograph to be a liability? Reverse-image-search before it goes
  commercial.

**On a set of images**

- Does the backbone hold? Same color scheme, lens/film, lighting, composition across every asset?
- Is the variation in the *head* (shot type, subject, environment) rather than the aesthetic?
- Proportions consistent across shots — or did each generation re-guess the scale?

**On a workflow**

- Can somebody else run it? (*"If only you can operate it, then it's not really a system."*)
- Does going from 1 asset to 400 require a different graph, or one number?
- Does it survive a model swap?
- Does 95% of it stay fixed when the input changes completely?
- Is there an inspection point after each transformation, or only at the end?
- **Did it actually save hours, measured?**

**On a style asset**

- Has it been characterized on a null prompt, or is it just a folder of images you like?
- Does it have a name and a one-line behaviour note?
- Do you know which other assets it stacks well with, and at what weights?
- Is it doing one job well (micro) or many jobs vaguely (unfocused broad)?

---

## VOICE PROFILE

**Register.** Practitioner, fast, unpretentious, slightly self-deprecating. Says "right?" constantly as a
comprehension check. Uses "you know" as filler. Swears mildly for emphasis. Talks in second person and
addresses the room's actual job ("you're a designer, you're a marketer, you're an entrepreneur").

**Positioning.** Deliberately non-expert about craft. *"I am not a designer. I am not a media buyer. I'm
none of those things really. I just try to solve common problems."* [MJM @ 01:16]. And on his own company:
*"a company you've probably never heard of"* [CONFIG @ 01:59]. He earns authority by describing operations,
never by claiming taste.

**Structure.** Problem → why it's a real problem → the smallest version of the problem → the mechanism →
a live build → a client case → "here's what to remember." Always closes on a short list of durable
principles rather than a tool recommendation.

**Tells.**
- "Right?" as a beat between clauses.
- "So again…" to loop back to the thesis.
- Naming things plainly: creative inflation, non-negotiables, asset hacking, feeder image, scale ref.
- Undercutting his own demo: *"that's actually a mistake. So again, everyone is getting to see what this
  looks like in real time. We're not all perfect."* [MJM @ 44:39]
- Volunteering the disclosure nobody asked for (mock work, AI stigma, copyright exposure).
- Deflating the magic: "not a lot of things have to change," "the only addition," "four clicks and we're
  here," "it doesn't have to be any more complicated than that."

**What he never does.** He never says a tool is the answer. He never claims an output is perfect. He never
teaches a prompt to copy — he teaches the formula that generates prompts. He never uses "in the style of."

**Closing posture.** *"Be flexible… be scalable… be yourself. You're the reason you're here. You don't have
to change. Just evolve a little bit."* And: *"Just do weird stuff."* [CONFIG @ 20:29–21:11]

---

## APPENDIX A — ERA-BOUND MECHANICS (verify before use)

**Read this section as history, not as instruction.** Everything below is a tool mechanic tied to a
specific product at a specific date. It is recorded because it shows *how the durable principle was
implemented at the time* — which is useful for recognising the equivalent handle in whatever tool is
current — and for no other reason. **Nothing here ships into a prompt or a workflow without being
verified against the live tool first.** His own rule governs: *"screw the models… every model I've
mentioned here, they're all going to change"* [CONFIG @ 20:30, 2026].

### A.1 — Midjourney v6 era (2024) — source [MJM], recorded 2024

| Mechanic | As stated then | Durable principle it implements |
|---|---|---|
| `/describe` in Discord — upload an image, get four candidate prompts | [MJM @ 23:34] | Pattern 18 — machine caption as raw material |
| The "alpha site" as the new non-Discord interface, "live for everyone in the next couple of weeks" | [MJM @ 44:02] | — (pure product news, now historical) |
| **Image weight** parameter: range **0.25–2**, default mid; low = closer to the text prompt, high = closer to the image | [MJM @ 49:16–49:41] | Pattern 23 — every reference has a coefficient |
| **Permutation prompting** via curly braces — `{0.5, 0.6, 0.7, 0.8, 0.9, 1}` generates each variant in one submission | [MJM @ 48:43] | Pattern 23 / Signature Move 9 — batch the sweep |
| `--stylize`, `--chaos`, aspect ratio named as the parameters most people never learn | [MJM @ 55:57–56:16] | "Sometimes it's just a parameter, sometimes it's the structure" — Pattern 10 |
| **Vary-region**: paint over a failed hand and regenerate only that area; optionally image-prompt inside the region | [MJM @ 53:54–54:04] | Pattern 15 — local repair as a routing path |
| Generate **low-res first** to win the hands, then upscale | [MJM @ 54:25] | Pattern 15 |
| **Magnific** as the imperfection/upscale pass — adds lines, blemish, bags, skin texture, veins | [MJM @ 35:35–36:24] | Pattern 14 — the last step adds damage |
| **InsightFace / InSwapper** for face swap; "the important part is having the facial structure somewhat match — a fat person on a skinny face is not going to look right" | [MJM @ 51:01–51:45] | Identity lock via reference, not prompt |
| Copy a job ID and `show` it in Discord to move a web generation back into the Discord toolset | [MJM @ 51:32] | — |
| Named v6 failure list: hands, stairs, reflections, too many subjects | [MJM @ 56:50–57:40] | Pattern 15 — maintain a *current* failure inventory |
| Consistent characters described as hard/unsolved and on the roadmap | [MJM @ 60:02–60:25] | **Superseded.** Treat as solved-elsewhere; see `mickmumpitz` lane when extracted |
| Reverse-image-search commercial output (he names dupli-checker) before it ships | [MJM @ 38:43–38:56] | **Still current as a rail** — the tool name is era-bound, the practice is not |

### A.2 — Midjourney v7 / moodboard era (2025) — source [MOOD], recorded 2025

| Mechanic | As stated then | Durable principle it implements |
|---|---|---|
| Moodboards as a first-class feature; boards can be stacked in one prompt | [MOOD, throughout] | Patterns 20–22 — self-minted tokens, tiers, stacking |
| Profile codes (`--p`) built from curated image sets; a "global profile" from personalization sits on top | [MOOD @ 16:24]; roryflynn.gumroad.com | Pattern 27 — several classes of handle, layered |
| Global profile can be weighted *against* the moodboards | [MOOD @ 16:38] | Pattern 23 — second-order weighting |
| `sref` codes and `sref` weighting named as the thing most trainees can't do | [MOOD @ 06:16–07:35] | Pattern 23 |
| Style-version (`sv`) as a separate dial — "sv1 still produces bangers" | [MOOD @ 07:39–07:46] | Old versions of a dial remain useful; don't assume newest = best |
| `--stylize` around 600–650 named as his working sweet spot; aspect 3:4 / 2:3 as habitual | [MOOD @ 19:00, 30:37] | Personal defaults, not law |
| Running a **period or slash** as the entire prompt to characterize a board | [MOOD @ 35:02] | Pattern 24 — **this one is generic enough to survive**; any generator accepts a near-null prompt |
| "Remix strong" / "vary strong" to branch off a winning frame | [MOOD @ 26:22–26:35] | Pattern 26 — branch from the winner, not the prompt |
| His own scaling complaint: 40–50 boards and no retrieval system | [MOOD @ 29:36] | Pattern 25/27 — the library problem is unsolved even for him |

### A.3 — Node-graph era (2026) — source [CONFIG], recorded 2026

Current at time of extraction; still verify, because this era will date too.

| Mechanic | As stated | Durable principle |
|---|---|---|
| **Figma Weave** as a node-based workflow builder, ~300+ AI tools in one workspace, infinite canvas | [CONFIG @ 05:49] | Pattern 31/35 — staged graphs over prompt-and-pray |
| **Router node** — one input fanned to multiple outputs | [CONFIG @ 13:47] | Fan-out |
| **Text iterator node** — splits an N-item LLM output into N individual generator inputs | [CONFIG @ 14:29] | Pattern 31 — scale as a parameter |
| **Compositor node** — manual drag-and-arrange inside the graph, then flatten | [CONFIG @ 16:01] | Pattern 33 — manual where manual is better |
| **Nano Banana** as the image model referenced by name on his slides (saliency diagram; scale-ref plate titled "…FOR NANO BANANA") | [CONFIG @ 09:46, 18:28] | Model name, fully era-bound |
| Font/typography generation: sans-serif template + reference image → ChatGPT → Claude Code → sliced OTF and vector files, ~30 minutes | [CONFIG @ 02:36–03:15] | "Just do weird stuff" — adjacency, not a taught workflow |
| Micro use cases panel: retouching, ecomm assets, localization, composition, environment fixes, compositing, asset dims, full campaigns, product swap | [CONFIG @ 19:30] | Pattern 2 — where small solved problems spread to |

### A.4 — Not carried into this skill at all

- The **2023 LinkedIn photorealism cheat sheet** (activity-7074452340103114752). The post is verified to
  exist; its content is an image asset behind a login and was never read. **No token list from it has been
  reconstructed, guessed, or paraphrased into this skill.** What the skill carries instead is the
  photography-language *doctrine* he teaches on camera (Patterns 11–13). If the PDF is ever obtained, it
  extends `workflows/photorealism-language.md` — and it should be re-dated on arrival, because a 2023
  token list is three model generations old.
- The claimed "176 photorealistic prompt tokens / 20 parameters / 20 style codes / 14 photographic
  elements" inventory of a later cheat sheet — third-party search snippet only, UNCONFIRMED, cited nowhere.
