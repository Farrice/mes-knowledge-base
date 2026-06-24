---
description: "/stanton-produce — end-to-end content production: compose Runia story-gate → Stanton architecture (premise/spine/change/arc) → the right production engine for the format → Stanton clamp-audit QA → voice + fact gates → finished piece. A conductor that orchestrates existing engines; it never rebuilds production."
---

# Produce (Andrew Stanton)
Hand this an objective and raw material and it returns a finished piece. It is a conductor, not a writer: Stanton owns the architecture (what the piece is really about, who its protagonist is, the one change, the clamp) and the QA (does every beat pull), and it routes the actual line-writing to the production engine that already does that job best. The discipline is composition. If this workflow ever starts rewriting copy-engine or parallax from scratch, it has failed — the system already has those, and rebuilding what is good degrades it.

## Pre-Flight
Read before executing:
1. `skills/andrew-stanton-audience-engineering/genius.md` (voice + Decision Framework + Anti-Patterns)
2. `skills/andrew-stanton-audience-engineering/references/implementation.md` (the story stack + which engine to stack per surface)
3. `skills/andrew-stanton-audience-engineering/references/cross-domain-patterns.md` (the per-format translation)

> **🔒 Pre-Flight Gate**: run the **Decision Framework** in `genius.md § Decision Framework`. You must be able to name the premise-sentence, the spine, and the change before any engine is allowed to write a line. No architecture, no production.

## Input Required
- The **objective** (what this piece is for: a sale, a subscribe, a booking, a belief shift, a brand introduction)
- The **format + channel** (LinkedIn post, Substack edition, sales page/VSL, ad/Reel, brand/origin, email sequence, listing, deck, explainer)
- The **raw material** (the take, the research, the proof, the offer, the property, the voice note — whatever exists)
- The **audience** and the one thing they should feel or do at the end
- Anything **locked** (a deadline, a hook, a claim that must appear, a brand voice file)

---

## Workflow

### Step 1: Story gate (is there a story, or a topic?)
Before architecture, confirm there is something to architect. Run the Runia / `story-compass` test in miniature: is there a **want → tension → change**, or just a topic dressed up? If it is a pure explainer (a how-to, a reference) with no change, that is fine — proceed, but flag it so the engine writes it as a *clamped explainer* (the telling carries it), not a forced narrative. If there is a story, continue to full architecture.

```
GATE: [STORY — has want/tension/change] | [TOPIC — explainer, clamp the telling] | [NEITHER — send back for raw material]
```

### Step 2: Stanton architecture (the spine the engine writes into)
Run the four foundation engines in order and record the result as a compact architecture spec. This is the only thing that gets handed to production.

| Engine | Workflow | Output |
|---|---|---|
| Premise | `/stanton-premise-sentence` | one true sentence: character + conflict + conclusion |
| Spine | `/stanton-spine` | the protagonist's fixed wiring + one-liner (want vs. need) |
| Change | `/stanton-change-engine` | the single five-second moment of change the piece builds to |
| Arc | `/stanton-anticipation-uncertainty` + `/stanton-surprising-inevitable` | where the clamp lives + the ending that is surprising yet inevitable |

Keep each to one or two lines. If you cannot land a true premise, stop and dig (a forced premise produces a flat piece no engine can save).

```
PREMISE: ____   SPINE: ____   CHANGE: from ____ → ____   ENDING (surprising+inevitable): ____
```

### Step 3: Route to the production engine (composition, not rebuild)
Hand the architecture spec to the engine that owns this format. Stanton does not write the line unless no engine fits.

| Format / objective | Production engine to stack | Stanton's contribution it carries |
|---|---|---|
| Sales page / VSL / landing / offer | `copy-engine` (→ Stefan Georgi, Jason Fladlien, Luke Iha) | premise + customer spine + clamp + surprising-inevitable close (`/stanton-sales-arc`) |
| Substack / newsletter edition | `parallax` | premise + spine + change + clamp-audit (now wired into parallax Phase 3) |
| Substack / content **series** | `parallax` + `/stanton-series-escalation` | series premise + edition ladder + escalating clamp |
| LinkedIn / short-form | `linkedin-daily` or `ghostwrite` | premise litmus + per-post clamp (now wired into linkedin-daily) |
| Ad / Reel / short video | `/stanton-30sec-arc` (→ Seena Rez, Dara Denney) | one change + pre-skip clamp + opposites |
| Brand / founder origin | `build-bos` / Donald Miller StoryBrand + `/stanton-brand-origin` | spine + opposites conflict + change + wonder beat |
| Email / launch sequence | `copy-engine` + `/stanton-series-escalation` | per-send change + escalating clamp to the offer |
| Listing / real estate | `jen-santulan-listing-content` + `/stanton-spine` | the buyer's spine (want a house, need to feel safe) + emotional staging |
| Deck / explainer / memo (knowledge work) | the relevant doc skill + `/stanton-telling-over-content` | clamp the dry material; rhythm and withheld exposition |
| No engine fits | Stanton drafts directly | `/stanton-telling-over-content` + `/stanton-just-write-the-sentence` |

Give the engine the architecture spec as its brief. Let it write the line in its own (or the brand's) voice. Do not paraphrase its output back into Stanton's voice.

### Step 4: Stanton QA loop (does every beat pull?)
Run the draft the engine returns through the diagnostic layer. This is where most of the lift happens.

1. **`/stanton-clamp-audit`** — walk it beat by beat; mark and re-clamp every slip. (For a series, audit the inter-edition clamp too.)
2. **`/stanton-root-not-symptom`** — if there is a pile of notes, find the one upstream fix before touching surface lines.
3. **`/stanton-fit-the-dinosaur`** — only if the draft revealed it is actually about something other than the premise you locked. Refit on a copy; protect the through-line.

Loop once. If a slip survives one re-clamp, it is a root-cause miss; go upstream, not deeper.

### Step 5: The gates (Chain 5 + 5.5)
Run the standing gates before delivery, in this order:
- **Voice** — the brand/Farrice voice rules for this surface (Stanton sets the arc, the voice rules own the line).
- **Prose** — `python3 execution/prose_classifier.py check <file>` (AI-slop ban bank).
- **Fact** — `fact-verifier` on any real name, stat, date, or claim. No receipt, does not ship.

### Step 6: Finalize (only if it is a real deliverable)
If this is shipping (not a demo), run `chain_runner.py finalize` with the format's type. Stanton + the engine are both credited in the route note.

## Content Type Adaptations
| Format | How the conductor adapts |
|--------|--------------------------|
| Screenplay / film / video | Step 2 runs full; Step 3 routes to the screenplay/video skill; the clamp-audit walks at playback speed, not reading speed. |
| Long-form essay / Substack | Route to `parallax`; the architecture spec becomes parallax's Phase 3 spine; clamp-audit replaces a generic "is it good?" read with a beat-by-beat pull check. |
| Short-form social | Route to `linkedin-daily`/`ghostwrite`; unclamp tolerance is near zero — one flat line and they scroll, so the clamp-audit is the decisive gate. |
| Sales / marketing copy | Route to `copy-engine`; Stanton's premise becomes the lead's organizing sentence and the clamp keeps the proof from going static. |
| Brand / campaign | Route to `build-bos`; the spine + opposites conflict become the brand's narrative core; audit the campaign as one clamped line across assets. |

## Output Format
```
OBJECTIVE: ____   FORMAT/CHANNEL: ____
STORY GATE: [STORY / TOPIC-explainer]

ARCHITECTURE (Stanton):
  PREMISE: ____
  SPINE:   ____
  CHANGE:  from ____ → ____
  ENDING:  ____ (surprising + inevitable)

PRODUCTION ROUTE: [engine used] — voice: [whose]
  (Stanton handed architecture; engine wrote the line)

THE FINISHED PIECE:
  ____________________

QA RECEIPT:
  • Clamp-audit: __ of __ beats held; re-clamped beats: ____
  • Fit-the-dinosaur: [not needed / refit — what changed]
  • Voice gate: [pass] · Prose: [score] · Fact: [VERIFIED/labelled]
```

## Quality Gate
> **🛡️ Anti-Pattern Check**: review against `genius.md § Anti-Patterns` + § Expert-Specific Quality Rubric. Flag and fix before delivering.
- A true premise-sentence, spine, and change existed **before** any line was written; the engine wrote into the architecture, not around a blank page.
- Production was **composed, not rebuilt** — an existing engine wrote the line in its own/the brand's voice; the conductor did not re-implement copy-engine or parallax.
- The draft passed a real beat-by-beat clamp-audit, not a vibe check; named slips were re-clamped and re-walked cold.
- All three gates ran (voice, prose, fact); no unverified real-world claim shipped.
- The output reads as the production engine's/brand's voice, with Stanton invisible in it — the architecture is felt, never announced.

## Common Pitfalls
- **Rebuilding production inside the conductor.** Writing the sales page from scratch here instead of routing to `copy-engine` duplicates a better engine and rots. Recovery: hand the architecture spec to the owning engine; the conductor's job ends at the brief and resumes at QA.
- **Skipping the story gate.** Architecting a topic that has no change yields a forced premise and a flat piece. Recovery: run Step 1; if it is an explainer, route it as a clamped explainer, do not fake a narrative.
- **Letting the engine drift off the premise.** Production engines optimize their own objective and can wander from the spine. Recovery: the clamp-audit in Step 4 checks the draft against the locked premise; anything off-premise gets cut or bent.
- **Paraphrasing the engine's output back into Stanton-voice.** That double-writes and flattens the brand voice. Recovery: Stanton shapes the architecture and audits the pull; the words stay the engine's.
