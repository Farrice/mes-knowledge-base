---
name: "source-command-autopilot"
description: "Gate-suppressed orchestration dispatcher across all 7 outcome classes. Composes the right mission package, runs end-to-end with only 3 taste gates (G1 intent, G2 cost, G3 prose), surfaces a copy-pasteable refinement ledger at the end."
---

# source-command-autopilot

Use this skill when the user asks to run the slash command `/autopilot` or migrated source command `autopilot`.

## Command Template

Read and execute the workflow at `.agent/workflows/autopilot.md` — Gate-suppressed dispatcher that takes fuzzy intent and runs the full chain without mid-flight halts. Internally manages Phase 0 (intent + package resolution) through Phase 5 (ledger emission), surfacing only G1 (intent ≤2 → sharpen), G2 (paid cost > $5 → approve once), and G3 (prose FLAGGED at Expert Standard ≥7 → taste call). All other halts suppressed.

## Operator Core Alignment

This project wrapper is intentionally thin. It follows `.agent/workflows/autopilot.md` as the **canonical behavior source** and must preserve the Operator Core closeout standard rather than define a competing one.

Every meaningful run ends with persistent per-exchange steering: for substantial work, include **3 Next Prompts** (Use Now / Harden / Expand) under the Insightful Momentum standard, and always close with an **Operator Lesson** that teaches the move behind the work, a **Next-time prompt** (copy-paste continuation), a **Subagent worth it?** check — noting that real Codex subagents require explicit authorization and default to read-only diagnostics — and a **Reuse hook** naming what to turn into a repeatable skill or workflow.
