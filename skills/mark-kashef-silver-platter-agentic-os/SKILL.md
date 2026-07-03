---
name: "Mark Kashef Silver Platter Agentic OS"
description: "Audit an operator's business tools, map Pantry -> Prep -> Plate, and turn the 80 percent data-prep layer into a reusable agentic OS build plan with summary tables, hooks, orchestrators, approval gates, and handoff files."
version: "1.0"
format: "skill-system"
workflows: 1
source_url: "https://www.youtube.com/watch?v=-WCNwxz3uoM"
source_package: "extractions/mark-kashef-perfect-agentic-os-kit/source_assets"
routing: long-tail
---

# Mark Kashef Silver Platter Agentic OS

Use this skill when an operator has an AI assistant, Claude Code setup, Codex workspace, or business tool stack that is not creating useful leverage because the data layer is messy. The job is not to summarize the business. The job is to map what the operator has today, decide what needs to become a weekly summary table or brief, and produce the build order for a useful agentic OS.

This is a companion to the existing Mark Kashef orchestration skills. Use those for agent-team architecture and council mechanics. Use this skill for the back-of-house data map and business operating system setup.

## Source Grounding

- Video evidence: `extractions/video-context/-WCNwxz3uoM/`
- Extraction brief: `extractions/mark-kashef-perfect-agentic-os-kit/extraction-brief.md`
- Local kit: `extractions/mark-kashef-perfect-agentic-os-kit/source_assets/`
- Contract: `semantic_libraries/antigravity/primitives/agentic-os-data-map-contract.md`

## Command Surface

Run through the workflow:

```bash
/silver-platter
/silver-platter --audit
/silver-platter --resume
/silver-platter ecommerce
```

Supported archetypes:

- `ecommerce`
- `saas`
- `professional_services`
- `healthcare_clinic`
- `wealth_advisory`
- `content_creator`
- `restaurant_multilocation`
- `real_estate_brokerage`
- `local_trades`

Aliases from the source package are also accepted in operator-facing copy: `law`, `clinic`, `wealth`, `creator`, `restaurant`, `realestate`, and `trades`.

## Operating Rule

Always preserve the 80/20 split:

- 80 percent: data prep, source inventory, summary tables, conversion hooks, scoped rules, audit trail, and clean handoffs.
- 20 percent: agents, orchestration, analysis, and automation layered on top.

If the operator asks for "agents" before the source data is mapped, route back to Pantry -> Prep -> Plate first.

## Component Order

1. **Audit** the current folder for existing Claude and Codex surfaces.
2. **Classify** the business archetype from `references/archetypes.md`.
3. **Interview** only for operator facts that cannot be derived from local files or defaults.
4. **Assemble** `data_map.json` with Pantry, Prep, Plate, recipes, setup priority, interaction layer, and opportunities.
5. **Render** `data_map.html` for visual review.
6. **Render** `OPPORTUNITIES.md` as the Local Markdown Source and present the main opportunities as a Rendered Conversation Document.
7. **Render** `builder_handoff.txt` for the person or agent who will scaffold the OS.
8. **Checkpoint** before external installs, regulated deployment, or any write outside the active workspace.

## Script Surface

```bash
python3 skills/mark-kashef-silver-platter-agentic-os/scripts/audit_existing_folder.py [path]
python3 skills/mark-kashef-silver-platter-agentic-os/scripts/render_data_map.py --input silver_platter_output/data_map.json --output silver_platter_output/data_map.html
python3 skills/mark-kashef-silver-platter-agentic-os/scripts/render_opportunities.py --input silver_platter_output/data_map.json --output silver_platter_output/OPPORTUNITIES.md
python3 skills/mark-kashef-silver-platter-agentic-os/scripts/render_handoff.py --input silver_platter_output/data_map.json --output silver_platter_output/builder_handoff.txt
python3 skills/mark-kashef-silver-platter-agentic-os/scripts/validate_examples.py
```

## Output Anatomy

```text
silver_platter_output/
├── data_map.json
├── data_map.html
├── OPPORTUNITIES.md
└── builder_handoff.txt
```

If the user explicitly wants Claude compatibility, also render `claude_code_guide_handoff.txt` from the same data map.

## Quality Bar

- The map uses the operator's actual tools and business words.
- Every generated brief has sources, schedule, owner, sample content, and a checkable output.
- Regulated archetypes put model/data containment before conversion hooks or automation.
- Hooks and rules are explained in plain English before primitive names are used.
- No external action, publishing, or install happens without approval.

