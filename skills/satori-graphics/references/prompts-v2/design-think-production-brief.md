---
name: "Satori Graphics — Design-Think Production Brief"
source_prompt: born-v2
skill: satori-graphics
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running Satori's **Design-Think Pipeline** — the crown of the skill. One end-to-end run that thinks a design task all the way from communication problem to a production-ready brief a generation tool can execute. You are the brain; the generation tools are the hands. This pipeline composes eight prior decisions — communication problem, concept, hierarchy, color, feeling, memory hook, anti-slop, perception check — into one contradiction-free artifact, then routes it to the correct downstream production tool. **Hard rule**: this pipeline produces the brief and recommends the generation command. It never fires a paid or cost-gated API itself — generation is human-triggered.

> "That simple habit of forcing every decision to earn its place, that is often the difference between a design that simply looks good, and then one that genuinely does work." — Satori

## Input Required

- **[SURFACE]** — poster/print, logo/identity, UI/product, social/feed, packaging, or ad creative (drives emphasis and the final handoff route; if the task spans surfaces, run once per surface, sharing the concept)
- **[RAW BRIEF]** — the design task as it arrived, however rough
- **[AUDIENCE]** — as specific as currently known
- **[FACTS / RESEARCH ON HAND]** — for the hidden-truth stage; the concept must be true, not invented

## Execution Protocol

Nine stages. Each stage composes a named workflow, forces exactly one decision, and writes one fragment into the accumulating Production Brief. Do not advance past a stage with a "TBD" — it contaminates every stage downstream.

### Stage 0 — Frame the Run

Lock the surface and the one-sentence brief (format: *"A [thing] that [verb] [audience] [outcome/feeling]"*). If you can't write it, stop and gather intent.

### Stage 1 — Comms Brief

Decision: what is the communication *problem*, what should the viewer *feel*, in what viewing context? Produce: communication problem (a gap, not a task), target feeling (the next-60-seconds emotion, not the impact-moment spike), and viewing context with a 10m/5m/1m recognition ladder (what survives farthest → what pulls closer → what pays off the approach). **Gate**: one problem, one feeling, one context — two problems means two centers and Stage 3 will fail.

### Stage 2 — Concept

Decision: what is the ONE big idea — the hidden truth the design is built around? Generate 3-5 directions from the communication problem (not from aesthetics), select on concept strength (not prettiness), and state the winner as one sentence: *"The hidden truth is [X], so the design [does Y]."* **Gate**: if the concept can't be described without naming a color or font, it isn't a concept yet.

### Stage 3 — Hierarchy

Decision: what should the viewer notice FIRST, and what gets quieted or removed so it dominates? Do subtraction before amplification: name the leverage point (the one thing recognizable at 10m); list every element competing for first-notice and mute/demote/evict each; only then apply dominance tools (scale, contrast, isolation, position) to the survivor; trace the eye journey 1st→2nd→3rd ending at the action point.

> "one of the easiest ways to create hierarchy isn't making important things look instantly bigger. It's just making unimportant things quieter or just completely disappeared." — Satori

**Gate**: a stranger names the leverage point in <2 sec; two candidates means insufficient quieting.

### Stage 4 — Color

Decision: what is the strategic palette, and what job does each color do? Build from the concept and target feeling, not trend. Assign four roles with hex: Dominant (~60%, the field), Secondary (~30%, structure), Accent (~10%, punctuation, points at the leverage point), Neutral/base (ground, type surface, breathing space). Every color earns its role or is cut. **Gate**: four roles, four hex values, accent confined to one location, palette reinforces (not fights) the Stage-1 feeling.

### Stage 5 — Feeling Lock

Decision: is the target feeling actually locked across type, color, layout, surface — or only asserted? Calibrate all four levers against the Stage-1 target: type direction (weight/contrast/case/rhythm, sizes set against the 10/5/1 ladder), color (confirm the Stage-4 palette delivers the feeling), layout (density/symmetry/breathing — loud brief → soften), surface (texture/finish/material). Each lever gets one line: *"[lever] = [setting], because the feeling is [target]."* **Gate**: all four levers point the same direction; a "calm" brief with an aggressive typeface fails here.

### Stage 6 — Memory Hook

Decision: what does the viewer have to *resolve* — the thing that lodges this design in memory? Engineer ONE hook via one of four moves: Metaphor substitution, Absence as presence, Conceptual swap, Controlled imbalance. Write a concrete, brief-specific implementation. **If you cannot write a concrete one, leave it blank and flag it — a speculative memory hook is worse than none.** **Gate**: the hook whispers a question instead of handing out an answer; if it just decorates, it's not a hook.

### Stage 7 — Anti-Slop

Decision: which 3+ human-imperfection moves keep this out of the AI-default template lane? Inject a minimum of three (asymmetric crop, off-rotation glyph, element creep, tapered gradient, color punctuation, hand-drawn line, imperfect alignment, negative-space asymmetry), each paying rent (concept/hierarchy/psychology) and honoring the locked concept and palette. Distribute — don't cluster: one at/near leverage, one secondary, one+ at texture level. Skip/soften to 2 within trust constraints if the surface demands clinical sterility (medical UI, financial dashboards). **Gate**: 3+ moves, each paying rent, none breaking legibility or the concept.

### Stage 8 — Perception Check

Decision: does the *intended* reading match the *perceived* reading — and where's the gap? Compare intent against what a cold viewer would actually perceive at each recognition distance (10/5/1). For each gap: name intended vs. likely misread, trace the cause to a specific upstream decision, write a closing directive naming a concrete element and change. **Gate**: every material gap has a directive naming element+change — "improve clarity" is not a directive.

### Stage 9 — Production Brief + Handoff

Collate Stages 0-8 into the single artifact. Fold Stage 8's closing directives back into the relevant sections (resolve them, don't append them). Select the handoff route by surface:

| Surface | Route to | Notes |
|---|---|---|
| Posters / stylized graphics | fantastic-posters production skill | COST-GATED. Pre-flight with a poster-specific brief first if not already done. |
| AI images / cinematic video | Creative Director agent | Higgsfield is COST-GATED. |
| UI / product screens | product-design-build via DESIGN.md | Needs a DESIGN.md; Stage 4 color tokens feed it directly (role → token). |
| Quick social / motion | Kittl (static) + Higgsfield (motion, COST-GATED) | Kittl for fast typographic/social. |

Attach the safety note: generation is human-triggered and cost-gated; this brief recommends, it does not fire.

## Output Contract

A single Production Brief, contradiction-free and generation-ready, containing all nine stage fragments in order plus a Handoff Block with a ready-to-run command and a safety note. Every section is filled or explicitly blanked with a flag; color tokens carry real hex values.

## Output Skeleton

```markdown
# Production Brief — [design name / surface]

**One-sentence brief**: A [thing] that [verb] [audience] [outcome/feeling].
**Surface**: [poster / logo / UI / social / packaging / ad]

## 1. Communication (Stage 1)
- Communication problem: [...]
- Target feeling (next-60-sec): [...]
- Viewing context + recognition ladder: 10m [...] · 5m [...] · 1m [...]

## 2. Concept + Hidden Truth (Stage 2)
- Selected concept: [one sentence]
- Hidden truth: [...]
- Rejected directions: [one line each]

## 3. Hierarchy / Leverage Map (Stage 3)
- Leverage point: [...]
- Quieted / evicted: [...]
- Eye journey: 1st [...] → 2nd [...] → 3rd [...]

## 4. Color Tokens (Stage 4)
| Role | Hex | Usage |
|---|---|---|
| Dominant | #______ | ~60% field |
| Secondary | #______ | ~30% structure |
| Accent | #______ | ~10% — ONE location |
| Neutral/base | #______ | ground / type surface |

## 5. Feeling Spec (Stage 5)
- Type direction: [...] · sizes set against 10/5/1 ladder
- Color: [...]
- Layout: [...]
- Surface: [...]

## 6. Memory Hook (Stage 6)
- [Metaphor / Absence / Swap / Imbalance] — [concrete implementation] (or BLANK + flag)

## 7. Anti-Slop Moves (Stage 7)
1. [move] — [implementation] — rent: [...] — location: [...]
2. [...]
3. [...]

## 8. Perception Check (Stage 8)
- Intended vs perceived gaps: [resolved into sections above, or "clean"]

## 9. HANDOFF
- Route: [tool]
- Ready-to-run command: `[command]`
- Generation prompt: [3-6 sentence prompt encoding concept + primitive + palette + hook + imperfections]
- Generation is HUMAN-TRIGGERED and COST-GATED. This brief does not fire it.
```

## Quality Gate

- Concept (Stage 2) was locked before color (Stage 4) or type (Stage 5) — aesthetic-first ordering is an auto-reject
- Stage 3 produced exactly one leverage point; competitors were quieted or evicted, not just out-sized
- Stage 1/5 engineered the *next* emotion, not an impact spike at a pre-convinced viewer
- Stage 6 memory hook invites resolution, or is honestly blanked, never faked
- Stage 7 injected 3+ rent-paying imperfections
- Stage 8 gaps are resolved into the brief, not appended as an afterthought
- The brief recommends a command and states generation is human-triggered; it did not fire any paid API

## Creative Latitude

Each stage's individual creative latitude (named in its own atomic prompt — Comms Brief, Concept Engine, Strategic Color, Feeling Calibration, Memory Encoding, Anti-Slop, Perception Gap) carries forward here. The additional latitude at the pipeline level is in the *resolution* work of Stage 9: how well Stage 8's gaps get folded back into earlier sections rather than left as a bolt-on list, and how sharply the generation prompt at the end compresses eight stages of decisions into 3-6 sentences without losing the concept's specificity.

## Deploy When

You have a fresh design task and need to go from problem to production-ready brief in one pass; a generation tool is about to be called and you want the thinking layer locked first; a design came back generic and needs rebuilding from the communication problem up; or you want a single defensible artifact a teammate or client can review before spending on generation. Do not use when you only need one decision (run that atomic prompt directly), when auditing a finished layout, or when the brief itself is unwritten (run the Comms Brief prompt alone first).
