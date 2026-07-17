---
description: End-to-end enriched extraction
tier: system
---

# /extract-forge — The Master Extraction Pipeline

The complete enriched extraction from source material to fully deployed mastery-level skill. Combines `/extract-vision` + `/extract` + `/extract-amplify` into a single pipeline that produces 8-15 practitioner-grade workflows — the Wright Thompson / Eric Roth standard.

This is the "do it all" command. One invocation, one conversation, one complete skill.

## Usage

```
/extract-forge [source material — YouTube URL, transcript, file, or pasted content]
```

## When to Use

- Source material is RICH (8,000+ words, deep methodology, multiple distinct techniques)
- The expert is in a domain critical to Farrice's business (writing, persuasion, brand, content psychology)
- You want mastery-level depth — not a quick 3-workflow capture
- This is an expert you'll reference repeatedly across multiple projects

## When NOT to Use

- Light sources (< 5,000 words) — use standard `/extract`
- Niche experts with narrow scope — standard extract is sufficient
- Time-constrained — forge takes a full session; standard extract is faster
- You just want to explore whether an expert is worth extracting — start with `/extract`, amplify later

## Pipeline

### Phase 0: Claim the Tree (mandatory — merge-discipline.md Law 0, Wave 0 2026-07-17)

A forge is a full-session multi-file build — exactly the shape the 2026-07-15 forge race
corrupted. Before anything else:

```bash
python3 execution/session_lock.py claim "extract-forge: <expert-name>"
```

BLOCKED (fresh foreign lock) = do not forge; coordinate with Farrice or move to a
worktree. Heartbeat the printed token between phases; release at Phase 8.

### Phase 1: Source Acquisition

1. **If YouTube URL**: Fetch transcript AND visual context **in parallel**
```bash
// turbo
python3 execution/fetch-transcript.py "<url>" "<expert-name>" &
python3 execution/fetch-video-context.py "<url>" "<expert-name>" || true &
wait
```

Visual context (frame extraction + grounded transcript) is additive — auto-skips non-video sources, >10min videos, uncaptioned-no-Whisper-key, or plugin-not-installed. See [`directives/video-vision-protocol.md`](../../directives/video-vision-protocol.md). For mastery-level extraction (forge), visual context is critical for visual creators (on-camera teachers, screen-recordings, slide-heavy content).

2. **Expert identification** (same as `/extract` Step 1.5):
   - Verify the actual expert (not the transcription tool)
   - Check `AGENT_INDEX.md` for existing agents
   - If expert exists, this becomes an EXPANSION, not a new extraction

3. **Read the full source material**. Do NOT skim. Forge requires complete comprehension. If `extractions/<expert-name>/visual-context.md` exists, **read it alongside the transcript** — it contains frame paths and visual notes Claude can reason over directly via the `Read` tool, and forge-tier extraction must capture visual genius patterns when present.

### Phase 2: Vision (from `/extract-vision`)

Run the vision process — but with creative latitude defaulting to **3 (Autonomous)** and depth defaulting to **Mastery (10-15)**. If Farrice provides direction, honor it. If not, the system drives.

**Abbreviated vision process:**

1. **If Farrice gave context** alongside the forge command, extract his creative direction from it. Don't re-ask what's already been answered.

2. **Run the leverage analysis** autonomously:
   - Uniqueness Audit (what does this expert do that no one else in the roster does?)
   - Business Leverage Map (deployability × differentiation matrix)
   - Cross-Expert Stacking Map (technique × expert = compound output)
   - Gap Fill Analysis (what capability this adds to the roster)

3. **Produce the Vision Document** — present as checkpoint. Wait for approval.

### Phase 3: Deep Extraction

Run the full MES 3.0 extraction (`directives/mes-3.0-extract.md`) at **Deep tier**:

1. Read and execute `directives/mes-3.0-extract.md`
2. Force Deep tier regardless of source length
3. Produce:
   - Genius patterns (aim for 10+)
   - Hidden knowledge
   - Hall of Fame Exemplars (minimum 3)
   - Signature Moves (minimum 5)
   - Quality Rubric (7+ criteria)

### Phase 4: Architecture Design

This is where forge diverges from standard extract. Instead of proposing 3-5 workflows, design the full skill architecture:

1. **Core Files Design**:
   - `genius.md` — unified genius context
   - `SKILL.md` — skill manifest with workflow table, stacking guide
   - `references/` — what reference documents are needed? (cross-domain patterns, source quotes, frameworks)

2. **Workflow Planning** — aim for 8-15 workflows organized in tiers:

   **Tier 1 — Foundation Workflows** (the 3-4 workflows that capture the expert's core methodology):
   - These are the "if you had only 3 tools" workflows
   - Every extraction has these

   **Tier 2 — Practitioner Workflows** (3-5 workflows for granular deployment):
   - Specific techniques that deserve their own slash command
   - Content-type specific applications
   - Diagnostic/audit tools

   **Tier 3 — Stacking Workflows** (2-4 workflows that explicitly pair with other experts):
   - Cross-expert chains
   - Creative applications outside the expert's obvious domain
   - System-level applications

3. **Present the architecture** — full workflow table with names, descriptions, tier assignments, and stacking partners. Wait for approval.

### Phase 5: Build

Execute the full build:

1. **Create directory structure**:
```bash
// turbo
mkdir -p skills/[skill-name]/workflows skills/[skill-name]/references agents/[expert-name]/memory
```

2. **Write `genius.md`** — unified genius context with all patterns, hidden knowledge, exemplars, signature moves, and quality rubric

3. **Write reference files** — cross-domain patterns, source quotes, frameworks (as needed based on architecture design)

4. **Write all workflows** — each workflow MUST include:
   - YAML frontmatter with description
   - Pre-Flight Gate (reference genius.md decision framework)
   - Skill Acquisition (what to load)
   - Execution steps (the actual methodology)
   - Content Type Adaptations table
   - Output Requirements
   - Quality Gate (reference genius.md anti-patterns)

5. **Write `SKILL.md`** — skill manifest with:
   - Workflow table organized by tier
   - Stacking guide (which workflows pair with which experts)
   - Quick reference

### Phase 5.5: Forge Execution Prompts (MANDATORY — spec: `directives/prompt-forging-spec.md`)

One **born-v2 structure-pure prompt** per distinct deliverable (typically 4-10), written to
`skills/[skill-name]/references/prompts-v2/`: Role & Activation (real credentials only), Input
Required `[BRACKET]`s, Execution Protocol at full depth FROM THE EXTRACTED MATERIAL (never
training memory — see the transcript-only-extraction solution card), Output Contract, Output
Skeleton (placeholders only), Quality Gate, Deploy When. Fidelity rule applies: thin source →
fewer/deeper prompts, flag `fidelity: low`, never invent.

Then wire (all four, non-optional):
1. `python3 execution/renaissance_audit.py` → 0 fail
2. `python3 execution/prompt_library.py build`
3. `python3 execution/wire_prompt_pointers.py --write`
4. `Execution prompt: references/prompts-v2/<file>.md` line under each workflow's output step

### Phase 6: Registration

1. **Create agent file**: `agents/[expert-name]/AGENT.md` (expansion if the expert already exists)
2. **Create slash command wrappers**: One `.agent/workflows/[prefix]-[name].md` per workflow
3. **Run the generators** (never hand-edit the registries) — refreshes `AGENT_INDEX.md` + `SKILL_INDEX.md`, mints the per-skill shim, creates/refreshes the **expert front-door command** (`/[expert-name]` = persona + full arsenal, tier-gated), and rebuilds the menu:

```bash
// turbo
python3 execution/sync_registries.py
python3 execution/generate_slash_commands.py
```

### Phase 7: Verification

1. **Structural check**: Confirm all files exist
2. **Content quality spot-check**: Read 2-3 workflows for practitioner-grade quality
3. **Slash command check**: Confirm wrappers correctly reference full workflows; confirm `.claude/commands/[expert-name].md` front door lists the new skill AND the new commands appear in `SLASH_COMMANDS.md` (fireable-but-not-in-menu = registration failure)
4. **Embodiment + blind-pass check** (`directives/embodiment-standard.md` — instrumented, Wave 2). Run this exact sequence:

   ```bash
   # 4a. Corpus gate — ≥2 real published pieces in extractions/[skill-dir]/reference-corpus/
   #     (exit 1 prints exactly what to collect)
   python3 execution/blind_pass.py prepare --expert [skill-dir]
   ```

   4b. **Side-by-side judgment** (human/model — never automated): 1-2 Tier-1 workflow outputs beside the reference-corpus pieces, judged against the recognition test. PASS = indistinguishable or preferred; A-tier promotion requires a Farrice-judged pass; FAIL → fix weakest checklist item, retry once, else ship B-tier with the gap named.

   ```bash
   # 4c. Record — appends the eval_set_v1.jsonl entry + extractions/[skill-dir]/blind-pass-log.md line
   python3 execution/blind_pass.py record --expert [skill-dir] --verdict PASS|FAIL \
       --notes "[which real pieces, what held / what gave it away]" \
       --generated [path] --reference [path]
   ```

5. **Heartbeat gate** (replaces the prose "REQUIRED before ship" pointer — 6 tier-affecting checks from `directives/skill-craft-standard.md` §8):

   ```bash
   # ≥2 failures = tier capped at B (exit 1). Fix the named checks or ship with the gap named.
   python3 execution/skill_auditor.py check --skill [skill-dir]
   ```

### Phase 8: Performance Log

Scores are NOT templated — derive them from the Phase 7.4 blind-pass verdict + checklist coverage (`directives/embodiment-standard.md` § Scoring Discipline). Any dimension ≥8 requires `--anchor-named "<anchor phrase>"` (the matching rubric_v1.md anchor as a string — finalize refuses unanchored ≥8s). Finalize also refuses `--type Extraction` without the Phase-7.4c recorded verdict (`--skip-blind-pass` is the logged override).

```bash
python3 execution/chain_runner.py finalize "[Expert] — [Domain] mastery extraction (forge)" \
    --expert [expert-name] --skill [skill-dir] --workflow extract-forge \
    --type Extraction --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --anchor-named "[rubric anchor phrase, required for any ≥8]" \
    --notes "[workflow count] workflows, [genius pattern count] patterns | blind-pass: [PASS/FAIL vs which real pieces] | heartbeat: [n/6]"
```

Then register the extraction for usage telemetry (informational only — feeds the monthly production-use report, never blocks):

```bash
// turbo
python3 execution/forge_gate.py record [skill-dir] --expert [expert-name]
```

---

## Checkpoints (3 total)

| # | After Phase | What You Approve |
|---|-------------|-----------------|
| 1 | Phase 2 (Vision) | Extraction Vision Document — creative direction + leverage analysis |
| 2 | Phase 4 (Architecture) | Full workflow table with tier assignments and stacking partners |
| 3 | Phase 7 (Verification) | Sample workflow review + structural verification |

## Forge vs. Standard Extract

| Dimension | `/extract` | `/extract-forge` |
|-----------|-----------|-----------------|
| Workflows | 3-5 | 8-15 |
| Extraction tier | Auto (Light/Standard/Deep) | Always Deep |
| Vision step | None | Built in |
| Amplification | None (run `/extract-amplify` separately) | Built in |
| Reference files | Optional | Standard (cross-domain patterns, frameworks) |
| Content-type adaptations | Optional | Mandatory per workflow |
| Cross-expert stacking | Not addressed | Explicit stacking guide |
| Checkpoints | 2 | 3 |
| Session time | 30-60 min | Full session (2-4 hours) |

## Pairs With

- `/extract-amplify` — use post-forge if you STILL want more (rare, but possible with very rich sources)
- `/extract-vision` — forge has vision built in; use vision standalone when you're not ready for the full forge
