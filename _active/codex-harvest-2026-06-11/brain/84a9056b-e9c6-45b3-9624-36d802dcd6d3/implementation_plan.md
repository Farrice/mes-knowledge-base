# MES 3.0 Savant-Level Extraction Upgrade

Upgrade the extraction pipeline to capture exemplars, signature moves, and quality rubrics from source material — then retrofit all existing agents with these components.

## User Review Required

> [!IMPORTANT]
> **This is a 2-phase approach:**
> 1. **Pipeline upgrade** — modify 4 existing files + create 1 new script so all future extractions automatically capture the savant-level context
> 2. **Retrofit enrichment** — run a parallel swarm to enrich all existing genius.md files with the new components
>
> The pipeline upgrade happens first so the pattern is locked in before we mass-retrofit.

> [!WARNING]
> The parallel swarm for retrofitting ~131 agents will cost approximately **$1.50-3.00** in Gemini API calls (flash tier). Each agent gets a targeted enrichment call that reads its existing genius.md + source extraction and generates the 3 new sections.

---

## Proposed Changes

### MES 3.0 Extraction Directive

#### [MODIFY] [mes-3.0-extract.md](file:///Users/farricecain/Google%20Antigravity/directives/mes-3.0-extract.md)

Add **3 new extraction components** to the extraction report template (Step 3, after Hidden Knowledge):

**1. Exemplar Extraction** (new section)
- `## Hall of Fame Exemplars` — Extract 2-3 verbatim or near-verbatim examples from the source material that demonstrate the expert's methodology at its best
- Include a "**What makes this excellent**" annotation for each exemplar
- Include 1 "**Anti-exemplar**" showing what mediocre output looks like in this domain
- Extraction instruction: *"Mine the source material for the expert's best demonstrations. These are the moments where they show, not tell — actual examples, case studies, before/afters, or worked solutions. If the source doesn't contain examples, note this as a gap."*

**2. Signature Moves Extraction** (new section)
- `## Signature Moves` — Extract 3-5 concrete, behavioral moves (not concepts) that define this expert
- Format: `**[Move Name]**: [1-2 sentence description of the specific action] → [When to deploy it]`
- Extraction instruction: *"Look for the expert's instinctive first actions, recurring micro-decisions, and constraints they always apply. These are the things they do without explaining — the moves a 1-year apprentice would learn by watching, not reading."*

**3. Quality Rubric Extraction** (new section)
- `## Expert-Specific Quality Rubric` — Extract 5-7 criteria that define excellence in THIS expert's domain
- Format: `**[Criterion]**: Score 4 = [description] | Score 7 = [description] | Score 10 = [description]`
- Extraction instruction: *"Reverse-engineer the expert's quality standards from their critiques, praise, corrections, and the gap between their 'good enough' and 'excellent.' What would they reject? What would make them proud?"*

Also upgrade the **5-Layer Analysis** (Step 2) — add a 6th lens:

**Layer 6 — Exemplar & Move Mining**
- What are the expert's best demonstrations in this material?
- What do their examples *reveal* about unstated quality standards?
- What actions do they take first, always, or reflexively?
- What do they notice that amateurs miss?

---

### Extract Workflow

#### [MODIFY] [extract.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/extract.md)

Update Step 2 (Run Extraction) and Step 4 (Checkpoint) to reference the 3 new components:

- Step 2: After "Run each finding through the internal validation checklist," add: *"Additionally, extract Hall of Fame Exemplars, Signature Moves, and Expert-Specific Quality Rubric per the upgraded mes-3.0-extract.md."*
- Step 4 checkpoint: Add exemplar count, signature move count, and quality rubric presence to the presentation items
- Step 5b: Update genius.md creation instructions to include the 3 new sections

---

### Genius.md Merge Function

#### [MODIFY] [skill_converter.py](file:///Users/farricecain/Google%20Antigravity/execution/skill_converter.py)

Update `merge_genius_file()` (lines 188-220) to include the 3 new sections when they exist in the extraction:

```diff
+    # Look for exemplars file
+    exemplars_path = skill_path / "references" / "exemplars.md"
+    if exemplars_path.exists():
+        sections.append("## Hall of Fame Exemplars\n")
+        sections.append(exemplars_path.read_text().strip())
+
+    # Look for signature moves file
+    moves_path = skill_path / "references" / "signature-moves.md"
+    if moves_path.exists():
+        sections.append("## Signature Moves\n")
+        sections.append(moves_path.read_text().strip())
+
+    # Look for quality rubric file
+    rubric_path = skill_path / "references" / "quality-rubric.md"
+    if rubric_path.exists():
+        sections.append("## Expert-Specific Quality Rubric\n")
+        sections.append(rubric_path.read_text().strip())
```

---

### Convert Extraction Workflow

#### [MODIFY] [convert-extraction.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/convert-extraction.md)

Update Step 1 (Audit Extraction) and Step 3 (Create genius.md) to include the new components:

- Step 1: Add "Hall of Fame Exemplars," "Signature Moves," and "Quality Rubric" to the items extracted from the report
- Step 3: Update the genius.md template to include the 3 new sections

---

### Enrichment Script (New)

#### [NEW] [genius_enricher.py](file:///Users/farricecain/Google%20Antigravity/execution/genius_enricher.py)

A new Python script that retrofits existing genius.md files with the 3 missing components. Architecture:

1. **Discovery** — Find all `skills/*/genius.md` files
2. **Assessment** — Read each genius.md and check if it already has Exemplars, Signature Moves, and Quality Rubric sections
3. **Enrichment** — For files missing components, fire a Gemini API call with:
   - The existing genius.md content
   - The extraction report (if available at `extractions/[expert]/extraction-report.md`)
   - A prompt that asks the model to generate the 3 missing sections based on the existing genius patterns, hidden knowledge, and any source material context
4. **Write** — Append the new sections to the existing genius.md (don't overwrite hand-crafted content)
5. **Clean** — Also detect and clean up the auto-generated DF/AP/VD template sections (the ones with corrupted text and generic anti-patterns)

CLI Usage:
```bash
# Enrich a single expert
python execution/genius_enricher.py --skill "skills/kallaway-word-mastery"

# Enrich all experts
python execution/genius_enricher.py --all

# Preview enrichment plan
python execution/genius_enricher.py --all --plan-only

# Enrich without cleaning DF/AP/VD
python execution/genius_enricher.py --all --no-clean
```

The enrichment prompt will include specific instructions to:
- Mine the existing genius patterns for implicit exemplars and signature moves
- Generate expert-specific (not generic) quality rubrics
- Remove templated DF/AP/VD sections and replace with expert-specific versions
- Match the tone and depth of the best hand-crafted genius.md files (Eric Roth as the gold standard)

---

## Verification Plan

### Automated Tests

1. **Structure validation** — After modifying `skill_converter.py`, run:
   ```bash
   python execution/skill_converter.py --skill "skills/kallaway-word-mastery" --plan-only
   ```
   Verify the plan-only output shows the skill with no errors.

2. **Enrichment dry run** — After creating `genius_enricher.py`, run:
   ```bash
   python execution/genius_enricher.py --all --plan-only
   ```
   Verify it discovers all genius.md files and correctly identifies which ones need enrichment.

3. **Single expert enrichment test** — Run on one expert:
   ```bash
   python execution/genius_enricher.py --skill "skills/kallaway-word-mastery" --dry-run
   ```
   Verify the generated sections are expert-specific (not generic), contain concrete behavioral content, and don't corrupt existing hand-crafted content.

### Manual Verification

1. **Before/after comparison** — After enriching Kallaway, compare the genius.md before and after to verify:
   - Hand-crafted Buckets 1-8 and GP-WM patterns are preserved unchanged
   - Auto-generated DF/AP/VD template sections are replaced with expert-specific content
   - New Exemplars, Signature Moves, and Quality Rubric sections are genuinely specific to Kallaway's methodology
   - No corrupted text remains

2. **Extraction pipeline test** — Run a real `/extract` on new source material after the `mes-3.0-extract.md` upgrade and verify the extraction report now includes the 3 new components
