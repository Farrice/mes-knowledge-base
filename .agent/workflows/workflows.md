---
description: Browse and search all available workflows
---

# /workflows — Browse Available Workflows

Browse, search, and discover all available workflows (formerly slash commands). This replaces the slash command menu.

## Usage
```
workflows                     — Show all categories with counts
workflows search <keyword>    — Search by keyword in name or description
workflows <category>          — Show all commands in a category
```

## Steps

### 1. Read the Master Index
Read `SLASH_COMMANDS.md` to get the full list of available workflows with descriptions.

### 2. Present Results

**If no arguments**: Show a grouped summary by category with counts:
- Research & Strategy (10 commands)
- Multi-Agent Execution (10 commands)
- Copywriting & Ads (28 commands)
- Sales & Persuasion (6 commands)
- etc.

**If search term provided**: Filter commands whose name or description contains the search term. Show matching results with full descriptions.

**If category provided**: Show all commands in that category with descriptions.

### 3. Offer to Run
If only one command matches, or the user seems to know what they want, offer to run it immediately.

## Categories

| Category | Keywords |
|----------|----------|
| Research & Strategy | research, brief, analyze, landscape, trends, betting, picks, props, odds |
| Multi-Agent | swarm, council, parallel, roundtable, atomize |
| Copywriting | ad, copy, hook, vsl, script, fascination |
| Sales | gap, frame, objection, npq, persuade |
| ICP & Consumer | icp, consumer, posture, profile |
| Brand Strategy | brand, campaign, culture, emotional, taste |
| StoryBrand | storybrand, message, one-liner |
| Screenwriting | adapt, character, screenplay, subtext, erosion |
| Content Engines | ghostwrite, flywheel, comedy, serial, listing |
| AI Brain | ai-brain, context, deploy, discovery, intelligence |
| Business & Offers | offer, proposal, client, lifestyle, product |
| Design & Visual | design, video, image, carousel, wireframe, sketch |
| Asset & Building | project, asset, launch, package, blueprint |
| System & Skills | extract, convert, create-skill, deploy, skill-evolution, gap-report, audit |
| Session & Workflow | session, focus, refine, calibrate, validate, pulse |
