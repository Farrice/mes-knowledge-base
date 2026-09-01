# Analyst's Truth Standard — Live Readout Pressure Test

Date: 2026-09-01
Artifact tested: `python3 execution/system_health.py --quick` in the isolated
Codex worktree.

## Reporting-Only Read

The initial report said Performance Log was `ERROR`, Sovereign Memory was
`MISSING`, Session State was `DORMANT`, and Routing Intelligence was `DORMANT`.
Constitution lint separately reported three missing-path references.

That description was accurate for the worktree. Acting on it literally would
have pointed repair effort at canonical memory, routing intelligence, and
constitution references.

## Evidence Added

- `VERIFIED`: the worktree did not contain `.memory/sovereign.db`,
  `.agent/cos/goals.json`, or `.agent/session-state.md` before bootstrap.
- `VERIFIED`: canonical main contained all three, including a 108,109,824-byte
  Sovereign Memory database.
- `VERIFIED`: `python3 execution/worktree_lane.py bootstrap` returned
  `LANE READY ... FULL POWER (18 links ...)`.
- `VERIFIED`: the repeated health report changed Sovereign Memory, Session
  State, and Routing Intelligence to `ACTIVE`; memory exposed 7,646 records.
- `VERIFIED`: the repeated constitution lint changed from three failures to
  `{"failures": []}`.
- `VERIFIED`: Performance Log remained `ERROR`, so bootstrap did not explain
  or repair every red status.

## Analysis And Diagnosis

The first readout mixed canonical system health with lane provisioning. The
missing memory and dormant state were not evidence of lost canonical data; they
were symptoms of an unbootstrapped worktree. The mechanism is strongly
supported by the before/after change after the prescribed bootstrap.

Alternative explanations remain for the surviving Performance Log error: its
data may be genuinely absent, its reader may use another path, or the current
status script may be stale. This pressure test does not diagnose that residual
error.

## Decision Delta

Do not repair, recreate, or migrate canonical memory based on the initial
report. Bootstrap the lane and rerun the same checks first. Treat only the
surviving Performance Log error as an unresolved system-health finding.

## Confirm, Weaken, Reverse

- **Confirm:** the provisioned lane retains active memory/session/routing state
  on another fresh health run.
- **Weaken:** any of those states regress while their canonical targets remain
  valid and linked.
- **Reverse:** canonical main also loses the files, or the provisioned lane
  still reports them missing.

## Judgment

| Dimension | Result | Reason |
|---|---|---|
| Decision change | MATERIAL | Prevented a false canonical-memory repair and selected lane bootstrap first. |
| Causal restraint | PASS | The residual Performance Log error remains unresolved. |
| Insight density | PASS | Every retained section supplies evidence, inference, a decision, or a falsification condition. |
| Explanation burden | LOW | One mechanism and one residual unknown replace three misleading repair targets. |
| Creative-range preservation | NOT APPLICABLE | This was a system readout, not creative work. |

This is a real workspace pressure test, not one of the three promotion receipts.
It validates the behavior shape but does not establish repeated production lift.
