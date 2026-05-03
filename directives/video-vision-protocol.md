# Video Vision Protocol

## Purpose

Automatically inject **visual context** (frame extractions + grounded transcripts) into any workflow that ingests video source material — without depending on the AI assistant remembering to invoke `/watch` or any other slash command.

**Why this exists.** Skill files distill expert thinking into frameworks. Transcripts preserve the words. But ~30-50% of meaning in modern video — especially short-form, screen-recorded, or on-camera teaching — lives in the **visual channel**: hooks-as-cuts, B-roll patterns, on-screen text, gesture, energy, slide content, product demonstrations. Transcript-only ingestion has a hard ceiling on how well any extraction or analysis can capture a visual creator.

**Why deterministic-wrapper-not-slash-command.** Per `feedback_ai-memory-dependent-observability.md` (2026-05-03 — banned pattern), any infrastructure that requires Claude to manually invoke a CLI for it to fire will go silent within 24 hours. Recall grounding observability proved this empirically. Workflows must call `execution/fetch-video-context.py` from `// turbo` blocks; the slash command `/watch` exists for interactive use only.

---

## Trigger — automatic, every video-source workflow

Visual capture fires when **all** of the following are true:

1. The workflow's source material is a video URL or local video file (auto-detected by `is_video_source()` in the wrapper)
2. The workflow appears in the integration table below
3. Not suppressed by `--no-vision` flag

**Does NOT fire for:** pasted transcripts, article URLs, local text files, code, images alone, or any source the wrapper classifies as non-video.

---

## Wrapper contract — `execution/fetch-video-context.py`

```bash
python3 execution/fetch-video-context.py <source> [expert_name] [options]
```

### Exit codes (workflows MUST branch on these)

| Code | Meaning | Workflow action |
|---|---|---|
| `0` | OK — `extractions/<expert>/visual-context.md` is ready | Load alongside transcript |
| `2` | SKIPPED — non-video source, >10min, `--no-vision`, uncaptioned-no-Whisper-key, plugin not installed | Continue with transcript-only flow |
| `1` | FAILED — system dep missing, network failure, plugin error | Log warning, continue with transcript-only flow |

**Critical**: A non-zero exit code from the wrapper NEVER blocks the parent workflow. Visual context is additive; transcript-only is always the fall-through path.

### Standard workflow invocation pattern

```bash
# // turbo
python3 execution/fetch-video-context.py "<source>" "<expert-name>" || true

if [ -f "extractions/<expert-name>/visual-context.md" ]; then
    echo "→ Visual context available — load alongside transcript"
fi
```

### Options

| Flag | Purpose |
|---|---|
| `--max-frames N` | Override frame budget (default: claude-video chooses by duration) |
| `--max-duration SEC` | Override 600s (10min) skip threshold |
| `--no-vision` | Force SKIP — for testing transcript-only flow |
| `--force` | Re-fetch even if `visual-context.md` cached |
| `--whisper` | Allow Whisper API fallback when no native captions (requires `GROQ_API_KEY`) |

---

## Storage convention

```
extractions/<expert>/
├── transcript.txt            # existing — UNCHANGED
├── extraction-report.md      # existing — UNCHANGED
├── visual-context.md         # NEW — markdown report (frame paths + timestamped transcript + visual notes)
└── frames/                   # NEW — gitignored, ~10MB typical
    ├── frame_000.jpg
    └── ...
```

`frames/` and `visual-context.md` are gitignored — both are regenerable from the source URL. The committed artifact remains `extraction-report.md`, which now references visual-context.md when present.

---

## Integration table — which workflows fire visual capture

### Tier 1 — Extract family (mandatory)

| Workflow | Trigger point | Notes |
|---|---|---|
| `extract.md` | Phase 1.6, after transcript fetch | Insert before expert ID step |
| `extract-forge.md` | Phase 1, alongside transcript fetch | Parallel to fetch-transcript |
| `parallel-extract.md` | Step 2, parallel batch | Fire alongside parallel transcripts |
| `extract-vision.md` | Step 1 prologue | Load visual-context.md for vision questions |
| `extract-amplify.md` | Source-loading step | Reference visual-context.md if present |
| `convert-extraction.md` | Step 1 audit | Surface visual-context.md to workflow generation |
| `extract-principle.md` | Inputs step | Add visual-context.md to inputs |
| `sinem-50-notes-extract.md` | Source ingestion | Standard wrapper invocation |

### Tier 2 — Video-study workflows (high-value)

| Workflow | Why it benefits |
|---|---|
| `watch-and-remix.md` | Entire purpose is studying viral video — visual hooks are 50% of what makes videos viral |
| `lookalike-content.md` | Finding viral content in niche — visual hook patterns matter |
| `format-scan.md` | Format trends are inherently visual |
| `hidden-gems.md` | Tone/energy signal needs visual |
| `style-from-creator.md` | Voice/structure includes gesture, pacing, energy |
| `hook-formula-extract.md` | Visual hook patterns (cuts, B-roll, on-screen text) |
| `talking-points.md` | Slide content + demonstrations |

### Tier 3 — Cross-cutting (when source is video)

| Workflow | Trigger condition |
|---|---|
| `4c-architect.md` | YouTube URL provided |
| `atomize.md` | Video source for atomization |
| `knowledge-alchemy.md` | Video knowledge ingestion |
| `mcclain-source-to-agent.md` | Persona engineering benefits from visual mannerisms |
| `art-direct.md` | Reference is video URL |
| `mood-board.md` | Video reference for mood |
| `storyboard.md` | Video reference for keyframes |
| `parallax.md` | Phase 2.5 zeitgeist scan when reference is video clip |

---

## Failure modes — all handled by silent skip-and-continue

| Condition | Wrapper behavior | Parent workflow |
|---|---|---|
| Plugin not installed | Exit 1 with `hint=run: /plugin install...` | Log warning, transcript-only |
| `ffmpeg`/`ffprobe`/`yt-dlp` missing | Exit 1 with `hint=brew install...` | Log warning, transcript-only |
| Source is not a video | Exit 2 silent | Transcript flow continues |
| Video > 10 min | Exit 2 with `reason=duration_exceeds_cap` | Transcript flow continues |
| Uncaptioned video, no `GROQ_API_KEY` | Exit 2 with `reason=uncaptioned_no_whisper_key` | Transcript flow continues |
| Network/yt-dlp failure | Exit 1 with stderr tail | Log warning, transcript-only |
| Cached (visual-context.md exists) | Exit 0 immediate, prints path | Load existing visual-context.md |

---

## Logging — `.agent/video-vision-log.jsonl`

Every invocation appends a JSON line:

```json
{
  "timestamp": "2026-05-03T18:51:39.111054+00:00",
  "status": "OK|SKIPPED|FAILED",
  "source": "https://...",
  "expert_name": "brad-bonanno",
  "reason": "...",
  "duration_sec": 187,
  "frames": 60,
  "elapsed_sec": 23.4
}
```

The log is gitignored (high-churn). Use it to:
- Debug failures on a specific source
- Audit which extractions had visual context vs transcript-only
- Future: correlate visual-context presence with Expert Standard score lift

### Audit query patterns

```bash
# Last 10 invocations
tail -10 .agent/video-vision-log.jsonl | jq .

# All FAILED events from last 7 days
jq -c 'select(.status == "FAILED")' .agent/video-vision-log.jsonl | tail -20

# Count by status
jq -r .status .agent/video-vision-log.jsonl | sort | uniq -c
```

---

## Backward compatibility safeguards

1. **Default-skip for non-video sources.** Pasted transcripts, article URLs, text files all flow exactly as before. Wrapper exits 2 silently.
2. **Default-skip for >10min videos.** Per claude-video's own constraint (frame budget gets too sparse). Wrapper logs and skips; parent continues.
3. **Default-skip when Whisper would be needed but no key configured.** No silent API spend.
4. **Idempotent.** Re-running a workflow on an existing expert dir doesn't re-fetch frames if `visual-context.md` exists. Pass `--force` to override.
5. **Failure never blocks.** Wrapper exit codes propagate as warnings, not errors.
6. **Existing extractions untouched.** Pre-2026-05-03 extractions continue to work — they just don't have a visual-context.md sidecar.

---

## Manual overrides

Usable in any workflow invocation or user message:

| Flag | Effect |
|---|---|
| `--no-vision` | Skip visual capture for this run (testing transcript-only flow) |
| `--force` | Re-fetch even if cached |
| `--max-duration 1200` | Allow up to 20-min videos (override 10-min cap) |
| `--whisper` | Activate Whisper fallback for uncaptioned sources |

---

## Disk hygiene

Frames are gitignored but accumulate locally. Recommended monthly cleanup:

```bash
find extractions -path '*/frames/*' -mtime +30 -delete
```

Or selective re-fetch with `--force` if a creator is still being actively studied.

---

## Relationship to other protocols

| Protocol | Interaction |
|---|---|
| `recall-grounding-protocol.md` | Recall fires at Tier 1.5 (skill load); video-vision fires at source-ingestion. Independent stages. |
| `agent-loading-protocol.md` | Visual context is loaded as part of source material before skill files |
| `content_creation_gate.md` | Content tasks that reference video sources benefit from visual context |
| `quality_gate.md` (Step 6) | Expert Standard scoring should credit visual-grounded outputs as positive signal — same as Recall grounding |
| `verification-agent-protocol.md` | Visual context provides primary-source frames for fact verification (e.g., "Madeon set" claim → cite the actual frame) |

---

## First-90-days evaluation criteria

After 30 extractions where video-vision fired:

- Did Expert Standard scores rise vs. baseline (pre-vision median ≈ 7) for visual creators specifically?
- Were there cases where visual context introduced factual errors? (if yes → tighten frame budget or duration cap)
- Which expert domains benefited most? (visual-heavy creators like Brad Bonanno, Jun Yuh, on-camera Lara Acosta vs. text-heavy creators)
- Did the Parallax Phase 2.5 fabrication failure mode actually go away?

Re-evaluate protocol tuning after that checkpoint.

---

## Plugin contract — what we depend on from claude-video

Pinned expectations (as of v0.1.2 / 2026-05-03):

- Entry point: `<plugin>/scripts/watch.py`
- Args: positional `<source>`, `--out-dir`, `--no-whisper`, `--max-frames`, `--resolution`, `--fps`, `--start`, `--end`, `--whisper {groq,openai}`
- Output: markdown report file in output dir + frame JPEGs

If a future plugin update breaks any of these, the wrapper will:
- Exit 1 with `reason=watch_py_nonzero` and stderr tail in the log
- Surface the breakage in `.agent/video-vision-log.jsonl`
- Allow the integration to be temporarily disabled by uninstalling the plugin (wrapper falls back to plugin_not_installed → exit 1, all workflows continue with transcript-only)

Pin the plugin to a known-good SHA in CI if drift becomes a problem:
```bash
ls ~/.claude/plugins/cache/*/watch/  # see installed SHAs
```
