---
name: "source-command-gpt-image"
description: "GPT Image 2.0 prompt director. Converts plain-text concepts into production-ready prompts for GPT Image 2.0, routing by output type — structured JSON (for UI mockups, infographics, landing pages, posters with dense layouts, character reference sheets, social media mockups, edi..."
---

# source-command-gpt-image

Use this skill when the user asks to run the migrated source command `gpt-image`.

## Command Template

<!-- auto-generated: skill-command shim (sync_registries.py) — safe to delete; regenerated on sync -->

Load and embody the skill at `skills/gpt-image-2-director/SKILL.md`. Also load `skills/gpt-image-2-director/genius.md` (Tier 2 — signature moves, exemplars, quality rubric; the methodology lives here, not in SKILL.md). Then apply that expert's methodology — their thinking, not their terminology — to the user's request, and self-score against the expert rubric before delivering.

This skill has runnable processes. Its flagship workflow is `skills/gpt-image-2-director/workflows/format-a-structured-json-layout.md`. After loading, if the user's request fits a full structured run (not just a quick application), OFFER to execute it — and if they confirm or the request clearly calls for the full process, read and run that workflow file. See the skill's 'Available Workflows' table for the other processes.
