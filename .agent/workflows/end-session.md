---
description: Run at the end of a deep-work session to clean the workspace, organize assets, and generate a handoff for the next session.
---

# 🧹 /end-session — Workspace Cleanup & Context Handoff

> **Purpose**: Prevent "artifact sprawl" by strictly enforcing the system's rule that intermediate files are disposable and deliverables must be organized. Creates a clean starting point for the next session.

## Usage

```
/end-session
```

## Protocol Steps

### 1. Artifact Triage (The "Delete or Keep" Filter)
Identify all files created in the current session's `brain/` directory.

- **Intermediates to Delete**: Temp extractions, web scraped text, rough drafts, raw data dumps.
- **Deliverables to Keep**: Final offer docs, finished flywheel packages, built skills.

### 2. File Organization
// turbo-all
1. Move any *Intermediates* into a `.tmp/` directory (or delete them entirely, as they should be regenerated if needed).
2. Ensure *Deliverables* are properly named and formatted.
3. Consolidate any fragmented notes into their canonical master files.

### 3. State Check
- Read the current `task.md`.
- Mark completed items, roll over uncompleted items to the next session.
- Ensure the final state of the `task.md` accurately reflects reality.

### 4. System Health Pulse
Run a quick health check to surface any dormant systems:
```bash
python execution/system_health.py --quick
```
If any systems are CRITICAL or DORMANT, note in the handoff summary so the next session can address them.

### 5. Git Checkpoint (Optional)
// turbo
- If the workspace is a Git repository, offer to run `git add .` and `git commit -m "Auto-commit at end of session: [Summary of work]"`
- Do not push without explicit confirmation.

### 6. Generate Handoff Summary
Output a concise "Handoff Code" block into the conversation that the user can copy-paste as their very first prompt in the *next* chat window. 

The handoff must follow the format in `directives/token-efficiency-protocol.md`:

```markdown
## Session Handoff
**Completed:** [2-3 bullet points of what was built]
**Remaining priority:** [Next immediate task]
**Core context to load:** [Paths to the 2-3 essential deliverable files]
```

### 7. Execution Offer
Before running, present the triage plan to the user:
> "I've scanned the workspace. I plan to move [X, Y, Z] to temporary storage, finalize [A, B], and update your task sheet. Want me to execute the cleanup?"
