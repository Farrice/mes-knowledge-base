# Skill Evolution Sprint — Evolution Hypotheses & Variant Design

## Background

Benchmarking identified two skills for evolution:

| Skill | Avg Score | Weakest Dimension | Weakest Workflow |
|-------|-----------|-------------------|------------------|
| `lara-acosta-linkedin-mastery` | 7.3/10 | Adversarial Resilience | `high-performance-content-engine` |
| `luke-iha-proof-ladder` | 8.3/10 | Expert Standard | `proof-copy-engine` |

---

## Skill 1: `lara-acosta-linkedin-mastery` — Adversarial Resilience

### Diagnosis

The current `high-performance-content-engine.md` (87 lines) has **no adversarial defense layer**. Specifically:

1. **No objection pre-emption** — Content doesn't anticipate or address skepticism ("LinkedIn Lunatics" backlash, humble-brag detection, "sounds like an AI" dismissal)
2. **No competitive differentiation gate** — Posts don't check "could a competitor write this exact post?"
3. **Quality gate is surface-level** — 5 checks, all positive-framing ("does this work?") rather than adversarial ("how would a critic attack this?")
4. **Missing genius patterns** — Pattern 22 (Post & Ghost Kill Switch) and Pattern 23 (Revenue Bridge) are not integrated into the workflow despite being in genius.md

### Evolution Hypothesis

> **If we add an Adversarial Resilience Layer** (critic persona audit + competitive uniqueness gate + anti-pattern stress test) **and integrate the missing 2026 genius patterns** (Revenue Bridge + Post & Ghost), **then the quality score will increase from 7.3 → 8.0+** because content will survive scrutiny instead of just performing on friendly metrics.

### Proposed Changes

#### [MODIFY] [high-performance-content-engine.md](file:///Users/farricecain/Google%20Antigravity/skills/lara-acosta-linkedin-mastery/workflows/high-performance-content-engine.md)

**Changes to make:**

1. **Add Phase 4.5: Adversarial Resilience Pass** (between Copy Execution and Growth Engine):
   - **The Critic's Eye**: Read every post as a skeptic. Flag anything that sounds like "generic LinkedIn advice," humble-bragging, or could trigger the "LinkedIn Lunatics" subreddit
   - **Competitive Uniqueness Gate**: For each post ask "Could [competitor name] post this word-for-word?" If yes → add proprietary methodology, specific numbers, or personal story that ONLY this author could write
   - **The Damaging Admission Injection**: At least 1 post per week must contain a genuine admission of failure or limitation (genius Pattern 5 + Luke Iha's Disarming Admission crossover)

2. **Add Phase 5.5: Revenue Bridge Integration** (genius Pattern 23):
   - Map each content type (4-3-2-1) to its role in the Revenue Bridge
   - Ensure lead magnet posts link to email capture, not direct sales
   - Annotate each post with its funnel position

3. **Upgrade Quality Gate** from 5 → 9 checks:
   - Add: **LinkedIn Lunatics Test** — Would this post be screenshot-mocked?
   - Add: **The "Replace My Name" Test** — Is any post interchangeable with a generic guru?
   - Add: **Revenue Bridge Compliance** — Does the monthly calendar feed email capture?
   - Add: **First-Hour Engagement Plan** — Is Post & Ghost protocol attached to each content day?

---

## Skill 2: `luke-iha-proof-ladder` — Expert Standard

### Diagnosis

The current `proof-copy-engine.md` (318 lines) is *architecturally strong* but has one critical gap:

1. **Narrative Weaving Mandate is aspirational, not procedural** — Phase 4 says "proof must feel like natural story momentum" but gives no concrete *technique* for achieving this
2. **Platform templates are mechanical** — LinkedIn, YouTube, etc. use bracket-formatted templates that produce structurally correct but "proof-report-dressed-as-story" output
3. **No voice calibration step** — Copy produced passes all proof gates but sounds like "a Luke Iha student" rather than the client's authentic voice
4. **Missing the "Coffee Test" enforcement** — The coffee test is described in Phase 4 but there's no structural enforcement (it's just a suggestion)

### Evolution Hypothesis

> **If we add a Narrative Integration Protocol** (proof-through-story techniques + voice calibration checkpoint + mandatory Coffee Test rewrite pass) **then the Expert Standard score will increase from 8.3 → 9.0+** because copy will sound like a real human WITH proof instincts rather than a proof robot wearing a human mask.

### Proposed Changes

#### [MODIFY] [proof-copy-engine.md](file:///Users/farricecain/Google%20Antigravity/skills/luke-iha-proof-ladder/workflows/proof-copy-engine.md)

**Changes to make:**

1. **Add Phase 3.5: Narrative Proof Techniques** (between Architecture and Platform Production):
   - **The Discovery Reveal**: Instead of "Here's a stat," structure proof as the character discovering the proof naturally: "When I ran the numbers... I found..."
   - **The Contrast Mechanism**: Frame proof through what DIDN'T work first → creates narrative tension that makes the proof land harder
   - **The Implication Bridge**: After every proof point, add one sentence on what this MEANS for the reader (proof → so what → personal relevance)

2. **Add Phase 3.7: Voice Calibration Checkpoint**:
   - Before platform production, require 2-3 reference samples of the client's actual voice
   - Map voice markers: sentence length, formality level, humor frequency, jargon comfort
   - After producing copy, do a "voice audit" — highlight every phrase the client would NOT say

3. **Upgrade Phase 4 from advisory → mandatory**:
   - **Coffee Test Rewrite**: After the read-aloud pass, rewrite any section that sounds like "citing sources" into "telling a story with numbers"
   - **Proof Velocity Check**: Ensure no section has 2+ proof points within 3 sentences (proof compounding, not competing)
   - **Loop Verification**: Number each open loop and verify each one closes before or at the CTA

---

## Verification Plan

### Testing Protocol

For each skill, run 3 standard benchmark tasks:

**Lara Acosta benchmarks:**
1. Write a LinkedIn post about a career pivot (Story type)
2. Generate a weekly content calendar for a B2B SaaS founder
3. Create a lead magnet promotional sequence

**Luke Iha benchmarks:**
1. Write a LinkedIn post selling a $2,000 course to cold audience
2. Write a newsletter edition about pricing psychology
3. Write ad copy for a coaching program

### Scoring

- Run each task twice: once with **current workflow**, once with **variant workflow**
- Score using the expert-specific quality rubric from each `genius.md`
- Require the variant to score **≥ 0.5 higher** on the weakest dimension to be accepted
- If variant scores lower on ANY dimension by more than 0.3, reject it

### Deployment

- If variant passes → replace the current workflow
- Log results to Notion Performance DB
- Update task.md checklist
