# Content Quality Benchmark + Repeatable Recipe

**Established:** 2026-06-19
**Benchmark artifact:** [`ai-boom-content-package.md`](ai-boom-content-package.md) — judged **ship-ready as-is** by Farrice ("I would ship them without even adding anything… they sound like me, feel accurate, hit the tones")
**Verdict in Farrice's bimodal taste:** clear **PASS** (the rare unambiguous one)
**Source trend report:** [`strategy_briefs/Trend_Report_AI-Agentic-x-Wellness.md`](../../strategy_briefs/Trend_Report_AI-Agentic-x-Wellness.md)

> **Purpose of this file:** Record (a) the proven quality bar this output represents, and (b) the *exact* mechanism that produced it, so the process is repeatable on demand for any topic.

---

## 1. The Quality Bar This Represents

This is the level to calibrate against. What "ship-ready" looked like here:

- **Strategically anchored** — built on a single converged thesis (the funnel bifurcation), not a topic summary. Reads as smart-money, not hype-follower.
- **Voice-clean** — zero banned AI-tells survived. Sounds like Farrice (concrete, confident, specific), not like a model.
- **Factually grounded** — every checkable claim verified against a primary source; one fabrication caught and removed pre-delivery.
- **Tangible-asset spine** — content points to a real, repeatable deliverable (the Funnel Bifurcation Audit) that doubles as the consulting offer's front door.
- **Multi-format** — one research spine → 2 LinkedIn posts + newsletter + audio, each format-native.

**Known ceiling (the one gap Farrice flagged):** "Could be a little more tension and emotional impact in some of these." → This is the lever to push a PASS into a *strong* PASS next time (see §4).

---

## 2. What Actually Produced the Quality (honest mechanism)

The two slash commands were the **scaffold**. They did NOT create quality alone. Quality = scaffold × four multipliers:

| Layer | The move | If you skip it |
|---|---|---|
| **Scaffold** | `/hunt-trends` then `/trend-to-newsletter` | No structure; ad-hoc |
| **① Depth** | Ran `/hunt-trends` as **3 parallel deep-research agents** with distinct lenses (macro / vertical intersection / live community pain) + word ceilings | Generic "AI is changing everything" mush. The *convergence* of 3 independent angles on one thesis is the strategic spine. |
| **② Lens** | `/trend-to-newsletter` **loaded Nicolas Cole's `genius.md`**, not just the workflow file | Topic-first content with no offer hook. Cole's tangible-faucet reframe is what made it a *product*, not a post. |
| **③ Voice** | Drafted under the **banned-AI-tells rules** (memory: em dashes ≤1-2, no "not X/it's Y," no triple anaphora, no cheap-question closes, Show>Tell) | It would sound like ChatGPT. These rules are why it sounds like *you*. |
| **④ QA** | **prose-doctor + fact-verifier in parallel** before delivery | prose-doctor cut 14 tells; fact-verifier caught a fabricated stat. The difference between "looks good" and "is good + true." |

**Mechanism in one line:** `scaffold × parallel-depth × expert-lens × voice-constraints × dual-adversarial-QA`. Each layer is load-bearing.

---

## 3. The Repeatable Recipe (copy-paste workflow)

Run this sequence for any topic to reproduce this quality:

### Step 1 — Hunt the trend WITH DEPTH
```
/hunt-trends [topic] + [target audience] + [angle / what makes ME look smart] + [intended formats]
```
**The non-obvious part:** don't accept a single search. The quality came from dispatching **3 parallel `deep-research` agents**, each a different lens:
- **Macro:** what's the big rising signal a founder/buyer cares about?
- **Vertical intersection:** how does it land specifically on MY niche (health/wellness/performance)?
- **Live community pain:** what are real people complaining about / wishing for RIGHT NOW (Reddit, forums) — the "shadow market"?

Give each a **word ceiling** (~550-600 words) and demand sources + confidence labels (VERIFIED/LIKELY/UNCONFIRMED).
→ Synthesize into a Trend Report with a **CONFIRMED wedge** (high desperation + low competition quality = shadow market). *If the three don't converge, there's no spine — go back.*

### Step 2 — Convert to content WITH THE EXPERT LENS
```
/trend-to-newsletter  source = [the Trend Report] + name your lead-candidate angles
```
**The non-obvious part:** actually **read the routed expert's `genius.md`** (here: `skills/nicolas-cole-newsletter-flywheel/genius.md`). Let their model reframe the work. Cole's question — *"what tangible asset does the reader GET, that only I curate?"* — is what turned a topic into a faucet + an offer.
→ Draft every format under the **banned-AI-tells constraints** (from MEMORY.md feedback rules).

### Step 3 — Dual adversarial QA (NON-NEGOTIABLE, run in parallel)
- `prose-doctor` → scans for the banned structural moves, applies surgical fixes, preserves voice.
- `fact-verifier` → inventories every real-world claim, verifies against primary sources, labels confidence, **catches fabrications before they ship.**

### Step 4 — Apply fixes → `chain_runner.py finalize`
Score honestly. In bimodal taste, 7.0-7.5 = marginal/soft-fail; push it or accept with eyes open.

---

## 4. To Push PASS → STRONG PASS (close the "tension/emotion" gap)

Farrice's one note was more emotional impact. Next time, add ONE of these between Step 2 and Step 3:
- **A real, permissioned anecdote** threaded into the hook (the "friend who got asked 'who wrote this'" was illustrative — a *true* version lands harder). This is the single biggest lever.
- A `/vicious-hook` or `/depth-social` pass on the openings specifically for tension.
- A `writers-room` pass (the only thing that reliably adds the emotional "heartbeat" layer per the founding-failure lesson).

**Trade-off:** these add time/tokens. For "good enough to ship," Steps 1-4 suffice. For "this is the best thing I've posted all month," add the emotion pass.

---

## 5. Provenance (this run, for the record)

- 3 deep-research agents (hunt-trends) + prose-doctor + fact-verifier = **5 sub-agents spawned**
- prose-doctor: **14 AI-tells removed**
- fact-verifier: **1 fabrication caught** ("1 in 5 brands accurately represented" — misattributed BMJ figure, not in the 5W study), all 5W stats VERIFIED vs primary source
- Chain finalize: composite 7.25 (marginal in the system's calibration; Farrice's human verdict overrode to clear PASS — a useful data point that the finalize rubric runs *conservative* vs. felt quality)
- Notion trace logged; finalize trace `trace_20260619_061601`
