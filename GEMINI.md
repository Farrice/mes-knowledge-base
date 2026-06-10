# GEMINI.md — Antigravity System (Rebuilt 2026-06-09)

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
4. **LOAD**: Tier 1.5a (Recall grounding—auto-fire at Step 4 for content/copy/brand domains; search mcp__recall, inject 1-3 high-signal cards, silent skip if <2) → Tier 1.5b (Sovereign memory: `python3 execution/memory_retrieve.py "<intent>" --top 10` before expert output) → Tier 1 (SKILL.md + workflow, ~1,350 tokens) → Tier 2 (+ genius.md, ~2,550) → Tier 3 (sub-agent, ~300). Content: min 2 skill files per `directives/content_creation_gate.md`. **Never produce expert output without loading.**
5. **PRODUCE**: Expert frameworks, not terminology. Tools OR text per response—never both. Enforce `directives/quality_assurance.md`.
5.5. **VERIFY**: Factual claims (real people/dates/events/statistics/sources)? Inventory → verify → label VERIFIED/LIKELY/UNCONFIRMED. Ref: `directives/verification-agent-protocol.md`. **Blocks delivery if Grounding <6.**
6. **FINALIZE**: Score Intent/Expert/Adversarial/Factual Grounding (N/A for pure creative) 1-10. Shell: `python3 execution/chain_runner.py finalize "[output]" --expert X --skill X --workflow X --type [Content|Strategy|Research|Extraction|Client|System|Creative|Analysis] --intent X --expert-score X --adversarial X --sub-agents [measured] --notes "X | Verification: [PASS/FAIL/PARTIAL/N/A]"`. Composite<7 or any<6 → retry weakest. Grounding veto: <6 = blocked regardless of composite. **Stop hook enforces finalize once per session (after observe-mode window, flip LEDGER_ENFORCE=1).**

**Skip conditions:** Score 4-5 → skip Step 2. "Just do it" → route silently (reuse route on follow-ups). No deliverable = no chain. System commands = chain does not apply. **Trivial ≠ skip — all content/copy/strategy/research/extraction runs the chain.**

---

## Deterministic Enforcement Layer (Hooks — PHYSICAL Gates, 2026-06-09)

Wired in `.claude/settings.json` → `execution/hooks/`. These gates are **real** — not advisory, not memory-dependent. Work WITH them.

| Gate | Hook | Behavior |
|---|---|---|
| **Cost gate** (Fal, Seedance, Kling, deep-research) | PreToolUse(Bash) → `cost_gate_hook.py` | **HARD BLOCK.** Denied = surface to user. Needs-approval = `cost_gate.py approve --service <id>` (15-min token), retry. |
| **Finalize debt** | Stop → `session_ledger_hook.py` | Skill loaded + artifact produced + no finalize = blocked ONCE with prefilled command. **Observe-mode ships; flip LEDGER_ENFORCE=1 after ~5 clean sessions.** |
| **Routing violations** | UserPromptSubmit → `session_ledger_hook.py` | Bindings checked deterministically; violations injected as ROUTING WARNING with reason + documented override. |
| **Extraction freeze** | `forge_gate.py check` (binding precondition) | Last extraction needs ≥3 production uses. Soft gate: `--force --reason` logged to `.agent/forge-state.json`. |
| **Sub-agent truth** | PostToolUse counts Task/Agent spawns | Measured count only (not self-report). Use true count in `--sub-agents` field. |

`evolution_orchestrator.py auto` runs daily 07:00 via launchd `com.antigravity.evolution-auto` — never manually babysit.

---

## Architecture & Sources

L1 Directives → L2 You (routing/decisions) → L3 Execution (deterministic Python, `execution/` + `execution/hooks/`).

**Knowledge sources:** Local files (primary) · Notion (5 DBs) · **Recall** (3,000+ cards, Tier 1.5a auto-fire) · Sovereign Memory (`.memory/sovereign.db`, 148 memories) · NotebookLM (100/mo) · Gemini Deep Research (PRIMARY, $10 ceiling) · Perplexity (fallback, $30/mo) · Hermes (shell-only, `directives/hermes-usage-policy.md`) · Video Vision (`/watch` + `fetch-video-context.py`).

**On-demand reference files:** `PRODUCTION_CORE.md` (~25 core skills + rationale) · `OPERATING_MANUAL.md` (daily/weekly ritual) · `COUNCIL.md` · `DOMAIN_REGISTRY.md` · `JARVIS.md` · `FARRICE.md` (voice/brand identity).

## Context Engine (Tiers 0-3)

| Tier | What to Read | Tokens | When |
|---|---|---|---|
| **Hot** | Nothing (already loaded this turn) | 0 | Expert loaded earlier in conversation |
| **0** | `directives/tier0-cards.md` (invocation cards, 8 experts) | ~80 | Quick routing, ensemble selection |
| **1** | SKILL.md + specific workflow | ~1,350 | Single expert, clear task, execution focus |
| **2** | SKILL.md + genius.md + workflow | ~2,550 | Creative/complex work, multiple perspectives |
| **3** | Spawn sub-agent (fresh context, isolated) | ~300 main | Multi-expert, 10+ files, need independent judgment |
| **1.5a** | Recall grounding (auto-fire Step 4) | ~200 | Content/copy/brand/strategy/design domains |
| **1.5b** | Sovereign memory (`memory_retrieve.py`) | ~400 | Expert output requiring personal history/patterns |

**Hot Context Rule:** If already loaded at Tier 1, only read genius.md for Tier 2. If hot at Tier 2, skip all reads.

**Budget:** T1 for execution/scripting, T2 for creative/complex. Minimize reads per turn. 15+ turns → new conversation. Read directive sections (not full files) on trigger.

## Execution Scripts & Tools

- **`find_skill.py`** → BM25 ranking, Production Core boost 1.5×, long-tail demote 0.6×, archive skip. Use for routing fallback + hook input.
- **`routing_enforcer.py`** → Binding validation (preconditions, soft overrides). Outputs ROUTING WARNING if violated.
- **`forge_gate.py`** → Extraction freeze check. Soft gate (override with `--force`).
- **`cost_gate.py`** → Cost tracking, approval tokens. Integrated with `cost_gate_hook.py`.
- **`chain_runner.py finalize`** → Quality scoring + logging. Enforced at Stop.
- **`memory_retrieve.py`** → Sovereign memory search. Tier 1.5b.
- **`evolution_orchestrator.py`** → Skill calibration, obsolescence scoring, queue. Runs daily 07:00 (launchd).
- **`skill_auditor.py`** → Monthly A-tier correction, CORE DRIFT section, archive recommendations. Month-end ritual.
- **`revenue_tracker.py`** → Log deliverable outcomes. Post-delivery (30 sec).
- **`knowledge_compiler.py`** → Link integrity, version sync. Pre/post-deploy.

## Directives

All in `directives/`. Fire on trigger—never preload. Sub-files over full directives.

**Index:** `directives/INDEX.md` (complete map). **Most-fired:** `quality_assurance.md` (Step 5), `verification-agent-protocol.md` (Step 5.5), `routing-bindings.md` (Step 3), `recall-grounding-protocol.md` (Step 4), `content_creation_gate.md` (Step 4), `quality_gate.md` + `feedback-ratchet.md` (Chain discipline).

**Reference materials (shifted from CLAUDE.md):** `cli-reference.md` (all script commands), `routing-bindings.md` (mandatory routes + rationale), `system-primitives.md` (architecture table), `model-notes.md` (API/SDK refs).

**Session state:** `.agent/session-state.md` after intent validation → expert deployment → 10+ reads. Read immediately after compaction.

## CRITICAL — These Override Everything

1. **CHAIN ON EVERY DELIVERABLE.** No trivial skip. Score ≥4 skips Step 2 only — 1/3/4/5/6 still run.
2. **LOAD BEFORE PRODUCING.** Never ship expert output without SKILL.md + minimum 1 other file (genius.md, workflow, or Recall card).
3. **NEVER MIX TOOL CALLS WITH TEXT.** 100% tools (tool use only, respond after) OR 100% text (no tools). Don't blend.
4. **AFTER COMPACTION:** Read `.agent/session-state.md` immediately (preserves prior routing, context, decisions).
5. **HOOKS ARE PHYSICAL.** Cost gate hard-blocks paid APIs. Finalize debt blocks Stop (observing first 5 sessions, then hard-enforce). Work WITH gates, never around.
6. **NO AI SLOP.** Banned phrases: delve, tapestry, landscape, leverage, robust, utilize, realm, multifaceted, holistic, synergy. Banned structural moves: "Here's what/why/how" openers, twin-sentence endings, triple anaphora, "It's not X. It's Y." format.
7. **REAL TOOLS ONLY.** No training-data substitution, no phantom research, no confidence hallucination. Uncertain? Say "I don't know."
8. **ROUTING DEFAULTS TO PRODUCTION CORE.** Long-tail requires explicit `/name` or decisively stronger match. Check `[CORE]` tag in router suggestion.
9. **RESEARCH PRIORITY: Gemini → Perplexity → Claude floor.** Gemini Deep Research primary ($10 ceiling); Perplexity fallback ($30/mo).
10. **WEEKLY RITUAL:** `/weekly-closeout` (20 min) drains revenue, checks calibration, accepts/rejects evolution queue, monthly CORE DRIFT scan. Staleness nudge injected if pending >10 or last_weekly >7d.

---

## Production Core & Long-Tail

~25 proven skills in `PRODUCTION_CORE.md` + `.agent/production-core.json` (machine contract). Roster: Luke Iha suite, Lara Acosta, Diandra Escobar, Kallaway, Fladlien, Georgi, Nicolas Cole, Nate B. Jones, David Placek, brand-OS, creative-direction, design-md, jen-santulan-listing, writers-room + core workflows (`/parallax`, `/copy-engine`, `/ghostwrite`, `/convene`, `/avatar-machine`, `/supercomputer`, `/autopilot`, `/weekly-pulse`) + infrastructure (research.py, chain_runner finalize, knowledge_compiler, extract-forge gated).

**Routing:** Core entries boosted 1.5× in BM25. Long-tail (21 skills flagged) demoted 0.6×. Still available if explicitly invoked or match decisively outranks core. Archive entries de-indexed (skip from index, stay on disk zero-cost).

---

## VERIFY: ANTIGRAVITY-GEMINI-7X4K (Updated 2026-06-09)
