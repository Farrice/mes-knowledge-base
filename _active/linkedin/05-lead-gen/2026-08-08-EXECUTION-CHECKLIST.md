# Campaign Day 1 — 20-Minute Execution Checklist

**Goal:** 5 sends logged = 14-day clock running  
**Time:** ~20 minutes (payment 10m + sends 10m)  
**Status:** All copy ready, payment link is only blocker

---

## ✅ PHASE 1: PAYMENT SETUP (10 min)

### Step 1: Create Stripe Link

- Go to [stripe.com](https://stripe.com)
- Sign up or log in
- Click **Payment Links** (left sidebar)
- Click **+ New**
- Fill:
  - **Name:** `The Angle Map: Campaign Analysis + 3 Angles`
  - **Description:** `60-minute live read on your campaign, three tailored angles for your buyer, written recommendations`
  - **Price:** `750.00`
  - **Quantity:** `Fixed (1)`
- Click **Create link**
- Copy the link (starts with `stripe.com/pay/...`)

### Step 2: Test the Link

- Open link in **incognito window**
- Confirm `$750.00` shows
- Do NOT complete (test card OK if prompted: `4242 4242 4242 4242`)

### Step 3: Update Mission 2b

- Open `/2026-07-31-MISSION-2B-SEND-READINESS.md`
- Find section: `$750 ANGLE MAP PAYMENT LINK:`
- Replace `[PLACEHOLDER — Replace with verified live link before first DM]` with your Stripe link
- Check the verification box ✓

---

## ✅ PHASE 2: EXECUTE 5 SENDS (10 min)

**Copy/paste ready below. Send all 5 in one sitting.**

### Send #1 — Tim Near (GateDrop)

**To:** [linkedin.com/in/timnear](https://linkedin.com/in/timnear)

**Copy:**

```
Tim, I saw GateDrop expanding in Utah and the Northeast, described as "built for people in motion."

The gap I see is that the message now has to welcome a much broader convenience-store buyer without sanding off the literal gate-drop moment that makes the brand recognizable.

That choice gets harder as the retail footprint moves beyond the original action-sports context, and you have maybe 60 days to own it in-store.

I've profiled three angles that work here — want me to walk through them?

Payment: [YOUR STRIPE LINK]
```

**Action:**
- [ ] Go to Tim's profile, click Message
- [ ] Paste above (customize Payment link)
- [ ] Send
- [ ] Log below

---

### Send #2 — Daniel Adix (LiQure)

**To:** [linkedin.com/in/danieladix](https://linkedin.com/in/danieladix)

**Copy:**

```
Daniel, I saw LiQure's reformulation and return to retail in June.

The gap I notice is your messaging is still positioned to the category decision-maker (hydration buyer), but retail shelf placement just moved you into "choice" territory where the actual buyer is making an impulse call.

Your founder voice + product positioning are built for deeper understanding. The shelf doesn't give you that room.

I have three angles that flip this — want to see them?

Payment: [YOUR STRIPE LINK]
```

**Action:**
- [ ] Go to Daniel's profile, click Message
- [ ] Paste above (customize Payment link)
- [ ] Send
- [ ] Log below

---

### Send #3 — Yasir Hashim (Lumen)

**To:** [linkedin.com/in/yasir-hashim-31a41713a](https://linkedin.com/in/yasir-hashim-31a41713a)

**Copy:**

```
Yasir, I saw Lumen's nationwide Sprouts launch this summer.

The gap I see: you're positioned as "the metabolic optimization device" to people who already know they want metabolic optimization. But Sprouts' buyer is still in "should I care about this" mode.

Sprouts shelf presence is your credibility move — use it as proof, not positioning.

I've mapped three angles that own this. Worth 60 minutes?

Payment: [YOUR STRIPE LINK]
```

**Action:**
- [ ] Go to Yasir's profile, click Message
- [ ] Paste above (customize Payment link)
- [ ] Send
- [ ] Log below

---

### Send #4 — Ivan Tsvilik (True Sea Moss)

**To:** [linkedin.com/in/ivantsvilik](https://linkedin.com/in/ivantsvilik)

**Copy:**

```
Ivan, I saw True Sea Moss launch at Whole Foods.

The gap: sea moss is hitting mainstream retail for the first time, and your customer is brand-new to the category. But your messaging assumes they already know why sea moss matters.

Whole Foods placement is your permission structure. Lead with that.

I have three angles built on this logic. Interested?

Payment: [YOUR STRIPE LINK]
```

**Action:**
- [ ] Go to Ivan's profile, click Message
- [ ] Paste above (customize Payment link)
- [ ] Send
- [ ] Log below

---

### Send #5 — Thomas Eddleston (FABRIC)

**To:** [linkedin.com/in/thomas-eddleston](https://linkedin.com/in/thomas-eddleston)

**Copy:**

```
Thomas, I saw FABRIC's Zero launch this spring.

The gap I notice: hop water is category-new (most buyers don't know it exists), but your messaging treats it as a known choice with a better formula.

Your founder voice is built for teaching. Your retail placement proves credibility. But you're not using the teaching move.

I mapped three angles around this. Want to see them?

Payment: [YOUR STRIPE LINK]
```

**Action:**
- [ ] Go to Thomas's profile, click Message
- [ ] Paste above (customize Payment link)
- [ ] Send
- [ ] Log below

---

## ✅ PHASE 3: LOG & ACTIVATE (2 min)

### Update Pipeline

Open `/pipeline.md`. In the **Active pipeline** table, update each row:

| Prospect | Sent | Reply | Held | Status update |
|---|---|---|---|---|
| Tim Near — GateDrop | ✓ [TODAY] | — | — | `SENT — awaiting response` |
| Daniel Adix — LiQure | ✓ [TODAY] | — | — | `SENT — awaiting response` |
| Yasir Hashim — Lumen | ✓ [TODAY] | — | — | `SENT — awaiting response` |
| Ivan Tsvilik — True Sea Moss | ✓ [TODAY] | — | — | `SENT — awaiting response` |
| Thomas Eddleston — FABRIC | ✓ [TODAY] | — | — | `SENT — awaiting response` |

### Update CASH-SCOREBOARD

Open `/CASH-SCOREBOARD-2026-07-29.md`. Update:

```
- **Clock start:** 2026-08-08
- **Clock end:** 2026-08-22 (14 days)
- **First 5 prospects sent:** ✓ 5/5
- **Current status:** Active (day 1 of 14)
```

### Update CAMPAIGN.md

Open `/CAMPAIGN.md`. Find mission 2b row. Update:

```
| 2b | External activation: send first 5 verified one-gap DMs... | ✅ DONE 08-08 → CLOCK RUNNING | ... |
```

Add log entry at end:

```
- 2026-08-08 (morning): **Campaign Day 1 EXECUTION COMPLETE.** Payment link created, 5 one-gap DMs sent to verified prospects (Tim Near/GateDrop, Daniel Adix/LiQure, Yasir Hashim/Lumen, Ivan Tsvilik/True Sea Moss, Thomas Eddleston/FABRIC). All sends logged in pipeline. CASH-SCOREBOARD activated with 14-day clock (end 2026-08-22). Next checkpoint: Day 3 (2026-08-11) for response check.
```

---

## COMMIT

```bash
git add -A
git commit -m "Campaign Day 1: payment link live + 5 first-wave DMs sent; 14-day clock running

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
git push
```

---

## Success Criteria

- [ ] Stripe link created and tested
- [ ] 5 DMs sent (check LinkedIn message history)
- [ ] All 5 logged in pipeline.md
- [ ] CASH-SCOREBOARD shows clock running
- [ ] CAMPAIGN.md updated with completion log
- [ ] Committed and pushed to main

**Status:** Ready to execute. Once payment link is live, all mechanics are go.
