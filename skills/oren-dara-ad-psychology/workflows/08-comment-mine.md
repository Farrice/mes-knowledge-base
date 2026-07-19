---
description: Mine a live ad's comment section into a virtue map, vernacular bank, and ranked next-iteration briefs — the loop that turned "honesty" comments into spiking ads within a day.
---

# `/adpsy-comment-mine` — Comment Virtue Mining

> Dara: "the big virtue that we got from this ad specifically from the comments was how obsessed our audience was with honesty… we even had people putting in Bible verses… we launched some of those ads yesterday and they're already starting to spike."

Comments are three assets at once: community payoff, engagement signal, and **next round's research**. The rare move here is mining for **virtues** (honesty, fairness, loyalty, craft) — values the audience reveals under emotion — not just pain points. Virtues beat desires for iteration speed.

## Pre-Flight Gate

- Has the ad been live ≥1 week with a real comment volume? Thin sections give false reads — say so and wait.
- This mines YOUR audience's comments. Competitor-comment mining is a different (weaker) input — flag it if that's all you have.

## Skill Acquisition

Read `genius.md` (Comment-Section-as-Strategy, Virtues > desires) + `references/source-quotes.md` Tactic 3 block.

## Input Required

- **[COMMENT EXPORT]**: the actual comments (paste/CSV) from the live ad(s) — and from the brand's organic if available
- **[THE AD]**: what ran (so reactions can be mapped to beats)
- **[CURRENT ROADMAP]** (optional): what's already planned, to rank iterations against

## Execution

1. **Read everything. Sort into four streams**: emotional eruptions (fury, testimony — the rage-bait payoff), **virtue signals** (what value are they defending? honesty, fairness, craft, family), vernacular (exact phrases in their register — the future hook bank), and objections/corrections.
2. **Build the virtue map.** For each revealed virtue: evidence quotes → intensity (how emotional, how repeated) → which ad beat triggered it. The strongest virtue is usually defended, not stated ("calling out an honest mechanic," Bible verses).
3. **Bank the vernacular.** 10-20 verbatim phrases usable as hooks/headlines — customer's words, zero paraphrase (feeds `/dara-winning-hooks` and `/dara-static-copy` mechanic #7).
4. **Write ranked iteration briefs.** For the top 1-2 virtues: one-paragraph brief each — concept leaning into the virtue, in the banked vernacular, with the tactic named (often shifts tactic: investigation → credible-honest-explainer). Dara's bar: virtue-led iterations shipped within days.
5. **Log the learning** into the account's research doc — this is the flywheel's return path.

## Content Type Adaptations

| Context | Adaptation |
|---|---|
| Low comment volume | Mine reviews + support tickets as proxy; label confidence |
| Organic-only brand | Same mine on organic comments; feeds first paid round |
| Client reporting | Virtue map is a client-facing deliverable — production-sheet format, ≤2 pages |
| Negative-only comments | Objection stream feeds `/dara-objection-engine` instead |

## Output Requirements

Comment Mine Report: virtue map (virtue → evidence quotes → intensity → trigger beat) · vernacular bank (verbatim) · objection list · 1-2 ranked iteration briefs with ship-by dates. ≤2 pages.

Execution prompt: `references/prompts-v2/08-comment-mine-report.md`

## Quality Gate

Rubric: comment design ≥7 (virtue-mine loop closed with concrete briefs); every virtue claim backed by ≥3 quotes. Automatic fail: paraphrased vernacular, virtues asserted without evidence, or a report with no shippable iteration.
