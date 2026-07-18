# Grading-Loop Redesign — Verdict-First Finalize (Wave 2 proposal)

**Status: PROPOSAL — awaiting Farrice ratification.** Nothing here is wired yet.
**Author**: Fable conductor, 2026-07-17, after the judge armed at 35/35 `calibrated_by_human`.
**Farrice's felt hypothesis (verbatim intent, from the day-one handoff)**: "rubric machinery
predates strong models — rework, don't just enforce."

## Why the current loop can't be fixed by enforcement alone

The April rubric (v1) was built when weak outputs were common and the failure mode was
*obvious slop*. Its mechanism: the **producing model scores itself** on 4 dimensions
against static prose anchors, names an anchor for ≥8, composite = mean.

Three structural problems, all evidenced in the stores:

1. **Self-grading saturates against strong models.** 94–99% of finalizes score 8+
   (audit finding, `_active/system-audit/`). A strong model genuinely *matches the
   surface description* of the Anchor-9 worked example almost every time — the anchor
   test no longer discriminates at the top. Enforcing the current rubric harder just
   manufactures better-argued 9s. This is the same disease Wave 3 was designed against
   (A-tier 56→4 via plausible-looking passes).
2. **The dimensions carry the verdict, but Farrice's taste doesn't work that way.**
   His calibration signature (memory: `user_taste-calibration-signature.md`) is
   **bimodal PASS/FAIL with a narrow marginal band** — he docks whole points per
   dimension on failures, he doesn't average. A mean-of-3 composite smears exactly the
   signal he provides.
3. **The prose anchors are frozen; the calibrated set is alive.** The rubric's worked
   examples are April prose. Meanwhile the eval set now holds **35 human-ratified cases
   + 30 pre-scored seed candidates** (honest spread: 11 FAIL / 8 MARGINAL / 11 PASS)
   with real outputs, real verdicts, real notes. The best anchor library the system owns
   IS the eval set — and finalize never touches it.

## The redesign — five moves

### 1. Verdict-first, dimensions-second
Finalize's primary output becomes a verdict matching Farrice's actual signature:
**SHIP / MARGINAL / FAIL** (narrow marginal band by construction). The 4 dimensions
stay — but demoted to *diagnostic tags* explaining a MARGINAL/FAIL (which dimension
caused it), never averaged into a headline number. Composite survives only as telemetry.

### 2. Name the precedent, not the anchor (machine-checkable)
"Score ≥8 = name the matching anchor" becomes **"SHIP = cite the nearest calibrated
precedent by EVAL-ID."** Finalize validates deterministically: the cited EVAL-ID exists
in `eval_set_v1.jsonl`, is `calibrated_by_human`, and its expected verdict/composite is
within tolerance of the claimed one (±1.0). Can't name a real precedent → can't claim
SHIP-grade. This converts the anchor ritual (prose, unfalsifiable) into a lookup
(deterministic, blockable) — and it's what actually arms the judge on his verdicts.

### 3. Producer never grades alone
The model that produced the deliverable proposes; a **judge pass disposes**. Judge tier
per Conductor Ladder (Opus for judgment; the conductor samples). Cost discipline: judge
every client-facing deliverable and 1-in-N internal ones (start N=3); the judge prompt
carries the 2–3 nearest calibrated cases as few-shot precedents, so it inherits
Farrice's ratified taste rather than generic model taste. Disagreement producer↔judge
> 1 verdict class → auto-retry weakest section once (the existing retry rule, now
triggered by a real signal instead of self-report).

### 4. The inflation guardrail becomes structural, not statistical
`detect_grade_inflation(window=10)` stays as telemetry, but the real fix is that
inflation becomes *impossible to express*: SHIP requires a precedent citation that
tolerance-checks. A model can't argue its way to 9.0 against a FAIL-precedent
neighborhood. (Wave 1 accept criterion "re-scored last 50 finalizes show <60% at 8+"
is then measured on judge verdicts, not self-scores.)

### 5. Every felt verdict compounds the judge
The loop that makes this self-improving: each Farrice gut verdict — /jam take picks,
blind-pass calls, feedback-ratchet entries, the 30 seed reviews when he runs them —
appends a calibrated row to the eval set (append-only, provenance-carrying). The judge's
precedent library grows every week he uses the system normally. This is the ratchet the
audit said was missing: quality signal flowing INTO the machinery instead of dying in
observe logs. Downstream (already-specced Apex W1.3): FAIL/MARGINAL verdicts weight
routing down — honest verdicts finally make routing learn.

## What stays

- **Factual Grounding veto** unchanged — scored (not N/A) and <6 blocks regardless.
  It's the one dimension that was never inflated because it's evidence-based.
- Rubric v1 prose anchors remain as *onboarding documentation* for what the dimensions
  mean — they just stop being the scoring instrument.
- `chain_runner.py finalize` CLI shape stays (scores still logged) — additive flags:
  `--verdict SHIP|MARGINAL|FAIL --precedent EVAL-0XX`.

## Rollout (graduated, same doctrine as the BINDINGS flip)

| Step | What | Gate |
|---|---|---|
| R0 | Farrice ratifies/edits this doc; runs the 3×20-min seed reviews (65 total calibrated) | his nod |
| R1 | Add `--verdict/--precedent` to finalize as ADVISORY (logged, never blocks), judge pass on client-facing only | 1 week observe |
| R2 | Precedent tolerance-check becomes blocking for SHIP; trial file + revert flag, same pattern as `.agent/routing-enforce-trial.json` | 1-week trial |
| R3 | Quality→routing weight wiring (Apex W1.3) on judge verdicts | after R2 holds |

## Open questions for Farrice

1. Verdict names: SHIP / MARGINAL / FAIL, or keep PASS/FAIL language from your seed reviews?
2. Judge sampling rate for internal work: 1-in-3 (proposed) or every finalize (higher spend)?
3. Should MARGINAL block delivery (retry-once mandatory) or deliver-with-flag?
