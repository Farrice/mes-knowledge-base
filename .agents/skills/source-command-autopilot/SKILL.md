---
name: "source-command-autopilot"
description: "Gate-suppressed orchestration dispatcher across all 7 outcome classes. Composes the right mission package, runs end-to-end with only 3 taste gates (G1 intent, G2 cost, G3 prose), surfaces a copy-pasteable refinement ledger at the end."
---

# source-command-autopilot

Use this skill when the user asks to run the slash command `/autopilot` or migrated source command `autopilot`.

## Command Template

Read and execute the workflow at `.agent/workflows/autopilot.md` — Gate-suppressed dispatcher that takes fuzzy intent and runs the full chain without mid-flight halts. Internally manages Phase 0 (intent + package resolution) through Phase 5 (ledger emission), surfacing only G1 (intent ≤2 → sharpen), G2 (paid cost > $5 → approve once), and G3 (prose FLAGGED at Expert Standard ≥7 → taste call). All other halts suppressed.
