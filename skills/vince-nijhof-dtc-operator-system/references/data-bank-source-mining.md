# Data Bank Source Mining — Reference

The systematic harvesting layer beneath every Vince Nijhof workflow that touches angles, copy, ICP, or messaging.

## Source Hierarchy (in order of signal density)

1. **Trustpilot reviews** (yours + competitors') — 150+ char filter
2. **Amazon reviews** (yours + competitor product page reviews) — 150+ char filter, "verified purchase" preferred
3. **Support tickets** (Gorgias / Zendesk export) — full-text export, filter for substantive complaints + praise
4. **Customer emails** (returns/refunds, "tell me about your experience" responses)
5. **DMs / Instagram comments** (lower signal, harder to extract — but raw vernacular)
6. **Reddit threads** in your category — competitor mentions, problem language
7. **YouTube comment sections** of competitor unboxing/review videos

## The 150-Character Filter (Critical Rule)

Reviews under 150 characters are usually:
- "Great product!"
- "Love it"
- "5 stars highly recommend"

Reviews 150+ characters typically contain:
- Specific use case ("I'm a busy mom with two babies under 4...")
- Specific pain point being solved ("I haven't slept through a full night in months until...")
- Specific outcome language ("...and now I don't hear the birds chirping at 5am")
- 3-5 angles per review (the use case, the pain, the outcome, the comparison)

**Always pre-filter before reading. Saves hours; surfaces only the angle-rich reviews.**

## Extraction Process

### Step 1: Bulk Pull
- Trustpilot: scrape API or use the public listing (300-500 reviews/brand minimum)
- Amazon: ScraperAPI, Helium 10, or manual top-100 most-helpful
- Gorgias/Zendesk: CSV export of last 90 days, all categories
- Emails: filter inbox by "your experience" / "feedback" / "thank you"

### Step 2: Filter
- Character count ≥150
- Verified purchase (where applicable)
- Date within last 12 months (older = potentially stale messaging-MF)
- Exclude bot patterns ("the best the best the best")

### Step 3: Dump to AI Project
Create a Claude/Gemini project specifically for the brand's data bank. Upload reviews as documents. Project instruction: "You are the customer voice analyst for [BRAND]. When asked, surface specific quotes that match emotional, use-case, or pain themes. Always cite the review source."

### Step 4: Categorize by Emotion
For each substantive review, tag with primary emotion engineered:
- **Fear** (of missing out, of being judged, of failure)
- **Loss** (already lost something, want it back)
- **Confidence** (now I feel capable / attractive / smart)
- **Convenience** (life is easier / faster / simpler)
- **Belonging** (I'm part of something / understood)
- **Status** (others recognize me / I look successful)
- **Relief** (finally, the pain is gone)
- **Curiosity** (I want to understand / try / learn)

### Step 5: Extract Angle Seeds
For each emotion category, extract 5-10 verbatim quotes that could become hook lines, headlines, or scenario opens. Format:

```
EMOTION: Relief
QUOTE: "I haven't slept through a full night in months until I started using [product]. Now I don't even hear the birds chirping at 5am — I just wake up fully blacked out."
USE CASE: Busy mom, sleep-deprived
PAIN POINT: Chronic insomnia, light sleeper
OUTCOME LANGUAGE: "Fully blacked out", "don't hear the birds"
HOOK CANDIDATE: "I haven't slept through a full night in months — until [product]."
```

### Step 6: Refresh Cadence
Re-mine monthly. Customer language shifts. New use cases emerge. Competitor reviews get updated. The data bank is a living asset, not a one-time audit.

## Anti-Patterns

- ❌ Skimming 50 reviews and "getting the vibe" — you'll miss the highest-leverage quotes
- ❌ Mining only your own brand — competitor reviews surface gaps you don't see internally
- ❌ Using reviews under 150 characters — pure noise
- ❌ Categorizing by feature instead of emotion — you'll write feature-led ads instead of emotion-led
- ❌ Treating the data bank as a one-time project — it must refresh monthly
- ❌ Letting strategists do the mining manually — set up the AI project, automate the pull, let strategists extract from the structured library

## Tooling Stack (Vince's Setup)

- **Pull**: ScraperAPI, Helium 10, Trustpilot API, Gorgias/Zendesk CSV export
- **Storage**: Notion database (one row per review, columns: source, character count, emotion, use case, quote, hook candidate)
- **AI Project**: Claude Project per brand, with all reviews uploaded + standing instruction set
- **Output**: Strategist queries the AI project for angle seeds when ideating

## Ethical Boundaries

- ✅ Mining your own customer feedback (always allowed)
- ✅ Mining publicly visible competitor reviews (Trustpilot, Amazon — public data)
- ⚠️ Mining competitor support tickets / private DMs (DON'T — you can't access ethically)
- ⚠️ Posting fake reviews to manipulate the data set (DON'T — both unethical and breaks the signal you need)

The data bank works because it's REAL customer voice. Faking it pollutes the signal that makes it valuable.
