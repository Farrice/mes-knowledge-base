---
description: Classify harness failures AUTO/EVIDENCE/JUDGMENT, repair the mechanical ones, and surface only what needs your judgment — with the recurrence learner that turns repeat failures into written prevention rules
---

# /self-heal — repair what a machine can prove, escalate only what needs taste

**You almost never need to run this.** It fires automatically at session close
(`end_session_closeout.py`, step 1) and reports in the `/cos` morning brief.
Reach for it when you want the current picture on demand, or after a big change.

## Why this exists

`verify_fleet` reports 73 verifiers as pass/fail with **no field for who fixes
this** — so every failure escalated to Farrice by default. 12 red checks looked
like 12 decisions. They were 3 root causes, 2 purely mechanical, and one had
been waiting days on a one-word `--bless` for a change a named feature commit
had already justified.

## The classification

| Class | Meaning | What happens |
|---|---|---|
| `AUTO` | mechanical, deterministic, reversible, self-verifying | repaired, committed, never mentioned |
| `EVIDENCE` | needs a decision, but the evidence is already on disk (a git commit trail) | repaired, mentioned once |
| `JUDGMENT` | taste, tradeoffs, or an **unexplained** change | never auto-healed; surfaced with a diagnosis |

## Commands

```bash
python3 execution/self_heal.py report        # read-only classification
python3 execution/self_heal.py heal          # apply AUTO + EVIDENCE repairs
python3 execution/self_heal.py heal --no-commit   # repair, let the caller commit
python3 execution/self_heal.py report --json
python3 execution/failure_learning.py        # recurrence -> prevention rules
python3 execution/failure_learning.py --report
```

## Reading the output

- `[FIXED]` — done, committed, nothing owed.
- `[COULD NOT FIX]` — the healer ran, re-checked, and refused to claim success.
  Believe it: a heal that does not verify green is reported as a failure.
- `needs your judgment` — the only lines worth your attention. Each carries a
  diagnosis and an exact command, never a stack trace.

## Guardrails (why this is safe to let run unattended)

- **Allowlist only.** An unknown failure is `JUDGMENT` by default.
- **Never heals by weakening an assertion.** Loosening a threshold to turn a
  check green is laundering — structurally forbidden and tested for.
- **Every heal re-runs its check.** `heal_failed` is a first-class outcome.
- **Drift with no commit trail is never blessed.** That silence is the
  lost-work signal the drift check exists to catch.
- **Scoped commits.** `git add <declared paths>` only — never `git add -A`.
  Decline with `SELF_HEAL_NO_AUTOCOMMIT=1`. Commits auto-push (post-commit hook).

## The anti-repeat loop

`failure_learning.py` reads `.agent/health/self-heal.jsonl` and converts
recurrence into rules in `evolution_store/failure-registry.md`:

| Pattern | Verdict |
|---|---|
| `heal_failed` ≥3× for one id | **CHRONIC** — the fix is broken; stop retrying it |
| healed ≥5× over ≥5 days | **RECURRING** — the cause is upstream, not here |
| a `JUDGMENT` id open ≥7 days | **ROTTING** — a decision nobody made |

That registry sat empty from 2026-04-04 to 2026-07-27 because its only writer
was `/aar`, a command nobody remembered to run. It now fills itself.

## Verifiers

```bash
python3 execution/verify_self_heal.py
python3 execution/verify_failure_learning.py
```

Both join the Sunday fleet automatically. Spec: `docs/solutions/2026-07-27-every-failure-defaults-to-the-human.md`.
