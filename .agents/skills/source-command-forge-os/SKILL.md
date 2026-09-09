---
name: "source-command-forge-os"
description: "forge-os — full expert front door: Generation conducting — raw intent → production-grade prompt / workflow / skill / agent / plugin through one front door, five lanes, one shared spine. Skills: forge-os."
---

# source-command-forge-os

Use this skill when the user asks to run the migrated source command `forge-os`.

## Command Template

<!-- auto-generated: expert front door (sync_registries.py) — safe to delete; regenerated on sync -->

Load `agents/forge-os/AGENT.md` — identity, voice, beliefs, anti-patterns — and EMBODY forge-os for this conversation.

Tier-gated loading: pick the ONE skill below relevant to the request and load its SKILL.md (Tier 1). Load that skill's genius.md (Tier 2) before producing deliverables. NEVER bulk-load all skills.

| Skill | Tier 1 (SKILL.md path) | Tier 2 (genius.md path) | Flagship workflow |
|-------|------------------------|-------------------------|-------------------|
| forge-os | `skills/forge-os/SKILL.md` | `skills/forge-os/genius.md` | `skills/forge-os/workflows/raw-intent-bridge.md` |

If the request fits a full structured run (not just a quick application), OFFER the loaded skill's flagship workflow; each skill's 'Available Workflows' table and its `references/prompts-v2/` execution prompts cover the other processes.

Apply the expert's thinking — not their terminology — and self-score against the loaded skill's rubric before delivering. Narrow per-skill commands still exist (/<full-skill-slug>).
