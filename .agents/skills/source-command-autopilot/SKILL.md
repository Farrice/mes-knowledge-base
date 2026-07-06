---
name: "source-command-autopilot"
description: "Google-local Codex front door for raw intent, route choice, Raw Intent Virtuoso Bridge packets, safe local execution, proof, and closeout."
---

# source-command-autopilot

Use this skill when the user asks to run the slash command `/autopilot` or migrated source command `autopilot`.

Autopilot is the Intent-to-outcome, safe execute-by-default front door for
workspace-local Codex work. It must emit an Execution Decision, a copy-paste
Run Prompt when blocked, a Run Receipt after meaningful work, and a Friction Ledger entry when routing, retrieval, proof, or operator friction appears.
Plugin packaging requests go through `/plugin-readiness-audit` and the local
plugin-readiness-audit proof ladder before any packaging recommendation.

## Command Template

Read and execute the workflow at `.agent/workflows/autopilot.md`. For rough
intent, messy context, or "I do not know how to ask Codex" starts, compile the
Raw Intent Virtuoso Bridge packet first:

```bash
python3 execution/raw_intent_run_packet.py "<raw intent>" --plain
```

Then follow Autopilot's chosen route, support gates, execution decision, and
verifier plan.

## Operator Core Alignment

This project wrapper is intentionally thin. It follows `.agent/workflows/autopilot.md` as the **canonical behavior source** and must preserve the Operator Core closeout standard rather than define a competing one.

Every meaningful run ends with persistent per-exchange steering: for substantial work, include **3 Next Prompts** (Use Now / Harden / Expand) under the Insightful Momentum standard, and always close with an **Operator Lesson** that teaches the move behind the work, a **Next-time prompt** (copy-paste continuation), a **Subagent worth it?** check — noting that real Codex subagents require explicit authorization and default to read-only diagnostics — and a **Reuse hook** naming what to turn into a repeatable skill or workflow.
