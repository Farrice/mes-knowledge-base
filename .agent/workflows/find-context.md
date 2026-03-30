---
description: Search across all past conversations and artifacts by keyword, domain, expert, or date
---

# /find-context — Context Search & Retrieval

Search your conversation history to find past work, artifacts, and expert outputs without manually hunting through directories.

## Usage

```
/find-context ghostwriting           # Keyword search
/find-context revenue sprint         # Multi-word search
/find-context --domain LinkedIn      # Filter by domain
/find-context --expert "Lara Acosta" # Filter by expert
/find-context --recent 5             # Last 5 conversations
```

## Steps

### 1. Parse the User's Search Intent

Translate the natural language query into the appropriate `context_search.py` flags:

| User says | Map to |
|-----------|--------|
| "Find my LinkedIn stuff" | `python execution/context_search.py "linkedin"` |
| "What did we do with Nicolas Cole?" | `python execution/context_search.py --expert "Nicolas Cole"` |
| "Show me walkthroughs" | `python execution/context_search.py --type walkthrough` |
| "What did we work on this week?" | `python execution/context_search.py --since 2026-03-24` |
| "Show me the last 5 sessions" | `python execution/context_search.py --recent 5` |
| "What domains have I covered?" | `python execution/context_search.py --all-domains` |

Multiple filters can be combined:
```bash
python execution/context_search.py "revenue" --domain Strategy --since 2026-03-25
```

### 2. Run the Search

// turbo
Execute the mapped command. If no index exists, run `python execution/conversation_index.py build` first.

### 3. Present Results

Show the search results to the user. For each relevant result, highlight:
- Conversation title and date
- Key artifacts with their file paths
- Expert involvement

### 4. Offer to Load Context

If the user identifies a conversation they want to revisit:

> "Want me to read the [artifact name] from that session and pick up where you left off?"

This is the key value — don't just *find* context, offer to *load* it so the user can immediately resume work.
