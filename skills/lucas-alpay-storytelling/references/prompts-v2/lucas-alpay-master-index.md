---
name: "Lucas Alpay Master Prompt Arsenal — Index (v1)"
source_prompt: "skills/lucas-alpay-storytelling/references/prompts/lucas-alpay-master-index.md"
skill: lucas-alpay-storytelling
standard: structure-pure-v2
refactored: 2026-07-11
---

# Lucas Alpay Master Prompt Arsenal — Index (v1)

## Role & Activation

This document is a navigation index, not a generative prompt — it maps the complete Lucas Alpay prompt library so an operator or agent can find the right prompt for a given task and understand how prompts combine into larger workflows.

The prompt library was built from three source analyses of practitioner methodology: a first-chapter engagement system, a multi-perspective character/emotional-architecture system (drawing on principles observable in widely studied songwriting craft), and an elevated-genre storytelling system (drawing on principles observable in acclaimed independent film).

## Input Required

- **[TASK TYPE]**: What kind of deliverable is needed (fiction scene, business copy, book architecture, agent persona)
- **[STAGE]**: Where in the project this falls (premise, character, structure, opening, scene, depth, momentum, polish)

## Execution Protocol

### Phase 1: Prompt Inventory Lookup
Consult the category tables (Fiction, Business, Book Writing, Expert Operating Systems) to find prompts matching [TASK TYPE].

### Phase 2: Stack Selection
Consult the relevant synergy stack (Fiction Writing Stack, Business Content Stack, or Complete Funnel Stack) to see which prompts combine for [STAGE].

### Phase 3: Sequencing
Follow the stack's order — each stack represents a tested sequence, not an arbitrary list.

### Phase 4: Deployment
Route to the individual v2 prompt file (naming convention below) and execute it directly with its own Input Required fields.

## Output Contract

- **Deliverable**: An accurate, current index of the prompt library's structure-pure v2 files
- **Components**: category inventory tables (name + one-line function per prompt), synergy stacks showing tested sequences, and the file naming convention
- **Format bounds**: entries must reference only prompts that actually exist in `references/prompts-v2/`; no invented prompt names or counts
- **Quality standard**: an operator should be able to find the right prompt for any task within two lookups (category table, then stack)

## Output Skeleton

```
## CATEGORY A: FICTION PROMPTS
| # | Prompt Name | Core Function |
|---|---|---|
[one row per fiction prompt actually present in prompts-v2/]

## CATEGORY B: BUSINESS PROMPTS
[same structure]

## CATEGORY C: BOOK WRITING PROMPTS
[same structure]

## CATEGORY D: EXPERT OPERATING SYSTEMS
[same structure]

## SYNERGY STACKS
[named stacks showing tested prompt sequences for common workflows, e.g. Fiction Writing Stack, Business Content Stack, Complete Funnel Stack]

## FILE NAMING CONVENTION
lucas-alpay-[section]-[number]-[short-name].md
```

*This is a navigation/reference document, not a single-deliverable prompt — its "skeleton" is the index structure above, re-verified against the actual prompts-v2/ directory whenever the library changes.*

## Quality Gate

1. **Every listed prompt exists**: each row in the category tables corresponds to an actual file in `references/prompts-v2/`
2. **No inflated prompt count**: the total count stated matches the actual file count, not a marketing figure
3. **No unverifiable framing**: no "virtuoso-level," "MES 3.0," or extraction-branding language — functional descriptions only
4. **Stacks reference real prompts**: every prompt named in a synergy stack exists in the inventory tables above it
5. **Naming convention matches reality**: the stated file naming pattern matches the actual v2 filenames on disk
