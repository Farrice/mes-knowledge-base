---
name: "source-command-source-to-skill-system"
description: "Run source-to-skill-system when source material should become a connected Codex skill system with component skills, step order, input/output handoffs, human checkpoints, validation, and a cold-start check."
---

# source-command-source-to-skill-system

Use this skill when the user asks to run `source-to-skill-system`, wants to turn a video/transcript/article/book into a reusable Codex skill system, wants better skill orchestration, or asks how to make skills work end to end instead of as isolated skills or mega-skills.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/source-to-skill-system.md` as the
canonical behavior source. It must stay a thin compatibility wrapper and
preserve:

- source material becomes connected skill systems, not isolated mega-skills
- evidence and existing-route fit come before building
- every build fills the Skill System Contract before implementation
- Agentic Engineering Packet is required for agentic engineering changes
- Goal Packet is required for self-improvement, maintenance, cleanup, or evolution changes
- companion OS layers are preferred over duplicate expert skills when improving existing control-plane behavior
- no hot skill promotion, global mirror, external write, new dependency, or broad workflow mutation without explicit approval and validation
- repair, drift-audit, and broken-system language routes to `/system-audit` or `/autopilot`
- real Codex subagents require explicit authorization
- no competing behavior contract

## Command Template

Read and execute the workflow at `.agent/workflows/source-to-skill-system.md`.
