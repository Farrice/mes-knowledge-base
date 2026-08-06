---
description: Audit an existing or planned launch against the Vander Wielen system and her eight self-named mistakes — a scored diagnostic that names the single highest-leverage fix
tier: 3
stacks_with: /offer-redteam, /jh-show-rate-diagnostics, /sv-launch-system
---

# /sv-launch-teardown — The Launch Diagnostic

Produces a **scored teardown** of a launch — planned, running, or post-mortem — against the twelve Vander Wielen mechanics and her eight self-named mistakes, ending in **one** highest-leverage fix.

This is diagnostic, not generative. It tells you what's broken and what to fix first.

## Pre-Flight Gate

Load `genius.md`. Establish scope before scoring:
- Is this a **pre-launch plan**, a **live launch**, or a **post-mortem**?
- What numbers exist? (Score what's measurable; mark the rest "not evidenced" rather than guessing.)

**Order of operations if stacking**: run `/offer-redteam` first — a broken offer produces launch symptoms that no launch mechanic fixes. Run `/jh-show-rate-diagnostics` first if the presenting problem is specifically attendance.

## Skill Acquisition

1. `skills/sam-vander-wielen/genius.md` — the Decision Rubric and anti-patterns
2. `skills/sam-vander-wielen/references/source-quotes.md`
3. `skills/sam-vander-wielen/references/source-ledger.md` — **Sam's numbers are her results, never the audit's benchmark**
4. The launch materials: emails, webinar recording/deck, registration page, checkout, ad creative

## Execution

### Step 1 — Score the Decision Rubric

Place the launch's *selling posture* on the named ladder:

| Level | Name | Marker |
|---|---|---|
| 1 | Pressure | Timers doing the work; nobody turned away |
| 2 | Signposted | Pitch pre-announced; everyone welcome |
| 3 | Granted | Consent asked and given; teaching stands alone |
| 4 | Narrowed | Consent + disqualifier with a real cost |
| 5 | Relaxed Confidence | Narrowed + visible patience |

### Step 2 — Run the Recognition Test

> *Would a registrant who did not buy still feel they got the better end of the deal?*

Answer with evidence from the actual assets, not intent.

### Step 3 — Audit the twelve mechanics

| # | Mechanic | Present? | Evidence | Gap |
|---|---|---|---|---|
| 1 | ~1-month teaser ramp | | | |
| 2 | Newness from packaging, not new product | | | |
| 3 | Consent ask before teaching | | | |
| 4 | Disqualifier with a self-costing reason | | | |
| 5 | Teaching stands alone | | | |
| 6 | Gap-naming close | | | |
| 7 | Show-up engine (personal contact) | | | |
| 8 | ONE live session | | | |
| 9 | Replay pushed, incl. audio format | | | |
| 10 | Multi-bump checkout | | | |
| 11 | Non-scalable layer with flywheel hooks | | | |
| 12 | Day-after growth restart | | | |

### Step 4 — Check the anti-patterns

| Anti-pattern | Present? |
|---|---|
| Resend-to-unopens outside close-cart | |
| Farm given away in subject lines | |
| Boosting called advertising | |
| Untested ad creative | |
| Going dark mid-promo | |
| New product built to justify the launch | |
| Anti-AI positioning with no AI-positive integration | |
| Multiple lives "for time zones" | |

### Step 5 — Check her eight named mistakes

These are structural, not launch-week issues. Flag any present:

1. Business named after the founder (sellability, founder-dependence)
2. No time limit on support/access
3. Signature phrase or asset not legally protected
4. No podcast / no owned audio channel
5. Capital sat on too long — working funnel, unfunded
6. **Refusing to scale ad spend that demonstrably works** (Sam's live, unresolved one)
7. No upsell despite obvious demand
8. Hired too fast, fired too slow

### Step 6 — Name ONE fix

Rank gaps by revenue impact × implementation cost. **Output exactly one primary fix**, with the next two listed as secondary.

Sam's ranking heuristic, from her own numbers: show-up mechanics and the close move the most money; the bump stack is the cheapest large lift (~25% for assembly work); the ramp is the longest lead time.

### Step 7 — Honest benchmarking

Sam's figures (60% attach, 23% of list registering, ~21× ROAS) are **her results on her list with her product.** Use them as existence proof — "this is achievable" — never as the audited launch's target. Any comparison must say so in the output.

## Content Type Adaptations

| Context | Adjustment |
|---|---|
| **Pre-launch plan** | Score design intent; mark all outcome rows "not yet evidenced" |
| **Post-mortem** | Lead with the numbers; mechanics explain them |
| **Service business** | Drop bumps and cart mechanics; weight show-up and close |
| **Client audit** | Every Sam figure explicitly labeled as hers; no implied projection |
| **First-ever launch** | Score generously on structure, harshly on the Recognition Test — that's the one that predicts everything else |

## Output Schema

```
LAUNCH TEARDOWN — [Launch] — [pre / live / post-mortem]

## Scope & Evidence
What was reviewed: [ ]
What could not be evidenced: [ ]

## Posture Score
Decision Rubric: [1–5] — [named level]
Evidence:
Recognition Test: PASS/FAIL — evidence:

## Mechanics Audit
[12-row table with evidence and gap]
Present: [n]/12

## Anti-Patterns
[8-row table]
Triggered: [n]/8

## Structural Mistakes
[8-row check]

## THE ONE FIX
Fix: [ ]
Why this first: [revenue impact × cost reasoning]
How to implement: [workflow pointer]
Secondary: 1. [ ]  2. [ ]

## Benchmarking Note
Sam's figures cited: [ ] — these are HER results, not this launch's target.
```

## Quality Gate

Reject and rebuild if:
- More than one primary fix is named (a teardown that returns twelve fixes returns none)
- Sam's numbers are used as the audited launch's benchmark or projection
- Rows are scored on intent rather than evidence from actual assets
- Unevidenced rows are guessed instead of marked
- The teardown runs on a launch whose *offer* is the actual problem — route to `/offer-redteam` first
- The Recognition Test is skipped

**Execution prompt**: `references/prompts-v2/launch-teardown.md`
