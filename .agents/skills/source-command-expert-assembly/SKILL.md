---
name: "source-command-expert-assembly"
description: "Hybrid expert panel system — roster selection + bespoke persona synthesis + multi-round deliberation + tiered implementation roadmap for any domain."
---

# source-command-expert-assembly

Use this skill when the user asks to run the migrated source command `expert-assembly`.

## Command Template

<!-- auto-generated: skill-command shim (sync_registries.py) — safe to delete; regenerated on sync -->

Load and embody the skill at `skills/expert-assembly-os/SKILL.md`. Also load `skills/expert-assembly-os/genius.md` (Tier 2 — signature moves, exemplars, quality rubric; the methodology lives here, not in SKILL.md). Then apply that expert's methodology — their thinking, not their terminology — to the user's request, and self-score against the expert rubric before delivering.

This skill has runnable processes. Its flagship workflow is `skills/expert-assembly-os/workflows/assemble.md`. After loading, if the user's request fits a full structured run (not just a quick application), OFFER to execute it — and if they confirm or the request clearly calls for the full process, read and run that workflow file. See the skill's 'Available Workflows' table for the other processes.
