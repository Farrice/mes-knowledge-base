---
name: "Kallaway — Contrast Framing"
source_prompt: born-v2
skill: kallaway-illusion-of-novelty
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running Step 2 of Kallaway's Illusion of Novelty — Contrast Framing, the component that converts a fact into an event. New means nothing on its own; it only registers through a comparative relationship to old. When the brain believes it might be wrong, it freezes and pauses to recalibrate — that freeze is intrigue. A new claim presented nakedly is a fact. The same claim anchored to the belief it overturns is an event. Fire this whenever a reveal lands flat, reads as "mildly interesting," or gets scrolled despite being true — the diagnosis is almost always a missing or mis-paired contrast anchor.

## Input Required

```
[NEW ANGLE] — the reveal from Step 1 (a contrast with nothing to contrast to is dead on arrival)
[AVATAR'S HELD BELIEF] — what the avatar already believes about THIS topic, stated as a sentence they'd nod at. Be specific: name the actual number/rule/ritual, not a vague gesture. If unknown, this workflow cannot proceed — surface it first.
[ASSET TYPE] — where the contrast will land (changes how much room/loudness it gets)
```

## Execution Protocol

### 1. Surface the held belief (be ruthlessly specific)
Pressure-test the belief three ways: **Specific enough?** ("Floss every day, especially before bed, or you get cavities" is anchorable; "flossing is good" is not.) **Held, not assigned?** — it must be something the avatar genuinely believes, not a belief you wish they had so your contrast works; strawmen collapse the instant the reader thinks "I never thought that." **About THIS topic?** — not an adjacent one; contrast against the belief that sits directly under the reveal.

Output: `HELD BELIEF: "<one sentence, in their voice>"`

### 2. Construct the TRUE-OPPOSITE
The new angle must directly negate the held belief — same axis, flipped pole. Test: write the belief and the angle as a pair and ask "is the second the literal opposite of the first, on the same dimension?" Example — Belief: "more is better." Opposite: "amount is irrelevant; timing decides." ✓ (same axis). Adjacent miss: "you should use a filter." ✗ (different axis → confusion). If the angle isn't the true opposite: either reframe it so it does oppose the belief on the same axis, or discard and pick a different held belief it genuinely overturns. Never force a near-miss through.

Output: `TRUE-OPPOSITE: "<the new angle, framed as the negation>"`

### 3. Write the contrast inline (5+ variants)
Put the old belief and the new angle adjacent in the same breath. Templates (**vary, never verbatim**):
- "Everyone thinks *X*. Turns out *Y*."
- "You've been told *X* your whole life — and the number was basically made up. What actually moves the needle is *Y*."
- "*X* used to be the gold standard. *Y* makes it obsolete."
- "For as long as you can remember, the answer was *X*. It was never *X*. It was *Y*."
- "The thing everyone optimizes — *X* — turns out to be the one thing that doesn't matter. *Y* does."
- "*X* isn't wrong, exactly. It's just answering a question nobody should be asking. The real question is *Y*."

Vary the rhythm and entry point (some lead with the belief, some lead with the reveal then snap back). Keep gossip-whisperer register — under-claim the magnitude, let the gap do the work. No "HUGE NEWS," no exclamation tone.

### 4. Confusion-vs-Contrast check (kill switch)
For each variant: read cold and check whether the reaction is "wait, I might be wrong about that" (contrast → keep) or "...what does that have to do with this?" (confusion → cut). A line that produces a shrug is ALSO a fail (too weak — the angle isn't a true opposite; loop back to Step 2). Discard or repair every variant that confuses or shrugs.

### 5. State the GAP explicitly
The deliverable is not the fact and not the contrast line — it is the gap the contrast opens between current belief and new reality. Name it in one sentence so downstream proof and protection know exactly what tension they're servicing:

`THE GAP: "<reader currently believes X drives the result; if Y actually drives it, everything they've been doing is aimed at the wrong lever>"`

## Output Contract

Return, in this order: HELD BELIEF (one sentence, avatar's voice); TRUE-OPPOSITE (the negation + shared-axis confirmation); 5+ contrast variants (numbered, varied rhythm, whisper-register); a keep/repair/cut verdict per variant with one-word reason; THE GAP (single statement); one-line honesty-spine confirmation of which part is manufactured feeling vs. which underlying facts are real and verifiable. If the held belief cannot be specifically named, return that as the blocker instead of shipping a strawman.

## Output Skeleton

```
HELD BELIEF: "[one sentence, avatar's voice]"
TRUE-OPPOSITE: "[new angle as direct negation]" — shared axis: [what dimension both sit on]

CONTRAST VARIANTS
1. [line] — verdict: [keep/repair/cut] — [one-word reason]
2. [line] — verdict: ...
... (5+ total)

THE GAP: "[reader believes X drives the result; if Y actually drives it, ...]"

HONESTY CONFIRMATION: manufactured = [the framing/angle]; real & verifiable = [the underlying facts]
```

## Quality Gate

- Is the held belief specific enough to be anchorable (a stated number/rule/ritual, not a vague gesture)?
- Is the true-opposite genuinely on the same axis as the held belief — not adjacent, not a strawman?
- Do all shipped variants pass the confusion-vs-contrast check (produce "I might be wrong," not a shrug or "what does that have to do with this")?
- Is every variant in whisper register — zero exclamation/billboard tone?
- Is the gap stated as a single explicit sentence, and does the honesty confirmation correctly separate manufactured framing from real, verifiable fact?

## Creative Latitude

The six templates are starting shapes, not a menu to pick from mechanically — the strongest contrast often comes from combining two templates or inventing a new rhythm entirely once the true-opposite is locked. Push on where the gap lives: sometimes the sharpest contrast steelmans the old belief for a full beat before the snap (this lands harder in long-form and thought-leadership than a quick dismissal). Vary entry point deliberately across the five-plus variants — belief-first, reveal-first, and mid-belief-interruption are all legitimate and should each get at least one variant so the operator can feel which cadence fits the avatar's voice.

## Deploy When

A reveal exists but reads flat, or a piece "should be working but isn't" and the audit traces the failure to Contrast. Feed its output to the full forge or hand the contrasted hook straight to a body-writing pass.
