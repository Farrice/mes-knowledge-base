# AGENTS.md — Antigravity System Harness

Guidance for Claude Code working in this repository.

## Environment
- `.env` at root with `NOTION_API_KEY`
- Python deps: `python-dotenv`, `requests` (no requirements.txt)
- **Notion:** Always `execution/notion_api.py` (pins `Notion-Version: 2022-06-28`). Never JS client. DB schemas: `directives/notion-databases.md`.
- Run all scripts from project root. Check `execution/` before creating new ones.

## Directories
- `skills/[name]/`: `SKILL.md` + `genius.md` + `workflows/*.md`
- `agents/[name]/`: `AGENT.md` + `memory/`; framework: `agents/_framework/`
- `.agent/workflows/`: `/command` → reads `.agent/workflows/[command].md`
- `execution/` scripts | `directives/` SOPs | `extractions/` per-expert | `knowledge/` base
- `councils/` | `research_outputs/` | `strategy_briefs/` | `deliverables/` | `.tmp/` (never commit)

## Artifact-First (HARD RULE)
Every user-facing deliverable → conversation artifact (`brain/<id>/`, `IsArtifact: true`). Workspace copy optional. Alert boxes + tables for premium formatting. Exception: system files only.

---

# The Chain — Every Deliverable, No Exceptions

**Step 1 SCORE** (1-5): +1 Deliverable +1 Audience +1 Context +1 End-state +1 Specificity.
**Step 2 SHARPEN** (if ≤3): Ask DICE dimensions, one round. `directives/intent-pipeline.md`.
**Step 3 ROUTE**: LinkedIn→Lara | Copy→Luke | SEO→Gotch | Brand→Oren/Grace | Ghost→Cole | Psychology→Kallaway | Consumer→Dai | Agentic→Saraev. Multi-domain: `directives/expert_auto_routing.md`. Always route explicitly.
**Step 4 LOAD**: Tier 0→1→2→3. Hot? Skip. Content: min 2 files per `directives/content_creation_gate.md`. **Never produce without loading.**
**Step 5 PRODUCE**: Expert frameworks, not terminology. Enforce `directives/quality_assurance.md`.
**Step 6 FINALIZE**: Score Intent/Expert/Adversarial 1-10. Run:
```bash
python3 execution/chain_runner.py finalize "[output]" \
    --expert X --skill X --workflow X --type X \
    --intent X --expert-score X --adversarial X --notes "X"
```
Composite <7 or any <6 → retry weakest, re-finalize. Non-negotiable.

**Narrowing:** Score ≥4 skip Step 2. "Just do it" route silently. Follow-up reuse route. No deliverable = no chain. "Trivial" is NOT a skip. Start Tier 1, escalate for creative/complex. FINALIZE for expert output only.

---

## Architecture
**L1** Directives → **L2** You (routing/decisions) → **L3** Execution (Python). Push complexity into code.

**Sources:** Local files | Notion (5 DBs) | NotebookLM (5 notebooks, 100/mo, `/query-notebook`) | Perplexity
**On-demand:** `COUNCIL.md` (experts), `DOMAIN_REGISTRY.md` (routing), `JARVIS.md` (invocation), `FARRICE.md` (voice)

## Context Engine
Hot (0) → Tier 0 (cards, ~80) → Tier 1 (SKILL.md+workflow, ~1350) → Tier 2 (+genius.md, ~2550) → Tier 3 (sub-agent, ~300). Hot first. Hot@T1 needing T2: only read genius.md. Never re-read SKILL.md for same expert.

## Directives
All in `directives/`. Fire at trigger — don't preload. Key: `quality_assurance.md`, `quality_gate.md`, `content_creation_gate.md`, `agent-loading-protocol.md`, `intent-pipeline.md`, `session-state-protocol.md`.
Session state: `.agent/session-state.md` after intent/deployment/decisions/10+ reads. Read after compaction.
