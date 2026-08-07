---
name: "source-command-end-session"
description: "End the session with handoff, automatic evidence capture, routing feedback, and local-first intelligence logging"
---

# source-command-end-session

Use this skill when the user asks to run the migrated source command `end-session`, close out the session, finish the session, log the session, capture feedback, or make the system learn from the work without manual routing/logging steps.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/end-session.md` as the canonical behavior source. It must stay a thin compatibility wrapper and preserve:

- whole-session closeout, retrieval handoff, and closeout intelligence capture
- clear separation from focused `/handoff` transfer packets and standalone `/steering-compass` next-prompt coaching
- `3 Next Prompts`
- `Operator Lesson`
- `Next-time prompt`
- `Subagent worth it?`
- `Reuse hook`
- `session_closeout_intelligence.py run --source end-session`
- `conversation_index.py stats`
- real Codex subagents require explicit authorization
- no competing behavior contract

## Command Template

Read and execute the workflow at `.agent/workflows/end-session.md` — End the session with handoff, automatic evidence capture, routing feedback, and local-first intelligence logging
