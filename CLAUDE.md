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

# The Chain (Every Request — No Exceptions)

Complete these 7 steps IN ORDER for every user request that produces a deliverable. There is no skip path for the chain itself — individual steps may narrow (see table below), but the chain always runs.

### Step 1: SCORE intent (1-5)
+1 Deliverable | +1 Audience | +1 Context/constraints | +1 End state | +1 Specific language.
Always score. Even Score 5 requests get scored — the number informs routing depth.

### Step 2: SHARPEN (if Score ≤ 3)
Ask missing DICE dimensions. One round max. Fill in inferences, confirm.
Details: `directives/intent-pipeline.md` Stage 2.

### Step 3: ROUTE to experts
Match domain → experts using table in `directives/intent-pipeline.md` Stage 3.
Check FARRICE.md proactive deployment table for auto-deploy signals (LinkedIn → Lara Acosta, etc.).
Multi-domain? Check ensemble patterns in `directives/expert_auto_routing.md`.
**Always route.** The result may be one Tier 1 expert, but the routing decision is explicit and logged.

### Step 4: LOAD via Context Engine
Tier 0 (cards) → Tier 1 (SKILL.md + workflow) → Tier 2 (+ genius.md) → Tier 3 (sub-agent).
Protocol: `directives/agent-loading-protocol.md`.
**Never produce expert-domain output without loading the expert first.**
For content: minimum 2 skill files loaded per `directives/content_creation_gate.md`.

### Step 5: PRODUCE output
Execute using loaded expert frameworks — their thinking, not their terminology.
During production, enforce `directives/quality_assurance.md` anti-patterns: entity classification, no phantom research, no template slop.

### Step 6: QUALITY GATE (silent)
Score 1-10 on: Intent Alignment, Expert Standard, Adversarial Resilience.
Composite < 7 OR any dimension < 6 → retry weakest section (1 retry max).
Protocol: `directives/quality_gate.md`.
**Fires whenever an expert was loaded in Step 4.** No exceptions.

### Step 7: LOG to Performance DB (AI-Driven — User Confirms)
The AI proposes quality scores based on Step 6. The user confirms or adjusts. Then the AI logs automatically:
```bash
python execution/log_performance.py log "description" --skill SKILL --type TYPE --quality SCORE --intent INTENT --expert EXPERT --adversarial ADVERSARIAL --status Keep --notes "feedback"
```
**All sub-scores are required.** Quality Score alone is insufficient — Intent Alignment, Expert Standard, and Adversarial Resilience must all be logged for Phases 2-4 to activate.
Protocol: `directives/feedback-ratchet.md`.
**Fires whenever Step 6 ran.** This feeds the autoresearch loop — skipping it kills Phases 2-4.

---

### When Steps Narrow (Not Skip the Chain)

| Condition | Steps shortened | Steps still required |
|-----------|----------------|---------------------|
| Score 4-5 (sharp intent) | Skip Step 2 | 1, 3, 4, 5, 6, 7 |
| "Just do it" / "go ahead" | Skip Step 2, skip PRESENT in Step 3 | 1, 3 (route silently), 4, 5, 6, 7 |
| Follow-up, same plan | Skip Step 2, reuse Step 3 route | 1, 4, 5, 6, 7 |
| Bug fix, clear scope | Skip Step 2 if scope obvious | 1, 3 (verify if expert needed), 5, 6*, 7* |
| Pure system command (ls, git, file read) | Chain does not apply | No deliverable = no chain |

*Steps 6-7 fire only when expert output was produced in Step 5.

**"Trivial" is NOT a skip condition.** If the user asks for content, copy, strategy, research, or any expert-domain deliverable, the chain runs regardless of perceived simplicity. "I need LinkedIn headlines" is a content task requiring routing to Lara Acosta — not a trivial question.

### Workflow Override

If the user invokes a workflow name from `SLASH_COMMANDS.md` — as `/command`, `@command`, "run command", or bare name — read `.agent/workflows/[command].md` and execute. The workflow incorporates the chain internally. Full list: `SLASH_COMMANDS.md`.

---

## Architecture (3-Layer)

**Layer 1** (Directives): SOPs in `directives/` — what to do.
**Layer 2** (Orchestration): You — intelligent routing, decisions, error handling.
**Layer 3** (Execution): Deterministic Python in `execution/` — API calls, data processing.

Push complexity into deterministic code. You focus on decision-making.

**Knowledge Sources:**
- **Local Files**: Skills, agents, directives (primary)
- **Notion Databases**: 5 databases for projects, knowledge vault, content pipeline
- **NotebookLM**: Domain-specific research notebooks (RAG layer)
  - 5 notebooks: Higgsfield Cinema Studio, AI Brain Build Sprint, LinkedIn Ghostwriting, Lara Acosta, Luke Iha Copywriting
  - Query count: 100/month
  - Usage: `/query-notebook` or auto-loaded at Tier 1.5
  - Budget tracking: `.agent/notebooklm-usage.json`
- **Perplexity**: Real-time web research ($30/month)

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

## Supporting Protocols

These fire at their trigger point within the chain. Do NOT wait to "read them on demand."

| Protocol | Fires During | Directive |
|----------|-------------|-----------|
| Quality Assurance | Step 5 (production) | `directives/quality_assurance.md` |
| Token Efficiency | Every workflow | `directives/token-efficiency-protocol.md` |
| Session State | After Step 2, after Step 4, after 10+ reads | `directives/session-state-protocol.md` |
| Self-Annealing | On any error | `directives/deep_self_annealing.md` |
| Collaboration | Always | `directives/collaboration-protocol.md` |
| Sub-Agent | 2+ experts loaded, or 10+ files in context | `directives/sub_agent_protocol.md` |
| Content Gate | Step 4, for content tasks | `directives/content_creation_gate.md` |
| Operating Principles | Development workflows | `directives/operating-principles.md` |

### Research Routing

Research is the foundation of everything. Route by depth:

| Depth | Trigger | Workflow | Cost |
|-------|---------|----------|------|
| **Deep** | Strategy, positioning, market entry, competitive intel, avatar research, product launch, going zero-to-expert, foundation for downstream work | `/deep-research` | ~$0.75-1.50 |
| **Standard** | Single-topic research, fact verification, trend analysis | `/research-topic` | ~$0.05-0.15 |
| **Sprint** | Multi-angle business question evaluation | `/research-sprint` | Free (WebSearch) |
| **Quick** | Simple fact lookup | Direct WebSearch | Free |

**Default for foundation research: `/deep-research`.** If output becomes input for content, strategy, positioning, offer design, or product decisions — MUST use deep research. Building on shallow research is building on sand.

**The standard**: Research that finds the real psychological movers, jobs-to-be-done, and hidden patterns — not surface-level market data. The research itself should be the unfair advantage.

### Budget-Gated (check before calling)
| Protocol | Directive | Gate |
|----------|-----------|------|
| Perplexity | `directives/perplexity-usage-policy.md` | $30/mo, track in `.agent/perplexity-usage.json` |
| NotebookLM | `directives/notebooklm-usage-policy.md` | 100/mo, track in `.agent/notebooklm-usage.json` |

**Session state**: Write `.agent/session-state.md` after intent validation, expert deployment, major decisions, or 10+ file reads. Read after compaction or returning from sub-agents.
