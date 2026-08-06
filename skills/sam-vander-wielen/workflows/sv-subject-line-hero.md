---
description: Write subject lines that make the subscriber the hero by name, plus edited preview text — the outcome-shaped, written-last method with the question-mark inflection variant
tier: 2
---

# /sv-subject-line-hero — Subscriber as Hero

Produces **subject lines and preview text** on Sam's highest-performing current mechanic: *"using the subscriber's name in the subject line and making them the hero of the subject line — and it's really getting people to open it."*

The shape is not "Hi [NAME]." It is **the reader's name inside a headline about the reader's desired outcome, written as if it already happened.**

## Pre-Flight Gate

Load `genius.md`. Two non-negotiables:

1. **Write the subject line last.** *"I always do this last… I think about what's the point of what I'm teaching in this newsletter. What's the outcome that they would really want?"* If the email isn't written, you can't do this step.
2. **Merge-tag safety.** Name personalization in a subject line fails loudly when the field is empty or dirty. Confirm a fallback before shipping.

## Skill Acquisition

1. `skills/sam-vander-wielen/genius.md`
2. `skills/sam-vander-wielen/references/source-quotes.md` — the verbatim examples are the calibration anchor
3. **The finished email** — required, not optional
4. The audience's single most-wanted outcome

## Execution

### Step 1 — Extract the outcome

Ask: *what is the point of what I'm teaching in this email, and what's the outcome they would most want from it?* Sam's reasoning, out loud: *"Well, Nathan would want 30,000 new subscribers."*

The outcome must be **specific and numeric where possible**.

### Step 2 — Write it as news about them

The formula: **[NAME] + [verb of achievement] + [specific outcome]** — stated as accomplished fact.

Sam's verbatim set:
- *"Nathan's email list just grew by 30,000 subscribers."*
- *"Nathan just made my book a bestseller."*
- *"Nathan just started his first podcast."*
- *"Nathan just got booked with clients"* / *"has a full roster of clients."*

The double-take is the mechanism: *"You're like — wait, what? And then you click on it."*

### Step 3 — Generate the placement variants

| Variant | Shape | Example |
|---|---|---|
| **Front** | Name leads | *"Nathan's email list just grew by 30,000 subscribers"* |
| **End** | Name closes | *"30,000 new subscribers for Nathan"* |
| **End + question mark** | Upward inflection | *"30,000 subscribers sounds good to Nathan?"* |

Sam on the third: *"Sometimes I'll use the question mark to give the upward inflection."*

### Step 4 — Check the relevance chain

The subject line's outcome must predict interest in the email's actual content. Sam: *"That's an email about newsletter growth. So if that person sees that subject line and is interested in it, they're also going to be interested in my newsletter itself."*

**If the outcome and the content don't match, the open is a bait-and-switch and the unsubscribe follows.**

### Step 5 — Write the preview text (never skip)

*"And then obviously — always, always edit the preview text."*

Two proven shapes:
- **Sneak peek**: *"Open me to learn how my easy email list strategy [added] 30K to your email list this year."*
- **Steal + emotional word**: *"Steal my email list strategy inside."* / *"Steal my way of my 500K launch inside."*

**"Steal" is her signature CTA verb** — *"A lot of times I say 'steal my secrets.' That works really well for me."*

### Step 6 — Run the curiosity check

The anti-pattern: *"They give away the farm in the subject line itself. There's no curiosity. There's no loop to get me to open."* A subject line that fully delivers the content has no reason to be opened.

### Step 7 — Merge-tag fallback

Specify the fallback token (e.g. "your") and read every variant aloud with it. *"Your email list just grew by 30,000 subscribers"* still works. *"Hey , ..."* does not.

## Content Type Adaptations

| Context | Adjustment |
|---|---|
| **No first-name data** | Use the fallback as the primary; the outcome-as-news shape works without a name |
| **B2B / enterprise** | Company name can substitute; drop the exclamation register |
| **Launch / close-cart emails** | Hero framing still works, but the deadline must appear in preview text, not the subject |
| **Cold list** | Do not use name personalization — reads as scraped. Use outcome-as-news only |
| **Real estate / regulated** | Outcome claims about the reader can imply promises; route through review |
| **Substack / public archive** | Subject line becomes the post title for non-subscribers — check it stands alone without the name |

## Output Schema

```
SUBJECT LINES — [Email topic] — [Send date]

## The Outcome
What the email teaches: [ ]
The outcome they most want from it: [ ]

## Variants
| # | Placement | Subject line | Char count |
| 1 | Front | | |
| 2 | End | | |
| 3 | End + ? | | |

Recommended: [#] — why:

## Preview Text
Option A (sneak peek):
Option B (steal + emotional word):
Recommended: [ ]

## Checks
Relevance chain (outcome predicts content interest): PASS/FAIL
Curiosity loop preserved (farm not given away): PASS/FAIL
Merge-tag fallback: [token] — read-aloud test: PASS/FAIL
Written last (email complete): Y/N
```

## Quality Gate

Reject and rebuild if:
- The email wasn't finished first
- The subject line gives away the farm — no reason to open
- The outcome doesn't predict interest in the actual content (bait-and-switch)
- No merge-tag fallback specified, or the fallback reads broken aloud
- Preview text left as default body text
- Name personalization used on a cold list
- Only one variant produced — the placement variants are the deliverable

**Execution prompt**: `references/prompts-v2/subject-line-hero.md`
