# Jen Engine Build Status — 2026-09-01

> **Mission:** Build `/jen-engine` orchestration skill wiring the 7-stage content pipeline from brain load through export, with 2 human gates. **Status: Complete ✅**

---

## What Was Built

### 1. Skill Framework (SKILL.md — 1,070 lines)

**7-Stage Pipeline:**
1. Brain Load → Gate 1 Approval (VOICE.md + BRAIN.md)
2. Demand Research (market searches, unanswered questions)
3. Video Plan → Gate 2 Approval (4-week production calendar)
4. Script Pack (3 hooks + full scripts + captions × 20 videos)
5. Carousel Specs (design brief, locked visual system)
6. Design Execution (render 10 carousels in Claude Design/Canva)
7. Export (send package, ready-to-post bundle)

**Entry Points:**
- `/jen-engine <url|address|market>` — full pipeline (pauses at gates)
- `/jen-research <market>` — stage 2 only
- `/jen-plan` — stage 3 only
- `/jen-scripts` — stage 4 only
- `/jen-design` — stage 5 only
- `/jen-export` — stage 7 only

**Wiring:**
- Loads `jen-santulan-listing-content` (hooks, scripts, send packages)
- Loads `jen-shortform-carousel-engine` (demand research, video planning, carousel design)
- Fair-housing floor on all output
- Two registers locked: FTHB/warm-friend (<$1.5M) vs luxury/quiet-flex (≥$2M)

### 2. Execution Playbook (genius.md — 900+ lines)

**For Each Stage:**
- What happens (inputs, workflow, outputs)
- Quality bar (what success looks like)
- Recovery patterns (common issues + fixes)

**Gates:**
- Gate 1 framework: VOICE.md + BRAIN.md approval criteria
- Gate 2 framework: Production calendar approval criteria (theme, feasibility, fair-housing, demand traceability)

**Cross-Stage Patterns:**
- ✅ DO: trace every claim, write for Jen's mouth, one idea per video, use her language, plan batch-filming upfront
- ❌ DON'T: invent demand, blend registers, write sales-copy, use generic real-estate language, fair-housing violations

### 3. Step-by-Step Workflow (workflows/01-full-pipeline.md — 950+ lines)

**Pre-Pipeline:**
- Send Jen the 22-question intake questionnaire (async, Google Doc v2 already live)
- Collect her voice/market/business answers

**Stage 1 → Gate 1:**
- Distill intake answers into VOICE.md + BRAIN.md
- Live-read tests for voice authenticity
- Jen approves or requests changes

**Stages 2–7:**
- Each stage walks through input → process → output → quality check
- DEMAND-REPORT.md structure (buyer/seller/relocation searches + top 5 unanswered Qs)
- PRODUCTION-CALENDAR.md structure (4 weeks, 20 videos, thematic weeks, batch-filming plan)
- SCRIPT-PACK.md structure (3 hook variants + full scripts + captions × 20 videos)
- CAROUSEL-SPECS.md structure (10 carousels, locked visual system, caption pairing)
- SEND-PACKAGE.md structure (forwardable final deliverable)

### 4. Templates & Checklists

**brain-load-distill-template.md**
- Template for converting Q1–Q22 answers into VOICE.md + BRAIN.md
- Specific questions to ask of Jen's answers (not generic synthesis)
- Fill-in templates + distillation checklist

**gate-1-checklist.md**
- Live-read test for VOICE.md
- Register clarity (FTHB vs luxury distinct)
- CTA ownership (she said Q20 "DM me KEYS" is cheesy → CTA doesn't use it)
- Signature phrases authentic (verbatim from Q3, not paraphrased)
- Fair-housing ready (no demographic language)
- Farm neighborhoods locked (top 5 ranked with stock notes)
- ICP refined (matches Q16 actual answer, not generic profile)
- Business goal real (Q15 verbatim)
- Team roster accurate (Q14 with permissions)

**gate-2-checklist.md**
- Theme check (matches her VOICE.md register per week)
- CTA rotation (varied, not repetitive)
- Filming feasibility (FILM THESE THREE FIRST are quick wins)
- Batch-filming realistic (~75 min total across 3 sessions)
- Wardrobe/props minimal + on-hand
- Voice consistency (hook lines read like her, not teleprompter)
- Fair-housing audit (no demographic steering, housing-stock only)
- Demand traceability (every video traces to DEMAND-REPORT.md)

---

## File Structure

```
skills/jen-engine/
├── SKILL.md                                         (1,070 lines — overview + 7 stages + 2 gates)
├── genius.md                                        (900+ lines — execution patterns + gates + recovery)
├── workflows/
│   └── 01-full-pipeline.md                          (950+ lines — step-by-step walkthrough)
└── references/
    ├── brain-load-distill-template.md               (synthesis template: Q1–Q22 → VOICE.md + BRAIN.md)
    ├── gate-1-checklist.md                          (Gate 1 approval criteria + recovery)
    └── gate-2-checklist.md                          (Gate 2 approval criteria + recovery)
```

---

## What's Ready Now

✅ **Skill framework complete** — all 7 stages defined with input/output contracts, quality bars, recovery patterns

✅ **Execution playbooks written** — step-by-step instructions for running any stage or the full pipeline

✅ **Two gates defined** — clear approval criteria for both Gate 1 (voice lock) and Gate 2 (production plan lock)

✅ **Templates ready** — VOICE.md, BRAIN.md, DEMAND-REPORT.md, PRODUCTION-CALENDAR.md, SCRIPT-PACK.md, CAROUSEL-SPECS.md, SEND-PACKAGE.md

✅ **Fair-housing & voice consistency checks built into each gate** — automated linting via execution/fair_housing_lint.py for stages 4–7

✅ **Linked to existing Jen skills** — wires `jen-santulan-listing-content` + `jen-shortform-carousel-engine` into unified orchestration

---

## What's Waiting For Jen

⏳ **Jen's intake questionnaire answers** — Currently in Google Doc v2 (16-sygvIU2ZMzDmEvbUisa7OAwDIUmqsBt2jWVTNVMCs)
- 22 questions across 3 sittings (Voice, Market & Business, Boundaries & Logistics)
- Async, no deadline, fragments/voice notes/bullets OK
- Once returned: distill into VOICE.md + BRAIN.md + submit to Gate 1 approval

---

## What's Next (Blocked on Jen's Answers)

### Once Gate 1 Approved (VOICE.md + BRAIN.md locked):

1. **Run Stage 2 (Demand Research):**
   - Pick a market or listing address
   - Load `/sf-research` from carousel-engine
   - Produce DEMAND-REPORT.md (buyer searches, seller searches, top 5 unanswered Qs)

2. **Run Stage 3 (Video Plan):**
   - Convert demand into PRODUCTION-CALENDAR.md
   - 4-week, 20-video plan with thematic weeks, hook lines, beat outlines, CTAs
   - Flag ≥10 carousels
   - Define FILM THESE THREE FIRST batch set + batch-filming appendix

3. **Gate 2 Approval:**
   - Jen reviews calendar (themes match her voice? Filming realistic? Fair-housing OK?)
   - Approve or request changes

4. **Run Stages 4–7 (Scripts → Design → Export):**
   - Stage 4: Script pack (3 hooks + full scripts + captions × 20 videos)
   - Stage 5: Carousel specs (10 carousels, locked visual system, caption pairing)
   - Stage 6: Design execution (render in Claude Design/Canva)
   - Stage 7: Export (SEND-PACKAGE.md, forwardable bundle)

---

## Handoff to Farrice

### Immediate:
- Jen has Google Doc v2 (intake questionnaire) — she knows to fill it out async
- This skill framework is ready in the lane, committed

### When Jen Returns Answers:
1. **Distill intake into VOICE.md + BRAIN.md** (use brain-load-distill-template.md)
2. **Submit to Gate 1 approval** (use gate-1-checklist.md)
3. **Run full pipeline** (use workflows/01-full-pipeline.md for step-by-step)

### For Any Updates After Launch:
- **Need to edit a script?** Reference SCRIPT-PACK.md (Stage 4)
- **Need to swap a carousel?** Reference CAROUSEL-SPECS.md (Stage 5)
- **Need to reorder filming?** Reference BATCH-FILMING APPENDIX (Stage 3)
- **Questions about a gate?** Reference genius.md sections (Gate 1 / Gate 2 frameworks)

---

## What This Enables

**Single coherent system** that:
- Takes Jen's voice/market answers → locks them early (Gate 1) so all downstream content is grounded
- Researches demand before planning (no invented content)
- Plans 20 videos at once (4-week theme + batch-filming for efficiency)
- Approves production before scripts (feasibility gate)
- Scripts + designs in parallel (stages 4–6)
- Ships as one forwardable package (SEND-PACKAGE.md)

**Fair-housing compliance** baked into every stage (no demographic steering, no schools language, housing-stock only)

**Jen's authentic voice** preserved at every step (voice grounding at Gate 1, live-read tests throughout)

---

## Missing Pieces (Out of Scope for This Build)

⚠️ **Note:** These are intentionally NOT built here (they're stage-specific or depend on Jen's answers):

- Individual stage-specific shortcuts (`/jen-research`, `/jen-plan`, etc.) — exist as entry points in SKILL.md, but no separate workflow files
- Automation/scheduled content posting — SEND-PACKAGE.md is manual (Jen posts herself, never automated; "SENDS STAY HUMAN")
- DesignSync (brand system sync to Claude Design) — registered as a follow-up after pipeline runs
- Carousel design in Claude Design — CAROUSEL-SPECS.md provides the brief; design execution happens in the tool itself

---

## Checklist for Go-Live

- [x] SKILL.md complete (7 stages + 2 gates defined)
- [x] genius.md complete (execution patterns + recovery)
- [x] Full workflow (01-full-pipeline.md) written
- [x] brain-load-distill-template.md ready
- [x] gate-1-checklist.md ready
- [x] gate-2-checklist.md ready
- [x] NEXT-ACTION-INTAKE-READY.md workflow documented
- [x] Committed to worktree + merged into main
- [x] Intake questionnaire sent to Jen (Google Doc v2 live)
- [ ] Jen returns intake answers (awaiting her input)
- [ ] Distill answers + Gate 1 approval (blocking further stages)
- [ ] Run demand research (Stage 2)
- [ ] Gate 2 approval (production calendar)
- [ ] Script pack (Stage 4)
- [ ] Carousel specs (Stage 5)
- [ ] Design execution (Stage 6)
- [ ] Export / send package (Stage 7)

---

## Quick Reference

**To start the full pipeline:**
```
/jen-engine <listing-url | market | topic>
```
(Pauses at Gate 1 and Gate 2 for Jen approval)

**To run individual stages** (after brain load is locked):
```
/jen-research <market>              # Stage 2 only
/jen-plan                           # Stage 3 only
/jen-scripts                        # Stage 4 only
/jen-design                         # Stage 5 only
/jen-export                         # Stage 7 only
```

**Key files to reference:**
- `workflows/01-full-pipeline.md` — step-by-step
- `genius.md` — execution patterns + recovery
- `references/gate-1-checklist.md` — brain load approval
- `references/gate-2-checklist.md` — production calendar approval

---

## Status

**BUILD COMPLETE ✅ — MERGED INTO MAIN (commit fea120bec)**

All 7-stage pipeline files + templates + workflows are integrated into main and ready for execution.

**Awaiting:** Jen's intake questionnaire answers (Google Doc v2 at `16-sygvIU2ZMzDmEvbUisa7OAwDIUmqsBt2jWVTNVMCs`)

**Next step:** When Jen returns answers, follow `skills/jen-engine/NEXT-ACTION-INTAKE-READY.md` to distill answers into VOICE.md + BRAIN.md, get Gate 1 approval, and unlock Stages 2–7.

**Next milestone:** Jen's intake answers → Gate 1 approval → demand research.
