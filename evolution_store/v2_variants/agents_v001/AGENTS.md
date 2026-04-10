# AGENTS.md — Antigravity System Harness

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Environment Setup

- **`.env` at project root** with `NOTION_API_KEY` — required for all Notion operations
- Python deps: `python-dotenv`, `requests` (no requirements.txt; install manually)
- No build step, no test suite — this is an AI orchestration system, not a traditional app

## Notion API — Critical Version Pin

`@notionhq/client` v5.9.0 uses a newer API that returns `data_sources` instead of `properties`. Schema updates silently succeed but don't persist; row inserts fail.

**Always use `execution/notion_api.py`** (pins `Notion-Version: 2022-06-28`). Never use the JS client. Database IDs and schemas: `directives/notion-databases.md`.

## Running Execution Scripts

All from project root. Check `execution/` for existing tools before creating new ones.

```bash
python execution/notion_api.py query <database_id>
python execution/notion_api.py capture "Title" "Body" --type Task --tags Revenue,Urgent
python execution/parallel_swarm.py "objective"       # --grounded, --research
python execution/generate_image.py "prompt"
python execution/skill_converter.py
python execution/sync_registries.py
```

---

## Directory & File Conventions

- **Skills** (`skills/[name]/`): `SKILL.md` + `genius.md` + `workflows/*.md`
- **Agents** (`agents/[name]/`): `AGENT.md` + `memory/`; framework in `agents/_framework/`
- **Workflows** (`.agent/workflows/`): Invoked via `/command`, `@command`, or bare name
- `execution/` — deterministic Python scripts | `directives/` — SOPs and protocols
- `extractions/` — raw reports per expert | `knowledge/` — organized knowledge base
- `councils/` — council configs | `research_outputs/` / `strategy_briefs/` / `deliverables/` — outputs
- `.tmp/` — intermediates (never commit)

## Artifact-First Delivery Rule (HARD RULE)

Every user-facing deliverable MUST be published as a **conversation artifact** (`brain/<conversation-id>/` with `IsArtifact: true`). A workspace copy may also be saved for persistence. Use alert boxes, blockquotes, tables for premium formatting. **Never deliver as only a workspace file.** Exception: pure system files (`.py`, `.json`, configs).

---

# The Chain (Every Deliverable — No Exceptions)

**Step 1 SCORE** (1-5): +1 Deliverable +1 Audience +1 Context +1 End-state +1 Specificity.
**Step 2 SHARPEN** (if ≤3): Ask missing DICE dimensions. One round max. Details: `directives/intent-pipeline.md`.
**Step 3 ROUTE**: Domain→expert. Known: LinkedIn→Lara, Copy→Luke, SEO→Gotch, Brand→Oren/Grace, Ghost→Cole, Psychology→Kallaway, Consumer→Dai, Agentic→Saraev. Multi-domain: `directives/expert_auto_routing.md`. Always route — the decision is explicit.
**Step 4 LOAD**: Tier 0 (cards) → Tier 1 (SKILL.md + workflow) → Tier 2 (+ genius.md) → Tier 3 (sub-agent). Hot expert? Skip reads. Content: min 2 skill files per `directives/content_creation_gate.md`. **Never produce without loading.**
**Step 5 PRODUCE**: Execute using loaded expert frameworks — their thinking, not terminology. Enforce `directives/quality_assurance.md`: entity classification, no phantom research, no template slop.
**Step 6 FINALIZE**: Score Intent/Expert/Adversarial 1-10 each. Run:
```bash
python3 execution/chain_runner.py finalize "[what you produced]" \
    --expert [name] --skill [skill-dir] --workflow [name] \
    --type [Content|Strategy|Research|Extraction|Client Work|System|Creative|Analysis] \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "[what worked, what didn't]"
```
**Composite <7 or any dimension <6**: Retry weakest section, re-finalize. Non-negotiable — feeds the autoresearch loop.

### Narrowing Rules
- Score 4-5: Skip Step 2. "Just do it": Route silently. Follow-up: Reuse route. No deliverable: Chain does not apply.
- **"Trivial" is NOT a skip condition.** Content/strategy/research always runs the chain.
- Start Tier 1. Escalate to genius.md for creative/complex or quality misses. FINALIZE fires only for expert output.

### Workflow Override
`/command`, `@command`, or bare name → read `.agent/workflows/[command].md` and execute.

---

## Architecture (3-Layer)

**L1** Directives (`directives/`) → **L2** You (routing, decisions) → **L3** Execution (`execution/` Python). Push complexity into deterministic code.

**Knowledge Sources:** Local files (primary) | Notion (5 databases) | NotebookLM (5 notebooks, 100/mo, `/query-notebook`) | Perplexity (web research)
**Key files** (on-demand): `COUNCIL.md` (24 experts), `DOMAIN_REGISTRY.md` (swim lanes), `JARVIS.md` (invocation), `FARRICE.md` (personal context/voice)

## Context Engine

**Hot** (already loaded, 0 tokens) → **Tier 0** (invocation-cards, ~80) → **Tier 1** (SKILL.md + workflow, ~1,350) → **Tier 2** (+ genius.md, ~2,550) → **Tier 3** (sub-agent, ~300 main). Check hot first. If hot at Tier 1 and need Tier 2, only read genius.md incrementally. Anti-pattern: re-reading SKILL.md for same expert twice.

## Directives

All SOPs in `directives/`. Fire at trigger point — do NOT preload. Key: `quality_assurance.md` (Step 5), `quality_gate.md` (after Step 5), `content_creation_gate.md` (Step 4), `agent-loading-protocol.md` (Step 4), `intent-pipeline.md` (Step 2-3), `session-state-protocol.md` (after major decisions).

**Session state**: Write `.agent/session-state.md` after intent validation, expert deployment, major decisions, or 10+ file reads. Read after compaction or returning from sub-agents.
