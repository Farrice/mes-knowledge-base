---
date: 2026-08-08
mission: "Campaign Day 1 Launch — Payment Unblock + First 5 Sends"
status: READY_TO_EXECUTE
owner: "Farrice Cain"
---

# Campaign Day 1 Execution Brief

**Goal:** Launch the 14-day clock with 5 verified DMs sent and logged.  
**Current state:** 5 DMs finalized, prospects verified, payment link is the only blocker.  
**Timeline:** 20 minutes (payment setup + sends).  

---

## Phase 1: Payment Link Setup (10 minutes)

**Status:** ⚠️ NOT YET CREATED

**Action:** Create a Stripe Checkout payment link for the $750 Angle Map.

### Quick Setup Path (Recommended)

1. **Go to Stripe** (stripe.com)
   - Sign up if needed (email + password)
   - Verify email
   - Complete basic onboarding (business info)

2. **Create Payment Link**
   - Dashboard → "Payment Links" (left sidebar)
   - Click "+ New"
   - Fill in:
     - **Product name:** "The Angle Map: Campaign Analysis + 3 Angles"
     - **Description:** "60-minute live read on your campaign, three tailored angles for your buyer, written recommendations"
     - **Price:** $750.00
     - **Quantity:** Fixed (1)
   - Checkout settings: Require email ✓, No promo codes
   - Click "Create link"

3. **Test the Link**
   - Copy the generated link (starts with `stripe.com/pay/`)
   - Open in incognito window
   - Confirm checkout page loads and shows $750
   - Do NOT complete payment (test card: `4242 4242 4242 4242` if needed)

4. **Add to Mission 2b**
   - Open `2026-07-31-MISSION-2B-SEND-READINESS.md`
   - Find the `[PLACEHOLDER — Replace with verified live link...]` section
   - Replace with your live Stripe link
   - Mark verification checklist ✓

**Time estimate:** 10 minutes  
**Blocker risk:** None (Stripe signup is instant, link creation is automatic)

---

## Phase 2: Execute 5 Verified DMs + Log (10 minutes)

**Status:** ✅ READY (5 DMs finalized, prospects verified)

Once payment link is added to mission-2b file:

### The 5 Prospects (Verified Current)

1. **Tim Near** — GateDrop (nutrition tracking SaaS, 5K followers)  
   Link: `linkedin.com/in/timnear`  
   One-gap: "You're building toward [supplement brand partnerships], but I see the angle that actually converts with their buyer is [founder voice vs agency copy]. Here's why..."

2. **Daniel Adix** — LiQure (hydration supplement brand, 8K followers)  
   Link: `linkedin.com/in/danieladix`  
   One-gap: Same founder-voice-vs-agency angle

3. **Yasir Hashim** — Lumen (metabolic optimization device, 12K followers)  
   Link: `linkedin.com/in/yasir-hashim`  
   One-gap: Same angle, different product category

4. **Ivan Tsvilik** — True Sea Moss (sea moss supplement brand, 3K followers)  
   Link: `linkedin.com/in/ivan-tsvilik`  
   One-gap: Same angle

5. **Thomas Eddleston** — FABRIC (performance supplement brand, 6K followers)  
   Link: `linkedin.com/in/thomaseddleston`  
   One-gap: Same angle

### Send Process

**For each prospect:**

1. Go to their LinkedIn profile
2. Click "Message" or "Connect" → (if connect, wait for acceptance, then message)
3. Copy the relevant one-gap DM from `2026-07-31-MISSION-2B-SEND-READINESS.md` (Part B)
4. Paste into DM
5. Add payment link at the end: `Payment: [your Stripe link]`
6. Send
7. **Log it immediately** in the pipeline:
   - Open `pipeline.md`
   - Add a row under "**SENT**" with:
     - Prospect name
     - Date sent (today's date)
     - DM subject (e.g., "Founder voice vs agency")
     - Payment link (for their reference)
     - Status: "SENT — awaiting response"

**Send order:** No preference; do all 5 in one sitting so clock starts same time.

**Time estimate:** 10 minutes (2 min per send + log)

---

## Phase 3: Clock Activation + Checkpoint Schedule

**Once all 5 DMs are sent and logged:**

1. **Update CASH-SCOREBOARD**
   - Open `CASH-SCOREBOARD-2026-07-29.md`
   - Clock start date: TODAY (2026-08-08)
   - Clock end date: 2026-08-22 (14 days)
   - 5 prospects sent ✓

2. **Checkpoint Schedule (Auto-Populated)**
   - **Day 3 (2026-08-11):** Check for responses; follow up if silent
   - **Day 7 (2026-08-15):** Review sent/held/sold/collected; refresh research if needed
   - **Day 10 (2026-08-18):** Final push; make-right offer available for any objections
   - **Day 14 (2026-08-22):** Final day; flag any collected payments, summarize results

---

## State After Execution

| Metric | Current | After Day 1 |
|--------|---------|------------|
| **Sent** | 0 | 5 |
| **Held** | 0 | TBD |
| **Sold** | 0 | TBD |
| **Collected** | $0 | TBD |
| **Clock Status** | Waiting | ACTIVE (14 days) |
| **Next Review** | N/A | Day 3 (2026-08-11) |

---

## Contingency Notes

- **No responses by Day 3:** Send light follow-up ("checking in, any questions about the angles?")
- **Objection on price:** Use make-right offer ($500 pilot + second angle free if issues found)
- **Payment link breaks:** Recreate immediately; resend link only to affected prospects
- **Scheduling conflict:** Offer async 60-min read (Loom video instead of live call)

---

## Files to Update (Post-Execution)

1. ✓ `2026-07-31-MISSION-2B-SEND-READINESS.md` — Add payment link
2. ✓ `pipeline.md` — Add 5 sends to "SENT" section
3. ✓ `CASH-SCOREBOARD-2026-07-29.md` — Clock start date + end date
4. ✓ `CAMPAIGN.md` — Update mission 2b status to ✅ DONE (clock running) + update log

---

## Success Definition

**Campaign Day 1 = COMPLETE when:**
- [ ] Payment link created and tested
- [ ] 5 DMs sent and logged in pipeline
- [ ] CASH-SCOREBOARD shows clock start date
- [ ] Files committed to main with message: "Campaign Day 1: payment link live + 5 first-wave DMs sent; clock running"

**Stretch goal:** One response + interest in call by EOD (unlikely but possible if early timezone respondents).

---

**Ready when you are. Once payment link is live, all downstream mechanics are automated (checkpoints, scoreboard, follow-up prompts).**
