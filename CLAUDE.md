<!--
Copyright © 2025-2026 Farrice Cain
Antigravity AI System - Proprietary and Confidential
Unauthorized reproduction, distribution, or modification prohibited
See LICENSE.md for details
-->

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

<!-- CLAUDE.md and AGENTS.md share identical format. GEMINI.md is Gemini-native (same intent, different format). When system intent changes here, run /sync-instructions to update GEMINI.md. -->

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

### Calibration & Quality Tools (Added 2026-04-03)

```bash
python execution/ground_truth.py gap-report          # Expert benchmark coverage
python execution/ground_truth.py compare <domain> <ai_output>  # Blind comparison
python execution/ground_truth.py add <domain> <file> --expert <name>  # Add sample
python execution/revenue_tracker.py pipeline          # Deliverables needing outcome data
python execution/revenue_tracker.py log "deliverable" --revenue 500 --outcome "result"
python execution/revenue_tracker.py report            # ROI by skill/expert
python execution/prose_classifier.py check <file>     # AI-prose detection
python execution/prose_classifier.py scan deliverables/  # Batch scan
```

**Ground Truth** (`knowledge/expert-benchmarks/`): Real expert output samples for blind comparison. 7 domains, 16 experts registered. Feeds calibration data into the feedback ratchet.
**Revenue Tracker** (`.agent/revenue-outcomes.json`): Connects quality scores to business outcomes. Pipeline command shows what needs tracking.
**Prose Classifier**: Integrated into `chain_runner.py` — warns if Expert Standard may be inflated due to AI-prose patterns.

### Knowledge Compiler (Added 2026-04-06)

```bash
python execution/knowledge_compiler.py stats             # Quick overview
python execution/knowledge_compiler.py full              # Full compilation (all stages)
python execution/knowledge_compiler.py briefing          # Session-start briefing
python execution/knowledge_compiler.py inventory         # Full manifest
python execution/knowledge_compiler.py stale             # Stale content (>30d)
python execution/knowledge_compiler.py overlap           # Overlapping files
```

**Knowledge Compiler** (`execution/knowledge_compiler.py`): Karpathy-inspired self-healing knowledge base. Scans `knowledge/`, `extractions/`, `research_outputs/` (217 files, 1.7M words). Generates manifest, session briefing, stale/overlap reports in `knowledge/compiled/`. Run monthly or after extraction sessions. Workflow: `/compile-knowledge`.

### Evolution Direction (Added 2026-04-06)

**Evolution Direction** (`directives/evolution-direction.md`): Karpathy's `program.md` analog — single source of truth for what to evolve, current priorities, constraints, stopping criteria. Read before every `/skill-evolution` run. Updated after every evolution cycle.

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

### Compressed Slash Command Convention (MANDATORY)

The slash command registration files at `.claude/commands/<name>.md` use a **compressed format**: they contain ONLY a brief description of what the command does. They do NOT contain execution instructions. The description is for routing/discovery — it tells you WHAT the command does, not HOW to run it.

When a user invokes `/<name>`:

1. The slash command file `.claude/commands/<name>.md` describes the command's purpose.
2. **You MUST then read `.agent/workflows/<name>.md`** — that file contains the actual workflow instructions.
3. **You MUST execute the workflow's instructions**, not respond to the description text.

This convention is non-negotiable. Slash command name maps 1:1 to workflow file name. If `.agent/workflows/<name>.md` does not exist for a slash command, surface that as an error rather than improvising — it indicates a missing or broken workflow that needs investigation.

Why this exists: the compressed format saves ~2,500 tokens per turn in system-prompt injection cost without losing any functionality. The previous format duplicated the "Read and execute the workflow at..." instruction in every single command file. This rule replaces that duplication.

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

## Supporting Protocols

These fire at their trigger point within the chain. Do NOT wait to "read them on demand."

| Protocol | Fires During | Directive |
|----------|-------------|-----------|
| Quality Assurance | Step 5 (production) | `directives/quality_assurance.md` |
| **Verification Agent** | **Step 5.5 (implementation tasks)** | **`directives/verification-agent-protocol.md`** |
| Token Efficiency | Every workflow | `directives/token-efficiency-protocol.md` |
| Session State | After Step 2, after Step 4, after 10+ reads | `directives/session-state-protocol.md` |
| Self-Annealing | On any error | `directives/deep_self_annealing.md` |
| Collaboration | Always | `directives/collaboration-protocol.md` |
| Sub-Agent | 2+ experts loaded, or 10+ files in context | `directives/sub_agent_protocol.md` |
| Content Gate | Step 4, for content tasks | `directives/content_creation_gate.md` |
| Operating Principles | Development workflows | `directives/operating-principles.md` |
| **Prose Classifier** | **Step 5.5 (before delivery)** | **`execution/prose_classifier.py` — auto-runs in `finalize()`** |
| **Ground Truth** | **After evolution cycles** | **`execution/ground_truth.py` — blind compare AI vs expert** |
| **Revenue Tracking** | **After client delivery** | **`execution/revenue_tracker.py` — connect quality to outcomes** |

### Budget-Gated (check before calling)
| Protocol | Directive | Gate |
|----------|-----------|------|
| Perplexity | `directives/perplexity-usage-policy.md` | $30/mo, track in `.agent/perplexity-usage.json` |
| NotebookLM | `directives/notebooklm-usage-policy.md` | 100/mo, track in `.agent/notebooklm-usage.json` |
| Apify | `directives/apify-usage-policy.md` | $29/mo Starter plan, track in `.agent/apify-usage.json`. Use for scraping/social listening; falls back to Perplexity at 90% cap |

**Session state**: Write `.agent/session-state.md` after intent validation, expert deployment, major decisions, or 10+ file reads. Read after compaction or returning from sub-agents.
