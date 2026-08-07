# Vibe Tax Google Ship Checklist

Status: ship-today checklist  
Date: 2026-05-12  
Surface: Local Markdown Source persistence copy  
External action: Google Sheet and Google Doc created; no publishing or outreach performed.

## Live Assets Created

| Asset | Link | Use |
|---|---|---|
| Vibe Tax Diagnostic Lab - Response Tracker | https://docs.google.com/spreadsheets/d/1OfZQHim1l086D3XzCyBwVe94PrMl-WzTPKugxutHOzY/edit | Backend tracker, scoring formulas, validation dashboard, and Google Form builder checklist. |
| Vibe Tax Read - Result Template | https://docs.google.com/document/d/1VYrZ7gtq4kbe87w-SW9hdOM5vmkdvANJCXIfEfqrg80/edit | One-page manual result template for concierge Vibe Tax Reads. |

## Ship Order

1. Open Google Forms and create a blank form.
2. Use this title:

```text
The Vibe Tax Diagnostic
```

3. Use this description:

```text
A 2-minute false-signal check for offers, content, and pages that look good but are not creating buyer movement. Answer based on the evidence you actually have, not the version you wish was true.
```

4. In Form settings, turn on email collection.
5. Add the questions below.
6. In Responses, link the Form to the live Response Tracker spreadsheet.
7. If Google creates a new response tab, tell Codex `form linked` and ask it to configure the new tab with formulas.
8. Add the Google Form link to LinkedIn Featured.
9. Publish the LinkedIn launch post manually.
10. Send 5 manual asks to qualified people.
11. For each serious submission, use the Google Doc result template and Gemini Gem instructions to send a 1-page read.

## Google Form Fields

### 1. First Name

Type: short answer  
Required: yes

### 2. Business Type

Type: multiple choice  
Required: yes

Options:

```text
Consultant
Agency
Coach
Creator
Service Owner
Other
```

### 3. Decision Being Made

Type: multiple choice  
Required: yes

Options:

```text
Offer
Content
Page
Positioning
Campaign
Sales Message
Other
```

### 4. Buyer Language Fit

Type: multiple choice  
Required: yes

Question:

```text
What is your current message mostly built from?
```

Options:

```text
0 - Mostly my own words, assumptions, or what sounds good to me.
1 - Some buyer phrases, but I cannot trace them clearly.
3 - Real phrases from calls, DMs, comments, or clients, but they are scattered.
5 - Repeated buyer phrases I can point to and reuse.
```

### 5. Shortlist Readiness

Type: multiple choice  
Required: yes

Question:

```text
If a serious buyer compared you to alternatives, what would they understand in 60 seconds?
```

Options:

```text
0 - What I do, but not why to choose me.
1 - The category, but not why I belong on the shortlist.
3 - My difference, but the proof is not obvious yet.
5 - Who it is for, why now, why me, and why trust it.
```

### 6. Proof Gap

Type: multiple choice  
Required: yes

Question:

```text
What proof supports the claim buyers most need to believe?
```

Options:

```text
0 - Mostly logic, credentials, or confidence.
1 - Some proof, but it does not prove the main decision risk.
3 - A few examples, but not tight before/after proof.
5 - Proof that shows the problem, mechanism, result, and relevance.
```

### 7. False Signal Risk

Type: multiple choice  
Required: yes

Question:

```text
Which signal are you most likely to over-trust right now?
```

Options:

```text
0 - Likes, compliments, peer praise, or my own excitement.
1 - Competitor patterns, AI summaries, or generic best practices.
3 - A mix of audience response and a few buyer conversations.
5 - Repeated buyer actions: replies, calls, paid interest, objections, referrals.
```

### 8. Human Resonance

Type: multiple choice  
Required: yes

Question:

```text
What does the right buyer feel when they read your message?
```

Options:

```text
0 - It sounds smart.
1 - They understand it, but may not feel seen.
3 - They recognize part of themselves, but the emotional cost is vague.
5 - They feel accurately understood before I explain the solution.
```

### 9. Social Repeatability

Type: multiple choice  
Required: yes

Question:

```text
Could someone repeat your core idea after one read?
```

Options:

```text
0 - Probably not; it needs too much context.
1 - They remember the topic, not the phrase.
3 - They can repeat the idea if prompted.
5 - They can repeat the phrase, enemy, and consequence.
```

### 10. Asset Or Decision

Type: paragraph  
Required: no

Prompt:

```text
Paste one offer, page, post, DM, sales line, or decision you want me to read.
```

### 11. Follow-Up Consent

Type: checkbox  
Required: yes

Option:

```text
Yes, send my result and occasional Vibe Tax examples. I can opt out anytime.
```

## Confirmation Message

Paste this under form presentation settings:

```text
Your score is in.

Do not treat the number like a grade. Treat it like a warning light.

If you pasted a real asset or decision, I may send a short read for the first serious submissions.
```

## LinkedIn Featured

Title:

```text
The Vibe Tax Diagnostic
```

Description:

```text
Find the false signal most likely costing you trust, content, or clients.
```

## LinkedIn Launch Post

```text
Your best-performing post might be lying to you.

Not because the metrics are fake.

Because the metric may not mean what you think it means.

Likes can mean:
"This was relatable."

Comments can mean:
"My peers agree."

Saves can mean:
"I want to think about this later."

None of that automatically means:
"I trust you enough to buy."

That gap is what I am calling the Vibe Tax.

It is the cost of building strategy from signals that look like progress but do not create buyer movement.

I built a short diagnostic for consultants, creators, coaches, agencies, and service owners who are making a real offer, content, or positioning decision from muddy signal.

It checks six things:

Buyer language fit.
Shortlist readiness.
Proof gap.
False signal risk.
Human resonance.
Social repeatability.

The score is not the point.

The point is finding the one signal you should stop trusting before it costs you another month.

Comment "scorecard" or hit the Featured link on my profile.

No automation.
No pitch theater.
Just a sharp read on where the signal might be lying.
```

First comment:

```text
The diagnostic takes about 2 minutes.

If you paste one offer, page, post, or decision, I will send a short read for the first serious submissions:

1. the signal I would distrust first,
2. the proof gap I would fix first,
3. one keep/revise/stop/test move.
```

## Gemini Gem Setup

Gem name:

```text
Vibe Tax Result Writer
```

Paste the Gem instructions from:

```text
_active/research-intelligence-entry-point/06-system/vibe-tax-diagnostic-lab-portable-schema-2026-05-12.md
```

Minimum knowledge to paste/upload:

1. Vibe Tax Diagnostic Lab Portable Schema
2. Vibe Tax Diagnostic Lab Copy And Flow
3. Offer Page
4. Copy Gate Result
5. Human Resonance Gate
6. Farrice voice/context notes

## QA Performed

| Check | Result |
|---|---|
| Google Sheet created | Pass |
| Response Tracker headers present | Pass |
| Score formulas present | Pass |
| Validation Dashboard formulas present | Pass |
| Form Builder Checklist present | Pass |
| Scoring sample test | Pass: `17 / Noisy Signal / Buyer Language Fit` |
| Sample row cleared | Pass |
| Google Doc template created | Pass |
| Google Doc sections read back | Pass |
| Google Form created | Not performed; no Google Forms connector exposed in this session. |
| LinkedIn Featured updated | Not performed; external publishing/account action remains manual. |

