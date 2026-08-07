---
description: Build a complete Vander Wielen-model launch — ~1-month teaser ramp, ONE live webinar, weaponized replay, close — as a dated calendar with asset list and revenue model
tier: 1
---

# /sv-launch-system — The Four-Day Launch Architecture

Produces a **dated, executable launch plan** on the Vander Wielen model: a month-long teaser ramp into a single live webinar, a hard replay push, and a four-day cart. This is the architecture that produced $500K+ in under four days from a 50,000-person list with one full-time employee — twice in three months, on an eight-year-old product.

## Pre-Flight Gate

Load `skills/sam-vander-wielen/genius.md`. Run the **Recognition Test** on the launch concept before planning a single day:

> *Would a registrant who did not buy still feel like they got the better end of the deal?*

If the free training only makes sense as a step toward the purchase, stop. Fix the training before building the calendar.

**Hard prerequisites — refuse to plan without these:**
- A product that already exists (this model relaunches; it does not launch net-new)
- A list, or a paid path to registrations
- A price point ≥ ~$1,000 (below this the non-scalable layer fails the Two-Minute Test)
- A founder willing to be personally present in the launch week

If any are missing, say so plainly and name what to build first.

## Skill Acquisition

1. `skills/sam-vander-wielen/genius.md` — decision rubric, anti-patterns
2. `skills/sam-vander-wielen/references/source-quotes.md` — verbatim scripts
3. `skills/sam-vander-wielen/references/source-ledger.md` — what's self-reported vs. derived
4. If a client launch: their existing offer, list size, and last launch numbers

## Execution

### Step 1 — Establish the economics floor

Collect or ask for: list size, price point, prior launch revenue (if any), ad budget, team size. Build the **honest model** before the calendar:

- Registration target = ~20–25% of list (Sam: 11,500 from ~50,000)
- Assume roughly half of sales come from the *pre-existing* list, half from new registrants
- Assume a meaningful share of buyers convert on a ~6-month lag — **do not** model all revenue inside the cart window
- Model bump revenue **separately** from core revenue (Sam's $103K was excluded from the $500K)

State every assumption as an assumption. Never present modeled numbers as forecasts.

### Step 2 — Design the newness angle (not a new product)

The product does not change. Answer: **what changed about the packaging?** Options that have worked: re-shot the course, re-bundled the modules, added a module addressing a live market anxiety (Sam added AI and ADA-compliance trainings), new bonus, new delivery format.

Then reverse-engineer the marketing angle *from* that change — the way Sam turned a studio re-shoot into a tangible buyer benefit. **Chronicle the making of the change as the pre-launch content.**

### Step 3 — Build the ~1-month teaser ramp

Produce a dated calendar working backward from webinar day. The ramp carries:
- Weekly newsletter beats teasing that something is coming (never a hard sell)
- The behind-the-scenes chronicle from Step 2
- The exclusivity/urgency newsletter play (`/sv-newsletter-magnet`)
- Registration ads going live (~2–3 weeks out)
- Organic content with pause-and-redo CTAs captured in one batch session

### Step 4 — Set the single live webinar

One. Not three. *"This is it. Sign up or don't."* Assign the date, the run-of-show slot, and the live-only bonus that the replay will not carry.

Hand the internal structure to `/sv-webinar-script`.

### Step 5 — Wire the show-up engine

Registration tag → question email → personal video loop. Full build in `/sv-showup-engine`. Schedule the founder's video hours explicitly on the calendar — this is a real time cost (583 videos × ~2 min ≈ 19 hours) and it must be visible in the plan, not assumed.

### Step 6 — Plan the replay push

Video replay **and** a private audio/podcast replay. Set the replay window, the tracking split, and the emails. Full build in `/sv-replay-engine`.

### Step 7 — Lay the four-day cart

Map the sequence: open → value/objection emails → close-cart day. Resends to unopens **only** on close-cart, and preferably narrowed to unopens who clicked the sales or checkout page. Checkout carries the multi-bump stack (`/sv-order-bump-stack`).

### Step 8 — Schedule the non-scalable layer and the day-after

Batch the handwritten notes. Then apply the rule: **the day the promo ends, the very next day turns back to newsletter growth.** Put that on the calendar as a real workday, not an aspiration.

## Content Type Adaptations

| Context | Adjustment |
|---|---|
| **Net-new product** | This model does not apply. Route to validation first (`/pat-flynn-validate-with-one-person`), relaunch on this model later. |
| **Service business** | Keep ramp + webinar + personal video; drop the 4-day cart and bumps. The webinar sells a call, not a checkout. |
| **Sub-$1,000 product** | Drop or heavily batch the non-scalable layer. Keep the ramp, webinar, replay, and bumps. |
| **No list** | Ramp becomes 8–12 weeks and is mostly paid + organic list-building. Do not compress. |
| **Client launch** | Every number in the model is labeled as an assumption with its source. Never present Sam's figures as the client's projection. |

## Output Schema

```
LAUNCH PLAN — [Product] — [Launch date]

## Economics Model (ASSUMPTIONS, not forecasts)
| Input | Value | Source |
| Registration target | | |
| Core revenue range | | |
| Bump revenue (modeled separately) | | |
| Ad budget + expected CAC | | |
| Lagged-conversion note | | |

## The Newness Angle
What changed in the packaging: [ ]
The marketing angle derived from it: [ ]
Pre-launch chronicle beats: [ ]

## Ramp Calendar (dated, working back from webinar day)
| Date | Channel | Asset | Owner | Status |

## Webinar Day
Date/time · live-only bonus · run-of-show pointer (/sv-webinar-script)

## Show-Up Engine
Trigger · question email · video loop · founder hours blocked: [N hrs]

## Replay Plan
Video window · audio/podcast replay · tracking split · emails

## Cart Sequence (4 days)
| Day | Emails | Angle | Resend rule |

## Non-Scalable Layer
Acts · volume · batch schedule · flywheel hook (/sv-unscalable-layer)

## Day-After
Newsletter-growth restart plan

## Risks & Unknowns
[named honestly]
```

## Quality Gate

Reject and rebuild if:
- The plan schedules more than one live webinar "to cover time zones" (anti-pattern: Sam cut three to one deliberately)
- The free training does not stand alone (fails the Recognition Test)
- Modeled numbers are presented as forecasts, or Sam's figures are transplanted as the client's projection
- Founder video hours are assumed rather than blocked on the calendar
- Resend-to-unopens appears anywhere except close-cart
- The plan requires a new product to justify the launch
- The non-scalable layer is recommended below the Two-Minute Test threshold without a stated exception

**Execution prompt**: `references/prompts-v2/launch-architecture.md`
