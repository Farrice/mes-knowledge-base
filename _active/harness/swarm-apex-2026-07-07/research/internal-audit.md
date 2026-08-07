# Internal Orchestration Stack Audit (2026-07-07, Sonnet Explore agent)

Full apex-plan wave text lives at `_active/harness/harness-apex-2026-07-07/PLAN.md` — not restated here.

## Capability Matrix

| Component | Real parallelism? | Synthesis | Key gaps |
|---|---|---|---|
| **/convene** (`.agent/workflows/convene.md` + `collective-genius-council.workflow.js` + `council_cast.py`) | **YES on the native Workflow surface** — `parallel(roster.map(m => () => agent(...)))` for Diverge + Deliberate Round A, schema-validated (`TAKE_SCHEMA`/`RESP_SCHEMA`). Codex surface (`convene.py`/`kimi_swarm.py`) explicitly never spawns real subagents — packet compiler only | Multi-stage: converge (preserves forks — "never blend to mush") → synthesize → learn digest to `knowledge/council-rubric.md` | Grounding per-voice opportunistic, not gated; roster depends on stale invocation-cards |
| **/supercomputer** | NO — Phase 2 is "for each step... in order"; no spawn instruction anywhere | Anchor-memory context threading + P3 grep-propagation check (prose, flagged open question at genius.md:84) | `workflows/` dir empty; single-threaded mission |
| **/autopilot** | Explicitly not parallel by default — fan-out requires per-run authorization, read-only diagnostics only | None (single dispatcher); closeout ritual | G1 (DICE ≤2) / G2 (spend >$5) / G3 (prose) gates = multi-clause prose, Wave 2 `gates.py` planned |
| **JCC plugin** | Designed for Agent-tool parallelism + aspirational TeamCreate/TaskCreate with graceful-degradation fallback (tools may not exist at runtime) | mission-decomposer computes DAG/critical-path ratio; synthesis-agent flags contradictions | ~100% prose; **internally contradictory scale tables** (scaling-thresholds.md: CAMPAIGN "5-8 experts" line 43 vs "3-5 concurrent" line 57-62); model: inherit everywhere; unproven at scale |
| **swarm-orchestrator agent** | Was real (Agent-tool batch) | Compound-not-average + Forks section | **ARCHIVED** 2026-05-02 — see no-claude-code-subagents below |
| **/swarm family** (swarm-commander skill: swarm, parallel-swarm, swarm-research, research-swarm, angle-swarm) | **Explicitly NOT parallel by design** — SKILL.md:9-13 claims "80-95% of true parallelism benefits using sophisticated prompt engineering... True parallel execution isn't required." batch-execution = sequential persona simulation in one context, file-based coordination. 6+ agents falls back to Gemini `parallel_swarm.py` (no tool access) | Mandatory 🟢GROUNDED/🟡SUPPLEMENTED/🔴PROJECTED tags per claim + dedicated Grounding Pass phase before synthesis + minority-position preservation | The grounding discipline is excellent and must survive the v2 rebuild; the execution model is the part to replace |
| **Expert layer** | N/A | N/A | **Count drift**: invocation-cards "148 genius upgrades"/council_cast "89 cards"/DOMAIN_REGISTRY "96 agents"/JCC "109+" — actual `agents/` dir = **221 persona directories**. No live-computed source of truth |
| **Injection mechanism** (`directives/agent-loading-protocol.md` Tier 3) | — | — | File-read-driven at spawn time (SKILL.md → genius.md → prompt); no compiled/cached persona artifact |

## Deterministic layer
- `chain_runner.py:264-324` — 27 qualifying workflows, auto-logs sub-agent misses to `evolution_store/sub_agent_misses.jsonl` (observe-only). Protocol had 0 activations 2026-02-17→04-24 until made deterministic 2026-05-12.
- `directives/sub_agent_protocol.md` — 4-field envelope (OBJECTIVE/OUTPUT-FORMAT/TOOLS/BOUNDARIES), **hard cap 12 parallel workers/phase**, tiered budget 1→2-4→5-10→12, adaptive re-routing via `parallel_swarm.py::execute_agent_with_fallback`.
- `execution/research.py` — Gemini→Perplexity→Claude floor, "HONEST RECEIPT on every result... can degrade — it cannot lie."
- `evolution_orchestrator.py::run_routing_learning` — as of Wave 1 (2026-07-07) finalize quality composites nudge `.agent/skill-weights.json` (≥8 up, <7 down), cursor at `.agent/routing-quality-cursor.json`.

## Deliverable packaging
- `package-deliverable.md` = manual playbook (Gamma paste-in → Canva → custom HTML→PDF → Notion). Its own "Future Automation Opportunity" section admits the automation script does not exist.
- `.agent/run-receipts/` = post-hoc text audit trail, not a shareable polished artifact. `deliverables/` = mostly raw .md + a few one-off HTML demos, no packaging convention.

## Binding constraints (quoted)
1. **No Claude Code subagents** — `directives/no-claude-code-subagents.md`: "`.claude/agents/` is closed... `_archived/` ... not an invitation to revive." 12 virtuoso subagents (incl. swarm-orchestrator) removed 2026-05-02: "produced subpar output... polluted routing... no quality return." **Reconciliation confirmed**: `.claude/agents/` today contains only `_archived/`; the harness freely uses generic ad-hoc Agent-tool dispatch (2026-07-06 handoff records "Fable orchestrating ~20 Sonnet subagents"). Rule = no standing named subagent roster; ad-hoc dispatch with expert-file injection is fine.
2. **No forced wiring** — hubs are independent peers; cross-hub handoffs are options, never pipeline steps (2026-07-02 handoff:36; apex PLAN.md:124).
3. **Density > completeness** — `directives/peak-operation.md:10`: word-ceiling every agent report (500-900 words); evidence lines, never documentation claims.
4. **Opus never pinned** — `directives/model-notes.md:7-11`: inherit → Sonnet → Haiku; `platform_compiler.py lint` fails active pins.
5. **Thin orchestrator** — `peak-operation.md:37`: "Sonnet is the default executor and auditor... Opus only for judgment-dense synthesis... The orchestrator stays thin."

## GAPS vs Manus-class platforms
1. No long unattended mission mode with live progress (everything is conversational/checkpoint-driven; receipts are post-hoc).
2. No browser-native autonomous worker type (Playwright = ad-hoc tool grant).
3. No automated deliverable packaging (manual playbook only).
4. Real concurrent fan-out inconsistently available: only the native Workflow surface demonstrates it (council workflow.js); swarm-commander is sequential simulation; autopilot approval-gated; Codex surface never spawns.
5. Swarm cross-checking is prose-based; Wave 2 verifiers (claim_audit, blind_pass) queued not shipped.
6. JCC parallelism claims internally contradictory + untested (Wave 3 pilot decides).
7. No durable multi-day mission graph with autonomous resumption (handoffs are human/model-read artifacts; COS World Pulse is the only shipped unattended loop).
8. Expert roster metadata stale/drifting (4 conflicting counts vs 221 actual).
