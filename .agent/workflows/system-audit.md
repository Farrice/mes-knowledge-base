---
description: Run a comprehensive health audit on the Antigravity system
---

# /system-audit

Run periodic health checks to catch conflicts before they cause problems.

// turbo-all

## Quick Check (30 seconds)

```bash
# 1. Check for duplicate skills
echo "=== DUPLICATE SKILLS ===" && ls -1 skills/ | sort | uniq -d

# 2. Check for duplicate agents  
echo "=== DUPLICATE AGENTS ===" && ls -1 agents/ | grep -v _framework | sort | uniq -d

# 3. Skills missing SKILL.md
echo "=== SKILLS WITHOUT SKILL.md ===" && for d in skills/*/; do [ ! -f "$d/SKILL.md" ] && echo "$d"; done

# 4. Agents missing AGENT.md
echo "=== AGENTS WITHOUT AGENT.md ===" && for d in agents/*/; do [[ "$d" != *_framework* ]] && [ ! -f "$d/AGENT.md" ] && echo "$d"; done
```

## Registry Sync Check

```bash
# Skills in GEMINI.md skills table vs filesystem (smarter pattern)
grep -E "^\| \`[a-z0-9-]+\`" GEMINI.md | grep -oE "\`[a-z0-9-]+\`" | tr -d '`' | sort -u > /tmp/gemini_skills.txt
ls -1 skills/ | grep -v "\.skill$" | sort > /tmp/actual_skills.txt

echo "=== SKILLS IN GEMINI.md BUT MISSING FROM FILESYSTEM ===" 
comm -23 /tmp/gemini_skills.txt /tmp/actual_skills.txt

echo "=== FILESYSTEM SKILLS NOT IN GEMINI.md (may be intentional) ===" 
comm -13 /tmp/gemini_skills.txt /tmp/actual_skills.txt | head -20
```

## Agent Naming Conflicts

Look for agents with similar names that might conflict:
```bash
echo "=== POTENTIALLY CONFLICTING AGENT NAMES ===" 
ls -1 agents/ | grep -v _framework | sort | while read a; do
  base=$(echo "$a" | cut -d'-' -f1-2)
  count=$(ls -1 agents/ | grep "^$base" | wc -l)
  [ "$count" -gt 1 ] && echo "$a (shares prefix with $count others)"
done | sort -u
```

## Prompt Count Summary

```bash
echo "=== TOP 10 SKILLS BY PROMPT COUNT ==="
for skill in skills/*/; do
  count=$(ls -1 "$skill/references/prompts/" 2>/dev/null | wc -l | tr -d ' ')
  [ "$count" -gt 0 ] && echo "$count $(basename $skill)"
done | sort -rn | head -10
```

## When to Run

- **After batch conversions** (like today)
- **After major refactors**
- **Weekly maintenance**
- **When things feel "off"**

## Common Fixes

| Issue | Fix |
|-------|-----|
| Duplicate agent dirs | Merge into canonical name, delete duplicate |
| Missing SKILL.md | Create from template or delete empty skill |
| Registry mismatch | Update GEMINI.md with correct skill name |
| Conflicting names | Rename to follow `[expert-name]-[domain]` pattern |
