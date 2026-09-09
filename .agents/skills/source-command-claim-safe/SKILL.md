---
name: "source-command-claim-safe"
description: "The claim-substantiation gate for health, wellness, and supplement brand marketing. Classifies claims (disease vs. structure/function vs. qualified vs. puffery), maps claim strength to required evidence tier (FTC's competent-and-reliable-scientific-evidence standard), rewrites..."
---

# source-command-claim-safe

Use this skill when the user asks to run the migrated source command `claim-safe`.

## Command Template

<!-- auto-generated: skill-command shim (sync_registries.py) — safe to delete; regenerated on sync -->

Load and embody the skill at `skills/claim-safe-health-marketing/SKILL.md`. Also load `skills/claim-safe-health-marketing/genius.md` (Tier 2 — signature moves, exemplars, quality rubric; the methodology lives here, not in SKILL.md). Then apply that expert's methodology — their thinking, not their terminology — to the user's request, and self-score against the expert rubric before delivering.

This skill has runnable processes. Its flagship workflow is `skills/claim-safe-health-marketing/workflows/01-claim-audit.md`. After loading, if the user's request fits a full structured run (not just a quick application), OFFER to execute it — and if they confirm or the request clearly calls for the full process, read and run that workflow file. See the skill's 'Available Workflows' table for the other processes.
