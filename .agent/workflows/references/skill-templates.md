# Skill Templates & Reference

Reference file for `/create-skill`. Contains templates, frontmatter reference, and common patterns for all skill types.

---

## 1. Claude Code Skill — SKILL.md Template

```yaml
---
# === REQUIRED ===
name: skill-name                    # lowercase, hyphens, numbers only. Max 64 chars.
                                    # Prefer gerund form: processing-pdfs, reviewing-code
                                    # Cannot contain "anthropic" or "claude"

description: >-                     # Max 1024 chars. Third person. No XML tags.
  Processes PDF files and extracts text, tables, and form data.
  Use when working with PDF files or when the user mentions
  PDFs, forms, or document extraction.

# === OPTIONAL (add only when needed) ===

# Invocation control
disable-model-invocation: true      # Only user can invoke via /name (default: false)
                                    # Use for: deploy, send, delete, anything with side effects
user-invocable: false               # Only Claude can invoke (default: true)
                                    # Use for: background knowledge, conventions, style guides

# Execution environment
context: fork                       # Run in isolated subagent (no conversation history)
                                    # Only useful for task-type skills with explicit instructions
agent: Explore                      # Subagent type when context: fork
                                    # Options: Explore, Plan, general-purpose, or custom agent name
model: sonnet                       # Model override (sonnet, haiku, opus)
allowed-tools: Read, Grep, Glob     # Restrict which tools Claude can use

# UX
argument-hint: "[filename] [format]" # Autocomplete hint for expected arguments

# Lifecycle
hooks:                              # Hooks scoped to this skill
  PreToolUse:                       # Before tool execution
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: "./scripts/lint.sh"
---

# Skill Title

[1-2 sentence overview]

## Instructions

[Core instructions — what Claude should do]

## Additional Resources

- For detailed reference: see [reference.md](reference.md)
- For examples: see [examples.md](examples.md)
```

### Description Writing Guide

**Format:** Third person. What it does + when to use it.

```yaml
# GOOD — specific triggers, third person, actionable
description: >-
  Generates descriptive commit messages by analyzing git diffs.
  Use when the user asks for help writing commit messages or
  reviewing staged changes.

# GOOD — includes symptoms and keywords
description: >-
  Debugs flaky tests by identifying race conditions and timing
  dependencies. Use when tests pass/fail inconsistently or have
  intermittent failures.

# BAD — too vague
description: Helps with documents

# BAD — first person
description: I can help you process Excel files

# BAD — summarizes workflow (Claude may follow description instead of reading skill)
description: >-
  Use when executing plans - dispatches subagent per task with
  code review between tasks
```

### String Substitutions

| Variable | Description | Example |
|---|---|---|
| `$ARGUMENTS` | All arguments passed | `/skill foo bar` → `foo bar` |
| `$ARGUMENTS[0]` or `$0` | First argument | `/skill foo bar` → `foo` |
| `$ARGUMENTS[1]` or `$1` | Second argument | `/skill foo bar` → `bar` |
| `${CLAUDE_SESSION_ID}` | Current session ID | For logging, session-specific files |
| `${CLAUDE_SKILL_DIR}` | Skill's directory path | Reference bundled scripts |

### Dynamic Context Injection

Run shell commands before skill content reaches Claude:

```markdown
## Current state
- Git status: !`git status --short`
- Current branch: !`git branch --show-current`
- PR diff: !`gh pr diff`
- Package info: !`cat package.json | head -20`
```

Output replaces the placeholder — Claude sees actual data, not the command.

---

## 2. Workflow Command Template

For `.agent/workflows/` slash commands:

```markdown
---
description: One-line description of what this command does
---

# /command-name — Title

[1-2 sentence description of what this workflow produces.]

## Usage

\`\`\`
/command-name [arguments]
\`\`\`

## Steps

### 1. First Step
[Instructions]

### 2. Second Step
[Instructions]

### N. Report
Present summary:
- What was produced
- Where files were created
- Next steps

## Options
- **[option]**: "[trigger phrase]" to [behavior]
```

---

## 3. Expert Completion Engine Skill Template

For `skills/` directory (created via `/extract` or `/convert-extraction`):

### SKILL.md
```yaml
---
name: "[Expert] — [Domain]"
description: "[1-2 sentence value proposition]"
version: "2.0"
format: "completion-engine"
workflows: 3
---

# [Expert] — [Domain]

[2-3 sentence expert context + core genius statement]

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| 01 | [Name] | [Specific deliverable] | [Trigger condition] |
| 02 | [Name] | [Specific deliverable] | [Trigger condition] |
| 03 | [Name] | [Specific deliverable] | [Trigger condition] |

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Legacy Prompts**: [references/_legacy-prompts/](references/_legacy-prompts/) — archived
```

### genius.md
```markdown
# [Expert Name] — Genius Context

> Load this file before executing any workflow. Contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## Genius Patterns
[Pattern Name]
- **What It Does**: [Executable behavior]
- **Deploy When**: [Trigger condition]
- **Success Metric**: [How to verify]

## Hidden Knowledge
[Tacit Insight]
- **Why Others Miss This**: [Explanation]
- **Deploy When**: [Context]
```

### Workflow File (`workflows/01-name.md`)
```yaml
---
name: "[Workflow Name]"
produces: "[Specific deliverable]"
expert: "[Expert Name]"
load_context: "genius.md"
---

# [Expert Name] — [Workflow Name]

## Role
[Expert identity + credibility — 2-3 sentences]

**Before executing**: Read genius.md for full extraction intelligence.

## Input Required
- **[Field 1]**: [Description]
- **[Field 2]**: [Description]

## Workflow

### Phase 1: [Name]
[Steps with embedded genius context]

### Phase 2: [Name]
[Steps building on Phase 1]

### Phase 3: [Name]
[Steps producing final deliverable]

## Output Contract
You will deliver:
- **[Component 1]**: [Exact specification]
- **[Component 2]**: [Exact specification]

Format: [Markdown/table/structure]
Length: [Approximate scope]

## Quality Gate
- [ ] [Expert-specific criterion 1]
- [ ] [Expert-specific criterion 2]
- [ ] [Expert-specific criterion 3]
```

---

## 4. Common Patterns

### Progressive Disclosure

Keep SKILL.md as an overview. Move details to supporting files:

```markdown
# SKILL.md — overview and navigation

## Quick start
[Minimal instructions to get started]

## Advanced features
- **Form filling**: See [FORMS.md](FORMS.md)
- **API reference**: See [REFERENCE.md](REFERENCE.md)
- **Examples**: See [EXAMPLES.md](EXAMPLES.md)
```

Claude loads supporting files only when needed — zero context cost until accessed.

### Plan-Validate-Execute

For batch/destructive operations:

```markdown
## Workflow

1. Analyze requirements
2. Create plan file: `changes.json`
3. Validate: `python scripts/validate.py changes.json`
4. If validation fails → fix plan → re-validate
5. Execute: `python scripts/apply.py changes.json`
6. Verify results
```

### Feedback Loop

Run validator → fix → repeat:

```markdown
1. Make your changes
2. Validate: `python scripts/validate.py`
3. If errors found:
   - Review error messages
   - Fix issues
   - Validate again
4. Only proceed when validation passes
```

### Conditional Workflow

Route based on task type:

```markdown
1. Determine the task type:
   - **Creating new?** → Follow "Creation workflow" below
   - **Editing existing?** → Follow "Editing workflow" below

2. Creation workflow:
   [steps]

3. Editing workflow:
   [steps]
```

### Visual Output

Bundle scripts that generate interactive HTML:

```markdown
## Usage
Run the visualization script:
\`\`\`bash
python ${CLAUDE_SKILL_DIR}/scripts/visualize.py .
\`\`\`
Opens `output.html` in your default browser.
```

### Checklist for Multi-Step Tasks

```markdown
Copy this checklist and track progress:

\`\`\`
Task Progress:
- [ ] Step 1: Analyze input
- [ ] Step 2: Create plan
- [ ] Step 3: Validate plan
- [ ] Step 4: Execute
- [ ] Step 5: Verify output
\`\`\`
```

---

## 5. Quality Checklist

Before deploying any Claude Code skill:

### Core Quality
- [ ] Name: lowercase, hyphens, max 64 chars, no reserved words
- [ ] Description: third person, what + when, max 1024 chars
- [ ] SKILL.md body under 500 lines
- [ ] Heavy content in supporting files (not inline)
- [ ] References one level deep from SKILL.md
- [ ] No time-sensitive information
- [ ] Consistent terminology throughout
- [ ] Concrete examples (not abstract)

### Architecture
- [ ] Progressive disclosure used for complex skills
- [ ] Scripts execute rather than load (unless reference)
- [ ] File paths use forward slashes
- [ ] Descriptive file names
- [ ] Table of contents on long reference files (100+ lines)

### Testing
- [ ] Baseline test: Claude tried task WITHOUT skill
- [ ] Direct invocation works: `/skill-name`
- [ ] Auto-triggering works (if not disabled)
- [ ] Arguments pass through correctly
- [ ] Progressive disclosure loads files on-demand
- [ ] Appears in "What skills are available?"
