---
name: "source-command-self-evolve"
description: "Improve a workflow, prompt, retrieval rule, or orchestration pattern using feedback, failure history, performance logs, regression checks, and measured evolution without adding unnecessary bloat."
---

# source-command-self-evolve

Use this skill when the user asks to run `self-evolve`, improve a workflow from feedback or failure history, use performance logs, run regression-aware evolution, reduce recurring mistakes, or improve routing/orchestration without adding unnecessary bloat.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/self-evolve.md` as the canonical behavior source.
It must stay a thin compatibility wrapper and preserve:

- mutation-gated measured evolution, not casual improvement
- incomplete or vague goal packets produce queue-only diagnosis and missing fields
- mutation requires a complete goal packet, Evolution Council Verdict, baseline, search set, measurable stop condition, turn cap, proof artifact, and no-regression check
- side effects must be local, reversible, and inside `/Users/farricecain/Codex Antigravity`
- human checkpoint for global mirrors, external actions, broad archive/delete, destructive cleanup, new dependencies, failed validation, or scope expansion
- no Mission mutation unless `verify_mission_activation_contract.py` fails and the user explicitly approves Mission repair
- repair, drift-audit, and broken-system language routes to `/system-audit` or `/autopilot`
- real Codex subagents require explicit authorization
- no competing behavior contract

## Command Template

Read and execute the workflow at `.agent/workflows/self-evolve.md` - Improve a workflow, prompt, retrieval rule, or orchestration pattern using feedback, failure history, performance logs, regression checks, and measured evolution without adding unnecessary bloat
