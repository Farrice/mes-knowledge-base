# Resonance Event #1 — Pre-Launch Command Center

*Single source of truth for the 10-week sprint to Event #1.*
*Created: 2026-05-19 · Owners: Andrea (Founder) + Farrice (Producer-in-Chief)*
*Status: Live. Updated weekly. Decisions and milestones land here, not in chat threads.*

> *Heart encounters, not head encounters. A daytime, sober dance party in Chicago for people who want to meet a partner. The mechanic is body-first: the music does the emotional labor so the people don't have to. The metric is couples, not followers.*

---

## How to read this document

The Command Center is the spine of pre-launch. Every other file in this folder references back to it. Every decision Andrea or Farrice makes between now and Event #1 lives in one of its sections. If you only have ten minutes a week with this brand, you read the Command Center on Mondays.

The structure is deliberate. Section 1 names the parameters that are locked versus the parameters Andrea is still deciding. Section 2 names the team, which is two people and a deployed agent stack, not the six-person roster a launch like this would normally need. Sections 3 through 6 are the work itself: workstreams, math, network mining, calendar. Sections 7 through 9 are the failure modes: this week's punch list, role doctrine, decision gates, risks. Section 10 indexes everything that's been shipped and everything queued.

Read top-to-bottom on a first pass. Skim the section opener and the table on every subsequent pass. The tables don't change much week-to-week. The framing is what carries the work.

---

## Section 1 — Parameters (locked + pending)

This section is the contract. Locked parameters do not get re-litigated in a working session; the only way they change is if Andrea names the change in writing. Pending parameters are explicitly held open and dated. The discipline is to know at any moment which row is which, so the team isn't quietly drifting on something already settled or quietly assuming something not yet decided.

### Locked
- **Brand:** Resonance — v1.1 BOS foundation shipped 2026-05-11
- **Format:** Daytime (2pm-5pm Saturday), sober, founder-curated, ~50 attendees, no bar
- **City:** Chicago (Lines 1, 2, 3, 6 hold — see `00-foundation/05-non-negotiables.md`)
- **Team:** Andrea (Founder + MC + DJ) + Farrice (Producer-in-Chief). Volunteers + paid hires as needed for day-of.
- **Founder voice:** v1.1 Brand Bible §5 Long / Short / Micro versions — pending Andrea sign-off but treated as canonical for v1.1 work
- **Target ratio:** 30W / 20M (acceptable floor 28W/22M; hard floor 25W/16M before reducing room size)
- **Budget approach:** Reverse from break-even. See Section 4 — Andrea adjudicates at first review.
- **IG handle:** [@resonance.chicago](https://instagram.com/resonance.chicago)

### Pending decision (Week 1)
- **Event date.** Mid-to-late July 2026. Andrea confirms by 2026-05-23. Default planning assumption: **Saturday July 18 or 25, 2026**.
- **Venue.** Outreach pack delivered this session (see `01-*` files). Tier 1 → Tier 2 → Tier 3 sequence. Decision target: **by 2026-06-02** (14 days from venue outreach kickoff).
- **Ticket price.** Three scenarios in Section 4. Andrea picks one once venue cost is known.

### Pending decision (later)
- **Profile #3 male avatar lock** — Marcus + Daniel as complementary avatars (Path B). Locked by agent 2026-05-19, Andrea reviews at next session.
- **Imani Profile #2 lock** — recommended in v1.1 ICP Master, Andrea adjudicates.
- **JR availability for Event #1** — pending confirmation. Backup DJ identified if no.

---

## Section 2 — The Team-of-Agents Roster

A launch like this would normally need a six-person team: a producer, a copywriter, a designer, a social lead, an ops manager, and a venue scout. Resonance is running with two operators and a deployed agent stack instead. The choice is deliberate.

Two reasons we built it this way. The first is fidelity: Andrea's voice is the brand, and the further every artifact is from her hand, the more it loses. A small team with a skilled agent layer keeps every public-facing line within one or two reviewers of her register. The second is reversibility: an agent stack is rebuildable when something breaks; a six-person team is a payroll commitment that survives whether or not Event #1 lands. Until couple-formation is proven, we keep the headcount where the proof is the proof.

What follows is eight roles. Each is a job the launch genuinely requires. The team is Andrea, Farrice, and a backing skill or agent that does the production work under one of them. Adjudication stays human. Production scales.

### 1. Pre-Launch Strategist
**Trigger:** Weekly Monday review + ad-hoc when a decision needs to lock.
**Backing:** Main thread (Claude with full BOS context loaded) using `/brief` or direct synthesis.
**Output:** This Command Center doc, kept living. Sprint pulse updates. Decision-gate enforcement.
**Calls it:** Farrice.

### 2. Brand Voice Guardian
**Trigger:** Before any public-facing artifact ships (IG post, email, DM script, landing page copy, venue pitch, application gate copy).
**Backing:** `agents/prose-doctor/` + Voice Document v1.1 + `prose-check` skill.
**Output:** Pass/Fail with revisions. Catches: AI tells, voice drift, banned phrases, the 8 banned structural moves, register mismatch (polished vs conversational).
**Calls it:** Whoever just drafted public-facing copy. EVERY TIME. Non-negotiable.

### 3. Content Engine
**Trigger:** Weekly content production (IG: 3x posts + daily stories; email: 1-2x/week post-launch).
**Backing:** `agents/master-copywriter/` + `hook-forge` + `hook-bank` + `/ghostwrite` skill.
**Output:** Content batches (carousels, reels scripts, stories, captions, email drafts) — paired with image briefs for visuals.
**Calls it:** Farrice. Andrea reviews + edits before publish.

### 4. Lead Capture Architect
**Trigger:** Landing page build (Week 2-3). Application gate design (Week 4-5). Email flow design (Week 3-4).
**Backing:** `client-conversion` + `funnel` + `vsl-lead` + `master-copywriter`.
**Output:** Landing page copy + form copy + email sequence drafts + application questions + decline scripts.
**Calls it:** Farrice.

### 5. Male Acquisition Strategist
**Trigger:** Weeks 1-9 — male attendance gets weekly attention as the asymmetric problem.
**Backing:** This session's dispatch (icp-deep-canvasser) + `02-male-acquisition-strategy.md` (this session output).
**Output:** Profile #3 (Marcus + Daniel) locked. 4-channel strategy. Weekly male-pipeline check during Weeks 4-9. Adjustments if the funnel under-yields.
**Calls it:** Farrice + Andrea jointly.

### 6. Event Producer
**Trigger:** Venue outreach (Week 1-3). Hire/volunteer list (Week 5-6). Run-of-show (Week 8). Day-of (Week 10).
**Backing:** `02-briefs/venue-pitch.md` + new `01-*` files (this session) + `05-ops/06-run-of-show.md` + new ops docs as needed.
**Output:** Venue locked, hire-list locked, run-of-show locked, day-of execution plan locked.
**Calls it:** Farrice. Andrea adjudicates venue + hires.

### 7. Revenue Architect
**Trigger:** Ticket-pricing decision (Week 2 once venue cost is known). Sponsor offers (whenever they appear; default = decline per BOS doctrine).
**Backing:** `revenue-stack` + `offer-stack` + Section 4 break-even model below.
**Output:** Locked ticket price + scenario projections + sponsor decision template (BOS `00-foundation/05-non-negotiables.md` sponsor doctrine).
**Calls it:** Farrice.

### 8. Risk Tracker
**Trigger:** Every working session — `RISKS.md` updated when anything changes status. Pre-call review before every Andrea check-in.
**Backing:** Existing `RISKS.md` + this Command Center.
**Output:** Live risk register. Flagged blockers surface in chat, not buried in docs.
**Calls it:** Farrice (and the system auto-surfaces in any deliverable that touches an open risk).

---

## Section 3 — The 8 Workstreams

The work of getting to Event #1 sorts into eight workstreams. Each one has an owner, a window in the 10-week sprint, and a single critical decision that locks the workstream forward. The map exists so that on any given Monday, Andrea and Farrice can look at one row and know which workstream is on the critical path that week and which workstreams can wait.

The order on the table is roughly the order of importance. Venue is first because every other variable resolves once venue is locked. Male acquisition is second because it's the asymmetric problem and gets weekly attention for nine straight weeks. The content engine, the landing page, the application gate, the network mining, the run-of-show, and the revenue stack follow. Read the table as a sequence of commitments, not a list of tasks.

| # | Workstream | Owner | Weeks | Critical decisions |
|---|---|---|---|---|
| 1 | **Venue lockdown** | Event Producer | 1-3 | By Week 3: venue locked OR Plan B (house party) activated |
| 2 | **Male acquisition (Profile #3 + 4 channels)** | Male Acquisition Strategist | 1-9 | Week 1: Profile #3 locked. Week 5: friend-pair mechanic seeded. Week 8: pipeline check |
| 3 | **Landing page + email signup** | Lead Capture Architect | 2-3 | Week 3: live with copy passing voice check |
| 4 | **IG content engine activation** | Content Engine | 2-10 | Week 2: bio + first 5 posts live. Week 4: rhythm locked (3x/wk + stories) |
| 5 | **Waitlist + application gate** | Lead Capture Architect | 4-5 | Week 5: gate live, taking applications |
| 6 | **Network mining (warm invites)** | Andrea + Farrice (irreducible) | 1-8 | Week 2: list generated. Week 5: Phase 1 outreach. Week 8: Phase 2 (friend-pair) |
| 7 | **Day-of staffing + run-of-show** | Event Producer | 5-9 | Week 6: hires/volunteers identified. Week 9: run-of-show locked |
| 8 | **Ticket pricing + revenue tracking** | Revenue Architect | 2 + 10 | Week 2: price locked. Post-event: P&L logged via `revenue_tracker.py` |

---

## Section 4 — Break-Even Math + Ticket Pricing Model

We optimized the math for $500 to $1,000 net profit, not the maximum extractable from 50 attendees. Two reasons. The first is proof: Event #1 needs to land as a model that works at a sustainable cadence, not a one-off that runs the founders to exhaustion. A $40 ticket at 50 attendees gross $2,000; lean costs of $1,030 to $1,230 leave $770 to $970 net. That band is wide enough to absorb a venue overage and narrow enough that the founders cannot quietly inflate the room or extract more from the attendees than the format honestly asks for. The second is signal: a small-net Event #1 lets the brand say "this is the room we built, and it broke even on day one" honestly, without padded press numbers or inflated sponsor decks. Once the room is proven, Event #2 scales the math without scaling the principle.

The table below is the actual model. Three cost scenarios (Lean, Standard, Premium) crossed with seven ticket prices. The recommendation is Lean Path + $40 ticket, with Tier 1 venue as the variable that decides whether the margin is $770 or closer to $970. Andrea picks the scenario once venue cost is known.

### Cost categories

| Category | Lean | Standard | Premium |
|---|---|---|---|
| Venue (3hr Saturday) | $500-700 (Tier 1 friend rate / barter) | $1,000-1,200 (Tier 2 mid-market) | $1,300-1,500 (Tier 2 premium) |
| Photographer / videographer | $0 (friend volunteer) | $300 (paid 3-hr coverage) | $500 (2 people, longer coverage) |
| Non-alcoholic drinks (water + iced tea + kombucha + sparkling) | $150 | $175 | $225 |
| Light snacks (dried fruit, nuts, dark chocolate) | $150 | $200 | $250 |
| Supplies (phone basket, signage, name protocols if used) | $80 | $100 | $150 |
| Event liability insurance (one-day) | $150 | $200 | $250 |
| Landing page tooling (Carrd / Beehiiv free or paid) | $0 | $19 | $29 |
| Email tooling (Beehiiv has email; free tier) | $0 | $0 | $0 |
| Light IG content boost (optional) | $0 | $100 | $300 |
| Day-of paid staff (ticket worker + setup help) | $0 (volunteers) | $200 | $400 |
| **Total cost** | **$1,030-1,230** | **$2,294-2,494** | **$3,304-3,604** |

### Revenue scenarios (50 attendees × ticket price)

| Ticket price | Total revenue | Lean profit | Standard profit | Premium profit |
|---|---|---|---|---|
| $30 | $1,500 | $270-470 | -$994 to -$794 | -$2,104 to -$1,804 |
| $35 | $1,750 | $520-720 | -$744 to -$544 | -$1,854 to -$1,554 |
| $40 | $2,000 | **$770-970** | -$494 to -$294 | -$1,604 to -$1,304 |
| $45 | $2,250 | $1,020-1,220 | -$244 to -$44 | -$1,354 to -$1,054 |
| $50 | $2,500 | $1,270-1,470 | $6-206 | -$1,104 to -$804 |
| $55 | $2,750 | $1,520-1,720 | $256-456 | **$-854 to -$554** |
| $60 | $3,000 | $1,770-1,970 | $506-706 | -$604 to -$304 |

### Recommendation

**The Lean Profit Path at $40/ticket** is the strongest first-event posture:
- Profit margin: $770-970 (45-50% margin)
- Sustainable for Event #2 reinvestment
- Aligns with BOS metric: *"stories over metrics" — couples formed, not premium pricing*
- $40 reads as "serious commitment, not premium product" — consistent with hell-yes filter
- Daybreaker / Pure Dating / The Wing first-event ticket prices were $25-45 range; $40 sits at the right perceived value

**If Tier 1 venue lands at $500 (friend rate / barter):** profit climbs to $970+. Use this margin to invest in Event #2 (better photographer, light IG boost, polished launch).

**If Standard Path becomes necessary (Tier 1 doesn't land):** raise ticket to $50 OR reduce attendees to 40 (40 × $45 = $1,800 minus $2,300 standard cost = -$500 — kills profitability; only viable if revenue covers via $55+ ticket). At Standard with $50 ticket, you're break-even on Event #1, which is acceptable but means Event #2 needs to scale to be profitable.

**Premium Path is not recommended for Event #1.** First-event polish doesn't compound; reputation does. Save Premium for Event #4-5 when the audience has proof.

### Sensitivity check

The biggest swing factor is **venue cost**. Tier 1 friend-rate venue is the difference between profitable Event #1 and break-even Event #1. **Venue outreach is therefore the highest-leverage week-1 work.**

### Where Andrea decides

Once venue cost is known (Week 2-3):
1. Pick scenario (Lean / Standard / Premium)
2. Pick ticket price ($35-50 range honest)
3. Lock the Tier 3 fallback if Lean isn't achievable

---

## Section 5 — Network Mining Plan (Andrea + Farrice — irreducible)

This is the section no agent can run for us. The current warm network sits at fewer than 10 hell-yes contacts, and that floor is what the room's first foundation gets built on. Phase 1 of the funnel is personal outreach from Andrea and Farrice directly: a name, a relationship, a one-line invite written for that specific person. A curated room cannot be sourced from a cold list. The names are the work, and the work is private.

The mechanic is straightforward. Each of us drafts our own lists in Week 1, separately, by category. We combine and sequence in Week 2. Phase 1 outreach starts Week 4. The confidentiality rule is non-negotiable: these lists never enter IG, email, the BOS, or any shared doc. The room is curated; the names that compose it are too.

### The Network Mining Exercise (do this in Week 1)

Each of you, separately, list the following:

**Andrea's lists (target totals in parentheses):**

1. **Hell-yes female friends in Chicago who are single, 28-40, want a partner** (target 10-15)
   - Phone contacts + Instagram followers + arts-world connections + Costa Rican / Latin scene
   - For each: their hell-yes recognition test — would she screenshot the manifesto and send it to her group chat?

2. **Hell-yes male friends in Chicago, 30-40, single, would fit Marcus or Daniel** (target 6-10)
   - Music scene (NYO alumni in Chicago, conservatory peers, JR's network)
   - DJ Homies network
   - Costa Rican / Latin scene (Marcus profile, especially)
   - Friend-of-friend introductions (someone she's met once who fit but never followed up)

3. **People who might know venues** (target 5-8)
   - Studio owners, gallery curators, dance space managers, music venue bookers she's met
   - The Tier 1 venue list seeds from here

4. **People who might know other singles** (target 10-15)
   - Especially: matchmakers, therapists, life coaches, fitness instructors with single clients
   - The Phase 2 referral network — they vouch for attendees they know

**Farrice's lists (target totals in parentheses):**

1. **Hell-yes single male friends in Chicago, 30-40** (target 8-12)
   - Your network is the male acquisition Channel 1's anchor
   - For each: would they trust your invite to a curated room?

2. **Strategic introduction targets** (target 5-8)
   - Journalists who cover Chicago culture (post-event press)
   - Influencers in the Chicago single-30s scene (Phase 3 visibility)
   - Possible venue connections from your side

### Output

Two private docs, one per person. Names, contacts, what makes them hell-yes (one sentence each), one specific outreach line per person.

**Confidentiality:** These lists never leave you and Andrea. Not in IG, not in email, not in the BOS. Phase 1 outreach is private. The room is curated; the names that compose it are too.

### When the lists land

- Andrea + Farrice each complete in Week 1
- Combined in Week 2 (de-duplicated, sequenced)
- Phase 1 outreach (Channel 1 men + female hell-yes anchors) begins Week 4
- Phase 2 outreach (friend-pair mechanic) begins Week 6
- Phase 3 outreach (warm network referrals) begins Week 7

---

## Section 6 — The 10-Week Sprint Calendar

The sprint is built as a sustainable cadence for two operators with day jobs and lives. Each week carries one to three priorities and no more. Most weeks ask for six to ten hours of focused work between us, peaking at fifteen in the final week. If a week's load creeps above that, the work for that week is overscoped and gets cut, not heroically absorbed.

Assume Saturday July 18, 2026 as the event date (Andrea adjusts to July 25 if she names that on or before May 23). The calendar reads as a ritual: Monday is the Command Center review, mid-week is the production work, Friday is the artifact handoff. Two operators, ten weeks, one event. The rhythm is the discipline.

### Week 1 — May 19-25 (current week)
**Priorities:** Confirm event date · Profile #3 locked · Male acquisition strategy locked · Venue outreach starts · Network lists drafted.
**Deliverables this week:**
- ✅ Pre-Launch Command Center (this doc)
- ✅ Profile #3 (Marcus + Daniel) locked in ICP Master (parallel agent in progress)
- ✅ `02-male-acquisition-strategy.md` (parallel agent in progress)
- ✅ Venue outreach pack: target list framework + warm pitch + cold email + follow-up tree (parallel agent in progress)
- Andrea network list (Andrea's homework)
- Farrice network list (Farrice's homework)
- Andrea confirms event date

### Week 2 — May 26-June 1
**Priorities:** Venue outreach in market · Landing page wireframe + copy drafted · IG bio rewrite + first 5 posts staged · Ticket price locked once venue cost known.
**Deliverables:**
- Tier 1 + Tier 2 venue outreach sent (4-6 warm + 8-10 cold)
- Landing page copy drafted (Lead Capture Architect)
- IG bio rewrite + first 5 posts (Content Engine)
- Ticket price scenario picked

### Week 3 — June 2-8
**Priorities:** Venue LOCKED (Tier 1/2 by Wed; Tier 3 activated if not) · Landing page LIVE with email signup · IG content engine running (3x/wk + daily stories).
**Deliverables:**
- Venue confirmed in writing
- Landing page live at `resonance.[domain]/event-1` (or hosted on Beehiiv/Carrd)
- IG content rhythm locked

### Week 4 — June 9-15
**Priorities:** Application gate built · Email welcome sequence live · Phase 1 outreach begins.
**Deliverables:**
- Application gate (3-5 questions, BOS hell-yes filter encoded)
- Welcome email sequence (3-5 emails)
- Andrea + Farrice each send 5-8 Phase 1 invites
- IG content escalating

### Week 5 — June 16-22
**Priorities:** Phase 1 conversions tracked · Friend-pair mechanic seeded · Day-of staffing scoped.
**Deliverables:**
- Phase 1 RSVPs (target: 15-20 confirmed)
- Day-of staffing list (photographer, ticket worker, social capture, setup helper)
- Friend-pair language live in IG + email

### Week 6 — June 23-29
**Priorities:** Public funnel open · Tier 2 IG content (founder origin, male-targeted posts) · Phase 2 outreach.
**Deliverables:**
- Public application form open
- Andrea founder-origin carousel live (drawing on v1.1 story)
- Phase 2 invitations sent (friend-pair language activated)
- Male channel content (Daniel-targeted) begins

### Week 7 — June 30-July 6
**Priorities:** Application volume management · Decline scripts in use · Male pipeline check (mid-funnel).
**Deliverables:**
- Acceptance/decline emails per application
- Male pipeline check (count confirmed men vs target of 20)
- IG content peak intensity

### Week 8 — July 7-13
**Priorities:** Final confirmations · Run-of-show drafted · Music set drafted · Day-of staffing locked.
**Deliverables:**
- Run-of-show v1 (Andrea + Farrice + day-of staff briefing material)
- 3-hour set draft from Andrea
- Final tickets sold
- Photographer + day-of staff confirmed

### Week 9 — July 14-17
**Priorities:** Final week. Logistics + reminders.
**Deliverables:**
- Attendee phone confirmation calls (Andrea + Farrice each take 25 names)
- Venue walkthrough (1-2 days before)
- Phone basket + signage + drinks/snacks bought
- Final IG push: anticipation + bring-your-presence content
- Pre-event call with staff/volunteers

### Week 10 — July 18 (event day) — July 25 (post-event)
**Priorities:** Event executes. Capture stories.
**Deliverables:**
- Event runs 2pm-5pm
- Exit interviews captured (Andrea's `05-ops/05-exit-interview-protocol.md`)
- Post-event recap content (Pillar 2 Story content begins)
- P&L logged via `revenue_tracker.py`
- AAR (after-action review) → feeds v1.2 BOS upgrade

---

## Section 7 — This Week's Punch List (May 19-25)

The punch list is the only part of this document that gets rewritten weekly. It's the section both of us check on Tuesday morning and Friday afternoon. Items are dated to the day they're due, owned by name, and the unchecked boxes are the truth of where the week stands. If something slips on Friday, it slips into Monday's Command Center review — not into a separate doc, not into chat.

**Today (May 19):**
- [x] Command Center doc shipped (this file)
- [x] Profile #3 + male acquisition strategy dispatched (background)
- [x] Venue outreach pack dispatched (background)
- [ ] Farrice reviews Profile #3 + strategy + venue pack when agents finish
- [ ] Farrice synthesizes outputs into chat for Andrea

**By Wed May 21:**
- [ ] Andrea reviews v1.1 BOS foundation (Drive folder `2026-05-11 — v1.1 Session 1 Foundation Review`)
- [ ] Andrea confirms event date (July 18 or 25)
- [ ] Andrea + Farrice each begin network lists

**By Fri May 23:**
- [ ] Network lists drafted (private to each)
- [ ] Venue target list finalized (Tier 1 names from Andrea's network + Tier 2 archetypes from research)
- [ ] First Tier 1 venue DMs sent
- [ ] Ticket price scenario draft (Andrea picks)

**By Sun May 25:**
- [ ] First Tier 2 cold pitches sent (4-6 venues)
- [ ] Landing page wireframe brief delivered to Lead Capture Architect (Session 3 dispatch)
- [ ] IG bio rewrite briefed (Content Engine dispatch)

---

## Section 7.5 — Andrea's Role at Event #1 (Doctrine Pointer)

**Andrea is the MC + host + curator at Event #1. She is NOT performing as DJ.** A separate DJ-of-record (hire by Week 4, public Week 7) plays. Andrea has a mic, not a controller. She welcomes guests, MCs briefly, works the floor. Andrea IS a DJ by identity (music school + national youth orchestra background) — that stays canonical in her bio, founder story, and brand voice. But at Event #1, she hosts. She'll DJ at a future event when she's ready.

This doctrine applies to: all caption copy, all photoshoot direction, all venue pitches, all volunteer briefings, all DJ-of-record outreach. Full doctrine + future DJ arc + DJ-of-record selection criteria at: **`08-andrea-event-role-doctrine.md`**.

Files updated 2026-05-19 to reflect this doctrine: `04-ig-profile-and-first-week-content.md` (bio v1), `02-male-acquisition-strategy.md` (hooks #3 + #6), `05-photoshoot-brief.md` (Shot Category D — host/MC posture).

---

## Section 8 — Decision Gates (the calendar of locks)

Decision gates are commitment devices. Each row in the table is a decision that, by the date listed, gets made and written down. If the decision isn't made by the date, the default activates automatically. We built it this way because two operators with day jobs are vulnerable to one particular failure mode: an open question that nobody closes because nobody owns the closing. Locks and defaults remove that failure mode. Either the decision is made by the owner on the date, or the default carries the work forward without a meeting. The one thing the system will not tolerate is an open decision past its date.

The table is the calendar of locks. Read it backwards from event day. Every gate before July 18 is load-bearing for something downstream.

| Date | Decision | Who decides | Backup plan |
|---|---|---|---|
| 2026-05-23 | Event date locked | Andrea | Default to July 18 if she's uncertain |
| 2026-05-30 | Ticket price locked | Andrea (informed by venue cost) | Default $40 if Tier 1 lands; $50 if Tier 2 |
| 2026-06-02 | Venue locked | Andrea + Farrice | Tier 3 (house party) activated if not |
| 2026-06-08 | Landing page live | Farrice | Carrd holding page if Beehiiv slips |
| 2026-06-15 | Application gate live | Farrice | Manual application via email if gate slips |
| 2026-07-06 | Male pipeline check | Andrea + Farrice | If <16 men confirmed: activate Backup Channels OR reduce room to 40 maintaining ratio |
| 2026-07-13 | Final attendee lock | Andrea + Farrice | Waitlist activated for no-shows |
| 2026-07-18 | Event day | Andrea executes | — |

---

## Section 9 — Risks + Open Questions

The risks list is the document that keeps us honest. Two distinctions matter. **Active risks** are real exposures we're already managing; each one has a named mitigation and a person watching it. **Open questions** are items Andrea adjudicates that affect downstream work but don't currently block it. The discipline is surfacing the risk the moment it's identified, in writing, before it migrates from "manageable" to "blocker." Anything that lives only in chat threads is invisible by Wednesday.

Cross-reference `RISKS.md` for the live register that updates between Command Center revisions.

### Active risks (managed but unresolved)

1. **Venue inventory tightening** — Chicago July weekends booking up. Mitigation: Week 1 outreach starts immediately (this session).
2. **Male acquisition under-yield** — historical base rate is 60-65% female-skew. Mitigation: 4-channel strategy active Week 1.
3. **Andrea's bandwidth** — she's also working her DJ life and her relationship. Mitigation: no week requires >8-10 hours of her time outside what she'd already be doing.
4. **First-event public-funnel pressure** — only 10 warm contacts. Mitigation: IG + landing page must convert hard; network mining grows the warm pool.

### Open questions (Andrea adjudicates)

1. **Event date** — July 18 or July 25? Locks Andrea's calendar + venue calendar.
2. **Costa Rica reference in public copy** — comfortable level for founder-origin posts? (From v1.1 Session 1 Handoff Q3.)
3. **Imani Profile #2 lock** — recommended, awaiting her sign-off.
4. **Enemy 5 (performance demand)** in Brand Bible — add or muddy? (From v1.1 Session 1 Handoff Q4.)
5. **Friend-pair mechanic phrasing** — once Profile #3 is reviewed, the application gate language for "bring a vouched guest" needs her sign-off.

---

## Section 10 — Production Files Index (this pre-launch directory)

This is the ledger of what's been built. Files ship by session; the index records which session shipped what, so anyone reading the directory can reconstruct the chronology and know which files are stable versus which are still being amended. The list is also the briefing material for a future hire: read top-to-bottom and you have the entire production state of pre-launch in one view.

As of 2026-05-19 (end of Session 2.5):

**Shipped Session 2.5 (2026-05-19):**
- ✅ `00-command-center.md` — this file (the spine)
- ✅ `01-venue-target-list-framework.md` — 3-tier framework + 7 decision questions
- ✅ `01a-venue-warm-pitch.md` — TEXT / DM / EMAIL versions
- ✅ `01b-venue-cold-pitch-email.md` — 5 subject lines + body + PS
- ✅ `01c-venue-followup-and-decision-tree.md` — 7 decision branches
- ✅ `02-male-acquisition-strategy.md` — 4-channel strategy + 14-line hook bank (Marcus + Daniel split)

**Shipped Session 3 (2026-05-19 continued — "help me as much as possible"):**
- ✅ `03-this-week-action-plan.md` — Day-by-day Tue 5/19 → Mon 5/26 with hour budgets per person
- ✅ `04-ig-profile-and-first-week-content.md` — IG bio + 5 feed posts + Stories sequence + Reel 1 with full copy + visual briefs *(bio v1 updated 2026-05-19 for MC pivot)*
- ✅ `05-photoshoot-brief.md` — 15 shot list + 3 locations + photographer brief + wardrobe + budget options + golden hour windows *(updated 2026-05-19 with Shot Category D — host/MC posture)*
- ✅ `06-tools-stack-setup.md` — Canva Pro / Claude Pro / Beehiiv / Tally / Linktree / VSCO onboarding sequence *(updated 2026-05-19 with 06a + 06b links)*
- ✅ `07-anti-omission-audit.md` — 42-item first-time-producer checklist (Legal / Day-of / Staff / Attendee / Contingencies / Post-Event)

**Shipped Session 4-part-A (2026-05-19 continued — Canva + Claude + MC pivot):**
- ✅ `06a-canva-pro-action-steps.md` — Cold-to-Day-1-post-ready in 90 min (5 stages: Brand Kit / Brand Voice / Folders / 12 templates / Day 1 graphic + Magic Resize) + quick-reference card (Magic Write prompts / iPhone color-grading / Sunday batch ritual / Content Planner)
- ✅ `06b-claude-pro-action-steps.md` — Resonance Brand HQ Project setup in 60 min (5 steps: Create Project / Paste system prompt / Upload 5 knowledge files / Test 5 starter workflows / Claude vs. Magic Write decision rule) with full prompt templates and example I/O
- ✅ `08-andrea-event-role-doctrine.md` — Single source of truth for Andrea's MC + host + curator role at Event #1 (not performing as DJ) + DJ-of-record arc + future DJ arc + volunteer/photographer briefing paragraph
- ✅ `02-male-acquisition-strategy.md` (edited) — hooks #3 + #6 updated to reflect MC-not-DJ doctrine

**Also shipped (cross-folder):**
- ✅ `brand-operating-system/00-foundation/02-icp-master.md` Section 4 — Profile #3 LOCKED (Marcus + Daniel as Path B complementary avatars)
- ✅ `RISKS.md` — IG handle locked (`@resonance.chicago`)

**Next session priorities (Session 4-part-B — landing page + waitlist + Code of Conduct):**
- `09-code-of-conduct-and-photo-release.md` — legal-light templates
- `10-hire-list-staffing-rates.md` — paid vs volunteer breakdown with Chicago rate ranges (DJ-of-record + photographer + door + floor host)
- `11-landing-page-copy.md` — Beehiiv landing page wireframe + copy
- `12-application-gate-questions.md` — Tally form questions + decline scripts
- `13-profitability-revised-math.md` — $500-$1,000 net target overlay on Command Center break-even

**Week 4+ priorities:**
- `13-email-sequences.md` — welcome + waitlist + T-14/T-7/T-1 reminder sequences
- `14-day-of-staffing-plan.md` — role descriptions + briefing script
- `15-run-of-show-event-1.md` — derivative of `05-ops/06-run-of-show.md`

---

*Command Center updated weekly. If anything contradicts the BOS spine docs (`00-foundation/`), the BOS spine wins and this file gets amended.*
