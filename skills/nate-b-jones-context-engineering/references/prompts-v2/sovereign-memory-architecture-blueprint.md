---
name: "Nate B. Jones — Sovereign Memory Architecture Blueprint"
source_prompt: born-v2
skill: nate-b-jones-context-engineering
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are designing Nate B. Jones's sovereign memory architecture: a complete persistent memory system with episodic/semantic/procedural tiers, built-in decay, distillation pipelines, and sovereignty guarantees. The governing principle: "You should own your memory. You should decide what your memory does. Somebody else should not own it for you." This blueprint is a deployable architecture document — schema definitions, decay mechanism, distillation pipeline, retrieval interface, sovereignty checklist, and an implementation timeline — not a conceptual overview.

## Input Required

- **[CURRENT PERSISTENCE STRATEGY]** — how the system currently stores state (Knowledge Items, conversation logs, session state files, third-party memory features)
- **[DATABASE TECHNOLOGY DECISION]** — PostgreSQL + pgvector + hypertables recommended by default; note if a different stack is mandated
- **[USE CASES]** — what persistent memory should enable for this system (name them explicitly — a memory architecture designed for "everything" is designed for nothing)
- **[SOVEREIGNTY REQUIREMENTS]** — local-only storage mandate? any third-party memory services (ChatGPT memory, Claude projects) already in use that need migration or coexistence? export/audit requirements?
- **[DIAGNOSTIC INPUT]** — output of a Context Bloat Diagnostic if available, to ground the design in the system's actual pain points rather than a generic template

## Execution Protocol

**Step 1 — Memory Requirements Discovery.** Establish, explicitly, before designing anything:
- What memories matter: expert routing preferences learned over time, task patterns (which workflows used most, in what order), user preferences (voice, formatting, communication style), error patterns (what went wrong and how it was fixed), cross-conversation insights.
- Access pattern: recall frequency (per task/session/week), current storage method, retrieval latency tolerance, accumulation rate.
- Sovereignty requirement: must all memory be local? any third-party memory services in use? export/migration requirements? audit trail requirements?

**Step 2 — Design the Three-Tier Memory Store.**
- Tier 1, Episodic (raw interactions): ground-truth record of all interactions. Time-series optimized storage (hypertable). Fields: id, timestamp, session_id, actor (user/agent/system), content_type (message/tool_call/tool_result/decision/error), content (jsonb), metadata (jsonb: expert, skill, workflow, tokens_used). Retention: 90 days full resolution → distill → archive. Index on timestamp, session_id, content_type.
- Tier 2, Semantic (distilled knowledge): patterns, rules, insights extracted from episodic memory. Vector-indexed storage. Fields: id, created_at, last_accessed, access_count, freshness_score (float 0.0-10.0), category (preference/pattern/rule/insight/error_pattern), content, embedding, source_episodes (references to episodic IDs), metadata (expert, domain, confidence). Retention: indefinite, subject to decay. Index on embedding (ivfflat), category, freshness_score.
- Tier 3, Procedural (operational knowledge): configurations, successful workflow sequences, system preferences. Structured JSON storage. Fields: id, key (unique, namespaced — e.g. "agent.nate.preferred_workflow"), value (jsonb), version, timestamps, source (manual/distilled/imported). Retention: indefinite, versioned. Index on key, version.

**Step 3 — Design the Decay Mechanism.** The Ebbinghaus Memory Ledger (Nick Saraev contribution): `freshness = base_value × (1 / (1 + k × days_since_last_access))`, where base_value is the initial importance score (1-10) and k is the decay rate constant (default 0.1). Accessing a memory resets its decay clock (reinforcement). Thresholds: ACTIVE ≥3.0 (actively served in context retrieval), DORMANT 1.0-3.0 (served only on direct query), ARCHIVE <0.3 (flagged for review/archival), COLD <0.1 (moved to cold storage, never deleted). Decay schedule: nightly calculation, alert when high-value memories approach DORMANT, monthly review of ARCHIVE-threshold memories, quarterly purge of COLD storage to external backup. Override mechanisms: `pin(memory_id)` freezes decay; `boost(memory_id, amount)` adds to freshness; `demote(memory_id)` manually pushes toward archival.

**Step 4 — Design the Distillation Pipeline.**
- Episodic → Semantic (weekly cron): query last 7 days of episodic entries grouped by content_type; detect patterns (repeated decisions → proposed rule, repeated tool sequences → proposed workflow, repeated errors → proposed error pattern, repeated preferences → proposed preference); generate candidate semantic entries; human review gate (approve/reject/modify) — never auto-write without review; write approved entries with initial freshness_score 7.0, generated embedding, linked source_episodes.
- Semantic → Procedural (monthly): query semantic entries with access_count ≥10 in last 30 days; if the entry describes a configuration/workflow pattern, propose promotion; human review gate; write to procedural tier as key-value configuration.

**Step 5 — Design the Retrieval Interface.** On agent invocation: extract task intent → embed it → query semantic memory for top-5 by cosine similarity → query procedural memory for relevant configurations tied to the active expert → inject with source attribution in the format `[Semantic] [date] <content> (freshness: N)` / `[Procedural] key = value`.

**Step 6 — Sovereignty Verification Checklist.** Confirm: all memory stored on controlled infrastructure (local/own cloud); no memory stored exclusively in third-party platform memory features; export path exists for all tiers as JSON/CSV; migration path validated (data moves to different infra without loss); every memory has creation timestamp and source reference; any memory can be permanently purged on demand; sensitive memories encrypted at rest; access control limits query to authorized agents/users.

**Step 7 — Implementation Sequence.** Week 1: stand up the database + schemas for all three tiers. Week 2: build ingestion pipeline (episodic), start recording. Week 3: build retrieval interface, test semantic search against episodic data. Week 4: implement distillation pipeline (episodic→semantic), first manual run. Month 2: build decay mechanism, run first decay cycle, implement procedural tier. Month 3: integrate into context loading pipeline, A/B test against static loading.

**Step 8 — Adoption Layer (Human Economics, not just token economics).** A sovereign memory store that its human stops feeding is dead infrastructure — design for the human side too:
- One Reliable Behavior: capture reduces to a single behavior with zero decisions at capture time. Systems die at the taxonomy moment — if capture requires the human to classify/file/choose a category, friction wins. Keep categories painfully small; let AI classification sort AFTER capture, not before.
- Loop vs. Storage: name the surfacing mechanism and cadence for every tier. If retrieval only happens when the human remembers to search, it's storage wearing a loop costume — add proactive surfacing (digest, pre-task context push).
- Trust Mechanisms: ship the trust triad — confidence score per classification (with a threshold routing low-confidence items to human review), an audit trail per item (what got filed where, why), and a one-tap fix affordance. Every correction is training signal.
- The Restart Protocol: define what happens to the backlog after a lapse (auto-archive or summarize-and-clear — never demand manual triage) and what the first 5-minute re-engagement action is. Time-to-resume after a lapse should be minutes, not a rebuild event.

## Output Contract

Deliver a comprehensive architecture document with:
1. Three-tier schema definitions (full field lists for episodic, semantic, procedural)
2. Decay mechanism specification (formula, thresholds, schedule, overrides)
3. Distillation pipeline design (both directions, with human review gates marked explicitly)
4. Retrieval interface specification (query flow, injection format)
5. Sovereignty checklist — completed (each item marked with actual status for the target system, not left as a template)
6. Adoption layer design (capture behavior, surfacing cadence, trust triad, restart protocol)
7. Implementation timeline with milestones
8. Technology stack decisions with rationale (why this database, why this decay constant, etc.)

## Output Skeleton

```
# Sovereign Memory Architecture Blueprint — [TARGET SYSTEM]

## Requirements Discovery
What memories matter: [list]
Access pattern: [frequency, latency tolerance]
Sovereignty requirement: [local-only? third-party in use? export/audit needs?]

## Three-Tier Schema
### Tier 1 — Episodic
[full field list, storage tech, retention, index]
### Tier 2 — Semantic
[full field list, storage tech, retention, index]
### Tier 3 — Procedural
[full field list, storage tech, retention, index]

## Decay Mechanism
Formula: freshness = base_value x (1 / (1 + k x days_since_last_access))
k = [value] | Thresholds: ACTIVE [n] / DORMANT [n] / ARCHIVE [n] / COLD [n]
Schedule: [cadence] | Overrides: pin / boost / demote

## Distillation Pipeline
Episodic → Semantic: [cadence, detection rules, review gate]
Semantic → Procedural: [cadence, promotion criteria, review gate]

## Retrieval Interface
Flow: [task intent → embed → query → inject]
Injection format: [example format string]

## Sovereignty Checklist
- [ ] Local/controlled infrastructure: [status]
- [ ] No exclusive third-party storage: [status]
- [ ] Export path (JSON/CSV) for all tiers: [status]
- [ ] Migration path validated: [status]
- [ ] Audit trail on every memory: [status]
- [ ] Delete/purge on demand: [status]
- [ ] Encryption at rest: [status]
- [ ] Access control: [status]

## Adoption Layer
Capture behavior: [single reliable action, zero decisions at capture]
Surfacing mechanism + cadence: [per tier]
Trust triad: [confidence score threshold / audit trail / fix affordance]
Restart protocol: [backlog handling after lapse, first re-engagement action]

## Implementation Timeline
Week 1: [ ] | Week 2: [ ] | Week 3: [ ] | Week 4: [ ] | Month 2: [ ] | Month 3: [ ]

## Technology Stack Decisions
[decision]: [rationale]
```

## Quality Gate

- [ ] All three tier schemas are fully specified (fields, storage tech, retention, index) — no tier left as a placeholder
- [ ] The decay formula and thresholds are stated exactly as specified, with the k-value and threshold numbers filled in for this system, not left generic
- [ ] Every distillation direction has an explicit human review gate — no auto-write from episodic to semantic or semantic to procedural
- [ ] Sovereignty checklist items are marked with actual status for the target system (met/not met/in progress), not left unchecked as a template
- [ ] Adoption layer section is present and specific — a memory architecture without a capture/surfacing/trust design is incomplete per this methodology

## Deploy When

- Moving from static file/session-state persistence to a real persistent memory system
- Third-party memory features (ChatGPT memory, Claude projects) are creating a sovereignty gap that needs a migration plan
- A Context Bloat Diagnostic has identified conversation-history bloat that a tiered, decaying memory store would resolve
- The system needs cross-conversation learning (routing preferences, error patterns) that currently resets every session
