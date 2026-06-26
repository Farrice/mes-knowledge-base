---
description: "/wang-insight-synthesis — take a disorganized pile of notes, research, clippings and observations and distill ONE voice-driven insight piece: find the throughline, mine the official-vs-ground friction, choose the anchor sentence, then write the whole thing in haste in one coherent voice. The synthetic/syncretic move — combine the big with the small, the formal with the informal, the rational with the irrational — not a summary, not a survey of open questions, but a finished piece that stakes an answer and reads as one mind thinking."
---

# Wang Insight Synthesis — A Pile of Notes Into One Voice-Driven Piece (Dan Wang)

Dan Wang does not sit down to write a letter from a clean outline. He spends a year dumping fragments into one running file — a sentence overheard at a Shenzhen stall, a number that contradicts the press release, a paragraph copied out of Stendhal, the taste of barbecue eaten in Austin while reading about semiconductor policy — and then, against a deadline, in roughly ten hasty days, he *synthesizes*. His own word for what he is reaching for is **synthetic, even syncretic**: combine the big with the small, the formal with the informal, the rational with the irrational, find the right sweet spot, refuse to be captured by a single genre or method. That is the move this workflow runs. It is not summary (summary flattens a pile into bullet points and kills the voice). It is not a survey of open questions (Wang's rule: "let's not just outline the questions — let's also try to have an answer"). It takes the heap as it actually is — messy, contradictory, half of it tangents — finds the one throughline strong enough to carry a piece, mines the friction inside the notes, builds the whole thing around one beautiful sentence, and writes it in a single coherent voice that oscillates between the meal and the macro-trend without ever sounding like two authors bolted together. The deadline is not the enemy. The haste is the forcing function that fuses the fragments into a piece the slow accumulation never would.

## Pre-Flight

Read before executing — load these `genius.md` sections (do not paraphrase from memory; the patterns are precise, and this workflow fails the instant it becomes a tidy summary of the notes instead of a synthesis that *combines* them into one voice):

- **Pattern 5 — Year-Long Note Accumulation → Sprint Production** — the engine. The pile is the input; the deadline-driven sprint is what fuses it. "Output feels both spontaneous AND deeply considered." This is the only Wang workflow whose *starting material is a mess* — embrace it.
- **Pattern 15 — The Network Effects of Knowledge** — the close. Reject the depreciation model of knowledge; the disparate, "irrelevant" notes are not noise — the breadth is what makes the synthesis possible. Learning compounds; the barbecue-while-reading is part of the substrate. This is what makes the piece syncretic rather than narrow.
- **Pattern 6 — The Single Beautiful Sentence Method** — the spine. Somewhere in the pile is the anchor; the piece is built around it, not summarized toward it. (Deep refinement → stack `wang-anchor-sentence`.)
- **Pattern 4 — Formal/Informal Friction Mining** — the analytical charge. The piece's insight is the gap between the official/stated story and the observed/ground truth — and that gap usually already lives *inside the pile*, in the contradiction between two notes. (Deep mapping → stack `wang-friction-map`.)
- **Pattern 8 — The Zoom In/Zoom Out Oscillation** — the voice mechanism. After every concrete note, elevate to what it means; after every abstraction, ground it in a note. This is how the formal and informal fuse into one register instead of two.
- **Pattern 19 — Contingency Over Just-So Stories** — the honesty guard. When the throughline explains *why something happened*, reconstruct how it felt before the event; resist the tidy hindsight narrative that smooths the pile into inevitability.
- **How to Use This Skill (synthesis/syncretic; ship at 85%)** — texture is the argument not the garnish; one coherent author not a committee; ship at 85% (the deadline forces synthesis, perfectionism kills cornerstone content); influence not imitation; do NOT label the moves.
- **Decision Framework** — the gate below.

> **🔒 Pre-Flight Gate**: run the **Decision Framework** in `genius.md § Decision Framework` before distilling a single line. This workflow lives or dies on three of its questions. **Q1 (the big question):** can you name the one tension this pile is actually *about* — and are you prepared to *answer* it, not just survey what the notes raise? A pile with no throughline is not ready; keep accumulating, or you'll produce a summary. **Q2 (the friction):** is there a real gap between the official/stated story and the observed/ground truth somewhere in this pile — often the *contradiction between two of your own notes*? No friction = no insight = you're about to restate the consensus. **Q5 (the anchor):** is there one beautiful, quotable sentence in the heap (or one you can refine out of it) to build around? If not, keep refining notes until one arrives — do not manufacture it. **The syncretic test (How to Use):** does this piece *combine* registers — the big and the small, the formal and the informal, the rational and the irrational — or is it captured by one genre (dry report / lush travelogue / insight-porn)? If it sits cleanly in one box, it isn't yet synthesis. And the honesty spine: synthesis *combines what's in the pile* — it never fabricates a note, a number, or a scene that wasn't observed. If the throughline needs a fact the pile doesn't contain, that's a research gap (→ `deep-research` / `research.py`), not a license to invent.

## Input Required

- **The pile** — the actual heap, dumped as-is. Notes, research excerpts, clippings, half-sentences, observations, a number you scribbled, a quote you copied, a meal you remember, a contradiction you noticed. Messy is correct. Do NOT pre-organize it — the disorder is the raw material, and pre-sorting often kills the surprising adjacency that becomes the throughline. Bring it all, including the "irrelevant" fragments (Pattern 15 — they're the network effect).
- **The format and rough length** — annual letter / essay / Substack / LinkedIn / X thread / marketing manifesto / copy / ghostwritten piece. Drives how much of the pile becomes prose and how much stays as the engine underneath.
- **The audience** — who reads this and what they're already preoccupied with (feeds Q1: the big question is *their* live tension, not your favorite note).
- **The deadline** — real or self-imposed. Non-optional. The sprint is the synthesis-forcing function (Pattern 5, Tacit 2); without a deadline the pile stays a pile. Name a ship date now.
- **The voice** — yours, or (if ghostwriting) the client's. One coherent author runs through the whole thing; name whose sensibility is doing the oscillating.
- **Felt verdict target** (optional) — what the reader should walk away holding: a wry recognition, an uncomfortable agreement, a reframe, a quiet ache. Helps Step 3 choose the anchor and Step 5 tune the close.

## Workflow

### Step 1 — Read the whole pile once, fast, hunting for heat (Pattern 5 + Pattern 10's instinct)

Do not organize. Do not outline. Read the entire heap in one pass, fast, the way Wang reads a book asking "did the author *want* to write this or *have* to?" — except here you're asking it of your own fragments. You are looking for **heat**: the notes you wrote with energy, the contradictions that nagged at you, the sentence you couldn't stop turning over, the observation that surprised you when you made it. Mark them. Ignore the dutiful, the obvious, the press-release-restating notes (those are the obligated sections of your own mind).

Tag each fragment as you go — one letter in the margin is enough:

| Tag | What it marks | Why it matters to the synthesis |
|---|---|---|
| **H** — Heat | You wrote it with energy; it surprised you; you keep returning to it | These cluster around the real throughline. Energy is the signal the slow accumulation buried |
| **T** — Texture | A concrete observed detail: a meal, a walk, a scene, an object, a number | The gateways (Pattern 3). Every abstraction will need one of these to ground it |
| **A** — Abstraction | A big claim, a pattern, a tectonic-plate idea | Floats unless married to a T. Note which A's have a T nearby |
| **F** — Friction | A contradiction — between two notes, or between a note and the official story | The analytical engine (Pattern 4). The gap *is* the piece |
| **L** — Line | A sentence that already rings — quotable, ironic, alive | Anchor candidates (Pattern 6). Star the strongest |
| **X** — Cut | Dutiful, obvious, or restating consensus | The pile's dead weight. Leave it in the file; it doesn't go in the piece |

> **The breadth guard (Pattern 15):** before you cut anything as "irrelevant," check whether a *distant* fragment (the Mozart aside, the barbecue, the unrelated book) actually rhymes with a Heat note. The syncretic surprise — the reason the piece reads as one mind seeing a connection no one else saw — almost always comes from an adjacency between two notes that don't obviously belong together. The network effect of knowledge is exactly this: the breadth makes the connection possible. Don't prune the pile to a single topic before the throughline reveals itself.

### Step 2 — Find the throughline: the one tension the Heat notes are circling (Q1)

A pile contains many small insights. A piece has *one* throughline — the single tension or question that the Heat cluster keeps orbiting. This is the synthesis decision, and it is a decision, not a discovery you wait passively for. Look at your H and F tags together and ask: **what is the one big question all this heat is actually about?** Then commit to *answering* it — Wang's "draft 1.5 of history," past the daily-news first draft, short of the historian's final one. Not "here are five things I noticed about X." One thing, argued.

Run the candidate throughlines through this filter:

| The throughline must… | Test | If it fails |
|---|---|---|
| **Be a live tension for the audience** (Q1) | Are the smartest readers in this space already arguing about it right now? | It's your hobby-horse, not the piece's reason to exist. Find the one the audience is preoccupied with |
| **Be answerable, not just survey-able** | Can you state a *position* on it in one sentence, however imperfect? | You have a topic, not a throughline. Keep reading the Heat until a claim forms |
| **Run through the friction** (Q2 / Pattern 4) | Does it ride the gap between the official story and the ground truth in the pile? | It restates consensus. There's no insight yet — find the F notes it ignores |
| **Subsume the most Heat** | Do most of your H and L notes ladder up to it, or only a few? | It's too narrow. The best throughline is the one that makes the *most* of the pile suddenly relevant |
| **Carry your disappointment / outsider distance** (Pattern 21 / 7) | Is there a standard underneath — "this could be better; why isn't it?" | Generic. The throughline with teeth comes from productive disappointment, not neutral reportage |

State the throughline as one declarative sentence. This is the spine the synthesis hangs on. (If the friction is rich and you want to map it formally before drafting, stack `wang-friction-map` here — it turns the F notes into a two-column engine. This workflow assumes a lighter, in-line friction read.)

```
THROUGHLINE (one declarative — the position you're staking): __________
THE BIG QUESTION it answers (the audience's live tension): __________
THE FRICTION it rides (official story ___ vs. ground truth ___): __________
```

### Step 3 — Choose the anchor and the syncretic structure (Pattern 6 + the synthetic move)

Now two decisions that turn a throughline into a *piece*.

**First, the anchor (Pattern 6, Q5).** Look at your L tags — the lines that already ring. Pick the one that compresses the throughline most: beautiful, quotable in isolation, with irony or tension coiled inside (a Wang line is almost always double-edged — the prosperity that tastes of survival, the chosen who still lock their cars). This becomes the gravitational center; the piece will be built to *earn* it, not to mention it. If no line in the pile is strong enough, this is the moment to refine one — stack `wang-anchor-sentence` for the full capture-and-refine method. Do not manufacture a thesis-in-costume; if nothing rings yet, the pile isn't ripe (Q5).

**Second, the syncretic structure.** This is the move that makes it Wang and not a report. You are deliberately *combining registers* so the piece can't be slotted into one lazy genre. Map your strongest fragments across the three Wang oppositions and confirm the piece will hold both poles of each:

| The opposition to fuse | The "big / formal / rational" pole (from your A and analysis notes) | The "small / informal / irrational" pole (from your T and observation notes) |
|---|---|---|
| **Big ↔ small** | The macro-trend, the systemic claim | The single meal, walk, object, scene that is its gateway |
| **Formal ↔ informal** | The official story, the data, the literature | The overheard line, the texture, the joke, the aside |
| **Rational ↔ irrational** | The argument, the mechanism, the causal claim | The mood, the irony, the aesthetic pleasure, the unease |

> **The sweet-spot rule (How to Use):** the synthesis isn't "first the analysis, then a travel anecdote for color." It's the two poles *in the same passage*, the zoom oscillating fast enough that the reader experiences one mind moving between them (Pattern 8). If your structure has a "report section" and a "voice section," you've bolted two authors together — re-thread so the texture and the idea share paragraphs. The piece that lasts transcends its own genre's pull (Pattern 18): not the dry report, not the lush travelogue, not the Gladwellesque one-anecdote-one-takeaway formula — the sweet spot none of those genres can hold.

```
ANCHOR (the line the piece is built to earn): "__________"
ANCHOR POSITION: [closer / hinge / cold open] — because __________
SYNCRETIC SPINE — the oscillation, beat by beat:
  Open: [TEXTURE the anchor will rhyme back to] → [the throughline it opens onto]
  Mid:  [the official story, formal] → eroded by [the observed ground truth, informal]
  Turn: [the friction named; contingency restored if explaining a 'why' — Pattern 19]
  Earn: [plain runway — quiet the prose before the anchor]
  ▶ ANCHOR LANDS
  Close: [the network-effects move — see Step 5]
```

### Step 4 — Write it in haste, in one voice, at 85% (Pattern 5 sprint, Tacit 1 & 2)

Now draft against the deadline. This is the sprint, and the haste is doing real work: it forces the fragments to fuse, because you don't have time to keep them separate. Write fast, in one sitting if you can, in the one coherent voice you named.

The drafting discipline:

- **Oscillate constantly (Pattern 8).** Ground every abstraction in a texture note within a sentence or two; elevate every texture to what it means. Never let a tectonic-plate claim float (AN-1); never let a pretty detail sit there carrying no idea (AN-2). The zoom is the voice.
- **One author, not a committee (How to Use).** The analytical paragraphs and the personal/observed paragraphs are the *same* sensibility oscillating, not two registers stitched together. If you can feel the seam between "the writer" and "the analyst," you've failed the synthesis — re-blend.
- **Let the contradictions in (Pattern 19).** Where two notes disagree, don't smooth them into a just-so story. The honest piece reconstructs how the moment actually felt before the outcome was known — "every event feels impossible before it happens and obvious after." Hold the contingency; it's what makes the eventual point feel earned, not assumed.
- **Influence, never imitation (How to Use).** Do not pastiche "Dan Wang voice." Soak the instinct — the zoom, the irony, the textured opening — and write so it's native to *this* subject and *this* voice. Forced "literary" cadence in someone else's register reads as costume.
- **The sentences are yours (AN-6).** The model is a sparring partner for thinking *through* the connections — never the pen for the prose. The flat, hedge-y, "on the one hand / on the other" AI register is the death of the voice. Write the sentences from within.
- **Ship at 85% (Tacit 1).** No writer is ever more than 85% satisfied. When you hit it, stop. The deadline is a feature; perfectionism past 85% kills cornerstone content and the synthesis is already done.

> **The haste paradox:** the goal is output that "feels both spontaneous AND deeply considered" (Pattern 5). The deep consideration is the year of accumulation; the spontaneity is the ten-day write. Don't try to make the draft feel labored — the labor already happened in the pile. Trust it and move.

### Step 5 — Close on the network effect; then the cold read (Pattern 15 + the synthesis gate)

**The close.** A Wang piece does not end on a summary. The strongest close enacts **Pattern 15 — the network effects of knowledge**: the seemingly disparate fragments turn out to be *connected*, and that connection is the reward — the reader feels the breadth pay off, the way the barbecue and the semiconductor policy and the Mozart aside were secretly one thought all along. The close is where the syncretic move is *vindicated*: the small detail you opened on rhymes back to the big question; the irrelevant note proves load-bearing. Reject the depreciation model — nothing in the pile was wasted; the learning compounded into this. End forward-looking, not recapping. (Avoid the cheap question-signoff; close on an image, a declaration, or a bookend back to the opening texture.)

**The cold read.** Read the whole piece aloud, cold, as a first-time reader, then run the four synthesis gates:

- **Synthesis, not summary:** does the piece *combine* the fragments into one argument, or does it list what the notes said? If a reader could reconstruct your tag list from the piece, you summarized — re-thread so the fragments fuse.
- **Syncretic, not captured:** can the reader slot this into one lazy genre (dry report / travelogue / insight-porn)? If yes, the registers didn't fuse — strengthen the weaker pole until both hold.
- **One voice:** is there an audible seam between the analytical and the personal? If yes, re-blend the oscillation (Pattern 8).
- **The anchor lands surprising-and-inevitable:** at the anchor, does the reader feel both "didn't see that coming" and "of course"? If only one, the runway (Step 3) didn't prepare it.

## Content Type Adaptations

| Format | Adaptation |
|---|---|
| **Social (LinkedIn / X)** | The whole post is a *micro-synthesis* — three or four fragments fused into one throughline, built around the anchor (usually the last line). Almost no runway: open on the single sharpest texture note, zoom to the one big question, land the anchor. The network-effects close is implicit — the surprising adjacency *is* the post. One considered synthesis beats ten reactive takes (Pattern 20). The thread version lets each fragment breathe; the single post compresses to the anchor alone. |
| **Marketing / brand** | The pile is your discovery notes, customer quotes, category research, and lived observations. The throughline is the friction between what the category *says* and what the customer *lives*; the synthesis becomes the campaign's organizing idea. The anchor becomes the manifesto line. Network-effects close: the disparate proof points (the review, the data, the founder's story) turn out to be one promise. Reject category-cliché phrasing (Tacit 7, the cover-photo strategy). |
| **Copywriting** | The pile is voice-of-customer notes, proof points, mechanism research, objections. Synthesize into one through-argument the page is built to deliver, grounded in concrete observed moments (texture over feature-list). Recognition anchoring (Pattern 16) before the anchor — the second-person "you've felt this." **Honesty spine non-negotiable:** synthesis combines *true* notes; it never fabricates proof to complete the throughline. A missing claim is a copy-engine / luke-iha job, not an invention. |
| **Ghostwriting** | The pile is the *client's* notes, voice memos, and observations — and the synthesis must read as one coherent author: the client. Soak their cadence; the oscillation between their analysis and their personal texture must be unmistakably theirs. Never insert your own showpiece sentence. The anchor is the line they'd have written on their best day (influence, not imitation). |
| **Content / essays / newsletters / annual letters** | Native habitat — the full Pattern 5 form. The pile is a season or year of accumulation; the deadline is the sprint. This is the workflow's home, and it feeds `literary-cornerstone-sprint` (this is the *front half* — the distillation that produces the throughline + anchor + syncretic spine the sprint then drafts to length). Layer the flower for re-readers (Pattern 2); ship at 85%; build reputation through radical infrequency paired with radical quality (Pattern 20). |

## Output Format

Deliver exactly this:

```
THE PILE: [n] fragments · format: __________ · deadline: __________ · voice: __________

— THE DISTILLATION —
THROUGHLINE (the position staked): __________
BIG QUESTION answered (audience's live tension): __________
FRICTION ridden (official ___ vs. ground ___): __________
SYNCRETIC CHECK: combines big↔small, formal↔informal, rational↔irrational [confirmed]

— THE ANCHOR —
"__________"
  Surface reading (scanner gets): __________
  Second reading (the irony / tension underneath): __________
  Position: [closer / hinge / cold open] — because __________

— THE SYNCRETIC SPINE (the oscillation that fuses the pile) —
  Open  → [texture note] opening onto [the throughline]
  Mid   → [official story] eroded by [observed ground truth]
  Turn  → [friction named; contingency held if explaining a 'why']
  Earn  → [plain runway before the anchor]
  ▶ ANCHOR LANDS
  Close → [network-effects: the disparate fragments revealed as one thought]

— THE PIECE —
[The finished, voice-driven synthesis at 85%, written in one coherent voice,
 oscillating zoom, grounded throughout, built to earn the anchor.]

THROUGHLINE RATIONALE (why this throughline, from this pile):
  [2-4 sentences: which Heat notes it subsumed, which friction it rides,
   which "irrelevant" fragment turned out load-bearing in the close.]

SYNTHESIS-GATE CHECK: synthesis-not-summary · syncretic-not-captured · one-voice · anchor-lands [confirmed]
```

### Worked example A — Substack essay (a pile about China's EV boom)

**The pile (excerpt of fragments):** a note on a factory floor in Hefei smelling of "hot epoxy and instant coffee" (T); the official figure — China made >60% of the world's EVs in 2024 (A, official); a scribbled contradiction — the dealership lot in a third-tier city full of unsold inventory under tarps (F, ground truth); a line copied from a battery engineer's offhand remark, "we are not building cars, we are building the grid" (L); an unrelated note about a Sichuan hotpot meal where the bill was paid by phone in two seconds (T); a paragraph on the price war eating margins (A); a memory of reading Kotkin on Soviet industrial overcapacity (the "irrelevant" breadth note, Pattern 15).

**The distillation.** THROUGHLINE: *China's EV dominance is real and is also a glut — the same overcapacity that looks like victory from the outside is, on the ground, a margin-destroying war that only the state can subsidize through.* BIG QUESTION: is China's EV lead a durable industrial triumph or a subsidized bubble? (the thing analysts are arguing about right now). FRICTION: official "60% of the world's EVs" vs. observed tarped, unsold inventory and vanishing margins. SYNCRETIC: big (industrial-policy claim) ↔ small (epoxy-and-coffee factory floor, two-second hotpot payment); formal (production data) ↔ informal (the engineer's aside); rational (overcapacity argument) ↔ irrational (the eerie pride of a country building at a loss).

**The anchor (refined from the L note):** *"They are not building cars. They are building the grid — and they will keep building it long after the building stops making sense."* — Position: hinge. Surface: the EV push is really an energy-infrastructure play. Second reading: "long after it stops making sense" — the overcapacity isn't a bug being corrected; it's the logic itself, the same fated-and-not-fated industrial momentum Kotkin saw in the Soviets. The Kotkin note — the "irrelevant" one — becomes the close: the disparate fragments (hotpot payment, tarped lot, Soviet overcapacity) turn out to be one thought about what it means for a state to build past the point of sense. Network effect vindicated; nothing in the pile wasted.

### Worked example B — LinkedIn post (a small pile about AI adoption)

**The pile:** a note that a client's whole team has ChatGPT licenses but the docs are still written by hand (F); the official story everyone posts — "AI is transforming knowledge work" (A); a texture note — the one analyst who quietly drafts in AI then rewrites every sentence so it sounds like her (T, H); a half-line, "the tool is adopted; the habit isn't" (L).

**The distillation.** THROUGHLINE: *AI adoption is being measured in licenses, but it lives or dies in habits — and the gap between the two is where all the disappointment is hiding.* FRICTION: official "AI is transforming work" vs. observed team-with-licenses-still-writing-by-hand. SYNCRETIC at post scale: big (the transformation narrative) ↔ small (the one analyst rewriting every sentence by hand).

**The anchor (closer):** *"The tool was adopted in a day. The habit is taking a year — and the dashboard only counts the day."* Surface: licenses ≠ usage. Second reading: the thing we measure (adoption) is the easy part; the thing that matters (habit) is invisible to the metric, so every "AI transformation" report is counting the wrong day. **The post:** open on the analyst quietly rewriting AI's sentences into her own voice (texture + Heat) → zoom to the license-vs-habit gap → land the anchor. One observation fused with one official story into one quotable line — micro-synthesis, not a take.

## Quality Gate

> **🛡️ Anti-Pattern Check**: review against `genius.md § Dan Wang Would Never... (Anti-Patterns)` and § Quality Rubric. Flag and fix before delivering.

- **Synthesis, not summary (Pattern 5 core):** the piece *combines* the fragments into one argument that none of them stated alone — it does not list or recap what the notes said. If a reader could reconstruct the pile from the piece, it summarized. Re-thread.
- **Syncretic, not genre-captured (How to Use / Pattern 18):** the piece holds both poles — big↔small, formal↔informal, rational↔irrational — and cannot be slotted into one lazy genre (dry report / lush travelogue / Gladwellesque insight-porn). If it sits cleanly in one box, the registers didn't fuse.
- **Every abstraction grounded, every texture earning (AN-1 / AN-2):** no tectonic-plate claim floats without a concrete observed gateway nearby; no sensory detail sits there carrying no idea. The zoom oscillates (Pattern 8).
- **The friction is real (AN-3 / Q2):** the insight rides a genuine gap between the official story and the ground truth — often the contradiction between two of your own notes. It does not restate the consensus as if it were analysis. Would an insider find it uncomfortable and accurate?
- **One coherent author (How to Use):** no audible seam between the analytical and the personal registers — it reads as one mind oscillating, not a voice-y intro bolted to a report body.
- **The anchor lands surprising-and-inevitable (Pattern 6):** the piece is built to earn one beautiful, quotable, ironic line; at the anchor the reader feels both "didn't see it coming" and "of course."
- **The close enacts the network effect (Pattern 15):** the disparate fragments are revealed as connected; the breadth pays off; the "irrelevant" note proves load-bearing. No summary close, no cheap question-signoff.
- **Contingency held, not just-so smoothed (Pattern 19 / AN-7):** where the piece explains a "why," it restores how the moment actually felt before the outcome — it doesn't smooth the pile into hindsight inevitability.
- **The sentences are the writer's, shipped at 85% (AN-6 / Tacit 1):** the prose came from within the human voice, not the model's smoothed register; the deadline forced synthesis and the piece shipped at 85% rather than stalling in perfectionism.
- **Honesty spine intact:** synthesis combined *only what was in the pile* — no fabricated note, number, scene, or proof point was invented to complete the throughline. Gaps were flagged for research, not filled by invention.

## Common Pitfalls

- **Summary wearing a synthesis costume.** The most common failure: the piece dutifully reports each cluster of notes in turn ("First, on production… Second, on margins… Third, a personal observation…") and calls the recap a synthesis. It has no single throughline and no fusion — it's an organized pile, not a piece. **Recovery:** return to Step 2 and force *one* declarative throughline that subsumes the most Heat; then re-draft so the fragments serve that one argument instead of taking turns. If you can still see the seams between notes, they haven't fused.
- **Pre-organizing the pile to death (the lost adjacency).** Sorting the heap into neat topic-buckets before reading for heat — which kills the surprising connection between two notes that don't obviously belong together, the exact connection that would have been the syncretic payoff (Pattern 15). **Recovery:** don't sort first. Read the whole mess in one fast pass (Step 1), tag for heat and texture, and let the throughline reveal the structure. The "irrelevant" fragment is often the close; pruning to one topic early throws it away.
- **Two authors bolted together.** A clean "analysis section" followed by a "personal/voice section" — the formal and informal never fuse, so the piece reads as a report with a travelogue stapled on (or vice versa). **Recovery:** Step 4's oscillation discipline. Put the texture and the idea in the *same* paragraphs; make the zoom move fast enough that one sensibility is visibly doing both. If you can name where "the writer" stops and "the analyst" starts, re-blend until you can't.
- **No throughline yet, so you force one (or fabricate a fact to complete it).** The pile genuinely lacks a live, answerable tension — but the deadline looms, so you either reverse a "profound" throughline out of thin air (it reads as a thesis in costume) or, worse, invent a note/number/scene to make the argument cohere. **Recovery:** honor the gates. If Q1/Q5 fail, the pile isn't ripe — keep accumulating, or ship a narrower honest piece on the one real fragment you have. If the throughline needs a fact the pile lacks, that's a research gap (→ `deep-research`), never a license to invent. A true small synthesis beats a fabricated big one every time.
