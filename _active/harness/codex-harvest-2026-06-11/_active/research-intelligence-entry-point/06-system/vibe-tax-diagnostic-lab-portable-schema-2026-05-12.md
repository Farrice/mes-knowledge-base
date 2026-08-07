# Vibe Tax Diagnostic Lab Portable Schema

Status: implementation schema  
Date: 2026-05-12  
Surface: Local Markdown Source persistence copy  
External action: none taken

## Purpose

This schema lets the Vibe Tax Diagnostic Lab move between Notion, Google Forms, Gemini Gems, Manus, ScoreApp, or a custom site without changing the actual product logic.

## Notion Database Schema

Database name:

```text
Vibe Tax Diagnostic Responses
```

Properties:

| Property | Type | Options / Format |
|---|---|---|
| Name | Title | First name or full name. |
| Email | Email | Required. |
| Business Type | Select | Consultant, Agency, Coach, Creator, Service Owner, Other. |
| Decision | Select | Offer, Content, Page, Positioning, Campaign, Sales Message, Other. |
| Buyer Language Fit | Select | `0 - Mostly assumptions`, `1 - Some buyer phrases`, `3 - Real but scattered phrases`, `5 - Repeated buyer phrases`. |
| Shortlist Readiness | Select | `0 - What I do only`, `1 - Category only`, `3 - Difference but weak proof`, `5 - Why now/why me/why trust`. |
| Proof Gap | Select | `0 - Logic or credentials`, `1 - Some weak proof`, `3 - Examples but weak before/after`, `5 - Problem/mechanism/result/relevance`. |
| False Signal Risk | Select | `0 - Likes/compliments/excitement`, `1 - Competitors/AI/best practices`, `3 - Mixed response and conversations`, `5 - Buyer actions`. |
| Human Resonance | Select | `0 - Sounds smart`, `1 - Understood but not seen`, `3 - Partial recognition`, `5 - Accurately understood`. |
| Social Repeatability | Select | `0 - Too much context`, `1 - Topic remembered`, `3 - Idea repeatable if prompted`, `5 - Phrase/enemy/consequence repeatable`. |
| Asset Or Decision | Text | Optional pasted offer, page, post, DM, sales line, or decision. |
| Consent | Checkbox | Required for follow-up. |
| Source | Select | LinkedIn Featured, LinkedIn Comment, LinkedIn DM, Direct Ask, Referral, Other. |
| Total Score | Number | Sum of six score values. |
| Score Band | Select | High Vibe Tax, Noisy Signal, Proof Gap, Shortlist Ready. |
| Primary Leak | Select | Buyer Language Fit, Shortlist Readiness, Proof Gap, False Signal Risk, Human Resonance, Social Repeatability. |
| Reply Status | Select | New, Read Sent, Replied, Brief Asked, Paid, Not Fit. |
| Paid Interest | Select | None, Soft, Asked Price, Requested Brief, Paid. |
| Buyer Phrase | Text | Exact phrase worth saving. |
| Objection | Text | Exact objection or hesitation. |
| Follow-Up Notes | Text | Manual notes. |

## Scoring Extraction

If the tool supports formulas, extract the first character from each scored select field and convert it to a number.

Pseudocode:

```text
score_value(answer) = first number before " - "

total =
  buyer_language_fit +
  shortlist_readiness +
  proof_gap +
  false_signal_risk +
  human_resonance +
  social_repeatability
```

Band logic:

```text
if total <= 9:
  "High Vibe Tax"
else if total <= 17:
  "Noisy Signal"
else if total <= 24:
  "Proof Gap"
else:
  "Shortlist Ready"
```

Primary leak tie-break logic:

```text
lowest = minimum of all six dimension scores

if false_signal_risk == lowest:
  "False Signal Risk"
else if proof_gap == lowest:
  "Proof Gap"
else if buyer_language_fit == lowest:
  "Buyer Language Fit"
else if shortlist_readiness == lowest:
  "Shortlist Readiness"
else if human_resonance == lowest:
  "Human Resonance"
else:
  "Social Repeatability"
```

## Gemini Gem

Gem name:

```text
Vibe Tax Result Writer
```

Short description:

```text
Turns a Vibe Tax Diagnostic response into a sharp one-page read with a false signal, proof gap, keep/revise/stop/test move, and paid brief bridge.
```

Paste-ready Gem instructions:

```text
You are the private result-writing engine for The Vibe Tax Diagnostic Lab.

You are writing in Farrice Cain's voice: direct, human, emotionally aware, strategic, and anti-theater. You are not writing like an AI consultant, a quiz funnel, or a generic brand strategist.

Your job is to turn one diagnostic response into a concise one-page Vibe Tax Read.

The public promise:
Find the false signal most likely costing the buyer trust, content, or clients.

The paid offer:
The Vibe Tax Brief is a 48-hour false-signal diagnostic that maps buyer language, hidden objections, competitor frames, proof gaps, positioning angles, sales conversation openers, and keep/revise/stop/test recommendations.

Hard rules:
- AI stays backstage. Do not mention AI unless the user explicitly asks.
- Do not inflate certainty. Use "I would distrust", "this suggests", or "the first place I would look" when evidence is thin.
- Do not use banned phrases: unlock your market potential, AI-powered research, data-driven insights, transform your strategy, take your business to the next level, comprehensive market research report, I help founders clarify their messaging.
- Make the buyer feel seen, not judged.
- Every result must include one false signal, one proof gap, and one keep/revise/stop/test move.
- If the person pasted an asset, reference only what is actually visible in the paste. Do not invent performance data or claims.
- Keep the output under 700 words unless asked for more.

Input format:
- Name:
- Email:
- Business Type:
- Decision:
- Buyer Language Fit:
- Shortlist Readiness:
- Proof Gap:
- False Signal Risk:
- Human Resonance:
- Social Repeatability:
- Total Score:
- Score Band:
- Primary Leak:
- Asset Or Decision:
- Notes:

Output format:

# Vibe Tax Read: [Name / Business]

## Snapshot
- Score: [Total]/30
- Band: [Score Band]
- Primary Leak: [Primary Leak]
- Decision reviewed: [Decision]

## What I Would Distrust First
[Name the signal. Explain why it may be expensive noise.]

## The Proof Gap
[Name the claim the buyer most needs to believe. Explain what proof is missing or weak.]

## Keep / Revise / Stop / Test
- Keep: [one thing not to throw away]
- Revise: [one thing to clarify]
- Stop: [one false signal to stop treating as truth]
- Test: [one 7-day test]

## Full Brief Bridge
[Soft CTA to the paid Vibe Tax Brief. Make it feel like the logical next step only if the gap is deep enough.]
```

## Gemini Gem Knowledge Files

Upload or paste these as knowledge:

1. `vibe-tax-diagnostic-lab-portable-schema-2026-05-12.md`
2. `vibe-tax-diagnostic-lab-copy-and-flow-2026-05-12.md`
3. `_active/research-intelligence-entry-point/OFFER-PAGE.md`
4. `_active/research-intelligence-entry-point/COPY-GATE-RESULT.md`
5. `_active/research-intelligence-entry-point/HUMAN-RESONANCE-GATE.md`
6. `FARRICE.md`
7. `_active/farrice-brand/ideation-bank/voice-signals.md`

If file upload is inconvenient, paste the Gem instructions and the scorecard schema first. The Gem can work from those alone for MVP.

## Google Doc-Style Output Schema

Document title:

```text
Vibe Tax Read: [Name / Business]
```

Sections:

1. Snapshot
2. What I Would Distrust First
3. The Proof Gap
4. Keep / Revise / Stop / Test
5. Full Brief Bridge

Acceptance criteria:

- Under 700 words.
- One page if pasted into Google Docs.
- No generic strategy claims.
- At least one specific line tied to the submitted asset or answer.
- Clear but soft paid bridge.

## Validation Tracker

Track daily for 7 days:

| Metric | Target | Notes |
|---|---:|---|
| Targeted asks/posts | 50 | Manual, qualified, no automation. |
| Form completions | 10+ | Minimum signal threshold. |
| Asset/decision pastes | 30%+ | Shows seriousness. |
| Manual result replies | 20%+ | Shows the result created conversation. |
| Paid brief questions | 3+ | Price, scope, "can you run this?" |
| Paid briefs | 1+ | First validation win. |
| Exact buyer phrases captured | 10+ | Use for future copy. |
| Objections captured | 5+ | Use for offer/page improvement. |

Decision rules:

| Result | Decision |
|---|---|
| 10+ completions, 3+ paid questions, 1 paid brief | Keep and raise visibility. |
| Completions but few replies | Improve result specificity and manual read. |
| Likes/comments but no completions | Improve CTA, Featured placement, and promise. |
| Fewer than 5 completions after 50 asks | Pivot hook, ICP, or promise. |

## Manus Upgrade Prompt

Use this only after the MVP gets signal.

```text
Build a public web app for The Vibe Tax Diagnostic Lab.

The app should collect name, email, business type, decision type, six scored diagnostic answers, optional pasted asset/decision, and consent. It should calculate total score from 0-30, assign a score band, identify the primary leak using the tie-break order, save the response to a database, and show a polished result page.

Score bands:
0-9 High Vibe Tax
10-17 Noisy Signal
18-24 Proof Gap
25-30 Shortlist Ready

Primary leak tie-break order:
False Signal Risk, Proof Gap, Buyer Language Fit, Shortlist Readiness, Human Resonance, Social Repeatability.

Public positioning:
The Vibe Tax Diagnostic Lab is a 2-minute false-signal check for offers, content, and pages that look good but are not creating buyer movement.

Do not lead with AI. The buyer-facing promise is false-signal detection, proof gaps, buyer language, and decision clarity.

Create:
- landing page,
- diagnostic form,
- score/result page,
- admin response table,
- CSV export,
- manual follow-up status fields,
- paid brief CTA.

Design style:
clean, sharp, editorial, authority-facing, not SaaS cute, not quiz-funnel cheesy.
```

## Source And Claim Notes

Use current source claims only in internal notes, proof pages, or cited sections. Do not lead public copy with stats.

Current support references:

- Gemini Gems help: https://support.google.com/gemini/answer/15146780
- Gemini Gem sharing: https://blog.google/products-and-platforms/products/gemini/sharing-gems/
- Notion Forms: https://www.notion.com/help/guides/use-forms-to-collect-organize-and-act-on-responses-in-notion
- Google Forms quiz/email support: https://support.google.com/docs/answer/7032287
- LinkedIn Lead Gen Forms specs: https://business.linkedin.com/marketing-solutions/success/ads-guide/lead-gen-forms
- Manus website builder: https://manus.im/docs/website-builder/getting-started
- Manus web apps: https://manus.im/features/webapp
- ScoreApp pricing/features: https://www.scoreapp.com/pricing/

