---
description: Create a CRM segmentation and campaign routing playbook based on B.A.N.K. buyer codes
---

# CRM Segmentation Playbook

## Pre-Flight Gate

Load `../genius.md` and `../references/bank-deployment-map.md`. CRM work must be simple enough to maintain.

## Input Required

- CRM or list structure
- Available fields and automations
- Lead sources, funnel stages, offers
- Whether B.A.N.K. code is direct, inferred, or unknown

## Execution

1. Define required fields and tags.
2. Create direct and inferred code capture paths.
3. Map each code to sequences, sales notes, and content routes.
4. Define confidence rules and re-scoring triggers.
5. Produce implementation checklist and campaign examples.

## Output Requirements

- **Field Schema**: field names and purpose.
- **Tagging Rules**: direct, inferred, unknown, confidence.
- **Routing Map**: code -> sequence -> sales action.
- **Data Capture Questions**: opt-in, form, call, or survey.
- **Automation Notes**: simple rules.
- **Maintenance Checklist**: review and cleanup cadence.

## Quality Gate

Do not overbuild. If a CRM cannot support complex routing, provide a lightweight tag-and-note version.

