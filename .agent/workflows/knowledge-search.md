---
description: Hybrid search across all knowledge sources with smart routing
---

# /knowledge-search — Unified Knowledge Retrieval

Search across files, Notion, NotebookLM, Perplexity, and skills with intelligent routing.

## Usage

```
/knowledge-search [query]
/knowledge-search --scope=notebooks [query]
/knowledge-search --scope=all [query]
```

## Knowledge Sources

- **NotebookLM**: Expert examples, recent research (1-3 queries/search)
- **Skills**: Expert methodologies (free, fast)
- **Files**: System docs, directives (free, fast)
- **Notion**: Project context, ICP (API quota)
- **Perplexity**: Current trends, market data ($30/mo)

## Scopes

- `auto` — Smart routing based on query type (default)
- `local` — Files + Skills only (fastest, free)
- `notebooks` — NotebookLM only
- `notion` — Notion databases only
- `web` — Perplexity only
- `all` — All 5 sources (comprehensive, expensive)

## Steps

1. Parse scope from command (default: auto)
2. Execute hybrid search via `notebooklm_knowledge_retrieval.py`
3. Results ranked by relevance, compressed to 1,500 tokens
4. Present unified output with source attribution

## Smart Routing (scope=auto)

| Query Type | Routes To | Example |
|------------|-----------|---------|
| Expert methodology | NotebookLM + Skills | "Lara's hook patterns" |
| Project context | Notion + NotebookLM | "My LinkedIn ICP" |
| Current trends | Perplexity | "2026 pricing trends" |
| Code/system | Files | "How to add expert" |
| Historical | Files + Notion | "Why we chose X" |

## Budget Impact

- NotebookLM: 1-3 queries per search (100/mo limit)
- Perplexity: $0.02-0.30 per search ($30/mo limit)
- Other sources: Free

## Performance

| Scope | Latency | Cost | Best For |
|-------|---------|------|----------|
| `local` | <1s | Free | Code questions |
| `notebooks` | 5-15s | 1-3 queries | Expert examples |
| `auto` | 2-10s | Varies | General (recommended) |
| `all` | 10-20s | High | Comprehensive research |

## Related

- `/query-notebook` — Direct NotebookLM query
- `/research-topic` — Deep Perplexity research

---

*Budget: Varies by scope*
