# Workflow: Kling Multi-Shot Narrative Video

> **Use**: Generate multi-scene narrative videos (brand trailers, product launch sequences, narrative ads) with distinct shots
> **Model**: Kling v3 Pro (only model that supports `multi_prompt`)
> **Default config**: 12s total, 3 shots × ~4s each, audio on
> **Cost**: 12s × $0.168 = $2.02 — **EXCEEDS $2 ceiling** → use 11s ($1.85) or audio off ($1.34)

## Concept

Kling v3 Pro accepts a `multi_prompt` array — each entry defines one shot's prompt, and Kling distributes the total duration across them, generating natural cuts between shots. Unlike Seedance (single-shot only), this lets you tell a 3-act story in one generation.

## When to Use

- Brand campaign trailers (3 acts: world / disruption / resolve)
- Product launch sequences (problem / product reveal / outcome)
- Narrative ads (setup / twist / payoff)
- Storyboard-driven content where multiple beats matter

**Don't use for**: single-action shots (use Kling single-prompt or Seedance), or anything requiring lipsync/character speech (Seedance handles audio better).

## Standard Run

### Step 1: Author the multi-prompt JSON

Create a file like `skills/fantastic-posters/templates/kling-shots-example.json`:

```json
[
  {"prompt": "Wide shot: empty warehouse at dawn, dust drifts through shafts of light from high windows, anticipation"},
  {"prompt": "Medium shot: crowd of figures arrives silhouetted against the open warehouse door, cinematic backlight"},
  {"prompt": "Close-up: hands raise in unison as bass drops, neon strobes pulse, faces lit in magenta and cyan, exhale"}
]
```

### Step 2: Pre-flight + run

```bash
# 11s × audio on = $1.85, within $2 ceiling
python3 execution/fal_budget_guard.py check --mode=kling --duration=11 --audio=on
# Estimated: $1.848

python3 execution/fal_video_kling.py \
    --multi-prompt skills/fantastic-posters/templates/kling-shots-example.json \
    --start-image "<your-poster-as-opening-frame>.png" \
    --duration 11 --audio on

# Log
python3 execution/fal_budget_guard.py log --mode=kling --duration=11 --audio=on \
    --status=success --actual-cost=1.848 \
    --brief="3-shot warehouse rave trailer"
```

## Custom Elements (Character / Object Consistency)

Kling supports `--elements` to lock characters or objects across shots — pass image references or video clips that should appear consistently. Reference them in prompts as `@Element1`, `@Element2`, etc.

Element JSON shape:
```json
[
  {
    "reference_image_urls": ["https://.../mybpm-mascot-back.png"],
    "frontal_image_url": "https://.../mybpm-mascot-front.png"
  },
  {
    "video_url": "https://.../existing-mascot-clip.mp4"
  }
]
```

Then in your prompt: `"@Element1 walks across the dance floor, the crowd parts around them"`.

**Cost note**: Elements don't change pricing. Same per-second rate.

## Cost Reference (within $2 ceiling)

| Duration | Audio off | Audio on | Voice control |
|---|---|---|---|
| 3s | $0.34 | $0.50 | $0.59 |
| 5s | $0.56 | $0.84 | $0.98 |
| 8s | $0.90 | $1.34 | $1.57 |
| 10s | $1.12 | $1.68 | $1.96 |
| 11s | $1.23 | $1.85 | **BLOCKED** ($2.16) |
| 12s | $1.34 | **BLOCKED** ($2.02) | **BLOCKED** ($2.35) |
| 15s | $1.68 | **BLOCKED** ($2.52) | **BLOCKED** ($2.94) |

**Rule of thumb**: For multi-shot, max practical config is 11s × audio on (3 shots × ~3.7s each). For longer, drop audio.

## Anti-Patterns

- ❌ **3+ shots in 5s.** Each shot needs ~3-4 seconds to land. 3 shots ÷ 5s = 1.7s per shot = unwatchable. Use 9-11s minimum for multi-shot.
- ❌ **More than 4 shots.** Kling can technically handle more but coherence degrades. 2-4 shots is the sweet spot.
- ❌ **Single-action prompts in multi_prompt.** If shots are too similar, the cuts feel arbitrary. Make each shot a distinct *moment*.
- ✅ **Author shots like a 3-act trailer.** World → disruption → resolve. Or setup → reveal → consequence.

## Output Schema

Each multi-shot run produces one **Shot Record**:

```markdown
## Kling Multi-Shot — <project/campaign>
- Shots (multi_prompt array): [N] entries, each one distinct moment (not a variation of the last)
- Duration / audio: <Ns> · <off|on|voice_control> — verified within $2 ceiling (table above)
- Elements used: [none | @Element1: <ref>, @Element2: <ref>]
- Pre-flight: `fal_budget_guard.py check --mode=kling --duration=<N> --audio=<mode>` → estimated $<n>
- Output file: `skills/fantastic-posters/out/<model>_<duration>s_<timestamp>.mp4`
- Post-flight log: `fal_budget_guard.py log --mode=kling --duration=<N> --audio=<mode> --status=success --actual-cost=<n> --brief="<one line>"` ✓
```

Complete only when shot count matches the table's per-shot-second rule (≥3-4s/shot) and the log's `--actual-cost` matches the pre-flight estimate.

## Quality Gate

- [ ] **Duration + audio combo stays under the $2 ceiling** — checked against the Cost Reference table, not assumed.
- [ ] **Each shot is a distinct moment** — 2-4 shots, not near-duplicate prompts; a spread that reads the same with the sound off fails.
- [ ] **Seconds-per-shot ≥ 3-4s** — 3 shots in 5s (1.7s/shot) is the named unwatchable failure; use 9-11s minimum for multi-shot.
- [ ] **Elements referenced correctly** — `@Element1`/`@Element2` used in prompts only when the elements JSON actually defines them.
- [ ] **Pre-flight ran, log ran with real `--actual-cost`** — not the estimate copy-pasted if the actual differs.

**Pass criteria**: all checked. A multi-shot render that "looks cinematic" but crams 4 shots into 5s fails the pacing gate regardless of visual quality.
