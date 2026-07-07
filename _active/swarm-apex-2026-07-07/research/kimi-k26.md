# Kimi K2.6 / OK Computer / Kimi Work — Mechanics Brief (2026-07-07, Sonnet deep-research)

## Thesis
Moonshot out-engineered the agent loop: K2-Thinking/K2.6 make long-horizon tool use a first-class training objective, shipped through two surfaces (cloud sandbox "OK Computer" for artifacts, on-device "Kimi Work" for real-browser-session automation). The weights aren't copyable, but three orchestration patterns are: swarm decomposition, heavy-mode reflect-and-aggregate, and default approval-gating.

## Agentic Mechanics
- [VERIFIED — HF model card, moonshotai/Kimi-K2-Thinking] End-to-end trained to interleave chain-of-thought with function calls; sustains coherent behavior across 200–300 consecutive tool invocations (prior gen degraded after 30–50).
- [VERIFIED — same] "Heavy Mode": rolls out 8 full trajectories simultaneously, then "reflectively aggregates all outputs" — self-consistency ensembling applied to entire agentic runs, not just final-answer voting.
- [LIKELY — secondary aggregators, not Moonshot primary] K2.6 Agent Swarm: up to 300 sub-agents / 4,000 total steps (vs ~100/1,500 in K2.5). Directionally credible; precise numbers unconfirmed.
- [UNCONFIRMED] BrowseComp numbers vary by source/config: 60.2% (K2-Thinking) / 83.2% (K2.6 tools) / 86.3% (K2.6 + Agent Swarm). Treat as directional.

## Product-Level Orchestration
- OK Computer [LIKELY — SCMP]: cloud agent mode; single prompt → multi-page site or editable deck; up to 1M rows of data; multimodal output. Manus/Genspark-style artifact generation, not general computer use.
- Kimi Work [VERIFIED via MarkTechPost, June 2026]: local desktop agent (macOS/Windows) — reads local files in place, drives a real already-logged-in browser via a "WebBridge" extension (inherits cookies/sessions vs anonymous sandbox), cron schedules + keep-awake for overnight jobs. Default posture: ask-before-acting on file writes and web actions.
- [LIKELY] Swarm decomposition is MapReduce-shaped: "one reader per file, then merge findings."

## Best At / Weak At
- [LIKELY — Nate's Newsletter, firsthand] Strongest at bounded single-artifact generation, decks specifically: "beautiful design, clean execution, fast iteration."
- [LIKELY — same] Weakest at sustained ADAPTIVE agentic work — performance drops when a task requires autonomously navigating obstacles or adapting approach across multi-hour workflows. Directly undercuts "300 tool calls" as a proxy for real multi-hour reliability.
- [UNCONFIRMED] Training-provenance allegation (Anthropic-attributed extraction campaign) — contested, changes credit assignment not benchmark numbers.

## Counter-Read
Benchmarks consistently place K2.6 at/above frontier peers on agentic tasks; the "degrades on adaptive work" signal is one anecdote vs three converging leaderboards. Don't over-weight either.

## Transferable Patterns
1. Heavy-mode reflect-and-aggregate: N parallel trajectories + dedicated reflection pass — implementable today as a subagent pattern.
2. Named swarm roles, not generic fan-out ("one reader per file, merge") — reduces redundancy, gives a clean merge step.
3. Default approval-gating on state-changing actions — audit our subagents for the same discipline on write/send/submit.
4. Score long-run agentic work on adaptive-obstacle-navigation, not step count — that's where marketing and reality diverge.

## Sources
Primary: HF Kimi-K2-Thinking model card. Secondary: MarkTechPost (Kimi Work), SCMP (OK Computer), Nate's Newsletter (firsthand), BenchLM/GMI Cloud/Kili aggregators (flagged UNCONFIRMED where untraceable to a Moonshot primary). Internal: Recall funding/architecture cards, `_active/codex-harvest-2026-06-11/execution/kimi_swarm.py` (prior internal modeling).
