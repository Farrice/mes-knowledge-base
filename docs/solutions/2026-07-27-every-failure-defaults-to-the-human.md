---
name: every-failure-defaults-to-the-human
problem_signature: "a check reports pass/fail with no notion of WHO fixes it, so every failure escalates to the human by default"
domain: system
tags: [self-healing, verification, classification, automation, compass-doctrine]
date: 2026-07-27
status: active
session: "a919a6cd"
---

## Problem

Farrice: *"What good does it do that we're logging these things if they don't
get fixed and healed and corrected? We're logging stuff, we're tracking
things, but nothing self-improving or self-healing... if it's not that big of
a deal that really needs my eyes or my blessings or my judgment."*

Concretely: 12 of 73 fleet verifiers red. One had been waiting days on a human
typing `--bless` for **1 drifted anchor out of 6,596** — a change made in a
named feature commit, `f41bd34f8 feat(dara): creative strategy layer`.

## Root Cause

**A missing classification, not a missing capability.** `verify_fleet` reports
pass/fail and nothing else. With no field answering *who fixes this*, every
failure escalates to the human by default. "12 failing" read as 12 decisions.
It was 3 root causes, 2 of them purely mechanical.

The escalations were also uninformative: a stack trace, not a diagnosis. Three
separate verifiers failed on the *same* cause (the workflow router no longer
ranks `/steering-compass` top-3, because the command corpus grew to 3,186)
and nothing said so.

## Approach That Worked

1. **Classify before escalating.** Add the field `verify_fleet` never had —
   *who fixes this* — and route on it (table below).
2. **Let git answer the deliberateness question.** Anything provable from the
   repo is evidence, not a decision to hand upward.
3. **Heal at session close, report in the brief.** The closeout spine applies
   fixes in the session that produced them; the 06:45 brief only reports.
4. **Demote a healer the moment its fix proves broken** rather than retrying
   it forever on a timer.
5. **Negative-control every safety property** before letting it write anything.

A three-way classification, applied before anything reaches a human:

| Class | Meaning | Action |
|---|---|---|
| `AUTO` | mechanical, deterministic, reversible, self-verifying | fix it, log it, never mention it |
| `EVIDENCE` | needs a human decision, but the evidence already exists on disk | fix it, say so once in `/cos` |
| `JUDGMENT` | taste, tradeoffs, or an unexplained change | never auto-heal; surface with a diagnosis |

The `EVIDENCE` tier is the unlock. "Was this change deliberate?" was being asked
of a human when **git already answers it**: an anchor whose file is tracked and
clean against HEAD went through a commit; that commit IS the deliberateness
evidence. Drift with *no* commit trail stays `JUDGMENT` forever — that silence
is the loss signal the check exists to catch.

Result: 12 red → 2 auto-repaired, 1 known-broken-fix demoted honestly, the
rest collapsed into 3 named root causes.

## Dead Ends

- **Auto-fixing `SLASH_COMMANDS.md`.** Shipped as `AUTO`, demoted to `JUDGMENT`
  on first run: `generate_slash_commands.py --check` reports 2,398 commands to
  append, then `main()` writes a 6-line diff. The generator is broken.
  Retrying a known-broken fix on a daily timer is how a self-healer becomes
  noise.
- **Keying deliberateness to a timestamp window** (`git log --since=<baseline
  mtime>`). `verify_born_intent_drift` REWRITES its baseline on every run to
  adopt newborn anchors, so the mtime means "last run", never "last bless".
  The window collapsed and flipped a correct `EVIDENCE` verdict to `JUDGMENT`
  mid-heal. Replaced with a timestamp-free committed-vs-working-tree test.
- **Running the scan inline in the `/cos` brief.** Pushed the morning brief
  past 120s. Now reads a cache written by the daily `heal` run — the same
  pattern `health_metrics.py` → `.agent/health/latest.json` already used.

## Verification

`python3 execution/verify_self_heal.py` → 38 pass / 0 fail. Seven sabotage runs
(see the table below); the first four:

| Sabotage | Result |
|---|---|
| `classify_drift` blesses everything (the dangerous bug) | 3 FAIL ✓ |
| healer stops re-running its check | 1 FAIL ✓ |
| `report` mutates the baseline | 1 FAIL ✓ |
| timestamp window reintroduced | 3 FAIL ✓ |

**A hole the verifier found in the healer:** `fleet_unhealed` skipped
`verify_system.py` unconditionally on the assumption a healer owned it. When
that verifier began failing for a reason no healer detected, the failure
vanished from the report entirely — *a red check made invisible by the tool
built to surface red checks.* A verifier is now skipped only when a detector
actually produced a finding for it; owned-but-unrepresented failures surface
as explicit blind spots.

**And a false RED the verifier produced against itself:** the "no timestamp
window remains" check string-matched `--since=` in the raw source and tripped
on the docstring *documenting the bug it guards against*. Tightened to match
live code only.

## Weaker-Model Trap

1. **Auto-healing by weakening the assertion.** Loosening a threshold to turn
   a check green is laundering — the exact failure the layer exists to stop.
   Structurally forbidden and tested for.
2. **Auto-blessing everything that drifted.** Blessing a change with no commit
   trail deletes the only warning that work went missing. A MIXED batch (some
   explained, some not) must escalate as a whole.
3. **Reporting a heal as successful without re-running the check.** Every
   healer re-verifies; `heal_failed` is a first-class outcome, and it fired
   for real on the SLASH_COMMANDS generator.
4. **Skipping a check because "a healer owns it."** Ownership is not
   representation. Skip only on an actual finding.

## Pointers

- `execution/self_heal.py` — `AUTO`/`EVIDENCE`/`JUDGMENT`, `HEALERS`, `CLASSIFIERS`, `HEALER_OWNS`
- `execution/verify_self_heal.py` — 38 checks · `execution/verify_failure_learning.py` — 30 checks
- `execution/cos_prep.py` — `gather_self_heal` / `render_self_heal` (report-only)
- `execution/end_session_closeout.py` — `step_self_heal`, runs before `commit-gate`
- `execution/failure_learning.py` · `evolution_store/failure-registry.md`
- `execution/hooks/pending_decisions_hook.py` — SessionStart surface
- `.agent/health/self-heal.jsonl` (audit log) · `self-heal-latest.json` (heal record) · `self-heal-report.json` (observation)
- Companion: `docs/solutions/2026-07-27-verification-with-no-reader.md`

## Session-End Architecture (Farrice, binding, 2026-07-27)

Healing happens at **session close**, not on a timetable. His words: *"it's not
something waiting to get healed later that day or the week, at a timetable
interval that is inconvenient if I'm creating at speed."* So:

- `end_session_closeout.py` step 1 (**before** `commit-gate`) runs
  `self_heal.py heal --no-commit`; the spine's commit gate then sweeps the
  repairs into the session's own commit rather than minting a second.
- The 06:45 `cos-prep` job was **demoted to `report`** — observation only.
- `pending_decisions_hook.py` (SessionStart) surfaces the JUDGMENT residue at
  the next session open, silent when clean.

## The seven negative controls

Every safety property was sabotaged and the suite had to fail:

| # | Sabotage | Caught by |
|---|---|---|
| A | `CHRONIC_FAILS` lowered 3 → 1 (registry records speculation) | **initially MISSED** — see below |
| B | learner appends a duplicate rule | 1 FAIL |
| C | learner overwrites hand-edited prose | 1 FAIL |
| D | `report` mode writes the heal cache again (D1 regression) | 1 FAIL |
| E | unscoped `git add -A` in the committer | 2 FAIL |
| F | healer loses its declared write-set | 1 FAIL |
| G | commit stages undeclared dirty files | 1 FAIL |

**Control A initially passed, and that is the most useful thing in this card.**
The threshold tests derived their counts from `fl.CHRONIC_FAILS`, so lowering
the constant moved the tests with it and all 24 checks stayed green while the
learner had begun recording noise. **A test that reads the constant it is
testing cannot detect that constant changing.** Fixed by pinning the values
(`CHRONIC_FAILS == 3`) and adding hardcoded-count probes.

## The false-RED trilogy (source-matching is not verification)

Three assertions in this suite produced false reds by string-matching source:

1. `"--since="` matched the docstring documenting the `--since=` bug.
2. `"git add -A"` matched the comment documenting the `git add -A` hazard.
3. `"add ."` matched a local variable named `add` followed by `.returncode`.

Tokenizing helped, then failed too. The fix that held: **parse the AST and
inspect the actual argv lists.** Textual matching cannot distinguish code from
prose from coincidence. `git_arg_lists()` in `verify_self_heal.py`.

## Final state

`verify_self_heal` 38/38 · `verify_failure_learning` 30/30 ·
`verify_execution_receipt` 34/34 · suites leave `git status` byte-identical ·
all three join the 76-verifier Sunday fleet.
