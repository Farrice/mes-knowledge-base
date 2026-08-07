---
name: "Nicolas Cole EDAN Writing Mechanics"
description: "Diagnose and compose writing through Cole's EDAN framework: Explanation, Description, Action, and Narration"
version: "1.0"
format: "completion-engine"
expert: Nicolas Cole
domain: Writing mechanics, narrative composition, paragraph architecture, deliberate writing practice
workflows: 8
---

# Nicolas Cole EDAN Writing Mechanics

This skill turns Cole's EDAN framework into an operating surface for reading, diagnosing, practicing, and composing writing. EDAN treats every sentence or paragraph as one of four functional blocks: Explanation, Description, Action, or Narration.

Use it when a draft feels flat, overexplained, vague, motionless, thematically thin, or hard to improve through normal "write more" advice.

## Core Thesis

Writing improves when the writer stops treating "writing" as one bundled activity and starts seeing the page as assembled moves. Explanation gives context. Description creates implied meaning. Action creates movement and consequence. Narration reveals point of view. Mastery comes from identifying the block, knowing what each block does, practicing each block in isolation, then combining blocks deliberately.

## Available Workflows

| # | Workflow | Slash Command | Produces |
|---|---|---|---|
| 1 | [EDAN Block Map](workflows/01-edan-block-map.md) | `/edan-block-map` | Sentence/paragraph classification map across Explanation, Description, Action, and Narration |
| 2 | [EDAN Balance Audit](workflows/02-edan-balance-audit.md) | `/edan-balance-audit` | Diagnosis of overused/missing blocks and a revision plan |
| 3 | [Description Upgrade](workflows/03-description-upgrade.md) | `/edan-description-upgrade` | Rewrites that replace blunt explanation with implied meaning |
| 4 | [Action Weight Test](workflows/04-action-weight-test.md) | `/edan-action-weight` | Consequence audit for actions, scenes, examples, and narrative beats |
| 5 | [Narration POV Forge](workflows/05-narration-pov-forge.md) | `/edan-narration-pov` | Point-of-view lines, theme signals, and narration placement guidance |
| 6 | [EDAN Opener Builder](workflows/06-edan-opener-builder.md) | `/edan-opener-builder` | Block sequence openers designed to create a specific reader effect |
| 7 | [Deliberate Practice Loop](workflows/07-deliberate-practice-loop.md) | `/edan-practice-loop` | Focused training plan for one EDAN block or block combination |
| 8 | [Source Study Deconstruction](workflows/08-source-study-deconstruction.md) | `/edan-source-study` | Reverse-engineered EDAN map from a model passage plus reusable patterns |

## Skill Stacking

| Stack With | What It Adds |
|---|---|
| `nicolas-cole-sentence-craft` | Sentence-level polish after the EDAN block function is correct |
| `nicolas-cole-nonfiction-value-architecture` | Reader-value promise before EDAN shapes the paragraph mechanics |
| `yann-martel-storytelling-mastery` | Story-level envelope, ambiguity, and co-creation after EDAN maps local moves |
| `michael-connelly-vivid-writing` | Scene economy and vivid implication for Description/Action upgrades |
| `ghostwriting-voice-engine` | Client voice preservation while adding narration and block variety |

## Quick Reference

- Genius Context: [genius.md](genius.md)
- Genius Patterns: [references/genius-patterns.md](references/genius-patterns.md)
- Hidden Knowledge: [references/hidden-knowledge.md](references/hidden-knowledge.md)
- Quality Rubric: [references/quality-rubric.md](references/quality-rubric.md)
- Source Map: [references/source-map.md](references/source-map.md)

## Decision Framework

Use this skill when the issue is mechanical assembly: what a sentence is doing, what a paragraph is overusing, where a scene needs implication, why an action lacks weight, or how to train a specific writing move. Use `nicolas-cole-nonfiction-value-architecture` before this when the piece does not yet know what value it gives the reader. Use `nicolas-cole-sentence-craft` after this when the block function is right but the prose needs polish.
