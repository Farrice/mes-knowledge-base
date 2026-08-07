---
name: final-bundle-hash-is-not-runtime-provenance
problem_signature: "A source-to-skill behavior verifier can hash every final artifact yet still falsely pass self-attested acceptance, hidden reads, post-hoc label mapping, empty intermediates, or fabricated method deltas."
domain: system
tags: [source-to-skill, behavior-proof, provenance, false-pass, verifier]
date: 2026-08-02
status: active
session: "019fc3b4-b911-7550-b84b-dd0a7943f329"
---

## Problem

A detached behavior fixture had exact file inventory, SHA-256 hashes, a blind-label commitment, score arithmetic, and a post-run receipt. Independent adversarial review still found several ways to manufacture a passing bundle: copy the expected acceptance status into the receipt, hash empty intermediate files, declare method reads that never happened, select labels after scoring, or cite arbitrary before/after text as a source-owned mechanic.

## Root Cause

The verifier conflated three different proof jobs. A hash proves byte integrity; structured checks prove some content constraints; neither proves chronology, actual reads, fresh context, model parity, complete attempt history, evaluator quality, method causality, embodiment, or market effect. Self-authored boolean attestations filled those gaps while looking machine-verified.

## Approach That Worked

1. Freeze the semantic contract before generation: exact acceptance route and decision markers, forbidden behavior, machine-readable opening evidence maps, non-empty intermediate headings, same-replicate audit directives, allowlisted Kyle-observed source rows, exact evaluator line citations, and fail-closed schemas.
2. Add an explicit provenance grade. `RUNTIME_OBSERVED` is the only registration-eligible grade. `ORCHESTRATOR_ATTESTED` and `OPERATOR_ATTESTED` may retain diagnostic fixture evidence, but they cannot unlock routes. Report utility, method influence, embodiment, and market proof as separate claims.

## Dead Ends

- Hashing an acceptance Markdown file without parsing its decision.
- Trusting receipt fields named `observed`, `pass`, `cold_start`, or `read_paths` as if their labels were runtime evidence.
- Using a salted commitment stored only in the final bundle as proof of temporal order.
- Letting any existing source row and any two excerpts count as a visible mechanic.
- Spending a large generation wave after learning the current worker surface cannot produce the provenance grade required by the approved registration policy.

## Verification

- `verify_relaynote_fixture.py`: PASS, 25 immutable files including manifest.
- `test_verify_behavior_run.py`: three adversarial test families pass, including unrelated-Markdown self-attestation rejection and output truth/qualifier mutations.
- `verify_skill_structure.py`: PASS, eight workflows, eight prompts, zero public routes.
- `skill_auditor.py check --skill kyle-milligan-copy-chief`: 0/7 failures.
- Formal behavior generation was intentionally not run; the current desktop worker runtime is capped at registration-ineligible `ORCHESTRATOR_ATTESTED` provenance.

## Weaker-Model Trap

A weaker model will treat more hashes and more receipt fields as stronger proof. Ask what each field is independently derived from. If the answer is “the same actor wrote both the claim and the receipt,” it is an attestation, not observation. Never convert a diagnostic pass into route promotion, embodiment, or market proof.

## Pointers

- `skills/kyle-milligan-copy-chief/tests/verify_behavior_run.py`
- `skills/kyle-milligan-copy-chief/tests/test_verify_behavior_run.py`
- `skills/kyle-milligan-copy-chief/tests/fixtures/relaynote/acceptance-contracts.json`
- `skills/kyle-milligan-copy-chief/tests/fixtures/relaynote/provenance-contract.json`
- `extractions/kyle-milligan-copywriting/architecture-checkpoint.md`
