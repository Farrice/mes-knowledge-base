# Delivery Spec — Parallax ICP Intelligence™

**Purpose:** Day-by-day SOP for every tier. Replicable — another operator could execute with Farrice's judgment applied at named checkpoints. Load-bearing principle: AI system handles synthesis and first-pass writing; Farrice's judgment fires at ICP selection, voice calibration, and final proof layer.

**Core infrastructure per engagement:** One Google Drive folder (pageless Docs), one Notion project row, one 60-min kickoff Zoom, one handoff Zoom per tier, chain_runner finalize after each phase.

---

## TIER 1 — PARALLAX CRYSTAL (7 days)

### Day 0 — Intake (upon payment)

**Automated:**
- Stripe payment → Zapier → creates Notion project row + Google Drive folder + sends intake-form email + books kickoff call via Cal.com.
- Intake form: 12 questions. Current URL. Top 3 posts (with metrics). Their own sentence for "who this is for." 3 clients/subscribers they love (names + why). 3 they've lost or hate (names + why). Current revenue from the work. Platform constraints.

**Farrice (non-delegatable, 15 min):** Reviews intake form before kickoff. Writes a one-paragraph pre-read summarizing what he sees. This is the Parallax signature — he brings a draft-read-of-them to the kickoff. Not a blank slate.

### Day 1 — Kickoff (60 min Zoom, recorded)

**Structure:**
- 5 min: Farrice reads back his pre-read. Prospect confirms or corrects.
- 20 min: The Patient Zero hunt — Farrice asks: "Walk me through three real humans who subscribe to you. Names. What do they do. How did they find you. What did they say when they first paid." This is the raw material for Consumer Posture.
- 15 min: The inverse — "Walk me through three people who *didn't* convert. What did they say."
- 10 min: Voice samples — prospect reads aloud a post they're proud of. Farrice captures cadence, rhythm, tells.
- 10 min: Ladder scoping — which specific pain do we center, which do we flag as adjacent.

**Farrice's judgment (non-delegatable):** The choice of Patient Zero. The AI can suggest based on pattern match. Farrice chooses which 3 real humans carry the document. This choice determines everything downstream.

### Day 2-3 — Synthesis (AI system heavy; Farrice judgment at 3 checkpoints)

**Parallel AI swarm (via `/parallel-swarm` and `/council`):**

| Section | Expert lens activated | Output |
|---|---|---|
| Consumer Posture | Dai Media (occupation/activity/thought process) | Draft posture section |
| Identity Sentence | Kallaway (5-input gate) + Lulu (articulation gap) | 3 candidate sentences |
| Pain Ladder | McRaney (deep canvassing) | Active vs pre-contemplation split |
| Trigger Event | Samuel Thompson (shadow market) | 3 trigger-event candidates |
| Language Map | Recall grounding + Luke Iha (proof voice) | Avoid/Use word lists |
| Kristen Stewart Test | Lulu | Pass/fail audit |

**Farrice's judgment (non-delegatable, 3 checkpoints ~30 min each):**
1. **Patient Zero finalization** — pick the 3 humans, reject 2 AI suggestions, replace with intuition.
2. **Identity Sentence selection** — pick 1 of 3 candidates; the AI writes the options, Farrice picks the one that won't flinch.
3. **Language Map avoid-list** — what reads as slop to this specific reader. Farrice has the taste receptors for this; AI tends to over-ban.

### Day 4 — Draft assembly

**AI system:** Drafts the Crystal Document using the 6-8 page template from the HVC grounding-document structure, populated from Day 2-3 synthesis. Drafts 5 pillar posts (hooks only, not full drafts). Drafts the 30-day calendar.

**Farrice (60-90 min):** Reads the full draft. Red-pens voice drift, over-framework-iness, any phrase a real prospect would flinch at. This is the "would X actually say this?" pass.

### Day 5 — Internal review gate

**Quality gate (per `directives/quality_gate.md` + chain finalize):**
- Intent alignment: does the doc center THIS client's reader, not a generic ICP?
- Expert standard: does it pass the "would Michelle Welsford (or whoever) recognize herself?" test?
- Adversarial resilience: can it survive the "this is just another ICP template" objection?
- Factual grounding: are the 3 real Patient Zeros actually findable humans, or composites?

If score < 7, one rewrite pass. If score ≥ 7, proceed.

### Day 6 — Client review

**Farrice sends:** Google Doc link (pageless), 3-min Loom walkthrough.

Client has 24 hours to mark up. Farrice does NOT schedule the handoff call before the client reviews. This preserves the "you've read it" anchor for the live session.

### Day 7 — Handoff call (45 min Zoom, recorded)

**Structure:**
- 10 min: Walk through the Crystal. Answer any markup questions.
- 20 min: Live rewrite of ONE of the client's drafts-in-progress, using the Language Map. This is the proof. The client watches their own writing shift.
- 15 min: The Day 30 check-in booked (free). Next steps conversation — ascend to Tier 2, retainer, or stay solo with the Crystal.

**Farrice finalizes:** `chain_runner.py finalize` logged. Notion row status → Delivered. Case study template created (blank, for Day 60 testimonial ask).

### Day 30 — Check-in (included, 30 min)

**Farrice reviews one shipped piece** against the Crystal. Notes where the Crystal landed, where voice drift is creeping back. Opens the Tier 2 upgrade conversation if the client is hungry for the revenue architecture.

---

## TIER 2 — PARALLAX ARCHITECTURE (14 days)

### Day 0-7: Everything in Tier 1

Same intake, kickoff, synthesis, draft, review, handoff for the Crystal Document. The Crystal IS part of the Architecture; it doesn't get skipped or compressed.

### Day 8-9 — Brand Voice Foundation

**AI system:** Drafts voice guide against Crystal + voice samples from kickoff. Uses the `/voice-document` and `/tone-calibrate` workflows. Structure: Brand Essence, Story, Voice Calibration (sounds like / does not sound like), 5 values as practices.

**Farrice (45 min):** The "does not sound like" list is the critical Farrice layer. AI tends to under-fill it. Farrice adds 5-10 specific phrasings that would be a voice betrayal for this specific client.

### Day 10-11 — Grace City Blueprint

**AI system (via `/grace-city-blueprint`):** Generates Grand Central Station north star, 4 destinations, 4 content lines, 3 passenger profiles, 5-rung revenue ladder, 30-day sprint.

**Farrice (60 min):** Destination selection and revenue-rung pricing. AI suggests conservative. Farrice calibrates to the client's actual capacity and stakes-appropriate pricing. Revenue ladder sign-off is non-delegatable.

### Day 11-12 — Message Audit (the BEFORE/AFTER)

**AI system:** Scrapes client's current homepage + About page. Scores against StoryBrand 7-element rubric. Drafts BEFORE/AFTER rewrite of hero section, 3-step plan, CTAs.

**Farrice (45 min):** The rewrite voice pass. AI delivers structurally correct copy; Farrice makes it sound like the client, not like StoryBrand-template English. This is the single most visible artifact in the deliverable and the single biggest risk of voice betrayal.

### Day 13 — Internal review gate

Same quality gate as Tier 1, with added check: does the Architecture hang together? Does the Crystal feed the Voice, does the Voice feed the Blueprint, does the Blueprint feed the Ladder? Each layer must close the prior layer's open loop.

### Day 14 — Client review + Handoff call (75 min Zoom)

**Structure:**
- 15 min: Walk through Architecture integration (how the docs talk to each other).
- 30 min: Live Message Audit walkthrough — Farrice shows BEFORE/AFTER on-screen, client reacts, adjustments made live in the doc.
- 20 min: Revenue Ladder conversation — what do they actually want to charge, where does the ladder start, where does it stop this quarter.
- 10 min: Day 45 follow-up booked (included). Tier 3 upgrade path named if applicable.

### Day 45 — Follow-up call (included, 30 min)

**Farrice reviews:** homepage live copy (did they deploy the rewrite?), 2 recent posts (are they using the Blueprint?), revenue ladder rung #1 adoption (did they launch it?). Opens Tier 3 conversation if applicable.

---

## TIER 3 — PARALLAX LAUNCH (21 days, done-with-you)

### Day 0-14: Everything in Tier 2

Same flow through Architecture completion. Do not compress.

### Day 15 — Identity Architecture working session (90 min)

**Farrice leads (non-delegatable):** This is the human-in-the-room session. Client reveals the frame they've been using ("non-profit founder," "consultant," "writer") and Farrice walks through the 5-layer Actor-Auteur rebuild (Individual / Occupation / Activity / Thought Process / Posture) to find the actual category they occupy.

**AI system:** Transcribes + drafts the Identity Architecture doc post-session.

### Day 16-17 — Three co-written pillar pieces

**AI system:** Drafts 3 full pillar pieces against Crystal + Voice + Identity Architecture. Uses relevant skill workflows (`/proof-copy-engine`, `/proof-architecture-builder`, `/new-media-ghostwriting`).

**Farrice (non-delegatable, 90 min per piece):** The voice pass on each one. The "does this sound like my client, not like AI" red-pen. This is the gate that makes Tier 3 worth the $2K over Tier 2.

### Day 18 — Client review #1

Client marks up the three pieces. Farrice revises once.

### Day 19 — Launch Announcement drafted

**AI system:** Drafts the announcement piece (post/essay/video script — client's choice).

**Farrice (60 min):** The "does this read as an announcement or as a mission statement" audit. Announcements name a specific reader. Mission statements point at an abstraction. Fix if drifted.

### Day 20 — Testimonial Ask System + Proof Spread Spec

**AI system:** Drafts 5-10 testimonial ask scripts (one per believer, customized per relationship). Drafts proof spread spec (the 3 artifacts, Siamese Twins claims).

**Farrice (45 min):** Relationship-specific voice pass on each testimonial ask. These are Farrice's highest-trust touchpoints with his client's network — zero template feel allowed.

### Day 21 — Launch Day War Room (60 min Zoom)

**Structure:**
- 10 min: Final pass on the announcement piece.
- 15 min: Publishing order and timing (what goes where, in what sequence).
- 15 min: Reply-handling protocol — what happens when the 47 DMs come in.
- 10 min: Testimonial asks go out — live, watch the client hit send on the first 2.
- 10 min: 30-day check-in booked. Parallax Retainer conversation opened.

### Day 45 — Follow-up + Retainer conversation

Same as Tier 2, plus: full retainer conversation if the client is shipping and wants ongoing infrastructure.

---

## WHERE FARRICE'S JUDGMENT IS NON-DELEGATABLE

Explicit list — this is the documentation another operator would need to execute with Farrice's taste intact:

1. **Patient Zero selection** (every tier, Day 1) — which 3 real humans anchor the document. AI suggests; Farrice picks.
2. **Identity Sentence selection** (every tier, Day 2-3) — pick 1 of 3 candidates.
3. **Language Map avoid-list** (every tier, Day 2-3) — what reads as slop.
4. **"Does not sound like" voice list** (Tier 2+, Day 8-9) — 5-10 phrasings that are voice betrayal.
5. **Revenue Ladder pricing** (Tier 2+, Day 10-11) — the number that matches stakes.
6. **Message Audit voice pass** (Tier 2+, Day 11-12) — making the rewrite sound like the client.
7. **Identity Architecture working session** (Tier 3 only, Day 15) — live diagnostic, human-in-room.
8. **Pillar piece voice pass** (Tier 3 only, Day 16-17) — 90 min per piece.
9. **Testimonial ask customization** (Tier 3 only, Day 20) — relationship-specific voice.

Every other task is AI-delegable. If volume hits and Farrice needs to staff, these 9 checkpoints are where human judgment continues to fire. A trained operator can execute everything else with Farrice's skill files and the chain protocol.

---

## CLIENT-FACING ARTIFACT LIST

| Tier | Artifacts delivered | Format | Hosted |
|---|---|---|---|
| 1 | Crystal Document + Language Map + 5 Pillar Hooks + 30-day Calendar | Google Doc (pageless) | Client Drive |
| 2 | All Tier 1 + Brand Voice Foundation + Grace City Blueprint + Message Audit BEFORE/AFTER + 90-day Calendar | 5 Google Docs (pageless) | Client Drive |
| 3 | All Tier 2 + Identity Architecture + 3 Pillar Pieces (co-written) + Launch Announcement + 5-10 Testimonial Ask Scripts + Proof Spread Spec | 9+ Google Docs + 1 designer brief (PDF) | Client Drive |

Every tier gets the recording of every Zoom. Every tier gets client-owned files (Parallax retains anonymized derivative rights for case study use with signed permission).

---

## SCOPE CREATION MECHANISM (Monk.Ai lens)

Every delivery checkpoint is also a surfacing moment. The SOP explicitly names when to raise the next-tier conversation:

| Trigger | Next-tier conversation surfaced |
|---|---|
| Day 7 handoff (Tier 1): client asks "but how do I price this?" | Tier 2 Revenue Ladder |
| Day 7 handoff (Tier 1): client asks "can you help me draft?" | Retainer (post-Tier 2) |
| Day 14 handoff (Tier 2): client asks "where does this post go first?" | Tier 3 Launch Announcement |
| Day 45 follow-up (Tier 2): client is deploying but voice is drifting | Tier 3 Identity Architecture |
| Day 21 Launch Day (Tier 3): client is thriving | Parallax Retainer ($2,500/mo) |

Audits don't end with reports. They open doors. Every report names what it opened.
