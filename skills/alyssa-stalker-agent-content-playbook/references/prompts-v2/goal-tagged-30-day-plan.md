---
name: "Alyssa Stalker — Goal-Tagged 30-Day Plan"
source_prompt: born-v2
skill: alyssa-stalker-agent-content-playbook
standard: structure-pure-v2
forged: born-v2
refactored: 2026-09-02
fidelity: high
---

## Role & Activation

You are building a month of agent content the way Coffee & Contracts structures it under Alyssa Stalker: "mostly local content, listing content because you got to show what it is that you sell, and then a little bit of authority building content and that's the smallest percentage." Goal decides ratio — grow → local ("the fastest way to attract new followers"); convert → listing; nurture → authority, about monthly. Every slot carries one message and a pre-declared expectation, because "every post has a different goal... you're not going to get a ton of likes on authority-building nurture style content." One experiment, held for data; never five at once.

## Input Required

```text
[AGENT: name, market, register notes]
[PRIMARY GOAL: grow / convert / nurture]
[CAPACITY: posts per week the agent can actually sustain]
[PERSON: one line from the One-Person Niche Card]
[OUTLIER HYPOTHESIS, optional: from the Outlier Audit Card]
[LAST 20 POSTS BY TAG, optional: local / listing / authority counts]
[ACTIVE LISTINGS / UPCOMING CLOSINGS, optional]
```

Never prescribe daily posting when CAPACITY is three. If OUTLIER HYPOTHESIS is absent, label the experiment a guess.

## Execution Protocol

1. **Set the goal** — one primary goal.
2. **Set the ratio** — starting points: grow ≈ 60/30/10 local/listing/authority; convert ≈ 40/50/10; nurture ≈ 50/30/20. Adjust to capacity. State that percentages translate "mostly / some / smallest."
3. **Read the current grid** — count the last 20 by tag; a listing- and authority-heavy grid is the billboard; the plan inverts it.
4. **Tag every slot** — local / listing / authority, the who, one message (sayable in 20–30 seconds).
5. **Pre-declare expectations** — local: reach/follows; listing: saves/DMs; authority: fewer likes, memory.
6. **Place one experiment** — from the hypothesis, repeated across 3–4 slots; data window; pivot / double-down rule.
7. **Thread the personal lens** — one real agent signal per week, usually in stories.
8. **Lo-fi by default** — carousels, single images, create-mode text posts, phone B-roll with a text hook; production reserved for listing showcases. A/B B-roll vs carousel on local where cheap.
9. **Human checkpoint** — agent confirms capacity and voice before the plan is "ready."

## Output Contract

Markdown plan, 400–800 words. Sections: Goal + capacity + ratio; Current grid table; Calendar table (one row per slot: week, day, tag, who, one message, format, expectation, experiment flag); Experiment block; Personal-lens thread; Handoff block. Every slot tagged and expectation-labeled. Exactly one experiment.

## Output Skeleton

```markdown
# GOAL-TAGGED 30-DAY PLAN — [agent] — [month]

## Goal + capacity
- Primary goal:
- Posts per week:
- Ratio: local __% / listing __% / authority __%

## Current grid (last 20)
| Tag | Count | Note |

## Calendar
| Wk | Day | Tag | Who | One message | Format | Expectation | Experiment? |

## Experiment
- Hypothesis:
- Slots:
- Data window:
- Pivot / double-down rule:

## Personal-lens thread
Wk1: … Wk2: … Wk3: … Wk4: …

## Handoff → jen-engine Stage 2 / enrico 08 / posting queue
- Output produced: Goal-Tagged 30-Day Plan
- Next input: [slots to fill]
- Validation: every slot tagged + expectation declared [yes/no]; capacity confirmed [yes/no]
- Open risk: [experiment is a guess / capacity unconfirmed]
```

## Quality Gate

- Every slot carries tag, who, one message, expectation?
- Authority at or under ~monthly and pre-declared low-engagement?
- Exactly one experiment with a data window?
- Fits stated capacity?
- Grid moving away from billboard?
- No just-sold/just-listed filler, no five simultaneous experiments?

## Creative Latitude

The calendar is a floor; the one-message column is where the month gets a personality. Let the local slots argue with each other — one insider tip, one contrarian take, one comfort post — so the grid reads like a person with a point of view, not a content service. The personal-lens thread should be specific enough to be slightly risky (the Yankees bet, the book never finished), because that is what makes people "feel like they get to know you."

## Deploy When

- Start of a month, after `/alyssa-stalker-outlier-audit`.
- A grid audit shows the billboard pattern.
- Before `jen-engine` Stage 2 fills its 20-video calendar.
