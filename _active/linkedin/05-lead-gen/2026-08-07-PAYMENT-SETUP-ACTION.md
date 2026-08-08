---
mission: 2b-setup
date: 2026-08-07
status: in-progress
---

# Payment Setup for $750 Angle Map — Immediate Actions

**Current state:** 5 DMs finalized, verified prospects ready, payment link is the ONLY blocker to sending.  
**Goal:** Create verified $750 payment URL and update mission-2b file.  
**Timeline:** 15 minutes to set up + test.

---

## OPTION A: Stripe Checkout (Recommended — 10 min setup)

**If you don't have Stripe yet:**
1. Go to [stripe.com](https://stripe.com) → Sign up (2 min, email + password)
2. Verify your email (1 min)
3. Complete onboarding (2–3 min, basic business info)

**To create your payment link:**

```
1. Log into Stripe Dashboard (dashboard.stripe.com)
2. Left sidebar → "Payment Links" (or search for it)
3. Click "+ New"
4. Fill in:
   - Product name: "The Angle Map: 60-Minute Live Read"
   - Description: "60-minute live campaign analysis + 3 actionable angles tailored to your market"
   - Price: $750.00 (USD)
   - Quantity: Fixed (1)
5. Under "Checkout settings":
   - Require email: YES (so you know who paid)
   - Allow promotion codes: NO
6. Click "Create link"
7. Copy the link (starts with stripe.com/pay/)
```

**Test it:**
- Open the link in an incognito window
- Click through to see the checkout form
- Do NOT complete payment (use a test card if needed: `4242 4242 4242 4242` with any future exp/CVC)
- Confirm the page loads and the amount shows $750

**Add the link to mission-2b file** (see below)

---

## OPTION B: Square Invoices (Alternative — 8 min if you have Square)

```
1. Log into Square (squareup.com)
2. Go to "Invoices"
3. Click "+ New invoice"
4. Customer: [leave blank for now]
5. Line item:
   - Description: "The Angle Map — 60-minute read + 3 angles"
   - Amount: $750.00
6. Terms: Due immediately
7. Save & send
8. Copy the payment link (share button → copy link)
```

---

## OPTION C: Calendly + Stripe (If you already use Calendly)

```
1. Log into Calendly
2. Go to your 60-minute event (create if needed)
3. Settings → Payment → Connect Stripe account
4. Set one-time fee: $750
5. Turn on "Require payment before booking"
6. Copy the event link (this now includes payment)
```

---

## UPDATE mission-2b FILE

Once you have a tested, verified link:

**File:** `05-lead-gen/2026-07-31-MISSION-2B-SEND-READINESS.md`

**Find this section (around line 61):**
```
**$750 ANGLE MAP PAYMENT LINK:**
```
[PLACEHOLDER — Replace with verified live link before first DM]
```

**Replace with:**
```
**$750 ANGLE MAP PAYMENT LINK:**
[YOUR-STRIPE-OR-SQUARE-URL-HERE]
```

**Check off the verification boxes:**
- [x] Link is tested and accepts payment
- [x] Confirmation email works
- [x] No test/sandbox mode active
- [x] Link is current and not expired

---

## WHAT HAPPENS NEXT

Once the link is live and mission-2b is updated:

1. **Copy DM #1 text** (line 95–100) → Paste into LinkedIn DM to Tim Near
2. **Log it** in `05-lead-gen/pipeline.md` (change Tim's stage to `dm'd` with date/time)
3. **Log in cash scoreboard** (`05-lead-gen/CASH-SCOREBOARD-2026-07-29.md`)
4. **Repeat for 5 total** (Tim, Daniel, Yasir, Ivan, Thomas)
5. **Once all 5 logged:** The 14-day clock starts

---

## Cost & Notes

- **Stripe:** Free to set up, 2.9% + $0.30 per transaction (so ~$2.48 per $750 sale)
- **Square:** Similar (2.9% + $0.30)
- **Calendly + Stripe:** Same Stripe fees, but bundled with scheduling

**This unblocks the entire campaign.** Once the 5 DMs are sent, the carousels (#4, #5, #6) can follow the 72-hour post-DM rule, and you're running a real money test with verified buyer demand.

No further system work is needed—this is purely a 15-minute external setup → paste-the-link → go step.
