---
title: Slash Commands — Recognizing Skill-Family Documentation
status: shipped
date: 2026-07-28
problem: "stale_slash_commands JUDGMENT reported 826 missing commands"
problem_signature: "a self-heal/verify check reports hundreds of workflows 'missing from SLASH_COMMANDS.md' and blames an unfixable generator bug — but the generator is deliberately grouping skill-family commands to keep the file small, and only the verifier's explicit-backtick scan fails to see them"
root_cause: "Architecture gap between generation and verification"
---

# Problem

`self_heal.py` reported a **JUDGMENT** finding: `stale_slash_commands` — 826 workflows missing from SLASH_COMMANDS.md with the generator unable to fix it.

The detection logic showed:
```
826 workflows missing from SLASH_COMMANDS.md, and the generator cannot fix it:
`generate_slash_commands.py --check` reports 2,398 to append but main() writes almost nothing — a generator bug
```

## Root Cause

**Not a generator bug.** The issue was an **architecture mismatch** between how commands are documented and how they're verified:

### How SLASH_COMMANDS.md Documents Commands (by design)

`generate_slash_commands.py` implements an intentional grouping strategy (Arsenal Loop, 2026-07-25) to keep file size manageable (< 350KB, per `health_metrics.py` guardrails):

1. **Skill-family commands** are grouped in the "Expert Skill Families" table with:
   - Count of commands in the family
   - Front-door command (e.g., `/luke-iha`)
   - First 3 examples with backticks (e.g., `` `/luke-ghostwrite-bridge` ``)
   - How to expand: `` `/arsenal --family luke-iha` ``

2. **Standalone commands** listed under "A–Z (844)" as bare names in letter groups

**Why this matters**: Hundreds of skill-family commands (like `/luke-iha-copy-engine-2`, `/luke-iha-cold-offer-stack`, etc.) are **implicitly documented** via the family count, not explicitly listed in backticks. This keeps SLASH_COMMANDS.md a 50KB document instead of 592KB.

### How verify_system.py Was Checking (incorrectly)

The `phase_slash_workflow_mapping` function (line 309) only looked for **explicitly backticked** command references:

```python
# Old code — only caught explicit backticks
documented_anywhere = set(re.findall(r'`/([a-z0-9][a-z0-9-]*)`', doc_text))
for wf in sorted(workflow_files - documented_anywhere):
    add(WARNING, phase, f"Workflow file `.agent/workflows/{wf}.md` is not in SLASH_COMMANDS.md")
```

This missed all skill-family commands that were only mentioned as family examples (first 3 of many), not individually listed.

---

# Solution

Updated `verify_system.py` to understand SLASH_COMMANDS.md's documentation architecture:

## 1. Added `skill_family_of()` Function

Mirrors `generate_slash_commands.py` logic — determines if a workflow command belongs to a skill family by reading its wrapper file:

```python
def skill_family_of(name: str) -> str | None:
    """Identify if a workflow command belongs to a skill family.
    
    Menu wrappers embed the full `skills/<skill>/workflows/<file>.md` path,
    so the family is read from the command's wrapper file rather than guessed
    from the command's prefix.
    """
    p = WORKFLOWS_DIR / f"{name}.md"
    if not p.exists():
        return None
    try:
        content = p.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"skills/([^/]+)/workflows/", content)
        if not m:
            return None
        skill = m.group(1)
        # Only a directory that actually exists counts as a family.
        return skill if (SKILLS_DIR / skill).is_dir() else None
    except Exception:
        return None
```

## 2. Added `extract_skill_families_from_slash_commands()` Function

Parses SLASH_COMMANDS.md's "Expert Skill Families" table to identify which families are documented:

```python
def extract_skill_families_from_slash_commands(doc_text: str) -> set[str]:
    """Extract skill family names from SLASH_COMMANDS.md.
    
    Parses the "Expert Skill Families" table to identify which skill families
    are documented. Returns a set of skill family names.
    """
    families = set()
    in_family_table = False
    for line in doc_text.splitlines():
        # Start of Expert Skill Families table
        if "Expert Skill Families" in line and "commands across" in line:
            in_family_table = True
            continue
        # End when we hit the Standalone Workflows section
        if in_family_table and line.startswith("###"):
            break
        # Extract skill names from table rows
        if in_family_table and line.startswith("|") and "**" in line:
            m = re.search(r'\*\*([a-z0-9][a-z0-9-]*)\*\*', line)
            if m:
                families.add(m.group(1))
    return families
```

## 3. Updated `phase_slash_workflow_mapping()` Logic

A workflow is now considered "documented" if:
- **Explicitly backticked** in SLASH_COMMANDS.md, OR
- **Part of a documented skill family** listed in the "Expert Skill Families" table

```python
# A workflow is "documented" if:
#   1. It's explicitly backticked in SLASH_COMMANDS.md, OR
#   2. It belongs to a skill family listed in the "Expert Skill Families" table
explicitly_documented = set(re.findall(r'`/([a-z0-9][a-z0-9-]*)`', doc_text))
documented_families = extract_skill_families_from_slash_commands(doc_text)

for wf in sorted(workflow_files):
    if wf in explicitly_documented:
        continue
    
    family = skill_family_of(wf)
    if family and family in documented_families:
        # Implicitly documented via skill family
        continue
    
    # Truly undocumented
    add(WARNING, phase, f"Workflow file `.agent/workflows/{wf}.md` not in SLASH_COMMANDS.md")
```

## 4. Fixed Prose Reference

Removed backticks from generic `/command` placeholder in SLASH_COMMANDS.md line 3 to prevent false regex matches:

```markdown
# Before
Or type the `/command` directly.

# After  
Or type a slash command directly.
```

---

# Verification

Before fix:
```
⚠️ Workflow file `.agent/workflows/{wf}.md` not in SLASH_COMMANDS.md
(reported 826 times)
```

After fix:
```
✅ ALL CLEAR — No errors or warnings found
## Phase 4: Slash Command → Workflow Mapping — ✅ Clean
```

---

# Key Insight

**Architecture principle**: When documentation changes (e.g., switching from explicit per-command entries to family-based grouping), verification logic must understand the new architecture. The generator was never broken — verify_system.py just didn't know how to read SLASH_COMMANDS.md's intentional grouping format.

This is why `arsenal.py` and `/arsenal` command serve descriptions on demand: they absorb the context cost that would otherwise bloat SLASH_COMMANDS.md to 600KB+.

---

# Files Changed

- `execution/verify_system.py`
  - Added `skill_family_of()` function
  - Added `extract_skill_families_from_slash_commands()` function
  - Updated `phase_slash_workflow_mapping()` logic to recognize skill-family documentation
  
- `SLASH_COMMANDS.md`
  - Fixed line 3 to remove backticks from generic `/command` placeholder

---

# Related

- `execution/generate_slash_commands.py` — defines family grouping strategy
- `docs/solutions/2026-07-15-concurrent-session-race-accept-repair-dedupe.md` — similar architecture-awareness issue
- `directives/arsenal-loop.md` — on-demand description serving to avoid context bloat

