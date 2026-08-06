---
description: Design the deliberate 5% — which non-scalable acts, at what volume, batched how, each carrying a flywheel hook that converts the gesture into followers, referrals, and voice-of-customer data
tier: 1
---

# /sv-unscalable-layer — Engineering the 5%

Produces a **designed non-scalable layer**: the specific human acts, their volume, their batch schedule, their per-unit time cost, and the flywheel hook built into each one.

The governing insight: Sam automates 95% of the launch **specifically so the remaining 5% is affordable.** *"There was nothing else for me to do because my launches are such well-oiled machines. My job is done."* One launch: **583 personalized videos + 329 handwritten notes.**

The frame Nathan supplies (crediting Will Guidara's *unreasonable hospitality*): be militant about 95% of the business **so you can be completely frivolous with the last 5%.**

## Pre-Flight Gate

Load `genius.md`. Answer three questions honestly before designing anything:

1. **Is the machine actually built?** If the founder's launch week is already full of operational work, the 5% will burn them out. *Automate first.* Say this plainly rather than designing acts they can't perform.
2. **Two-Minute Test.** State per-unit time against per-unit revenue out loud. If it sounds absurd, batch down or cut.
3. **Is the founder the trust asset?** If buyers don't care who they are, personal contact is noise.

Any "no" → report the prerequisite instead of producing a plan.

## Skill Acquisition

1. `skills/sam-vander-wielen/genius.md`
2. `skills/sam-vander-wielen/references/source-quotes.md`
3. `skills/sam-vander-wielen/references/cross-domain-patterns.md` — **"Where the Two-Minute Test fails"**
4. The user's price point, expected buyer volume, and current automation state

## Execution

### Step 1 — Audit what is NOT yet automated

List every launch-week task. Mark each: automated / delegated / founder-only. The founder-only list should reduce to three kinds of work: **create content, human contact, show up live.** Everything else is a prerequisite fix, not a 5% act.

### Step 2 — Choose the acts

Select from proven forms; each must clear the Two-Minute Test.

| Act | Sam's volume | Placement | Per-unit cost |
|---|---|---|---|
| Personal video to registrants | 583 | Pre-event (drives show-up) | ~2 min |
| Handwritten thank-you note | 329 | Post-purchase | ~2–3 min |
| Personal video on emotional replies | ongoing | Whenever a reader writes something real | ~2 min |
| Small gifts on life events | ad hoc | When the team hears something | delegated |
| Founder-answered support | 5,500 members, M/W/F | Ongoing, 48-hr promise | ~1 hr/session |

Sam's placement logic: **pre-purchase contact drives attendance; post-purchase contact drives the flywheel.** Do both or pick deliberately, but know which job each act does.

### Step 3 — Build the flywheel hook into each act

**This is the step everyone skips.** A thank-you note that only says thank you is a courtesy. Sam's note ends with a request that does work:

- **Ask them to reach out on Instagram** → converts buyer to follower
- **Give them a reason to actually do it** → a question they want to answer:
  - *"What's a book you've read recently that you love that you'd recommend?"*
  - *"If you were a pasta noodle shape, what shape would you be?"*

The result: *"It's so funny to me how many customers never followed us on Instagram and now they're following us"* — and from there, podcast episodes get shared, books get recommended, referrals start.

**For every act you design, name the hook and the destination.** Hook without destination = courtesy. Destination without hook = spam.

### Step 4 — Batch it

Sam batches everything. Nathan batches team cards on flights, ten at a time, a month ahead, with the team supplying the list. Design:
- Batch size
- Cadence (per-launch, monthly, weekly)
- Who supplies the input list
- Where the physical materials live

### Step 5 — Compute and block the real cost

Total per-unit time × expected volume = hours. **Put the hours on the calendar.** Unblocked hours are how this becomes resentment.

### Step 6 — Set the boundary

Sam's disqualification is credible because her workload enforces it. Define what the founder will *not* do, so the 5% stays sustainable: her rule is that lifetime support does not extend to *"a contract for their dog walker's cousin"* — she names the line and holds it.

## Content Type Adaptations

| Context | Adjustment |
|---|---|
| **Sub-$1,000 product** | Cut personal video to repliers-only; keep the note for buyers only. Or skip entirely and say why. |
| **High-volume / low-touch** | Segment: the 5% goes to the top decile of buyers, stated openly as such |
| **Team-delivered brand** | The act must come from a named human the buyer will actually interact with |
| **Real estate / regulated** | Note-and-question flywheel ports cleanly; route any copy through compliance |
| **B2B** | Swap the whimsical question for a professional one; the mechanic is identical |
| **Physical product / DTC** | Notes in the box, not mailed separately; hook routes to a review or an Instagram tag |

## Output Schema

```
NON-SCALABLE LAYER — [Business] — [Launch/period]

## Prerequisite Check
Machine built? [Y/N + what's missing]
Two-Minute Test: "Two minutes for a $[X] sale is [verdict]"
Founder is trust asset? [Y/N]
VERDICT: PROCEED / FIX FIRST / SKIP + why

## Automation Audit
| Task | Status | Action |
Founder-only list after fixes: [should be ≤3 kinds of work]

## The Acts
| Act | Volume | Placement (pre/post purchase) | Job it does | Per-unit min |

## Flywheel Hooks
| Act | The hook (verbatim ask) | Destination | What it produces |

## Batch Plan
| Act | Batch size | Cadence | Input list owner | Materials |

## Time Budget
| Act | Units | Min each | Total hrs | Blocked on |
TOTAL: [ ] hours

## The Boundary
What the founder will NOT do: [ ]
How the boundary gets stated to customers: [ ]
```

## Quality Gate

Reject and rebuild if:
- The machine isn't built and the plan proceeds anyway (this is the burnout path)
- Any act lacks a flywheel hook **and** a destination
- Hours are computed but not blocked on a calendar
- The Two-Minute Test wasn't stated at the user's actual price point
- The plan assumes founder willingness that hasn't been confirmed
- The acts are performed by a brand account rather than a named human
- No boundary is defined — an unbounded 5% becomes an unbounded obligation (Sam's own lifetime-support mistake, [32:34])

**Execution prompt**: `references/prompts-v2/unscalable-layer.md`
