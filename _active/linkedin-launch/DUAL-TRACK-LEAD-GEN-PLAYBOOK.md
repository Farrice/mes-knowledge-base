# Dual-Track Lead-Gen Playbook — LinkedIn to Client/Role
## Role Track + Client Track Operating Manual

> **Two parallel pipelines from the same daily content.** The ROLE track targets brand teams for a fractional/FTE creative-strategist seat. The CLIENT track targets the same decision-makers for project/retainer work. Both start with your daily LinkedIn content and flow through identical signal points until the discovery call, where they fork based on the lead's situation. This playbook tells you what to measure, what to do daily, how to build proof, how to run discovery, and what conversion looks like.

---

# SECTION 1: SIGNAL HIERARCHY
## What to Measure, in Priority Order

Your daily motion feeds these signals. Track them in the KPI stub at the end of this doc.

| Signal | Who | What It Means | Next Move |
|--------|-----|---------------|-----------|
| **Decision-maker profile views** | Brand founder, CMO, head of content | Recognition. They read your content and came to look at you. | Warm via comments on their brand's feed (next 3 days); if 3+ views from same account, add to DM queue |
| **Decision-maker saves** | Brand founder, CMO, head of content | Future relevance. They're keeping your post to refer back to. | Same as above; save = stronger signal than view |
| **Substantive comments from decision-makers** | On your posts, on your comments on their feed | They're reading, thinking, engaging directly. | Respond with real depth (not "thanks for the comment"); opens door for DM in 1–3 days |
| **Share requests / connection requests from decision-makers** | Incoming requests (via LinkedIn) | Warm, initiated by them. | Warm accept + DM opener within 24hr (don't wait for comment flow) |
| **DM replies to your teardown DM** | Brand founder/growth lead you DM'd with the teardown | The warmest signal. They're ready. | Qualify (role vs. client) + book discovery call within 48hr |
| **Profile views / saves from agencies** | Agencies that work with your target brands | Reach + potential sub-contracting or referral (secondary pipeline). | Optional: warm via comment or agency-specific DM (wait for 5+ views first) |

**Reach is NOT a priority metric.** Optimize for decision-maker signal (profile views + saves + comments), not likes or followers.

---

# SECTION 2: DAILY MOTION
## What You Do Every Day (60–90 min/day)

### Morning (15 min) — Post
- Publish 1x daily via `/linkedin-daily` (runs your Cognitive Signature gate + voice gate + fact-verify).
- Lane = current beachhead per `MASTER-STRATEGY.md` (wellness/supplement/performance brand niche).
- Post at 9–10am ET (brand founders typically scroll early).

### Mid-Morning (30–45 min) — Comment
- Spend 30–45 min on **substantive commenting** (not "great post"—actual depth). Target 10/day across:
  - 5 comments on brand founders' brand accounts (Gainful, Four Sigmatic, Create Wellness, etc. — names from `research/wellness-supplement-brand-niche.md`)
  - 5 comments on category voices / content creators in your space (coaches, strategists, other voices building in wellness)
- **Comment = micro-demo.** Each comment proves you think like a strategist (practitioner depth, not cheerleader).
- Track which brands/accounts you comment on (for warm-up sequencing later).

### End of Day (15 min) — Signal Scan & DM Queue Update
- **Scan** the last 24hr of `performance-log.md` + LinkedIn notifications for decision-maker signal:
  - Profile views from brand founder/CMO/head of content? Note name + brand + date.
  - Saves from the same? Flag as "warm."
  - Comments on your posts from decision-makers? Respond with depth (not a thank-you).
  - Connection requests from decision-makers? Accept + soft DM opener within 24hr.
- **Update** `pipeline.md`: move any "identified" leads to "warmed" (if they engaged with your content) or "dm'd" (if you sent the teardown).
- **Identify 1 new teardown target** for the week (pick from `research/wellness-supplement-brand-niche.md` Top-10 that you haven't yet torn down; prioritize brands with engaged communities).

---

# SECTION 3: TEARDOWN CADENCE
## Building Proof, 1x/Week Minimum

The teardown is the keystone asset—it's content, portfolio, and lead-gen in one pass. Run this **weekly, every Monday or your preferred day.**

### Step 1: Prep (1 hr)
- Run `python3 execution/brand_radar.py` if your radar is >1 week old (pulls real recent posts + engagement for your target brand).
- Open `daily/brand-radar-YYYY-WW.md` and pick the brand you want to teardown this week (look for: 1) engaged community, 2) sameness pattern visible in recent feed, 3) founder/growth lead you can DM).
- Read their last 5–7 posts. Identify the sameness pattern (activity not angle, feature-as-benefit, category mimicry).

### Step 2: Build the Teardown (1.5–2 hrs)
Following `offers/teardown-system.md`, build the 6-part teardown:
1. **Credit first** — what they're doing well (reassure the human; they already feel behind).
2. **The sameness tell** — the one structural pattern causing them to blend in (named, specific, kind).
3. **The body-level truth** — the real reason their consumer acts at the nervous-system level (your 18yr edge; use `icp-emotional-map.md` §7).
4. **3 angles I'd ship** — concrete, true-before-scaled, compliance-aware. Each tied to consumer emotion, not feature.
5. **Compliance-safe note** — what's substantiable vs. warning-letter risk (your edge; builds trust).
6. **Close** — for the public post: recognition line. For the DM: "Want this on your last 30 days? That's the Angle Audit."

**Use the worked example in `teardown-system.md` (Gainful) as your template.**

### Step 3: Triple-Route (1 hr)
1. **Public proof post:** Post the principle/mechanism version to LinkedIn (generalize, don't name the brand directly in the opener; build the credibility in the text). This is your portfolio.
2. **Elite Magnet DM:** Send the full custom teardown to the brand's founder/growth lead. Subject: "Pulled apart your last 5 posts—here's the angle gap + 3 I'd ship. No pitch." (See `pipeline.md`—add the brand + stage to "dm'd").
3. **Proof Tracker entry:** Log the teardown to `proof-tracker.md` (date, type, brand, link, any result). This compounds the proof token library.

### Step 4: Wait & Tag (ongoing)
- When they reply to the DM, tag as "replied" in `pipeline.md` + move to discovery-call prep.
- If no reply after 5 days, comment on their next brand post (warm them again) before a follow-up DM.

**Cadence target: 1 named teardown/week = 4–5 warm leads/month into the discovery funnel.**

---

# SECTION 4: DISCOVERY CALL PLAYBOOK
## When They Say "Yes" (Different Questions Per Track)

You've warmed them via comments + sent the teardown. They reply or request a call. Now you qualify which track they're actually on.

### Opening Frame (Both Tracks)
*"Thanks for looking at the teardown. Just want to make sure I'm pitching the right thing. Let me ask a few things..."*

### ROLE TRACK Questions
Ask if they're hiring or thinking about hiring for their marketing/content team:
- **"Tell me about the role—what's the pain? Is this embedded (day-to-day in the trenches) or fractional (strategy + monthly direction)?"**
  - *Listening for:* budget, timeline, depth of involvement, how decision-making works on their team.
  - *Your pitch angle:* Position yourself as the fractional creative strategist who doesn't need onboarding (you've already read their brand via the teardown). "I can start Monday"—urgency + proof.
- **"What's your current content stack? Who owns strategy vs. execution?"** (Identifies your entry point and reporting line.)
- **"What does success look like in your first 90 days?"** (Scopes the role; lets you prove you can deliver it.)

### CLIENT TRACK Questions
Ask if they want to run a pilot before hiring someone:
- **"Walk me through your current content system and where it breaks."**
  - *Listening for:* pain points, what they've tried, why it failed, budget for solutions, decision speed.
  - *Your pitch angle:* "The Proof Run tests this in your actual feed in 7 days. You'll know if the angle shift works before we talk retainer."
- **"Who owns content decisions on your team? Is that person on this call?"** (Qualifies buyer vs. influencer.)
- **"If I showed you 8 posts + a VSL script in your brand voice by next Friday, would that move the needle?"** (Tests buy-in on speed + format.)

### Bridge Question (Both Tracks)
**"Before we go further—would it make sense to run a paid diagnostic (the Angle Audit) to nail the exact angle gaps, so when you do hire / when I build the proof run, we're all aligned?"**
- This introduces the Angle Audit ($500–1,500) as the risk-free next step.
- Upsells naturally from free teardown → paid audit → proof run/embed.
- Answers: "How serious are they?" + "Do they get the system?"

### Call Close (Both Tracks)
- **If warm:** "Let's run the Angle Audit this week. I'll spend 2–3 hours deep-diving your creative + the divergence fixes. We do a 30–45 min walkthrough. Then you know exactly what I'd build."
  - Send the Angle Audit proposal document same day. Make it easy to say yes (clear scope, clear price, clear timeline).
- **If not yet ready:** "I get it—no rush. I'll keep posting on your categories. Next time your team's talking about hiring or testing content, I'm a call away."
  - Add them to "warm, not-yet-ready" in `pipeline.md`. Re-engage via thoughtful comments 2x/month. They'll convert later (most role/client wins take 2–4 touches).

---

# SECTION 5: CONVERSION SEQUENCE
## Path to Revenue (Proof Run → Embed)

Both tracks follow the same ladder (per `OFFER-LADDER.md`). The fork is at the *positioning*, not the asset.

### Tier 0 → Tier 1: Teardown → Angle Audit
- **Teardown** (free Elite Magnet) = the discovery call opener.
- **Angle Audit** ($500–1,500, deliver in 3–5 days) = deep diagnostic of their creative + 3–5 divergence angles + 30–45 min walkthrough.
- **Win condition:** They say, "This is exactly right. Can you build these?"

### Tier 1 → Tier 2: Angle Audit → Proof Run
- **Proof Run** ($1,500–3,000, 7-day sprint) = 8 brand-voice posts + 1 VSL script, refund guarantee.
- **Positioning by track:**
  - **ROLE track:** "This is your audition. You'll see 8 posts in your feed that prove I can write *in* your voice, not *about* your brand. This is what 90 days looks like."
  - **CLIENT track:** "This proves the angle shift works in your feed before you commit to a retainer. If it doesn't sound like your brand, you get your money back."
- **Win condition:** They ship it. Results flow in (engagement, DMs from customers, internal team buy-in).

### Tier 2 → Tier 3: Proof Run → Embed
- **Embed** ($4–9K/mo fractional seat OR project retainer) = ongoing creative strategy, angle development, content system, methodology install.
- **ROLE track conversion:** 40–50% of proof runs convert to fractional seats ($4–9K/mo, day-to-day embedded or 2x/week strategic advisor).
  - Pitch: "Your brand voice is now in my engine. I can scale this without you having to reinvent strategy every week."
  - First 90 days: collaborative (they're shadowing, learning the system); months 4+ = you operate with less input (they trust the process).
- **CLIENT track conversion:** 40–50% of proof runs convert to 3–12 month retainers ($4–9K/mo) or ongoing project engagements.
  - Pitch: "We've proven the angle shift works. Now let's install it across your full funnel (social, email, website copy, ads)."
  - Scope: monthly strategy calls + 4–6 pieces/month + angle library maintenance + brand-POV coaching.

### Revenue Math (Year 1 Target)
- **Month 1–2:** 1–2 Angle Audits → 0–1 Proof Runs ($500–3K revenue)
- **Month 3–4:** 2–3 Angle Audits → 1–2 Proof Runs → 1 Embed signed ($3–15K revenue)
- **Month 5–12:** 3–5 Proof Runs/mo → 2–4 new Embeds/mo → compounding retainer base ($8–15K/mo by month 6+)

**Acquisition cost:** $0 (organic content + teardowns). **Gross margin:** 85%+ (you're the service).

---

# SECTION 6: WEEKLY TASK CHECKLIST

## Every Monday (or your weekly anchor day)
- [ ] Publish teardown (public post + Elite Magnet DM). Log to `pipeline.md` (brand, stage) + `proof-tracker.md` (date, link).
- [ ] Scan `performance-log.md` + LinkedIn notifications for decision-maker signal. Tag any new "warmed" leads.
- [ ] Update `pipeline.md`: move leads by stage. Flag any "dm'd" that need a 5-day warm-up comment.
- [ ] Read `_active/linkedin-launch/MASTER-STRATEGY.md`. Confirm beachhead/lane is still the priority. If drift → run `repoint`.

## Daily (Mon–Fri)
- [ ] Post 1x via `/linkedin-daily` (9–10am ET).
- [ ] Spend 30–45 min on 10 substantive comments (5 brand accounts, 5 category voices).
- [ ] End-of-day: scan signal, tag new leads, update `pipeline.md`.

## When a Lead Replies to Teardown DM
- [ ] Respond within 24hr with discovery-call frame (see Section 4). Offer two time slots for call.
- [ ] Before the call: if ROLE track, review their team/hiring; if CLIENT track, review their current content stack.
- [ ] After the call: send Angle Audit proposal same day (clear scope, price, timeline). Make it a no-brainer.

## When Angle Audit is Purchased
- [ ] Deliver in 3–5 days (tight diagnostic + 30–45 min walkthrough call).
- [ ] Close the call with: "Want to run the Proof Run and test these in your feed?"
- [ ] Send Proof Run proposal immediately if they're warm.

## When Proof Run is Shipped
- [ ] Log outcome to `proof-tracker.md` (date, brand, tier, $, result delta if available).
- [ ] Track engagement (engagement rate, DMs, comments). Log to proof-tracker after 7–14 days.
- [ ] Pitch the Embed: "We've got proof. Now let's build the system." Send Embed proposal.

---

# SECTION 7: KPI TRACKER STUB

## Weekly Snapshot (Copy This Into a Google Sheet or `performance-log.md`)

```
WEEK OF: [DATE]

SIGNAL METRICS (Priority Order)
- Decision-maker profile views this week: ___
  Names: ___
- Decision-maker saves this week: ___
  Names: ___
- Substantive comments from decision-makers: ___
  Names: ___
- Connection requests from decision-makers: ___
  Names: ___
- Teardown DM replies this week: ___
  Names: ___

ACTIVITY METRICS
- Posts published: ___
- Comments made: ___
- Teardowns delivered: ___
- Discovery calls booked: ___
- Angle Audits sold: ___
- Proof Runs sold: ___
- Embeds signed: ___

REVENUE THIS WEEK
- Angle Audits revenue: $___
- Proof Run revenue: $___
- Embed MRR (cumulative): $___
- Weekly total: $___

PIPELINE MOVEMENT
- Leads moved to "warmed" this week: ___
- Leads moved to "dm'd" this week: ___
- Leads moved to "replied" this week: ___
- Leads moved to "call booked": ___
- Leads closed (audit/proof/embed): ___

NOTES / BLOCKERS
- What worked this week: ___
- What didn't: ___
- Next week's focus: ___
```

## Month 1–3 Target
| Metric | Month 1 | Month 2 | Month 3 |
|--------|---------|---------|---------|
| Decision-maker profile views | 10–15 | 20–30 | 40–50 |
| Substantive comments from ICP | 2–3 | 5–8 | 10–15 |
| Teardowns delivered | 2–3 | 4–5 | 5–6 |
| Discovery calls booked | 0–1 | 2–3 | 4–6 |
| Angle Audits sold | 0–1 | 1–2 | 2–4 |
| Proof Runs sold | 0 | 0–1 | 1–2 |
| Embeds signed | 0 | 0 | 1–2 |
| Revenue | $0–500 | $500–4K | $4–12K |

---

# REFERENCE DOCUMENTS
- `MASTER-STRATEGY.md` — beachhead, ICP, lane mix, KPI definitions
- `OFFER-LADDER.md` — tier definitions, pricing, positioning per track
- `teardown-system.md` — worked example (Gainful) + 6-part template
- `icp-emotional-map.md` — body-level consumer truth (your 18yr edge)
- `research/wellness-supplement-brand-niche.md` — target brand list + buyer psychology
- `pipeline.md` — live lead tracker (human-tagged only)
- `proof-tracker.md` — real outcomes (published teardowns + paid work results)
- `performance-log.md` — daily engagement snapshot (posts, comments, signal)
- `offers/client-onboarding-sop.md` — onboarding playbook for new clients
- `skills/client-acquire/` + `skills/linkedin-cs-outreach/` — outreach + qualification templates (optional depth layer)
