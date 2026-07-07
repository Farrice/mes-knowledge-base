# Manus AI — Mechanics Brief (2026-07-07, Sonnet deep-research)

## Thesis
Manus's real architecture is the opposite of the "swarm of specialized agents" story most secondary coverage tells: per its own chief scientist, Manus deliberately runs with almost no role-differentiated sub-agents (a planner, a general executor, a knowledge module — that's nearly it) and treats CodeAct + an aggressively engineered flat context as the actual intelligence, only spinning up homogeneous (not specialized) sub-agents for one narrow case: parallel "wide research" fan-out.

## Agent Loop Mechanics
- [VERIFIED — manus.im blog + gist technical writeup, github.com/renschni/4fbc70b31bad8dd57f3370239dccd58f] The loop is: analyze event stream → select one action → execute in a cloud Ubuntu sandbox VM → append the observation to context → repeat. Explicitly single-action-per-iteration, which bounds runaway behavior.
- [VERIFIED — same gist + CodeAct research] Actions are executable Python/shell code, not discrete tool calls. The agent writes scripts chaining multiple operations, reads back stdout/stack traces, debugs itself. Manus's framing: code-as-action beats JSON-function-calling on success rate for complex multi-step tool use.
- [VERIFIED — Recall card, direct quote from Yichao "Peak" Ji, co-founder/chief scientist, LangChain webinar, youtube.com/watch?v=6_BcCthVvb8] NOT a role-divided multi-agent system internally: "we do not divide by role. We only have very few agents — a huge general executor agent and a planner agent and a knowledge management agent... we are very cautious about adding more sub agents because communication is very hard."
- [LIKELY] The planner produces a step roadmap written to a persistent `todo.md`, injected into context as a "special event," checked off as steps complete — survives context resets because it lives on disk.

## Context Engineering Specifics
- [VERIFIED — manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus, primary] KV-cache hit rate = "the single most important metric"; input:output ratio ~100:1. Cached Sonnet input $0.30/MTok vs $3 uncached — 10x gap drives every decision.
- [VERIFIED] Rules: byte-identical prompt prefix (no timestamps in system prompts), strictly append-only context with deterministic JSON serialization, session IDs pinning requests to the same backend worker.
- [VERIFIED] `todo.md` recitation = deliberate attention hack: rewriting and re-appending the todo pushes the global plan into the recent-token attention window, avoiding lost-in-the-middle goal drift across ~50 tool calls per task.
- [VERIFIED] File system = the real unlimited context. Compression is restorable-by-design: content dropped but URL/file path kept, so re-fetchable.
- [VERIFIED] Failed actions and stack traces deliberately left in context — seeing failure "implicitly updates the model's internal beliefs." Tools aren't dynamically removed (breaks cache); unavailable tools hidden via logit-masking.

## Deliverable Pipeline
- [LIKELY] Reports, decks (.pptx/PDF with speaker notes), spreadsheets, live-hosted websites are produced by the same general executor writing and running code in the sandbox — consistent with "zero predefined workflows, just more context to the model."
- [UNCONFIRMED] Reviewer/marketing claims of "specialized sub-agents per deliverable" conflict with Peak's primary-source statement. Flagged, not reconciled.

## Multi-Agent / Wide Research
- [VERIFIED — Peak Ji, same webinar] "Wide Research" (internally "agentic map-reduce") spins up 100+ sub-agents, each a full non-specialized Manus instance. Shared context via sandbox/file system (main agent passes file paths, not raw content); each sub-agent must call a constrained "submit result" tool with schema-constrained decoding for a uniform reduce step. [VERIFIED] Pro-tier ($199/mo) first.

## Best At / Weaknesses
- [LIKELY, converging reviews — lindy.ai, allaboutai.com, metaflow.life] Best: bulk structured-data extraction/transformation, autonomous multi-step cited web research, functioning deployed websites from one prompt.
- [VERIFIED — review roundups] Weakness: opaque credit burn — 400 credits on 4 Google Maps lookups, 1000 credits before first output, no real-time spend alerts, billing on failed runs.

## Transferable Patterns
1. todo.md-recitation: persistent re-appended plan file checked at end of context, not written once.
2. Don't prune tool availability dynamically — mask/route instead, preserving cache.
3. Keep failures in context deliberately.
4. Anti-multi-agent discipline: resist role-proliferation; communication is the hard part. Validates the 2+ experts / 10+ files sub-agent bar.
5. Fan-out = homogeneous sub-agents + schema-constrained submit contract + shared file system handoff — not bespoke role prompts per worker.

## Sources
Internal: Recall cards on Peak Ji LangChain webinar + 2 Manus spotlight videos. External: manus.im context-engineering blog (primary); manus.im wide-research post (primary); renschni gist teardown; venturebeat; metaflow.life/lindy.ai/allaboutai.com (secondary reviews).
