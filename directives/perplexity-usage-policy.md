# Perplexity API Usage Policy

> **Monthly Budget Limit: $20**
> This directive applies to ALL agents, workflows, and research tasks.
> **Last Updated: 2026-02-14**

## Purpose

Perplexity provides higher-quality, citation-backed research than basic web search. It is the **PRIMARY and MANDATORY tool for market intelligence, competitive analysis, social listening, and deep research**. However, API costs must be managed with hard guardrails to prevent runaway spending.

> [!IMPORTANT]
> **The Perplexity-First Research Standard means: if a task requires research, Perplexity MUST be invoked. LLM-only generation is NEVER acceptable for research deliverables.**

---

## When to Use Perplexity (MANDATORY)
- Market intelligence research
- Competitor analysis
- Social listening (Reddit, forums, review sites)
- Trend verification and validation
- Deep research tasks (`/research-topic`, `/generate-brief`, `/spy-market`)
- Fact-checking with citations needed
- Any research where accuracy and sources matter
- **Any agent swarm with a research component** (minimum 1 query per research agent)

## When to Use Basic Web Search (FALLBACK)
- Quick factual lookups (dates, simple facts)
- General browsing/exploration
- When Perplexity budget is exhausted (with explicit user notification)
- Non-critical background context

## When LLM-Only Is Acceptable (NO RESEARCH TOOL NEEDED)
- Creative copywriting (hooks, headlines, email drafts)
- Framework application (applying a known methodology)
- Synthesis of already-gathered research data
- Persona embodiment and expert analysis (when data already exists)
- Code generation and technical implementation

---

## Cost Tracking & Budget

| Metric | Value |
|--------|-------|
| **Monthly Budget** | $20.00 |
| **Warning Threshold** | $16.00 (80%) — notify user |
| **Hard Cap** | $20.00 (100%) — block and notify |
| **Est. Queries Available** | ~300-500 (Sonar), ~100-200 (Sonar Pro), ~30-50 (Deep Research) |
| **Reset Date** | 1st of each month |

### Tracking File
Usage is tracked in: `.agent/perplexity-usage.json`

### Model Selection
| Requirement | Model | Est. Cost/Query |
|:---|:---|:---|
| Quick fact-check | Sonar | ~$0.01-0.02 |
| Trend analysis, social listening | Sonar Pro | ~$0.03-0.05 |
| Strategic feasibility | Sonar Reasoning Pro | ~$0.05-0.10 |
| Deep market intel | Sonar Deep Research | ~$0.10-0.30 |

---

## 🎯 Adaptive Research Tiering

> **Principle**: Match research intensity to the stakes. Not every task needs Deep Research. But any task that becomes a FOUNDATION must be grounded in truth.

### Tier Classification (Assess BEFORE research begins)

| Tier | Stakes | Research Tool | Budget | When to Use |
|:---|:---|:---|:---|:---|
| **Tier 1: Foundation** | Decisions, strategy, positioning, avatar research, market entry | Perplexity Deep Research + Sonar Pro | Up to $2/task | When the output becomes the BASIS for downstream work (copy, positioning, pricing, offers) |
| **Tier 2: Validation** | Fact-checking, trend verification, competitive spot-checks | Perplexity Sonar Pro | Up to $0.50/task | When you have a hypothesis and need to confirm/deny it with real data |
| **Tier 3: Context** | Background info, general landscape, quick answers | Perplexity Sonar or `search_web` | Up to $0.10/task | When you need directional context but won't build strategy on it |
| **Tier 4: Synthesis** | Combining already-gathered data, applying frameworks | None needed (LLM is appropriate) | $0 | When the data is already in hand and you're applying expert methodology to it |

### Decision Logic
```
IS THIS TASK CREATING A FOUNDATION? (strategy, positioning, avatar profiles, market entry)
  → YES → Tier 1: Perplexity Deep Research. Go deep. This is where the money should go.
  → NO →

DOES THIS TASK REQUIRE FACTUAL ACCURACY? (pricing, competitor names, market size, trends)
  → YES → Tier 2: Perplexity Sonar Pro. Validate claims.
  → NO →

IS THIS TASK DIRECTIONAL? (background context, general landscape)
  → YES → Tier 3: Sonar or search_web. Quick and cheap.
  → NO → Tier 4: LLM synthesis is fine. No external tool needed.
```

### The "False Foundation" Rule
> If an LLM-generated output will become the input for other agents or downstream deliverables, it MUST be Tier 1 or Tier 2. Building strategy on unverified LLM projections is building on sand.

### Budget-Aware Pivoting
When budget is running low, pivot intelligently — don't just stop:
1. **$20 → $10 remaining**: Continue normal operations, but prefer Sonar Pro over Deep Research
2. **$10 → $5 remaining**: Switch Tier 1 tasks from Deep Research to Sonar Pro
3. **$5 → $2 remaining**: Collapse all queries aggressively (The Collapsing Rule). Use Sonar only.
4. **$2 → $0.50 remaining**: Fall back to `search_web` for all tiers. Notify user.
5. **$0.50 → $0**: STOP all external research. Alert user. Offer to proceed with LLM-only (clearly tagged 🔴 PROJECTED).

---

## 🛡️ Cost Guardrails & Loop Protection

### Pre-Query Checks (MANDATORY before every Perplexity call)
1. **Read** `.agent/perplexity-usage.json` for current spend
2. **Calculate** remaining budget: `$20.00 - current_spend`
3. **If remaining < $2.00**: Switch to Sonar (cheapest model) only
4. **If remaining < $0.50**: BLOCK all Perplexity calls, notify user, fall back to `search_web`

### Loop Detection Guards
To prevent agents caught in research loops from burning budget:

| Guard | Rule | Action |
|:---|:---|:---|
| **Per-Task Cap** | Max 10 queries per task/swarm | Block at 11th query, notify user |
| **Per-Minute Cap** | Max 3 queries per 60 seconds | Pause and warn |
| **Duplicate Detection** | Same query within same task | Skip, reuse cached result |
| **Diminishing Returns** | 3 consecutive queries returning <10% new info | Stop and synthesize what you have |

### Swarm-Specific Rules
When running agent swarms:
- **Total swarm budget**: Max 10 Perplexity queries per swarm deployment
- **Per-agent allocation**: Each research agent gets 2-3 queries max
- **Orchestrator controls**: Central orchestrator tracks cumulative count
- **Batch queries**: Combine related research into single prompts (The Collapsing Rule)

---

## Query Optimization (The Collapsing Rule)

**Bad** — 4 separate queries:
```
Query 1: "executive health coaching market size 2026"
Query 2: "executive health coaching pricing"
Query 3: "executive health coaching competitors"
Query 4: "executive health coaching trends"
```

**Good** — 1 collapsed query:
```
"Analyze the executive health and wellness coaching market in 2026: market size, pricing tiers, 
major competitors with their positioning, and emerging trends. Include citations."
```

This saves 75% of query costs while getting better results (Perplexity handles multi-part queries well).

---

## Logging Protocol

Every Perplexity query MUST be logged to `.agent/perplexity-usage.json`:
```json
{
    "timestamp": "2026-02-14T18:10:00-08:00",
    "type": "research|social_listening|competitive_intel|trend_verification",
    "model": "sonar|sonar_pro|sonar_reasoning_pro|sonar_deep_research",
    "description": "Brief description of what was queried",
    "task_context": "Name of the task/swarm this query belongs to",
    "estimated_cost": 0.05,
    "new_info_score": "high|medium|low"
}
```

---

## Override

User can adjust the monthly limit by:
- Updating this file directly
- Verbally authorizing a temporary increase (agent must log the override)
- Setting a per-project budget in the task plan

---

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-04-11 |

**Update Rule**: When this protocol fires (Perplexity query executed), update the date and increment count.

*Effective: 2026-02-05 | Updated: 2026-03-09 — Budget increased to $20/month per user request. Added loop protection, provenance tagging, and swarm governance*
