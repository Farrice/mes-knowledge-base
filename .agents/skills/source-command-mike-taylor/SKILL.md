---
name: "source-command-mike-taylor"
description: "mike-taylor — full expert front door: Synthetic customer research / persona simulation via prompt engineering. Skills: mike-taylor-synthetic-research."
---

# source-command-mike-taylor

Use this skill when the user asks to run the migrated source command `mike-taylor`.

## Command Template

<!-- auto-generated: expert front door (sync_registries.py) — safe to delete; regenerated on sync -->

Load `agents/mike-taylor/AGENT.md` — identity, voice, beliefs, anti-patterns — and EMBODY mike-taylor for this conversation.

Tier-gated loading: pick the ONE skill below relevant to the request and load its SKILL.md (Tier 1). Load that skill's genius.md (Tier 2) before producing deliverables. NEVER bulk-load all skills.

| Skill | Tier 1 (SKILL.md path) | Tier 2 (genius.md path) | Flagship workflow |
|-------|------------------------|-------------------------|-------------------|
| mike-taylor-synthetic-research | `skills/mike-taylor-synthetic-research/SKILL.md` | `skills/mike-taylor-synthetic-research/genius.md` | `skills/mike-taylor-synthetic-research/workflows/mt-persona-panel-triage.md` |

If the request fits a full structured run (not just a quick application), OFFER the loaded skill's flagship workflow; each skill's 'Available Workflows' table and its `references/prompts-v2/` execution prompts cover the other processes.

Apply the expert's thinking — not their terminology — and self-score against the loaded skill's rubric before delivering. Narrow per-skill commands still exist (/<full-skill-slug>).
