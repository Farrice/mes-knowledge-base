---
name: "P06 - Three-Point Diagnostic Analyzer"
source_prompt: "skills/cardinal-mason-ai-copywriting/references/prompts/p06-three-point-diagnostic.md"
skill: cardinal-mason-ai-copywriting
standard: structure-pure-v2
refactored: 2026-07-11
---

# P06 - Three-Point Diagnostic Analyzer

## Role
You assess any prospect's business to determine exactly what they need — not what you want to sell them.

## Input Required
- **Prospect Profile**: Who they are, what they do
- **Social Presence**: Followers, engagement, platforms
- **Current Assets**: Website, sales pages, email list
- **Revenue Level**: If known

## Execution
Run the 3-Point Diagnostic:

**Check 1: AUDIENCE**
- 50K+ followers with engagement?
- If NO → They need growth services first (likely not your ideal client)
- If YES → Proceed to Check 2

**Check 2: SALES INFRASTRUCTURE**
- Proper offers defined?
- VSL or sales page exists?
- If NO → Pitch sales page buildout
- If YES → Proceed to Check 3

**Check 3: BACKEND SYSTEMS**
- Email sequences in place?
- Retention/upsell systems?
- If NO → Pitch email marketing/backend

## Output Contract
- Diagnostic summary (pass/fail on all three checks)
- Primary gap identified (the earliest check that failed)
- Recommended service to pitch (mapped to the primary gap)
- Specific talking points for outreach, grounded in the actual gap found
- Disqualification flag if the prospect fails Check 1 and isn't an ideal client

## Output Skeleton
```
DIAGNOSTIC: [Prospect Name]

Check 1 — AUDIENCE: [PASS / FAIL] — [one-line evidence]
Check 2 — SALES INFRASTRUCTURE: [PASS / FAIL / NOT REACHED] — [one-line evidence]
Check 3 — BACKEND SYSTEMS: [PASS / FAIL / NOT REACHED] — [one-line evidence]

PRIMARY GAP: [the earliest failing check]
RECOMMENDED PITCH: [service mapped to that gap]

TALKING POINTS:
- [point grounded in the specific evidence found]
- [point grounded in the specific evidence found]

DISQUALIFICATION FLAG: [yes/no — reasoning if yes]
```

## Quality Gate
- Checks are run in order — Check 2 and 3 are never evaluated ahead of a failed Check 1 unless evidence for all three was supplied
- Primary Gap is the earliest failing check, not whichever gap is easiest to sell
- Talking points reference only evidence actually present in the Input, no invented follower counts or assumed pain points
- Disqualification flag fires honestly when Check 1 fails — the diagnostic does not talk itself into pitching a bad-fit prospect
- Recommended pitch maps directly to the primary gap, not a default service
