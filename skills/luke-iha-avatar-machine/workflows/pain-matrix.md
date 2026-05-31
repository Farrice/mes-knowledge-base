---
description: Plot a market across the 10 Pain Matrix dimensions (1-10) plus the mirrored Benefit Matrix, with a marketing consequence per score
tier: 1
stacks_with: luke-iha-vicious-hooks, luke-iha-copy-blocks
---

# Pain & Benefit Matrix Plotter

The diagnostic core. Decomposes a market's pain into 10 orthogonal dimensions, scores each 1–10, and — critically — reads the **marketing consequence** off each score. Then mirrors it as a Benefit Matrix to define the transformation.

## Pre-Flight Gate
- Market named? If only a product, infer the market.
- Remember the rule (genius.md): **the score is the input, the consequence is the output.** A matrix of numbers with no consequences is an auto-fail.
- Don't collapse dimensions into each other — they're orthogonal. A market can be high-stigma AND high-visibility.

## PHASE 0 — GROUND (auto-fires; skip with `--no-ground`)
Per `references/research-spine.md`. The 10 scores must read off REAL market signal — never contextual guessing.
- If the cold-start dossier exists (`.tmp/copy-engine/deep-research.md` + `voc-pack.md`), load it; each score must trace to its evidence.
- Standalone & not `--no-ground` — route through the ONE grounding chokepoint (reuses a fresh per-market dossier at **$0**; cold-starts paid only on a cache miss, so this never re-fires research for an already-grounded market):
```bash
// turbo
python3 execution/avatar_manifold_runner.py ground --slug <slug> --market "<market>" --tier deep 2>/dev/null \
  || echo "DEGRADE → mcp__recall__search (focused); score with [MODELED] flags where unfilled"
```
- Each of the 10 scores names the dossier evidence justifying it; if a dimension is ungrounded, tag the score `[MODELED]`.

## Skill Acquisition
Load `references/framework-library.md` § A (the 10 dimensions, low/high plays). Load genius.md Pattern 1 + 8.

## Execution
1. **Score all 10** pain dimensions 1–10:
   1) Source (Physiological→Psychological) 2) Causal Clarity 3) Visibility 4) Urgency 5) Social Stigma 6) Measurability 7) Frequency 8) Locus of Control (Internal→External) 9) Emotional Intensity 10) First Person (Self→Other).
2. For **each**, write a **Specific Consequence** — the concrete marketing implication of that score (pull the low/high play from § A, made specific to this market).
3. Output as a table: `Dimension | Rating | Specific Consequence`.
4. **Summary** — name the 2–3 highest-leverage dimensions (usually the extremes) and the headline strategy they dictate.
5. **Benefit Matrix** — re-plot the same 10 axes for the *solved* state; note the biggest Pain→Benefit gaps (those gaps are what you sell).
6. Flag any dimension that implies an **Ejection Trigger** (e.g. high psychological + pain market → don't say "it's in your head").

## Content Type Adaptations
| Market type | Watch |
|---|---|
| Health/physical | Source, Causal Clarity, Measurability drive mechanism choices |
| Relationship/dating | Stigma, Emotional Intensity, Locus of Control dominate |
| MMO/biz-opp | Measurability + Locus of Control + Urgency |
| Pet/parent (Other) | First Person flips the entire appeal to reciprocity |

## Output Requirements
- 10-row table, every row with a real consequence (no blanks, no "N/A").
- Summary naming the leverage dimensions.
- Benefit Matrix + gap callouts.

## Quality Gate
Rubric criterion 1 (Dimensionality) must hit 9: all 10 scored with distinct consequences. Auto-fail: scores without consequences; fewer than 10 dimensions; consequences that just restate the score.
