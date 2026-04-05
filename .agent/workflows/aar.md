---
description: JCC After-Action Review — capture mission learnings
---

# /aar — JARVIS Command Center After-Action Review

Trigger After-Action Review — capture what worked, what didn't, expert effectiveness, and learnings from the most recent mission.

## Execution

1. Read the AAR skill at `~/.claude/plugins/installed/jarvis-command-center/skills/after-action-review/SKILL.md`
2. Generate an AAR for the most recent completed mission covering:
   - Expert ratings (1-5 effectiveness per deployed expert)
   - User redirections (how many times the user had to correct course)
   - Effective pairings (which expert combinations produced the best output)
   - Failures and root causes
3. Append the entry to `~/.claude/plugins/installed/jarvis-command-center/evolution/mission-log.md`
4. If any failures occurred, generate prevention rules for `~/.claude/plugins/installed/jarvis-command-center/evolution/failure-registry.md`
