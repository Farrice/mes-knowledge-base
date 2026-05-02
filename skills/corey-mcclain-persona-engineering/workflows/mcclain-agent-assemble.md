---
name: Agent Assembly
command: /mcclain-agent-assemble
expert: Corey McClain
category: Agent Forge
description: Wire all LLMP layers into a deployable agent — Logic, Library, Memory, Persona — with full file creation
inputs: Expertise distillation, skill architecture, persona document, expert name
outputs: Complete deployed agent — SKILL.md, genius.md, all workflows, AGENT.md, memory/, registered slash commands
---

# Agent Assembly

The construction phase. You have the intelligence (expertise distillation), the blueprint (skill architecture), and the soul (persona document). Now you build.

This workflow takes all extracted and designed materials and produces the complete file set for a production-grade persona-based expert agent. Every file, every workflow, every slash command wrapper, every registration entry.

## Pre-Flight Gate

- [ ] Expertise distillation complete (genius patterns, hidden knowledge, signature moves, quality rubric)
- [ ] Skill architecture approved (workflow table, tier assignments, stacking chains)
- [ ] Persona document complete (narrative life document, 500-2000 words)
- [ ] Expert name and skill directory name confirmed

## Workflow

### Step 1 — Directory Scaffolding

Create the file structure:

```bash
// turbo
mkdir -p skills/[skill-name]/workflows skills/[skill-name]/references agents/[expert-name]/memory
```

### Step 2 — Genius.md Construction

Build the unified genius context file from the expertise distillation:

**Structure** (follow the established pattern from existing genius.md files):

1. **Core Genius** — 1 paragraph, the expert's irreducible contribution
2. **Genius Patterns** — All patterns with executable behavior, deploy triggers, and success metrics
3. **Hidden Knowledge** — Numbered entries with explanations
4. **Hall of Fame Exemplars** — Minimum 3 with context, example, and what makes it excellent
5. **Anti-Exemplar** — What mediocre looks like and why it fails
6. **Signature Moves** — Numbered with deploy triggers
7. **Quality Rubric** — Table format: Criterion × Score 4/7/10
8. **Methodology** — Named methodology with level/phase breakdown
9. **Applied Intelligence** — Capability unlocks + system enhancements

**Token discipline**: Genius.md should be 3,000-6,000 words. Dense enough to be comprehensive. Not so long it bloats the context window.

### Step 3 — Workflow File Construction

Build each workflow from the skill architecture:

**Every workflow MUST include:**

```markdown
---
name: [Workflow Name]
command: /[prefix]-[workflow-name]
expert: [Expert Name]
category: [Foundation | Practitioner | Stacking]
description: [One-line — what it produces]
inputs: [What it needs]
outputs: [What it delivers]
---

# [Workflow Name]

[Opening paragraph — what this workflow does and why]

## Pre-Flight Gate
[Checklist of prerequisites]

## Workflow
### Step 1 — [Name]
[Instructions]
...

## Content Type Adaptations
| Content Type | Adaptation |
|-------------|------------|

## Quality Gate
[Final checklist before marking complete]
```

**Construction rules:**
- Foundation workflows: 80-120 lines (substantial, core methodology)
- Practitioner workflows: 60-100 lines (focused, specific technique)
- Stacking workflows: 100-140 lines (need to document both expert contributions)
- Every workflow references genius.md for quality standards
- Every workflow ends with a quality gate checklist

### Step 4 — SKILL.md Construction

Build the skill manifest:

```markdown
---
name: [Expert Name] — [Domain]
domain: [Domain description]
expert: [Expert Name]
version: 1.0
---

# [Expert Name] — [Domain]

[One paragraph — what this skill enables]

## Quick Reference
| Component | File |
|-----------|------|
| Genius Context | genius.md |
| AGENT.md | agents/[expert-name]/AGENT.md |
| Workflows | workflows/ ([N] total) |

## Workflow Table

### Tier 1 — Foundation
[Table: Workflow | Slash Command | Description]

### Tier 2 — Practitioner
[Table]

### Tier 3 — Stacking
[Table]

## Stacking Guide
[Table: Pair With | What Compounds | Recommended Workflow]

## When to Use This Skill
[Use when / Don't use when]
```

### Step 5 — AGENT.md Construction

Build the agent file using `agents/_framework/AGENT_TEMPLATE.md`:

1. **Core Competencies**: Derive from top 5 genius patterns
2. **Available Skills**: Map from workflow table
3. **Decision Framework**: Extract from methodology architecture
4. **Activation Triggers**: When to invoke this agent vs. using skills directly
5. **Handoff Protocol**: Map from stacking chains
6. **Memory Reference**: Point to `memory/context.md`

### Step 6 — Memory Initialization

Create `agents/[expert-name]/memory/context.md`:

```markdown
# [Expert Name] Memory

## Active Projects
(None yet)

## User/Brand Context
(To be populated as work proceeds)

## Learnings
(To be populated from completed work)

## Past Work Reference
(To be populated from completed work)
```

### Step 7 — Persona Integration

Install the persona document into the agent architecture:

1. Save persona as `agents/[expert-name]/persona.md`
2. Reference persona in AGENT.md under a "Persona" section
3. Ensure persona is loaded into context when the agent is invoked
4. Verify persona is NOT compressed or summarized — full narrative loads every time

### Step 8 — Slash Command Wrapper Creation

Create `.agent/workflows/[prefix]-[name].md` for every workflow:

```markdown
---
description: [Same description as the full workflow]
---

# /[prefix]-[name]

[Same opening as the full workflow — 1-2 sentences]

## Usage

\```
/[prefix]-[name] [arguments]
\```

## Full Workflow

Read and execute: `skills/[skill-name]/workflows/[workflow-file].md`

Load context: `skills/[skill-name]/genius.md`
```

### Step 9 — Context Compression Pass

Apply compression to everything EXCEPT the persona:

1. **Logic files**: Convert verbose instructions to tables/rules where clarity is maintained
2. **Library files**: Deduplicate across reference materials
3. **Workflow files**: Ensure no redundancy between workflows
4. **Persona**: DO NOT TOUCH. Narrative prose is the mechanism.

### Step 10 — Registration

1. Add agent to `AGENT_INDEX.md`
2. Add skill to `SKILL_INDEX.md`
3. Verify all slash command wrappers are in `.agent/workflows/`

---

## Quality Gate

- [ ] All files created: SKILL.md, genius.md, all workflows, AGENT.md, memory/context.md, persona.md
- [ ] Every workflow has a corresponding slash command wrapper
- [ ] SKILL.md workflow table matches actual files in workflows/ directory
- [ ] Genius.md is 3,000-6,000 words — comprehensive but not bloated
- [ ] Persona document is referenced in AGENT.md and loads uncompressed
- [ ] Agent is registered in system indices
- [ ] Compression applied to Logic/Library/Memory — NOT to Persona
