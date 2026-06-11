# Claude Code Harness → Antigravity Evolution Roadmap

What to steal, adapt, and build from the leaked 512K-line harness to make our system significantly better.

---

## SKILL DEPLOYMENT RECOMMENDATION

### What You're Doing
Using the Claude Code harness leak as a competitive intelligence source to identify specific, high-ROI upgrades to the Antigravity system — then building them.

### Primary Skill
**Nick Saraev (Agentic Workflows)** → `/harness-evolve` + `/self-evolve`
- **Why**: This is pure harness architecture work — orchestration patterns, memory systems, verification protocols
- **What it produces**: Concrete system upgrades with before/after performance

### Support Skills
1. **`/orchestration-blueprint`** — Design the new multi-agent Coordinator Mode
2. **`/bitter-lesson-check`** — Audit our hand-coded patterns against their LLM-powered alternatives
3. **`/system-audit`** — Baseline our current system before modifications

---

## The 6 High-ROI Adoptions (Priority Order)

### 1. 🔴 Adversarial Verification Agent (HIGHEST IMPACT)

**What they have:** A dedicated verification agent that is _adversarial by design_. It tries to _break_ implementations, not confirm they work. It's read-only (blocked from editing files), must run actual commands (not just read code), and outputs `VERDICT: PASS/FAIL/PARTIAL` with command transcripts.

**What we have:** Quality gate scoring (intent alignment, expert standard, adversarial resilience) — numbers on a 1-10 scale. No adversarial execution. We score, we don't verify.

**The gap:** Our quality gate is a self-assessment. Their verification agent is an _independent adversary_. The difference is the difference between grading your own homework and having someone try to poke holes in it.

**What to build:**
- New directive: `directives/verification-agent-protocol.md`
- Adversarial verification step that fires after Step 5 (PRODUCE) for any implementation work
- The verifier CANNOT edit files — it can only run commands, read code, and issue verdicts
- Integrate with `chain_runner.py` so finalize won't fire until verification passes
- Key prompt pattern to steal: _"You have two documented failure patterns. First, verification avoidance: when faced with a check, you find reasons not to run it. Second, being seduced by the first 80%."_

**Effort:** Medium (1 session)
**Impact:** Eliminates "looks right but doesn't work" failures

---

### 2. 🔴 Semantic Memory Selection (HIGH IMPACT)

**What they have:** An LLM (Sonnet) that reads a manifest of all memory files with descriptions, then selects up to 5 that are relevant to the current query. It skips API docs for tools already in use but keeps gotchas/warnings. This runs _every turn_.

**What we have:** Manual tiered loading (Tier 0→3) driven by rule-based routing. We load experts based on domain matching, not semantic query relevance. Our KI system has summaries but no LLM-powered selection.

**The gap:** Their system is query-aware and automatic. Ours requires explicit routing decisions. We miss relevant KIs and skills because the routing is keyword-based, not semantic.

**What to build:**
- New execution script: `execution/memory_selector.py`
- At conversation start, build a manifest of all skills (SKILL.md descriptions), KIs (metadata.json summaries), and relevant directives
- Use Gemini Flash to select the 3-5 most relevant items for the current query
- Inject selected items into context before Step 4 (LOAD)
- This replaces the manual "check KI summaries" instruction with an automatic system

**Effort:** Medium (1-2 sessions)
**Impact:** Eliminates the "forgot we had a skill for this" anti-pattern

---

### 3. 🟡 Coordinator Mode for `/swarm` (MEDIUM-HIGH IMPACT)

**What they have:** A coordinator that spawns parallel workers with precise, self-contained prompts. Key patterns:
- **Research → Synthesis → Implementation → Verification** pipeline (4 phases)
- The coordinator _must synthesize findings itself_ before directing workers. Anti-pattern: "Based on your findings, fix it" (lazy delegation)
- Workers can't see the conversation — every prompt must be self-contained
- Continue vs. spawn decision based on context overlap

**What we have:** `/parallel-swarm` fires 3 agents simultaneously but with less structured handoff. No synthesis step between research and implementation. Our swarm is fire-and-forget, not coordinate-and-synthesize.

**The gap:** We spray agents but don't coordinate them. Their coordinator pattern forces understanding _between_ phases. Our swarms produce raw outputs — their coordinator produces integrated results.

**What to build:**
- Rewrite `/parallel-swarm` workflow with the 4-phase pipeline
- Add mandatory synthesis step: "Before directing implementation, YOU must understand the research — include specific file paths, line numbers, and exactly what to change"
- Add the continue-vs-spawn decision logic
- Add worker isolation: each worker prompt must be fully self-contained

**Effort:** Medium (1 session to rewrite workflow)
**Impact:** Transforms swarm from "parallel execution" to "coordinated intelligence"

---

### 4. 🟡 Prompt Modularization (MEDIUM IMPACT)

**What they have:** 30 separate system prompts, each scoped to a specific concern. Dynamically assembled at runtime based on feature flags and environment.

**What we have:** 2 monolith files (`CLAUDE.md` at ~200 lines, `GEMINI.md` at ~100 lines) that try to cover everything.

**The gap:** Their modular approach means each prompt is smaller, more testable, and independently evolvable. Our monoliths are hard to A/B test and impossible to evolve piece-by-piece.

**What to build:**
- Decompose `GEMINI.md` into modular sections in `.claude/rules/`:
  - `chain.md` — The 6-step chain (currently ~40% of the file)
  - `routing.md` — Expert routing table
  - `context-engine.md` — Tiered loading rules
  - `quality.md` — Quality gate + anti-patterns
  - `efficiency.md` — Token optimization rules
  - `memory.md` — Session state + compaction recovery
- Each module can be evolved independently via `/harness-evolve`
- Add `paths:` frontmatter for conditional injection (their pattern — only load routing rules when routing is needed)

> [!IMPORTANT]
> This is the unlock for our `/self-evolve` workflow. You can't evolve a monolith — you need modules. Breaking the prompt into pieces is _prerequisite_ for automated prompt evolution.

**Effort:** Low-Medium (1 session)
**Impact:** Enables automated evolution of individual system components

---

### 5. 🟢 3-Mode Compaction (LOWER IMPACT, HIGH VALUE)

**What they have:** Three compaction modes:
1. **Full** — Summarize entire conversation (9 required sections)
2. **Partial Recent** — Keep old context, summarize only new messages  
3. **Partial Older** — Summarize old messages, keep recent intact

Plus an `<analysis>` drafting scratchpad that gets stripped before the summary reaches context.

**What we have:** Session-state anchors (`.agent/session-state.md`) — single checkpoint format. No compaction modes. We write one anchor and hope it survives.

**The gap:** Their multi-mode approach means context loss is _graduated_ — they keep the most useful parts intact depending on the situation. Our single anchor is all-or-nothing.

**What to build:**
- Extend `directives/session-state-protocol.md` with graded compaction triggers
- Add "What to preserve" rules: recent user messages are always kept verbatim (their Section 6)
- Add the analysis-then-summary pattern to our checkpoint writer

**Effort:** Low (0.5 session)
**Impact:** Better context survival during long sessions

---

### 6. 🟢 Frustration Detection (NICE-TO-HAVE)

**What they have:** Regex-based keyword detection in `userPromptKeywords.ts` that flags frustrated user messages. Practical, not sophisticated.

**What we have:** Nothing. We rely on explicit user feedback.

**What to build:**
- Simple keyword list in `directives/user-state-awareness.md`
- When frustration detected: stop proposing, start fixing. Shift from advisory to execution mode.
- Integrate with the chain: frustration = auto-narrow (skip Step 2, route silently, produce fast)

**Effort:** Very low (30 min)
**Impact:** Better user experience when things go wrong

---

## What NOT to Copy

| Their Pattern | Why Skip It |
|---|---|
| **KAIROS/autoDream** | Autonomous nightly daemon — cool but we're not a persistent background process. Our `/self-evolve` handles evolution on-demand. |
| **BUDDY (Tamagotchi)** | Novelty feature, no strategic value |
| **Anti-distillation defenses** | We're not a product being scraped — irrelevant |
| **ULTRAPLAN (remote Opus)** | Cloud container reasoning — we don't have this infrastructure |
| **YOLO mode** | Auto-approve all actions — too dangerous for our orchestration layer |

---

## Execution Roadmap

### Phase 1: Foundation (This Week)
1. **Prompt Modularization** (#4) — 1 session → Enables everything else
2. **Verification Agent** (#1) — 1 session → Biggest quality improvement
   - Run `/harness-evolve` on quality gate to integrate verification

### Phase 2: Intelligence (Next Week)  
3. **Semantic Memory Selection** (#2) — 1-2 sessions
4. **Coordinator Mode** (#3) — 1 session to rewrite `/parallel-swarm`

### Phase 3: Polish (Week After)
5. **3-Mode Compaction** (#5) — 0.5 session
6. **Frustration Detection** (#6) — 30 min

### Total Investment: ~5-6 sessions over 2-3 weeks

---

## Skills to Deploy

| Phase | Workflow | Purpose |
|---|---|---|
| Phase 1 | `/harness-evolve` | Evolve quality gate → verification agent integration |
| Phase 1 | `/self-evolve` | Evolve chain instructions after modularization |
| Phase 2 | `/orchestration-blueprint` | Design Coordinator Mode architecture |
| Phase 2 | `/bitter-lesson-check` | Audit manual routing vs semantic selection |
| All | `/system-audit` | Baseline before + measure after each phase |

---

## The Meta-Insight

The biggest lesson from this leak isn't any single feature — it's that **Anthropic treats their agent's harness as a product, not a prompt**. 30 modular prompts, each testable and evolvable. Adversarial verification with documented failure modes. Semantic context selection that runs every turn.

We have more domain expertise (24 experts, 200+ workflows). They have better infrastructure. The play is to graft their infrastructure patterns onto our expertise system.

> **Want me to start with Phase 1? I'd begin by modularizing `GEMINI.md` into separate rule files, then build the Verification Agent protocol.**
