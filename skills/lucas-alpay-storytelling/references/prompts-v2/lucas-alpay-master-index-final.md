---
name: "Lucas Alpay Master Prompt Arsenal — Index (Final)"
source_prompt: "skills/lucas-alpay-storytelling/references/prompts/lucas-alpay-master-index-final.md"
skill: lucas-alpay-storytelling
standard: structure-pure-v2
refactored: 2026-07-11
---

# Lucas Alpay Master Prompt Arsenal — Index (Final)

## Role & Activation

This document is a navigation index, not a generative prompt — it maps the complete Lucas Alpay prompt library so an operator or agent can find the right prompt for a given task and understand how prompts combine into larger workflows. It supersedes the earlier v1 index where prompt names/numbering differ.

## Input Required

- **[TASK TYPE]**: What kind of deliverable is needed (fiction scene, business copy, book architecture, agent persona)
- **[STAGE]**: Where in the project this falls (opening, character, momentum, category-specific stages below)

## Execution Protocol

### Phase 1: Prompt Inventory Lookup
Consult the category tables (Fiction Writing, Business/Marketing, Book Writing, Expert Operating Systems) to find prompts matching [TASK TYPE].

### Phase 2: Stack Selection
Consult the relevant combined workflow (Fiction Project, Marketing Campaign, Brand Development, Premium Positioning) to see which prompts combine for [STAGE].

### Phase 3: Sequencing
Follow the workflow's order — each represents a tested sequence.

### Phase 4: Deployment
Route to the individual v2 prompt file (naming convention below) and execute it directly with its own Input Required fields.

## Output Contract

- **Deliverable**: An accurate, current index of the prompt library's structure-pure v2 files
- **Components**: category inventory tables (name + one-line function per prompt), combined workflows showing tested sequences, and the file naming convention
- **Format bounds**: entries must reference only prompts that actually exist in `references/prompts-v2/`; no invented prompt names or counts
- **Quality standard**: an operator should be able to find the right prompt for any task within two lookups (category table, then workflow)

## Output Skeleton

```
## CATEGORY A: FICTION WRITING
[subsections by stage — e.g. First Chapter Mastery, Character Mastery, Narrative Momentum]
| # | Prompt Name | Function |
|---|---|---|
[one row per fiction prompt actually present in prompts-v2/]

## CATEGORY B: BUSINESS/MARKETING
[same structure]

## CATEGORY C: BOOK WRITING
[same structure]

## CATEGORY D: EXPERT OPERATING SYSTEMS
[same structure]

## COMBINED WORKFLOWS
[named workflows showing tested prompt sequences, e.g. Fiction Project, Marketing Campaign, Brand Development, Premium Positioning]

## FILE NAMING CONVENTION
lucas-alpay-[category][number]-[short-name].md
```

*This is a navigation/reference document, not a single-deliverable prompt — its "skeleton" is the index structure above, re-verified against the actual prompts-v2/ directory whenever the library changes.*

## Quality Gate

1. **Every listed prompt exists**: each row in the category tables corresponds to an actual file in `references/prompts-v2/`
2. **No inflated prompt count**: the total count stated matches the actual file count, not a marketing figure
3. **No unverifiable framing**: no "virtuoso extraction," "MES 3.0," or completion-badge language ("✅ COMPLETE") — functional descriptions only
4. **Workflows reference real prompts**: every prompt named in a combined workflow exists in the inventory tables above it
5. **Naming convention matches reality**: the stated file naming pattern matches the actual v2 filenames on disk
6. **No duplicate/contradictory numbering vs. the v1 index**: if this index's F1-F21 naming differs from `lucas-alpay-master-index.md`, the discrepancy is noted rather than silently presented as consistent
