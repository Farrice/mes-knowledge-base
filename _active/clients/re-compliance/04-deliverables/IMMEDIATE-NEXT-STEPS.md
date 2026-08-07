# Immediate Next Steps (Tue–Fri Week 1)

**Today's Date**: Mon 7/14 (prep complete)  
**Next Action**: Send email to Jen (today or first thing Tue)  
**Deadline**: Fri 7/18 (10 receipts ready for website launch)

---

## TODAY (Mon 7/14) or TOMORROW (Tue 7/15 AM)

### Send Email to Jen
- [ ] Copy template from `JEN-EMAIL-TEMPLATE.md`
- [ ] Customize tone if needed (use your voice)
- [ ] Attach or link to:
  - `JEN-LISTING-INTAKE-TEMPLATE.md` (submission format)
  - `audit-test-listing-1.json` (sample complete audit)
  - `JEN-COORDINATION-WEEK1.md` (full plan/timeline)
- [ ] Send via email or Slack
- [ ] Expected response: Tue 7/15 afternoon or Wed morning

---

## TUESDAY 7/15 (Listings Arrive)

### When Jen Submits Listings

1. **Verify data quality** — use RECEIPT-VALIDATION-CHECKLIST.md (Pre-Audit Validation section)
   - [ ] Addresses are complete (full address, city, state, ZIP)
   - [ ] MLS remarks are full text (not summarized)
   - [ ] No corrupted text or encoding errors
   - [ ] Single listing per entry
   
2. **Log receipt** — create handoff note
   - [ ] Date/time received
   - [ ] Number of listings (target: 5–10)
   - [ ] Quick scan for any privacy concerns or notes

3. **Confirm with Jen** (optional 2-min email)
   - "Got your listings! Audits running now. Results Wed."

---

## TUESDAY–WEDNESDAY 7/15–7/16 (Audits Run)

### Run RE-1 Auditor on Each Listing

For each Jen listing:
1. Copy the MLS remarks exactly as provided
2. Run `workflows/01-fh-auditor.md` (RE-1 audit logic)
3. Generate JSON audit report
4. Save to `_active/clients/re-compliance/04-deliverables/receipts/jen-listing-[NUMBER]-audit.json`

**Output per audit**:
```json
{
  "listing_address": "[Jen's property address]",
  "audit_date": "2026-07-15 or 2026-07-16",
  "audit_status": "PASS | VIOLATIONS_FOUND | HIGH_RISK",
  "violation_count": { ... },
  "violations_by_tier": { ... },
  "before_after_sample": { ... },
  "defensibility_statement": "...",
  "agent_education": { ... },
  "next_steps": [ ... ],
  "authority_sources": [ ... ]
}
```

---

## WEDNESDAY 7/16 (QA & Validation)

### Run RECEIPT-VALIDATION-CHECKLIST.md (Critical Gate)

- [ ] **Audit Execution Validation** (JSON structure, required fields)
  - All 10 audits have proper JSON structure
  - All required fields present (no placeholder text)
  - Dates consistent (audit_date = 7/15 or 7/16)
  
- [ ] **Accuracy Validation** (≥95% confidence, 0 false positives)
  - Spot-check 3–5 audits: do violations actually exist in original text?
  - No false negatives: missed any obvious "perfect for families"?
  - Confidence levels justified (HIGH for direct violations, MEDIUM for dog-whistle)
  - Citations are accurate (case law, CFR numbers correct)
  
- [ ] **Compliant Rewrite Quality**
  - Rewrites preserve property truth
  - Rewrites eliminate violation language
  - Rewrites are actionable (agent could copy-paste to MLS)
  
- [ ] **Documentation Validation** (defensibility, authority, education)
  - Defensibility statement present
  - Case law citations present (at least 1–2 per audit)
  - Authority sources listed (not empty)
  - Agent education section is specific to listing (not generic)

- [ ] **Visual/Marketing Validation**
  - Before/after samples are compelling
  - Violation counts are clear
  - Addresses are anonymizable if needed

**If any audit fails validation**:
- [ ] Re-run the audit (refresh the workflow)
- [ ] Check for false positives (might be calibration issue)
- [ ] Consult genius.md + hud-word-phrase-list.md for verification
- [ ] If uncertain, log as "needs review" and move to next

**All 10 pass validation?**
- [ ] Proceed to Jen approval (Wed evening)

---

## WEDNESDAY–THURSDAY 7/16–7/17 (Jen Approval & Packaging)

### Get Jen's Approval

1. **Send summary to Jen** (if using current listings)
   - Brief email with results summary
   - "10 audits complete. Here are the results. Review compliant versions?"
   - Share 2–3 before/after samples as examples (your choice which)

2. **Jen reviews** (typically 30 min–1 hour)
   - Looks at compliant rewrites
   - Approves use in marketing/website
   - Optional: decides to update her MLS listings with compliant versions

3. **Document approval**
   - Email confirmation or Slack screenshot
   - Note: "Jen approved all receipts for website/marketing use"

### Package Receipts

**On Thu 7/17:**

1. **Create summary document** (`_active/clients/re-compliance/04-deliverables/summary.md`)
   - List all 10 audits with key stats (address, violation count, status)
   - Aggregate stats: "10 audits completed: 6 violations found, 0 false positives"
   - Social-proof angle: "98% compliance catch rate"

2. **Organize receipts** into folders (optional)
   - `receipts/json/` (all JSON audit reports)
   - `receipts/before-after-samples/` (text excerpts for website)
   - `receipts/screenshots/` (visual before/after images, if created)

3. **Create screenshots** (optional but powerful for marketing)
   - 3–5 before/after samples as visual cards
   - Text overlay: "Before | After" with violation count
   - Use for website, LinkedIn, sales page

---

## FRIDAY 7/18 (Final Sign-Off)

### Final QA & Handoff

- [ ] **Status check**
  - All 10 receipts complete (JSON + Jen approval)
  - No outstanding validation issues
  - Summary document created
  - Screenshots created (optional)

- [ ] **Commit to git**
  ```bash
  git add _active/clients/re-compliance/04-deliverables/receipts/jen-listing-*.json
  git add _active/clients/re-compliance/04-deliverables/summary.md
  git add _active/clients/re-compliance/04-deliverables/screenshots/ (if created)
  git commit -m "Add Jen audit receipts: 10 real-listing before/after samples"
  git push
  ```

- [ ] **Sign off** using RECEIPT-VALIDATION-CHECKLIST.md
  - All 10 audits pass ≥95% confidence gate
  - 0 false positives
  - Defensibility statements present
  - Ready for website launch
  - Status: ✓ READY FOR WEEK 2

### Handoff to Week 2

**Week 2 starts with**:
- 10 real audit receipts (proof of concept)
- Social-proof summary (ready for website copy)
- Screenshots (ready for landing page)
- RE-1 skill (LIVE, production-ready)

**Week 2 deliverables**:
- Website landing page (with receipt showcase)
- Stripe integration (payment processing)
- Free sample skill preview (lead magnet)
- 14-day guarantee messaging

---

## Quick Checklist (Print This)

```
WEEK 1 EXECUTION CHECKLIST (Tue–Fri)

□ Tue 7/15 AM: Send email to Jen (use template)
□ Tue 7/15 PM: Jen submits listings (5–10 addresses + MLS remarks)
□ Tue–Wed 7/15–16: Run 10 RE-1 audits, generate JSON receipts
□ Wed 7/16: QA validation (run RECEIPT-VALIDATION-CHECKLIST.md)
□ Wed–Thu 7/16–17: Jen approval + packaging (summary + screenshots)
□ Thu 7/17 PM: Commit receipts to git
□ Fri 7/18 AM: Final sign-off (all 10 pass ≥95% confidence)
□ Fri 7/18: Ready for Week 2 website launch

CONTACTS:
- Jen's email/Slack: [INSERT]
- Response expected: Tue 7/15 PM or Wed 7/16 AM
- Handoff date: Fri 7/18
```

---

## Files You'll Need (Bookmarks)

- `JEN-EMAIL-TEMPLATE.md` — Email to send today
- `RECEIPT-VALIDATION-CHECKLIST.md` — QA gate (Wed 7/16)
- `JEN-LISTING-INTAKE-TEMPLATE.md` — What Jen's submission looks like
- `skills/re-compliance-pack/workflows/01-fh-auditor.md` — Audit logic
- `skills/re-compliance-pack/references/hud-word-phrase-list.md` — Violation reference
- `audit-test-listing-1.json` — Sample audit (to attach to email)

---

## Confidence Check

✓ **Ready to execute?**
- [x] RE-1 skill is built and tested
- [x] Email template is ready to send
- [x] QA checklist is prepared
- [x] Infrastructure is staged
- [x] Timeline is realistic (5 business days)

**You're good to go.** Send the email to Jen and begin Week 1 execution.

---

**Updated**: 2026-07-14 (Mon end-of-day)  
**Next Action**: Send email to Jen (today or Tue AM)  
**Checkpoint**: Fri 7/18 (10 receipts ready for website launch)
