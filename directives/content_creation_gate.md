# Content Creation Pre-Flight Gate (MANDATORY)

> **Purpose**: Ensure expert skills are loaded and applied before ANY content creation task.
> **Effective**: 2026-02-17 | **Updated**: 2026-02-27 (Context Engine integration)
> **Trigger**: Any task involving writing, drafting, creating, or building content (copy, posts, emails, scripts, guides, PDFs, lead magnets, profile copy, headlines, about sections, pages, etc.)
> **Loading Protocol**: See `directives/agent-loading-protocol.md` for the tiered loading chain

---

## Why This Exists

The expert skill system was being bypassed for content creation tasks. The AI would write content from general knowledge instead of loading and applying the expert frameworks built specifically for this purpose. This happened because:
1. No pre-flight gate existed for content tasks (unlike research, which has the Perplexity-First gate)
2. The quality gate only triggered on expert-produced output — creating a loophole where skipping experts = skipping quality checks

**This directive closes that loophole.**

---

## Pre-Flight Checklist (Run BEFORE Writing Anything)

### Step 1: Domain Detection
Classify the content task:

| Content Type | Signal Keywords | Default Expert Ensemble |
|:---|:---|:---|
| **Lead Magnet / Free Resource** | lead magnet, PDF, guide, resource, freebie | Stockton Walbeck + Harry Dry + Cardinal Mason |
| **Profile / About Copy** | LinkedIn, about, headline, bio, positioning | Lara Acosta + Harry Dry + Caleb Ralston (**+ Writers' Room — see below**) |
| **Sales / Offer Copy** | sales page, offer, pricing, conversion | Cardinal Mason + Harry Dry + Alen Sultanic |
| **Social Posts** | post, content, LinkedIn post, thread | Kallaway + Shaan Puri + Lara Acosta |
| **Email Sequence** | email, sequence, nurture, follow-up | Cardinal Mason + Harry Dry + Seena Rez |
| **Video Script** | script, video, hook, Loom, TikTok | Seena Rez + Lucas Alpay + Kallaway |
| **DM / Outreach** | DM, outreach, message, cold | Jeremy Miner + Alen Sultanic |
| **Long-form / Guide** | article, guide, post, essay | Dan Koe + Nicolas Cole + Harry Dry |

### Step 1b: Writers' Room Trigger (Profile Content)

**If content type = "Profile / About Copy"** — the Writers' Room workflow (`.agent/workflows/writers-room.md`) is MANDATORY from draft 1. Do NOT produce a first draft without running the full 3-layer treatment.

**Why**: Profile content has the highest rate of "structurally sound but flat" failure. Two sessions proved that expert loading alone produces 5/10 profile copy. The writers' room treatment (Structure → Emotion → Platform/Voice) is what produces 10/10.

**Additional pre-treatment for profile content**:
1. **Content ecosystem check**: Read ALL active content in `_active/linkedin-launch/arcs/` before writing. Map off-limits language (phrases owned by upcoming/recent posts).
2. **Reader-as-protagonist**: The About section reader must be the main character, not Farrice. Write in second person. Minimum 4 recognition beats ("that's me" moments).
3. **Platform constraints**: Confirm char limits and truncation behavior before writing (see `memory/content-voice-calibration.md` Platform Constraints section).

### Step 2: Card Check FIRST (Tier 0 — MANDATORY)

Before loading any full skill files, **read `agents/_framework/invocation-cards.md`** to:
- Confirm the right experts for this content type (~50 tokens each vs ~500+)
- Identify the best PAIRS WITH combinations
- Find the correct ENTRY PROMPT for each expert

### Step 3: Load Expert Skill Files (Tiered — MANDATORY)

**Tier 1** (clear task, single expert focus): Read SKILL.md + specific prompt (~1,350 tokens)
**Tier 2** (creative/complex content): Read SKILL.md + genius-patterns + prompt (~2,550 tokens)
**Tier 3** (multi-expert, session context full): Spawn sub-agent with fresh context (~300 tokens main)

See `directives/agent-loading-protocol.md` for full decision matrix.
See `directives/skill-paths-reference.md` for expert-to-file-path mapping.

**Minimum**: Load at least 2 experts before writing. 3 is preferred.

### Step 4: Pattern Extraction

After reading, identify:
- **3 key patterns** from the loaded skills that apply to this task
- **1 quality test** from the skills to run against the output (e.g., Three Rules Test, Kristen Stewart Test)
- **1 anti-pattern** the expert would warn against

### Step 4b: Reader Self-Interest Check

Before writing customer-facing copy, answer ONE question from the ICP's perspective: **"What do I get?"**

If you can't answer that concretely and compellingly, you're not ready to write. This is not a formula — it's the baseline creative instinct that every expert copywriter brings to every line. The expression should be as varied and surprising as the content itself.

### Step 5: Expert-Driven Execution

Write the content using the loaded frameworks. The patterns MUST **inform** the writing, not template it.

### Step 5b: Post-Production Expert Test (MANDATORY)

After producing the content, run this test before ANY delivery:

> **"Could the named expert distinguish this from their own work?"**

- If **YES** → proceed to Step 6
- If **NO** → the output is general-training slop wearing an expert name. **Reject and regenerate.** Re-read the loaded skill's anti-patterns and decision frameworks, then rewrite using the expert's specific methodology more aggressively. Do NOT soften, hedge, or genericize.

### Step 5c: General-Training Detection Test

**Flag and REJECT any output where:**
1. No specific pattern from the loaded skill is identifiable in the output
2. The output could have been produced without reading the skill file
3. The output uses generic frameworks instead of the named expert's unique methodology
4. The vocabulary, rhythm, or structure matches "helpful AI writing" rather than the expert's voice DNA

If ANY of these four conditions is true, the content MUST be regenerated — not edited, regenerated — using the loaded expert patterns as the structural foundation, not decoration.

### Step 6: Quality Gate (Modified Trigger)

Run the 3-point quality gate from `quality_gate.md`. Now it fires because skills were loaded.

### Step 7: Provenance Tag

At the end of the output (or in the artifact metadata), include:
```
SKILLS LOADED: [list]
PATTERNS APPLIED: [list by name]
QUALITY TEST: [which test, pass/fail]
```

---

## Hard Rules (Non-Negotiable)

1. **No content output without at least 2 skill files read** — If you catch yourself writing content without having loaded skills, STOP and load them. Content produced without loaded skills MUST be rejected and regenerated. There is no "good enough" exception.
2. **"I already know this" is not an excuse** — The value of reading skill files isn't information, it's *framework activation*. Reading the patterns primes your output quality even if you "know" the concepts. Skipping this step = guaranteed general-training output.
3. **Speed is not a valid reason to skip** — Loading 2-3 skill files adds ~30 seconds. The quality difference is worth it every time.
4. **"Good enough" general-training output is NEVER acceptable** — If the output could have been produced by any capable AI without reading the expert's skill files, it has failed regardless of surface quality. Reject and regenerate using the loaded methodology.
5. **Expert workflow quality gates are binding** — If a loaded workflow contains a Quality Gate with enforcement language ("do NOT deliver if..."), those rejection triggers MUST be honored. Delivering content that fails a workflow quality gate is a system violation.

---

## Integration

- **Works WITH** `expert_auto_routing.md` — This gate handles the specific case of content creation
- **Works WITH** `quality_gate.md` — Ensures the gate always fires for content tasks
- **Overrides** any impulse to "just write it" without expert loading

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-03-19 |

**Update Rule**: When this gate fires (skill files loaded before content creation), update the date and increment the count.

---

*Created: 2026-02-17 | Triggered by: Root Cause Analysis — Expert System Bypass*
