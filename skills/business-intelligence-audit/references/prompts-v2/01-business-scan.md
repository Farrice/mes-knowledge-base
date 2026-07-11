---
name: "Business Scan"
source_prompt: "skills/business-intelligence-audit/references/prompts/01-business-scan.md"
skill: business-intelligence-audit
standard: structure-pure-v2
refactored: 2026-07-11
---

# Prompt 01: Business Scan

> Extract core business intelligence from any website in under 10 minutes.

---

## Purpose

Get a comprehensive snapshot of what a business does, who they serve, and how they position themselves. This is the foundation for all other analysis.

---

## Input Required

- **Primary URL:** The main website URL
- **Optional:** LinkedIn company page, key landing pages

---

## Execution Protocol

```
You are a McKinsey-trained business analyst conducting initial discovery on a potential consulting client.

Extract and synthesize information from [URL] into a structured business profile.

## Instructions

1. Use read_url_content to extract the homepage first
2. Follow key navigation links (About, Services, Products)
3. Organize findings into the Output Skeleton structure
4. Apply the "So What" test—only include insights that matter

Apply MECE principles—be comprehensive but avoid redundancy.
```

---

## Output Contract

- **Format:** Structured markdown business profile, section headers as in the Output Skeleton
- **Length:** 1-2 pages
- **Sections required:** Company Overview, Value Proposition, Business Model, Proof Elements, Digital Presence Signals, Initial Observations — all six, none skipped
- **Every claim traceable:** each bullet must trace to something actually observed on the extracted pages; if a field can't be confirmed, write "not stated" rather than inferring
- **Scoring fields** (Design Quality) must carry a one-line rationale, not a bare number

---

## Output Skeleton

```
### Company Overview
- Name: [as stated]
- Industry/Category: [category]
- Founded: [year, or "not stated"]
- Location: [location, or "not stated"]
- Size Signal: [solo / small team / company — inferred from visible signals, cite the signal]

### Value Proposition
- Primary Claim: [main headline/promise, one line]
- Secondary Claims: [supporting value props, bullet list]
- Target Audience: [who they explicitly say they serve]
- Problem They Solve: [stated pain point]

### Business Model
- How They Make Money: [products/services/pricing actually visible]
- Delivery Model: [digital / physical / consulting / SaaS / etc.]
- Price Positioning: [premium / mid-market / budget — with the signal that supports it]

### Proof Elements
- Social Proof Type: [which types are present: testimonials / case studies / logos / metrics]
- Specific Claims: [any numbers, results, or outcomes mentioned — quoted from source, not invented]
- Credibility Signals: [certifications / press / partnerships actually shown]

### Digital Presence Signals
- Content Strategy: [blog / podcast / video — active or dormant, with last-activity signal if visible]
- Tech Stack Signals: [platforms/tools visible in source]
- Design Quality: [score 1-10] — [one-line rationale for the score]

### Initial Observations
- Strengths: [what's working, each tied to evidence above]
- Gaps: [what's missing or could improve]
- Hypotheses: [open questions for deeper analysis — framed as questions, not conclusions]
```

---

## Quality Gate

- [ ] All six required sections present, none left as generic placeholder text
- [ ] Every "Specific Claims" entry is quoted or paraphrased from the actual source, not invented
- [ ] Design Quality score includes a one-line rationale
- [ ] Each Initial Observation passes the "So What" test — states why it matters
- [ ] No two bullets in the same section restate the same fact (MECE check)
- [ ] Output is scannable in under 5 minutes

---

## Follow-Up Prompts

After Business Scan, typically run:
- **Prompt 02 (Competitive Intelligence)** → if positioning seems unclear
- **Prompt 04 (Messaging Audit)** → if copy/positioning needs analysis
- **Prompt 06 (Gap Identifier)** → if initial gaps seem significant
