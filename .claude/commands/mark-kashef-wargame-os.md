---
description: "Fire when a mission will be executed by a cheaper model/session than the one planning it, when a wrong turn mid-execution is expensive, or when Farrice says wargame/battle plan/pre-fight/judgment banking. Converts frontier-model judgment into a failure-map a cheap executor run..."
---
<!-- auto-generated: skill-command shim (sync_registries.py) — safe to delete; regenerated on sync -->

Load and embody the skill at `skills/mark-kashef-wargame-os/SKILL.md`. Also load `skills/mark-kashef-wargame-os/genius.md` (Tier 2 — signature moves, exemplars, quality rubric; the methodology lives here, not in SKILL.md). Then apply that expert's methodology — their thinking, not their terminology — to the user's request, and self-score against the expert rubric before delivering.

This skill has runnable processes. Its flagship workflow is `skills/mark-kashef-wargame-os/workflows/wargame-order.md`. After loading, if the user's request fits a full structured run (not just a quick application), OFFER to execute it — and if they confirm or the request clearly calls for the full process, read and run that workflow file. See the skill's 'Available Workflows' table for the other processes.
