---
description: Register a new NotebookLM notebook for RAG integration
---

# /add-notebook — Register NotebookLM Notebook

Interactively register a NotebookLM notebook to make it available for queries via `/query-notebook` and automatic context loading.

## Usage

```
/add-notebook
```

The user will type this slash command, and you'll walk them through the registration process.

---

## Steps

### 1. Collect Notebook Information

Ask the user for three pieces of information:

**Notebook URL:**
```
Please provide the full NotebookLM URL.

How to get it:
1. Open NotebookLM (notebooklm.google.com)
2. Click on the notebook you want to register
3. Copy the URL from your browser

Format: https://notebooklm.google.com/notebook/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
```

**Friendly Name:**
```
What should we call this notebook?

Examples:
• "LinkedIn Ghostwriting Research"
• "AI Brain Build Sprint"
• "Marketing Strategy 2026"
```

**Purpose:**
```
Brief description (one sentence) of what's in this notebook.

Examples:
• "LinkedIn content frameworks and hook patterns"
• "Research and strategy for AI coaching offers"
• "Q1 marketing campaign planning and competitive analysis"
```

### 2. Run Interactive Registration

Execute the Python script in interactive mode:

```bash
cd "/Users/farricecain/Google Antigravity" && python execution/discover_notebooks.py --add
```

**The script will:**
1. Prompt for the notebook URL (paste the URL from step 1)
2. Prompt for the friendly name (enter the name from step 1)
3. Prompt for the purpose (enter the description from step 1)
4. Extract the notebook ID from the URL
5. Check for duplicates
6. Add the entry to `mcp-servers/notebooklm/notebooks.md`
7. Confirm success

### 3. Verify Registration

After the script completes, verify the notebook was registered:

```bash
cd "/Users/farricecain/Google Antigravity" && python execution/discover_notebooks.py --list
```

This will show all registered notebooks including the new one.

### 4. Confirm to User

Show confirmation message:

```
✓ Notebook registered successfully!

**Name**: [Friendly Name]
**ID**: [notebook-id]
**Purpose**: [Purpose]

You can now query this notebook:
• /query-notebook "[Friendly Name]" "your question"
• /knowledge-search (will auto-route when relevant)

**Budget**: [X] NotebookLM queries remaining this month
```

---

## Error Handling

### Invalid URL Format

If the script shows: `❌ Invalid URL. Expected format: https://notebooklm.google.com/notebook/XXXXXXXX`

Tell the user:
```
The URL format is incorrect. Please:
1. Go to notebooklm.google.com
2. Open the specific notebook
3. Copy the FULL URL from the browser address bar
4. It should look like: https://notebooklm.google.com/notebook/abc123-def456...
```

### Duplicate Notebook

If the script shows: `⚠️ Notebook already registered`

Ask the user:
```
This notebook is already registered. Would you like to:
1. Keep the existing entry (type: n)
2. Update it with new information (type: y)
```

### Missing Information

If name or purpose is empty:
```
Both name and purpose are required. Let's try again:
• Name: Short, memorable identifier
• Purpose: One sentence describing the content
```

---

## Quick Reference

**List all notebooks:**
```bash
python execution/discover_notebooks.py --list
```

**Add notebook (interactive):**
```bash
python execution/discover_notebooks.py --add
```

**Add multiple notebooks:**
The script will ask "Add another? (y/n)" after each registration.

---

## Related Workflows

- `/query-notebook` — Query a registered notebook
- `/knowledge-search` — Hybrid search across all sources

---

*Workflow Type: User-Invoked*
*Budget: Free (registration only, no queries used)*
