# Notion Database Registry

These are Farrice's structured Notion databases. Use `execution/notion_api.py`
with `NOTION_API_KEY` from `.env` to read/write to them. Do not use the JS
Notion client; the project wrapper pins the API version that preserves database
property behavior.

## Databases

| Database | ID | Purpose |
|---|---|---|
| **Projects** | `cf93599a-a201-4e55-a6b9-f2f58ae6fd77` | Active work with status, type, priority, next actions |
| **Knowledge Vault** | `5c63b25c-e040-4c6f-8a7b-906643090694` | MES 3.0 extractions, research briefs, frameworks, patterns |
| **Content Pipeline** | `ff77ee45-8ee8-4fce-996e-20c76fa65d9c` | Content from idea → draft → published with platform targeting |
| **Captures** | `f55d202d-233c-4284-a8f1-7ab1c145ffe1` | Quick captures from Telegram, voice, manual entry |
| **Farrice Cain — Personal Context** | `0911ef04-8117-463f-8b21-e7f6c1a1ef4a` | Personal insights, worldview, identity, journal extractions |
| **Performance Log** | `31f49875-a897-81db-b599-dee5e7961b5c` | Autoresearch feedback ratchet — quality signals per output for self-improvement |

## API Access

```bash
python3 execution/notion_api.py query knowledge --limit 5
python3 execution/notion_api.py vault-create "Title" --expert X --domain Y --type "Research Brief"
python3 execution/notion_api.py status
python3 execution/log_performance.py sync-pending --dry-run
```

The Notion API key and database aliases are stored in the Antigravity root
`.env`. `execution/notion_api.py` also keeps safe default aliases for the
registry IDs above so named lookups continue working if an env alias is absent.

## Codex Boundary

Use the project wrapper for deterministic Antigravity reads and writes:

- performance logging
- Knowledge Vault pointers
- database schema checks
- local-first sync/backfill
- command and workflow execution

Use the Codex Notion connector for inspection, schema discovery, and manual
workspace work when the user asks for Notion directly. Do not use it as the
hidden execution path for Antigravity logging unless the wrapper is unavailable
and the user approves that fallback.

Do not add a Notion MCP server to `.codex/config.toml` by default. The current
default is local-first files plus the pinned wrapper, with Notion as an optional
metadata/search mirror.

When sandbox DNS blocks `api.notion.com`, treat local JSONL and the local wiki
as the source of truth. Run `python3 execution/notion_api.py status` to confirm
whether the failure is DNS/network, a missing key, or a real API/schema issue.

## Key Properties Per Database

### Projects
- Name (title), Status (Active/Planning/On Hold/Completed/Archived), Type (Product/Content/Client Work/System/Research/Personal), Priority (P0-P3), Next Action, Description, Started, Tags

### Knowledge Vault
- Name (title), Source, Expert, Domain, Type (MES 3.0 Extraction/Research Brief/Framework/Case Study/Pattern Library/Book Notes), Key Patterns, Genius Score (2-5), Date Extracted, Antigravity Skill, Tags (Crown Jewel/Hidden Knowledge/Actionable/Reference)

### Content Pipeline
- Name (title), Stage (Raw Idea → Flywheel Processing → Draft → Review → Ready to Publish → Published), Platform (multi), Content Type, Hook, Core Idea, Expert Framework Used, Publish Date, Performance, Tags

### Captures
- Name (title), Type (Idea/Task/Note/Observation/Question/Voice Memo/Reference), Source (Telegram/Claude Code/Manual), Processed (checkbox), Raw Content, Captured At, Tags

### Farrice Cain — Personal Context
- Name (title), Category (Identity/Worldview/Values/Strengths/Growth Edge/Life Experience/Fatherhood/Creative Vision/Business Philosophy/Health/Emotional Pattern/Decision), Depth (Surface/Medium/Deep/Foundational), Source (Journal/Flywheel/Conversation/Telegram/AI Extraction/Life Event/Manual), Confidence (Certain/Strong/Evolving/Questioning), Emotion (multi), Raw Entry, Extracted Insight, Connected To, Date, Tags (Manifesto Material/Origin Story/Recurring Theme/Contradiction/Evolution Marker/Content Seed/Dad Life)

### Performance Log
- Output (title), Date, Agent (text), Skill (text), Workflow (text), Task Type (Content/Strategy/Extraction/Research/Client Work/System/Creative/Analysis), Quality Score (number 1-10), User Rating (number 1-10), Intent Alignment (number 1-10), Expert Standard (number 1-10), Adversarial Resilience (number 1-10), Status (Keep/Discard/Needs Improvement/Baseline), Notes, Experiment Tag
- Script: `execution/log_performance.py`
- Protocol: `directives/feedback-ratchet.md`

## Usage Patterns

**From Telegram bridge:** When the user captures something, classify it and push to the right database. Quick thoughts → Captures. Journal reflections → Personal Context. Content ideas → Content Pipeline.

**After extractions:** Every MES 3.0 extraction should create a Knowledge Vault entry with the source, expert, key patterns, and link to the Antigravity skill path.

**Project tracking:** When starting or completing significant work, update the Projects database with status and next actions.

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-04-13 (Karpathy Wiki deployment — Knowledge Vault auto-sync) |
| **Activation Count** | 1 |
| **30-Day Review Date** | 2026-05-13 |

**Update Rule**: When this protocol fires (database ID referenced), update the date and increment count.

## Karpathy Wiki Integration (2026-04-13)

- **Knowledge Vault auto-sync**: `chain_runner.py finalize` creates entries for quality >= 7 outputs
- **CLI**: `python3 execution/notion_api.py vault-create "Title" --expert X --domain Y --type "Research Brief"`
- **Autofill config**: See `directives/notion-autofill-guide.md` for AI autofill + Custom Agents
- **Architecture**: Notion = pointer + metadata layer. Files stay local (knowledge/, extractions/). Notion enables discoverability via search/AI Q&A.
- **Codex default**: The local wiki (`knowledge/`, `knowledge/index.md`, `knowledge/log.md`, `knowledge/compiled/`) remains the execution memory. Notion mirrors high-value metadata when network access is available.
