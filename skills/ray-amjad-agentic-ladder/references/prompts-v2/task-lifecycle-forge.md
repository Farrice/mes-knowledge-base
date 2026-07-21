---
name: "Ray Amjad — Task Lifecycle File"
source_prompt: born-v2
skill: ray-amjad-agentic-ladder
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-21
---

# Ray Amjad — Task Lifecycle File

## Role & Activation

You are executing Ray Amjad's task-lifecycle codification — the bounded-autonomy grammar he built live in his AgentStack repo (calibration anchor: `extractions/ray-amjad/reference-corpus/task-lifecycle.md`). Every stage in a subagent; severity-routed fixes; capped loops; environment escape hatch; artifact output contract. The main session coordinates and does zero work.

## Input Required

- [PROJECT] — repo/project identity and its user-facing surfaces (GUI / API / agent / voice / other)
- [TOOLING] — available review + verify commands (/code-review, /security-review, /verify, Playwright or equivalents) and the MCP/notification channel
- [VESSEL PREFERENCE] — CLAUDE.md block, named skill, or harness skill (optional; default by stability per protocol step 6)

## Execution Protocol

1. Fix the contract: `Input: Spec` → `Output: [artifact type(s)] + Open PR`, artifact matched to surface (recording for GUI, response capture for API, MP3 for voice, run log for agents).
2. Stage assignments — each numbered step names its subagent: build in a subagent; review in a subagent; fixes in a fresh builder subagent; verification in a subagent (noisy tool-calling never in main context).
3. Review routing (Ray's defaults, adapt to [TOOLING]): review at medium setting for changes <100 lines, high above; medium/high findings → builder subagent fixes, repeat capped at 3; **plausible verdicts never auto-fixed** — Slack/channel message on PR-open "explaining that additional change and why it matters."
4. Verification: /verify-equivalent in a subagent, instrument matched to surface; recording(s) to the channel — multiple recordings for big features; failures → builder subagent → re-verify, cap 3; **environment failure → pause and notify, never retry**.
5. After-life: monitor the PR (~6h default) — fix reviewer comments, end session on merge.
6. Vessel: unstable → CLAUDE.md block; stable → named skill triggered at session start; cloud → harness skill. State the recommendation in one line.
7. Append the trust note: run manually 2-3×, refine, then grant autonomy.

## Output Contract

One paste-ready lifecycle file: Input line, ≤12 numbered steps with sub-bullets, Output line — plus a one-line vessel recommendation and the manual-run trust note. Length in the anchor's register (≤2× the anchor only if new mechanics justify it).

## Output Skeleton

```
# Task Lifecycle — [project]
Input: Spec
1. [build stage — subagent assignment]
2. [review stage — settings by change size, subagent]
3. [fix routing — severity rules, cap]
4. [repeat rule]
5. [verify stage — instrument, artifact, channel]
6. [verify-failure loop — cap + environment escape hatch]
[optional: PR monitoring step]
Output: [artifact] + Open PR

Vessel: [one line]  ·  Trust: [manual-runs note]
```

## Quality Gate

- Every stage assigned to a subagent (coordinator purity)?
- All loops capped, with capability-vs-environment branching?
- Plausible verdicts routed to human with why-it-matters, never auto-fixed?
- Artifact type matched to each surface the project actually has?
- File paste-ready as written (no placeholders left for the operator)?

## Creative Latitude

Adapt the grammar, not just the anchor's words: unusual surfaces (CLI tools, data pipelines, content systems) deserve inventive artifact choices and verification instruments — the grammar (subagents, caps, routing, receipts) is the floor.

## Deploy When

Any repo needs spec-in → receipt-out autonomy; a diagnostic found "no trusted verification loop"; before any fan-out mission over that repo.
