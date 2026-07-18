# Sovereign Memory Architecture Blueprint

> Design a complete persistent memory system with episodic/semantic/procedural tiers, built-in decay, distillation pipelines, and sovereignty guarantees. Output is a deployable architecture document.

## Prerequisites
- Context Bloat Diagnostic completed (to understand current memory pain points)
- Understanding of current data persistence strategy (KIs, conversation logs, session state)
- Decision on database technology (recommended: PostgreSQL + pgvector + hypertables)
- Clear use cases for what persistent memory should enable

## Steps

### Step 1 — Memory Requirements Discovery
Interview the system (or user) to establish:

**What memories matter?**
- Expert routing preferences learned over time
- Task patterns (which workflows get used most, in what order)
- User preferences (voice, formatting, communication style)
- Error patterns (what went wrong prior and how it was fixed)
- Cross-conversation insights (patterns that span multiple sessions)

**What's the access pattern?**
- How often are memories recalled? (per task? per session? per week?)
- How are memories currently stored? (files? databases? in-context?)
- What's the current retrieval latency tolerance?
- How much memory accumulation per day/week/month?

**What's the sovereignty requirement?**
- Must all memory be stored locally?
- Any third-party memory services in use (ChatGPT memory, Claude projects)?
- Export/migration requirements?
- Audit trail requirements?

### Step 2 — Design the Three-Tier Memory Store

**Tier 1 — Episodic Memory** (Raw Interactions)
```yaml
Purpose: Ground truth record of all interactions
Storage: Time-series optimized (hypertable)
Schema:
  - id: UUID
  - timestamp: timestamptz
  - session_id: UUID
  - actor: enum(user, agent, system)
  - content_type: enum(message, tool_call, tool_result, decision, error)
  - content: jsonb
  - metadata: jsonb (expert, skill, workflow, tokens_used)
Retention: 90 days full resolution → distill → archive
Index: timestamp, session_id, content_type
```

**Tier 2 — Semantic Memory** (Distilled Knowledge)
```yaml
Purpose: Patterns, rules, and insights extracted from episodic memory
Storage: Vector-indexed (pgvector)
Schema:
  - id: UUID
  - created_at: timestamptz
  - last_accessed: timestamptz
  - access_count: integer
  - freshness_score: float (0.0-10.0)
  - category: enum(preference, pattern, rule, insight, error_pattern)
  - content: text
  - embedding: vector(1536)
  - source_episodes: UUID[] (references to episodic IDs)
  - metadata: jsonb (expert, domain, confidence)
Retention: Indefinite, subject to decay
Index: embedding (ivfflat), category, freshness_score
```

**Tier 3 — Procedural Memory** (Operational Knowledge)
```yaml
Purpose: Configurations, workflows, and operational patterns
Storage: Structured JSON (PostgreSQL)
Schema:
  - id: UUID
  - key: text (unique, namespaced like "agent.nate.preferred_workflow")
  - value: jsonb
  - version: integer
  - created_at: timestamptz
  - updated_at: timestamptz
  - source: text (manual, distilled, imported)
Retention: Indefinite, versioned
Index: key, version
```

### Step 3 — Design the Decay Mechanism

**Ebbinghaus Memory Ledger** (adapted from Nick Saraev's contribution):

```python
def calculate_freshness(base_value, days_since_last_access, k=0.1):
    """
    Decay function: freshness drops logarithmically since last access.
    Accessing a memory resets its clock (spaced repetition reinforcement).
    """
    return base_value * (1 / (1 + k * days_since_last_access))

# Thresholds
ACTIVE = 3.0     # Above: actively served in context retrieval
DORMANT = 1.0    # Below ACTIVE, above DORMANT: served only on direct query
ARCHIVE = 0.3    # Below: flagged for review/archival
COLD = 0.1       # Below: moved to cold storage (not deleted)
```

**Decay schedule:**
- Run decay calculation nightly
- Alert when high-value memories approach DORMANT threshold
- Monthly review of memories hitting ARCHIVE threshold
- Quarterly purge of COLD storage to external backup

**Override mechanisms:**
- `pin(memory_id)` — freeze decay, always active
- `boost(memory_id, amount)` — add to freshness score
- `demote(memory_id)` — manually push toward archival

### Step 4 — Design the Distillation Pipeline

**Episodic → Semantic Distillation** (weekly cron):
```
1. Query episodic tier: last 7 days, grouped by content_type
2. Pattern detection:
   - Repeated decisions → proposed rule
   - Repeated tool sequences → proposed workflow
   - Repeated errors → proposed error pattern
   - Repeated preferences → proposed preference
3. Generate candidate semantic entries
4. Human review gate: approve / reject / modify
5. Write approved entries to semantic tier
   - Initial freshness_score: 7.0
   - Generate embedding for content
   - Link source_episodes
```

**Semantic → Procedural Promotion** (monthly):
```
1. Query semantic tier: access_count ≥ 10 in last 30 days
2. If entry describes a configuration or workflow pattern:
   - Propose promotion to procedural tier
   - Format as key-value configuration
3. Human review gate
4. Write to procedural tier
```

### Step 5 — Design the Retrieval Interface

**Context Loading Integration:**
When an agent invocation begins:
1. Extract task intent from user message
2. Embed task intent
3. Query semantic memory: top 5 most relevant memories by cosine similarity
4. Query procedural memory: any relevant configurations for the active expert
5. Inject retrieved memories into context with source attribution
6. Format:
   ```
   ## Relevant Memory
   - [Semantic] [2026-04-01] When doing X, we prefer Y because Z. (freshness: 7.2)
   - [Semantic] [2026-03-15] Error pattern: A causes B. Fix: C. (freshness: 5.1)
   - [Procedural] nate.preferred_workflow = "context-audit → compression → validate"
   ```

### Step 6 — Sovereignty Verification Checklist
- [ ] All memory stored on infrastructure you control (local/own cloud)
- [ ] No memory stored exclusively in third-party platform memory features
- [ ] Export path: all tiers can be exported as JSON/CSV
- [ ] Migration path: data can move to different infrastructure without loss
- [ ] Audit trail: every memory has creation timestamp and source reference
- [ ] Delete capability: any memory can be permanently purged on demand
- [ ] Encryption at rest: sensitive memories protected
- [ ] Access control: only authorized agents/users can query memory

### Step 7 — Implementation Sequence
1. **Week 1**: Set up PostgreSQL with pgvector extension. Create schemas for all three tiers.
2. **Week 2**: Build ingestion pipeline (episodic tier). Start recording interactions.
3. **Week 3**: Build retrieval interface. Test semantic search against episodic data.
4. **Week 4**: Implement distillation pipeline (episodic → semantic). First manual run.
5. **Month 2**: Build decay mechanism. Run first decay cycle. Implement procedural tier.
6. **Month 3**: Integration into context loading pipeline. A/B test against static loading.

## Output Schema

**Contract**: Complete persistent memory system architecture with episodic/semantic/procedural tiers, Ebbinghaus-inspired decay, distillation pipelines, retrieval integration, and sovereignty verification.

**Deliverables**:
1. Three-Tier Schema Definitions — SQL/JSON for episodic (time-series), semantic (vector-indexed), procedural (configuration) tiers with retention policies
2. Decay Mechanism Specification — Ebbinghaus function implementation (base_value × 1/(1+k×days), thresholds: ACTIVE/DORMANT/ARCHIVE/COLD), decay schedule (nightly), overrides (pin/boost/demote)
3. Distillation Pipeline Design — episodic→semantic (weekly), semantic→procedural (monthly), with human review gates
4. Retrieval Interface Specification — context-loading integration showing memory injection format and precedence rules
5. Sovereignty Checklist — completed verification of local storage, export paths, audit trails, delete capability, encryption, access control
6. Implementation Timeline — 6-month phased rollout (setup → ingestion → retrieval → distillation → decay → integration)
7. Technology Stack Decisions — database choice (PostgreSQL + pgvector recommended), rationale for hypertables, justification for versioning strategy

**Quality Gates**:
- [ ] All three tiers have explicit schemas with clear ownership and retention rules
- [ ] Decay mechanism is implemented as Python function; thresholds are calibrated to real access patterns
- [ ] Distillation pipeline includes human review gate — no automatic promotion without sign-off
- [ ] Retrieval interface is integrated into existing context-loading chain (show before/after flow)
- [ ] Sovereignty checklist is 100% complete (no placeholder items)
- [ ] Implementation timeline is realistic with clear Week 1/Month 2/Month 3 milestones
- [ ] Technology choices are justified (why PostgreSQL vs. alternatives; why pgvector vs. pinecone)

**Output Format**: Architecture document (markdown) + SQL schema file + Python pseudocode for decay/distillation + project plan (markdown).

## Output Format
Deliver as a comprehensive architecture document with:
- Three-tier schema definitions
- Decay mechanism specification
- Distillation pipeline design
- Retrieval interface specification
- Sovereignty checklist (completed)
- Implementation timeline with milestones
- Technology stack decisions with rationale
