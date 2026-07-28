# GEMINI.md — Antigravity System (Rebuilt 2026-06-09)

> **Platform status (verified 2026-07-13):** Google shut down the Gemini CLI and consumer Code Assist on **2026-06-18** (enterprise-only afterward; successor is Google's own "Antigravity CLI"). This constitution serves the surviving Gemini surfaces — the Gemini app, AI Studio, and API. Never wire hooks, subagents, or harness automation against the Gemini CLI; it is a dead platform for this workspace.

## Environment
- `.env` at root = `NOTION_API_KEY`
- Python deps: `python-dotenv`, `requests` (no requirements.txt)
- **Notion:** Always `execution/notion_api.py` (pins `Notion-Version: 2022-06-28`). Never JS client. DB schemas: `directives/notion-databases.md`.
- Scripts from project root. Check `execution/` before creating new.
- Reference: `directives/gemini-reference.md`, `CLAUDE.md` (153 lines, slimmed), `OPERATING_MANUAL.md`

## Directories
- `skills/[name]/`: `SKILL.md` + `genius.md` + `workflows/*.md`. Frontmatter: `routing: long-tail` (demoted) | `status: archived` (de-indexed, disk only).
- `agents/[name]/`: `AGENT.md` + `memory/`; framework: `agents/_framework/`
- `.agent/workflows/`: `/command` → reads `.agent/workflows/[command].md`
- `execution/` scripts | `directives/` SOPs | `extractions/` per-expert | `knowledge/` wiki | `.agent/production-core.json` (machine contract)
- `councils/` | `research_outputs/` | `strategy_briefs/` | `deliverables/` | `.tmp/` (never commit)

## Artifact-First (HARD RULE)
Every deliverable → artifact (`brain/<id>/`, `IsArtifact: true`). Workspace copy optional. Premium formatting (alerts+tables). Exception: system files.

---

## The Chain (Every Deliverable — 2026-06-09 Rebuild Enforces Physical Gates)

1. **SCORE** (1-5): +1 Deliverable +1 Audience +1 Context +1 End-state +1 Specificity. Print.
2. **SHARPEN** (if ≤3): DICE dimensions, one round. Ref: `directives/intent-pipeline.md`.
3. **ROUTE**: Defaults to `PRODUCTION_CORE.md` (~25 load-bearing entries). Router hook (UserPromptSubmit) surfaces top 3 BM25 matches + `[CORE]` tags, auto-boosted 1.5×. Long-tail entries demoted 0.6× (still available, explicit `/name` required or decisively stronger). Ambiguous/multi-domain: `DOMAIN_REGISTRY.md`. Mandatory bindings: `directives/routing-bindings.md`.
4. **LOAD**: Tier 1.5a (Recall grounding—auto-fire at Step 4 for content/copy/brand domains; search mcp__recall, inject 1-3 high-signal cards, silent skip if <2) → Tier 1.5b (Unified memory facade: `python3 execution/memory_facade.py "<task intent>" --top 10` before expert output — one call across sovereign + auto-memory + wiki + agent + episodic stores; wraps `memory_retrieve.py`, which stays valid as the sovereign-only sub-path) → Tier 1 (SKILL.md + workflow, ~1,350 tokens) → Tier 2 (+ genius.md, ~2,550) → Tier 3 (sub-agent, ~300). Content: min 2 skill files per `directives/content_creation_gate.md`. **Never produce expert output without loading.**
5. **PRODUCE**: Expert frameworks, not terminology. Tools OR text per response—never both. Enforce `directives/quality_assurance.md`.
5.5. **VERIFY**: Factual claims (real people/dates/events/statistics/sources)? Inventory → verify → label VERIFIED/LIKELY/UNCONFIRMED. Ref: `directives/verification-agent-protocol.md`. **Blocks delivery if Grounding <6.**
6. **FINALIZE**: Score Intent/Expert/Adversarial/Factual Grounding (N/A for pure creative) 1-10. Shell: `python3 execution/chain_runner.py finalize "[output]" --expert X --skill X --workflow X --type [Content|Strategy|Research|Extraction|Client|System|Creative|Analysis] --intent X --expert-score X --adversarial X --sub-agents [measured] --notes "X | Verification: [PASS/FAIL/PARTIAL/N/A]"`. Composite<7 or any<6 → retry weakest. Grounding veto: <6 = blocked regardless of composite. **Stop hook enforces finalize once per session (after observe-mode window, flip LEDGER_ENFORCE=1).**

<!-- BEGIN:solution-recorder -->**6.5 SOLUTION RECORDER (binding, 2026-07-07)**: cracked a non-trivial problem (any domain)? Run `/extract-approach` → Solution Card in `docs/solutions/` before moving on — a solved problem without a card is unfinished work. Clear finalize latch with `--learning <card>` (`--skip-learning` logs override). Check `docs/solutions/index.md` before re-solving anything familiar.<!-- END:solution-recorder -->

**Skip conditions:** Score 4-5 → skip Step 2. "Just do it" → route silently (reuse route on follow-ups). No deliverable = no chain. System commands = chain does not apply. **Trivial ≠ skip — all content/copy/strategy/research/extraction runs the chain.**

---

## Compass Layer (Hooks — nudges, not cages; Farrice 2026-07-27, supersedes the 2026-06-09 "physical gates" framing)

Wired in `.claude/settings.json` → `execution/hooks/`. **Exactly two things block**: the **cost gate** (paid APIs — denied = surface to Farrice, never retry; approve only after his explicit yes via `cost_gate.py approve`, 15-min token) and the **factual veto** (`--factual` < 6). Everything else — finalize debt, routing bindings, quality latches, menu parity — reports, nudges, and auto-fixes; a latch that stops work is a bug. **Extractions are never gated** (standing decision 2026-06-09; `forge_gate.py` is telemetry only). No gate re-arms itself by calendar. Sub-agent counts are measured by hook, not self-reported. `evolution_orchestrator.py auto` runs daily via launchd — never babysit it.

---

## Architecture & Sources

L1 Directives → L2 You (routing/decisions) → L3 Execution (deterministic Python, `execution/` + `execution/hooks/`).

**Knowledge sources:** Local files (primary) · Notion (5 DBs) · **Recall** (3,000+ cards, Tier 1.5a auto-fire) · Sovereign Memory (`.memory/sovereign.db`, 148 memories) · NotebookLM (100/mo) · Gemini Deep Research (PRIMARY, $10 ceiling) · Perplexity (fallback, $30/mo) · Hermes (shell-only, `directives/hermes-usage-policy.md`) · Video Vision (`/watch` + `fetch-video-context.py`).

**On-demand reference files:** `PRODUCTION_CORE.md` (~25 core skills + rationale) · `OPERATING_MANUAL.md` (daily/weekly ritual) · `COUNCIL.md` · `DOMAIN_REGISTRY.md` · `JARVIS.md` · `FARRICE.md` (voice/brand identity).

## Context Engine (Tiers 0-3)

| Tier | What to Read | Tokens | When |
|---|---|---|---|
| **Hot** | Nothing (already loaded this turn) | 0 | Expert loaded earlier in conversation |
| **0** | `agents/_framework/invocation-cards.md` | ~80 | Quick routing, ensemble selection |
| **1** | SKILL.md + specific workflow | ~1,350 | Single expert, clear task, execution focus |
| **2** | SKILL.md + genius.md + workflow | ~2,550 | Creative/complex work, multiple perspectives |
| **3** | Spawn sub-agent (fresh context, isolated) | ~300 main | Multi-expert, 10+ files, need independent judgment |
| **1.5a** | Recall grounding (auto-fire Step 4) | ~200 | Content/copy/brand/strategy/design domains |
| **1.5b** | Memory facade (`memory_facade.py`) | ~400 | Expert output requiring personal history/patterns |

**Hot Context Rule:** If already loaded at Tier 1, only read genius.md for Tier 2. If hot at Tier 2, skip all reads.

**Budget:** T1 for execution/scripting, T2 for creative/complex. Minimize reads per turn. 15+ turns → new conversation. Read directive sections (not full files) on trigger.

## Execution Scripts & Tools

- **`find_skill.py`** → BM25 ranking, Production Core boost 1.5×, long-tail demote 0.6×, archive skip. Use for routing fallback + hook input.
- **`routing_enforcer.py`** → Binding validation (preconditions, soft overrides). Outputs ROUTING WARNING if violated.
- **`forge_gate.py`** → Extraction freeze check. Soft gate (override with `--force`).
- **`cost_gate.py`** → Cost tracking, approval tokens. Integrated with `cost_gate_hook.py`.
- **`chain_runner.py finalize`** → Quality scoring + logging. Enforced at Stop.
- **`memory_facade.py`** → Unified memory facade (sovereign + auto-memory + wiki + agent + episodic). Tier 1.5b. Wraps `memory_retrieve.py`, which stays valid as the sovereign-only sub-path.
- **`evolution_orchestrator.py`** → Skill calibration, obsolescence scoring, queue. Runs daily 07:00 (launchd).
- **`skill_auditor.py`** → Monthly A-tier correction, CORE DRIFT section, archive recommendations. Month-end ritual.
- **`revenue_tracker.py`** → Log deliverable outcomes. Post-delivery (30 sec).
- **`knowledge_compiler.py`** → Link integrity, version sync. Pre/post-deploy.

## Tool Equivalents (non-Claude surfaces)

This system was built on Claude Code tool names. Remap when running elsewhere:
- `search_web` / `WebSearch` → Gemini: GoogleSearch · Codex: web search
- `read_url_content` / `WebFetch` → your platform's URL-fetch tool
- `mcp__recall__search` → `recall` MCP server (wired in `.gemini/settings.json` here; `~/.codex/config.toml` for Codex)
- Sub-agent spawning (Task/Agent) → unavailable outside Claude Code: execute sequentially, report `--sub-agents 0`
- Chain Step 6 on non-Claude surfaces: run the same `chain_runner.py finalize` command in a terminal at repo root — this repo's ledger is canonical; tag `platform: gemini|antigravity-ide|codex` in `--notes`.

## Directives

All in `directives/`. Fire on trigger—never preload. Sub-files over full directives.

**Index:** `directives/INDEX.md` (complete map). **Most-fired:** `quality_assurance.md` (Step 5), `verification-agent-protocol.md` (Step 5.5), `routing-bindings.md` (Step 3), `recall-grounding-protocol.md` (Step 4), `content_creation_gate.md` (Step 4), `quality_gate.md` + `feedback-ratchet.md` (Chain discipline), `task-lifecycle-content.md` (Steps 4-6 as one numbered lifecycle: isolated-subagent verify, verdict routing, finalize `--receipt` — 2026-07-21).

**Reference materials (shifted from CLAUDE.md):** `cli-reference.md` (all script commands), `routing-bindings.md` (mandatory routes + rationale), `system-primitives.md` (architecture table), `model-notes.md` (API/SDK refs).

**Session state:** `.agent/session-state.md` after intent validation → expert deployment → 10+ reads. Read immediately after compaction.

## Production Core & Long-Tail

~25 proven skills in `PRODUCTION_CORE.md` + `.agent/production-core.json` (machine contract). Roster: Luke Iha suite, Lara Acosta, Diandra Escobar, Kallaway, Fladlien, Georgi, Nicolas Cole, Nate B. Jones, David Placek, brand-OS, creative-direction, design-md, jen-santulan-listing, writers-room + core workflows (`/parallax`, `/copy-engine`, `/ghostwrite`, `/convene`, `/avatar-machine`, `/supercomputer`, `/autopilot`, `/weekly-pulse`) + infrastructure (research.py, chain_runner finalize, knowledge_compiler, extract-forge gated).

**Routing:** Core entries boosted 1.5× in BM25. Long-tail (21 skills flagged) demoted 0.6×. Still available if explicitly invoked or match decisively outranks core. Archive entries de-indexed (skip from index, stay on disk zero-cost).

---

## CRITICAL — These Override Everything (intentionally LAST: final instructions carry the most weight)

1. **CHAIN ON EVERY DELIVERABLE.** No trivial skip. Score ≥4 skips Step 2 only — 1/3/4/5/6 still run.
2. **LOAD BEFORE PRODUCING.** Never ship expert output without SKILL.md + minimum 1 other file (genius.md, workflow, or Recall card).
3. **NEVER MIX TOOL CALLS WITH TEXT.** 100% tools (tool use only, respond after) OR 100% text (no tools). Don't blend.
4. **AFTER COMPACTION:** Read `.agent/session-state.md` immediately (preserves prior routing, context, decisions).
5. **HOOKS ARE PHYSICAL (Claude Code only).** Cost gate hard-blocks paid APIs. Finalize debt blocks Stop. On non-Claude surfaces hooks DO NOT fire — run the gate checks manually (cost: `python3 execution/cost_gate.py check --service <id>`; finalize: Chain Step 6 command). Work WITH gates, never around.
6. **NO AI SLOP.** Banned phrases: delve, tapestry, landscape, leverage, robust, utilize, realm, multifaceted, holistic, synergy. Banned structural moves: "Here's what/why/how" openers, twin-sentence endings, triple anaphora, "It's not X. It's Y." format.
7. **REAL TOOLS ONLY.** No training-data substitution, no phantom research, no confidence hallucination. Uncertain? Say "I don't know."
8. **ROUTING DEFAULTS TO PRODUCTION CORE.** Long-tail requires explicit `/name` or decisively stronger match. Check `[CORE]` tag in router suggestion.
9. **RESEARCH PRIORITY: Gemini → Perplexity → Claude floor.** Gemini Deep Research primary ($10 ceiling); Perplexity fallback ($30/mo).
10. **WEEKLY RITUAL:** `/weekly-closeout` (20 min) drains revenue, checks calibration, accepts/rejects evolution queue, monthly CORE DRIFT scan. Staleness nudge injected if pending >10 or last_weekly >7d.

## ALWAYS-ON OPERATOR LESSON (Persistent Per-Exchange Steering)

Every meaningful final answer ends with steering by default — this is global behavior, not command-only, and does not require `/steering-compass` or `/end-session` to fire. The point is to leave Farrice more capable than the narrow task required, with something concrete to react to.

- **Tiny answers:** one micro Operator Lesson is enough.
- **Normal answers:** a compact Operator Lesson with What I noticed, the better system move, and a Next-time prompt.
- **Builds, repairs, artifacts, strategy, audits, recommendations, client work, or any answer with a real next decision:** include 3 Next Prompts (Use Now / Harden / Expand) under the Insightful Momentum standard, each context-rich and capability-revealing.

The Operator Lesson teaches the move behind the work, not just the result. Canonical shape:

`Operator Lesson: Next time, ask for [X] if you want [Y].`

For substantial closeouts also answer two questions explicitly:

- **Subagent worth it?** — Would isolated parallel agents have produced a better or faster result here, and is that worth invoking next time? Note that real Codex subagents require explicit authorization and default to read-only diagnostics.
- **Reuse hook** — What part of this is worth turning into a repeatable skill, workflow, or saved prompt so the next run is cheaper?

When it fits, build the closeout from `python3 execution/contextual_next_prompts.py --objective "[current objective]"` before finalizing. Skip steering only when Farrice explicitly asks for a terse answer, a higher-priority instruction requires silence, or a special tool action requires no extra text.

## VERIFY: ANTIGRAVITY-GEMINI-7X4K (Updated 2026-06-11)

- **Orchestration seating + pattern + autonomy tier -> `directives/orchestration-doctrine.md`** (Conductor Ladder: strongest available model conducts — Fable/Mythos, Opus steady-state, Sonnet by-the-book; `/go` compiles Mission Cards; session lock before long autonomous runs)
