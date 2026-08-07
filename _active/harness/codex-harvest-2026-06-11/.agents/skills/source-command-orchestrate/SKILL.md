---
name: "source-command-orchestrate"
description: "Menu-only backend for turning a live goal into ranked execution options with expert stacks, workflows, and verification criteria"
---

# source-command-orchestrate

Use this skill only when the user asks to run the migrated source command `orchestrate`, asks for an execution menu, wants ranked options, or wants to compare possible workflow/expert-stack paths.

Do not use this skill when the user wants the system to choose and begin work. Route that through `source-command-autopilot`, which owns intent lock, route choice, and safe-run execution after trace.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/orchestrate.md` as the canonical behavior source. It must stay a thin compatibility wrapper and preserve:

- menu-only backend behavior
- must not execute, mutate files, or choose on Farrice's behalf
- execution intent routes through `/autopilot`
- real Codex subagents require explicit authorization
- no competing behavior contract

## Command Template

Read and execute the workflow at `.agent/workflows/orchestrate.md` - Menu-only backend that turns a live goal into ranked execution options, expert stacks, workflows, and verification criteria
