---
description: Research + observation-harvesting engine that produces a ranked "That's a Thing" observation bank from a topic, a domain, or your own life.
tier: system
---

# /segura-antenna — The Antenna Engine ⭐

Produces a scored, ranked bank of raw observations (the unarticulated-universals everyone has lived but no one has said) by running the topic through live research — what's already been said vs. the friction nobody's named — then Segura's recognition antenna. Deploys **Pattern 1: The "That's a Thing" Antenna** as the core engine.

## When to Use
- You need premises, hooks, or angles before drafting any piece.
- A topic/domain feels crowded and you need the gap nobody else is hitting.
- Mining "my own life" for unrepeatable material (kids, family, work, daily annoyances).
- Breaking creative block — generate raw charge, not finished jokes.

## When NOT to Use
- The bit/story already exists and needs shaping → route to a development workflow (Long-First, Edit-Second).
- You need joke *mechanics* on material you already have → route to Robert Mack's skill.

## Pre-Flight Gate
Load genius.md. Governed by **Pattern 1 (The Antenna)**, **Pattern 3 (Universal-but-Unarticulated)**, **Pattern 2 (Complaining is the Engine)**, **Pattern 13 (Story Ownership)**, and the **"That's a Thing" Flag** move. Disqualify if the input is a finished draft (route out). Branch on input type: **topic/domain** → run live research (Step 2); **"my own life"** → skip research, harvest user notes/thought-bank instead.

## Skill Acquisition
- Load: skills/tom-segura-comedy-storytelling/genius.md — Patterns **1, 3, 2, 13**; Moves **The "That's a Thing" Flag**, **The Annoyance Dig**.
- Stacking (optional): for the recognition-essay finish, also load `skills/nicolas-cole-sentence-craft/` or `skills/lara-acosta-linkedin-mastery/` per the genius.md Stacking Map.

## Execution
1. **Classify the input.** Tag it `topic/domain` or `my-own-life`. This sets the harvest source for Steps 2-3.
2. **Run live research (topic/domain only).** Map **(a)** what people ALREADY say (saturated takes — dead lanes) and **(b)** the friction and universal experiences NOBODY has articulated. **The gap between (a) and (b) is the gold.** Tools: `mcp__perplexity-ask__perplexity_search`, `WebSearch`, or the **tavily-search** skill. **Gate any paid call via `cost_gate` (budget-gated per CLAUDE.md).** Run free first; escalate to paid only if the gap stays fuzzy.
3. **Harvest raw (my-own-life only).** Pull from `_active/farrice-brand/thought-bank/inbox/`, recent notes, and stated experiences. Per **Pattern 13: Story Ownership** — report, never invent.
4. **Dig the annoyances.** Run **The Annoyance Dig** on each friction point: never state the surface gripe — expand on *why* it's disproportionate until the irrational core surfaces (Hidden 3: the joke is the dig, not the obvious). Generate 15-25 raw observations. Keep the dumb ones (Pattern 5: Just Say Them All).
5. **Flag the antennae.** Per **Pattern 1** + the **"That's a Thing" Flag** — mark every observation with legs: the charged line, the thing noticed "60, 70 times" but never voiced (Pattern 3).
6. **Score the bank.** Rate each observation 1-10 on the four axes below; compute **dev-potential = Universality + Unarticulated-ness + Ownership + Charge**.
7. **Rank and flag the top 3** as **"get it out — someone's going to say this"** (Pattern 3's urgency signal), each with its dig expanded.

**Scoring axes:**

| Axis | Question | High score = |
|---|---|---|
| **Universality** | Has everyone experienced it? | The "of course" charge — instant recognition |
| **Unarticulated-ness** | Has anyone said it out loud? | Research found the saying nowhere (the gap) |
| **Ownership** | Is it uniquely yours? | Only you could tell it (Pattern 13) |
| **Charge** | Annoyance/opinion temperature | Disproportionate feeling, never the neutral take (Pattern 2) |

## Content Type Adaptations
| Content Type | How this shifts |
|---|---|
| Stand-up / spoken | Bank stays raw fragments; weight Charge highest. Save the full dig for the stage. |
| Essay / newsletter (Parallax) | Weight Universality + Unarticulated-ness; top pick becomes the recognition-essay premise. |
| LinkedIn / social | Top 3 become hook candidates; hand off to Lara's hook engine downstream. |
| Sales / DR copy | Map Charge to a felt customer annoyance; the dig becomes problem-agitation. |
| Video / sketch script | Flag observations that survive being played straight (Pattern 8) — the absurd-but-grounded. |

## Output Requirements
- **Format**: A ranked table — Observation (raw) | Universality | Unarticulated | Ownership | Charge | Dev-Potential | Lane. Research-sourced items cite the gap they fill.
- **Must include**: 15-25 scored observations; the (a)-vs-(b) research delta for topic/domain inputs; the dig expanded for the top 3.
- **Ends with**: The top 3 flagged **"get it out — someone's going to say this,"** each with its one-line dig.

## Quality Gate
Score against the genius.md rubric (name the anchor for any score ≥8). Reject if present: **the neutral take** (no temperature, Pattern 2); **stopping at the obvious** (surface complaint, no dig, Hidden 3); **the derivative middle** (saturated takes research already found, Pattern 13); **comprehensive but dead** (everything plainly stated, no charge or ownership). Retry the weakest axis once before delivery.
