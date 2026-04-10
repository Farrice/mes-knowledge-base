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

## Rule 5: Chain Step Internalization

**Steps 1-3 of The Chain should be executed in-head, not via file reads.**

| Step | Old Behavior | New Behavior | Savings |
|------|-------------|--------------|---------|
| 1. SCORE | Read intent-pipeline.md | Internalized formula | ~500 tokens |
| 2. SHARPEN | Read intent-pipeline.md Stage 2 | Ask directly if needed | ~500 tokens |
| 3. ROUTE | Read DOMAIN_REGISTRY.md + invocation-cards.md | Internalized for known domains | ~1,200 tokens |

Total per-request savings: **~2,200 tokens** for routine tasks.

### Known Domain Routes (Internalized)

| Domain | Expert | No file read needed |
|--------|--------|-------------------|
| LinkedIn | Lara Acosta | ✅ |
| Copywriting | Luke Iha | ✅ |
| SEO | Nathan Gotch | ✅ |
| Brand Strategy | Oren / Grace | ✅ |
| Ghostwriting | Nicolas Cole | ✅ |
| Content Psychology | Kallaway | ✅ |
| Consumer Posture | Dai Media | ✅ |
| Agentic Workflows | Nick Saraev | ✅ |

For ambiguous or multi-domain requests, read `DOMAIN_REGISTRY.md` + `invocation-cards.md` as before.

---

## Rule 6: Hot Context Cache

**Don't re-read expert files already loaded in the current conversation.**

| Scenario | Action | Savings |
|----------|--------|---------|
| Expert loaded at Tier 1, same task arrives | Skip all reads (Hot) | ~1,350 tokens |
| Expert hot at Tier 1, Tier 2 needed | Read only genius.md (incremental) | ~1,350 tokens |
| Expert hot at Tier 2, any task arrives | Skip all reads (Hot) | ~2,550 tokens |

---

## Anti-Patterns

| ❌ Don't | ✅ Do Instead |
|----------|--------------|
| Read 3 skill files to decide which expert to use | Check invocation cards (~50 tokens each) |
| Keep full extraction report in context during conversion | Compress to handoff summary |
| Manually count files and cross-check registries | Run validation scripts |
| Load all 86 agents' keywords for every request | Use tiered routing (quick-ref → search → index) |
| Carry raw research data into content creation steps | Summarize findings, cite only actionable insights |
| Re-read SKILL.md for the same expert twice in one conversation | Check Hot Context Stack first (~1,350 tokens saved) |
| Read intent-pipeline.md to score a routine request | Internalized formula: +1 per DICE dimension |
| Read DOMAIN_REGISTRY.md for LinkedIn/Copywriting/SEO routing | Use internalized known domain routes |

---

## Integration

This protocol fires **alongside** (not instead of):
- `directives/intent-pipeline.md` — intent processing and expert routing
- `directives/workflow-chains.md` — chain contracts (references this file for handoff format)
- `directives/sub_agent_protocol.md` — sub-agent handoffs
- `directives/quality_gate.md` — output quality

---

## Rule 7: System Prompt Hygiene

**The system prompt (AGENTS.md + GEMINI.md + workflow list) is injected into EVERY message. Bloat here is the most expensive kind — it compounds on every single turn.**

### Limits
- **Workflow descriptions**: ≤8 words. The model needs a routing hint, not a sentence.
- **AGENTS.md + GEMINI.md combined**: Target < 12,000 chars. Currently ~9,300 + ~1,500 = ~10,800.
- **No duplication between AGENTS.md and GEMINI.md**. If it's in AGENTS.md, don't repeat it in GEMINI.md.
- **Workflow count**: If workflows exceed 400, audit for dormant/redundant ones quarterly.

### Why This Matters
- 416 workflows × ~140 chars each = ~58K chars injected per message
- Gemini models crash at `could not convert a single message before hitting truncation` when system prompt exceeds their budget
- Claude tolerates it (200K+ context) but still wastes tokens on every turn

### Audit Command
```bash
# Check workflow injection size
python3 -c "
import os, re
d='.agent/workflows'; total=0
for f in sorted(os.listdir(d)):
    if f.endswith('.md'):
        with open(os.path.join(d,f)) as fh: c=fh.read(500)
        m=re.search(r'description:\s*(.+)',c)
        if m: total+=len(f'- /{f[:-3]} (path): {m.group(1).strip()}')
print(f'Workflow injection: {total} chars (~{total//4} tokens)')
"
```

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-04-03 |
| **Activation Count** | 2 |
| **30-Day Review Date** | 2026-05-03 |
| **Status** | **ACTIVELY ENFORCED** — System Prompt Hygiene added |

---

*Created: 2026-02-18 | Updated: 2026-04-03 (Rule 7: System Prompt Hygiene — ACTIVE)*
*Classification: Mandatory Optimization Protocol*

