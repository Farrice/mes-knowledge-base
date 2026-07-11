---
name: "7S Organizational Scan"
source_prompt: "skills/business-intelligence-audit/references/prompts/07-7s-organizational-scan.md"
skill: business-intelligence-audit
standard: structure-pure-v2
refactored: 2026-07-11
---

# Prompt 07: 7S Organizational Scan

> Apply McKinsey 7S Framework to visible business elements.

---

## Purpose

Assess organizational alignment across Strategy, Structure, Systems, Shared Values, Skills, Style, and Staff—to the extent visible from external data.

---

## Input Required

- **Website content** (about, team, culture pages)
- **LinkedIn company/team profiles**
- **Job postings** (if available)

---

## Execution Protocol

```
You are applying the McKinsey 7S Framework to assess organizational alignment.

Based on externally visible information for [COMPANY], analyze the seven elements:

| Element | Type | What to Look For |
|---------|------|-------------------|
| Strategy | Hard | Stated competitive approach, mission, positioning |
| Structure | Hard | Org chart, team roles, hierarchy signals |
| Systems | Hard | Tech stack, processes, tools mentioned |
| Shared Values | Soft | Mission statement, culture claims, values |
| Skills | Soft | Capabilities highlighted, areas of expertise |
| Style | Soft | Communication tone, brand voice, leadership style |
| Staff | Soft | Team composition, hiring patterns, diversity |

Note: This is an external assessment. Many 7S elements are only fully visible internally — flag where visibility is limited rather than guessing.
```

---

## Output Contract

- **All seven elements scored:** Strategy, Structure, Systems, Shared Values, Skills, Style, Staff — each with stated/implicit view, alignment check, and a /10 score with rationale
- **7S Alignment Matrix:** six rows (Structure through Staff) showing current state, alignment with Strategy, and any gap
- **Alignment Issues:** every genuine misalignment named with an explanation
- **Organizational Insights:** strength areas, risk areas, and a maturity signal (Pre-Fall or Post-Fall)
- **Visibility limits explicitly flagged** wherever external data can't confirm a claim

---

## Output Skeleton

```
### 7S Analysis

#### Strategy
- Stated Strategy: [from mission/positioning copy]
- Implicit Strategy: [what actions actually reveal]
- Alignment Check: [does messaging match actions — yes/no]
- Score: [x]/10

#### Structure (External Visibility)
- Team Size Signal: [signal + source]
- Hierarchy Signals: [flat vs layered, with evidence]
- Departmental Structure: [visible from hiring/team page]
- Score: [x]/10

#### Systems
- Tech Stack Visible: [tools observed]
- Process Signals: [how they describe working]
- Automation Level: [signal]
- Score: [x]/10

#### Shared Values
- Stated Values: [from mission/culture copy]
- Evidence of Values in Action: [observed, not assumed]
- Value-Reality Gap: [if any]
- Score: [x]/10

#### Skills
- Core Competencies Claimed: [from copy]
- Evidence of Competencies: [proof observed]
- Skill Gaps Implied: [from hiring/messaging]
- Score: [x]/10

#### Style
- Leadership Visibility: [signal]
- Communication Tone: [description]
- Brand Personality: [description]
- Score: [x]/10

#### Staff
- Team Composition: [from team page/LinkedIn]
- Hiring Signals: [open roles, if any]
- Culture Signals: [from employee content/reviews]
- Score: [x]/10

### 7S Alignment Matrix

| Element | Current State | Aligned with Strategy? | Gap |
|---------|-----------------|--------------------------|-----|
| Structure | | | |
| Systems | | | |
| Shared Values | | | |
| Skills | | | |
| Style | | | |
| Staff | | | |

### Alignment Issues

1. [Misalignment]: [explanation]
2. [Misalignment]: [explanation]

### Organizational Insights
- Strength Areas: [where alignment is solid]
- Risk Areas: [where misalignment creates friction]
- Maturity Signal: [Pre-Fall or Post-Fall, with the evidence]
```

---

## Quality Gate

- [ ] All seven 7S elements scored with a one-line rationale, not a bare number
- [ ] Alignment Matrix has no blank "Gap" cells — state "none observed" explicitly where true
- [ ] Every Alignment Issue is tied to a named conflict between two specific elements
- [ ] Maturity Signal (Pre-Fall/Post-Fall) is backed by at least one piece of evidence
- [ ] Structure and Staff fields flag where external visibility is limited, rather than guessing

---

## Limitations

Note: This is an *external* assessment. Many 7S elements are only fully visible internally. Flag where visibility is limited.
