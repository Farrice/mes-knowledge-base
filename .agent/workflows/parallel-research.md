---
description: Deploy 3 research agents in parallel to investigate different angles of a topic simultaneously
---

# /parallel-research — Parallel Research Team

Deploy 3 independent research agents that investigate different facets of a topic simultaneously, then synthesize their findings into a unified brief.

## Usage

```
/parallel-research [topic or question]
/parallel-research --angles "market size, competitors, buyer psychology" [topic]
```

## When to Use

- Deep research needed across multiple dimensions
- Strategy brief that requires market + competitive + customer data
- Any research task that naturally splits into independent angles

## Steps

### 1. Decompose the Research Question

Split the topic into 3 independent research angles. Default decomposition:

| Angle | Focus | Output |
|-------|-------|--------|
| **Market Intelligence** | Market size, trends, growth, segments | Market landscape with data points |
| **Competitive Analysis** | Key players, positioning, pricing, gaps | Competitive matrix with opportunities |
| **Buyer Psychology** | Pain points, language, objections, buying triggers | Buyer profile with verbatims |

If the user specifies `--angles`, use those instead.

Present the plan:
```
## Research Deployment

**Topic**: [topic]

| Agent | Angle | Key Questions |
|-------|-------|---------------|
| Researcher A | [Angle 1] | [2-3 specific questions] |
| Researcher B | [Angle 2] | [2-3 specific questions] |
| Researcher C | [Angle 3] | [2-3 specific questions] |

Launch? Or adjust angles?
```

Wait for user approval.

### 2. Launch Parallel Research Agents

Spawn 3 Task tool sub-agents **in a single message**:

Each agent prompt:
```
You are a research specialist investigating: [specific angle]

**Topic**: [topic]
**Your angle**: [angle description]
**Key questions to answer**:
1. [question 1]
2. [question 2]
3. [question 3]

**Instructions**:
1. Use WebSearch to find current data (2025-2026 sources preferred)
2. For each finding, record: the data point, the source URL, and one actionable implication
3. Write your findings to: .tmp/research-[angle-slug].md

**Output format**:
## [Angle Name] — Research Findings

### Key Data Points
- [Finding 1] — Source: [URL] — Implication: [action]
- [Finding 2] — Source: [URL] — Implication: [action]
[...]

### Summary (3 sentences max)
[Synthesized takeaway]

### Confidence: [High/Medium/Low]
```

### 3. Synthesize

After all 3 agents return, read their outputs and produce a unified brief:

```markdown
# Research Brief: [Topic]

**Date**: [date]
**Angles Covered**: [3 angles]

## Executive Summary
[3-5 sentences synthesizing across all angles]

## Key Findings

### [Angle 1]
[Top 3-5 findings with sources]

### [Angle 2]
[Top 3-5 findings with sources]

### [Angle 3]
[Top 3-5 findings with sources]

## Cross-Cutting Insights
[Patterns that emerged across multiple angles]

## Recommended Actions
| # | Action | Based On | Effort | Impact |
|---|--------|----------|--------|--------|
| 1 | [action] | [which angle/finding] | [L/M/H] | [L/M/H] |

## Sources
[All URLs cited]
```

Save to `.tmp/research-brief-[topic-slug].md`.

### 4. Deliver

Present the brief to the user. Suggest next steps:
- `/brief` for a full McKinsey-grade strategy brief
- `/swarm` for multi-expert analysis
- Direct expert consultation (route via intent pipeline)

## Limits

- 3 agents max (more angles = shallower research per angle)
- Each agent gets ~5 web searches
- Total research time: 2-5 minutes depending on topic complexity
