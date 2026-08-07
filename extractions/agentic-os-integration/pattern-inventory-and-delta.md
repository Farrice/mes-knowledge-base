# Pattern Inventory + Delta Analysis: Simon Scrapes Agentic OS Videos

**Sources (unified extraction):**
- `agentic-os-v1-skills-upgrade/` — "THIS Gives Claude Skills a Massive Upgrade (It's Easy!)" · 12:56 · Simon Scrapes
- `agentic-os-v2-agentic-os/` — "Creating Your Own Agentic OS is Easy (Insanely Powerful)" · 24:34 · Simon Scrapes

**Channel context:** Simon Scrapes runs the "Agentic Academy" community. Videos teach reusable Claude Code architecture patterns. **Not practitioner methodology** (per gate-first redirect) — pure architectural tutorial. Treated as system-design source material.

**Method:** Patterns numbered V1.N (Video 1) and V2.N (Video 2). Each carries (a) what the source shows, (b) timestamp, (c) Antigravity equivalent if any, (d) delta classification.

**Delta classification key:**
- `CONFIRMS` — Antigravity already does this; no change needed
- `EXTENDS` — Antigravity has something similar but the video sharpens it; small refinement worth taking
- `MISSING` — Real gap; would need to add infrastructure
- `CONFLICTS` — Videos teach what Antigravity has explicitly rejected (or rejected for good reason)
- `LANGUAGE` — Antigravity has the capability but lacks the clean naming/distinction the video offers

---

## Video 1 Patterns — Skill Systems Architecture

### V1.1 — Skills are MODULAR BUILDING BLOCKS, not isolated outputs or megafiles

**Source (00:02-04:58):** "Skills are supposed to be modular, composable building blocks. The official line is that Claude can load multiple skills simultaneously and your skill therefore should work well alongside others." Two anti-patterns named: (a) **Skills in isolation** — human is still the glue between them; (b) **Mega-skills** — 1,000-line skill.md that does everything, loses modularity / maintainability / progressive disclosure.

**Antigravity equivalent:** Completion Engine v2.0 architecture (skills/*/SKILL.md + genius.md + workflows/*.md). 232 skills, average ~4 workflows each = 886 total workflow files. SKILL.md files designed to be loaded as units.

**Delta: `CONFIRMS` + `LANGUAGE`** — Architecture is correct. But the field "skill" is overloaded — some skills are atomic (e.g. `voice-document`), others are full compositions with many workflows (e.g. `extract-forge` has 8-phase workflow). The video's clean distinction — **atomic skills vs. skill systems** — is more crisp than current Antigravity vocabulary.

---

### V1.2 — Orchestrator Skill = THE BRAIN of a Skill System

**Source (05:01-06:25):** "Skills are effectively components of the skill system. ... A skill system is a prompt and an instruction set wired around multiple skills." The orchestrator must understand five things:
1. Skill architecture (which skills, what order)
2. Inputs needed for each skill
3. How outputs hand off between skills
4. Human-in-the-loop checkpoints
5. How visual results are displayed

**Antigravity equivalent:** `.agent/workflows/*.md` (886 files) — these ARE orchestrator instructions. CLAUDE.md "Mandatory Workflow Routing" table is the routing layer. `chain_runner.py finalize` is the post-execution gate.

**Delta: `EXTENDS`** — Antigravity workflows largely cover (1)-(3) but are uneven on (4) human-in-the-loop checkpoints and (5) visual results display. Many workflows declare phases but don't surface "pause here for user approval" as explicit gates. **Parallax Phase 2.5 ground+zeitgeist gate** is the gold standard — it has a halt/proceed step. Most workflows lack equivalent.

---

### V1.3 — Skill Library (10-30 atomic skills) → Many Skill Systems

**Source (10:30-11:38):** "You have a skill library, a refined library of, let's say, 10 to 30 skills that you build once and reuse it everywhere. So any changes you make to the transcript skill will automatically be ported into any skill system that's using it. ... A transcript skill feeds into short-form video AND newsletter AND SEO content production."

**Antigravity equivalent:** Skills/agents/workflows directories exist but the **atom vs composition** distinction isn't explicit. The audit shows 124 agent-skill aligned pairs + 61 standalone skills + 10 standalone agents — many of those 61 standalone skills could be atomic building blocks (`creative-direction`, `mcp-builder`, `frontend-design`, `gemini-api-dev`, etc.) but they're not labeled as such.

**Delta: `MISSING` + `LANGUAGE`** — No registry of atomic-vs-composed skills. The "transcript skill feeds 3 different skill systems" pattern is exactly the kind of compounding the user is feeling absent. Real gap.

---

### V1.4 — Sub-Agents for CONTEXT ISOLATION between chain steps

**Source (10:14-10:24):** "When you're chaining skills like this, context management becomes everything. Each skill in the chain gets exactly what it needs to do its job. Nothing more and nothing less. So we spin off sub-agents at relevant parts to keep the context window narrow and the quality of each output high before it's passed on between the skills."

**Antigravity equivalent:** `directives/sub_agent_protocol.md` (154 lines, detailed) defines SkillExecutor / CodeReviewer / DocSyncer / Researcher archetypes. **Last Activated: Not yet activated. Activation Count: 0.** `directives/agent-loading-protocol.md` (Tier 3) likewise has 0 activations.

**Delta: `CONFLICTS` + `MISSING`** — Two-layer finding: (a) Protocol exists but is dormant — this is exactly the "infrastructure built but never fires" pattern from `feedback_ai-memory-dependent-observability.md`. (b) The 2026-05-02 `feedback_no-claude-code-subagents.md` ban applies to `.claude/agents/` operator subagents specifically, NOT to context-isolation sub-agents via the `Agent` tool. These are different things and Antigravity rejected the wrong one's lookalike. **The video's pattern is permitted and would be useful — but the protocol it depends on has never been used.**

---

### V1.5 — Progressive Disclosure as the load-time discipline

**Source (03:49-04:09):** "Anthropic specifically designed skills to load only the context that's needed. And that's how they keep responses fast and maintain their high quality. A mega skill is going to blow that all up — everything's going to load at once once the skill loads."

**Antigravity equivalent:** Tiered loading (`directives/agent-loading-protocol.md`): T0 cards (80 tokens) → T1 SKILL.md+workflow (1,350) → T2 +genius.md (2,550) → T3 sub-agent (300 main). CLAUDE.md has explicit "Chain Efficiency Rules — Token Optimization" section that mirrors this.

**Delta: `CONFIRMS`** — Antigravity's tiered loading IS the progressive disclosure pattern. Already implemented and more sophisticated than the video describes.

---

## Video 2 Patterns — Agentic OS 9-Component Architecture

### V2.1 — Static Context: Identity File (CLAUDE.md / AGENTS.md / SOUL.md)

**Source (02:48-04:08):** "Every agentic tool reads an identity file first ... claude.md in Claude Code, agents.md in CodeX, soul.md in Open Claude ... injected into the system prompt at the start of every session." Recommends **AI-interview-to-build** (15 questions) instead of writing from scratch. Splits into user.md (about you) + personality.md (about the agent).

**Antigravity equivalent:** CLAUDE.md (extensive — 343 lines), FARRICE.md (user identity), AGENTS.md (Gemini/Codex), GEMINI.md. Also `_active/farrice-brand/` for ongoing brand identity work.

**Delta: `CONFIRMS`** — Antigravity has this multiple times over. The AI-interview build pattern isn't used (user wrote CLAUDE.md by hand + iteration), which is fine — current CLAUDE.md is more sophisticated than what a 15-question interview would produce.

---

### V2.2 — Static Context: Brand Context (referenced by skills, not in CLAUDE.md)

**Source (05:01-06:55):** "Brand context — how your business speaks, ICP, market positioning ... won't necessarily be injected at the start of the conversation inside the claude.md, but there are certain skills that will be able to reference them for your context, and this alone will 3x your output quality. ... 3x to 10x your output quality, I guarantee it."

**Antigravity equivalent:** `_active/farrice-brand/` (extensive brand work), `_active/farrice-brand/thought-bank/` (per recent memory entry), strategy_briefs, ICP profile referenced from CLAUDE.md (`deep-icp-primary-reference.md`). Lara Acosta + Luke Iha skill files inject voice patterns. Tier 1.5 Recall grounding pulls brand cards automatically.

**Delta: `CONFIRMS`** — Antigravity has this and goes deeper (e.g., `feedback_extract-forge-gate-first.md`, voice rules per-skill, deep ICP profile). **However**: the video's framing of "shared brand context folder that all skills pull from in one place" is cleaner than Antigravity's distributed approach. Worth noting but not a load-bearing change.

---

### V2.3 — Dynamic Context: 6-Level Memory System

**Source (07:01-10:30):** Six memory levels, most users need 1+2+3:
1. claude.md (static rules)
2. Session-start hook (forces context to load deterministically)
3. Semantic search (Mem Search, Claude-Mem) — search by meaning
4. Verbatim recall (Mem Palace) — for client work where exact phrasing matters
5. Knowledge bases
6. Cross-tool memory

**Antigravity equivalent:**
- L1: CLAUDE.md ✓
- L2: SessionStart hook fired today ("`/watch`: ready for videos with native captions") ✓
- L3: **Recall** (3,000+ saved cards, semantic search) auto-fires at Tier 1.5 for grounding-relevant domains. Plus NotebookLM (5 notebooks, 100 queries/month).
- L4: MEMORY.md system + per-file `memory_*.md` notes
- L5: `knowledge/` directory (240 files, 1.8M words, Karpathy Wiki) — explicit knowledge base
- L6: Notion integration for cross-tool

**Delta: `CONFIRMS`** — Antigravity ships **all six levels**, plus Notion + NotebookLM as bonus layers. Far more advanced than the video. **However**: the video's framing of memory as 6 discrete levels with explicit purpose (vs the current distributed setup) could improve documentation clarity.

---

### V2.4 — Skills as Specialist Knowledge (short, modular, references brand context, optional self-learning)

**Source (10:36-13:18):** "Skills should also always reference your business context, so when your copywriting skill runs, it's not guessing your brand voice. ... Bonus points if you've built in a rule inside your skill which is effectively self-learning ... every time it runs, it's going to read the feedback first before it runs ... through a learnings.md file."

**Antigravity equivalent:** Skills reference voice/brand via SKILL.md prompts. **Self-learning**: 4-dimension `chain_runner.py finalize` rubric + `feedback-ratchet.md` (149 lines, regression detection, evolution triggers) + `eval_harness.py` + `evolution_orchestrator.py`. Per-skill learnings are stored in `evolution_store/`.

**Delta: `CONFIRMS`** — Antigravity's feedback ratchet is 10x more sophisticated than a learnings.md file. But note: the audit (2026-04-24) found 94-99% of finalize scores were 8+ (grade inflation). The video's simpler "read feedback before running" loop is less sophisticated but harder to grade-inflate. Worth noting but not changing.

---

### V2.5 — Skill Systems (Chained skills with orchestrator + scheduled tasks)

**Source (13:46-16:08):** "Skill A is going to complete. We might have that human in the loop step. Skill B is going to continue to iterate until it's complete. And each one passes to the next with one skill orchestrator actually kind of a meta skill chaining all of these together to finally achieve an output." Examples: social media content generation, ad generation and monitoring, SEO blog generation.

**Antigravity equivalent:** `.agent/workflows/` (886 files) including `/parallax`, `/extract-forge`, `/campaign`, `/jarvis-command-center` plugins. JCC mission types (Solo / Strike / Campaign / Full Deploy) explicitly multi-phase with sub-agents.

**Delta: `CONFIRMS` + `EXTENDS`** — Antigravity has skill systems. The pattern is correct. **What's missing**: explicit "scheduled autonomous runs" of skill systems. Antigravity has `/schedule` skill but most workflows are user-initiated, not cron-triggered. The video's pattern of "skill system runs every Monday, pings me when done" is real and absent.

---

### V2.6 — Multi-Level Planning (Match plan depth to project complexity)

**Source (16:10-18:08):** "Three or four levels of planning so you can leverage those frameworks out the box. Level 1 = inbuilt shift-tab planning mode. Level 2 = generated PRD for half-day to multi-day projects. Level 3 = GSD (Get Shit Done) framework for highly complex like full SaaS builds. Designed to solve context rot."

**Antigravity equivalent:** Plan mode (active right now — this very conversation). `/strategic-clarity`, `/brief`, `/generate-brief`, `/mini-brief`. `/big-project` skill for multi-step project management. JCC Mission Briefing system.

**Delta: `CONFIRMS`** — Antigravity has multi-level planning. The video pattern is correct but Antigravity is more developed.

---

### V2.7 — Multi-Client Architecture (Parent CLAUDE.md + Per-Client CLAUDE.md Override)

**Source (18:18-20:38):** "We've used the inbuilt context inheritance from parent folders inside Claude Code. So we have one master claude.md, and that is the parent folder that passes down a lot of the methodology that is consistent across multiple clients. Then inside the root folder, we have individual client folders. Inside those client folders we have client one, client two, etc. Wherever we want specific client instructions, we've actually duplicated that Claude.md at the top and just added specific instructions which either conflict or override the Claude.md from the parent methodology."

**Antigravity equivalent:** Root `CLAUDE.md` ✓. Client folders exist (`_active/clients/javier-human-values/`, `_active/clients/jen-santulan/`, `_active/farrice-brand/`, etc.) but **`find` returned ZERO per-client CLAUDE.md files** — no inheritance is actually wired up. Skills live at root `skills/`, available to all projects but not per-client customizable.

**Delta: `MISSING`** — This is a real, clean gap. Client work currently inherits global behavior; client-specific voice/constraints have to be re-prompted each session. The Claude Code parent-folder inheritance feature is real and Antigravity isn't using it.

---

### V2.8 — Outputs in Predictable Places (Per-project folder structure)

**Source (20:38-22:16):** "There's no out-the-box way to solve this. So we've just created a simple folder structure per project, per skill, so that when we run a specific skill, let's say the Excalidraw diagram skill, we can jump into the output folder, which is the Agenty OS video, this video, and we can see directly the image that we're looking at."

**Antigravity equivalent:** `extractions/`, `deliverables/`, `_active/`, `projects/`, `research_outputs/`, `strategy_briefs/` — extensive folder structure documented in CLAUDE.md.

**Delta: `CONFIRMS`** — Antigravity has this and is more developed. Per-project organization is solid.

---

### V2.9 — Access from Anywhere (VPS + Telegram/Discord channels)

**Source (22:21-23:34):** "Get the system off your laptop, run on a server (VPS). And use Anthropic's built-in channels feature, which allows you to effectively talk from your phone via Telegram to the instance which has access to all of your files in the background."

**Antigravity equivalent:** None. Antigravity runs entirely on local laptop. No remote access layer.

**Delta: `MISSING` (but low priority)** — Real gap; would unlock mobile use. But not the "missing piece" the user is feeling — they're feeling system cohesion, not mobile access.

---

## Cross-Cutting Insight: The Felt Gap vs. The Real Gap

The user's stated feeling: *"workflows to work together more cohesively and compound, and improve and work together as a unified system versus a bunch of different individual tools."*

Mapping that feeling against the deltas above:

**Pattern V1.1 + V1.3 (LANGUAGE / MISSING)**: The atomic-skill ↔ skill-system distinction is absent in Antigravity vocabulary. "Skill" is overloaded — sometimes means a single tool (`creative-direction`), sometimes means an 8-phase orchestration (`/extract-forge`). When everything is "a skill," the user can't see the composition layer that would make the system feel unified rather than atomized.

**Pattern V1.4 (CONFLICTS / MISSING)**: Sub-agent protocol exists but has **0 activations**. The orchestration tissue is documented but inactive — exactly the `feedback_ai-memory-dependent-observability.md` pattern. The system as built relies on Claude remembering to spawn sub-agents at the right moment; it doesn't.

**Pattern V2.7 (MISSING)**: No per-client CLAUDE.md inheritance. Every project session re-encodes the entire global context. Client-specific voice / constraints / methodology aren't separable from the root.

**Pattern V1.2 (EXTENDS)**: Workflows often lack explicit human-in-the-loop gates. Production runs that need a "pause here" don't have it (Parallax 2.5 is the rare exception that proves the rule — and it exists because Edition 02 shipped with 7 fabrications).

**Pattern V2.5 (EXTENDS)**: Skill systems exist (workflows), but scheduled autonomous runs are absent. Everything is user-initiated. The compounding loop (skill A done → skill B fires automatically → human reviews tomorrow) is documented but not wired.

The "missing piece" is not new capability. It's **architectural language + protocol activation**. The system has 232 skills, 135 agents, 886 workflows, but two of its core orchestration protocols (`sub_agent_protocol.md`, `agent-loading-protocol.md`) have never fired. JARVIS.md is 4 months stale. The clean distinctions Simon Scrapes uses — **atoms vs systems, orchestrator skill, sub-agents for context isolation, parent/child CLAUDE.md inheritance, explicit human-in-loop gates** — would let the user see the system as the unified thing it almost already is.
