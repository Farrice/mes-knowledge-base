---
name: "SWOT Synthesis"
source_prompt: "skills/business-intelligence-audit/references/prompts/08-swot-synthesis.md"
skill: business-intelligence-audit
standard: structure-pure-v2
refactored: 2026-07-11
---

# Prompt 08: SWOT Synthesis

> Aggregate all findings into strategic framework.

---

## Purpose

Synthesize all audit data into a classic SWOT analysis—but with depth and evidence backing each point.

---

## Input Required

- All previous prompt outputs (01-07)
- Or: Fresh extraction with synthesis

---

## Execution Protocol

```
You are synthesizing audit findings into a strategic SWOT analysis.

Based on all data collected for [COMPANY], create an evidence-based SWOT.

## Instructions

1. Review all previous analyses
2. Identify clear themes for each quadrant
3. Back each point with specific evidence
4. Prioritize by impact

Every SWOT point must pass:
1. Is this specific to THIS company? (not generic)
2. Is there evidence? (not assumption)
3. Does it lead to action? (not just observation)
```

---

## Output Contract

- **Four quadrants populated:** Strengths, Weaknesses, Opportunities, Threats — each with at least 3 evidence-backed rows
- **Top 3 per quadrant:** each paired with a leverage/address/capture/mitigate action
- **TOWS Matrix:** all four cross-strategy cells (SO, WO, ST, WT) populated
- **Key Strategic Implications:** one Offensive Move, one Defensive Move, one Quick Win — each traceable to a specific quadrant entry

---

## Output Skeleton

```
### Strengths (Internal, Helpful)

| Strength | Evidence | Strategic Value |
|----------|----------|-------------------|
| [strength] | [evidence from prior prompts] | [value] |

Top 3 Strengths to Leverage:
1. [Strength] → [how to leverage]
2. [Strength] → [how to leverage]
3. [Strength] → [how to leverage]

### Weaknesses (Internal, Harmful)

| Weakness | Evidence | Risk Level |
|----------|----------|-------------|
| [weakness] | [evidence] | [level] |

Top 3 Weaknesses to Address:
1. [Weakness] → [how to address]
2. [Weakness] → [how to address]
3. [Weakness] → [how to address]

### Opportunities (External, Helpful)

| Opportunity | Market Signal | Potential Upside |
|-------------|-----------------|---------------------|
| [opportunity] | [signal] | [upside] |

Top 3 Opportunities to Pursue:
1. [Opportunity] → [how to capture]
2. [Opportunity] → [how to capture]
3. [Opportunity] → [how to capture]

### Threats (External, Harmful)

| Threat | Source | Probability |
|--------|--------|--------------|
| [threat] | [source] | [level] |

Top 3 Threats to Monitor/Mitigate:
1. [Threat] → [mitigation strategy]
2. [Threat] → [mitigation strategy]
3. [Threat] → [mitigation strategy]

### TOWS Matrix (Strategy Implications)

| | Strengths | Weaknesses |
|---|-----------|------------|
| Opportunities | [SO strategy] | [WO strategy] |
| Threats | [ST strategy] | [WT strategy] |

### Key Strategic Implications

1. Offensive Move: [highest-impact SO strategy]
2. Defensive Move: [highest-impact WT mitigation]
3. Quick Win: [easiest high-value action]
```

---

## Quality Gate

- [ ] Every SWOT row cites evidence from a prior audit prompt, not a fresh assumption
- [ ] Every entry is specific to this company — reads it aloud and it could not apply to any competitor unchanged
- [ ] All four TOWS cells are populated, none left blank
- [ ] The three Key Strategic Implications each trace to a specific quadrant entry above
- [ ] No quadrant has fewer than 3 rows
