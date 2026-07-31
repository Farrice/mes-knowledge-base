---
status: canonical
date_prepared: 2026-07-31
mission: 2b
---

# First-Wave Send-Ready Packet

**Goal:** Send five qualified one-gap DMs and log them. Day 1 clock starts when the first five reach the inbox.

**Infrastructure blocker:** The $750 payment URL must exist before you send the second message to any prospect. Do not send Message 2 (which quotes the price) until the payment link is live and verified.

## Five send-ready messages

Copy-paste each into a LinkedIn DM. Verify the buyer's name, profile URL, and the trigger source one final time before hitting send.

---

### 1. Tim Near — GateDrop
**Profile:** https://www.linkedin.com/in/timnear  
**Trigger:** [GateDrop distribution announcement, June 30, 2026](https://www.bevnet.com/pr/2026/06/30/gatedrop-accelerates-retail-expansion-with-broader-distribution-wins)

**Message:**

> Tim, GateDrop is expanding in Utah and the Northeast while describing itself as "built for people in motion."
> The message now has to welcome a much broader convenience-store buyer without sanding off the literal gate-drop moment that makes the brand recognizable.
> That choice gets harder as the retail footprint moves beyond the original action-sports context.
> If useful, I can send the one-paragraph read.

**Log action after send:**
- Change row in `pipeline.md` to `dm'd` (Stage column)
- Record: Date sent, variant 1 (Tim Near example)

---

### 2. Daniel Adix — LiQure
**Profile:** https://www.linkedin.com/in/danieladix  
**Trigger:** [LiQure reformulation and retail return, June 9, 2026](https://www.bevnet.com/pr/2026/06/09/liqure-launches-berry-spritz-a-new-flavor-enhanced-formula-and-expanded-retail-presence-backed-by-fresh-investment)

**Message:**

> Daniel, Berry Spritz is back with new packaging and the line that it is "closer to a premium vitamin gummy than a supplement."
> The unresolved choice is whether drinking-recovery science or the premium lifestyle ritual leads the relaunch.
> With fresh investment and retail back in motion, that hierarchy will shape every campaign angle.
> I can send the short read if you want it.

**Log action after send:**
- Change row in `pipeline.md` to `dm'd`
- Record: Date sent, variant 2 (Daniel Adix example)

---

### 3. Yasir Hashim — Lumen
**Profile:** https://www.linkedin.com/in/yasir-hashim-31a41713a  
**Trigger:** [Lumen nationwide Sprouts launch, July 7, 2026](https://www.bevnet.com/pr/2026/07/07/lumen-launches-nationwide-at-sprouts-debuting-exclusive-cocolada-flavor-of-its-awardwinning-sparkling-protein-drinks)

**Message:**

> Yasir, the Sprouts announcement puts Lumen "at the gym, at your desk, or on the go" from morning through night.
> Clear protein is a sharp format difference, but the consumption occasion is deliberately broad.
> At shelf, one memorable non-shake moment may need to organize the others.
> If that decision is live, I can send the short read.

**Log action after send:**
- Change row in `pipeline.md` to `dm'd`
- Record: Date sent, variant 3 (Yasir Hashim example)

---

### 4. Thomas Eddleston — FABRIC
**Profile:** https://www.linkedin.com/in/thomas-eddleston  
**Trigger:** [FABRIC Zero launch, May 11, 2026](https://www.bevnet.com/pr/2026/05/11/fabric-launches-zero-a-nonalcoholic-hop-water-built-on-function-without-the-nonsense)

**Message:**

> Thomas, Zero has a clean thesis in "function without the nonsense."
> The launch still places it in coffee pairings, afternoon resets, post-work wind-downs, and social settings.
> The functional argument is sharp; the open decision is which occasion makes it memorable first.
> I can send the one-paragraph read if that choice is live.

**Log action after send:**
- Change row in `pipeline.md` to `dm'd`
- Record: Date sent, variant 4 (Thomas Eddleston example)

---

### 5. Ivan Tsvilik — True Sea Moss
**Profile:** https://www.linkedin.com/in/ivantsvilik  
**Trigger:** [True Sea Moss Whole Foods launch, April 22, 2026](https://www.prnewswire.com/news-releases/true-sea-moss-expands-retail-presence-with-launch-at-whole-foods-market-stores-302750726.html)

**Message:**

> Ivan, the Whole Foods announcement aims to make sea moss "a seamless part of the modern lifestyle."
> The ingredient is distinctive, but a new shelf buyer still has to decide when and how the jar enters the day.
> A sharper first-use ritual could make the story easier to act on without inflating the health promise.
> If useful, I can send the short read.

**Log action after send:**
- Change row in `pipeline.md` to `dm'd`
- Record: Date sent, variant 5 (Ivan Tsvilik example)

---

## Payment URL decision

**Current state:** Blocked — no payment link exists yet.

**What you need before second touch:**
- A working $750 payment link (Stripe, Gumroad, invoice URL, or equivalent)
- A verified test of the link from a different account to confirm it resolves and works
- The link URL ready to paste into Message 2

**Message 2 template (send only after first reply OR as Day 2 follow-up if unanswered):**

> The short read is this: [two-sentence interpretation].
> If you want the decision made rather than another loose opinion, I do that through **The Angle Map**.
> It includes a 60-minute live read and three campaign angles, with hooks, approved-proof direction, and an editorial claim-safety line for each.
> It is **$750 prepaid and delivered within 48 hours**. Worth seeing the exact scope?
>
> [After confirmation, send: *Here's the payment link and scope document. Once payment and the approved inputs are in, the 48-hour clock starts.*]

**Quick wins to unblock this:**
1. **Stripe:** 10 min to create account, 5 min to set a $750 payment link (fastest path if you don't already have a Stripe account).
2. **Gumroad:** 5 min to set a $750 one-time product link.
3. **Invoice fallback:** If neither works, you can send a PayPal invoice or manual payment request after the buyer says yes.

**Rule:** Do not send Message 2 or quote the price until the payment link is live and you've tested it yourself.

---

## Logging summary

After each send, update `pipeline.md`:
- Change the prospect's **Stage** from `contact verified` to `dm'd`
- Add the date and variant used

After all five sends are complete:
1. Update `CASH-SCOREBOARD-2026-07-29.md` row 1 under "New sent" to `5`
2. Update the "Notes" column with the calendar date (Day 1 begins when the first five DMs reach the inbox)
3. Commit and push

---

## One final check before sending

Before you copy the first message, verify:

- [ ] Tim Near's profile is still live at https://www.linkedin.com/in/timnear
- [ ] Daniel Adix's profile is still live at https://www.linkedin.com/in/danieladix
- [ ] Yasir Hashim's profile is still live at https://www.linkedin.com/in/yasir-hashim-31a41713a
- [ ] Thomas Eddleston's profile is still live at https://www.linkedin.com/in/thomas-eddleston
- [ ] Ivan Tsvilik's profile is still live at https://www.linkedin.com/in/ivantsvilik
- [ ] You've read the trigger announcement for each to confirm the brand announcement still exists and the context is current
- [ ] Payment infrastructure plan is decided (Stripe / Gumroad / invoice fallback) and will be live before you send Message 2

**Ready to send.** Report back after the five DMs reach the inbox, and we'll log the Day 1 clock start.
