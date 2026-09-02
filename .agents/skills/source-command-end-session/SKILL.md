---
name: "source-command-end-session"
description: "Clean workspace, organize assets, generate handoff"
---

# source-command-end-session

Use this skill when the user asks to run the migrated source command `end-session`.

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
- exact named handoff save plus `handoff_store.py verify <thread> --source <path> --json`
- Codex coordination through `codex_end_session.py run --manifest <json>`
- `[Domain]: [Specific Object] - [Outcome]`, rename every meaningful task, pin unfinished work, and archive only verified `done`
- automatic commit and push only in a dedicated `codex/*` worktree
- Never auto-commit, auto-merge, or auto-push `main`
- real Codex subagents require explicit authorization
- no competing behavior contract
- `close ready` never archives or merges main
- `close done` requires integration proof and a coordinator archive receipt
- `bulk closeout audit` is read-only and dispatches nothing
- Bare `ready` and `done` are status words, never commands


## Command Template

Read and execute the workflow at `.agent/workflows/end-session.md` — Clean workspace, organize assets, generate handoff
