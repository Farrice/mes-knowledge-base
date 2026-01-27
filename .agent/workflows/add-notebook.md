---
description: Add a NotebookLM notebook to the registry for AI querying
---

# Add NotebookLM Notebook

This workflow registers a new NotebookLM notebook so Claude can query it during project work.

## Required Information

1. **Notebook URL** - The full URL from NotebookLM (e.g., `https://notebooklm.google.com/notebook/abc123-def456`)
2. **Notebook Name** - A friendly name to reference it (e.g., "Marketing Research", "Client Project X")
3. **Purpose** - Brief description of what the notebook contains

## Steps

### 1. Extract Notebook ID

Parse the notebook ID from the provided URL:
- URL format: `https://notebooklm.google.com/notebook/NOTEBOOK_ID`
- Extract everything after `/notebook/`

### 2. Update Registry

Add the notebook to `/Users/farricecain/Google Antigravity/mcp-servers/notebooklm/notebooks.md`:

```markdown
| [Name] | `[notebook-id]` | [Purpose] |
```

### 3. Test Connection

// turbo
Run this command to verify the notebook is accessible:

```bash
cd /Users/farricecain/Google\ Antigravity/mcp-servers/notebooklm && \
source ~/.local/bin/env && \
export SSL_CERT_FILE=$(uv run python -c "import certifi; print(certifi.where())") && \
uv run notebooklm-mcp --config notebooklm-config.json chat --message "Summarize your available sources" --notebook-id [NOTEBOOK_ID]
```

### 4. Confirm Success

Report to user:
- Notebook registered with name and ID
- Test query result (or note if notebook needs sources)
- Reminder: Tell Claude "Query my [notebook name]" to use it

## Example Usage

```
/add-notebook

URL: https://notebooklm.google.com/notebook/55c8cd8d-bbb9-4975-9d11-0b961878ac6f
Name: AI Business Research  
Purpose: Market research and niche analysis for AI product launches
```
