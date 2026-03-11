# Sub-Agent Protocol

> **Purpose**: Defines *when* and *how* to spawn sub-agents for context isolation. Includes archetypes, spawn triggers, and the SkillExecutor for expert skill work.
> **Updated**: 2026-03-03 (Parallel Execution Patterns added)
> **Reference**: `skills/nick-saraev-agentic-workflows/references/prompts/crown_jewel_06_sub_agent_designer.md`
> **Loading Protocol**: `directives/agent-loading-protocol.md` (Tier 3 = sub-agent)

---

## Why Sub-Agents Exist

Sub-agents solve one problem: **context pollution**. As a conversation grows, accumulated context degrades output quality. Sub-agents get a fresh context window, which means:
- Honest code review (not influenced by "I just wrote this" bias)
- Clean research (not anchored by prior assumptions)
- Accurate documentation (reads the actual code, not memory of the code)

---

## Auto-Spawn Triggers

These scenarios should **automatically** prompt consideration of spawning a sub-agent. The agent does NOT need a user command to trigger these — they fire based on the work being done.

| Trigger | Archetype | When Exactly |
|---------|-----------|-------------|
| Major code modification (50+ lines changed) | **CodeReviewer** | After completing the code change, before marking task done |
| Directive created or significantly updated | **DocSyncer** | After the directive change, verify it matches the actual code/tool state |
| Deep research needed mid-task | **Researcher** | When the main task needs external data but you don't want to pollute current context |
| Multi-file refactor | **CodeReviewer** | After the refactor, review each file with fresh eyes |
| Pre-deployment check | **CodeReviewer** | Before any `modal deploy` or production push |
| Expert skill execution (2+ experts or 10+ files loaded) | **SkillExecutor** | When Tier 3 loading is needed per Context Engine |
| Multi-expert ensemble or council | **SkillExecutor** | When running `/roundtable`, `/swarm`, or multi-expert workflows |

**Key**: "Consideration" means evaluate whether the spawn is worth it. Don't spawn for trivial changes.

---

## Archetypes

### CodeReviewer (Read-Only)
- **Permissions**: READ-ONLY on target files
- **Mission**: Find bugs, security issues, performance problems, logic errors
- **Cannot**: Modify code, access credentials, run scripts
- **Output format**: Markdown review with severity ratings (🔴 Critical, 🟡 Warning, 🟢 Suggestion)

### DocSyncer (Read + Write Directives)
- **Permissions**: READ on `execution/`, WRITE on `directives/`
- **Mission**: Ensure directives match actual code behavior
- **Cannot**: Modify code, only documentation
- **Output format**: Diff of directive updates with rationale

### Researcher (Read + Web)
- **Permissions**: READ on current context summary, Web search access
- **Cannot**: Modify any files, access credentials
- **Output format**: Structured findings with sources and confidence tags (🟢🟡🔴)

### SkillExecutor (Read Skills + Execute) — NEW: Context Engine Tier 3
- **Permissions**: READ on skill files, READ on user-provided input, WRITE to `.tmp/` only
- **Mission**: Load expert skill files in fresh context, apply methodology, return compressed result
- **Cannot**: Modify code, access credentials, read files outside skill scope
- **Output format**: Expert-driven deliverable + provenance tag (~300-500 tokens compressed)

**When to use SkillExecutor:**
- 2+ experts needed for the same task
- Session has already loaded 10+ files (context is getting full)
- Running `/roundtable`, `/swarm`, or multi-expert ensembles
- Full extraction pipeline (`/extract` → `/convert-extraction`)

**When NOT to spawn (just load directly):**
- Under ~1,000 tokens of expected output
- Follow-up refinements to work already in context
- Rapid-fire mode (user wants speed over depth)
- Purely conversational or Q&A

**SkillExecutor Prompt Template:**
```
## PHASE 1: SKILL ACQUISITION (Do this FIRST)

Read these files in order:
1. /Users/farricecain/Google Antigravity/skills/[skill-name]/SKILL.md
2. /Users/farricecain/Google Antigravity/skills/[skill-name]/references/genius-patterns.md
3. /Users/farricecain/Google Antigravity/skills/[skill-name]/references/prompts/[specific-prompt].md

After reading, confirm: What are the 3 most important patterns? What is the output structure? What would the expert say is WRONG?

## PHASE 2: EXPERT-DRIVEN EXECUTION
Apply the methodology to: [Task description]

## PHASE 3: OUTPUT
Embody principles (not templates). Reference patterns by name. Pass the skill's quality test.

## PHASE 4: RECURSIVE REFLECTION
Would the expert be proud? Is this creative application or mechanical copy? Remarkable or merely competent?

## VERIFICATION
SKILL FILES READ: [list] | PATTERNS APPLIED: [list] | QUALITY CHECK: [test, pass/fail]
```

**Return format** (what the main context receives):
```markdown
## SkillExecutor Result: [Expert Name]

**Task**: [1-line]
**Patterns Applied**: [list by name]
**Quality Check**: [test name] — [pass/fail]

### Output
[The deliverable, compressed to essentials]

### Key Insight
[1-2 sentences of the most important thing the expert's framework revealed]
```

---

## Permission Matrix

| Resource | CodeReviewer | DocSyncer | Researcher | SkillExecutor |
|----------|:-----------:|:---------:|:----------:|:------------:|
| `execution/*.py` | READ | READ | — | — |
| `directives/*.md` | READ | READ+WRITE | READ | — |
| `skills/*/` | — | — | — | READ |
| `agents/*/` | — | — | — | READ |
| `.tmp/` | — | — | — | WRITE |
| `.env` / credentials | — | — | — | — |
| Web search | — | — | ✅ | — |
| File modification | — | Directives only | — | `.tmp/` only |
| Perplexity API | — | — | Budget-gated | — |

---

## Communication Protocol

### Main Agent → Sub-Agent (Handoff)
```json
{
  "task": "Review execution/email_enrichment.py for bugs and security issues",
  "context_summary": "Script was just refactored to use async batch processing",
  "files_to_review": ["execution/email_enrichment.py"],
  "permissions": "READ-ONLY",
  "expected_output": "Markdown code review with severity ratings"
}
```

### Sub-Agent → Main Agent (Report)
```json
{
  "findings": [
    {
      "severity": "🔴 Critical",
      "file": "email_enrichment.py",
      "line": 142,
      "issue": "API key exposed in error message string",
      "fix": "Use generic error message, log key reference to debug only"
    }
  ],
  "summary": "1 critical, 2 warnings, 3 suggestions",
  "confidence": "high"
}
```

---

## Parallel Execution Patterns

Sub-agents can run in parallel when their tasks are independent. This is critical for workflows that would otherwise take 3-5x longer sequentially.

### Decision Tree: When to Parallelize

```
Is the task decomposable into independent parts?
├── NO → Run sequentially (single sub-agent or embodiment)
└── YES → Do agents need to communicate during execution?
    ├── YES → Use Agent Teams (TeamCreate + SendMessage)
    └── NO → Do you need 2-5 independent workers?
        ├── YES → Use Parallel Task Calls (multiple Task tools in one message)
        └── NO (6+ workers or need Gemini cost savings)
            └── Use parallel_swarm.py (Gemini API)
```

### Tier 1: Parallel Task Calls (2-5 agents, no coordination)

**How it works**: Make multiple `Task` tool calls in a **single message**. Each spawns an independent sub-agent with a fresh context window. They execute simultaneously and return results independently.

**Best for**: Extraction swarm, research team, content sprint — any workflow where agents work on independent pieces and don't need each other's output.

**Template**:
```
[In a single message, include multiple Task tool calls:]

Task 1: {subagent_type: "general-purpose", prompt: "Research angle A..."}
Task 2: {subagent_type: "general-purpose", prompt: "Research angle B..."}
Task 3: {subagent_type: "general-purpose", prompt: "Research angle C..."}
```

**Workflow templates**:
- `/parallel-extract` — 2-5 extractions simultaneously
- `/parallel-research` — 3 research angles simultaneously
- `/parallel-content` — 3-5 content pieces simultaneously

### Tier 2: Agent Teams (2-5 agents, need coordination)

**How it works**: Use `TeamCreate` to form a team, spawn teammates with `Task` (with `team_name`), and coordinate via `SendMessage`. Agents can assign tasks, share findings, and build on each other's work.

**Best for**: Complex projects where Agent B needs Agent A's output, or where a lead agent needs to review/synthesize work from multiple workers.

**When to use over Tier 1**:
- Agents depend on each other's output (e.g., researcher feeds strategist)
- A lead agent needs to review and redirect work mid-flight
- The task has a dependency graph (not purely parallel)

### Tier 3: Gemini Parallel Swarm (5-10+ agents, cost-sensitive)

**How it works**: `execution/parallel_swarm.py` fires parallel API calls to Gemini, each embodying a different expert. Very low cost (~$0.15 for 5 agents).

**Best for**: Large-scale expert embodiment where you need 5-10+ perspectives and cost matters more than tool access.

**Limitations**: Agents can't use Claude Code tools (no file read/write, no web search). They only have the expert skill context injected into their prompt.

### Parallel Execution Rules

1. **Independence test**: Before parallelizing, verify each agent's task can complete without another agent's output
2. **Max 5 parallel Task calls**: More than 5 creates resource contention and degrades quality
3. **Always collect and synthesize**: Parallel outputs need a synthesis step — don't just dump raw outputs
4. **Failure isolation**: If one parallel agent fails, others continue. Report the failure, don't retry the whole batch
5. **Write to separate files**: Each parallel agent writes to its own output file (`.tmp/[workflow]/[agent].md`) to avoid conflicts

### Sequential vs. Parallel: Common Patterns

| Workflow | Execution | Why |
|----------|-----------|-----|
| `/extract` (single) | Sequential | One source, one expert — no parallel benefit |
| `/parallel-extract` (batch) | Parallel Task Calls | Independent sources, no interdependence |
| `/roundtable` | Sequential | Experts build on each other's positions |
| `/parallel-research` | Parallel Task Calls | Independent research angles |
| `/swarm` (5+ agents) | Gemini parallel or sequential batches | Too many agents for Task tool parallelism |
| `/parallel-content` | Parallel Task Calls | Independent content pieces |
| Complex build project | Agent Teams | Dependency graph, coordination needed |

### Why Sequential Fallback Happens (and How to Prevent It)

**Root causes**:
- `/swarm` and `/roundtable` embody experts one at a time in a single context window
- Making Task calls one-per-message forces sequential execution
- Not decomposing tasks into independent pieces before starting

**Prevention**:
- Multiple Task calls in the SAME message = true parallelism
- Each agent gets explicit file paths for input and output (no shared state)
- Use the parallel workflow templates for batch operations
- Reserve sequential embodiment for workflows that genuinely need cross-expert dialogue (roundtable, council)

---

## Anti-Patterns

| Don't | Why |
|-------|-----|
| Share full conversation context with sub-agent | Defeats the purpose — they need fresh eyes |
| Spawn for trivial changes (<20 lines) | Overhead exceeds benefit |
| Chain 3+ sub-agents deep | Coordination cost explodes |
| Give sub-agents write access to code | Only the main agent modifies code |
| Spawn without a clear return condition | Sub-agent must know exactly when to stop |
| Make Task calls one per message when they're independent | Forces sequential when parallel is possible |
| Use Agent Teams for purely independent tasks | Coordination overhead with no benefit |
| Run 6+ parallel Task calls | Resource contention degrades all agents |

---

## Integration Points

- **Triggered by**: The auto-spawn triggers above (built into agent behavior)
- **Prompt structure**: Phase 1-4 template (in this file for SkillExecutor, in `directives/agent-loading-protocol.md` for general loading)
- **Quality gate**: Sub-agent output runs through `directives/quality_gate.md`
- **Context Engine**: SkillExecutor is the Tier 3 implementation of the tiered loading chain
- **Parallel workflows**: `.agent/workflows/parallel-*.md` (extract, research, content)
- **Referenced from**: CLAUDE.md/AGENTS.md/GEMINI.md Sub-Agent Protocol section

---

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-04-11 |

**Update Rule**: When this protocol fires (sub-agent spawned), update the date and increment count.

*Created: 2026-02-17 | Updated: 2026-03-03 (Parallel Execution Patterns — 3-tier parallelism model)*
