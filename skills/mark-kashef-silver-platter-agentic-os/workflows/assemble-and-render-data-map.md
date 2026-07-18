---
name: "Silver Platter — Data Map Assembly and Render"
produces: "data_map.json + data_map.html"
expert: "Mark Kashef Silver Platter Agentic OS"
load_context: "genius.md"
---

# Mark Kashef Silver Platter — Data Map Assembly and Render

## Role
You are running Component Order steps 4-5: assemble `data_map.json` (Pantry, Prep, Plate, recipes, setup priority, interaction layer, opportunities) from the audit + interview output, then render it to `data_map.html` for visual review. Hold the 80/20 rule non-negotiable — see `genius.md` § The Core Thesis. Full field-by-field assembly logic lives in `references/prompts-v2/data-map-assembly.md`; this workflow is the execution contract for that assembly plus the render step.

**Before executing**: read `genius.md` § Pattern 1 (Pantry -> Prep -> Plate) and § Pattern 2 (Orchestrator Above Specialists).

## Input Required
- Audit findings + archetype classification (from `audit-and-classify.md`).
- Answers to `remaining_questions` from the interview.
- Named tools/sources with any volume the operator volunteered (e.g. "18,000 subs").

## Workflow

1. Assemble `data_map.json` per `references/prompts-v2/data-map-assembly.md` §Execution Protocol — Pantry sources, Prep silver-platter briefs (each with source, cadence, owner, sample content), Plate outputs (each with a named consumer and approval gate), recipe templates from `references/recipe_templates.md`, setup priority from `references/setup_priority_template.md`.
2. For every numeric metric slated for a Prep table, mark it `deterministic: true` and route it to Python aggregation, not LLM computation — this is the direct fix for the hallucination risk Kashef names at transcript `00:16:29`.
3. Run `python3 skills/mark-kashef-silver-platter-agentic-os/scripts/render_data_map.py --input silver_platter_output/data_map.json --output silver_platter_output/data_map.html`.
4. Validate structure against the five shipped examples: `python3 skills/mark-kashef-silver-platter-agentic-os/scripts/validate_examples.py`.

## Output Schema
```
data_map.json:
  pantry: [ {source, type, access_method} ]
  prep:   [ {name, source, cadence, owner, sample_content, deterministic: bool} ]
  plate:  [ {output, consumer, approval_gate: bool} ]
  recipes: [ {name, template_ref} ]
  setup_priority: [ {step, rationale} ]
  interaction_layer: {orchestrator_present: bool, specialists: [...]}
  opportunities: [ {title, effort, impact} ]
data_map.html: <rendered visual, self-contained, no external asset dependency>
```

## Quality Gate
1. `data_map.json` validates against `scripts/validate_examples.py` with zero errors.
2. Every Prep entry that touches a numeric KPI is marked `deterministic: true` — no metric is left to LLM arithmetic.
3. Regulated archetypes carry Bedrock/containment language on the first Pantry/Prep step touching sensitive data, per `genius.md` § Pattern 4.
4. `data_map.html` renders standalone (no missing template dependency) — confirmed by the standard-library fallback path when Jinja2 is unavailable.

> **🛡️ Anti-Pattern Check**: A beautiful `data_map.html` with no build order behind it is a named failure in `genius.md` § Anti-Patterns — this workflow only completes the map, not the deliverable; hand off to `opportunities-and-handoff.md` next.
