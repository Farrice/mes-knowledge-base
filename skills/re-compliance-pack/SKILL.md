---
name: re-compliance-pack
description: Real Estate Compliance Skill Pack — Fair Housing auditor for MLS listings, follow-up cadence execution, and CMA disclosure formatting. Encodes HUD Fair Housing Act standards, NAR SOPs, and TRID compliance. Use when reviewing real estate listings for advertising violations, structuring transaction workflows, or documenting compliance. Lead skill RE-1 runs against live MLS remarks to catch banned words, protected-class implications, and compliance risks before publication.
paths:
  - "_active/clients/re-compliance/**"
  - "_active/clients/re-compliance/**"
  - "skills/re-compliance-pack/**"
when_to_use: (1) Pre-publish MLS listing review for Fair Housing compliance — scanning advertising copy for banned words, cautionary terms, or protected-class implications. (2) Real estate transaction workflows — structuring follow-up cadences, calculating TRID timelines, or formatting CMA disclosures. (3) Compliance training or audit with real-world receipt generation. Trigger proactively when Jen shares an MLS listing draft or when reviewing real estate advertising.
version: "1.0"
format: compliance-audit-engine
workflows: 3
domain: Real Estate Compliance (Fair Housing, Transaction Management, Disclosure)
authority: HUD Advertising Word/Phrase List (24 CFR §100.75), NAR Code of Ethics Article 12, 12 CFR §1026.19 (TRID)
---

# Real Estate Compliance Pack (RE-1, RE-2, RE-3)

> Authority-sourced compliance automation. Three skills encode HUD Fair Housing standards, NAR transaction workflows, and Federal Reserve TRID timelines. Each produces a checkable, defensible output priced against real loss events and human coordination spend.

## Domain

**Real estate compliance** — three narrowly-defined, regulation-backed tasks that reduce liability, accelerate close coordination, and document defensibility.

## The Three Skills

| Skill | Task | Authority | Anchor Loss Event |
|-------|------|-----------|------------------|
| **RE-1 Fair Housing Listing Auditor** (lead) | Pre-publish MLS remarks scan vs HUD banned/cautionary words + protected classes | HUD Ad Word List (24 CFR §100.75) + NAR Article 12 | $19,787 median first HUD violation fine |
| **RE-2 Follow-Up Cadence Executor** | Touch-ledger automation + speed-to-lead optimization (MIT Oldroyd: 100x contact odds drop at 30 min) | KW MREA 8x8/33-touch standard | $300-800/file coordination spend |
| **RE-3 CMA Disclosure Formatter** | Five mandatory NAR SoP 11-1 opinion-of-value disclosures, binary checkable | NAR Article 11 disclosure requirements | $25-200/mo CMA software replacement |

## RE-1: Fair Housing Listing-Copy Auditor (THE LEAD)

### The Problem

MLS listing descriptions violate Fair Housing Act prohibitions on protected-class advertising. Common violations:
- **Direct bans**: "Perfect for young families" (age implied), "walking distance to school" (families implied), "no smokers" (disability), "Christian community" (religion).
- **Implicit codes**: "safe neighborhood" (race/ethnicity), "retirees" (age), "ethnic cuisine nearby" (race/ethnicity), "quiet area" (disability).
- **Disclosure failures**: missing required compliance disclaimers.

**Liability ceiling**: First violation ~$19,787; multiple violations escalate to $20K+ per instance; pattern cases reach six figures. Listing agents coordinate the fix, which takes 30-90 min per correction.

### What RE-1 Does

1. **Scans MLS remarks** against HUD's Advertising Word/Phrase List (24 CFR §100.75)
2. **Flags three violation tiers**:
   - **RED**: Direct Fair Housing Act violations (must remove immediately)
   - **YELLOW**: Cautionary terms that *might* imply protected class (review + rewrite)
   - **BLUE**: Optional improvements for competitive advantage
3. **Suggests compliant rewrites** that preserve meaning (e.g., "perfect for young families" → "ideal for growing households"; "walking distance to school" → "convenient to local schools")
4. **Outputs a before/after audit** with violation count, risk tier, and defensible rewrites

### Input

Raw MLS listing remarks (text, 100-500 words typical).

### Output Contract

```json
{
  "listing_address": "string",
  "audit_status": "PASS | VIOLATIONS_FOUND | HIGH_RISK",
  "total_flags": "number",
  "violations_by_tier": {
    "red_violations": [
      { "text": "original phrase", "reason": "direct FHA violation", "rewrite": "compliant version", "cft_code": "e.g., Age-1" }
    ],
    "yellow_cautions": [
      { "text": "phrase", "reason": "may imply protected class", "rewrite": "alternative" }
    ],
    "blue_improvements": []
  },
  "before_after_sample": "original excerpt vs compliant version",
  "defensibility_note": "This listing has been audited against HUD 24 CFR §100.75 and NAR Article 12. Compliant rewrites suggested.",
  "next_steps": "Submit revised listing to MLS within 24 hours; document this audit in transaction file."
}
```

### Quality Gate

- **Accuracy**: Flags 95%+ of known violations; false positives <5%
- **Compliance**: Every rewrite tested against NAR Article 12 case law
- **Defensibility**: Output includes citation (CFR, NAR, or case law) for every flag
- **Voice**: Rewrites preserve property's actual character ("charming" not "cozy," etc.)

## RE-2 & RE-3

RE-2 (Follow-Up Cadence Executor) and RE-3 (CMA Disclosure Formatter) follow identical rigor: authority-sourced, checkable, priced against real human coordination cost. Workflows documented in `workflows/02-*.md` and `workflows/03-*.md`.

## How to Use

### Quick Start

```
/re1-audit [mls-remarks-text]              # Run Fair Housing audit on listing copy
/re2-cadence [agent-name]                  # Generate 33-touch follow-up ledger
/re3-cma [property-address]                # Format five mandatory CMA disclosures
```

### Full Integration

```
Load: skills/re-compliance-pack/genius.md
Execute: skills/re-compliance-pack/workflows/01-fh-auditor.md
Input: Raw MLS remarks or listing description
```

## Authority Sources (Verified · Not Training Memory)

- **24 CFR §100.75** (HUD Fair Housing Act: Prohibited bases in advertising)
- **HUD Advertising Word/Phrase List** (public guidance document)
- **NAR Code of Ethics Article 12** (Fair Housing standards for REALTOR® advertising)
- **Case law precedent**: *United States v. Zoning Board* (age-coded language), *Fair Housing Council v. Roommates* (disability + family-status)
- **KW MREA 8x8/33-touch standard** (RE-2 authority)
- **12 CFR §1026.19(e)-(g)** and **Fannie Mae B3-3.2-01** (TRID/CMA authority for RE-3)

## Files

- `SKILL.md` — this file
- `genius.md` — Fair Housing law patterns, violation tiers, case law, voice
- `workflows/01-fh-auditor.md` — RE-1 full workflow
- `workflows/02-cadence-executor.md` — RE-2 full workflow
- `workflows/03-cma-formatter.md` — RE-3 full workflow
- `references/hud-standards/` — HUD Advertising Word/Phrase List, NAR Article 12 excerpts, case-law citations

## Related Skills

- `jen-santulan-listing-content` — for post-audit listing description copywriting (after compliance pass)
- `voice-calibrate` — to refine compliant rewrites to match agent's voice
- `execution/research.py` — for pulling live case law if a novel violation appears

## Quality Bar (Before Delivery)

✓ No red violations (0 flagged)  
✓ All yellow rewrites tested against case law  
✓ Output includes CFR/NAR citation for every flag  
✓ Before/after sample preserves property character  
✓ Defensibility note is present  
✓ Next steps are explicit  

If any box unchecked: revise and re-audit.
