# Vibe Tax Notion AI Prompt Pack

> Status: Ready to use
> Date: 2026-05-12
> Owner: Farrice
> Purpose: Build the Notion-native intake and operations shell for The Vibe Tax Diagnostic

## How To Use This

Use these prompts inside Notion AI to build the database shell, helper formulas, form instructions, and rough result drafts.

Important boundary: Notion is the intake and operations layer. Codex is the final result writer.

Notion AI can help create a database and formula drafts. It should not be trusted as the full Vibe Tax expert system.

## Prompt 1: Build The Database

```text
Create a database called “Vibe Tax Diagnostic Responses.”

This database tracks responses for a lead magnet called The Vibe Tax Diagnostic: a 2-minute false-signal check for offers, content, and pages that look good but are not creating buyer movement.

Create these properties:

Name: title
Email: email
Business Type: select with Consultant, Agency, Coach, Creator, Service Owner, Other
Decision: select with Offer, Content, Page, Positioning, Campaign, Sales Message, Other

Buyer Language Fit: select with:
0 - Mostly my own words, assumptions, or what sounds good to me.
1 - Some buyer phrases, but I cannot trace them clearly.
3 - Real phrases from calls, DMs, comments, or clients, but they are scattered.
5 - Repeated buyer phrases I can point to and reuse.

Shortlist Readiness: select with:
0 - What I do, but not why to choose me.
1 - The category, but not why I belong on the shortlist.
3 - My difference, but the proof is not obvious yet.
5 - Who it is for, why now, why me, and why trust it.

Proof Gap: select with:
0 - Mostly logic, credentials, or confidence.
1 - Some proof, but it does not prove the main decision risk.
3 - A few examples, but not tight before/after proof.
5 - Proof that shows the problem, mechanism, result, and relevance.

False Signal Risk: select with:
0 - Likes, compliments, peer praise, or my own excitement.
1 - Competitor patterns, AI summaries, or generic best practices.
3 - A mix of audience response and a few buyer conversations.
5 - Repeated buyer actions: replies, calls, paid interest, objections, referrals.

Human Resonance: select with:
0 - It sounds smart.
1 - They understand it, but may not feel seen.
3 - They recognize part of themselves, but the emotional cost is vague.
5 - They feel accurately understood before I explain the solution.

Social Repeatability: select with:
0 - Probably not; it needs too much context.
1 - They remember the topic, not the phrase.
3 - They can repeat the idea if prompted.
5 - They can repeat the phrase, enemy, and consequence.

Asset Or Decision: text
Consent: checkbox
Source: select with LinkedIn Featured, LinkedIn Comment, LinkedIn DM, Direct Ask, Referral, Other
Reply Status: select with New, Read Sent, Replied, Brief Asked, Paid, Not Fit
Paid Interest: select with None, Soft, Asked Price, Requested Brief, Paid
Buyer Phrase: text
Objection: text
Follow-Up Notes: text
Result Doc Link: URL

Add formula properties for:
Buyer Language Score
Shortlist Score
Proof Score
False Signal Score
Human Score
Repeatability Score
Total Score
Score Band
Primary Leak
Codex Input

The score formulas should extract the first number from each scored select property. Total Score should sum the six scores. Score Band should return:
0-9 High Vibe Tax
10-17 Noisy Signal
18-24 Proof Gap
25-30 Shortlist Ready

Primary Leak should choose the lowest score, with this tie-break order:
False Signal Risk, Proof Gap, Buyer Language Fit, Shortlist Readiness, Human Resonance, Social Repeatability.
```

## Prompt 2: Formula Helper

Use this inside each Notion formula editor if a formula breaks.

```text
Fix this Notion formula so it extracts the leading number from the select property and returns it as a number. If the property is empty, return empty.

The select values begin with 0, 1, 3, or 5.

Property name: [PROPERTY NAME]
```

## Prompt 3: Codex Input Formula

```text
Create a Notion formula property called “Codex Input.”

It should return a clean text block I can copy into Codex.

The output should use this structure:

Run Vibe Tax Result Writer on this diagnostic response.

Name:
Email:
Business Type:
Decision:
Buyer Language Fit:
Shortlist Readiness:
Proof Gap:
False Signal Risk:
Human Resonance:
Social Repeatability:
Total Score:
Score Band:
Primary Leak:
Asset Or Decision:
Buyer Phrase:
Objection:
Follow-Up Notes:

Use the matching properties from this database. Leave blank fields blank. Do not invent information.
```

## Prompt 4: Form And Page Instructions

```text
Write setup instructions for turning this database into a public Vibe Tax Diagnostic intake form.

The form should collect:
Name
Email
Business Type
Decision
Buyer Language Fit
Shortlist Readiness
Proof Gap
False Signal Risk
Human Resonance
Social Repeatability
Asset Or Decision
Consent

Use this public description:
“A 2-minute false-signal check for offers, content, and pages that look good but are not creating buyer movement. Answer based on the evidence you actually have, not the version you wish was true.”

Use this confirmation message:
“Your score is in. Do not treat the number like a grade. Treat it like a warning light. If you pasted a real asset or decision, I may send a short read for the first serious submissions.”
```

## Prompt 5: Result Draft Inside Notion AI

Use only if you want a quick rough read inside Notion, not the final version.

```text
Draft a rough Vibe Tax Read from this database row.

Follow this structure:
Snapshot
What I Would Distrust First
The Proof Gap
Keep / Revise / Stop / Test
Full Brief Bridge

Rules:
Do not mention AI.
Do not overstate certainty.
Make the person feel seen, not judged.
Every result must include one false signal, one proof gap, and one keep/revise/stop/test recommendation.
Keep it under 700 words.

If the row includes Asset Or Decision, reference only what is actually present. Do not invent context.
```

## Prompt 6: Create Operating Views

```text
Create useful views for the Vibe Tax Diagnostic Responses database.

Create these views:

New Reads:
Filter Reply Status is New.
Sort newest first.

Needs Follow-Up:
Filter Reply Status is Read Sent or Replied.
Sort newest first.

Brief Interest:
Filter Paid Interest is Soft, Asked Price, Requested Brief, or Paid.
Sort newest first.

Proof Bank:
Show Name, Business Type, Decision, Buyer Phrase, Objection, Paid Interest, Follow-Up Notes.
Filter Buyer Phrase is not empty or Objection is not empty.

Validation Dashboard:
Group by Source.
Show Reply Status, Paid Interest, Score Band, Primary Leak, and Result Doc Link.
```

## Prompt 7: Manual Form Setup Checklist

Use this because Notion AI may not create the form view directly.

```text
Create a step-by-step checklist for manually adding a public Notion Form view to this database.

The checklist should include:
1. Open the database.
2. Add a new Form view.
3. Add only the intake fields the respondent should see.
4. Hide internal operations fields.
5. Make Name, Email, Business Type, Decision, the six scored questions, and Consent required.
6. Keep Asset Or Decision optional but encouraged.
7. Use the public description and confirmation message from this database brief.
8. Copy the public form link.
9. Add it to LinkedIn Featured as “The Vibe Tax Diagnostic.”
10. Submit one test response and verify Total Score, Score Band, Primary Leak, and Codex Input.
```

## Prompt 8: Formula QA Row

```text
Create a sample test row with these scores:

Buyer Language Fit: 0
Shortlist Readiness: 1
Proof Gap: 3
False Signal Risk: 5
Human Resonance: 5
Social Repeatability: 3

Expected result:
Total Score: 17
Score Band: Noisy Signal
Primary Leak: Buyer Language Fit

If the result is different, inspect the score formulas and primary leak formula until this test passes.
```

## Prompt 9: Notion-To-Codex Bridge Reminder

```text
Add a short operating note at the top of the database:

This database collects and organizes Vibe Tax Diagnostic responses. Codex is the final result writer.

For any row that needs a high-quality read:
1. Open the row.
2. Copy the “Codex Input” field.
3. Paste it into Codex with this prompt:

Run Vibe Tax Result Writer on this diagnostic response.

Use /vibe-tax-brief for diagnosis and /vibe-tax-deploy voice boundaries. Do not send anything externally.

[PASTE CODEX INPUT]
```

## What To Avoid

- Do not ask Notion AI to invent buyer research.
- Do not ask Notion AI to publish or message anyone.
- Do not treat Notion AI result drafts as final.
- Do not make the form longer than the six scored questions plus required intake fields.
- Do not hide the paid offer bridge, but keep it soft and human.
