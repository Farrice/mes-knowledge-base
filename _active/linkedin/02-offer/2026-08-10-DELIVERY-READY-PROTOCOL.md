---
date: 2026-08-10
mission: delivery-protocol
status: TEMPLATE_READY
owner: Farrice Cain
---

# Delivery Ready Protocol — $750 Angle Map Fulfillment

**Trigger:** Payment clears (confirmed by Stripe webhook or manual check)  
**Timeline:** Deliver within 48 hours of cleared payment (per offer language)  
**Deliverable:** 60-minute read + three campaign angles + written recommendations  
**Formats available:** [Choose one per your preference below]

---

## Payment Received Workflow

### Step 1: Confirm Payment (Immediate — <5 min)

1. **Check Stripe dashboard** or payment confirmation email
2. **Verify amount:** $750.00 USD
3. **Verify customer:** Confirm buyer name + email match prospect from pipeline
4. **Log in CASH-SCOREBOARD:** Move prospect to "collected" stage with date/amount
5. **Log in revenue tracker:** Run the command from `CASH-SCOREBOARD-2026-07-29.md` (System Logging section)

### Step 2: Send Delivery Confirmation (Within 2 hours)

**Email to buyer** (template):

```
Subject: Angle Map Ready — [Brand Name] Campaign Read

[Buyer first name],

Payment received for your 60-minute Angle Map read. Thanks.

I've finished my analysis of [Brand Name]'s messaging positioning and the campaigns running now. 

Here's what I'm seeing:
1. [Angle 1 headline — one sentence]
2. [Angle 2 headline — one sentence]
3. [Angle 3 headline — one sentence]

Let me show you the reasoning. [Choose delivery format below.]

— Farrice
```

### Step 3: Schedule Delivery (48-hour window)

**Choose one delivery format (lock this now so it's clear to buyer):**

---

## Delivery Format Options

### OPTION A: Live 60-Minute Call (Primary)

**Setup:**
1. Send Calendly link with 5 available 60-min slots within next 48 hours
   - (Or use your preferred scheduling tool)
   - Block it as "paid event" so buyer knows it's confirmed
2. Email: "Pick a slot that works for your timezone. I'll have the three angles + recommendations ready to walk through."
3. Prep: Have browser open with your brief + angle notes during call

**Delivery on call:**
- **0–5 min:** Quick context reset ("here's what I read")
- **5–20 min:** Angle 1 deep dive (why it matters, how to build it, proof points)
- **20–35 min:** Angle 2 deep dive
- **35–50 min:** Angle 3 deep dive
- **50–60 min:** Written recommendations summary (send during or right after)

**Send after call:**
- Written brief (Google Doc or PDF) with angles + recommendations + supporting data
- File naming: `[Brand Slug]_AngleMap_[Date]_[Angle1]_[Angle2]_[Angle3].pdf`

**Advantages:** Live allows real-time questions, full context transfer, relationship building  
**Risk:** Timezone/scheduling complexity; if they bail, pivot to async (Loom)

---

### OPTION B: Recorded Video Brief (Async Fallback)

**If buyer declines live call or timezone doesn't work:**

1. Record a 60-minute Loom video:
   - Screencast your brief or document
   - Talk through all three angles
   - Pause for emphasis, not for interaction
   - Aim for conversational tone (not stiff presentation)

2. Edit for length (aim for 55–65 min actual recorded)

3. Send Loom link + written brief + recommendations doc

**Advantages:** Buyer can watch on their schedule; you work once, they consume once  
**Risk:** No real-time Q&A; may feel less premium than live

---

### OPTION C: Written Brief + Optional Call (Premium)

**Best for:** Buyers who prefer reading + selective deep dives

1. Write a comprehensive brief (3–5 pages):
   - Executive summary
   - Category landscape (2–3 paragraphs)
   - Three angles (with proof for each)
   - Recommendations (2–3 specific actions per angle)
   - Appendix (data sources, evidence)

2. Send as PDF + offer 30-min optional call for questions

**Advantages:** Highest-polish deliverable; clear takeaways in writing  
**Risk:** Lower relationship activation if they don't take the call

---

## Decision Tree: Which Format to Use

```
Does buyer confirm live availability within 48 hours?
  → YES: Use OPTION A (Live Call)
  → NO: Does buyer prefer async?
    → YES: Use OPTION B (Loom Video)
    → NO: Use OPTION C (Written Brief)
  → UNCLEAR: Offer A + B ("Live is better; if that doesn't work, I'll record it")
```

---

## Files to Prepare (Before Delivery)

### Your Angle Map Brief Template

Create one master document for each prospect with:

```
# [Brand Name] — Angle Map Analysis

## 1. SITUATION
[2–3 paragraphs on the brand, their position, their current messaging]

## 2. THE THREE ANGLES

### Angle 1: [Headline]
**Why it matters:** [1–2 sentences on why this is the gap]
**How to build it:** [3–5 bullets on the proof / mechanism / execution]
**Proof points:** [2–3 concrete examples from the category or their own data]

### Angle 2: [Headline]
[Same structure]

### Angle 3: [Headline]
[Same structure]

## 3. RECOMMENDATIONS
[3–5 bullets on first moves per angle]

## 4. EVIDENCE
[Links + quotes + sourcing]
```

**Timing:** Complete this before the call/recording (prep = 30–45 min per brand)

---

## Post-Delivery Logging

### Update CASH-SCOREBOARD
- Move prospect to "delivered" stage with delivery date
- Note delivery format used (live / async / written)
- If delivered, flag for proof permission request if applicable

### Update Pipeline
- Move prospect to "delivered" stage
- Note delivery date + format
- Set "next action" to "follow-up (Day 5–7)" if building to Sprint upsell

### Capture Proof (Important)
- Ask buyer: "Can I use this work as a case study / reference example?" (for Source Registry)
- If yes: request permission + plan to document the outcome later
- File in `02-offer/case-studies/[brand-slug]/` once delivered

---

## Next Actions After Delivery

### Day 2–3 After Delivery
- Check for feedback / questions
- Offer revision or deep dive if needed (included in $750)

### Day 5–7 After Delivery
- If delivery went well: Send Sprint upsell ($2,500, 10-day intensive campaign build)
- If questions came up: Address first, then mention Sprint

### Day 10–14
- Request case study permission + brief feedback
- Update CASH-SCOREBOARD with outcome (accepted angles? next steps? interest in Sprint?)

---

## Success Definition

**Angle Map delivery = COMPLETE when:**
- [ ] Payment logged in CASH-SCOREBOARD + revenue tracker
- [ ] Buyer received three angles + written recommendations within 48 hours
- [ ] Buyer understood the analysis (no urgent clarification needed)
- [ ] Case study permission requested (even if declined)
- [ ] Outcome tracked for next offer decision

---

## Contingency: Issues During Delivery

### If buyer requests revision on one angle
- **Included in $750:** One revision per angle (up to 2 replacements total)
- **Send within 24 hours of request**
- **Note in CASH-SCOREBOARD:** "1 revision requested + delivered"

### If buyer wants to extend to full call
- **Offer:** "Let's do a follow-up 30-min focused on implementation" (no extra charge)
- **Set expectations:** This moves toward Sprint territory (deeper 10-day build)

### If buyer ghosts after payment
- **Day 3 check-in:** Light email "Just confirming — did the brief land in your inbox?"
- **Day 5:** Assume delivery received; move to "delivered" stage even without confirmation
- **Do not pursue further unless they reply**

---

**Delivery protocol is locked. Choose your preferred format above, update this doc, commit, and you're ready to fulfill.**
