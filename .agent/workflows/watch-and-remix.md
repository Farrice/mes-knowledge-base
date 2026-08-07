---
description: Study trending/viral content, reverse-engineer the mechanic that made
---

# /watch-and-remix — Viral Mechanic Reverse Engineering

Find content that's performing well online, extract the structural mechanic that makes it work, then generate 3 original remixes in Farrice's voice using different expert agents. Learn from what's winning without copying.

## Usage

```
/watch-and-remix [URL]
/watch-and-remix https://linkedin.com/posts/creator-viral-post
/watch-and-remix https://twitter.com/user/status/123456789
/watch-and-remix "paste the full text of a viral post here"
```

## When to Use

- You spotted a trending post/video and want to create your own version
- You want to study what formats and structures are performing well
- You need content inspiration grounded in real performance data, not hypotheticals
- You want to build a library of proven mechanics you can deploy anytime

---

## Steps

### 1. Ingest the Source

Handle input based on type:

| Input Type | Action |
|------------|--------|
| LinkedIn URL | Playwright (`browser_navigate` + `browser_evaluate`) — `read_url_content` returns empty hydration shells on LinkedIn |
| Twitter/X URL | Playwright (`browser_navigate` + `browser_evaluate`) — same JS-rendering issue |
| Instagram / TikTok URL | Playwright with persistent profile (login-gated) per `directives/browser-automation-routing.md` |
| YouTube URL | Run `python3 execution/fetch-transcript.py "[url]" "source"` AND `python3 execution/fetch-video-context.py "[url]" "source" \|\| true` (visual frames are critical for video viral mechanics — visual hooks, B-roll cadence, on-screen text are 50% of why short-form video goes viral). See [`directives/video-vision-protocol.md`](../../directives/video-vision-protocol.md). |
| Blog/article URL (static) | Use `read_url_content` to extract content |
| Pasted text | Save to `.tmp/watch-and-remix/source.md` |

Save the raw source to `.tmp/watch-and-remix/source.md`.

### 2. Mechanic Extraction (Parallel — 3 Agents)

Spawn 3 Task tool sub-agents **in a single message** to analyze the source from different angles:

**Agent 1: Hook Analyst**
```
You are a content strategist analyzing a viral piece of content.

## SKILL ACQUISITION
Read these files:
1. /Users/farricecain/Google Antigravity/skills/kallaway-content-psychology/SKILL.md
2. /Users/farricecain/Google Antigravity/skills/kallaway-content-psychology/genius.md
3. /Users/farricecain/Google Antigravity/skills/kallaway-content-psychology/workflows/hook-engineering-matrix.md

## SOURCE CONTENT
[Full text of the viral piece]

## VISUAL CONTEXT (if source was video)
If `extractions/source/visual-context.md` exists, READ IT — and READ the first 5 frames in `extractions/source/frames/` directly via the Read tool. The visual hook is often a different beat than the verbal hook (cut-driven, on-screen text, gesture). Analyze BOTH the verbal hook AND the visual hook patterns.

## YOUR ANALYSIS
Focus only on the hook—the first 1–3 lines. Describe visible structure first, then label any audience-response explanation as a hypothesis unless supplied performance evidence supports it. Analyze:

1. **Hook type**: Question / Bold claim / Story open / Contrarian / Data shock / Pattern interrupt / Identity call-out
2. **Hook template**: Write the structural pattern with blanks (e.g., "I [shocking action]. Here's what happened:")
3. **Possible psychological response**: What emotion or attention response might the opening invite? Label it `OBSERVED` only when supported by supplied evidence; otherwise `HYPOTHESIS`.
4. **Opening mechanics**: What visible or structural element could attract attention? Describe the element as observed and its behavioral effect as a hypothesis.

Write to: .tmp/watch-and-remix/analysis-hook.md
```

**Agent 2: Framework Analyst**
```
You are a content architect analyzing a viral piece of content.

## SKILL ACQUISITION
Read these files:
1. /Users/farricecain/Google Antigravity/skills/dan-koe-multipassionate-mastery/SKILL.md
2. /Users/farricecain/Google Antigravity/skills/dan-koe-multipassionate-mastery/genius.md
3. /Users/farricecain/Google Antigravity/skills/dan-koe-multipassionate-mastery/workflows/infinite-content-engine.md

## SOURCE CONTENT
[Full text of the viral piece]

## YOUR ANALYSIS
Focus ONLY on the structural framework — the skeleton that holds the piece together:

1. **Content pattern**: Listicle / PAS (Problem-Agitate-Solve) / Before-After / Story Arc / Myth-Busting / How-To / Rant / Framework reveal
2. **Skeleton with blanks**: Write the numbered/sequenced structure as a template others could fill in
3. **Pacing analysis**: Short punchy sentences? Long narrative? Alternating? Where does it speed up/slow down?
4. **Information density**: High (every line teaches) / Medium (mix of story and insight) / Low (emotional narrative)
5. **Transitions**: How does it move between points? Numbering? "But here's the thing"? "Most people miss this"?

Write to: .tmp/watch-and-remix/analysis-framework.md
```

**Agent 3: Engagement Analyst**
```
You are an engagement-pattern analyst studying observable content mechanics and forming labeled hypotheses about audience response.

## DECISION-FIRST SKILL ACQUISITION
Read these files first:
1. /Users/farricecain/Google Antigravity/skills/shaan-puri-storytelling/references/story-deployment-map.md
2. /Users/farricecain/Google Antigravity/skills/shaan-puri-storytelling/workflows/shaan-story-deploy.md
3. /Users/farricecain/Google Antigravity/skills/shaan-puri-storytelling/references/prompts-v2/shaan-story-deploy.md

Do not preload `genius.md`. Use the router to decide whether a Shaan mechanic belongs. If the viral workflow is selected, load it and `genius.md` only after the decision. This agent analyzes; it does not become a second body writer.

## SOURCE CONTENT
[Full text of the viral piece]

## YOUR ANALYSIS
Focus only on observable mechanics and clearly labeled hypotheses about why people may have engaged. Do not claim a mechanic drove behavior unless causal evidence is supplied:

1. **Possible audience response**: Label as `OBSERVED` when evidenced by comments or other supplied data; otherwise `HYPOTHESIS`.
2. **Shareability hypothesis**: Identity signal, usefulness, controversy, status, or another mechanism—never present motive as known without evidence.
3. **Response invitations**: Identify structural elements that may invite comments or shares; separate visible behavior from interpretation.
4. **CTA pattern**: How does it drive action? Soft ask? Hard sell? No CTA (pure engagement)?
5. **Audience tribe**: Who is this written FOR? What group identity does it activate?

Write to: .tmp/watch-and-remix/analysis-engagement.md
```

### 3. Synthesize the Mechanic Blueprint

After all 3 agents return, read their analyses and produce a unified blueprint:

```markdown
## Mechanic Blueprint: [Source Description]

**Source**: [URL or description]
**Platform**: [LinkedIn / Twitter / YouTube / etc.]
**Estimated performance**: [If visible — likes, comments, shares]

### The Hook
- **Type**: [from hook analyst]
- **Template**: "[pattern with blanks]"
- **Possible response**: [OBSERVED or HYPOTHESIS + psychological mechanism + evidence]

### The Framework
- **Pattern**: [from framework analyst]
- **Skeleton**:
  1. [Step/section 1 with blank]
  2. [Step/section 2 with blank]
  3. [...]
- **Pacing**: [description]

### The Engagement Engine
- **Possible audience response**: [OBSERVED or HYPOTHESIS + evidence]
- **Shareability hypothesis**: [possible mechanism; do not state motive as known]
- **Response invitation**: [visible element + hypothesized effect]

### Remix Instructions
- **KEEP** (the mechanic): [observed hook structure, framework pattern, pacing, and only evidence-labeled response hypotheses]
- **REPLACE** (the content): [their topic, their examples, their voice, their CTA]
- **ADAPT** (for Farrice): Apply multi-passionate identity, anti-guru positioning, "systems AND soul" lens, training arc metaphors
```

Save to `.tmp/watch-and-remix/mechanic-blueprint.md`.

Present the blueprint to the user — this alone is valuable as a reusable template.

### 4. Generate 3 Remixes (Parallel — 3 Agents)

Spawn 3 more Task tool sub-agents **in a single message**, each creating a different remix:

**Remix 1: Same Platform, Farrice's Topic**
```
You are Lara Acosta (if LinkedIn) / Shaan Puri (if Twitter) / Nicolas Cole (if blog).

## SKILL ACQUISITION
Read the relevant expert's skill files.

If the selected expert is Shaan Puri, execute `.agent/workflows/shaan-story-deploy.md` first and do not preload `genius.md`. Use only the selected dosage and production route.

## MECHANIC BLUEPRINT
[Inject the full mechanic blueprint from Step 3]

## YOUR TASK
Create a remix using the SAME platform format and the SAME structural mechanic, but written about a topic from Farrice's world.

Read /Users/farricecain/Google Antigravity/FARRICE.md for:
- Current positioning and interests
- Voice markers (anti-guru, systems AND soul, training arcs)
- Topics Farrice is passionate about

Pick the topic from Farrice's interest stack that BEST fits this mechanic.

Follow the hook template, framework skeleton, and pacing pattern exactly.
Voice should be distinctly Farrice's — not the original creator's.

Write to: .tmp/watch-and-remix/remix-1-same-platform.md
```

**Remix 2: Same Mechanic, Different Angle**
```
You are Dan Koe, applying the multipassionate mastery lens.

## SKILL ACQUISITION
Read:
1. /Users/farricecain/Google Antigravity/skills/dan-koe-multipassionate-mastery/SKILL.md
2. /Users/farricecain/Google Antigravity/skills/dan-koe-multipassionate-mastery/genius.md

## MECHANIC BLUEPRINT
[Inject blueprint]

## YOUR TASK
Create a remix using the SAME structural mechanic, but approaching from a completely different angle. If the original was tactical, go philosophical. If it was personal story, go data-driven. If it was serious, find the humor.

Apply Farrice's voice and positioning. Read FARRICE.md for context.

Write to: .tmp/watch-and-remix/remix-2-different-angle.md
```

**Remix 3: Cross-Platform Adaptation**
```
You are [platform-appropriate expert — if source is LinkedIn, use Shaan Puri for Twitter; if source is Twitter, use Lara Acosta for LinkedIn; etc.].

## SKILL ACQUISITION
Read the relevant expert's skill files.

If the selected expert is Shaan Puri, execute `.agent/workflows/shaan-story-deploy.md` first and do not preload `genius.md`. Use only the selected dosage and production route.

## MECHANIC BLUEPRINT
[Inject blueprint]

## YOUR TASK
Take this mechanic and ADAPT it to a different platform format.
- LinkedIn → Twitter thread (compress, add thread structure)
- Twitter → LinkedIn post (expand, add depth)
- YouTube → Short-form script (distill to 30-60s)
- Blog → Email newsletter (add personal CTA)

Keep the hook pattern and emotional arc. Adapt the pacing and length to the target platform.
Apply Farrice's voice. Read FARRICE.md for context.

Write to: .tmp/watch-and-remix/remix-3-cross-platform.md
```

### 5. Present Everything

```markdown
# Watch & Remix: [Source Description]

**Source**: [URL]
**Date**: [date]

---

## Mechanic Blueprint

[Full blueprint from Step 3 — the reusable template]

---

## Remix 1: [Platform] — [Topic]
[Full content piece]

## Remix 2: Different Angle — [Topic]
[Full content piece]

## Remix 3: Cross-Platform ([Target Platform]) — [Topic]
[Full content piece]

---

## Mechanic Library Entry
Save this blueprint for future use? It can be referenced anytime you want to create content using this proven structure.
```

Save to `.tmp/watch-and-remix/remix-[date].md`.

### 6. Offer Next Steps

- Edit any remix
- Run `/atomize --remix` on one of the remixes to produce 11 derivative pieces
- Save the mechanic blueprint to a growing library (`.tmp/mechanic-library/`)
- Find more trending content to study

---

## Parallelism Details

| Stage | Tier | Agents | Why |
|-------|------|--------|-----|
| Source ingestion | Sequential | Main orchestrator | Must fetch before analyzing |
| Mechanic extraction | Tier 1 (Parallel Task Calls) | 3 | Each analyst looks at a different dimension |
| Blueprint synthesis | Sequential | Main orchestrator | Must combine all 3 analyses |
| Remix generation | Tier 1 (Parallel Task Calls) | 3 | Each remix is independent |
| Presentation | Sequential | Main orchestrator | Assembly |

**Total**: 6 sub-agents across 2 parallel batches. ~2-4 minutes total.

## Error Handling

- If source fetch fails: ask user to paste the content directly
- If any analyst agent fails: proceed with remaining analyses (2 of 3 is still useful)
- If any remix agent fails: present available remixes, offer to regenerate the failed one

## Output Files

```
.tmp/watch-and-remix/
  source.md
  analysis-hook.md
  analysis-framework.md
  analysis-engagement.md
  mechanic-blueprint.md
  remix-1-same-platform.md
  remix-2-different-angle.md
  remix-3-cross-platform.md
  remix-[date].md   (combined final output)
```

**Execution prompts**: before producing the deliverable, check `skills/kallaway-content-psychology/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
