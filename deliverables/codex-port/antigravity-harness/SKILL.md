---
name: antigravity-harness
description: Use when the user wants Codex to access the imported Antigravity system: expert routing, agent methodologies, local workflows, context retrieval, directives, and the Antigravity Chain.
---

# Antigravity Harness In Codex

## Source Locations
- Live Antigravity repo: `/Users/farricecain/Google Antigravity`
- Codex vendor import: `/Users/farricecain/.codex/vendor_imports/antigravity-system`
- Native imported skills: `/Users/farricecain/.codex/skills`

## Operating Rule
When the user asks for Antigravity, an Antigravity expert, an imported workflow, or work that clearly matches the Antigravity system, load this skill first, then use the imported system files as local source-of-truth context.

## Fast Route
Run commands from the live repo unless the user explicitly asks to operate on the vendor copy:

```bash
cd "/Users/farricecain/Google Antigravity"
python3 execution/expert_router.py route "user request"
python3 execution/tool_router.py route "user request"
python3 execution/context_retriever.py search "user request"
python3 execution/workflow_router.py search "user request"
```

Use `DOMAIN_REGISTRY.md`, `AGENT_INDEX.md`, and `SKILL_INDEX.md` as fallback indexes.

## Loading Protocol
1. Identify the relevant expert or skill with `execution/expert_router.py` or `execution/context_retriever.py`.
2. Load the matching `skills/<slug>/SKILL.md` before producing domain output.
3. For complex or creative work, also load `genius.md` and one relevant workflow from `skills/<slug>/workflows/`.
4. For agent persona context, load `agents/<slug>/AGENT.md`.
5. For system behavior, prefer specific directive files in `directives/` over broad full-file reads.

## Important Directives
- Main harness rules: `GEMINI.md`
- Expert registry: `AGENT_INDEX.md`
- Skill registry: `SKILL_INDEX.md`
- Slash workflows: `SLASH_COMMANDS.md` and `.agent/workflows/`
- QA: `directives/quality_assurance.md`
- Intent pipeline: `directives/intent-pipeline.md`
- Notion access: `execution/notion_api.py`

## Codex Adaptation
Codex may use commentary plus tools during implementation, so interpret Antigravity's "never mix tool calls with text" rule as an Antigravity artifact-production preference, not as a reason to violate higher-priority Codex platform instructions.

For deliverables, preserve the Antigravity habit of routing, loading local context, producing from loaded sources, and validating quality before final response.
