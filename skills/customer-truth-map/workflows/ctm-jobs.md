---
description: Phase 4 Step 1 engine — reframe each PAIN from the map into a Job-to-be-Done ("When [situation], I want to [motivation], so I can [desired outcome]"), then surface 1–2 unconsidered angles per job. Jobs point at outcomes, where positioning and offer ideas live, not just features. Outputs a jobs list mapped to source pains.
---

# /ctm-jobs — Reframe Pains into Jobs-to-be-Done (Phase 4, Step 1)

A map of quotes tells you *how* customers talk; this workflow starts telling you *what to do about it.* Take the PAINS section of the Customer Truth Map and reframe each pain into a **Job-to-be-Done** — the deeper progress the customer is trying to make — then propose angles you hadn't considered. Fire this after `/ctm-map`, before `/ctm-gaps` builds the gap table from these jobs.

People don't want your product; they **hire** it to make progress (Jobs-to-be-Done, Clayton Christensen, *Competing Against Luck*). Underneath every pain is a job, and the job points at an **outcome** — and the outcome is where the bigger, more durable ideas live. A reminder feature solves a pain; an outcome-level job can open a whole positioning angle, maybe a whole offer.

## Pre-Flight Gate

Load [`../genius.md`](../genius.md) if it is not already hot in this conversation. Do not reframe a single pain before these are answered — they are the Decision Framework from `../genius.md`, narrowed to what Phase 4 Step 1 consumes.

1. **A built map with a populated PAINS section?** Is there a saved Customer Truth Map from `/ctm-map` with real, source-tagged pain quotes? No map → run `/ctm-map` first. This workflow reframes existing real pains; it never invents a pain to reframe.
2. **One customer, one problem cluster?** Are the pains all the same narrow customer's? Jobs blur the moment two audiences are mixed (the "solo bookkeeper who just lost a big client" test).
3. **Source pains traceable?** Each job will be mapped back to the exact pain quote it came from. The pain quotes must still carry their source tags.
4. **Which output is this feeding?** These jobs feed `/ctm-gaps` next, then copy/content/offer. Reframe at the outcome level so the jobs are useful downstream, not just restated complaints.

## Skill Acquisition

- **Always:** [`../genius.md`](../genius.md) (Genius Pattern 6 "Pain → Job reframe," the Hall-of-Fame follow-up exemplar, Quality Rubric criterion 6 Job Depth).
- **The canonical method:** [`../references/customer-truth-map-guide.md`](../references/customer-truth-map-guide.md) Phase 4 Step 1 — the primary truth; where this workflow diverges, the guide wins.
- **The exact prompt:** [`../references/prompt-library.md`](../references/prompt-library.md) **P5** (expert verbatim — the JTBD reframe format + the unconsidered-angles ask).
- **Upstream input:** `/ctm-map` (the saved map; specifically its PAINS section).
- **Downstream:** the jobs feed `/ctm-gaps` (Pain/Job → Current Fix → Gap), and outcome-level jobs hand off to `/ctm-to-offer` and `/ctm-to-content`.

## Why jobs beat pains (read before reframing)

A **pain** is a complaint at the surface; a **job** is the progress underneath it, stated at the outcome level. The difference is the difference between a feature request and a market position.

Take the guide's own example. Pain: *"I keep forgetting to follow up with leads."* Reframe it to a job: *"When a promising lead goes quiet, I want to stay on their radar without feeling pushy, so I can win the work without nagging."*

- The **pain** points at a feature — a reminder, a notification, a checklist. Solve it and you've built a small thing.
- The **job** points at an outcome — *stay on their radar without feeling pushy.* That phrase isn't a feature; it's a whole positioning angle ("the follow-up that never feels like nagging"), maybe a whole offer. The reframe moved a feature request up to a market position.

That upward move — from "fix this annoyance" to "make this progress" — is the entire point of the phase. A job that just restates the pain in three clauses has failed; a job that surfaces the outcome the customer is actually hiring for has done the work.

## Execution

Each numbered step has a move, a diagnostic, and a template marked *vary, never verbatim*. A worked thread runs through all of them — audience: **solo bookkeepers who just lost a big client.**

### 1. Pull the PAINS and run P5

**Move.** Paste the PAINS section of the map (real, source-tagged quotes) and run prompt **P5** from [`../references/prompt-library.md`](../references/prompt-library.md): for each pain, dig past the surface complaint to the deeper progress the customer is trying to make, and rewrite it as a job.

**Diagnostic:** Did AI keep the source pains attached, or did it abstract them into generic pains? Each job must trace back to a real quote.

### 2. Write each job in the canonical format

**Move.** Every job takes the format from the guide / P5:

> **"When [situation], I want to [motivation], so I can [desired outcome]."**

The three slots do specific work: *situation* = the trigger moment; *motivation* = what they're reaching for; *desired outcome* = the progress they're actually hiring for. The outcome slot is the load-bearing one — it's where positioning and offers come from.

**Diagnostic (the depth test):** Read only the `so I can [desired outcome]` clause. Is it an *outcome* (a state they want to be in) or a *feature* (a thing they want to have)? Outcome → keep. Feature → the job hasn't gone deep enough; push past the first answer.

**Template (vary):** *"When [a big client leaves and the pipeline is suddenly bare], I want to [replace that revenue without panic-pitching], so I can [stop checking my bank app at 2am]."*

### 3. Propose 1–2 unconsidered angles per job

**Move.** For each job, suggest one or two angles the customer (or you) might not have considered that would help them make that progress. The job opened the outcome; the angles are the unexpected routes to it. These are where content hooks and offer ideas seed.

**Diagnostic:** Is each angle aimed at the *outcome* clause, not the *situation*? An angle that just re-solves the surface pain is a feature in disguise.

**Template (vary):** *"Angle: a 'win-back pipeline in 30 days' positioning that reframes the panic moment as the one time prospects are most reachable."*

### 4. Map every job back to its source pain

**Move.** Output a jobs list where each job sits next to the exact source-pain quote it was reframed from. Traceability is the proof the job is grounded in real language and not invented on a slow Tuesday.

**Diagnostic:** Could `/ctm-gaps` open this list and, for every job, see the real quote it rests on? If a job has no source pain, it's a guess — cut it or trace it.

### Worked thread — solo bookkeeper, the jobs list

| Source pain (real, tagged) | Job-to-be-Done | Unconsidered angle(s) |
|---|---|---|
| *"i lost my biggest client friday and i keep recalculating the same number hoping it changes"* — [r/Bookkeeping, 2026-03] | **When** a single big client leaves and the math suddenly doesn't work, **I want to** rebuild predictable revenue fast without desperation-pitching, **so I can** feel safe in my own business again. | (1) reframe the cliff as the *best* prospecting window (urgency reads as availability); (2) a "never-one-client-again" diversification offer. |
| *"honestly im not even sure what id say to land another one this size"* — [r/Bookkeeping, 2026-03] | **When** I need to win a client as big as the one I lost, **I want to** know exactly how to pitch at that tier, **so I can** stop undercharging out of fear. | (1) a "talk to bigger clients" script as lead magnet; (2) positioning around *confidence at the high tier*, not bookkeeping features. |

> Every quote above is `[illustrative]` — placeholders for format only. **A real run reframes harvested verbatim pains only**, each a gate-passed, source-tagged quote from the saved map; the jobs are reframes of those real lines, never invented complaints.

## Content-Type Adaptations

The JTBD format is universal; *which outcome clause matters and how the angles point* shifts by what the jobs will feed.

| Downstream use | How the jobs reframe changes |
|---|---|
| **Feeding `/ctm-gaps`** | Keep jobs tightly tied to a single pain each, so the gap table has a clean Pain/Job column. Outcome clause should name a state competitors and DIY fixes can be measured against. |
| **Feeding `/ctm-to-copy`** | The `so I can [outcome]` clause often *is* the headline promise. Reframe so that clause reads in the customer's own emotional register, not in feature-speak. |
| **Feeding `/ctm-to-content`** | Angles matter most here — each unconsidered angle is a content hook candidate. Push for angles that reframe the situation, since reframes are what make content feel novel. |
| **Feeding `/ctm-to-offer`** | Weight the outcome clause hard — an offer is built on the outcome, not the situation. Flag jobs whose outcomes a current offer doesn't actually deliver; those are offer-extension seeds. |
| **B2B / high-consideration** | Situation often involves multiple stakeholders; split the job by who feels the trigger. Outcome is usually risk-reduction or status, rarely the feature. |
| **B2C / impulse** | Situation is emotional and immediate; outcome is identity or relief. Keep the language raw — the customer's exact emotional words carry the job. |

## Output Requirements

Return, in this order:

1. **A jobs list** — every job in the format *"When [situation], I want to [motivation], so I can [desired outcome],"* with an outcome-level (not feature-level) final clause.
2. **1–2 unconsidered angles per job** — each aimed at the outcome clause, each a candidate hook or offer seed.
3. **Source-pain mapping** — every job sitting next to the exact, source-tagged pain quote it was reframed from.
4. **One-line honesty confirmation:** that every job traces to a real pain from the map and no pain was invented to create a job.

If the map's PAINS section was missing or untraceable, return that as the blocker and route to `/ctm-map` rather than reframing imagined pains.

## Quality Gate

Score against the `../genius.md` Quality Rubric. This workflow **owns criterion 6 (Job Depth)** and must also clear:

- **Job Depth (rubric 6):** pains are reframed to *outcome-level* jobs that open positioning, not just features. A job whose `so I can` clause names a feature (not a state) hasn't gone deep enough — name the matching follow-up exemplar from `../genius.md` or lower the score.
- **Verbatim Integrity (rubric 1) — the veto.** Every job traces to a real, source-tagged pain quote from the map. **A job built on an invented or paraphrased pain is an automatic fail, regardless of every other score** — the reframe is allowed to rewrite the *pain into a job*, never to invent the underlying customer language.
- **Narrowness (rubric 3):** jobs are all the same narrow customer's; mixed-audience jobs blur and produce un-actionable angles.

**Honesty Spine (non-negotiable).** The customer's words are the gold; AI sorts the gold from the pebbles — **organizing, never inventing.** The reframe is permitted to translate a pain into the job underneath it; it is never permitted to invent a pain, a customer, or an outcome the language doesn't support. Every job rests on a real quote, or it doesn't ship.

**Self-check (one line):** *Does every job's outcome clause name a state the customer wants to be in (not a feature), and does every job trace to a real source pain?* If yes, the jobs list ships to `/ctm-gaps`. If no, the failing job goes back to the reframe — push past the first answer to the real outcome.
