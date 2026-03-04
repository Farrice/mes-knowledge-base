---
description: Deploy 3 research agents with a synthesis lead that can send follow-up questions — business intelligence with Agent Teams coordination
---

# /research-sprint — Business Intelligence Sprint

Deploy 3 research agents in parallel to investigate different angles of a business question, coordinated by a synthesis lead that can request follow-ups. Uses Agent Teams (Tier 2) for bidirectional communication.

## Usage

```
/research-sprint [business question]
/research-sprint "Should I launch a paid community for AI operators?"
/research-sprint --angles "pricing models, competitor communities, audience willingness" "Paid community for AI operators"
```

## When to Use

- Evaluating a business opportunity before committing
- Pricing a new offer and need market data
- Validating product-market fit with real signals
- Understanding a new audience segment

---

## Steps

### 1. Classify the Question and Determine Angles

Auto-detect the question type by keyword matching, then set default research angles:

| Question Type | Signal Words | Default Angles |
|--------------|-------------|----------------|
| Market Entry | "enter," "launch into," "new market," "opportunity" | Market Size & Timing, Competitive Moat Analysis, Early Adopter Signals |
| Pricing | "price," "charge," "monetize," "revenue model" | Willingness-to-Pay Research, Competitive Pricing Landscape, Value Metric Analysis |
| Product-Market Fit | "PMF," "validate," "demand," "need" | Demand Signal Mapping, Existing Solution Gaps, Buyer Intent Patterns |
| Audience Research | "who," "avatar," "audience," "customer" | Psychographic Profiling, Watering Hole Mapping, Language & Pain Mining |
| General Strategy | (fallback) | Market Validation, Competitive Landscape, Audience Signals |

If the user specified `--angles`, use those instead of defaults.

Present the plan:

```markdown
## Research Sprint Deployment

**Question**: [business question]
**Detected type**: [question type]

| Agent | Angle | Key Questions | Tool Budget |
|-------|-------|---------------|-------------|
| Researcher A | [Angle 1] | 1. [q1] 2. [q2] 3. [q3] | 5 web searches |
| Researcher B | [Angle 2] | 1. [q1] 2. [q2] 3. [q3] | 5 web searches |
| Researcher C | [Angle 3] | 1. [q1] 2. [q2] 3. [q3] | 5 web searches |

**Synthesis lead**: Will review findings and may send 1-2 follow-up questions to any researcher.

Launch? Or adjust angles/questions?
```

Wait for user approval.

### 2. Create the Agent Team

Use `TeamCreate` with `team_name: "research-sprint"`.

Spawn **all 4 agents in a single message** — 3 researchers + 1 synthesizer:

#### Researcher Prompt Template

Each researcher gets this structure:

```
You are a research specialist on team "research-sprint". Your name is "researcher-[a/b/c]".

**Business question**: [question]
**Your assigned angle**: [angle name]
**Key questions to answer**:
1. [question 1]
2. [question 2]
3. [question 3]

**Instructions**:
1. Use WebSearch to find current data (2025-2026 sources preferred)
2. For each finding, record: the data point, the source URL, and one actionable implication
3. Write your findings to: .tmp/research-sprint/[angle-slug].md
4. After writing, send a message to "synthesizer" with a 3-sentence summary of your top findings

**Output format**:
## [Angle Name] — Research Findings

### Key Data Points
- [Finding 1] — Source: [URL] — Implication: [action]
- [Finding 2] — Source: [URL] — Implication: [action]
[...]

### Summary (3 sentences max)
[Synthesized takeaway]

### Data Quality
- Sources found: [count]
- Recency: [most recent source date]
- Confidence: [High/Medium/Low]

**IMPORTANT**: If you receive a follow-up question from the synthesizer, investigate it using additional WebSearch calls, update your findings file, and reply with the answer.
```

#### Synthesizer Prompt

```
You are the Synthesis Lead on team "research-sprint". Your name is "synthesizer".

**Business question**: [question]

**Your role**: Wait for all 3 researchers to send you their summaries. Then:

1. Read all 3 research files from .tmp/research-sprint/
2. Identify:
   - Cross-cutting patterns (themes appearing across 2+ angles)
   - Contradictions (findings that conflict between researchers)
   - Gaps (important questions that remain unanswered)
3. If you find contradictions or critical gaps, send a SPECIFIC follow-up question to the relevant researcher. Example: "researcher-a, your market size of $2B conflicts with researcher-b's $800M. Can you find a third source to triangulate?"
4. Max 2 follow-up rounds. After follow-ups resolve (or if none needed), produce the synthesis brief.

Write the brief to: .tmp/research-sprint/synthesis-brief.md

**Brief format**:

# Research Sprint Brief: [Question]

**Date**: [date]
**Question type**: [detected type]
**Angles covered**: [3 angles]

## Executive Summary
[3-5 sentences that directly answer the business question]

## Key Findings

### [Angle 1]
[Top 3-5 findings with sources]

### [Angle 2]
[Top 3-5 findings with sources]

### [Angle 3]
[Top 3-5 findings with sources]

## Cross-Cutting Insights
[Patterns that emerged across multiple angles]

## Contradictions & Caveats
[Any findings that conflicted + how they were resolved]

## Recommended Actions
| # | Action | Based On | Effort | Impact | Confidence |
|---|--------|----------|--------|--------|-----------|
| 1 | [action] | [which finding] | [L/M/H] | [L/M/H] | [High/Med/Low] |

## Sources
[All URLs cited, organized by angle]

After writing the brief, send a message to the team lead: "Synthesis complete. Brief is at .tmp/research-sprint/synthesis-brief.md" with a 3-line executive summary.
```

### 3. Monitor the Sprint

The orchestrator waits for the synthesizer's completion message. During this time:

- 3 researchers work in parallel (Tier 1 within the team)
- Each sends a summary to the synthesizer when done
- Synthesizer may send 1-2 follow-up questions to specific researchers
- Max 2 follow-up rounds (prevents spiraling)

This bidirectional communication is the Tier 2 advantage over `/parallel-research`.

### 4. Deliver the Brief

After the synthesizer signals completion:

1. Read `.tmp/research-sprint/synthesis-brief.md`
2. Present the full brief to the user
3. Suggest next steps:
   - `/brief` for a full McKinsey-grade strategy document using these findings
   - `/roundtable` to debate the recommended actions with expert agents
   - `/launch-day` if the research validates a content push
   - Direct expert consultation for deep-dive on any specific finding

### 5. Shutdown Team

Use `SendMessage` with `type: "shutdown_request"` to each teammate.

---

## Parallelism Details

| Stage | Tier | Why |
|-------|------|-----|
| 3 researchers | Tier 1 (parallel) within Tier 2 team | Initial research is independent per angle |
| Follow-up questions | Tier 2 (Agent Teams) | Synthesizer messages specific researchers |
| Synthesis | Sequential (single agent) | Must read all findings first |

## Error Handling

- **1 researcher fails**: Synthesizer produces brief from 2 angles. Notes: "Angle [X] research failed — findings based on 2 of 3 angles."
- **Synthesizer fails**: Orchestrator reads the 3 raw research files and does simpler synthesis (fallback to `/parallel-research` behavior).
- **Follow-up loop exceeds 2 rounds**: Synthesizer proceeds with available data, notes unresolved contradictions.
- **All researchers return low-confidence results**: Synthesizer flags this in the brief. Recommends Perplexity Deep Research for higher-quality sources.

## Output Files

```
.tmp/research-sprint/
  angle-1-[slug].md
  angle-2-[slug].md
  angle-3-[slug].md
  synthesis-brief.md
```
