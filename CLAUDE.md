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
python execution/fetch-transcript.py "<youtube_url>" "<expert>"          # transcript-only
python execution/fetch-video-context.py "<video_url>" "<expert>"          # frame-grounded vision (claude-video wrapper)
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

# Skill auditor — tier-grade 234 skills (Fix 3)
python3 execution/skill_auditor.py audit                  # A/B/C/REVIEW classification
python3 execution/skill_auditor.py duplication            # Skills × agents overlap
python3 execution/skill_auditor.py update-index --apply   # Annotate SKILL_INDEX.md with tiers
python3 execution/skill_auditor.py archive --tier C --apply  # Move tier to _archive/skills/ (PREVIEW FIRST)
```

**Audit infrastructure rationale**: The 2026-04-24 system audit (`_active/system-audit/audit-2026-04-24.md`) found that scaffolding had outpaced evals — at that time 210 skills + 117 agents + 58 directives with only 16 ground-truth benchmarks. As of 2026-05-23 the system has grown to **234 skills + 134 agents + 64 directives + 888 workflow files + 101 execution scripts** with ground-truth still at 7 domains (brand-strategy, content-strategy, copywriting, linkedin, sales-psychology, screenwriting, seo). The 6 tools above close the measurement gap: routing is now deterministic (not advisory), grounding is observable (not silent), the rubric is anchored (not vibes), the orchestrator closes the Phase 1-4 loop (not just logging), and the skill auditor surfaces tier evidence (not estimates). The 2026-04-24 calibrate-first-run found 94-99% of finalize scores were 8+; Wave 1-3 Excellence Lift (caps + taste_signature + excellence_predictor) and the 2026-05-23 cap-value fix (7.5 → 7.25, commit `807ea9d7`) brought the distribution into genuinely bimodal shape. **Read the audit report before significantly changing the system.** Directive navigation map: `directives/INDEX.md`.

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

### Per-Client / Per-Project CLAUDE.md Inheritance

Client and brand-specific projects use Claude Code's parent-folder CLAUDE.md inheritance to override root behavior with client-specific voice, non-goals, and constraints. When you `cd` into one of these folders, the child CLAUDE.md loads alongside root.

Active per-project CLAUDE.md files (Phase B Move 3, shipped 2026-05-12):

| Project | File | Domain |
|---------|------|--------|
| Andrea / Resonance | `projects/andrea-dj/CLAUDE.md` | Curated daytime sober dance party, Chicago, 12 Non-Negotiables |
| Jen Santulan | `_active/jen-listings/CLAUDE.md` | LA real estate, SFV specialist, warm-friend voice |
| Farrice / Parallax | `_active/farrice-brand/CLAUDE.md` | Substack + LinkedIn, memoir-grade interiority, banned structural moves |

**Inheritance contract (required header in every child CLAUDE.md):**
- Declare inheritance from root: `> Inherits from: /Users/farricecain/Google Antigravity/CLAUDE.md (The Chain, Architecture, Skill tiers, Quality Gate)`
- Provide a one-paragraph brand identity (NOT a duplicate of the brand bible — a pointer + one-paragraph anchor)
- "When to Load Full Context" table — task → which existing brand context file to load
- **Override List** — explicit list of where this project's behavior diverges from root (voice rules, banned patterns, skipped chain steps, etc.)
- Anti-Patterns specific to the client

**Why this exists:** Pre-2026-05-12, every Antigravity session re-encoded global behavior. Client-specific voice/constraints had to be re-prompted each session. Voice mismatches happened. Per-client CLAUDE.md inheritance lets `cd projects/andrea-dj` auto-load Andrea's 12 Non-Negotiables, `cd _active/jen-listings` auto-load Jen's warm-friend voice rules, etc. Adding new clients: copy the structure from any of the 3 worked examples; the contract is uniform.

**Anti-pattern:** Don't duplicate brand bibles in the child CLAUDE.md. Point to the existing brand context files. The child CLAUDE.md is the *inheritance contract*, not the brand archive.

---

## System Primitives (Irreducible Parts)

> **Why this table exists** (Item L of 2026-05-21 synthesis brief): Antigravity has **234 skills + 134 agents + 64 directives + 888 workflow files + 101 Python execution scripts** (counts as of 2026-05-23 — re-grep before assuming). When responsibilities drift, the failure is silent. This table names the irreducible *execution-layer* primitives — each row answers "what owns this responsibility, and what triggers it?" If a future session reassigns one of these owners without updating this table, drift is on us. Source-file column is canonical.

| Primitive | Owns | Triggered By | Source File |
|---|---|---|---|
| `intent_to_package` | Outcome-class detection → assembled mission package (workflow + skills + experts + plugins + cost tier). Prescriptive routing. | `/autopilot` Phase 1; any explicit mission-package request | `execution/intent_to_package.py` |
| `routing_enforcer` | Runtime validation of the CLAUDE.md Mandatory Workflow Routing table. Deterministic, not advisory. | Pre-flight before any binding-matching task; `chain_runner.finalize` post-hoc check | `execution/routing_enforcer.py` |
| `anchor_memory` | Project-scoped persistent context anchors — early-step outputs (brand brief, hero visual) become forced references for every later step. | `/supercomputer` + multi-deliverable missions across phases | `execution/anchor_memory.py` |
| `cost_gate` | Unified pre-flight approval for every paid creative API (Fal, Perplexity, NotebookLM, Gemini). One approve/deny gate, one cost preview. | Every paid-API invocation; `/autopilot` G2 gate (>$5 aggregate) | `execution/cost_gate.py` |
| `taste_signature` | Bimodal taste filter on top of the calibrated rubric. Wave 2 Excellence Lift. Encodes Farrice's "clear PASS or clear FAIL, narrow marginal band" signature. | Inside `chain_runner.finalize` after rubric scoring | `execution/taste_signature.py` |
| `excellence_predictor` | Pre-flight composite prediction + grade-inflation detector. Wave 3. Predicts iteration cost BEFORE execution so effort is budgetable. | `/autopilot` Phase 1 before execution; calibration drift checks | `execution/excellence_predictor.py` |
| `orchestration_ledger` | Post-run trace emitter — what fired, what's next, copy-pasteable refinement prompts. No interrogative — run ends, ledger surfaces. | End of every `/autopilot` session | `execution/orchestration_ledger.py` |
| `chain_runner.finalize` | The single atomic call that owns Step 6: quality gate + caps enforcement (`_enforce_caps`) + Notion log + protocol tracking + session state + post-hoc routing check. Expert output without `finalize` is incomplete. | Step 6 of every expert-domain deliverable | `execution/chain_runner.py` |
| `recall_logger` | Observability for silent Tier 1.5 grounding decisions. Closes the AI-Memory-Dependent-Observability failure class. | Every Recall search attempt; auto-fires from `finalize` as deterministic backstop | `execution/recall_logger.py` |
| `eval_harness` | Score outputs against the anchored rubric (`evolution_store/ground_truth/rubric_v1.md`). Worked-example calibration drift detection. | Manual scoring; weekly `evolution_orchestrator` runs | `execution/eval_harness.py` |

**Rule of inheritance**: a workflow may compose any number of these primitives, but it does not duplicate their logic. If a workflow's markdown reimplements one of these, that's drift — the primitive's source file is the contract.

**Atom-vs-system taxonomy** (skill-layer architecture) is a *sub-classification* underneath this primitive table, not a competing layer. See the dedicated section below.

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
stylized poster generation (vintage, Swiss, Ukiyo-e, brutalism, neon-noir, editorial, real-estate, typography-first chalkboard/menu/packaging/UI mockups, etc.) / "make a poster" / "edit this poster" / "make a transparent logo" → `skills/fantastic-posters/` (Fal + GPT Image 2, **38 styles**, full surface: text-to-image · `--input`/`--mask` edit (see `directives/fal-edit-mode-guide.md`) · `--variants=N` (1-4 in single API call) · `--rembg` (chained transparency) · sizes up to 3840×2160 (`--size=banner-3to1|hero-2to1|poster-xl|WxH`). MUST gate via `execution/fal_budget_guard.py check --mode=<poster|edit|rembg>`),
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
| Competitive intelligence requiring live primary-source quotes / screenshots / JS-rendered pages | `/competitor-intel` or `/spy-market` skill + Playwright per `directives/browser-automation-routing.md` for primary-source quotes/screenshots | Generic WebFetch text scrape (returns hydration shells on Webflow / Framer / Next.js sales pages) |
| Login-gated source verification (LinkedIn profile facts, Substack analytics, MLS data, paywalled research) | Playwright with persistent profile per `directives/browser-automation-safety.md` + `directives/browser-automation-routing.md` (Tier 1 read-only — auth content access) | WebFetch (returns login wall HTML, not actual content) |
| Source material includes a video URL or local video file (extract / extract-forge / parallel-extract / extract-vision / extract-amplify / convert-extraction / extract-principle / sinem-50-notes-extract / watch-and-remix / lookalike-content / format-scan / hidden-gems / style-from-creator / hook-formula-extract / talking-points / 4c-architect / atomize / knowledge-alchemy / mcclain-source-to-agent / art-direct / mood-board / storyboard / parallax) | `python3 execution/fetch-video-context.py "<source>" "<expert>"` (auto-fires from each workflow's `// turbo` block) per `directives/video-vision-protocol.md` | Transcript-only ingestion when source is video — visual hooks, on-screen text, gesture, B-roll patterns are 30-50% of meaning for visual creators. Wrapper auto-skips non-video, >10min videos, uncaptioned-no-Whisper-key, plugin not installed — never blocks parent workflow |
| Brand Operating System / "BOS" / "build a complete brand system" / Resonance-style package / 6-layer brand build (foundation + visual + briefs + marketing + AI handoff + ops) | `/build-bos` (orchestrates 7-phase build via `skills/brand-operating-system/`) | `agents/brand-system-builder/` direct invocation (Phase B component, not orchestrator), `/design-md-synthesize` alone (Phase C component), `/brand-library` alone (Phase C component) — single-component skills are valid for single-layer scopes only |
| Multi-deliverable marketing/creative mission — "build me a brand for X", "make me a campaign for X", "launch [product] on [platform]", "full marketing for X", "full content drop on X", "[hero shot] AND [listing visuals] AND [ad concepts] for X" (cross-deliverable cohesion required) | `/supercomputer` (orchestrates anchor-memory + pre-flight cost gate via `skills/supercomputer/` — self-hosted Higgsfield Supercomputer equivalent) | Single-skill execution (`/build-bos` alone, `/parallax` alone, `/fantastic-posters` alone) — Supercomputer mode requires `execution/anchor_memory.py` + `execution/cost_gate.py` enforcement to keep deliverables coherent across phases. Full trigger phrase list in `directives/supercomputer-mode.md`. |
| Gate-suppressed orchestration — "autopilot", "run end-to-end", "no gates", "just execute the whole thing", "true autopilot", "stop asking just do" — user has explicitly opted into running the full chain with only taste-level gates | `/autopilot` (via `.agent/workflows/autopilot.md` — composes via `execution/intent_to_package.py`, predicts via `execution/excellence_predictor.py`, emits ledger via `execution/orchestration_ledger.py`). Three gates only: G1 (intent score ≤2 → sharpen), G2 (paid cost > $5 aggregate → approve once), G3 (prose FLAGGED at Expert Standard ≥7 → taste call). Wave 4 ships Research outcome populated; other classes the resolver tells the user which workflow to invoke directly until Wave 5. | `/supercomputer`, `/jcc-deploy`, `/campaign`, `/big-project` direct invocation — they halt at Phase 1 "Proceed?" even when user said "no gates". Autopilot wraps them and suppresses the halts. Calibration foundation is the Excellence Lift Layer (Wave 1-3): `_enforce_caps` in `execution/chain_runner.py` (AI prose cap, copy calibration cap, factual veto), `execution/taste_signature.py` (5 bimodal rules), `execution/excellence_predictor.py` (pre-flight prediction + grade-inflation detector). Without those, autopilot would inherit the 94-99%-above-8 grade inflation from the pre-Wave-1 quality gate. |

**Why this exists**: A 2026-04-21 session degraded to 6/10 across 4 iterations on a Parallax edition because `writers-room` was invoked by the user's conversational ask and executed literally. `/parallax` was the correct workflow and was never loaded. Root cause captured in `/Users/farricecain/.claude/plans/additional-edits-this-line-fluffy-cake.md`. When user's conversational prompt and system's correct routing disagree, system wins and explains the override in one sentence.

**Why `/autopilot` exists** (2026-05-21): A user feedback session surfaced that "autopilot-like" workflows today (`/supercomputer`, `/jcc-deploy`, `/campaign`) actually NARRATE more than they execute — they halt at gates, give "here's what to run" recommendations, force a review-then-implement loop. The user wants to move UP to the orchestration / taste / refinement / judgment layer. `/autopilot` is the gate-suppression dispatcher built specifically to deliver that: outcome-class detection → mission package assembly → end-to-end run with only taste-level halts → Orchestration Ledger with copy-pasteable refinement prompts. The full plan is at `/Users/farricecain/.claude/plans/based-on-all-of-sprightly-whale.md`.

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
- **Video Vision** (claude-video / `/watch` plugin + `execution/fetch-video-context.py` wrapper): Frame-grounded vision over any video URL or local video file. Auto-fires from 23 workflow integrations whenever source material is a video — adds `extractions/<expert>/visual-context.md` (frame paths + grounded transcript) and `extractions/<expert>/frames/` sidecars. See `directives/video-vision-protocol.md`. Naming: `/watch` (claude-video plugin slash command for interactive use) is distinct from `/watch-and-remix` (existing skill workflow).
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

## Skill Architecture — Atoms vs Systems

> **Operating distinction** (added 2026-05-12): The 232 entries under `skills/` and 886 entries under `.agent/workflows/` divide into two architectural tiers. Naming the distinction makes the compounding layer visible. **Source**: Simon Scrapes ("Agentic OS" + "Skill Systems" videos) integration brief at `_active/system-integration/2026-05-12-agentic-os-elevation-brief.md`.

### Atomic Skill (tier: atom)

Single tool, one job, designed for reuse across many compositions. The smallest functional unit. Atoms compound — upgrading one atom upgrades every system that uses it.

Clear examples in Antigravity:
- `voice-document` / `voice-calibrate` / `voice-niche` — voice capture primitives
- `mood-board` / `creative-prompt` / `name-framework` / `one-liner` — single-deliverable creative tools
- `find-context` / `knowledge-search` / `compile-knowledge` — knowledge retrieval primitives
- `create-skill` / `add-notebook` / `index-conversations` — system maintenance primitives
- `prose-check` / `slop-check` / `verify` / `grounding-pass` — audit primitives
- `generate-image` / `generate-video` / `generate-asset` — single-output generators

**Test**: Does this skill produce one deliverable type via one workflow file with no internal phase gates? → atom.

### Skill System (tier: system)

Multi-phase orchestrated composition. References multiple atoms (or other systems). Has an end-to-end deliverable with explicit phase structure and a clear orchestrator.

Clear examples in Antigravity:
- `/extract-forge` (8 phases: source → vision → extraction → architecture → build → registration → verification → finalize)
- `/parallax` (memoir-grade Substack production with Phase 2.5 ground-check gate)
- `/writers-room` (multi-expert refinement with 9-expert loadout)
- `/jcc-deploy`, `/campaign`, `/strike`, `/solo`, `/refine`, `/upgrade`, `/aar` (JCC mission types — multi-agent coordination)
- `/swarm`, `/parallel-swarm`, `/research-swarm`, `/swarm-research` (parallel expert deployment)
- `/big-project`, `/newsletter-flywheel`, `/authority-flywheel`, `/proof-pipeline`, `/cold-to-close-proof-funnel`, `/launch-day` (production flywheels)
- `/build-bos`, `/brand-arena`, `/zero-to-brand` (multi-phase brand builds)

The orchestrator (SKILL.md + workflow files of a system) carries five responsibilities:
1. **Skill architecture** — which atoms/sub-systems run, in what order
2. **Inputs** — what each phase needs to do its job
3. **Handoffs** — output of phase N becomes clean input for phase N+1
4. **Human-in-loop checkpoints** — explicit halt/proceed gates between phases (Parallax 2.5 is the pattern)
5. **Visual results display** — how output is surfaced (file path, dashboard link, Notion page)

**Test**: Multiple phases that depend on each other? Multiple expert lenses applied in sequence? Explicit gate-and-proceed structure? → system.

### Expert Skills as a Special Case

Many `skills/` entries represent expert methodologies (Lara Acosta, Luke Iha, Cardinal Mason, Wright Thompson, etc.). These are NOT a separate tier — they classify as atom or system depending on scope:
- Expert with a single workflow producing one deliverable type → atom (e.g., `lara-acosta-headline-engineering`)
- Expert with a multi-phase end-to-end production line → system (e.g., `luke-iha-cross-domain`)

Expert skills are "lenses" — they apply a person's methodology to a task. The atom/system question is about whether the lens runs once or chains through phases.

### Sub-Agents Are Not a Third Tier

Sub-agents (per `directives/sub_agent_protocol.md`) provide **context isolation between atoms in a system** — they are an execution-time choice, not an architectural tier. A system MAY spawn sub-agents at multi-expert phases; an atom typically does not. Sub-agent protocol currently has 0 recorded activations — this is the dormant-but-documented orchestration tissue the 2026-05-12 brief identifies as load-bearing for the "feels like a unified system" experience.

### Frontmatter Convention

Skills are progressively annotated with `tier: atom | system` in SKILL.md frontmatter. The label is **advisory**, not load-bearing — most skills can stay unlabeled until usage clarifies. Highest-leverage atoms are labeled first; ambiguous cases stay unlabeled. Workflows in `.agent/workflows/*.md` inherit the tier of their parent skill.

### Why This Distinction Matters

When the system feels like "a toolbox, not a unified system," the cause is usually that the same word ("skill") points to both a screwdriver and an entire workshop. Atoms compound across systems; systems are composed from atoms. The compounding layer is where the "feels unified" sensation comes from — and it only becomes visible once atom-vs-system is named.

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
| **Video Vision Auto-Fire** | **Source-ingestion step of any of 23 video-aware workflows (extract family, video-study workflows, Creative Director, parallax)** | **`directives/video-vision-protocol.md` — wrapper at `execution/fetch-video-context.py` invokes the claude-video plugin (`/watch`) to produce frame-grounded `visual-context.md` sidecars. Exit codes: 0 OK / 2 SKIPPED / 1 FAILED. Never blocks parent workflow.** |
| **Workflow Gate Convention** | **Mid-execution phase boundaries in system-tier workflows (production-from-scratch, multi-expert ensemble, public-facing output, chain_runner-touching code)** | **`directives/workflow-gate-convention.md` — structured halt/proceed gates with explicit conditions + skip syntax. Distinct from quality_gate.md (post-execution 4-dim scoring). Gold-standard implementation: Parallax Phase 2.5. Worked example shipped 2026-05-12: writers-room Phase 2.5.** |

### Budget-Gated (check before calling)

**Research priority order (2026-04-23 — Gemini primary)**: Foundation/Standard/Deep research → Gemini Deep Research FIRST (`/deep-research-gemini`). Perplexity is fallback + quick-facts only. See `directives/research-protocol.md` for the full priority matrix.

| Protocol | Directive | Gate |
|----------|-----------|------|
| **Deep Research (Gemini) — PRIMARY** | `directives/google-api-usage-policy.md` | 3-layer defense: Ultra covers AI Studio (primary) + pay-as-you-go explicitly OFF + $10 prepaid ceiling. Track in `.agent/gemini-api-usage.json`. Invoked via `/deep-research-gemini` or `execution/deep_research_client.py`. Max possible spend: $10. **Use this first for any foundation/strategic research.** |
| Perplexity — FALLBACK + quick facts | `directives/perplexity-usage-policy.md` | $30/mo, track in `.agent/perplexity-usage.json`. Fires automatically when Gemini Deep Research unavailable. Also for single-claim fact checks via sonar-pro/ask. |
| NotebookLM | `directives/notebooklm-usage-policy.md` | 100/mo, track in `.agent/notebooklm-usage.json` |
| Apify | `directives/apify-usage-policy.md` | $29/mo Starter plan, track in `.agent/apify-usage.json`. Use for scraping/social listening; falls back to Perplexity at 90% cap |
| **Fal API (fantastic-posters + video)** | `directives/fal-usage-policy.md` · `directives/fal-edit-mode-guide.md` | $20 wallet w/ $5 refill threshold, track in `.agent/fal-usage.json` (v2 mode-aware). **MANDATORY pre-flight gate**: every Fal call must pass `python3 execution/fal_budget_guard.py check --mode=<...>` first. Modes: `poster` ($1 ceiling), `edit` ($1), `rembg` ($0.10, chained transparency), `kling` ($2), `seedance-480p` ($1.50), `seedance-720p` ($3), `seedance-1080p` (HARD-BLOCKED, no override). Cross-mode: per-day $6, per-cycle $15, rate-limit 5/5min, halt after 2 consecutive failures. Hookify enforced. Wrappers: `./gen.sh` (posters/edit/rembg), `execution/fal_video_kling.py`, `execution/fal_video_seedance.py`. |
| **Whisper API (video-vision fallback)** | `directives/video-vision-protocol.md` | Deferred — only fires when claude-video processes an uncaptioned video AND `--whisper` flag is passed. Default behavior: `fetch-video-context.py` exits 2 (SKIPPED) with `reason=uncaptioned_no_whisper_key`. To activate: set `GROQ_API_KEY` in `.env` (Groq Whisper preferred — pennies per video; OpenAI Whisper fallback if Groq unavailable). Most YouTube has native captions — Whisper rarely needed. |

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
