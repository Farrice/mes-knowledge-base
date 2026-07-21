---
description: Forge a project-specific Task Lifecycle (CLAUDE.md block or skill) — build→review→fix→verify→record→PR with caps and escalation
---

# Task Lifecycle Forge — Spec In, Receipt Out

Codifies Ray's bounded-autonomy grammar for a specific repo: every stage in a subagent, severity-routed fixes, capped loops, environment escape hatch, artifact output contract. The exemplar to match: `extractions/ray-amjad/reference-corpus/task-lifecycle.md`.

## Pre-Flight Gate

Load `genius.md` (patterns 2-6, 9) + the corpus exemplar. Require: repo/project identity, its user-facing surfaces (GUI/API/agent/voice/…), available review+verify tooling (/code-review, /security-review, /verify, Playwright or equivalent), and the notification channel. Missing surface info → ask; never assume.

## Skill Acquisition

- `genius.md` — Verification Surface Rule, Recording Receipt, Coordinator Not Worker, Severity-Routed Escalation, Capped Repair Loops
- `extractions/ray-amjad/reference-corpus/task-lifecycle.md` — the calibration anchor

## Execution

1. **Fix the contract**: Input: Spec → Output: artifact(s) + open PR. Name the artifact type per surface (recording for GUI, response capture for API, MP3 for voice, run log for agents).
2. **Assign every stage to a subagent**: build, review, fix, verify — main session coordinates only.
3. **Wire review routing**: review setting by change size (his defaults: medium <100 lines, high above); medium/high findings → builder subagent fixes, capped repeats (default 3); *plausible* verdicts → never auto-fixed, notify with why-it-matters on PR-open.
4. **Wire verification**: /verify (or equivalent) in a subagent, instrument matched to surface; artifact sent to the named channel; verification failures → builder subagent → re-verify, cap 3; **environment failures → pause + notify, never retry**.
5. **Add the after-life**: PR monitoring window (his default ~6h) — fix comments, end session on merge.
6. **Choose the vessel** per the migration path: new/unstable → CLAUDE.md block; stabilized → named skill triggered at session start; cloud harness → harness skill.
7. **Trust-ledger note**: instruct the operator to run it manually 2-3 times, refining, before granting autonomy (hidden knowledge #1).

## Content Type Adaptations

| Project type | Adaptation |
|---|---|
| Web app / GUI | Playwright recording mandatory; screenshots insufficient for flows |
| API/backend | Request/response captures as artifacts; add contract tests to step 2 tooling |
| Voice/audio agents | MP3 recording artifact; fake-mic strategy + credit caps noted as environment needs |
| Non-code (content/ops pipeline) | Same grammar — review=QA gate, verify=surface check, PR=deliverable hand-off |

## Output Requirements

A paste-ready lifecycle file (numbered, ≤12 steps, Input/Output contract lines) + one-line vessel recommendation + manual-run trust note.
Execution prompt: `references/prompts-v2/task-lifecycle-forge.md` — honor its Output Contract.

## Quality Gate

Reject if: any stage runs in the main session; any loop uncapped; environment failure retried instead of paused; plausible verdicts auto-fixed; artifact type unmatched to surface; longer than the anchor exemplar by >2× without new mechanics (genius.md anti-patterns).
