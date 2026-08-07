---
description: Deep Research via Gemini Interactions API (pilot)
---

# /deep-research-gemini — Deep Research via Gemini (PRIMARY)

Execute grounded research using Google's Deep Research API (Dec 2025) or Deep Research Max (April 2026) — Gemini 3.1 Pro-backed autonomous research agents with 93.3% DeepSearchQA accuracy.

**This is the PRIMARY deep-research path (as of 2026-04-23).** Perplexity sonar-deep-research is the fallback when this is unavailable. The `/deep-research` umbrella workflow now routes its foundation layer here first.

## Safety

Three layers of defense against overspend — see `directives/google-api-usage-policy.md`:
1. Ultra subscription covers AI Studio usage (Ultra linked to AI Studio, April 20 2026)
2. Pay-as-you-go explicitly disabled (no overflow billing)
3. $10 prepaid balance as absolute ceiling (physically cannot exceed)

Maximum possible spend: **$10**, no matter what.

## When to Use

Use `/deep-research-gemini` (PRIMARY path) when:
- You need foundation research (strategy, positioning, market entry)
- Research output will feed downstream agent work (so accuracy matters)
- `/grounding-pass` keeps finding errors — you need a more reliable source
- Any Standard or Deep depth research task — this is now the default

Falls back to Perplexity sonar-deep-research automatically when:
- Deep Research prepaid is exhausted (< $0.50 remaining)
- Deep Research API errors or rate-limits
- Per-task cap reached (5 Deep Research calls per task)

## Usage

```
/deep-research-gemini [topic or question]
/deep-research-gemini --max [topic]   # Use Deep Research Max (slower, more comprehensive)
/deep-research-gemini --compare [topic]  # Run BOTH Perplexity and Gemini, side-by-side
```

## Steps

### 1. Pre-flight safety check

Read `.agent/gemini-api-usage.json`:
- If `prepaid_balance < $0.50` → STOP. Fall back to `/deep-research` (Perplexity).
- If task context shows ≥5 Deep Research calls this session → STOP. Per-task cap.
- If warn threshold (80%) hit → proceed but notify user of remaining balance.

### 2. Execute research

// turbo
```bash
python3 execution/deep_research_client.py "[query]" --mode standard --task-context "[workflow name]"
```

Or for max comprehensiveness:
// turbo
```bash
python3 execution/deep_research_client.py "[query]" --mode max --task-context "[workflow name]"
```

### 3. Route through research quality gate

After the call completes, validate using existing `execution/research_quality_gate.py`:
- Provenance audit (% of findings with source URLs)
- Recency check
- Echo chamber detection (unique domain count)
- Minimum 5 sources for standard, 15 for max

### 4. Present results

Surface:
- **Summary**: The synthesized research text
- **Citations**: Source URL list (verify each is a real, accessible source)
- **Quality score**: From `research_quality_gate.py`
- **Cost**: Actual spend against prepaid (should be $0 if Ultra covered)
- **Duration**: How long Deep Research took

### 5. Log for pilot evaluation

If this is a pilot comparison run (Phase 2 of the maximize-subscriptions plan):
- Record in `.agent/evolution-logs/2026-deep-research-pilot.md`
- Fields: query, mode, duration, est. cost, quality score, subjective rating vs Perplexity
- After 10 runs, Farrice decides: promote, keep both, or drop

---

## Comparison Mode (`--compare`)

When run with `--compare`, executes the same query against both research backends:

1. Run `/deep-research` (Perplexity sonar-deep-research) → save to `.tmp/research/perplexity-[slug].md`
2. Run `/deep-research-gemini` → save to `.tmp/research/gemini-[slug].md`
3. Diff the two outputs:
   - Citation count
   - Unique domains cited
   - Synthesis quality (subjective, user judges)
   - Contradiction catching
4. Output to `.tmp/research/compare-[slug].md` with side-by-side view

This is the **quality test protocol** from the pilot plan.

---

## Fallback Behavior

If Deep Research fails for any reason:
- API error → log, fall back to Perplexity
- Budget exhausted → log, fall back to Perplexity
- Timeout (>15 min) → log, partial result returned or fall back
- Rate limit (429) → wait + retry once, then fall back

Never silently return empty research. Always either succeed with Deep Research OR cleanly fall back to Perplexity with the fallback tagged.

---

## What This Produces

A grounded research report with:
- Synthesized answer to the query
- Citation list (real URLs, verifiable)
- Quality score
- Duration + cost metadata
- Flag for whether Ultra covered the call or prepaid was consumed

Saved to `.tmp/research/gemini-[depth]-[slug].md`.

---

## Invariants

**Never:**
- Call Deep Research without reading `.agent/gemini-api-usage.json` first
- Use `GEMINI_API_KEY` (legacy pay-as-you-go) — always use `GOOGLE_AI_STUDIO_KEY`
- Silently fall back — always log the fallback and tag the output
- Exceed 5 Deep Research calls per task context without explicit override

**Always:**
- Verify prepaid balance before start
- Log every call with full context to `.agent/gemini-api-usage.json`
- Route output through `research_quality_gate.py`
- Tag output with source (`Deep Research` vs `Deep Research Max` vs `Perplexity fallback`)
