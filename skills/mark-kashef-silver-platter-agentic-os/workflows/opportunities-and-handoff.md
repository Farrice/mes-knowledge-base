---
name: "Silver Platter — Opportunities Brief and Builder Handoff"
produces: "OPPORTUNITIES.md + builder_handoff.txt (+ claude_code_guide_handoff.txt if requested)"
expert: "Mark Kashef Silver Platter Agentic OS"
load_context: "genius.md"
---

# Mark Kashef Silver Platter — Opportunities Brief and Builder Handoff

## Role
You are running Component Order steps 6-8: render the opportunities brief as the Local Markdown Source and present it as a Rendered Conversation Document, then render the builder handoff for whoever scaffolds the OS, then checkpoint before any external install or write outside the active workspace. This is the executable-build-order deliverable — the thing a bare `data_map.html` is not (`genius.md` § Anti-Patterns). Full copy patterns live in `references/prompts-v2/opportunities-brief.md` and `references/prompts-v2/builder-handoff.md`.

**Before executing**: read `genius.md` § Pattern 5 (A Skill Is an Infinite Game) and § Pattern 4 (Regulated Data Comes First) if the archetype was flagged regulated in the audit step.

## Input Required
- Validated `data_map.json` from `assemble-and-render-data-map.md`.
- Archetype and regulated flag from `audit-and-classify.md`.
- Target builder: human operator, Claude Code, or Codex (changes handoff format).

## Workflow

1. `python3 skills/mark-kashef-silver-platter-agentic-os/scripts/render_opportunities.py --input silver_platter_output/data_map.json --output silver_platter_output/OPPORTUNITIES.md`. Sequence opportunities by setup priority, not by novelty — each entry names sources, schedule, owner, sample content, and a checkable output, per the SKILL.md Quality Bar.
2. `python3 skills/mark-kashef-silver-platter-agentic-os/scripts/render_handoff.py --input silver_platter_output/data_map.json --output silver_platter_output/builder_handoff.txt`, using `references/claude_code_handoff_template.md` as the template contract if the target builder is Claude Code.
3. If the archetype is regulated, confirm the handoff opens with model-containment/Bedrock language and per-domain hooks/rules before any conversion-hook or automation step — the healthcare example at transcript `00:20:24`–`00:20:45` is the negative case this guards against.
4. Checkpoint explicitly before any external install, regulated deployment, or write outside the active workspace. No automated proceed.
5. Present the opportunities brief to the operator as the Rendered Conversation Document — the plain-English walkthrough, not the raw markdown dump.

## Output Schema
```
OPPORTUNITIES.md:
  - opportunity: <title>
    sources: [...]
    schedule: <cadence>
    owner: <role or tool>
    sample_content: <example line/table>
    checkable_output: <what proves it worked>
builder_handoff.txt:
  target: human | claude_code | codex
  build_order: [ {step, rationale, checkpoint: bool} ]
  regulated_gate: <containment language, only if archetype.regulated == true>
```

## Quality Gate
1. Every `OPPORTUNITIES.md` entry has sources, schedule, owner, sample content, and a checkable output — none are missing.
2. `builder_handoff.txt` names the first buildable step explicitly (per validation-report.md's Cold-Start Proof requirement).
3. Regulated archetypes carry an approval gate on every human-facing Plate output before automation is proposed.
4. No external action, publish, or install is taken without an explicit operator checkpoint.

> **🛡️ Anti-Pattern Check**: Cross-reference `genius.md` § Anti-Patterns before delivering — confirm this handoff is not a rebrand of an existing Mark Kashef orchestration skill, and that the build order is genuinely executable, not decorative.
