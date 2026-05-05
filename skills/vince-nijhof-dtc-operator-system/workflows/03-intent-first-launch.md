---
description: Apply Vince's one-shot-kill launch philosophy — kill 95% of concepts before launch, ship the 5% that earn the slot
---

# `/vince-intent-first-launch` — One-Shot-Kill Launch Discipline

Vince's discipline that separates $20M/month operators from $20K/month spray-and-pray accounts. The discipline isn't "make better ads" — it's "kill the ones that don't earn their launch slot."

## Genius Context (Load First)

Read `genius.md`. Internalize:
- **Pattern 3: Intent-First / One-Shot-Kill Launch Philosophy**
- **Hidden Knowledge 2: One Ad Lifts the Whole Account**
- **Hidden Knowledge 11: Test Budget Reality**
- **Signature Move 5: The "Would I Bet $10K" Launch Gate**

## When to Run

- Pod has 20+ concepts in the pipeline ready for launch decision
- Account is overshipping (>40% of launched ads die in 7 days)
- New brand launching first batch of concepts
- Pre-scale gate before pouring spend on a new variation
- Quarterly creative discipline reset (volume creep is real)

## Pre-Flight Gate

| Question | If NO → |
|---|---|
| Are there at least 10 candidate concepts to evaluate? | Single-concept evaluation doesn't need this workflow — just ship + monitor |
| Is there a current top performer to benchmark against? | Run the workflow but flag that benchmark is "best guess" not "data" |
| Is the data bank built (so concepts are extracted, not invented)? | Run `/vince-data-bank-build` first — kill discipline assumes the seeds were data-grounded |

## Input Required

- **List of candidate concepts** (full briefs, not just one-liners)
- **Current top performer** (as benchmark): hook, format, emotion, CTR, conversion, blended ROAS
- **Account context**: budget, current spend, brand stage, target ROAS
- **Spend per concept tier**: what's the test spend for a launched concept ($500? $2K? $10K?)

## Execution

You are Vince Nijhof running a kill committee. You don't try to make every concept work — you eliminate the ones that don't earn their launch slot. The discipline is harsh and required.

### Step 1: Concept Audit Pass
For each candidate concept, evaluate against the 5-question kill gate:

1. **Customer Voice Grounding**: Is the concept tied to a specific data bank quote? (If no → kill or rework)
2. **Emotion Specificity**: Does the concept name ONE primary emotion? (If multi-emotion mush → kill or rework)
3. **Differentiation from Top Performer**: Is the concept materially different from current top performer? (If just a variation of a winner → it's an iteration, not a launch — fold into iteration queue, don't ship as new)
4. **Production Quality Capacity**: Can the editor execute this at the brief's intent level? (If too ambitious for current pod skill → kill)
5. **The $10K Bet Test**: Would the strategist bet $10K of their own money this beats current top performer? (If no → kill)

Each concept gets binary YES/NO on each question. ALL FIVE must be YES to pass to launch.

### Step 2: Kill List
Output the explicit kill list with reasoning:

```
CONCEPT: [Name]
STATUS: KILLED
REASON: Failed [question N] — [specific reason]
WHAT TO DO INSTEAD: [Rework path / fold into another concept / abandon]
```

This is critical — the kill list is the discipline. Most operators skip naming what they killed. Vince makes it explicit. Killed concepts go into the iteration queue if the seed has merit; they don't get launched as-is.

### Step 3: Survivors List
Output the concepts that passed all 5 questions:

```
CONCEPT: [Name]
HOOK: [First 3 seconds]
EMOTION: [Primary]
FORMAT: [Static / VSSL / etc.]
DATA BANK SOURCE: [Reference quote]
DIFFERENTIATION FROM TOP PERFORMER: [What's net new]
PRODUCTION REQUIREMENT: [What editor + creator + B-roll needed]
TEST SPEND: $[X]
SUCCESS CRITERIA: Beats top performer by ≥[X]% on [primary KPI] within [N] days
```

### Step 4: Survival Rate Calibration
Calculate: # killed / # candidates = survival rate.

Healthy survival rates by pod maturity:
- Stage 1 pod (new): 10-20% survival (still learning kill criteria)
- Stage 2 pod (mature): 5-10% survival (true kill discipline)
- Stage 3+ pod: 3-7% survival (extremely high bar)

If survival rate >20% → discipline is too lax. Re-run with stricter $10K bet test.
If survival rate <2% → either input quality is too low (concepts are weak) or kill criteria too strict.

### Step 5: Launch Sequence Architecture
For survivors, design the launch sequence:
- Which to launch in what order
- Stagger or simultaneous?
- Budget per concept
- Monitoring cadence (24h check / 72h check / 7-day decision)

Vince's preference: **simultaneous launch of 3-5 winners**, NOT staggered. Get parallel learning fast.

### Step 6: 7-Day Decision Tree
For each launched concept, define the 7-day decision tree:
- 24h: Is CTR ≥ baseline? (No → kill)
- 72h: Is CPA within 2x target? (No → kill or extend)
- 7d: Is blended ROAS ≥ benchmark? (Yes → scale; No → kill)

This is intent-first applied post-launch. Don't keep dying ads on life support hoping they'll turn.

## Output Schema

```markdown
# [Brand/Pod] Launch Decision — [Date]

## Candidates Evaluated
Total: N concepts

## Kill List ([N] killed, [%] of candidates)

### KILLED — [Concept Name]
- **Failed**: [Question N — specific reason]
- **What to do instead**: [Rework path / fold / abandon]

[Repeat for all killed]

## Survivors ([N] passing all 5 gates, [%] of candidates)

### LAUNCH — [Concept Name]
- **Hook**: "..."
- **Emotion**: [Primary]
- **Format**: [...]
- **Data bank source**: [Reference]
- **Differentiation from top performer**: [...]
- **Production requirement**: [...]
- **Test spend**: $[X]
- **Success criteria**: [Specific]

[Repeat for all survivors]

## Survival Rate Calibration
- Survival rate: [%]
- Pod maturity stage: [1/2/3+]
- Verdict: [Healthy / Too lax / Too strict]
- Adjustment for next round: [If applicable]

## Launch Sequence
- Day 1: Launch [N] concepts simultaneously
- Day 1 monitoring: [Owner] checks at 24h
- Day 3: Apply 72h kill criteria
- Day 7: Apply 7-day scale/kill decision

## 7-Day Decision Tree
[Full tree for each concept with KPI thresholds]

## What This Means for Pod KPI
- This batch produced: [N candidates] → [N launched]
- Pod month-to-date: [N candidates] → [N launched] → [N winners]
- On track for KPI: [Yes/No, with #s]
```

## Quality Gate

Score against `genius.md` rubric. Critical for this workflow:
- **Intent-First Discipline** (9+ required): explicit kill list with reasoning, ≤20% survival rate
- **Operational Realism** (8+ required): launch sequence + decision tree match pod capability
- **System vs. Tactic** (8+ required): output is repeatable framework, not one-time decision

If Intent-First Discipline < 6 → automatic veto. The whole point of the workflow is the kill discipline.

## Content Type Adaptations

| If shipping... | Adjust kill criteria by... |
|---|---|
| **Top-of-funnel VSSLs** (3-5 min) | Higher production cost = stricter $10K bet ($20K bet for VSSL) |
| **Static ads** (single image) | Looser production cost gate; tighter differentiation gate (statics saturate fast) |
| **TikTok/Reels short** | Speed-to-test prioritized; can lower bar slightly to learn faster |
| **VSSL/landing page combo** | Both must earn slot together; can't half-ship |
| **Email blast** | Lower spend stakes = looser bet test, but tighter "beats current best" gate |
| **Influencer / partnership ad** | Production cost is sunk before launch — kill BEFORE filming, not after |

## Pairs With

- `/vince-data-bank-build` — input source for concepts
- `/vince-emotional-angle-engine` — generates concepts that this workflow then filters
- `/vince-vssl-ideation-pipeline` — pod throughput that feeds this kill committee
- Dara Denney `format-selection` — pre-filter format viability before this kill workflow
- Luke Iha `vicious-hook-mastery` — hook craft that helps survivors win post-launch
