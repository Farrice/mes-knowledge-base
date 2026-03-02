# Completion Engine Skill Architecture — Design Doc

**Date**: 2026-02-28
**Status**: Approved
**Problem**: Expert skills packaged as 15-45 atomic prompts fragment the expert's integrated thinking. Each prompt carries 1/Nth of the genius. Results require heavy rework because the nuance — the tacit knowledge that makes an expert's output actually work — gets diluted across disconnected files.
**Solution**: Consolidate each expert's skill into 3-5 end-to-end workflows that carry the FULL extraction intelligence and produce specific, defined deliverables.

---

## The Paradigm Shift

| Aspect | Old (Prompt Library) | New (Completion Engine) |
|--------|---------------------|------------------------|
| Unit of work | Single prompt | End-to-end workflow |
| Genius loading | 1/N per prompt | 100% per workflow |
| Output | Fragment (one step) | Complete deliverable |
| User decision | Pick from 15-45 prompts | Pick from 3-5 workflows |
| Expert thinking | Decomposed, fragmented | Integrated, holistic |

## New Skill Format

```
skills/[expert-name-domain]/
├── SKILL.md              # Who, when, 3-5 workflow index
├── genius.md             # ALL genius patterns + hidden knowledge (unified)
└── workflows/
    ├── 01-[primary-workflow].md
    ├── 02-[secondary-workflow].md
    ├── 03-[tertiary-workflow].md
    └── (max 5)
```

### SKILL.md Structure (New)

```markdown
---
name: "[Expert] — [Domain]"
description: "[1-2 sentence value prop]"
version: "2.0"
format: "completion-engine"
workflows: 3-5
---

# [Expert Name] — [Domain]

[2-3 sentence expert context + core genius statement]

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| 01 | [Name] | [Specific deliverable] | [Trigger condition] |
| 02 | [Name] | [Specific deliverable] | [Trigger condition] |
| 03 | [Name] | [Specific deliverable] | [Trigger condition] |

## Quick Reference
- **Core Philosophy**: [1 sentence]
- **Best For**: [3-4 use cases]
- **Pairs With**: [2-3 complementary agents]
- **Genius Context**: [genius.md](genius.md) — load before any workflow
```

### genius.md Structure

Merged from existing genius-patterns.md + hidden-knowledge.md:

```markdown
# [Expert Name] — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## Genius Patterns
[All patterns from genius-patterns.md, preserved exactly]

## Hidden Knowledge
[All items from hidden-knowledge.md, preserved exactly]

## Operating Principles
[Distilled from AGENT.md core philosophy if available]
```

### Workflow File Structure

```markdown
---
name: "[Workflow Name]"
produces: "[Specific deliverable description]"
expert: "[Expert Name]"
load_context: "genius.md"
---

# [Expert Name] — [Workflow Name]

## Role
You are [Expert Name], [credibility]. You don't explain [domain] —
you execute it end-to-end and deliver a complete [deliverable].

**Before executing**: Read genius.md to load full extraction intelligence.

## Input Required
- **[Field 1]**: [Description]
- **[Field 2]**: [Description]
(keep to 3-6 essential inputs)

## Workflow
[Integrated end-to-end flow that mirrors how the expert actually thinks.
NOT decomposed atomic steps — a continuous process where each phase
feeds the next. Genius patterns and hidden knowledge are embedded
INLINE where they apply, not referenced as separate files.]

### Phase 1: [Name]
[Steps with embedded genius context]

### Phase 2: [Name]
[Steps building on Phase 1 output]

### Phase 3: [Name]
[Steps producing final deliverable]

## Output Contract
You will deliver:
- **[Component 1]**: [Exact specification]
- **[Component 2]**: [Exact specification]
- **[Component 3]**: [Exact specification]

Format: [Markdown/table/document structure]
Length: [Approximate scope]

## Quality Gate
[Expert-specific quality check — "Would [Expert] approve this?"]
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]
```

## Conversion Strategy

### What Gets Converted
- **111 expert skills** → new completion engine format
- Tool skills (17) and meta skills (11) → untouched

### Conversion Process (Per Skill)

**Phase 1 — Deterministic (no LLM)**:
1. Merge `references/genius-patterns.md` + `references/hidden-knowledge.md` → `genius.md`
2. Create `workflows/` directory
3. Archive old prompts to `references/_legacy-prompts/`

**Phase 2 — Intelligent (Gemini Flash)**:
1. Read SKILL.md categories + all prompt file content
2. Identify 3-5 natural end-to-end workflows from prompt groupings
3. Generate each workflow file (consolidating relevant prompts + embedding genius context)
4. Rewrite SKILL.md in new format

### Batch Execution
- Process skills in parallel batches of 10-15
- Each skill: 1 planning call + 3-5 generation calls = 4-6 Gemini calls
- Total: ~555-666 API calls across all 111 skills
- Estimated cost: $3-6 (Gemini Flash pricing)
- Estimated time: 30-60 minutes

## Updated Extraction Pipeline

### New Flow (transcript → deployed skill)

```
Transcript → [AUTO] MES 3.0 Extraction
    → [CHECKPOINT 1] Review extraction + approve workflow plan
    → [AUTO] Generate genius.md + workflow files
    → [AUTO] Create agent + register
    → [CHECKPOINT 2] Review one workflow output
    → DEPLOYED
```

### Changes to Existing Scripts
- `extraction_swarm.py` → replaced by `skill_converter.py` for conversion
- New script generates workflows instead of individual prompts
- Same Gemini API infrastructure, different output format

## Migration Notes

- Existing extraction reports are PRESERVED — they're the source of truth
- Old prompt files archived to `references/_legacy-prompts/` (git tracks history)
- Agent AGENT.md files updated to reference new workflow-based skills
- AGENT_INDEX.md and SKILL_INDEX.md updated with new format indicators
- Invocation cards remain valid — routing is unchanged
