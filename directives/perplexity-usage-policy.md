# Perplexity API Usage Policy

> **Monthly Budget: $30** | Tracked in `.agent/perplexity-usage.json` | Reset: 1st of month
> Applies to ALL agents, workflows, and research tasks.

---

## When to Use

| Tool | Use When |
|------|----------|
| **Perplexity** (MANDATORY) | Market intel, competitor analysis, social listening, trend verification, deep research, fact-checking with citations, any research-as-foundation task |
| **Basic web search** (fallback) | Quick facts, general browsing, budget exhausted (notify user) |
| **LLM-only** (no tool) | Creative copy, framework application, synthesis of gathered data, persona embodiment, code gen |

> **False Foundation Rule**: If LLM-generated output becomes input for downstream agents/deliverables, it MUST use Tier 1 or Tier 2 research. No building strategy on unverified projections.

---

## Research Tiering

| Tier | Stakes | Tool | Budget |
|------|--------|------|--------|
| **1: Foundation** | Strategy, positioning, avatar, market entry | `sonar-deep-research` (2-3 queries) | ≤$2/task |
| **2: Validation** | Fact-check, trend verify, competitive spot-check | Sonar Pro | ≤$0.50/task |
| **3: Context** | Background, landscape, quick answers | Sonar or `search_web` | ≤$0.10/task |
| **4: Synthesis** | Combining gathered data, applying frameworks | None | $0 |

## Model Selection

| Model | Cost/Query | Use |
|-------|-----------|-----|
| Sonar | ~$0.01-0.02 | Quick fact-check |
| Sonar Pro | ~$0.03-0.05 | Trend analysis, social listening |
| Sonar Reasoning Pro | ~$0.05-0.10 | Strategic feasibility |
| Sonar Deep Research | ~$0.10-0.30 | Deep market intel |

---

## Budget-Aware Pivoting

| Remaining | Action |
|-----------|--------|
| $30→$15 | Normal ops, prefer Sonar Pro over Deep Research for non-foundation |
| $15→$7 | Tier 1 uses Sonar Pro. Reserve Deep Research for `/deep-research` only |
| $7→$3 | Collapse queries aggressively. Sonar only. `/deep-research` → `/research-sprint` |
| $3→$0.50 | Fall back to `search_web`. Notify user |
| <$0.50 | STOP all external research. Alert user. LLM-only tagged PROJECTED |

---

## Guardrails

**Pre-query (MANDATORY)**: Read `.agent/perplexity-usage.json`, calculate remaining, enforce caps.

| Guard | Rule |
|-------|------|
| Per-task cap | Max 10 queries/task |
| Per-minute cap | Max 3 queries/60s |
| Duplicate detection | Same query same task → skip, reuse cached |
| Diminishing returns | 3 consecutive queries <10% new info → stop, synthesize |
| Swarm budget | Max 10 queries/swarm, 2-3/agent |

## Query Optimization (Collapsing Rule)

Collapse related queries into single multi-part prompts. 4 separate queries → 1 collapsed query = 75% savings.

## Logging

Every query → `.agent/perplexity-usage.json`: timestamp, type, model, description, task_context, estimated_cost, new_info_score.

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |

*Created: 2026-02-05 | Compressed: 2026-04-13*
