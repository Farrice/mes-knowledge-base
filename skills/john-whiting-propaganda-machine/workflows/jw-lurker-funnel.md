---
description: Design the buy-side ecosystem for lurker audiences — no-opt-in pages, button-click intent events, the YouTube binge loop, micro-audience anti-optimization, and pace-based budget reallocation — so prospects consume and close on their own volition.
tier: system
expert: john-whiting
stacks_with: [luke-iha]
---

# The Lurker Funnel — Build How They Buy, Not How You Sell

> "My content has to be really good and my ecosystem has to be how my clients want to buy, not how I want to sell." — John Whiting

`jw-retargeting-architecture` decides WHO sees WHAT at WHAT frequency. This workflow designs the *surfaces and events* the funnel runs on when the audience is made of **lurkers** — high-status prospects who never opt in, never comment, and treat every form as a setter-ambush warning. Genius patterns #15 (Lurker Funnel), #18 (Anti-Optimization Discipline), #19 (YouTube Binge Loop), #20 (Pace-Based Reallocation), with #16 (Familiarity-Bias Omnipresence) riding along.

---

## Pre-Flight Gate

1. **Does the retargeting architecture already exist?** This workflow re-skins the surfaces of a working 3-tier funnel; it does not replace the tier logic. No TOF/MOF/BOF build → run `jw-retargeting-architecture` first.
2. **Is the audience actually lurker-shaped?** Evidence, not vibes: low opt-in rates despite traffic, DMs that arrive pre-sold, prospects who consumed for weeks before surfacing, an ICP whose status drops by "raising a hand." If the audience happily opts in and books calls, a classic lead-gen funnel is cheaper — don't fix what isn't broken (that's a feeling-based rebuild, Rubric #1 fail).
3. **Are there historical ratios, or a commitment to build them?** Pace-based reallocation (Step 6) runs on spend→leads→views→qualified→clients ratios. No tracking → wire the GPS first (`jw-the-map` / data layer), or accept that Step 6 starts as data collection.
4. **Run `jw-ethics-gate` intent check.** A funnel with no opt-in and pixel events firing on button clicks must still pass reversible respect: if the prospect saw exactly which events you optimize on and why, would it read as "he built it so I could buy in peace" — or as surveillance? If the mechanism only works in the dark, kill it.

If all four pass, build.

## Skill Acquisition

Load `genius.md` (full). Core patterns: **#15 The Lurker Funnel**, **#18 Anti-Optimization Discipline**, **#19 The YouTube Binge Loop**, **#20 Pace-Based Budget Reallocation**, supported by **#16 Familiarity-Bias Omnipresence** and Hidden Knowledge: *status-upgrade framing*, *"ability to book, not booking."* Honor the **VOICE REFERENCE** (spine intact on every surface) and the **ETHICS GATE**.

---

## The Build (7 steps)

### Step 1 — Map how the buyer actually behaves
Write the behavior profile from evidence: Do they opt in? (Whiting's don't — "you don't want to be on another email list.") Do they DM? (Only when ready — "you know there's a setter on the other end.") Do they lurk and binge? (His DMs open with "I feel like I haven't even watched one of these videos in full... but I'm in.") Every funnel decision downstream serves THIS profile, not a template. *"What I share about what works for me works because I'm hyper-specific on who I'm marketing to."*

### Step 2 — Strip the hunt signals
Remove every element that tells the lurker they've been spotted:
- **Offer/VSL page with NO opt-in.** They watch the VSL, see the offer, see named video testimonials — no gate, no form.
- **Ads that are just videos in the feed.** Disable the CTA button and every auto-added AI element. No "Learn More," no lead form.
- **The DM disarm.** The automation's first move states the absence of the trap: *"It's not a setter or closer in here. It's just really me. Ask me whatever you want — or don't."*
- **Status-upgrade framing** on anything they must "get": buying is insider access, never an admission of a problem.

### Step 3 — Define the intent event (the button click = booked call)
Pick the highest-intent action the lurker WILL take and make it the conversion event: Whiting fires a standard **submit-application pixel event on a button click** (an app deep-link button on the offer page), then runs a leads-objective campaign maximizing that event. The click means "I've watched your VSL and want the offer details" — *"basically the equivalent of a booked call."* Expect the cost per event to look scandalous next to cheap opt-ins; that's the price of only paying for qualified intent. Attribution is fuzzier with no opt-in — bridge it with page-tag → DM correlation, not wishful ROAS math.

### Step 4 — Build the binge loop
Long-form is where the 7 hours accumulate, so engineer the exit from the scroll INTO the binge:
- Every YouTube long-form gets an **app deep link** (opens the app, not a logged-out browser — the friction detail decides whether they watch).
- Run cheap **traffic ads from the warm ring to the newest long-form** (animated thumbnail as the creative).
- **Every video's CTA = another video.** No pitch, no opt-in: *"I'm just forcing you to consume my shit."*
- The offer page's secondary button is the YouTube channel itself: not-ready lurkers get routed to more consumption, and "all roads lead back here anyway."

### Step 5 — Anti-optimization discipline (micro-audience rules)
For warm rings under ~2K people, the media-buyer playbook is wrong. Set spend to the floor that buys full reach ($2–3/day per ad set), cap per-asset frequency (~2×/7 days) so nobody hides your content, then **leave it alone**: *"So goddamn small of an audience that it doesn't matter. Let it run."* No creative testing, no CPM reviews, no learning-phase babysitting. The only dial is combined frequency (target ≈ 1+/day per warm-ring member). Scale by ADDING assets, never by optimizing them.

### Step 6 — Pace-based budget reallocation
Build the ratio calculator from history: spend → front-end buyers → offer-page views → qualified DMs → clients. Weekly, compare **pace per stage**. The stage behind pace gets budget FROM stages ahead of pace — Whiting was 162% ahead on front-end acquisition, behind on page views, moved TOF budget to MOF page-view ads, and qualified DMs snapped back ahead of pace. The funnel is one pool of money finding its bottleneck, which is `jw-data-bottleneck` applied to ad spend.

### Step 7 — The doors-open close
Last 7 days of the month: a hidden seats-left counter + application deadline timer goes live on the offer page, plus one or two ads to the warm ring only — *"You've been watching my shit. I've opened seats. Go here if you want the details or fucking don't."* Real seats, real deadline (Ethics Gate #1 — fake scarcity kills the machine). The month's accumulated consumption converts in a compressed window with zero human chasing.

---

## Content Type Adaptations

| Deliverable | How the lurker funnel adapts |
|---|---|
| **Coaching / high-ticket, no calls (Authority Flywheel)** | Hero use case, full build as written: no-opt-in offer doc, DM-keyword automation with the disarm opener, binge loop on the long-form library, doors-open close monthly. |
| **LinkedIn-native (× Lara Acosta)** | No pixel events — the "button click" becomes the profile-visit → featured-link click; the binge loop is the featured section + pinned posts; the disarm is stated in the DM opener. Lurker behavior is even stronger on LinkedIn; never gate the offer doc. |
| **Newsletter / Substack (× Nicolas Cole)** | The lurker exception: a newsletter IS an opt-in — so the opt-in must be framed as insider access (status up), never "get help" (status down). Binge loop = back-catalog links in every edition. |
| **Paid ads (× Luke Iha)** | Full instrumentation. Luke's hooks dress the traffic ads; the intent event replaces the lead form. Report cost-per-intent-event next to what a booked call used to cost — that's the honest comparison. |
| **Low / no ad budget (organic-only)** | No paid binge loop — the CTA-chain between videos/posts carries it. The doors-open close still works (email + pinned post + stories to the warm list). Anti-optimization becomes "post the cadence, stop checking analytics daily." |

## Output Requirements

Deliver a **Lurker Funnel Build Sheet**:
1. **Buyer-behavior profile** — evidence-backed (opt-in rates, DM patterns, consumption traces), not assumed.
2. **Hunt-signal strip list** — every gate/button/form removed or disarmed, page by page, plus the DM disarm script.
3. **The intent event** — the chosen action, the pixel/standard event that fires, the campaign objective, and the attribution bridge (page-tag → DM correlation).
4. **Binge-loop map** — deep links per long-form, traffic-ad plan, the CTA chain between videos.
5. **Micro-audience spend plan** — per-ad-set floor spend, frequency caps, the combined-frequency target, and the explicit "do not optimize" rule.
6. **The ratio calculator + reallocation rule** — historical ratios per stage, the weekly pace check, where budget moves when a stage lags.
7. **Doors-open close spec** — real seat count, deadline mechanics, the warm-ring-only ad copy. **Ethics Gate sign-off** on the whole build.

## Quality Gate

Score against the genius.md rubric (1–10). Load-bearing dimensions:
- **Reality-grounded? (#1)** — The buyer profile and the ratios come from actual data. "Our audience feels like lurkers" without opt-in/DM evidence fails outright.
- **Objections pre-handled? (#3)** — The disarm opener and no-opt-in page ARE objection-handling (the objection: "I'll get ambushed"). If the funnel still contains a single ambush signal, the whole lurker thesis collapses.
- **Leveraged? (#6)** — Once built, the machine runs on frequency + the monthly close. A funnel needing daily optimization violates Step 5 by design.
- **Ethics Gate passed? (#7)** — Watch the two failure modes specific to THIS build: (a) **fake scarcity** in the doors-open close — invented seat counts or resetting timers fail gate #1, kill it; (b) **dark-pattern eventing** — optimizing on signals the prospect would feel spied-on to learn about fails reversible respect.
- **Self-selecting? (#4)** — The consumption path must still polarize. A binge loop of agreeable content warms everyone including wrong-fits — the clips it circulates keep the confrontational spine (Mode A/B).

**Funnel-specific failure modes:** bolting an opt-in back on "just to capture emails" (kills the disarm); judging the intent event by opt-in-era CPA benchmarks (the data lies — compare to booked-call cost); optimizing micro-audience ads because idle hands (Step 5 violation); a doors-open close with no real deadline.

If any dimension <6, rebuild that step once and re-score.
