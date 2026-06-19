---
description: The Propaganda Engine OS — point it at ANY objective (content, offer, service, launch, raw idea) and it deploys John Whiting's attention→attraction→pipeline genius end to end, grounding and inferring instead of demanding predetermined inputs. Ships finished, ethics-gated, expert-stacked work that out-produces a solo operator.
tier: system
expert: john-whiting
stacks_with: [autopilot, copy-engine, supercomputer, lara-acosta, nicolas-cole, luke-iha, jeremy-miner, david-mcraney, kallaway]
---

# The Propaganda Engine OS

> "My lead strategy is just basically yell at the people that I want, yell at the people that I don't want, and just force it in front of people. I just bait them with what's on their mind right now and then switch it into here's what you need." — John Whiting

Point this at **any** objective and it deploys the propaganda genius — the way Whiting builds content that gets eyeballs, attention, attraction, and a pipeline — then ships the finished work. No predetermined input set required: it grounds and infers from what already exists, asks only for what's genuinely missing, and never hard-blocks.

**The invariant: propaganda thinking is the constant; the application flexes to the objective.** Content, offer, service, launch, campaign, cold-start, reposition — same brain, different deployment.

**The non-negotiable: it grounds, it does not fabricate.** Not-input-gated means *infer intelligently and label assumptions*, never *invent facts*. Real grounding (your files + cache + research) where it exists; flagged assumptions where it doesn't; a question only when a missing fact is load-bearing and unrecoverable. (Honors `feedback_say-i-dont-know.md` + `directives/quality_assurance.md`.)

---

## Anti-Hoarding Contract (what this WIRES, never rebuilds)

| Capability | Reuses | Never rebuild |
|---|---|---|
| Intent parse · gate-suppression (G1/G2/G3) · parallel fan-out · finalize | `/autopilot` (`intent_to_package.py`, four-field envelope, `chain_runner.py`) | ✅ |
| Ground-once · $0 cache reuse · VOC/market research | `/copy-engine` (`avatar_manifold_runner.py ground`) | ✅ |
| Multi-deliverable cross-phase coherence · anchor memory | `/supercomputer` (`anchor_memory.py`) | ✅ |
| Cost classification on paid steps | `creative_router.py` / cost gate hook | ✅ |
| Craft per asset | the expert roster (Lara, Cole, Luke, McRaney, Kallaway, Georgi…) | ✅ |
| Propaganda intelligence | the 15 `jw-*` workflows (14 genius patterns + the ethics-gate primitive) + `genius.md` | ✅ |
| **NET-NEW (the only thing this file adds)** | the **objective→propaganda-sequence router** + the OS spine | — |

If a phase below needs a capability that already exists, **call it, don't reimplement it.**

---

## Skill Acquisition
Load `genius.md` (full) — all 14 genius patterns, the **VOICE REFERENCE** (Mode A raw / Mode B translate-the-thinking + spine test), the **ETHICS GATE**, the rubric. Load `references/objective-router.md` (the classification map). This OS sequences the other `jw-*` workflows; it does not replace them.

---

## PHASE 0 — Intake (any objective, zero schema)

Accept the objective in whatever form it arrives: a sentence ("make this offer irresistible"), a goal ("get eyeballs on the Authority Flywheel"), a raw idea, a voice-memo transcript, a URL, a pasted draft, a campaign brief. **The objective is the only required input.**

Generate a session slug: `jw-{YYYYMMDDHHMMSS}-{slug-of-objective[:24]}`. (Timestamp passed in, never `Date.now()`.)

Do **not** ask for a structured input set. Whatever's missing, Phase 2 grounds or infers.

## PHASE 1 — Classify through the propaganda lens (NET-NEW)

Read the objective and resolve, via `references/objective-router.md`:

1. **The propaganda job** — which Whiting outcome does this serve?
   `EYEBALLS` (reach/attention) · `ATTRACTION` (belief-shift / desire) · `PIPELINE` (conversion / self-close) · `OFFER` (irresistibility / one-best-client) · `QUALITY` (self-selection / repel wrong-fits). Most objectives stack 2-3.
2. **The objective archetype** → its jw-sequence recipe (router table). E.g. *single content piece*, *content campaign/series*, *offer or service design*, *launch*, *cold-start audience*, *authority build*, *sales asset*, *reposition*.
3. **The stacked experts** for craft (router names them per archetype).
4. **The output shape** — what finished artifacts ship (post set / campaign calendar / sales page / offer doc / asset library).

State it in one line: `Engine: <archetype> · job=<EYEBALLS+PIPELINE> · sequence=[jw-big-domino→jw-objection-arsenal→…] · stack=[lara, luke] · output=<N LinkedIn posts + 1 lead asset>.`

## PHASE 2 — Ground Once (wire copy-engine; this is why it's not input-gated)

Assemble context in priority order, cheapest first, **without halting**:

1. **Your own system (free, instant):** `FARRICE.md`, the active ICP (`_active/linkedin-launch/...`), brand files, `_active/farrice-brand/thought-bank/`, any project `CLAUDE.md`. For client work, the client folder.
2. **The grounding cache (`$0` on reuse):**
   ```bash
   python3 execution/avatar_manifold_runner.py ground --slug <market-slug> --market "<market>" --product "<offer>" --tier <free|lean|deep>
   ```
   WARM → reuse at $0. COLD → cost-preview first (G2); if declined, fall to `--tier free` and BANNER `[MODELED]`. Real market research only when the objective rides on a market you haven't grounded.
3. **Recall (free, model-side):** `mcp__recall__search` for expert/voice/pattern cards (Tier 1.5).
4. **Live research** only if a load-bearing fact is missing and recoverable: `execution/research.py` (Receipt-carrying).

**Grounding rule (the not-narrow contract):** infer aggressively from 1-3; **label every inference as an assumption**; ask a question ONLY when a missing fact is load-bearing AND unrecoverable by grounding. Never hard-block on a missing input — degrade to `[ASSUMED: …]` and keep moving. (This is autopilot's gate-suppression applied to grounding, bounded by the no-fabrication rule.)

## PHASE 3 — Run the propaganda sequence (the spine, adapted)

The constant spine, scaled to the archetype (router says how much of it fires):

1. **Install the big domino** (`jw-big-domino`) — the ONE belief that makes the objective's audience need the outcome. Everything re-anchors to it.
2. **Arm the objections** (`jw-objection-arsenal`) — mine real objections (from grounding); pre-handle each as an asset. (Skip for pure top-of-funnel reach objectives; mandatory for pipeline/offer.)
3. **Engineer self-selection** (`jw-self-selection-filter`) — polarize: repel wrong-fits, magnetize right-fits. Keeps quality upstream.
4. **Set the tone/awareness ladder** (`jw-tone-awareness-ladder`) — meet the audience's rung, walk them to the buying line (or the attention/share line for EYEBALLS jobs).
5. **Produce the assets** — fan out (Phase 3a). Bait with what they want, switch to what they need (Core Philosophy #4).
6. **Architect distribution** (`jw-retargeting-architecture` for paid; `jw-content-cadence-engine` for organic) — frequency + sequencing that force-feeds the 7-hour rule.

### Phase 3a — Parallel asset production (wire autopilot fan-out)
For multi-asset objectives, fan out via parallel Agent calls using autopilot's **four-field envelope** (OBJECTIVE / OUTPUT FORMAT / TOOLS / BOUNDARIES + ANCHORS). One asset per worker; each worker loads the stacked expert the router assigned (e.g. objection-killer → Luke Iha hooks + Jeremy Miner handling; belief-shift → McRaney; render → Lara/Cole). Respect autopilot's read/write posture: **diagnosis/research parallel; final write passes sequential or scope-isolated** (one file path per worker, hard anti-scope clause). HARD CAP 12 workers/phase. Workers write to `.tmp/jw-engine/<session>/` and return ≤500-token summaries + paths.

## PHASE 4 — Gate (fabrication + quality + ethics + spine)

Gate the **full asset file at its path** — never the worker's ≤500-token summary. Every produced asset, before it ships:
0. **Assumption-label audit (the no-fabrication backstop — a checked step, not a vibe).** Scan the asset and its grounding summary for every claim about a number, result, name, date, or market fact. Each must trace to a grounding source OR carry an `[ASSUMED:…]` / `[MODELED]` tag. Any unlabeled, unsourced claim is a **Gate-1 ethics fail** — kill it or label it. This makes "not-input-gated ≠ fabricated" physical instead of promised. (Honors `feedback_ai-memory-dependent-observability.md`: pair the narrative rule with a deterministic check; under 12-worker fan-out, hope is not a control.)
1. **`jw-ethics-gate`** — true claims · real proof · buyer's genuine interest · reversible respect. Line-item, not impression. Fail any → kill or fix.
2. **Spine test** (genius.md Voice Reference, Mode B) — does it still make the wrong-fit uncomfortable and the right-fit feel seen? Sanded-down = fail → restore the edge.
3. **Prose classifier** — `python3 execution/prose_classifier.py check <path>` (G3). FLAGGED → fix via the relevant craft expert (often `/writers-room` or the stacked expert).

## PHASE 5 — Output + Learn

1. Ship finished artifacts to `deliverables/<slug>/` (or the project folder); anchor each via `anchor_memory.py anchor … --ref-for finalize`.
2. **Finalize** each scored deliverable: `chain_runner.py finalize … --skill john-whiting-propaganda-machine --workflow jw-engine --sub-agents <N> --source-request "<objective verbatim>"`.
3. **The surpass loop:** append what worked to the session's record (the `jw-record-month-formula` pattern) so the grounding cache + winning-asset patterns compound. Each run starts warmer and sharper than the last.

---

## Content Type Adaptations (the OS *is* the adaptation layer — these are entry examples)

| Objective you throw at it | What the engine does |
|---|---|
| **"Sell the Authority Flywheel / my coaching offer without calls" ($2K–$5K)** | Full spine. Ground ICP from your files → big-domino for the Invisible Expert → objection arsenal → self-selection → asset library + retargeting plan → gated → shipped. The hero use case. |
| **"Get eyeballs on [topic] this week"** | EYEBALLS job. Big-domino + tone-ladder + cadence-engine; stack Kallaway (share-triggers) + Lara (LinkedIn). Skips heavy objection-handling. Output: a post set engineered for reach + saves. |
| **"Make this offer/service irresistible"** | OFFER job. Routes `jw-one-best-client` + `jw-vehicle-engineer` + big-domino; output: one-sentence offer + sales-page spine + the 3 objections that must die. |
| **"Launch [thing] in 2 weeks"** | Multi-deliverable. Borrows supercomputer cross-phase coherence: pre-launch belief-shift → self-selection → launch assets → retargeting. Anchored dependency graph. |
| **"Cold-start an audience from zero"** | Grounds the market (copy-engine), installs the domino, leads with borrowed-authority + polarization for reach; longer time-to-trust flagged. |
| **A raw voice memo / half-formed idea** | Phase 2 infers the objective + grounds from your files; proposes the archetype it detected (one-line confirm), then runs. No structured brief required — this is the "Frictionless Audio" path. |

## Output Requirements
A **Propaganda Engine Run**: (1) the one-line classification (archetype · job · sequence · stack · output); (2) the grounding summary with every `[ASSUMED:…]` and `[MODELED]` flag visible; (3) the big domino; (4) the finished, post-ready asset(s); (5) the distribution plan; (6) per-asset ethics+spine+prose gate results; (7) the finalize + what-worked log entry.

## Quality Gate
Score against the genius.md rubric. OS-specific:
- **Not-narrow honored?** Did it run from the objective alone, grounding/inferring — not demand a predetermined input set? (If it interrogated instead of grounding, it failed the design intent.)
- **Not fabricated?** Every assumption labeled, every claim real. Not-input-gated never means invented. (Ethics Gate #1 + Factual Grounding Standard.)
- **#1 Reality-grounded · #4 Self-selecting · #5 Edge intact · #6 Leveraged · #7 Ethics · #8 One big domino** — per genius.md.
- **Anti-hoarding honored?** Reused autopilot/copy-engine/roster rather than rebuilding. If it reimplemented existing machinery, fail and rewire.
- **Surpass posture?** Did it use volume × stacked craft × gate × cache, not a single-pass solo draft? A lone unstacked draft is a miss — that's matching Whiting, not surpassing him.

If any load-bearing dimension <6, fix that phase once and re-score.
