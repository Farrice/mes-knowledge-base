# Jen Engine — Next Action: Processing Intake Answers

> **Status:** Waiting on Jen's intake questionnaire responses (Google Doc v2 at `16-sygvIU2ZMzDmEvbUisa7OAwDIUmqsBt2jWVTNVMCs`)

---

## When Jen Returns Her Answers

Once Jen completes and returns the 22-question intake questionnaire, execute this workflow:

### Step 1: Distill Intake into VOICE.md + BRAIN.md
**Time:** ~45 min  
**Reference:** `skills/jen-engine/references/brain-load-distill-template.md`

1. Open Jen's completed Google Doc answers
2. Use the distill template to extract:
   - **VOICE.md** (her two registers, signature phrases, cringe list, tone mapping, CTA phrasing)
   - **BRAIN.md** (farm neighborhoods, buyer/seller Qs, ICP, business goal, team roster)
3. Fill in the templates exactly (verbatim quotes from her answers, not paraphrased)
4. Save both files to `_active/clients/jen-listings/01-voice-brain/`

**Checklist:**
- [ ] VOICE.md: Both registers have examples from her answers
- [ ] VOICE.md: Signature phrases are direct quotes from Q3 (not cleaned up)
- [ ] VOICE.md: CTA phrasing is from Q20 (her language, not sales-y)
- [ ] BRAIN.md: Top 5 neighborhoods ranked by importance (from Q8)
- [ ] BRAIN.md: Buyer/seller questions in client voice (from Q9/Q10, not cleaned up)
- [ ] BRAIN.md: ICP matches Q16 exactly (price band, situation, timeline)
- [ ] BRAIN.md: 90-day goal is Q15 verbatim

### Step 2: Submit to Gate 1 Approval
**Time:** ~30 min (live review with Jen)  
**Reference:** `skills/jen-engine/references/gate-1-checklist.md`

1. Read VOICE.md aloud to Jen. Listen for her reactions.
   - Does it sound like her?
   - Any rewrites needed?
2. Review BRAIN.md with her:
   - Are neighborhoods ranked correctly?
   - Is the 90-day goal right?
   - Does she want any team members in content? Under what conditions?
3. Use the gate-1-checklist to verify:
   - Live-read test passes (VOICE.md sounds authentic)
   - Register clarity is distinct (FTHB vs luxury not blended)
   - CTA ownership is clear (not cheesy)
   - Signature phrases are authentic (verbatim, not paraphrased)
   - Fair-housing ready (no demographic language)
4. Get Jen's approval or document specific rewrites needed
5. If approved, document the sign-off:
   - Date reviewed
   - Jen's decision: ✅ APPROVED
6. Commit both files to git

### Step 3: Gate 1 Approved → Unlock Stages 2–7

Once Gate 1 is locked:

**Immediately available:**
```
/jen-research <market>          # Stage 2 only (demand research)
/jen-plan                       # Stage 3 only (video planning)
/jen-scripts                    # Stage 4 only (script pack)
/jen-design                     # Stage 5 only (carousel design brief)
/jen-export                     # Stage 7 only (export/send package)
```

Or run the full pipeline:
```
/jen-engine <listing-url | market | topic>    # Stages 2–7 (pauses at Gate 2)
```

---

## Key Files (Already Built & Ready)

| File | Purpose |
|------|---------|
| `SKILL.md` | 7-stage pipeline definition with all entry points |
| `genius.md` | Execution patterns, quality bars, recovery loops for each stage |
| `workflows/01-full-pipeline.md` | Step-by-step walkthrough for full pipeline run |
| `references/brain-load-distill-template.md` | Template for converting Q1–Q22 into VOICE.md + BRAIN.md |
| `references/gate-1-checklist.md` | Gate 1 approval criteria + recovery patterns |
| `references/gate-2-checklist.md` | Gate 2 approval criteria (production calendar) + recovery |

---

## Estimated Timeline After Intake

| Stage | Task | Est. Time | Blocker |
|-------|------|-----------|---------|
| **1** | Distill + Gate 1 approval | 1.5 hours | Jen's answers |
| **2** | Demand research | 1–2 hours | Gate 1 lock |
| **3** | Video plan + Gate 2 approval | 2–3 hours | Research complete |
| **4** | Script pack | 3–4 hours | Gate 2 lock |
| **5** | Carousel specs | 1–2 hours | Scripts + flags |
| **6** | Design execution | 2–4 hours (design tool) | Carousel specs |
| **7** | Export / send package | 30 min | Design complete |
| **Total** | Brain load → forwardable send | ~11–19 hours | — |

---

## Fair-Housing Compliance Built-In

All stages include fair-housing screening:
- ✅ Gate 1: VOICE.md + BRAIN.md must have zero demographic language
- ✅ Gate 2: Production calendar must pass lint (no steering language, housing-stock only)
- ✅ Stages 4–7: Automated linting via `execution/fair_housing_lint.py` (scripts through export)

No demographic targeting (age, race, family size, schools) is permitted at any stage.

---

## Questions?

- **Gate 1 struggling?** See `references/gate-1-checklist.md` Recovery section
- **Gate 2 struggling?** See `references/gate-2-checklist.md` Recovery section
- **Full pipeline walkthrough?** See `workflows/01-full-pipeline.md`
- **What does each stage do?** See `SKILL.md` (7-stage table with loads/produces)
- **Execution patterns?** See `genius.md` (DO/DON'T guidelines + recovery loops)

---

**Jen Engine is READY. Waiting on intake answers. This file updates when she returns them.**
