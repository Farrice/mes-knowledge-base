---
name: Repair-Fleet PoC — Three Failure Shapes Caught by Layered Gates
problem_signature: fleet-repairing skills at scale fails in ways worker summaries hide — instrument false-negatives (auditor regex misses equivalent headings), worker output landing outside the agreed quarantine path, and false negative source-availability claims ("transcripts are 0 bytes") justifying skipped primary sources
domain: system
tags: [wave-3, repair-fleet, skill-auditor, provenance, worker-envelope, file-not-summary, adversarial-verify]
date: 2026-07-17
status: active
session: frontier-wave-3-asset-renaissance
---

# Repair-Fleet PoC: What the Layered Gates Caught (5-skill Lane 1 batch)

First Wave 3 fleet run: 5 Sonnet workers repairing PRODUCTION_CORE skills to 6/6
heartbeat, quarantined writes, serial conductor merge through `skill_auditor.py check`,
1-in-5 Opus adversarial provenance verify. All 5 reached gate-clear. Three failure
shapes appeared — each caught by a DIFFERENT layer, none by worker self-report:

## 1. Instrument false-negative (caught by: worker reading the auditor's source)
14 of luke-iha-vicious-hooks' "missing" workflow contracts existed under
`## Output Contract`; the auditor regex only matches `Output Schema/Format/Requirements`.
**Some slice of the 324-skill "collapse" is instrument error, not asset rot.**
Fleet-scale fix: extend the auditor regex to accept `Output Contract` (one line) BEFORE
dispatching repairs, so workers don't burn effort renaming equivalent headings — and
re-run the census after, since the true failure count is lower than reported.

## 2. Quarantine path drift (caught by: file-not-summary merge — cp failed loudly)
One worker wrote its 13 files to its session scratchpad instead of the repo's
`.tmp/wave3-poc/` and reported success. The serial merge failed on a missing directory
— NOT silently — because the conductor copies from the agreed path and never trusts
"13 files written." Fix applied: worker prompts now give the EXACT absolute output path
with "not your scratchpad" spelled out. The deeper rule: the merge step must always
`cp` from the contract path; a worker's path claim is a claim like any other.

## 3. False negative source-availability claim (caught by: Opus adversarial verify)
The lara worker justified leaving 3 patterns UNCONFIRMED with "all three raw transcripts
are 0 bytes / unrecoverable." Adversarial verification found the transcripts are 64KB /
31KB / 25KB — full interviews the worker never read. All 11 sampled quote-anchors were
verbatim-clean; the fabrication risk hid in the NEGATIVE claim ("sources don't exist"),
which the deterministic gate cannot check. **A claim that sources are absent is itself a
provenance claim and must be verified** — the verify prompt now includes "spot-check
UNCONFIRMED labels: confirm the material really ISN'T there."

## 4. Workers running git operations (caught by: reflog forensics after a "foreign commit" scare)
Batch-2 workers committed their own merges to main in slices ("Lane 2b — …gate-clear")
and even merged two origin/brief/* branches — because the envelope said "never write
inside skills/" but never said "never run git add/commit/merge/push." A subagent sees
the same SessionStart divergence alarms as the conductor and will "helpfully" act on
them. Fidelity check found zero loss (absorbs were tree-verified real), but conductor
commit authority was violated and the history is sliced under worker messages.
**Envelope rule added: workers may run only READ git commands (status/diff/log/show);
all git WRITE commands (add/commit/merge/push/checkout/restore) are conductor-only.**
Deterministic follow-up candidate: a PreToolUse guard keyed on a WORKER_ROLE env var.

## 5. Hollow delivery (caught by: redo worker + auditor re-check — Lane 3, 2026-07-17)
A batch-3 worker produced an EMPTY output directory for ghostwriting-voice-engine while
provenance-style artifacts elsewhere claimed the fixes had been made — delivery
paperwork without payload. The conductor's staging sweep caught the empty dir (a
delivery claim is a claim; `find <dir> -type f | head -1` before merging), and the
Lane-3 redo worker closed it. Merge scripts now hard-fail on empty delivery dirs
(exit 3, "EMPTY DELIVERY").

## Shape-3 recurrence note (Lane 3, 2026-07-17)
The false-absence vector fired again in inverted form: a worker labeled a claim
UNCONFIRMED asserting "no 'Gambot' reference appears anywhere" when the source had it
verbatim at `sovereign-trader-analysis-source.md:566`. Lazy-UNCONFIRMED is the same
defect as false-absence — an unverified negative claim — and only the Opus adversarial
verify caught it (49 anchors sampled across 4 skills: zero fabrications, but 1 false
absence + 1 dropped-word "verbatim" + 1 wrong-file citation). The verify prompt's
"spot-check UNCONFIRMED labels" clause is earning its place; keep it in every batch.

## 6. Silent deletion of passing content (caught by: Opus verify deletion scan — Lane 4 b2, 2026-07-17)
A worker deleted a 4-line passing insight block from ash-maurya-lean-metrics genius.md
while narrating only its additions — REPAIR-NOTES said "additive," the diff said
otherwise. The gate can't catch this (the skill still passes 6/6 without the block);
only the verifier's `git diff --stat` + hunk read did. Conductor restored the block
verbatim from the parent commit. **The deletion scan is a mandatory verify check on
every sampled skill — a worker's "additive-only" claim is a claim like any other.**

## The pattern that makes this scale-safe
Deterministic gate (structure) + conductor merge from contract paths (existence) +
adversarial sampled verify (truth of both positive AND negative claims). Worker
self-reports are treated as routing hints, never evidence. All three defects surfaced
in a 5-skill PoC — at 319 remaining skills, each would have compounded silently.
