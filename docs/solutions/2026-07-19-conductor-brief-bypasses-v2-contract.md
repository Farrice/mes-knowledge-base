---
name: Conductor Brief Bypasses v2 Output Contract → Audit-Shaped Output
problem_signature: expert-domain output comes back as an options memo / "what the expert would do" commentary instead of the user's asset rebuilt with decisions — despite the skill having structure-pure v2 prompts; user says "informative, but no real value"
domain: orchestration
tags: [orchestration, subagents, prompts-v2, output-contract, audit-vs-artifact, expert-deployment]
date: 2026-07-19
status: active
session: ron-lynch-arsenal
---

## Problem

Ron Lynch × Proof-to-Market deal-structure run returned a well-grounded OPTIONS MEMO (tables of what Lynch would do). Farrice: "I was expecting to actually see my offer structured through his lens and put together... it didn't give me any real value." The skill had 17+ passing v2 prompts at the time — the failure was not in the prompt library.

## Root Cause

Three-seam stack, all at the ORCHESTRATION layer, none in the prompts:
1. **Question-shaped ask passed through literally** ("what would a Lynch version look like?") — answered as a question instead of upgraded to the artifact.
2. **Conductor hand-briefed the subagent** without binding it to the skill's matching v2 prompt — so the Output Contract/Skeleton never governed the run and the model defaulted to helpful-explainer mode.
3. **Propose-only guardrail over-rotated**: "canonical offer untouched" was executed as "describe options" instead of "make the decisions, mark ratify-or-strike."

## Approach That Worked

1. Rebuild the asset itself: identity word chosen, pricing re-anchored, gates installed, sequence decided — closing with a ratify-or-strike line (propose-only AND decided are compatible).
2. The 5-second test: if the deliverable could be titled "What [expert] would do," it failed; it must only title as "Your [asset], done."
3. **Dispatch rule (binding forward)**: any Agent/subagent brief for expert-domain output MUST (a) name the matching `references/prompts-v2/` prompt and instruct the agent to Read it and honor its Output Contract, or (b) paste the Output Skeleton into the brief when no prompt matches. Never hand-brief expert output from scratch.
4. Question-shaped asks about the user's own asset get upgraded to build-shaped tasks at Mission Compile (Step 0/1), not answered literally.
5. Memory pair: `feedback_expert-lens-means-rebuild-not-audit.md` (CRITICAL, always-on).

## Dead Ends

- Blaming the prompt library — renaissance audit was 0-fail; the prompts are output-shaped by construction. Auditing them again finds nothing.
- Adding more "be practitioner-grade" prose to skill files — the leak is the unbound dispatch, not missing instructions.
