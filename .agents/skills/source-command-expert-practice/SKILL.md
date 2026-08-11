---
name: "source-command-expert-practice"
description: "Cold conductor that validates a practitioner or protocol packet, classifies proof stage and risk, selects one practice lane owner, and emits a bounded route receipt before paid POP or lane work begins."
---

# source-command-expert-practice

Use this skill when the user asks to run the migrated source command `expert-practice`.

## Command Template

<!-- auto-generated: skill-command shim (sync_registries.py) — safe to delete; regenerated on sync -->

Load and embody the skill at `skills/expert-practice-os/SKILL.md`. Also load `skills/expert-practice-os/genius.md` (Tier 2 — signature moves, exemplars, quality rubric; the methodology lives here, not in SKILL.md). Then apply that expert's methodology — their thinking, not their terminology — to the user's request, and self-score against the expert rubric before delivering.

This skill has runnable processes. Its flagship workflow is `skills/expert-practice-os/workflows/01-diagnose-and-route-practice.md`. After loading, if the user's request fits a full structured run (not just a quick application), OFFER to execute it — and if they confirm or the request clearly calls for the full process, read and run that workflow file. See the skill's 'Available Workflows' table for the other processes.
