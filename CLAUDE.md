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

### Audit Infrastructure (Added 2026-04-25 — Phases A+B from system audit)

```bash
# Routing enforcement (Fix 2)
python3 execution/routing_enforcer.py check --request "..." --workflow <name> --quiet
python3 execution/routing_enforcer.py list                # Show all mandatory bindings

# Recall grounding observability (Fix 5)
python3 execution/recall_logger.py log --status fired|skipped|failed [...]
python3 execution/recall_logger.py report --days 7        # Grounding × Expert Standard correlation

# Calibrated rubric + eval harness (Fix 1)
python3 execution/eval_harness.py status                  # Calibration progress
python3 execution/eval_harness.py calibrate --days 7      # Inflation drift detection
python3 execution/eval_harness.py anchor --dimension <d> --score <n>  # Look up rubric anchor

# Evolution orchestrator — closes Phase 1-4 loop (Fix 4)
python3 execution/evolution_orchestrator.py auto          # Run all due cycles
python3 execution/evolution_orchestrator.py daily         # Daily report
python3 execution/evolution_orchestrator.py weekly        # Weekly baselines
python3 execution/evolution_orchestrator.py monthly       # Phase 4 gap analysis
python3 execution/evolution_orchestrator.py status        # Last-run state + grounded skills
python3 execution/evolution_orchestrator.py queue         # Phase 2 + binding review queues

# Skill auditor — tier-grade 210 skills (Fix 3)
python3 execution/skill_auditor.py audit                  # A/B/C/REVIEW classification
python3 execution/skill_auditor.py duplication            # Skills × agents overlap
python3 execution/skill_auditor.py update-index --apply   # Annotate SKILL_INDEX.md with tiers
python3 execution/skill_auditor.py archive --tier C --apply  # Move tier to _archive/skills/ (PREVIEW FIRST)
```

**Audit infrastructure rationale**: The 2026-04-24 system audit (`_active/system-audit/audit-2026-04-24.md`) found that scaffolding had outpaced evals — 210 skills + 117 agents + 58 directives but only 16 ground-truth benchmarks. These 6 tools close the measurement gap: routing is now deterministic (not advisory), grounding is observable (not silent), the rubric is anchored (not vibes), the orchestrator closes the Phase 1-4 loop (not just logging), and the skill auditor surfaces tier evidence (not estimates). Calibrate first run found 94-99% of finalize scores were 8+ — empirical confirmation of grade inflation. **Read the audit report before significantly changing the system.** Directive navigation map: `directives/INDEX.md`.

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

### Real Claude Code Subagents (Added 2026-04-28) — 12 Virtuoso-Tier Workers

12 production-grade subagents in `.claude/agents/` (distinct from the 119 expert personas in `agents/<expert>/`). Personas are thinking lenses loaded as Tier 2 context; subagents are repeatable workers with isolated context invokable via the Agent tool.

**Foundation:** `deep-research`, `fact-verifier`, `prose-doctor`
**Production:** `expert-extractor`, `icp-deep-canvasser`, `synthesis-engine`
**Quality:** `adversarial-reviewer`, `content-finalizer`
**Outcomes/Specialty:** `master-copywriter`, `brand-system-builder`, `competitive-intel`, `swarm-orchestrator`

**Canonical chains:**
- Strategic brief: `deep-research` → `synthesis-engine` → `master-copywriter` → `prose-doctor` → `adversarial-reviewer` → `content-finalizer`
- LinkedIn post: persona-load (Lara) → `master-copywriter` → `prose-doctor` → `adversarial-reviewer` → `content-finalizer`
- Parallax edition: raw take → `fact-verifier` → persona-load (Cole) → `master-copywriter` → `prose-doctor` → `adversarial-reviewer` → `content-finalizer`
- New extraction: `expert-extractor` → `synthesis-engine` → `content-finalizer`
- Brand launch: `icp-deep-canvasser` → `competitive-intel` → `brand-system-builder` → `master-copywriter` → `adversarial-reviewer` → `content-finalizer`

Full roster, invocation patterns, and architecture: **`directives/subagent-roster.md`**.

Each subagent embodies a top-1% practitioner identity, inherits the user's accumulated knowledge infrastructure (Recall, extractions, knowledge), encodes hard rules from documented past failures (Parallax 02 fabrications, 8 banned structural moves, voice rules from MEMORY.md), and self-checks before returning. Generic LLM output is the failure mode — these agents are designed to be the exception.

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
**Recall grounding (Tier 1.5):** For grounding-relevant domains (content, copy, brand, voice, storytelling, positioning, strategy, sales, marketing, persuasion, comms, creative, **design / UI / brand-system / DESIGN.md synthesis**), auto-fire `mcp__recall__search` before skill load. Inject 1-3 high-signal cards as source material. Silent skip if <2 cards or weak signal. Full protocol: `directives/recall-grounding-protocol.md`.

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
**Calibrated rubric (Fix 1 / 2026-04-24)**: Score against the anchored rubric at `evolution_store/ground_truth/rubric_v1.md`. Each dimension has worked examples at 3 / 6 / 9 anchors. **If you score ≥8 on any dimension, name which anchor matches and why** — if you can't name the anchor, lower the score. The 2026-04-24 calibration check found 94-99% of recent finalize scores were 8+, which is statistically implausible and confirms grade inflation. The rubric exists to prevent this. Use `python3 execution/eval_harness.py anchor --dimension <dim> --score <n>` to look up an anchor mid-scoring.
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
consumer posture → Dai Media, agentic workflows → Nick Saraev,
**design system / DESIGN.md / "make it look like [brand]" / brand tokens → `skills/design-md/`,
UI/component/page code from a DESIGN.md → `skills/product-design-build/`,
art direction / cinematic / streetwear / AI image-or-video prompts → `skills/creative-direction/` (via Creative Director agent),
stylized poster generation (vintage, Swiss, Ukiyo-e, brutalism, neon-noir, editorial, real-estate, etc.) / "make a poster" → `skills/fantastic-posters/` (Fal + GPT Image 2, 33 styles, MUST gate via `execution/fal_budget_guard.py check --mode=poster`),
image-to-video / "animate this poster" / "make a video" / "video trailer" → `skills/fantastic-posters/` video wrappers (Kling v3 Pro for multi-shot/cheaper, Seedance 2.0 720p for cinematic+audio; MUST gate via `execution/fal_budget_guard.py check --mode=<kling|seedance-720p>`; 1080p HARD-BLOCKED)**),
route without reading `DOMAIN_REGISTRY.md` or `invocation-cards.md`. Only read routing files for ambiguous or multi-domain requests.

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
| DESIGN.md authoring / extract / synthesize / brand-system / "make it look like [brand]" | `/design-md-synthesize` or `/design-md-extract` or `/brand-library` (via Creative Director agent) | Generic Tailwind/CSS suggestions |
| UI / component / page code generation from a DESIGN.md | `/product-build` or `/component-build` (skills/product-design-build/) | Hand-rolling without DESIGN.md as source-of-truth |
| Existing DESIGN.md needs lint / WCAG / refinement | `/design-md-validate` | Eyeballing — always run `npx @google/design.md lint` |
| Competitive intelligence requiring live primary-source quotes / screenshots / JS-rendered pages | `competitive-intel` subagent (Playwright wired) per `directives/browser-automation-routing.md` | Generic WebFetch text scrape (returns hydration shells on Webflow / Framer / Next.js sales pages) |
| Login-gated source verification (LinkedIn profile facts, Substack analytics, MLS data, paywalled research) | Playwright via `deep-research` / `fact-verifier` subagent with persistent profile per `directives/browser-automation-routing.md` | WebFetch (returns login wall HTML, not actual content) |

**Why this exists**: A 2026-04-21 session degraded to 6/10 across 4 iterations on a Parallax edition because `writers-room` was invoked by the user's conversational ask and executed literally. `/parallax` was the correct workflow and was never loaded. Root cause captured in `/Users/farricecain/.claude/plans/additional-edits-this-line-fluffy-cake.md`. When user's conversational prompt and system's correct routing disagree, system wins and explains the override in one sentence.

**Phase 2.5 GROUND + ZEITGEIST CHECK is non-optional for Parallax Editions 02+.** After raw-take capture (Phase 2) and before drafting (Phase 3), `/parallax` runs claim extraction, budget-tiered verification (Recall → Perplexity), zeitgeist scan, and a halt/proceed gate. This exists because Edition 02 shipped with 7 fabrications that slipped past mechanical audits (Madeon as unknown DJ, wrong day, invented distance, song-age math, etc.). The only way to skip is an explicit `--no-ground` flag, which should only be used when the edition has zero external factual surface (pure memoir with no public figures, events, brands, or stats). Full protocol in `.agent/workflows/parallax.md` Phase 2.5.

**Routing enforcement (deterministic, not advisory)**: The bindings table above is mirrored in `execution/routing_enforcer.py`. Before producing for any task that matches a binding signal, run a pre-flight check:
```bash
python3 execution/routing_enforcer.py check --request "<user request>" --workflow <chosen-workflow> --quiet
```
Non-zero exit means the chosen workflow violates a mandatory binding. Pivot to the mandatory workflow OR invoke the documented override (e.g., `--no-ground` for Parallax memoir editions). Every check is logged to `evolution_store/traces/routing_decisions.jsonl`. `chain_runner.py finalize()` also runs a post-hoc check when `--workflow` is supplied, so violations surface in the gate output even if the pre-flight was skipped. **Update both this table and `routing_enforcer.py BINDINGS` together when adding new bindings — code is the source of truth.**

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
| **Browser Automation Safety** | **Any Playwright/browser MCP invocation** | **`directives/browser-automation-safety.md` — Tier 1 reads auto-fire; Tier 2 state-changes (post/send/submit/buy) require explicit confirmation; never type credentials** |
| **Browser Automation Routing** | **Step 4 (LOAD) + Step 5 (PRODUCE) — when task involves live web** | **`directives/browser-automation-routing.md` — when to use Playwright vs WebFetch vs Perplexity vs Apify; Playwright primary for JS-rendered, login-gated, screenshot-evidence, multi-step navigation** |

### Budget-Gated (check before calling)

**Research priority order (2026-04-23 — Gemini primary)**: Foundation/Standard/Deep research → Gemini Deep Research FIRST (`/deep-research-gemini`). Perplexity is fallback + quick-facts only. See `directives/research-protocol.md` for the full priority matrix.

| Protocol | Directive | Gate |
|----------|-----------|------|
| **Deep Research (Gemini) — PRIMARY** | `directives/google-api-usage-policy.md` | 3-layer defense: Ultra covers AI Studio (primary) + pay-as-you-go explicitly OFF + $10 prepaid ceiling. Track in `.agent/gemini-api-usage.json`. Invoked via `/deep-research-gemini` or `execution/deep_research_client.py`. Max possible spend: $10. **Use this first for any foundation/strategic research.** |
| Perplexity — FALLBACK + quick facts | `directives/perplexity-usage-policy.md` | $30/mo, track in `.agent/perplexity-usage.json`. Fires automatically when Gemini Deep Research unavailable. Also for single-claim fact checks via sonar-pro/ask. |
| NotebookLM | `directives/notebooklm-usage-policy.md` | 100/mo, track in `.agent/notebooklm-usage.json` |
| Apify | `directives/apify-usage-policy.md` | $29/mo Starter plan, track in `.agent/apify-usage.json`. Use for scraping/social listening; falls back to Perplexity at 90% cap |
| **Fal API (fantastic-posters + video)** | `directives/fal-usage-policy.md` | $20 wallet w/ $5 refill threshold, track in `.agent/fal-usage.json` (v2 mode-aware). **MANDATORY pre-flight gate**: every Fal call must pass `python3 execution/fal_budget_guard.py check --mode=<...>` first. Modes: `poster` ($1 ceiling), `edit` ($1), `kling` ($2), `seedance-480p` ($1.50), `seedance-720p` ($3), `seedance-1080p` (HARD-BLOCKED, no override). Cross-mode: per-day $6, per-cycle $15, rate-limit 5/5min, halt after 2 consecutive failures. Hookify enforced. Wrappers: `./gen.sh` (posters), `execution/fal_video_kling.py`, `execution/fal_video_seedance.py`. |

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
