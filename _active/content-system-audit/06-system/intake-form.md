# Intake Form — Tally.so Build Spec

> **Tool**: Tally.so (free tier sufficient). Alternative: Typeform if preferred.
> **Form length**: 6 questions, ~5-7 min completion. Kept short to maximize completion rate.
> **Adapted from**: `_active/farrice-brand/offers/intake-form-questions.md` (coach-focused) → reframed for consultant ICP.
> **Drops**: methodology questions, "ideal client struggle" framing, "frameworks/methods/signature concepts."
> **Adds**: content bottleneck question, current AI tool usage, platform mix, time-cost question.

---

## Form Settings

- All questions required except Q4 and Q6
- Q1, Q2: Multiple choice (radio + checkbox)
- Q3, Q5, Q7: Long answer (paragraph)
- Q4: Short answer (URL field, optional)
- Q6: Short answer (URL field × 3, optional)
- Q8: Short answer (URL field, required — for the strongest voice sample)
- Send confirmation email with Calendly link after submission

---

## Form Header (Client Sees This)

**Title:** Content System Audit — Pre-Call Intake

**Description:**

Thanks for booking. Before we get on the call, I need a few minutes of context so I can show up with most of the diagnostic already done.

Five minutes of honest answers here saves us 20 minutes on the call. Be direct — vague answers waste your time and mine.

---

## Questions

### Q1: What's currently eating the most time in your content workflow?

**What the client sees:**

"Pick the bottleneck that costs you the most hours per week. (Choose one.)"

- [ ] Coming up with what to post (blank-page paralysis)
- [ ] Writing the actual post (slow drafting)
- [ ] Editing AI output that sounds generic
- [ ] Repurposing across platforms (LinkedIn, Substack, etc.)
- [ ] Posting consistently when client work blows up the calendar

*What it captures: The primary friction point. This determines which workflow stage to optimize first. "AI editing" buyers need prompt architecture; "blank-page" buyers need ideation systems; "repurposing" buyers need pipeline templates.*

*Form setting: Multiple choice, single-select, required.*

---

### Q2: What AI tools are you currently using for content?

**What the client sees:**

"Check all that apply."

- [ ] ChatGPT (free or Plus)
- [ ] Claude (Anthropic)
- [ ] Notion AI
- [ ] Jasper, Copy.ai, or similar marketing AI
- [ ] Custom GPTs or saved prompts
- [ ] None — I write everything from scratch
- [ ] I tried AI tools and gave up

*What it captures: Their existing stack + sophistication level. Determines whether we're building from scratch or refactoring an existing flow.*

*Form setting: Checkbox (multi-select), required.*

---

### Q3: Where is AI making you sound generic?

**What the client sees:**

"Be specific. What does AI keep producing that doesn't sound like you? (Examples: 'every post starts with a question,' 'too many em-dashes,' 'corporate-LinkedIn voice,' 'the conclusions are always obvious.') If you don't use AI, write what your manual writing struggles with instead."

*What it captures: The specific anti-patterns we'll bake into the negative-constraint section of their custom prompt. Every consultant has a different list — this is the most valuable single answer for system prompt engineering.*

*Form setting: Long answer (paragraph), required.*

---

### Q4: Where do you publish? (Optional URLs)

**What the client sees:**

"Drop the links to where you publish so I can study your existing voice patterns:"

- LinkedIn profile URL: [text]
- Substack / blog URL: [text]
- Other (X, podcast, YouTube): [text]

*What it captures: Their actual distribution surface area + URLs for me to scrape past content for voice extraction. Optional because some prospects haven't started yet.*

*Form setting: Three short-answer URL fields, all optional.*

---

### Q5: What's your current production cost per post?

**What the client sees:**

"How long does it take you to write and publish one LinkedIn post or Substack edition right now? Be honest. (Examples: '2 hours per LinkedIn post,' 'a full Saturday for the newsletter,' 'no idea, I avoid it.')"

*What it captures: Baseline metric for ROI math. The audit's promise is "60 min for 2 weeks of content." We need their starting number to make the after/before contrast concrete on the call.*

*Form setting: Long answer (paragraph), required.*

---

### Q6: Drop links to your 3 best past pieces (Optional but extremely helpful)

**What the client sees:**

"Three pieces of writing that sound MOST like you — the ones where you'd say 'yeah, that's me.' LinkedIn posts, blog posts, podcast clips, anything counts. The more we have, the better we can tune the system to your voice."

- Best piece #1: [text]
- Best piece #2: [text]
- Best piece #3: [text]

*What it captures: Voice training data. These get fed into the voice fingerprint extraction (`voice-calibrate` skill). 3+ samples is the floor for a defensible voice spec.*

*Form setting: Three short-answer URL fields, all optional.*

---

### Q7: One thing that would make this audit worth $1,000 to you?

**What the client sees:**

"What outcome would make you say this was the best $249 you spent this quarter? (One sentence is fine.)"

*What it captures: Their actual success metric. Lets me front-load the call with what matters to them, not what I assume matters. Often reveals whether they want speed, quality, consistency, or external validation.*

*Form setting: Long answer (paragraph), required.*

---

### Q8: Best contact method (in case Calendly link breaks)

**What the client sees:**

"Email or LinkedIn URL — whichever I should use if I need to reach you before the call."

*Form setting: Short answer, required.*

---

## Post-Submission Confirmation Email

Send this immediately after they submit (Tally → Zapier → Gmail, or Tally email automation):

---

**Subject:** Content System Audit — booked. Here's what happens next.

**Body:**

Hey [NAME],

Got your intake. Two notes before our call:

1. **The call is 45 minutes, recorded.** I'll handle the recording. Show up however you'd show up to a meeting with someone you respect — no prep slides, no agenda you need to follow.

2. **What we'll do**: First 10 min I diagnose where your time is leaking. Middle 25 min we build your custom workflow live (you'll watch the system get architected on screen). Last 10 min I demo the prompt set with one of your actual content ideas.

After the call, you'll have:
- A Notion workspace tuned to your inputs
- 3 Claude prompts engineered around your voice patterns
- A 2-page PDF blueprint you can hand a VA, an EA, or your future self in six months

Delivery: within 24 hours of our call.

If you have any voice samples you didn't add to the form (podcast clips, voice notes, anything where you actually *talk* the way you think), reply with the link. The more I have, the better the system gets.

Calendar link if you haven't booked yet: [Calendly URL]

Talk soon,
Farrice

---

## Tally Build Notes

- Use Tally's "logic" feature to skip Q4/Q6 if user picked "I write everything from scratch" in Q2 — they likely don't have URLs yet
- Set up Tally → Calendly redirect on submission (cleaner than email-then-book)
- Set up Tally → Notion database write so each intake auto-creates a client record
- Set up Tally → Stripe link in confirmation email if booking + payment isn't bundled

## Notes for future iteration

- If consultants consistently give weak answers on Q5 (production cost), they don't track time — flag in call and quantify together
- If Q3 (where AI sounds generic) returns frequent "I don't know," we're attracting prospects too early in the AI adoption curve. May need to add a pre-qualifier
- After 5 audits, A/B test removing Q1 (replace with open-ended "what's broken") — multiple choice may anchor the bottleneck before we've actually diagnosed it
