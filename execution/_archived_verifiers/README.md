# Archived Verifiers (de-indexed, on disk)

Approved for archive 2026-07-21 (Farrice-delegated review of pending-review.md
PR-2026-07-15-V01..V09 + PR-2026-07-21-V01..V05; full reasons live in
`.agent/health/pending-review.md`). verify_fleet.py globs `execution/verify_*.py`
only, so files here never fire.

Classes: fork-residue contracts (schemes with zero git history on canon),
contracts written ahead of builds that never landed, deliberately-not-adopted
architecture (765e9db12), completed one-off missions, and a banned pattern
(.claude/agents/ enforcement).

To resurrect one: `git mv` it back to `execution/`, re-anchor its pins per
docs/solutions/2026-07-21-verifier-text-pin-triage-pattern.md, and prove exit 0.
