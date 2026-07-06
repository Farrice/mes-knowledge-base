---
name: "source-command-self-evolve"
description: "Workflow, prompt, retrieval logic, or orchestration pattern"
---

# source-command-self-evolve

Use this skill when the user asks to run the migrated source command `self-evolve`.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/self-evolve.md` as the canonical
behavior source. It must stay a thin compatibility wrapper with no competing
behavior contract.

Verification phrases: canonical behavior source; complete goal packet; real Codex subagents require explicit authorization; no competing behavior contract.

Preserve the current Self-evolve contract: mutation-gated measured evolution;
queue-only diagnosis for incomplete or vague goal packets; complete goal
packet; Evolution Council Verdict; baseline; search set; measurable stop
condition; turn cap; proof artifact; no-regression check; local, reversible
side effects; human checkpoint for risky changes;
`verify_mission_activation_contract.py` before any approved Mission repair; and
real Codex subagents require explicit authorization.

## Command Template

Read and execute the workflow at `.agent/workflows/self-evolve.md` — Workflow, prompt, retrieval logic, or orchestration pattern
