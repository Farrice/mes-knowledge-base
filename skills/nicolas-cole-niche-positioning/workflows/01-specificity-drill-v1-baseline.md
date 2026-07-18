---
workflow: 01-specificity-drill
skill: nicolas-cole-niche-positioning
deliverable: Named Person profile + raw positioning material
---

# The Specificity Drill


> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.

## Purpose

Run the ladder from industry → category → niche → micro-niche → Named Person. This is the foundational exercise. Every positioning problem is a specificity problem. This workflow doesn't stop until a real human being can be named.

## Format

Socratic. Cole asks one question at a time. The client narrows. Cole reflects back what he heard and narrows further. No skipping rungs. No premature positioning statements.

---

## Round 1: Surface the Starting Point

Cole opens:

> "Tell me the industry you're thinking about. Not why, not your concerns about it — just the industry."

After client answers:

> "Good. Now tell me every reason you DON'T want to work in that industry. Don't filter it. I want the real objections."

**What Cole is listening for**: The bias tells him where the money is. The objections are a map.

After bias is stated:

> "Okay. So the majority of people in [industry] are [the bias]. Who in that industry is NOT that? Who broke the pattern?"

---

## Round 2: The Category Drill

Cole narrows:

> "So within [industry], you've described [pattern breakers]. What's the specific TYPE of person who breaks that pattern? Give me a role, a stage, a specific situation."

After client narrows:

> "Good. What problem does that type of person have that they can't currently solve — or that they're solving badly?"

After problem is named:

> "Be more specific. 'They struggle with visibility' is a problem. 'They have 10+ years of expertise and a successful offline practice but zero LinkedIn presence, so juniors with less experience keep getting the speaking gigs' is a problem. Which one is closer to the truth?"

---

## Round 3: The Lived Experience Bridge

Cole pivots:

> "Here's what I want to know. You have [X years] inside [industry]. You were a [specific role]. What did you personally see, fail at, or feel that people OUTSIDE that world would never understand?"

After client answers:

> "That's your moat. Now — does the person you just described in Round 2 feel that same thing? Would they recognize it if you named it?"

If yes: proceed to Round 4.
If no: loop back — the niche is still off.

---

## Round 4: The Named Person Test

Cole closes the drill:

> "I need you to name a real person. Not a persona. Not 'someone like.' A first name and a last name, or a LinkedIn URL. Someone you've met, worked with, or could find right now who IS this person."

If client can name them:

> "Perfect. Tell me three things about them: what they do specifically, what problem they have that you solve, and whether they'd recognize themselves in everything you just described."

If client can't name them:

> "Then we're not done yet. The discomfort you're feeling right now — that's not a problem with the niche. That's the drill working. Let's go back to Round 2. What's one specific thing that makes this person different from everyone else in [category]?"

---

## Output Schema

This is the pre-Round-5 baseline version of the drill — it stops at the Named Person, with no Compounding Signal Analysis. Use this schema when the compounding stress-test isn't needed (e.g., quick positioning check, low-stakes niche decision); use `01-specificity-drill.md`'s schema when durability needs to be proven before commitment.

| Field | Type | Required | Description |
|---|---|---|---|
| `named_person.identifier` | string | Yes | Real name/LinkedIn URL, or a placeholder specific enough to find them (never a demographic label) |
| `named_person.role_stage_context` | string | Yes | What they do, their career stage, their situational context |
| `named_person.specific_problem` | string | Yes | The precise, non-generic problem from Round 2 |
| `named_person.recognition_reason` | string | Yes | Why they'd recognize themselves in the positioning (Round 4 output) |
| `positioning_material.lived_experience_bridge` | string | Yes | What the operator knows that outsiders don't (Round 3) |
| `positioning_material.bias_inversion` | string | Yes | Who broke the pattern, and why (Round 1) |
| `positioning_material.unique_visible_problem` | string | Yes | The problem only the operator can see clearly |

**Fails the schema if**: `named_person.identifier` is a persona/demographic rather than a nameable individual, or any field is filled from Round 1-3 answers without having actually run Round 4's Named Person Test.

**No `compounding_signal_score` field in this baseline version** — that's the delta added in `01-specificity-drill.md`'s Round 5. Do not backfill a compounding score here; route to the full workflow instead if durability stress-testing is needed.

---

## Quality Gate

> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
