---
description: Diagnose why an existing piece isn't landing — score it against the canonical Gut-Check Scorecard (0–2 per component /10) plus the optional 9-criterion deep layer, then return a prioritized, routed fix list.
---

# /novelty-audit — The Novelty Diagnostic (Kallaway's GUT CHECK mode)

This is Kallaway's **GUT CHECK** mode — the source doc's first operating mode (`../references/illusion-of-novelty-doc.md` §0, Overview): paste an existing piece, score it against the canonical Scorecard, name which of the five components are missing/weak, and rewrite the weak lines side-by-side with the originals. The primary scoring instrument is the **canonical Gut-Check Scorecard** (`../references/gut-check-scorecard.md`); this workflow runs it.

Takes any EXISTING piece (a hook, post, script, email, page) that feels flat or under-performs and returns a compact scorecard plus the 1–2 highest-leverage fixes, each routed to the workflow that repairs it. Fire this when something "should be working but isn't," when a draft reads boring on a topic you know is good, or before a rewrite so you cut the right cable instead of redoing the whole thing.

## Pre-Flight Gate

Load `../genius.md` if it is not already hot in this conversation. This audit is only as sharp as the avatar behind it, so answer these from the Decision Framework before scoring — an audit run on a guessed avatar produces a confident-wrong scorecard:

1. **Who is the actual avatar** for this piece, and **what does that avatar already believe** about the topic? (Without the held belief you cannot judge Contrast Integrity — you'll grade against your own assumption, not theirs.)
2. **What outcome does the avatar genuinely want?** (Needed to judge whether Outcome Mapping is present or merely implied.)
3. **Is the topic genuinely new, or old?** Old = the piece needed an angle; a flat old-topic piece almost always failed at Step 1 reveal or Step 2 contrast, not later.
4. **Is there an HONEST urgency window for this topic at all?** If no real window exists, a *missing* urgency component is correct, not a defect — do not dock it.

If the requester cannot supply the avatar and held belief, run that gap first (route to `kallaway-audience-obsession` / ICP work) before auditing. Note it in the scorecard rather than scoring around it.

## Skill Acquisition

- **Primary instrument:** `../references/gut-check-scorecard.md` — Kallaway's own 0–2-per-component /10 table, the Illusion Integrity pass/fail override, the 3-question sanity test, and the canonical output order. This is the go/no-go. Run it first, every time.
- **Canonical source-of-truth:** `../references/illusion-of-novelty-doc.md` — when anything here disagrees with that doc, the doc wins.
- **Always:** `../genius.md` — the five components, the Trust Ladder, the nine rubric criteria with their anchors, and the anti-pattern list (the OPTIONAL deeper layer, subordinate to the scorecard — use it for depth on *why* a 1 is a 1, not as the primary score).
- **The repair workflows you'll route to** (read on demand once you know the failure zone, not all upfront):
  - `./novelty-reveal.md` — fixes a missing or weak New Reveal + Outcome Mapping
  - `./novelty-contrast.md` — fixes a missing, strawman, or unrelated Contrast
  - `./novelty-urgency.md` — adds an honest urgency window (or confirms the correct skip)
  - `./novelty-proof.md` — climbs the Trust Ladder toward the viewer
  - `./novelty-protect.md` — removes mascot reveals and converts town-crier tone to gossip-whisperer
- **When the held belief is missing:** `kallaway-audience-obsession` / ICP skills supply it.
- **When the piece feels novel but doesn't hold past the hook:** the failure is often retention, not novelty — flag a handoff to `kallaway-addictive-storytelling` (`/addiction-loop-architect`) rather than over-fixing the front end.

## Execution

Run the passes in order. Pass 1 IS the audit — the canonical Gut-Check Scorecard produces the go/no-go number. Passes 2–3 are overrides that can veto a high score. Pass 4 is an OPTIONAL deeper layer. Resist the urge to start rewriting mid-audit; diagnose fully, then route.

### Pass 1 — The Canonical Gut-Check Scorecard (PRIMARY — 0–2 per component, /10)

This is the primary scoring instrument. Score each of the five components 0/1/2 against the canonical table (`../references/gut-check-scorecard.md`, lifted from source doc §8). Quote the line that carries each component, or note its absence. Sum for a /10.

| # | Component | 0 points | 1 point | 2 points |
|---|-----------|----------|---------|----------|
| 1 | **New Reveal** | topic presented as-is; nothing framed as new/changed | something framed as new, but vague or buried late | clear reveal of a new thing OR new angle, in the hook zone |
| 2 | **Outcome Mapping** | reveal not tied to anything the viewer wants | outcome implied but generic ("this is great") | reveal explicitly tied to a specific outcome the viewer wants |
| 3 | **Contrast Framing** | no old belief referenced | old way mentioned, but not a true opposite / not next to the new angle | old belief and new angle in the same breath, true opposites |
| 4 | **Urgency** | FAKE urgency present (worse than none — flag it) | no urgency, and none was genuinely available (fine — take the point) | genuine recency or closing window, with a "when" |
| 5 | **Bullseye Proof** | no proof at all | cold third-party proof only (study/stat) | warm-crowd or bullseye proof — someone the viewer sees themselves in |

**The counter-intuitive Urgency rule (do not get this wrong):** an **honest skip earns 1 point, not 0.** A piece with no genuine urgency window caps at **9/10 — and that is correct, not a defect.** Only **FAKE/bolted-on urgency scores 0** (it is worse than none). Never dock a piece for honestly skipping urgency, and never coach inventing a window to chase the 10th point.

Score reading (`../references/gut-check-scorecard.md`): **9–10 + Integrity PASS** = ship (9 is the honest ceiling with no real urgency window) · **6–8** = one or two components carrying 1s, route each to its repair workflow · **≤5, or any Integrity FAIL** = under-built/leaking, rebuild the failing zone before polishing.

### Pass 2 — Illusion Integrity check (PASS/FAIL — overrides the number)

A high score means nothing if the illusion leaks. Two binary gates (source doc §6 / §8):

- **Mascot showing?** Does ANY line hedge, downplay, or admit the idea is old — "this is really just…", "as you probably know…", "this has been around forever, but…", "to be fair, this isn't new…", or the false-modesty family ("I'm no expert but…", "you've probably heard this…")? → **FAIL.** Locate the exact line, cut it, re-score. The single most common silent killer is a mascot reveal sitting inside an otherwise solid piece — hunt for it specifically.
- **Town Crier delivery?** Does it announce like a billboard ("HUGE NEWS, this changes EVERYTHING") instead of whispering a secret? → flag those lines for a register rewrite (gossip-whisperer).

### Pass 3 — The 3-Question Sanity Test (the final gut check)

Would the *target viewer* say YES to all three (source doc §1)? Any NO points straight at the weak component and confirms the score.

| Question | YES if… | Delivered by |
|---|---|---|
| **Relevant** — "do I care?" | the avatar is named or their situation is called out | usually the call-out / Outcome Mapping |
| **Novel** — "is this new to me?" | something has been *revealed* as changed/different | New Reveal (component 1) |
| **Interesting** — "am I intrigued?" | a *gap* opens between held belief and the new reality | Contrast Framing (component 3) |

Relevance is the cheap one and is almost never the true failure. If Novel or Interesting is a NO, that is the zone — and it should already show as a 0/1 in Pass 1.

### Pass 4 — (OPTIONAL deeper layer) The 9-Criterion Rubric

Subordinate to the scorecard. Run this only when an operator wants depth on *why* a component scored a 1, or when the go/no-go is borderline (6–8). It adds what the canonical scorecard doesn't grade explicitly — hook *density*, *domain fit*, and the standalone honesty veto. Score each, **name the anchor** for any score ≥8 (if you can't name it, lower the score), and carry the caps from `../genius.md`:

1. **Three-Question Pass** — all three YES? Missing any = fail.
2. **Hook Density** — opener carries ≥2 components (New Reveal + Outcome min) in ≤2 lines? Single-job hook = cap at 5.
3. **Contrast Integrity** — anchored to the *actual* held belief as a *true opposite*? Strawman/unrelated = confusion = fail.
4. **Urgency Honesty** — if used, is the window real? Fake/bolted-on = automatic ≤4. (Honest skip is *not* docked — mirrors the scorecard's 1-point rule.)
5. **Trust-Ladder Height** — bullseye 9–10 · warm crowd 6–7 · third-party only 5 · no proof = fail. No fabricated proof.
6. **Illusion Intact** — zero mascot reveals? One mascot reveal = automatic ≤5.
7. **Whisper Test** — gossip-whisperer not town-crier? Salesy register = cap at 6.
8. **Honesty Spine** — facts true even though novelty is manufactured? Any fabricated fact = automatic fail.
9. **Domain Fit** — execution adapted to the real asset/platform/vertical? Generic slop = cap at 6.

### Pass 5 — Zone Diagnosis

Collapse the findings into the **primary failure zone** — the one place the most attention is lost. Pieces usually fail in exactly one zone; fix that first.

| Zone | Symptom | Owns components | Tell in the data |
|---|---|---|---|
| **HOOK** | scroll-past; never earns the LOOK | 1, 2, 3 | Pass 1 shows Novel=NO or Interesting=NO; low Hook Density |
| **BODY** | hooks but isn't believed; doubt sets in | 4 | strong opener, third-party-only or absent proof, low Trust-Ladder height |
| **DELIVERY** | believable but feels off / salesy / deflated | 5 | a mascot reveal present, or town-crier tone; Whisper Test fails |

If Pass 3 says the piece is novel and intriguing yet still doesn't hold attention *past* the hook, the failure is retention, not novelty — note "out of scope: hand to `/addiction-loop-architect`" rather than forcing a novelty fix.

### Pass 6 — The 1–2 Highest-Leverage Fixes + Side-by-Side Rewrites

The canonical instruction (`../references/gut-check-scorecard.md`, "How to deliver an audit"): after the score table and the Integrity verdict, give the **1–2 highest-leverage fixes ONLY** — not a laundry list — then rewrite the weak *lines* **side-by-side** with the originals. **Do NOT rewrite the whole script.** Fix the biggest leaks first; one fix per cable. Route each weak component to its repair workflow.

| If the leak is… (the component scoring 0/1) | Fix | Route to |
|---|---|---|
| weak/missing New Reveal or Outcome (rows 1–2) | re-mine the angle, retie to a wanted result | `./novelty-reveal.md` |
| naked claim / strawman contrast (row 3) | anchor the new angle to the real held belief | `./novelty-contrast.md` |
| fake urgency (or a real window left unused) (row 4) | replace with honest window or confirm the skip | `./novelty-urgency.md` |
| third-party-only / no proof (row 5) | climb the Trust Ladder toward the viewer | `./novelty-proof.md` |
| mascot reveal / town-crier tone (Integrity FAIL) | scrub the hedge, drop the voice to a whisper | `./novelty-protect.md` |

**Sequencing rule:** fix the HOOK zone before BODY before DELIVERY — a piece nobody looks at can't be saved by better proof. Stop at the top 2; the long tail rarely moves the number.

### Worked mini-example (fresh topic: gutter cleaning)

**Sample post audited (deliberately flat):**
> "Cleaning your gutters is important for protecting your home. Clogged gutters can cause water damage over time, so it's a good idea to clean them at least twice a year. Most people don't realize how big a problem this can become. Call us today to book a cleaning — limited slots available this week!"

**Pass 1 — Gut-Check Scorecard (0–2 each):**
- 1 New Reveal — **0.** Restates common knowledge ("important / twice a year"); nothing framed as new or changed.
- 2 Outcome Mapping — **1.** Outcome is implied but generic ("protect your home"), not tied to a specific wanted result.
- 3 Contrast Framing — **0.** "Most people don't realize…" gestures at a gap but anchors to nothing the reader actively believes — no true opposite.
- 4 Urgency — **0.** "Limited slots available this week!" is a bolted-on sales deadline with no real basis. FAKE urgency scores 0 (worse than an honest skip).
- 5 Bullseye Proof — **0.** No example, no mimic, not even a study.
- **Total: 1/10.**

**Pass 2 — Illusion Integrity:** No mascot reveal (nothing was built to leak), but the exclamation-point CTA is pure **Town Crier** → flag for register rewrite. Verdict: integrity not FAILED on the mascot gate, but the delivery line needs the whisper.

**Pass 3 — 3-Question Sanity Test:** Relevant? weak-YES ("your home" gestures but never names *who*). Novel? **NO.** Interesting? **NO.** Two NOs confirm the 0s in rows 1 and 3.

**Zone (Pass 5):** Primary failure = **HOOK.** The piece never earns the LOOK; proof and tone are downstream problems that don't matter until something new is revealed.

**Pass 6 — The 1–2 highest-leverage fixes (canonical: top 2 only, side-by-side):**

*Fix 1 — HOOK → `./novelty-reveal.md` + `./novelty-contrast.md`* (rows 1–3, the leaks recovering the most attention): mine a real new angle and anchor it to the held belief.
- Original: *"Cleaning your gutters is important for protecting your home… clean them at least twice a year."*
- Rewrite: *"You've been told gutters just need a twice-a-year clean. For a third of homes, twice a year does nothing — because your gutters are pitched wrong and the water never reaches the downspout."* (New aspect = pitch/slope; outcome = stops the re-clog cycle; anchored to the held belief as a true opposite. Honest if true of the avatar's roofs.)

*Fix 2 — BODY → `./novelty-proof.md`* (row 5): replace nothing-proof with a viewer-mimic.
- Original: *(no proof)*
- Rewrite: *"Had a homeowner on [your street type] who'd paid for cleanings for years and still got basement water — turned out two runs were pitched backward. One adjustment, dry basement all rainy season."*

**CUT/FLAG:** the fake "limited slots this week" — route to `./novelty-urgency.md`, which confirms there's no honest window here, so the correct move is to skip urgency (worth 1 point), not fake it (worth 0).

Net: two routed fixes plus one cut convert a 1/10 flat fail into a piece that earns Novel + Interesting and lands honest proof — without a from-scratch rewrite. The score moves toward 8/10 (with an honest urgency skip capping the ceiling at 9, which is correct).

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

Follow the **canonical output order** (`../references/gut-check-scorecard.md`, "How to deliver an audit"): **(1) score table FIRST**, before any commentary; (2) Illusion Integrity verdict; (3) the **1–2 highest-leverage fixes only**; (4) **side-by-side rewrites** of the weak lines. Never rewrite the whole script. Return a single compact artifact, in this shape:

```
NOVELTY AUDIT (Gut Check) — [piece title / first line]
Avatar: [who] · Held belief: [the "old"] · Wanted outcome: [the result] · Honest urgency window: [yes/no]

1) GUT-CHECK SCORECARD (0–2 each)
   1 New Reveal       [0/1/2] — [quoted line or absence]
   2 Outcome Mapping  [0/1/2] — [reason]
   3 Contrast Framing [0/1/2] — [reason]
   4 Urgency          [0/1/2] — [REAL / honest-skip=1 / FAKE=0]
   5 Bullseye Proof   [0/1/2] — [rung reached]
   ── TOTAL: [n]/10  (9 = honest ceiling if no real urgency window)

2) ILLUSION INTEGRITY: PASS / FAIL
   Mascot line(s): [quoted, or "none"]   Town-Crier line(s): [quoted, or "none"]
   3-question sanity: Relevant [Y/N] · Novel [Y/N] · Interesting [Y/N]

   PRIMARY FAILURE ZONE: HOOK / BODY / DELIVERY — [why]

3) THE 1–2 HIGHEST-LEVERAGE FIXES (sequenced HOOK→BODY→DELIVERY)
   Fix 1 → [route: ./novelty-*.md] — [what to change]
   Fix 2 → [route: ./novelty-*.md] — [what to change]   (only if it moves the number)
   CUT/FLAG: [anything to delete, e.g. fake urgency]

4) SIDE-BY-SIDE REWRITES (weak lines only)
   Original: "[…]"
   Rewrite:  "[…]"
```

Optionally append the 9-criterion deeper layer (Pass 4) when the score is borderline (6–8) or an operator asks *why* a component scored a 1 — never lead with it. Keep it scannable — a scorecard, not an essay. The fix list is the payload; the operator should be able to fire the routed workflows immediately.

## Quality Gate

This audit itself must satisfy the canonical scorecard (`../references/gut-check-scorecard.md`) and `../genius.md`:

- **Scorecard ran first:** the 0–2-per-component /10 table is the score, delivered before any commentary. If you led with prose or the 9-criterion rubric, the audit is out of order — re-issue it.
- **Contrast scored against the REAL belief (scorecard row 3 / rubric #3):** grade the piece against the avatar's *actual* held belief — if you scored Contrast against a belief you assumed rather than verified, the audit is invalid. Re-run the Pre-Flight Gate.
- **Urgency rule applied correctly (scorecard row 4):** FAKE urgency = 0; honest skip = **1** (caps the piece at 9/10, which is correct). Do NOT dock a piece for *correctly skipping* urgency when no honest window exists. In the deeper layer this mirrors rubric #4's automatic ≤4 for bolted-on urgency.
- **Both overrides applied:** Illusion Integrity (any mascot line = FAIL, locate-and-cut; town-crier = rewrite) and the 3-question sanity test ran, and either can veto a high number.
- **Deeper-layer caps (only if Pass 4 was run):** one mascot reveal = ≤5, salesy register = cap 6, no proof = fail. Don't soften them to be polite about a draft.
- **Anti-patterns scanned:** explicitly check for fake urgency, fabricated proof, mascot reveals (hedge / false modesty / "everyone knows this"), town-crier tone, naked claims, strawman contrast, single-job hooks, generic slop.

**HONESTY SPINE (non-negotiable):** the illusion is of NOVELTY only. When you propose fixes, every suggested reveal, urgency window, and proof example must be REAL for the actual topic and avatar — never fabricate a study, a deadline, or a customer to make the rewrite hit harder. An audit that fixes a flat piece by inventing facts has failed worse than the piece it was repairing.

**Self-check (one line):** Did I score against the *real* held belief, apply every cap honestly, name the single primary failure zone, and route the top fixes to real workflows with sample lines that fabricate nothing?
