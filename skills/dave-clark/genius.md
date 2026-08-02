# Dave Clark — Genius Context

> Co-Founder & Chief Creative Officer, Promise. Two decades of traditional film and commercial
> directing (Coca-Cola, Snapchat, HP, Warner Bros., Intel) before generative tools existed.
> *Borrowing Time*, *Dismal Swamp*, *Battalion*, *Another* (Cannes Next 2024), *NinjaPunk*,
> *My Friend Zeph*, *Hardcore 94*.
>
> **The axis he owns: the layer above tool craft.** Everyone else in this space teaches syntax.
> Clark is the one who can tell you, in a DP's vocabulary, why the image you just generated is dead —
> and the one shipping AI work through Netflix/Amazon QC and studio chain-of-title.

---

## How to read this file

**Everything in the core method below is model-independent.** It survives Runway → Veo → Sora → whatever
ships next quarter, because none of it is about a model. It is about direction, selection, coverage,
cadence, light, colour space, and provenance — the things that were true with an Arri and will be true with
whatever replaces the current generation of generators.

**Tool-specific mechanics are quarantined in [Appendix A](#appendix-a--era-bound-mechanics-202324--verify-before-use).**
Those came from 2023-11 and 2024-02 sources. They are historically accurate and operationally stale.
Never build a deliverable on them without verifying against the current tool state.

Source keys, exact publication dates, and the full fidelity ledger: [`references/source-notes.md`](references/source-notes.md).
`[REEL-obs]` = observed from 28 frames of his 2025-02-17 Promise director reel, not stated doctrine.
Source weighting: **[FORBES26] 2026-07-24** and **[NFS] 2025-11-04** are primary; **[EVERY] 2024-02-28** and
**[FWAI] 2023-11-18** are historic and mined only for what transcends their tool era.

---

## The thesis in one line

> *"To me, the future of AI is just filmmaking… I think at the end of the day, the goal is for AI to become
> an afterthought."* — [CANNES, 2025-06-24 @ 00:53]

Every pattern below is downstream of that. If the AI is the interesting part, the film has failed.
Flat AI video is video where the *technology* is the subject. Cinematic AI video is video where a person made
a hundred small directorial decisions and the technology disappeared behind them.

---

## THE FLAT-VS-CINEMATIC AXIS (the thing this skill exists for)

Clark never published a framework for this. What follows is assembled from his stated practice plus the
observed signature of his own reel — every line traceable, every claim tagged. This is the diagnostic spine
of the whole skill, and **none of it references a model.**

### Why AI video comes out flat — the eight causes, ordered by how often each is the real one

| # | Cause | The tell | Source |
|---|---|---|---|
| 1 | **One generation deep.** Not a prompting problem — a *selection* problem. | Everything in the piece is a first take. | *"I talk to a lot of people and they're like, dude, how does your stuff look like that? I go on [a generator], my stuff looks like crap, it's all warpy. I was like — how many generations you do? Well, just one."* [EVERY 2024 @ 59:42] |
| 2 | **Metronome cutting.** Uniform clip length is the loudest AI tell there is. | 3s, 3s, 3s, 3s. The eye clocks the tool's max duration. | *"It's not just 3 second clip after 3 second clip after 3 second clip."* [EVERY 2024 @ 19:29] |
| 3 | **Unmotivated, omnidirectional light.** The models' default is soft global illumination from nowhere. | You cannot point at where the light is coming from. Face evenly lit. Shadows lifted grey. | [REEL-obs 2025] — zero front-lit frames in 28; every frame has one nameable source, usually behind the subject |
| 4 | **Clean air.** No atmosphere in the mid-ground, so the planes collapse into a poster. | Depth comes only from lens blur, never from anything physically between camera and subject. | [REEL-obs 2025] — mist/haze/smoke/water/dust/spark in every single frame |
| 5 | **No capture layer.** Digitally immaculate, therefore never photographed. | No grain, no gate weave, no handheld micro-motion, no lens artifact. | *"[The] handheld look that I created… as an adjustment layer… helps cover up a lot of the inconsistencies between shots."* [FWAI 2023 @ 16:13]; [REEL-obs 2025] telecine burn-in at t=00:19 |
| 6 | **No coverage.** Every shot is a new setup, so nothing reads as a *scene*. | Cuts feel like a slideshow of unrelated postcards, not like a place you're standing in. | [FWAI 2023 @ 15:57] — see Pattern 7 |
| 7 | **Adjective prompting.** "Cinematic, moody, epic, 8k" is a wish, not a direction. | The prompt could describe a thousand different images. | [EVERY 2024 @ 27:29] — he replaces adjectives with a named film *plus the reason it looks that way* |
| 8 | **Nothing at stake.** The novelty carries eight seconds and then nothing does. | You can't say what the piece is *about* in one sentence. | *"You still need to actually have an idea, you have to know how to tell a story, or you're just going to get a bunch of crappy AI generated videos."* [FWAI 2023 @ 06:45] |

**The load-bearing insight:** six of these eight are fixed *after* generation or *before* it — in selection,
editing, coverage planning, and reference discipline. Only two are prompt problems, and neither is a
model-choice problem. That is why prompt-craft skills plateau at "impressive clip" and never reach "watchable
film." **Flatness is almost never a prompting failure. It is a directing failure wearing a prompting costume.**

And it is why swapping models does not fix it. A better generator moves cause #3 and #4 slightly. It moves
causes #1, #2, #5, #6, #7 and #8 not at all.

### What cinematic looks like in his own frames — the observed signature [REEL-obs, 2025-02-17]

Seven things true of all 28 frames, across WWII swamp, WWII naval, sci-fi mech, cyberpunk alley, school
brawl, monolithic pyramid, astronaut:

1. **One dominant motivated source, behind or beside — never in front.** Rim and edge separation does the
   work. In several shots the face is the *least* lit part of the frame.
2. **A real black point.** Shadows land on actual black. Highlights are allowed to clip at source (fire,
   flare, rim). The register he names out loud: *"whites are really white and blacks are really black."*
   [EVERY 2024 @ 27:43]
3. **Atmosphere in the mid-ground, always.** Nothing is shot through clean air.
4. **Desaturated cool base + exactly ONE warm accent family.** Teal/slate/graphite, with fire or sodium or a
   red practical as the only warm. Never two competing warms.
5. **Foreground occlusion.** The camera looks *through* something — a post, a doorway, a shoulder, a gate.
   Depth is built out of planes, not out of blur.
6. **A capture-artifact layer** — grain, gate weave, telecine burn-in, handheld micro-motion.
7. **Anamorphic-wide framing with the human small in the field.** The environment is a character.

Six of the seven are **composition and grade decisions, not generation decisions.** That is the whole point,
and it is why this signature is transferable to any model, any year.

---

# CORE METHOD — model-independent

Ordered so the current (2025–26) architecture comes first and the older craft detail sits underneath it.

---

## PART I — The 2025–26 architecture (primary sources)

### 1. Drift is the boss fight, and it is not a prompting problem

The most important pattern in the corpus, and where 2026 Clark separates from 2024 Clark:

> *"You can't prompt your way to the ends."* — [FORBES26, 2026-07-24]
>
> *"With generative AI, you often get generative drift. So maintaining consistency across a project is a real
> challenge."* — [NFS, 2025-11-04]
>
> The hardest part is *"holding the same look across 20 minutes without the model drifting."* — [FORBES26]

The answer is **architecture, not prompt craft.** On *Hardcore 94*, Promise: trained character-specific models
on the original hand-drawn artwork; separated characters and backgrounds into distinct layers; positioned
cameras and characters inside a **3D environment (Unreal)**; then fed those spatial positions back into the
image generators [FORBES26]. And at [NFS]: *"creating custom workflows and Python code to make AI tools work
with certain 3D products."*

**The durable rule: anything that must stay the same across many shots has to live OUTSIDE the model.**
A trained model, a 3D scene, a layer separation, a locked plate, a script, a style reference. Ask a model to
*remember* and it will drift; hand it the answer every time and it can't. Length is the variable that converts
a prompting problem into an engineering problem, and the conversion happens roughly where a clip becomes a scene.

This is model-independent by construction — it is a statement about what generative models *are*, not about
which one you picked. Better models raise the drift threshold; they never remove it.

### 2. Colour-space compliance is the actual studio-grade dividing line

The most underrated pattern here, and the one nobody else in the AI-video space teaches:

> *"We were able to show how you get something that's AI-generated to the same, or at least close to the same,
> type of color space as the live action scenes."* — [NFS, 2025-11-04]

8-bit → 16-bit matching, so generated plates sit in a timeline beside Arri Alexa and Sony Venice footage and
clear **Netflix and Amazon QC** [NFS]. He was already chasing this in 2024 on the hybrid short: *"trying to
figure out how to make stable diffusion look like and work with footage that you shot on an Arri or on a Sony
Venice — it needs to match the fidelity."* [EVERY 2024 @ 07:41]

Call this **edit survivability**: will this asset survive contact with a real post pipeline? Bit depth,
colour space, frame rate, resolution, and gamma have to be decided *before* generation, because none of them
can be recovered afterwards. This is the concrete, unglamorous, non-negotiable version of "cinematic."
Below this line your work is content. Above it, it can be released. Almost every AI-video course stops at
"looks good on a phone."

### 3. The frame must be explainable

> *"In an industry built on ownership, guild rules and chain of title, a convincing image is not enough.
> The frame must be explainable."* — [FORBES26, 2026-07-24]

Promise built **MUSE**, which records every prompt iteration, the technical settings applied, and the
production approvals at each stage — an auditable production trail — plus a **Copyright Guardian** that flags
IP conflicts in generated material and marks cleared assets, generating formal chain-of-title documentation at
project completion [FORBES26].

The doctrinal move: **provenance is a craft requirement, not a legal afterthought.** The reason a beautiful AI
film gets refused isn't that it's ugly — it's that nobody can say where it came from. Generalises to any
commercial deliverable: log inputs, settings and approvals *as you go*, because "trust me, it looks great"
doesn't survive contact with a rights holder. (His 2024 position was parody/fair-use reasoning
[EVERY 2024 @ 56:38]; the thinking visibly hardened as the stakes moved from Reddit to distribution.)

### 4. Hybrid is the default, not the compromise

> *"It's not that they made [it] with 100% AI — it's a hybrid production. It's real, it's still using real
> actors, still using real crew, but then finding a way to create something that normally probably would cost
> two times, three times the amount."* — [FWAI 2023 @ 28:11]
>
> *"You don't have to use it, just like people don't have to use CGI, you don't have to use VFX."* — [FORBESLA]

The whole slate is hybrid, and this has *strengthened* over time rather than fading. *My Friend Zeph*:
live-action actors on set and on blue screen, generated backgrounds, AI de-aging [NFS, 2025-11-04].
*Another*: live-action + GenAI, Cannes Next 2024 [BIO]. On staff and on call: Joel Hynek (VFX supervisor,
the original *Predator*) [FORBES26]; a VFX supervisor from *John Wick 3* and *The Conjuring* [EVERY 2024 @ 07:53];
*John Wick* stunt choreographers, modelers, editors, cinematographers [FORBESLA]. The economics: turn a
$50–75M picture into a $10–20M picture using generative + virtual staging + photogrammetry [FWAI 2023 @ 24:26].

**Diagnostic value: the question is never "can AI do this shot?" It is "which layer of this shot is cheapest
to get right, and from where?"** Plate, performance, environment, effect, grade — each can come from a
different source, including a camera. Flat work is usually flat because someone forced all five layers
through one generator.

---

## PART II — Direction discipline (durable; drawn from the historic sources, tools stripped)

### 5. The generator is a camera, and you are still operating it

> *"Think of generators as your film cameras… every day when I'm using this stuff I'm thinking about it as if
> it's my Arri Alexa, it's my Sony Venice, it's my 35 millimeter film camera. That's how I look at it when I'm
> using it… you're able to basically capture anything a film camera does — but more, because the AI camera
> sees the world through your words."* — [FWAI 2023 @ 05:26–05:58]

Not a metaphor for encouragement. A **specification discipline**. If the generator is a camera, a prompt is
not a wish — it is a camera report: position, height, lens, movement, light source and direction, subject
action. The thing you'd hand a DP. Most flat AI video is flat because the operator typed a *mood* into a
*camera*.

The corollary in the same breath is the one people miss: *"also camera is not limited by physics — so you want
to have a guy floating in space, you can film that from any angle that you want."* [FWAI 2023 @ 06:00]
The physics exemption is a **budget, not a style.** Spend it on one impossible shot per piece, not on all of
them. A film where every shot is impossible reads as a screensaver.

### 6. The shot list IS the prompt list

> *"I still approach it like I would any other short film… I started with the script, I have an outline, I kind
> of had a shot list — which my shot list is what I use to prompt my stuff."* — [FWAI 2023 @ 08:20]

Script → outline → shot list → prompts. The prompt is the *last* artifact in the chain, not the first.
Which means **every taste decision has already happened before a tool opens.** Coverage, order, camera control
and composition are decided on paper — *"I wanted to maintain certain levels of camera control and composition
and things of that nature, so I was able to kind of think of that beforehand."* [FWAI 2023 @ 08:32]

He's honest that he doesn't always work this way — *"sometimes I just crack open a beer and I… stay up till 4
in the morning generating a bunch of stuff and see what I get"* [FWAI 2023 @ 08:42] — and equally honest about
which mode produces which result. The 4am mode produces **material**. The shot-list mode produces **films**.
He names *Lost Transmissions* as a case where *"I actually treated it like more like a film."*

**The transferable rule: whatever you're about to generate, write its shot list first — even if it's four lines.
The list is where the film gets directed. The tool is only where it gets photographed.**

### 7. Coverage from one setup — generate the pair, not the shot

> *"It's generating an image as a medium close-up, but then also getting the wide shot version of it — so when
> I'm cutting it together it feels like it's just this consistent narrative. It's really just the same shot."*
> — [FWAI 2023 @ 15:57]

Two sizes of the same moment is what makes a cut read as *a scene in a place* rather than *two unrelated
images*. It's the cheapest continuity in filmmaking and almost nobody doing AI video does it, because
prompt-first thinking generates *the next shot* instead of *this shot's coverage*.

Follow it with a **global capture layer** and the illusion closes: *"I'm using — which I use a lot — a handheld,
that kind of handheld look that I created… as an adjustment layer, so that helps cover up a lot of the
inconsistencies between shots."* [FWAI 2023 @ 16:13] One layer over the whole timeline puts every shot inside
the same physical camera. Corroborated visually in [REEL-obs 2025] at t=00:19, where a full telecine/gate
burn-in — timecode and edge-code numerals top and bottom of frame — sits over footage never photographed.

### 8. Reference language, not adjective language — and know *why* the reference looks like that

He directs an image the way a director briefs a DP: name a film, then name the mechanism underneath it.
Live, on a *Seven*-referenced frame:

> *"You got the film grain, you got the harsh perfume lighting — which is always funny, because I watched the
> behind the scenes of *Seven* and that was what the DP said. He was like, Fincher told me to watch a bunch of
> perfume ads, like we wanted to create that new — just like you said — where it was like whites are really
> white and blacks are really black. That's exactly what it did."*
>
> *"Perfume ads back in like the 80s and early 90s were very dramatic, so it was very high contrast, almost
> felt black and white, but there's always a splash, a wash of color — which is how *Seven* looks."*
> — [EVERY 2024 @ 27:29–28:05]

Three levels deep in one breath: the film → the DP's actual instruction → the physical description of the
result. **That is what "having taste" concretely means in this medium** — not knowing more style words, but
being able to decompose a look you admire into the operations that produced it. Compare "make it cinematic"
(unactionable) with "harsh perfume lighting: near-monochrome high contrast, real black point, one wash of
colour" (executable by any model or any human, this year or next).

He also reads images **feel first, mechanism second** — *"it almost feels like he's in a church, is this some
culty underground… kind of gives me John Wick vibes"* [EVERY 2024 @ 29:46] — then converts the feeling into the
next instruction. Feel → name → mechanism → prompt.

### 9. Generations are takes. You are a model manager, not a prompter.

The framing, from Dan Shipper on the live build:

> *"You are a model manager, and your job is to get out of the model the best thing you possibly can, like a
> manager would get the best out of an employee. And so if it's not working, your job is to figure out how to
> make it work."* — [EVERY 2024 @ 60:11]

Clark's own version lands harder because it's a film frame:

> *"I think of it like — these are our camera rolls. So you yell cut, you do another take. It's kind of the same
> idea, you do multiple takes and then you see what the best [is]."* — [EVERY 2024 @ 60:53]

No director shoots one take of anything. The single-generation habit is the most common cause of flat AI video
in existence, and it isn't a skill gap — it's a **mental-model gap.** People treat generation as a vending
machine (input → correct output) instead of as principal photography (setup → many takes → selection in the edit).

**The Rule of Five:** five generations of every shot, minimum, before judging anything. And the honest ceiling:
*"sometimes you get lucky, the first one was money. Most times that's not the case. Sometimes it takes 20."*
[EVERY 2024 @ 55:49]

### 10. Composite the take — don't pick the take

The single highest-leverage undisclosed technique in the corpus. Nobody watching his work guesses this:

> *"What people actually don't know is — what I actually do is I take multiple generations into [the NLE] and I
> layer them, and I take parts from each clip that I like better. Like I might like the smoke here better, but
> I might like [the performance] less than the other one — so I'll be able to just kind of mask him in."*
> — [EVERY 2024 @ 54:08]

The best shot is frequently **not in any single generation.** It's assembled from the smoke of take 2, the
performance of take 4, and the light of take 1. Every generation is **a layer of coverage on the same setup**,
not a competing candidate for one slot.

This reframes selection entirely. The question is never "which of these five is best?" It's "what is best
*in each* of these five, and can it be masked into one plate?"

**Companion move — mask the source resolution back in.** *"Sometimes if I really want [the] likeness to shine
through, I'll actually go back to the original image, mask in his real face, and then use some of the movement
from around his head — so his face actually stays high quality."* [EVERY 2024 @ 55:56] The animated plate
carries motion; the still carries fidelity; you keep both. He calls the moment out live while watching a bad
take: *"this is an instance where I would mask in the real face."* [EVERY 2024 @ 57:28]

### 11. Cadence engineering — beat the metronome or be exposed by it

He identifies the medium's dominant tell and names his fix as the reason his work stands out:

> *"So what I'm able to do is make clips last longer and then mix that with quicker cut clips, so it actually
> makes the storytelling and the filmmaking more like something we're used to seeing on TV. I always think about
> the Tony Scott type films like *Man on Fire* where there was always these kind of quick cuts, or Snyder with
> *300* and *Dawn of the Dead*… editing is a huge piece of my type of filmmaking with AI."* — [EVERY 2024 @ 17:57]
>
> *"I think that maybe helps my stuff stand out sometimes a little bit more, because it's not just 3 second clip
> after 3 second clip after 3 second clip. Sometimes you'll get an 8 second clip because I slowed it down, then
> you'll get a one second clip — and I use that cadence to help tell it."* — [EVERY 2024 @ 19:23]

**The durable principle: duration is an editorial variable, not a tool constraint.** Whatever the current
generation limit is, you generate to be *retimed* — high frame rate down, short clips stitched, long beats
alternated against quick cuts. *Oppenheimer* was the reference for the time-travel light whips in *Borrowing
Time* [EVERY 2024 @ 17:44]. (The 2023–24 mechanics for achieving this are in Appendix A; the principle
outlives them.)

### 12. Direct the performance — don't generate it

> *"They have this whole speech-to-speech, which I used in *Borrowing Time*… I can talk and act out how I want
> the — like the judge, the white judge in the movie was my voice, it was just voice-to-voice… And the woman,
> the mother, was my voice. And then obviously the voiceover was just my plain voice, because I just thought it
> sounded better and more natural to have the natural pauses and the things like that. So I mixed."*
> — [EVERY 2024 @ 20:12–20:26]

He performs every role himself and converts the timbre. The **acting** — pauses, emphasis, the read — is human
and directed; only the voice colour is synthetic. And he'll refuse the conversion where the raw human read is
better. Same principle as Pattern 10: keep the human decision in the layer where humans are better, synthesise
only the layer where they aren't.

The tell on the other side: *"a lot of people tend to use the ones that sound like AI"* [EVERY 2024 @ 19:40].
Default preset voices are the audio equivalent of unmotivated light.

### 13. Prompt the model's understanding, not the model's category labels

> *"You just got to use other prompts instead of red blood — it's red liquid, or it's red paint. Like all the
> blood on the walls is just red paint dripping down the wall. But it works, and it will still come back with
> actually really gory bloody stuff, doesn't look like paint at all — because the AI knows what you're trying
> to do, in a weird messed up way."* — [FWAI 2023 @ 15:23]

Under the moderation story is a general principle about how these models parse: **describe the physical
phenomenon, not the loaded category.** "Red liquid running down plaster" is *more* specific than "blood" and
therefore renders better *even with no filter in the way*. Category words are compressed; phenomenon words are
rendered. He learned it fighting a filter; it's a craft rule.

He also keeps *"a notepad of stuff that I know works"* because *"there's a look that I've definitely established
I like to apply to most things that I do"* [FWAI 2023 @ 13:50] — a personal, working, non-theoretical style
library. And he leaves room for accident: *"I like happy accidents… putting in a different type of lighting or
color."* [FWAI 2023 @ 14:07]

### 14. Frame the frame — aspect is a pre-generation decision, and reframing beats cropping

> *"I like to finish a lot in widescreen… sometimes I end up just generating in your typical square or 16:9
> because I'm just lazy, and then I have to crop it — so I actually have to go back and extend the image
> sometimes… if I'm not happy with the framing I want to extend the background, I do do that. Sometimes I do
> that while I'm actually in the video edit."* — [FWAI 2023 @ 13:00–13:23]

Two rules. **(a)** Set the aspect *before* you generate — he defaults to 16:9 or 2.39:1 and treats a square
default as a self-inflicted wound. Live, he stops mid-session to standardise: *"let me put this in — for now on,
all images will be 16:9 ratio, so I don't have to keep adding that."* [EVERY 2024 @ 39:01]
**(b)** When framing is wrong, **extend the plate outward, never crop it** — generative fill preserves resolution
and keeps reframing a live post decision instead of a destructive one. Same family as colour space (Pattern 2):
decisions that can't be recovered downstream get made upstream.

### 15. Choose a genre whose grammar forgives the medium's current failure modes

> *"Horror is perfect for that type of thing. If you think about *Blair Witch Project* or *Paranormal Activity*,
> it's always a horror film that creates a new subgenre."* — [EVERY 2024 @ 08:13]

Found footage exists *because* the camera was bad. Handheld, artifact, degradation, missing information and
unstable identity are the *aesthetic*, not the defect. Clark's slate (*Dark Retreat*, *Dead Invasion*,
*Dismal Swamp*, the POV feature with Bloody Disgusting) sits inside genres that metabolise exactly the artifacts
generative video produces. Compare the failure mode of a clean two-hander drama shot with a model that can't
hold a face for eight seconds.

**Strategic form: pick the container whose conventions absorb your constraints** — POV, found footage, dream,
memory, surveillance, archival, nightmare, animation. Not a compromise; it's the same move indie filmmakers have
always made, and it's how new subgenres get born. This one *re-targets* as models improve rather than expiring:
the constraint list changes, the move doesn't.

---

## PART III — Why any of it matters

### 16. The story is the moat — and it's the only durable one

> *"It's cool to see something that's not like Harry Potter or Star Wars go viral."* — [EVERY 2024 @ 02:18]

*Borrowing Time* is his father's actual story: a twelve-or-thirteen-year-old Black boy in the Jim Crow South who
whistled at a white woman and got in severe trouble for it; the following year someone else got life on a similar
accusation. Clark's sci-fi conceit — a lawyer in the present travelling back to defend him — came from *"man, if
my father ended up going to jail and I was able to go back in time and represent him in court… that's a cool
story, I've never seen that before."* [EVERY 2024 @ 02:42–03:47]

His commercial argument, not just the moral one:

> *"If you try to go pitch out to Hollywood they're going to say — eh, period piece, eh, been there done that,
> and plus you're not Stephen Spielberg, so sorry, you're not going to make that movie. But because of AI I'm
> able to visualize it in a really cool way — and that got on Forbes."* — [EVERY 2024 @ 03:53]

On virality: the novelty gets the click, but *"they end up talking about the content and the theme and unpacking
things, so the novelty sort of fades into the background — which is where we want this to be."* [EVERY 2024 @ 26:36]
Same reason he cites his father's Vietnam and Deep-South stories in [FWAI 2023 @ 00:33]: *"he has the most
incredible stories that no one will ever know… you have like 10 movies that could have starred Denzel Washington."*

**Every operator will have the same tools within a year. The stories in your notebook are the only asset that
doesn't commoditise.** He treats each piece as owned IP on purpose: *"absolutely everything that I create, it's
an IP, it's an extension of my creative ideas that I have in a notebook."* [EVERY 2024 @ 04:48]

### 17. Short-form AI film as the new sizzle — pitch with pictures instead of permission

> *"For *Dismal Swamp* it was to create a little one-minute sizzle or rip-o-matic, if you will, using AI generated
> footage. If you think about traditionally in Hollywood, a lot of directors will take pieces from other
> directors' movies and cut together a sizzle to pitch an idea — but with AI I took my script, I fed my script
> into the prompts, and I made it based on all the stuff that was in my head. Couldn't do that five years ago."*
> — [EVERY 2024 @ 05:11]

The rip-o-matic used to be assembled from *other people's* films, so a pitch could only ever show what already
existed. Now the sizzle **is** the vision. Receipts: *Dismal Swamp* drew A-level Hollywood producers and execs
[EVERY 2024 @ 05:02] and did ~200,000 views in under 12 hours on Reddit [FWAI 2023 @ 25:44]; *Dark Retreat*, made
for a Curious Refuge Halloween contest, travelled to a producer on the A24/James Wan Backrooms film and became a
POV feature in development with Bloody Disgusting and the *V/H/S* team [FWAI 2023 @ 23:00–24:00].

Dan Shipper's analogue, which Clark accepted: tweets test articles, articles test books — **AI shorts test
features.** [EVERY 2024 @ 06:53]

### 18. Buy yourself more time in the stage where judgment compounds

> *"I'm writing scripts now probably in one third of the time that I used to write them… I'm able to hurry up and
> get that first draft written, get my story written down on paper, and then I can focus real time on the rewrite
> — as opposed to focus all the time on the first [draft], which we know is painful."* — [FWAI 2023 @ 03:12]

The value isn't speed. It's **reallocating human attention to the stage where human judgment actually compounds.**
The rewrite is where a script gets good; the blank page is just friction. Same shape as Pattern 12 (direct the
performance, synthesise the timbre) and Pattern 10 (human selection, machine generation). Consistent across the
whole corpus: **find the stage where taste is decisive, and buy yourself more time in it.**

He's specific about the ceiling too: *"not that it's ready to write a full script or do your dialogue for you,
but it definitely as sure as hell can help you with that first draft."* [FWAI 2023 @ 03:05]

---

## Signature Moves — durable operations

Tool-agnostic by construction. Where a 2023–24 implementation exists, Appendix A carries it, dated.

| Move | Operation | Why it works | Source |
|---|---|---|---|
| **The Rule of Five** | Five generations of every shot, minimum, before judging. Twenty if the shot matters. | Selection depth, not prompt quality, is the #1 determinant of output quality. Cause #1 of flat. | [EVERY 2024 @ 52:13, 55:49] |
| **Composite the take** | Layer all generations in the NLE; mask the best element out of each into one plate. | The best shot usually doesn't exist in any single generation. | [EVERY 2024 @ 54:08] |
| **Mask the fidelity back in** | Mask the original still's face over the animated head; keep the motion from around it. | Motion plate carries movement, still carries fidelity. Beats the drift/degradation tell. | [EVERY 2024 @ 55:56, 57:28] |
| **Retime, don't accept the clip length** | Generate to be retimed — high frame rate slowed, short clips stitched, long beats against quick cuts. | Turns tool-max duration into an editorial variable. Kills the metronome tell. | [EVERY 2024 @ 17:22, 19:23] |
| **The coverage pair** | Generate the medium close-up AND its wide from the same setup, before moving on. | Two sizes of one moment is what makes a cut read as a scene. | [FWAI 2023 @ 15:57] |
| **The global capture layer** | One handheld/grain/gate adjustment layer across the entire timeline. | Puts every shot inside the same physical camera; hides inter-shot inconsistency. | [FWAI 2023 @ 16:13]; [REEL-obs 2025] t=00:19 |
| **Phenomenon over category** | Replace the loaded category word with the physical phenomenon ("red paint dripping down the wall"). | Phenomenon words render; category words are compressed. Also clears filters. | [FWAI 2023 @ 15:23] |
| **Extend, don't crop** | Wrong framing → generative-fill the plate outward and reframe in the edit. Never crop. | Preserves resolution; keeps reframing a live post decision. | [FWAI 2023 @ 13:00] |
| **Externalise what must persist** | Anything that has to stay identical across shots lives outside the model — trained model, 3D scene, layer separation, locked plate. | Models drift by construction. Don't ask them to remember; hand them the answer. | [FORBES26 2026]; [NFS 2025] |
| **Spec the delivery before you generate** | Aspect, bit depth, colour space, frame rate and resolution decided upstream. | None of them are recoverable downstream. | [NFS 2025]; [FWAI 2023 @ 13:00]; [EVERY 2024 @ 39:01] |
| **Direct the performance, synthesise the colour** | Act every role yourself; convert timbre; keep your own raw read where it's better. | Human performance, synthetic colour. Preset voices are the audio version of unmotivated light. | [EVERY 2024 @ 20:12] |

---

## Quality Rubric — how Clark separates good from bad

Ordered as he actually checks, in the order he checks it.

| Dimension | Passes | Fails |
|---|---|---|
| **Idea** | You can say what it's about in one sentence, and it's yours. | *"You still need to actually have an idea… or you're just going to get a bunch of crappy AI generated videos."* [FWAI 2023] |
| **Selection depth** | ≥5 takes per shot; best elements composited. | One generation, shipped. [EVERY 2024] |
| **Cadence** | Clip lengths vary deliberately; long beats against quick cuts. | Metronome. 3s, 3s, 3s. [EVERY 2024] |
| **Coverage** | Sizes pair up; cuts read as one place. | Every shot a new setup. [FWAI 2023] |
| **Light** | One nameable motivated source; real black point; one warm accent family. | Ambient, sourceless, lifted, evenly lit. [REEL-obs 2025]; [EVERY 2024] |
| **Capture layer** | Grain/gate/handheld present and consistent across the timeline. | Digitally immaculate, therefore never photographed. [FWAI 2023] |
| **Reference discipline** | The look is named as a film *plus* the mechanism underneath it. | Adjectives. "Cinematic, moody, epic." [EVERY 2024] |
| **Consistency across length** | Look and identity hold; anything that must persist lives outside the model. | Drift. *"You can't prompt your way to the ends."* [FORBES26 2026] |
| **Edit survivability** | Colour space, bit depth and frame rate matched to the live-action plates; clears platform QC. | Looks fine on a phone. [NFS 2025] |
| **Provenance** | Prompts, settings and approvals logged; assets cleared. | *"A convincing image is not enough."* [FORBES26 2026] |

**The composite verdict he uses on his own work, out loud:** never "good." He says *"these are more cinematic —
like they're really something good going on"* and *"oh yeah, it looks like right out of a movie"* [EVERY 2024 @ 47:00].
The bar is **does this read as a frame from a film that exists.** And when it doesn't: *"I don't like that the
light is kind of going out as we're going in"* [EVERY 2024 @ 57:36] — specific, mechanical, one named defect.
Never a vibe complaint.

---

## Voice Profile

**Register.** Working director, not lecturer. Conversational, self-interrupting, generous with credit, allergic
to self-mythology. Says "dude" and "man" a lot. Undersells constantly — *"I'm just lazy"* about aspect ratios,
*"it's been a nightmare"* about the hybrid VFX, *"I don't do it as often as people think I do."*

**Tell #1 — he narrates the decision, not the conclusion.** A rejection: *"I don't like that the light is kind
of going out as we're going in."* An acceptance: *"I like this little leak back here going on, it's kind of cool
cinematic."* Always the specific mechanism, never "this one's better."

**Tell #2 — feel first, mechanism second.** *"It almost feels like he's in a church, is this some culty
underground… gives me John Wick vibes"* → then converts the feeling into the next instruction. Never leads with
theory.

**Tell #3 — he cites the behind-the-scenes, not the film.** Not "like *Seven*." Rather: "the DP of *Seven* said
Fincher told him to watch perfume ads." His references are always one level below the surface.

**Tell #4 — relentlessly non-defensive about the medium's limits.** *"It sucks right now."* *"It's usually crap
after the first four."* *"Most of the stuff is bad."* He never oversells the tools, which is exactly why the
craft claims land.

**Tell #5 — the abundance frame is genuine and it's political.** *"Everyone has a chance to create something
incredible"* [EVERY 2024 @ 10:52], grounded in access — a white kid from Arkansas with no connections, a Black
kid from the hood, and his own father, who *"has the most incredible stories that no one will ever know."*

**What he never does:** hype a tool as a replacement for judgment; claim 100% AI; disparage traditional
filmmaking (*"I want to work with Leonardo DiCaprio, I don't want to work with his AI double"* [FWAI 2023 @ 10:46]);
pretend the first take was the take.

---

# APPENDIX A — Era-Bound Mechanics (2023–24) — VERIFY BEFORE USE

> ⚠️ **Everything below is dated tool state from [FWAI] 2023-11-18 and [EVERY] 2024-02-28.**
> It is preserved because it shows *how* he implemented the durable principles at one moment in time, and
> because the reasoning is often instructive. **It is not current guidance.** Tool names, limits, parameters
> and behaviours have all moved. Never build a deliverable on this appendix without verifying against the
> present tool state. No workflow or execution prompt in this skill depends on any line of it.

| Era-bound mechanic | As stated | Durable principle it implements |
|---|---|---|
| Midjourney / DALL·E for stills; Runway + Pika for image-to-motion; Topaz for upscale; HeyGen for lip-sync; Kaiber; ElevenLabs for voice; Premiere / After Effects / DaVinci for post; Photoshop generative fill for extends [FWAI @ 02:26–05:24] | His 2023 daily stack | Pattern 4 — every layer from wherever it's cheapest to get right |
| *"Runway you can extend up to 12 seconds — it's usually crap after the first four. I do a bunch of four second generations and then I stitch them."* [FWAI @ 28:53] | Runway Gen-2 duration behaviour | Pattern 11 — duration is an editorial variable |
| *"I bring in a Runway clip… I'll also change the frame rate — 24fps to 60, sometimes 120 [in Topaz] — and then you can extend the clip… slowed it down in post, and then sped it up."* [EVERY @ 17:22] | Topaz Labs frame interpolation as retiming | Pattern 11 — duration is an editorial variable |
| Runway **Motion Brush**: paint regions, set per-region motion type and amount (ambient 0.5 for cloth/hair, vertical for smoke, proximity for light rays), *"paint everything then go back and mess with the parameters"* [EVERY @ 49:55–52:06] | A specific 2023 Runway feature | Pattern 5 — the generator is a camera; you specify motion per element rather than hoping |
| *"Generate five at a time"* on Runway credits [EVERY @ 52:13] | Credit-plan mechanics | The **Rule of Five** — durable |
| *"Runway outputs almost at 4K… more like 3.2K, so I don't have to spend time upressing everything like I would with Pika"* [FWAI @ 31:39] | 2023 resolution comparison | Pattern 2 — spec the delivery before you generate |
| Custom "Blazian GPT" — a fine-tuned DALL·E-backed GPT trained on his own conversations, *"almost create a mentor out of it… a combination of my opinions, combination of what Spielberg might look for in imagery"* [EVERY @ 21:30–22:20] | An early custom-GPT image workflow | Pattern 13 — a personal, working style library; and Pattern 1 — externalise what must persist |
| Story-forward chat prompting: *"show me the next scene" / "what happened before this?"*, then *"give me a detailed prompt to use in Midjourney that will get us an image similar to…"* [EVERY @ 32:03, 44:26] | Chat-to-image-model prompt laundering | Pattern 6 — the shot list drives the prompt |
| *"If you go with shorter descriptions it'll get you the nice kind of frames"* [EVERY @ 41:04] | Midjourney v5-era prompt-length behaviour | Model-specific. **Do not generalise.** |
| Moderation routing: new account after a ban; Cronenberg triggers shadowban [FWAI @ 14:38–15:10] | 2023 Midjourney moderation | Pattern 13 — phenomenon over category |
| *"Negative prompts, I use a lot of negative prompting"*; chaos parameter [FWAI @ 14:16–14:28] | Midjourney v5 parameters | Model-specific syntax; the *intent* (subtract the model's defaults) is durable |
| Stable Diffusion + a *John Wick 3* / *Conjuring* VFX supervisor to match Arri/Venice plates; *"it's been a nightmare"* [EVERY @ 07:38–08:04] | 2024 hybrid VFX state | Pattern 2 — colour space / edit survivability. **Superseded** by the 2025 [NFS] account |

**Promotion rule:** if a later source corroborates one of these mechanics as still-current practice, promote the
principle into the core method and leave the dated implementation here. Do not promote a mechanic on the strength
of the old source alone.

---

## Cross-pollination

- **Nick St. Pierre** (hunt #1) — image art direction is the substrate Clark's shot list gets executed on.
  St. Pierre owns the *prompt*; Clark owns the *shot list above it* and the *edit below it*. Load both for any
  board-to-film chain.
- **Rory Flynn** (hunt #3) — systematises what Clark does by instinct. Correct order: Clark's judgment first,
  Flynn's operations second. Systematise a taste you have; systematising one you don't gives you scaled mediocrity.
- **PJ Accetturo** (`skills/pj-accetturo-ai-video/`) — the ad-shaped sibling. PJ optimises for the platform;
  Clark optimises for the release print. When they disagree, the deliverable decides.
- **cinema-worldbuilder-pro** — the write-the-visible prompt discipline is the executional layer under Pattern 5.
- **Andrew Stanton** (`skills/andrew-stanton-audience-engineering/`) — Pattern 16 is the same claim from the
  narrative side. Pair them when the diagnosis is "technically fine, nothing at stake."
