---
description: Convert an MES 3.0 extraction into a production-ready skill
---

# /convert-extraction Workflow

Convert an MES 3.0 expert extraction into a modular, deployable skill.

## Prerequisites
- Extraction file must be in the Google Antigravity workspace
- Extraction should follow MES 3.0 format (Genius Patterns, Hidden Knowledge, Crown Jewel Prompts, etc.)

## Workflow Steps

### Step 1: Gather Extraction Details
Ask the user:
1. What is the file path to the extraction?
2. What is the expert's name?
3. What is the primary domain/skill area?

### Step 2: Read and Analyze Extraction
// turbo
Read the extraction file to identify:
- Number of Genius Patterns
- Number of Hidden Knowledge points
- Number of Crown Jewel Prompts
- Key methodology components

### Step 3: Initialize Skill Structure
// turbo
```bash
python3 "/Users/farricecain/Google Antigravity/skills/skill-creator/scripts/init_skill.py" [expert-name]-[domain] --path "/Users/farricecain/Google Antigravity/skills"
```

### Step 4: Clean Placeholder Files
// turbo
```bash
rm -rf skills/[skill-name]/scripts
rm -f skills/[skill-name]/assets/example_asset.txt
rm -f skills/[skill-name]/references/api_reference.md
mkdir -p skills/[skill-name]/references/prompts
mkdir -p skills/[skill-name]/assets/examples
```

### Step 5: Create SKILL.md
Create main skill file with:
- Quoted description in frontmatter (avoid YAML-breaking colons)
- Overview section (from Executive Summary)
- Deployable Capabilities list
- Workflow Decision Tree (which prompt for which use case)
- Quick Start section (from implementation pathway)
- Resource links to all reference files

### Step 6: Create Reference Files
Extract and condense into separate files:
- `references/genius-patterns.md` - All patterns with Execute/Success Metric format
- `references/hidden-knowledge.md` - Tacit knowledge points with Deploy instructions
- `references/implementation.md` - Timeline pathways (24hr/7day/30day)

### Step 7: Create Prompt Files
For each Crown Jewel Prompt → `references/prompts/[prompt-name].md`

Each prompt file must include:
- Role section (practitioner mode, not teacher)
- Required Input section
- Execution section (numbered steps)
- Output section (format, elements, quality standard)
- Creative Latitude section
- Example Usage section (brief, not full deliverable)

### Step 8: Create Example Outputs
Add 1-2 example outputs to `assets/examples/`:
- Extract from "THE ACTUAL DELIVERABLE" sections in original extraction
- Trim to essential demonstration (not full length)

### Step 9: Add LICENSE
// turbo
Copy MIT License to LICENSE.txt

### Step 10: Validate and Package
// turbo
```bash
python3 "/Users/farricecain/Google Antigravity/skills/skill-creator/scripts/package_skill.py" "/Users/farricecain/Google Antigravity/skills/[skill-name]"
```

### Step 11: Confirm Completion
Report to user:
- Skill name and location
- Number of files created
- List of prompts available
- Packaged .skill file location

## Quality Standards

- SKILL.md must have workflow decision tree
- Each prompt file must be self-contained and executable
- Patterns condensed to Execute/Success Metric format
- Hidden knowledge condensed to Deploy format
- No full example deliverables in prompt files (those go to assets/)

## Naming Convention
`[expert-firstname]-[expert-lastname]-[primary-domain]` or `[expert-name]-[primary-domain]`

Examples:
- `samuel-thompson-product-launch`
- `nicolas-cole-content-stacking`
- `alex-hormozi-offer-creation`
