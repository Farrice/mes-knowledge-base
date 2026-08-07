# Recall Source-Grounding Protocol

## Purpose

Automatically inject high-signal source material from the Recall knowledge base (3,000+ cards, growing) into **Step 4 (LOAD)** of The Chain — with zero cognitive load, zero maintained lists, zero orphaned paths.

**Why this exists:** Skill files distill expert thinking into frameworks. Recall preserves the raw source — transcripts, actual expert language, real examples. Grounding in source material prevents the "Expert Standard 3-4 / generic output wearing expert terminology" failure mode documented in `MEMORY.md` (see 2/10 LinkedIn session lessons).

---

## Trigger — automatic, every expert load

Recall grounding fires when **all** of the following are true:

1. Step 3 of The Chain routed to an expert (not a system-only task)
2. The expert's domain falls in the **grounding-relevant set**:
   - Content, copywriting, brand, voice, hooks, storytelling, positioning, strategy, sales, ghostwriting, marketing, persuasion, comms, attention, audience, creative
3. Not suppressed by a `--no-ground` flag

**Does NOT fire for:** code tasks, data processing, system commands, pure analytical work, file organization, debugging, API integration, deployment ops.

The "grounding-relevant" check is derived from the expert's swim lane in `DOMAIN_REGISTRY.md` — no hand-maintained list of experts.

---

## Query Pattern

Construct ONE combined query against Recall:

```
tool: mcp__recall__search
queries: [
  "{expert_full_name} {intent_keywords}",   # expert-specific — e.g. "Lara Acosta LinkedIn hook"
  "{domain_concept} {intent_keywords}"       # cross-expert pattern — e.g. "hook writing"
]
mode: "focused"
```

The two-query form is cheap (one API call via array) and captures both expert-specific content AND cross-expert pattern content. Recall's `focused` mode is already semantic-relevance filtered.

---

## Score Gate — the tunable knob

Recall returns results ranked by semantic relevance. Gate inclusion as follows:

1. **Require ≥2 cards** returned across both queries combined
2. **Cap at top 3 cards total, 2 chunks each** → hard token budget ≈ 1,200 tokens
3. **Relevance heuristic** (score proxy — Recall doesn't expose numeric scores):
   - **HIGH signal** (include all top 3): expert name appears as a tag OR in chunk content, on at least 2 of the returned cards
   - **MEDIUM signal** (include top 1-2 only): keyword matches but expert name absent — likely tangential
   - **LOW signal** (skip entirely): only 1 card returned, or all cards lack the expert name AND the intent keywords appear only in generic chunks
4. **When in doubt, under-ground.** Better to return to skill files alone than to inject noise.

---

## Injection Format

When grounding fires, inject into context **before** loading skill files:

```
--- Recall source grounding (N cards, {expert_name}) ---
[card_id: {id}] {title}
Source: {source_url}
{chunk_content_preview ~200 tokens}

[card_id: {id}] {title}
Source: {source_url}
{chunk_content_preview ~200 tokens}
---
```

Then proceed with normal Tier 1 / Tier 2 skill file loading. **Do NOT announce the grounding to the user** unless they explicitly ask what source material was used. The protocol is invisible infrastructure.

---

## Token Budget — hard caps

| Tier | Recall budget |
|---|---|
| Tier 1 (SKILL.md only) | 3 cards × 2 chunks ≈ 1,200 tokens |
| Tier 2 (SKILL.md + genius.md) | 1 card × 2 chunks ≈ 600 tokens |
| Tier 3 (sub-agent) | Sub-agent decides; main thread stays lean |

If Tier 2 is loaded AND Recall returns high signal, prefer 2 cards × 1 chunk (diverse source) over 1 card × 2 chunks (deeper single source).

---

## Failure Modes — all handled by silent skip

| Condition | Behavior |
|---|---|
| Recall MCP disconnected / tools unavailable | Skip silently, proceed with skill files |
| 0–1 cards returned | Skip silently, no announcement |
| All results score below relevance heuristic | Skip silently |
| API timeout > 5s | Skip, proceed immediately |
| User passed `--no-ground` flag | Skip, no announcement |
| Expert domain outside grounding-relevant set | Don't query at all |

Silent skip is mandatory. Never announce "I tried Recall but…" — it creates noise. The skill files are the baseline; Recall is a bonus.

---

## Logging — `recall_logger` is mandatory (Fix 5 / 2026-04-24)

**Every grounding decision (fire OR skip OR fail) must be logged to `evolution_store/traces/recall_grounding.jsonl` via `execution/recall_logger.py`.** Silent skip is still the user-facing behavior, but silent in the traces is the failure mode that this fix exists to prevent — a feature you can't measure can't be tuned and can't be trusted.

**Call pattern** — fire ONE of these immediately after each grounding decision:

```bash
# When grounding fired successfully
python3 execution/recall_logger.py log --status fired \
    --domain content --expert lara-acosta \
    --query "Lara Acosta LinkedIn hook" \
    --cards-returned 3 --signal high

# When grounding was skipped (use canonical reasons)
python3 execution/recall_logger.py log --status skipped \
    --reason {disconnected|no_signal|low_signal|timeout|no_ground_flag|non_grounding_domain} \
    --domain content --query "..."

# When grounding failed mid-flight
python3 execution/recall_logger.py log --status failed \
    --reason timeout --domain content --query "..."
```

**Also keep the `--notes` line in `finalize` for human readability:**
```
Recall grounding: {N} cards | top: "{title}" | signal: HIGH
```

**Weekly correlation check** — produces a hypothesis test on whether grounding actually lifts Expert Standard scores:
```bash
python3 execution/recall_logger.py report --days 7
```

If after ≥30 fired-grounding sessions the lift_vs_baseline is ≤0 or near-zero, the Tier 1.5 design hypothesis is wrong and the relevance gate or query construction needs revision. Until that data exists, grounding is theoretically useful — not measurably useful.

---

## Manual overrides

Usable in any workflow invocation or user message:

- **`--ground-deep`** — up to 5 cards, token budget expanded to ~2,500 tokens. Use for deep creative work (manifestos, long-form content, brand work).
- **`--ground-topic "X"`** — append specific topic terms to the grounding query. Use when the user's intent keywords are vague.
- **`--no-ground`** — suppress grounding entirely. Use when the user wants pure skill-file output (e.g., to test a skill in isolation) or when the task is exploratory/diagnostic.

---

## Self-calibration — why this requires zero maintenance

- **New experts get grounded automatically** once their content is extracted into Recall (tag appears → query hits → cards return).
- **Thin domains silently skip** — no bloat when Recall has nothing relevant.
- **Relevance improves naturally** as the library grows.
- **No hand-maintained "which experts to ground" list** — the grounding-relevant domain set is broad enough to cover anything Recall would plausibly have content on.
- **Score gate tunes itself** to signal quality; thin signal → under-ground → degrades gracefully to current behavior.

---

## Relationship to other protocols

| Protocol | Interaction |
|---|---|
| `agent-loading-protocol.md` | Recall fires BEFORE Tier 1 skill file load, as Tier 1.5 context |
| `content_creation_gate.md` | Content tasks get grounding by default (overlapping trigger) |
| `quality_gate.md` (Step 6) | Expert Standard scoring should credit grounded outputs as a positive signal |
| `cross-pollination.md` | Recall's cross-expert patterns feed Phase 3 naturally |
| `feedback-ratchet.md` | Logs capture grounding signal for future calibration |

---

## First-90-days evaluation criteria

After 30 chain invocations where grounding fired:
- Did Expert Standard scores rise vs. baseline (pre-grounding median ≈ 7)?
- Were there any cases where grounding introduced factual errors? (if yes → tighten score gate)
- Which expert domains benefited most? (inform future extraction priorities)

Re-evaluate protocol tuning after that checkpoint.
