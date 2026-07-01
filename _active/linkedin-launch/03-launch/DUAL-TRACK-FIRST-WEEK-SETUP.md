# Dual-Track Lead-Gen: First Week Setup Guide
## Get the System Running in 5 Days

> **You don't need perfect.** You need the system running. This guide walks you through the first week: set up your signal tracking, post your first teardown, run discovery calls on any warm leads, and measure what lands. Everything after Week 1 is iteration.

---

## PRE-WEEK-1: Setup (Friday, 2 hrs)

### 1. Confirm Your Beachhead (15 min)
Open `/Users/farricecain/Google Antigravity/_active/linkedin-launch/01-research/MASTER-STRATEGY.md`. Answer:
- **What's my primary niche/lane for the next 4 weeks?** (wellness/supplement/performance brands, or different?)
- **Who are my Top-5 target brands?** (from `research/wellness-supplement-brand-niche.md`)
- **What's the offer I'm leading with?** (Angle Audit? Proof Run? Fractional seat? Embed?)

If MASTER-STRATEGY is stale or missing, run `/farrice-engine repoint` and come back here.

### 2. Set Up Your Signal Tracker (30 min)
In a Google Sheet or a local `signal-log.md`, create three tabs:

**TAB 1: Weekly Signal Summary**
```
WEEK OF: [DATE]
Decision-maker profile views: [count, names]
Decision-maker saves: [count, names]
Substantive comments from ICP: [count, names]
Connection requests from decision-makers: [count, names]
Teardown DM replies: [count, names]
```

**TAB 2: Live Lead Tracker** (mirrors `pipeline.md` but real-time)
```
| Name | Brand | Role | Track | Stage | Last Touch | Next Action |
|------|-------|------|-------|-------|------------|-------------|
|      |       |      |       |       |            |             |
```

**TAB 3: Teardown Queue**
```
| Brand | Founder/Growth Lead | Status (prep/building/posted/dm'd/replied) | Date Sent | Notes |
|-------|---------------------|-------------------------------------------|-----------|-------|
|       |                     |                                             |           |       |
```

### 3. Pull Your First Teardown Target (15 min)
- Run `python3 execution/brand_radar.py` (updates your `daily/brand-radar-YYYY-WW.md`).
- Pick **one brand from Top-10** that has:
  - Clear sameness pattern (look at 5 recent posts).
  - Engaged audience (comments + shares visible).
  - Founder/growth lead you can find/DM.
- Add to Teardown Queue (TAB 3). Status: "prep".

---

## WEEK 1: Daily Motion

### Monday
**Morning (15 min)**
- Post 1x via `/linkedin-daily`.

**Mid-Morning (45 min)**
- Spend 45 min on comments:
  - 5 substantive comments on your Top-5 target brands (Gainful, Four Sigmatic, Create Wellness, etc.).
  - 5 substantive comments on category voices / content creators in wellness.
  - Log brand names to your tracker (for warm-up sequencing).

**End of Day (15 min)**
- Check LinkedIn notifications for any profile views, saves, comments, connection requests.
- Tag anyone decision-maker-level in your signal tracker.
- Update pipeline: anyone who engaged with your post = move to "warmed".

**Evening (1.5–2 hrs) — BUILD TEARDOWN 1**
- Follow the 6-part template in `teardown-system.md`:
  1. Credit first
  2. Sameness tell
  3. Body-level truth
  4. 3 angles I'd ship
  5. Compliance-safe note
  6. Close
- Save draft. Review for voice (read aloud—does it sound like you?). Run through `directives/ai-slop-ban-bank.md` (no cheap question closes, no twin-sentence aphorisms, etc.).

---

### Tuesday–Wednesday
**Morning (15 min each day)**
- Post 1x via `/linkedin-daily`.

**Mid-Morning (45 min each day)**
- Continue the commenting pattern (10/day across brand + category accounts).
- Log new signal.

**End of Day (15 min each day)**
- Signal scan. Any new decision-maker engagement? Tag it.

**Evening Tuesday (1 hr) — FINALIZE & ROUTE TEARDOWN 1**
- Finalize teardown draft. Does it prove you can think strategically about their brand?
- Split into two versions:
  - **Public proof post** (generalize the principle, reference the brand respectfully).
  - **Elite Magnet DM** (full custom teardown, personalized to the founder/growth lead).
- Post the public version to LinkedIn. Log the link in `proof-tracker.md`.
- Find the brand founder/growth lead's LinkedIn DM. Send the Elite Magnet version.
- Log to `pipeline.md`: brand, stage = "dm'd", asset sent = "teardown", date sent = [today].

**Evening Wednesday (optional)**
- If the teardown got engagement (saves, comments, views), reply with depth. Don't wait for them to move; warm them more.

---

### Thursday
**Morning (15 min)**
- Post 1x via `/linkedin-daily`.

**Mid-Morning (45 min)**
- Comments (10/day, same pattern).

**End of Day (15 min)**
- Signal scan. Any replies to the teardown DM? Flag immediately. Move to "replied" in pipeline.

**Evening (if any teardown replies came in) — DISCOVERY CALL PREP**
- Follow Section 4 of the playbook (DISCOVERY CALL PLAYBOOK).
- Send them two time options for a 30–45 min call this week.
- Before the call: if ROLE track, review their team/org. If CLIENT track, review their content gaps.

---

### Friday
**Morning (15 min)**
- Post 1x via `/linkedin-daily`.

**Mid-Morning (45 min)**
- Final comments of the week.

**End of Day (1 hr) — WEEK 1 REVIEW**
- Signal review:
  - How many decision-maker profile views? Saves? Comments from ICP?
  - Any new warm leads?
  - Any teardown replies?
- Pipeline review:
  - Update `pipeline.md` with week's changes.
  - Any leads ready for a discovery call this week? (If so, book it.)
- Forecast next week:
  - Will any current "warmed" leads be ready for a teardown DM? (Add to next week's queue.)
  - Which brand is Teardown 2? (Add to next week's prep.)

**Log to your tracker (TAB 1).**

---

## IF YOU GET A DISCOVERY CALL THIS WEEK

**Before the Call (30 min)**
- Read the playbook Section 4 (DISCOVERY CALL PLAYBOOK) again. Know your ROLE track questions + CLIENT track questions.
- Pull their brand's 3 most recent posts. Read them. Know what you'd do differently.
- Write 3 bullet-point talking points: "If this is a role, here's what I'd do in 90 days."

**During the Call (30–45 min)**
- Start with: *"Thanks for looking at the teardown. Just want to make sure I'm pitching the right thing. Let me ask a few things..."*
- If ROLE track: "Tell me about the role—what's the pain? Embedded or fractional?"
- If CLIENT track: "Walk me through your current content system and where it breaks."
- Listen more than you pitch. You're qualifying, not selling.
- Close with: "Before we go further—would it make sense to run a paid diagnostic (the Angle Audit) to nail the exact angle gaps?"

**After the Call (30 min)**
- Send them the Angle Audit proposal within 2 hours. Same day. Make it easy to say yes.
  - Scope: "2–3 hours to deep-dive your creative + divergence fixes. 30–45 min walkthrough. You know exactly what I'd build."
  - Price: $500–1,500 (your choice—go lower if you need proof fast).
  - Timeline: "Delivery [date 3–5 days from now]."
- Log to `pipeline.md`: stage = "call booked", next action = "send Audit proposal".

---

## END-OF-WEEK-1 CHECKLIST

- [ ] Posted 5x via `/linkedin-daily` (once per day Mon–Fri).
- [ ] Made 50 substantive comments (10/day, five brands + five category voices).
- [ ] Built + posted 1 teardown (public proof post + Elite Magnet DM).
- [ ] Logged to `pipeline.md` (all new leads, stages, dates).
- [ ] Logged to `proof-tracker.md` (teardown date + link).
- [ ] Logged to signal tracker (decision-maker views, saves, comments).
- [ ] IF discovery calls happened: sent Angle Audit proposals within 2 hours of call end.
- [ ] Filled out Week 1 summary in KPI tracker (Section 7 of playbook).

**Expected Week 1 outcome:**
- 0–2 teardown DM replies (normal; most convert after 2–3 warm touches).
- 2–5 decision-maker profile views / saves.
- 1–2 leads moved to "warmed" via commenting engagement.
- 0–1 discovery calls scheduled (or none; that's fine—Week 2 brings more).

**If you got 0 of the above:** that's OK. You're building signal. Week 2 ramps up because you've now got 50 comments + 1 proof teardown + 5 posts in the feed. Momentum compounds.

---

## WEEK 2 & BEYOND: Iteration

**Keep the same daily motion (post 1x + comments 10x).**

Add these changes:

1. **Teardown cadence:** 1 teardown/week, same day (e.g., every Monday). By mid-Week 2, you'll have 2 on the table.
2. **Signal cycling:** As leads move through stages (warmed → dm'd → replied → call booked), adjust your outreach:
   - "Warmed" leads get 2x/week substantive comments on their brand feed (gentle warm-up).
   - "Dm'd" leads get a 5-day wait; if no reply, 1 warm comment on their next brand post + follow-up DM.
   - "Replied" leads = discovery call within 48hr.
3. **Proof runs:** Once Angle Audits close, deliver in 3–5 days. Log to `proof-tracker.md`. Upsell the Proof Run same day as delivery.
4. **Revenue tracking:** Every Angle Audit or Proof Run sold = log to `proof-tracker.md` + `execution/revenue_tracker.py` (if using).

---

## TROUBLESHOOTING

**Q: I'm posting and commenting but getting no decision-maker signal.**
- A: This is normal Week 1. Decision-makers don't find you on Day 1. You need:
  - 20–30 comments minimum (they see you in their notification feed if you comment on their accounts).
  - 5+ posts so they have something to find when they search you.
  - Week 2–3 is when signal accelerates.
  - If still flat after Week 2: check your comment quality (is it actually insightful, or cheerleading?). Check your posts (are they proving Cognitive Signature, or just saying smart things?).

**Q: I got a teardown DM reply but I'm not sure which track (role vs. client).**
- A: Ask in the discovery call (it's literally the first question in Section 4). Don't guess.

**Q: No one's booking discovery calls.**
- A: Discovery calls are a lagging indicator. They come from:
  - Warm touchpoints (they need 2–3 before they feel safe enough to call).
  - Proof (the teardown + your posts prove you can do it).
  - Timing (they need to *need* help now, not eventually).
  - In Week 1–2, assume most leads are "interested but not urgent." Keep nurturing. Call volume accelerates in Week 3+.

**Q: Do I need to customize every discovery call question?**
- A: No. Use the playbook Section 4 verbatim until you've run 5+ calls. Then optimize based on what you learn.

**Q: What if an Angle Audit inquiry comes in but I'm not ready to deliver in 3–5 days?**
- A: Tell them straight: "I can deliver [date]. Does that work?" If they say no, let them go. You'll get another. Don't over-commit.

---

## SUCCESS SIGNALS (What Moves the Needle)

- **Week 1 success:** You shipped a teardown + got 2–3 decision-maker signal points. You built the infrastructure (signal tracker, pipeline, teardown queue).
- **Week 2 success:** You got 1–2 discovery calls booked OR 1 Angle Audit sold.
- **Week 3 success:** You shipped your first Angle Audit + got your first Proof Run inquiry OR booked 2+ discovery calls.
- **Week 4 success:** You're in the rhythm—posting daily, commenting substantively, teardowns on cadence, discovery calls coming in every 3–4 days, first proof run shipped.

**By end of Month 1:** You'll have ~2–3 Angle Audits sold ($1–4K revenue), building proof tokens, and 3–5 warm leads in the pipeline. The system is running.

