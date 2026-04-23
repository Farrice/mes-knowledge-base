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

### Knowledge Compiler — Karpathy Wiki Engine (Updated 2026-04-13)

```bash
python execution/knowledge_compiler.py stats             # Quick overview
python execution/knowledge_compiler.py full              # Full compilation (all 6 stages)
python execution/knowledge_compiler.py briefing          # Session-start briefing
python execution/knowledge_compiler.py inventory         # Full manifest
python execution/knowledge_compiler.py index             # Living index (knowledge/index.md)
python execution/knowledge_compiler.py lint              # Full wiki health check
python execution/knowledge_compiler.py stale             # Stale content (>30d)
python execution/knowledge_compiler.py overlap           # Overlapping files
python execution/knowledge_compiler.py auto-archive      # Auto-archive stale (dry run)
python execution/knowledge_compiler.py auto-archive --execute  # Actually move files
python execution/knowledge_compiler.py log <action> "title" --domain X --expert Y
python execution/knowledge_compiler.py archive "query" result.md --domain X
```

**Knowledge Compiler** (`execution/knowledge_compiler.py`): Karpathy LLM Wiki engine. 240 files, 1.8M words across `knowledge/`, `extractions/`, `research_outputs/`. Three Karpathy operations: **ingest** (cascade updates via index + log), **query** (search write-back via archive), **lint** (contradictions, orphans, dead links, stale detection). Living index at `knowledge/index.md`, chronological log at `knowledge/log.md`. Compilation outputs in `knowledge/compiled/`. Reflection pass via `/reflect` generates second-order synthesis articles in `knowledge/synthesis/`.

**Notion Knowledge Vault Sync**: `python execution/notion_api.py vault-create "Title" --expert X --domain Y` — auto-triggered by `chain_runner.py finalize` for quality >= 7. Notion is pointer + metadata layer; files stay local.
**Autofill Config**: `directives/notion-autofill-guide.md` — step-by-step for Performance Log, Content Pipeline, Knowledge Vault AI autofill properties + Custom Agents setup.

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

> **Operating Principle** (from Reflection Pass): The Chain's 6 steps, tiered loading, quality gate, and evolution engine are complex BY DESIGN — but the OUTPUT should be simple. Complex process → simple result. All this machinery exists for ONE purpose: to find the single truth and deliver it through the right mechanism with the right proof at the right identity level (see `knowledge/synthesis/the-persuasion-stack.md`). If a session produces "comprehensive" output instead of "singular" output, the system failed regardless of quality score.

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
Tier 0 (cards) → **Tier 1.5 (Recall source grounding — automatic, silent)** → Tier 1 (SKILL.md + workflow) → Tier 2 (+ genius.md) → Tier 3 (sub-agent).
Protocol: `directives/agent-loading-protocol.md`.
**Never produce expert-domain output without loading the expert first.**
For content: minimum 2 skill files loaded per `directives/content_creation_gate.md`.
**Recall grounding (Tier 1.5):** For grounding-relevant domains (content, copy, brand, voice, storytelling, positioning, strategy, sales, marketing, persuasion, comms, creative), auto-fire `mcp__recall__search` before skill load. Inject 1-3 high-signal cards as source material. Silent skip if <2 cards or weak signal. Full protocol: `directives/recall-grounding-protocol.md`.

### Step 5: PRODUCE output
Execute using loaded expert frameworks — their thinking, not their terminology.
During production, enforce `directives/quality_assurance.md` anti-patterns: entity classification, no phantom research, no template slop.

### Step 5.5: VERIFY (Factual Grounding)
**Trigger**: Output contains any claim about real people (names, titles, companies), specific events/dates, statistics or metrics, technical facts (API behavior, library versions, syntax), market/industry claims, or source attributions. Does NOT fire for: pure creative writing, personal voice content, brainstorming lists, stylistic drafts, or opinion pieces without factual load.

Run verification per `directives/verification-agent-protocol.md`:
- **Implementation deliverables**: Run it, break it (adversarial checks)
- **Factual deliverables**: Claim inventory → source verification → confidence labeling (VERIFIED/LIKELY/UNCONFIRMED) → contradiction scan
- Verify BEFORE the user sees the document. Research → verify → compile → deliver. Not: compile → deliver → get caught → fix.
- If VERDICT: PASS → proceed to Step 6. If FAIL → re-research, re-verify before rewriting.

### Step 6: FINALIZE (Quality Gate + Log + Protocol Tracking — Single Call)
After producing expert output, score it mentally on 4 dimensions (1-10 each):
- **Intent Alignment**: Does it match what the user actually asked for?
- **Expert Standard**: Would the real expert recognize this as quality work?
- **Adversarial Resilience**: Would it survive critical scrutiny?
- **Factual Grounding**: Are real-world claims verified against primary sources? Unverifiable items flagged? Mark **N/A** for pure creative/opinion work with no factual claims (matches Step 5.5 trigger conditions); otherwise score 1-10.

Then run the chain finalize command — this handles EVERYTHING (quality gate, regression check, Notion performance log, protocol activation tracking, session state):
```bash
python3 execution/chain_runner.py finalize "[what you produced]" \
    --expert [expert-name] \
    --skill [skill-directory-name] \
    --workflow [workflow-name] \
    --type [Content|Strategy|Research|Extraction|Client Work|System|Creative|Analysis] \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "[what worked, what didn't] | Factual Grounding: [1-10] | Verification: [PASS/FAIL/PARTIAL/N/A]"
```
**If composite < 7 or any dimension < 6**: Retry the weakest section once, then re-finalize.
**Factual Grounding veto**: If Dimension 4 is scored (not marked N/A) and scores <6, delivery is blocked regardless of composite. A polished document with wrong facts is worse than a rough draft with right facts — because the user trusts the polish.
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

### Mandatory Workflow Routing (Domain → Workflow Bindings)

Some domains have dedicated production workflows. If the user's task matches the domain, deploy the bound workflow **even if the user names a different workflow in their prompt**. Override literal ask with correct routing.

| Domain signal | Mandatory workflow | Never substitute |
|---|---|---|
| Parallax Substack editions, "parallax edition", "next substack", parallax prompt packs | `/parallax` | `writers-room` (diagnostic-on-draft, not production-from-raw-take) |
| LinkedIn post production from scratch | `/ghostwrite` or Lara Acosta skill | `writers-room` (for refinement only) |
| Writers' room refinement of an existing draft | `writers-room` | `/parallax` or other production workflows |

**Why this exists**: A 2026-04-21 session degraded to 6/10 across 4 iterations on a Parallax edition because `writers-room` was invoked by the user's conversational ask and executed literally. `/parallax` was the correct workflow and was never loaded. Root cause captured in `/Users/farricecain/.claude/plans/additional-edits-this-line-fluffy-cake.md`. When user's conversational prompt and system's correct routing disagree, system wins and explains the override in one sentence.

**Phase 2.5 GROUND + ZEITGEIST CHECK is non-optional for Parallax Editions 02+.** After raw-take capture (Phase 2) and before drafting (Phase 3), `/parallax` runs claim extraction, budget-tiered verification (Recall → Perplexity), zeitgeist scan, and a halt/proceed gate. This exists because Edition 02 shipped with 7 fabrications that slipped past mechanical audits (Madeon as unknown DJ, wrong day, invented distance, song-age math, etc.). The only way to skip is an explicit `--no-ground` flag, which should only be used when the edition has zero external factual surface (pure memoir with no public figures, events, brands, or stats). Full protocol in `.agent/workflows/parallax.md` Phase 2.5.

---

## Architecture (3-Layer)

**Layer 1** (Directives): SOPs in `directives/` — what to do.
**Layer 2** (Orchestration): You — intelligent routing, decisions, error handling.
**Layer 3** (Execution): Deterministic Python in `execution/` — API calls, data processing.

Push complexity into deterministic code. You focus on decision-making.

**Knowledge Sources:**
- **Local Files**: Skills, agents, directives (primary)
- **Notion Databases**: 5 databases for projects, knowledge vault, content pipeline
- **Recall** (3,000+ saved cards — YouTube transcripts, articles, extractions): Auto-queried at Tier 1.5 for content/brand/voice/strategy work via `directives/recall-grounding-protocol.md`. Invisible infrastructure — no manual trigger needed. Tools: `mcp__recall__search`, `mcp__recall__get_document_content`, `mcp__recall__explore_kb`, `mcp__recall__filter_by_metadata`.
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
| **Verification Agent** | **Step 5.5 (implementation AND factual deliverables)** | **`directives/verification-agent-protocol.md`** |
| Token Efficiency | Every workflow | `directives/token-efficiency-protocol.md` |
| Session State | After Step 2, after Step 4, after 10+ reads | `directives/session-state-protocol.md` |
| Self-Annealing | On any error | `directives/deep_self_annealing.md` |
| Collaboration | Always | `directives/collaboration-protocol.md` |
| Sub-Agent | 2+ experts loaded, or 10+ files in context | `directives/sub_agent_protocol.md` |
| Content Gate | Step 4, for content tasks | `directives/content_creation_gate.md` |
| **Recall Grounding** | **Step 4 (Tier 1.5), auto-fires for grounding-relevant domains** | **`directives/recall-grounding-protocol.md`** |
| Operating Principles | Development workflows | `directives/operating-principles.md` |
| **Prose Classifier** | **Step 5.5 (before delivery)** | **`execution/prose_classifier.py` — auto-runs in `finalize()`** |
| **Ground Truth** | **After evolution cycles** | **`execution/ground_truth.py` — blind compare AI vs expert** |
| **Revenue Tracking** | **After client delivery** | **`execution/revenue_tracker.py` — connect quality to outcomes** |

### Budget-Gated (check before calling)

**Research priority order (2026-04-23 — Gemini primary)**: Foundation/Standard/Deep research → Gemini Deep Research FIRST (`/deep-research-gemini`). Perplexity is fallback + quick-facts only. See `directives/research-protocol.md` for the full priority matrix.

| Protocol | Directive | Gate |
|----------|-----------|------|
| **Deep Research (Gemini) — PRIMARY** | `directives/google-api-usage-policy.md` | 3-layer defense: Ultra covers AI Studio (primary) + pay-as-you-go explicitly OFF + $10 prepaid ceiling. Track in `.agent/gemini-api-usage.json`. Invoked via `/deep-research-gemini` or `execution/deep_research_client.py`. Max possible spend: $10. **Use this first for any foundation/strategic research.** |
| Perplexity — FALLBACK + quick facts | `directives/perplexity-usage-policy.md` | $30/mo, track in `.agent/perplexity-usage.json`. Fires automatically when Gemini Deep Research unavailable. Also for single-claim fact checks via sonar-pro/ask. |
| NotebookLM | `directives/notebooklm-usage-policy.md` | 100/mo, track in `.agent/notebooklm-usage.json` |
| Apify | `directives/apify-usage-policy.md` | $29/mo Starter plan, track in `.agent/apify-usage.json`. Use for scraping/social listening; falls back to Perplexity at 90% cap |

**Session state**: Write `.agent/session-state.md` after intent validation, expert deployment, major decisions, or 10+ file reads. Read after compaction or returning from sub-agents.

---

## Model & SDK Notes (Opus 4.7 Aligned — 2026-04-17)

**Primary model**: Claude Opus 4.7 (1M context variant, `claude-opus-4-7[1m]`). Sonnet 4.6 for single-turn content; Haiku 4.5 for routing/classification.

**What changed from 4.6 → 4.7 (relevant to this system):**
- **Stricter instruction following**: 4.7 reads directives literally. "When applicable" and "fires for X" phrasings now trigger more consistently — tightened in Step 5.5 and Step 6 above.
- **Anthropic SDK param restrictions**: If any future Python code calls Anthropic's SDK directly, do NOT set `temperature`, `top_p`, or `top_k` — 4.7 rejects non-default values with 400 errors. Also: `thinking.budget_tokens` is deprecated; use `effort: "low|medium|high|xhigh"` instead.
- **Tokenizer change**: Text may consume 1.0x–1.35x more tokens vs 4.6. Tier-1 loads (~1,350 tokens) may run ~1,400-1,800. Factor into caching decisions.
- **Prompt caching**: 5-minute TTL (default), 1-hour TTL available at higher cost. Cache writes = 25% premium; cache reads = 10% of input. Large context (skills + genius.md) benefits most from caching within a session.

**SDK safety check — Python scripts in `execution/`:**
- `gemini_client.py`, `skill_converter.py`, `parallel_swarm.py`, `extraction_swarm.py`, `generate_*.py`, `memory_selector.py` call **Gemini** (not Anthropic). Their `temperature`/`thinking_budget` usage is Gemini-API valid — NO changes needed.
- No Python files currently call the Anthropic SDK directly. If that changes, enforce the param restrictions above.

**Claude Code harness**: This conversation runs on Opus 4.7 via Claude Code itself — you do not call the Anthropic API from scripts. Harness handles model config.
