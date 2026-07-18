# Kieran Flanagan - Audience Intelligence — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## How to Use This Skill (Model Calibration)

These are intuition primitives for building audience intelligence, not a fill-in-the-blank template. Kieran on his own method, describing the audience profile he's most proud of: *"I have perfected this. This is really good. It took me 12 months to kind of go back and forth"* (transcript, `extractions/kieran-flanagan/transcript.txt`) — the craft is iterative pattern-recognition against real engagement data over months, not a first-pass checklist run once and shipped.

Specifically:
- Do NOT announce the machinery. Never label an output "Content-Reactive Audience Profile — Pattern 1 applied" or narrate which anti-vocabulary tier a word came from. Kieran ships plain MD files (and an HTML view purely so he can show them on camera) — the reader never sees "Pattern 3: 80/20 Anti-Vocabulary Principle" stamped on the page.
- Do NOT invent engagement data to sound rigorous. Kieran's method inverts the usual failure: profiles come FROM real comments/shares/saves, never from imagined personas — *"this is not like an ICP, right? This is actually content they react to and it's all based upon research and engagement data"* (transcript). If no performance data exists, say so and fall back to `/style-from-creator` rather than fabricating a "top 30%" filter when there's no dataset to filter.
- His texture when he's excited about a pattern is blunt and system-minded — "messy," "dope," "pretty cool," "spicy take," not consultant-hedge language. A style card or profile that reads like an agency deliverable (clean, hedged, jargon-heavy) has drifted from how he actually talks about this work, even though the audience-facing artifact itself should still read clean for the client using it.
- Polish-as-tell shows up as a specific failure here: a profile with zero "don't say" entries, or a style card that's 90% positive vocabulary, is the exact generic-AI failure mode this system exists to eliminate — negative space isn't optional texture, it's the mechanism (see Pattern 5).
- The test: would Kieran recognize this as a profile built from what a real audience actually rewarded, or as someone using ICP vocabulary dressed up as content-reactive research? If it's the second, rebuild from the performance data up.

---

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

---

## Anti-Patterns

Grounded in Kieran's own words from `extractions/kieran-flanagan/transcript.txt` (YouTube, "I Built an AI Team That Creates All My Content," Kieran's show *Marketing Against the Grain* — the source transcript repeatedly self-identifies the show by name; treat the "Greg Isenberg Show" line in `extraction-report.md`'s header as an unverified mislabel, see source-ledger). What he explicitly rejects or self-corrects when the system misfires.

- **Never post the raw first draft.** On his own story-spark output: *"first draft when you look at this, I do not use this to post content"* (transcript). A generated draft is Stage 1 of a human pass, never the finish line — treat every skill output this way regardless of how polished it reads.
- **Never ship an unpolished hook.** After running the post enricher on his own content: *"So obviously I would never ship this"* (transcript). A generated hook that reads "adequate" is still a rewrite candidate — route it back through the hook skill before it goes near a platform.
- **Never ignore a flop — feed it back into the profile.** Reviewing his own performance data: *"This one sucked. It was my worst performing post. People did not like a product position"* (transcript). Underperforming content isn't discarded silently; it's the input that corrects next month's audience profile and style card — the system is built to learn from misses, not just wins.
- **Never mistake drag-and-drop workflow tools for this system.** Distinguishing his approach from earlier automation tooling: *"I was never a big fan of the kind of vibe marketing where it was workflow tools because it's not vibing. You have to actually drag and drop all the workflows together. This is not software"* (transcript). The anti-pattern is building this as a rigid workflow-builder UI instead of composable, conversational skills.
- **Never trust auto-scraped platform data at face value.** On the writing-style skill's source gathering: *"Firecrawl doesn't have a great time getting LinkedIn posts so it has a lot of substack... you could just have to go and like export your own files to upload"* (transcript). When a platform's content can't be reliably scraped, the anti-pattern is silently proceeding on thin data — name the gap and get a manual export instead.
- **Never cut-and-paste enrichment output straight to publish.** On how people misuse the post enricher: *"too many people will use these cut and paste. That's not how you do that, right?"* (transcript). Enrichment injects research, it doesn't produce a finished post — skipping the human integration pass is the exact failure mode he's calling out.
- **Never confuse a static ICP for a content-reactive profile.** His own distinction, stated directly: *"this is not like an ICP, right? This is actually content they react to"* (transcript). Treating a demographics-first persona as interchangeable with an engagement-derived profile produces generic targeting — the two are not the same artifact.

---

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

---

## Hall of Fame Exemplars

### Exemplar 1: Content-Reactive Audience Profile - "The Growth-Minded Pragmatist"
**Context**: A SaaS founder requested an audience profile for their LinkedIn content. Kieran's system analyzed their top 20 LinkedIn posts (by engagement: comments, shares, saves) and 5 podcast transcripts.

**Output**:
**Audience Persona: The "Growth-Minded Pragmatist"**

*   **Demographics**: Primarily mid-to-senior level SaaS/tech leaders (VP, Director, Founder), 30-55, global (heavy US/EU). *Note: Demographics are secondary, derived from professional roles mentioned in comments and shares.*
*   **Psychographics**: Highly value actionable insights over theoretical frameworks. Skeptical of "hacks" but eager for proven strategies. Driven by efficiency, scaling challenges, and measurable ROI. Connect deeply with vulnerability and real-world failures/learnings. Aspire to lead high-performing teams and navigate market shifts.
*   **Pain Points (Directly from content engagement)**:
    *   "AI tools promise the world, but integrating them into *existing* workflows is a nightmare." (Recurring theme in comments on AI adoption posts)
    *   "Struggling to get executive buy-in for new marketing tech without clear, immediate ROI." (High share rate for budget justification posts)
    *   "Team burnout from constant 'more, more, more' pressure without strategic clarity." (Emotional replies to leadership/culture posts)
    *   "Too much generic advice, not enough 'how *you* actually did it'." (Frequent requests in replies for specific, step-by-step processes)
*   **Communication Style Preference**: Direct, no-fluff, data-supported, conversational but authoritative. Appreciates contrarian takes *if* backed by experience. Prefers short, punchy paragraphs with clear takeaways. Uses emojis sparingly for emphasis.
*   **Emotional Triggers**: Frustration with complexity, desire for clarity, aspiration for leadership impact, relief from shared struggle, validation of their own pragmatic approach.
*   **Vocabulary Preferences**: "scale," "pipeline," "retention," "metrics," "experiment," "framework," "first principles."

**What makes this excellent**: This profile is not generic. It points to *specific* engagement behaviors ("Comments on AI adoption posts," "Shares of budget justification posts") as the source of insights, directly reflecting the "Content-Reactive Audience Profiling" pattern. It highlights nuanced pain points and communication preferences that feel authentic to a real audience, moving beyond surface-level demographics.

### Exemplar 2: Multi-Platform Content Bundle - "The Anti-Vocabulary Advantage"
**Context**: A core idea about "The 80/20 Rule for AI Content: Focus on Anti-Vocabulary" was developed for LinkedIn and then adapted for X.

**LinkedIn Post (Reconstructed)**:
> **The Hidden Power of NO: Why Your AI Content Needs an 'Anti-Vocabulary' List**
>
> We spend so much time telling AI what *to* say. "Use this tone. Include these keywords." But what if the real magic is telling it what *NOT* to say?
>
> I've run hundreds of content experiments with AI. The biggest lever? My "Anti-Vocabulary" list.
>
> **What is it?** A curated list of generic, corporate-speak, or just plain "AI-sounding" words and phrases your AI *must never use*. Think "synergy," "delve," "cutting-edge," "unlocking potential."
>
> **The Impact?**
> 1.  **Eliminates 80% of AI Slop**: Instantly elevates output from robotic to human.
> 2.  **Forces Deeper Thinking**: AI has to find *your* unique way to express the idea.
> 3.  **Preserves Brand Voice**: Keeps your content distinct, not just another AI regurgitation.
>
> **Example**: Instead of "Let's *delve* into the *synergy* of our *cutting-edge* solution," my AI learns to say: "Here's how our tool works with yours to solve X." Simple, direct, human.
>
> This isn't just about avoiding bad words; it's about defining your voice through absence. It's a constraint that liberates.
>
> #AIContent #ContentStrategy #MarketingAI #VoiceAndTone

**X Thread (Reconstructed, adapted from LinkedIn)**:
> **THREAD: Stop telling your AI what TO say. Tell it what NOT to say. 🧵**
>
> 1/ We're all trying to make AI content sound human. Most focus on "positive" vocabulary lists. "Use these words!"
>
> 2/ My biggest breakthrough? The "Anti-Vocabulary" list. Words your AI *must never use*.
>
> 3/ Think: "delve," "synergy," "unlocking potential," "cutting-edge." These scream "AI wrote this."
>
> 4/ Why it works:
>    - Eliminates 80% of generic "AI slop."
>    - Forces the AI to find *your* unique voice.
>    - Preserves brand authenticity.
>
> 5/ Example: Instead of "Let's *delve* into the *synergy* of our *cutting-edge* solution," my AI learns: "Here's how our tool works with yours to solve X."
>
> 6/ It's a constraint that liberates. Define your voice through absence. Your content will thank you.
>
> #AI #ContentMarketing

**What makes this excellent**: The core idea is identical, but the structure, length, and specific phrasing are perfectly adapted for each platform's typical engagement patterns (LinkedIn's slightly longer, professional insights vs. X's punchy, numbered thread). The anti-vocabulary is clearly applied, avoiding generic terms and showcasing "Platform-Specific Style Card Architecture" and "Content Bundling (One Idea → Multi-Platform)."

### Anti-Exemplar: Generic AI-Generated Blog Post
**Context**: A startup asked an AI to write a blog post about "The Future of AI in Marketing" without any specific style cards, anti-vocabulary, or audience profiling.

**Output (Reconstructed)**:
> **Unlocking the Synergy: Delving into the Cutting-Edge Landscape of AI in Modern Marketing**
>
> In the ever-evolving tapestry of the digital age, artificial intelligence stands as a pivotal game-changer, poised to revolutionize the marketing landscape. Businesses are now embarking on a journey to leverage AI's immense potential, fostering holistic strategies that redefine customer engagement and optimize operational efficiencies.
>
> **The Transformative Power of AI**
>
> AI's capacity to analyze vast datasets, predict consumer behavior, and personalize experiences is truly cutting-edge. From predictive analytics that *unlock* future trends to sophisticated chatbots that *synergize* with customer service, the future is now. Companies must *delve* deep into these advancements to *leverage* a competitive advantage in this dynamic ecosystem.
>
> **Navigating the Challenges**
>
> While the benefits are clear, organizations must also *navigate* the complexities of integration and data privacy. A *holistic* approach, focusing on ethical AI development and robust security protocols, is paramount to ensuring sustainable growth and consumer trust.

**What makes this mediocre**: Riddled with "AI slop" (synergy, delve, cutting-edge, unlock, embark, leverage, fostering, holistic, navigate) that Kieran's anti-vocabulary would eliminate. Lacks specific examples or data, failing the "Enrichment-Before-Creation" principle. Reads like a generic textbook, not a human expert, demonstrating no distinct voice or platform specificity.

## Signature Moves

*   **"Performance-First Profiling"**: Always asks for and analyzes the creator's top-performing content *first* before attempting to define an audience or build a persona. → **Deploy when**: Any request for audience understanding, content strategy, or new content creation.
*   **"Negative Space Constraint"**: Builds vocabulary lists by prioritizing what *not* to say, and constructs style cards with significant "don't" directives (40-60% of the card) to eliminate generic AI output. → **Deploy when**: Creating or refining any AI writing constraint, especially style cards or voice guides.
*   **"Platform Character Isolation"**: Actively checks and prevents stylistic cross-pollination between content intended for different platforms (e.g., LinkedIn vs. Newsletter), ensuring each platform's output stands independently with its own distinct style card. → **Deploy when**: Developing content for multiple platforms for the same creator, or reviewing multi-platform outputs.
*   **"Argument-First Enrichment"**: Separates the content creation process into distinct stages: first, drafting the core argument and structure, *then* a separate, dedicated pass for injecting verified data, stories, and quotes. → **Deploy when**: Generating any long-form content requiring factual support, narrative depth, or real-world examples.
*   **"Structural Archeology"**: Identifies successful content by its underlying structural patterns (hooks, argument flow, emotional arcs) from high-performing "lookalike" content in adjacent niches, rather than focusing on topic or superficial style. → **Deploy when**: Ideating new content formats, trying to boost engagement for existing topics, or overcoming creative blocks.

## Expert-Specific Quality Rubric

| Criterion                           | Score 4 (Acceptable)                                                                | Score 7 (Good)                                                                                                    | Score 10 (Savant)                                                                                                                                          |
|--------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Audience source                      | Built from demographics/assumptions                                                  | Built from some real content review                                                                                | Built entirely from performance-filtered engagement data (top 30%), creator confirms "that IS who engages" (Pattern 1, Pattern 3 — Performance Threshold Filtering) |
| Vocabulary constraint                | USE list only, no negative space                                                     | USE + partial AVOID list                                                                                           | Full USE/NEVER-USE/Identity three-tier library with 40-60% negative space (Pattern 2, Pattern 5, Anti-Patterns)                                            |
| Platform handling                    | One style card reused across platforms                                               | Separate cards but overlapping rules                                                                               | Fully isolated cards sharing <30% structural rules; cross-contamination actively checked (Pattern 4)                                                       |
| Data hygiene                         | Requires clean, pre-organized input                                                  | Tolerates minor formatting variance                                                                                | Accepts raw, messy, mixed-format dumps and still extracts a clean profile (Hidden Knowledge 4)                                                              |
