---
description: Audit any content for inauthenticity signals
---

# /word-audit

Detect and fix the uncanny valley in AI-generated or ghostwritten content — line-by-line authenticity map with voice-pocket rewrites.

## Execution

1. **Read skill files:**
   - `skills/kallaway-word-mastery/genius.md` — Focus on GP-WM-09 (Believability Gate) and GP-WM-10 (HTBT)
   - `skills/kallaway-word-mastery/workflows/believability-audit.md`

2. **Gather inputs:**
   - Content to audit
   - Voice reference (sample of the author's natural writing — tweets, emails, transcripts) — optional but powerful
   - Publishing context

3. **Execute the Believability Audit** end-to-end (all 6 steps)

4. **Deliver:**
   - Overall believability score [1-10]
   - Inauthenticity map (every flagged line with signal type, root cause, and rewrite)
   - Top 5 before/after comparisons
   - Rewritten content with all fixes applied
   - Voice pocket notes for future reference

## Stacks With

- `/word-sprint` (includes believability as Pass 5)
- `/voice-audit` (pair for full voice fidelity check)
- `/authenticity-audit` (broader authenticity analysis)

**Execution prompts**: before producing the deliverable, check `skills/kallaway-word-mastery/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
