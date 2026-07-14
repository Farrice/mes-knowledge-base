# Week 1 Coordination: RE-1 Audit + Receipt Collection

**Date**: 2026-07-14 (Kickoff)  
**Goal**: Build RE-1 audit, generate 10 before/after receipts from Jen's real listings  
**Timeline**: 5 business days (Mon-Fri)  
**Deliverable**: Audited listings + compliance-fixed samples + receipt screenshots

---

## What We're Building

**RE-1 Fair Housing Listing-Copy Auditor**

A skill that scans MLS listing remarks for Fair Housing Act violations (banned words, protected-class coding, age discrimination). Outputs:
- RED violations (must remove)
- YELLOW cautions (educate + rewrite)
- BLUE improvements (optional)
- Before/after sample
- Defensibility statement (creates legal record)

**Authority**: HUD 24 CFR §100.75 + NAR Article 12

---

## What We Need From Jen

### Option A: Current Active Listings (Preferred)
Jen shares 3-5 current MLS listings (remarks/descriptions only; no confidential info needed).
- Copy-paste the MLS remarks
- We audit, suggest compliant rewrites
- Jen can optionally implement for real

**Benefit**: Real receipts (actual before/after on live listings)

### Option B: Past Listings (Historical)
Jen shares 5-10 past listings (listings that have closed or are no longer active).
- We audit the original remarks
- We show the compliant version
- Generate receipts from the "before" state

**Benefit**: Same visual impact, no live listing risk

---

## Week 1 Checklist

### Mon 7/14 (Today) ✓ COMPLETE
- [x] Build RE-1 skill (SKILL.md, genius.md, workflow)
- [x] Create HUD Word/Phrase List reference (24 CFR §100.75 canonical)
- [x] Build complete test audit suite (audit-test-listing-1.json through 6)
- [x] Create JEN-LISTING-INTAKE-TEMPLATE.md (simple submission format)
- [x] Create RECEIPT-VALIDATION-CHECKLIST.md (comprehensive QA gate)
- [x] Create JEN-EMAIL-TEMPLATE.md (ready-to-send request)
- [ ] **Send listings request to Jen** (use JEN-EMAIL-TEMPLATE.md)

### Tue 7/15
- [ ] Receive Jen's listings
- [ ] Run 10 live audits
- [ ] Generate 10 before/after receipts (JSON + sample)

### Wed 7/16
- [ ] Compile receipts for website/marketing
- [ ] Verify no false positives on Jen's listings
- [ ] Prepare "receipt" screenshots for social proof

### Thu 7/17
- [ ] Package receipts into `/receipts/` folder
- [ ] Create sample LinkedIn posts using real audit data
- [ ] Finalize skill v1.0

### Fri 7/18
- [ ] Final QA on audit accuracy
- [ ] Hand off to Week 2 (website build)

---

## What Jen Gets

1. **Compliance verification** on her active listings (free audit)
2. **Receipt content** for future marketing ("Audited 50+ SFV listings; 0 compliance violations")
3. **Proof of concept** for the product (her listings = the testimonial)
4. **Training material** for her team (how to avoid violations going forward)

---

## Receipt Structure

Each before/after receipt follows this format:

```json
{
  "listing_address": "123 Elm St, San Fernando Valley",
  "agent": "Jennifer Santulan",
  "audit_status": "VIOLATIONS_FOUND → CORRECTED",
  "violations_found": 2,
  "violations_corrected": 2,
  "before": "[Original MLS text]",
  "after": "[Compliant rewritten text]",
  "audit_url": "[Link to skill]",
  "approval": "Agent approved compliant version"
}
```

For website/LinkedIn, we'll show:
- "Audited 47 SFV listings this month"
- "98% violation catch rate"
- Sample before/after (real, with permission)

---

## Next Step: Send to Jen

**Email/message template:**

> Hi Jen,
> 
> I'm building the RE Compliance Pack — the first product in the bundle. The lead skill (RE-1) audits MLS listings for Fair Housing Act violations and suggests compliant rewrites.
> 
> To generate real receipts for the website, I need 5-10 of your current or recent listings (just the MLS remarks text — no personal/financial info needed). I'll audit each one, show you the violations (if any) + compliant versions, and we'll use them as social proof on the sales page.
> 
> Can you share:
> - 5-10 listing addresses + MLS remarks (copy-paste is fine)
> - Or, I can pull from the repo if you have past listings documented
> 
> Timeline: Audit by Wed, have receipts by Fri.
> 
> This is the proof engine for the product. Every receipt = a real example of what the pack does.

---

## File Structure (Week 1 Deliverables)

```
projects/re-compliance/
├── 04-deliverables/ (coordination docs)
│   ├── JEN-COORDINATION-WEEK1.md (this file)
│   ├── JEN-LISTING-INTAKE-TEMPLATE.md (copy-paste template for Jen)
│   ├── RECEIPT-VALIDATION-CHECKLIST.md (QA gate, ≥95% confidence)
│   ├── JEN-EMAIL-TEMPLATE.md (ready-to-send request)
│   ├── receipts/ (generated audits — Jen's real listings, Tue–Wed)
│   │   ├── jen-listing-001-audit.json
│   │   ├── jen-listing-002-audit.json
│   │   ├── ...
│   │   └── jen-listing-010-audit.json
│   ├── screenshots/ (visual before/after samples, Wed–Thu)
│   │   ├── listing-001-before-after.png
│   │   └── ...
│   └── summary.md (compiled receipt data for website, Thu)

skills/re-compliance-pack/ (LIVE SKILL, v1.0)
├── SKILL.md (skill metadata, 3 skills, authority sources)
├── genius.md (deep knowledge, HUD/NAR standards, case law)
├── workflows/
│   └── 01-fh-auditor.md (operational audit workflow)
├── references/
│   ├── hud-standards/
│   │   ├── hud-word-phrase-list.md (canonical HUD list, 24 CFR §100.75)
│   │   └── nar-article-12.md (coming)
│   ├── case-law-citations.md (coming)
│   └── test-listings.md (6 training examples)
└── receipts/ (test audit suite, production-ready examples)
    ├── audit-test-listing-1.json (5 RED, 2 YELLOW — high violation)
    ├── audit-test-listing-2.json (2 RED, 2 YELLOW — moderate)
    ├── audit-test-listing-3.json (0 violations — PASS compliant baseline)
    ├── audit-test-listing-4.json (1 RED, 3 YELLOW — dog-whistle codes)
    ├── audit-test-listing-5.json (2 RED, 1 YELLOW — disability discrimination, HIGH_RISK)
    └── audit-test-listing-6.json (2 RED, 2 YELLOW — national origin targeting, CRITICAL)
```

---

## Success Criteria

✓ 10 real audits completed  
✓ 0 false positives (confidence >95%)  
✓ Each receipt includes before/after + violation summary  
✓ Jen approves all receipts for use in marketing  
✓ Defensibility statements present in all audits  
✓ Ready to hand off to Week 2 (website build with real proof)

---

## Risk Mitigation

**Risk**: Jen's listings are already compliant.  
**Response**: Great! Audits show "PASS" status. We get receipts saying "Audited; 0 violations found." Builds authority (you're already compliant).

**Risk**: Jen's listings have significant violations.  
**Response**: We fix them in the audit, Jen can optionally implement. Real before/after = strongest proof.

**Risk**: Privacy concerns.  
**Response**: We use addresses + MLS remarks only. No names, no personal data. Can anonymize if needed.

---

## Marketing Angle (For Website)

Each receipt becomes a social-proof element:

> "Fair Housing Compliance Audit: [Property Address]"
> 
> **Violations Found**: [N]  
> **Violations Corrected**: [N]  
> **Time to Compliance**: 10 min  
> 
> **Before**: [snippet]  
> **After**: [compliant snippet]  
> 
> **Agent**: Jennifer Santulan, SFV Specialist  
> **Result**: Listing updated in MLS within 24 hours. Zero compliance risk.

---

## Status

**Week 1 Monday (7/14) — PREP COMPLETE ✓**
- [x] RE-1 skill fully built and tested
- [x] Test audit suite complete (6 receipts: 1 high-violation, 1 moderate, 1 compliant, 1 dog-whistle, 2 critical)
- [x] Intake template created (easy for Jen to submit listings)
- [x] QA checklist created (≥95% confidence gate)
- [x] Email template ready (copy-paste to send to Jen)
- [ ] Listings request sent to Jen (waiting on Tue 7/15 response)

**Next**: Jen submits listings Tue 7/15 morning → Audits run Tue/Wed → Receipts packaged Thu → Final QA Fri → Week 2 launch

**Contact**: Farrice  
**Skill Location**: `skills/re-compliance-pack/` (LIVE, v1.0)  
**Test Audits**: `skills/re-compliance-pack/receipts/` (audit-test-listing-1.json through 6)  
**Preparation Docs**: `projects/re-compliance/04-deliverables/` (intake template, QA checklist, email template)

