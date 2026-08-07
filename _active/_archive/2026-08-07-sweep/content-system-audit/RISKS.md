# RISKS — Content System Audit

> Per the Flag-Risks-Early Standard (MEMORY.md, 2026-04-22). Surface risks the moment they're discovered. Update this file as launch progresses. Don't bury risks inside other deliverables.

---

## R1 — Scope creep during audit (HIGH severity)

**Risk**: The 45-min call expands into 90+ min. Post-call deliverable balloons from 2-page blueprint to building their entire content stack. $249 turns into $2K of unpaid work.

**Why it matters**: Kills hourly economics. A single scope-creep audit at 6 hours → effective rate of $41/hr. Below LA cost-of-living floor.

**Mitigation**:
- Calendly slot capped at 45 min (auto-decline overruns)
- Backend pitch IS the boundary: "If you want me to actually integrate this into your stack, that's the $1K DWY sprint"
- Pre-call email explicitly states deliverables: "1 call, 1 Notion workflow, 3 prompts, 1 PDF. Anything beyond is the DWY."
- Track time per client. If avg fulfillment exceeds 2.5 hrs by client #5, raise prices or trim deliverables.

**Status**: Open. Active during all client work.

---

## R2 — ICP overlap confusion with $250 Proof Run (MEDIUM severity)

**Risk**: A coach prospect lands on the Audit page (or vice versa) and gets confused. Or a hybrid prospect (consultant who's also building methodology) doesn't know which to buy.

**Why it matters**: Confusion kills conversion. Two competing $250 offers from the same person looks amateur.

**Mitigation**:
- Different sales pages, different URLs, different DM scripts
- No cross-linking between offers in public-facing content until prospect already converted to one
- If a Proof Run prospect mentions "system" / "workflow" / "AI tools" — pivot to Audit
- If an Audit prospect mentions "I have a coaching methodology" — pivot to Proof Run
- Quarterly review: if conversion is split badly, sunset one

**Status**: Open. Monitor in first 5 client conversations.

---

## R3 — AI-slop accusation on launch posts (HIGH severity)

**Risk**: Anti-AI-slop is the WHOLE positioning. If the launch posts get accused of being AI-written, the offer is dead at launch.

**Why it matters**: Reputational. The product literally fails the marketing test if the marketing was written by AI.

**Mitigation**:
- All 3 LinkedIn posts pass `prose-doctor` subagent for the 8 banned structural moves (MEMORY.md AI Structural Tells, 2026-04-20)
- All 3 Substack Notes pass Notes Trailer Playbook check
- Sales page passes prose-doctor + adversarial-reviewer
- Voice fingerprint test: would Farrice say this to a friend? If no, rewrite.
- Read every published asset out loud once before posting. AI slop dies on the tongue.

**Status**: Open. Critical gate before any publish.

---

## R4 — First fulfillment takes 4+ hours instead of 2 (MEDIUM severity)

**Risk**: Plan budgets 2 hrs per client. Client #1 (without templates yet) realistically takes 4-6 hrs.

**Why it matters**: Margin compression. But this is EXPECTED — client #1 is the design partner.

**Mitigation**:
- Client #1 is explicitly framed as beta + design partner ($99)
- Treat first delivery as R&D investment, not delivery
- Templates emerging from client #1 absorb 80% of clients #2-5's work
- By client #5, fulfillment should be 90 min total per client

**Status**: Open. Acceptable risk in beta phase.

---

## R5 — Authority Flywheel cannibalization (LOW severity)

**Risk**: Audit at $249 is so much cheaper than Authority Flywheel ($2K-$5K) that prospects always pick the cheaper option, killing the higher-ticket pipeline.

**Why it matters**: Could compress overall revenue if Audit attracts AF-fit prospects.

**Mitigation**:
- Different offer ladders: Audit serves consultants who want to do their own writing; Authority Flywheel serves consultants who want it done for them
- Audit → DWY → Authority Flywheel is an upgrade path, not a competition
- If a prospect explicitly asks "should I do the Audit or the Flywheel?" → "Audit if you'll write your own posts. Flywheel if you want me to write them."
- 90-day check: if Audit clients NEVER upgrade to Flywheel, the offers are too distinct (not a ladder)

**Status**: Open. Monitor at 30/60/90 days.

---

## R6 — Beta clients don't convert to standard pricing (MEDIUM severity)

**Risk**: Word spreads that the Audit is $99. New prospects expect that price. Standard pricing dies.

**Why it matters**: $99 isn't sustainable. Need $249 baseline.

**Mitigation**:
- Public messaging always says $249. Beta is invitation-only ("I have 3 spots at $99 for testimonials")
- Beta clients sign brief acknowledgement: "This is beta pricing for case study purposes. Standard is $249."
- Stripe products kept separate ($99-beta is a private link, not a public checkout)
- After client #3, $99 link is killed

**Status**: Open. First test in beta period.

---

## R7 — DMs flagged as spam by LinkedIn (MEDIUM severity)

**Risk**: Sending 15-20 cold DMs/day triggers LinkedIn's anti-spam systems. Account restricted or banned.

**Why it matters**: Distribution channel goes dark. No way to reach buyers.

**Mitigation**:
- Per existing dm-script-playbook §"Rules of Engagement": NEVER >20 connection requests/day
- Pre-warm protocol (5 days of comments before connect) — prospects accept at 40-45%, not flagged
- Mix LinkedIn DMs with Reddit DMs (different platform = different risk surface)
- Personalize EVERY message. LinkedIn's spam detection picks up on copy-paste.
- If account warning appears, drop volume by 50% for 1 week

**Status**: Open. Standard distribution risk.

---

## Review cadence

- **Daily during sales push (Day 3-9)**: Review R3 (slop) before each publish, R7 (DM spam) before outreach
- **Weekly during fulfillment phase (Day 7-14)**: Review R1 (scope creep) after each client call
- **30-day review**: Full risk register update + decisions on R2, R5, R6
