# End-Session Visible Closeout Benchmark

## Purpose

This benchmark keeps the visible `/end-session` answer truthful to the actual
closeout lifecycle. It separates two valid result surfaces:

1. a verified completed closeout with compact, ranked continuation prompts
2. an approval-blocked or partial closeout with one exact authority boundary

It prevents ceremonial completeness: a polished answer that looks finished
while the durable handoff, Git receipt, global pointer, or native task action is
still dry-run, blocked, invalid, or incomplete.

## Authority And Source Evidence

- Function owner: `.agent/workflows/end-session.md`
- Coordinator truth: `execution/codex_end_session.py`
- Completed prompt data: `execution/contextual_next_prompts.py`
- Visible-surface verifier: `execution/verify_end_session_visible_closeout.py`
- Supporting contract: `semantic_libraries/antigravity/primitives/collaborative-steering-compass.md`
- Lifecycle rule: only `task_actions.archive: true` after a valid, non-dry-run,
  verified `done` receipt authorizes an archive claim

## Skill System Contract

| Field | Contract |
|---|---|
| Source evidence | The authority paths above plus the current coordinator receipt |
| Objective | Make visible closeout language match durable closeout state |
| Components | `/end-session`, Codex coordinator, compact renderer mode, benchmark verifier |
| Step order | Run coordinator -> read receipt -> choose visible state -> render or block -> verify |
| Inputs | Objective, exact handoff source, manifest, coordinator receipt, native task-action outcome |
| Outputs | Completed closeout or bounded approval-blocked closeout |
| Handoff summary | State, exact receipt result, recoverable path, next allowed action |
| Composition rule | `/end-session` owns; `/system-audit` diagnoses; `/source-to-skill-system` packages; no competing skill |
| Human checkpoint | Any global write, push, archive without valid receipt, or missing authority |
| Validation | Run `python3 execution/verify_end_session_visible_closeout.py` |
| Behavior-changing proof | Good fixtures pass and old-format/false-completion controls fail |
| Result surface | The final user-visible closeout answer |
| Context policy | Keep the receipt and exact blocker hot; load rich steering internals only on demand |
| Reuse hook | Every `/end-session` result and every future closeout renderer/sync change |

## Goal Packet

| Field | Value |
|---|---|
| target | Canonical local End-session visible-output contract |
| scope | Workflow, compact renderer mode, local wrapper/sync source, benchmark, verifier |
| per_item_criteria | Preserve lifecycle truth; remove retired labels; avoid self-routing; retain exactly three useful prompts only after completion |
| permitted_side_effect | Local reversible edits in the active Codex lane |
| proof_artifact | This benchmark plus verifier output |
| measurable_stop | Both good fixtures pass; every known-bad fixture fails; existing coordinator tests pass |
| turn_cap | One implementation pass plus one focused repair pass |
| evaluator | `execution/verify_end_session_visible_closeout.py` and End-session integration verifiers |
| wake_up_check | `python3 execution/verify_end_session_visible_closeout.py` |
| human_checkpoint | Global `~/.codex` sync, push, merge, archive, or destructive cleanup |
| rollback_or_archive_rule | Revert the lane patch; preserve receipts and benchmark evidence; never delete handoffs |

## Agentic Engineering Packet

| Field | Value |
|---|---|
| Objective | Make the next closeout visibly honest and compact |
| Source truth | Canonical workflow, coordinator task actions, renderer, and current instruction contract |
| Context plan | Keep only owner files and fixture text hot; skip unrelated steering libraries |
| Work chunks | Contract patch; compact render mode; fixture verifier; integration wiring |
| Review loop | Run focused verifier, then coordinator/operator-core no-regression checks; stop on pass |
| Dependency gate | Standard library only; no package or tool installation |
| Structure pass | One owner, one benchmark, one verifier; no new command, skill, hook, or schema |
| Use-now artifact | The completed and approval-blocked visible templates below |
| Hardening proof | Positive fixtures, negative controls, static owner checks, existing End-session tests |

## Concurrency Invariant

End-session coordination and lane reconciliation must share one operation lock
located on integration `main`. The lock is acquired before either closeout writes
or lane sealing begins and remains held through the operation. A contended
coordinator exits without writing; a contended reconciler parks the lane. The
verifier must prove contention fails, release permits retry, and the reconciler's
lock acquisition appears before its seal step.

For `codex-owned` Git policy, the legacy closeout spine must also skip broad
mission-brief regeneration and lane auto-merge. Only the manifest coordinator may
checkpoint its approved paths and push its current `codex/*` branch.

## State Decision

| Receipt and native action state | Visible result |
|---|---|
| `valid: true`, `dry_run: false`, no blockers, requested native action succeeded | Verified completed closeout |
| Dry run, denied escalation, invalid receipt, blocker, verifier failure, push failure, or incomplete native action | Approval-blocked or partial closeout |

Presentation never upgrades the state. A prepared handoff is not a saved
handoff; a dry-run action is not an archive; a local commit is not a verified
remote receipt.

## Winning Example: Verified Completed

```markdown
Closeout: COMPLETE
Coordinator receipt: VALID — handoff verified and requested task action applied.
Handoff: `.agent/handoffs/2026-08-31-parallel-lanes-reliability.md`

## 3 Next Prompts
1. **Prove cold-start retrieval for Parallel Lanes Reliability** — Confirms the saved handoff contains enough context for a fresh task.
   **Prompt:** "Replay the Parallel Lanes Reliability handoff in a cold-start simulation and report missing context."
2. **Stress-test the lane reconciler against a false-safe merge** — Protects the automation from merging active or semantically risky work.
   **Prompt:** "Add one adversarial lane-reconciler fixture for a conflict-free but unsafe lane and verify it parks."
3. **Turn lane health into a compact operator status card** — Makes the reliable state visible without opening every lane.
   **Prompt:** "Design a compact lane-health status card using existing list and reconciler receipts; do not add a new dashboard."

Operator move: Let receipts choose the lifecycle state before presentation chooses the format.
```

## Winning Example: Approval-Blocked

```markdown
Closeout: PENDING APPROVAL
Coordinator receipt: BLOCKED — global closeout registry write and branch push were not authorized.
Task remains unarchived. Prepared artifacts remain in `.tmp/end-session/parallel-lanes-reliability/`.
Approval needed: "Approve the End-session coordinator to write its pointer receipts under `~/.codex/end-session` and push only `codex/parallel-lanes-reliability-closeout`."
```

## Failure Cases

### False completion after dry run

```markdown
Saved + pinned: `.agent/handoffs/...`
Archived successfully.
```

Fail because dry-run or blocked evidence cannot authorize saved, pinned, or
archived claims.

### Completion-shaped menu while blocked

```markdown
Closeout blocked pending approval.
## 3 Next Prompts
1. **Keep going** ...
```

Fail because continuation prompts visually bury the authority boundary.

### Retired rich-field leakage

```markdown
1. **Use Now**
   - **Output/Capability Move:** ...
   - **Operator Insight:** ...
   - **Hidden Gap/Opportunity:** ...
   - **Capability Revealed:** ...
```

Fail because internal routing metadata and generic family labels replaced the
current compact user-facing contract.

### Closeout self-loop

```markdown
**Prompt:** "/end-session produce the fresh-session smoke test..."
```

Fail because a completed closeout must not route back into its own close ritual.

### Vague approval boundary

```markdown
I need your approval to continue.
```

Fail because it omits the exact authority, target, and recoverable state.

## Verifier Expectations

The deterministic verifier must:

- pass the completed example only when it has `Closeout: COMPLETE`, a valid
  coordinator receipt, exactly three numbered prompts, three copy-ready prompt
  lines, and an `Operator move:`
- pass the blocked example only when it has `Closeout: PENDING APPROVAL`, a
  blocked receipt, `Task remains unarchived`, a recoverable artifact path, and
  one `Approval needed:` sentence
- reject a blocked output containing `## 3 Next Prompts`
- reject completion claims after dry-run, denied, blocked, or invalid receipts
- reject `Use Now / Harden / Expand` and the retired rich-field labels from the
  compact completed surface
- reject any completed closeout prompt that routes back into `/end-session`
- statically confirm that the canonical workflow gates compact rendering on a
  valid non-dry-run receipt and points to this benchmark
- leave rich JSON prompt data available for internal routing and diagnostics;
  only the closeout presentation is compacted

## Cold-Start Replay Prompt

```text
Read semantic_libraries/antigravity/primitives/end-session-visible-closeout-benchmark.md and the current coordinator receipt. Classify the closeout as completed or approval-blocked. Render only the matching example shape, then run python3 execution/verify_end_session_visible_closeout.py. Do not write global files, push, merge, or archive unless the receipt and explicit authority permit it.
```

## Reuse Hook

Use this benchmark whenever `/end-session`, `contextual_next_prompts.py`, its
sync helper, global thin wrappers, or native task lifecycle actions change. It
is a companion primitive, not a new command or competing closeout workflow.
