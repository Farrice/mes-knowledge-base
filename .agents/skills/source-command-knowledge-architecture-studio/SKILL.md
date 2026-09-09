---
name: "source-command-knowledge-architecture-studio"
description: "knowledge-architecture-studio — full expert front door: knowledge extraction, expertise structuring, and agent encapsulation. Skills: knowledge-architecture-studio."
---

# source-command-knowledge-architecture-studio

Use this skill when the user asks to run the migrated source command `knowledge-architecture-studio`.

## Command Template

<!-- auto-generated: expert front door (sync_registries.py) — safe to delete; regenerated on sync -->

Load `agents/knowledge-architecture-studio/AGENT.md` — identity, voice, beliefs, anti-patterns — and EMBODY knowledge-architecture-studio for this conversation.

Tier-gated loading: pick the ONE skill below relevant to the request and load its SKILL.md (Tier 1). Load that skill's genius.md (Tier 2) before producing deliverables. NEVER bulk-load all skills.

| Skill | Tier 1 (SKILL.md path) | Tier 2 (genius.md path) | Flagship workflow |
|-------|------------------------|-------------------------|-------------------|
| knowledge-architecture-studio | `skills/knowledge-architecture-studio/SKILL.md` | `skills/knowledge-architecture-studio/genius.md` | `skills/knowledge-architecture-studio/workflows/01-extract-knowledge-architecture.md` |

If the request fits a full structured run (not just a quick application), OFFER the loaded skill's flagship workflow; each skill's 'Available Workflows' table and its `references/prompts-v2/` execution prompts cover the other processes.

Apply the expert's thinking — not their terminology — and self-score against the loaded skill's rubric before delivering. Narrow per-skill commands still exist (/<full-skill-slug>).
