# Token Efficiency Protocol

> **Purpose**: Minimize token consumption and context pollution across all agent workflows. Adapted from Anthropic's Programmatic Tool Calling philosophy: *keep context clean, push deterministic work to code, only show the model what it needs to reason about.*
> **Created**: 2026-02-18 | **Updated**: 2026-02-27 (Context Engine integration — ACTIVELY ENFORCED)
> **Classification**: Mandatory Optimization Protocol
> **Status**: **ACTIVE** — Referenced from CLAUDE.md Core Protocols table. This protocol fires on every workflow.

---

## Core Principle

> "Every token in your context window should earn its place. If it's not helping the model reason, it's hurting it."

---

## Rule 1: Handoff Summaries (Workflow Chains)

**When passing output between workflow chain steps, compress to a handoff summary.**

❌ **Wrong**: Keep the full extraction report in context while generating individual prompt files  
✅ **Right**: Produce a handoff summary with only what the next step needs

### Handoff Summary Format

At each chain boundary (e.g., `/extract` → `/convert-extraction`), the completing step must produce:

```markdown
## Chain Handoff: [Step Name] → [Next Step Name]

**Expert**: [Name]
**Domain**: [1-line]
**Patterns Found**: [count] — [name1], [name2], [name3]...
**Prompts to Generate**: [list of prompt slugs]
**Key Methodology**: [1-2 sentences of the core framework]
**Files Created**: [list of file paths]
**Next Step Needs**: [what specifically the next step should read]
```

The next step reads this handoff summary + only the specific files it needs — NOT the full upstream output.

### When to Apply

- Any workflow chain with 2+ steps (see `directives/workflow-chains.md`)
- Any multi-file operation where intermediate results aren't needed downstream
- Sub-agent handoffs (see `directives/sub_agent_protocol.md`)

---

## Rule 2: Push Deterministic Work to Scripts

**If a task doesn't require LLM reasoning, script it.**

The LLM should NOT be manually:
- Counting prompt files and cross-referencing lists
- Inserting entries alphabetically into registries
- Validating that file counts match expected totals
- Generating boilerplate directory structures
- Checking if a skill is already registered

### Available Scripts

| Task | Script | Usage |
|------|--------|-------|
| Search experts by keyword | `execution/search_experts.py` | `python3 execution/search_experts.py "keyword"` |
| Validate skill completeness | `execution/validate_skill.py` | `python3 execution/validate_skill.py skill-name` |

### When to Build New Scripts

If you find yourself doing the same mechanical task 3+ times across conversations, create a script in `execution/` and log it here.

---

## Rule 3: Invocation Cards (Lazy Loading)

**Don't read full skill files until you need them. Start with the invocation card.**

An invocation card is a 5-10 line compressed summary of an agent's methodology that's sufficient for:
- Deciding if this is the right expert
- Starting the approach
- Making preliminary recommendations

Full file reads (`SKILL.md` → `genius-patterns.md` → `prompt.md`) happen ONLY when:
- Actually executing the expert's methodology
- Generating deliverables using their frameworks
- The invocation card doesn't have enough detail

### Invocation Card Format

```
AGENT: [Name]
DOMAIN: [1-line]
CORE METHOD: [The 1 thing they do differently]
BEST FOR: [2-3 specific use cases]
ENTRY PROMPT: [slug of the best starting prompt]
PAIRS WITH: [1-2 agents that stack well]
```

### Card File Location

Cards are stored in `agents/_framework/invocation-cards.md` — a single file with **40 expert cards** for fast scanning without multiple file reads. This is the **Tier 0** entry point in the Context Engine's tiered loading chain (see `directives/agent-loading-protocol.md`).

---

## Rule 4: Smart Skill Discovery (Context Engine Tiered Chain)

**Start at Tier 0. Escalate only when needed.** Full tiered chain protocol: `directives/agent-loading-protocol.md`.

Key principle: Don't read full skill files until you need them. Use invocation cards (~50 tokens each) for routing; escalate to Tier 1-3 only for execution.

---

## Token Budget Guidelines

| Operation | Token Budget | Enforcement |
|-----------|-------------|-------------|
| System prompt (CLAUDE.md/AGENTS.md/GEMINI.md) | ~750 tokens | Slimmed from ~5,700 — uses on-demand directive pointers |
| Skill invocation (per expert) | ~500 tokens | Use invocation card first |
| Workflow chain step | ~2,000 tokens | Use handoff summaries |
| Research output | ~5,000 tokens | Summarize before injecting into next step |
| Sub-agent handoff | ~300 tokens | Structured JSON, not prose |

---

## Anti-Patterns

| ❌ Don't | ✅ Do Instead |
|----------|--------------|
| Read 3 skill files to decide which expert to use | Check invocation cards (~50 tokens each) |
| Keep full extraction report in context during conversion | Compress to handoff summary |
| Manually count files and cross-check registries | Run validation scripts |
| Load all 86 agents' keywords for every request | Use tiered routing (quick-ref → search → index) |
| Carry raw research data into content creation steps | Summarize findings, cite only actionable insights |

---

## Integration

This protocol fires **alongside** (not instead of):
- `directives/intent-pipeline.md` — intent processing and expert routing
- `directives/workflow-chains.md` — chain contracts (references this file for handoff format)
- `directives/sub_agent_protocol.md` — sub-agent handoffs
- `directives/quality_gate.md` — output quality

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-02-27 |
| **Activation Count** | 1 |
| **30-Day Review Date** | 2026-03-29 |
| **Status** | **ACTIVELY ENFORCED** — Context Engine integration |

---

*Created: 2026-02-18 | Updated: 2026-02-27 (Context Engine — ACTIVE)*
*Classification: Mandatory Optimization Protocol*
