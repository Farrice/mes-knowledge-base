---
description: "Runs MetaHarness propose-evaluate-log-iterate loops to permanently improve agentic systems (workflows, prompts, retrieval logic, memory, orchestration). A coding-agent proposer inspects prior code + execution traces, diagnoses failure modes, proposes targeted edits or full rew..."
---
<!-- auto-generated: skill-command shim (sync_registries.py) — safe to delete; regenerated on sync -->

Load and embody the skill at `skills/self-evolving-systems/SKILL.md`. Also load `skills/self-evolving-systems/genius.md` (Tier 2 — signature moves, exemplars, quality rubric; the methodology lives here, not in SKILL.md). Then apply that expert's methodology — their thinking, not their terminology — to the user's request, and self-score against the expert rubric before delivering.

This skill has runnable processes. Its flagship workflow is `skills/self-evolving-systems/workflows/trajectory-ratchet.md`. After loading, if the user's request fits a full structured run (not just a quick application), OFFER to execute it — and if they confirm or the request clearly calls for the full process, read and run that workflow file. See the skill's 'Available Workflows' table for the other processes.
