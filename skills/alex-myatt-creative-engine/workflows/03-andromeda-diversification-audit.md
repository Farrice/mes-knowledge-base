---
description: Diagnostic of an existing ad account against Entity ID grouping risk, Vacation Test pass rate, and budget-not-spending pathology — with rebuild plan
---

# Workflow 03 — Andromeda Diversification Audit

> **Tier 1 — Foundation.** The account-rescue diagnostic. Use when budget isn't spending, CTR collapsed, client says "we run lots of ads but nothing works." Reveals the Entity ID grouping that 80% of brands have.

---

## Pre-Flight Gate

- [ ] You have access to (or screenshots of) the last 20-30 ads run on the account
- [ ] You know the account's daily budget cap AND actual daily spend (the gap is the diagnostic)
- [ ] You can see CTR, CPM, CPA trends for the last 30-60 days

**If client says "everything is fine"**: ask for the daily-spend / budget-cap ratio. If <70%, Andromeda is the issue regardless of what they think.

---

## Skill Acquisition

1. **`genius.md`** — Vacation Test, Volume-as-Probability, Decision Framework
2. **`references/andromeda-mechanics.md`** — full Entity ID logic + economic underpinning
3. **`references/creative-pyramid-quickref.md`** — diversity layers reference

---

## Execution

You are Alex Myatt diagnosing an Andromeda compliance failure. Direct, numbers-specific. Don't soften the diagnosis — most accounts fail this. The rebuild is the deliverable.

### Step 1 — The Spend-Gap Diagnostic (60 seconds)

```
ACCOUNT SPEND HEALTH
- Daily budget cap: $[X]
- Last 7-day average daily spend: $[Y]
- Spend / Cap ratio: [Y/X = Z%]

DIAGNOSIS:
- 90%+ → account is healthy, look elsewhere for the problem
- 70-90% → mild Andromeda signal, audit recommended
- <70% → Meta is refusing to spend the budget. Andromeda Entity ID problem is likely.
```

**Key insight**: most brands assume "low spend = Meta bug" or "raise the cap." Both wrong. Meta is making an economic decision: it has data showing your ads won't justify slot value. Almost always: Entity ID grouping.

### Step 2 — Entity ID Audit (Vacation Test on existing ads)

Lay out the last 20-30 ads. For each consecutive pair (Ad N → Ad N+1):
- "Would a viewer who saw Ad N a week ago think Ad N+1 is different or same?"
- Score: pass / fail

```
VACATION TEST AUDIT (last 20 ads, 19 consecutive pairs)
- Pair 1→2: PASS / FAIL — [1-line reason]
- Pair 2→3: PASS / FAIL — [1-line reason]
...

PASS RATE: [X / 19]
```

**Diagnosis bands**:
- 80%+ pass → account is genuinely diverse; Andromeda probably not the issue
- 50-80% pass → moderate grouping, fixable with surgical adds
- <50% pass → systemic grouping; account needs rebuild

### Step 3 — Identify the Entity Clusters

Group the existing ads by perceived Entity (similar Idea/Style/Hook):

```
ENTITY CLUSTERS (estimated)
Cluster A: [N ads share this entity — described as: "static product on white bg with X% off"]
Cluster B: [N ads share this entity — described as: "founder talking-head about benefit Y"]
Cluster C: [N ads share this entity — described as: "..."]
...

ESTIMATE: account is running [N entities] across [M ads]. Effective Volume is N, not M.
```

**Reality check**: most "we run 30 ads/month" accounts are actually running 4-6 entities × surface variants. They have a Volume problem disguised as a Diversity problem.

### Step 4 — Layer-by-Layer Failure Analysis

For each existing entity, identify WHERE the diversity failed:

| Diversity Layer | Pass / Fail | Notes |
|---|---|---|
| Idea variation | | Are entities saying fundamentally different things? |
| Style variation | | Are formats genuinely different (UGC vs founder vs versus)? |
| Hook variation | | Are first 2-3 seconds varied across hook types? |
| Surface only? | | Is "diversity" mostly color/copy-tweak/angle? |

**Common pattern**: 4-6 entities all share the same Style (e.g., all UGC) and similar Ideas, with surface tweaks creating false diversity.

### Step 5 — IVOC Sanity Check (Relevance pillar)

Pull 5-10 verbatim customer quotes from any 2 unmoderated venues for the product category. Compare to the language in current ads:

```
RELEVANCE AUDIT
- Customer says: "[verbatim quote]"
- Current ad says: "[ad copy]"
- Match: TIGHT / LOOSE / NONE

Pattern across 10 quotes: [account is using brand language vs customer language]
```

If <30% match: Relevance pillar is also failing. Account needs IVOC mining + rebrief.

### Step 6 — Rebuild Plan

```
REBUILD PRESCRIPTION

PRIORITY 1 (Week 1):
- Fix Entity ID grouping at the FUNDAMENTAL layer
- Generate [N] new entities at the Idea level (not just Style/Hook)
- Method: run /myatt-ces or /myatt-grid for full rebuild

PRIORITY 2 (Week 2):
- IVOC mining sprint to refresh Relevance
- Method: run /myatt-ivoc

PRIORITY 3 (Week 2-3):
- Pre-launch Vacation Test on every new batch
- Method: run /myatt-vacation-test as gate

EXPECTED OUTCOME:
- Spend / Cap ratio rises to 90%+ within 14 days
- CTR rises by [X-Y%] within 21 days
- CPA stabilizes within 30 days
```

### Step 7 — The Conversation With the Client

Client likely thinks the problem is:
- "Ad fatigue" → partially right but wrong mechanism
- "Need bigger budget" → wrong; budget is irrelevant if Meta won't spend
- "Bad creative" → wrong; creative is fine, diversity at the wrong layer is the issue
- "Algorithm change" → right vibe, wrong specifics

Brief the client in their language:

```
"Your creative is fine. The problem is Meta now groups similar ads and won't spend on a group it has data against. You're effectively running 4 ads, not 30 — the surface differences don't count anymore. We need to rebuild diversity at the fundamental layer (different angles of attack, not just different colors)."
```

---

## Content Type Adaptations

| Surface | Adaptation |
|---|---|
| **Meta paid (default)** | Full audit as written |
| **TikTok paid** | Different algorithm — Vacation Test still useful, Entity ID logic doesn't apply directly. Focus on Hook density failure. |
| **YouTube ads** | Audit applies; Entity ID logic applies but classifier is more permissive |
| **LinkedIn organic** | Run on last 10 posts. Failure = audience fatigue / engagement decline rather than budget pathology |
| **Email sequences** | Run on last 10 sends. Failure = open-rate decline rather than spend issue |

---

## Output Requirements

- [ ] Spend-Gap Diagnostic with band classification
- [ ] Vacation Test audit (every consecutive pair scored)
- [ ] Entity Cluster identification (real Volume vs apparent Volume)
- [ ] Layer-by-layer failure analysis
- [ ] IVOC Relevance audit (10 quotes vs current copy)
- [ ] Rebuild Prescription with priority order + expected outcomes
- [ ] Client conversation script

Deliverable: 2-4 pages. Diagnostic-grade, not strategy-grade.

---

## Quality Gate

- [ ] Andromeda compliance audit ≥7 (every layer scored, not vibed)
- [ ] Diversity diagnostic at fundamental layer ≥7 (not surface)
- [ ] Research provenance ≥7 (real IVOC for Relevance audit)

**Anti-pattern check**:
- [ ] Don't blame "ad fatigue" generically — name the specific Entity ID groupings
- [ ] Don't recommend "more ads" — recommend FUNDAMENTALLY different ads
- [ ] Don't suggest budget changes as primary fix — Meta won't spend more on a failing group

---

## Stacking

- **Downstream rebuild**: feed audit into `/myatt-ces` or `/myatt-grid` for the actual rebuild
- **Research refresh**: run `/myatt-ivoc` if Relevance pillar failed
- **Ongoing QA**: install `/myatt-vacation-test` as standing gate before any new launch
- **Client retention**: stack with `/myatt-care-square` — a good audit is also a Perception win, even if Results take 30 days
