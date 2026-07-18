---
description: "Phase 3 of a Supercomputer mission — deterministic anchor_verify.py audit that every anchor with a ref_for obligation actually propagated into its dependent deliverables before Finalize."
---

# Anchor Propagation Verification — The Phase 3 Gate

Dispatches `skills/supercomputer/references/prompts-v2/anchor-propagation-verification.md` (the
engine — read it first, this file is the workflow contract wrapping it). This is the audit that
separates a genuine Supercomputer mission from "ChatGPT + image gen plugged in"
(`skills/supercomputer/genius.md`) — a deterministic, tool-driven check, never a subjective read
of whether the deliverables "feel" coherent.

## Invocation

Runs automatically before every Phase 4 (Finalize) in a Supercomputer mission that registered one
or more anchors with a non-empty `ref_for` field. Never skipped, never merged into the finalize
step itself.

## Stages

1. **Pull the anchor list** — `python3 execution/anchor_memory.py describe <slug>`.
2. **Isolate obligations** — only anchors with a non-empty `ref_for` carry a verification
   requirement; an anchor nothing downstream references yet is informational, not a gate.
3. **Run the verifier per anchor** against every dependent deliverable in its `ref_for` list:
   `python3 execution/anchor_verify.py check --anchor <path> --targets <paths>` — add
   `--terms "a,b,c"` for load-bearing terms auto-extraction would miss.
4. **Binary/image anchors** — verify the *text* deliverable that describes or briefs the image,
   not the pixel data itself.
5. **Gate at 7/10.** Any target scoring below 7: inject the anchor path + the named missing terms
   verbatim into a regeneration prompt, regenerate, re-run the check before moving on.
6. **Block Phase 4** until every obligated anchor clears ≥7 against all its listed targets, on
   first pass or after retry.

## Output Schema

One verification block per anchor with a `ref_for` obligation: anchor path/type, the dependent
targets checked, the numeric score (1-10) per target, the specific missing terms per target (or
"none"), pass/fail against the ≥7 gate, and — for any failure — what was injected on retry and the
re-verified score. The deliverable closes with exactly one summary line naming overall clearance
to proceed to Finalize (yes/no, and if no, which anchor+target is still blocking). A block that
reports a score without a corresponding `anchor_verify.py check` invocation, or that omits an
anchor with a live `ref_for` obligation, has not produced this deliverable.

## Quality Gate

- Every anchor with a non-empty `ref_for` was checked — none skipped silently, none merged into a
  single "looks fine" judgment call.
- Every reported score traces to an actual `anchor_verify.py check` run, never an
  estimated/assumed number.
- Every score below 7 went through the full retry protocol (explicit term injection → regenerate
  → re-verify) before being marked resolved — no score was rounded up or waived.
- Binary/image anchors were verified against their describing text deliverable, never against the
  image file itself.
- The final summary line correctly gates Phase 4 — never "CLEARED" while any obligated anchor is
  still below 7.
