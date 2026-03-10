# Expertise Gap Protocol — Self-Healing Knowledge Loop

> **Purpose**: Detect when no expert skill covers the current task, assess severity, and self-heal by acquiring the missing expertise — rather than silently falling back to training data.
> **Trigger**: Intent Pipeline Stage 3 (ROUTE) fails to match an expert, OR router agent finds no invocation card match.
> **Extends**: `deep_self_annealing.md` (which handles *errors*) to also handle *missing expertise*.
> **Effective**: 2026-03-04

---

## When This Fires

After Stage 3 ROUTE completes domain matching:
1. Invocation cards scanned — no relevant expert found
2. DOMAIN_REGISTRY.md swim lanes checked — no coverage for this domain
3. AGENT_INDEX.md deep-searched (fallback) — still no match

**When to skip (do NOT trigger):**
- User said "just do it" or "go ahead" — they accept training-data quality
- One-word factual questions ("What's the capital of France?")
- Existing expert is close enough (>70% domain overlap) — stretch, don't gap-fill
- Follow-up within an already-approved plan — expert was already chosen
- System/meta tasks (file management, git, debugging) — no expert needed

---

## Step 1: Gap Assessment

### 1a. Classify Severity

| Level | Signal | Default Mode |
|-------|--------|-------------|
| **Low** | One-off question, no deliverable, exploratory | Advisory |
| **Medium** | Recurring domain, part of larger project, or user seems invested | Guided |
| **High** | Deliverable being shipped, client work, reputation on the line | Guided (or Autonomous if enabled) |

### 1b. Determine What's Missing

Articulate the gap precisely:
- **Domain**: What area of expertise is needed?
- **Depth**: Surface knowledge (any generalist could answer) or deep methodology (needs a practitioner)?
- **Closest existing experts**: Who in the system is adjacent? What specifically do they lack for this task?

---

## Step 2: Execute Mode

### Advisory Mode (Low Severity — Default)

Proceed with training data, but be transparent:

```markdown
**Gap Notice**: No expert skill covers [domain]. This output is generated from
general training data, not from an extracted practitioner methodology.

Confidence: 🔴 PROJECTED (training-data only)

**To upgrade this capability**, extract from a practitioner in [domain].
Recommended search: "[suggested search terms for finding a practitioner]"
```

**Rules:**
- Always tag output with `PROJECTED` provenance (per `quality_assurance.md`)
- Never pretend training-data output is expert-grade
- Include the gap notice at the END of the output (don't block delivery)
- Log the gap (see Step 3)

### Guided Mode (Medium/High Severity)

Pause and research before proceeding:

**Phase 1 — Research practitioners** (web search):
- Search for top practitioners, authors, and course creators in the identified domain
- Prioritize sources by extractability:

| Source Type | Signal Density | Extractability |
|-------------|---------------|----------------|
| Long-form interview / podcast (30+ min) | Very High | Best — rich methodology + examples |
| YouTube tutorial / masterclass | High | Great — structured teaching |
| Book or course | High | Great — but may need manual input |
| Article / blog post (2,000+ words) | Medium | Good — if methodology-dense |
| Twitter thread / short posts | Low | Poor — opinions, not systems |

**Phase 2 — Present findings**:

```markdown
## Expertise Gap Detected

**Domain needed**: [specific domain]
**Closest existing expert**: [name] — [why they're not sufficient]

### Recommended Sources for Extraction

| # | Practitioner | Source | Why |
|---|-------------|--------|-----|
| 1 | [Name] | [YouTube/Article/Course] | [Methodology signal] |
| 2 | [Name] | [YouTube/Article/Course] | [Methodology signal] |
| 3 | [Name] | [YouTube/Article/Course] | [Methodology signal] |

**Recommended action**: Extract from #1 using `/extract`, then resume your task
with expert backing.

Options:
- **Extract now** — I'll run the full extraction pipeline (~10-15 min)
- **Proceed without** — I'll deliver from training data, tagged as PROJECTED
- **I have a source** — Paste a transcript, article, or practitioner prompt
```

**Wait for user decision.**

**Phase 3 — Execute extraction** (if approved):
- YouTube URL → `python3 execution/fetch-transcript.py "<url>" "<expert>"` → `/extract`
- Article/transcript → direct `/extract`
- Practitioner prompt → `/convert-prompt`
- After extraction completes, **resume the original task** with the new skill loaded

### Autonomous Mode (User-Enabled)

Same as Guided, but skip the user checkpoint in Phase 2:
- Auto-select the highest-ranked source
- Auto-trigger extraction
- Run quality verification on the extraction (CHECKPOINT 2 from `/extract`)
- If extraction quality is low (< 5 genius patterns or weak methodology signal), fall back to Guided mode and ask user
- Resume original task with new skill loaded

**Enable with**: `--self-heal` flag on any command, or set in session:
```
Set mode: autonomous gap healing enabled
```

**Safety rails for Autonomous mode:**
- Still logs everything (source, extraction, skill created)
- Still runs quality verification
- Falls back to Guided if extraction quality is poor
- Never extracts from paid/gated content without user approval

---

## Step 3: Post-Gap Learning

After any gap is detected (regardless of mode), log it:

### Gap Log Entry (append to `.agent/gap-log.md`)

```markdown
## [Date] — [Domain]

**Task**: [What the user was trying to do]
**Severity**: [Low/Medium/High]
**Mode**: [Advisory/Guided/Autonomous]
**Resolution**: [Proceeded with training data / Extracted from [source] / User provided prompt]
**Skill Created**: [Path to new skill, if any]
**Time to Resolve**: [Duration]
```

### Recurring Gap Detection

After logging, scan the gap log:
- **Same domain appears 3+ times** → Flag for proactive extraction: "The [domain] gap has appeared 3 times. Recommend proactive extraction to permanently close it."
- **Same domain + same severity** → Auto-upgrade severity for next occurrence

### System Updates (after successful extraction)

- New invocation card added to `agents/_framework/invocation-cards.md`
- New entry in `DOMAIN_REGISTRY.md` (appropriate swim lane)
- Run `python execution/sync_registries.py`
- Gap log entry updated with resolution

---

## Decision Flowchart

```
ROUTE fails to find expert
  ↓
Is this a skip condition? ──YES──→ Proceed normally (no gap protocol)
  │ NO
  ↓
Classify severity (Low / Medium / High)
  ├─ LOW → Advisory: deliver + tag PROJECTED + log gap
  ├─ MEDIUM → Guided: research → present → user decides → extract or proceed
  └─ HIGH → Guided/Autonomous: research → extract → resume
       ↓
     --self-heal enabled?
       ├─ YES → Auto-select source → extract → quality check
       │         ├─ Quality OK → deploy skill → resume task (GROUNDED)
       │         └─ Quality LOW → fall back to Guided (ask user)
       └─ NO → Present findings → wait for user decision
```

---

## Provenance Tags (from `quality_assurance.md`)

All output from gap-affected tasks MUST be tagged:

| Tag | Meaning | When |
|-----|---------|------|
| `GROUNDED` | Expert skill loaded, methodology applied | After successful extraction + deployment |
| `SUPPLEMENTED` | Mix of expert skill + training data | Adjacent expert stretched to cover gap |
| `PROJECTED` | Training data only, no expert backing | Advisory mode, or user chose to proceed without extraction |

---

## Integration

- **Triggered by**: `directives/intent-pipeline.md` Stage 3 (ROUTE) gap check
- **Triggered by**: `directives/router_agent.md` Level 6 (System Gap) escalation
- **Uses**: Web search tools for practitioner research
- **Calls**: `/extract` or `/convert-prompt` for skill creation
- **Logs to**: `.agent/gap-log.md`
- **Tags with**: Provenance system from `directives/quality_assurance.md`
- **Extends**: `directives/deep_self_annealing.md` (error recovery → knowledge recovery)

### Autoresearch Integration (Phase 4)

This protocol now feeds into the Intelligence Gap Detector:

- **Gap log entries** are analyzed by `execution/gap_analysis.py` for recurring patterns
- **Recurring gaps** (3+ occurrences) are surfaced in `/gap-report` as high-priority extraction candidates
- **Performance data** from resolved gaps (post-extraction quality scores) validates whether the extraction actually closed the gap
- Run `python execution/gap_analysis.py recommendations` to see gap-closing priorities
- Run `/gap-report` for a full monthly intelligence gap analysis

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-04-03 |

**Update Rule**: When this protocol fires (gap detected), update the date and increment count.

---

*Created: 2026-03-04 | Classification: Mandatory Orchestration Protocol*
*Extends: deep_self_annealing.md (errors) to cover missing expertise*
