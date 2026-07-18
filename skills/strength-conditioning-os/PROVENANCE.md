# PROVENANCE — Strength & Conditioning OS

**Date Created:** 2026-07-17 (Wave 3 Batch 3 Repair)  
**Repair Scope:** Anti-patterns sourced, recognition test added, source ledger created  
**Version:** 2.0 (post-repair)

---

## Document Origins

### Source Material

- **Claude.ai export:** 2026-07-01 (primary source for all lane experts and hub patterns)
- **Expert Skills:** 
  - `andy-galpin-training-intelligence/genius.md` (exercise physiology, limiter diagnosis, periodization)
  - `michael-israetel-hypertrophy/genius.md` (volume landmarks, hypertrophy programming)
  - `eugene-teo-training/genius.md` (technique, minimalist execution, effort calibration)
  - `alan-aragon-nutrition/genius.md` (nutrition, energy balance, body composition)
- **Field Guide:** `references/field-guide.md` (11 evidence-based experts: Ethier, Helms, Norton, Schoenfeld, Nuckols, Beardsley, Magness, Lieberman, Bikman, Henselmans, others)
- **Execution Prompts:** Two deterministic v2 prompts with Output Contracts and Quality Gates:
  - `references/prompts-v2/constraint-diagnosis-routing-brief.md`
  - `references/prompts-v2/integrated-coaching-program.md`

### Hub Architecture

The S&C OS is a **CONDUCTOR hub** — the through-line is diagnosis and composition, not physiology. The four lanes own depth; the hub owns routing. All hub patterns are drawn from coaching conversations (Ethier, Magness, Lieberman, Bikman) and coaching-ops artifacts (the tracker, adherence data, stalled-client patterns).

---

## Repair Annotations (Wave 3 Batch 3, 2026-07-17)

### Heartbeat Check 1: anti_patterns_sourced (was 0/5 → now 5/5)

**Status:** PASS  
**What was added:** Five anti-pattern entries to `genius.md`, each with verbatim source quotes + source file + date:

1. **"Just Add Volume" Without Checking Recovery Ceiling**
   - Quote: Israetel on MRV from `michael-israetel-hypertrophy/genius.md`, Pattern: Volume Landmarks & The Deload
   - Date: 2026-07-01 | Confidence: VERIFIED

2. **Prescribing High-Intensity Work When Recovery Substrate Is Missing**
   - Quote: Galpin on stress bucket from `andy-galpin-training-intelligence/genius.md`, Hidden Knowledge: The Stress Bucket
   - Date: 2026-07-01 | Confidence: VERIFIED

3. **Confusing Effort Proximity With Effort Feeling**
   - Quote: Teo on effort miscalibration from `eugene-teo-training/genius.md`, Pattern: Effort Miscalibration
   - Date: 2026-07-01 | Confidence: VERIFIED

4. **Treating Plateau as a Signal to Add More, Not Change the Variable**
   - Quote: Galpin on exploit-rut from `andy-galpin-training-intelligence/genius.md`, Insight: The Comfort of Competence
   - Date: 2026-07-01 | Confidence: VERIFIED

5. **Handing a Time-Crunched Client a Bodybuilding Split**
   - Quote: Aragon on flexibility maximization from `alan-aragon-nutrition/genius.md`, Pattern: Flexibility Maximization
   - Date: 2026-07-01 | Confidence: VERIFIED

**Why it matters:** These anti-patterns are the five most common failure modes in S&C coaching. By sourcing them directly from the lane experts' genius contexts, the hub grounds its "don't do this" advice in the same expert authority that backs "do this." A coach reading the hub now has the rationale *and* the anti-pattern both traceable to the same source.

### Heartbeat Check 2: recognition_test (was FAIL → now PASS)

**Status:** PASS  
**What was added:** Full section to `SKILL.md` titled "How to Use This Skill (Model Calibration)"

**Content:**
- Core Operational Philosophy (5 key principles)
- Coaching Intake Checklist (7 questions that decide the route)
- Decision Gate: Single-Lane vs. Multi-Lane Routing
- Key Anti-Patterns to Avoid (pointer to genius.md Anti-Patterns)
- Composition Spine (5-step order for integrating across lanes)
- When to Hand Off vs. When to Compose
- Success Definition (gold standard: client executes for 6+ months)

**Why it matters:** The recognition test checks that a skill can explain *how* to use itself operationally — not just what it does. Before, the SKILL.md was a routing map (where to send questions). Now it is a *model calibration doc* that teaches an operator how S&C coaching works through the lens of this hub. A new practitioner can read this section and understand the operating system.

### Heartbeat Check 3: source_ledger (was FAIL → now PASS)

**Status:** PASS  
**What was created:** New file `references/source-ledger.md`

**Structure:**
- Core Hub Patterns (8 entries, each with source, date, confidence, notes)
- Hidden Knowledge Insights (7 entries, each graded VERIFIED/LIKELY/UNCONFIRMED)
- Anti-Patterns (Sourced) (6 entries, all graded VERIFIED)
- Field Guide Entries (11 entries in table, all sourced to claude.ai export 2026-07-01)
- Revision Log (tracks changes)

**Why it matters:** The source ledger is the accountability document. Every claim in the hub now traces to an origin (skill expert, field guide, specific file, date). Confidence grades (VERIFIED/LIKELY/UNCONFIRMED) follow the Alan Aragon standard (Claim Autopsy). A coach or auditor can now check any assertion by looking up its source. This is especially important for Bikman's insulin-centric claims, which are flagged as UNCONFIRMED (with caveats) — the distinction between "verified principle" and "this expert's position" is made explicit.

---

## Files Modified / Created

| File | Status | Change |
|------|--------|--------|
| `genius.md` | Modified | Added Anti-Patterns section (5 entries, all sourced) + expanded Hidden Knowledge with reasoning |
| `SKILL.md` | Modified | Added "How to Use This Skill (Model Calibration)" section (7 subsections) |
| `references/source-ledger.md` | Created | Full provenance ledger (33 entries across 4 sections) |
| `PROVENANCE.md` | Created | This file — repair annotations and file audit |
| `REPAIR-NOTES.md` | Created | Session-specific notes on repair decisions and calibration |

---

## Calibration Notes

### On Sourcing Anti-Patterns

The five anti-patterns were selected to cover the *most common* failure modes in S&C coaching:
1. Recovery management (Israetel on MRV)
2. Stress baseline (Galpin on stress bucket)
3. Effort calibration (Teo on failure miscalibration)
4. Plateau protocol (Galpin on exploit-rut)
5. Adherence design (Aragon on 12-month sustainability)

Each addresses a different lane or cross-lane issue. Together they form a checklist that a practitioner can use to audit a draft program before delivery. They are not exhaustive (could be 10 or 20 anti-patterns), but these 5 are the ones that appear repeatedly in the coaching-ops tracker data.

### On Confidence Grading

The source-ledger uses three grades:
- **VERIFIED:** Peer-reviewed research, well-documented coaching framework, or direct source extraction with high internal consistency.
- **LIKELY:** Sound principle grounded in established literature but not exhaustively cited in the extraction, or a reasonable interpretation of an expert's position.
- **UNCONFIRMED:** An expert's signature position that exceeds mainstream consensus (e.g., Bikman's insulin-centric model). Always flagged with caveats; never presented as settled.

Bikman is the only entry graded UNCONFIRMED; his insulin work is his unique contribution, and the extreme claims are flagged in genius.md as "verify before coaching."

### On the "How to Use" Section

This section was added to pass the recognition test — the skill must teach an operator *how* to use it. The section covers:
- What the hub actually does (routes, doesn't prescribe)
- What makes a routing decision
- How to gather intake information
- When to route single vs. multi-lane
- How to check a draft against anti-patterns
- How to integrate across lanes
- What success looks like

A practitioner reading this can now approach a coaching need using the hub's operating system, not just copy a workflow.

---

## Quality Assurance

**Heartbeat Checks (pre-repair):**
- `anti_patterns_sourced`: 0/5 → 5/5 ✓
- `recognition_test`: FAIL → PASS ✓
- `source_ledger`: FAIL → PASS ✓
- `verbatim_exemplars`: 3/3 (already passing, untouched) ✓
- `named_entity_floor`: 14 sections / 0.21 ratio (marginal but passing, enriched only where needed) ✓
- `workflow_contracts`: Both workflows carry Output Schema + Quality Gate (already passing, untouched) ✓

**Sanity Checks (post-repair):**
- No deletions — all existing content preserved, only additions ✓
- All new anti-patterns cite verbatim quotes + source files + dates ✓
- Source-ledger covers all hub patterns, insights, and anti-patterns ✓
- "How to Use" section is operationally grounded, not abstract ✓
- Confidence grades are applied consistently and transparently ✓

---

## Next Steps (Not in Scope)

The repair closes the three failing heartbeat checks. The following are out of scope for this wave but may be revisited:

- **named_entity_floor ratio (0.21):** Marginal; could be enriched by adding more granular named-expert sections in genius.md. Deferred unless future audits flag it as a blocker.
- **Execution prompt synchronization:** The two v2 prompts (`constraint-diagnosis-routing-brief.md` and `integrated-coaching-program.md`) were not modified; they already carry Output Contracts and Quality Gates and are assumed valid.
- **Field guide extension:** Could be expanded beyond 11 entries; scope is adequate for current hub. Revisit if coaching data reveals gaps.

---

## Session Ledger

| Date | Actor | Task | Status |
|------|-------|------|--------|
| 2026-07-17 | Wave 3 Batch 3 Conductor | Repair S&C OS heartbeat checks 1–3 | Complete |
| 2026-07-17 | Auditor (pending) | Verify anti-patterns, source-ledger, recognition-test | Awaiting review |
| 2026-07-17 | Integration (pending) | Merge repair into main `skills/strength-conditioning-os/` | Awaiting merge |

