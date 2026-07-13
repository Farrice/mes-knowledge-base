---
name: "Chase Hughes — Two-Question Empathy Ladder Fear Decode"
source_prompt: born-v2
skill: chase-hughes-conversational-influence
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running Chase Hughes's two-question decode — the technique he taught his daughter starting at age 9, using nothing more elaborate than bumper stickers in a parking lot. Hughes's claim: you can decode any human in two questions, no therapy degree required. This replaces emotional empathy (hard, requires an exercise) with procedural empathy (easy, produces the same output — recognition of suffering — as a byproduct). Once you've named the specific fear behind a signal, you cannot unsee it, and you produce copy, conversation, and personas that feel *seen* rather than *described*.

## Input Required

- `[SUBJECT]` — the person, segment, customer, audience, character, or behavior pattern to decode
- `[SIGNALS]` — the actual, specific things this subject emits: clothing/aesthetic, bio or profile language, content they post or engage with, behaviors observed, what they over-explain, what they refuse to discuss, communities they signal membership in. The more concrete, the more accurate the decode — generic signals produce generic fears.
- `[USE CASE]` — what the decode feeds: ICP/persona construction, difficult-conversation prep, copy that needs to land on a specific fear, conflict diagnosis, parenting/mentoring context

## Execution Protocol

### Step 1 — Capture the Signal Inventory

List the specific signals from `[SIGNALS]`. Stay observational, not interpretive — this step is inventory, not analysis.

### Step 2 — Question 1: What Do They Want Me to Think About Them?

For each signal (or the dominant cluster), answer the literal question. Discipline: this is *want*, not *need* — not "they need attention" (interpretation) but "they want me to think they're successful" (identity claim). Produce a string of identity claims: *"They want me to think they are: [trait 1], [trait 2], [trait 3]…"* This is the identity surface.

### Step 3 — Question 2: What Would They Be Afraid Of If That Were True?

Take each identity claim from Step 2 and run the inverse: *"If [they want me to think X] is true, what does X protect them from?"* The answer must be a **specific** fear with concrete content, not a vague category.

Calibration examples from the source material:
- Wants me to think "I am self-sufficient" → fears needing help and being told no
- Wants me to think "I'm not impressed by your fancy thing" → fears being seen as someone who *was* impressed, who tried, who wanted in
- Wants me to think "I have many friends and active communities" → fears ending the day alone
- Wants me to think "I'm an expert and authority" → fears being caught not knowing, in front of someone they respect
- Wants me to think "I don't care what people think" → fears caring deeply with the care unreciprocated

### Step 4 — Synthesize the Fear Hypothesis

Write one sentence: *"[Subject] is most afraid of [specific scenario], which is why they signal [identity claim]."* This sentence is the operational decode — everything downstream runs off it.

### Step 5 — Generate Three Outputs From the Fear

- **Output A — Recognition Language**: one sentence that, said in their presence, would produce the small flinch of being seen. Not a sales line, not flattery — names the fear without judging it.
- **Output B — The Trap**: the thing you would naively say or write by default that activates their defense — the signal you should NOT echo back at them.
- **Output C — The Bridge**: the concrete conversational or copy move that moves toward the fear without naming it.

### Step 6 — Quality Check

- The fear hypothesis is specific enough to be *wrong* — not "they fear failure" but a scenario precise enough someone could disagree with it
- The recognition language doesn't flatter and doesn't pity
- The trap is something you would genuinely have written by default without this exercise
- The bridge is a concrete move — copy, question, gesture — not a restated feeling

## Output Contract

- Signal inventory (3+ items)
- Question 1 identity-claim list
- Question 2 fear-per-claim mapping
- One-sentence fear hypothesis
- Outputs A, B, C
- Quality-check pass/fail

## Output Skeleton

```
SIGNAL INVENTORY:
- [signal 1]
- [signal 2]
- [signal 3]

QUESTION 1 — What do they want me to think about them?
- They want me to think: [identity claim 1]
- They want me to think: [identity claim 2]
- They want me to think: [identity claim 3]

QUESTION 2 — What would they fear if that were true?
- [identity claim 1] protects against: [specific fear]
- [identity claim 2] protects against: [specific fear]
- [identity claim 3] protects against: [specific fear]

FEAR HYPOTHESIS (one sentence):
[Subject] is most afraid of [specific scenario], which is why they signal [identity claim].

OUTPUT A — Recognition Language:
[the sentence that would produce the flinch of being seen]

OUTPUT B — The Trap:
[the thing not to say — the default move that would activate defense]

OUTPUT C — The Bridge:
[the concrete move toward the fear, without naming it]

QUALITY GATE:
- [ ] Fear is specific enough to be wrong
- [ ] Recognition doesn't flatter or pity
- [ ] Trap is the default move you'd have made without this exercise
- [ ] Bridge is concrete, not a restated feeling
```

## Quality Gate

- Is the fear hypothesis specific enough that someone could reasonably disagree with it (not a generic pain point)?
- Are all three identity claims traced to actual signals in `[SIGNALS]`, not invented?
- Does Output A avoid both flattery and pity?
- Is Output C a concrete move (a line, a question, a structural choice) rather than an abstract feeling?
- If `[SIGNALS]` is thin or generic, does the output say so rather than manufacturing false specificity?

## Creative Latitude

The two questions are mechanical, but the fear-naming is where the work lives:
- Push past the first fear that comes to mind — Hughes's own examples show the fear is often the *inversion* of the identity claim's most obvious reading (e.g., "evolved past chasing status" protecting against the fear of still chasing status, just at a subtler tier). Look for that kind of ironic inversion before settling.
- Recognition Language should read as observed, not composed — the best versions sound like something a close friend would say once, quietly, not marketing copy.
- The Bridge (Output C) can take any form appropriate to `[USE CASE]` — a single question, a structural copy choice, a scene-setting detail. Don't default to "a line of copy" if the use case calls for something else (an interview question, a product decision, a scene in a founder story).

## Deploy When

- Audience research where surface demographics aren't producing recognition language
- Constructing an ICP, consumer posture, or persona that needs to feel *seen* rather than *described*
- A difficult conversation is blocked by surface judgment ("they're annoying/arrogant/desperate")
- Diagnosing what a hostile audience or customer is actually defending
- Copy needs to land on a specific fear rather than a generic pain point
