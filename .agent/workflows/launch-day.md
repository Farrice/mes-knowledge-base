---
description: Produce 3-5 content pieces in parallel with Brand Voice consistency review via Agent Teams — your content launch day on autopilot
---

# /launch-day — Content Launch Day Sprint

Produce multi-platform content simultaneously, then run a Brand Voice consistency audit before delivery. Uses Agent Teams (Tier 2) so a brand reviewer can coordinate with the content writers.

## Usage

```
/launch-day [topic]
/launch-day --formats "linkedin, twitter, email" [topic]
/launch-day "Why most AI tools fail solopreneurs" --cta "link to newsletter"
```

## When to Use

- Content day: produce a week's cross-platform content in one session
- Product launch: need coordinated messaging across email + social + video
- Authority push: one big idea expressed across every platform you're on

---

## Steps

### 1. Capture the Brief

From the user's topic, determine:
- **Core message**: The single idea all content shares
- **Target audience**: Default from FARRICE.md (multi-passionate solopreneurs)
- **Formats**: Default all 5; user can specify a subset
- **CTA**: Offer URL, newsletter signup, or "build authority" (organic)

Present:

```markdown
## Launch Day Sprint

**Topic**: [topic]
**Core message**: [1-line distillation]
**CTA**: [offer/link or "build authority"]

| # | Format | Expert | Deliverable |
|---|--------|--------|-------------|
| 1 | LinkedIn post | Lara Acosta | 1 post, hook + CTA |
| 2 | Twitter thread | Shaan Puri | 5-7 tweet thread |
| 3 | Email | Cardinal Mason | 1 conversion email |
| 4 | TikTok script | Seena Rez | 30-60s PSAEP script |
| 5 | Blog article | Nicolas Cole | 800-1200 word article |

**Post-generation**: Brand Voice Consistency Review (Erica Mallet methodology)

Launch all 5 + reviewer? Or adjust?
```

Wait for user approval.

### 2. Create the Agent Team

Use `TeamCreate` with `team_name: "launch-day"`.

Then spawn **all agents in a single message** — 5 content agents + 1 brand reviewer (6 total as teammates):

#### Content Agent Prompt Template

Each content agent gets this structure (replace bracketed fields per format):

```
You are [Expert Name], writing a [format] as part of a launch-day content sprint.
Your name on this team is "[format-slug]-writer".

## PHASE 1: SKILL ACQUISITION
Read these files in order:
1. /Users/farricecain/Google Antigravity/skills/[skill-name]/SKILL.md
2. /Users/farricecain/Google Antigravity/skills/[skill-name]/genius.md
3. /Users/farricecain/Google Antigravity/skills/[skill-name]/workflows/[workflow].md

## PHASE 2: CONTEXT
**Topic**: [topic]
**Core message**: [message]
**CTA**: [cta]
**Target audience**: Multi-passionate, nerdy, spiritual solopreneurs
**Voice markers**: Anti-guru skepticism, "systems AND soul," training arcs, course graveyard metaphors, density over length

## PHASE 3: EXPERT-DRIVEN EXECUTION
Produce a [format] applying [Expert Name]'s methodology fully.
Write output to: .tmp/launch-day/[format-slug].md

## PHASE 4: RECURSIVE REFLECTION
Would [Expert Name] be proud? Is this Farrice's voice informed by the expert's methodology?

## VERIFICATION
SKILL FILES READ: [list] | PATTERNS APPLIED: [list] | QUALITY CHECK: [pass/fail]
```

#### Expert Routing

| Format | Skill Name | Workflow | Output File |
|--------|-----------|----------|-------------|
| LinkedIn | lara-acosta-linkedin-mastery | high-performance-content-engine.md | `.tmp/launch-day/linkedin-post.md` |
| Twitter | shaan-puri-storytelling | viral-social-content-engine.md | `.tmp/launch-day/twitter-thread.md` |
| Email | cardinal-mason-ai-copywriting | 04-authority-content-multiplication.md | `.tmp/launch-day/email.md` |
| TikTok | seena-rez-tiktok-commerce | viral-video-production-engine.md | `.tmp/launch-day/tiktok-script.md` |
| Blog | nicolas-cole-sentence-craft | atomic-compression-density-audit.md | `.tmp/launch-day/blog-article.md` |

#### Brand Reviewer Prompt

```
You are the Brand Voice Reviewer on team "launch-day". Your name is "brand-reviewer".

Your role: Wait for a message from the team lead telling you content is ready, then perform a brand voice consistency audit.

## SKILL ACQUISITION
Read these files FIRST:
1. /Users/farricecain/Google Antigravity/FARRICE.md — the brand owner's voice, values, vocabulary
2. /Users/farricecain/Google Antigravity/skills/erica-mallet-brand-magnetism/SKILL.md
3. /Users/farricecain/Google Antigravity/skills/erica-mallet-brand-magnetism/genius.md
4. /Users/farricecain/Google Antigravity/skills/erica-mallet-brand-magnetism/workflows/brand-audit-multiplication.md

## WHEN NOTIFIED
Read all content pieces from .tmp/launch-day/ (linkedin-post.md, twitter-thread.md, email.md, tiktok-script.md, blog-article.md — whichever exist).

Produce this audit:

## Brand Voice Audit

### Voice Consistency Score: [1-10]

### Piece-by-Piece Assessment
| Piece | Voice Match (1-10) | Tone Match (1-10) | Vocabulary Match (1-10) | Flags |
|-------|-------------------|-------------------|------------------------|-------|

### Cross-Piece Issues
- [Messaging contradictions between pieces]
- [Tonal whiplash that would confuse the audience]
- [CTA inconsistencies]

### Revision Notes
For each piece scoring below 7: specific, line-level revision instructions.

Write output to: .tmp/launch-day/brand-review.md
Then send a message to the team lead summarizing the audit results.
```

### 3. Collect Content and Trigger Review

After all 5 content agents return, use `SendMessage` to notify the brand-reviewer:

```
Content: "All 5 content pieces are ready in .tmp/launch-day/. Please run the brand voice audit now."
```

Wait for the brand-reviewer to return its audit.

### 4. Apply Revisions (if needed)

After the brand-reviewer returns:

- **All pieces score 7+**: Present as-is with the review summary
- **Any piece scores below 7**: Apply the reviewer's specific revision notes (the main orchestrator makes edits, not another sub-agent)
- **Overall score below 5**: Flag to the user: "Brand voice has significant inconsistencies — review before posting"

### 5. Present Final Output

```markdown
# Launch Day: [Topic]

**Date**: [date]
**Pieces generated**: [N]
**Brand Voice Score**: [overall from reviewer]

---

## 1. LinkedIn Post (via Lara Acosta)
[Full post]

---

## 2. Twitter Thread (via Shaan Puri)
[Full thread]

---

## 3. Email (via Cardinal Mason)
[Full email with subject line]

---

## 4. TikTok Script (via Seena Rez)
[Full script with timing and visual cues]

---

## 5. Blog Article (via Nicolas Cole)
[Full article]

---

## Brand Voice Review Summary
**Overall Score**: [X/10]
[Key findings — what was consistent, what was flagged, what was revised]
```

Save to `.tmp/launch-day/sprint-[date].md`.

### 6. Shutdown Team and Offer Next Steps

Use `SendMessage` with `type: "shutdown_request"` to each teammate. Then offer:
- Edit any piece individually
- Schedule/post directly (if social tools available)
- Generate more formats from the same theme
- Run `/atomize` on the blog article for even more derivative content

---

## Parallelism Details

| Stage | Tier | Why |
|-------|------|-----|
| 5 content agents | Tier 1 (Parallel Task Calls) within Tier 2 team | Each piece is independent |
| Brand review | Tier 2 (Agent Teams) | Reviewer must wait for all content, needs SendMessage notification |
| Revisions | Sequential (main orchestrator) | Simple edits based on review notes |

## Error Handling

- **1 content agent fails**: Other 4 continue. Brand reviewer audits available pieces. Flag the gap.
- **Brand reviewer fails**: Present content without review. Note: "Brand review unavailable — manual voice check recommended."
- **2+ content agents fail**: Abort the sprint, report which failed, offer to retry as `/parallel-content` (simpler path).
- **Brand reviewer returns all scores < 5**: Don't auto-fix. Present the review and ask the user how to proceed.

## Output Files

```
.tmp/launch-day/
  linkedin-post.md
  twitter-thread.md
  email.md
  tiktok-script.md
  blog-article.md
  brand-review.md
  sprint-[date].md   (combined final output)
```
