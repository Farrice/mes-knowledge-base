---
name: Skill Architecture Designer
command: /mcclain-skill-architect
expert: Corey McClain
category: Agent Forge
description: Design complete skill architecture — workflow tiers, stacking chains, genius.md structure — from extracted patterns
inputs: Expertise distillation output, identity profile, expert name
outputs: Complete skill architecture blueprint — workflow table, tier assignments, stacking map, file structure
---

# Skill Architecture Designer

Transform raw extracted intelligence into a structured skill architecture. This is the blueprint phase — you're deciding what workflows to build, how they tier, what stacks with what, and how the genius.md organizes. No code yet. Pure architectural design.

The difference from standard extraction architecture: every workflow is designed with the persona layer in mind. The architecture isn't just "what can this expert do" — it's "what can this expert do when they're fully embodied as a persona-based agent."

## Pre-Flight Gate

- [ ] Expertise distillation complete (genius patterns, signature moves, methodology map)
- [ ] Identity profile complete (worldview, voice, formation seeds)
- [ ] Expert name and domain confirmed

## Workflow

### Step 1 — Workflow Mining

From the expertise distillation, identify every potential workflow:

1. **From Signature Moves**: Each move rated "High" workflow potential → candidate workflow
2. **From Genius Patterns**: Patterns tagged Logic or Library → may need dedicated deployment workflows
3. **From Methodology Phases**: Each distinct phase in the methodology map → candidate workflow
4. **From Output Types**: Each distinct deliverable the expert can produce → candidate workflow
5. **From Decision Nodes**: Complex decision points → diagnostic/audit workflows

List ALL candidates. You'll cut later. Over-mine, then curate.

### Step 2 — Tier Assignment

Sort candidates into tiers:

**Tier 1 — Foundation** (3-4 workflows):
- The "if you had only 3 tools" workflows
- Core methodology deployment
- The workflow that captures the expert's central loop
- The diagnostic that tells you whether to use this expert at all

**Tier 2 — Practitioner** (3-5 workflows):
- Specific techniques that deserve their own command
- Content-type or context-specific applications
- Audit/diagnostic tools
- Granular deployment of individual genius patterns

**Tier 3 — Stacking** (2-4 workflows):
- Cross-expert compound workflows
- Creative applications outside the expert's obvious domain
- System-level integrations with existing Antigravity infrastructure

**Cut criteria** — remove candidates that:
- Overlap significantly with another candidate (merge them)
- Are too thin to sustain a full workflow (fold into a Foundation workflow as a step)
- Don't produce distinct outputs from another workflow
- Only apply in extremely rare situations

### Step 3 — Stacking Chain Design

For each Tier 3 workflow, map the compound:

```markdown
| Stack Partner | What Compounds | Workflow Name | Recommended Sequence |
|--------------|---------------|---------------|---------------------|
| [Expert] | [What happens when combined] | [workflow-name] | [Run A first → then B] |
```

Also check: which existing Antigravity experts naturally pair?
- Voice experts (ghostwriting, voice calibration) → persona voice integration
- Content experts (Kallaway, Grace, Diandra) → persona-shaped content agents
- Strategy experts (Oren, Dai, Junyuh) → persona-shaped strategy agents
- Architecture experts (Nate, Saraev) → memory/compression integration

### Step 4 — Genius.md Structure Design

Plan the genius.md organization:

```markdown
## Genius.md Structure

### Core Genius
[1 paragraph — the expert's irreducible contribution]

### Genius Patterns (N total)
[List all patterns with 1-line descriptions]

### Hidden Knowledge (N entries)
[List all hidden knowledge entries]

### Hall of Fame Exemplars (N total)
[List exemplars with brief context]

### Signature Moves (N total)
[List moves with deployment triggers]

### Quality Rubric
[N criteria — from expertise distillation]

### Methodology: [Method Name]
[Architecture from methodology map]

### Applied Intelligence
[Capability unlocks + system enhancements]
```

### Step 5 — File Structure Blueprint

Design the complete directory layout:

```
skills/[expert-name]-[domain]/
├── SKILL.md
├── genius.md
├── workflows/
│   ├── [prefix]-[workflow-1].md
│   ├── [prefix]-[workflow-2].md
│   └── ...
└── references/ (if needed)
    └── [reference-files].md

agents/[expert-name]/
├── AGENT.md
└── memory/
    └── context.md
```

### Step 6 — Architecture Presentation

Present the complete architecture as a single table:

```markdown
## Skill Architecture: [Expert Name] — [Domain]

### Workflow Table

#### Tier 1 — Foundation
| Workflow | Slash Command | Description | LLMP Focus |
|----------|--------------|-------------|------------|

#### Tier 2 — Practitioner
| Workflow | Slash Command | Description | LLMP Focus |
|----------|--------------|-------------|------------|

#### Tier 3 — Stacking
| Workflow | Slash Command | Description | Stack Partner |
|----------|--------------|-------------|--------------|

### Stacking Guide
[Table from Step 3]

### File Count
- Genius patterns: [N]
- Workflows: [N]
- Reference files: [N]
- Total files: [N]
```

---

## Output Schema

The **Skill Architecture Blueprint**, in the exact Step 6 template (`## Skill Architecture: [Expert Name] — [Domain]`): Workflow Table split by Tier 1/2/3 (each row: Workflow / Slash Command / Description / LLMP Focus or Stack Partner), the Stacking Guide table from Step 3, and a File Count summary (genius patterns / workflows / reference files / total). Paired with the Step 4 Genius.md Structure outline and the Step 5 File Structure directory tree. This is the design doc that precedes any file creation — no code, no markdown files written yet.

## Quality Gate

- [ ] 8-15 workflows designed (or 3-5 if --light flag)
- [ ] Every workflow has a distinct output that doesn't overlap with another
- [ ] Tier 1 captures the core methodology — you could use only Tier 1 and still get value
- [ ] At least 2 stacking chains map to existing Antigravity experts
- [ ] Genius.md structure accommodates all extracted intelligence
- [ ] File structure follows Antigravity conventions
