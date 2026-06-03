---
description: "Author, extract, validate, and operate on DESIGN.md files (Google Labs spec, April 2026) — the universal brand-system-as-code format that any AI agent (Claude Code, Cursor, Stitch, Copilot, v0) consumes to produce on-brand UI without re-explaining the design system every prompt"
---
<!-- auto-generated: skill-command shim (sync_registries.py) — safe to delete; regenerated on sync -->

Load and embody the skill at `skills/design-md/SKILL.md`. Also load `skills/design-md/genius.md` (Tier 2 — signature moves, exemplars, quality rubric; the methodology lives here, not in SKILL.md). Then apply that expert's methodology — their thinking, not their terminology — to the user's request, and self-score against the expert rubric before delivering.

This skill has runnable processes. Its flagship workflow is `skills/design-md/workflows/03-import-brand.md`. After loading, if the user's request fits a full structured run (not just a quick application), OFFER to execute it — and if they confirm or the request clearly calls for the full process, read and run that workflow file. See the skill's 'Available Workflows' table for the other processes.
