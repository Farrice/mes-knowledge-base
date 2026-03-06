---
description: Query a specific NotebookLM notebook for domain-specific research and context
---

# /query-notebook — Direct NotebookLM Query

Query a registered NotebookLM notebook for domain-specific research, examples, and applied methodology patterns.

## Usage

```
/query-notebook [notebook-name-or-id] [your question]
```

**Examples:**
```
/query-notebook "LinkedIn Ghostwriting Research" "What are the top 3 hook patterns?"
/query-notebook "AI Brain Build Sprint" "How should I structure my offer?"
/query-notebook b665051a "Lara Acosta CTA strategies"
```

---

## Steps

### 1. Identify Notebook

Parse notebook name or ID from command:
- If **name** provided (e.g., "LinkedIn Ghostwriting Research"):
  - Look up in `mcp-servers/notebooklm/notebooks.md` registry
  - Match by name (case-insensitive)
- If **ID** provided (e.g., `b665051a-20f2-419b-b0a8-4b77d3382464`):
  - Use ID directly

**If not found:**
```python
from notebooklm_client import NotebookLMClient

client = NotebookLMClient()
notebooks = client.list_notebooks()

print("Available notebooks:")
for nb in notebooks:
    print(f"• {nb['name']} ({nb['id']})")
    print(f"  Purpose: {nb['purpose']}\n")

# Ask user to clarify or use /add-notebook to register
```

### 2. Check Budget

```python
queries_used, queries_remaining = client.check_budget()

if queries_remaining < 1:
    print(f"⚠️ NotebookLM budget exhausted ({queries_used}/100 queries used).")
    print(f"Resets on 1st of next month.")
    print(f"Falling back to skills-only mode.")
    return
elif queries_remaining <= 20:
    print(f"⚠️ Budget low: {queries_remaining} queries remaining.")
```

### 3. Execute Query

```python
result = client.query(
    notebook_id=notebook_id,
    query=user_query,
    task_context="user_query_notebook"
)
```

### 4. Present Result

```markdown
## {notebook_name} Response

{result.compress()}

---

**Notebook**: {result.notebook_name}
**Query time**: {result.duration_seconds}s
**Cached**: {result.cached}
**Budget remaining**: {queries_remaining - 1}/100 queries
```

**Follow-up options:**
- Query another notebook
- Load the relevant expert skill (Tier 1.5 with notebook context)
- Export to Notion for persistent storage

---

## Budget Tracking

Every query is logged to `.agent/notebooklm-usage.json`:

```json
{
    "timestamp": "2026-03-06T10:30:00-08:00",
    "notebook_id": "b665051a-20f2-419b-b0a8-4b77d3382464",
    "notebook_name": "LinkedIn Ghostwriting Research",
    "query": "What are the top 3 hook patterns?",
    "task_context": "user_query_notebook"
}
```

---

## Error Handling

### Budget Exhausted
```
⚠️ NotebookLM budget exhausted (100/100 queries used).

Falling back to skills-only mode. Load the relevant expert skill:
• For LinkedIn: skills/lara-acosta-linkedin-mastery/
• For AI offers: skills/samuel-thompson-idea-validation/

Budget resets on: March 1, 2026
```

### Notebook Not Found
```
❌ Notebook not found: "Marketing Research"

Available notebooks:
• Higgsfield Cinema Studio (55c8cd8d...)
• AI Brain Build Sprint (ca3520ff...)
• LinkedIn Ghostwriting Research (b665051a...)

Use /add-notebook to register a new notebook.
```

### Query Failed
```
❌ Query failed: [error message]

This could be:
• Authentication issue — re-run /add-notebook setup
• Notebook has no sources — add sources to NotebookLM first
• Rate limit hit — wait a few minutes and retry

Falling back to skills-only mode for now.
```

---

## Tips

**Query Optimization** (save budget):
- Combine related questions into one query
- Check cache first (duplicate queries are free)
- Use specific questions vs broad exploration

**When to Use:**
- Need recent research context (2024-2026 data)
- Want applied examples from expert methodology
- Cross-referencing expert claims with research
- Quick lookups that don't require full skill loading

**When NOT to Use:**
- Primary expert knowledge (load skills first)
- Code/system questions (use directives/files)
- When budget is exhausted (skills-only mode)

---

## Related Workflows

- `/knowledge-search` — Hybrid search across files, Notion, NotebookLM, Perplexity
- `/add-notebook` — Register a new NotebookLM notebook
- `/extract` → Upload extraction to NotebookLM for future RAG

---

*Workflow Type: User-Invoked*
*Budget: 1 query per execution*
