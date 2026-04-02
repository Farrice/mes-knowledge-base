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

Complete these 6 steps IN ORDER for every user request that produces a deliverable. There is no skip path for the chain itself — individual steps may narrow (see table below), but the chain always runs.

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

### Step 6: FINALIZE (Quality Gate + Log + Protocol Tracking — Single Call)
After producing expert output, score it mentally on 3 dimensions (1-10 each):
- **Intent Alignment**: Does it match what the user actually asked for?
- **Expert Standard**: Would the real expert recognize this as quality work?
- **Adversarial Resilience**: Would it survive critical scrutiny?

Then run the chain finalize command — this handles EVERYTHING (quality gate, regression check, Notion performance log, protocol activation tracking, session state):
```bash
python3 execution/chain_runner.py finalize "[what you produced]" \
    --expert [expert-name] \
    --skill [skill-directory-name] \
    --workflow [workflow-name] \
    --type [Content|Strategy|Research|Extraction|Client Work|System|Creative|Analysis] \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "[what worked, what didn't]"
```
**If composite < 7 or any dimension < 6**: Retry the weakest section once, then re-finalize.
**This is non-negotiable.** Expert output without `finalize` is incomplete. This feeds the autoresearch loop — skipping it kills Phases 2-4.
Protocols: `directives/quality_gate.md`, `directives/feedback-ratchet.md`.

---

### When Steps Narrow (Not Skip the Chain)

| Condition | Steps shortened | Steps still required |
|-----------|----------------|---------------------|
| Score 4-5 (sharp intent) | Skip Step 2 | 1, 3, 4, 5, 6 |
| "Just do it" / "go ahead" | Skip Step 2, skip PRESENT in Step 3 | 1, 3 (route silently), 4, 5, 6 |
| Follow-up, same plan | Skip Step 2, reuse Step 3 route | 1, 4, 5, 6 |
| Bug fix, clear scope | Skip Step 2 if scope obvious | 1, 3 (verify if expert needed), 5, 6* |
| Pure system command (ls, git, file read) | Chain does not apply | No deliverable = no chain |

*Step 6 fires only when expert output was produced in Step 5.

**"Trivial" is NOT a skip condition.** If the user asks for content, copy, strategy, research, or any expert-domain deliverable, the chain runs regardless of perceived simplicity. "I need LinkedIn headlines" is a content task requiring routing to Lara Acosta — not a trivial question.

### Chain Efficiency Rules (Token Optimization)

**Steps 1-2 (SCORE + SHARPEN): Internalized — no file reads required.**
The scoring formula (+1 Deliverable, +1 Audience, +1 Context, +1 End state, +1 Specific language)
is memorized. Do NOT read `directives/intent-pipeline.md` to score intent.
Only read it if running `/validate-intent` explicitly.

**Step 3 (ROUTE): Internalized for known domains.**
If the domain maps to an obvious expert (LinkedIn → Lara Acosta, copywriting → Luke Iha,
SEO → Nathan Gotch, brand → Oren/Grace, ghostwriting → Nicolas Cole, content psychology → Kallaway,
consumer posture → Dai Media, agentic workflows → Nick Saraev), route without reading
`DOMAIN_REGISTRY.md` or `invocation-cards.md`. Only read routing files for ambiguous or multi-domain requests.

**Step 4 (LOAD): Deferred Tier escalation.**
Start at Tier 1 (SKILL.md only). Load genius.md ONLY if:
- The first-pass output doesn't meet quality expectations
- The task is explicitly creative/complex (screenwriting, brand strategy, deep extraction)
- The user asks for "the best" or "world-class" output

**Step 6 (FINALIZE): Required only for expert-domain output.**
Quick answers, system commands, file organization, and conversations do NOT require finalize.

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

**Tiered loading chain — check Hot first, then start at Tier 0, escalate only when needed.**

| Tier | What to Read | Token Cost | When |
|------|-------------|-----------|------|
| **Hot** | Nothing (already loaded) | 0 | Expert was loaded earlier this conversation |
| **0 — Card** | `agents/_framework/invocation-cards.md` | ~80 | Routing, ensemble selection |
| **1 — Standard** | SKILL.md + specific workflow | ~1,350 | Single expert, clear task |
| **2 — Deep** | SKILL.md + genius.md + workflow | ~2,550 | Creative/complex work |
| **3 — Sub-Agent** | Spawn sub-agent (fresh context) | ~300 main | Multi-expert, 10+ files loaded |

**Hot Context Rule**: Before loading any expert, check if they were already loaded this conversation. If hot at Tier 1 and Tier 2 is needed, only read genius.md (incremental). If hot at Tier 2, skip all reads. Anti-pattern: re-reading SKILL.md for the same expert twice in one conversation (~1,350 tokens wasted).

**Never rely on general training when expert skills exist.** Route via invocation cards first. Routing: `DOMAIN_REGISTRY.md` + `directives/expert_auto_routing.md`. Full protocol: `directives/agent-loading-protocol.md`.

---

## Directive Index

All SOPs live in `directives/`. Fire at their trigger point — do NOT preload.

### Chain Protocols (fire during the 6-step chain)
| Directive | When |
|-----------|------|
| `quality_assurance.md` | Step 5 — anti-patterns, entity classification, no phantom research |
| `quality_gate.md` | After Step 5 — silent self-annealing quality gate |
| `feedback-ratchet.md` | After Step 6 — logs quality scores for longitudinal tracking |
| `content_creation_gate.md` | Step 4 — pre-flight gate for content tasks (min 2 skill files) |
| `deep_self_annealing.md` | On any error — tiered recovery system |
| `ai-slop-detector.md` | Step 5 — prose-level pattern awareness for AI-shaped writing |
| `verification-agent-protocol.md` | Between Step 5-6 — adversarial verification for implementations |
| `collaboration-protocol.md` | Always — anti-sycophancy mandate |
| `operating-principles.md` | Development workflows |
| `user-state-awareness.md` | Every turn — lightweight frustration detection |

### Routing & Loading
| Directive | When |
|-----------|------|
| `intent-pipeline.md` | Step 2-3 — full DICE dimensions + routing tables |
| `agent-loading-protocol.md` | Step 4 — tiered loading chain (Hot → Tier 3) |
| `expert_auto_routing.md` | Step 3 — domain tables + ensemble patterns |
| `multi-expert-synthesis.md` | Multi-domain tasks — combining expert perspectives |
| `skill-paths-reference.md` | Quick lookup: expert → skill file paths |

### Research & Knowledge
| Directive | When |
|-----------|------|
| `research-protocol.md` | Research tasks — grounded intelligence standard |
| `hybrid-knowledge-retrieval.md` | Smart routing across all knowledge sources |
| `perplexity-usage-policy.md` | Budget: $30/mo, track in `.agent/perplexity-usage.json` |
| `notebooklm-usage-policy.md` | Budget: 100/mo, track in `.agent/notebooklm-usage.json` |

### Extraction & Skills
| Directive | When |
|-----------|------|
| `extraction-workflow.md` | Processing new expert extractions into agents/skills |
| `extraction-to-skill.md` | Converting MES 3.0 extractions into production skills |
| `mes-3.0-extract.md` | MES 3.0 extraction from source material |
| `mes-3.0-validate.md` | Validation: mechanical rubric + Oren CEV taste check |
| `skill-evolution-protocol.md` | 20+ Performance Log entries or regression — variant testing |
| `cross-pollination.md` | After a skill evolution KEEP — propagate to related skills |
| `expertise-gap-protocol.md` | No expert covers the task — self-healing knowledge loop |

### Session & System
| Directive | When |
|-----------|------|
| `session-state-protocol.md` | After Step 2, after Step 4, after 10+ reads |
| `session-end-commit.md` | End of session — commit protocol |
| `token-efficiency-protocol.md` | Every workflow — minimize context pollution |
| `sub_agent_protocol.md` | 2+ experts loaded, or 10+ files in context |
| `parallel_thought.md` | Complex/swarm-worthy tasks — parallel build orchestrator |
| `parallelism-cheat-sheet.md` | Quick reference for parallel execution patterns |
| `workflow-chains.md` | Multi-step workflows — output-to-input contracts |

### Domain-Specific
| Directive | When |
|-----------|------|
| `ghostwriting-delivery.md` | Any ghostwriting task — full delivery SOP |
| `sales-conversation.md` | Sales prep — Miner + Bernoff frameworks |
| `content-creation.md` | Content creation using expert council |
| `daily-council.md` | Morning routine — daily focus via expert council |
| `decision-council.md` | Major decisions — expert council framework |
| `notion-databases.md` | Notion API — database IDs, schemas, registry |

### Setup & Reference
| Directive | When |
|-----------|------|
| `mcp-server-setup.md` | MCP server setup — Workspace, Notion, SQLite |
| `mcp-research-setup.md` | MCP research setup — Perplexity Sonar + Tavily |
| `gemini-reference.md` | On-demand reference material stripped from GEMINI.md |

**Session state**: Write `.agent/session-state.md` after intent validation, expert deployment, major decisions, or 10+ file reads. Read after compaction or returning from sub-agents.
