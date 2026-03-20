---
description: Run the AI Slop Detector as a final pass on any content — catches vocabulary kills, em-dash overuse, structural tropes, rhythm uniformity, and emotional tells
---

# AI Slop Detection Pass

Run this on any content before delivery. Works on content you just generated OR content pasted by the user.

## PHASE 1: LOAD THE DETECTOR

Read this file:
1. `/Users/farricecain/Google Antigravity/directives/ai-slop-detector.md`

Internalize the 7 sections. You are now a prose-level pattern detector, not an editor.

## PHASE 2: IDENTIFY THE CONTENT

If the user provided content inline, use that. If not, use the most recently generated content in this conversation.

If no content is available, ask: "Paste the content you want me to run through the slop detector."

## PHASE 3: RUN THE 5-CHECK SCAN

Run each check against the content. Report findings inline with the specific flagged text.

### Check 1: Tier 1 Vocabulary Scan
Scan for every Tier 1 word (delve, tapestry, landscape, leverage, robust, pivotal, realm, multifaceted, comprehensive, meticulous, beacon, commendable, intricate/intricacies). Also scan for Tier 2 words (showcase, underscore, noteworthy, paramount, vibrant, unparalleled, unprecedented, garner, accentuate, pioneering, transformative, seamless, groundbreaking, innovative, cutting-edge, revolutionary, game-changer, empower, streamline, elevate, optimize, scalable, synergy, foster, democratize, reimagine).

**Report format**:
- List every flagged word with the sentence it appears in
- Tier 1 = KILL (must replace)
- Tier 2 = ALERT (replace unless it's the genuinely precise word for the context)
- Suggest a replacement for each

### Check 2: Em-Dash Frequency
Count every em-dash (—) and en-dash (–) in the piece. Calculate the word count. Report the ratio.

**Threshold**: Max 2 per 500 words. If over, flag each em-dash and suggest whether it should be a comma, period, parenthetical, or kept.

### Check 3: Sentence Length Variance
Measure word count of each sentence. Report:
- Shortest sentence (words)
- Longest sentence (words)
- Average sentence length
- Whether variance is sufficient (human range: 3–40 words; AI range: 15–25 words)

If variance is low (all sentences within 5 words of each other), flag as metronome rhythm.

### Check 4: Structural Trope Scan
Scan for:
- "Here's what..." family (broke it, got me, no one tells you, I learned, the thing)
- Throat-clearing openers (Let me be honest, The truth is, Let's face it, It's no secret)
- False pivots (But here's where it gets interesting, Something shifted, Everything changed)
- Negation-reveal ("It's not X, it's Y")
- Canned handoffs ("[Problem]? Meet [solution]")
- Meta-commentary (In this article we will, Let's break it down, Let's unpack that)
- Engagement bait closers (Agree?, Thoughts?, What would you add?)

**Threshold**: Max 1 per piece, and only if it genuinely serves the moment. 3+ = regenerate.

### Check 5: Emotional & Authenticity Tells
Flag if the content contains:
- Ghost citations ("Studies show..." without naming the study)
- Performative empathy without specific cost/failure/moment
- Fence-sitting (presenting both sides without committing)
- Motivational poster tone (every challenge is an "opportunity")
- Missing personal stakes (no dollars, no time lost, no named failures, no specific moments)
- Sycophantic glazing ("Great question!")
- Latinate bias (utilize, facilitate, commence, approximately — when simpler words work)

## PHASE 4: SCORE AND VERDICT

### Scoring
| Check | Status |
|-------|--------|
| Tier 1 Vocabulary | PASS / FAIL (X kills found) |
| Em-Dash Frequency | PASS / FAIL (X per 500 words) |
| Sentence Variance | PASS / FAIL (range: X–Y words) |
| Structural Tropes | PASS / FAIL (X tropes found) |
| Emotional Tells | PASS / FAIL (X tells found) |

### Verdict
- **ALL PASS**: Content is clean. Deliver.
- **1–2 FAIL**: Flag the specific issues. Offer to rewrite the flagged sections only (not the whole piece).
- **3+ FAIL**: Content is AI-shaped. Offer full regeneration of the flagged sections, preserving the strategic thinking but rewriting the prose.

## PHASE 5: REWRITE (if requested)

If the user says "fix it" or "rewrite":
1. Preserve the strategic content and core argument
2. Replace all Tier 1 vocabulary with concrete, specific alternatives
3. Reduce em-dashes to max 2 per 500 words
4. Vary sentence lengths (add short punches between longer constructions)
5. Replace structural tropes with original transitions
6. Add specificity where ghost citations or vague stakes exist
7. Run the 5-check scan again on the rewritten version to confirm it passes

Present the rewritten version with a brief diff summary of what changed.
