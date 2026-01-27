---
description: Convert MES 3.0 extractions to production-ready skills with COMPLETE coverage guarantee
---

# /convert-extraction Workflow

This workflow ensures **100% prompt coverage** when converting MES 3.0 extractions to production skills.

## MANDATORY FIRST STEP: Complete Audit

**Before ANY creation work begins:**

```bash
# 1. List all extraction files for the expert
find "/Users/farricecain/Desktop/Cladue Extractions MES 3.0" -name "*ExpertName*" -type f

# 2. For EACH file found, extract all prompt headers
grep -n "^# EXPERTNAME -" "filepath"
```

// turbo-all

Create a **complete prompt inventory** in the task artifact BEFORE writing any files:

```markdown
## Prompt Inventory (COMPLETE)

| # | File | Prompt Name | Line # | Status |
|---|------|-------------|--------|--------|
| 1 | file1.md | PROMPT NAME 1 | 562 | [ ] |
| 2 | file1.md | PROMPT NAME 2 | 871 | [ ] |
... (list ALL prompts from ALL files)
```

**Rule**: If multiple extraction files exist (pt.1, pt.2, etc.), ALL files must be audited and ALL prompts must appear in the inventory.

---

## Phase 1: Foundation Setup

1. Create skill directory structure:
   ```
   skills/[skill-name]/
   ├── SKILL.md
   ├── references/
   │   ├── genius-patterns.md
   │   └── prompts/
   └── examples/
   ```

2. Create SKILL.md with:
   - Core frameworks from extraction overview
   - Available prompts table (list ALL from inventory)
   - File structure
   - Quick start guide

3. Create genius-patterns.md with:
   - Advanced patterns
   - Hidden knowledge
   - Expert heuristics

---

## Phase 2: Prompt Conversion

**For EACH prompt in the inventory:**

1. Read the full prompt from extraction file
2. Create corresponding `.md` file in `references/prompts/`
3. Mark as `[x]` in inventory

**Quality checks per prompt:**
- [ ] Has ROLE & ACTIVATION section
- [ ] Has INPUT REQUIRED section
- [ ] Has EXECUTION PROTOCOL section
- [ ] Has OUTPUT DELIVERABLE section
- [ ] Has at least one EXAMPLE OUTPUT
- [ ] Has DEPLOYMENT TRIGGER

---

## Phase 3: Agent Creation

1. Create agent directory:
   ```
   agents/[agent-name]/
   ├── AGENT.md
   └── memory/
       └── context.md
   ```

2. AGENT.md must include:
   - Core identity and philosophy
   - Voice and communication style
   - Decision frameworks
   - Available skills table
   - Invocation triggers

---

## Phase 4: Integration

1. Add agent to GEMINI.md:
   - Add to Available Agents table
   - Add skill to Available Skills table
   - Add to relevant Task Type routing

2. Update COUNCIL.md if agent belongs to councils

---

## Phase 5: Verification

**Before marking complete:**

```bash
# Count prompts in skill
ls -1 "skills/[skill-name]/references/prompts/" | wc -l

# Compare to inventory count
# MUST MATCH
```

Create verification table in walkthrough:

```markdown
## Verification

| Source | Count |
|--------|-------|
| Extraction files | X prompts |
| Created prompts | X prompts |
| Match? | ✅ YES |
```

---

## Anti-Patterns to Avoid

❌ **Starting creation before complete audit**
→ Leads to missed prompts

❌ **Reading only first extraction file**
→ Miss pt.2, pt.3, etc.

❌ **Creating prompts without tracking**
→ Lose count, miss items

❌ **Trusting memory for prompt count**
→ Always verify with grep + ls

---

## Error Recovery

If prompts are discovered missing after initial "completion":

1. Re-run full audit
2. Add missing prompts to inventory
3. Create missing prompts
4. Update SKILL.md prompt table
5. Update agent if needed
6. Re-verify counts match
