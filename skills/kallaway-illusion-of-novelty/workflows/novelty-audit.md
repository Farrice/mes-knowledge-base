---
description: Diagnose why an existing piece isn't landing — score it against the five components + 9-criterion rubric and return a prioritized, routed fix list.
---

# /novelty-audit — The Novelty Diagnostic

Takes any EXISTING piece (a hook, post, script, email, page) that feels flat or under-performs and returns a compact scorecard plus the 1–3 highest-leverage fixes, each routed to the workflow that repairs it. Fire this when something "should be working but isn't," when a draft reads boring on a topic you know is good, or before a rewrite so you cut the right cable instead of redoing the whole thing.

## Pre-Flight Gate

Load `../genius.md` if it is not already hot in this conversation. This audit is only as sharp as the avatar behind it, so answer these from the Decision Framework before scoring — an audit run on a guessed avatar produces a confident-wrong scorecard:

1. **Who is the actual avatar** for this piece, and **what does that avatar already believe** about the topic? (Without the held belief you cannot judge Contrast Integrity — you'll grade against your own assumption, not theirs.)
2. **What outcome does the avatar genuinely want?** (Needed to judge whether Outcome Mapping is present or merely implied.)
3. **Is the topic genuinely new, or old?** Old = the piece needed an angle; a flat old-topic piece almost always failed at Step 1 reveal or Step 2 contrast, not later.
4. **Is there an HONEST urgency window for this topic at all?** If no real window exists, a *missing* urgency component is correct, not a defect — do not dock it.

If the requester cannot supply the avatar and held belief, run that gap first (route to `kallaway-audience-obsession` / ICP work) before auditing. Note it in the scorecard rather than scoring around it.

## Skill Acquisition

- **Always:** `../genius.md` — the five components, the Trust Ladder, the nine rubric criteria with their anchors, and the anti-pattern list (the spine of the scoring).
- **The repair workflows you'll route to** (read on demand once you know the failure zone, not all upfront):
  - `./novelty-reveal.md` — fixes a missing or weak New Reveal + Outcome Mapping
  - `./novelty-contrast.md` — fixes a missing, strawman, or unrelated Contrast
  - `./novelty-urgency.md` — adds an honest urgency window (or confirms the correct skip)
  - `./novelty-proof.md` — climbs the Trust Ladder toward the viewer
  - `./novelty-protect.md` — removes mascot reveals and converts town-crier tone to gossip-whisperer
- **When the held belief is missing:** `kallaway-audience-obsession` / ICP skills supply it.
- **When the piece feels novel but doesn't hold past the hook:** the failure is often retention, not novelty — flag a handoff to `kallaway-addictive-storytelling` (`/addiction-loop-architect`) rather than over-fixing the front end.

## Execution

Run five passes, in order. Each pass writes one block of the scorecard. Resist the urge to start rewriting mid-audit; diagnose fully, then route.

### Pass 1 — The Three-Question Scan (does it earn YES on all three?)

For each of the three viewer questions, mark YES/NO and name the component that delivers it. A NO anywhere is the loudest signal of where the piece dies.

| Question | YES if… | Delivered by |
|---|---|---|
| **Relevant** — "do I care?" | the avatar is named or their situation is called out | usually the call-out / Outcome Mapping |
| **Novel** — "is this new to me?" | something has been *revealed* as changed/different | New Reveal (Step 1) |
| **Interesting** — "am I intrigued?" | a *gap* opens between held belief and the new reality | Contrast Framing (Step 2) |

Relevance is the cheap one and is almost never the true failure. If Novel or Interesting is a NO, you've found the zone before you even score the rubric.

### Pass 2 — Five-Component Presence-and-Quality Check

For each component, mark **STRONG / WEAK / MISSING** and write the one-line reason. Quote the actual line from the piece that carries it (or note its absence).

| # | Component | STRONG looks like | WEAK / MISSING tell |
|---|---|---|---|
| 1 | New Reveal + Outcome | a changed aspect named AND tied to a wanted result, ≤2 lines | reveal with no outcome (gets scrolled), or outcome with no genuine new angle (boring) |
| 2 | Contrast Framing | new angle sits directly against the avatar's *actual* held belief, true opposite | naked new claim (no anchor), or contrast paired to an unrelated/strawman belief = confusion |
| 3 | Urgency | a REAL "just changed / about to close" window | bolted-on fake deadline (trust-burning) — or honestly absent (mark **HONEST SKIP**, not a defect) |
| 4 | Bullseye Proof | proof close to the viewer's life (mimic example, or the creator's own result) | third-party study only (bottom rung), or no proof at all |
| 5 | Protect the Illusion | committed storyline + gossip-whisperer tone | a mascot reveal (hedge / false modesty / "everyone knows this"), or town-crier billboard tone |

The single most common silent killer here is a Component-5 mascot reveal sitting inside an otherwise solid piece — false modesty ("you've probably heard this"), or a hedge that admits the angle is old. It collapses the loop the first four components built. Hunt for it specifically.

### Pass 3 — Score the 9-Criterion Rubric

Score each criterion and **name the anchor** for any score ≥8 (per the rubric rule; if you can't name it, lower the score). Carry the automatic caps and vetoes exactly as written in `../genius.md`:

1. **Three-Question Pass** — all three YES? Missing any = fail.
2. **Hook Density** — opener carries ≥2 components (New Reveal + Outcome min) in ≤2 lines? Single-job hook = cap at 5.
3. **Contrast Integrity** — anchored to the *actual* held belief as a *true opposite*? Strawman/unrelated = confusion = fail.
4. **Urgency Honesty** — if used, is the window real? Fake/bolted-on = automatic ≤4.
5. **Trust-Ladder Height** — bullseye 9–10 · warm crowd 6–7 · third-party only 5 · no proof = fail. No fabricated proof.
6. **Illusion Intact** — zero mascot reveals? One mascot reveal = automatic ≤5.
7. **Whisper Test** — gossip-whisperer not town-crier? Salesy register = cap at 6.
8. **Honesty Spine** — facts true even though novelty is manufactured? Any fabricated fact = automatic fail.
9. **Domain Fit** — execution adapted to the real asset/platform/vertical? Generic slop = cap at 6.

### Pass 4 — Zone Diagnosis

Collapse the findings into the **primary failure zone** — the one place the most attention is lost. Pieces usually fail in exactly one zone; fix that first.

| Zone | Symptom | Owns components | Tell in the data |
|---|---|---|---|
| **HOOK** | scroll-past; never earns the LOOK | 1, 2, 3 | Pass 1 shows Novel=NO or Interesting=NO; low Hook Density |
| **BODY** | hooks but isn't believed; doubt sets in | 4 | strong opener, third-party-only or absent proof, low Trust-Ladder height |
| **DELIVERY** | believable but feels off / salesy / deflated | 5 | a mascot reveal present, or town-crier tone; Whisper Test fails |

If Pass 1 says the piece is novel and intriguing yet still doesn't hold attention *past* the hook, the failure is retention, not novelty — note "out of scope: hand to `/addiction-loop-architect`" rather than forcing a novelty fix.

### Pass 5 — Prioritized, Routed Fix List

Pick the **1–3 highest-leverage fixes**, ordered by attention recovered per edit. Route each to its repair workflow. One fix per cable; do not prescribe a full rewrite when a single component is the leak.

| If the leak is… | Fix | Route to |
|---|---|---|
| weak/missing New Reveal or Outcome | re-mine the angle, retie to a wanted result | `./novelty-reveal.md` |
| naked claim / strawman contrast | anchor the new angle to the real held belief | `./novelty-contrast.md` |
| fake urgency (or a real window left unused) | replace with honest window or confirm the skip | `./novelty-urgency.md` |
| third-party-only / no proof | climb the Trust Ladder toward the viewer | `./novelty-proof.md` |
| mascot reveal / town-crier tone | scrub the hedge, drop the voice to a whisper | `./novelty-protect.md` |

**Sequencing rule:** fix the HOOK zone before BODY before DELIVERY — a piece nobody looks at can't be saved by better proof. Stop at the top 3; the long tail rarely moves the number.

### Worked mini-example (fresh topic: gutter cleaning)

**Sample post audited (deliberately flat):**
> "Cleaning your gutters is important for protecting your home. Clogged gutters can cause water damage over time, so it's a good idea to clean them at least twice a year. Most people don't realize how big a problem this can become. Call us today to book a cleaning — limited slots available this week!"

**Pass 1 — Three Questions:**
- Relevant? Weak-YES. "Your home" gestures at the avatar but never calls out *who* (no specific homeowner situation).
- Novel? **NO.** "Cleaning gutters is important / twice a year" is the thing every homeowner has heard 10,000 times. Nothing revealed as changed.
- Interesting? **NO.** No gap opened — no held belief is challenged.

**Pass 2 — Components:**
- New Reveal + Outcome — **MISSING.** Restates common knowledge; no new aspect, no specific wanted outcome beyond vague "protect your home."
- Contrast — **MISSING.** "Most people don't realize how big a problem this can become" gestures at contrast but anchors to nothing the reader actively believes.
- Urgency — **WEAK / FAKE.** "Limited slots available this week!" is a bolted-on sales deadline with no real basis. Trust-burning.
- Bullseye Proof — **MISSING.** No example, no mimic, not even a study.
- Protect the Illusion — **TOWN-CRIER.** The exclamation-point CTA reads as a billboard; nothing whispered.

**Pass 3 — Rubric (abbrev.):** Three-Question Pass = **fail** (two NOs). Hook Density = 2 (single-job, restates the obvious). Contrast Integrity = 2. Urgency Honesty = **3** (bolted-on deadline, automatic ≤4). Trust-Ladder = **fail** (no proof). Illusion Intact = 7 (no mascot reveal, just nothing built). Whisper Test = 4 (salesy CTA caps it). Honesty Spine = pass (facts aren't false, just stale). Domain Fit = 5 (generic).

**Pass 4 — Zone:** Primary failure = **HOOK.** The piece never earns the LOOK; proof and tone are downstream problems that don't matter until something new is revealed.

**Pass 5 — Prioritized fix list:**
1. **HOOK → `./novelty-reveal.md`** (highest leverage): mine a real new angle. e.g. *"There's a reason your gutters clog again six weeks after a cleaning — and it's not the leaves. It's the* pitch *of the gutter, and almost nobody checks it."* New aspect = pitch/slope, outcome = stops the re-clog cycle. Honest if true of the avatar's roofs.
2. **HOOK → `./novelty-contrast.md`**: anchor it to the held belief. *"You've been told gutters just need a twice-a-year clean. For a third of homes, twice a year does nothing — because the water never reaches the downspout in the first place."*
3. **BODY → `./novelty-proof.md`**: climb the ladder. Replace nothing-proof with a mimic: *"Had a homeowner on [your street type] who'd paid for cleanings for years and still got basement water — turned out two runs were pitched backward. One adjustment, dry basement through the whole rainy season."*
4. **Cut entirely:** the fake "limited slots this week" — flag to `./novelty-urgency.md`, which will confirm there's no honest window here and the correct move is to skip urgency, not fake it.

Net: three routed edits convert a flat fail into a piece that earns Novel + Interesting and lands honest proof — without a from-scratch rewrite.

## Content-Type Adaptations

The audit *logic* is constant; what shifts is where each component is expected to live and which zone matters most for that asset.

| Asset | What this audit checks / weights differently |
|---|---|
| **Short-form video script** | Zone HOOK is everything — the first ~2 seconds must carry New Reveal + Outcome or the watch dies. Audit the spoken opener line-by-line; tone (whisper vs. crier) is audible, so grade delivery hard. Proof can be visual (show the mimic), so don't penalize a thin verbal stat if a relatable on-screen example does the work. |
| **LinkedIn post** | The first 1–2 lines pre-"see more" carry Steps 1–3; everything after the fold is Body. Audit the truncation point: does the visible hook earn the click-to-expand? Mascot reveals hide in the humble-brag register ("I'm no expert but…") — scrub those. Whisper tone reads as lowercase, conspiratorial framing. |
| **X/Twitter thread** | Tweet 1 is the entire HOOK zone and must pass alone. Audit each subsequent tweet for re-hook decay. Contrast often lives in tweet 2 ("Everyone does X. Here's why that's backwards."). Proof tweets late — check the Trust-Ladder rung of the example tweet, not a linked study. |
| **Email** | Subject line + preview = the New Reveal + Outcome compression; audit them as the hook. Body carries Contrast and Proof. Watch for town-crier subject lines (ALL-CAPS, "🚨") that fail the Whisper Test on sight. Honest urgency in email is the most-abused lever — scrutinize any deadline for a real basis. |
| **Ad / VSL** | Highest stakes on Honesty Spine and Urgency Honesty — paid + scripted = the place fabrication and fake scarcity creep in. Audit the open (3-sec hook), the contrast pivot, the proof block, and the close separately. A salesy register here is the default failure; grade Whisper Test strictly. |
| **Sales / Landing page** | Above-the-fold headline = Steps 1–3; sub-head = Contrast; body = stacked Proof. Audit the headline for single-job failure (most landing-page headlines do one job). Mascot reveals appear as over-disclaimered fine print that deflates the claim. Proof should be testimonial-as-mimic, not logo-soup. |
| **Long-form article** | The HOOK zone is the title + first paragraph; the deck/sub-head carries Contrast. Body has room for *layered* proof — audit whether it climbs the ladder (mimic story → warm crowd → study) or just dumps third-party citations. Long form forgives a slower reveal but not a missing one. |
| **Ghostwritten thought-leadership** | Audit against the *named person's* avatar and held-belief, not a generic one — Domain Fit is the criterion most at risk. The signature move to verify: is there a *named mechanism* (cheap-novelty lever)? Mascot reveals are deadly here (false modesty undercuts authority); grade Illusion Intact hard. Voice must read as their whisper, not a marketer's crier. |

## Output Requirements

Return a single compact artifact, in this shape:

```
NOVELTY AUDIT — [piece title / first line]
Avatar: [who] · Held belief: [the "old"] · Wanted outcome: [the result] · Honest urgency window: [yes/no]

THREE-QUESTION SCAN
  Relevant: YES/NO  ·  Novel: YES/NO  ·  Interesting: YES/NO   → [one-line read]

COMPONENT CHECK (STRONG / WEAK / MISSING)
  1 New Reveal+Outcome: [status] — [reason + quoted line]
  2 Contrast:            [status] — [reason]
  3 Urgency:             [status / HONEST SKIP] — [reason]
  4 Bullseye Proof:      [status] — [rung reached]
  5 Protect Illusion:    [status] — [mascot reveal? tone?]

RUBRIC (1–10; anchor named for any ≥8; caps/vetoes applied)
  1 Three-Question … 6 Illusion … 9 Domain Fit  → composite [n]/10

PRIMARY FAILURE ZONE: HOOK / BODY / DELIVERY — [why]

PRIORITIZED FIXES (top 1–3, sequenced HOOK→BODY→DELIVERY)
  1. [leak] → [route: ./novelty-*.md] — [the specific fix, with a sample line]
  2. …
  3. …
  CUT/FLAG: [anything to delete, e.g. fake urgency]
```

Keep it scannable — a scorecard, not an essay. The fix list is the payload; the operator should be able to fire the routed workflows immediately.

## Quality Gate

This audit itself must satisfy `../genius.md`:

- **Contrast Integrity (rubric #3):** grade the piece against the avatar's *actual* held belief — if you scored Contrast against a belief you assumed rather than verified, the audit is invalid. Re-run the Pre-Flight Gate.
- **Urgency Honesty (#4) + caps:** apply the automatic ≤4 for any bolted-on urgency you find, and do NOT dock a piece for *correctly skipping* urgency when no honest window exists.
- **Trust-Ladder + Illusion + Whisper (#5–#7):** apply the caps exactly — one mascot reveal = ≤5, salesy register = cap 6, no proof = fail. Don't soften them to be polite about a draft.
- **Anti-patterns scanned:** explicitly check for fake urgency, fabricated proof, mascot reveals (hedge / false modesty / "everyone knows this"), town-crier tone, naked claims, strawman contrast, single-job hooks, generic slop.

**HONESTY SPINE (non-negotiable):** the illusion is of NOVELTY only. When you propose fixes, every suggested reveal, urgency window, and proof example must be REAL for the actual topic and avatar — never fabricate a study, a deadline, or a customer to make the rewrite hit harder. An audit that fixes a flat piece by inventing facts has failed worse than the piece it was repairing.

**Self-check (one line):** Did I score against the *real* held belief, apply every cap honestly, name the single primary failure zone, and route the top fixes to real workflows with sample lines that fabricate nothing?
