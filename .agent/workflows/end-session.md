---
description: Run at the end of a deep-work session
---

# 🧹 /end-session — Session Handoff

> **Purpose**: Generate a clean handoff for the next session. Deep cleanup is optional — assets are already organized when produced.

## Usage

```
/end-session              # Quick handoff (default)
/end-session --deep       # Full cleanup + handoff
```

## Quick Handoff (Default — 1-2 Tool Calls)

### 1. Generate Handoff Summary
// turbo
Output the handoff block:

```markdown
## Session Handoff
**Completed:** [2-3 bullet points of what was built]
**Remaining priority:** [Next immediate task]
**Core context to load:** [Paths to the 2-3 essential deliverable files]
**Hot experts this session:** [List of experts loaded — so next session can warm-start]
```

### 2. Update Conversation Index
// turbo
Update the master conversation index with final artifacts and completion status:
```bash
python execution/conversation_index.py update <current-conversation-id>
```

### 3. Git Checkpoint (Optional)
// turbo
If the workspace is a Git repo, offer to commit:
> "Want me to commit? `git add . && git commit -m 'Session: [Label]'`"

Do not push without explicit confirmation.

---

## Deep Cleanup (`--deep`)

Run all steps above, plus:

### 3. Artifact Triage
Identify files in the current session's `brain/` directory:
- **Delete**: Temp extractions, raw data dumps, rough drafts
- **Keep**: Final offer docs, finished skills, deliverables

### 4. Finalize Session Workspace
// turbo
If a session workspace exists:

```bash
python3 execution/session_workspace.py finalize
```

### 5. File Organization
// turbo
- Move intermediates to `.tmp/`
- Ensure deliverables are properly named
- Consolidate fragmented notes into canonical files

### 6. State Check
- Read `task.md`, mark completed items, roll over uncompleted items

---

## When to Use
- **Quick Handoff**: End of any session — costs almost nothing
- **Deep Cleanup** (`--deep`): After heavy sessions (extractions, multi-expert work, client deliverables)
- Skip entirely if the session was conversational with no artifacts produced
