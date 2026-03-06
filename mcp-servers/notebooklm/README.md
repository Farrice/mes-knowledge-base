# NotebookLM Integration

RAG knowledge retrieval from Google NotebookLM notebooks.

## Quick Start

### Direct Python Script (Recommended)

```bash
# Query specific notebook
python execution/notebooklm_client.py query b665051a "What are Lara's hook patterns?"

# Search all notebooks
python execution/notebooklm_client.py search "LinkedIn authority building"

# List registered notebooks
python execution/notebooklm_client.py list

# Check budget
python execution/notebooklm_client.py budget
```

### Via Workflows

```bash
# Direct notebook query
/query-notebook "LinkedIn Ghostwriting Research" "What are hook patterns?"

# Hybrid search across all sources
/knowledge-search What are Lara's hook patterns?
```

---

## Registered Notebooks

See `notebooks.md` for full registry. Currently:

1. **Higgsfield Cinema Studio** — AI video generation prompts
2. **AI Brain Build Sprint** — Offer design, audience psychology
3. **LinkedIn Ghostwriting Research** — LinkedIn methodology, market intelligence

---

## Budget

- **Monthly Limit**: 100 queries
- **Warning**: 80 queries (80%)
- **Tracking**: `.agent/notebooklm-usage.json`
- **Reset**: 1st of each month

---

## Adding Notebooks

Use `/add-notebook` or manually update `notebooks.md`

---

## Architecture

Direct Python scripts (zero MCP overhead) → notebooklm-mcp CLI → Chrome automation → Google NotebookLM

---

## Files

```
mcp-servers/notebooklm/
├── README.md                          # This file
├── notebooks.md                       # Notebook registry
├── notebooklm-config.json            # CLI configuration
└── chrome_profile_notebooklm/        # Persistent Chrome auth

execution/
├── notebooklm_client.py              # Python wrapper (primary)
└── notebooklm_knowledge_retrieval.py # Hybrid search

directives/
├── notebooklm-usage-policy.md        # Budget policy
└── hybrid-knowledge-retrieval.md     # Routing logic

.agent/
├── notebooklm-usage.json             # Usage tracking
└── knowledge-cache.json              # 7-day cache

.agent/workflows/
├── query-notebook.md                 # /query-notebook
└── knowledge-search.md               # /knowledge-search
```

---

*For details: `directives/notebooklm-usage-policy.md` and `directives/hybrid-knowledge-retrieval.md`*
