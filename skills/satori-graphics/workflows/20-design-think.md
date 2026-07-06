---
description: The flagship end-to-end orchestrator — runs the full Satori thinking stack on any design task and terminates in a production-ready brief plus a routed, human-triggered generation command.
---

# 20 — Design-Think Pipeline (/satori-design-think)

> The crown of the skill. One command that thinks a design task all the way from communication problem to a production brief a generation tool can execute — Satori is the brain, the generation tools are the hands.

This is the generative end-to-end. It does not audit an existing layout (that's `/satori-lift-audit`) or run one decision in isolation (that's every other workflow). It **composes** the stack — `/satori-comms-brief` (WF-15), `/satori-concept` (WF-16), `/satori-lift-audit` (WF-01), `/satori-color` (WF-17), `/satori-feeling-calibrate` (WF-19), `/satori-memory-encoding` (WF-08), `/satori-anti-ai-slop` (WF-09), `/satori-perception-gap` (WF-18) — and assembles their outputs into a single artifact routed to the correct generation tool.

Every stage forces a decision before any pixel exists. That is the whole point: **design is decision-making before it is expression** (genius.md, The Underlying Belief). This pipeline is the decision audit, run start to finish, terminating in a spec.

## Pre-Flight Gate

**Use this when**:
- You have a fresh design task (poster, identity, UI screen, social asset, packaging, ad) and need to go from problem → production-ready brief in one pass
- A generation tool (fantastic-posters, Creative Director, product-design-build, Kittl, Higgsfield) is about to be called and you want the thinking layer locked first so the output isn't AI-default slop
- A design came back generic and you want to rebuild it from the communication problem up, not patch the surface
- You want a single defensible artifact a teammate or client can review before anyone spends a cent on generation

**Do NOT use this when**:
- You only need ONE decision — run the specific workflow directly (`/satori-color`, `/satori-memory-encoding`, etc.). The pipeline is overhead if you already know the concept.
- You're auditing a finished layout — use `/satori-lift-audit` + `/satori-flip-test`, not the generative pipeline.
- The brief itself is unclear or unwritten — the pipeline will stall at Stage 1. Fix the brief first (`/satori-comms-brief` alone, or a one-sentence reduction per genius.md GP-08).
- It's pure typography selection (route to Kittl) or DESIGN.md token codification (route to `jack-roberts-design-mastery` / `/design-md-extract`). See genius.md "When NOT to Use Satori Tools."

**Hard rule this workflow enforces**: this pipeline **produces the brief and recommends the generation command — it never auto-fires a paid or cost-gated API**. fantastic-posters (Fal) and Higgsfield are cost-gated in this repo. The human reviews the brief, then triggers generation. See the Handoff Block safety note.

## Skill Acquisition

```
Load: skills/satori-graphics/genius.md
  ├─ The Underlying Belief (decision-before-expression)
  ├─ GP-06 (LIFT System) ........... Stage 3 hierarchy
  ├─ GP-03 (Memory Encoding) ....... Stage 6 memory hook
  ├─ GP-11 (Anti-AI-Slop) .......... Stage 7 imperfection
  ├─ GP-08 (One-Sentence Brief) .... Stage 0 setup
  └─ Anti-Patterns (Auto-Reject) ... Quality Gate

Composed workflows (load each as its stage runs — Tier 1.5 hot-context; if already loaded, skip re-read):
  workflows/15-comms-brief.md    → /satori-comms-brief   (Stage 1)
  workflows/16-concept.md        → /satori-concept       (Stage 2)
  workflows/01-lift-audit.md     → /satori-lift-audit    (Stage 3)
  workflows/17-color.md          → /satori-color         (Stage 4)
  workflows/19-feeling-calibrate.md → /satori-feeling-calibrate (Stage 5)
  workflows/08-memory-encoding.md → /satori-memory-encoding (Stage 6)
  workflows/09-anti-ai-slop.md   → /satori-anti-ai-slop  (Stage 7)
  workflows/18-perception-gap.md → /satori-perception-gap (Stage 8)

Reference (optional):
  references/source-quotes.md    — verbatim grounding
  references/lift-system-decision-criteria.md — Stage 3 scoring
```

## Execution

The pipeline runs nine stages. Each stage **composes** a workflow, **forces one decision**, and **writes one fragment** into the accumulating Production Brief. Do not advance a stage until its decision is locked in a sentence — a stage that outputs "TBD" contaminates every stage downstream.

### Stage 0 — Frame the run (setup, ~2 min)

Before Stage 1, lock two things:

1. **The surface.** Poster/print · logo/identity · UI/product · social/feed · packaging · ad creative. The surface drives the Content-Type Adaptations (below) *and* the final Handoff route. If the task spans surfaces (e.g., a brand system), run the pipeline once per surface and keep the concept (Stage 2) shared.
2. **The one-sentence brief** (genius.md GP-08). Format: *"A [thing] that [verb] [audience] [outcome/feeling]."* If you can't write it, you're not ready to design — stop and gather intent.

Write both to the brief header. Every later decision gets checked against this sentence; if a decision contradicts it, the decision is wrong, not the sentence.

### Stage 1 — COMMS BRIEF (composes `/satori-comms-brief`, WF-15)

**Decision forced**: What is the communication *problem*, and what should the viewer *feel* — in what viewing context?

> *"Apple starts with a communication problem first and only adds what's necessary to solve it."* — Satori

Run WF-15 to produce three locks:
- **Communication problem** — the single thing the design must accomplish, stated as a problem ("nobody believes this drop is limited," not "make a hype poster").
- **Target feeling** — the one emotion the viewer should carry *out* (predictive-empathy framing, genius.md GP-02): the next-60-seconds emotion, not the impact-moment spike.
- **Viewing context** — where/how/at what distance it is seen. Establish the recognition-distance ladder now:

> *"before I touch the typography, I want to ask myself what somebody needs to recognize from 10 m, 5 m, and finally 1 m."* — Satori

Fill the ladder for this surface: **10 m** (what's recognizable across a room / in-feed thumbnail) → **5 m** (what pulls them closer) → **1 m** (what rewards the close read). This ladder is reused in Stage 3 (hierarchy) and Stage 5 (type sizing).

**Writes to brief**: Communication Problem · Target Feeling · Viewing Context + 10/5/1 ladder.
**Gate**: One problem, one feeling, one context. If there are two problems, the design will have two centers and fail Stage 3.

### Stage 2 — CONCEPT (composes `/satori-concept`, WF-16)

**Decision forced**: What is the ONE big idea — the hidden truth the design is built around?

Run WF-16 to generate 3-5 concept directions, then select one. The winner names a **hidden truth**: the non-obvious insight about the audience, product, or moment that the design makes visible. A concept is not a layout or a color — it's the idea that survives being described over the phone.

- Generate directions from the communication problem (Stage 1), not from aesthetics.
- Select on concept strength, not prettiness (genius.md HK-04 — standardized comparison removes the aesthetic confound).
- State the winner as one sentence: *"The hidden truth is [X], so the design [does Y]."*

**Writes to brief**: Selected Concept + Hidden Truth (one sentence) · the 2-4 rejected directions (one line each — proves the winner was chosen, not defaulted).
**Gate**: If the concept can't be described in one sentence without naming a color or font, it's not a concept yet. Re-run.

### Stage 3 — HIERARCHY (composes `/satori-lift-audit`, WF-01 + genius GP-06)

**Decision forced**: What should the viewer notice FIRST — and what gets made quieter or removed so it dominates?

Identify the **leverage point** (LIFT's L): the single element carrying the concept. Then create hierarchy the easy way:

> *"one of the easiest ways to create hierarchy isn't making important things look instantly bigger. It's just making unimportant things quieter or just completely disappeared."* — Satori

Do the subtraction first, the amplification second:
1. **Name the leverage point** — the one thing that must be recognized at 10 m (from Stage 1 ladder).
2. **Quiet or kill the competition** — list every element competing for first-notice. For each: mute (lower contrast/size/saturation), demote (push to 5 m or 1 m tier), or evict (rent test, genius.md GP-01). Removing a competitor buys more hierarchy than enlarging the hero.
3. **Amplify the survivor** — only now apply dominance tools (scale, contrast, isolation, position).
4. **Trace the eye journey** (LIFT's I) — 1st → 2nd → 3rd, ending at the desired action/feeling point.

**Writes to brief**: Leverage Point · Hierarchy/Leverage Map (what dominates, what's quieted, what's evicted) · Eye-journey 1-2-3.
**Gate**: A stranger names the leverage point in <2 sec. Two candidates = you didn't quiet enough; return to step 2.

### Stage 4 — COLOR (composes `/satori-color`, WF-17)

**Decision forced**: What is the strategic palette — and what job does each color do?

Run WF-17 to build a palette from the concept and target feeling, not from trend. Assign **four roles** with hex tokens:
- **Dominant** — the field the eye rests in (~60%).
- **Secondary** — supports and structures (~30%).
- **Accent** — the punctuation, used in ONE place, points at the leverage point (~10%).
- **Neutral/base** — ground, type surface, breathing space.

Every color earns its role or gets cut (rent test). The accent is the color discipline test: if it appears in three places, it's no longer an accent.

**Writes to brief**: Color Tokens table — role · hex · usage note. (These tokens feed the UI/product Handoff DESIGN.md directly.)
**Gate**: Four roles, four hex values, accent confined to one location. Palette must reinforce the Stage 1 feeling, not fight it.

### Stage 5 — FEELING LOCK (composes `/satori-feeling-calibrate`, WF-19)

**Decision forced**: Is the target feeling actually locked across type, color, layout, and surface — or only asserted?

Run WF-19 to calibrate the four feeling levers against the Stage 1 target feeling:
- **Type direction** — weight, contrast, case, rhythm. Set sizes against the 10/5/1 recognition ladder (Stage 1): the 10 m element is the largest, 1 m detail the smallest. Recognition distance decides size before taste does.
- **Color** — confirm the Stage 4 palette delivers the feeling (warm/cool, saturated/muted, high/low contrast).
- **Layout** — density, symmetry/asymmetry, breathing room. Loud brief → soften (genius.md GP-02 predictive-empathy soften).
- **Surface** — texture, finish, material implication (matte vs gloss, paper vs screen, grain vs clean).

Each lever gets one line: *"[lever] = [setting], because the feeling is [target]."*

**Writes to brief**: Feeling Spec — Type direction · Color confirm · Layout · Surface, each tied to the target feeling.
**Gate**: All four levers point the same direction. A "calm" brief with an aggressive typeface fails here — resolve before advancing.

### Stage 6 — MEMORY HOOK (composes `/satori-memory-encoding`, WF-08 + genius GP-03)

**Decision forced**: What does the viewer have to *resolve* — the thing that lodges this design in memory?

Designs that hand-deliver meaning don't get encoded; designs that require a beat of resolution do (genius.md GP-03, HK-08). Run WF-08 to engineer ONE hook via one of four moves:
- **Metaphor substitution** (records arranged as a heart)
- **Absence as presence** (body-shaped empty clothes)
- **Conceptual swap** (Thinker statue with an off-switch for a head)
- **Controlled imbalance** (something deliberately off-grid that demands the eye)

Write a concrete, brief-specific implementation. **If you cannot write a concrete one, leave it blank and flag it — a speculative memory hook is worse than none** (per WF-12 discipline).

**Writes to brief**: Memory Hook — [move] + one-sentence concrete implementation (or BLANK + flag).
**Gate**: The hook whispers a question instead of handing out an answer. If it just decorates, it's not a hook.

### Stage 7 — ANTI-SLOP (composes `/satori-anti-ai-slop`, WF-09 + genius GP-11)

**Decision forced**: Which 3+ human-imperfection moves keep this out of the AI-default template lane?

Run WF-09 to inject a minimum of three deliberate imperfections — "ruin the perfection in a bring-it-to-life way" (genius.md GP-11). Each must pay rent (concept/hierarchy/psychology) and honor the locked concept and palette. Distribute, don't cluster: one at/near the leverage point, one in a secondary zone, one+ at texture level.

Common moves: asymmetric crop · off-rotation glyph (2-7°) · element creep · tapered gradient · color punctuation · hand-drawn line · imperfect alignment · negative-space asymmetry.

**Skip / soften** if the surface demands clinical sterility (medical UI, financial dashboards) — note that and reduce to 2 within trust constraints.

**Writes to brief**: Anti-Slop Moves — 3+ named moves, each with implementation + rent reason + location.
**Gate**: 3+ moves, each paying rent, none breaking legibility or the concept. Clustered or rent-less moves are chaos, not character — reject and re-pick.

### Stage 8 — PERCEPTION CHECK (composes `/satori-perception-gap`, WF-18)

**Decision forced**: Does the *intended* reading match the *perceived* reading — and where's the gap?

Run WF-18 to compare what you intend the design to communicate against what a cold viewer would actually perceive, at each recognition distance (10/5/1). For each gap:
- Name the intended message vs the likely misread.
- Trace the cause to a specific decision (hierarchy, color, hook, type).
- Write a closing directive (a concrete change to a specific element).

This is the fresh-eyes discipline (genius.md HK-03) made mechanical — it catches the flaw the designer has gone blind to.

**Writes to brief**: Perception Gaps — intended vs perceived + closing directives (or "no gaps — clean").
**Gate**: Every material gap has a closing directive that names an element and a change. "Improve clarity" is not a directive.

### Stage 9 — PRODUCTION BRIEF + HANDOFF

**Decision forced**: Assemble everything into one production-ready brief and route it to the correct generation tool.

1. Collate Stages 0-8 into the single artifact (template in Output Requirements).
2. Fold Stage 8's closing directives back into the relevant sections (don't append them — resolve them).
3. Select the Handoff route by surface (Stage 0) and write the ready-to-run command.
4. Attach the safety note: generation is human-triggered and cost-gated.

#### The Handoff Block

| Surface | Route to | Ready-to-run command | Notes |
|---|---|---|---|
| **Posters / stylized graphics** | `skills/fantastic-posters/` | `/fantastic-posters` (feed §Generation Prompt) | **COST-GATED** (Fal wallet, `fal_budget_guard.py`). Pre-flight with `/satori-poster-think` (WF-12) if not already done. |
| **AI images / cinematic video** | Creative Director — `skills/creative-direction/` | `/art-direct` → then generate (Higgsfield / Kittl / Midjourney / Flux) | Higgsfield is **COST-GATED**. `/mood-board`, `/storyboard` for sequences. |
| **UI / product screens** | `skills/product-design-build/` | `/satori-design-md-grid` (WF-13) to inject color tokens → `/design-md-extract` → `/product-build` | Needs a DESIGN.md. **Color tokens from Stage 4 feed it directly** (role → token). |
| **Quick social / motion** | Kittl + Higgsfield | `/kittl-graphic` (static) · Higgsfield (motion) | Higgsfield **COST-GATED**. Kittl for fast typographic/social. |

> **SAFETY NOTE — READ BEFORE GENERATING.** This pipeline **produces the brief and recommends the command. It does NOT auto-fire any paid or cost-gated API.** fantastic-posters (Fal) and Higgsfield are hard-gated in this repo (`directives/` cost-gate, PreToolUse hook). The human reviews the Production Brief, then triggers generation manually — and, if the tool is cost-gated, only after the repo cost gate approves. Satori is the brain; a human hand pulls the trigger.

**Writes to brief**: Full assembled Production Brief + Handoff Block + Generation Prompt + safety note.
**Gate**: The brief is complete, contradiction-free, and a second designer (or a generation tool) could execute it without re-asking. Then, and only then:

> *"That simple habit of forcing every decision to earn its place, that is often the difference between a design that simply looks good, and then one that genuinely does work."* — Satori

## Content-Type Adaptations

The pipeline runs all nine stages every time; the **emphasis** shifts by surface. Weight the stages named below and lighten the rest.

| Surface | Where the pipeline leans | Recognition ladder | Handoff route |
|---|---|---|---|
| **Poster / print** | Stage 2 (concept) + Stage 3 (single dominant leverage point) + Stage 7 (anti-slop) carry it. Physical distance is real — the 10 m read must survive a wall. | 10 m = one hero read, 5 m = headline, 1 m = credits/detail | fantastic-posters (cost-gated) |
| **Logo / identity** | Stage 2 (concept/verb) + Stage 6 (memory hook) are everything; Stage 4 palette is secondary (a logo must survive one-color). Skip heavy Stage 5 surface. Route hierarchy through GP-07/GP-10 not full LIFT. | 10 m = silhouette recognizable, 1 m = construction detail | Creative Director / `/design-md-extract` to codify |
| **UI / product** | Stage 3 (hierarchy = primary action) + Stage 4 (tokens) + Stage 8 (perception = usability) dominate. Stage 7 anti-slop softened toward restraint (function over character). | 10 m = primary CTA/state, 5 m = nav, 1 m = microcopy | product-design-build via DESIGN.md (**Stage 4 tokens feed directly**) |
| **Social / feed** | Stage 1 (thumbnail viewing context) + Stage 3 (thumbnail hierarchy) + Stage 6 (scroll-stopping hook) lead. Transferability across square↔vertical is non-negotiable. | 10 m = thumbnail-legible, 5 m = hook line, 1 m = CTA | Kittl (static) + Higgsfield (motion, cost-gated) |
| **Packaging** | Stage 4 (color = shelf differentiation) + Stage 5 (surface/material) + Stage 8 (shelf perception) carry it. Concept must read from a shelf-distance glance. | 10 m = shelf-block color, 5 m = brand + product, 1 m = ingredients/back | Creative Director / dieline to production |
| **Ad creative** | Stage 1 (target feeling) + Stage 3 (CTA is the unmistakable leverage point) + Stage 7 (escape template-ad slop) lead. Decoration must never outweigh the CTA. | 10 m = message + brand, 5 m = offer, 1 m = CTA/terms | fantastic-posters or Creative Director (both cost-gated) |

## Output Requirements

The deliverable is a **single Production Brief** — one artifact, contradiction-free, generation-ready. It contains, in order:

```markdown
# Production Brief — [design name / surface]

**One-sentence brief**: A [thing] that [verb] [audience] [outcome/feeling].
**Surface**: [poster / logo / UI / social / packaging / ad]

## 1. Communication (Stage 1 · WF-15)
- Communication problem: [...]
- Target feeling (next-60-sec): [...]
- Viewing context + recognition ladder: 10 m [...] · 5 m [...] · 1 m [...]

## 2. Concept + Hidden Truth (Stage 2 · WF-16)
- Selected concept: [one sentence]
- Hidden truth: [the non-obvious insight]
- Rejected directions: [one line each]

## 3. Hierarchy / Leverage Map (Stage 3 · WF-01 / GP-06)
- Leverage point (noticed first): [...]
- Quieted / evicted: [what got muted or removed to create hierarchy]
- Eye journey: 1st [...] → 2nd [...] → 3rd [...]

## 4. Color Tokens (Stage 4 · WF-17)
| Role | Hex | Usage |
|---|---|---|
| Dominant | #______ | ~60% field |
| Secondary | #______ | ~30% structure |
| Accent | #______ | ~10% — ONE location, points at leverage |
| Neutral/base | #______ | ground / type surface |

## 5. Feeling Spec (Stage 5 · WF-19)
- Type direction: [...]  · sizes set against 10/5/1 ladder
- Color: [confirms feeling how]
- Layout: [density / symmetry / breathing]
- Surface: [texture / finish / material]

## 6. Memory Hook (Stage 6 · WF-08 / GP-03)
- [Metaphor / Absence / Swap / Imbalance] — [concrete implementation]  (or BLANK + flag)

## 7. Anti-Slop Moves (Stage 7 · WF-09 / GP-11)
1. [move] — [implementation] — rent: [concept/hierarchy/psychology] — location: [...]
2. [...]
3. [...]

## 8. Perception Check (Stage 8 · WF-18)
- Intended vs perceived gaps: [resolved into sections above, or "clean"]

## 9. HANDOFF
- Route: [tool]
- Ready-to-run command: `[command]`
- Generation prompt: [3-6 sentence prompt encoding concept + primitive + palette + hook + imperfections]
- ⚠️ Generation is HUMAN-TRIGGERED and COST-GATED. This brief does not fire it.
```

The brief is complete only when: every section is filled (or explicitly blanked with a flag), the color tokens carry real hex values, the Handoff has a ready-to-run command, and the safety note is present. Composes WF-01, 08, 09, 15, 16, 17, 18, 19.

## Quality Gate

Before the brief ships, verify against genius.md Anti-Patterns (Auto-Reject) — this pipeline exists to prevent all ten:

- [ ] **No decoration without reason** — every element in the brief pays rent (Stage 3/7 rent test).
- [ ] **Concept before aesthetics** — Stage 2 concept was locked before Stage 4 color / Stage 5 type. Aesthetic-first ordering is an auto-reject.
- [ ] **One leverage point** — Stage 3 produced exactly one; competitors were quieted or evicted, not just out-sized.
- [ ] **Not loud-by-default** — Stage 1/5 engineered the *next* emotion (predictive empathy), not an impact spike at a pre-convinced viewer.
- [ ] **Memory encoding present** — Stage 6 hook invites resolution (or is honestly blanked, never faked).
- [ ] **Anti-slop ≥3** — Stage 7 injected 3+ rent-paying imperfections; the brief doesn't read as an AI default template.
- [ ] **Not more-equals-better** — subtraction (Stage 3 quieting, rent evictions) did more work than layering.
- [ ] **Transferability** — Stage 5 + recognition ladder confirm the concept holds at 10/5/1 and across the surface's formats.
- [ ] **Perception gap closed** — Stage 8 gaps are resolved into the brief, not appended as afterthoughts.
- [ ] **Cost-gate honored** — the brief RECOMMENDS a command and states generation is human-triggered; it did not fire any paid API.

**Pass criteria**: all ten checked. Any unchecked box = the offending stage re-runs before handoff. A brief that "looks comprehensive" but fails a box is a system failure regardless of length — the point is the single truth delivered through the right tool, not volume.

## Related Workflows

**Composed by this pipeline** (run standalone when you need just one decision):
- `/satori-comms-brief` (WF-15) — communication problem + feeling + viewing context
- `/satori-concept` (WF-16) — concept generation + selection, hidden truth
- `/satori-lift-audit` (WF-01) — hierarchy / leverage / eye / friction / transferability
- `/satori-color` (WF-17) — strategic 4-role palette + hex tokens
- `/satori-feeling-calibrate` (WF-19) — lock feeling via type / color / layout / surface
- `/satori-memory-encoding` (WF-08) — resolve-something memory hook
- `/satori-anti-ai-slop` (WF-09) — 3+ human-imperfection injection
- `/satori-perception-gap` (WF-18) — intended vs perceived reconciliation

**Adjacent / pre- and post-pipeline**:
- `/satori-why-before-what` (WF-04) — element rent test; fold into Stage 3/7 if evictions get contested
- `/satori-poster-think` (WF-12) — lighter 4-input pre-flight when the surface is a poster and you don't need the full nine stages
- `/satori-flip-test` (WF-10) — 90-sec structural audit; run on the *generated* output after the human triggers it
- `/satori-design-md-grid` (WF-13) — carries Stage 4 tokens into a DESIGN.md for the UI/product handoff
- `/satori-brand-audit` (WF-14) — when the task spans many touchpoints, audit the system after running this pipeline per surface

**Downstream generation** (human-triggered, cost-gated where noted): `/fantastic-posters` · `/art-direct` (Creative Director) · `/product-build` · `/kittl-graphic` · Higgsfield.
