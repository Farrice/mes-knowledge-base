# Hybrid Signal Notion Intake Spec

## Verdict

Use Notion as the intake and tracking layer.

Google Forms is acceptable for speed, but Notion fits this offer better because the buyer is sending valuable work artifacts. The experience should feel like a serious diagnostic desk, not a generic survey.

## Notion Architecture

### Public-facing view

Name:

> AI Misfire Map Intake

Job:

Collect one prompt, SOP, workflow, content process, sales process, delivery process, or failed AI output from a prospect.

Public promise:

> Send one AI output, prompt, SOP, or workflow. I will show where AI is being forced to guess.

### Private database

Name:

> AI Misfire Signal Pipeline

Job:

Track submissions, mini-diagnoses, paid audit opportunities, follow-up, and proof candidates.

## Database Fields

| Field | Type | Purpose |
|---|---|---|
| Submission | Title | Short label for the submitted asset |
| Name | Text | Prospect name |
| Email | Email | Follow-up email |
| LinkedIn URL | URL | Manual review and connection context |
| Business / Role | Text | Buyer context |
| Buyer Segment | Select | Founder-led expert, AI-forward agency, Local premium service, Other |
| Asset Type | Select | Prompt, SOP, Workflow, Failed AI output, Content process, Sales process, Proposal process, Delivery process, Other |
| Submitted Asset | Text | Pasted asset or summary |
| AI Goal | Text | What they hoped AI would do |
| Misfire | Text | What went wrong |
| Frequency | Select | Once, Weekly, Multiple times per week, Daily, Constant |
| Cost of Problem | Select | Annoying, Time drain, Revenue risk, Client quality risk, Founder bottleneck, Unknown |
| Paid Audit Interest | Select | Yes, Maybe, No, Unknown |
| Status | Status | New, Needs Mini-Diagnosis, Qualified Audit, Follow-Up, Won, Lost, Proof Candidate |
| Source | Select | LinkedIn post, LinkedIn DM, Comment, Referral, Email, Apify radar, Other |
| Next Follow-Up | Date | Manual follow-up date |
| Notes | Text | Internal notes only |

## Views

1. **New Submissions**
   - Filter: Status is New.
   - Use: triage every intake.

2. **Needs Mini-Diagnosis**
   - Filter: Status is Needs Mini-Diagnosis.
   - Use: free three-bullet diagnostic queue.

3. **Qualified Audit**
   - Filter: Status is Qualified Audit.
   - Use: paid AI Misfire Express opportunities.

4. **Follow-Up**
   - Filter: Status is Follow-Up.
   - Sort: Next Follow-Up ascending.
   - Use: daily manual outreach queue.

5. **Won / Lost**
   - Filter: Status is Won or Lost.
   - Use: conversion review and offer learning.

6. **Proof Candidates**
   - Filter: Status is Proof Candidate.
   - Use: anonymized before/after assets and future case studies.

7. **AI Misfire Map Intake**
   - Type: Form.
   - Use: public-facing submission path.
   - Visible fields: Name, Email, LinkedIn URL, Business / Role, Buyer Segment, Asset Type, Submitted Asset, AI Goal, Misfire, Frequency, Cost of Problem, Paid Audit Interest.

## Public Form Copy

### Title

AI Misfire Map Intake

### Description

Send one prompt, SOP, workflow, content process, sales process, delivery process, or failed AI output.

I will look for where AI is being forced to guess, what operating meaning is missing, and whether the fix is a prompt tweak, SOP rewrite, or deeper agent-ready work primitive.

Messy is fine.

### Submission promise

Selected submissions may receive a short diagnosis:

- where AI guessed
- what source of truth or decision rule was unclear
- what the first operating-layer fix would be

If the problem is deeper and worth solving, I may recommend a paid AI Misfire Express audit.

## Privacy Boundary

The form collects external client/prospect artifacts only.

Do not expose:

- Codex Antigravity internals
- local workflow names beyond public-friendly terms
- agent/persona files
- proprietary prompts
- internal command surfaces
- implementation scripts
- source extraction archives

If a prospect submits confidential material, keep it in Notion and the manual tracker only unless they explicitly authorize use as anonymized proof.

## First Manual Operating Loop

1. Review each new submission.
2. Assign buyer segment.
3. Mark unqualified examples as Lost or Follow-Up.
4. For viable examples, produce a three-bullet mini diagnosis.
5. If the diagnosis reveals repeated correction tax, founder bottleneck, revenue risk, or client quality risk, bridge to AI Misfire Express.
6. If the prospect pays or gives permission, tag as Proof Candidate after delivery.

## Quality Gate

- The form must ask for one concrete asset, not broad interest.
- The form must feel like a diagnostic, not a newsletter opt-in.
- Internal systems stay private.
- Every submission should create a next action: diagnose, follow up, qualify, or close.
