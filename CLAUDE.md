# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

<!-- CLAUDE.md and AGENTS.md share identical format. GEMINI.md is Gemini-native. Run /sync-instructions after system intent changes. -->

---

## Environment Setup

- **`.env` at project root** with `NOTION_API_KEY` — required for all Notion operations
- Python deps: `python-dotenv`, `requests` (no requirements.txt; install manually)
- No build step, no test suite — this is an AI orchestration system, not a traditional app

## Notion API — Critical Version Pin

`@notionhq/client` v5.9.0 returns `data_sources` instead of `properties`. Schema updates silently succeed but don't persist; row inserts fail.

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
python execution/fetch-transcript.py "<youtube_url>" "<expert>"          # transcript-only
python execution/fetch-video-context.py "<video_url>" "<expert>"          # frame-grounded vision (claude-video wrapper)
```

### Calibration & Quality Tools

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

**Ground Truth** (`knowledge/expert-benchmarks/`): 7 domains, 16 experts. Blind comparison feeds feedback ratchet.
**Revenue Tracker** (`.agent/revenue-outcomes.json`): Connects quality scores to business outcomes.
**Prose Classifier**: Integrated into `chain_runner.py` — warns if Expert Standard inflated by AI-prose patterns.

### Audit Infrastructure

```bash
# Routing enforcement
python3 execution/routing_enforcer.py check --request "..." --workflow <name> --quiet
python3 execution/routing_enforcer.py list

# Recall grounding observability
python3 execution/recall_logger.py log --status fired|skipped|failed [...]
python3 execution/recall_logger.py report --days 7

# Calibrated rubric + eval harness
python3 execution/eval_harness.py status
python3 execution/eval_harness.py calibrate --days 7
python3 execution/eval_harness.py anchor --dimension <d> --score <n>

# Evolution orchestrator
python3 execution/evolution_orchestrator.py auto|daily|weekly|monthly|status|queue

# Skill auditor
python3 execution/skill_auditor.py audit|duplication
python3 execution/skill_auditor.py update-index --apply
python3 execution/skill_auditor.py archive --tier C --apply  # PREVIEW FIRST
```

**Rationale**: 234 skills + 134 agents + 64 directives + 888 workflows + 101 scripts with only 7 ground-truth domains. These 6 tools close the measurement gap: routing is deterministic, grounding is observable, the rubric is anchored, the orchestrator closes Phase 1-4, and the skill auditor surfaces tier evidence. Wave 1-3 Excellence Lift + 2026-05-23 cap-value fix (7.5 -> 7.25, commit `807ea9d7`) brought scores into bimodal shape. **Read `_active/system-audit/audit-2026-04-24.md` before significantly changing the system.** Directive nav: `directives/INDEX.md`.

### Knowledge Compiler — Karpathy Wiki Engine

```bash
python execution/knowledge_compiler.py stats|full|briefing|inventory|index|lint|stale|overlap
python execution/knowledge_compiler.py auto-archive [--execute]
python execution/knowledge_compiler.py log <action> "title" --domain X --expert Y
python execution/knowledge_compiler.py archive "query" result.md --domain X
```

240 files, 1.8M words across `knowledge/`, `extractions/`, `research_outputs/`. Three operations: **ingest** (cascade updates), **query** (search write-back), **lint** (contradictions, orphans, stale). Living index: `knowledge/index.md`. Log: `knowledge/log.md`. Reflection: `/reflect` -> `knowledge/synthesis/`.

**Notion Vault Sync**: `python execution/notion_api.py vault-create "Title" --expert X --domain Y` — auto-triggered by `finalize` for quality >= 7.
**Autofill Config**: `directives/notion-autofill-guide.md`.

### Evolution Direction

`directives/evolution-direction.md`: Single source of truth for what to evolve. Read before `/skill-evolution`. Updated after every cycle.

---

## Directory Conventions

- **Skills** (`skills/[name]/`): `SKILL.md` + `genius.md` + `workflows/*.md`
- **Agents** (`agents/[name]/`): `AGENT.md` + `memory/`
- **Agent framework** (`agents/_framework/`): `invocation-cards.md`, `AGENT_TEMPLATE.md`, `orchestrator.md`
- **Workflows** (`.agent/workflows/`): Invoked via `/extract`, `@extract`, "run extract", or bare name

## File Organization

- `.tmp/` — intermediates (never commit)
- `execution/` — deterministic Python scripts
- `directives/` — SOPs and protocols
- `extractions/` — raw extraction reports and transcripts
- `knowledge/` — organized knowledge base
- `councils/` — council configurations
- `research_outputs/` — research project outputs
- `strategy_briefs/` — strategic dossiers
- `deliverables/` — client/project deliverables
- `products/` — product builds
- `projects/` — active project workspaces

### Per-Client / Per-Project CLAUDE.md Inheritance

Child CLAUDE.md files auto-load client-specific voice/constraints when you `cd` into project folders.

| Project | File | Domain |
|---------|------|--------|
| Andrea / Resonance | `projects/andrea-dj/CLAUDE.md` | Curated daytime sober dance party, Chicago |
| Jen Santulan | `_active/jen-listings/CLAUDE.md` | LA real estate, SFV specialist |
| Farrice / Parallax | `_active/farrice-brand/CLAUDE.md` | Substack + LinkedIn, memoir-grade interiority |

**Inheritance contract** (required in every child CLAUDE.md):
- Declare inheritance from root CLAUDE.md
- One-paragraph brand identity (pointer + anchor, NOT duplicate of brand bible)
- "When to Load Full Context" table (task -> context file)
- **Override List** (divergences from root behavior)
- Client-specific Anti-Patterns

---

## System Primitives (Irreducible Parts)

Each row names who owns the responsibility and what triggers it. If a workflow reimplements a primitive's logic, that's drift — the source file is the contract.

| Primitive | Owns | Triggered By | Source File |
|---|---|---|---|
| `intent_to_package` | Outcome-class detection -> mission package | `/autopilot` Phase 1 | `execution/intent_to_package.py` |
| `routing_enforcer` | Runtime validation of Mandatory Routing table | Pre-flight + `finalize` post-hoc | `execution/routing_enforcer.py` |
| `anchor_memory` | Project-scoped persistent context anchors | `/supercomputer` + multi-deliverable missions | `execution/anchor_memory.py` |
| `cost_gate` | Pre-flight approval for paid APIs (Fal, Perplexity, NotebookLM, Gemini) | Every paid-API call; `/autopilot` G2 (>$5) | `execution/cost_gate.py` |
| `taste_signature` | Bimodal taste filter atop calibrated rubric (Wave 2) | `finalize` after rubric scoring | `execution/taste_signature.py` |
| `excellence_predictor` | Pre-flight prediction + grade-inflation detector (Wave 3) | `/autopilot` Phase 1; calibration drift | `execution/excellence_predictor.py` |
| `orchestration_ledger` | Post-run trace: what fired, what's next, refinement prompts | End of `/autopilot` | `execution/orchestration_ledger.py` |
| `chain_runner.finalize` | Step 6: quality gate + caps + Notion log + protocol tracking + routing check | Step 6 of every expert deliverable | `execution/chain_runner.py` |
| `recall_logger` | Observability for Tier 1.5 grounding decisions | Every Recall attempt; deterministic backstop in `finalize` | `execution/recall_logger.py` |
| `eval_harness` | Score against anchored rubric; calibration drift detection | Manual scoring; weekly `evolution_orchestrator` | `execution/eval_harness.py` |
| `context_ethics_gate` | Deterministic Defense/Ethics backstop for `/ce-*` context-engineering output (structural destabilization + consent checks, verdict log) | Inside `/ce-design`/`/ce-build`/`/ce-honesty`; deterministic backstop in `finalize` (Step 11.9) | `execution/context_ethics_gate.py` |

Atom-vs-system taxonomy (below) is a sub-classification underneath this table, not a competing layer.

---

# The Chain (Every Request — No Exceptions)

> Complex process -> simple result. All machinery exists to find the single truth and deliver it through the right mechanism with the right proof at the right identity level (see `knowledge/synthesis/the-persuasion-stack.md`). "Comprehensive" output = system failure regardless of score.

Complete 6 steps IN ORDER for every deliverable request. Steps may narrow (see table below), but the chain always runs.

### Step 1: SCORE intent (1-5)
+1 Deliverable | +1 Audience | +1 Context/constraints | +1 End state | +1 Specific language.
Always score — the number informs routing depth.

### Step 2: SHARPEN (if Score <= 3)
Ask missing DICE dimensions. One round max. Fill inferences, confirm.
Details: `directives/intent-pipeline.md` Stage 2.

### Step 3: ROUTE to experts
Match domain -> experts via `directives/intent-pipeline.md` Stage 3. Check FARRICE.md proactive deployment table. Multi-domain: `directives/expert_auto_routing.md`.
**Always route.** Even if the result is one Tier 1 expert, the routing decision is explicit.

### Step 4: LOAD via Context Engine
Tier 0 (cards) -> **Tier 1.5a (Recall grounding — automatic, silent)** -> **Tier 1.5b (Sovereign memory retrieval)** -> Tier 1 (SKILL.md + workflow) -> Tier 2 (+ genius.md) -> Tier 3 (sub-agent).

**Sovereign memory (Tier 1.5b)**: Deterministic cascade over `.memory/sovereign.db` (148 memories, 21 pinned voice rules). Invoke before expert output:
```bash
python3 execution/memory_retrieve.py "<task intent>" --top 10
```
Returns pinned voice rules + semantic/procedural matches + recent episodic decisions. Primary cross-session compounding mechanism. Protocol: `directives/agent-loading-protocol.md` Tier 1.5.

**Never produce expert-domain output without loading the expert first.**
For content: minimum 2 skill files per `directives/content_creation_gate.md`.
**Recall grounding (Tier 1.5a):** For grounding-relevant domains (content, copy, brand, voice, storytelling, positioning, strategy, sales, marketing, persuasion, comms, creative, design/UI/DESIGN.md), auto-fire `mcp__recall__search`. Inject 1-3 high-signal cards. Silent skip if <2 cards. Protocol: `directives/recall-grounding-protocol.md`.

### Step 5: PRODUCE output
Execute using loaded expert frameworks — their thinking, not their terminology.
Enforce `directives/quality_assurance.md`: entity classification, no phantom research, no template slop.

### Step 5.5: VERIFY (Factual Grounding)
**Fires when** output contains claims about real people/events/dates, statistics, technical facts, market claims, or source attributions. **Does NOT fire** for pure creative, personal voice, brainstorming, stylistic drafts, opinion without factual load.

Per `directives/verification-agent-protocol.md`:
- **Implementation**: Run it, break it (adversarial checks)
- **Factual**: Claim inventory -> source verification -> confidence labeling (VERIFIED/LIKELY/UNCONFIRMED) -> contradiction scan
- Verify BEFORE delivery. If FAIL -> re-research, re-verify before rewriting.

### Step 6: FINALIZE (Quality Gate + Log + Protocol Tracking)
Score on 4 dimensions (1-10 each):
- **Intent Alignment**: Matches what user asked for?
- **Expert Standard**: Would the real expert recognize this as quality?
- **Adversarial Resilience**: Survives critical scrutiny?
- **Factual Grounding**: Claims verified? Unverifiable flagged? **N/A** for pure creative/opinion.

```bash
python3 execution/chain_runner.py finalize "[what you produced]" \
    --expert [expert-name] --skill [skill-dir] --workflow [workflow-name] \
    --type [Content|Strategy|Research|Extraction|Client Work|System|Creative|Analysis] \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "[what worked/didn't] | Factual Grounding: [1-10] | Verification: [PASS/FAIL/PARTIAL/N/A]"
```
**If composite < 7 or any dimension < 6**: Retry weakest section once, re-finalize.
**Factual Grounding veto**: Scored (not N/A) and <6 = delivery blocked regardless of composite.
**Calibrated rubric**: Score against `evolution_store/ground_truth/rubric_v1.md`. Each dimension has anchors at 3/6/9. **If you score >=8, name the matching anchor** — can't name it, lower the score. Use `python3 execution/eval_harness.py anchor --dimension <dim> --score <n>`.
**Non-negotiable.** Expert output without `finalize` is incomplete. Feeds Phases 2-4.
Protocols: `directives/quality_gate.md`, `directives/feedback-ratchet.md`.

---

### When Steps Narrow (Not Skip the Chain)

| Condition | Steps shortened | Steps still required |
|-----------|----------------|---------------------|
| Score 4-5 (sharp intent) | Skip Step 2 | 1, 3, 4, 5, 6 |
| "Just do it" / "go ahead" | Skip Step 2, route silently | 1, 3, 4, 5, 6 |
| Follow-up, same plan | Skip Step 2, reuse Step 3 route | 1, 4, 5, 6 |
| Bug fix, clear scope | Skip Step 2 if obvious | 1, 3, 5, 6* |
| Pure system command | Chain does not apply | No deliverable = no chain |

*Step 6 fires only when expert output was produced.

**"Trivial" is NOT a skip condition.** Content/copy/strategy/research/expert-domain = chain runs. "LinkedIn headlines" requires routing to Lara Acosta.

### Chain Efficiency Rules

**Steps 1-2**: Internalized — no file reads. Only read `directives/intent-pipeline.md` for explicit `/validate-intent`.

**Step 3 (ROUTE)**: Internalized for known domains:
- LinkedIn -> Lara Acosta | copywriting -> Luke Iha | SEO -> Nathan Gotch | brand -> Oren/Grace
- ghostwriting -> Nicolas Cole | content psychology -> Kallaway | consumer posture -> Dai Media
- agentic workflows -> Nick Saraev
- design system / DESIGN.md / brand tokens -> `skills/design-md/`
- UI/component code from DESIGN.md -> `skills/product-design-build/`
- art direction / cinematic / AI image prompts -> `skills/creative-direction/`
- poster gen ("make a poster/logo") -> `skills/fantastic-posters/` (Fal + GPT Image 2, 38 styles, text-to-image + edit + rembg + variants. MUST gate via `execution/fal_budget_guard.py check --mode=<poster|edit|rembg>`)
- image-to-video / "animate this" -> `skills/fantastic-posters/` video wrappers (Kling v3 Pro or Seedance 2.0 720p. MUST gate via `fal_budget_guard.py`. 1080p HARD-BLOCKED)

Only read `DOMAIN_REGISTRY.md`/`invocation-cards.md` for ambiguous or multi-domain requests.

**Step 4 (LOAD)**: Start Tier 1. Load genius.md ONLY if first-pass output falls short, task is explicitly creative/complex, or user asks for "the best."

**Step 6 (FINALIZE)**: Required only for expert-domain output. Quick answers, system commands, conversations = no finalize.

### Workflow Override

If user invokes a workflow name (as `/command`, `@command`, "run command", or bare name) — read `.agent/workflows/[command].md` and execute. Full list: `SLASH_COMMANDS.md`.

### Mandatory Workflow Routing (Domain -> Workflow Bindings)

If the task matches a domain below, deploy the bound workflow **even if the user names a different one**. System wins; explain the override in one sentence. Origin: 2026-04-21 session degraded to 6/10 because `writers-room` was used instead of `/parallax`.

| Domain signal | Mandatory workflow | Never substitute |
|---|---|---|
| Parallax Substack editions | `/parallax` | `writers-room` (diagnostic-on-draft only) |
| LinkedIn post from scratch | `/ghostwrite` or Lara Acosta skill | `writers-room` (refinement only) |
| Writers' room refinement of existing draft | `writers-room` | Production workflows |
| DESIGN.md authoring / extract / synthesize / brand-system | `/design-md-synthesize` or `-extract` or `/brand-library` | Generic Tailwind/CSS |
| UI / component code from DESIGN.md | `/product-build` or `/component-build` | Hand-rolling without DESIGN.md |
| DESIGN.md lint / WCAG / refinement | `/design-md-validate` | Eyeballing — always run `npx @google/design.md lint` |
| Competitive intel needing JS-rendered pages / screenshots | `/competitor-intel` or `/spy-market` + Playwright | WebFetch (returns hydration shells) |
| Login-gated source verification | Playwright per `directives/browser-automation-safety.md` | WebFetch (returns login wall) |
| Video source material (23 video-aware workflows) | `python3 execution/fetch-video-context.py` per `directives/video-vision-protocol.md` | Transcript-only ingestion (visual hooks = 30-50% of meaning) |
| Brand Operating System / "BOS" / 6-layer brand build | `/build-bos` (7-phase via `skills/brand-operating-system/`) | Single-component skills alone |
| Multi-deliverable marketing/creative mission | `/supercomputer` (anchor-memory + cost gate) | Single-skill execution alone — requires `anchor_memory.py` + `cost_gate.py` for cross-phase cohesion. Triggers: `directives/supercomputer-mode.md` |
| Gate-suppressed orchestration ("autopilot", "no gates", "just execute") | `/autopilot` — 3 gates only: G1 (intent <=2), G2 (cost >$5), G3 (prose FLAGGED at Expert Standard >=7) | `/supercomputer`, `/jcc-deploy` etc. (halt at Phase 1 even when user said "no gates") |
| Context engineering / "engineer the conditions" / "make the behavior automatic" / "what's upstream of the outcome" | `/ce-design` (Context Engineering OS in `skills/chase-hughes-context-engineering/`; emits a Context-Design Spec, then hands to the production expert) | Single-tactic copy/LinkedIn workflow alone. Multi-deliverable missions defer to `/supercomputer` (which composes `/ce-build`). Defense/Ethics Gate enforced by `execution/context_ethics_gate.py` |
| Build an avatar / ICP / manifold from scratch · "plot the market" · cold-start buyer intelligence | `/avatar-machine` (full cold-start → finished copy) or `/avatar-manifold` (intelligence only) — `skills/luke-iha-avatar-machine/`. **Phase 0 GROUND auto-fires** (`execution/avatar_manifold_runner.py`: Gemini Deep Research + Apify VOC + FB Ad Library + Recall, gated by `research_quality_gate.py --strict`). Skip only with `--no-ground` (user-supplied VOC via `--voc-file`). | `icp-build`/`icp-research`/`icp-deep-dive` (reasoning-only; model structure but skip real-VOC research → modeled language fails rubric crit 6). GROUND is the deterministic backstop. |
| Cold-start → converting copy · "write copy that converts for market X" · end-to-end copy from a blank page (VSL/ad/email/landing) | `/copy-engine` (`.agent/workflows/copy-engine.md`) — **Ground Once, Refine Free.** Grounds the market ONCE via `avatar_manifold_runner.py` (WARM reuse = $0; cold-start cost-previewed ~$0.50–2.50, often $0 under Ultra), writes `warm_core`, assembles the 6 copy blocks, gates proof via `verify_proof_ledger.py`. Every later iteration/refinement/writers-room pass reuses the cache at $0. | Writing copy from ungrounded context (false-confidence / fabricated-market failure). Refinement of EXISTING copy reuses the cache via standalone copy-blocks workflows (`/craves-polish`, `/curiosity-engine`, etc.) at $0. Enforced by `routing_enforcer` binding `cold_start_converting_copy`. |
| Multi-expert / collaborative / council work · "get the experts together" · "convene the council" · "multiple perspectives on X" · cross-domain creative/strategy where collective genius beats one voice | **Collective Genius Council** `.agent/workflows/collective-genius-council.workflow.js` via **`/convene`** (presets: `/council` `/roundtable`=tight · `/strike`=fast · `/campaign`=wide+`/supercomputer` · `/deploy-council`=max). Convenes a deliberately diverse cross-domain council (`council_cast.py`: per-domain cap + cross-pollination wildcards) + Farrice's lens, runs genuine 2-round deliberation (genius-loaded, contradictions preserved as forks), synthesizes an outcome none could reach alone, emits a **"How the Masters Thought"** digest → `knowledge/council-sessions/` + a growing `knowledge/council-rubric.md`. Holds the grounding floor; $0 incremental. | The fragile/broken paths: the JCC stubs (`/strike` `/campaign` `/jcc-deploy` forwarded to a MISSING plugin — now repointed here) and `execution/parallel_swarm.py` (deprecated subprocess pattern). Enforced by `routing_enforcer` binding `collective_genius`. |
| Generic research · "deep research on X" · "research this / the market / the landscape" · strategic intelligence · zero-to-expert grounding | **Unified Research Engine** `execution/research.py`. For **deep/max**, PRIMARY = the native expert **SWARM** (`.agent/workflows/deep-research-swarm.workflow.js` via the Workflow tool): decompose → cast world-class personas → parallel fan-out (10-12 deep, ~36 max) → gap-fill → adversarial verify → synthesize, **$0 incremental**, Gemini Deep Research merging in parallel. For quick/standard: `python3 execution/research.py "<q>" --depth <tier>` (Gemini-first → Perplexity → Tavily-research bedrock floor). Every result carries a **Research Receipt** (engine · REAL/DEGRADED/FAILED · provenance · $cost). Failed/empty calls cost **$0**; the floor guarantees a real sourced result even if every paid path fails. **It can degrade — it cannot lie or fabricate.** | Answering research from training memory instead of live cited sources. Domain-specific grounding (avatar/copy/parallax) uses its own binding. Enforced by `routing_enforcer` binding `unified_research`. |

**Avatar Machine Phase 0 GROUND is non-optional for cold-start builds.** Gemini Deep Research foundation + Apify VOC mining + FB Ad Library hooks + Recall grounding, floor-checked (≥15 source URLs, zero `[MODELED]`) by `research_quality_gate.py --strict`. Skip only with `--no-ground` + `--voc-file` (the "import, don't regenerate" path for markets you already have real VOC on). Enforced by `routing_enforcer.py` binding `avatar_manifold_coldstart`.

**Parallax Phase 2.5 GROUND + ZEITGEIST is non-optional for Editions 02+.** Claim extraction, budget-tiered verification (Recall -> Perplexity), zeitgeist scan, halt/proceed gate. Skip only with explicit `--no-ground` (pure memoir, zero external factual surface). Origin: Edition 02 shipped 7 fabrications.

**Routing enforcement**: Bindings mirrored in `execution/routing_enforcer.py`. Pre-flight:
```bash
python3 execution/routing_enforcer.py check --request "<user request>" --workflow <chosen-workflow> --quiet
```
Non-zero exit = violation. `finalize()` also runs post-hoc check. **Update both this table and `routing_enforcer.py BINDINGS` together.**

---

## Architecture (3-Layer)

**Layer 1** (Directives): SOPs in `directives/`.
**Layer 2** (Orchestration): You — routing, decisions, error handling.
**Layer 3** (Execution): Deterministic Python in `execution/`.

Push complexity into deterministic code. You focus on decision-making.

**Knowledge Sources:**
- **Local Files**: Skills, agents, directives (primary)
- **Notion**: 5 databases (projects, knowledge vault, content pipeline, captures, personal context)
- **Recall** (3,000+ cards): Auto-queried at Tier 1.5 for content/brand/voice/strategy. Tools: `mcp__recall__search`, `mcp__recall__get_document_content`, `mcp__recall__explore_kb`, `mcp__recall__filter_by_metadata`
- **Video Vision** (`/watch` plugin + `execution/fetch-video-context.py`): Frame-grounded vision. Auto-fires from 23 workflows for video source material. See `directives/video-vision-protocol.md`
- **NotebookLM**: 5 notebooks (Higgsfield, AI Brain, LinkedIn Ghostwriting, Lara Acosta, Luke Iha). 100/mo. Track: `.agent/notebooklm-usage.json`
- **Perplexity**: $30/month web research (fallback to Gemini for deep research)
- **Hermes** ($20/mo): Local agent CLI. Shell-only (NOT MCP). Policy: `directives/hermes-usage-policy.md`. Track: `.agent/hermes-usage.json`

**Key files (on-demand, not preloaded):**
- `COUNCIL.md` — 24 experts + 5 councils
- `DOMAIN_REGISTRY.md` — Expert swim lanes
- `JARVIS.md` — Expert invocation protocol
- `FARRICE.md` — Personal context, identity, voice

---

## Skill Architecture — Atoms vs Systems

Two tiers. Naming the distinction makes the compounding layer visible.

**Atomic Skill** — Single tool, one job, reusable across compositions. Upgrading one atom upgrades every system using it.
Examples: `voice-document`, `mood-board`, `name-framework`, `prose-check`, `generate-image`
**Test**: One deliverable type, one workflow, no internal phase gates? -> atom.

**Skill System** — Multi-phase orchestrated composition. Has explicit phase structure and clear orchestrator.
Examples: `/extract-forge` (8 phases), `/parallax` (Phase 2.5 gate), `/writers-room` (9-expert loadout), JCC missions, swarm workflows, brand builds
**Test**: Multiple interdependent phases, multiple expert lenses in sequence, gate-and-proceed structure? -> system.

Expert skills classify as atom or system depending on scope (single workflow = atom, multi-phase production = system). Sub-agents provide context isolation between atoms in a system — execution-time choice, not a tier. Frontmatter annotation (`tier: atom | system`) is advisory; unlabeled is fine.

---

## Context Engine

| Tier | What to Read | Token Cost | When |
|------|-------------|-----------|------|
| **Hot** | Nothing (already loaded) | 0 | Expert loaded earlier this conversation |
| **0** | `agents/_framework/invocation-cards.md` | ~80 | Routing, ensemble selection |
| **1** | SKILL.md + specific workflow | ~1,350 | Single expert, clear task |
| **2** | SKILL.md + genius.md + workflow | ~2,550 | Creative/complex work |
| **3** | Spawn sub-agent (fresh context) | ~300 main | Multi-expert, 10+ files loaded |

**Hot Context Rule**: If already loaded at Tier 1, only read genius.md for Tier 2. If hot at Tier 2, skip all reads.
**Never rely on general training when expert skills exist.** Protocol: `directives/agent-loading-protocol.md`.

---

## Supporting Protocols

| Protocol | Fires During | Directive |
|----------|-------------|-----------|
| Quality Assurance | Step 5 | `directives/quality_assurance.md` |
| Verification Agent | Step 5.5 | `directives/verification-agent-protocol.md` |
| Token Efficiency | Every workflow | `directives/token-efficiency-protocol.md` |
| Session State | After Step 2/4, after 10+ reads | `directives/session-state-protocol.md` |
| Self-Annealing | On any error | `directives/deep_self_annealing.md` |
| Collaboration | Always | `directives/collaboration-protocol.md` |
| Sub-Agent | 2+ experts, or 10+ files | `directives/sub_agent_protocol.md` |
| Content Gate | Step 4, content tasks | `directives/content_creation_gate.md` |
| Recall Grounding | Step 4 (Tier 1.5), grounding domains | `directives/recall-grounding-protocol.md` |
| Operating Principles | Development workflows | `directives/operating-principles.md` |
| Prose Classifier | Step 5.5 (in `finalize`) | `execution/prose_classifier.py` |
| Ground Truth | After evolution cycles | `execution/ground_truth.py` |
| Revenue Tracking | After client delivery | `execution/revenue_tracker.py` |
| Browser Safety | Any Playwright invocation | `directives/browser-automation-safety.md` — Tier 1 auto-fire; Tier 2 state-changes need confirmation |
| Browser Routing | Steps 4+5 with live web | `directives/browser-automation-routing.md` — Playwright for JS-rendered/login-gated/screenshots |
| Video Vision | Source ingestion in 23 workflows | `directives/video-vision-protocol.md` — exit 0 OK / 2 SKIPPED / 1 FAILED, never blocks |
| Workflow Gates | Phase boundaries in system workflows | `directives/workflow-gate-convention.md` — halt/proceed gates, distinct from quality_gate.md |

### Budget-Gated (check before calling)

**Research priority**: Gemini Deep Research FIRST -> Perplexity fallback. See `directives/research-protocol.md`.

| Service | Directive | Budget / Gate |
|---------|-----------|---------------|
| Gemini Deep Research (PRIMARY) | `directives/google-api-usage-policy.md` | $10 prepaid ceiling. Track: `.agent/gemini-api-usage.json`. Invoke: `/deep-research-gemini` or `execution/deep_research_client.py` |
| Perplexity (fallback + quick facts) | `directives/perplexity-usage-policy.md` | $30/mo. Track: `.agent/perplexity-usage.json` |
| NotebookLM | `directives/notebooklm-usage-policy.md` | 100/mo. Track: `.agent/notebooklm-usage.json` |
| Apify | `directives/apify-usage-policy.md` | $29/mo. Track: `.agent/apify-usage.json`. Falls back to Perplexity at 90% |
| Fal API (posters + video) | `directives/fal-usage-policy.md` + `directives/fal-edit-mode-guide.md` | $20 wallet. **MANDATORY**: `python3 execution/fal_budget_guard.py check --mode=<...>` before every call. Modes: poster ($1), edit ($1), rembg ($0.10), kling ($2), seedance-480p ($1.50), seedance-720p ($3), seedance-1080p (HARD-BLOCKED). Cross-mode: $6/day, $15/cycle, 5/5min rate-limit. Wrappers: `./gen.sh`, `execution/fal_video_kling.py`, `execution/fal_video_seedance.py` |
| Whisper (video-vision fallback) | `directives/video-vision-protocol.md` | Deferred. Set `GROQ_API_KEY` in `.env` to activate. Most YouTube has native captions |

**Session state**: Write `.agent/session-state.md` after intent validation, expert deployment, major decisions, or 10+ reads.

---

## Model & SDK Notes

**Primary**: Claude Opus 4.7 (1M context). Sonnet 4.6 for single-turn; Haiku 4.5 for routing/classification.

**Current rules:**
- Anthropic SDK: do NOT set `temperature`, `top_p`, `top_k` (400 errors). Use `effort: "low|medium|high|xhigh"` instead of `thinking.budget_tokens`.
- Tokenizer: ~1.0x-1.35x more tokens vs 4.6. Factor into caching.
- Prompt caching: 5-min TTL default, 1-hour at higher cost. Cache reads = 10% of input cost.
- Python scripts in `execution/` call **Gemini** (not Anthropic) — their params are fine.
- Claude Code harness handles model config. You do not call Anthropic API from scripts.
