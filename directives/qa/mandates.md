# QA Mandates

> Always do these. Enforcement fires at Step 5 (PRODUCE).

## 1. Entity Understanding First
Before ANY research/generation, classify: `ENTITY TYPE: [Product|Service|Demographic|Program|Location|Concept]` + list sub-entities.

## 2. Agentic Research for Intelligence
Workflows generating "intelligence" MUST: use search_web or Perplexity for live data, cite sources, NOT use hardcoded templates.

## 3. Pre-Flight Validation for Raw Intent
When user provides rough concept: STOP → Present 2-3 interpretations → Clarify → Execute only after alignment.

## 4. Post-Delivery Verification
Spot-check 2-3 claims against external sources. Mark: 🟢 Verified / 🟡 Plausible / 🔴 Unverified.

## 5. Perplexity-First Research Gate
Any research/intel/competitive/trend task MUST invoke external tools BEFORE agent outputs.
- Check `directives/perplexity-usage-policy.md` for budget
- Execute Perplexity queries for social listening, competitive intel, market validation, trends
- Log queries to `.agent/perplexity-usage.json`
- If budget exhausted → search_web. NEVER LLM-only.
- Tag: `🟢 GROUNDED` / `🟡 SUPPLEMENTED` / `🔴 PROJECTED` (must disclose)
