---
description: Convert MES 3.0 extractions into production-ready Antigravity skills
---

# Extraction-to-Skill Conversion

Convert MES 3.0 extractions into production-ready skills. This directive handles the structural conversion — for extraction itself, see `directives/mes-3.0-extract.md`. For validation, see `directives/mes-3.0-validate.md`.

## When to Use

You have an MES 3.0 extraction with:
- Content Assessment
- Executive Summary
- Genius Patterns
- Hidden Knowledge
- Methodology/Implementation
- Crown Jewel Prompts
- Example Outputs

## Conversion Mapping

| MES 3.0 Component | Skill Location |
|-------------------|----------------|
| Content Assessment + Executive Summary | SKILL.md (overview section) |
| Genius Patterns | references/genius-patterns.md |
| Hidden Knowledge | references/hidden-knowledge.md |
| Methodology + Implementation | references/implementation.md |
| Crown Jewel Prompts | references/prompts/*.md (one file per prompt) |
| Transcendence Opportunities | SKILL.md (integration section) |
| Example Outputs | assets/examples/*.md |

## Step-by-Step Process

### 1. Initialize Skill
```bash
python3 skills/skill-creator/scripts/init_skill.py [expert-name]-[domain] --path skills/
```

### 2. Clean Placeholders
```bash
rm -rf skills/[skill-name]/scripts
rm skills/[skill-name]/assets/example_asset.txt
rm skills/[skill-name]/references/api_reference.md
mkdir -p skills/[skill-name]/references/prompts
mkdir -p skills/[skill-name]/assets/examples
```

### 3. Create SKILL.md
Structure:
- Frontmatter with name + description
- Overview (from Executive Summary)
- Deployable Capabilities (from deployable skills list)
- Workflow Decision Tree (which prompt for which use case)
- Quick Start (from implementation pathway)
- Integration notes
- Resource links to all files

### 4. Create Reference Files
- `references/genius-patterns.md` - Extract and condense patterns
- `references/hidden-knowledge.md` - Extract tacit knowledge
- `references/implementation.md` - Extract timelines and pathways

### 5. Create Prompt Files
For each Crown Jewel Prompt → `references/prompts/[prompt-name].md`

Structure each prompt file:
- Role section
- Required Input section
- Execution section
- Output section
- Creative Latitude section
- Example Usage section

Key: Condense from MES format. Remove "THE ACTUAL DELIVERABLE" full examples (put those in assets/examples instead).

### 6. Create Example Outputs
- `assets/examples/[example-name].md` - Sample outputs showing prompt quality

### 7. Add LICENSE
Copy standard MIT license to LICENSE.txt

### 8. Validate & Package
```bash
python3 skills/skill-creator/scripts/package_skill.py skills/[skill-name]
```

## Quality Checklist

- [ ] SKILL.md has quoted description in frontmatter (no colons breaking YAML)
- [ ] All links in SKILL.md use relative paths
- [ ] Each prompt file is self-contained and deployable standalone
- [ ] At least 1 example output per prompt
- [ ] Prompt count matches source material depth (no arbitrary caps)
- [ ] Skill packages without validation errors
- [ ] If not yet validated, run `directives/mes-3.0-validate.md` before registration

## Naming Convention

`[expert-name]-[primary-domain]`

Examples:
- `samuel-thompson-product-launch`
- `nicolas-cole-content-stacking`
- `alex-hormozi-offer-creation`
