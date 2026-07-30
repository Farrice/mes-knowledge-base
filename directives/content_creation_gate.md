---
status: superseded
superseded_by: directives/task-lifecycle-content.md
superseded_date: 2026-07-29
amnesty_note: >
  Rule amnesty 2026-07-29 (Farrice-ratified). Activation count 0; broken pointer (memory/content-voice-calibration.md does not exist); '3-point gate' names a gate that has been 4-point since Factual Grounding shipped; Hard Rules 4/5 ('gates are binding — reject and regenerate') contradict the Compass Doctrine. Live floors: CLAUDE.md Step 4 (2 skill files for content) + task-lifecycle-content.md (slop check, reader contract).
---

# Content Creation Pre-Flight Gate (EXPECTED)

> Trigger: Any writing/drafting/creating task. Loading protocol: `directives/agent-loading-protocol.md`

---

## Step 1: Domain Detection

| Content Type | Default Expert Ensemble |
|:---|:---|
| Lead Magnet / Free Resource | Stockton Walbeck + Harry Dry + Cardinal Mason |
| Profile / About Copy | Lara Acosta + Harry Dry + Caleb Ralston (**+ Writers' Room expected**) |
| Sales / Offer Copy | Cardinal Mason + Harry Dry + Alen Sultanic |
| Social Posts | Kallaway + Shaan Puri + Lara Acosta |
| Email Sequence | Cardinal Mason + Harry Dry + Seena Rez |
| Video Script | Seena Rez + Lucas Alpay + Kallaway |
| DM / Outreach | Jeremy Miner + Alen Sultanic |
| Long-form / Guide | Dan Koe + Nicolas Cole + Harry Dry |

### Step 1b: Writers' Room (Profile Content Only)
Profile content → `.agent/workflows/writers-room.md` EXPECTED from draft 1. 3-layer treatment: Structure → Emotion → Platform/Voice. Additional: check `_active/linkedin-launch/04-deliverables/content-os/arcs/` for off-limits language, write reader-as-protagonist (≥4 recognition beats), confirm char limits via `memory/content-voice-calibration.md`.

## Step 2: Card Check (T0 — EXPECTED)
Read `agents/_framework/invocation-cards.md` → confirm experts, identify PAIRS WITH, find ENTRY PROMPT.

## Step 3: Load Expert Skills (Tiered — EXPECTED)
Semantic-first: `python3 execution/context_retriever.py search "query"` → top chunks.
Fallback: T1 (SKILL.md + prompt ~1,350 tokens) | T2 (+genius.md ~2,550) | T3 (sub-agent ~300 main).
**Minimum: 2 experts loaded. 3 preferred.**

## Step 4: Pattern Extraction
After loading, identify: **3 key patterns** | **1 quality test** (Three Rules, Kristen Stewart, etc.) | **1 anti-pattern**

### Step 4b: Reader Self-Interest Check
Before customer-facing copy, answer from ICP perspective: **"What do I get?"** If you can't answer concretely → not ready to write.

## Step 5: Expert-Driven Execution
Write using loaded frameworks. Patterns MUST inform, not template.

### Step 5b: Post-Production Expert Test (EXPECTED)
> "Could the named expert distinguish this from their own work?"
YES → proceed | NO → reject and regenerate using expert methodology more aggressively.

### Step 5c: General-Training Detection
Flag and REJECT if: (1) no specific pattern identifiable, (2) output could exist without reading skill, (3) generic frameworks used, (4) vocabulary matches "helpful AI" not expert voice. If ANY true → regenerate, not edit.

### Step 5d: AI Slop Detection
Run `directives/ai-slop-detector.md`: Tier 1 vocab scan → em-dash check (max 2/500) → sentence variance → structural trope scan (max 1/piece). Tier 1 words present or 3+ tropes → regenerate.

## Step 6: Quality Gate
Run `quality_gate.md` 3-point gate.

## Step 7: Provenance Tag
`SKILLS LOADED: [list] | PATTERNS APPLIED: [list] | QUALITY TEST: [test, pass/fail]`

---

## Hard Rules

1. **No content without ≥2 skill files read** — no "good enough" exception
2. **"I already know this" is not an excuse** — reading primes framework activation
3. **Speed is not a valid reason to skip** — 30 seconds for quality
4. **General-training output is NEVER acceptable** — reject and regenerate
5. **Expert workflow quality gates are binding** — honor rejection triggers

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-03-19 |

*Created: 2026-02-17 | Compressed: 2026-04-13*
