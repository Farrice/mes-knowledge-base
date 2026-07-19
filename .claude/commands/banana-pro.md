---
description: "Higgsfield image prompt director for Banana Pro, Soul Cinema, and GPT-2. Modes: (0) face lock for new characters — Banana Pro (default), GPT-2 (higher fidelity, more credits), or Soul Cinema two-pass, on mid-gray seamless with a black camisole/tank baseline; (1) single-image c..."
---
<!-- auto-generated: skill-command shim (sync_registries.py) — safe to delete; regenerated on sync -->

Load and embody the skill at `skills/banana-pro-director/SKILL.md`. Also load `skills/banana-pro-director/genius.md` (Tier 2 — signature moves, exemplars, quality rubric; the methodology lives here, not in SKILL.md). Then apply that expert's methodology — their thinking, not their terminology — to the user's request, and self-score against the expert rubric before delivering.

This skill has runnable processes. Its flagship workflow is `skills/banana-pro-director/workflows/mode-0-face-lock.md`. After loading, if the user's request fits a full structured run (not just a quick application), OFFER to execute it — and if they confirm or the request clearly calls for the full process, read and run that workflow file. See the skill's 'Available Workflows' table for the other processes.
