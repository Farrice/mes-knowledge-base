# Browser Assistant Prompts And Visual Asset Briefs

## LinkedIn Safety Boundary

Use browser assistance for:

- summarizing public post text you provide,
- drafting possible comments,
- ranking relevance,
- preparing manual replies,
- refining your own posts,
- turning submitted artifacts into Misfire Maps.

Do not use browser assistance for:

- scraping LinkedIn,
- automated profile collection,
- auto-liking,
- auto-commenting,
- auto-DMing,
- fake engagement,
- bypassing access controls,
- pretending to have read work you did not inspect.

## Prompt 1 - Feed Analyzer

```text
Act as my LinkedIn signal analyst.

Positioning:
Creative Strategist + AI Operating Partner. I help founder-led experts turn customer language and founder judgment into AI-ready marketing systems.

Core thesis:
AI outputs become unreliable when the marketing system behind the task is invisible: buyer language, proof hierarchy, offer logic, CTA timing, taste boundaries, and source-of-truth rules.

I will paste one LinkedIn post at a time.

For each post, return:
- ICP relevance: high / medium / low
- conversation lane: AI workflow, content strategy, founder bottleneck, sales/proposals, SOP/ops, agency delivery, other
- the exact line I should respond to
- one useful distinction I can add
- one comment under 90 words
- one softer alternate comment under 60 words
- whether to DM later: yes/no
- why a DM would or would not be appropriate

Rules:
- No flattery-only comments.
- No pitch in the comment.
- No invented context.
- If relevance is low, say SKIP.
- Keep LinkedIn actions manual.
```

## Prompt 2 - Comment Composer

```text
Write 5 manual LinkedIn comment options for this post.

My lens:
The visible AI output is often only the symptom. The real problem is a missing marketing system: customer language, proof rules, decision boundaries, taste, source of truth, or CTA timing.

Comment requirements:
- under 90 words
- no "great post"
- no sales pitch
- must add a new distinction
- must sound like a practitioner, not a brand account
- include one version that is more contrarian
- include one version that is more generous

Post:
[paste post]
```

## Prompt 3 - Warm DM Qualifier

```text
Decide whether this person should receive a DM from me.

Context:
[paste only context I genuinely have: their comment, my comment, their reply, or public statement]

My offer:
Free instant AI Misfire Diagnostic and paid Misfire Map for one AI-assisted artifact.

Return:
- DM appropriate: yes/no
- why
- risk of sounding opportunistic: low/medium/high
- one DM under 80 words if appropriate
- if not appropriate, one public reply instead

Rules:
- Do not pitch without context.
- Ask for one artifact, not a call.
- Keep it human and specific.
```

## Prompt 4 - Artifact Diagnostic Assistant

```text
You are helping me create an AI Misfire Map.

Input:
1. What the artifact was supposed to do:
[paste]

2. AI output / SOP / prompt / workflow:
[paste]

3. What felt off:
[paste]

Analyze:
- 3-7 places AI was forced to guess
- the missing judgment/source of truth behind each guess
- whether the issue is prompt, SOP, customer language, proof, offer logic, quality test, or workflow boundary
- the first agent-ready rule that would prevent this next time
- one paid audit bridge if the problem is repeated or costly

Rules:
- Do not overdeliver for free.
- Cap the free diagnosis at 3 bullets unless I explicitly ask for the paid report.
- Use buyer language before technical language.
```

## Prompt 5 - Post Polish Gate

```text
Run a publishable copy gate on this LinkedIn post.

User-calibrated standard:
The copy must have punch, voice, tension, buyer language, brand/news/attention anchor, proof mechanism, anti-slop, and a concrete artifact-first CTA.

Score each 1-10, but do not give 9+ unless there is live market proof.

Return:
- Verdict: PASS / REVISE
- weakest 3 dimensions
- exact line-level revisions
- a stronger hook
- a stronger rehook
- a stronger first comment
- whether it still sounds like generic AI consulting

Post:
[paste]
```

## Visual Asset Briefs

### Asset 1 - Featured Tool Card

| Field | Direction |
|---|---|
| Size | LinkedIn Featured/document thumbnail friendly: 1200 x 627 and 1080 x 1080 variants. |
| Headline | Paste one AI output. See where it guessed. |
| Subhead | Instant AI Misfire Diagnostic for founder-led experts. |
| Visual | Split-screen: left "polished output"; right "Misfire Map" with highlighted guess points. |
| Style | Clean diagnostic markup, white/ink base, one sharp accent color, document-review feel. |
| Avoid | Robots, blue-glow AI imagery, generic circuit boards, vague futuristic gradients. |

### Asset 2 - Demo Screenshot Sequence

| Frame | Caption | Visual |
|---|---|---|
| 1 | The output looked done. | AI-generated paragraph with generic phrases highlighted. |
| 2 | But the work was missing. | Labels: buyer language, proof rule, CTA timing, source of truth. |
| 3 | The correction became the system. | First work primitive: rule, example, boundary, quality test. |

### Asset 3 - LinkedIn Banner

| Field | Direction |
|---|---|
| Headline | Creative Strategist + AI Operating Partner |
| Support line | Customer language + founder judgment -> AI-ready marketing systems |
| Visual | Diagnostic desk / annotated document / before-after system map. |
| CTA | Send one misfire. |

### Asset 4 - Carousel

| Slide | Copy |
|---:|---|
| 1 | The most dangerous AI output is the one that looks finished. |
| 2 | The founder reads it and thinks: "close, but not what we mean." |
| 3 | That sentence is diagnostic data. |
| 4 | AI guessed because the marketing system was invisible. |
| 5 | Missing: customer language, proof rules, CTA timing, source of truth, taste boundaries. |
| 6 | The correction becomes the first rule. |
| 7 | Paste one output. Get the Misfire Map. |

## Tool Deployment Options

| Option | Speed | Notes |
|---|---|---|
| Local demo | Immediate | Use the local tool to record Loom/screenshots today. |
| Netlify/Vercel static site | Fast | Deploy the static files when ready. Add a real form endpoint later. |
| Tally/Typeform + manual report | Fastest external form | Better for capture, weaker for instant transformation. |
| Custom app with email backend | Best long-term | Connect email/report delivery after the proof of demand. |

## First Recording Script

```text
Most lead magnets ask you to trust the framework.

This one lets you test the problem.

Paste an AI output that looked finished but still needed rescue.

Tell it what you wanted.

Tell it what felt off.

The diagnostic maps where the system guessed: buyer language, proof, mechanism, CTA timing, source of truth, and boundaries.

This is the same pattern I look for in AI Misfire Maps.

The goal is not better AI content.

The goal is making the marketing judgment behind the content visible enough for AI to use.
```

