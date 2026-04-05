---
description: Stress-test deliverable Creator+Critic agent pair before shipping
---

# /adversarial-review -- Ship-Ready Quality Gate

Stress-test any deliverable with a parallel Scorer + Critic agent pair. The Scorer evaluates against the expert's own quality rubric. The Critic red-teams the output for weaknesses, generic language, and credibility gaps. Returns a revision guide with a SHIP / REVISE / REWORK verdict.

## Usage

```
/adversarial-review [file path]
/adversarial-review .tmp/content-sprint/linkedin-post.md
/adversarial-review  (no arg = uses most recent deliverable from this session)
```

## When to Use

- Before shipping any client-facing deliverable
- After a content sprint or parallel content run -- quality-check before publishing
- When you've revised something 2+ times and need an honest external read
- Before finalizing strategy briefs, proposals, or high-stakes copy
- When the chain's Step 6 finalize scores feel inflated and you want a second opinion

## When NOT to Use

- The deliverable is a first draft you already know needs work (just revise it)
- You need creative alternatives, not critique (use `/variant-sprint`)
- The output is internal/system work (AGENT.md, SKILL.md) -- not worth the cost
- You want adversarial refinement of an *idea* before writing (use `/adversarial-refine`)

---

## Steps

### 1. Accept Deliverable

Take the deliverable via one of:
- **File path**: Read the file at the given path
- **Paste**: Accept pasted content directly
- **Session context**: If no path or paste, identify the most recent expert-domain deliverable produced in this session

Confirm what's being reviewed:

```
## Adversarial Review Target

**Deliverable**: [title or description]
**Source**: [file path or "pasted" or "session output"]
**Domain**: [content / strategy / copy / research / creative]
**Primary expert used**: [expert name]
**Expert skill path**: skills/[skill-name]/

Launching Scorer + Critic in parallel. Stand by.
```

### 2. Identify Domain and Expert

Determine:
- Which expert domain this deliverable belongs to
- Which expert's skill was used to produce it (check session context or infer from content)
- The path to that expert's `genius.md` (contains the 4-7-10 quality rubric)

If the expert can't be determined, use the domain's primary expert from `DOMAIN_REGISTRY.md`.

### 3. Fire 2 Agents IN PARALLEL

Spawn 2 Agent tool calls **in a single message**. Each agent runs independently.

---

**Agent 1: Scorer**

```
You are a quality assessment specialist. Your job is to score a deliverable against the producing expert's own quality standards.

**Deliverable to score**:
[Full text of the deliverable]

**Instructions**:
1. Read the expert's genius file: skills/[skill-name]/genius.md
2. Find the quality rubric (look for "4-7-10" scoring, quality dimensions, or evaluation criteria)
3. If no explicit rubric exists, construct one from the expert's core principles (3-5 dimensions)
4. Score the deliverable on EACH dimension (1-10 scale)
5. Be honest. Score inflation is the enemy. A 7 means "good, professional work." A 10 means "the expert themselves would showcase this." A 4 means "technically correct but generic."

**Scoring rules**:
- If the output could have been produced WITHOUT loading the expert's skill files, it scores 4 or below on Expert Standard
- If the output uses the expert's terminology but not their actual thinking, it scores 5 or below
- If the output demonstrates the expert's methodology in action (not just referencing it), it scores 7+

**Output format**:
## Quality Scorecard

### Rubric Source
[Where the rubric came from -- genius.md section or constructed from principles]

### Dimension Scores

| Dimension | Score (1-10) | Evidence | Gap to 10 |
|-----------|-------------|----------|-----------|
| [Dimension 1] | [score] | [specific passage or absence that justifies score] | [what a 10 would look like] |
| [Dimension 2] | [score] | [evidence] | [gap] |
| [Dimension 3] | [score] | [evidence] | [gap] |
| [Dimension 4] | [score] | [evidence] | [gap] |

### Overall Expert Standard Score: [X/10]

### Honest Assessment
[2-3 sentences: Would [Expert Name] be proud of this? Why or why not?]

Write output to: .tmp/adversarial-review/scorer.md
```

---

**Agent 2: Critic**

```
You are a ruthless but constructive critic. Your job is to red-team a deliverable and find every weakness before the audience does.

**Deliverable to critique**:
[Full text of the deliverable]

**Domain**: [domain]
**Intended audience**: [audience, from session context or FARRICE.md ICP]

**Instructions**:
1. Read through the entire deliverable as a skeptical member of the target audience
2. Run the prose classifier:
   ```bash
   python3 execution/prose_classifier.py "[first 500 chars of deliverable]"
   ```
3. Identify ALL of the following:

**Weakness scan**:
- **Weakest section**: Which part would a reader skip or disengage from? Why?
- **Most generic/AI-sounding passage**: Which lines could have come from any AI without expert loading? Quote them exactly.
- **Least credible claim**: Which claim would a skeptic challenge first? Is there proof behind it?
- **Missing proof**: Where does the deliverable assert without demonstrating? (Tell vs Show violations)
- **Disengagement points**: Where would the target audience's attention drop? Map the attention curve.
- **Structural issues**: Flow breaks, redundancy, pacing problems, weak transitions
- **Voice authenticity**: Does this sound like a real human or a writing machine? Flag specific lines.

**AI prose detection**:
- Flag any sentences that match common AI patterns: "In today's...", "It's important to...", "Let's dive in...", "game-changer", "moreover", "comprehensive", "landscape", "leverage", "utilize"
- Flag structural AI tells: uniform paragraph length, predictable alternation, list-heavy without narrative, hedging language

4. Rank all weaknesses by impact on overall quality (high/medium/low)

**Output format**:
## Red Team Report

### Prose Classifier Result
[Output from prose_classifier.py]

### Top Weaknesses (ranked by impact)

**1. [Weakness name]** -- Impact: HIGH
- **Where**: [Quote the specific passage]
- **Why it fails**: [Specific reason]
- **Fix**: [Concrete rewrite suggestion, not "improve this"]

**2. [Weakness name]** -- Impact: HIGH
- **Where**: [Quote]
- **Why it fails**: [Reason]
- **Fix**: [Concrete suggestion]

**3. [Weakness name]** -- Impact: MEDIUM
- **Where**: [Quote]
- **Why it fails**: [Reason]
- **Fix**: [Concrete suggestion]

[Continue for all weaknesses found]

### AI Prose Flags
| Line/Passage | AI Pattern Detected | Suggested Rewrite |
|-------------|--------------------|--------------------|
| "[passage]" | [pattern name] | "[rewrite]" |

### Attention Curve
[Map where engagement is HIGH / MEDIUM / LOW through the piece]
- Opening: [HIGH/MED/LOW] -- [why]
- Middle: [HIGH/MED/LOW] -- [why]
- Close: [HIGH/MED/LOW] -- [why]

### Strongest Element
[What's genuinely good about this deliverable -- the Critic must acknowledge strengths too]

Write output to: .tmp/adversarial-review/critic.md
```

### 4. Wait for Both Agents to Return

Both agents run independently and write outputs to `.tmp/adversarial-review/`. Wait for both to complete.

### 5. Synthesize into Revision Guide

Read both outputs and produce a unified revision guide:

```markdown
# Adversarial Review: [Deliverable Title]

**Date**: [date]
**Expert used**: [expert name]
**Domain**: [domain]

---

## Rubric Scorecard

| Dimension | Score | Key Evidence |
|-----------|-------|-------------|
| [Dim 1] | [X/10] | [1-line summary] |
| [Dim 2] | [X/10] | [1-line] |
| [Dim 3] | [X/10] | [1-line] |
| [Dim 4] | [X/10] | [1-line] |
| **Overall** | **[X/10]** | |

---

## Top 3 Weaknesses (ranked by impact on quality)

### 1. [Weakness Name]
**Impact**: [HIGH/MEDIUM]
**What's wrong**: [Specific diagnosis -- quote the offending passage]
**Fix**: [Actual rewrite or structural change -- not "make it better"]

### 2. [Weakness Name]
**Impact**: [HIGH/MEDIUM]
**What's wrong**: [Diagnosis]
**Fix**: [Rewrite]

### 3. [Weakness Name]
**Impact**: [HIGH/MEDIUM]
**What's wrong**: [Diagnosis]
**Fix**: [Rewrite]

---

## Prose Classifier Result
[Full output from prose_classifier.py]

## AI Prose Flags
[Summary of any AI-sounding passages with rewrites]

---

## Verdict: [SHIP / REVISE / REWORK]

**SHIP** = Overall score 8+ AND no HIGH-impact weaknesses. Ready to publish/send.
**REVISE** = Overall score 6-7 OR 1-2 HIGH-impact weaknesses with clear fixes. Fix the top weaknesses and it's ready.
**REWORK** = Overall score below 6 OR 3+ HIGH-impact weaknesses. Fundamental issues require a new approach, not surface edits.

### If REVISE:
Estimated revision effort: [10 min / 30 min / 1 hour]
Priority order: Fix weakness #1 first, then #2, then #3.

### If REWORK:
Root cause: [Why the deliverable failed at a fundamental level]
Recommended approach: [What to do differently -- reload expert at Tier 2? Use different expert? Run writers' room?]
```

Save to `.tmp/adversarial-review/review-[deliverable-slug].md`.

---

## Verdict Calibration

The verdict is NOT a feeling. It maps to specific thresholds:

| Verdict | Overall Score | HIGH-Impact Weaknesses | Action |
|---------|--------------|----------------------|--------|
| SHIP | 8+ | 0 | Publish as-is (minor polish optional) |
| REVISE | 6-7 | 0-2 | Fix listed weaknesses, then ship |
| REWORK | Below 6 | 3+ | Re-approach from scratch with different strategy |

## Anti-Patterns

- **Don't inflate scores.** A 7 is genuinely good work. Most first drafts are 5-6. Reserve 9-10 for work that would make the expert proud to put their name on.
- **Don't give vague fixes.** "Improve the opening" is useless. "Replace the current opening with a specific client story that demonstrates the problem" is actionable.
- **Don't skip the prose classifier.** It catches AI patterns that human reading misses.
- **Don't ignore the Scorer when the Critic is harsh (or vice versa).** Both perspectives matter. A high Scorer + harsh Critic means "good bones, rough surface." A low Scorer + gentle Critic means "smooth surface, hollow inside."
- **Don't use this as procrastination.** If the deliverable is clearly ready, ship it. The review exists for genuine uncertainty, not perfectionism.

---

## Follow-Up Workflows

After reviewing:
- **SHIP**: Finalize with `/rate` or chain Step 6
- **REVISE**: Edit manually or run `/writers-room` on the specific weak sections
- **REWORK**: Route back through the chain from Step 3 (re-select expert or escalate to Tier 2)

---

*Created: 2026-04-03*
*Related workflows: `/adversarial-refine` (for ideas), `/writers-room` (for content revision), `/rate` (quick scoring)*
