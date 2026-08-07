# Setup Checklist — Manual Actions for Launch

> **Owner**: Farrice (these require account access I don't have)
> **Total time**: ~3-4 focused hours
> **Critical path**: Stripe → Tally → Calendly → Sales Doc → Schedule posts → Begin DMs

---

## Phase 0 — Decisions Before Setup (15 min)

- [ ] **Decision A**: Confirm beta pricing — first 3 clients at $99? (Plan default: yes)
- [ ] **Decision B**: Verify Note 3 anecdote — is the fractional CFO case real? If not, pick Fallback A or B from `04-deliverables/substack-notes.md`
- [ ] **Decision C**: Stripe products — separate $99 and $249 products, OR single $249 product with private $99 promo code? (Recommended: separate products, $99 link kept private)
- [ ] **Decision D**: Calendar conflict — confirm 3 × 45-min slots available this week + next for beta clients

---

## Phase 1 — Stripe (30 min)

- [ ] Log into Stripe Dashboard
- [ ] Create Product: **Content System Audit (Beta)** — $99 — one-time payment
  - Description: "Beta pricing for first 3 clients in exchange for testimonial. Standard rate is $249."
  - URL: KEEP PRIVATE (don't list publicly — share only via DM after qualification)
- [ ] Create Product: **Content System Audit** — $249 — one-time payment
  - Description: "45-min audit + Notion workflow + 3 custom Claude prompts + 2-page blueprint. Delivered within 24 hrs of call."
- [ ] Configure post-payment redirect → Tally intake form URL (so payment auto-routes to intake)
- [ ] Test payment with $1.00 test product OR Stripe test mode
- [ ] Save both checkout URLs in `_active/_archive/2026-08-07-sweep/content-system-audit/06-system/links.md` (create file)

---

## Phase 2 — Tally Form (30 min)

- [ ] Create new Tally form: "Content System Audit — Pre-Call Intake"
- [ ] Build 8 questions per `_active/_archive/2026-08-07-sweep/content-system-audit/06-system/intake-form.md`
- [ ] Configure logic: skip Q4/Q6 if Q2 = "I write everything from scratch"
- [ ] Set up post-submission email automation (Tally Pro feature OR Zapier free tier)
  - Subject + body per `06-system/intake-form.md` § "Post-Submission Confirmation Email"
- [ ] Set up post-submission redirect to Calendly URL
- [ ] Test full flow: submit form → check email lands → confirm Calendly redirect works
- [ ] Save Tally URL in `_active/_archive/2026-08-07-sweep/content-system-audit/06-system/links.md`

---

## Phase 3 — Calendly (15 min)

- [ ] Create new event type: **Content System Audit — 45 min**
- [ ] Set duration: 45 min hard cap (do NOT enable buffer/overrun — 45 min cap protects against scope creep per RISKS.md R1)
- [ ] Set availability: 3-5 slots per day during launch week, mornings preferred (high-energy time per Farrice's workflow)
- [ ] Configure Zoom or Google Meet auto-attach
- [ ] Pre-call reminder: 24 hr + 1 hr before (forces them to actually show up)
- [ ] Confirmation message: "Looking forward to mapping your system. Reply if you have voice samples I didn't get from the intake."
- [ ] Save Calendly URL in `_active/_archive/2026-08-07-sweep/content-system-audit/06-system/links.md`

---

## Phase 4 — Sales Page Google Doc (20 min)

- [ ] Create new Google Doc: "Content System Audit"
- [ ] **Apply pageless format** (Format → Pageless mode) — REQUIRED per MEMORY.md feedback (2026-04-13). Never PAGES mode.
- [ ] Paste copy from `_active/_archive/2026-08-07-sweep/content-system-audit/04-deliverables/sales-page.md`
- [ ] Replace `[Stripe link]` placeholder with the $249 Stripe URL
- [ ] Set sharing to "Anyone with the link can view"
- [ ] Test: open in incognito to verify pageless renders + link works
- [ ] Optional: shorten URL via short.io or bit.ly for cleaner DM-pasting
- [ ] Save sales page URL in `_active/_archive/2026-08-07-sweep/content-system-audit/06-system/links.md`

---

## Phase 5 — Pre-Launch Social Setup (45 min)

### LinkedIn

- [ ] Pin Post 1 ("The Enemy") OR Post 3 ("The Receipt") to top of profile during launch week
  - Recommendation: Post 3 first (lowest AI-tell risk, strongest pull-through per master-copywriter)
- [ ] Update LinkedIn headline to align with offer (suggested: "I build AI content workflows for solo consultants who want to keep writing — without losing the afternoon to it.")
- [ ] Update About section if it's been a while — read across to existing posts so language doesn't cannibalize
- [ ] Verify profile photo, banner, contact info are current

### Substack

- [ ] Pin Note 1 OR confirm Notes auto-publishing schedule
- [ ] Update Parallax About section if it mentions ghostwriting/Authority Flywheel — Audit prospects need to see system-builder positioning
- [ ] Optional: add a "Work with me" link in Substack settings → sales doc

---

## Phase 6 — Day 1 Publishing (30 min)

- [ ] Publish **LinkedIn Post 3 ("The Receipt")** between 8-10 AM PT (peak engagement window)
  - Pin to profile after publishing
- [ ] Publish **Substack Note 1 ("Decisions, not writing")** at lunch
- [ ] Begin pre-warm protocol on first 5 prospects (follow + bell + first comment)

---

## Phase 7 — Day 2-9 Outreach Routine (2.5 hrs/day)

Daily, every day until 1 paid sale OR Day 9 fail-gate:

| Time | Activity |
|---|---|
| 30 min | 5 substantive comments on prospect posts (50-100 words each) |
| 30 min | 10-15 personalized connection requests (post-prewarm) |
| 45 min | 10-20 cold DMs (variants 1-3 from `04-deliverables/dm-scripts.md`) |
| 30 min | 10-15 follow-ups on existing convos |
| 15 min | 1 Substack Note (rotate Notes 1-3 over the week) |

### Content cadence

- Day 1: LinkedIn Post 3 (Receipt) + Substack Note 1
- Day 3: LinkedIn Post 1 (Enemy) + Substack Note 2
- Day 5: LinkedIn Post 2 (Myth) + Substack Note 3
- Days 2, 4, 6, 7: 1 Substack Note + comment volume on LinkedIn

---

## Phase 8 — First Sale Trigger (when it happens)

- [ ] Confirm Stripe payment cleared
- [ ] Verify Tally intake form submitted
- [ ] Block 30 min pre-call for diagnostic prep (read intake + skim 3 writing samples)
- [ ] Block 90 min post-call for first-time fulfillment (template build + delivery)
- [ ] Update `_active/_archive/2026-08-07-sweep/content-system-audit/RISKS.md` R4 with actual fulfillment time
- [ ] Send Day-7 follow-up email with $1K DWY pitch

---

## Phase 9 — Post-Client #1 (Asset Build)

Per Phase 3 of the master plan (`~/.claude/plans/help-me-excute-this-jolly-breeze.md`):

- [ ] Create `skills/content-system-audit/SKILL.md` + 3 workflows
- [ ] Save anonymized prompt examples to `products/content-system-audit/prompt-examples/`
- [ ] Capture testimonial (voice memo or text quote)
- [ ] Run finalize per Chain Step 6: `python3 execution/chain_runner.py finalize ...`

---

## Validation gates (kill / pivot / proceed)

| Day | Gate | Pivot if failed |
|---|---|---|
| Day 2 | Stripe + Tally + Calendly tested end-to-end | Block sales until fixed — broken funnel = no revenue |
| Day 4 | Post 1 published, 50+ DMs sent | If <10 DM replies → switch to Reddit r/consulting only |
| Day 7 | 1 booked call | If 50+ DMs / zero calls → diagnose ICP fit, consider $49 beta or different niche |
| Day 9 | 1 paid beta client | If still zero → STOP outreach, run audit on the launch (likely positioning issue, not effort issue) |
| Day 14 | Client #1 delivered + testimonial | If client #1 NPS <8 → don't scale, debug deliverable |

---

## Files referenced

| File | Purpose |
|---|---|
| `README.md` | Offer brief + project context |
| `06-system/objection-handles.md` | 10 buyer objections + responses for live calls / DMs |
| `RISKS.md` | Live risk tracker (update weekly) |
| `04-deliverables/dm-scripts.md` | 10 DM variants (cold + warm + transition + breakup) |
| `04-deliverables/launch-posts.md` | 3 LinkedIn launch posts (voice-passed + prose-doctor verified) |
| `04-deliverables/sales-page.md` | Sales page copy ready for Google Doc |
| `06-system/intake-form.md` | Tally form spec (8 questions + confirmation email) |
| `04-deliverables/substack-notes.md` | 3 Substack Notes with verification flags |
| `setup-checklist.md` | THIS FILE — all manual setup actions |
