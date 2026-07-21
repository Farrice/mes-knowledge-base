---
name: "Ray Amjad — System Ladder Audit Card"
source_prompt: born-v2
skill: ray-amjad-agentic-ladder
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-21
---

# Ray Amjad — System Ladder Audit Card

## Role & Activation

You are executing the ladder audit against a BUILT Claude Code system — its CLAUDE.md, hooks, routines, skills, memory — rather than a person's habits. Method: Ray's two-test loop-trust diagnosis + Boris's L3/L4 tooling columns as the checklist. Rule: audit from the system's actual files, never from memory of the system.

## Input Required

- [SYSTEM FILES READ] — the actually-read CLAUDE.md, hook configs, routine/cron definitions, lifecycle-adjacent directives (list what was read)
- [SYSTEM OUTPUT EVIDENCE] — how recent deliverables shipped (artifact receipts? automated review or ritual?)
- [DOCTRINE FILES] — for Antigravity: orchestration doctrine + failure-map locations (optional otherwise)

## Execution Protocol

1. Build the mechanics table — for each cell, record EXISTS (where: file/hook) / PARTIAL (the gap) / MISSING:
   self-verification loops on the output's surface · automated review with severity routing · capped repair loops · context pull-in (wikis/memory with the contradiction rule) · loops and routines running unattended · proactive kickoff (Claude kicks off Claude) · monitor-by-exception.
2. Score the system's level via the two-test challenge applied to its outputs (receipts vs claims; review automated vs ritual).
3. Map Ray-shaped upgrades: for each PARTIAL/MISSING cell, the mechanism that closes it (task lifecycle grammar / environment provisioning / routine spec / fan-out grammar / vision filter) and the concrete file or hook it would live in. Extend, never rebuild, where a partial mechanism exists.
4. Trust-ledger check: for every autonomous loop already running, evidence it earned trust (manual runs, failure maps) — flag optimism-granted autonomy.
5. Rank by Boris's unlock column; cap at 5 upgrades.

## Output Contract

One audit card: mechanics table (7 rows) · system level with two-test evidence lines · top-5 upgrade list (mechanism → target file → unlock) · optimism-granted-autonomy flags · files-read provenance line.

## Output Skeleton

```
SYSTEM LADDER AUDIT — [system]
Files read: [list]

| Mechanic | Status | Where / gap |
|---|---|---|
| Self-verification on surface | […] | […] |
| Automated review + routing | […] | […] |
| Capped repair loops | […] | […] |
| Context pull-in | […] | […] |
| Loops & routines | […] | […] |
| Proactive kickoff | […] | […] |
| Monitor-by-exception | […] | […] |

Level: [N] — [two-test evidence, one line each]
Top upgrades (max 5): 1) [mechanism → file → unlock] …
Autonomy flags: [optimism-granted loops, if any]
```

## Quality Gate

- Every table row cites a file/hook or names the specific gap?
- Level evidenced from outputs, not architecture diagrams?
- ≤5 upgrades, each with a concrete target file?
- Extend-not-rebuild honored where partial mechanisms exist?
- Trust-ledger check performed on all running loops?

## Deploy When

Auditing Antigravity or any client's Claude Code system; before granting an existing system wider autonomy; annually per system.
