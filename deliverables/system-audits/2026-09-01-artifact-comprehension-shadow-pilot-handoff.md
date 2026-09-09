# System: Artifact Comprehension Shadow Pilot - Behavior Proven

## Completed

- Replaced the over-engineered conversational v0.1 with a narrow workspace-only artifact-comprehension layer that preserves the existing global Clear Depth response behavior and three-next-prompts closeout.
- Passed the human behavior gate after two refinements: insight-dense explanations remain concise, decision flows preserve direction, and jargon or decorative structure is rejected.
- Added intelligent output-surface selection so substantial work uses one fitting primary surface—conversation, writing block, native artifact, quantitative visual, slides, Briefing Room, or generated visual—only when that surface improves comprehension or use.
- Verified 8/8 representation fixtures, 13/13 artifact sabotage catches, 8/8 surface-selection fixtures, 6/6 surface-overuse catches, and the workspace authority and compiler checks.

## Decisions Locked

- Keep ordinary conversation governed by the existing global Clear Depth rules; do not add a second conversational response system.
- Apply the shadow only to substantial artifacts and durable knowledge work.
- Prefer insight density, reasons, and logic over fact lists; use plain language and less jargon.
- Use a decision flow when sequence, dependencies, or direction materially improve understanding.
- Choose one primary output surface. A second surface must perform a genuinely different job.
- Preserve the rollback boundary: workspace only; no merge, global activation, hook change, renderer change, or parallel dashboard.

## Remaining Priority

No work remains inside the approved v0.1 shadow-pilot boundary. The next independent decision is whether to review this proven branch for integration; promotion is deliberately not part of this closeout.

## Core Context Paths

- `deliverables/system-audits/2026-09-01-intelligent-output-surface-map.md`
- `deliverables/system-audits/2026-09-01-artifact-comprehension-morning-review.md`
- `execution/fixtures/burnout_safe_output/artifact-comprehension-contract-v0.2.md`

## Do Not Rebuild

- Do not redesign the global Clear Depth or three-next-prompts systems; they were explicitly preserved because they already work.
- Do not revive the broad v0.1 conversational shell or turn the surface selector into a mandatory menu.
- Do not merge, globally activate, modify hooks, or expand the runtime without a separate review and explicit approval.

## Proof And Retrieval

- Branch: `codex/burnout-safe-output-shadow-v01`
- Final implementation commit before closeout: `9cdcd05af`
- Human verdict: `APPROVED DIRECTION / BEHAVIOR PASS`
- Retrieval command: `/resume artifact-comprehension-shadow-pilot`

## Next-Time Prompt

Review the artifact-comprehension shadow pilot at commit `9cdcd05af` against current `main`. Preserve Clear Depth, the approved decision-flow behavior, the one-primary-surface rule, and the rollback boundary. Report only integration conflicts, regressions, or an evidence-backed promotion recommendation; do not merge or activate globally.

## Subagent Worth It?

No for ordinary use. A read-only verifier could help only during a future integration review because the current behavior and sabotage suites already passed.

## Reuse Hook

Use the surface map as the decision aid whenever a substantial deliverable could be easier to consume through a native artifact, quantitative chart, slides, Briefing Room, or a generated visual. The default remains the smallest surface that materially improves the work.
