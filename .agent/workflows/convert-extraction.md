---
description: Convert MES 3.0 extractions to completion-engine skills with end-to-end workflows
---

# /convert-extraction Workflow (v2.0 — Completion Engine)

Converts a completed extraction report into a fully registered, deployable completion-engine skill with 3-5 end-to-end workflows.

// turbo-all

---

## Step 0: Determine Source

| Source | Path | Action |
|--------|------|--------|
| Fresh extraction | `extractions/[expert]/extraction-report.md` | Read report |
| Existing skill (reconvert) | `skills/[skill-name]/` | Read SKILL.md + references |

---

## Step 1: Audit Extraction

Read the extraction report and extract:
- **Expert name** and domain
- **Genius patterns** (count and names)
- **Hidden knowledge** (count and items)
- **Core methodology/frameworks**
- **Proposed workflows** (not individual prompts)

Identify 3-5 natural end-to-end workflows based on the extraction content:

```markdown
## Workflow Plan

| # | Workflow | Produces | Description |
|---|---------|----------|-------------|
| 01 | [name] | [deliverable] | [end-to-end flow] |
...
```

**Workflow sizing rules:**
- 3 or fewer source items → 1-2 workflows
- 4-10 → 2-3 workflows
- 11-25 → 3-4 workflows
- 26+ → 4-5 workflows

---

## Step 2: Create Skill Structure

```bash
mkdir -p skills/[skill-name]/workflows agents/[expert-name]/memory
```

Naming: `skills/[firstname-lastname-domain]/`

---

## Step 3: Create genius.md

Merge genius patterns + hidden knowledge into a single unified file:

```markdown
# [Expert Name] — Genius Context

> Load this file before executing any workflow.

## Genius Patterns
[All patterns: What They Do → Executable Behavior → Deploy When → Success Metric]

## Hidden Knowledge
[All items: Tacit Insight → Why Others Miss This → Deploy When]
```

---

## Step 4: Generate Workflow Files

**Option A: Manual generation** (for 1-3 workflows)

For each workflow, create `skills/[skill-name]/workflows/[NN]-[slug].md`:

```markdown
---
name: "[Workflow Name]"
produces: "[Specific deliverable]"
expert: "[Expert Name]"
load_context: "genius.md"
---

# [Expert] — [Workflow Name]

## Role
[Expert identity + credibility — 2-3 sentences]

**Before executing**: Read genius.md for full extraction intelligence.

## Input Required
[3-6 essential inputs]

## Workflow
[Integrated end-to-end flow. Embed genius patterns INLINE.
Each phase builds on the previous. Produce a COMPLETE deliverable.]

## Output Contract
[Exact specification of deliverable components]

## Quality Gate
[3-5 expert-specific criteria]
```

**Option B: Automated conversion** (for existing skills with many prompts)

```bash
python execution/skill_converter.py --skill "skills/[skill-name]"
```

---

## Step 5: Write SKILL.md

Completion engine format:

```markdown
---
name: "[Expert] — [Domain]"
description: "[Value prop]"
version: "2.0"
format: "completion-engine"
workflows: [N]
---

# [Expert] — [Domain]

[Expert context + core genius statement]

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| 01 | [Name](workflows/01-slug.md) | [Deliverable] | [Trigger] |

## Quick Reference
- **Genius Context**: [genius.md](genius.md)
```

---

## Step 6: Create Agent Files

### AGENT.md
Standard agent template referencing workflows (not individual prompts).

### memory/context.md
Initialize with activation date.

---

## Step 7: Register

Add to `AGENT_INDEX.md` and `SKILL_INDEX.md`.

---

## Step 8: Verification

```bash
# Count workflow files
ls -1 "skills/[skill-name]/workflows/" | wc -l

# Verify structure
find "skills/[skill-name]" -type f | sort

# Check registrations
grep "[expert-name]" AGENT_INDEX.md SKILL_INDEX.md
```

| Check | Expected | Actual |
|-------|----------|--------|
| genius.md | 1 | |
| Workflow files | [N] | |
| SKILL.md (v2.0) | 1 | |
| Agent files | 2 | |
| Registry entries | 2 | |

---

## Key Differences from v1.0

| v1.0 (Prompt Library) | v2.0 (Completion Engine) |
|----------------------|--------------------------|
| 15-45 individual prompt files | 3-5 workflow files |
| genius-patterns.md + hidden-knowledge.md separate | genius.md unified |
| Each prompt = 1/N of genius | Each workflow = 100% genius |
| User picks from prompt menu | User picks from workflow menu |
| Output = fragment | Output = complete deliverable |
