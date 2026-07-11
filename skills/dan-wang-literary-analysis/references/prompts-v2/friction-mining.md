---
name: "Friction Mining Analysis"
source_prompt: skills/dan-wang-literary-analysis/references/prompts/friction-mining.md
skill: dan-wang-literary-analysis
standard: structure-pure-v2
refactored: 2026-07-11
---

# Friction Mining Analysis

Find insights in the gap between official narratives and ground truth reality.

## Role

You are systematically identifying where official stories diverge from lived experience — the richest source of genuine insight in any domain.

## Required Input

- **DOMAIN**: The organization, industry, country, or movement to analyze
- **OFFICIAL SOURCES**: What press releases, websites, spokespeople, and institutions claim
- **GROUND TRUTH ACCESS**: Observations, interviews, data, or experience from actual operation

## Execution

1. **Official Narrative Mapping**: Document what the formal story claims. What does the website say? The annual report? The mission statement? The interview answers?

2. **Ground Truth Documentation**: What do you actually observe? What do employees/participants/customers actually experience?

3. **Divergence Identification**: Where do official and ground truth conflict? These friction points ARE the insight.

4. **Productive Friction Analysis**: For each divergence, ask: What does this gap reveal about actual priorities, constraints, or dysfunction?

5. **Informal System Detection**: What workarounds exist because the formal system doesn't work? These reveal real operating logic.

6. **Synthesis**: Compile divergences into narrative that explains how things actually work.

## Output Contract

- **Official Narrative Summary**: A concise statement of what the formal sources claim, sourced to specific documents/statements — not paraphrased into a strawman
- **Ground Truth Observations**: The actual observed/experienced reality, with enough specificity that a reader can verify or contest it
- **Key Friction Points**: Minimum 5 named divergences between official and ground truth
- **What This Reveals**: A short analysis per friction point — the priority, constraint, or dysfunction the gap exposes
- **Actual Operating Logic**: A synthesis of how the domain really functions, distinct from the official account
- **Strategic Implications**: What the friction map means for engaging with this domain

## Output Skeleton

```
## Official Narrative Summary
[what the formal sources claim, with source references — press release / site / mission statement / spokesperson]

## Ground Truth Observations
[what is actually observed or experienced, with specificity]

## Key Friction Points (minimum 5)
1. [official claim] vs. [ground truth] — [one-line statement of the gap]
2. [...]
3. [...]
4. [...]
5. [...]

## What This Reveals
[per friction point: the priority/constraint/dysfunction the gap exposes]

## Actual Operating Logic
[synthesis of how the domain really works, including any informal workarounds/unwritten rules]

## Strategic Implications
[what this means for someone deciding how to engage with this domain]
```

## Quality Gate

- Are there at least 5 named friction points, each citing a specific official claim and a specific observed reality?
- Does each friction point's "what this reveals" go beyond restating the gap — does it name the priority, constraint, or dysfunction?
- Is the "actual operating logic" section a genuine synthesis, not a repeat of the friction list?
- Would an insider find at least one observation uncomfortable but accurate — i.e., is this actual friction, not a restatement of the official story?
- Is every ground-truth claim traceable to an observation, interview, or data point rather than assumed?
