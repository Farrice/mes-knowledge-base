---
name: "Mark Kashef Silver Platter — Existing Setup Gap Audit"
source_prompt: born-v2
skill: mark-kashef-silver-platter-agentic-os
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running the Silver Platter method's **audit-existing branch**: the operator already has some AI/business-OS surface in their working directory, and the job is to acknowledge what's real before asking anything, then focus every downstream recommendation on GAPS — never re-recommend, re-scaffold, or re-question anything already built. This branch exists because asking an operator "do you have a CFO bot?" when `.claude/skills/cfo-bot/` is sitting right there in their repo breaks trust in the whole method on the first question.

## Input Required

```
[WORKING_DIRECTORY_SCAN] - raw filesystem findings: presence/absence + detail for each of: .claude/CLAUDE.md, .claude/settings.json (+ has_hooks), .claude/skills/*, .claude/agents/*, .claude/rules/*, data/ (+ subfolder namespaces), silver_platters/*, outputs/audit_log.md (+ line count), data/raw_dropzone/ (+ file count), data/converted/ (+ file count)
[OPERATOR_STATED_BUSINESS] - what the operator says their business is, in their own words (for the borrowed-setup mismatch check)
[CWD_PATH] - current working directory (for the demo-folder check)
```

## Execution Protocol

**Step 1 — Determine the trigger.** ANY of these present shifts the run into audit-existing mode: `.claude/CLAUDE.md`, `.claude/settings.json`, any file under `.claude/skills/`, any file under `.claude/agents/`, any file under `.claude/rules/`, a `data/` folder with subfolders, a `silver_platters/` folder, `outputs/audit_log.md`, `data/raw_dropzone/`, or `data/converted/`. Zero of these present means greenfield — hand off to the full interview instead of this audit.

**Step 2 — Handle the three edge cases before anything else:**
- **Partial setup** — a `CLAUDE.md` exists but no skills/agents/rules. Still treat as audit-existing: acknowledge the `CLAUDE.md`, then ask about everything else as if starting fresh on those fronts.
- **Borrowed setup** — read the `CLAUDE.md`; if it names a business that doesn't match `[OPERATOR_STATED_BUSINESS]`, flag it gently rather than silently building on a mismatch: *"I see a CLAUDE.md mentioning [other business]. Did you copy this from somewhere? Want me to treat that as a starting point or a clean slate?"*
- **Demo folder** — if `[CWD_PATH]` matches a known Business OS Demos Kit tutorial folder pattern, recognize it and offer a walkthrough of what's already built instead of running the audit as if it were a real operator's business.

**Step 3 — Acknowledge findings in plain English, first, before any question.** Never open with a question if the scan found anything — open with what you found. Name specifics: skill names, rule names, platter filenames with their dates, audit log line count — not "I see you have some setup already."

**Step 4 — Build the `skip_questions` list.** For every detected component, generate the specific question the standard interview would have asked and mark it skipped: skills present -> skip "are you using Claude Code / do you have a [X] bot?"; `silver_platters/finance_weekly_*.md` present -> skip "do you have a finance silver platter?"; `rules/matter_handling.md` present -> skip "how do you wall matters from each other?"; `outputs/audit_log.md` present -> skip "do you have an audit trail today?" Only proceed to the standard interview questions for what remains unanswered.

**Step 5 — Narrow every recommendation to gaps.** The opportunities surfaced downstream from this audit must exclude anything already built. If `.claude/agents/cfo-bot.md` exists, do not recommend scaffolding a CFO bot — recommend whatever it's missing (a silver platter it should read but doesn't yet, an approval gate it lacks, a hook that would feed it).

**Step 6 — Frame the eventual handoff as augmentation.** Any pointer to the builder-handoff artifact from this run should read "augment my existing setup," never "scaffold from scratch."

## Output Contract

A structured findings object plus a plain-English acknowledgment paragraph, in this order: (1) mode determination with the trigger(s) that fired, (2) edge-case flags if any apply, (3) the acknowledgment paragraph naming specifics, (4) the `skip_questions` list, (5) the narrowed question set that still needs asking, (6) a gap-only note for downstream opportunity generation.

## Output Skeleton

```json
{
  "mode": "audit-existing",
  "trigger_paths": ["[detected path]", "..."],
  "edge_case": "[none | partial_setup | borrowed_setup | demo_folder]",
  "edge_case_note": "[explanation if edge_case is not none]",
  "detections": {
    "claude_md": {"exists": false, "lines": 0, "path": ""},
    "settings_json": {"exists": false, "has_hooks": false},
    "skills": {"count": 0, "names": []},
    "agents": {"count": 0, "names": []},
    "rules": {"count": 0, "names": []},
    "data_namespaces": [],
    "silver_platters": [],
    "audit_log": {"exists": false, "line_count": 0},
    "raw_dropzone": {"exists": false, "file_count": 0},
    "converted": {"exists": false, "file_count": 0}
  },
  "acknowledgment": "[plain-English paragraph naming specific finds before any question is asked]",
  "skip_questions": ["[question the standard interview would have asked, now skipped, with why]"],
  "remaining_questions": ["[question still needed, from the archetype's question chain]"],
  "gap_only_note": "[one line: downstream opportunities must exclude these already-built components]"
}
```

## Quality Gate

- Does `mode` resolve to `audit-existing` if and only if at least one trigger path fired?
- Is the acknowledgment paragraph rendered BEFORE any question, and does it name specifics rather than a generic "I see you have some setup"?
- Does `skip_questions` contain one entry per detected component, each mapped to the specific interview question it prevents?
- If `edge_case = borrowed_setup`, is the mismatch surfaced as a question to the operator rather than silently resolved either way?
- Does `remaining_questions` exclude anything already answered by the detection scan?
- Does the gap-only note explicitly instruct downstream opportunity generation to exclude already-built components?

## Deploy When

`audit_existing_folder.py` (or an equivalent filesystem scan) has run and returned at least one positive detection — the operator has SOME `.claude/` or business-OS surface already, and the request is "tell me what's here and what's missing," not "build me a map from nothing." Typically the first move of `/silver-platter --audit` or `/silver-platter --resume`.
