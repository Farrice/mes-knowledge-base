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

### 5.5. Forge Execution Prompts (MANDATORY — spec: `directives/prompt-forging-spec.md`)
// turbo
A skill without its execution prompts is half-finished. For each distinct deliverable the skill produces (derived from its workflows; typically 4-10):
- Write a **born-v2 structure-pure prompt** to `skills/[skill-name]/references/prompts-v2/` — Role & Activation (real credentials only), Input Required `[BRACKET]`s, Execution Protocol at full methodology depth FROM THE EXTRACTED MATERIAL (never training memory), Output Contract, Output Skeleton (placeholders only), Quality Gate, Deploy When. Fidelity rule: thin source → fewer/deeper prompts, never invented filler.
- Wire: `python3 execution/renaissance_audit.py` (must be 0 fail) → `python3 execution/prompt_library.py build` → `python3 execution/wire_prompt_pointers.py --write` → add `Execution prompt: references/prompts-v2/<file>.md` under each workflow's output step.

### 6. Create Agent Files
// turbo
- `agents/[expert-name]/AGENT.md` — standard agent template
- `agents/[expert-name]/memory/context.md` — initialize with activation date

### 7. Register (generators, not hand-edits)
// turbo
Run BOTH generators — they refresh `AGENT_INDEX.md` + `SKILL_INDEX.md`, mint the per-skill command shim, create/refresh the **expert front-door command** (`/[expert-name]` = AGENT.md persona + every skill they own, tier-gated), and put everything in the menu:

```bash
python3 execution/sync_registries.py
python3 execution/generate_slash_commands.py
```

Verify: `.claude/commands/[expert-name].md` exists and lists the new skill; the skill's commands appear in `SLASH_COMMANDS.md` (`grep`). A skill that is fireable but absent from the menu is a registration failure — the 2026-07-15 audit found 1,192 accumulated strays from skipping this.

### 8. CHECKPOINT 2: Quality Verification (embodiment, not eyeball — instrumented, Wave 2)

Run this exact sequence (the judgment stays human/model; the ritual and record are code):

```bash
# 1. Corpus gate — ≥2 real published pieces in extractions/[skill-dir]/reference-corpus/
#    (exit 1 prints exactly what to collect; collect it, re-run)
python3 execution/blind_pass.py prepare --expert [skill-dir]
```

2. **Side-by-side judgment** (human/model — per `directives/embodiment-standard.md` Blind-Pass Protocol): generate 1-2 outputs with the new skill's Tier-1 workflow, place beside the reference-corpus pieces, judge against the recognition test. Farrice judges when stakes are high (A-tier promotion). PASS = indistinguishable or preferred. FAIL → fix the weakest checklist item, iterate once, else ship B-tier with the gap named.

```bash
# 3. Record the verdict — appends the eval_set entry + ledger line automatically
python3 execution/blind_pass.py record --expert [skill-dir] --verdict PASS|FAIL \
    --notes "[which real pieces, what held / what gave it away]" \
    --generated [path] --reference [path]

# 4. Heartbeat gate — 6 tier-affecting craft checks (skill-craft-standard.md §8);
#    ≥2 failures = tier capped at B (exit 1). Fix or ship with the gap named.
python3 execution/skill_auditor.py check --skill [skill-dir]
```

Present the blind-pass result — not just a sample workflow — for user review.

### 9. Performance Log
Scores derive from the Checkpoint-2 blind-pass verdict + checklist coverage — never templated (`directives/embodiment-standard.md` § Scoring Discipline). Any dimension ≥8 requires `--anchor-named "<anchor phrase>"` (the rubric_v1.md anchor, as a string — finalize refuses unanchored ≥8s). Finalize also refuses `--type Extraction` without the Step-8 recorded verdict (`--skip-blind-pass` is the logged override).
```bash
python3 execution/chain_runner.py finalize "[Expert] — [Domain] extraction" \
    --expert [expert-name] --skill [skill-dir] --workflow extract \
    --type Extraction --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --anchor-named "[rubric anchor phrase, required for any ≥8]" \
    --notes "[genius patterns count], [workflows count], [key insight] | blind-pass: [PASS/FAIL] | heartbeat: [n/6]"
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
