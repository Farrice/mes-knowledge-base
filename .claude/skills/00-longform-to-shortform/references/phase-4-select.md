# Phase 4: SELECT

Reference: `.claude/skills/vid-clip-selection/SKILL.md` (phases 1-4 only, skip Phase 5 human review)

```bash
PHASE_START=$(date +%s)
```

1. Read the SRT transcript
2. Identify candidate clips using the 5-category scoring framework:
   - **Hook Strength** (0-20): Does it grab attention in first 3 seconds?
   - **Standalone Value** (0-25): Does it make sense without context?
   - **Emotional Resonance** (0-20): Does it provoke reaction?
   - **Information Density** (0-20): Insight-per-second ratio
   - **Shareability** (0-15): Would someone share this?
3. Score each candidate (total out of 100)
4. Respect `duration_range` from config for clip boundaries
5. Write `{run_dir}/clip_candidates.json`:

```json
[
  {
    "id": 1,
    "title": "descriptive-clip-title",
    "start_time": "00:05:23",
    "end_time": "00:06:48",
    "start_sec": 323.0,
    "end_sec": 408.0,
    "duration_seconds": 85,
    "scores": {
      "hook_strength": 18,
      "standalone_value": 22,
      "emotional_resonance": 16,
      "information_density": 18,
      "shareability": 12
    },
    "total_score": 86,
    "hook_line": "Short, compelling hook derived from the video title",
    "summary": "Brief description of the clip content"
  }
]
```

**Timestamp rules:**
- `start_time` / `end_time` are HH:MM:SS for readability in logs and reports
- `start_sec` / `end_sec` are **float seconds** — these are what downstream phases consume
- Always include both. Convert HH:MM:SS → seconds: `H*3600 + M*60 + S`
- `duration_seconds` must equal `end_sec - start_sec` (rounded)

**Hook line generation:** The `hook_line` must NOT be a transcript excerpt. Read the video title from `{run_dir}/run-metadata.json` (field: `title`). Generate a compelling, short hook (3-8 words) derived from the video title and the clip's specific content. The hook should work as a title card that draws the viewer in. Examples:
- Video title "Creating Your Own Agentic OS Is Easy", clip about skill creation -> hook: "Creating Your Own Agentic OS"
- Video title "Anthropic's Boris Cherny on Sequoia" -> hook: "Anthropic's Boris Cherny on Sequoia"
- If the video title itself is punchy and short (under 8 words), use it directly as the hook for the highest-scoring clip. Other clips can use shorter derivatives of the title.

If the `hook_line` appears to be a full transcript sentence (contains verbs, reads like speech), it is wrong — rewrite it as a title-card style hook.

## Exclusion Patterns

Before scoring, scan the transcript for outro/CTA segments and exclude them from clip candidates:

**Outro trigger phrases** (case-insensitive):
- "subscribe", "make sure you subscribe"
- "see you in the next one", "see you in the next video"
- "let me know below", "let me know in the comments"
- "thanks for watching", "thank you for watching"
- "hit the bell", "hit that bell"
- "if you haven't already"

**Rules:**
1. Mark the earliest outro trigger as `outro_start_sec`
2. If a clip candidate's `end_sec` falls within or after the outro segment, truncate `end_sec` to `outro_start_sec - 2.0` (leave 2s buffer)
3. If truncation drops duration below `min_duration` from config, extend `start_sec` earlier to compensate
4. If the clip still can't meet `min_duration` after extending start, discard it
5. Never include outro/CTA speech in a clip — it breaks standalone value

```bash
PHASE_END=$(date +%s)
echo "Phase 4 SELECT: $((PHASE_END - PHASE_START))s" >> "$RUN_DIR/phase-timings.txt"
```
