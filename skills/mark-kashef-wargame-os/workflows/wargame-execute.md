---
description: A wargame is graded DONE and it's time to hand it to a cheaper executor — dispatch it as the route, run every verification, log what survived contact
---

# /wargame-execute — Hand The Route To The Cheap Model

Takes a wargame that has passed `/wargame-grade` and runs it for real, through a cheaper model than the one that drafted and graded it. This is the payoff of the whole apparatus — "you pay for the genius once, you keep it forever" — so the pre-flight gate here is unusually strict: an ungraded or placeholder-laden wargame never reaches an executor.

## Pre-Flight Gate

1. **Is the wargame DONE in `LEDGER.md`?** `Read`/`Grep` the ledger for this mission's most recent verdict. Anything other than a literal `DONE` verdict (NOT-DONE, BLOCKED, missing, or only a self-grade with no red-team record) halts this workflow — route back to `/wargame-grade` instead.
2. **Are there zero unfilled placeholders?** `Bash`: `grep -n '{{' wargames/NN-<name>.md tasks/NN-<name>.md` — any hit is a hard stop. A DONE grade on a wargame that still contains a `{{PLACEHOLDER}}` is a ledger error, not a green light.
3. **Is the executor genuinely cheaper than the drafting/grading tier?** If not, there's no judgment-arbitrage gap to exploit — just execute directly without this workflow.
4. **Does the mission brief still match the wargame's frozen choices?** If Farrice changed the brief since grading, the wargame is stale — re-run `/wargame-run` before executing.

## Skill Acquisition

Load before executing:
- `skills/mark-kashef-wargame-os/genius.md` — Core Mechanism (supervision transfer), heuristic 1 (judgment arbitrage), Anti-Pattern 4 (no judgment calls left to the executor)
- The graded wargame: `wargames/NN-<name>.md`
- The mission brief: `tasks/NN-<name>.md`
- `LEDGER.md` — for the prior grade record and to append the execution entry

## Execution

1. **Verify gate results explicitly** — state the DONE verdict found, the grep result (empty), and the tier gap before proceeding. If any check failed, stop here; do not proceed "mostly."
2. **Read both artifacts** — `Read` the wargame file (the route) and the mission brief (the definition of done) in full.
3. **Dispatch the executor** — `Agent` with an explicit cheaper `model` (e.g. `"sonnet"`, never inherit a higher tier by default), passing: the mission brief as its orders, the wargame's moves/triggers/aborts/verification runs as its route, and instructions to (a) follow triggers exactly when observed, (b) stop and flag at any abort condition rather than improvise past it, (c) run every verification run listed, (d) report expected-vs-observed for each move it executed, never just "done."
4. **Run in the foreground** (`run_in_background: false`) — this mission needs its result before the ledger can close.
5. **Collect the per-move report** — expected vs. observed for each move, which triggers fired, whether any abort condition was hit, and the verification run results against their stated pass definitions.
6. **Classify the outcome per move**: matched the Expect line (survived contact as predicted), diverged and the wargame's Fail/Counter-move caught it (survived contact via the banked judgment), or diverged in a way the wargame never predicted (a genuine miss — the wargame's judgment gap, not the executor's failure).
7. **Write the ledger closure** — `Edit` `LEDGER.md`: what survived contact as predicted, what the counter-moves caught, what broke that neither the wargame nor the executor anticipated, and the specific patch that would close that gap next time.
8. **Route unanticipated breaks back** — if step 6 found any genuine miss, flag the mission for another `/wargame-grade` cycle before it's declared complete; a wargame that missed something in the field was not actually DONE.

## Dispatch Shape (Step 3, concrete)

```
Agent({
  description: "Execute wargamed mission <NN-name>",
  subagent_type: "general-purpose",
  model: "sonnet",
  prompt: "<mission brief verbatim> + <wargame moves/triggers/aborts/verification
    verbatim> + 'Follow this route. Do not ask a question — every fork already has
    a trigger. If you hit an abort condition, stop and report it instead of
    improvising. Report expected-vs-observed for every move you execute, and run
    every verification listed before you report done.'"
})
```

The prompt hands over artifacts (the brief, the route) — never a request to "use your judgment," because heuristic 1's whole premise is that judgment was already banked upstream. If the executor has to reason its way past a gap, that gap is a `/wargame-grade` miss, not something to patch conversationally mid-run.

## Content Type Adaptations

| Mission type | Verification runs the executor performs | What "survived contact" looks like |
|---|---|---|
| **Code build** | test suite before/after, browser exercise of every link/form/interactive element at the stated breakpoint | no unpredicted layout/behavior break; predicted fails caught by their counter-moves |
| **Copy-content** | reread as the stated skeptical ICP, confirm every line moves toward the CTA | voice and CTA match without a live judgment call; variant limits respected |
| **Research-analysis** | citation check on every claim, conflict-disclosure check | every claim traces to a source; no averaged-over conflicting data |
| **Ops-automation** | dry run of each automated phase's acceptance check | guardrail fires before the failure it's meant to catch, in the order predicted |

## Output Schema

```markdown
# Execution Closure — [mission] — NN-[name]

## Gate
- DONE verdict cited: [ledger date/cycle]
- Placeholder scan: [clean]
- Executor: [model] (drafting/grading ran at [tier])

## Per-Move Result
| Move | Expected | Observed | Trigger fired? | Verdict |
|---|---|---|---|---|

## Verification Runs
| Run | Pass definition | Result |
|---|---|---|

## Survived Contact
[what matched prediction, what the counter-moves caught]

## Unanticipated Breaks
[none / list with the move, what happened, and the patch owed to the wargame]

## Next Action
[complete / route to /wargame-grade for cycle N+1]
```

## Output Requirements

A `LEDGER.md` entry per mission recording: the DONE grade cited, the executor model used, per-move expected-vs-observed, which counter-moves fired and caught real divergence, any genuinely unanticipated break, and the patch recommended for the next `/wargame-grade` cycle if one is needed.

## Quality Gate

- [ ] Execution never started on a wargame without a literal DONE verdict on record (never "probably fine")
- [ ] Zero `{{PLACEHOLDER}}` confirmed via grep, not assumed from the grade alone
- [ ] The executor ran at a genuinely cheaper tier than drafting/grading — the arbitrage is real, not nominal
- [ ] The executor's report is expected-vs-observed per move, not a summary claim of "it worked" (Anti-Pattern 8 in the wider standard: claims without evidence)
- [ ] Any unpredicted break was routed back to `/wargame-grade`, not quietly patched in the field and forgotten
