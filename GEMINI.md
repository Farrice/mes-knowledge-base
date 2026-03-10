# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

<!-- Mirrored: CLAUDE.md, AGENTS.md, and GEMINI.md must stay identical. Edit one → update all three. -->

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

## Directory Conventions

- **Skills** (`skills/[name]/`): `SKILL.md` + `genius.md` + `workflows/*.md` (completion engine format)
- **Agents** (`agents/[name]/`): `AGENT.md` + `memory/` directory
- **Agent framework** (`agents/_framework/`): `invocation-cards.md`, `AGENT_TEMPLATE.md`, `orchestrator.md`
- **Workflows** (`.agent/workflows/`): Workflow implementations — invoked via `/extract`, `@extract`, "run extract", or bare name. System reads `.agent/workflows/extract.md`

## File Organization

- `.tmp/` — intermediates (never commit)
- `execution/` — deterministic Python scripts (API calls, data processing)
- `directives/` — SOPs and protocols
- `extractions/` — raw extraction reports and transcripts (per expert)
- `knowledge/` — organized knowledge base (books, frameworks, MES 3.0)
- `councils/` — council configurations (ai, brand, content, creative, revenue)
- `research_outputs/` — research project outputs
- `strategy_briefs/` — McKinsey-grade strategic dossiers
- `deliverables/` — client/project deliverables
- `products/` — product builds (e.g., PromptBase)
- `projects/` — active project workspaces
- Deliverables → cloud services (Google Sheets/Slides)

---

# Agent Instructions

> **MANDATORY FIRST ACTION — EVERY NEW REQUEST (NO EXCEPTIONS)**
>
> **Stage 1 — SCORE** intent sharpness 1-5:
> Has deliverable? (+1) | Audience? (+1) | Context/constraints? (+1) | End state? (+1) | Specific language? (+1)
>
> **Stage 2 — SHARPEN** (if Score ≤ 3):
> Ask missing DICE dimensions only (Deliverable, Intended audience, Context, End state). One round max.
> If Score 1-2 and multiple interpretations exist, present 2-3 options.
> Fill in what you can infer, confirm: "Here's what I heard — is this right?"
>
> **Stage 3 — ROUTE** (Score 4+):
> Match domain → experts using table in `directives/intent-pipeline.md`. Multi-domain? Check ensemble patterns in `directives/expert_auto_routing.md`.
> Load experts via Context Engine (Tier 0 cards → Tier 1 skill → Tier 2 genius → Tier 3 sub-agent).
>
> **Stage 4 — PRESENT** (complex/multi-step only):
> Show expert recommendation, await confirmation. Skip for simple tasks, follow-ups, or "just do it."
>
> **Workflow invoked?** If the user references a workflow name from `SLASH_COMMANDS.md` — whether as `/command`, `@command`, "run command", or the bare name — read `.agent/workflows/[command].md` and execute. Full list: `SLASH_COMMANDS.md`.
> **Skip pipeline for:** trivial questions, follow-ups within approved plan, "just do it", bug fixes.
> **Full pipeline details:** `directives/intent-pipeline.md`

---

## Architecture (3-Layer)

**Layer 1** (Directives): SOPs in `directives/` — what to do.
**Layer 2** (Orchestration): You — intelligent routing, decisions, error handling.
**Layer 3** (Execution): Deterministic Python in `execution/` — API calls, data processing.

Push complexity into deterministic code. You focus on decision-making.

**Key files (read on-demand, not preloaded):**
- `COUNCIL.md` — 24 experts + 5 standing councils. Read for expert selection.
- `DOMAIN_REGISTRY.md` — Expert swim lanes + compound pairing. Read for routing.
- `JARVIS.md` — Expert invocation protocol. Read for multi-expert workflows.
- `FARRICE.md` — Personal context, identity, voice. Read for content/brand work.

---

## Context Engine

**Tiered loading chain — always start at Tier 0, escalate only when needed.**

| Tier | What to Read | Token Cost | When |
|------|-------------|-----------|------|
| **0 — Card** | `agents/_framework/invocation-cards.md` | ~80 | Routing, ensemble selection |
| **1 — Standard** | SKILL.md + specific workflow | ~1,350 | Single expert, clear task |
| **2 — Deep** | SKILL.md + genius.md + workflow | ~2,550 | Creative/complex work |
| **3 — Sub-Agent** | Spawn sub-agent (fresh context) | ~300 main | Multi-expert, 10+ files loaded |

**Never rely on general training when expert skills exist.** Route via invocation cards first. Routing: `DOMAIN_REGISTRY.md` + `directives/expert_auto_routing.md`. Full protocol: `directives/agent-loading-protocol.md`.

---

## Core Protocols (Read On-Demand)

| Protocol | Directive | Fires When |
|----------|-----------|------------|
| Intent Pipeline | `directives/intent-pipeline.md` | Every new request |
| Quality Gate | `directives/quality_gate.md` | After expert-driven output (silent 3-point check, 1 retry max) |
| Quality Assurance | `directives/quality_assurance.md` | Every output (anti-pattern checks) |
| Self-Annealing | `directives/deep_self_annealing.md` | On any error (Tier 1/2/3 recovery) |
| Token Efficiency | `directives/token-efficiency-protocol.md` | Every workflow |
| Session State | `directives/session-state-protocol.md` | After major decisions, before compaction |
| Sub-Agent | `directives/sub_agent_protocol.md` | Multi-expert work, 10+ files loaded |
| Collaboration | `directives/collaboration-protocol.md` | Always (push back once, then execute) |
| Operating Principles | `directives/operating-principles.md` | Development workflows |
| Perplexity Budget | `directives/perplexity-usage-policy.md` | Before any research call ($10/mo) |

**Session state**: Write `.agent/session-state.md` after intent validation, expert deployment, major decisions, or 10+ file reads. Read after compaction or returning from sub-agents.

**Perplexity**: $10/month. Track in `.agent/perplexity-usage.json`. Sonar default; Deep Research for critical only.

---

## Mandatory Post-Output Actions

After producing ANY deliverable using an expert skill or workflow:

1. **Quality Gate** — Run silent 3-point check (Intent Alignment, Expert Standard, Adversarial Resilience). Score each 1-10. Protocol: `directives/quality_gate.md`
2. **Performance Log** — Log the quality scores:
   ```bash
   python execution/log_performance.py log "description" --skill SKILL_NAME --type TYPE --quality SCORE --status Keep
   ```

These actions feed the autoresearch feedback loop. Skipping them means Phases 2-4 (Skill Evolution, Cross-Pollination, Gap Detection) cannot activate.

**Skip for**: trivial questions, follow-up adjustments, debugging, file operations, system commands.
