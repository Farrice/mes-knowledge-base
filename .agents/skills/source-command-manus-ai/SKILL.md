---
name: "source-command-manus-ai"
description: "Manus.ai McKinsey-level consulting system: competitive intelligence, budget estimation, growth mapping, and AI-powered strategic research"
---

# source-command-manus-ai

Use this skill when the user asks to run the migrated source command `manus-ai`.

## Command Template

<!-- auto-generated: skill-command shim (sync_registries.py) — safe to delete; regenerated on sync -->

Load and embody the skill at `skills/manus-ai-consulting/SKILL.md`. Also load `skills/manus-ai-consulting/genius.md` (Tier 2 — signature moves, exemplars, quality rubric; the methodology lives here, not in SKILL.md). Then apply that expert's methodology — their thinking, not their terminology — to the user's request, and self-score against the expert rubric before delivering.

This skill has runnable processes. Its flagship workflow is `skills/manus-ai-consulting/workflows/strategic-market-intelligence-report.md`. After loading, if the user's request fits a full structured run (not just a quick application), OFFER to execute it — and if they confirm or the request clearly calls for the full process, read and run that workflow file. See the skill's 'Available Workflows' table for the other processes.
