---
name: kdp-book-one-policy-safe-runtime-proof
problem_signature: "A creator-led KDP extraction can turn unsafe or unverified tactics into a fast AI-book workflow unless policy truth, proof axes, permission gates, and detached runtime behavior are built into the owner."
domain: system
tags: [kdp, extraction, policy, runtime-proof, evidence]
date: 2026-08-04
status: active
session: "codex/kdp-book-one-proof-system"
---

## Problem

A useful creator method said to validate demand, draft with AI, edit, package, publish, and repeat. Taken literally, that path also carried stale or unsafe shortcuts: static BSR rules, review exchanges, PDF-as-default ebook advice, vague copyright claims, and production activity treated as likely income. The existing Sean Dollwet skill had related workflows but no single first-book owner, durable state, permission boundary, or detached behavior proof.

## Root Cause

The source mixed three different kinds of truth: observed production mechanics, self-reported commercial claims, and platform-policy advice. Earlier skill surfaces preserved too much of that material as operating instruction. They did not keep local capability, production progress, marketplace events, and external permission on separate ledgers.

## Approach That Worked

1. Capture the anchor and ten companion videos with source, incentive, and uncertainty labels, then let current KDP and U.S. Copyright Office guidance override creator advice.
2. Keep Sean Dollwet as the function owner. Add a Book One conductor that composes the existing demand, blueprint, manuscript, cover, compliance, and organic workflows instead of building a duplicate KDP skill.
3. Add a local state machine with independent production, capability, market, and permission axes. Make upload permission explicit and prevent skipped transitions.
4. Turn known failure modes into adversarial fixtures: undisclosed AI, missing rights, review exchange language, PDF-only ebook input, route collisions, and premature upload readiness.
5. Require a detached fresh-context probe. Fix every gap it finds before promoting local behavior to `RUNTIME_OBSERVED`.

## Dead Ends

Structural checks alone were insufficient because the menu initially ranked the child pilot above `/kdp-engine`, and “AI slop” triggered a competing mandatory writing route. A first detached probe exposed both. The preflight command also wrote a receipt during diagnosis, so it needed a true `--dry-run` path.

Regenerating the full arsenal index inside an isolated worktree created thousands of timestamp-only changes. The durable fix is to preserve the baseline index entries and add only the two new Book One records.

## Verification

- `execution/verify_kdp_book_one_system.py --write-receipt` passes state, permission, policy, contract, routing, and detached-runtime checks.
- `execution/skill_auditor.py check --skill sean-dollwet-kdp-publishing` passes 7 of 7 checks with all 11 workflows reachable.
- `execution/renaissance_audit.py` passes all 3,773 prompt files.
- The command menu ranks `/kdp-engine` first; the workflow router marks only that owner as mandatory.
- A dry-run preflight returns `HOLD`, `NO_PERMISSION`, and no external action without writing a compliance receipt.
- The real pilot records `RUNTIME_OBSERVED` only on the capability axis. Production and market remain `NO_EVENT`; permission remains `NO_PERMISSION`.

## Weaker-Model Trap

A weaker model will summarize the videos, repeat the income claims, produce a topic list, and start drafting. It may call a structural pass “tested” or treat a finished file as sales proof. The replay guard is: route through `/kdp-engine`, read the current proof axes, require a dated market dossier and niche approval, and stop at the next unmet gate.

## Pointers

- `extractions/sean-dollwet-kdp-book-one-system/skill-system-contract.md`
- `extractions/sean-dollwet-kdp-book-one-system/behavior-proof.md`
- `extractions/sean-dollwet-kdp-book-one-system/detached-runtime-receipt.json`
- `skills/sean-dollwet-kdp-publishing/workflows/00-book-one-pilot.md`
- `execution/kdp_book_one.py`
- `execution/verify_kdp_book_one_system.py`
- `_active/publishing/kdp-book-one-pilot/00-start-here/BOOK-ONE-COCKPIT.md`
