---
name: "The Pause Test Audit"
produces: "Frame-by-frame audit of an existing video draft, scoring each pause-point and prescribing rewrites"
expert: "Brad Bonanno"
load_context: "genius.md"
---

# Brad Bonanno — The Pause Test Audit

## Role

Pre-publish diagnostic for any explainer video draft. Takes a video URL or local file, applies frame-grounded vision (via `execution/fetch-video-context.py`), and scores every 5-second pause-point on whether a paused viewer would get value. Outputs a structural rewrite prescription.

**Before executing**: Read [genius.md](../genius.md) for full extraction intelligence — especially Pattern 1 (15% Demo Rule), HK1 (Talking-head as parasocial trust), HK4 (Pause Test as KPI), and the 7-criterion Quality Rubric.

## Input Required

1. **Video source** — URL (YouTube/Vimeo/Loom/etc.) or local video path. Must be ≤10 minutes for tight audit; longer videos work but frame budget gets sparse.
2. **Creator's positioning** — 1-2 sentences on what the video is selling (a tool, a methodology, a service). Determines what counts as "value-delivering" pause-frames.
3. **Target audience** — Who's the viewer? What's their skepticism level? (Determines which objections need pre-empting per Pattern 5.)
4. **Channel goal** — Standalone evergreen video, OR part of a compound cliffhanger architecture? (Determines whether Pattern 6 audit applies.)

## Workflow

### Phase 1 — Fetch Visual Context

```bash
// turbo
python3 execution/fetch-video-context.py "<video-url-or-path>" "audit-<slug>" || true
```

Wait for `extractions/audit-<slug>/visual-context.md` to materialize. If wrapper exits 2 (SKIPPED for >10min or non-video), prompt user to either confirm `--max-duration` override or pivot to text-based script audit (lower fidelity).

### Phase 2 — Build the Frame-by-Frame Modality Map

Read `extractions/audit-<slug>/visual-context.md` to get the frame index. Then `Read` each frame at the timestamps below:
- Every 5th frame (covers ~5-second intervals at default 0.155 fps for 5-10min videos)
- All frames within 10 seconds of major topic transitions (mentioned in transcript)
- Opening 3 frames (hook + thumbnail validation)
- Closing 3 frames (cliffhanger / CTA validation)

For each frame read, classify into one of 4 modalities:

| Modality | What it looks like | What it does |
|---|---|---|
| **Talking-head (TH)** | Creator on camera, looking at lens, mid-speech | Parasocial trust |
| **Demo (D)** | Screen recording, UI, terminal, dashboard | Show-don't-tell |
| **Infographic (IG)** | Branded graphic with icons + labels + numbers | Trust anchor |
| **Dead (X)** | Transitions, outros, blank, low-engagement | NEGATIVE — fails Pause Test |

Build the modality map:

```
00:00 (frame 1)  TH  — Hook frame, mouth open, hand raised  ✓ thumbnail-grade
00:30 (frame 5)  TH  — Mid-explanation                       ✓
01:00 (frame 10) D   — Split-screen demo, source on left     ✓ Matrix Moment
01:30 (frame 15) TH  — Returns to talking-head explanation   ✓
...
```

### Phase 3 — Compute the 7 Quality Rubric Scores

Apply the rubric from genius.md Section "Quality Rubric." For each criterion:

1. **Modality Mix Discipline**: Count TH / D / IG / X. Target: 70-80% / 10-20% / 5-15% / 0%. Score 1-5.
2. **Pause Test**: Count X frames. 0% X = score 5. 5-10% X = score 3. >20% X = score 1.
3. **Single-Source Demo Discipline**: Count distinct demo sources. 1 source = score 5. 4+ sources = score 1.
4. **Pre-empted Objections**: Scan transcript for "you're probably thinking..." / "I can hear..." / "but wait..." patterns. Count. 2+ with infographic-anchored proof = score 5.
5. **Trust-Anchor Infographic Count**: Count IG frames. 2-4 with consistent visual language = score 5.
6. **Compound Cliffhanger**: Final 60-90 seconds — does it tease a bigger promise tied to next video? Score 5 if yes with dashboard frame; score 1 if no.
7. **Bottom-Left PIP Discipline**: Audit demo frames — is creator's webcam bottom-left, smaller than demo? Score 5 if consistent; 1 if face dominates.

### Phase 4 — Identify Top 3 Structural Failures

Surface the 3 highest-leverage rewrites. Format each:

```markdown
### Failure N: [Pattern Name]

**Where**: timestamp + frame number
**What's broken**: [specific evidence]
**Why it matters**: [which pattern from genius.md is violated]
**Prescription**: [exact rewrite — script change, B-roll insert, infographic to add, demo cut to remove]
**Estimated impact**: [retention lift / pause-value lift / shareability lift]
```

### Phase 5 — Deliver the Audit Report

```markdown
# Pause Test Audit: [Video Title]

**Source**: [URL]
**Duration**: [MM:SS]
**Audited against**: Brad Bonanno's 7-criterion rubric

## Scorecard
| Criterion | Score (1-5) | Evidence |
|---|---|---|
| 1. Modality Mix Discipline | X/5 | [TH/D/IG/X breakdown] |
| 2. Pause Test | X/5 | [X% dead frames] |
| 3. Single-Source Demo Discipline | X/5 | [N distinct sources] |
| 4. Pre-empted Objections | X/5 | [N objections + which had IG proof] |
| 5. Trust-Anchor Infographic Count | X/5 | [N infographics + visual consistency] |
| 6. Compound Cliffhanger | X/5 | [tease/handoff present?] |
| 7. Bottom-Left PIP Discipline | X/5 | [PIP audit across N demo frames] |
| **Total** | X/35 | [Pass = 25+, Top 10% = 30+] |

## Top 3 Structural Rewrites
[Per-failure prescription blocks from Phase 4]

## What's Working (preserve in rewrite)
- [3-5 bullets — the modality choices that already work]

## Re-audit trigger
Re-run this workflow after the rewrite. Acceptable threshold: ≥25/35 with no individual criterion below 3.
```

## Output Schema

```yaml
audit_report:
  video_source: string (URL or path)
  video_title: string
  duration_seconds: int
  total_score: int (0-35)
  pass_threshold_met: bool (>=25)
  top_decile: bool (>=30)
  scorecard:
    modality_mix: int (1-5)
    pause_test: int (1-5)
    single_source_demo: int (1-5)
    preempted_objections: int (1-5)
    trust_anchor_infographics: int (1-5)
    compound_cliffhanger: int (1-5)
    pip_discipline: int (1-5)
  modality_map:
    - timestamp: "MM:SS"
      frame_path: string
      modality: enum [TH, D, IG, X]
      notes: string
  top_3_rewrites:
    - failure_pattern: string
      timestamp: string
      evidence: string
      prescription: string
      estimated_impact: string
  preserved_strengths: array of strings
```

## Example Output

**Scenario**: A creator drafted a 6-minute YouTube tutorial on a new SaaS product. Wants pre-publish audit before launch.

```markdown
# Pause Test Audit: "How I Built My SaaS in 7 Days With Cursor"

**Source**: youtube.com/watch?v=example123
**Duration**: 5:48
**Audited against**: Brad Bonanno's 7-criterion rubric

## Scorecard
| Criterion | Score | Evidence |
|---|---|---|
| 1. Modality Mix Discipline | 2/5 | 95% screen recording (D), 5% TH, 0% IG. Pure-screen-recording mode. |
| 2. Pause Test | 2/5 | 22% of sampled frames are dead — long stretches of unchanged terminal output |
| 3. Single-Source Demo Discipline | 5/5 | Built one SaaS app throughout — disciplined |
| 4. Pre-empted Objections | 1/5 | No objections named or rebutted |
| 5. Trust-Anchor Infographic Count | 1/5 | Zero infographics. Cost claim ("under $50") hand-wavy with no chart |
| 6. Compound Cliffhanger | 3/5 | Mentions "I'll show how I scaled it" but no dashboard tease |
| 7. PIP Discipline | 4/5 | Webcam bottom-right (not bottom-left), but small and non-competing |
| **Total** | 18/35 | **FAIL — needs structural rewrite before publish** |

## Top 3 Structural Rewrites

### Failure 1: Pure-Screen-Recording Collapses Parasocial Layer
**Where**: 00:30 - 04:45 (no talking-head frames in 4-minute window)
**What's broken**: Creator's face appears only at 00:00-00:25 and 05:30-05:48. The middle 4 minutes are pure screen recording.
**Why it matters**: Violates Pattern 1 (15% Demo Rule) AND HK1 (parasocial trust accumulation). Without TH frames, viewer never builds the "I trust this person" feeling — every demo frame has to do double duty.
**Prescription**: Insert 4-6 talking-head cuts during the build sequence. Each ~10-15s. Use them at decision points ("Here's why I picked Stripe over Lemon Squeezy"). Total addition: ~60-90s of TH content.
**Estimated impact**: 25-40% retention lift in middle third (typical drop-off zone).

### Failure 2: Cost Claim Without Anchor
**Where**: 03:12 — "It cost me under $50 to build"
**What's broken**: Hand-wavy claim with no visual proof. Skeptical viewers (the SaaS-curious cohort) need numerical anchor.
**Why it matters**: Violates Pattern 4 (Branded Infographic Frames as Trust Anchors) and Pattern 5 (Pre-empt the Skeptic).
**Prescription**: Build a single branded infographic showing exact cost breakdown:
- Cursor Pro: $20/mo
- Vercel hosting: Free tier
- Domain: $12/yr
- Stripe: 0% setup
- Total month-1: $32
Insert as a 3-second cut at 03:15. Use clean white bg, consistent icons, exact numbers (not approximations).
**Estimated impact**: Pre-empts the "how much did this REALLY cost?" objection; chart becomes shareable.

### Failure 3: No Objection Pre-emption
**Where**: Whole video
**What's broken**: Zero "you're probably thinking..." beats. Viewer's strongest objections (vibe coding doesn't scale, AI-built code is fragile) go unaddressed.
**Why it matters**: Violates Pattern 5. Comments will be dominated by these objections.
**Prescription**: Insert 2 pre-emption beats:
1. ~02:00: "I can hear the engineers in the comments — 'this won't scale.' Here's the architecture..." → architecture diagram infographic
2. ~04:30: "And you're probably wondering — what about the AI hallucinating bugs? Let me show you the test suite..." → test coverage infographic
**Estimated impact**: 50-70% reduction in skeptical comments; comment thread skews constructive.

## What's Working
- Single-source demo discipline (one SaaS built throughout — viewer can track)
- PIP positioning (bottom-right is acceptable; small, non-competing)
- Closing CTA mentions next video
- Hook line at 00:00-00:08 is clean and grips

## Re-audit trigger
Re-run after rewrite. Target ≥25/35 with all criteria ≥3.
```

**What makes this excellent**: The audit doesn't just score — it prescribes specific timestamp-anchored rewrites with estimated impact. The creator can take this report and execute it in a single editing session. Each prescription cites the SPECIFIC pattern from genius.md being violated, so the creator learns the framework, not just the fixes.

## Quality Gate

Before delivering this audit, verify:

- [ ] All 7 criteria scored with evidence (not just numbers)
- [ ] Modality map covers at least 30% of frames (~24 frames for an 8-min video)
- [ ] Top 3 rewrites are timestamp-anchored AND pattern-anchored (cite genius.md pattern)
- [ ] Each rewrite has estimated impact (retention / pause-value / shareability)
- [ ] "What's Working" section is included — never a pure failure list
- [ ] Re-audit trigger specified

**Pass standard**: Could the creator execute this audit in a single session and produce a measurably better video? If yes, ship it. If no, the audit isn't tactical enough.
