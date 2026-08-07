# CORPUS-02: Capability Handoff Missing

## Observed Failure

After the corpus was delivered, Farrice said:

> “I didn't get a chance to read any of it. I just saw that you did something.”

The closeout reported seals, scores, fixtures, and the pending case but did not give the operator a plain explanation of what the six-domain corpus changed, what new capacity existed, or how to invoke it in everyday work.

## Violated Gate

A reusable skill system must expose a user-facing operating surface. Artifact completion is not operator adoption.

## Expected Behavior

Every completed reference corpus must provide, at its start surface:

1. a plain description of the capability gained;
2. practical use cases;
3. at least one default invocation;
4. the proof boundary and unresolved behavior;
5. a link to the full AAR.

## Smallest Owner

The corpus package owns this failure through `00-START-HERE.md`, `USER-GUIDE.md`, `AFTER-ACTION-REVIEW.md`, and `verify_corpus.py`.

## Preservation Lock

- Do not edit any V1 or V2 reference asset.
- Do not change the router, its three decisions, its six production routes, or its one-owner rule.
- Do not claim human A-tier recognition or market proof.

## Repair

- Added a plain-language user guide.
- Added a complete AAR.
- Added both artifacts to the start surface.
- Made the final corpus verifier require the guide, AAR, and this fixture.

## Status

**REPAIRED.** The executable verifier now fails if the user-facing capability handoff disappears.
