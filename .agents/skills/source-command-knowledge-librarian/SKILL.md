---
name: "source-command-knowledge-librarian"
description: "Run knowledge-librarian to produce a compact session-start knowledge pulse with relevant solution docs, underused workflows, expert stacks, stale or overlap risks, and one exact start command without dumping the library."
---

# source-command-knowledge-librarian

Use this skill when the user asks to run `knowledge-librarian`, wants a
session-start library pulse, needs prior reusable solution docs, wants
underused skills/workflows surfaced, asks what knowledge/workflows they are not
using, or needs one start command from the library without a giant inventory.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/knowledge-librarian.md` as the
canonical behavior source. It must stay a thin compatibility wrapper and
preserve:

- compact session-start knowledge pulse by default
- read-only default scans with `knowledge_compiler.py stats` and `knowledge_compiler.py solutions ... --stdout`
- existing compiled briefing may be read, but briefing refresh is not run by default
- every named capability is grounded in local evidence
- no state snapshot, compiled knowledge refresh, solution-doc creation, Mission mutation, cleanup, destructive action, or global mirror unless explicitly requested
- repair, drift-audit, and broken-system language routes to `/system-audit` or `/autopilot`
- real Codex subagents require explicit authorization
- no competing behavior contract

## Command Template

Read and execute the workflow at `.agent/workflows/knowledge-librarian.md` - Compact session-start knowledge pulse that finds relevant solution docs, underused workflows, expert stacks, stale or overlap risks, and one exact start command without dumping the library
