---
description: "/harding-perception-content — produce a full perception-driven piece (post / essay / Substack edition) that makes an overlooked everyday subject luminous through precise attention and the literal chain, persuades by recognition rather than a takeaway, and ends by opening a door so the reader returns. The perception engine for CONTENT — not the hot-take engine. Stacks with parallax (zeitgeist-first edition pipeline) and kallaway (perception of novelty, honesty spine intact)."
---

# Perception Content — Re-See the Ordinary So the Reader Recognizes It (Paul Harding)

Most content answers "what should you think about X?" This answers "have you ever actually *looked* at X?" — and lands harder, because nobody argues with a thing they suddenly recognize as true. Harding's whole faith is that **the world means itself**: a swan boat on the Boston Common, a hayed meadow gone to stubble, the four-o'clock light on a kitchen wall — rendered precisely enough, in motion, it turns luminous on its own, and the reader feels *"that's absolutely true; I've always known it and never seen anybody put it into words."* That recognition is the persuasion. It cannot be installed by a takeaway. It can only be *uncovered* by reverent, pre-linguistic attention to one real, overlooked thing, then handed to the reader with the seam erased between the world and the seeing of it.

This is the **perception engine, not the hot-take engine**. The hot-take engine wins the scroll and is forgotten by lunch — "I read that post once." The perception engine produces the piece nobody says they read once. The difference is depth, not width: Harding wrote a 200-page book he wanted "800 pages deep because it's not 800 pages wide." You are doing that to a post. The most common failure is rushing — to the angle, the lesson, the clever line. Slow down. That is the headstone line.

> **Where this sits in the stack.** The sibling `/harding-perception-engine` builds *one luminous passage* (the description craft, bottom-up). **This workflow uses that engine to build a whole publishable piece** — opening, body, close, and the structural choices that make a re-seen-ordinary subject work as *content* that resonates and re-reads. It is the content-deployment layer. When in doubt about a single passage inside this piece, drop into `/harding-perception-engine`; come back here for the shape of the whole thing.

## Pre-Flight

Read before executing — load these `genius.md` sections (do not paraphrase from memory; lyric prose dies under mechanical layering, and these patterns are the difference between *seeing* and *slotting*):

- **Pattern 2 — Slow Down to Pre-Linguistic Attention** — the engine's first gear: refuse "yeah, I got it, I know that already"; sift beneath recognition to "what is *actually there* when you're in the scene." Every perception piece opens on a thing genuinely re-seen, never an abstract claim.
- **Pattern 3 — The Literal Chain (Stay With It Until It Means Something)** — the body's spine: take one literal observation and keep asking *"then what?"*, link by physically-true link, never reaching for "it's symbolic." Meaning *accrues*; it is not stated. This is what makes a short piece feel substantive — "this is your brain on art, the filament lights up."
- **Pattern 10 — Persuade by Recognition, Not Argument** — the close and the whole strategy: aim for the reader's *recognition* of a felt truth they couldn't articulate; **open a door, never close it with a takeaway.** A stated lesson means "they never have to think about it again," and most are tautological ("be kind to strangers — no kidding").
- **Pattern 9 — Depth, Not Width** — the format discipline: compress meaning *down*, not *out*. Maximum density of lived experience at maximum readability — re-readable, never soden. The piece nobody says they read once.
- **Cross-Domain Applications — the Content creation row** — "make the overlooked everyday luminous through precise attention — the perception engine, not the hot-take engine. Overwrite then distill to dense, lucid pieces. End by opening a door, so the reader returns." This is the row this workflow operationalizes.

Also load if used in the polish/layer passes: **Pattern 6 — The Two Things (Literal + Felt)**, **Pattern 11 — Drummer's Cadence**, **Pattern 13 — Clutter Then Distill**, and the **How-to-Use (Opus Calibration)** note ("would Paul Harding recognize this as a mind paying real attention — or as someone filling lyric-prose slots?").

> **🔒 Pre-Flight Gate**: run the **Decision Framework** in `genius.md § Decision Framework` before executing. Confirm specifically: **Q1** (you are slowing down to what's *literally there* — you have NOT already jumped to "here's the angle / it means X"; if you have, you skipped the looking, and the piece will be a hot take wearing a description costume), **Q3** (you are giving the literal thing AND the felt experience of it — you are NOT explaining the feeling), and **Q7** (you are NOT about to land a lesson — the close opens a door). **Honesty spine, non-negotiable:** every precisely-rendered detail must be a *real, true* particular, and any persuasive claim the piece carries must amplify a TRUE thing — Harding's craft makes a true thing land harder; it never manufactures sensation to fake authenticity or makes a false claim *sound* recognized-as-true. **The contact gate:** if you cannot get into actual sensory contact with the subject (real memory, real object, real observed scene), stop — go look, recall harder, or pick a thing you have genuinely perceived. You cannot make luminous what you have not seen.

## Input Required

- **The subject (one overlooked ordinary thing)** — specific, not categorical: *the swan boat on the Common pond when I was seven*, *the stubble of a hayed meadow at dusk*, *the steam off a client's coffee in a 7am Zoom*. Not "boats," not "summer," not "morning routines." If it arrived as a category, narrow it to a single instance you can re-enter.
- **Point of contact (honesty anchor)** — how you get into real sensory contact: it's in front of you / a vivid memory / an observed scene you can re-inhabit. The piece must come from contact, not invention.
- **Format / where it lands** — Substack edition · long-form essay · social post (LinkedIn/X/Substack Note) · marketing-brand piece · ghostwritten piece. Drives length, how much literal chain the body can run, and how the close opens.
- **The felt charge (optional)** — what the subject *means* to the perceiver (the creek that "means death"; the meadow that means a season you can't get back). Refracted through the thing in the body, never stated. If unknown, leave blank — the literal chain often surfaces it.
- **Zeitgeist tether (optional — for parallax / topical work)** — the trending conversation or theme this ordinary subject quietly answers. The subject stays the front door; the tether is the door's *relevance*, not its replacement. (See Stacking, below.)
- **Whose grain (ghostwriting only)** — if writing as someone else, name them; *what* gets noticed and *how* it's named refracts through their register, not Harding's.

## Workflow

### Step 0 — Choose the right vehicle: is this a perception piece at all? (gate)

Not every content brief wants this engine. Run the one-question gate before anything else: **does this resonate as recognized truth, or does it deliver information?**

| If the goal is… | Route |
|---|---|
| Re-seeing an ordinary thing so the reader recognizes a felt truth they couldn't articulate; depth-not-width; re-readable | **This workflow.** Proceed. |
| A timely opinion / argument / "here's what to think about X" | Hot-take / argument engine (not this — Harding refuses argumentation; AN-3) |
| A how-to, a list, a tactical breakdown, news | Information format (not this; perception ≠ instruction) |
| A trending topic that *needs* a soul, not a take | **This workflow, tethered** — run `/parallax` for the zeitgeist + briefing, then bring the topic here as the *tether* and find the ordinary subject that quietly carries it (Stacking, below) |

If the brief is genuinely "make people think differently," it may still be this — but only if the change comes by *recognition*, not by being told. If you can't name the ordinary subject the piece will re-see, you don't have a perception piece yet; you have a topic. Find the thing.

### Step 1 — Find the ordinary subject and get into contact (Pattern 2, contact gate)

The subject is the whole game and the most under-thought part of a content brief. Perception content does not start from a thesis or a trend — it starts from **one real, overlooked thing the reader has also seen but never looked at.** Universality lives in the specific: everyone has ridden some version of the swan boat, watched some version of the meadow cut down. Pick the particular; the recognition is what makes it universal.

Then get into contact — physically, or by re-entering the memory until it's vivid — and catch the first word your mind hands you for it, and *distrust it*. The first label is habituated ("the peaceful pond," "the golden field"). Write the first labels down expressly so you can ban them.

```
SUBJECT (one specific overlooked thing): __________
WHY THE READER HAS ALSO SEEN IT (the universality in the specific): __________
POINT OF CONTACT (honesty anchor): __________  [real memory / in front of me / observed scene]
FIRST (HABITUATED) LABELS — banned for the rest of the piece: __________ , __________ , __________
```

> Selection test: could the reader say "I've seen that too" *and* "I never thought about it like that"? If only the first, it's too generic to be worth re-seeing; if only the second, it's too exotic to be recognized. You want both. (For parallax/topical work, the subject should also quietly answer the tether — but it must be a real thing first, relevance second.)

### Step 2 — Find the seed image: the pre-linguistic detail the piece opens on (Pattern 2)

Look at the subject sense by sense as if you'd never seen it, and record only what is *literally there* — no metaphor, no meaning, no feeling yet. Stay longer than is comfortable. The line a perception piece opens on is almost never the obvious feature; it's **the one detail you'd have skipped on autopilot.** That overlooked detail *is* the proof you actually slowed down, and it's where the piece's authority comes from.

| Sense | Literal question (no metaphor, no meaning yet) | What is actually there |
|---|---|---|
| **Sight** | Exact shapes, colors, edges, light; depth of field — what's sharp, what's blurred? | __________ |
| **Sound** | What is actually audible — the small sounds under the obvious one? | __________ |
| **Touch / temperature** | Texture, weight, heat, the air on skin? | __________ |
| **Smell / taste** | What's literally in the air or the mouth, however faint? | __________ |
| **Motion / change over time** | What is *moving* or *changing* — light shifting, a surface settling, the slow drift? (Non-negotiable — see Step 4.) | __________ |

From this table, name the **seed image**: the single most precise, most overlooked, most physically-true detail. (Harding's was the *mold-seam down the plaster swan's breast* — not "the swan," the seam where the halves would never quite come apart.) The whole piece will open on this and grow from it. Do not pick the obvious feature. Pick the seam.

```
SEED IMAGE (the overlooked literal detail the piece opens on): __________
```

### Step 3 — Open on the seed, not on a claim (the perception-content opening rule)

This is the move that separates perception content from a hot take with nice sentences. **The first line is the seed image, rendered precisely — never an abstract claim, never "here's what I learned," never a thesis you'll then illustrate.** The reader should be *inside the seeing* before they know why. Harding brings the reader down to the place he found and says, in effect, *look what I found* — he does not announce in advance what it will mean.

| Open with… | Don't open with… |
|---|---|
| The precise seed image, in motion (Step 2 + Step 4) | An abstract claim ("Life is about noticing the small things.") |
| A thing the reader can see in their own body | A "here's what / here's why / here's how" frame (AI-tell, banned) |
| The specific particular ("The pond held the willows upside down and didn't let them move.") | The category or the trend named directly |
| Mid-perception, as if mid-sentence into the seeing | A setup explaining what you're about to describe |

> The honesty-spine guard at the open: the seed image must be *real*. A fabricated "vivid" opener is the most dangerous failure in this whole workflow — the better your craft, the more convincing the lie, and the entire engine runs on the reader trusting that what you saw, you actually saw.

### Step 4 — Run the literal chain through the body (Pattern 3 — the spine of the piece)

The body of a perception piece is not paragraphs of explanation. It is **the literal chain**: hold the seed image and keep asking *"then what?"*, following one physically-true consequence at a time, never once reaching for "it's symbolic." In *Tinkers* the dying man sees cracks in the ceiling; Harding stays super-literal — the cracks widen, the ceiling caves to wires and plumbing, the roof gives to clouds, the clouds fall out to blue, the blue drains to stars, the stars fall, and what's left is the black, his funeral shroud. Every link is literal. The funeral shroud is *earned* by the chain, not installed. **Meaning accrues; you never state it.** This is "your brain on art — the filament lights up": the reader's recognition fires because the chain led them there, not because you told them.

Two engines power the body; use both:

| Move | What you do | Guard |
|---|---|---|
| **The "Then What?" Walk (Pattern 3)** | Take the seed image and iterate one true consequence at a time. "Then what is actually there? Then what does that become? Then what?" Let the chain run past where you expected to stop. | Never jump to "it's symbolic." If you reached the "point" without an unbroken literal chain leading there, go back to the last literal link and ask "then what?" again (AN-1). |
| **Botanist's precision + the calculus (Pattern 8)** | Render each link *exactly* (not beautifully), then describe how it *changes over time*. Mine the **verbs** — the life is there: the wake *opens, widens, thins, is taken back*; the light *climbs, reddens, withdraws*. | If a passage is frozen, it's a photograph, not perception. Something must move. If an adjective is doing "beauty duty," replace it with a more exact noun/verb (AN-4). |

> **Depth-not-width discipline (Pattern 9) runs continuously here.** You are compressing meaning *down*, not padding *out*. A perception piece earns its length by density of lived experience, never by word-count or extra examples. One literal chain followed all the way down beats three half-chains. If you're adding a second subject to "cover more," stop — go *deeper* into the one.

### Step 5 — Layer the felt experience through the thing, seam erased (Pattern 6 + Pattern 4)

The chain renders the world. Now give the reader **both things**: the world (neutrally, accurately true) *and* the perceiver's experience of it. The meadow is objectively a cut field; the felt charge is the season you can't get back — and the reader knows the feeling without you ever naming it. The gap between the literal thing and the felt thing is a whole dimension; that gap is where recognition happens.

- **The literal thing came first and stays true.** The reader trusts the feeling *because* they were shown the real thing before being asked to feel anything.
- **Refract, do not state.** Never write the emotion's name ("it was so nostalgic," "I felt grief"). Let the feeling live in *what gets noticed and how it's named* — the depth of field, the verbs, the colors registered.
- **Erase the seam (co-extensivity, Pattern 4).** Do not announce the move from outside to inside ("I looked at the field and remembered…"). Let the perception *be* the interiority. No clanking gears — a reader can't locate where description ends and the perceiving mind begins.

> If a sentence's only job is to tell the reader how to feel, you owe them the precise thing instead, with the feeling refracted through it. Stating the feeling is, in Harding's terms, "the most violent thing you could do to the reader." It also kills re-readability — a stated feeling is consumed once; a refracted one rewards return.

### Step 6 — Close by opening a door, never landing a lesson (Pattern 10 — the recognition close)

The ending is where perception content lives or dies, and where almost everyone reverts to the hot-take reflex: the takeaway, the "and that's when I realized," the moral. **Kill it.** Harding: a message means "they never have to think about it again," and most lessons are tautological. Art **dilates** the reader; it does not instruct them. The close should leave the reader *opened* — recognizing a felt truth, wanting to return to the piece — not *closed*, with a lesson filed away.

| The recognition close does… | Banned closes (the hot-take reflex) |
|---|---|
| Ends on the precise thing or the felt charge, refracted | "And that's when I realized…" |
| Opens forward / leaves the image resonating | "The lesson here is…" / "So remember to…" |
| Lands on recognition ("somebody finally put that into words") | A tidy moral the reader can agree-with-and-forget |
| An image-close, a declaration, or a bookend back to the seed | A generic question signoff ("What do you think?") — banned |

Choose one of three recognition closes: **(a) Image-close** — end on the seed image transformed by the chain, resonating (the wake "taken back without a mark"). **(b) Bookend** — return to the opening seed, now charged by everything between. **(c) Quiet declaration** — one plain, true sentence that names the recognized thing without moralizing it ("the day was a thing that closed over you and took you back without a mark"). Never a takeaway; never a cheap question.

> The test (Pattern 10 success metric): the reader thinks *"that's absolutely true; I've always known it and never seen anybody put it into words"* — not *"good point, noted."* The first wants to return to the piece. The second files it. You are building the one nobody says they read once.

### Step 7 — Distill, then tune by ear (Patterns 13 + 11 — the polish that makes it re-readable)

Read the whole piece **aloud, cold**, twice.

1. **Distill pass (Pattern 13 — systole/diastole).** You should have overwritten; now carve back to elegance until "there it is" — every word apt, all depths of field working, the prose "so lucid the reader forgets they're reading prose on a page." Cut any sentence written to be *admired* (AN-4). Cut any received, off-the-rack phrase (AN-2). Confirm the banned habituated labels from Step 1 appear *nowhere*. Depth-not-width: if the piece got *wider* (more examples, more subjects) instead of *deeper*, carve back to the one chain.
2. **Cadence pass (Pattern 11 — the drummer's ear).** Feel the beats; Harding revised to remove "one extra eighth note." Match rhythm to mood — monosyllabic and angular for weight, fluent and polysyllabic to move fast. Kill sing-song, kill cutesy internal rhyme. Keep it "angular, a little choppy, but funky." If a line doesn't *play* aloud, re-tune it.

> **Final gut check (the calibration test):** would Paul Harding recognize this as a mind paying real attention — or as someone filling lyric-prose slots? If unsure, it's the second. The most common tell: the piece *announces* its significance somewhere instead of letting the chain earn it. Slow down and rewrite one more time.

## Content Type Adaptations

| Format | Adaptation |
|---|---|
| **Social (LinkedIn / X / Substack Note)** | The whole post is one short literal chain off one seed image. Open on the seed (Step 3), run a *tight* chain (Step 4), keep the felt layer light (Step 5), close *open* (Step 6). Depth-not-width is brutal here — one luminous re-seen image beats five competent observations; a short post that feels substantive and re-readable is the entire goal. No "here's what I learned" frame, ever (AI-tell, banned). The description *is* the post. |
| **Marketing / brand** | The brand's "character" emerges from what its world *notices* and how it names things (description-becomes-character), not adjectives on the about-page. Pick a *real* overlooked thing in the product/experience, run the chain on it, let the felt benefit refract through (recognition, not a claim). **Honesty spine is load-bearing — the particular must be true.** Never slather; precision releases the wonder a claim can only assert. |
| **Copywriting** | Give the reader the **literal product detail (true)** via the chain, then the **felt experience of it** via Step 5 — let them infer the benefit through recognition, which they trust more than a stated benefit. **The detail must be real, and the claim it amplifies must be substantiated** — route any unprovable claim back to copy-engine / luke-iha; this engine renders and amplifies a *true* thing, it never manufactures proof or makes a false claim *sound* recognized. The close still opens (no hard moral); the CTA, if any, follows separately. |
| **Ghostwriting** | Surrender to the **client's** grain, not Harding's. The ordinary subject is *theirs*, the seed image is what *they* would have overlooked, the chain runs in *their* register and kind of verb — never pastiche a master onto them. Erase the seam between their world and their worldview (Step 5). The piece must read as theirs; the recognition is the *reader's* recognition of *the client's* truth. |
| **Substack edition / long-form essay** | The native habitat — the most room. Full Steps 1–7. Let the literal chain run long (Pattern 3 territory; extend with `/harding-then-what` if it wants to go further). Overwrite then distill hard (Step 7). May carry a zeitgeist tether (Stacking) — but the ordinary subject stays the front door and the chain stays the spine. End by opening a door so the reader returns to the edition rather than filing it. |

## Output Format

Deliver exactly this:

```
SUBJECT (one overlooked thing): __________   ·   FORMAT: __________   ·   WHOSE GRAIN: __________
POINT OF CONTACT (honesty anchor): __________  [real memory / in front of me / observed scene]
ZEITGEIST TETHER (if topical): __________   ·   FELT CHARGE: __________
BANNED HABITUATED LABELS: __________
SEED IMAGE (the overlooked literal detail the piece opens on): __________

— THE PIECE —
[Opens on the seed image rendered precisely and in motion (Steps 3–4), the literal chain run through
the body link by physically-true link with meaning accruing not stated (Step 4), the felt experience
refracted through the thing with the seam erased (Step 5), distilled and tuned aloud (Step 7), and
closing by opening a door — image-close / bookend / quiet declaration, no takeaway, no cheap question (Step 6).]

— CRAFT NOTE (two lines, plain) —
The chain: [seed image] → [link] → [link] → [where it accrued to]. What I cut: __________.
Recognition target: the reader thinks "________" (a felt truth they'd never seen put into words) — not "good point, noted."
```

### Worked example A — Substack edition / essay opening (the swan boat; Harding's own transcript example, deployed as content)

**Subject:** the swan boat on the Common pond when I was seven. · **Format:** Substack edition opening. · **Contact:** vivid childhood memory. · **Felt charge:** time closing over you, the foreknowledge of loss. · **Banned labels:** *the pretty swan boats*, *a peaceful pond*, *a magical summer day*. · **Seed image:** the mold-seam down the plaster swan's breast.

**The piece (opening):**
> The pond held the willows upside down on its skin and didn't let them move. We slid out over them. Behind us the foot-paddle slapped its slow metronome and the wake opened in two long arms, widened, thinned, and was taken back into the water without a mark, again, and again, so that the pond kept closing over where we had just been. The swan up front was plaster, white, its neck a painted S, and down its breast ran the seam where the two halves of the mold had been pressed together and would never quite come apart. The shade of a willow crossed the bench and the wood went from warm to cool under my legs and then warm again on the other side. I was seven and did not yet have the words that would one day let me lose this — but I knew, the way a boy knows a thing in his skin first, that the day was a thing that closed over you and took you back without a mark.

*Why it works as content (Harding's standard):* It opens on the **seed image** — the wake taken back, the mold-seam — never on a claim or a "here's what summer taught me" frame (Step 3). The body is a **literal chain** (Pattern 3): the wake *opens, widens, thins, is taken back*; the shade *crosses*; the wood goes *warm to cool to warm* — meaning accrues, never stated. The felt charge (loss, time) is **refracted through** the wake "taken back without a mark," with the seam erased (Steps 4–5, Patterns 6/4). It **closes by opening a door** — a quiet declaration that names the recognized thing without moralizing it; no takeaway, no "cherish every moment" (Step 6, Pattern 10). Depth-not-width: one subject, one chain, all the way down (Pattern 9). The reader doesn't think "good point" — they think *"I've ridden that boat; somebody finally put that into words."* The banned labels never appear.

### Worked example B — LinkedIn / short social post (a hayed meadow at dusk; for a coach writing about endings)

**Subject:** the meadow behind the gym after the first cut, at dusk. · **Format:** LinkedIn post. · **Contact:** observed scene, this week. · **Felt charge:** a season of work ending while you're still standing in it. · **Banned labels:** *peaceful*, *the beauty of nature*, *a fresh start*. · **Seed image:** the stubble holding the shape of the swaths the mower drove. · **Honesty spine:** every detail is of the real field.

**The piece:**
> The meadow behind the gym got cut yesterday and the stubble still holds the shape the mower drove — long pale swaths curving where it turned, so the whole field reads like a record of every pass, laid down and left. The cut grass went from green to grey to almost gold as the light dropped, and the smell of it kept coming up off the ground after dark, sweeter than the standing field ever smelled, the way a thing gives up the most of itself right after it's taken down. The crickets started in the part already in shadow before they started in the part still lit, so you could hear the dark crossing the field a few feet ahead of where you could see it. I stood there a while. The season's work was all over the ground and the season wasn't done with me yet.

*Why it works as social content:* One seed image (the stubble holding the swaths) opens it — no "here's what I learned about endings" (Step 3, AI-tell avoided). A **tight literal chain** runs the short body: the swaths → the color dropping green-to-grey-to-gold → the smell coming up *sweeter after it's cut* → the crickets marking the dark crossing the field (Step 4, with the calculus in every verb). The felt truth — a season of effort ending while you're still inside it — is **refracted**, never stated, and lands in the quiet-declaration close that *opens* rather than instructs (Steps 5–6). Depth-not-width: short, dense, re-readable — the post nobody says they read once (Pattern 9). Honesty spine intact: it amplifies a *true* observed thing; it claims nothing it can't show.

## Stacking

This workflow is built to compose. The stacks change *what subject* you re-see and *how the piece earns attention* — never the engine, never the honesty spine.

| Stack with | What it adds | How it composes |
|---|---|---|
| **`/parallax`** (zeitgeist-first edition pipeline) | The trending topic + Farrice briefing. | Run `/parallax` Phase 1–2 to get the zeitgeist tether and the briefing, then bring the topic *here* as the **tether** and find the ordinary subject that quietly carries it — the subject stays the front door, the trend stays the relevance. Return the perception piece into the parallax package as the edition's essay. Parallax supplies the *what's-in-the-air*; Harding supplies the *soul that makes it re-read*. |
| **`/kallaway-illusion`** (perception of novelty) | The *feeling* that an old/ordinary subject is new and worth attention — the front-end perception engine (new reveal · contrast framing · outcome mapping). | Use kallaway to make the re-seen-ordinary subject *feel novel enough to earn the first read* (an old thing, freshly angled), then let Harding's literal chain deliver the *actual* depth that makes it re-read. **Honesty spine of BOTH stays intact:** kallaway engineers the feeling of novelty on a *real* angle; Harding renders a *true* particular. Neither fakes the substance — the facts and the perception both stay real. Novelty earns the click; recognition earns the return. |
| **`/harding-perception-engine`** | A single luminous passage, built bottom-up from raw observation. | When any one passage *inside* this piece needs deeper rendering (the opening, a key link in the chain), drop into `/harding-perception-engine` for that passage, then set it back into the whole. This workflow owns the *shape of the piece*; the engine owns the *craft of the passage*. |
| **`/harding-recognition-audit`** (if present) | A pass that checks the close *opens a door* and the piece persuades by recognition, not a takeaway. | Run as the final QA before delivery — it's the dedicated check for Step 6 and Pattern 10. |
| **`/addictive-perception-content`** | Engagement/retention mechanics for perception-driven pieces. | Compose when the piece needs to hold attention across length without trading away depth — it tunes *retention* while Harding holds *substance*. Guard: never let retention mechanics reintroduce a hot-take frame or a takeaway close. |

## Quality Gate

> **🛡️ Anti-Pattern Check**: review against `genius.md § Paul Harding Would Never... (Anti-Patterns)` and § Expert-Specific Quality Rubric (rows: **Pre-Linguistic Attention**, **Literal Chain (no rush to symbol)**, **The Two Things**, **Co-extensivity**, **Precision-as-Wonder**, **Cadence**, **Recognition over Lesson**). Flag and fix before delivering.

- **Opens on a seen thing, not a claim (Step 3, Pattern 2):** the first line is the precise seed image, not an abstract statement, not a "here's what/why/how" frame, not the trend named. If it opens on a claim, it's a hot take in a description costume — rebuild the opening on the seed.
- **The body is a literal chain (Pattern 3, AN-1, Rubric: Literal Chain):** meaning *accrues* link by physically-true link; nothing is announced as "symbolic," and you never arrive at the "point" without an unbroken chain leading there. If significance is stated, go back to the last literal link and ask "then what?"
- **Slowed down past recognition (Pattern 2, Rubric: Pre-Linguistic Attention):** the seed image and at least one body link are things the reader would skip on autopilot — freshly *seen*, not recalled from the category. The banned habituated labels (Step 1) appear *nowhere*.
- **Precision, not ornament, with the calculus (Pattern 8, AN-4, Rubric: Precision-as-Wonder):** the ordinary turned luminous *through* exact, moving description — something changes over time, the verbs carry it, and no decorative adjective is doing the lifting. No pathetic-fallacy slather, no adjective stacks.
- **Both things, refracted not stated (Pattern 6, AN-3, Rubric: The Two Things):** the literal thing came first (true), the felt experience is refracted *through* it — no emotion named, no feeling explained.
- **No clanking gears (Pattern 4, Rubric: Co-extensivity):** a reader can't locate where description ends and the perceiving mind begins. No "I looked at it and remembered…" seams.
- **Closes by opening a door (Step 6, Pattern 10, AN-3, Rubric: Recognition over Lesson):** the ending invites recognition and leaves the reader opened — an image-close, bookend, or quiet declaration. NO takeaway, NO "and that's when I realized," NO moral, NO cheap question signoff. The reader wants to return, not to file it.
- **Depth, not width (Pattern 9):** the piece is dense and re-readable, earning its length by lived experience, not by extra examples or a second subject. One chain, all the way down. The piece nobody says they read once.
- **It plays aloud (Pattern 11, Rubric: Cadence):** read cold, accents fall where meaning wants them — angular, lucid, no sing-song, no stray eighth note.
- **Honesty spine intact:** every rendered particular is *true* of the real subject, and any persuasive claim the piece carries amplifies a *substantiated* true thing — no invented "vivid" detail, no device making a false or unprovable claim *sound* recognized-as-true. In commercial work, route unsubstantiated claims back to the copywriter; this engine amplifies truth, it never manufactures it.
- **The calibration test:** would Harding recognize a mind paying real attention, or someone filling lyric-prose slots? If the second — rewrite.

## Common Pitfalls

- **The hot-take reflex wearing a description costume (Step 0 / Step 3 failure, AN-1 + AN-3).** The piece *looks* like perception content — nice sentences, a concrete subject — but it actually opens on a claim, illustrates a pre-decided point, and closes on a takeaway. The description was decoration on an argument. This is the single most common failure and the whole reason this engine exists. **Recovery:** re-run Step 0 (is this a perception piece at all?) and Step 3 (open on the seed, not the claim). Delete the thesis-up-front and the takeaway-at-the-end; let the literal chain (Step 4) carry the meaning so it *accrues*. If you can't bear to cut the takeaway, you wrote a hot take — route it to the right engine and start the perception piece over from a real seed image.

- **Going wide to feel substantive instead of going deep (Pattern 9 failure).** Adding a second subject, a third example, a broader frame — covering more ground to make a short piece feel "complete." This produces width, which is exactly the wrong axis; "comprehensive" is the tell of failure. **Recovery:** Step 7 distill. Cut back to the *one* subject and the *one* literal chain, and go *deeper* — ask "then what?" two more links than you did. A swan boat followed all the way down to "took you back without a mark" beats a swan boat plus a sunset plus a childhood lesson. Density, not coverage. The substance is in the depth of attention, never the breadth of topics.

- **Stating the felt charge instead of refracting it (Step 5 failure, AN-3).** Writing "it was so nostalgic, and it made me realize how fleeting time is" — telling the reader how to feel, which is "the most violent thing you could do" and, in content terms, kills re-readability (a stated feeling is consumed once). **Recovery:** Step 5. Cut every named emotion and every "made me realize." Give the precise literal thing first (Steps 3–4), then let the feeling live in *what gets noticed and how it's named* — the wake taken back without a mark, the smell sweeter after the field is cut. The reader feels it harder, and returns to the piece, because they recognized it rather than being handed it.

- **Inventing the seed image because it "sounds good" (honesty-spine breach — the most dangerous, because the craft makes the lie convincing).** Reaching for a vivid opener you didn't actually observe — especially in topical or commercial work where a perfect detail is tempting. The better your precision, the more believable the fabrication, and the entire engine runs on the reader trusting that what you rendered, you saw. **Recovery:** re-establish the **point of contact** (Step 1). Describe only what you have genuinely perceived or can truthfully recall; if the detail isn't real, go observe it or choose a different true subject. In copy, route unprovable claims back to copy-engine / luke-iha. Harding's craft makes a *true* thing land harder — it never fakes one, and a perception piece built on a fabricated detail isn't elevated content, it's a convincing lie.
