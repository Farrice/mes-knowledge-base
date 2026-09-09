---
name: "source-command-marketing-studio"
description: "Higgsfield Marketing Studio prompt director. Converts plain-text ad concepts into production-ready English video prompts optimized for Higgsfield Marketing Studio. Routes by preset (UGC, Tutorial, Unboxing, Hyper Motion, Product Review, TV Spot, Wild Card, UGC Virtual Try On,..."
---

# source-command-marketing-studio

Use this skill when the user asks to run the migrated source command `marketing-studio`.

## Command Template

<!-- auto-generated: skill-command shim (sync_registries.py) — safe to delete; regenerated on sync -->

Load and embody the skill at `skills/marketing-studio-director/SKILL.md`. Also load `skills/marketing-studio-director/genius.md` (Tier 2 — signature moves, exemplars, quality rubric; the methodology lives here, not in SKILL.md). Then apply that expert's methodology — their thinking, not their terminology — to the user's request, and self-score against the expert rubric before delivering.

This skill has runnable processes. Its flagship workflow is `skills/marketing-studio-director/workflows/hyper-motion-ad-prompt.md`. After loading, if the user's request fits a full structured run (not just a quick application), OFFER to execute it — and if they confirm or the request clearly calls for the full process, read and run that workflow file. See the skill's 'Available Workflows' table for the other processes.
