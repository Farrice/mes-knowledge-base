# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

<!-- AGENTS.md is a pointer to GEMINI.md (Gemini-native, separately tuned). Run /sync-instructions after system intent changes. -->
<!-- Slimmed 2026-06-09 (rebuild/deterministic-enforcement): reference blocks moved to directives/cli-reference.md, system-primitives.md, routing-bindings.md, model-notes.md. Nothing deleted — relocated. -->

---

## Environment Setup

- **`.env` at project root** with `NOTION_API_KEY` — required for all Notion operations
- Python deps: `python-dotenv`, `requests` (no requirements.txt; install manually)
- No build step, no test suite — this is an AI orchestration system, not a traditional app

## Notion API — Critical Version Pin

**Always use `execution/notion_api.py`** (pins `Notion-Version: 2022-06-28`). Never use the JS client (v5.9.0 silently breaks schema updates). Database IDs: `directives/notion-databases.md`.

## CLI Reference

All script commands (calibration, audit, knowledge compiler, cost/forge gates): **`directives/cli-reference.md`**.
**Read `_active/system-audit/audit-2026-04-24.md` before significantly changing the system.** Directive nav: `directives/INDEX.md`.

---

## Deterministic Enforcement Layer (hooks — these gates are PHYSICAL, not advisory)

Wired in `.claude/settings.json` → `execution/hooks/`. When a gate fires, work WITH it — never around it.

| Gate | Hook | Behavior |
|---|---|---|
| **Cost gate** (paid APIs: Fal, Seedance, Kling, deep-research) | PreToolUse(Bash) → `cost_gate_hook.py` | **HARD BLOCK.** Denied = surface to Farrice, do not retry. Needs-approval = ask Farrice; ONLY after explicit yes run `cost_gate.py approve --service <id>`, then retry (15-min token) |
| **Finalize debt** | Stop → `session_ledger_hook.py` | Expert skill loaded + artifact produced + no finalize = turn-end blocked ONCE with prefilled command. Run it honestly |
| **Routing bindings** | UserPromptSubmit → `session_ledger_hook.py` | Violations injected as ROUTING WARNING with the binding reason — pivot or use the documented override flag |
| **Sub-agent truth** | PostToolUse counts real Task/Agent spawns | Use the measured count in `--sub-agents`; zero spawns on a qualifying workflow logs a miss |

Extractions (`/extract`, `/extract-forge`) are **never gated** — Farrice's standing decision 2026-06-09. `forge_gate.py status/record` is usage telemetry only.

`evolution_orchestrator.py auto` runs daily 07:00 via launchd (`com.antigravity.evolution-auto`) — never manually babysit evolution cycles.

---

# The Chain (Every Request — No Exceptions)

> Complex process -> simple result. All machinery exists to find the single truth and deliver it through the right mechanism with the right proof at the right identity level (`knowledge/synthesis/the-persuasion-stack.md`). "Comprehensive" output = system failure regardless of score.

Complete 6 steps IN ORDER for every deliverable request. Steps may narrow (table below), but the chain always runs.

**Step 1: SCORE intent (1-5).** +1 each: Deliverable, Audience, Context/constraints, End state, Specific language.

**Step 2: SHARPEN (if Score <= 3).** Ask missing DICE dimensions. One round max. Details: `directives/intent-pipeline.md` Stage 2.

**Step 3: ROUTE to experts.** **Routing defaults to `PRODUCTION_CORE.md` entries** — the router hook surfaces `[CORE]` matches per prompt; long-tail requires explicit `/name` invocation or a decisively stronger match. Multi-domain: `directives/expert_auto_routing.md`. Mandatory bindings: see Routing summary below + `directives/routing-bindings.md`.

**Step 4: LOAD via Context Engine.** Tier 0 (cards) -> **Tier 1.5a (Recall grounding — auto for content/copy/brand/voice/strategy/design domains: fire `mcp__recall__search`, inject 1-3 high-signal cards, silent skip if <2; `directives/recall-grounding-protocol.md`)** -> **Tier 1.5b (Sovereign memory: `python3 execution/memory_retrieve.py "<task intent>" --top 10` before expert output)** -> Tier 1 (SKILL.md + workflow) -> Tier 2 (+ genius.md) -> Tier 3 (sub-agent).
**Never produce expert-domain output without loading the expert first.** Content: minimum 2 skill files per `directives/content_creation_gate.md`.

**Step 5: PRODUCE output.** Their thinking, not their terminology. Enforce `directives/quality_assurance.md`: entity classification, no phantom research, no template slop.

**Step 5.5: VERIFY (Factual Grounding).** Fires when output contains claims about real people/events/dates, statistics, technical facts, market claims, or source attributions. Does NOT fire for pure creative/personal voice/opinion. Per `directives/verification-agent-protocol.md`: claim inventory -> source verification -> confidence labels (VERIFIED/LIKELY/UNCONFIRMED) -> contradiction scan. Verify BEFORE delivery.

**Step 6: FINALIZE (Quality Gate + Log).** Score 4 dimensions (1-10): Intent Alignment, Expert Standard, Adversarial Resilience, Factual Grounding (N/A for pure creative).

```bash
python3 execution/chain_runner.py finalize "[what you produced]" \
    --expert [expert-name] --skill [skill-dir] --workflow [workflow-name] \
    --type [Content|Strategy|Research|Extraction|Client Work|System|Creative|Analysis] \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] --sub-agents [measured count] \
    --notes "[what worked/didn't] | Factual Grounding: [1-10] | Verification: [PASS/FAIL/PARTIAL/N/A]"
```

- **If composite < 7 or any dimension < 6**: retry weakest section once, re-finalize.
- **Factual Grounding veto**: scored (not N/A) and <6 = delivery blocked regardless of composite.
- **Calibrated rubric**: `evolution_store/ground_truth/rubric_v1.md` — anchors at 3/6/9. **Score >=8 = name the matching anchor**; can't name it, lower the score.
- **Non-negotiable** — and now Stop-hook enforced. Protocols: `directives/quality_gate.md`, `directives/feedback-ratchet.md`.

### When Steps Narrow (Not Skip the Chain)

| Condition | Steps shortened | Still required |
|-----------|----------------|----------------|
| Score 4-5 (sharp intent) | Skip Step 2 | 1, 3, 4, 5, 6 |
| "Just do it" / follow-up same plan | Skip Step 2, route silently / reuse route | 1, (3,) 4, 5, 6 |
| Bug fix, clear scope | Skip Step 2 if obvious | 1, 3, 5, 6* |
| Pure system command | Chain does not apply | No deliverable = no chain |

*Step 6 fires only when expert output was produced. **"Trivial" is NOT a skip condition** — content/copy/strategy/research = chain runs.

### Routing Summary (full table + reasons: `directives/routing-bindings.md`; machine source: `routing_enforcer.py BINDINGS`; update together)

- Parallax editions -> `/parallax` (never writers-room) · LinkedIn from scratch -> `/ghostwrite`/Lara · refinement of existing draft -> `writers-room`
- Cold-start converting copy -> `/copy-engine` (Ground Once, Refine Free) · avatar/ICP cold-start -> `/avatar-machine` (Phase 0 GROUND non-optional)
- Brand OS -> `/build-bos` · multi-deliverable mission -> `/supercomputer` · "no gates" -> `/autopilot` · context engineering -> `/ce-design`
- Multi-expert/council -> `/convene` · generic research -> `execution/research.py` (Receipt-carrying; never answer research from training memory)
- DESIGN.md work -> `/design-md-*` · UI from DESIGN.md -> `/product-build` · posters/video -> `skills/fantastic-posters/` (cost-gated)
- New extraction -> `/extract` or `/extract-forge`, ungated (forge_gate.py is telemetry only; genius.md enrichment of A-tier skills remains available as an option, never a requirement)
- JS-rendered/login-gated web -> Playwright (`directives/browser-automation-safety.md`), never WebFetch · video sources -> `fetch-video-context.py`

Known internalized routes: LinkedIn -> Lara Acosta | copywriting -> Luke Iha/Georgi | SEO -> Nathan Gotch | brand -> Oren/Grace | ghostwriting -> Nicolas Cole | content psychology -> Kallaway | agentic workflows -> Nick Saraev. Ambiguous/multi-domain: read `DOMAIN_REGISTRY.md`/`invocation-cards.md`.

### Workflow Override

If user invokes a workflow name (as `/command`, `@command`, "run command", or bare name) — read `.agent/workflows/[command].md` and execute. Full list: `SLASH_COMMANDS.md`. Workflows with `status: superseded` frontmatter redirect — follow the `superseded_by` pointer.

---

## Architecture (3-Layer)

**Layer 1** (Directives): SOPs in `directives/`. **Layer 2** (Orchestration): You — routing, decisions, error handling. **Layer 3** (Execution): Deterministic Python in `execution/`. Push complexity into deterministic code.

Primitives table (who owns what): `directives/system-primitives.md`.

**Knowledge Sources**: Local files (primary) · Notion (5 DBs) · **Recall** (3,000+ cards, Tier 1.5 auto) · Video Vision (`/watch` + `fetch-video-context.py`) · NotebookLM (100/mo) · Perplexity ($30/mo) · Hermes (shell-only, `directives/hermes-usage-policy.md`).

**Key files (on-demand)**: `PRODUCTION_CORE.md` (the ~25 that do the work) · `OPERATING_MANUAL.md` (how Farrice runs this) · `COUNCIL.md` · `DOMAIN_REGISTRY.md` · `JARVIS.md` · `FARRICE.md`.

## Context Engine

| Tier | What to Read | Token Cost | When |
|------|-------------|-----------|------|
| **Hot** | Nothing (already loaded) | 0 | Expert loaded earlier this conversation |
| **0** | `agents/_framework/invocation-cards.md` | ~80 | Routing, ensemble selection |
| **1** | SKILL.md + specific workflow | ~1,350 | Single expert, clear task |
| **2** | SKILL.md + genius.md + workflow | ~2,550 | Creative/complex work |
| **3** | Spawn sub-agent (fresh context) | ~300 main | Multi-expert, 10+ files loaded |

**Hot Context Rule**: If already loaded at Tier 1, only read genius.md for Tier 2. If hot at Tier 2, skip all reads. **Never rely on general training when expert skills exist.** Protocol: `directives/agent-loading-protocol.md`.

## Directory Conventions

- **Skills** (`skills/[name]/`): `SKILL.md` + `genius.md` + `workflows/*.md`. Frontmatter: `routing: long-tail` = demoted in default routing; `status: archived` = de-indexed (stays on disk)
- **Agents** (`agents/[name]/`): `AGENT.md` + `memory/` · **Framework** (`agents/_framework/`)
- **Workflows** (`.agent/workflows/`): invoked via `/name`, `@name`, "run name", or bare name
- `.tmp/` intermediates (never commit) · `execution/` deterministic Python · `directives/` SOPs · `extractions/` raw extractions · `knowledge/` wiki · `councils/` configs · `research_outputs/` · `strategy_briefs/` · `deliverables/` · `products/` · `projects/`

### Per-Client / Per-Project CLAUDE.md Inheritance

Child CLAUDE.md files auto-load client-specific voice/constraints when you `cd` into project folders.

| Project | File | Domain |
|---------|------|--------|
| Andrea / Resonance | `projects/andrea-dj/CLAUDE.md` | Curated daytime sober dance party, Chicago |
| Jen Santulan | `_active/jen-listings/CLAUDE.md` | LA real estate, SFV specialist |
| Farrice / Parallax | `_active/farrice-brand/CLAUDE.md` | Substack + LinkedIn, memoir-grade interiority |

**Inheritance contract**: declare inheritance from root; one-paragraph brand identity (pointer, not duplicate); "When to Load Full Context" table; **Override List**; client-specific Anti-Patterns.

## Supporting Protocols & Budgets

Protocol -> directive map: `directives/INDEX.md`. The ones that fire most: Quality Assurance (Step 5), Verification (5.5), Session State (write `.agent/session-state.md` after intent validation/expert deployment/10+ reads), Sub-Agent (2+ experts or 10+ files), Recall Grounding (Step 4), Browser Safety/Routing (Playwright), Video Vision, Workflow Gates.

**Budget-gated APIs** (hook-enforced; policies in `directives/<service>-usage-policy.md`): Gemini Deep Research ($10 ceiling, PRIMARY for research) -> Perplexity ($30/mo fallback) · NotebookLM (100/mo) · Apify ($29/mo) · Fal ($20 wallet, `fal_budget_guard.py`, seedance-1080p HARD-BLOCKED) · Whisper (deferred). Trackers in `.agent/*.json`.

**Model & SDK notes** (when writing LLM-calling scripts): `directives/model-notes.md`.
