# Experiment Plan — Claim Receipt Comprehension and Search Observation

## Experiment 1: internal comprehension acceptance

**Hypothesis:** the five-field Claim Receipt will let an internal reviewer identify the claim, source, limit, reviewer, and update state more reliably than the constructed generic baseline.

**Unit:** one reviewer response against `before-answer-fixture.md` and `improved-answer-asset.md`.

**Questions:**

1. What exact claim is being made?
2. What source supports it?
3. What does the source not prove?
4. Who has the pen?
5. What triggers re-review?

**Pass:** all five answers are locatable in the improved asset, and at least three were not locatable in the constructed baseline.

**Falsifier:** the reviewer still cannot locate one or more required fields, or the added structure makes the answer less useful.

**Proof state:** `PREDICTED` until a dated review receipt exists.

## Experiment 2: external search observation (parked)

This experiment can begin only after a real client/site, explicit publication approval, a published URL, and a dated baseline exist.

If activated, preserve:

- exact query set and intent;
- engine/surface, model/version when exposed, locale, and session mode;
- run number and timestamp;
- answer/position/citation evidence;
- GSC/GA4 import hashes and date ranges;
- separate `PUBLISHED`, `INDEXED`, `RANKED`, `CITED`, `TRAFFIC`, `CONVERTED`, and `COLLECTED` events.

Synthetic prompts remain a designed sample, not true demand or stable rank. A citation is not traffic; traffic is not conversion; conversion is not collected revenue.

## Learning boundary

Either experiment may propose a review of a brief, score criterion, or workflow. It cannot mutate the skill automatically. Promotion requires human judgment, a Goal Packet, and regression proof.
