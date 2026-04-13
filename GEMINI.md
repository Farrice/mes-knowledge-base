# GEMINI.md — Antigravity System

## Environment
- `.env` at root = `NOTION_API_KEY`
- Python deps: `python-dotenv`, `requests` (no requirements.txt)
- **Notion:** Always `execution/notion_api.py` (pins `Notion-Version: 2022-06-28`). Never JS client. DB schemas: `directives/notion-databases.md`.
- Scripts from project root. Check `execution/` before creating new.
- File map: `directives/gemini-reference.md`

## Directories
- `skills/[name]/`: `SKILL.md` + `genius.md` + `workflows/*.md`
- `agents/[name]/`: `AGENT.md` + `memory/`; framework: `agents/_framework/`
- `.agent/workflows/`: `/command` → reads `.agent/workflows/[command].md`
- `execution/` scripts | `directives/` SOPs | `extractions/` per-expert | `knowledge/` base
- `councils/` | `research_outputs/` | `strategy_briefs/` | `deliverables/` | `.tmp/` (never commit)

## Artifact-First (HARD RULE)
Every deliverable → artifact (`brain/<id>/`, `IsArtifact: true`). Workspace copy optional. Premium formatting (alerts+tables). Exception: system files.

---

## The Chain

1. **SCORE** (1-5): +1 Deliverable +1 Audience +1 Context +1 End-state +1 Specificity. Print.
2. **SHARPEN** (if ≤3): DICE dimensions, one round. Ref: `directives/intent-pipeline.md`.
3. **ROUTE**: `python3 execution/expert_router.py route "query"` → 96 agents/15 domains. Compounds: `compounds "query"`. Tool scope: `python3 execution/tool_router.py route "query"`. Fallback: `DOMAIN_REGISTRY.md`. Print expert + tool clusters.
4. **LOAD**: Semantic-first: `python3 execution/context_retriever.py search "query"` → top chunks. Fallback: Tier 0→1→2→3. Content: min 2 files per `directives/content_creation_gate.md`. Never produce unloaded. Print files.
5. **PRODUCE**: Expert frameworks, not terminology. Tools OR text per response—never both. Enforce `directives/quality_assurance.md`.
6. **FINALIZE**: Score Intent/Expert/Adversarial 1-10. `python3 execution/chain_runner.py finalize "[output]" --expert X --skill X --workflow X --type X --intent X --expert-score X --adversarial X --notes "X"` Composite<7 or any<6→retry. Expert output only.

**Skip:** Score ≥4→skip Step 2. "Just do it"→route silently. Follow-ups reuse route. No deliverable=no chain. System commands skip. Start Tier 1, escalate for creative/complex.

---

## Architecture
L1 Directives → L2 You (routing) → L3 Execution (Python). Push complexity into code.
Sources: Local | Notion (5 DBs) | NotebookLM (5 notebooks, 100/mo, `/query-notebook`) | Perplexity
On-demand: `COUNCIL.md` | `DOMAIN_REGISTRY.md` | `JARVIS.md` | `FARRICE.md` (voice)

## Context Engine
Semantic retrieval first: `context_retriever.py search "query"` → ranked chunks (~134 words avg). Full-file fallback: T0(cards,~80)→T1(SKILL.md+workflow,~1350)→T2(+genius.md,~2550)→T3(sub-agent,~300). Hot first. T1→T2: genius.md only. Never re-read SKILL.md same expert.
**T0:** `directives/tier0-cards.md` (8 experts). T0 for simple; T1 when frameworks needed.

**Budget:** Reads compound every turn—minimize. T1 for execution, T2 for creative/complex. 15+ turns→new conversation. Workflows: `python3 execution/workflow_router.py search "query"`. Read directive sections, not full files.

## Execution Tools
- **Expert Router:** `python3 execution/expert_router.py route|compounds "query"` — 96 agents, 15 domains
- **Tool Router:** `python3 execution/tool_router.py route|clusters|stats "query"` — dynamic tool selection, ~75% token reduction
- **Context Retriever:** `python3 execution/context_retriever.py search|index|stats "query"` — 3,239 chunks, TF-IDF retrieval
- **Memory Store:** `python3 execution/memory_store.py store|recall|search|decay|stats` — persistent cross-session memory with Ebbinghaus decay
- **Workflow Router:** `python3 execution/workflow_router.py search "query"` — 479 workflows

## Directives
All in `directives/`. Fire on trigger—never preload. Sub-files over full directives.
- QA: `qa/anti_patterns.md` | `qa/mandates.md` | Full: `quality_assurance.md`
- Other: `quality_gate.md`, `content_creation_gate.md`, `agent-loading-protocol.md`, `intent-pipeline.md`, `session-state-protocol.md`
Session state: `.agent/session-state.md` after intent/deployment/decisions/10+ reads. Read after compaction.

## CRITICAL — These Override Everything

1. **CHAIN ON EVERY DELIVERABLE.** No trivial skip.
2. **LOAD BEFORE PRODUCING.** No output without SKILL.md load.
3. **NEVER MIX TOOL CALLS WITH TEXT.** 100% tools OR 100% text.
4. **AFTER COMPACTION:** Read `.agent/session-state.md` immediately.
5. **NO AI SLOP.** Banned: delve, tapestry, landscape, leverage, robust, utilize, realm, multifaceted, holistic, synergy.
6. **REAL TOOLS ONLY.** No training-data substitution. Phantom research = failure.

## VERIFY: ANTIGRAVITY-GEMINI-7X4K
