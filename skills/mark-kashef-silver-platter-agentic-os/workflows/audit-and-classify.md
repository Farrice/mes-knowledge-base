---
name: "Silver Platter — Audit and Archetype Classification"
produces: "Working-Directory Audit Findings + Business Archetype Classification"
expert: "Mark Kashef Silver Platter Agentic OS"
load_context: "genius.md"
---

# Mark Kashef Silver Platter — Audit and Archetype Classification

## Role
You are running Component Order steps 1-3 of the Silver Platter method: audit the current folder for existing Claude/Codex surfaces, classify the business archetype from `references/archetypes.md`, and build the short list of interview questions that local files and defaults cannot already answer. This is the audit-first move Kashef names at transcript `00:09:22` ("the `/silver-platter` skill auditing existing infrastructure before asking questions") — never open with a question the filesystem has already answered.

**Before executing**: read `genius.md` § Pattern 3 (Hire Agents Like a Bootstrapped Company Hires Employees) and § Anti-Patterns for the cold-start and schema-question failure modes.

## Input Required
- **Working directory path** to scan.
- **Operator-stated business description**, in their own words.
- **Archetype hint**, if the operator named one (`ecommerce`, `saas`, `professional_services`, `healthcare_clinic`, `wealth_advisory`, `content_creator`, `restaurant_multilocation`, `real_estate_brokerage`, `local_trades`) — else infer.

## Workflow

1. Run `python3 skills/mark-kashef-silver-platter-agentic-os/scripts/audit_existing_folder.py [path]`. Read its findings before anything else.
2. Determine trigger: any of `.claude/CLAUDE.md`, `.claude/settings.json`, `.claude/skills/*`, `.claude/agents/*`, `.claude/rules/*`, `data/` with subfolders, `silver_platters/*`, `outputs/audit_log.md`, `data/raw_dropzone/`, `data/converted/` present shifts the run into audit-existing mode (see `references/prompts-v2/existing-setup-audit.md` for the full branch logic, including the partial-setup, borrowed-setup, and demo-folder edge cases).
3. Acknowledge findings in plain English before asking anything — name specific skill names, rule names, platter filenames with dates, audit-log line counts.
4. Classify the archetype against `references/archetypes.md`. Regulated archetypes (`healthcare_clinic`, `wealth_advisory`, `professional_services` handling matter data) are flagged here, before any recommendation touches automation.
5. Build the `skip_questions` list: every detected component removes its corresponding interview question. Only unresolved facts route to `references/question_library.md`.

## Output Schema
```
audit_findings:
  existing_surfaces: [ {path, type, detail} ]     # e.g. .claude/skills/cfo-bot, "skill", "handles monthly P&L"
  mode: greenfield | audit-existing
archetype:
  name: <one of the 9 archetypes, or "unclassified — infer from description">
  regulated: true | false
  confidence: high | medium | low
skip_questions: [ <interview question text, with the finding that answered it> ]
remaining_questions: [ <question text from references/question_library.md> ]
```

## Quality Gate
1. Every acknowledged finding names a real path or filename — never "I see you have some setup already."
2. No question in `remaining_questions` duplicates something the audit already answered.
3. Regulated archetypes are flagged at this stage, not discovered later during build-plan assembly.
4. Borrowed-setup and demo-folder edge cases are checked explicitly, not skipped for speed.

> **🛡️ Anti-Pattern Check**: Before handing off to data-map assembly, confirm against `genius.md` § Anti-Patterns — specifically the cold-start/agent-overlap failure and the "hire agents for the sake of having agents" failure.
