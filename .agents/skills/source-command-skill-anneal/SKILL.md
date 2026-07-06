---
name: "source-command-skill-anneal"
description: "Apply self-annealing to a specific skill's prompts"
---

# source-command-skill-anneal

Use this skill when the user asks to run the migrated source command `skill-anneal`.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/skill-anneal.md` as the
canonical behavior source. It must stay a thin compatibility wrapper with no
competing behavior contract.

Verification phrases: canonical behavior source; prompt-level skill/component annealing; real Codex subagents require explicit authorization; no competing behavior contract.

Preserve the current Skill-anneal contract: prompt-level skill/component
annealing; queue-only diagnosis for incomplete or vague goal packets; target
skill directory; failure examples; rubric/test-input set; proof artifact;
measurable stop condition; turn cap; explicit no-regression clause; single
weakest criterion; local, reversible side effects; human checkpoint for risky
changes; broad workflow evolution routes to `/self-evolve`; and real Codex
subagents require explicit authorization.

## Command Template

Read and execute the workflow at `.agent/workflows/skill-anneal.md` — Apply self-annealing to a specific skill's prompts
