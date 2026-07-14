---
name: RE-1 Fair Housing Listing-Copy Auditor
description: Pre-publish audit of MLS listing remarks for Fair Housing Act compliance. Scans against HUD Advertising Word/Phrase List (24 CFR §100.75) and NAR Article 12. Outputs RED violations (immediate removal), YELLOW cautions (review + rewrite), and BLUE improvements. 10-15 min per listing; produces defensible before/after audit with citations.
version: "1.0"
input: Raw MLS listing remarks (100-500 words)
output: JSON audit report + before/after sample + next-step guidance
---

# RE-1 Workflow: Fair Housing Listing-Copy Auditor

## INPUT

Paste the **raw MLS listing remarks/description** exactly as written. Include full text (title, headline, body, remarks).

Example:
```
Title: Beautiful Home in Family-Friendly Community
Remarks: Perfect for young families looking to settle in a quiet neighborhood. 
Walking distance to top-rated schools. Safe area with excellent community feel. 
Ideal for retirees or active professionals. Easy access to ethnic restaurants...
```

---

## AUDIT LOGIC

### Step 1: Scan for Direct Violations (Tier 1 · RED)

Read the listing once, line by line. Flag **every phrase** that:
- Names a protected class as target audience ("perfect for young families," "ideal for retirees")
- Uses direct demographic language ("Christian community," "young professionals," "elderly")
- Excludes household types ("not for families," "not suitable for those with...")

**List these as RED violations.**

### Step 2: Identify Contextual Risks (Tier 2 · YELLOW)

Read again for case-law-documented code language:
- "Safe neighborhood" / "quiet area" — possible race or disability coding
- "Walking distance to schools" — familial-status coding (per HUD Guidance 2016)
- "Playgrounds nearby" — familial-status implication
- "Ethnic restaurants" / "diverse dining" — possible race coding
- "Suitable for investors" / "up and coming" — gentrification language (risky if demographic framing)

For each, check: **Does this phrase exclude or imply preference for a household type?**

- If YES → flag as YELLOW
- If NO (purely factual) → BLUE (improvement only)

**Example decision**:
- "Walking distance to schools" (standalone) = YELLOW (educate agent)
- "Walking distance to local schools" (neutral) = Usually OK, but worth YELLOW if paired with family language
- "Top-rated schools: Lincoln Elementary (8.5/10), Central MS (8.2/10)" = OK (specific, factual)

### Step 3: Suggest Compliant Rewrites

For every RED flag:
1. Identify what the agent *meant* (e.g., the property is spacious, near schools, in a quiet area)
2. Rewrite to preserve that meaning **without demographic coding**
3. Cite the violation type (e.g., "Age-coded familial status language")

**RED Rewrite Examples**:
- ❌ "Perfect for young families" → ✅ "Spacious home with multiple bedrooms, ideal for growing households"
- ❌ "Ideal for retirees" → ✅ "Low-maintenance layout with convenient downtown access"
- ❌ "Quiet neighborhood, perfect for families" → ✅ "Tree-lined cul-de-sac; convenient to parks and schools"
- ❌ "Walking distance to schools" → ✅ "Walking distance to Lincoln Elementary and Central Middle School"
- ❌ "Safe area" → ✅ "Gated community" or "Neighborhood watch active" (if factual)

For every YELLOW flag:
1. Provide a neutral alternative
2. Note that agent should decide if rewrite is needed (it's likely OK, but educate)

### Step 4: Grade Overall Audit Status

- **PASS**: Zero RED violations, ≤2 YELLOW cautions
- **VIOLATIONS_FOUND**: 1-3 RED violations
- **HIGH_RISK**: 4+ RED violations or multiple YELLOW cautions compounded

### Step 5: Output the Audit Report (JSON)

Structure:
```json
{
  "listing_address": "[address from MLS or input]",
  "audit_date": "YYYY-MM-DD",
  "audit_status": "PASS | VIOLATIONS_FOUND | HIGH_RISK",
  "summary": "[1-2 sentence overview]",
  
  "violation_count": {
    "red_violations": 0,
    "yellow_cautions": 0,
    "blue_improvements": 0
  },
  
  "violations_by_tier": {
    "red_violations": [
      {
        "original_text": "Perfect for young families",
        "violation_type": "Age/Familial Status Coding",
        "authority": "Fair Housing Act, 42 U.S.C. §3604; Fair Housing Center case law",
        "risk_level": "HIGH — direct violation",
        "suggested_rewrite": "Spacious home ideal for growing households",
        "citation": "United States v. Newberry (4th Cir. 1999); HUD Fair Housing Act & Advertising Guidance (2016)"
      }
    ],
    "yellow_cautions": [
      {
        "original_text": "Walking distance to schools",
        "caution_type": "Possible Familial-Status Implication",
        "authority": "HUD Fair Housing Act Guidance (2016)",
        "risk_level": "MEDIUM — contextual; verify if paired with family language",
        "suggested_rewrite": "Walking distance to Lincoln Elementary and Central MS",
        "citation": "HUD Guidance 2016; Fair Housing Center case law"
      }
    ],
    "blue_improvements": [
      {
        "original_text": "Great schools",
        "improvement_type": "Vague marketing language",
        "suggested_rewrite": "Walking distance to top-rated Lincoln Elementary (8.5/10 rating)",
        "note": "Optional; improves specificity and credibility"
      }
    ]
  },
  
  "before_after_sample": {
    "original_excerpt": "Perfect for young families looking to settle in a quiet neighborhood. Walking distance to top-rated schools. Safe area with excellent community feel. Ideal for retirees or active professionals.",
    "compliant_version": "Spacious home in established residential neighborhood. Walking distance to Lincoln Elementary and Central Middle School. Established community with parks and recreation nearby. Convenient downtown access and outdoor entertaining space."
  },
  
  "defensibility_statement": "This listing has been audited against HUD 24 CFR §100.75 (Fair Housing Act prohibited bases in advertising) and NAR Code of Ethics Article 12. Flagged violations are documented below with citations. Compliant rewrites preserve the property's actual appeal while eliminating Fair Housing Act risk.",
  
  "agent_education": "Age-coded language ('young families,' 'retirees') is a high-volume violation in real estate. The Fair Housing Act protects 'familial status' — having children under 18. Replacing demographic targets with feature-based language strengthens the listing and eliminates compliance risk. Estimated time to edit: 10-15 minutes.",
  
  "next_steps": [
    "1. Review compliant rewrites above",
    "2. Edit listing remarks in MLS (resubmit within 24 hours to avoid violation escalation)",
    "3. Update MLS with new copy — no need to list as 'repriced' or flag change",
    "4. Save this audit report in transaction file (creates defensible record)",
    "5. If questions, consult broker/legal counsel on novel cases"
  ],
  
  "liability_note": "This audit is a compliance tool, not legal advice. For questions or novel violations, consult your broker, MLS, or legal counsel. Documented audit provides defensibility record.",
  
  "authority_sources": [
    "24 CFR §100.75 (HUD Fair Housing Act, Prohibited bases in advertising)",
    "NAR Code of Ethics Article 12 (Fair Housing standards for REALTOR® advertising)",
    "HUD Fair Housing Act & Real Estate Advertising Guidance (2016)",
    "Fair Housing Council v. 1734 East 82nd Street (9th Cir. 2019) — 'Safe neighborhood' coding",
    "Fair Housing Center v. Sears (8th Cir. 2009) — 'Quiet area' disability coding",
    "United States v. Newberry (4th Cir. 1999) — Age-coded familial status language",
    "Fair Housing Center of West Michigan v. Karwoski (6th Cir. 2015) — Visual + textual discrimination"
  ]
}
```

---

## PROCESSING RULES

### Rule 1: Assume Good Intent
Most agents don't know Fair Housing Act nuances. Flag as education, not blame. Phrase feedback positively: "I caught it before MLS did — good catch rate."

### Rule 2: Distinguish Fact from Assumption
- "Steps to entry" = factual statement (OK, though could be neutral)
- "Requires climbing stairs" = factual statement (OK)
- "Requires physical ability" = lifestyle assumption (RED)
- "Perfect for active homeowners" = lifestyle assumption (YELLOW)
- "Tree-lined cul-de-sac" = factual feature (OK)
- "Quiet neighborhood" = contextual (YELLOW, educate)

### Rule 3: Protected Classes Are Always Targets
If a phrase could *exclude* a protected class, it's risky. The Fair Housing Act protects membership in that class, not the property's suitability for any particular group.

### Rule 4: Cite Every Flag
Every RED and YELLOW must include a citation (CFR, case law, or HUD Guidance). BLUE flags don't need citations; they're optional improvements.

### Rule 5: Always Include Next Steps
Audit is not helpful without actionable remediation. End every report with: edit timeline, MLS resubmission process, documentation step, and where to go if questions arise.

---

## QUALITY GATE (Before Delivery)

- [ ] ✓ All RED violations flagged and cited
- [ ] ✓ All case-law-documented YELLOW cautions identified
- [ ] ✓ Compliant rewrites preserve property character (test: would agent agree this is accurate?)
- [ ] ✓ Before/after sample included
- [ ] ✓ JSON structure complete
- [ ] ✓ Authority citations present for every violation
- [ ] ✓ Next steps are explicit and actionable
- [ ] ✓ Liability/education tone is balanced (no shame, clear guidance)
- [ ] ✓ Defensibility statement included

If any box unchecked, revise and re-run audit.

---

## EXAMPLE AUDIT (From Hypothetical Listing)

**Input listing:**
```
Charming 4-bed home in prestigious gated community. Perfect for growing families. 
Walking distance to award-winning schools. Safe, quiet neighborhood ideal for retirees. 
Excellent area for active professionals. Near ethnic restaurants and cultural centers.
```

**Output (abbreviated):**

```json
{
  "listing_address": "[Address]",
  "audit_status": "VIOLATIONS_FOUND",
  "summary": "4 RED violations found (familial status, age coding, lifestyle assumptions). Compliant rewrites provided.",
  
  "violation_count": {
    "red_violations": 4,
    "yellow_cautions": 1,
    "blue_improvements": 2
  },
  
  "violations_by_tier": {
    "red_violations": [
      {
        "original_text": "Perfect for growing families",
        "violation_type": "Age/Familial Status Coding",
        "risk_level": "HIGH",
        "suggested_rewrite": "Spacious 4-bedroom home ideal for households of all sizes",
        "citation": "United States v. Newberry (4th Cir. 1999)"
      },
      {
        "original_text": "Ideal for retirees",
        "violation_type": "Age Discrimination",
        "risk_level": "HIGH",
        "suggested_rewrite": "Low-maintenance layout with convenient downtown proximity",
        "citation": "Fair Housing Act §3604(c); 42 U.S.C."
      },
      {
        "original_text": "Excellent area for active professionals",
        "violation_type": "Lifestyle/Age Assumption (Excludes retirees, disabled)",
        "risk_level": "MEDIUM-HIGH",
        "suggested_rewrite": "Convenient to downtown employment centers and recreation",
        "citation": "Fair Housing Center v. Sears (8th Cir. 2009) — lifestyle coding"
      },
      {
        "original_text": "Near ethnic restaurants and cultural centers",
        "violation_type": "Possible Race Coding (when used as sole neighborhood marker)",
        "risk_level": "MEDIUM",
        "suggested_rewrite": "Diverse neighborhood with fine dining and cultural events",
        "citation": "HUD Fair Housing Guidance (2016)"
      }
    ],
    "yellow_cautions": [
      {
        "original_text": "Walking distance to award-winning schools",
        "caution_type": "Familial-Status Implication (if paired with family language)",
        "risk_level": "MEDIUM",
        "suggested_rewrite": "Walking distance to Lincoln Elementary (9.2/10) and Central MS (8.8/10)",
        "note": "Standalone, acceptable; becomes problematic when compounded with 'perfect for families'"
      }
    ],
    "blue_improvements": [
      {
        "original_text": "Safe, quiet neighborhood",
        "improvement_type": "Vague marketing; consider specifics",
        "suggested_rewrite": "Tree-lined cul-de-sac; gated community with 24-hr security" (if true)
      }
    ]
  },
  
  "before_after_sample": {
    "original": "Perfect for growing families. Walking distance to award-winning schools. Safe, quiet neighborhood ideal for retirees. Excellent area for active professionals.",
    "compliant": "Spacious 4-bedroom home in established residential community. Walking distance to Lincoln Elementary (9.2/10) and Central MS (8.8/10). Tree-lined cul-de-sac with parks and recreation. Convenient to downtown employment and fine dining."
  },
  
  "next_steps": [
    "1. Rewrite in MLS using compliant copy (10-15 min)",
    "2. Resubmit to MLS within 24 hours",
    "3. Document audit in transaction file",
    "4. If novel language, consult broker"
  ]
}
```

---

## When to STOP Auditing

If a listing is so saturated with violations that it's easier to rewrite from scratch:
- ✓ Provide 4-5 violations as RED examples
- ✓ Offer a pre-written compliant version
- ✓ Note: "Recommend full rewrite; provided sample above"
- ✓ Suggest agent send rewrite to broker for sign-off

---

## Workflow End

Hand the JSON audit report + defensibility statement to the agent.

**Success condition**: Agent edits MLS, updates within 24 hours, saves audit in file. Risk eliminated, defensible record created.

