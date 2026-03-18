# Kieran Flanagan - Audience Intelligence — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## Genius Patterns

## Pattern 1: Content-Reactive Audience Profiling
**Execute**: Build audience profiles from what ALREADY resonates — feed existing high-performing content into the profiler and let the audience tell you who they are through engagement behavior. Never start from demographics or surveys.

**Process**: Collect 10-20 best-performing content pieces → Analyze patterns in engagement (comments, shares, saves, replies) → Extract: jobs to be done, pain points, communication style, emotional triggers, vocabulary preferences, content format preferences → Store as living document that updates with new performance data.

**Success Metric**: Generated audience profile matches actual engagement data within 85%+ accuracy. Creator says "yes, that IS who engages with my stuff" — not "that's who I WANT to engage."

---

## Pattern 2: Platform-Specific Style Card Architecture
**Execute**: Create entirely separate style cards for each platform. The same human sounds fundamentally different on LinkedIn vs. newsletter vs. X. Encode that difference with distinct vocabulary libraries, tone parameters, formatting rules, and structural constraints.

**Style Card Structure**:
1. **Vocabulary Library** — Words the creator actually uses on THIS platform (verified by frequency analysis)
2. **Anti-Vocabulary** — Words they NEVER use (this list does more work than the USE list)
3. **Tone Parameters** — Conversational depth, formality level, jargon tolerance
4. **Structural Rules** — Avg sentence length, paragraph patterns, hook format, section flow
5. **Example Outputs** — 3-5 verified examples the creator approves as "sounds like me on [platform]"

**Success Metric**: Creator reads output and says "that sounds like me ON LINKEDIN" not just "that sounds like me."

---

## Pattern 3: The 80/20 Anti-Vocabulary Principle
**Execute**: Use anti-vocabulary (words to AVOID) as a more powerful constraint than positive vocabulary. Build two lists: USE list (~20-30 words the creator reaches for naturally) and NEVER USE list (~50-100 words that are AI-generic or not in this creator's voice). The NEVER USE list eliminates 80% of "AI slop" with 20% of the effort.

**Common Anti-Vocabulary Items**: "delve," "tapestry," "landscape," "in the realm of," "leverage," "game-changer," "unlock," "embark," "navigate," "fostering," "holistic," "synergy," "cutting-edge."

**Success Metric**: First drafts require <30% human editing vs. 60-80% without vocabulary constraints.

---

## Pattern 4: The Platform Isolation Rule
**Execute**: NEVER let LinkedIn style infect newsletter style. Each platform gets its own completely independent style card, even for the same creator. The creator is a different "character" on each platform. When creating a style card, actively compare it against the creator's other platform cards and flag any cross-contamination.

**Why**: Cross-pollination produces "uncanny valley" content — it sounds RIGHT on no platform because it's a blend of all platforms.

**Success Metric**: Style cards for the same creator on different platforms share <30% of their structural rules.

---

## Pattern 5: Style Cards Require Negative Space
**Execute**: Effective style cards allocate 40-60% of their content to describing what NOT to do. What the creator would never say, formats they'd never use, tones that feel wrong. Only describing what TO do produces generic output because there are infinite ways to do something "right" but very specific ways that feel "wrong" for a creator.

**Success Metric**: Style card has equal or greater "don't" constraints as "do" directives.

## Hidden Knowledge

5 tacit expertise points that separate amateurs from professionals.

---

## 1. Content-Reactive vs. Persona-Based Is the Difference
**The Truth**: Traditional personas are fiction — built from demographics and marketing team imagination. Content-reactive profiles are built from ACTUAL content that ACTUALLY performed. The audience tells you who they are through engagement behavior.

**Deploy**: When someone says "build me an audience profile," always ask for their top-performing content first. If they don't have any, use `/style-from-creator` to analyze a similar creator's audience reactions.

---

## 2. Anti-Vocabulary Does 4x the Work of Positive Vocabulary
**The Truth**: Experienced AI content creators obsess over finding the right words. Kieran discovered that eliminating the WRONG words is 4x more effective. A 50-word "never use" list eliminates more AI slop than a 200-word "always use" list.

**Deploy**: Always build the NEVER USE list first. It's faster to compile and has more impact per word.

---

## 3. Performance Threshold Filtering (Top 30%)
**The Truth**: When analyzing content for patterns, only use the top 30% by performance. Including average-performing content dilutes the signal. The genius is in the outliers, not the mean.

**Deploy**: When fed a content library, always filter to top 30% by the most relevant engagement metric (saves > comments > likes) before extracting patterns.

---

## 4. Messy Data → Clean Profile Is the Skill
**The Truth**: Kieran doesn't need clean, organized data. He feeds "messy" CSV exports, mixed-format content dumps, and raw analytics into the profiler. The skill is in extracting signal from noise, not requiring pristine inputs.

**Deploy**: Accept any data format. Don't ask users to organize their data before feeding it in. The tool should handle messy inputs gracefully.

---

## 5. Identity Vocabulary Mapping
**The Truth**: The deepest layer of a vocabulary library isn't words the creator "uses" but words that map to their IDENTITY. These are terms that feel like "them" at a core level — not stylistic choices but identity markers that audiences associate with the creator's brand.

**Deploy**: When building vocabulary libraries, separate into three tiers: (1) Identity words (who they ARE), (2) Style words (how they sound), (3) Topic words (what they discuss). Identity words are the highest priority and hardest to get right.
