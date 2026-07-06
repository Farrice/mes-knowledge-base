---
name: "source-command-system-audit"
description: "Control-plane audit for broken, drifted, duplicated, slow, or not-firing harness behavior"
---

# source-command-system-audit

Use this skill when the user asks to run the migrated source command `system-audit`, reports not-firing hooks, routing drift, operating-alignment issues, duplicated command surfaces, or broken harness behavior.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/system-audit.md` as the
canonical behavior source. It must stay a thin compatibility wrapper with no
competing behavior contract.

Preserve the current System-audit contract:

- control-plane audit and repair
- read-only proof first
- distinguish structural health from firing behavior
- repairs are severity-ranked, verifier-backed, and workspace-local by default
- global `~/.codex` edits require explicit approval
- Mission remains untouched unless `verify_mission_activation_contract.py` fails and Farrice explicitly approves Mission repair
- real Codex subagents require explicit authorization

## Command Template

Read and execute the workflow at `.agent/workflows/system-audit.md` - Google-local control-plane audit and repair with read-only proof first, manual hook-equivalent gates, and registry hygiene as a supporting section.
