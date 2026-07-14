---
date: 2026-07-13
session: operator-guide backfill (guides fleet)
tier: operator-guide
status: enriched
---

# Context Engineering OS — What We Built and How to Use It

> `skills/chase-hughes-context-engineering/` (built 2026-05-30 from Chase Hughes's 23,512-word Modern Wisdom appearance) is the operating layer for one inversion: **stop engineering outcomes — engineer the context where the outcome is inevitable.** Front door: `/ce-design`. Ten `/ce-*` workflows total, every one passing a deterministic Defense/Ethics Gate. Spine: `skills/chase-hughes-context-engineering/SKILL.md` + `genius.md`; companion line-level skill: `chase-hughes-conversational-influence`.

## ⚡ If you only read 10 lines

- Doctrine: behavior ← permission ← context/category ← perception (**PCP**). The planning verb is always "what is upstream of the thing I want?"
- Front door: `/ce-design "<desired end-state>"` → 8-section Context-Design Spec a production expert (Luke Iha, Lara) writes INTO.
- Five internal stages: Upstream → Force-Map → PCP → Conditions-Build → Defense/Ethics Gate → Followability.
- The ethics gate is **deterministic and blocking**: `python3 execution/context_ethics_gate.py check --file <spec-path> --kind spec --workflow ce-design --technique "<named technique>"` — exit 2 = BLOCK, REVIEW = clear named flags in writing, PASS = proceed.
- Be honest about what that gate is: this is a manipulation-capable toolkit with a machine backstop, not a vibe. It blocks manufacturing-chaos-to-sell-the-cure, flags coercive power-asymmetry, and logs every verdict so it can't silently no-op.
- Finished work, not just specs: `/ce-write` (7 verticals → publishable copy) and `/ce-offer` (the offer doctor, 6-axis rebuild).
- Route here on: "engineer the conditions", "make the behavior automatic", "what's upstream of the outcome" (routing binding: `context_engineering` → `ce-design`).
- Defense face: `/ce-defend` — FEAR loop / fractionation / prepackaged-enemy scan, brief-format output.
- `/ce-read` = likelihood, never verdict. "This means they're lying" = automatic fail. Video sources ground via `fetch-video-context.py` first.
- Quality bar: could you defend the full design if the target saw it? If it only works hidden, it fails.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/ce-design` | 8-section Context-Design Spec (the OS front door) | Designing an offer/funnel/launch/onboarding where the action should feel self-chosen |
| `/ce-pcp` | The core atom: condition chain + Perception→Context→Permission drift + the loaded category word | You want just the macro-frame, fast |
| `/ce-followability` | Followability + contagious-confidence build at cause level | On-camera, pitch, leadership, copy authority |
| `/ce-write` | Finished, publishable copy (social/content/media/storytelling/marketing/copywriting/ghostwriting) | You want the psychology fused with a craft expert, done |
| `/ce-offer` | 6-axis offer diagnosis + rebuild (category-flip, named mechanism, value stack, proof ladder) | An offer is weak and you don't know why |
| `/ce-honesty` | Benevolent SMRP sequence (four-wall dissolution) + consent/power pre-flight | Sales discovery, coaching, hard conversations |
| `/ce-read` | Behavioral read: baseline → change-cluster-context → likelihood statement | Reading a person, transcript, or pitch |
| `/ce-source-code` | Emotional-debt root-cause diagnostic + release prescription | Self/coaching depth; memoir-grade content fuel |
| `/ce-defend` | Inoculation brief (technique named + resistance move) | Scanning a feed/pitch/relationship for engineered influence |
| `/ce-build` | End-to-end composite (upstream → ethics gate → production handoff) | A complete offer/campaign/content-system in one run |

## The mental model

1. **Build the recipient, not the pitch.** The amateur reaches for a script or a close. Hughes's inversion: engineer *conditions* — build the perfect recipient first, defer the ask, and the behavior falls out for free and feels self-chosen. "Agreed but didn't act" is the diagnostic tell that you pushed an outcome at a recipient who was never built.

2. **Two skills, two layers, no overlap.** This skill is the macro architecture (PCP, FEAR/fractionation, followability, SMRP, Behavior Suite, COPE, emotional debt, defense) from Modern Wisdom. `chase-hughes-conversational-influence` is the line-level moves (engineered self-conclusion, archetype priming, empathy ladder) from the Unlearn podcast. PCP sets the macro-context; engineered self-conclusion is the line-level move inside it. Stack both when a deliverable needs architecture *and* craft.

3. **The defense is the receipt.** Every offensive mechanic ships with its detection tell, its resistance move, and its ethical deployment. Uncensored by design — you can't deploy ethically what you half-understand, and you can't defend against what you can't name. Intent is the only difference between control and help, and intent gets checked by a machine, not by mood.

## /ce-design — the front door

**What it is.** Input a desired end-state + target + channel; the workflow (`.agent/workflows/ce-design.md`) loads SKILL.md, genius.md, and three references (pcp-and-upstream, context-design-spec, fear-fractionation-pressure), runs the five stages, and emits a spec a production expert executes. Runs standalone or as a Chain Step-3.5 front-end — the routed expert writes INTO the spec, then Steps 5.5/6 run normally.

**When to reach for it.** A direct ask would trigger resistance and the real lever is the context, not the copy. Offers, funnels, launches, onboarding.

**When NOT to.** Multi-deliverable missions → `/supercomputer` composes `/ce-build` instead. Line-level copy polish with the context already right → the conversational-influence skill or the craft expert directly. Anything where the outcome doesn't stand on its own merits — the gate will block it anyway; save the run.

**How to invoke.**

```
/ce-design "<desired end-state>"
```

Then, before the spec ships (Stage 4, BLOCKING):

```bash
python3 execution/context_ethics_gate.py check --file <spec-path> --kind spec --workflow ce-design --technique "<named technique>"
```

## The ethics gate — named honestly

This skill contains brainwashing architecture (the FEAR formula, fractionation), interrogation protocols (SMRP), and behavioral-reading systems. The reason it's deployable rather than radioactive is `execution/context_ethics_gate.py` — a deterministic backstop, also wired into `chain_runner.py` finalize (Step 11.9), per the AI-memory-dependent-observability ban: the check is code, not a persona promising to be good.

What it structurally catches: **manufactured destabilization** (creating chaos/fear/scarcity to sell the cure — BLOCK), **missing defensive reads** (offense shipped without the detection tell — BLOCK/rewrite), **coercive power-asymmetry** (e.g. running SMRP on someone who can't freely exit: employee, subordinate, partner mid-conflict — flagged REVIEW regardless of intent). Every verdict is logged. The prompts-v2 contracts carry the same exit semantics (exit 2 = BLOCK, halt and rewrite).

The honest limit: a gate can catch structure, not motive. A technically-clean spec aimed at a bad end is still on the operator. The quality bar in SKILL.md is the real test — *the target performs the behavior, experiences it as their own choice, and you could defend the full design if they saw it.*

## Composition table

| Stacks with | What compounds | Flow |
|---|---|---|
| Luke Iha (copy) | Spec designs the macro-context; Luke writes line-level copy into it | `/ce-pcp` → hand spec to Luke |
| Lara Acosta (LinkedIn) | Followability + PCP at post level | `/ce-followability` → Lara's template |
| McRaney (deep canvassing) | SMRP four-wall dissolution = belief-change open | `/ce-honesty` → deep-canvass |
| Oren / Grace (positioning) | The loaded category word is a positioning lever | `/ce-pcp` category step → positioning brief |
| `chase-hughes-conversational-influence` | Macro context + line-level self-conclusion | `/ce-design` → `/hughes-feel-clever` inside it |
| `/supercomputer` | Mission cohesion wrapping `/ce-build` | `/ce-build` per deliverable under the anchor |

## Honest edges

- **No ground-truth benchmark exists for behavioral influence**, so at build time finalize capped these deliverables at the 7.25 bimodal ceiling regardless of quality — judge by adversarial verification, not the composite score.
- `/ce-read` outputs likelihood only; treating it as lie detection is an automatic quality-gate fail ("there's no behavior for deception, zero").
- Single-source extraction (one Modern Wisdom appearance, deep as it is) — Hughes's broader corpus isn't folded in.
- The gate's REVIEW verdicts require you to clear each named flag in writing; skipping that quietly defeats the whole design.
