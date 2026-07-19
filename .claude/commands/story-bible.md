---
description: "Interview-driven skill that helps AI filmmakers, worldbuilders, and storytellers turn their story into a single dense canon document — the story's bible. Output is a ready-to-install SKILL.md the user drops into Claude as their own custom skill, so every future prompt (image,..."
---
<!-- auto-generated: skill-command shim (sync_registries.py) — safe to delete; regenerated on sync -->

Load and embody the skill at `skills/story-bible-builder/SKILL.md`. Also load `skills/story-bible-builder/genius.md` (Tier 2 — signature moves, exemplars, quality rubric; the methodology lives here, not in SKILL.md). Then apply that expert's methodology — their thinking, not their terminology — to the user's request, and self-score against the expert rubric before delivering.

This skill has runnable processes. Its flagship workflow is `skills/story-bible-builder/workflows/character-deep-dive.md`. After loading, if the user's request fits a full structured run (not just a quick application), OFFER to execute it — and if they confirm or the request clearly calls for the full process, read and run that workflow file. See the skill's 'Available Workflows' table for the other processes.
