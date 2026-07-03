---
description: Audit an operator's business tools, map Pantry -> Prep -> Plate, and produce the silver-platter agentic OS build package
domains: system, business, operations, data
---

# /silver-platter - Mark Kashef Silver Platter Agentic OS

## Purpose

Turn messy business tools into a useful agentic OS data map and build order. The workflow audits what already exists, identifies the business archetype, derives the data map, renders the visual dashboard, and produces deterministic opportunities plus a builder handoff.

## Source Evidence

Read these before running a serious build:

1. `CLAUDE.md`
2. `semantic_libraries/antigravity/primitives/agentic-os-data-map-contract.md`
3. `skills/mark-kashef-silver-platter-agentic-os/SKILL.md`
4. `extractions/mark-kashef-perfect-agentic-os-kit/extraction-brief.md`
5. `extractions/video-context/-WCNwxz3uoM/video-context-ledger.md`
6. `extractions/video-context/-WCNwxz3uoM/uncertainty-report.md`

Load extra reference files only when needed:

- `skills/mark-kashef-silver-platter-agentic-os/references/archetypes.md`
- `skills/mark-kashef-silver-platter-agentic-os/references/question_library.md`
- `skills/mark-kashef-silver-platter-agentic-os/references/tool_defaults.md`
- `skills/mark-kashef-silver-platter-agentic-os/references/recipe_templates.md`
- `skills/mark-kashef-silver-platter-agentic-os/references/setup_priority_template.md`
- `skills/mark-kashef-silver-platter-agentic-os/references/opportunity_patterns.md`

## Modes

```bash
/silver-platter
/silver-platter --audit
/silver-platter --resume
/silver-platter ecommerce
```

Internal system-cohesion platters are supported through the recurring ops
runner, not a new user-facing slash command:

```bash
python3 execution/recurring_ops.py weekly-system-pulse
python3 execution/recurring_ops.py weekly-system-pulse --dry-run
```

For this internal OS use case, `/system-audit` supplies the proof spine and
Silver Platter supplies the Pantry -> Prep -> Plate mapping lens.

Supported archetypes: `ecommerce`, `saas`, `professional_services`, `healthcare_clinic`, `wealth_advisory`, `content_creator`, `restaurant_multilocation`, `real_estate_brokerage`, `local_trades`.

Aliases: `law`, `clinic`, `wealth`, `creator`, `restaurant`, `realestate`, `trades`.

## Operating Contract

| Field | Required Behavior |
|---|---|
| Source evidence | Cite video package and local kit paths; keep transcript-only visual limits explicit |
| Objective | Produce a reusable agentic OS data map and build order |
| Components | Root skill, this workflow, renderer scripts, source package, command bridge, semantic primitive |
| Step order | audit -> archetype -> interview -> data map -> render -> opportunities -> handoff -> checkpoint |
| Inputs | Working directory, business description, named tools, repeated weekly pain, preferred reading channel |
| Outputs | `data_map.json`, `data_map.html`, `OPPORTUNITIES.md`, `builder_handoff.txt` |
| Human checkpoint | Required before installs, external writes, regulated deployment, or modifying a user's actual `.claude/` |
| Validation | Example validation, render smoke tests, command discoverability, skill validation, cold-start proof |
| Result surface | Visual dashboard plus Rendered Conversation Document summary |
| Context policy | Keep command hot; keep full references and examples cold until needed |

For system-cohesion use, the same contract maps:

- Pantry: verifiers, routing logs, protocol tracker, system health, mission artifacts, recurring reports.
- Prep: route health, misroute ledger, dormant protocol summary, activation blockers, verifier status.
- Plate: weekly operator readout, supervised repair queue, next smoke-test prompt.

## Execution

1. **Audit first.**
   ```bash
   python3 skills/mark-kashef-silver-platter-agentic-os/scripts/audit_existing_folder.py [path]
   ```
   If existing Codex or Claude surfaces are found, acknowledge them and skip questions the audit already answered.

2. **Classify archetype.**
   Use `references/archetypes.md`. Translate the slug into plain English for the operator.

3. **Interview only for missing business facts.**
   Never ask schema-shaped questions. Ask about actual tools, weekly pain, scale, and where the operator wants to read the brief.

4. **Assemble `silver_platter_output/data_map.json`.**
   It must include `business`, `pantry`, `prep`, `plate`, `opportunities`, `recipes`, `setup_priority`, and `interaction_layer`.

5. **Render outputs.**
   ```bash
   python3 skills/mark-kashef-silver-platter-agentic-os/scripts/render_data_map.py --input silver_platter_output/data_map.json --output silver_platter_output/data_map.html
   python3 skills/mark-kashef-silver-platter-agentic-os/scripts/render_opportunities.py --input silver_platter_output/data_map.json --output silver_platter_output/OPPORTUNITIES.md
   python3 skills/mark-kashef-silver-platter-agentic-os/scripts/render_handoff.py --input silver_platter_output/data_map.json --output silver_platter_output/builder_handoff.txt
   ```

6. **Present the result.**
   Show the main opportunities in conversation as a Rendered Conversation Document. Treat `OPPORTUNITIES.md` as the Local Markdown Source, and keep that source readable without visible metadata frontmatter.

7. **Checkpoint before building the operator's OS.**
   This command maps and prepares. It must not silently install dependencies, write external systems, publish, send messages, or modify another workspace.

## Regulated Archetype Rule

For `healthcare_clinic`, `professional_services`, and `wealth_advisory`, model/data containment must appear before conversion hooks, silver platters, specialists, or slash commands. The build order must include Bedrock or equivalent approved deployment, scoped folders, path-scoped rules, audit logs, and approval gates.

## Validation

```bash
python3 skills/mark-kashef-silver-platter-agentic-os/scripts/validate_examples.py
python3 skills/mark-kashef-silver-platter-agentic-os/scripts/render_data_map.py --input skills/mark-kashef-silver-platter-agentic-os/examples/marco_ecommerce/data_map.json --output /private/tmp/marco_silver_platter.html
python3 skills/mark-kashef-silver-platter-agentic-os/scripts/render_data_map.py --input skills/mark-kashef-silver-platter-agentic-os/examples/sally_law/data_map.json --output /private/tmp/sally_silver_platter.html
python3 skills/mark-kashef-silver-platter-agentic-os/scripts/render_data_map.py --input skills/mark-kashef-silver-platter-agentic-os/examples/dr_anwar_derma/data_map.json --output /private/tmp/dr_anwar_silver_platter.html
python3 execution/validate_skill.py mark-kashef-silver-platter-agentic-os
python3 execution/validate_skill.py source-command-silver-platter
```

## Cold-Start Proof

A fresh operator should be able to ask:

```text
/silver-platter --audit
```

The system must identify:

- source evidence paths
- component order
- output files
- human checkpoints
- first action: run the audit script before asking tool-stack questions
