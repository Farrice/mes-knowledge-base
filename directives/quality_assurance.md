---
status: superseded
superseded_by: directives/quality_gate.md
superseded_date: 2026-07-29
amnesty_note: >
  Rule amnesty 2026-07-29 (Farrice-ratified). Activation count 0 since creation; review date 4 months overdue; three mandates route through the retired `search_web` tool; M3 ('STOP, present interpretations') and M4/AP3 (post-delivery verify passes) directly contradict Partner Posture and the ratified dialect law. Surviving unique rule (GROUNDED/SUPPLEMENTED/PROJECTED labels) folded into quality_gate.md.
---

# Quality Assurance: Anti-Patterns & Mandates

> Embedded in Step 5 (PRODUCE). Internalize during production — not post-production.

---

## 🔴 ANTI-PATTERNS

### AP1: Template Slop
Generating output by filling templates without grounding in real data. Symptoms: `random.randint()` for scores, `f"Best {niche}"` for keywords, unsourced CPC/traffic numbers. **Fix:** All intelligence MUST use Agentic Research (live `search_web`, Perplexity, source citations).

### AP2: Entity Blindness
Treating all inputs the same without classifying what TYPE of thing it is.

| Entity Type | Correct Approach |
|:---|:---|
| Product | Feature/benefit keywords, vs competitors |
| Service | Local modifiers, trust signals |
| Demographic | Programs/assistance that SERVE them |
| Program | Eligibility, dates, application process |
| Location | Geographic specifics, neighborhood guides |

**Fix:** ALWAYS classify input entity BEFORE generating output.

### AP3: Speed Without Validation
Delivering output without cross-checking. **Fix:** Cross-check key claims against external sources. Ask: "Would an expert find this embarrassing?" Cite sources.

### AP4: Phantom Research ⚠️
Marking research tasks complete without invoking external tools. Output LOOKS like deep research — making it harder to catch than Template Slop. **Fix:** See Mandate 5.

### AP5: Structurally Sound But Flat
Content covering all points with correct structure but zero tension/emotion/curiosity. Passes structural checklist, fails vibe check. A 9/10 body with 5/10 emotional register = 5/10 piece.

**Fix:**
1. **Tension Test:** Does the piece build and release tension at least once?
2. **Recognition Test:** ≥2-3 moments where target reader thinks "that's exactly me"?
3. Default to writers' room for content ≥500 chars (Structure → Emotion → Platform/Voice)
4. Never accept first draft of profile copy without writers' room pass

### AP6: AI-Shaped Prose
Expert methodology applied but written in recognizably AI cadence. Tier 1 vocabulary: delve, tapestry, landscape, leverage, robust, pivotal, realm, multifaceted. Excessive em-dashes (>2/500 words). Uniform sentence length. Formulaic reveals ("Here's what no one tells you:"). Ghost citations ("Studies show..."). **Fix:** Run slop detection (`directives/ai-slop-detector.md`).

### AP7: Echo Chamber Deliberation ⚠️
Multi-agent outputs unanimously validating user's existing beliefs by repackaging their own data in expert language — without external research.

**Fix:**
1. Before multi-agent deliberation, run 3-5 Perplexity queries challenging user's position
2. **Echo Chamber Test:** If EVERY agent agrees with what user already believed → re-run with disconfirming queries
3. **Fabrication Scan:** Every number must have a source. No source = 🔴 PROJECTED
4. **Uncomfortable Insight Rule:** Valid output must contain ≥1 finding the user didn't already know
5. Never attribute user assumptions to experts

---

## 🟢 MANDATES

### M1: Entity Understanding First
Before ANY research/generation, classify: `INPUT → ENTITY TYPE → SUB-ENTITIES`

### M2: Agentic Research for Intelligence
All intelligence workflows MUST: use `search_web`/Perplexity for live data, cite sources, NOT use hardcoded templates.

### M3: Pre-Flight Validation for Raw Intent
When user provides rough concept: STOP → present 2-3 interpretations → clarify → execute.

### M4: Post-Delivery Verification
Spot-check 2-3 claims against external sources. Mark confidence: 🟢 Verified / 🟡 Plausible / 🔴 Unverified.

### M5: Perplexity-First Research Gate ⚠️
Any research/intelligence/competitive/market task MUST invoke external tools BEFORE generating agent outputs.

**Enforcement:**
1. Check `directives/perplexity-usage-policy.md` for budget
2. Execute queries via `mcp_perplexity-ask_perplexity_ask`
3. Log every query to `.agent/perplexity-usage.json`
4. Budget exhausted → fall back to `search_web` — NEVER to LLM-only generation
5. Tag deliverables: 🟢 GROUNDED / 🟡 SUPPLEMENTED / 🔴 PROJECTED (must disclose)

---

## Failure Mode Reference

| Failure Mode | Risk | Mitigation |
|:---|:---|:---|
| Template Slop | HIGH | Agentic Research |
| Entity Blindness | MED | Entity Classification |
| Speed Without Validation | MED | Post-Delivery Verification |
| Intent Mismatch | HIGH | Pre-Flight Validation |
| Phantom Research | HIGH | Perplexity-First Gate |
| Echo Chamber | HIGH | Anti-Echo Gate + Uncomfortable Insight Rule |

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-03-19 |

*Last Updated: 2026-04-13 | Compressed via Context Engineering Sprint*
