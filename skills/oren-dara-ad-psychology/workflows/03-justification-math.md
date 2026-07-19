---
description: Build the justification layer for a purchase — cost-per-use math, heirloom/investment framing, girl-math variants, plus the inverse "we're not cheap" status filter. The buyer already wants it; hand them the excuse.
---

# `/adpsy-justification-math` — Selfish Desires & Justification Math

> Oren on Patek Philippe: "all that does is check a box in a certain type of guy's or girl's mind that says, yeah, cool, I can justify this purchase."

Price is "always the number one objection" (Dara). This workflow doesn't argue value — it licenses a desire that already exists. And it runs **both ends**: justification for the objectors, a status filter for the aspirationals ("We're not cheap because we don't want to be").

## Pre-Flight Gate

- Is desire already present (product-aware or solution-aware buyer stalling on price)? If the buyer doesn't want it yet, this is the wrong tactic — route `/adpsy-tactic-select`.
- Luxury insider positioning beyond ad copy → stack `oren-luxury-psychology` after this, don't merge into it.

## Skill Acquisition

Read `genius.md` (Tactic 2, Both-Ends Price Play) + `references/source-quotes.md` Tactic 2 block. Anchors: Patek "carry it on for the next generation" · girl math "$6 a brush" · bed sheets "$1 per week" at $400+ AOV · "We're not cheap because we don't want to be" · masstige inverse "Expensive doesn't always equal better."

## Input Required

- **[PRODUCT + PRICE/AOV]** and expected ownership life / usage frequency
- **[PERSONA]** + who they justify the purchase TO (self, spouse, kids, boss)
- **[POSITION]**: premium, masstige, or value — determines which end(s) of the play
- **[REAL OBJECTION LANGUAGE]** (reviews/comments where price appears)

## Execution

1. **Do the actual math.** Break price to cost-per-use/week/wear over honest ownership life ("$1 per week"). Never fake the denominator — a reader who redoes the math and gets a different answer is a lost customer and a comment-section liability.
2. **Write the justification checkboxes.** 3-5 framings, each naming WHO the buyer answers to: investment-for-child (Patek), durability-vs-replacement, "girl math"/"boy math" playful register, time-saved, use-it-enough ("using them for 60 hours… only 6 cents per").
3. **Write the inverse.** The status filter: "if you can't afford it, that's kind of the point" — an ad that *rejects* the wrong buyer ("we actually don't want to cater to the person who wants to buy $30 polyester sheets"). One headline + one supporting line.
4. **Pick by position.** Premium: both ends. Masstige: justification + "expensive doesn't always equal better." Value: pure math framing.
5. **Balance check.** Dara's warning: "make sure you're not over catering" to the price objection — if every asset justifies, the filter (and the status signal) dies. Specify the mix.
6. **Vessel handoff**: objection ads → `/dara-objection-engine`; static headliners → `/dara-static-copy`.

## Content Type Adaptations

| Context | Adaptation |
|---|---|
| Subscription | Math per delivery/serving; compare to the habit it replaces |
| Gifting season | Justification shifts to the giver's identity ("the person who gives X") |
| Organic repost | Girl-math register works on paid even when it'd flop organic — Oren's note; don't judge the ad by organic taste |
| B2B / services | Who-they-answer-to = boss/CFO; math in time or risk, not dollars-per-week |

## Output Requirements

Justification Suite: honest math block (shown work) · 3-5 justification checkboxes with target-of-justification named · inverse status-filter ad (headline + line) · position-based mix recommendation · vessel handoff.

Execution prompt: `references/prompts-v2/03-justification-suite.md`

## Quality Gate

Rubric: mechanism named ≥7; the math must survive a skeptical redo; at least one framing must be in the persona's playful register (not brand-speak). Automatic fail: fabricated denominators, over-catering (all justification, no filter, for a premium brand), or luxury language that `oren-luxury-psychology` would flag as outsider-tell.
