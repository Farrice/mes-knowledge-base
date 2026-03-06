# NotebookLM Usage Policy

> **Monthly Query Limit: 100**
> This directive applies to ALL agents, workflows, and research tasks.
> **Last Updated: 2026-03-06**

## Purpose

NotebookLM provides conversational RAG access to domain-specific research notebooks. It supplements the expert skill system by providing examples, recent context, and applied methodology patterns. However, query budgets must be managed to prevent overuse and ensure strategic deployment.

> [!IMPORTANT]
> **NotebookLM is for supplemental context, not primary knowledge.** Skills provide methodology; NotebookLM provides examples and recent research. Never bypass loading the appropriate expert skill in favor of notebook queries alone.

---

## When to Use NotebookLM (STRATEGIC)

- **Expert methodology application**: "What examples does [notebook] show for X pattern?"
- **Recent context supplementation**: Adding 2026 market data to established frameworks
- **Cross-domain research**: Finding intersection patterns across notebooks
- **Expertise gap validation**: Checking if existing research covers a domain before extraction
- **Post-extraction reinforcement**: Querying uploaded extraction reports for quick reference

## When NOT to Use NotebookLM

- **Primary expert knowledge** — Load skills first (Tier 1-2), supplement with notebooks (Tier 1.5) only when needed
- **Code/system questions** — Use files/directives, not notebooks
- **Historical decisions** — Use git log, session state, not notebooks
- **When budget exhausted** — Fall back to skills-only mode

---

## Cost Tracking & Budget

| Metric | Value |
|--------|-------|
| **Monthly Budget** | 100 queries |
| **Warning Threshold** | 80 queries (80%) — notify user |
| **Hard Cap** | 100 queries (100%) — block and notify |
| **Reset Date** | 1st of each month |

### Tracking File
Usage is tracked in: `.agent/notebooklm-usage.json`

### Query Cost Model
Unlike Perplexity (cost per query), NotebookLM uses **query count**:
- Each notebook query = 1 query (regardless of complexity)
- Cache hits = 0 queries (reuses cached response)
- Search all notebooks (3 notebooks) = 3 queries

---

## 🎯 Adaptive Query Tiering

> **Principle**: Match query intensity to information value. Not every task needs notebook context.

### Tier Classification (Assess BEFORE querying)

| Tier | Stakes | NotebookLM Use | Budget | When to Use |
|:---|:---|:---|:---|:---|
| **Tier 1: Foundation** | Strategy, positioning, offer design, methodol

ogy validation | Query all relevant notebooks | Up to 10 queries/task | When you need examples/patterns from research to validate or enrich expert methodology |
| **Tier 2: Validation** | Fact-checking expert claims, trend verification | Query 1-2 notebooks | Up to 3 queries/task | When you need to confirm if research supports an assertion |
| **Tier 3: Context** | Background info, quick reference | Query primary notebook | 1 query max | When you need a specific data point or example |
| **Tier 4: Synthesis** | Applying loaded skills to the task | No notebook needed | 0 queries | Skills provide sufficient methodology without supplemental research |

### Decision Logic
```
DOES THIS TASK CREATE A FOUNDATION DELIVERABLE? (strategy, positioning, offer, sales page)
  → YES → Are relevant notebooks available with recent research?
    → YES → Tier 1: Query notebooks for examples/patterns (up to 10 queries)
    → NO → Tier 4: Skills only
  → NO →

DOES THIS TASK REQUIRE FACT VALIDATION? (expert methodology claims, trend assertions)
  → YES → Tier 2: Query 1-2 notebooks to validate (up to 3 queries)
  → NO →

IS THIS A QUICK REFERENCE LOOKUP? (specific example, data point)
  → YES → Tier 3: Single notebook query (1 query max)
  → NO → Tier 4: Skills provide sufficient context

BUDGET EXHAUSTED?
  → YES → Tier 4: Skills only (notify user of degraded mode)
```

### Budget-Aware Pivoting
When budget is running low, pivot intelligently:
1. **100 → 50 remaining**: Continue normal usage
2. **50 → 20 remaining**: Switch all tasks to Tier 3 (1 query max) or Tier 4 (skills only)
3. **20 → 5 remaining**: Reserve for critical Tier 1 foundation tasks only
4. **5 → 0**: STOP all notebook queries. Skills-only mode. Notify user.

---

## 🛡️ Cost Guardrails & Loop Protection

### Pre-Query Checks (MANDATORY before every NotebookLM call)
1. **Read** `.agent/notebooklm-usage.json` for current query count
2. **Calculate** remaining budget: `100 - queries_used`
3. **If remaining < 20**: Switch to Tier 3/4 only (notify user)
4. **If remaining < 1**: BLOCK all queries, notify user, use skills-only mode

### Loop Detection Guards
To prevent agents caught in query loops from burning budget:

| Guard | Rule | Action |
|:---|:---|:---|
| **Per-Task Cap** | Max 5 queries per task/workflow | Block at 6th query, notify user |
| **Per-Notebook Cap** | Max 2 queries to same notebook per task | Warn at 3rd attempt |
| **Duplicate Detection** | Same query within same task | Skip, reuse cached result |
| **Cache-First** | Always check cache before querying | Bypass budget for cache hits |

### Workflow-Specific Rules
- **Intent Pipeline**: Max 1 notebook query per routing (Step 3c)
- **Expertise Gap Protocol**: Max 3 notebook queries (Phase 1b)
- **Tier 1.5 Loading**: Max 1 notebook query per skill load
- **/query-notebook**: User-invoked, no per-task cap (respects monthly limit)
- **/knowledge-search**: Max 3 notebooks queried per search

---

## Query Optimization (The Collapsing Rule)

**Bad** — 3 separate queries:
```
Query 1: "What are Lara's hook patterns?"
Query 2: "What are Lara's CTA strategies?"
Query 3: "What are Lara's proof methods?"
```

**Good** — 1 collapsed query:
```
"Summarize Lara Acosta's methodology for hooks, CTAs, and proof from the LinkedIn research."
```

This saves 66% of query budget while getting better integrated results.

---

## Caching Strategy

### Cache Duration
- **TTL**: 7 days
- **Storage**: `.agent/knowledge-cache.json`
- **Cache Key**: SHA256 hash of `notebook_id:query` (case-insensitive)

### Cache Behavior
- **Cache Hit**: 0 queries used, instant response
- **Cache Miss**: 1 query used, response cached for 7 days
- **Cache Invalidation**: Automatic after 7 days

### Cache Optimization
- Standardize query phrasing for higher cache hit rate
- Example: "What are the hook patterns?" and "Hook patterns?" hash differently
- Prefer consistent query templates when possible

---

## Logging Protocol

Every NotebookLM query MUST be logged to `.agent/notebooklm-usage.json`:
```json
{
    "timestamp": "2026-03-06T10:30:00-08:00",
    "notebook_id": "b665051a-20f2-419b-b0a8-4b77d3382464",
    "notebook_name": "LinkedIn Ghostwriting Research",
    "query": "What are Lara's top 3 hook patterns?",
    "task_context": "linkedin_content_creation"
}
```

---

## Notebook Registry

All notebooks are registered in: `mcp-servers/notebooklm/notebooks.md`

| Notebook | Purpose | Use When |
|----------|---------|----------|
| **Higgsfield Cinema Studio** | AI video generation prompts | Creating video content, cinematic prompts |
| **AI Brain Build Sprint** | Offer design, audience psychology | Building AI-focused products/offers |
| **LinkedIn Ghostwriting Research** | LinkedIn methodology, market state | Personal brand, LinkedIn content, ghostwriting |

**Adding Notebooks**: Use `/add-notebook` workflow or manually update `notebooks.md`

---

## Integration Points

### Intent Pipeline (Stage 3c)
After routing to expert, check if notebook supplementation needed:
- Expertise gap filled via extraction? → Query domain notebook (1 query)
- Complex multi-expert task? → Query for cross-domain patterns (1 query)
- User explicit request? → Always query

### Agent Loading (Tier 1.5)
After loading SKILL.md + workflow, check for relevant notebook:
- If notebook exists for domain → Query for recent context/examples (1 query, max 500 tokens)
- Inject as supplemental context

### Expertise Gap Protocol (Phase 1b)
Before recommending extraction:
- Search all notebooks for existing domain research (up to 3 queries)
- If found → Offer: use existing / extract fresh / hybrid

---

## Override

User can adjust the monthly limit by:
- Updating this file directly
- Verbally authorizing a temporary increase (agent must log the override)
- Setting a per-project budget in the task plan

---

## Fallback When Budget Exhausted

When NotebookLM budget is exhausted:
1. **Notify user**: "NotebookLM budget exhausted (100/100 queries). Skills-only mode active. Resets on [date]."
2. **Switch to skills-only**: Load Tier 2 (genius.md) instead of Tier 1.5
3. **Offer Perplexity**: For foundation tasks requiring external research, suggest Perplexity ($10/mo budget)
4. **Document**: Log all budget-constrained decisions in session state

---

*Effective: 2026-03-06 | Created: NotebookLM RAG Integration*
*Classification: Mandatory Resource Governance Protocol*
