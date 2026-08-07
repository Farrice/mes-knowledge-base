# WARGAME.md — Alignment Architect Launch: Red-Team Pass (2026-07-07)

Graded against `.agent/workflows/wargame-grade.md` posture: grade point by point, don't soften to finish faster, weakest surface first, record the attack that hit and the patch it produced. Five surfaces attacked, hardest first. Nine files read in full (00-05).

---

## 1. ECONOMICS

**The arithmetic.** SCOREBOARD.md's own 4-week TARGET row sums to $1,750-$3,700 collected over 30 days; midpoint of the stated ranges is **$2,725**. That midpoint sits below the "$3-3.5K/mo good start" bar named in today's constraints, before any discount for risk. The stacked conversion assumption behind it — 20% DM→conversation × 33% conversation→audit close — is a labeled GUESS implying roughly 6.6% of all 55 planned DMs convert to a paid $300-500 out-of-pocket sale, decided alone, often on one call, by a self-funded ICP whose defining wound is distrust of marketing. That is an optimistic stack, not a conservative one. Sprint upside (weeks 3-4) is also front-loaded: only an audit sold in week 1 or 2 has runway to become a paid Sprint by day 30, so the model's own math needs its earliest, least-proven sales to be the ones that convert.

**CONFIRMED — MAJOR — payment-timing gap.** Nowhere in OFFER.md, FIRST-CALL-GUIDE.md, or DELIVERY-SOP.md was payment collection timing stated. A diagnostic-first, invoice-later model would slow the exact cash speed the constraints call urgent ("$200-300/wk matters immediately") and put fee collection at risk after value is already delivered. **FIX APPLIED**: `01-offer/OFFER.md` now states Audit is "paid to book the session" and Sprint takes a "50% deposit to start, balance due at the Week 3 sign-off call." `02-outreach/FIRST-CALL-GUIDE.md` close script now sends the payment link in the same breath as the material request — session doesn't book until both land.

**WATCH — no month-2 replenishment mechanism.** The 30-day model spends the initial ~55-name warm list once. Nothing in DELIVERY-SOP or OFFER describes how the pipeline refills in month 2 without a fresh source of names (referral-from-client ask, second-degree warm intros). The $2,725-$3,700 modeled is a launch-month spike against a finite list, not yet evidence of a repeatable monthly number. Logged, not fixed — fixing this is a month-2 planning problem, not a defect in this package.

**Honest number this plan supports**: after the payment-timing fix, **$1,500-2,500 collected in month 1** is the realistic band — the low-to-mid half of the plan's own target range, discounted for the optimistic conversion stack and the fact that most of it is one-time Audit/Sprint fee, not yet a demonstrated recurring rate. The stated "$3-3.5K/mo starting target" is reachable only at the top of the plan's own optimistic case, not the expected case.

---

## 2. COOZ REPEAT

**Structural, not asserted.** Checked against Cooz's four named failure modes in GROUND.md § 5: unbounded guarantee, architect-does-everything, plane-built-mid-flight, client-reps gap.

- Unbounded guarantee → OFFER.md's guarantee is bounded twice over: Audit fee credits to Sprint only if booked within 14 days; one defined week of refinement if the installed plan produces zero qualified conversations in 30 days. No "until it happens" language anywhere.
- Architect-does-everything → DELIVERY-SOP.md's "Anti-Burnout Clause" is five explicit negative commitments ("does not post on client channels," "does not chase a missed gate," "does not offer unbounded revisions," "does not reshape the offer mid-engagement," "does not run the client's inbox"), each traced back to the specific Cooz failure it counters.
- Plane-built-mid-flight → spine locked in OVERRIDE.md and GROUND.md before outreach starts; DELIVERY-SOP states new scope buys a new rung rather than renegotiating the current one.
- Client-reps gap → four explicit, dated gate checks (pre-book material, Week 1 warm list, Week 2 written approval, Week 3 client-sent first outreach) with a stated **gate-miss rule**: the Sprint clock pauses and resumes within 24h of the gate arriving, no chasing. This is a mechanism, not a hope.

FIRST-CALL-GUIDE.md's "Can you just do it for me?" script directly names the Cooz trap and holds the line rather than softening it to close faster — the one place an executor might be tempted to relapse into the old pattern is explicitly scripted against.

**CONFIRMED — MINOR — Rung 2 had no hour ceiling.** Rung 0 and Rung 1 both carry explicit Farrice-hour budgets (2.75h, 3.75h); Rung 2 (the recurring retainer) had only a client-count cap (3), not a per-client hour cap — the exact shape of scope that quietly expanded with Cooz. Rung 2 doesn't activate inside this 30-day test, but shipping it undefined would reopen the door later. **FIX APPLIED**: OFFER.md Rung 2 now caps at "2 hours of Farrice time per client per month," with overage triggering a written scope renegotiation rather than silent absorption.

**Verdict on this surface**: the package structurally prevents the Cooz repeat. This is the strongest of the five surfaces.

---

## 3. BUYER WALLET

Will a warm-network fitness/transformation coach pay $300-500 out of pocket for a diagnostic? Price resistance bites exactly where the ICP's core wound lives: someone who admits "I'm great at my work but terrible at marketing myself" is, by definition, not a confident buyer of marketing-adjacent services, and the ICP's client-acquisition history (referral-only, per GROUND.md #12-13) signals real skepticism of paid positioning work generally.

**Mitigation that's real**: the FIRST-CALL-GUIDE's call structure delivers the diagnostic insight — the named pattern — live and free in the first 20 minutes, then sells the artifact (written diagnostic, specific pricing fix, Sprint-fit read) as the paid deliverable. That's a legitimate demo-then-sell structure, not empty scarcity. The "I can't afford it" objection script neither manipulates nor chases past a genuine no.

**WATCH — free-demo cannibalization risk.** The distinction between "insight given free on the call" and "artifact sold after" is real but thin for a sufficiently skeptical prospect who could reasonably ask why $400 buys a written version of what they just heard for free. Not disprovable without running calls; logged as a risk to monitor in week 1-2 call outcomes, not fixed pre-emptively.

**WATCH — no funded-buyer variant is actually ready.** The task asks directly whether a Path A bridge exists as a live fallback if AA's wallet stalls. SCOREBOARD.md § 1 names a bridge — an AA client who later scales becomes a Path A warm intro — but this is explicitly a future, speculative pathway contingent on an AA client's own growth, not a parallel offer Farrice can run today. Honest answer: **no funded-buyer variant is ready now.** If AA's $300-500 price point meets hard resistance in week 1-2, there is no pre-built alternate offer to pivot to inside the 30-day window. Logged, not fixed — building one is a scope decision beyond a surgical wargame edit.

---

## 4. MESSAGE CRINGE TEST

Ran `execution/prose_classifier.py check` against every content file (objective AI-slop signal) plus a manual friend-test read of every DM and post.

**Automated results**: WARM-DM-SCRIPTS.md CLEAN (0/10), FIRST-CALL-GUIDE.md CLEAN (0/10), OFFER.md CLEAN (1.5/10, parallel-structure only), LINKEDIN-QUEUE.md WARNING (2/10, 97 parallel blocks across 2,182 words — structural rhythm, not slop vocabulary; QA Notes already self-audit against the slop bank). No banned vocabulary, no banned structural moves (twin-sentence endings, triple anaphora, "It's not X, it's Y.") found in any file.

**CONFIRMED — MAJOR — Cooz DM asserts an unverified outcome.** WARM-DM-SCRIPTS.md's Day-0 Cooz opener originally read "Proud of where you've landed." GROUND.md and today's authoritative facts both frame Cooz as a "case-study-in-progress," never confirmed to have reached his $3-5K/mo (let alone $10K/mo) goal — that ambiguity is the entire reason the engagement's guarantee never resolved cleanly. Telling the one recipient who'd know the truth that he's "landed" risks reading as hollow or presumptuous, and it violates the package's own receipts-led standard by asserting an outcome with no receipt behind it. **FIX APPLIED**: reworded to "Proud of how far you've come, and I know there's more still cooking" — warm, honest, and doesn't claim a result GROUND.md doesn't support.

**CONFIRMED — MAJOR — public content about identifiable real people with no consent step.** Post 3 (LinkedIn queue) names "Josh and Katie" by first name alongside their exact fee ($3,500). Post 11 tells the Cooz story in enough specific detail (year-long engagement, $3,000, transformation coach, unbounded guarantee) that Cooz would recognize himself immediately even unnamed. Nothing in GROUND.md, OFFER.md, or the outreach scripts included a consent-before-publish step, and the Cooz DM was scheduled with no mention that an identifiable public post about him was coming — a real risk of him finding it in his feed unwarned, in the same window Farrice is DMing him for referrals. This is squarely a "would a real friend find this off" failure: publishing about a friend's paid engagement and dollar figure without a heads-up, while simultaneously asking him for business favors, reads as extractive even when the content itself (correctly) frames the failure as Farrice's own. **FIX APPLIED**: Cooz's Day-0 DM now includes an explicit heads-up ("I'm posting our story on LinkedIn soon, no names, framed as my lesson, not yours — wanted you to hear it from me first"). Josh & Katie's Day-0 DM now asks permission directly ("cool if I use your first names?"). LINKEDIN-QUEUE.md's QA Notes now gate posts 3 and 11 on that nod landing first, with anonymization as the fallback if it doesn't.

No other cringe-flags survived the manual read — the pain/POV/receipts/method rotation reads as a person talking, not a funnel, and the "not one of those guru types" and "shouting into the void" posts in particular land as genuine pattern-naming rather than persona performance.

---

## 5. CONGRUENCE OR RATIONALIZATION

Steel-manned the skeptic directly: **AA eats 100% of the daily-hour budget and Path A dies silently while SCOREBOARD.md asserts it didn't.**

**CONFIRMED — CRITICAL — the skeptic was right about the math as written.** DELIVERY-SOP.md's "The Math" section, before this pass, allocated the entire 1-3hr daily cap to AA activity only: "Farrice's own outreach (warm DMs + one LinkedIn post)... plus fulfillment for up to 2 concurrent clients," and its own "non-call days" bullet stated spare capacity goes toward "intake a second Audit" — more AA, not Path A. There was no line item, no hour reservation, and no tracked metric anywhere in the package for Path A's own outreach during the 30-day window. SCOREBOARD.md § 1 *asserts* "Path A is not dismantled... one lane, two rungs" in prose, but the only measured table in the entire package (the weekly scoreboard) tracked AA activity exclusively — DMs, conversations, Audits, Sprints, dollars, posts. Nothing counted whether Path A's own warm-intro or funded-brand outreach happened at all. **A claim with no metric that could falsify it is not a fact, it's a hope** — which is precisely the shape of the prior four redirects this override was supposed to be different from.

This is the closest this package came to being the 5th redirect wearing a scoreboard. It wasn't rationalization in the sense of dishonest framing — the shared-vertical, shared-warm-network argument in SCOREBOARD.md § 1 is genuinely true (Josh & Katie, Jen's brokerage, Javier are real Path A-adjacent contacts, not invented ones). The failure was operational: the hour math and the tracking table simply never allocated anything to the thing the prose claimed was protected.

**FIX APPLIED** (two files, same defect):
- `04-delivery/DELIVERY-SOP.md`: added a non-negotiable Path A carve-out — 15-20 minutes of every non-call day's outreach budget goes to Path A *before* any spare minutes go to a second AA Audit intake.
- `05-congruence/SCOREBOARD.md`: added a "Path A touches" column to the weekly table (target 3+/week) with an explicit rule that two consecutive weeks under 3 touches is a silent-death signal on Path A, named out loud the same Friday it happens, independent of how AA's own numbers read.

The kill condition's own qualifier ("a kill only counts if the reps happened") is genuinely falsifiable now for AA (44/55 DMs is a countable fact). Before this fix, the parallel claim about Path A had no equivalent falsifiable test. It does now.

---

## VERDICT

**FIX-THEN-SHIP.**

Six defects confirmed and fixed in place (1 CRITICAL, 4 MAJOR, 1 MINOR); four risks logged as WATCH with no edit (economics replenishment, funded-buyer readiness, free-demo cannibalization, and the inherent optimism of the GUESS-labeled conversion stack). The Cooz-repeat structural design (surface 2) is genuinely strong and needed only one small tightening. The message layer (surface 4) was clean on automated slop detection but carried two real relational risks that would not have shown up in any keyword scan — both are now closed. The congruence surface (surface 5) had the package's single most serious defect: the "one lane, two rungs" claim was true in intent and false in the only measured artifact that could have proven it. That is now fixed and falsifiable.

**Honest revenue number this plan supports**: **$1,500-2,500 collected in month 1**, not the full $3-3.5K stated target — reachable only in the plan's own optimistic case, not its expected case. The plan should ship with that number in mind, not the higher one, and Farrice should read Friday's SCOREBOARD ACTUAL row against $1,500-2,500 as the honest bar, treating anything above it as upside rather than treating anything below $3K as failure.

Ship it with the six fixes in place. Watch the four logged risks in weeks 1-2, especially the Path A touches column — that number, more than the AA dollars, is the one that tells the truth about whether this override was the right call.
