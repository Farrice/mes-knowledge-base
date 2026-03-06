---
description: Create a new skill — routes between Claude Code skills, workflow commands, and expert completion engine skills
---

# /create-skill — Skill Creation Workflow

Create any type of skill in the Antigravity system, following latest Anthropic best practices (March 2026).

## Usage

```
/create-skill [optional: skill name or description]
```

## Step 1: Route — What Are You Building?

Ask the user (if not obvious from context):

| If they want to... | Type | Go to |
|---|---|---|
| **Extend Claude's capabilities** (commands, workflows, reference, behavioral instructions) | Claude Code Skill | Step 2 |
| **Create a reusable workflow command** (a `/slash-command` that executes a process) | Workflow Command | Step 8 |
| **Package expert knowledge** from source material into deployable expertise | Expert Completion Engine | Redirect to `/extract` |
| **Convert an existing extraction** into a completion engine skill | Expert Completion Engine | Redirect to `/convert-extraction` |

**Quick decision guide:**
- "I want Claude to always do X when Y happens" → **Claude Code Skill**
- "I want a command I can run to do X" → **Workflow Command** (if multi-step process) or **Claude Code Skill** (if simple)
- "I have a transcript/article from an expert" → **`/extract`**

---

## Claude Code Skill Creation (Steps 2-7)

### Step 2: Define & Scope

Gather these from the user (fill in what you can infer, confirm):

**Required:**
- **Name**: Lowercase letters, numbers, hyphens only. Max 64 chars. Prefer gerund form (`processing-pdfs`, `reviewing-code`). Cannot contain "anthropic" or "claude".
- **Description**: Third person. What it does AND when to use. Max 1024 chars. Include specific trigger keywords.
- **Purpose**: What capability does this add?

**Classification:**
- **Reference** — adds knowledge Claude applies to current work (conventions, patterns, style guides)
- **Task** — step-by-step instructions for a specific action (deploy, commit, generate)
- **Technique** — reusable method with clear steps (debugging, testing, reviewing)

**Location:**
- Personal (`~/.claude/skills/[name]/`) — available in all your projects
- Project (`.claude/skills/[name]/`) — available in this project only

**Invocation model:**
- Both user and Claude can invoke (default)
- User-only: `disable-model-invocation: true` — for workflows with side effects
- Claude-only: `user-invocable: false` — for background knowledge

### Step 3: Architecture

Determine the skill's structure based on complexity:

**Simple skill** (< 100 lines of instructions):
```
skill-name/
└── SKILL.md
```

**Standard skill** (100-500 lines, or needs supporting files):
```
skill-name/
├── SKILL.md           # Overview + navigation (< 500 lines)
├── reference.md       # Detailed docs (loaded on-demand)
└── examples.md        # Usage examples (loaded on-demand)
```

**Complex skill** (domain-specific, scripts, multiple reference files):
```
skill-name/
├── SKILL.md           # Overview + navigation (< 500 lines)
├── reference/
│   ├── domain-a.md    # Domain-specific reference
│   └── domain-b.md    # Domain-specific reference
├── examples.md        # Usage examples
└── scripts/
    ├── validate.py    # Utility script (executed, not loaded)
    └── generate.sh    # Generation script
```

**Key architecture rules (from Anthropic best practices):**
- SKILL.md body under 500 lines — move heavy content to supporting files
- References one level deep from SKILL.md — no nested chains
- Long reference files (100+ lines) get a table of contents at top
- Name files descriptively: `form_validation_rules.md`, not `doc2.md`
- Forward slashes only in paths (no backslashes)
- Scripts are **executed** (not loaded into context) unless explicitly marked as reference

### Step 4: Configure Frontmatter

Build the YAML frontmatter based on the skill's needs. Read `references/skill-templates.md` for the complete template with all fields.

**Always include:**
```yaml
---
name: skill-name
description: What this skill does and when to use it. Third person. Include trigger keywords.
---
```

**Add these as needed:**

| Field | When to Add | Example |
|-------|-------------|---------|
| `disable-model-invocation: true` | Skill has side effects (deploy, send, delete) | Deploy, messaging |
| `user-invocable: false` | Background knowledge Claude should auto-apply | API conventions |
| `allowed-tools: Read, Grep` | Restrict tools for safety | Read-only analysis |
| `context: fork` | Run in isolated subagent (won't see conversation) | Heavy research tasks |
| `agent: Explore` | Specify subagent type when using `context: fork` | Codebase exploration |
| `model: sonnet` | Override model for this skill | Cost-sensitive tasks |
| `argument-hint: [filename]` | Show autocomplete hint for expected args | `/skill issue-123` |
| `hooks: {...}` | Lifecycle hooks scoped to this skill | Auto-lint after edits |

### Step 5: Scaffold

Create the directory structure and generate SKILL.md with the configured frontmatter and placeholder content.

```bash
mkdir -p [location]/[skill-name]/scripts  # if scripts needed
```

**Write SKILL.md** following this structure:

```markdown
---
name: [name]
description: [description]
[additional frontmatter fields as determined in Step 4]
---

# [Skill Title]

[1-2 sentence overview — what this skill does]

## [Main Instructions]

[Core content — what Claude should do when this skill is active]

## Additional Resources  (if supporting files exist)

- For [topic]: see [reference.md](reference.md)
- For [examples]: see [examples.md](examples.md)
```

**Write supporting files** as needed — each with a clear table of contents if over 100 lines.

### Step 6: Write Content

This is the core creative step — the user should provide or co-create the actual skill logic.

**Content guidelines (from Anthropic best practices):**

1. **Concise is key.** Claude is smart — only add context Claude doesn't already have. Challenge each paragraph: "Does Claude really need this?"

2. **Match degree of freedom to fragility:**
   - High freedom for flexible tasks (code review, analysis)
   - Low freedom for fragile operations (database migrations, deployments)

3. **Use workflows for complex tasks.** Break into clear sequential steps. For multi-step processes, provide a checklist Claude can track.

4. **Implement feedback loops.** Pattern: run validator → fix errors → repeat. Greatly improves output quality.

5. **Plan-validate-execute** for batch/destructive operations. Create intermediate plan file → validate with script → execute only after validation passes.

6. **One default approach, not many options.** Don't present 5 libraries — pick one and mention alternatives only when a specific trigger applies.

7. **Consistent terminology.** Pick one term and use it throughout (not "endpoint" / "URL" / "path" / "route" interchangeably).

8. **No time-sensitive information.** Use "current method" / "old patterns" sections instead of dates.

9. **Use examples for output quality.** Input/output pairs help more than descriptions.

10. **Dynamic context injection** — for skills that need live data:
    ```
    !`gh pr diff`        # Injects actual PR diff
    !`git status`        # Injects current git status
    !`cat package.json`  # Injects file content
    ```

11. **String substitutions** available:
    - `$ARGUMENTS` — all args passed to the skill
    - `$ARGUMENTS[0]`, `$1` — positional args
    - `${CLAUDE_SESSION_ID}` — current session ID
    - `${CLAUDE_SKILL_DIR}` — directory containing SKILL.md

### Step 7: Test & Deploy

**7a. Baseline test (evaluate WITHOUT the skill):**
Ask Claude to perform the task the skill is designed for, WITHOUT the skill loaded. Document what it does wrong or misses. This establishes what the skill needs to teach.

**7b. Test WITH the skill:**
- Test direct invocation: `/skill-name [args]`
- Test auto-triggering: describe the task naturally and see if Claude loads the skill
- Test progressive disclosure: does Claude load supporting files only when needed?
- Test with arguments if applicable

**7c. Verify discovery:**
Ask "What skills are available?" — the skill should appear.

**7d. Iterate:**
If Claude doesn't trigger when it should → improve description keywords.
If Claude triggers when it shouldn't → make description more specific.
If Claude ignores supporting files → make references more explicit in SKILL.md.

**7e. Deploy:**
- Commit to git
- Verify it appears in skill list

---

## Workflow Command Creation (Steps 8-10)

For `.agent/workflows/` commands — the Antigravity slash command system.

### Step 8: Define the Command

- **Name**: kebab-case, action-oriented (`create-skill`, `deploy-skill`, `research-topic`)
- **Purpose**: What process does this command execute?
- **Inputs**: What does it need from the user?
- **Output**: What deliverable does it produce?

### Step 9: Write the Workflow

Create `.agent/workflows/[command-name].md`:

```markdown
---
description: [One-line description of what this command does]
---

# /[command-name] — [Title]

[1-2 sentence description of what this workflow produces.]

## Usage

\```
/[command-name] [arguments]
\```

## Steps

### 1. [First Step Name]
[Instructions for step 1]

### 2. [Second Step Name]
[Instructions for step 2]

### N. Report
Present summary of what was produced.

## Options
- **[option]**: "[trigger phrase]" to [behavior]
```

**Conventions:**
- Frontmatter only needs `description`
- Steps are numbered with `### N. Name` headers
- Include checkpoints (`CHECKPOINT`) before irreversible actions
- Mark turbo steps with `// turbo` for parallel execution
- End with a Report step summarizing what was produced
- Include an Options section for alternative modes

### Step 10: Register

Add the command to `SLASH_COMMANDS.md` under the appropriate category.

Format:
```markdown
* **`/[command-name]`** — [One-line description matching the frontmatter description].
```

---

## Quick Reference: Skill Types Comparison

| Aspect | Claude Code Skill | Workflow Command | Expert Completion Engine |
|---|---|---|---|
| **Location** | `.claude/skills/[name]/` | `.agent/workflows/[name].md` | `skills/[name]/` |
| **Format** | SKILL.md + supporting files | Single markdown file | SKILL.md + genius.md + workflows/ |
| **Invocation** | `/name` or auto-triggered | `/name` only | Via `/deploy-skill` |
| **Frontmatter** | name, description + 8 optional fields | description only | name, description, version, format, workflows |
| **Best for** | Extending Claude's behavior | Multi-step processes | Expert knowledge deployment |
| **Standard** | Agent Skills (agentskills.io) | Antigravity custom | Completion Engine v2.0 |
| **Create with** | This workflow (Steps 2-7) | This workflow (Steps 8-10) | `/extract` or `/convert-extraction` |
