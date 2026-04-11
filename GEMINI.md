# GEMINI.md — Antigravity System

## Environment
- `.env` at root = `NOTION_API_KEY`
- Python deps: `python-dotenv`, `requests` (no requirements.txt)
- **Notion:** Always `execution/notion_api.py` (pins `Notion-Version: 2022-06-28`). Never JS client. DB schemas: `directives/notion-databases.md`.
- Scripts from project root. Check `execution/` before creating new ones.
- Directory/file details: `directives/gemini-reference.md`

## Directories
- `skills/[name]/`: `SKILL.md` + `genius.md` + `workflows/*.md`
- `agents/[name]/`: `AGENT.md` + `memory/`; framework: `agents/_framework/`
- `.agent/workflows/`: `/command` → reads `.agent/workflows/[command].md`
- `execution/` scripts | `directives/` SOPs | `extractions/` per-expert | `knowledge/` base
- `councils/` | `research_outputs/` | `strategy_briefs/` | `deliverables/` | `.tmp/` (never commit)

## Artifact-First (HARD RULE)
Every user-facing deliverable → conversation artifact (`brain/<id>/`, `IsArtifact: true`). Workspace copy optional. Alert boxes + tables for premium formatting. Exception: system files only.

---

## The Chain — Every Deliverable, No Exceptions

**Step 1 SCORE** (1-5): +1 Deliverable +1 Audience +1 Context +1 End-state +1 Specificity. Print score.
**Step 2 SHARPEN** (if ≤3): Ask DICE dimensions, one round. `directives/intent-pipeline.md`. Skip if ≥4.
**Step 3 ROUTE**: `python3 execution/expert_router.py route "problem description"` → selects from 96 agents across 15 domains. Compounds: `python3 execution/expert_router.py compounds "query"`. Fallback: `DOMAIN_REGISTRY.md`. Always route explicitly. Print expert.
**Step 4 LOAD**: Tier 0→1→2→3. Hot? Skip. Content: min 2 files per `directives/content_creation_gate.md`. **Never produce without loading.** Print files loaded.
**Step 5 PRODUCE**: Expert frameworks, not terminology. Tool calls in one response, text in the next — NEVER mix. Enforce `directives/quality_assurance.md`.
**Step 6 FINALIZE**: Score Intent/Expert/Adversarial 1-10. Run:
```bash
python3 execution/chain_runner.py finalize "[output]" \
    --expert X --skill X --workflow X --type X \
    --intent X --expert-score X --adversarial X --notes "X"
```
Composite <7 or any <6 → retry weakest. Non-negotiable. FINALIZE for expert output only.

**Narrowing:** Score ≥4 skip Step 2. "Just do it" route silently. Follow-up reuse route. No deliverable = no chain. System commands skip chain. Start Tier 1, escalate for creative/complex.

---

## Architecture
**L1** Directives → **L2** You (routing/decisions) → **L3** Execution (Python). Push complexity into code.

**Sources:** Local files | Notion (5 DBs) | NotebookLM (5 notebooks, 100/mo, `/query-notebook`) | Perplexity
**On-demand:** `COUNCIL.md` (experts), `DOMAIN_REGISTRY.md` (routing), `JARVIS.md` (invocation), `FARRICE.md` (voice)

## Context Engine
Hot (0) → Tier 0 (cards, ~80) → Tier 1 (SKILL.md+workflow, ~1350) → Tier 2 (+genius.md, ~2550) → Tier 3 (sub-agent, ~300). Hot first. Hot@T1 needing T2: only read genius.md. Never re-read SKILL.md for same expert.

**Context Budget Rules:**
- Every file read compounds: re-sent on EVERY subsequent turn. Minimize reads.
- Prefer Tier 1 for execution tasks. Tier 2 only for creative/complex work.
- After 15+ turns, suggest new conversation to reset accumulation.
- Route workflows via `python3 execution/workflow_router.py search "query"` — don't scan the full listing.
- Read only the sections of directives you need, not entire files.

## Directives
All in `directives/`. Fire at trigger — don't preload. Key directives have modular sub-files:
- QA: `directives/qa/anti_patterns.md` (anti-patterns only) | `directives/qa/mandates.md` (mandates only) | Full: `directives/quality_assurance.md`
- Other: `quality_gate.md`, `content_creation_gate.md`, `agent-loading-protocol.md`, `intent-pipeline.md`, `session-state-protocol.md`
- **Prefer loading sub-files over full directives.** Load the full file only when you need all sections.
Session state: `.agent/session-state.md` after intent/deployment/decisions/10+ reads. Read after compaction.

## CRITICAL — These Override Everything

1. **CHAIN RUNS ON EVERY DELIVERABLE.** No skip for "trivial."
2. **LOAD EXPERT BEFORE PRODUCING.** No expert output without reading SKILL.md first.
3. **NEVER MIX TOOL CALLS WITH TEXT.** Response = 100% tools OR 100% text.
4. **AFTER COMPACTION:** Read `.agent/session-state.md` IMMEDIATELY.
5. **NO AI SLOP.** Banned: delve, tapestry, landscape, leverage, robust, utilize, realm, multifaceted, holistic, synergy.
6. **USE REAL TOOLS.** No training-data substitution. Phantom research = automatic failure.

## VERIFY: ANTIGRAVITY-GEMINI-7X4K
