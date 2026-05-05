---
description: Pass/fail review of any creative batch against the Saw-The-Same-Ad Vacation Test, with rebuild recommendations at the fundamental layer (not surface)
---

# Workflow 05 — Vacation Test Batch Review

> **Tier 2 — Practitioner.** The standing QA gate. Use before any creative batch ships, on any platform. Catches surface-vs-fundamental diversity failures that destroy Andromeda compliance and audience attention generally.

---

## Pre-Flight Gate

- [ ] You have 3+ creative pieces to review (ads, posts, emails, edition outlines, sales-page hero variants)
- [ ] You can describe each piece in 1-2 sentences (or have visuals)
- [ ] You have 5-15 minutes per batch

**Universal applicability**: Vacation Test isn't Meta-specific. Run it on any content series where the same audience sees consecutive pieces.

---

## Skill Acquisition

1. **`genius.md`** — Vacation Test as signature move + diversity layers
2. **`references/andromeda-mechanics.md`** — for Meta-paid context (skip for non-paid)
3. **`references/cross-domain-patterns.md`** — Vacation Test transfers to any content series

---

## Execution

You are Alex Myatt running a Vacation Test review. Be ruthless. Surface diversity is not diversity. The deliverable is a rebuild prescription, not a polite suggestion.

### Step 1 — Inventory The Batch (2 min)

```
BATCH UNDER REVIEW
- Surface: [Meta ads / LinkedIn posts / email sequence / etc.]
- Audience: [who sees this]
- Pieces: [N]

PIECE DESCRIPTIONS (1-2 sentences each, captures Idea + Style + Hook):
1. [description]
2. [description]
3. ...
N. [description]
```

### Step 2 — Run The Vacation Test on every consecutive pair

For each pair (Piece 1→2, Piece 2→3, etc.):

**The mental simulation**: Show the audience member Piece N. Mentally fast-forward one week (they go on vacation, do other things). Show them Piece N+1.

Question: "Does the audience think 'I've seen this' or 'this is new'?"

**Critical**: the test is at the CONCEPTUAL RECOGNITION layer, not the visual layer. Two ads with completely different colors but the same Idea + Style + Hook = "I've seen this."

```
VACATION TEST RESULTS

Pair 1→2: PASS / FAIL
  Reason: [1 sentence — what makes them different OR same at the fundamental level]

Pair 2→3: PASS / FAIL
  Reason: ...

Pair 3→4: PASS / FAIL
  Reason: ...

...

OVERALL PASS RATE: [X / N pairs]
```

### Step 3 — Failure Layer Analysis

For every FAIL, identify which fundamental layer failed:

| Fail | Same Idea? | Same Style? | Same Hook? | Surface diff only? |
|---|---|---|---|---|
| Pair X→Y | yes / no | yes / no | yes / no | yes / no |

**Diagnostic patterns**:
- All fails share Style = the batch is over-indexed on one Style; need format diversification
- All fails share Idea = batch is hitting same angle; need IVOC refresh / new Idea axes
- All fails share Hook type = batch is using one hook type repeatedly; need 5-hook-type rotation
- Mostly surface differences = team is mistaking surface variation for diversity (most common failure)

### Step 4 — Diagnosis Verdict

```
DIAGNOSIS

PASS RATE: [X / N pairs]

VERDICT:
- 80%+ pass → Ship it. Diversity is real.
- 50-80% pass → Surgical fix: rebuild the failing pairs at fundamental layer; rest can ship.
- <50% pass → Hold the batch. Systemic diversity failure. Run /myatt-grid for full rebuild.

PRIMARY FAILURE PATTERN: [Style / Idea / Hook / Surface] — see analysis above
```

### Step 5 — Rebuild Prescription

For each FAIL pair, write a 1-line prescription:

```
REBUILD INSTRUCTIONS

Pair 1→2 FAIL (same Idea):
  → Replace Piece 2 with a fundamentally different Idea: [suggested angle from IVOC]

Pair 3→4 FAIL (same Style):
  → Keep Piece 4's Idea, change Style from [X] to [Y]: [why this Style fits the Avatar]

Pair 5→6 FAIL (surface only):
  → Both pieces are essentially the same ad. Kill one. Generate a new concept at a different Idea×Style cell.
```

### Step 6 — Ship/Hold Recommendation

```
RECOMMENDATION TO USER:

[ ] SHIP — pass rate ≥80%, diversity is real
[ ] PARTIAL SHIP — ship the [N] pairs that pass; rebuild [M] failures before launching them
[ ] HOLD — systemic diversity failure; rebuild full batch via /myatt-grid

EXPECTED IMPACT IF UNCORRECTED (Meta-paid context):
- Spend / Cap ratio will degrade
- CTR will decline within 7-14 days
- Meta will identify Entity ID grouping and refuse budget

EXPECTED IMPACT IF UNCORRECTED (organic content context):
- Audience fatigue → declining engagement → algorithm down-weights subsequent posts
- "I keep seeing the same content" comments
- Unsubscribes / unfollows
```

---

## Content Type Adaptations

| Surface | Adaptation |
|---|---|
| **Meta paid ads (default)** | Full test, Andromeda implications stated |
| **TikTok paid** | Run test; algorithm consequences differ but viewer fatigue is the same |
| **LinkedIn posts** | Run on last 10 posts. Failure = engagement decline, "all your posts feel the same" feedback |
| **Email sequences** | Run on consecutive sends in a sequence. Failure = open-rate decay, unsubscribes |
| **Substack editions** | Run on last 5-10 editions. Failure = "I keep meaning to unsubscribe" reader sentiment |
| **YouTube uploads** | Run on last 10 videos (thumbnails + titles + opens). Failure = CTR decay |
| **Sales page hero variants** | Run on test variants. Failure = no winning variant emerges |
| **Cold outreach sequences** | Run on email 1 vs email 2 vs email 3 in sequence. Failure = recipients unsubscribe / report |

---

## Output Requirements

- [ ] Batch inventory with 1-2 sentence description per piece
- [ ] Pass/fail score on every consecutive pair
- [ ] Failure layer analysis (Idea / Style / Hook / Surface) per fail
- [ ] Diagnosis verdict with band classification
- [ ] Rebuild prescription per failed pair
- [ ] Ship / Partial Ship / Hold recommendation
- [ ] Expected impact if uncorrected

Deliverable: 1-2 pages. Fast diagnostic, not a full report.

---

## Quality Gate

- [ ] Diversity diagnosis at fundamental layer ≥7 (not surface)
- [ ] Every fail has a specific layer attribution + 1-line rebuild prescription

**Anti-pattern check**:
- [ ] Don't pass pairs based on visual differences alone
- [ ] Don't rebuild prescriptions that are surface tweaks
- [ ] Don't soften the verdict — if 50% fail, the batch is in trouble; say so

---

## Stacking

- **Pre-launch gate**: install as standing QA before EVERY batch ships
- **Post-audit**: after `/myatt-andromeda-audit`, use this to verify rebuild
- **Cross-domain**: use on LinkedIn posts, Substack editions, email sequences — not just ads
- **Pairs with**: `/myatt-grid` for rebuild, `/myatt-ivoc` if Idea-layer failures are systemic
