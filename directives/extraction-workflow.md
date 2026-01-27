---
description: Scalable workflow for processing new expert extractions into agents and skills
---

# Extraction Workflow

End-to-end process for converting new MES 3.0 extractions into production agents and skills. Designed for scale—you have thousands coming.

## Overview

```
NEW EXTRACTION ARRIVES
        ↓
1. INTAKE → knowledge/extractions/inbox/
        ↓
2. ASSESS → Quality check + tier assignment
        ↓
3. DECIDE → Agent-worthy or skill-only?
        ↓
4. BUILD → Create agent/skill using templates
        ↓
5. REGISTER → Add to COUNCIL.md
        ↓
6. ARCHIVE → Move to processed/
        ↓
7. TEST → Invoke and verify
```

---

## Phase 1: Intake

### Move to Inbox
```bash
# Single file
mv ~/Downloads/[extraction-file].md ~/Google\ Antigravity/knowledge/extractions/inbox/

# Multiple files (same expert, multiple parts)
mv ~/Downloads/Claude-*[expert-name]*.md ~/Google\ Antigravity/knowledge/extractions/inbox/
```

### Rename to Standard Format
```
[expert-name]-[topic].md
[expert-name]-[topic]-pt2.md
[expert-name]-[topic]-pt3.md
```

Examples:
- `jeremy-miner-sales-masterclass.md`
- `cardinal-mason-ai-copywriting-pt1.md`
- `cardinal-mason-ai-copywriting-pt2.md`

---

## Phase 2: Assessment

### Quality Checklist

Read the extraction and verify it contains:

- [ ] **Content Assessment** - Source quality rating
- [ ] **Executive Summary** - One-paragraph expert distillation
- [ ] **Genius Patterns** - At least 5 extracted patterns
- [ ] **Hidden Knowledge** - Tacit/insider insights
- [ ] **Methodology** - Step-by-step frameworks
- [ ] **Crown Jewel Prompts** - At least 3 deployable prompts
- [ ] **Example Outputs** - Proof the prompts work

**Minimum viable extraction:**
- Has executive summary
- Has at least 3 genius patterns
- Has at least 3 prompts

If missing critical components, move to `knowledge/extractions/reference/` (useful but not convertible).

### Tier Assignment

Assign based on alignment with goals (Revenue → Family Presence):

| Tier | Focus | Priority |
|------|-------|----------|
| **Tier 1** | Revenue Direct | Build first |
| **Tier 2** | Content & Brand | Build second |
| **Tier 3** | Craft & Creation | Build third |
| **Tier 4** | AI & Operations | Build fourth |
| **Tier 5** | Design & Visual | Build last |

**Tier 1 indicators:** Sales, monetization, client acquisition, pricing, offers
**Tier 2 indicators:** Content strategy, personal brand, audience building
**Tier 3 indicators:** Writing craft, storytelling, creative excellence
**Tier 4 indicators:** AI tools, automation, workflows, systems
**Tier 5 indicators:** Visual design, graphics, aesthetics

---

## Phase 3: Decision - Agent or Skill?

### Build Full Agent When:
- Expert has distinct persona/philosophy
- Extraction includes decision frameworks
- You'll invoke them for strategic advice (not just execution)
- Their approach affects HOW you think about problems
- Would benefit from persistent memory

**Agent = Full persona + decision frameworks + memory + skill access**

### Build Skill Only When:
- Extraction is primarily prompts and patterns
- Expert is more "toolkit" than "advisor"
- You need their techniques but not their worldview
- Single-domain utility (one type of output)

**Skill = Prompts + patterns + examples (lighter weight)**

### Hybrid Approach (Recommended for most)
Build skill first → Add agent wrapper if invoking regularly

---

## Phase 4: Build

### 4A: Build Skill (Always do this first)

Follow `directives/extraction-to-skill.md` for full process. Quick reference:

```bash
# 1. Initialize skill structure
python3 skills/skill-creator/scripts/init_skill.py [expert-name]-[domain] --path skills/

# 2. Clean placeholders
rm -rf skills/[skill-name]/scripts
rm skills/[skill-name]/assets/example_asset.txt
rm skills/[skill-name]/references/api_reference.md
mkdir -p skills/[skill-name]/references/prompts
mkdir -p skills/[skill-name]/assets/examples

# 3. Create files from extraction
# - SKILL.md (from executive summary)
# - references/genius-patterns.md
# - references/hidden-knowledge.md
# - references/implementation.md
# - references/prompts/*.md (one per prompt)
# - assets/examples/*.md

# 4. Validate
python3 skills/skill-creator/scripts/package_skill.py skills/[skill-name]
```

### 4B: Build Agent (If agent-worthy)

**Step 1: Create agent folder**
```bash
mkdir -p ~/Google\ Antigravity/agents/[expert-name]/memory
```

**Step 2: Create AGENT.md**

Use template at `agents/_framework/AGENT_TEMPLATE.md`. Key sections:

```markdown
# [Expert Name] Agent

[Identity paragraph - who they are, their unique expertise]

## Philosophy
[Core beliefs, operating principles - from hidden knowledge]

## Core Competencies
1. [Competency from genius patterns]
2. [Competency from genius patterns]
3. [Competency from genius patterns]
4. [Competency from genius patterns]
5. [Competency from genius patterns]

## Available Skills
| Capability | Prompt | When Used |
|------------|--------|-----------|
[Map from skill prompts]

## Decision Framework
[How this expert approaches problems - from methodology]

## Activation Triggers
[When to invoke this agent vs use skill directly]

## Approval Gates
[High-stakes actions requiring user confirmation]

## Handoff Protocol
[When to delegate to other experts]

## Invocation
[Summary invocation text for system prompts]
```

**Step 3: Create memory/context.md**
```markdown
# [Expert Name] Context

## User Profile
[Populated after first interaction]

## Project Context
[Current projects using this expert]

## Preferences Learned
[Voice, style, approach preferences]

## Past Work Summary
[Key deliverables created]

## Notes
[Important learnings and adjustments]
```

**Step 4: Create symlink to skill**
```bash
cd ~/Google\ Antigravity/agents/[expert-name]
ln -s ../../skills/[skill-name]/references/prompts prompts
```

---

## Phase 5: Register

### Add to COUNCIL.md

**Quick Reference table:**
```markdown
| **[Expert Name]** | [Domain] | Active | `@[expert-handle]` |
```

**Expert Registry section:**
```markdown
#### [Expert Name]
- **Domain:** [Primary domain, secondary domain]
- **Agent Path:** `agents/[expert-name]/`
- **Skill Path:** `skills/[expert-name]-[domain]/`
- **Extraction:** `knowledge/extractions/processed/[files]`
- **Key Frameworks:** [Main frameworks from extraction]
- **Invoke:** `@[expert-handle]` or [natural language triggers]
- **Status:** Active
```

**Add to appropriate council:**
Update relevant council member table in COUNCIL.md.

### Update CLAUDE.md

Add to Available Agents table (if agent built):
```markdown
| **[Expert Name]** | [Domain description] | "@[expert-handle]" or [trigger requests] |
```

Add to Available Skills table (always):
```markdown
| `[skill-name]` | [Use for description] |
```

---

## Phase 6: Archive

### Move Processed Extractions
```bash
mv ~/Google\ Antigravity/knowledge/extractions/inbox/[expert-name]*.md \
   ~/Google\ Antigravity/knowledge/extractions/processed/
```

### Directory State After Processing
```
knowledge/extractions/
├── inbox/           # Empty or only unprocessed files
├── processed/       # All converted extractions
│   ├── jeremy-miner-sales-masterclass.md
│   ├── cardinal-mason-ai-copywriting-pt1.md
│   └── ...
└── reference/       # Extractions kept but not converted
    └── [partial-extraction].md
```

---

## Phase 7: Test

### Single Expert Test
```
@[expert-handle] Help me with [domain-specific request]
```

Verify:
- [ ] Agent persona comes through (if agent built)
- [ ] Frameworks from extraction are used
- [ ] Output quality matches extraction examples
- [ ] Memory updates after interaction

### Council Test (if added to council)
```
@[council-name] [request in council domain]
```

Verify:
- [ ] New expert contributes alongside existing members
- [ ] Perspective is distinct and valuable
- [ ] No conflicts with existing experts

### Skill-Only Test (if no agent)
```
Read skills/[skill-name]/references/prompts/[prompt].md
Execute the prompt with sample input
```

Verify:
- [ ] Prompt produces expected output type
- [ ] Quality matches extraction examples

---

## Quick Reference Commands

### Full Workflow (Copy-Paste Template)
```bash
# 1. Move to inbox
mv ~/Downloads/Claude-*[EXPERT]*.md ~/Google\ Antigravity/knowledge/extractions/inbox/

# 2. Rename files
cd ~/Google\ Antigravity/knowledge/extractions/inbox/
# Rename to: [expert-name]-[topic].md

# 3. Initialize skill
cd ~/Google\ Antigravity
python3 skills/skill-creator/scripts/init_skill.py [expert-name]-[domain] --path skills/

# 4. Clean skill folder
rm -rf skills/[skill-name]/scripts
rm skills/[skill-name]/assets/example_asset.txt
rm skills/[skill-name]/references/api_reference.md
mkdir -p skills/[skill-name]/references/prompts
mkdir -p skills/[skill-name]/assets/examples

# 5. Create agent folder (if building agent)
mkdir -p agents/[expert-name]/memory

# 6. After creating files, validate skill
python3 skills/skill-creator/scripts/package_skill.py skills/[skill-name]

# 7. Archive extraction
mv knowledge/extractions/inbox/[expert-name]*.md knowledge/extractions/processed/
```

---

## Batch Processing

For processing multiple extractions efficiently:

1. Move all to inbox
2. Assess and tier all (make list)
3. Process by tier (highest priority first)
4. Build all Tier 1 skills
5. Add agents for Tier 1
6. Update COUNCIL.md once (not per expert)
7. Test all Tier 1
8. Repeat for next tier

---

## Troubleshooting

### Extraction Has Multiple Parts
Combine intellectually when building skill/agent. Parts usually cover:
- Part 1: Foundations, philosophy, core patterns
- Part 2: Methodology, prompts
- Part 3: Advanced techniques, examples

### Expert Overlaps With Existing
- If same domain: Consider whether new expert adds unique value
- If complementary: Add to same council
- If redundant: Keep in reference/, don't build

### Extraction Quality is Low
- Move to `reference/` folder
- Note what's missing
- May be useful for augmenting other experts

### Skill Validation Fails
- Check YAML frontmatter (quoted descriptions, no colons)
- Check all paths are relative
- Ensure all required files exist

---

*Last updated: 2026-01-23*
*Designed for scale: thousands of extractions → hundreds of experts*
