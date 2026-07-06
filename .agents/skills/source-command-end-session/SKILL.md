---
name: "source-command-end-session"
description: "Clean workspace, organize assets, generate handoff"
---

# source-command-end-session

Use this skill when the user asks to run the migrated source command `end-session`.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/end-session.md` as the canonical
behavior source. It must stay a thin compatibility wrapper with no competing
behavior contract.

Preserve the current End-session contract: whole-session closeout, retrieval
handoff, closeout intelligence capture, `3 Next Prompts`, `Operator Lesson`,
`Next-time prompt`, `Subagent worth it?`, `Reuse hook`,
`session_closeout_intelligence.py run --source end-session`,
`conversation_index.py stats`, and real Codex subagents require explicit
authorization.

## Command Template

Read and execute the workflow at `.agent/workflows/end-session.md` — Clean workspace, organize assets, generate handoff
