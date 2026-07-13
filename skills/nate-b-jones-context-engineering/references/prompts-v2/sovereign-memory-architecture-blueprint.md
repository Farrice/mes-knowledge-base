---
name: "Nate B. Jones — Sovereign Memory Architecture Blueprint"
source_prompt: born-v2
skill: nate-b-jones-context-engineering
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are designing Nate B. Jones's Sovereign Memory Architecture: a complete persistent memory system with episodic, semantic, and procedural tiers, built-in decay, a distillation pipeline, and sovereignty guarantees. "You should own your memory. You should decide what your memory does. Somebody else should not own it for you." The output is a deployable architecture document, not a philosophical treatment — every section produces a schema, a mechanism spec, or a checklist that a team could build against.

## Input Required

- **[TARGET SYSTEM]** — the agentic system that needs persistent memory (current data persistence strategy: Knowledge Items, conversation logs, session state files, or none)
- **[USE CASES]** — what persistent memory should enable for this system (routing preferences, task patterns, user preferences, error patterns, cross-conversation insights — confirm which apply)
- **[DATABASE DECISION]** — database technology if already decided; default recommendation is PostgreSQL + pgvector + hypertables
- **[SOVEREIGNTY CONSTRAINTS]** — any hard requirements (must be local-only, no third-party memory services, specific export/audit obligations)

## Execution Protocol

Run all seven steps in order. Step 3 (decay) and Step 6 (sovereignty) are non-negotiable — a memory system without a decay mechanism becomes bloat, and one without sovereignty guarantees is not actually sovereign regardless of what else it does well.

**Step 1 — Memory Requirements Discovery.** Interview the system or user to establish three things:
- *What memories matter*: expert routing preferences learned over time, task patterns (which workflows get used most, in what order), user preferences (voice, formatting, communication style), error patterns (what went wrong before and how it was fixed), cross-conversation insights (patterns spanning multiple sessions). Confirm which of these apply to [TARGET SYSTEM] — do not assume all five.
- *What's the access pattern*: how often memories are recalled (per task / per session / per week), how memory is currently stored (files / databases / in-context), current retrieval latency tolerance, expected accumulation rate per day/week/month.
- *What's the sovereignty requirement*: must all memory be stored locally, are any third-party memory services already in use, what export/migration requirements exist, what audit trail is required.

**Step 2 — Design the Three-Tier Memory Store.** Specify schemas for all three tiers:
- *Tier 1 — Episodic Memory* (raw interactions): ground truth record of all interactions. Time-series optimized storage (hypertable). Fields: id, timestamp, session_id, actor (user/agent/system), content_type (message/tool_call/tool_result/decision/error), content (jsonb), metadata (jsonb — expert, skill, workflow, tokens_used). Retention: 90 days at full resolution, then distill, then archive. Indexed on timestamp, session_id, content_type.
- *Tier 2 — Semantic Memory* (distilled knowledge): patterns, rules, and insights extracted from episodic memory. Vector-indexed storage (pgvector). Fields: id, created_at, last_accessed, access_count, freshness_score (float, 0.0-10.0), category (preference/pattern/rule/insight/error_pattern), content, embedding, source_episodes (references to episodic IDs), metadata (expert, domain, confidence). Retention: indefinite, subject to decay. Indexed on embedding (ivfflat), category, freshness_score.
- *Tier 3 — Procedural Memory* (operational knowledge): configurations, successful workflow sequences, system preferences. Structured JSON storage. Fields: id, key (unique, namespaced e.g. "agent.nate.preferred_workflow"), value (jsonb), version, created_at, updated_at, source (manual/distilled/imported). Retention: indefinite, versioned. Indexed on key, version.

**Step 3 — Design the Decay Mechanism.** Specify the Ebbinghaus Memory Ledger (Nick Saraev contribution):
```
freshness = base_value * (1 / (1 + k * days_since_last_access))
```
Where `base_value` = initial importance score (1-10), `k` = decay rate constant (default 0.1), `days_since_last_access` = time since last retrieval or reinforcement. Accessing a memory resets its decay clock.

Thresholds:
- `ACTIVE = 3.0` — above this, actively served in context retrieval
- `DORMANT = 1.0` — below ACTIVE, above DORMANT: served only on direct query
- `ARCHIVE = 0.3` — below this: flagged for review/archival
- `COLD = 0.1` — below this: moved to cold storage, not deleted

Decay schedule: run the decay calculation nightly; alert when high-value memories approach the DORMANT threshold; monthly review of memories hitting the ARCHIVE threshold; quarterly purge of COLD storage to external backup.

Override mechanisms: `pin(memory_id)` freezes decay, always active; `boost(memory_id, amount)` adds to the freshness score; `demote(memory_id)` manually pushes toward archival.

**Step 4 — Design the Distillation Pipeline.**
- *Episodic → Semantic* (weekly cron): scan episodic logs from the last 7 days, grouped by content_type. Detect patterns — repeated decisions → proposed rule, repeated tool sequences → proposed workflow, repeated errors → proposed error pattern, repeated preferences → proposed preference. Generate candidate semantic entries. Human review gate: approve/reject/modify. Write approved entries to the semantic tier with initial freshness_score 7.0, generated embedding, and linked source_episodes.
- *Semantic → Procedural* (monthly): query semantic entries with access_count ≥10 in the last 30 days. If an entry describes a configuration or workflow pattern, propose promotion to the procedural tier, formatted as key-value configuration. Human review gate, then write to procedural tier.

**Step 5 — Design the Retrieval Interface.** When an agent invocation begins: extract task intent from the user message, embed the task intent, query semantic memory for the top 5 most relevant entries by cosine similarity, query procedural memory for any configuration relevant to the active expert, inject retrieved memories into context with source attribution in this format:
```
## Relevant Memory
- [Semantic] [date] When doing X, we prefer Y because Z. (freshness: n.n)
- [Semantic] [date] Error pattern: A causes B. Fix: C. (freshness: n.n)
- [Procedural] namespace.key = "value"
```

**Step 6 — Sovereignty Verification.** Confirm each of the following for [TARGET SYSTEM] and mark pass/fail with evidence:
- All memory stored on infrastructure you control (local/own cloud)
- No memory stored exclusively in third-party platform memory features
- Export path: all tiers can be exported as JSON/CSV
- Migration path: data can move to different infrastructure without loss
- Audit trail: every memory has a creation timestamp and source reference
- Delete capability: any memory can be permanently purged on demand
- Encryption at rest for sensitive memories
- Access control: only authorized agents/users can query memory

**Step 7 — Implementation Sequence.** Default sequence from the source methodology, adapted to [TARGET SYSTEM]'s actual constraints — if the target system's timeline differs, state the adaptation and why:
- Week 1: set up PostgreSQL with pgvector extension; create schemas for all three tiers
- Week 2: build the ingestion pipeline (episodic tier); start recording interactions
- Week 3: build the retrieval interface; test semantic search against episodic data
- Week 4: implement the distillation pipeline (episodic → semantic); first manual run
- Month 2: build the decay mechanism; run the first decay cycle; implement the procedural tier
- Month 3: integrate into the context loading pipeline; A/B test against static loading

## Output Contract

Deliver a single architecture document containing, in order:
1. Memory requirements summary (what matters, access pattern, sovereignty requirement — from Step 1 discovery)
2. Three-tier schema definitions (episodic, semantic, procedural — full field lists)
3. Decay mechanism specification (formula, thresholds, schedule, override functions)
4. Distillation pipeline design (both cron jobs, human review gates)
5. Retrieval interface specification (context loading integration, injection format)
6. Sovereignty checklist, completed with pass/fail + evidence per item
7. Implementation timeline with milestones, adapted to the target system
8. Technology stack decisions with rationale
Length: as long as the architecture requires — this is a deployable spec, not a summary; do not compress schema fields for brevity.

## Output Skeleton

```
# Sovereign Memory Architecture Blueprint — [TARGET SYSTEM]

## Memory Requirements
What matters: [selected from the five categories, with rationale]
Access pattern: [recall frequency, current storage, latency tolerance, accumulation rate]
Sovereignty requirement: [local-only? third-party services in use? export/audit needs?]

## Three-Tier Schema

### Tier 1 — Episodic Memory
[full field list, storage, retention, index]

### Tier 2 — Semantic Memory
[full field list, storage, retention, index]

### Tier 3 — Procedural Memory
[full field list, storage, retention, index]

## Decay Mechanism
Formula: freshness = base_value * (1 / (1 + k * days_since_last_access))
| Threshold | Value | Meaning |
|---|---|---|
| ACTIVE | 3.0 | actively served in context retrieval |
| DORMANT | 1.0 | served only on direct query |
| ARCHIVE | 0.3 | flagged for review/archival |
| COLD | 0.1 | moved to cold storage |
Schedule: nightly decay run / monthly ARCHIVE review / quarterly COLD purge
Overrides: pin() / boost() / demote()

## Distillation Pipeline
Episodic → Semantic (weekly): [pattern detection rules, review gate, write specification]
Semantic → Procedural (monthly): [promotion criteria, review gate, write specification]

## Retrieval Interface
[context loading integration steps + injection format example]

## Sovereignty Checklist
| Requirement | Status | Evidence |
|---|---|---|
| Local/own-controlled infrastructure | | |
| No exclusive third-party memory storage | | |
| Export path (JSON/CSV, all tiers) | | |
| Migration path validated | | |
| Audit trail on every memory | | |
| Delete capability | | |
| Encryption at rest | | |
| Access control | | |

## Implementation Timeline
Week 1: [ ] | Week 2: [ ] | Week 3: [ ] | Week 4: [ ] | Month 2: [ ] | Month 3: [ ]

## Technology Stack
| Layer | Choice | Rationale |
|---|---|---|
```

## Quality Gate

- [ ] All three tier schemas include their full field list, storage type, retention policy, and index — not a partial sketch
- [ ] The decay mechanism section states the formula and all four thresholds (ACTIVE/DORMANT/ARCHIVE/COLD) exactly as specified, with the nightly/monthly/quarterly schedule and all three override functions
- [ ] Both distillation cron jobs (weekly episodic→semantic, monthly semantic→procedural) include the human review gate — no pipeline writes to a permanent tier without one
- [ ] Every sovereignty checklist item is marked pass/fail with evidence, not left blank or asserted without support
- [ ] Implementation timeline is adapted to the target system's real constraints when they differ from the default sequence, with the adaptation stated explicitly

## Deploy When

- A Context Bloat Diagnostic has identified that the system reloads full context every conversation instead of persisting state
- The target system needs to retain learned preferences, patterns, or error history across sessions rather than per-conversation
- Moving off third-party memory features (ChatGPT memory, Claude projects) toward a sovereign, portable, queryable store
- Before building any distillation or decay automation — this blueprint is the schema those pipelines need to exist first
