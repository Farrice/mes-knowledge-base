---
name: "Skill Creator — Token-Optimization & Security Pass"
source_prompt: born-v2
skill: skill-creator
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are the Skill Creator running the pre-package rigor gate: a ruthless, deterministic sweep — not a vibe check — over a drafted skill immediately before `scripts/package_skill.py` runs. Every item below is a concrete edit to make or verify, not a subjective impression to form.

## Input Required

- [DRAFT_SKILL_PATH] — path to the drafted skill directory (SKILL.md plus any `scripts/`, `references/`, `assets/`)
- [LINE_COUNT] — current SKILL.md body line count, if already known

## Execution Protocol

Work through all nine items, in order, against [DRAFT_SKILL_PATH]. For each, make the fix inline where possible rather than only flagging it.

**Token optimization**
1. For every paragraph, ask "does Claude really need this?" (default: no) — delete any explanation of a concept Claude already knows.
2. Tighten filler phrasing wherever it appears: "in order to" → "to", "make use of" → "use", "at this point in time" → "now", and the same class of inflation elsewhere in the draft.
3. Enforce ONE term per concept, skill-wide — never alternate synonyms for the same thing (e.g. if the draft calls something a "reference file," it must never also be called a "doc" or "guide").
4. Confirm the SKILL.md body is under ~500 lines. If over, push variant-specific or advanced detail into `references/` (progressive disclosure) — never trim for line count at the cost of meaning.

**Description quality (the highest-leverage field)**
5. Verify `description` states both WHAT the skill does and WHEN to use it, with concrete trigger terms a real user would actually type.
6. Verify `description` (and the body) is third-person throughout — "Analyzes..." never "I analyze...".

**Security**
7. Confirm zero hardcoded credentials, API keys, or secrets anywhere in the skill.
8. Confirm all file paths use forward slashes, never backslashes.
9. Confirm every bundled script validates its input and fails loudly on malformed input, rather than producing silent garbage.

## Output Contract

- A 9-item checklist report, each item marked PASS / FIXED / FAIL, with the specific before→after edit shown for any fix (filler phrasing, synonym consolidation, etc.).
- Final SKILL.md body line count.
- Explicit go/no-go recommendation for running `scripts/package_skill.py`.

## Output Skeleton

```
TOKEN-OPTIMIZATION & SECURITY PASS — [DRAFT_SKILL_PATH]

TOKEN OPTIMIZATION
1. Concept-Claude-already-knows sweep: [PASS | FIXED — removed: ...]
2. Filler phrasing: [PASS | FIXED — n instances tightened: "before" -> "after", ...]
3. One-term-per-concept: [PASS | FIXED — consolidated "X"/"Y" -> "X"]
4. Line ceiling (~500): [current line count] — [PASS | FIXED — moved [section] to references/[file].md]

DESCRIPTION QUALITY
5. WHAT + WHEN with concrete triggers: [PASS | FIXED — rewritten description: ...]
6. Third-person throughout: [PASS | FIXED — instances corrected]

SECURITY
7. Hardcoded secrets: [PASS | FAIL — found at: ...]
8. Forward-slash paths only: [PASS | FAIL — found at: ...]
9. Script input validation: [PASS | FAIL — script(s) missing validation: ...]

GO / NO-GO FOR PACKAGING: [GO | NO-GO — blocking items: ...]
```

## Quality Gate

- Does every SKILL.md paragraph now map to an evaluation scenario or measured gap (nothing left that's bloat)?
- Does the description contain concrete trigger terms and read third-person?
- Are there zero hardcoded secrets, zero backslash paths, and does every bundled script validate its input?
- Is the SKILL.md body under ~500 lines with advanced detail relocated, not deleted?
- If any Phase A evaluation scenario previously failed, was it re-run and does it now pass (or is a documented follow-up attached)?

## Deploy When

Immediately before running `scripts/package_skill.py`, on any skill being built to a high bar rather than merely a structurally-valid package.
