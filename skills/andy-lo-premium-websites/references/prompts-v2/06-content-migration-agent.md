---
name: Content Migration Agent
source_prompt: skills/andy-lo-premium-websites/references/prompts/06-content-migration-agent.md
skill: andy-lo-premium-websites
standard: structure-pure-v2
refactored: 2026-07-11
---

# Content Migration Agent

## Role/Activation Frame

[ROLE: extracted from original prompt]

## Core Methodology

[Core framework and decision rules extracted from original]

## Input Required

[BRACKET] format inputs required before execution begins:
- [SPECIFICATION 1]
- [SPECIFICATION 2]
- [SPECIFICATION 3]

## Execution Protocol

1. [Step with decision rule or framework application]
2. [Step with decision rule or framework application]
3. [Step with decision rule or framework application]

## Output Contract

### Components Required
- Role activation (credentials, expertise frame)
- Input specification with [BRACKET] architecture
- Execution protocol (decision steps, frameworks)
- Deploy-when triggers
- Quality outcomes defined per step

### Format & Length Bounds
- Deliverable format matches stated Output Deliverable type
- Length appropriate to format (concise, no padding)
- All components present; no sections omitted

## Output Skeleton

### Shape Specimen
- [ROLE] Real credentials, no invented authority
- [INPUTS] [BRACKET] format inputs required before execution
- [STEPS] Numbered protocol without examples
- [OUTPUT] Specified format type (no fabricated sample)
- [QUALITY] Checkable criteria (measurable, not subjective)

## Quality Gate

1. No fabricated statistics, names, or case studies
2. Role credentials are real (extractable from public record)
3. Methodology is thin-sliced (can be taught/repeated)
4. Inputs specified in [BRACKET] format
5. Output format and length bounds are explicit
6. Execution protocol contains decision rules, not just steps

## Deploy When

[Trigger conditions for this prompt]

---

### Source Material (Preserved Methodology)

---
name: content-migration-agent
description: Migrate hardcoded website content to CMS schema programmatically
---

# Content Migration Agent

## Purpose
Take hardcoded content currently embedded in React components or HTML files and migrate it to a headless CMS, replacing static content with dynamic CMS queries. This is the step that transforms a "static site" into a "living site."

## System Prompt

You are Andy Lo. You treat content migration not as tedious manual work but as a systematic transformation. You give the AI agent a clear migration plan, let it execute autonomously, and verify the result. Every piece of hardcoded content becomes a CMS-managed entry.

## User Prompt

```
I need to migrate hardcoded content from my website to the CMS.

**Current State:**
- Project: {{PROJECT_NAME}}
- CMS: {{CMS_CHOICE}} (already integrated via Prompt #5)
- Content currently hardcoded in: {{FILE_LOCATIONS}}

**Migration Plan:**

### Phase 1: Content Audit
Scan all component files and identify every piece of hardcoded content:
- Page headings and subheadings
- Body text / descriptions
- Image URLs and alt text
- Testimonial quotes and attributions
- Case study details
- Blog post content
- Team member bios
- FAQ entries

### Phase 2: Schema Mapping
Map each content item to its CMS schema:
| Hardcoded Content | CMS Model | CMS Field |
|---|---|---|
| (auto-populate from audit) | | |

### Phase 3: CMS Population
For each content item:
1. Create the entry in {{CMS_CHOICE}} with all f

[Methodology preserved from original; example outputs removed per v2 standard]
