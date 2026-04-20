# Conversion Tracker — Spec + Paste-Ready Google Sheets Headers

**Purpose:** Single source of truth for Parallax outreach funnel. Executable in Google Sheets. Updated daily. Drives mid-week pivots and weekly decisions.

**Premise (Validation-First Outreach):** Every message is PMF research. If the tracker doesn't show which script + channel + avatar + time-window combination is converting, the outreach is blind — and blind outreach burns prospect lists without learning.

---

## GOOGLE SHEETS SETUP

Create a new Google Sheet titled: `Parallax Outreach Tracker — [Start Date]`

### Sheet 1: "Prospects" (paste headers into Row 1)

```
prospect_id	name	handle_or_url	channel	avatar	qual_score	entry_type	personalization_hook	script_variant	sent_date	sent_time_PT	opened	opened_date	replied	reply_date	reply_type	reply_notes	call_booked	call_booked_date	call_happened	call_happened_date	offer_tier_fit	status	closed_amount	closed_date	notes
```

### Sheet 2: "Daily Log" (paste headers into Row 1)

```
date	sends_today	opens_today	replies_today	positive_replies	neutral_replies	objection_replies	hard_nos	calls_booked_today	cumulative_sends	cumulative_replies	reply_rate_pct	notes_and_observations
```

### Sheet 3: "Script Performance" (paste headers into Row 1)

```
script_variant	avatar	total_sends	total_opens	total_replies	positive_replies	calls_booked	closed	reply_rate	conversion_rate	retain_or_kill
```

### Sheet 4: "Weekly Pivot" (paste headers into Row 1)

```
week_num	total_sends	total_replies	reply_rate_pct	calls_booked	calls_held	closed_deals	closed_revenue	winning_variant	winning_avatar	winning_channel	pivot_decision_for_next_week	notes
```

---

## FIELD DEFINITIONS

| Field | Values / Format | Notes |
|---|---|---|
| `prospect_id` | 1-50 | Matches prospect-list-50.md numbering |
| `name` | Text | Full name |
| `handle_or_url` | URL or @handle | Verified contact vector |
| `channel` | Substack / LinkedIn / Twitter / Email | Primary touch |
| `avatar` | 01 / 02 / 03 | Stalled Substack / Signal Bleeder / Mission Founder |
| `qual_score` | 1-10 | From prospect list |
| `entry_type` | Cold / Warm / Referral / Partner | How the touch originated |
| `personalization_hook` | Text (1 line) | The specific thing referenced |
| `script_variant` | A / B / C (cold) or M1 / M2 / S1 / S2 / R1 / R2 (warm) or P1 / P2 / L1 / L2 (referral) | Track the exact variant |
| `sent_date` | YYYY-MM-DD | Date message fired |
| `sent_time_PT` | HH:MM | Pacific Time |
| `opened` | Y/N/Unknown | Set Y only if explicitly confirmed (LinkedIn read receipts, Substack open confirmation) |
| `opened_date` | YYYY-MM-DD | When confirmed open |
| `replied` | Y/N | |
| `reply_date` | YYYY-MM-DD | |
| `reply_type` | Positive / Neutral / Objection / Hard No | Positive = interest/wants call; Neutral = "tell me more"; Objection = a reason they can't; Hard No = "not interested" or silence after bump |
| `reply_notes` | Text — verbatim first sentence of reply | Verbatim — this is PMF data |
| `call_booked` | Y/N | |
| `call_booked_date` | YYYY-MM-DD | |
| `call_happened` | Y/N | |
| `call_happened_date` | YYYY-MM-DD | |
| `offer_tier_fit` | Crystal / Architecture / Launch / None | Fit assessed on call |
| `status` | New / Sent / Opened / Replied / Call Booked / Call Held / Proposal Sent / Closed / Dead | Lifecycle state |
| `closed_amount` | $ amount or 0 | |
| `closed_date` | YYYY-MM-DD | |
| `notes` | Text | Any color — partner angle, future revisit, objection pattern |

---

## END-OF-DAY CHECKLIST (DAILY — 15 MINUTES)

Farrice runs this before closing laptop each outreach day:

- [ ] Every send today logged in "Prospects" sheet (prospect_id, script_variant, sent_date, sent_time_PT)
- [ ] Any replies received logged with reply_type + verbatim first sentence
- [ ] "Daily Log" row for today filled in (sends, opens, replies, reply_type breakdown)
- [ ] Reply rate computed: cumulative_replies / cumulative_sends × 100
- [ ] Tomorrow's 5-10 prospects confirmed (handles verified, referenced posts screenshotted)
- [ ] Scan: any positive reply unanswered >4 hours? Respond now.

---

## WEEKLY REVIEW DECISION POINTS (SUNDAY — 60 MINUTES)

Run this every Sunday before Week 2+ starts. Populate "Weekly Pivot" sheet.

### 1. Reply rate benchmarks

| Reply rate | Diagnosis | Action |
|---|---|---|
| ≥10% | Validated — scripts + avatars + channels are right | Scale the winning combo, 2x volume next week |
| 5-9% | Functional — soft validation | Hold scripts, test 1 variant swap in lowest-performing avatar |
| 2-4% | Signal-of-life, not validated | Kill worst-performing variant, rewrite 2 new variants, rerun |
| <2% | Script failure OR list failure | Diagnose: if opens are healthy but replies are zero → script problem. If opens are zero → list/handle problem. Fix the bigger one. |

### 2. Per-avatar performance

Compute reply rate per avatar (Sheet 3 auto-filter):

- Avatar 01 reply rate: X%
- Avatar 02 reply rate: X%
- Avatar 03 reply rate: X%

**Decision:** double down on the avatar with highest reply rate for Week 2. Cut the lowest. Exception: if Avatar 03 replies are all positive (even if few), Avatar 03 is the $4,997 close path — do NOT cut it.

### 3. Per-variant performance

- Variant A (Zero Proof): X sends, Y reply rate
- Variant B (Value-First): X sends, Y reply rate
- Variant C (Proof-Led): X sends, Y reply rate

**Retain** the top variant. **Kill** the worst variant. **Rewrite** a new variant to replace the killed one, using the verbatim-reply-notes data from the retained variant's wins.

### 4. Per-channel performance

- Substack Notes/DM: X sends, Y reply rate
- LinkedIn DM: X sends, Y reply rate
- Email: X sends, Y reply rate

**Decision:** pour Week 2 volume into the top channel. If Substack outperforms LinkedIn 2x, ditch LinkedIn for the next 14 days. Concentrate.

### 5. Pipeline health

- Calls booked this week: X
- Calls held this week: X (show rate: X%)
- Proposals sent: X
- Closed: X at $X total

**Benchmarks for the 7-day sprint:**
- Floor: 1 Crystal close ($1,497) in 7 days = $300-$500 threshold hit (if deposit, not full)
- Target: 2 closes ($2,994-$4,494) in 7 days
- Stretch: 1 Architecture close ($2,997) in 14 days + 1 Crystal = $4,494 → $2K-$5K 30-day threshold on track

---

## MID-WEEK PIVOT CHECKPOINT (WEDNESDAY — 20 MINUTES)

Hard checkpoint. No skipping. Runs Day 3 end-of-day.

**Step 1: Compute reply rate for Days 1-3.**

**Step 2: Run pivot decision table:**

| Condition | Action |
|---|---|
| Reply rate ≥5% | Continue Variant B as primary. Hold cadence. |
| Reply rate 3-4% | Rotate: next 10 cold sends use Variant A (Zero Proof) instead of B. Keep B for Avatar 03. |
| Reply rate <3% | Kill all cold Variant B sends. Rotate to A + C mix. Consider killing lowest-qual 10 prospects in favor of re-fills from partner targets (Trojan Horse list). |
| Zero replies on Avatar 03 | Push Javier for warm-intro activation by EOD Day 3 regardless of his original "Thursday" commitment. |
| Zero replies on any avatar after 10+ sends | Examine the variant — it's the problem, not the avatar. Rewrite. |

**Step 3: Log the pivot decision in "Daily Log" notes column.**

---

## LEAD CAPTURE WORKFLOW (WHEN REPLIES HAPPEN)

When a positive reply lands:

1. **Within 4 hours**: respond in-channel. Don't let it sit overnight.
2. **Respond with**: 1-2 sentence acknowledgment + calendar link + HVC case study link. Do NOT launch into discovery in-DM.
3. **Update tracker**: status → "Replied," reply_type = "Positive," add verbatim first sentence.
4. **When call booked**: update status → "Call Booked," send pre-call note with HVC case study + "bring one question about your reader."
5. **After call held**: status → "Call Held," offer_tier_fit populated, notes column gets 2-3 sentences of what they need + emotional temperature.
6. **Proposal sent**: status → "Proposal Sent." Flag for follow-up if no response in 72 hours.
7. **Closed**: status → "Closed," closed_amount + closed_date filled. Celebrate, then log in revenue tracker (separate system per CLAUDE.md).

---

## RED FLAGS IN THE TRACKER

Watch for these patterns — they indicate system failure:

- **All replies are neutral, zero positive**: script is too clinical, doesn't create enough pull. Rewrite with more story (Variant C lean).
- **Calls booked but low show rate (<60%)**: pre-call notes not landing. Add 24-hour-before reminder.
- **Calls held but zero closes**: offer framing on the call is the failure, not the outreach. Escalate to review pricing-psychology.md + offer-one-pager.md usage on calls.
- **One avatar has 100% of replies but 0% of closes**: wrong avatar for the offer OR wrong offer for the avatar. Pivot offer positioning OR pivot avatar.
- **Same prospect replies positive but never books call**: friction in the booking link. Test it from incognito. Fix.

---

## MINIMUM VIABLE TRACKER (IF FARRICE CAN'T SET UP GOOGLE SHEETS DAY 1)

If Google Sheets feels like friction on Day 1, use this 5-column fallback markdown table — upgrade to Sheets by Day 3:

```
| Prospect | Channel | Sent date | Reply? | Status |
|----------|---------|-----------|--------|--------|
```

This captures the minimum survival data. Upgrade to full Sheets by Day 3 or the pivot analysis fails.

---

## POST-SPRINT (DAY 7 + BEYOND)

After the 7-day sprint, the tracker evolves:

- Add a "Week 2 / Week 3 / Week 4" tab for each week's new prospect batch
- Add a "Pipeline" tab — prospects who went cold but could be revived in 30/60/90 days
- Add a "Closed Deals" tab — connects to revenue tracker (`execution/revenue_tracker.py`) per CLAUDE.md protocol

The tracker is a living system. Every message adds data. The data compounds.
