---
description: Run 2-5 extractions in parallel using sub-agents — each processes a different source simultaneously
---

# /parallel-extract — Parallel Extraction Swarm

Run multiple expert extractions simultaneously. Each sub-agent gets a fresh context window, reads its source material, and produces an extraction report independently.

## Usage

```
/parallel-extract [list of sources — YouTube URLs, files, or pasted transcripts]
```

## When to Use

- 2+ transcripts/sources ready for extraction at the same time
- Batch processing after a video binge or research session
- Time-sensitive: need multiple extractions done fast

## Steps

### 1. Identify Sources and Experts

For each source provided:
- Identify the expert (from video title, channel, or content)
- Check `AGENT_INDEX.md` for existing agents (avoid duplicate extraction)
- Assign each source to a sub-agent

Present the plan:
```
## Parallel Extraction Plan

| # | Source | Expert | Status |
|---|--------|--------|--------|
| 1 | [URL/file] | [Expert Name] | Ready |
| 2 | [URL/file] | [Expert Name] | Ready |
| 3 | [URL/file] | [Expert Name] | Ready |

Launch all [N] extractions in parallel? Or adjust?
```

Wait for user approval.

### 2. Fetch Transcripts (if YouTube URLs)

// turbo
Run transcript fetches in parallel:
```bash
python3 execution/fetch-transcript.py "<url_1>" "<expert-1>" &
python3 execution/fetch-transcript.py "<url_2>" "<expert-2>" &
python3 execution/fetch-transcript.py "<url_3>" "<expert-3>" &
wait
```

### 3. Launch Parallel Sub-Agents

Spawn one Task tool sub-agent per extraction **in a single message** (this is what makes them parallel):

Each sub-agent prompt:
```
You are an extraction specialist. Read and execute these steps:

1. Read the source material: [file path]
2. Read the extraction methodology: directives/mes-3.0-extract.md
3. Determine extraction tier (Light / Standard / Deep)
4. Produce the extraction report with:
   - Expert identity and domain
   - Genius patterns (numbered, with examples)
   - Hidden knowledge (non-obvious insights)
   - Methodology framework
   - Applied Intelligence section
5. Write the report to: extractions/[expert-name]/extraction-report.md
6. Write a 3-5 sentence summary of key findings

Do NOT create skill files yet — extraction only.
```

**Critical**: All Task tool calls go in the SAME message. This triggers true parallel execution.

### 4. Collect and Review

After all sub-agents return:
- Read each extraction report
- Present a unified summary:

```
## Extraction Results

| # | Expert | Tier | Genius Patterns | Hidden Knowledge | Key Insight |
|---|--------|------|----------------|-----------------|-------------|
| 1 | [Name] | [Tier] | [count] | [count] | [1-line] |
| 2 | [Name] | [Tier] | [count] | [count] | [1-line] |
| 3 | [Name] | [Tier] | [count] | [count] | [1-line] |
```

### 5. Convert to Skills (Optional)

If the user wants to proceed to skill creation:
- Run `/extract` Step 4+ for each extraction (workflow planning checkpoint)
- Or batch convert: `python execution/skill_converter.py`

## Limits

- **Max 5 parallel extractions** (context and API limits)
- Each sub-agent operates independently — no communication between them
- If one fails, others continue unaffected
