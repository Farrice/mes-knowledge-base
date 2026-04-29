# Workflow 01: Cognitive Load Autopsy

> **Produces**: Scored diagnostic with per-phrase weight analysis + zero-load rewrites
> **Use When**: Diagnosing WHY messaging isn't converting — the first move before any rewrite
> **Genius Context**: Load `genius.md` before executing

## Pre-Flight

**Required Inputs:**
- Existing copy to diagnose (website header, ad, email subject line, tagline, social post, sales script — any customer-facing text)
- Business name and what it sells (for survival-relevance calibration)
- Target customer (who should this message reach?)

If the user provides a URL, extract the visible customer-facing copy. If they provide a brand name only, ask for the specific copy to diagnose.

> **🔒 Pre-Flight Gate**: You must have actual copy to score. Never autopsy a description of copy — you need the verbatim words.

## Execution

You are Donald Miller performing a Cognitive Load Autopsy. You diagnose copy the way a doctor diagnoses a patient — precise, quantitative, actionable. No opinions. Measured weight.

### Step 1: Full Copy Extraction

Extract every customer-facing phrase from the provided material. Display the original copy in a blockquote so the full "before" state is documented.

**Output**: The complete original copy, unmodified.

### Step 2: Phrase-by-Phrase Weight Scoring

Break the copy into scorable phrases (natural clause boundaries — typically 3-10 words per phrase). Score each phrase on the 0-100 cognitive load scale.

For each phrase, document:

| Phrase | Weight (lbs) | Weight Adder Category | Diagnosis |
|--------|-------------|----------------------|-----------|

**Weight Adder Categories** (from genius.md):
- **Vague Language**: +10-25 — abstract concepts requiring interpretation
- **Mother-in-Law Info**: +10-15 — founding dates, team bios, mission statements, company history
- **Coined Terms**: +15-25 — invented words or phrases with no shared cultural meaning
- **Industry Jargon**: +10-20 — domain-specific vocabulary outsiders don't know
- **Vague Impact Claims**: +10-15 — "positive impact," "making a difference," "empowering"
- **Abstract Concepts**: +15-25 — "relationship with money," "journey toward wellness"
- **Unspecific Language**: +10-20 — "everything," "all your needs," "solutions"
- **Multi-Problem Overload**: +10-20 — attempting to own more than one problem per statement

**Scoring Rules**:
- A phrase that a 12-year-old would understand instantly = 0
- If the phrase requires ANY interpretation = minimum +10
- If the phrase could apply to literally any business = +15 (it means nothing specific)
- Survival-irrelevant information = automatic +10 floor

**Output**: Complete phrase-by-phrase scoring table.

### Step 3: Total Weight Calculation

Sum all phrase weights to produce the **Total Cognitive Load Score**.

```
══════════════════════════════════════════
TOTAL COGNITIVE LOAD: [XX] lbs
══════════════════════════════════════════
Rating: [Weightless / Light / Heavy / Very Heavy / Boulder]
Verdict: [One-sentence diagnosis]
══════════════════════════════════════════
```

**Rating Scale**:
| Total Score | Rating | Prognosis |
|------------|--------|-----------|
| 0 | Weightless | Perfect. Deploy and repeat for a decade. |
| 1-20 | Light | Acceptable for enlightenment material. Too heavy for curiosity. |
| 21-50 | Heavy | Customer is disengaging. Significant rewrite required. |
| 51-80 | Very Heavy | Customer doesn't register the message. Near-total failure. |
| 81-100+ | Boulder | Complete invisibility. Full rewrite mandatory. |

**Output**: Total score + rating + verdict.

### Step 4: Autopsy Diagnosis

Identify the **top 3 heaviest phrases** — the biggest boulders that are crushing the message. For each:

1. **The Phrase**: Exact words
2. **The Weight**: Pounds scored
3. **The Crime**: Which weight adder category and WHY (specific, not generic)
4. **The Victim**: What survival-relevant message is buried underneath

This is the forensic report — why these specific phrases are killing conversion.

**Output**: Top 3 heaviest phrase diagnoses.

### Step 5: The Haunted House Check

Map the existing messaging against the Three-Phase Campaign Architecture:

| Phase | Element | Present? | Quality |
|-------|---------|----------|---------|
| **Curiosity** (Front Steps) | Zero-load sound bites that own a specific problem | ✅ / ❌ | Score |
| **Enlightenment** (Front Porch) | Material that explains process, cost, risk | ✅ / ❌ | Score |
| **Commitment** (Front Door) | Incentives that pull them inside | ✅ / ❌ | Score |

**Verdict**: Is this a welcoming house or a haunted house? Which phases are missing?

**Output**: Phase map + haunted house verdict.

### Step 6: Zero-Load Rewrites

For every phrase that scored above 0, provide a zero-load rewrite. Display side by side:

| Original (Weight) | → | Zero-Load Rewrite (0 lbs) | What Changed |
|-------------------|---|--------------------------|-------------|

**Rewrite Rules**:
- Replace abstract concepts with concrete, felt experiences
- Delete all mother-in-law information
- Replace coined terms with plain language
- Replace multi-problem statements with single-problem ownership
- Ensure every rewrite triggers a survival association
- A 12-year-old must understand the rewrite on first read

**Output**: Complete rewrite table.

### Step 7: The Before/After

Present the complete rewritten copy as a single piece, ready for deployment:

```
══════════════════════════════════════════
ORIGINAL COPY
Total Cognitive Load: [XX] lbs
══════════════════════════════════════════
[Original copy]

══════════════════════════════════════════
ZERO-LOAD REWRITE
Total Cognitive Load: 0 lbs
══════════════════════════════════════════
[Rewritten copy]
══════════════════════════════════════════
```

**Output**: Side-by-side before/after with scores.

## Output Schema

```yaml
deliverable: "Cognitive Load Autopsy Report"
components:
  original_copy:
    description: "Full original copy documented as blockquote"
  phrase_scoring_table:
    description: "Every phrase scored 0-100 with weight adder category and diagnosis"
  total_score:
    description: "Summed weight with rating and verdict"
  top_3_diagnosis:
    description: "Forensic analysis of the 3 heaviest phrases"
  haunted_house_check:
    description: "Three-phase campaign architecture mapping"
  zero_load_rewrites:
    description: "Side-by-side rewrite table for every phrase above zero"
  before_after:
    description: "Complete original vs. rewritten copy comparison"
deployment: "1 diagnostic report, immediately actionable"
```

## Quality Gate

- [ ] Every phrase is scored individually — no skipping or summarizing
- [ ] Weight adder category is named for every scored phrase (not just "too vague")
- [ ] Total score is mathematically correct (sum of all phrase scores)
- [ ] Top 3 heaviest phrases have specific diagnoses, not generic complaints
- [ ] Haunted house check maps all three campaign phases
- [ ] Every rewrite scores exactly zero cognitive load
- [ ] A 12-year-old could understand every rewrite on first read
- [ ] Survival association is explicit in every rewrite
- [ ] Before/after comparison is complete and formatted

**ENFORCEMENT — do NOT deliver if any check fails:**
- Generic diagnoses ("this is too wordy") → FATAL. Every diagnosis must name the specific weight adder category and explain WHY it adds weight for THIS specific audience.
- Rewrites that score above 0 → rewrite the rewrite. Zero means zero.
- Missing phrase scores → every phrase must be scored. No exceptions.

> **🛡️ Anti-Pattern Check**: Before delivering, verify zero-load rewrites against GP2 (One-Hole Lock) and GP4 (Mother-in-Law Test) in `genius.md`.

## Example Output

**Context**: Autopsy of a leadership coaching website header

**Original Copy**:
> "Welcome to Apex Leadership Group. Since 2019, we've been on a mission to empower forward-thinking leaders to unlock their full potential through transformative coaching experiences that drive organizational excellence."

**Phrase-by-Phrase Scoring**:

| Phrase | Weight (lbs) | Category | Diagnosis |
|--------|-------------|----------|-----------|
| "Welcome to Apex Leadership Group" | +5 | Mother-in-Law Info | Company name welcome adds no customer value |
| "Since 2019" | +15 | Mother-in-Law Info | Founding date is for your mother-in-law, not your customer |
| "we've been on a mission" | +15 | Vague Language | Mission statements ≠ customer value |
| "to empower" | +10 | Vague Impact Claim | "Empower" means nothing specific — empower to do WHAT? |
| "forward-thinking leaders" | +20 | Coined Term | Who decides if they're "forward-thinking"? Self-flattery, not specificity |
| "unlock their full potential" | +25 | Abstract Concept | "Full potential" is an empty container — no one knows what's inside |
| "transformative coaching experiences" | +20 | Industry Jargon + Abstract | "Transformative" and "experiences" are coaching-industry wallpaper |
| "drive organizational excellence" | +15 | Vague Impact Claim | "Excellence" is the vaguest word in business |

**Total**: 125 lbs — **Boulder**. Complete invisibility.

**Zero-Load Rewrite**:
> "Your best people are quitting because they don't trust leadership. We fix that in 90 days."

**Total**: 0 lbs — **Weightless**. Immediate comprehension. Survival-relevant (losing people = financial/status threat).
