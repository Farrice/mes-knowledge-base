# Resonance — Gap-Action Sprint

*This is the "what a senior event producer would do this week" document. Pairs with the comprehensive anti-omission audit at [`pre-launch/07-anti-omission-audit.md`](../pre-launch/07-anti-omission-audit.md) (42 items, 34 Must-haves). The audit names what could break; this sprint names what to do about it in the next 7 days, plus surfaces the gaps the audit doesn't cover.*

*Authored: 2026-05-25. Sprint window: 2026-05-26 → 2026-06-02 (venue lock day). Owner split: Andrea (relational + brand) / Farrice (legal + operational).*

---

## Read This First — What's Already Covered

The anti-omission audit is exceptional and well-built. It already addresses:

✓ Legal/Liability (insurance, photo release, CoC, refunds, ADA, sound permit, alcohol/BYO, tax entity)
✓ Day-of Logistics (check-in flow, phone basket, bathrooms, water/snack, decibel monitoring, lighting, exits, first-aid, incident protocol, trash, DJ load-in)
✓ Staff briefing (arrival time, script, comms channel, thank-yous, backups)
✓ Attendee Experience (email cadence, day-of text, parking/transit, arrival window, exit interviews, T+30 follow-up)
✓ Contingencies (venue/DJ/photographer backup, weather, no-show, application surge)
✓ Post-event (photo selection, recap cadence, refund window)

**Of those 42 items, 33 of 34 Must-haves are still "Open" status.** The audit names them; it doesn't yet have owner + date on each. This document fixes that.

---

## Section 1 — TRUE GAPS (not in the audit, surface them now)

These are first-time-event-producer blind spots the existing audit doesn't fully cover. None are existential; all are recoverable; together they prevent ~6-8 hours of late-stage scramble.

### Gap 1 — Ticketing + Application Platform Decision (BLOCKS APPLICATION OPEN)

**What's missing:** The audit (item 1.2) names Tally for the photo release form but doesn't lock the ticketing platform. The application gate (`03-marketing/06-why-gate-mechanics.md`) lives somewhere — but where?

**The decision matrix:**

| Platform | Strengths | Weaknesses | Cost |
|---|---|---|---|
| **Tally (application gate) + Stripe Payment Links (payment)** | Free tier handles all features. Tally is voice-aligned (clean, founder-controlled). Stripe is bulletproof. Andrea reviews + approves before sending payment link. | Two-step flow (apply → wait → pay). Email orchestration is manual unless wired via Zapier. | $0 + 2.9% + $0.30 per ticket |
| **Eventbrite** | Industry-standard, attendees recognize. Payment, refund, reminder emails all built-in. Embeds easily. | Templated brand surface (Resonance voice doesn't fit Eventbrite chrome). Eventbrite holds funds 5-7 days post-event. Their "Discover" page may surface Event #1 alongside off-brand events. | 3.7% + $1.79 per paid ticket |
| **Posh** | Designed for curated events. Cleaner brand surface than Eventbrite. Built-in waitlist. | $1.99 per ticket fee. Smaller install base. Some attendee friction. | $1.99 per ticket |
| **Withfriends** | Built for membership + recurring events. Strong brand surface. | Recurring-event model not yet relevant; over-engineered for Event #1. | Variable |

**Recommendation:** **Tally form (application gate) + Stripe Payment Link (post-vet payment).** Voice-aligned, founder-controlled, lowest fees, payment-after-vet enforces the curation discipline. Wire confirmation emails via Beehiiv (Andrea's newsletter platform).

**Decision needed:** by 2026-05-29 (so the form ships before Phase 2 announcement opens applications)
**Owner:** Farrice (build), Andrea (sign-off on form copy + question phrasing)

### Gap 2 — Landing Page (BLOCKS @resonance.chicago BIO LINK)

**What's missing:** RISKS.md item #6 says the landing page can ship on a Beehiiv subdomain (`events.beehiiv.com/resonance`) or Carrd subdomain until permanent domain locks. The audit doesn't address this; the bio link in `@resonance.chicago` needs somewhere to go before Phase 1 ships.

**The minimal landing page for Phase 1** (ships when Phase 1 announcement does):
- Hero photograph (one of the variant heroes we just generated)
- Manifesto excerpt (4-6 sentences)
- One-liner: "Daytime. Sober. Curated. Chicago. First event July 2026."
- Waitlist signup (email + first name only)
- Founder paragraph (story Short version, 92 words)
- Mailchimp/Beehiiv embed for waitlist

**Recommendation:** **Beehiiv landing page (free with the newsletter platform).** Andrea owns the newsletter platform decision per RISKS #8 (still open). If Beehiiv is the platform pick, landing page is free. If she picks Substack, use Carrd ($19/year). Lock newsletter platform decision this week to unblock landing page build.

**Decision needed:** Newsletter platform pick by 2026-05-29.
**Owner:** Andrea (platform decision), Farrice (page build + copy from announcement package).

### Gap 3 — Andrea's Pre-Launch Brand Portrait

**What's missing:** `pre-launch/05-photoshoot-brief.md` exists for the event but Andrea needs a strong portrait BEFORE Event #1 for: the @resonance.chicago profile photo, the IG carousel founder posts (Phase 1), the press teaser paragraph image, the About-page anchor, the landing page founder paragraph.

**Without it:** Phase 1 ships with a placeholder profile photo or an old DJ headshot that doesn't match the daytime-as-mechanic visual register.

**The brief:** One 90-minute photoshoot, daytime hours, in a Chicago space that matches the chosen visual variant. Mixed: 3-4 portrait crops + 3-4 environmental "Andrea at the booth" or "Andrea in the room" shots. Photographer: a friend with good camera + the photography-rules.md brief paste-in, OR a $300-500 booking from Andrea's photo network.

**Recommendation:** **Book within 14 days.** Once visual variant locks (this week), brief the photographer with the chosen variant's composition emphasis. Shoot in the venue if locked by then; otherwise in a clean Chicago daylight space (loft, dance studio, gallery).

**Decision needed:** Photographer + date by 2026-06-05.
**Owner:** Andrea (book, brief, attend).

### Gap 4 — DJ Written Agreement (with JR or Whoever Anchors)

**What's missing:** The audit (5.2) mentions a $100 retainer for the *backup* DJ, but there's no template or named requirement for a written agreement with the *primary* anchor DJ (JR or backup). First-time producers commonly skip this because the DJ is a friend/family.

**Why it matters:** "Verbal yes from a cousin" is fine until something happens (illness, conflict, miscommunication on time/rate). A 1-pager written agreement protects both sides. Day, hours, set length, what's covered (Andrea sets sound + curation + gear; JR plays his set within Andrea's curated arc), payment, what happens if either cancels, mutual cross-promotion.

**Recommendation:** **A 1-page Memo of Understanding (MOU) emailed and signed by both** within 7 days of JR confirming. Casual tone, peer-to-peer voice (Andrea's register, not legal-load-bearing). Covers: date, doors open/close, set times, Andrea's curation authority over sound, payment ($X or barter — Andrea decides), cancellation grace period (48 hours either side, refund of any deposit), photo/social use rights, plus-one allowance (1 plus-one for JR, vetted by Andrea).

**Decision needed:** As soon as JR confirms (this week or next).
**Owner:** Farrice (drafts the MOU template), Andrea (sends to JR after they confirm verbally).

### Gap 5 — The "One Trusted Friend in the Room" Doctrine

**What's missing:** The audit covers staff and attendees but doesn't name the SPECIFIC role of one trusted friend whose ONLY job is watching Andrea on event day. Andrea is DJing AND curating AND welcoming AND adjudicating — her bandwidth will be at capacity. She needs one person whose job is to:

- Watch her energy
- Force her to drink water at T+45 and T+90
- Step her outside for 90 seconds if she looks overwhelmed
- Handle any 1:1 conversation she gets pulled into beyond what serves the room
- Catch what she misses

This is NOT staff (the door host, the floor host). This is Andrea's day-of attaché. Likely Farrice or a close friend Andrea names.

**Recommendation:** **Name this person by 2026-06-15 (T-30 days).** Brief them on the role. They are unpaid (or barter — Andrea decides). They wear no obvious staff signal. They are not on the comms channel. They have one job.

**Decision needed:** Andrea picks the person by 2026-06-15.
**Owner:** Andrea (picks), Farrice (briefs).

### Gap 6 — Cash Flow Timing + Day-of Cash

**What's missing:** Ticket revenue lands in Andrea's account on a delay. Eventbrite holds funds 5-7 business days post-event. Stripe deposits typically 2 business days. Venue may want a deposit pre-event. Day-of, $150-200 cash matters for: emergency snack/ice runs, broken-thing fixes, tipping a staff helper who came through.

**Recommendation:**
- **Pre-event cash flow:** Andrea verifies she has venue deposit covered from personal funds OR confirms ticket revenue lands before venue payment is due. If not, Farrice + Andrea pre-fund venue deposit; ticket revenue replenishes Andrea after event.
- **Day-of cash:** Andrea (or Farrice as treasurer) carries $200 cash in an envelope, day-of, on her person.

**Decision needed:** Cash flow check at T-14 days (~2026-07-04).
**Owner:** Both.

### Gap 7 — Music Public-Performance Licensing (Verify, Don't Solve)

**What's missing:** ASCAP/BMI public-performance licensing for the music played at the event. For most small private events under 50 attendees in a non-commercial space, this is venue-handled OR exempt under "private event" rules. Worth verifying.

**Recommendation:** **One conversation with the venue contact**: "Does your space carry ASCAP/BMI licensing for events with recorded music, or do we need to handle it separately?" 90% of rentable venues carry it. If not, BMI offers a single-event license at ~$100-200 for events under 100 attendees.

**Decision needed:** Confirmed by 2026-06-15.
**Owner:** Farrice (asks during venue contract phase).

### Gap 8 — The "One Quiet Journalist" Doctrine (Optional, Year-2 Asset)

**What's missing:** The audit defers all press to Event #2. Sound logic. BUT: if there's ONE Chicago journalist whose beat overlaps with Resonance's room (curated rooms, daytime culture, dating culture, Latino arts), inviting them as a quiet attendee (not press, just a person who'd love this) at Event #1 builds a Year-2 press asset without compromising Event #1 curation.

**Candidate beats:**
- *Block Club Chicago* — neighborhood culture, curated daytime events
- *Chicago Reader* — arts and nightlife (with daytime twist)
- *Time Out Chicago* — events + curation
- *South Side Weekly* — community-rooted journalism

**Recommendation:** **Skip for Event #1. Park in Year-2 capture.** The audit is right to defer; this is a "if you have a journalist friend already, invite them as a person, not press" option. Don't actively pitch.

**Decision needed:** No action this sprint. Captured here so it's not forgotten.

---

## Section 2 — Anti-Omission Audit MUST-HAVES — This Week's Action Items

The audit has 34 Must-haves still Open. Not all need attention this week. These 12 are schedule-critical for the 7-day sprint (2026-05-26 → 2026-06-02):

| # | Item | Owner | Action this week | Audit ref |
|---|------|-------|---|---|
| 1 | **COI / Event liability insurance** quote + bind | Farrice | Get 2-3 quotes (Markel, Thimble, Eventbrite Insurance) by 2026-05-29. Bind upon venue lock. | §1.1 |
| 2 | **Photo release form** | Farrice + Andrea | Andrea reviews release language (1 hour). Farrice builds in Tally by 2026-05-30. Embed in application flow. | §1.2 |
| 3 | **Code of Conduct** 1-pager | Both | Andrea drafts tone in 30 min. Farrice adds operational language. Ship by 2026-05-31. | §1.3 |
| 4 | **Refund policy** | Farrice → Andrea sign-off | Farrice drafts (full refund 7+ days, 50% 3-7, no refund 72-hr). Andrea signs off. Lands on landing page when it ships. | §1.4 |
| 5 | **ADA accessibility** | Andrea (venue convo) | Every venue conversation includes step-free access question. Document in venue tracker. | §1.5 |
| 6 | **Alcohol/BYO waiver** | Farrice | Confirmed during venue contract review. Standard clause language drafted by 2026-05-31. | §1.7 |
| 7 | **Confirmation email sequence** | Farrice | Beehiiv template built by 2026-06-05. Sequence: at-application, T-14, T-7, T-1. Not blocking until applications open. | §4.1 |
| 8 | **No-show approach decision** | Andrea | Pick: overbook 5-8 (capacity 55) OR waitlist + 24-hour auto-convert. Decide by 2026-06-05. | §5.5 |
| 9 | **Backup DJ identified** | Andrea + Farrice | Backup name and verbal "you might be called" by 2026-06-15. $100 retainer offer. | §5.2 |
| 10 | **Photographer + backup photographer** | Farrice | Book event photographer by 2026-06-12. Backup name (friend with iPhone + must-capture list) by 2026-06-15. | §5.3 |
| 11 | **Andrea's day-of role doctrine** | Both | Re-read `pre-launch/08-andrea-event-role-doctrine.md`. Confirm: Andrea welcomes for first 30 min then transitions to DJ. Hand-off to door host. | (existing doc) |
| 12 | **Incident protocol pre-rehearsed** | Andrea + Farrice | 60-minute session 7-10 days pre-event. Walk through 4 scenarios: hunter slips through, attendee visibly drunk, medical, harassment claim. | §2.10 |

---

## Section 3 — Andrea's 24-Hour Pre-Event Doctrine (NEW — first-time producer protection)

Not in the existing role doctrine. First-time event producers commonly burn out at T-24 to T-3 hours from anticipatory adrenaline + last-minute scope creep. This doctrine protects against that.

### T-24 hours (Friday evening before Saturday event)
- **No new decisions.** Anything Andrea is "still deciding" at T-24 is decided by Farrice or postponed to Event #2. Andrea's only job from T-24 is recovery.
- **Phone off social media.** Resonance IG is on Farrice's phone for the night. No checking responses, no replying to DMs, no scrolling.
- **Bedtime ≤ 11pm.** Even if not tired. Body recovery for a Saturday afternoon performance.
- **Pre-prepared meal Friday dinner.** Not a "we'll order" night. Pre-cooked, easy, predictable.

### T-8 hours (Saturday 6am for 2pm event)
- **Slow morning.** No alarm shock. Wake naturally OR alarm at 8am at the earliest.
- **Walk + sunlight before screens.** 20 minutes outside.
- **Eat at 9am.** Real food. Protein + carbs.
- **No event work before 10am.** Read, music, anything not Resonance.

### T-4 hours (Saturday 10am-12pm)
- **Final hair/wardrobe.** Done by 11am.
- **One last walk-through with Farrice via text or call.** Andrea voices any final concern; Farrice confirms it's handled or absorbs it.
- **Arrival at venue 12:30pm sharp.** With load-in crew. Stays one step ahead of staff arrival (1pm).

### T-90 minutes (12:30pm-2pm)
- **Briefing at 12:45pm.** Andrea owns the room-philosophy section (5 min). Farrice owns operational (10 min).
- **DJ setup + sound check by 1:30pm.** Andrea + JR/backup work together.
- **Andrea's quiet 15 minutes from 1:30-1:45pm.** Bathroom break. Hydrate. Sit. The trusted friend (Gap 5) confirms she's good. Door host opens 2pm sharp.

### Post-event (5pm onward)
- **Andrea doesn't drive.** Farrice or trusted friend handles transportation home.
- **No content posting Saturday night.** T+24 first content drop is on the schedule. Anything earlier is adrenaline talking, not strategy.
- **Sunday morning: write 3 sentences.** One paragraph in her notes app — what felt true, what surprised, what she'd change. That's the first AAR. Everything else is Monday onward.

---

## Section 4 — The 7-Day Sprint Calendar

Mapping the above into a daily cadence. Andrea + Farrice review this every morning of the sprint.

### Mon 2026-05-26 (Day 1)
- **Andrea:** Answer the 15-question Network Inventory privately (Outreach Playbook §G). Name 4-6 Tier 1 friend-with-space candidates.
- **Farrice:** Get 2 COI insurance quotes (Markel, Thimble). Build Tally photo release form draft.

### Tue 2026-05-27 (Day 2)
- **Andrea:** Send first 2-3 warm friend-with-space asks (Outreach Playbook §B.3 — DM/text/voice memo formats).
- **Farrice:** Send first 4-5 cold paid-venue pitches (using sharpened version in Outreach Playbook §C.3). COI quote review.

### Wed 2026-05-28 (Day 3)
- **Andrea:** Send remaining 2-3 warm friend asks. Review CoC tone draft from Farrice. Pick newsletter platform (Beehiiv vs Substack).
- **Farrice:** Send remaining 3-5 cold venue pitches. Draft refund policy. Begin landing page build.

### Thu 2026-05-29 (Day 4) — **TICKETING DECISION GATE**
- **Andrea:** Tally vs Eventbrite vs Posh — decide. Sign off on application question phrasing. Site visit any responding venues.
- **Farrice:** Build ticketing flow per Andrea's pick. Tally form draft if she goes Tally route.
- **JR follow-up check:** Has JR replied? If no by EOD, schedule Andrea's Day 7 peer-to-peer follow-up message.

### Fri 2026-05-30 (Day 5)
- **Andrea:** First friend responses landing. Triage. Site visits booked for any Tier 1 yes. Photoshoot brief drafted for pre-launch brand portrait.
- **Farrice:** Photo release form live in Tally. Refund policy drafted, Andrea signs off. Landing page draft.
- **Visual variant pick** (after Farrice reviews hero shots — separate doc): pick A, B, or C. Begin BOS visual layer refresh.

### Sat 2026-05-31 (Day 6)
- **Andrea:** Application review prep (read 5-10 sample hell-yes answers from `06-why-gate-mechanics.md` to calibrate her gut). Quiet day if possible.
- **Farrice:** CoC final language ship. ADA accessibility script for venue conversations.

### Sun 2026-06-01 (Day 7) — **JR FOLLOW-UP GATE**
- **Andrea:** If JR hasn't replied, sends the peer-to-peer follow-up per Outreach Playbook §F.1.
- **Both:** Sunday review. Read RISKS.md. Update audit Open → In Progress. Walk through Day 8-14 calendar.

### Mon 2026-06-02 (Day 8) — **VENUE LOCK DECISION GATE**
- Friend OR paid venue contracted today OR Plan B (Tier 3 house party) activates with named candidate.
- COI binds upon venue contract signature (Farrice).
- Phase 2 announcement enters draft state pending JR + visual variant locks.

---

## Section 5 — What I'm Confident We're NOT Missing

The audit + this gap document together cover:

✓ Every legal/liability item
✓ Every day-of operational item
✓ Every staff role and briefing
✓ Every attendee touchpoint from RSVP → T+30 follow-up
✓ Every named contingency (venue, DJ, photographer, weather, no-show, surge)
✓ Every post-event capture (photos, recap, refund window)
✓ Tools stack decision (Tally + Stripe + Beehiiv recommendation)
✓ Landing page decision path
✓ Pre-launch brand portrait
✓ DJ MOU
✓ One-trusted-friend day-of doctrine
✓ Cash flow timing
✓ Music licensing verification path
✓ Andrea's 24-hour pre-event doctrine

Things that are **deliberately deferred** to Event #2:
- Active press pitching
- Sponsor relationships
- Influencer partnerships
- LLC formation (if Event #1 nets >$1K and Event #2 confirmed, then begin within 30 days)
- Membership/subscription model
- Multi-city expansion

If a category not on either list (audit or this sprint) starts feeling urgent, that's a signal we missed something. Add it to RISKS.md and surface in next Andrea call.

---

## Section 6 — Andrea's One-Glance Read

If Andrea has 90 seconds and wants the executive summary:

> *We're 7-8 weeks from event. This week: lock the venue (June 2). Find JR's answer (June 1). Pick the visual variant (this week). The audit at `pre-launch/07-anti-omission-audit.md` has 34 must-do items; 12 of them need movement this week (Section 2 above). Eight gaps weren't in the audit — most matter, three are big (ticketing platform, landing page, your day-of trusted friend); we have a path on each. Your 24-hour pre-event doctrine is now written (Section 3). If anything feels off, read this doc + the audit before the call.*

---

*Document ends. Update when an item moves to Resolved or a new gap surfaces.*
