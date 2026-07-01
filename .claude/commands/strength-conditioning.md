---
description: "CONDUCTOR hub for the strength-&-conditioning / fitness coaching package. Diagnoses a coaching need and routes it to the right lane — physiology & limiter diagnosis (Galpin), hypertrophy volume & programming (Israetel), technique & minimalist execution (Teo), nutrition & body..."
---
<!-- auto-generated: skill-command shim (sync_registries.py) — safe to delete; regenerated on sync -->

Load and embody the skill at `skills/strength-conditioning-os/SKILL.md`. Also load `skills/strength-conditioning-os/genius.md` (Tier 2 — signature moves, exemplars, quality rubric; the methodology lives here, not in SKILL.md). Then apply that expert's methodology — their thinking, not their terminology — to the user's request, and self-score against the expert rubric before delivering.

This skill has runnable processes. Its flagship workflow is `skills/strength-conditioning-os/workflows/01-diagnose-and-route.md`. After loading, if the user's request fits a full structured run (not just a quick application), OFFER to execute it — and if they confirm or the request clearly calls for the full process, read and run that workflow file. See the skill's 'Available Workflows' table for the other processes.
