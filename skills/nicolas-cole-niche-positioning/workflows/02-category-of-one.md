---
workflow: 02-category-of-one
skill: nicolas-cole-niche-positioning
deliverable: 1 Category of One positioning statement + 3 variants
prerequisite: 01-specificity-drill.md output
---

# Category of One


> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.

## Purpose

Take the Named Person and raw material from the Specificity Drill and crystallize it into a positioning statement that creates a category only you occupy. The test: could any competitor say this exact sentence? If yes, the mechanism (Z) is wrong.

## The Formula

> "I help [X — the Named Person] achieve [Y — the specific transformation] through [Z — the mechanism only you have]."

X = specific enough that the Named Person would say "that's me"
Y = the outcome they actually want, not what they think they should want
Z = the mechanism that comes from YOUR lived experience, not a category description

---

## Round 1: Lock X

Cole reviews the Named Person from the drill:

> "We have [Named Person]. Now let's make sure X is specific enough. If I read 'I help health coaches' — that's 400,000 people. If I read 'I help health coaches with 10+ years of offline expertise who have zero LinkedIn presence' — that's maybe 40,000. Which version makes [Named Person] say 'that's literally me'?"

Iterate until X produces recognition, not just relevance.

---

## Round 2: Lock Y

Cole digs into the real outcome:

> "What does [Named Person] actually want? Not what they say in polite company — what do they want at 11pm when they're frustrated? 'More visibility' is what they say. 'The speaking gig that went to someone half as qualified' is what they want. Which version?"

Test Y against: would [Named Person] pay for this? Would they forward this to a colleague?

---

## Round 3: Lock Z — The Mechanism

Cole surfaces the unfair advantage:

> "Now the hard part. Why YOU? Not your credentials. Not your years of experience as a bullet point. The SPECIFIC thing you know, felt, or failed at that makes you the only person who can help [Named Person] get [Y]?"

After client answers:

> "Good. Now put that in Z. Not 'LinkedIn ghostwriting.' Not 'content strategy.' The specific mechanism that comes from your lived experience. If I can replace your name with someone else's and it still sounds true — we haven't found Z yet."

---

## Round 4: The Competitor Test

Cole runs the test:

> "Read me your positioning statement. Now — could any of your top 3 competitors say this exact sentence and have it be true? If yes, Z is wrong. Let's find the part that's uniquely yours."

Repeat until no competitor can say it.

---

## Round 5: Three Variants

Cole generates 3 variants from the same core, each leaning into a different unfair advantage angle:

**Variant A — Lived Experience angle**: Lead with the insider knowledge / what you personally know
**Variant B — Transformation angle**: Lead with the specific outcome (what [Named Person] gets to become)
**Variant C — Contrast angle**: Lead with what makes [Named Person's] situation unique vs. others who tried and failed

---

## Output Schema

This workflow consumes `named_person` and `positioning_material` from `01-specificity-drill.md`'s Output Schema. Its own deliverable is a locked statement plus angle variants — not raw drill material.

| Field | Type | Required | Description |
|---|---|---|---|
| `positioning_statement.x` | string | Yes | The Named-Person-specific audience clause, locked in Round 1 (must pass "that's literally me") |
| `positioning_statement.y` | string | Yes | The real 11pm-frustration outcome from Round 2, not the polite-company version |
| `positioning_statement.z` | string | Yes | The lived-experience mechanism from Round 3 — fails if it's a swappable category label ("content strategy") rather than personal |
| `positioning_statement.full_sentence` | string | Yes | The assembled "I help X achieve Y through Z" statement |
| `variants.A_lived_experience` | string | Yes | Variant leading with insider knowledge |
| `variants.B_transformation` | string | Yes | Variant leading with the outcome |
| `variants.C_contrast` | string | Yes | Variant leading with contrast vs. failed alternatives |
| `competitor_test_result.pass` | boolean | Yes | Whether the Round 4 competitor test was passed (no top-3 competitor could truthfully say the sentence) |
| `competitor_test_result.reasoning` | string | Yes | Which competitors cannot say it, and specifically why (the Z-clause is what disqualifies them) |
| `named_person_confirmation` | boolean + string | Yes | Would [Named Person] recognize themselves — plus a one-line justification tied back to X/Y/Z |

**Fails the schema if**: `competitor_test_result.pass` is true but `reasoning` doesn't name the specific disqualifying element of Z, or any variant in Round 5 is a copy-paste of `positioning_statement.full_sentence` with no angle shift.

---

## Quality Gate

> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
