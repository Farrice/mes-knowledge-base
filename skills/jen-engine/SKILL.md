---
name: jen-engine
description: "End-to-end content orchestration for Jen Santulan's listings — 7-stage pipeline from brain-load intake through design export. Wires demand research, video planning, scriptwriting, and carousel design into a single forwardable production system with 2 human gates. Default entry: /jen-engine <listing|market|topic> for full pipeline, or stage-specific: /jen-research, /jen-plan, /jen-scripts, /jen-design."
version: "1.0"
format: orchestration-engine
domain: Real estate content production (LA / SFV)
---

# Jen Engine — Content Production Orchestration

> **Role:** Orchestrates 7 production stages (brain-load → demand research → video plan → scripts → carousel specs → design execution → export) into a single end-to-end system. Wires `jen-santulan-listing-content` + `jen-shortform-carousel-engine` + design tools with two human approval gates. Output: locked voice files, production calendars, script packs, carousel briefs, ready-to-shoot specs, and forwardable send packages.

---

## Pipeline Architecture

### 7 Stages + 2 Gates

| Stage | Trigger | Loads | Produces | Gate |
|-------|---------|-------|----------|------|
| **1. Brain Load** | Intake answers (async form) | Jen's voice/market/business context | `VOICE.md` + `BRAIN.md` | ✅ **Gate 1:** Approve voice lock + brain inputs before research |
| **2. Demand Research** | Gate 1 approved | `/sf-research` from carousel-engine + market context | Demand Report (BUYER/SELLER/RELOCATION searches + top 5 unanswered Qs) | — |
| **3. Video Plan** | Research complete | Demand Report + production calendar template | 4-week Production Calendar (20 videos, thematic weeks, batch-filming notes, top-3 film-first set) | ✅ **Gate 2:** Approve shoot plan + calendar before scripts/design |
| **4. Script Pack** | Gate 2 approved | `/sf-scripts` from carousel-engine + production calendar | 3 hook variants per video + full word-for-word scripts + captions (IG/TikTok/YouTube) + recording run sheet | — |
| **5. Carousel Specs** | Scripts complete (carousel-flagged videos) | `/sf-carousels` brief from carousel-engine + Script Pack captions | Carousel design brief (5–7 slides per carousel, visual system locked, ≤10 carousels from 20-video plan) + caption pairing list | — |
| **6. Design Execution** | Carousel specs locked | Claude Design (or Canva) + brand system | Final carousel PNGs/PDFs + ready-to-post Instagram copy | — |
| **7. Export** | Design complete | Listing send-package template from `jen-santulan-listing-content` | Forwardable send text (one-click-sendable format with all assets, CTAs, scheduling notes) | — |

---

## When to Use

- **New listing content pipeline:** `/jen-engine <url|address|market>` → full 7-stage run (pauses at each gate for approval)
- **Demand research only:** `/jen-research <market>` → stage 2 (requires brain load from a prior run or dry-run)
- **Production planning:** `/jen-plan` → stage 3 (requires demand report)
- **Scripts & captions:** `/jen-scripts` → stage 4 (requires production calendar)
- **Carousel design brief:** `/jen-design` → stage 5 (requires script pack + flagged carousels)
- **Export only:** `/jen-export` → stage 7 (requires all prior stages complete)

---

## Core Dependencies

### Brain Load (Gate 1 Input)

Jen's intake questionnaire (`_active/clients/jen-listings/jen-voice-brain-intake.md`) → 22-question async form covering:
- **Voice** (7 Qs): how she actually talks, phrases/words she uses, what makes her cringe
- **Market & Business** (9 Qs): farm neighborhoods, client questions, business goals, ICP, team roster
- **Boundaries & Logistics** (6 Qs): what she won't talk about, comfort with filming, CTA phrasing, Instagram changes

**Gate 1 Decision:** Approve answers → distill into:
- `VOICE.md` — locked Jen voice profile (registers, signature patterns, anti-patterns)
- `BRAIN.md` — locked business context (neighborhoods, ICP, current goals, team)

### Skills Loaded

- `jen-santulan-listing-content` (4 workflows)
  - `workflows/01-listing-content.md` — hooks-only pass
  - `workflows/listing-package.md` — URL → send package
  - Prompts: `references/prompts-v2/*.md`
  - Fair-housing lint: `execution/fair_housing_lint.py`

- `jen-shortform-carousel-engine` (4 stages)
  - Stage 1: `/sf-research [market]` → Demand Report
  - Stage 2: `/sf-plan` → Production Calendar
  - Stage 3: `/sf-scripts [videos]` → Script Pack
  - Stage 4: `/sf-carousels [batch]` → Carousel briefs

### Design System

- Brand spec: `_active/clients/jen-listings/CLAUDE.md` (register ladder: <$1.5M warm-friend vs ≥$2M "Quiet Flex Elite Advisor")
- Fair-housing floor: no safe/family/schools on camera, housing-stock/price/amenities only
- Carousel banlist (from carousel-engine): no stock photos, no emojis, no gradients, no drop shadows, no clip art

---

## Firing Order (Step-by-Step)

### Pre-Pipeline: Collect Brain Load

1. **Send Jen the intake questionnaire** (Google Doc: `16-sygvIU2ZMzDmEvbUisa7OAwDIUmqsBt2jWVTNVMCs`)
2. **Wait for her async answers** (she fills in voice/market/boundary questions)
3. **Distill into VOICE.md + BRAIN.md:**
   - VOICE.md: registers, signature phrases, anti-patterns, cringe-list, CTA phrasing she owns
   - BRAIN.md: farm neighborhoods (top 5 ranked), typical client Qs, business goals, team roster, ICP refinement

### Stage 1: Gate 1 (Jen Approves Brain Load)

```
Input: Jen's raw intake answers (async form)
Process: Distill into VOICE.md + BRAIN.md
Gate Decision: Does Jen approve voice lock + business context?
Output: Locked VOICE.md + BRAIN.md (now available for all downstream stages)
```

### Stage 2: Demand Research

```
Input: Gate 1 approved + BRAIN.md market context
Command: /jen-research <market | listing address>
Process: Load /sf-research workflow from carousel-engine
  - Google/YouTube search suggestions (LA-specific)
  - People-also-ask, Reddit (r/LosAngeles + neighborhood subs)
  - Facebook/Nextdoor themes
  - LA Times/LAist coverage
  - Zillow/Redfin trends
  - Current-event triggers (rates, insurance, new construction)
Output: Demand Report
  - BUYER SEARCHES (exact phrases + evidence + worry + difficulty)
  - SELLER SEARCHES
  - RELOCATION SEARCHES
  - Top 5 QUESTIONS NOBODY IS ANSWERING (ranked, difficulty-rated)
  - PRODUCE FIRST flags (top 3 items for quick wins)
```

### Stage 3: Video Plan (Production Calendar)

```
Input: Demand Report + Gate 1 approved VOICE/BRAIN
Command: /jen-plan
Process: Load /sf-plan workflow from carousel-engine
  - Convert demand into 4-week, 20-video Production Calendar (Mon–Fri)
  - Theme each week; sequence Mon (strongest hook) / Wed (educational) / Fri (story/timely)
  - Each entry: number + title + demand source + format + hook line + beat outline + CTA + recording note
  - Flag ★ VISUAL-worthy ideas (target ≥10 of 20 carousels)
  - FILM THESE THREE FIRST batch set with same-day micro-plan
  - Batch-filming appendix (group by location for 2–3 shoot sessions)
Output: Production Calendar (locked)
Gate Decision: Does Jen approve shoot plan + production calendar?
  - Confirm themes match her voice (VOICE.md)
  - Confirm locations/props/timing are feasible
  - Confirm no fair-housing violations
```

### Stage 4: Script Pack

```
Input: Gate 2 approved Production Calendar + VOICE.md
Command: /jen-scripts
Process: Load /sf-scripts workflow from carousel-engine
  For each planned video:
  - (A) 3 hook variants [pattern-interrupt] / [stakes] / [specificity] (one marked RECOMMENDED)
  - (B) Full word-for-word script (90–150 spoken words, 30–60s, hook → context → 3 payoff beats → CTA)
  - (C) Bullet version (hook verbatim + 3 beat cues ≤6 words + CTA)
  - (D) THREE caption blocks separately optimized:
    * Instagram (hook-first, 2–4 value lines, keyword CTA, 3–5 hashtags)
    * TikTok (shorter, question-forward)
    * YouTube Shorts (keyword-front-loaded title + description + tags)
  - (E) On-screen text plan (3–5 overlays with timing)
  - Recording run sheet (all 20 videos, shoot-order, call times, props checklist)
Output: Script Pack (complete, press-record ready)
Quality check: Fair-housing lint on all spoken + on-screen text
```

### Stage 5: Carousel Specs (Design Brief)

```
Input: Script Pack + ★ VISUAL-flagged items from Production Calendar
Command: /jen-design
Process: Load /sf-carousels workflow from carousel-engine
  - Select 10 strongest visual ideas from ★ VISUAL flags
  - Spec each carousel at 5–7 slides, 1080×1350:
    * Slide 1: HOOK typographic (≤12 words, legible at 150px)
    * Middle slides: ONE idea per slide (≤25 words, stats as visuals not sentences)
    * Final slide: CTA + @realestatewithjing lockup
  - Enforce banlist: no stock photos, no emojis, no gradients, no drop shadows, no clip art
  - APPROVAL GATE: build ONE sample carousel, get approval, lock visual system
  - Caption pairing list (script-to-carousel mapping)
Output: Carousel Design Brief (portable — ready for Claude Design handoff)
  OR final carousel PNGs/PDFs (if built here)
```

### Stage 6: Design Execution

```
Input: Carousel specs + caption pairing list + VOICE.md + brand system
Process: Render in Claude Design (or Canva)
  - Use brand system from CLAUDE.md (Jen's two registers)
  - Lock the visual system from sample carousel (siblings, not clones)
  - Render all 10 carousels
  - Generate Instagram copy for each (from caption pairing list)
Output: Carousel PNGs/PDFs + ready-to-post IG captions
```

### Stage 7: Export (Send Package)

```
Input: All prior stages complete + carousel PDFs + listing info (if listing-tied)
Command: /jen-export
Process: Load listing-package workflow from jen-santulan-listing-content
  - If listing-tied: generate send package (hooks + scripts + captions + forwardable text)
  - If demand-driven: generate sendable content package (scripts + carousels + captions + posting calendar)
Output: Forwardable send text
  - One-click-sendable format (Slack/email)
  - All assets (scripts, carousel PDFs, captions)
  - Posting calendar (what day/time to post each video)
  - CTAs (keyword DM sequences, comment engagement notes)
```

---

## File Structure & Handoffs

### Brain Load Files (persist for all downstream stages)

```
_active/clients/jen-listings/
├── VOICE.md                      (locked Jen voice, registers, phrases, CTAs)
├── BRAIN.md                      (locked Jen business, neighborhoods, team, ICP, goals)
└── 01-intake/
    ├── jen-intake-raw.md         (original 22-Q answers, as-is)
    └── jen-intake-distilled.md   (synthesis notes for VOICE.md + BRAIN.md)
```

### Per-Project/Per-Listing Files (generated per run)

```
_active/clients/jen-listings/
├── <property-id>/
│   ├── DEMAND-REPORT.md          (Stage 2 output: market searches + unanswered Qs)
│   ├── PRODUCTION-CALENDAR.md    (Stage 3 output: 4-week 20-video plan)
│   ├── SCRIPT-PACK.md            (Stage 4 output: 3 hooks + scripts + captions per video)
│   ├── CAROUSEL-SPECS.md         (Stage 5 output: design brief)
│   ├── CAROUSEL-BATCH/           (Stage 6 output: PNGs/PDFs)
│   │   ├── 01-carousel.png
│   │   ├── 02-carousel.png
│   │   └── ...
│   └── SEND-PACKAGE.md           (Stage 7 output: forwardable send text)
│
└── <market-topic>/               (for non-listing demand-driven content)
    ├── DEMAND-REPORT.md
    ├── PRODUCTION-CALENDAR.md
    ├── SCRIPT-PACK.md
    ├── CAROUSEL-SPECS.md
    └── SEND-PACKAGE.md
```

### Handoff Contracts

- **Gate 1 → Stage 2:** Jen approves VOICE.md + BRAIN.md → Demand Research proceeds
- **Stage 2 → Stage 3:** DEMAND-REPORT.md feeds Production Calendar
- **Stage 3 → Gate 2:** Production Calendar awaits Jen approval on shoot plan + themes + feasibility
- **Gate 2 → Stage 4:** Calendar locked → Script Pack generated with exact hooks/beats from calendar
- **Stage 4 → Stage 5:** Script Pack captions become carousel copy (caption pairing list)
- **Stage 5 → Stage 6:** Design brief or sample-carousel-locked system → batch render
- **Stage 6 → Stage 7:** Carousel PDFs + captions + scripts → send package assembly

---

## Entry Commands

```bash
/jen-engine <listing-url | market | topic>    # Full pipeline (pauses at both gates)
/jen-engine --dry-run                          # Full pipeline without Gate approvals (for preview)

# Stage-specific (for updates/edits)
/jen-research <market>                         # Stage 2 only (requires brain load)
/jen-plan                                      # Stage 3 only
/jen-scripts                                   # Stage 4 only
/jen-design                                    # Stage 5 only
/jen-export                                    # Stage 7 only (requires all prior complete)
```

---

## Quality Gates (Built-In)

1. **Voice Grounding (VOICE.md approval):** Does every line pass Jen's "would I say this?" test?
2. **Fair-Housing Lint (all stages):** No safe/family/schools, no demographic steering, housing-stock/price/amenities only
3. **Demand Verification (Stage 2):** Every search phrase traces to an observed source; no invented demand
4. **Carousel Banlist (Stage 5):** No stock photos, no emojis, no gradients, no drop shadows, no clip art
5. **Speakability (Stage 4):** Scripts read naturally out loud (Jen's mouth, not a teleprompter)
6. **SFV Authority (all content):** Leverages farm neighborhood depth, local landmarks, cross-neighborhood comps, FTHB programs

---

## Quick Reference: Related Skills

- `jen-santulan-listing-content` — individual listing content (hooks, education, neighborhoods, send packages)
- `jen-shortform-carousel-engine` — demand research, video planning, script generation, carousel design
- `voice-calibrate` — for polishing non-Jen content into Jen voice
- `kallaway-addictive-storytelling` — deeper dopamine/curiosity engineering (optional enhancement)

---

## What This Skill Does NOT Do

- ❌ Direct messaging or replying to Jen's audience (SENDS STAY HUMAN)
- ❌ Publishing to Instagram directly (human approval + Jen posts)
- ❌ Inventing demand or writing without research
- ❌ Blending the two registers (FTHB vs luxury are separate)
- ❌ Skipping fair-housing verification

---

## Files

- `SKILL.md` — this file
- `genius.md` — execution patterns, gate decision frameworks, error recovery
- `workflows/01-full-pipeline.md` — step-by-step full-run execution
- `references/brain-load-distill-template.md` — intake answers → VOICE.md + BRAIN.md synthesis
- `references/gate-1-checklist.md` — approval criteria for voice lock
- `references/gate-2-checklist.md` — approval criteria for production calendar
