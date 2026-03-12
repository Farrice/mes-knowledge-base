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

### Step 5: Expert-Driven Execution

Write the content using the loaded frameworks. The patterns should **inform** the writing, not template it.

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

## Hard Rules

1. **No content output without at least 2 skill files read** — If you catch yourself writing content without having loaded skills, STOP and load them.
2. **"I already know this" is not an excuse** — The value of reading skill files isn't information, it's *framework activation*. Reading the patterns primes your output quality even if you "know" the concepts.
3. **Speed is not a valid reason to skip** — Loading 2-3 skill files adds ~30 seconds. The quality difference is worth it every time.

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
