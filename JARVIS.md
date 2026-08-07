<!--
Copyright © 2025-2026 Farrice Cain
Antigravity AI System - Proprietary and Confidential
Unauthorized reproduction, distribution, or modification prohibited
See LICENSE.md for details
-->

# JARVIS Interaction Protocol (v2.0)

> Your unified interface for operating Antigravity at the OS level. How to invoke experts, compose skill systems, isolate context via sub-agents, and let the orchestration tissue fire deterministically instead of by memory.

**Status:** Refreshed 2026-05-12 against current system (135 registered agents, 232 skills, 886 workflows). Next full review: 2026-07-12 (60 days).

---

## Core Principle

You operate on top of a structured orchestration system, not a generic chat tool. The system has:

- **A council of experts** (currently 135 registered agents — see `DOMAIN_REGISTRY.md` for swim lanes and `agents/_framework/invocation-cards.md` for routing cards, not a hardcoded list in this file)
- **A skill library** that divides into **atoms** (single-purpose tools) and **systems** (multi-phase orchestrated compositions) — see CLAUDE.md "Skill Architecture — Atoms vs Systems"
- **A loading protocol** that escalates from card-check (Tier 0) to deep load (Tier 2) to sub-agent (Tier 3) — `directives/agent-loading-protocol.md`
- **Quality + evolution tissue** that learns from every finalized deliverable — `directives/feedback-ratchet.md`, `evolution_store/`

Your experts don't just answer questions — they think alongside you. Your skill systems don't just produce one output — they chain atoms into compounding workflows. JARVIS is the protocol for accessing all of that naturally.

---

## Invocation Methods

### 1. Direct @Mention (Single Expert)

```
@cardinal-mason Help me write a sales email for a SaaS product
@jeremy-miner How do I handle the "I need to think about it" objection?
@shaan-puri Tell me a story framework for my podcast intro
```

**System behavior:** Reads the agent's `agents/<expert>/AGENT.md` (Tier 1 standard load) + `memory/context.md`, embodies persona for the response. For creative/complex work, escalates to Tier 2 (add genius.md). For 2+ experts or 10+ files loaded, escalates to Tier 3 (sub-agent).

**Discovery:** Don't memorize the expert roster. If you don't know who to invoke, describe the task — the system routes via `DOMAIN_REGISTRY.md`.

---

### 2. Natural Language Request (System Routes)

```
"I need help with copywriting"          → primary copywriting expert + ensemble
"How should I price this offer?"        → Samuel Thompson + Revenue Council
"Make this content more engaging"       → Content Council
"I'm preparing for a sales call"        → Jeremy Miner + Michael Bernoff
```

**Routing logic** (per `directives/intent-pipeline.md`):
1. SCORE intent (1-5) — does the request have a clear deliverable, audience, context, end-state, specific language?
2. SHARPEN if Score ≤ 3 — ask missing dimensions, one round max
3. ROUTE — match domain → expert(s) via DOMAIN_REGISTRY + invocation-cards
4. LOAD — Tier 1.5 (Recall grounding, automatic) → Tier 1 (SKILL.md) → escalate as needed
5. PRODUCE — execute using loaded expert frameworks (their thinking, not their terminology)
6. FINALIZE — 4-dimension quality gate via `chain_runner.py finalize`

---

### 3. Slash Command / Skill System

```
/parallax                          # Multi-phase Substack production
/extract-forge                     # 8-phase mastery extraction
/writers-room                      # Multi-expert refinement
/jcc-deploy                        # JCC mission — full deploy
/build-bos                         # 7-phase brand operating system build
```

Slash commands invoke **skill systems** (multi-phase orchestrators). The system loads `.agent/workflows/<name>.md` and executes per its phase structure. Atom-tier slash commands (e.g., `/voice-document`, `/name-framework`, `/mood-board`) produce single deliverables; system-tier commands chain phases with gates.

**Full list:** `SLASH_COMMANDS.md`. **Mandatory routing overrides:** see CLAUDE.md "Mandatory Workflow Routing" table — system wins over user's literal ask when the bound workflow is the right tool.

---

### 4. Council Invocation (Multi-Perspective)

```
@revenue-council What's wrong with my pricing strategy?
@content-council Review this newsletter draft
@brand-council How should I position myself in this market?
@ai-council What's the best way to automate this workflow?
@creative-council Give me direction for this visual project
```

**Council behavior:**
1. Each council member loads at Tier 1
2. Each provides their unique perspective using their actual frameworks
3. Perspectives synthesized — areas of agreement + disagreement explicit
4. Final recommendation weighs each expert's domain relevance

Council membership lives in `COUNCIL.md`. **Don't rely on JARVIS.md to enumerate it** — that list drifts.

---

### 5. Multi-Expert Synthesis (Custom)

```
"What would @cardinal-mason and @harry-dry both say about this landing page?"
"Get @jeremy-miner and @michael-bernoff's take on this sales conversation"
"Synthesize @mitch-albom and @dan-wang for this writing project"
```

**Synthesis protocol** (Tier 3 sub-agent territory when 2+ experts loaded):
1. Spawn parallel sub-agents (one per expert) for context isolation — per `directives/sub_agent_protocol.md` parallel execution rules
2. Each expert analyzes from their framework
3. Synthesis layer: overlaps (consensus wisdom), unique contributions, conflicts with reasoning
4. Integrated recommendation

---

## Skill Architecture — Atoms vs Systems (Operating Distinction)

> See CLAUDE.md "Skill Architecture — Atoms vs Systems" for the canonical definition (added 2026-05-12).

**Quick reference for JARVIS-level invocation:**

| Tier | What it is | Examples | When to invoke |
|------|------------|----------|----------------|
| **atom** | Single tool, one job, designed for reuse | `/voice-document`, `/name-framework`, `/mood-board`, `/one-liner`, `/find-context`, `/knowledge-search`, `/prose-check` | Quick single-deliverable tasks. No internal phase gates. |
| **system** | Multi-phase orchestrated composition with gates | `/parallax`, `/extract-forge`, `/writers-room`, `/jcc-deploy`, `/campaign`, `/build-bos`, `/big-project`, `/newsletter-flywheel`, `/authority-flywheel` | End-to-end production. Multi-expert. Explicit human-in-loop gates between phases. |

**Why this matters at the JARVIS level:** When you can name what tier a skill is, you can predict its behavior. Atoms produce one thing fast. Systems chain phases, gate for approval, and compound. Don't invoke a system when an atom does the job; don't invoke an atom when the task needs a system's orchestration.

**Expert skills (Lara Acosta, Luke Iha, Cardinal Mason, etc.)** classify as atom OR system depending on whether their workflow runs once or chains through phases. Most expert skills are atom-tier with the expert's methodology applied to a single deliverable type.

---

## Sub-Agent Activation (Context Isolation)

Sub-agents (per `directives/sub_agent_protocol.md`) are the system's way of giving each phase of a skill system its own clean context window. They are not extra experts — they are **execution-time context isolation**.

**Auto-spawn triggers:**

| Trigger | Archetype | When |
|---------|-----------|------|
| 2+ experts loaded | SkillExecutor | Multi-expert workflows (`/roundtable`, `/swarm`, ensemble) |
| 10+ files in main context | SkillExecutor | Long sessions where context pollution is starting |
| Major code change (50+ lines) | CodeReviewer | After change, before marking done |
| Deep research mid-task | Researcher | When main task needs data without context pollution |
| Pre-deployment | CodeReviewer | Before `modal deploy` or production push |

**Status (2026-05-12 Phase D — Observability Shipped):** The protocol now has a **deterministic backstop** in `execution/chain_runner.py finalize()`. Every chain finalize call where `--workflow` is in the qualifying set AND `--sub-agents 0` (or omitted) logs a miss to `evolution_store/sub_agent_misses.jsonl`. Soft warning printed in finalize output — no gate-blocking yet. 30-day review on 2026-06-12 to decide whether to escalate to blocking or remove false-positive workflows from the qualifying set. **Reporting actual spawns:** pass `--sub-agents N` flag. Full syntax + explicit Agent-tool spawn patterns: `directives/sub_agent_protocol.md` "How to Spawn" section.

**Banned pattern (per `feedback_no-claude-code-subagents.md` 2026-05-02):** Do NOT create files under `.claude/agents/`. The sub-agent pattern here uses the `Agent` tool for in-conversation context isolation, NOT Claude Code's `.claude/agents/` operator-level subagents. These are different and only one is permitted.

---

## Interaction Modes

### Advisory Mode (Default)
Expert provides analysis, recommendations, frameworks.

```
User: @cardinal-mason What's wrong with this email?
Cardinal Mason: [Analysis using 7 Principles, specific recommendations]
```

### Execution Mode
Expert creates deliverables using their frameworks.

```
User: @cardinal-mason Write me a 5-email welcome sequence
Cardinal Mason: [Executes using email sequence workflow, creates full deliverable]
```

### Teaching Mode
Expert explains their methodology, helps you learn.

```
User: @jeremy-miner Teach me NEPQ
Jeremy Miner: [Explains framework, examples, practice scenarios]
```

### Debate Mode
Multiple experts argue different perspectives.

```
User: @revenue-council Debate whether I should raise or lower my prices
[Each expert argues their position, agreement/disagreement highlighted]
```

---

## Memory & Context (6-Level Stack)

Antigravity ships all 6 levels of the memory hierarchy. Most operations use Levels 1–3; Levels 4–6 are bolt-ons for specific needs.

| Level | What it is | Where it lives in Antigravity |
|-------|-----------|------------------------------|
| 1 | Static rules (identity files) | `CLAUDE.md`, `FARRICE.md`, `AGENTS.md`, `GEMINI.md` |
| 2 | Session-start hook (deterministic context injection) | `.claude/` hook config — fires on session open (e.g., `/watch` plugin readiness, recall reminders) |
| 3 | Semantic search (meaning-based recall) | **Recall** (3,000+ cards, auto-fires Tier 1.5 per `directives/recall-grounding-protocol.md`) + NotebookLM |
| 4 | Verbatim recall | MEMORY.md system + per-topic memory files |
| 5 | Knowledge base | `knowledge/` (240 files, 1.8M words — Karpathy Wiki via `execution/knowledge_compiler.py`) |
| 6 | Cross-tool memory | Notion integration (5 databases) + Performance Log |

**Cross-expert memory:** Experts can read each other's `memory/context.md` (read-only). Update only your own.

---

## Quality Assurance (The Chain — Step 6 Finalize)

Every expert-domain deliverable runs through `chain_runner.py finalize`:

```bash
python3 execution/chain_runner.py finalize "[what you produced]" \
    --expert [expert-name] \
    --skill [skill-directory-name] \
    --workflow [workflow-name] \
    --type [Content|Strategy|Research|Extraction|Client Work|System|Creative|Analysis] \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "[notes] | Factual Grounding: [1-10] | Verification: [PASS/FAIL/PARTIAL/N/A]"
```

**4-dimension scoring** (anchored rubric at `evolution_store/ground_truth/rubric_v1.md`):
1. Intent Alignment
2. Expert Standard
3. Adversarial Resilience
4. Factual Grounding (Step 5.5 verification)

**Composite < 7 OR any dimension < 6 → retry weakest section, re-finalize.**
**Factual Grounding < 6 (when scored) → delivery BLOCKED.**
**Anchor check at ≥8 scores** — if you can't name the rubric anchor, lower the score (94-99% inflation problem caught 2026-04-24).

---

## Handoff Protocol

When one expert recognizes another's domain is needed:

```
Cardinal Mason: "This copy is solid, but I'm noticing the underlying
offer positioning might need work. This is really @samuel-thompson's
territory — want me to hand off for unit economics analysis?"

User: "Yes, hand off"

[Cardinal Mason summarizes context → Samuel Thompson receives and continues]
```

**Handoff includes:**
1. Summary of work done
2. Key decisions made
3. Open questions
4. Recommended next steps

For automated handoffs in skill systems, the orchestrator manages this — output of phase N becomes clean input for phase N+1 (atom-vs-system contract).

---

## Deterministic Backstop Principle

> Per `feedback_ai-memory-dependent-observability.md` (2026-05-03 — banned pattern after 8 days of dormant Recall grounding).

**Rule:** No piece of orchestration infrastructure can rely solely on JARVIS-the-protocol (or any AI agent's memory) to invoke it. If a behavior is supposed to fire automatically, it must have a deterministic backstop in `chain_runner.py finalize()` or equivalent — a check that runs whether or not the AI remembers.

**Why:** Memory drifts. The protocol gets compressed away. Hooks and explicit invocations in execution code don't.

**Where this applies:**
- Sub-agent spawn on qualifying triggers — deterministic check in `chain_runner.py`, not "Claude remembers"
- Recall grounding at Tier 1.5 — auto-fires from hook, not "Claude remembers"
- Video vision auto-fire — wrapper at `execution/fetch-video-context.py`, not "Claude remembers"
- Routing enforcement — `execution/routing_enforcer.py` runs pre-flight, not "Claude remembers"

**When you add a new must-fire behavior, the question is: where does the deterministic backstop live?**

---

## Decision Framework: Which Expert? (Quick Routing)

For full routing logic, see `DOMAIN_REGISTRY.md` + `directives/expert_auto_routing.md` + `agents/_framework/invocation-cards.md`. Quick mental model:

```
Selling / closing / objections?           → Jeremy Miner (+ Michael Bernoff for mindset)
Copy that converts?                       → Cardinal Mason (+ Harry Dry for examples)
Content / storytelling?                   → Shaan Puri (+ Mitch Albom for premium writing)
LinkedIn / personal brand growth?         → Lara Acosta
Ghostwriting / new media kingmaking?      → Nicolas Cole
Brand / positioning?                      → Oren Klaff / Greg Hoffman / Brand Council
Viral / social content?                   → Seena Rez
AI agents / automation / workflows?       → Nick Saraev / AI Council
Product / launch / unit economics?        → Samuel Thompson
Major business decision (multi-axis)?     → Revenue Council / Jim O'Shaughnessy
DESIGN.md / brand visual system?          → Creative Director (+ /design-md-synthesize)
Extraction (rich source material)?        → /extract-forge (gate-first per feedback)
Substack edition production?              → /parallax (Phase 2.5 ground-check mandatory)
Uncertain?                                → Describe the goal; system routes
```

**Domain keyword auto-invocation** is documented in `DOMAIN_REGISTRY.md` and CLAUDE.md "Mandatory Workflow Routing" table. Don't enumerate it here.

---

## Per-Client Context (Phase B — Shipped 2026-05-12)

Active client projects use Claude Code's parent-folder CLAUDE.md inheritance. When you `cd` into a project folder, the per-client CLAUDE.md loads alongside root.

| Project | File | When it loads |
|---------|------|---------------|
| Andrea / Resonance | `_active/clients/andrea-dj/CLAUDE.md` | Working from `_active/clients/andrea-dj/` or subfolders |
| Jen Santulan | `_active/clients/jen-listings/CLAUDE.md` | Working from `_active/clients/jen-listings/` or subfolders |
| Farrice / Parallax | `_active/farrice-brand/CLAUDE.md` | Working from `_active/farrice-brand/` or subfolders |

Each child CLAUDE.md declares (a) inheritance from root, (b) one-paragraph brand identity, (c) "when to load full context" table, (d) override list (where this project diverges from root), (e) anti-patterns specific to the client.

**Pattern documented in:** root CLAUDE.md "Per-Client / Per-Project CLAUDE.md Inheritance" section under Directory Conventions / File Organization. Future clients: copy any of the 3 existing files as template. **Don't duplicate brand bibles** — child CLAUDE.md is the inheritance contract, not the brand archive.

**Adding a new client:** Create `<projects-or-_active>/<client>/CLAUDE.md` following the same 5-section contract. The inheritance fires automatically; no registration step needed.

---

## Integration Points

JARVIS integrates with:

| System Component | Integration |
|------------------|-------------|
| `CLAUDE.md` | Core operating system. The Chain (Steps 1–6). Architecture (3-Layer). **Skill Architecture (Atoms vs Systems)**. |
| `COUNCIL.md` | Expert registry, council membership |
| `DOMAIN_REGISTRY.md` | Expert swim lanes, compound pairing, routing source-of-truth |
| `FARRICE.md` | Personal context for all experts |
| `agents/_framework/invocation-cards.md` | Tier 0 routing cards (80 tokens/expert) |
| `directives/agent-loading-protocol.md` | Tiered loading (T0 → T3) |
| `directives/sub_agent_protocol.md` | Context isolation, parallel execution, adaptive re-routing |
| `directives/feedback-ratchet.md` | Quality compounding loop |
| `directives/recall-grounding-protocol.md` | Tier 1.5 invisible grounding |
| `execution/chain_runner.py` | Quality gate + Notion log + protocol tracking (the deterministic backstop for The Chain) |
| `execution/evolution_orchestrator.py` | Phase 1-4 evolution loop |
| `knowledge/` | Karpathy Wiki — 240 files, semantic recall via Recall + NotebookLM |

---

## Getting Started (Operator Quickstart)

1. **Quick win**: `@cardinal-mason Help me improve this [paste copy]`
2. **Learn a framework**: `@jeremy-miner Teach me your NEPQ approach`
3. **Multi-perspective**: `@revenue-council Review my pricing`
4. **Run a skill system**: `/parallax` for a Substack edition, `/extract-forge` for mastery extraction
5. **System maintenance**: `/system-pulse` (weekly), `/system-audit` (deeper)
6. **Forgot how something works?** Read the file referenced in CLAUDE.md "Supporting Protocols" — don't ask JARVIS to remember.

Your council is ready. Your skill library is loaded. Your evolution tissue is wired. Just ask.

---

*Last full review: 2026-05-12*
*Refresh trigger: drift > 60 days OR significant architectural change (new tier, new chain step, new protocol category)*
*Protocol version: 2.0*
*Source for v2.0 refresh: `_active/_archive/2026-08-07-sweep/system-integration/2026-05-12-agentic-os-elevation-brief.md` Move 5*
