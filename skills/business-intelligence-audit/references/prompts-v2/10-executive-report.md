---
name: "Executive Report Generator"
source_prompt: "skills/business-intelligence-audit/references/prompts/10-executive-report.md"
skill: business-intelligence-audit
standard: structure-pure-v2
refactored: 2026-07-11
---

# Prompt 10: Executive Report Generator

> Synthesize everything into a professional deliverable.

---

## Purpose

Create the final client-ready audit report that synthesizes all findings into an executive-level document.

---

## Input Required

- All previous prompt outputs (01-09)
- Client name and context

---

## Execution Protocol

```
You are generating an executive-level audit report for delivery to a consulting client.

Synthesize all analysis for [COMPANY] into a professional deliverable.

## Instructions

1. Apply the Pyramid Principle—lead with insights, not process
2. Use visual elements (tables, matrices) for clarity
3. Make every page earn its place
4. End with clear next steps
```

---

## Output Contract

- **Format options:** Markdown (default), PDF export, Google Slides, or Notion — same content, different shell
- **Executive Summary:** maximum one page — key findings, top recommendations, overall assessment
- **Nine required sections:** Executive Summary, Business Overview, Competitive Position, Customer Intelligence, Messaging Analysis, Digital Presence, Gap Analysis, Strategic Framework (SWOT), Recommendations, Next Steps, Appendix
- **Every section is a synthesis, not a copy-paste** of the source prompt's raw output — condensed to what an executive reader needs
- **Length discipline:** scannable in 5 minutes, readable in 15

---

## Output Skeleton

```
# Business Intelligence Audit
## [COMPANY NAME]
### Prepared by: [name/firm]
### Date: [date]

## Executive Summary
[one page max: what did we find, what should they do, why now]

### Key Findings
1. [Finding] — [implication]
2. [Finding] — [implication]
3. [Finding] — [implication]

### Top Recommendations
1. [Recommendation] — Impact: [level] | Effort: [level]
2. [Recommendation] — Impact: [level] | Effort: [level]
3. [Recommendation] — Impact: [level] | Effort: [level]

### Overall Assessment
[one paragraph: overall health + primary opportunity]

## Business Overview
[condensed from Business Scan]

## Competitive Position
[condensed from Competitive Intelligence]

| Dimension | [Client] | Key Competitors | Opportunity |
|-----------|----------|-------------------|---------------|
| | | | |

## Customer Intelligence
[condensed from Customer Intelligence]

### Customer Posture Profile
[brief description of ideal customer]

## Messaging Analysis
[condensed from Messaging Audit]

| Element | Score /10 | Priority Fix |
|---------|-----------|----------------|
| Headlines | | |
| Value Prop | | |
| Proof | | |
| CTAs | | |

## Digital Presence
[condensed from Digital Presence Analysis]

| Channel | Status | Score /10 | Priority |
|---------|--------|-----------|-----------|
| | | | |

## Gap Analysis

| Gap | Category | Impact | Effort |
|-----|----------|--------|--------|
| | | | |

## Strategic Framework (SWOT)

| Strengths | Weaknesses |
|-----------|------------|
| [bullets] | [bullets] |
| Opportunities | Threats |
| [bullets] | [bullets] |

## Recommendations

#### Immediate (This Week)
1. [action]

#### Short-Term (30 Days)
1. [action]

#### Medium-Term (90 Days)
1. [action]

## Next Steps
1. [next step]
2. [next step]
3. [next step]

## Appendix
- Detailed data and supporting evidence
- Methodology notes
- Data sources
```

---

## Quality Gate

- [ ] Executive Summary fits on one page and leads with the answer, not the process
- [ ] Every finding in Key Findings is paired with a stated implication, not left as a bare observation
- [ ] Report is scannable in 5 minutes and fully readable in 15 (test by timing a read-through)
- [ ] All nine content sections present and each is a condensed synthesis, not a raw paste of the source prompt output
- [ ] No section is padded to fill space — every paragraph earns its place per the Pyramid Principle

---

## Format Options

This report can be delivered as:
- **Markdown** → Clean, readable, version-controllable
- **PDF** → Professional client-ready (export from markdown)
- **Google Slides** → For presentation delivery
- **Notion** → For collaborative review

---

*This is the capstone prompt that brings together all other analyses.*
