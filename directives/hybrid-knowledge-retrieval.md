# Hybrid Knowledge Retrieval

> **Purpose**: Smart routing across all Antigravity knowledge sources for optimal information retrieval.
> **Effective**: 2026-03-06

## Overview

The hybrid knowledge retrieval system orchestrates searches across 5 knowledge sources, automatically routing queries to the most appropriate source(s) based on query type. This prevents over-reliance on any single source and ensures the most relevant, up-to-date information is retrieved.

---

## Knowledge Sources

| Source | Content Type | Best For | Token Cost | Speed |
|--------|-------------|----------|------------|-------|
| **NotebookLM** | Domain research, expert examples | Expert methodology patterns, recent context | 1 query (100/mo budget) | Slow (3-10s) |
| **Skills** | Expert methodologies, frameworks | Primary expert knowledge | 0 (local) | Fast (<1s) |
| **Files** | Directives, CLAUDE.md, system docs | Code/system questions, protocols | 0 (local) | Fast (<1s) |
| **Notion** | Projects, knowledge vault, content pipeline | Project context, ICP, current initiatives | API quota | Medium (1-3s) |
| **Perplexity** | Real-time web research | Current trends, market data | $30/mo budget | Medium (2-5s) |

---

## Routing Table

### Auto-Routing (Scope: "auto")

The system classifies queries and routes to appropriate sources:

| Query Type | Signals | Primary Source | Secondary Source | Use Case |
|------------|---------|----------------|------------------|----------|
| **Expert Methodology** | "What did [expert] say", "[expert]'s approach", "hook patterns" | NotebookLM | Skills | "What are Lara's hook patterns?" |
| **Project Context** | "my ICP", "our positioning", "current project" | Notion | NotebookLM | "What's my LinkedIn ICP?" |
| **Current Trends** | "latest", "2026 data", "recent" | Perplexity | — | "Latest AI coaching pricing 2026" |
| **Code/System** | "how to add", "agent/skill/directive", "implementation" | Files | — | "How do I add a new expert?" |
| **Historical** | "why did we choose", "previous decision", "what happened" | Files (git, session state) | Notion | "Why did we choose X approach?" |

### Manual Scopes

Override auto-routing with explicit scope:

```python
result = retriever.search(query, scope="notebooks")  # NotebookLM only
result = retriever.search(query, scope="local")       # Files + Skills only
result = retriever.search(query, scope="all")         # All 5 sources
```

**Available Scopes:**
- `auto` — Smart routing (default)
- `local` — Files + Skills (fastest, zero cost)
- `notion` — Notion databases only
- `notebooks` — NotebookLM only
- `web` — Perplexity only
- `all` — All 5 sources (expensive, comprehensive)

---

## Token Budgeting

**Hard Limit**: 1,500 tokens per search result

**Compression Strategy**:
1. Rank all results by relevance score
2. Include highest-ranked results first
3. Truncate when total exceeds 1,500 tokens
4. Ensure minimum 100 tokens per result

**Per-Source Token Estimates**:
- NotebookLM response: ~500 tokens (max after compression)
- Skills grep result: ~125 tokens (truncated)
- Files snippet: ~200 tokens (context around match)
- Notion page: ~300 tokens
- Perplexity result: ~400 tokens

---

## Integration Points

### Intent Pipeline (Step 3c)

After routing to expert, check if supplemental knowledge needed

### Expertise Gap Protocol (Phase 1b)

Before extraction recommendation, search existing research

### /knowledge-search Workflow

User-facing hybrid search command

---

## Budget Coordination

### Multi-Source Budget Tracking

When hybrid search uses multiple budgeted sources:

| Source | Budget | Per-Query Cost | Tracking |
|--------|--------|----------------|----------|
| NotebookLM | 100 queries/mo | 1 query per notebook | `.agent/notebooklm-usage.json` |
| Perplexity | $30/mo | $0.02-0.30 per query | `.agent/perplexity-usage.json` |
| Notion | 3 req/sec (API limit) | N/A | No tracking (free tier) |
| Files/Skills | Unlimited | 0 | No tracking (local) |

### Budget Exhaustion Fallback

When budgets exhausted → Gracefully downgrade to `scope="local"`

---

## Performance Characteristics

| Scope | Sources Queried | Typical Latency | Token Output | Cost |
|-------|----------------|----------------|--------------|------|
| `local` | 2 (files, skills) | <1s | 300-500 | $0 |
| `notebooks` | 1-3 (NotebookLM) | 5-15s | 500-1500 | 1-3 queries |
| `auto` | 2-3 (varies) | 2-10s | 500-1500 | Varies |
| `all` | 5 (all sources) | 10-20s | 1500 (compressed) | High |

---

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-04-11 |

**Update Rule**: When this protocol fires (hybrid retrieval (Notion + NotebookLM + search) used), update the date and increment count.

*Classification: Knowledge Infrastructure Protocol*
*Effective: 2026-03-06*
