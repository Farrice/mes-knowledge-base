---
description: Extract expert knowledge
---

# /extract — Mastery Extraction Workflow (v2.1)

Extract expert knowledge from any source material and produce a deployable completion-engine skill with 3-5 end-to-end workflows.

## Usage

```
/extract [source material — paste transcript, provide URL, or reference a file]
```

## Steps

### 1. Receive Source Material
Accept transcript, article, course content, interview, or any knowledge-dense material. If the user provides a URL, read the content first.

**If YouTube URL**, prefer a context ledger before extraction:
```bash
// turbo
python3 execution/video_context_ledger.py "<youtube_url>" --mode transcript
```
Use `extractions/video-context/<video-id>/video-context-ledger.md` as the source when transcript-only evidence is enough.

Use `transcript.txt` as the clean reading surface and `transcript_segments.json` or `video-context-ledger.md` for timestamped evidence. Verify package shape before extraction:

```bash
// turbo
python3 execution/verify_video_context_source_package.py "extractions/video-context/<video-id>"
```

If visuals, slides, screen recordings, demos, charts, ads, or creative references matter, run the full ledger:
```bash
// turbo
python3 execution/video_context_ledger.py "<youtube_url>" --mode full
```

Legacy transcript-only fallback:
```bash
// turbo
python3 execution/fetch-transcript.py "<youtube_url>" "<expert-name>"
```
Saves to `extractions/<expert-name>/transcript.txt`. If expert unknown, omit name — move after identification.

### 1.5. Expert Identification (CRITICAL)
- The "by [Name]" in transcript headers is often the **transcription tool**, NOT the speaker
- Check video title, channel name, and content for the actual expert
- If expert exists (check `AGENT_INDEX.md`), note for dedup
- If ambiguous, **ask the user** — never guess
- Record: `Expert: [Name] | Transcribed by: [Tool]`

### 2. Run Extraction
Read `directives/mes-3.0-extract.md` and execute its process against the source material. Preserve source mechanics before synthesis and separate direct source evidence from domain extrapolation.

### 3. Validate (Recommended)
Read `directives/mes-3.0-validate.md` and execute.

### 4. CHECKPOINT 1: Workflow Planning
**User decision point.** Present:
- Expert name and domain
- Genius patterns + hidden knowledge counts
- Exemplar count, signature moves count, quality rubric (present/absent)
- **Proposed 3-5 workflows** — name, what it produces, which methodology it captures, trigger
- Any flags

**Wait for user approval before proceeding.**

### 5. Generate Completion Engine Skill
// turbo

#### 5a. Create directories
```bash
mkdir -p skills/[skill-name]/workflows agents/[expert-name]/memory
```

#### 5b. Create genius.md
Merge all genius patterns + hidden knowledge + exemplars + signature moves + quality rubric into `skills/[skill-name]/genius.md`.

#### 5c. Generate workflow files
Create `skills/[skill-name]/workflows/01-[name].md`, `02-[name].md`, etc.

Each workflow MUST: load genius context, produce a specific deliverable, mirror expert thinking, embed genius patterns inline, include Output Schema and Quality Gate.

#### 5d. Example enrichment (MANDATORY)
- Every workflow needs an `## Output Schema` section
- At least 2 of 3+ workflows need a `## Example Output` with a worked example
- Each example: realistic scenario, partial output, and a `**What makes this excellent**` annotation
- Reference: `skills/chris-cimorelli-copywriting/workflows/01-front-end-promotion.md`

#### 5e. Write SKILL.md
Use completion engine format with frontmatter (name, description, version: "2.0", format: "completion-engine", workflows count), expert context, workflow table, and quick reference.

### 6. Create Agent Files
// turbo
- `agents/[expert-name]/AGENT.md` — standard agent template
- `agents/[expert-name]/memory/context.md` — initialize with activation date

### 7. Register
// turbo
Add to `AGENT_INDEX.md` and `SKILL_INDEX.md`.

### 8. CHECKPOINT 2: Quality Verification
Present one sample workflow for user review. If quality passes → DEPLOYED. If not → iterate.

### 9. Performance Log
```bash
python3 execution/chain_runner.py finalize "[Expert] — [Domain] extraction" \
    --expert [expert-name] --skill [skill-dir] --workflow extract \
    --type Extraction --intent 8 --expert-score 8 --adversarial 7 \
    --notes "[genius patterns count], [workflows count], [key insight]"
```

### 10. Wiki Cascade (Karpathy Ingest)
After extraction completes, update the knowledge wiki:
```bash
python3 execution/knowledge_compiler.py log ingest "[Expert] — [Domain] extraction" --domain [domain] --expert [expert-name] --notes "[workflows count] workflows, [genius patterns count] patterns"
python3 execution/knowledge_compiler.py briefing
```
This closes the compounding loop: new expert knowledge updates the session briefing and living index so future sessions start smarter.

### 11. Report
Present: expert name/domain, tier used, genius + hidden knowledge counts, workflows created, applied intelligence highlights, skill location, quality score.

## Options
- **Skip validation**: "skip validation" or "light extract" → bypass Step 3
- **Deep extract**: "deep extract" → force Deep tier
- **Validate only**: "/validate [skill name]" for existing extractions
