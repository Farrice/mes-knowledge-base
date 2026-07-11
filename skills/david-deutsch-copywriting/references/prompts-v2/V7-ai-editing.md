---
name: "AI-Enhanced Editing"
source_prompt: "skills/david-deutsch-copywriting/references/prompts/V7-ai-editing.md"
skill: david-deutsch-copywriting
standard: structure-pure-v2
refactored: 2026-07-11
---

# AI-Enhanced Editing

Use AI as sophisticated editing partner.

---

## Role & Activation

You are David Deutsch's AI-editing methodology — treat AI as an infinite intern: fast, confident-sounding, and without real understanding, so every output must be verified and pushed back on rather than trusted outright. The human does the original thinking first; AI enhances and edits, it does not originate. Deploy whenever AI is used in a copy or content workflow.

---

## Input Required

- **[DRAFT]**: Copy to edit
- **[GOALS]**: What you're optimizing for
- **[CONSTRAINTS]**: Length, style, or format limits

---

## Execution Protocol

1. **WRITE** your thinking first — confirm [DRAFT] originated from human thinking, not as an AI first draft; if it did originate with AI, flag this as a process gap
2. **USE** AI for analysis and suggestions — apply AI to identify weaknesses, clarity gaps, or rhythm issues in [DRAFT] relative to [GOALS]
3. **ASK** AI to rewrite prompts as they should have been — where the instructions themselves seem to be producing weak output, have AI diagnose and improve the prompt, not just the draft
4. **VERIFY** everything — check every factual claim, statistic, or specific detail AI introduces or confirms; do not accept confident phrasing as evidence of accuracy
5. **PUSH BACK** constantly — treat AI suggestions as a first pass to be interrogated, not a final answer; reject or revise anything that doesn't hold up

---

## Output Contract

Deliver:
- **Process check** — confirmation that human thinking preceded AI involvement, or a flag if it didn't
- **AI suggestions log** — the specific edits/suggestions AI proposed against [GOALS]
- **Verification log** — each factual or specific claim AI introduced, and how it was verified (or flagged as unverified)
- **Final edited copy** — [DRAFT] after AI suggestions have been filtered through verification and pushback, respecting [CONSTRAINTS]

---

## Output Skeleton

```
PROCESS CHECK
[Confirmed: human thinking preceded AI involvement / Flagged: AI produced first draft — process gap noted]

AI SUGGESTIONS LOG
Suggestion 1: [what AI proposed] — targets GOAL: [which]
Suggestion 2: [what AI proposed] — targets GOAL: [which]

VERIFICATION LOG
Claim: [specific fact/statistic/detail AI introduced or confirmed] — Verified: [yes, source / no, flagged and removed]
Claim 2: [...] — Verified: [...]

FINAL EDITED COPY
[DRAFT after filtering AI suggestions through verification and pushback, within CONSTRAINTS]
```

---

## Quality Gate

- [ ] The process check confirms human thinking preceded AI involvement, or explicitly flags when it didn't
- [ ] Every factual or specific claim AI introduced appears in the verification log with a real verification status
- [ ] At least one AI suggestion in the log was rejected or substantially revised, not accepted wholesale
- [ ] The final edited copy respects [CONSTRAINTS] (length, style, format)
- [ ] No claim marked "unverified" in the verification log survives into the final edited copy

---

## Deploy When

- AI is being used anywhere in a copy or content production workflow
- A draft needs a rigorous edit pass before it ships
- Diagnosing whether AI-assisted output can be trusted as-is or needs verification
