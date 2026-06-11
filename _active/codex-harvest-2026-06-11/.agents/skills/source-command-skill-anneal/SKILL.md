---
name: "source-command-skill-anneal"
description: "Apply self-annealing to a specific skill's prompts"
---

# source-command-skill-anneal

Use this skill when the user asks to run `skill-anneal`, anneal a specific
skill prompt, repair a SKILL.md component using failure examples, improve a
skill's prompts with a rubric/test-input set, or tune one skill-system component
without rewriting the whole workflow.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/skill-anneal.md` as the canonical behavior source.
It must stay a thin compatibility wrapper and preserve:

- prompt-level skill/component annealing, not broad workflow evolution
- incomplete or vague goal packets produce queue-only diagnosis and missing fields
- annealing requires target skill directory, failure examples, rubric/test-input set, proof artifact, measurable stop condition, turn cap, and explicit no-regression clause
- preserve upstream input, downstream output, and validation contract when the skill belongs to a larger skill system
- limit edits to the single weakest criterion unless the user approves a broader rewrite
- side effects must be local, reversible, and inside `/Users/farricecain/Codex Antigravity`
- human checkpoint for broader workflow evolution, global mirrors, external actions, broad archive/delete, destructive cleanup, new dependencies, failed validation, or Mission repair
- broad workflow evolution routes to `/self-evolve`; repair/drift/broken-system language routes to `/system-audit` or `/autopilot`
- real Codex subagents require explicit authorization
- no competing behavior contract

## Command Template

Read and execute the workflow at `.agent/workflows/skill-anneal.md` — Apply self-annealing to a specific skill's prompts
