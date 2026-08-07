---
name: "source-command-repeatability-spine"
description: "Run repeatability-spine when the user cannot repeat the magic, a revision got worse, a route chose the wrong workflow, a patch introduced a regression, or a good output needs a preservation lock before revision."
---

# source-command-repeatability-spine

Use this skill when the user asks to run `repeatability-spine`, says a revision failed, says the rewrite got worse or flat, says the system cannot repeat the magic, says the route picked the wrong workflow, or wants to preserve what made a previous output work.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/repeatability-spine.md` as the
canonical behavior source. It must stay a thin compatibility wrapper and
preserve:

- preserve the good example before repair
- every run needs grounded evidence, one primary failure class, Preservation Lock, repair route, validation, regression guard, and replay prompt
- inaccessible conversations are pending evidence, not invented findings
- routing failures require a verifier query or routing feedback log before being called repaired
- mutation-capable repair routes require a Goal Packet before edits
- global `~/.codex` behavior changes require workspace proof and explicit approval
- broad broken-harness triage routes to `/autopilot` or `/system-audit`
- real Codex subagents require explicit authorization
- no competing behavior contract

## Command Template

Read and execute the workflow at `.agent/workflows/repeatability-spine.md`.
