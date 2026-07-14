# Receipt Validation & QA Checklist

**Purpose**: Verify audit quality, accuracy, and completeness before packaging for website  
**Timing**: Wed 7/16 afternoon (after Jen's listings are audited Tue/Wed morning)  
**Owner**: Farrice (quality gate for receipts)  
**Standard**: ≥95% confidence, 0 false positives, full documentation

---

## Pre-Audit Validation (When Listings Arrive)

### Listing Data Quality
- [ ] **Address complete** — full address, city, state, ZIP present
- [ ] **MLS remarks provided** — full copy-paste from MLS (not summarized)
- [ ] **Remarks length reasonable** — 100–1000 words (typical MLS description)
- [ ] **No corrupted text** — no encoding errors, broken characters, or unreadable sections
- [ ] **Single listing per entry** — not a batch or multi-listing description

**Action if any fail**: Return to Jen with request to resubmit; continue with others.

---

## Audit Execution Validation (After Audits Run)

### Audit Completeness
- [ ] **JSON structure valid** — proper brackets, no syntax errors
- [ ] **All required fields present**:
  - [ ] `listing_address`
  - [ ] `audit_date`
  - [ ] `audit_status` (PASS, VIOLATIONS_FOUND, or HIGH_RISK)
  - [ ] `violation_count` (red_violations, yellow_cautions, blue_improvements)
  - [ ] `violations_by_tier` (all three tiers with details or empty arrays)
  - [ ] `before_after_sample`
  - [ ] `defensibility_statement`
  - [ ] `authority_sources`
  - [ ] `audit_metadata`
- [ ] **No placeholder text** — all fields filled in (no "[TBD]" or "[EXAMPLE]")
- [ ] **Dates consistent** — `audit_date` matches week 1 (2026-07-14 or 2026-07-15/16)

**Action if any fail**: Re-run audit; verify workflow execution.

---

## Accuracy Validation (Critical Gate)

### Violation Detection Accuracy
For each listing, verify that:
- [ ] **No false positives** — violations flagged actually exist in the original text
  - Spot-check: Read the original phrase and confirm it matches the violation description
  - Red flag: If agent/lawyer would disagree with the violation assessment, flag and consult
- [ ] **No false negatives** — common violations not missed
  - Spot-check against HUD Word/Phrase List (tier 1 direct violations especially)
  - Cross-ref against `references/hud-word-phrase-list.md` for missed patterns
  - Red flag: Obvious "perfect for families" or "ideal for retirees" not caught = re-run audit
- [ ] **Confidence level justified** — stated confidence matches violation density
  - **HIGH** = ≥3 violations with direct case-law match, or 1–2 explicit violations
  - **MEDIUM** = 2–3 violations with mixed case-law/HUD guidance support
  - **LOW** = edge-case or novel violations; should be rare in Week 1
- [ ] **Citation accuracy** — case law and CFR cited correctly
  - Spot-check: Does "Fair Housing Council v. 1734 East 82nd Street (9th Cir. 2019)" exist? (Yes, it's a real 2019 case)
  - Red flag: CFR sections like "24 CFR §100.75" — verify against actual HUD regulations (confirmed valid)

**Action if any fail**: 
- Mild (1 false positive in 10 audits): Log, note, continue; escalate if pattern emerges
- Severe (multiple false positives; missed obvious violation): Re-run full audit; check workflow

---

### Compliant Rewrite Quality
For each RED and YELLOW violation:
- [ ] **Rewrite preserves property truth** — agent would approve the rewrite as accurate
  - "Perfect for families" → "Spacious home ideal for households of all sizes" ✓ (preserves size/space truth)
  - "Ideal for retirees" → "Low-maintenance layout" ✓ (preserves maintenance truth)
  - Red flag: Rewrite removes key selling point agent cares about
- [ ] **Rewrite eliminates violation** — compliant version has no violation language
  - Scan rewrite for banned phrases (families, retirees, active, safe, quiet, etc.)
  - Red flag: Rewrite still contains problematic language
- [ ] **Rewrite is actionable** — agent could copy-paste into MLS without further editing
  - Red flag: Rewrite is vague ("Remove language") instead of specific ("Replace with...")

**Action if any fail**: Request rewrite adjustment; re-run if needed.

---

### Before/After Sample Quality
- [ ] **Before excerpt is direct quote** — verbatim from original MLS remarks
- [ ] **After excerpt is offered rewrite** — shows what compliant version looks like
- [ ] **Both excerpts are parallel length** — roughly equivalent word count (±20%)
- [ ] **Sample is representative** — shows the main violations in the listing (not just one small phrase)

**Action if any fail**: Regenerate or manually fix sample section.

---

## Documentation Validation (Marketing Readiness)

### Authority & Defensibility
- [ ] **Defensibility statement present** — explains audit compliance with HUD standards
- [ ] **Case law citations present** — at least 1–2 case-law citations per audit
- [ ] **Authority sources listed** — `authority_sources` array is not empty
- [ ] **CFR/statute citations accurate** — "42 U.S.C. §3604," "24 CFR §100.75" are real references
- [ ] **No generic language** — no vague "industry standards" or "best practices"

**Action if any fail**: Supplement with actual citations; reference genius.md for cases.

### Agent Education
- [ ] **Education section present** — `agent_education` with headline, pattern, fix_approach, benefit
- [ ] **Tone is educational, not punitive** — "here's the pattern" not "you violated"
- [ ] **Specific examples** — references actual phrases from the listing, not generic examples

**Action if any fail**: Rewrite education section with specific phrases.

### Next Steps
- [ ] **Next steps are actionable** — agent could follow them without further guidance
- [ ] **Timeline is realistic** — "10–15 minutes to edit" for actual complexity level
- [ ] **MLS resubmission process clear** — explains how/when to resubmit

**Action if any fail**: Revise next steps for clarity.

---

## Visual/Marketing Validation

### Receipt as Social Proof
For website/LinkedIn use:
- [ ] **Before/after sample is compelling** — visibly shows compliance improvement
  - Red flag: "Before" text is already mostly compliant; weak proof of violation
  - Red flag: "After" is unrecognizable rewrite; looks too different
- [ ] **Violation count is clear** — easy to see "2 RED violations corrected"
- [ ] **Address is anonymizable** — if needed, can be masked for privacy without losing proof value
  - Example: "4-Bed Home, San Fernando Valley" works if full address is sensitive

**Action if any fail**: Flag for optional anonymization; document if needed.

---

## Meta-Validation (Process Quality)

### Audit Metadata
- [ ] **Auditor version is consistent** — all audits show "RE-1 Fair Housing Listing-Copy Auditor v1.0"
- [ ] **Audit duration is reasonable** — all audits between 5–15 minutes (typical for listings of this complexity)
- [ ] **Workflow path is correct** — all audits cite `workflows/01-fh-auditor.md`
- [ ] **Audit date is week 1** — all show 2026-07-14, 2026-07-15, or 2026-07-16

**Action if any fail**: Verify workflow execution; check for stale/cached results.

---

## Aggregate Quality Check (10 Receipts)

After all 10 audits pass individual validation:

- [ ] **Status distribution reasonable**:
  - Expected: ~5–6 VIOLATIONS_FOUND, 1 PASS, 1–2 HIGH_RISK (typical SFV listing violations)
  - Red flag: All 10 show PASS (unrealistic; real agents make mistakes)
  - Red flag: All 10 show HIGH_RISK (suggests audit is over-flagging)
  
- [ ] **Violation type distribution diverse**:
  - Expected: Mix of RED violations, YELLOW cautions, dog-whistle codes
  - Red flag: All violations are the same type (e.g., only familial status, never age or disability)
  
- [ ] **No duplicate audits** — each receipt is a unique listing, not a copy
  
- [ ] **Confidence levels are calibrated** — not all HIGH or all MEDIUM; mix based on violation density

**Action if any fail**: Review full audit set; consult Farrice if pattern issues detected.

---

## Final Sign-Off (Fri 7/18)

Before packaging for website:

- [ ] All 10 receipts pass pre-audit validation
- [ ] All 10 receipts pass audit execution validation
- [ ] All 10 receipts pass accuracy validation (≥95% confidence, 0 false positives)
- [ ] All 10 receipts pass documentation validation
- [ ] All 10 receipts pass marketing validation
- [ ] Jen has reviewed and approved compliant versions (if using current listings)
- [ ] Receipts are ready for website/social proof use

**Signed off by**: [Farrice]  
**Date**: [Fri 7/18 or earlier]  
**Status**: ✓ READY FOR WEEK 2 WEBSITE BUILD

---

## Common QA Issues & Resolutions

| Issue | Cause | Fix |
|-------|-------|-----|
| False positive: "schools" flagged as familial-status violation | Over-zealous keyword match | Verify context; "schools" alone is OK if not paired with family language; downgrade YELLOW if contextual |
| Rewrite too different from original | Preservation heuristic over-applied | Check that core amenity is still visible; rewrite should preserve "this is a home near schools" while removing "families" framing |
| No BLUE improvements offered | Listing is already clean on secondary issues | OK — not every listing has improvement opportunities |
| HIGH_RISK status but violations don't seem severe | Disability or national origin violations (auto-escalate) | Correct — these are CRITICAL categories; escalation is appropriate |
| Audit duration 30+ minutes (outlier) | Very long listing or many violations | Normal for complex listings; no action needed |
| Confidence level MEDIUM but violations seem clear | Caution on novel or context-heavy violations | Accept if justified; ensure citations support it |

---

## Checklist Completion

Print/save this checklist and complete during Week 1:

- **Tue 7/15**: Pre-Audit Validation (as listings arrive)
- **Wed 7/16 AM**: Audit Execution Validation (after audits run)
- **Wed 7/16 PM**: Accuracy, Documentation, Visual Validation (QA pass)
- **Thu 7/17 AM**: Aggregate Quality Check + Jen approval
- **Fri 7/18 AM**: Final Sign-Off (ready for website)

**Status**: [PASS / NEEDS REVISION / ESCALATE]
