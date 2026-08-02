# Nick St. Pierre — Judgment, Taste Heuristics, and What He Actually Checks

Creative Director, Original Creative Agency. @nickfloats. The person a16z's Matt Bornstein called
having *"deeper intuition around how to control AI image models than anyone else."*

Read this for the **judgment**. `SKILL.md` carries the method; `references/era-bound-mechanics.md`
carries the dated tool syntax. Every quote below is verbatim with its date.

---

## The one-line thesis

**Direction is a sequence of controlled decisions; prompting is just where the decisions get
typed.** Everything he does is an attempt to convert a random-feeling generator into an
instrument that responds to one variable at a time — so that a result can be *attributed*, banked,
and repeated, rather than merely liked.

His own framing of why the framework exists (2023-03-02):

> "Additive Prompting is by no means the 'correct' way of prompting. It's a framework I developed
> to better understand the impact & interplay of variables in my prompts on the overall
> composition of my images."

Not "the right prompt." **Understanding the interplay of variables.** That is an art-director's
problem statement, not a prompter's.

---

## Pattern 1 — The control prompt: hold everything, move one thing

Every study he publishes fixes a base string and moves exactly one slot. From the film-stock guide
(2023-02-04):

> "For easy comparison, all images in this thread are [street style] photo of [a woman], shot on
> [Film Type]"

Then the next day, same subject, one new slot (2023-02-05):

> "Same base prompt as yesterday, this time with [lighting]"

Then the next (2023-02-06): *"Same base prompt as yesterday, this time with [Shot Type] &
[Position]… I'll note when changes are made to this prompt."*

**The mechanism:** with a fixed control, a difference in the output is *caused* by the one token
you moved. You are no longer collecting pretty images — you are measuring the model's response
curve for a specific direction lever. That is what makes the result bankable: you learn what
"Cinestill 800T" *does*, not merely that one image with it looked nice.

**The failure this prevents:** rerolling. Rerolling changes everything at once and teaches you
nothing; you end up with a folder of luck and no vocabulary. When he does want randomness he says
so explicitly and treats it as a separate act (2026-06-25, on batch draft with random style refs:
"explore style space 24x faster").

**How to tell it's being done wrong:** two images in a comparison differ in more than one slot.
His own discipline on this, when asked how he holds a face steady across looks (2023-02-08):
*"It also helps to have simple prompts where you only change a single, specific variable."*

## Pattern 2 — Lock the winner, then add the next layer

The sweep is not a survey; it ends in a decision. Mid-way through the fashion study (2023-02-07),
after sweeping four designers:

> "I liked Gucci and stuck with that one as I started playing with the outfit."

Designer gets locked. *Then* color sweeps against locked designer. Then material sweeps against
locked designer + locked color. Each layer inherits every decision above it.

**Why this is the whole discipline in one move:** it converts an exponential space into a linear
one. Four films × eight lightings × six shot types × five palettes is 960 combinations you will
never see; four, then eight, then six, then five sequential comparisons is 23 decisions you
actually make. **The output of a session is a decision path, not a folder.**

**The layer order he actually worked in** (Feb 2023 series, in publication order): subject +
medium → film stock / emulsion → lighting → shot type & camera position → wardrobe, color,
material → atmosphere & ambiance → location & time of day → mood descriptors. He said out loud
what the order was for (2023-02-05): *"We'll be working our way up to more complex scenes as we
go."* Foundation first, styling later, mood last.

## Pattern 3 — Compensating tokens: know what the model drops, and pay for it

His shot-type guide is not a glossary; it is a list of the places where asking for a thing does
not get you the thing (2023-02-06):

- **Medium shot** — *"To achieve a proper Medium shot you'll want to specify some body language,
  like [walking], or [sitting]. If not, you'll tend to get a med close-up."* The framing is
  bought with an action, not with the framing word.
- **Low / high angle** — *"I like to include [from below] in the prompt for low-angle shots"* /
  *"[from above]"*. The angle word alone under-delivers; the spatial phrase reinforces it.
- **Wide shot** — *"For wide shots, you'll want to add context for what's going on in the
  background."* A wide frame with nothing specified for the background is a wide frame of nothing.
- **Emotion** — *"I find more descriptive words like [overjoyed] produce better results than
  [happy]."* Generic affect words are weak; specific ones land.

**The general law:** a direction word names an intent; a **second, concrete token supplies the
evidence the model needs to execute it.** Angle + spatial phrase. Framing + body language. Wide +
what's out there. Emotion + specificity. This survives every model change, because it is about
under-specification, not about a parser.

## Pattern 4 — Aspect ratio and lighting are the true drivers of "cinematic"

The taste call in this corpus that pays off most often (2023-02-26). He built a shot by combining a
character prompt with an interior prompt and observed:

> "If you read the prompts, there's no 'cinematic' reference, yet it has a cinematic feel. I've
> found aspect ratio and lighting to be the true drivers of cinematic looks."

And then, honestly, the qualifier: *"Adding in 'Cinematic Shot' at the beginning doesn't seem to
hurt though. Also, things like 'Dramatic' or 'Volumetric' lighting seem to add to the cinematic
feel, but it all depends on the shot you want."*

**The judgment:** adjectives about a *look* are the weakest lever available. The look is produced
by the physical facts of the frame — its shape and how it is lit. Asking for "cinematic" is asking
the model to guess which cinema; specifying 2:1 and volumetric backlight *is* the cinema.

Generalise it: **whenever you are tempted to name a quality, name the physical cause of that
quality instead.** "Luxurious" is weak; marble, brass, velvet, jewel tones and a chandelier are
strong. He does both — but the nouns do the work and the adjectives close.

## Pattern 5 — Contrast as the anti-slop lever

His stated route out of generic AI aesthetics (2024-01-30):

> "High contrast prompts always lead to such sick results… Contrast in lighting, colors, textures,
> art styles, genres, film stocks, perspective, etc. Lean into the contrast, see where it takes
> you."

His framing in the 12-guides Article (2024-02-29) makes the target explicit: contrast is how you
*"make your images pop and stand out against the boring and lazy AI aesthetics you see posted all
over the internet."*

The worked example is worth studying because the contrasts are **stacked deliberately in seven
dimensions at once**: a mezzotint (illustrative) crossed with photo (medium contrast), rendered on
the anime model for photographic content (model contrast), a Sukeban figure in platinum chainmail
(subculture × material), on a Martian vineyard (genre collision), deep red soil against muted
naturals (palette contrast), subject positioned *above* the vineyard (perspective contrast), on
Cinestill 800T (stock contrast against a daylight scene).

**The check:** *what in this frame is in tension with what?* An image where every element agrees
with every other element is the definition of the AI default look. Slop is not a resolution
problem or a prompt-length problem — **slop is the absence of tension.**

## Pattern 6 — Never name a quality the tool can fake; never name an artist

Two anti-patterns he states flatly.

On quality buzzwords (2023-12-30), under **Things to avoid**:

> "Style buzzwords like 8k, vray, HDR, etc"
> "Prompts that are just comma-separated keywords"

And under **Ways to troubleshoot**: *"Remove 'vibey' terminology."*

On artists (2024-03-21):

> "I don't use artist names in my prompts. Never have."

**Why this is judgment and not squeamishness:** an artist's name is a compression of a thousand
decisions you did not make. It gets you a plausible pastiche and it gets you no vocabulary — you
cannot sweep it, you cannot decompose it, and you cannot explain to a client what produced the
look. Film stocks, lighting names, lens behaviour and materials are decomposable; "in the style of
[artist]" is not. The same objection applies to `8k` and `HDR`: they are quality *assertions*, not
direction.

## Pattern 7 — Reference over adjective (the 2024 hinge, the 2025 doctrine)

By 2024-03-21 he had reduced the text half of the job to three slots:

> "Text prompts really only need 3 things: {medium} {subject} {environment}. Almost all other
> details can be driven by image references now… Now is the time to start getting comfortable
> using images in your prompts."

By 2025-12-04 this had become a full position — the most important thing he has written:

> "Text-first prompting is a terrible UX. Language models came first, so we made visual tools
> speak in paragraphs, even though visual artists don't work in paragraphs. Most of us aren't
> walking through a museum, thinking 'ahhh yes, it's the chiaroscuro combined with the desaturated
> palette creating a melancholic intimacy thats doing it for me.' **Visual preference isn't
> linguistic. We just see it and we know. The eye knows what the mouth cannot say.** … The craft
> won't (and shouldn't) be about finding the right adjectives. It'll be **a collection of choices
> that shape your preferences and refine your tastes until the tool thinks like you do.** … the
> most interesting art is the kind you don't have the words for yet."

**What this means operationally:** the deliverable of a direction session is not a great prompt.
It is an accumulating set of **visual choices** — reference images, style codes, moodboards,
palettes, locked characters — that carry taste forward without needing to be re-described. The
text prompt shrinks toward medium/subject/environment as the reference library grows.

He restates it as a scoring rule in 2026 (2026-02-20), objecting to a base-model comparison:

> "this is also a base model comparison, no style references, parameters, moodboards, etc, which
> all provide additional aesthetic control."

**A judgment that follows:** never evaluate a model — or your own work — on raw text-to-image
output. That measures the model's defaults, not your direction. The gap between the two is the
entire job.

## Pattern 8 — The image is the substrate, not the output

Three separate demonstrations of the same idea.

- **Character lock (2023-02-18):** a portrait becomes the seed; the same prompt plus the image
  plus a fixed seed carries a face into new clothing, poses, locations. *"It starts with a model,
  and it seems to work best with a head and shoulders portrait photo."*
- **Composite direction (2023-02-26):** *"if I combine my Character Prompt + Interior Prompt, I
  end up with a Cinematic Shot."* Two banked prompt-objects compose into a third kind of shot.
- **Motion (2025-06-25):** *"Everything in this video was generated from a single frame,
  directing the character into different scenes over time with extensions."* And (2025-06-23):
  *"Incredibly impressed with how well Midjourney video follows direction and maintains style
  across video extensions… This was generated from a sequence of six prompts."*

**The doctrine:** every still you make is potentially a seed, a style source, a character anchor,
or the first frame of a shot. Direct the image as an asset with descendants, not as a deliverable
that ends when you like it. This is why the image layer is where craft pays back
most — video, boards, worlds and campaigns are all downstream of it.

## Pattern 9 — Casting, not generating

Language he uses without irony (2023-02-18/19):

> "I'm currently in the process of casting some new models."

And the accompanying craft observation:

> "I've found models that have a more unique/distinct look are more likely to result in consistent
> results."

**Two things at once.** First, the frame: you are casting a face, then shooting it in wardrobe,
in locations, under lighting — the vocabulary of production, applied deliberately. Second, a real
technical insight with a plain cause: a distinctive face occupies a sparser region of the model's
distribution, so re-generations land closer to it. Generic-pretty faces drift because
generic-pretty is the mode.

**The practical rule:** when you need consistency, cast *against* the average on purpose.

## Pattern 10 — Publish the limits with the method

He is unusually honest about failure, and it is a craft signal, not modesty. From the interiors
thread (2023-02-23):

> "The images aren't picture-perfect. They can be a bit blurry at times."
> "Adding too many specific furniture items can sometimes confuse it. I try to limit myself to 3
> max."

From the character thread (2023-02-19): *"you might not get as much consistency, but with the
right prompt & enough variations, you'll get some good ones."*

From the blending thread (2023-02-26): *"I noticed when blending like this I need the lighting in
the source images to match to achieve realism, & I get locked into the perspective of my source
images."* — and the conclusion: *"Image blending can work, but it's not very consistent."*

On camera distance and faces (2023-02-12): *"the further from the camera the subject gets the
worse the facial construction/details get."*

**The pattern behind the pattern:** he does not report a technique without reporting its
*operating envelope* — where it holds, where it breaks, what it costs. A direction system that
only lists what works is a sales pitch. **Knowing the failure mode is what lets you choose a
different lever instead of grinding rerolls.**

Also note the *density budget* implied by "3 furniture items max": specificity is a limited
resource. Spend it on the things the shot is about, and let the model fill the rest. He says this
directly when blending (2023-02-26): *"I removed a lot of variables… keeping the shot type,
subject, pose, location style, lighting, and descriptors. The images fill in the rest."*

## Pattern 11 — Combo Commands: describe one idea from several angles

His own coined term (2023-02-10):

> "A 'Combo Command' is my term for using multiple variations of a single idea to help Midjourney
> understand the intention of key phrases."
> "The benefits of Combo Commands are twofold: they produce more consistent outputs; they let you
> assign color or even blend colors w/ minimal impact on other items in your scene, such as the
> model's clothing."

Paired with a precision observation: *"Midjourney also does a pretty good job distinguishing
between particle sizes of similar conditions such as 'Misty' … and 'Steamy'. Notice the difference
in density and visibility?"*

**Two durable lessons.** (1) When a single word is doing too much work, **triangulate it** — say
the idea three neighbouring ways so the intended sense is the intersection, not the model's guess.
(2) **Atmosphere is a physical variable with resolvable grades** — mist, fog, steam, haze, smoke
differ in particle size, density and visibility, and a director who knows the difference gets it.
He names the same rigour for light: *"For lighting there are 3 approaches I like: use the time of
day (morning/evening); use weather conditions (sunny/overcast); use backlight & side light.
Combining these 3 into unique lighting Combo Commands produces even better results."*

## Pattern 12 — Cross-tool grammar: the same spine on a different model

He is a Midjourney partisan, which makes this the more useful evidence. Directing Nano Banana Pro
(2025-11-20) — not Midjourney, no parameters, pure prose — the structure is exactly his spine:

> "A **medium shot** of the 14 fluffy characters sitting squeezed together side-by-side on a worn
> beige fabric sofa and on the floor. They are all facing forwards, watching a vintage,
> wooden-boxed television set placed on a low wooden table in front of the sofa. The room is
> **dimly lit, with warm light from a window on the left and the glow from the TV illuminating**
> the creatures' faces and fluffy textures. The background is a cozy, slightly cluttered living
> room with a braided rug, a bookshelf with old books, and rustic kitchen elements in the
> background. **The overall atmosphere is warm, cozy, and amused.**"

Medium → subject with explicit spatial arrangement and facing → **named light sources with
directions** ("from a window on the left," "the glow from the TV") → environment inventory →
one mood sentence to close. No buzzwords, no artist names, no parameters. **The grammar survives
the model change** — which is precisely why it is worth learning as craft rather than as MJ trivia.

## Pattern 13 — The delta is the direction, and taste is the scarce input

His 2026 position, stated repeatedly.

> "The delta between the AI content you typically see on X and what a true storyteller like
> Darren Aronofsky manages to produce with the same tools is truly insane." (2026-01-29)

> "We invented one of the most beautiful and expressive creative mediums to ever exist and you're
> using it to automate UGC campaigns with fake influencers on tiktok." (2026-01-28)

> On Paul Graham's *"In the AI age, taste will become even more important. When anyone can make
> anything, the big differentiator is what you choose to make"* — **"Maybe you nerds will listen
> now that Paul has said it."** (2026-02-14)

And the older, sharper version of the same conviction, on authorship (podcast, ~2023, [10:14]):

> "If you're just writing a prompt that generates an output… that image isn't your art. You wrote
> the prompt and it's your idea, but that image isn't your art… it's about intent and it's about
> process… the point that you can bring in to actually transform it into something that's truly
> beautiful… is going to be your own story, your own authentic addition to the narrative."

> "What I share, what I post, is research, it's experimentation, it is not art." [12:06]

**Why this matters to the craft and not just the ethics:** if the tools are common and the delta
is direction, then the only defensible investment is the accumulation of taste and reusable
decisions — style banks, locked characters, moodboards, a documented sweep history. That is
exactly what his method produces as a by-product.

---

## What he checks, in order, looking at a generated image

Reconstructed from what he consistently comments on across the corpus. Use as a critique pass.

1. **Is one variable responsible for the difference?** If not, the comparison teaches nothing —
   rebuild the control (Pattern 1).
2. **Did the framing actually arrive?** Medium shot that came back a medium close-up, wide shot
   with an empty background, low angle that reads eye-level → a compensating token is missing
   (Pattern 3).
3. **What is in tension here?** If nothing, the image is on the default aesthetic and will read as
   slop no matter how clean it is (Pattern 5).
4. **Is the light *named* and *placed*?** Source, direction, quality, time of day — or is it just
   "beautiful lighting"? (Patterns 4, 12.)
5. **Is anything a quality-assertion rather than a direction?** 8k, HDR, ultra-detailed, an artist
   name → cut and replace with the physical cause (Pattern 6).
6. **Are the materials and textures stated?** He requires at least one or two texture references
   in any built environment (2023-02-23: *"It's important to include at least 1 or 2 texture
   references like metal, linen, wood, etc"*).
7. **Is the specificity budget over-spent?** More than ~3 specific objects, or a detailed setting
   fighting detailed subjects, muddies everything (Pattern 10; 2023-12-30: *"prompts w/ many
   specific details about multiple subjects may get muddied by a very detailed setting
   description… If things get crazy, remove some of the specifics"*).
8. **Face fidelity vs camera distance** — is the shot asking for a face at a distance the model
   can't hold? (Pattern 10.)
9. **Can this become a seed?** Is it clean enough, distinctive enough, and consistent enough to
   anchor a character, a style, or a first frame? (Pattern 8.)
10. **Would this have looked the same without me?** If yes, no direction happened (Pattern 13).

---

## Voice, for anyone writing as him

Lowercase-casual, generous, technically exact. He publishes prompts in ALT text so people can
steal them, and says why (podcast, [17:33]): *"I'm not here to hold the secrets from you and just
post pretty images."* When someone offered to pay for his content (2023-03-06): *"thats a nice
thing to say. but you wont have to pay for anything. giving you all the info for free. ill make
the brands pay me for your eyeballs later."*

He hedges precisely and never oversells — "I've found," "it seems to work best," "this was a happy
accident I found through experimentation," "I have no idea" when he doesn't. He is scathing about
laziness and about exploitation, warm about other people's work, and allergic to the label
"AI artist." He describes his own obsession without embarrassment — going *"manic"* on control in
January 2023, chasing *"authoring at the speed of thought."*

Signature moves in his prose: name the technique, show the exact prompt, show the failure, invite
you to remix it, tell you what he's still testing.
