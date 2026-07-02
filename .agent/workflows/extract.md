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

**If YouTube URL**, auto-fetch the transcript:
```bash
// turbo
python3 execution/fetch-transcript.py "<youtube_url>" "<expert-name>"
```
Saves to `extractions/<expert-name>/transcript.txt`. If expert unknown, omit name — move after identification.

### 1.6. Visual Context Capture (Auto, additive)

If the source is a video URL or local video file, fetch frame-grounded visual context **in parallel with transcript**. Adds a sidecar `visual-context.md` (frame paths + grounded transcript + visual notes) when available — never blocks transcript-only flow.

```bash
// turbo
python3 execution/fetch-video-context.py "<youtube_url>" "<expert-name>" || true
```

Auto-skips for: non-video sources, videos > 10min, uncaptioned-no-Whisper-key, plugin not installed. See [`directives/video-vision-protocol.md`](../../directives/video-vision-protocol.md). Exit 2 = SKIPPED (silent), exit 0 = OK (visual-context.md ready), exit 1 = FAILED (logged warning, continue with transcript).

If `extractions/<expert-name>/visual-context.md` exists after this step, load it alongside `transcript.txt` for all downstream extraction passes — visual hooks, on-screen text, gestures, and B-roll patterns become extractable.

### 1.5. Expert Identification (CRITICAL)
- The "by [Name]" in transcript headers is often the **transcription tool**, NOT the speaker
- Check video title, channel name, and content for the actual expert
- If expert exists (check `AGENT_INDEX.md`), note for dedup
- If ambiguous, **ask the user** — never guess
- Record: `Expert: [Name] | Transcribed by: [Tool]`

### 2. Run Extraction
Read `directives/mes-3.0-extract.md` and execute its process against the source material.

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

### 8. CHECKPOINT 2: Quality Verification (embodiment, not eyeball)
Run the embodiment check per `directives/embodiment-standard.md` (E4 2026-07-02): 10-item build checklist + mini blind-pass — generate 1 output with the new skill's primary workflow and place it beside a real published piece by the expert. PASS (indistinguishable/preferred) → DEPLOYED. FAIL → fix the weakest checklist item, iterate once, else ship B-tier with the gap named. Append the verdict as an eval entry (≥1 per ship). Present the blind-pass result — not just a sample workflow — for user review.

### 9. Performance Log
Scores derive from the Checkpoint-2 blind-pass verdict + checklist coverage — never templated (`directives/embodiment-standard.md` § Scoring Discipline). Any dimension ≥8 requires `--anchor-named` + naming the anchor in notes.
```bash
python3 execution/chain_runner.py finalize "[Expert] — [Domain] extraction" \
    --expert [expert-name] --skill [skill-dir] --workflow extract \
    --type Extraction --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "[genius patterns count], [workflows count], [key insight] | blind-pass: [PASS/FAIL] | anchors: [named for any ≥8]"
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
