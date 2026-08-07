# Integration Brief: Agentic OS Pattern Elevation

**Date:** 2026-05-12
**Sources:** Simon Scrapes — *"THIS Gives Claude Skills a Massive Upgrade"* + *"Creating Your Own Agentic OS is Easy"* (unified extraction)
**Trigger:** User feeling that "workflows are individual tools, not a unified system"
**Method:** `/extract-forge` redirected to Pattern-Integration Run per `feedback_extract-forge-gate-first.md`
**Companion doc:** `extractions/agentic-os-integration/pattern-inventory-and-delta.md`

---

## Executive Answer (One Paragraph)

The "missing piece" the user is feeling is real, but it is not new capability — it is **architectural language and protocol activation**. Antigravity ships 232 skills, 135 agents, 886 workflows, six layers of memory, and a quality-ratchet evolution engine. By component count, it is more sophisticated than the system Simon Scrapes describes across both videos. But two of Antigravity's core orchestration protocols (`sub_agent_protocol.md`, `agent-loading-protocol.md`) have **zero recorded activations** since they were created. JARVIS.md, the operator-level interface doc, is four months stale. There is no explicit distinction in the file tree or vocabulary between **atomic skills** (the 10-30 reusable building blocks Simon describes) and **skill systems** (the orchestrated compositions that chain them) — every directory under `skills/` is called a skill, whether it's a single tool or an 8-phase production line. The result is a system that *behaves* like a unified OS most of the time but that the user *experiences* as a toolbox, because the connective tissue is documented but inactive and the vocabulary obscures the layer where compounding happens. The fix is not to build new infrastructure. It is to (a) name the layer that already exists, (b) activate the protocols that already exist, and (c) wire the inheritance pattern that Claude Code itself already supports.

---

## Top 5 Integration Moves (Ranked by Leverage)

### MOVE 1 — Codify "Atomic Skill" vs "Skill System" Vocabulary

**Why this is first**: Every other move gets clearer once the user can name the difference between a building block and an orchestration. Without this naming, the user sees 232 entries in `skills/` and feels overwhelmed; with it, they see ~30 atoms + ~200 systems and feel oriented.

**What changes:**
- Add a section to `CLAUDE.md` after "Architecture (3-Layer)" titled **"Skill Architecture — Atoms vs Systems"** that defines:
  - **Atomic skill** = single tool, one job, designed for reuse across many systems (e.g., `voice-document`, `fetch-video-context`, `mcp-builder`, `creative-direction`)
  - **Skill system** = multi-phase composition with orchestrator logic, references multiple atomic skills, has an end-to-end deliverable (e.g., `/extract-forge`, `/parallax`, `/jcc-deploy`)
  - The orchestrator skill carries the five responsibilities from Simon Scrapes V1.2: architecture / inputs / handoffs / human-in-loop / visual display
- Annotate `SKILL_INDEX.md` and `AGENT_INDEX.md` with an explicit `tier: atom | system` field
- Add `tier:` to skill frontmatter for the ~30 highest-leverage atoms first (don't try to label all 232 — pareto)

**Files touched:** `CLAUDE.md`, `SKILL_INDEX.md`, `AGENT_INDEX.md`, ~30 SKILL.md files (highest-leverage atoms only).

**Expected effect:** When the user opens `skills/`, they can sort by tier. Workflows can declare "this composition uses these atoms" → compounding becomes visible. Future skill creation has a default question — "is this an atom or a system?"

**Risk:** Categorization debates ("is `creative-direction` an atom or a system?"). **Mitigation:** Start with the 5-10 unambiguous atoms first; let the rest stay unlabeled until usage clarifies.

**Rollback:** Revert frontmatter additions. No structural changes; pure metadata.

---

### MOVE 2 — Activate the Sub-Agent Protocol Via Deterministic Triggers

**Why this is second**: The protocol exists at `directives/sub_agent_protocol.md` (154 lines, detailed, with auto-spawn triggers documented). Activation count = 0. This is the textbook `feedback_ai-memory-dependent-observability.md` failure: infrastructure built but never fires because it depends on Claude remembering. Same fix pattern: deterministic backstop.

**What changes:**
- Update `chain_runner.py finalize` to log when a deliverable was produced WITHOUT sub-agent spawn for tasks that match auto-spawn triggers (>50 line code change, multi-file refactor, 2+ experts, 10+ files loaded). Log to `evolution_store/sub_agent_misses.jsonl`.
- Add a pre-execution check in 5-10 high-leverage workflows (`/parallax`, `/extract-forge`, `/campaign`, `/jcc-deploy`, `/big-project`) that explicitly invokes sub-agents via the `Agent` tool at their multi-expert phases — not "consider spawning" but a hard call.
- After 30 days, audit the misses log: if Claude still consistently skips sub-agent spawns on qualifying tasks, escalate to `chain_runner.py finalize` blocking the gate when a qualifying task wasn't sub-agented.

**Files touched:** `execution/chain_runner.py`, 5-10 workflow files in `.agent/workflows/`, new log file `evolution_store/sub_agent_misses.jsonl`.

**Expected effect:** The orchestration tissue starts firing. Context-pollution issues during long sessions decrease. Multi-expert work becomes truly multi-expert instead of single-thread emulating multiple voices.

**Risk:** Sub-agent spawn adds latency + token cost for tasks that don't actually need isolation. **Mitigation:** Restrict triggers to genuinely qualifying tasks (2+ experts OR 10+ files OR 50+ line code change). Don't sub-agent trivially.

**Rollback:** Remove pre-execution checks; revert `chain_runner.py` logging line.

**Constraint check:** This does NOT add `.claude/agents/` subagent files (per `feedback_no-claude-code-subagents.md` — banned). It uses the `Agent` tool for context-isolated sub-agents, which is permitted and distinct.

---

### MOVE 3 — Per-Client CLAUDE.md Inheritance

**Why this is third**: The Claude Code parent-folder inheritance feature is real, Antigravity is not using it, and the user has multiple active clients (Jen, Javier, Andrea, MyBPM, Parallax-self, Farrice-brand) whose specifications conflict with each other ("warm and enthusiastic" for Jen vs "memoir-grade interiority" for Parallax). Today the user re-prompts these constraints every session.

**What changes:**
- Create `projects/<client>/CLAUDE.md` for 3-5 active clients with:
  - One-paragraph identity for this client's voice/constraints/non-goals
  - Pointer to client-specific brand context (`_active/<client>/brand/`)
  - Override list — what aspects of root CLAUDE.md don't apply (e.g., "Skip Step 5.5 verification for memoir content")
- Document the inheritance pattern in root CLAUDE.md so future client folders follow it
- For Jen Santulan (highest-leverage client): create `_active/clients/jen-santulan/CLAUDE.md` first as the worked example

**Files touched:** 3-5 new `projects/<client>/CLAUDE.md` files; one paragraph added to root `CLAUDE.md` documenting the pattern.

**Expected effect:** When user `cd`s into a client folder, the per-client context loads automatically. Voice mismatches stop happening at session start. Each client folder becomes truly self-contained.

**Risk:** Parent-child conflicts where child CLAUDE.md doesn't make it clear what's being overridden. **Mitigation:** Mandatory "Inherits from root CLAUDE.md except:" header at top of every child CLAUDE.md.

**Rollback:** Delete child CLAUDE.md files; revert root paragraph.

---

### MOVE 4 — Explicit Human-In-Loop Gates as Workflow Default

**Why this is fourth**: Parallax Phase 2.5 ground-check is the only place in the system with an explicit halt/proceed gate, and it exists ONLY because Edition 02 shipped with 7 fabrications. Every other production workflow proceeds end-to-end on the assumption that Claude has the context. This is the structural risk that produced the Tess Barclay forge near-miss and the Edition 02 fabrications.

**What changes:**
- Add a "Workflow Gate Convention" section to `directives/quality_gate.md`:
  - Multi-phase workflows MUST declare gate points (phase boundaries where user explicitly approves to proceed)
  - Production-from-scratch workflows MUST gate before generation (Parallax 2.5 pattern as default)
  - Refinement-on-existing workflows MAY gate after diagnosis, before rewrite
- Audit the top 10 production workflows (Parallax, extract-forge, campaign, jcc-deploy, brief, parallel-content, content-bundle, big-project, parallel-extract, content-sprint) and add explicit gates where they're missing
- Pattern: a gate is a phase that produces a TWO-PATH output (proceed conditions + halt conditions) and a clear question for the user

**Files touched:** `directives/quality_gate.md`, ~10 workflow files.

**Expected effect:** The fabrication-class of failures becomes structurally hard to repeat. User feels in control of long workflows rather than discovering bad output after 8 phases.

**Risk:** Too many gates = workflow feels bureaucratic. **Mitigation:** Cap at 2-3 gates per workflow; reserve for genuinely high-stakes phase boundaries (verification, before public-facing output, before client delivery).

**Rollback:** Revert workflow edits; the directive section is additive (won't break anything if reverted).

---

### MOVE 5 — JARVIS.md Refresh (Operator-Level Interface Sync)

**Why this is fifth**: JARVIS.md is the doc that says "how to talk to your council." It's 4 months stale (last updated 2026-01-23), references a "19 expert council" when the system has 135 agents, and lists experts (Cardinal Mason, Jeremy Miner) that may or may not still be the active roster. This file is what an operator (the user, or a hypothetical second user) reads to understand HOW to use Antigravity at the OS level.

**What changes:**
- Rewrite JARVIS.md to reflect the current system:
  - 135 agents, organized by domain (not enumerated)
  - The atom-vs-system distinction from Move 1
  - The sub-agent activation pattern from Move 2
  - Pointer to per-client CLAUDE.md from Move 3
  - The "deterministic backstop" principle from `feedback_ai-memory-dependent-observability.md`
- Update DOMAIN_REGISTRY.md cross-reference if needed
- Mark JARVIS.md as "Last full review: 2026-05-12" with a 60-day review reminder

**Files touched:** `JARVIS.md` (full rewrite), small touch on `DOMAIN_REGISTRY.md`.

**Expected effect:** JARVIS.md becomes the actual front-door doc again. When the user wants to remember how to invoke a council or hand off between experts, this file matches reality.

**Risk:** Documentation churn — the rest of the system continues to evolve; the rewrite is stale within 90 days. **Mitigation:** Build the 60-day review reminder into the doc itself.

**Rollback:** Restore the previous version from git.

---

## Sequencing

**Phase A (immediate, low risk, high signal): Move 1 + Move 5**
- Codify vocabulary, refresh the operator-level doc. These are documentation changes; they don't change runtime behavior but they re-orient the user's mental model. Done together because Move 5's rewrite needs Move 1's vocabulary.

**Phase B (after Phase A): Move 3**
- Per-client CLAUDE.md inheritance. Client work is real now; this pays off immediately. Done alone because it changes per-project behavior and benefits from being tested on one client (Jen) before rolling to others.

**Phase C (after Phase B): Move 4**
- Workflow gates. Touches production workflows; needs Phase A's vocabulary in place so the gates are described against the right architectural model.

**Phase D (most ambitious, last): Move 2**
- Sub-agent protocol activation. Touches `chain_runner.py` (load-bearing code) and 5-10 workflows. Highest risk because it changes how long runs allocate context. Save for last so Phase A-C have settled.

---

## Honest Rejection List (Patterns NOT to Integrate)

### REJECTED: V1.4 sub-agent pattern as Claude Code subagents
**Why:** `feedback_no-claude-code-subagents.md` (2026-05-02) bans `.claude/agents/` operator subagents based on Coach Cooz failure + routing pollution. The video's pattern is permitted via the `Agent` tool (context-isolation) and that's what Move 2 implements. **Do not interpret the video as license to revisit the subagent ban.**

### REJECTED: V2.1 AI-interview-to-build identity file
**Why:** CLAUDE.md and FARRICE.md are more sophisticated than what a 15-question interview would produce. The video's pattern is good for new users; user is past that stage.

### REJECTED: V2.4 simple learnings.md self-learning loop
**Why:** Antigravity has a 4-dimension quality gate, evolution orchestrator, feedback ratchet, regression detection, and grade inflation auditing. A learnings.md file would be a regression. **However**: the 2026-04-24 audit found 94-99% of finalize scores were 8+ (grade inflation). The fix for that is anchored rubric calibration (already in `evolution_store/ground_truth/rubric_v1.md`), not a simpler feedback loop.

### REJECTED: V2.9 VPS hosting + Telegram channels
**Why:** Real gap, but tangential to the "unified system" feeling. Mobile access doesn't fix the felt issue. **Defer** until/unless the user wants to operate Antigravity from phone, at which point revisit.

### REJECTED: Sub-agents as the default for everything
**Why:** Even the videos limit this to specific qualifying triggers. Aggressive sub-agent use balloons cost without quality gain on short tasks. Move 2 keeps the threshold high.

---

## Constraint Validation (Sanity Check)

Before any Phase 5 execution, every move must pass these checks per existing feedback rules:

- [x] No `.claude/agents/` subagent files created (per `feedback_no-claude-code-subagents.md`)
- [x] No AI-memory-only manual invocation paths added — every "should fire" has a deterministic backstop (per `feedback_ai-memory-dependent-observability.md`)
- [x] No auto-evolution without human anchors — Move 2's audit at 30 days is human-reviewed, not auto-pruned (per `feedback_auto-evolution-cant-substitute-for-ground-truth.md`)
- [x] No fabricated methodology — gate-first redirect was honored; videos treated as architectural source, not expert methodology (per `feedback_extract-forge-gate-first.md`)
- [x] Per-client CLAUDE.md additions tested on one client first (per `feedback_client-spec-first-then-pivot.md`)

---

## What This Brief Is NOT

- Not a critique of the existing system. Antigravity is more capable than the system the videos describe. The diagnosis is **dormant capability**, not absent capability.
- Not a refactor proposal. No file moves, no deletions, no renames. Every move is additive or label-level.
- Not a new product. There is nothing to ship to anyone external. This is internal system clarity.
- Not urgent. The system functions today. These moves compound the system's coherence; they don't unblock anything.

---

## Falsification Criteria + Success Metrics (Added 2026-05-12 post-finalize retry)

The strongest critique of this brief is *"where's the falsifiable test?"* — it diagnoses the felt gap as architectural language + protocol activation, but doesn't say what would prove that diagnosis wrong or what success looks like after each move. This section closes that gap.

### Diagnosis Falsification

The core diagnosis — *"missing piece is architectural language + protocol activation, not new capability"* — would be **wrong** if any of these turn out to be true:

1. **User reads CLAUDE.md atom-vs-systems section + JARVIS.md v2.0 and reports "I still feel the same fragmentation."** Then the issue was never vocabulary; the felt experience is pointing at something the brief didn't capture.
2. **A 30-day observation of skill invocations shows users (or Claude) consistently pick the wrong tier-tier combination** despite the new vocabulary. Then the labels don't help where the friction actually lives.
3. **Activating the sub-agent protocol (Phase D Move 2) produces no measurable quality improvement** in `chain_runner.py finalize` 4-dimension scores on multi-expert workflows. Then the protocol's 0 activations were a *correct* under-use, not a dormant capability gap.
4. **Per-client CLAUDE.md inheritance (Phase B Move 3) creates more confusion than it removes** — measured by client-session voice mismatches per month before/after. Then the inheritance pattern wasn't the issue.

If 1 or 2 fires after Phase A, halt the brief's sequencing and re-diagnose. If 3 or 4 fires after Phase B/D, roll back that specific move.

### Per-Move Success Metrics

| Move | Success criterion (testable) | Time horizon | Anti-success signal (rollback trigger) |
|------|-----------------------------|---------------|---------------------------------------|
| 1 (atom-vs-system vocab) | User can sort `skills/` mentally into atoms / systems / unsure within 2 weeks of reading the CLAUDE.md section. Next 5 new skills created have `tier:` in frontmatter from day one. | 14 days | User finds the vocabulary "more confusing not less" or stops using it within 30 days. |
| 5 (JARVIS.md refresh) | User opens JARVIS.md when onboarding a new collaborator or reminding themselves of invocation patterns AND it matches actual system behavior (no "wait, that's stale"). | 30 days | User catches a JARVIS.md claim that contradicts current system state within first 60 days. |
| 3 (per-client CLAUDE.md) | Next 3 client sessions auto-load correct voice/constraints with zero session-start re-prompting. Voice-mismatch incidents drop from baseline. | 60 days | Parent-child CLAUDE.md conflicts produce 2+ ambiguous-state sessions in first 30 days. |
| 4 (workflow gates) | Top 10 production workflows surface explicit halt/proceed gates. Zero fabricated-fact incidents (Parallax Ed 02 class) on gated workflows. | 90 days | Gates feel bureaucratic — user disables them or skips them via override flags >25% of the time. |
| 2 (sub-agent activation) | `evolution_store/sub_agent_misses.jsonl` shows >50% reduction in "qualifying task ran without sub-agent" over 30-day window. Composite quality scores on multi-expert workflows increase >0.5 points vs 30-day pre-activation baseline. | 30-60 days | Activation adds latency/cost with no quality improvement >0.3 points. |

### Measurement Hooks That Already Exist

These metrics can be measured with current infrastructure — no new tooling required:

- `chain_runner.py finalize` already logs 4-dimension scores per deliverable → quality movement is queryable
- `execution/eval_harness.py calibrate --days 30` already detects score drift
- `evolution_store/traces/routing_decisions.jsonl` already logs routing choices → tier-tier mismatches surface
- `directives/feedback-ratchet.md` already triggers `/skill-evolution` on 3+ regressions → bad moves get caught
- Notion Performance Log already aggregates outcomes → user can review before/after monthly

### What This Brief Refuses to Predict

- **Whether the user will feel different after Phase A.** Subjective gap-closing isn't measurable in advance; it can only be tested by shipping and observing.
- **The right ordering of B/C/D.** Recommended A → B → C → D, but if Phase A reveals the felt gap was per-client context all along, jump straight to B.
- **Whether Move 2 will ever be necessary.** Sub-agent activation might be the load-bearing move, OR it might be a sophisticated answer to a problem that doesn't exist for the user's actual workflow. Phase D is gated on observation, not assumption.

---

## Recommendation

Execute **Phase A** (Move 1 + Move 5) first. Both are pure documentation; together they take 1-2 hours and immediately re-orient how the user reads the system. Defer Phases B/C/D pending Phase A landing. If Phase A clicks ("yes, I see the system differently now"), proceed. If it doesn't ("vocabulary feels artificial, I prefer the current state"), halt and re-examine the original premise.

The user opened with conviction: *"a missing piece to elevate and enrich our entire operating system."* The diagnosis above suggests there is no missing piece — but there is a clarifying piece, and the difference matters. The cost of being wrong here is low (documentation changes are reversible). The cost of fabricating new infrastructure to chase a felt gap that's actually a vocabulary issue would be high.
