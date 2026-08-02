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

Verification phrases: canonical behavior source; real Codex subagents require explicit authorization; no competing behavior contract.

Preserve the current End-session contract: whole-session closeout, retrieval
handoff, closeout intelligence capture, `3 Next Prompts`, `Operator Lesson`,
`Next-time prompt`, `Subagent worth it?`, `Reuse hook`,
`session_closeout_intelligence.py run --source end-session`,
`conversation_index.py stats`, exact named handoff save plus
`handoff_store.py verify <thread> --source <path> --json`, Codex coordination
through `execution/codex_end_session.py run --manifest <json>`,
`[Domain]: [Specific Object] - [Outcome]`, archive only after a verified
`done` receipt, automatic commit and push only for manifest-owned paths in a
dedicated `codex/*` worktree, and Never auto-commit, auto-merge, or auto-push `main`.
Real Codex subagents require explicit authorization.

## Command Template

Read and execute the workflow at `.agent/workflows/end-session.md` — Clean workspace, organize assets, generate handoff
