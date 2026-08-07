# Parallax Post-Subscribe Intelligence Capture

**Tyler Denk framework:** The moment after a reader hits "subscribe" is the highest-intent moment in the entire relationship. Most publications waste it with a generic "thanks for signing up" confirmation. Parallax uses it to capture buyer-qualification data — framed as editorial, not as sales.

**Principle:** Every subscriber is an acquisition node, not a reader. The survey segments the list into avatar-matched groups so Farrice can route future content, offers, and DMs intelligently.

**Honesty rule:** The survey must feel like editorial curiosity, not qualification theatre. If a reader would roll their eyes at the framing, it's broken.

---

## Where the Survey Lives

### Option A (recommended for launch) — Typeform, linked from Email 1

Typeform (or Tally, free) hosts a standalone 3-question survey. The link is in Email 1 as a PS offer: *"If you'd rather answer a three-question version instead of a free-form reply, here's the short survey."*

**Why Typeform over Substack native:** Substack's built-in welcome email can't branch based on answers. Typeform responses can feed into a Notion database or Zapier automation that tags the subscriber for Avatar 01/02/03 welcome-sequence variants (Phase 2).

**Cost:** Free tier covers up to 10 responses/month. Upgrade to $25/mo tier if response volume exceeds that (i.e., Parallax grows past ~40 new subscribers/week, which would be a good problem).

### Option B — Substack native welcome question

Substack allows a single "welcome question" on the subscribe confirmation page. Use this as a low-friction backup for subscribers who won't leave Substack to fill out a longer form.

**Single-question version:**
> *What are you trying to see differently this quarter?*

This is the same question Email 1 asks. The Typeform version extends it to 3 questions for subscribers willing to go deeper.

### Option C (Phase 2) — Survey embedded directly in Email 1

Embed the 3 questions as clickable radio buttons inside Email 1. Each click routes to a thank-you page and tags the subscriber in the email tool. Requires a tool like ConvertKit/Kit or Beehiiv with native segmentation. Substack does NOT support this natively.

**Recommendation:** Launch with Option A + Option B running in parallel. Migrate to Option C if/when Parallax moves off Substack for advanced segmentation (Phase 2).

---

## The Three Questions

### Question 1 (identity signal)

> *What are you trying to see differently this quarter?*
>
> *(Free text — one or two sentences. No wrong answer.)*

**Purpose:** Editorial feel. Mirrors the Manifesto's parallax theme. Not a qualifier on its surface — but the free-text answer reveals avatar patterns (publication-related answers → Avatar 01, practice-related → Avatar 02, mission-related → Avatar 03).

**What Farrice learns:** The raw word choice is the tell. "My newsletter" → Avatar 01. "My practice" or "my clients" → Avatar 02. "Our programs" or "our work" → Avatar 03.

---

### Question 2 (work context)

> *Which of these sounds most like where you are right now?*
>
> *(Pick one.)*

**A.** I write a publication. It has a small audience that's slowly growing — but I'm not yet monetizing it the way I'd like to.

**B.** I run an independent practice (consulting, coaching, advisory). I have clients; I don't have a pipeline that pulls.

**C.** I lead a mission-driven organization. The work matters; the articulation doesn't carry yet.

**D.** I'm still early. I read newsletters like this one to figure out what I want to build.

**E.** None of the above — let me tell you: [free text]

**Purpose:** Direct avatar sorting. A = Avatar 01, B = Avatar 02, C = Avatar 03. D is the early-stage filter (disqualified from immediate ICP offer — routed to a nurture track that builds up to readiness). E is the outlier capture.

**Framing logic:** Written in the reader's voice, not the seller's. "I write a publication" is a USE-word. "I'm still early" is a real identity, not a disqualifier. This feels like a profile question, not a funnel.

---

### Question 3 (trigger-event filter — qualifies TODAY)

> *What was the specific moment recently when you thought "I need to figure this out"?*
>
> *(Free text. The more specific, the better.)*

**Purpose:** This is the buyer-qualification question hidden inside an editorial survey. An answer like *"A donor asked me who this is for and I spoke for 90 seconds while they nodded politely"* is a $4,997 buyer trying to find the door. An answer like *"Just curious about the newsletter"* is not buying anything this year.

**How Farrice uses the answer:**
- Trigger-event answer = add to "hot list" — within 14 days, send a personal note asking if they want the free diagnostic.
- No-trigger answer = standard welcome sequence, no personal follow-up.

**Why the question is phrased as a "recent moment":** Sparks memory retrieval. The reader pulls up a specific scene, not a generic pain. Farrice gets language he can quote back in a personal outreach email.

---

## The Survey Confirmation Page

**After submission, the reader lands on a custom thank-you page:**

> **You sent me the answers. I read all of them.**
>
> *(No VA. No filter. Just me and a coffee.)*
>
> The next Parallax edition drops Thursday. Based on what you wrote, I'll send you a note sometime this week — either a specific resource that matches where you are, or just a reply to what you said.
>
> If I don't land in your inbox, check spam. If I did and the email didn't resonate, hit reply with "no thanks" and I'll stop.
>
> — Farrice

**Why this page matters:** Same principle as the rest of the sequence — every surface feels editorial. No "You've been added to our segmented marketing funnel." Just a human saying "I read your answer."

---

## Response Routing (what happens based on answers)

### Response routing table

| Q2 Answer | Q3 Answer pattern | Route |
|---|---|---|
| A (publication) | Dashboard scroll / paid conversion / post that underperformed | Hot Avatar 01 → personal outreach within 14 days, offer the free ICP Tell |
| A (publication) | Vague / generic | Standard Email 2 + Email 3 sequence |
| B (practice) | 340 reactions and zero clients / Sunday dread / pipeline | Hot Avatar 02 → personal outreach, Architecture-framed |
| B (practice) | Vague | Standard sequence |
| C (mission) | Donor asked / city launch / grant rejection | Hot Avatar 03 → personal outreach, Launch-framed |
| C (mission) | Vague | Standard sequence |
| D (early) | Any | Nurture track → no offer, just continue reading Parallax |
| E (other) | Any | Farrice reviews manually, replies personally |

### Personal outreach template (hot-list — Avatar 01 example)

> Subject: Re: your answer to the Parallax survey
>
> Hey [first name],
>
> You wrote: *"[quote their Q3 answer]."*
>
> That moment you described is the exact moment I built Parallax ICP Intelligence for. I'm not going to pitch you anything in this email — but if you want a free 20-minute diagnosis on where your reader is going missing, that's something I offer Parallax subscribers.
>
> No obligation, no sequence. Here's the link if it's useful: [ICP Tell application].
>
> If not — no worries. See you Thursday for the next edition.
>
> — Farrice

**Variant templates for Avatar 02 and Avatar 03** follow the same structure, with the middle paragraph swapped for Architecture or Launch framing. Always reference Q3 verbatim. Always end with "see you Thursday" to remind them Parallax isn't an ad channel.

---

## What the Survey MUST NOT Do

- **Not** ask about company size, budget, or revenue directly. Those are sales questions disguised as surveys and every reader clocks them.
- **Not** offer a lead magnet as a reward for filling it out. The survey IS the interaction. Gating content behind it breaks the editorial frame.
- **Not** use progress bars, "question 1 of 7" framing, or anything that signals "long survey." Three questions, visible at once, done in 60 seconds.
- **Not** ask about email preferences ("how often do you want to hear from me?"). Parallax has a cadence (Tuesday + Thursday). The reader opted into that when they subscribed.
- **Not** segment on demographics ever. Dai Media principle: demographics lie. Consumer posture (occupation / activity / thought process) is what the survey captures via Q2 + Q3.

---

## Phase 2 — Advanced Segmentation (once list hits 1,000 subscribers)

**Migrate welcome sequence to avatar-matched variants:**
- Avatar 01 variants: Emails 2 + 3 swap in publication-writer case studies (once Michelle-Welsford-style client stories exist)
- Avatar 02 variants: Emails 2 + 3 swap in consulting-practice case studies
- Avatar 03 variants: Emails 2 + 3 keep the Javier story (already Avatar 03 match)

**Trigger-event re-fire:** Every 90 days, send a single email to the "non-hot" segments asking Q3 again — *"what's the specific moment this quarter that made you think about this?"* Updates the hot list as circumstances change. Readers shift from non-buyer to buyer over time; the quarterly re-ping catches them.

**Predictive scoring (Phase 3):** Train a lightweight classifier on Q3 answers from closed deals vs. no-shows vs. disqualified prospects. The pattern is already visible in the first 20 buyers: the sales-intent phrase structure ("I just had a bad [moment]" / "A [person] asked me [question]") predicts conversion at ~80% accuracy. Automate tagging once signal is strong.

---

## Metrics to Track

| Metric | Target | Purpose |
|---|---|---|
| Subscribe → Survey completion | 30%+ | Signal health of Email 1. If <30%, rewrite the PS. |
| Hot-list personal outreach → Call booked | 40%+ | Signal quality of the Q3 filter. If <40%, tighten the question. |
| Avatar D percentage | <30% of total | Signal whether Parallax is reaching the right readers. If >30%, content too generic. |
| Avatar A/B/C split | Roughly 50/30/20 | Matches the ICP tier capacity (4 Crystals / 2 Arch / 1 Launch per month). If skewed, rebalance content mix. |

The survey is both a qualification tool AND a content-feedback tool. Every month, Farrice pulls the latest 30 Q1/Q3 answers and lets them inform the next two editions. The survey feeds the editorial calendar — not just the sales pipeline.
