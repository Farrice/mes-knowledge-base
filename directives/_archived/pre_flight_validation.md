# ✈️ Pre-Flight Validation Directive

> **Purpose**: When the user provides rough, raw, or incomplete intent, DO NOT immediately execute. First present variations and clarify.

---

## When to Trigger Pre-Flight Validation

**Trigger Conditions**:
1. User says something like "I want to build...", "Create a...", "Make me a..."
2. The request is vague or lacks specifics (no clear niche, audience, outcome)
3. The request involves building a new workflow, skill, or multi-step system
4. The user explicitly says "I have an idea" or "I'm thinking about..."

**Do NOT Trigger For**:
- Clear, specific requests with all parameters defined
- Bug fixes or corrections to existing work
- Simple factual questions
- Explicit instructions to "just do it"

---

## The Pre-Flight Validation Protocol

### Step 1: Acknowledge & Reflect
Briefly restate the user's intent to show understanding.
```
"I understand you want to [summary of intent]."
```

### Step 2: Entity Classification
Identify the core entities involved.
```
**Entities Identified**:
- [Entity 1]: [Type] — [What it is]
- [Entity 2]: [Type] — [What it is]
```

### Step 3: Present Variations (2-3 Options)
Show the user different interpretations or approaches.

```markdown
## Option A: [Interpretation Name]
- **Approach**: [Brief description]
- **Output**: [What the user would get]
- **Pros**: [Strengths]
- **Cons**: [Weaknesses]

## Option B: [Interpretation Name]
- **Approach**: [Brief description]
- **Output**: [What the user would get]
- **Pros**: [Strengths]
- **Cons**: [Weaknesses]

## Option C: [Hybrid/Alternative]
- **Approach**: [Brief description]
- **Output**: [What the user would get]
```

### Step 4: Clarifying Questions
Ask targeted questions to resolve ambiguity.
```
**Before I proceed, I need to clarify**:
1. [Question about scope]
2. [Question about audience/intent]
3. [Question about output format]
```

### Step 5: Confirm & Execute
Wait for user confirmation before building.
```
"Once you confirm [Option X], I'll proceed with [deliverable]."
```

---

## Example: Pre-Flight Validation in Action

**User**: "I want to build a tool that helps me find keywords."

**Agent Response (Pre-Flight)**:
---
I understand you want to build a keyword research tool. Let me present some variations:

**Entities Identified**:
- **Keywords**: Could mean SEO keywords, PPC keywords, or content topics
- **Tool**: Could mean a workflow, a Python script, or a full skill

## Option A: SEO Keyword Research Workflow
- **Approach**: Agent-based workflow using `search_web` to find low-competition keywords
- **Output**: A `/hunt-keywords` command you can run anytime
- **Pros**: Fast, grounded in real search data
- **Cons**: Requires manual interpretation of results

## Option B: Full Market Intelligence Skill
- **Approach**: Multi-workflow skill with trend scanning, intent analysis, and brief generation
- **Output**: A complete skill folder with multiple commands
- **Pros**: Comprehensive, reusable across projects
- **Cons**: Takes longer to build, more complex

## Option C: One-Shot Keyword Audit
- **Approach**: I research keywords for a specific niche right now, deliver a brief
- **Output**: A markdown file with your keywords, ready to use
- **Pros**: Immediate value, no setup
- **Cons**: Not reusable for other niches

**Before I proceed**:
1. Which option matches your vision?
2. Is this for SEO, PPC, or content planning?
3. Do you have a specific niche in mind, or is this general-purpose?

---

## Integration with Existing System

This directive integrates with:
- `directives/quality_assurance.md` — Prevents anti-patterns during execution
- `GEMINI.md` — Add reference to this directive in Expert-First Work Protocol
- `/validate-intent` workflow — Explicit workflow for running pre-flight checks

---

*Last Updated: 2026-02-05 | Requested by: Farrice Cain*
