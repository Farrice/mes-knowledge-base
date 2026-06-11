# Platform Bakeoff — Protocol & Pre-Committed Decision Rule

Purpose: choose the daily driver with scored evidence, not vibes. Platforms: Claude Code, Codex (CLI/Desktop), Antigravity IDE (+ Gemini CLI only if installed). Capability gate: a platform must pass its canary probe (`capability-matrix.md`) before it runs tasks.

## How to run
1. One platform per sitting, all 6 tasks, same prompts, **paste each `tasks/task-NN.md` verbatim** — no coaching, no retries beyond what the platform itself offers.
2. Save every output to `runs/<platform>/task-NN.md`. Record at the top: date, model used (exact), wall-clock minutes, anything that errored.
3. Score later, in a separate Claude Code session, **blind**: shuffle outputs so the scorer doesn't know the platform, score against `evolution_store/ground_truth/rubric_v1.md` anchors (Intent / Expert / Adversarial / Factual Grounding where applicable; ≥8 requires naming the matching anchor).
4. Append one JSON line per (task, platform) to `scores.jsonl`:
   `{"task": 1, "platform": "codex", "model": "gpt-5.5", "intent": 7, "expert": 6, "adversarial": 7, "grounding": null, "minutes": 9, "notes": "..."}`
5. Run `python3 scorecard.py` — it aggregates and applies the decision rule below mechanically.

## Pre-committed decision rule (locked 2026-06-11, before any task was run)
- **Daily driver** = highest composite average across all 6 tasks, **minimum 7.5 composite with no single task below 6.5**.
- **Tie-break**: winner of task 03 (research with receipts) — research quality compounds across everything else.
- **Role assignment for non-winners**: any platform scoring ≥7.0 on a specific task class keeps that lane (e.g., Codex = code lane via task 06; Antigravity IDE = UI/browser lane). Below 7.0 everywhere = experimental only.
- **If no platform clears the bar**: Claude Code remains daily driver **by data, not inertia**, and satellites are re-tested after their next packaging fix.
- The rule may not be edited after the first run is recorded. Post-hoc rationalization is the failure mode this file exists to prevent.

## Constants (fairness)
- Each platform uses its own best default model; the model is RECORDED, because "what you actually get day-to-day" is the thing being tested — capacity errors (e.g., Opus unavailable) count as real performance.
- All platforms work in THIS repo. Finalize for every run: `python3 execution/chain_runner.py finalize ... --notes "... | platform: <name> | bakeoff: task-NN"` — the ledger is canonical here.
