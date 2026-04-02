---
description: Rebuild or update the conversation index to make
---

# /index-conversations — Rebuild the Conversation Index

Regenerates the master index of all conversation directories in `brain/`. Run this periodically or after bulk work.

## Usage

```
/index-conversations           # Full rebuild
/index-conversations <conv-id> # Update a single conversation
```

## Steps

### 1. Run the Indexer

// turbo
```bash
python execution/conversation_index.py build
```

This scans all conversation directories in `~/.gemini/antigravity/brain/`, extracts metadata from artifacts and logs, and produces:
- `brain/_index/conversations.json` — machine-readable index
- `brain/_index/conversations.md` — human-readable master index

### 2. Report Results

Present the stats output to the user. Highlight:
- Total conversations indexed
- Top domains and experts
- Any errors encountered

### 3. Offer Follow-up

> "Index rebuilt with [N] conversations. Want me to search for something specific? Try `/find-context [topic]`"
