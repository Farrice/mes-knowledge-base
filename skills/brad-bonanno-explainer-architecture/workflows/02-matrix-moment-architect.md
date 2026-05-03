---
name: "The Matrix Moment Architect"
produces: "Pre-recording demo strategy: source artifact, visual hierarchy, temporal proof beat, and shot list for 1-2 split-screen demo sequences"
expert: "Brad Bonanno"
load_context: "genius.md"
---

# Brad Bonanno — The Matrix Moment Architect

## Role

Generative pre-recording workflow. Designs the 1-2 split-screen demo sequences that will carry your video's "show, don't tell" weight — the moments that visually prove your tool/methodology's central claim. Outputs a complete demo brief: source artifact selection, visual hierarchy (PIP placement, screen layout), temporal proof beat structure, and a shot list ready to record.

**Before executing**: Read [genius.md](../genius.md) — especially Pattern 2 (Single Source Demo Discipline), Pattern 3 (The Matrix Moment Visual Setup), HK2 (Webcam PIP Position), HK5 (Same Source = Continuity), and Exemplar A (Sam Altman Matrix Moment).

## Input Required

1. **The thesis** — 1 sentence on what your video is selling. ("My tool watches video instantly." / "My methodology compresses 10 hours into 30 minutes." / "My agent does X while you watch.")
2. **The speed/efficiency claim** — Specifically, what time/effort gap does your tool/methodology create? ("8x faster" / "0.5 seconds vs. 5 minutes" / "instant vs. 2 weeks of manual work")
3. **Available demo artifacts** — What sources COULD you demo on? List 3-5 candidates (specific YouTube videos, specific UI flows, specific documents). The artifact selection happens in Phase 1.
4. **Recording constraints** — Single-take or multi-cut? Screen-recording software (Loom, ScreenFlow, OBS)? Webcam quality?
5. **Total demo budget** — How many seconds of demo content are you allocating? (Pattern 1 says ~10-20% of video; for an 8-min video, that's ~50-100 seconds of demo.)

## Workflow

### Phase 1 — Source Artifact Selection (Pattern 2 + HK5)

The single most important demo decision: which ONE flagship artifact runs across your entire video.

For each candidate, score on 5 axes (1-5):
| Axis | What scores high | What scores low |
|---|---|---|
| **Recognizability** | Audience instantly knows what it is (Sam Altman lecture, Stripe checkout, ChatGPT) | Obscure — viewer needs explanation before demo lands |
| **Visual richness** | Has visible structural elements (slides, UI, dashboard) | Plain text or audio-only |
| **Time-gap dramatizability** | Long enough that the speed claim has real punch (45-min lecture, 10-page doc) | Short — speed advantage feels trivial |
| **Continuity-ability** | Can plausibly appear in 3-5 demo cuts without becoming repetitive | One-shot only |
| **Emotional weight** | Audience CARES about this artifact (high-status, useful, relevant) | Boring or generic |

**Selection rule**: Pick the artifact with highest TOTAL score. If tied, prefer the one with highest **emotional weight** — emotional weight is what makes the demo land beyond "wow that's fast."

**Anti-pattern check**: If you find yourself picking 2+ artifacts to "show breadth," STOP. That's amateur creative cowardice. Commit to one. Pattern 2 is non-negotiable.

### Phase 2 — Visual Hierarchy Design (Pattern 3 + HK2)

Lock the canonical layout for every demo cut:

```
┌─────────────────────────┬─────────────────────────┐
│                         │                         │
│   SOURCE ARTIFACT       │   YOUR TOOL / OUTPUT   │
│   (left, dominant)      │   (right, dominant)     │
│   ~50% of frame         │   ~50% of frame         │
│                         │                         │
│                         │                         │
├─────────┐               │                         │
│ Webcam  │               │                         │
│ PIP     │               │                         │
│ (small) │               │                         │
└─────────┴───────────────┴─────────────────────────┘
```

**Locked rules**:
- **Source on LEFT, output on RIGHT** (Western reading order — viewer eye tracks L→R, follows the time arrow naturally)
- **Webcam PIP bottom-LEFT, smaller than demo content** (HK2 — face guides, doesn't compete)
- **Clean rounded card around PIP** if production budget allows
- **No labels overlaying the demo panes** — let visuals speak; if labels needed, place at top of each pane

**Recording specs**:
- Capture at 1280×720 minimum (1920×1080 preferred)
- Webcam at consistent crop ratio (typically 16:9 letterboxed)
- Background: same gray wall / consistent setup across all demo recordings (continuity)
- Lighting: soft front-key, no hard shadows on face

### Phase 3 — The Temporal Proof Beat Structure (Pattern 3)

The Matrix Moment isn't just a visual layout — it's a temporal proof structure. Design the time-difference reveal:

**Structure**:
1. **T₀ — Setup** (5-10s): Both panes are at neutral state. Source video paused, tool ready. Creator narrates: "I'm going to press play on [source] and run [tool]."
2. **T₁ — Trigger** (1-2s): Press play on source AND fire tool simultaneously. Both panes start "running."
3. **T₂ — Source Progress Visible** (10-30s): Source plays in real-time on left. DON'T speed up. Viewer must FEEL the time gap.
4. **T₃ — Tool Completes** (visible on right): Tool finishes and produces output. Source is still mid-playback on left.
5. **T₄ — The Reveal** (3-5s): Creator narrates the time gap explicitly. *"[Source] is still introducing what they're going to talk about and [tool] has already ingested the entire thing."* Pause for impact.

**Critical**: The viewer must SEE the source video's playhead position when the tool finishes. That visual time-evidence is what makes the moment a magic-trick reveal instead of a claim.

**Reference**: Exemplar A in genius.md — Brad's Sam Altman demo runs frames 11 (t=01:04, lecture starting) and 23 (t=02:22, lecture STILL in intro while structured summary is materialized on right). 78 seconds of source playback = visible proof.

### Phase 4 — Shot List Generation

Produce a recording-ready shot list:

```markdown
## Matrix Moment Shot List

**Source artifact**: [Selected artifact name + URL]
**Layout**: Split-screen with PIP bottom-left
**Total demo budget**: [N seconds]

### Demo Cut 1: The Reveal Beat ([X seconds total])
**Beat**: T₀ Setup → T₁ Trigger → T₂ Source Progress → T₃ Tool Completes → T₄ Reveal
**Recording sequence**:
1. (5-10s) Setup shot: both panes at neutral state. Narration: "[opening narration]"
2. (1-2s) Trigger shot: simultaneous press-play + tool fire
3. (10-30s) Continuous shot: source plays on left, tool runs on right
4. (3-5s) Reveal shot: tool finishes. Source playhead clearly visible.
5. (3-5s) Reaction shot: cut to talking-head, deliver the time-gap line

**Narration script**:
> [Verbatim line for each beat — write out the exact words]

### Demo Cut 2: The Continuation Beat ([X seconds total])
**Purpose**: Returns to the same source artifact later in the video to extend the visual through-line (per Pattern 2).
**When in video**: [Approximate timestamp]
**Beat**: Source still familiar to viewer → tool's output now richer → narration extends the original claim
[Same recording sequence structure as Cut 1]

### Optional: Demo Cut 3 (only if total demo budget permits)
[Same source artifact, third visit. Audit: does this third cut add value or is it gilding the lily?]
```

### Phase 5 — Pre-Recording Audit

Before recording, run this audit:
- [ ] One source artifact selected (Pattern 2)
- [ ] Layout matches canonical: source left, tool right, PIP bottom-left (Pattern 3 + HK2)
- [ ] Temporal proof beat structure designed (T₀ through T₄)
- [ ] Source video's playhead will be VISIBLE when tool completes (otherwise no temporal proof)
- [ ] Narration script written verbatim
- [ ] Total demo content within 10-20% of video duration (Pattern 1)
- [ ] Recording specs confirmed (resolution, lighting, background continuity)

If any check fails, return to that Phase before recording.

## Output Schema

```yaml
matrix_moment_brief:
  thesis: string
  speed_efficiency_claim: string
  selected_source_artifact:
    name: string
    url: string
    selection_score: int (sum of 5 axes)
    selection_rationale: string
  visual_hierarchy:
    layout: "split-screen, source-left output-right"
    pip_position: "bottom-left"
    pip_size_ratio: float (PIP area / total frame area; target ~0.05)
    background_continuity: string (description of consistent setup)
  temporal_proof_beat:
    setup_seconds: int
    source_playback_seconds: int (T₂ duration)
    reveal_narration: string (verbatim)
  shot_list:
    - cut_number: int
      duration_seconds: int
      timestamp_in_video: string
      beats: array of beat objects
      narration_script: string
      recording_specs:
        resolution: string
        layout_check: bool
        pip_check: bool
  total_demo_seconds: int
  total_video_target_seconds: int
  demo_ratio_check: bool (target 0.10-0.20)
```

## Example Output

**Scenario**: A creator is making an 8-min YouTube video about an AI agent that converts long PDFs into searchable summaries. Wants the Matrix Moment for the central demo.

```markdown
## Matrix Moment Shot List: PDF-to-Summary Agent

**Source artifact**: Stripe's 2024 Annual Letter (47-page PDF, public, well-known company)
- Selection score: Recognizability 5 + Visual richness 4 + Time-gap 5 + Continuity 4 + Emotional weight 5 = 23/25
- Rationale: Audience knows Stripe. 47 pages = real time gap. Letter has visible chapter structure that lets viewer track tool progress.

**Layout**: Split-screen, PDF on left, agent UI on right, webcam PIP bottom-left in green-bordered card (matching channel branding)
**Total demo budget**: 75 seconds (15% of 8-min video)

### Demo Cut 1: The Reveal Beat (45 seconds)

**Beat**: T₀ Setup → T₁ Trigger → T₂ PDF scrolls real-time → T₃ Agent completes → T₄ Reveal

**Recording sequence**:
1. (8s) Setup: PDF open at page 1, agent UI ready, "/summarize" command visible. Narration:
   > "I just downloaded Stripe's 2024 letter. 47 pages. I'm going to scroll through it like a normal human while my agent reads it."

2. (2s) Trigger: Hit "scroll" on left and "submit" on right simultaneously.

3. (25s) Continuous: PDF scrolls down at human reading pace on left. Agent UI shows progress bar + materializing summary on right. NO speed-up. Viewer must FEEL the reading time.

4. (5s) Reveal shot: Agent's structured summary fully visible on right (chapter headers, key metrics, exec quotes). PDF on left is still on page 11 of 47.

5. (5s) Reaction: Cut to talking-head close-up. Narration:
   > "I'm 11 pages in. The agent finished the entire letter. That's the time gap. Every page I would have skimmed, it actually read."

**Narration is the meta-line, not the demo line** — the demo did the work; narration just names the gap.

### Demo Cut 2: The Continuation Beat (20 seconds)

**Purpose**: Returns to the SAME Stripe letter at ~05:30 to demonstrate query mode.
**Beat**: Same letter visible (continuity) → user types follow-up question → agent answers from full document context

**Recording sequence**:
1. (3s) Setup: PDF returns to view, agent UI shows "Ready for follow-up." Narration: "Now I can ask anything about it."
2. (12s) Type query: "What were the 3 biggest growth drivers Stripe cited?" → Agent answers with citations to specific pages. PDF on left auto-scrolls to cited pages.
3. (5s) Reaction: Talking-head. "And those page citations are actual page numbers in the source. Verify any claim in seconds."

### Total demo content: 65 seconds (~13.5% of 8-min video) ✓ within target

### Pre-recording audit:
- [✓] One source artifact (Stripe letter)
- [✓] Layout: PDF left, agent right, PIP bottom-left
- [✓] Temporal proof: page 1 → page 11 visible during agent run
- [✓] Reveal narration written verbatim
- [✓] 13.5% demo ratio within 10-20% target
- [✓] Background continuity: same setup as talking-head frames
```

**What makes this excellent**: The shot list is a pre-recording artifact that locks the structural decisions (single source, layout, temporal beat) BEFORE the camera rolls. Most creators improvise demos and end up with rambling screen-recordings. This brief gets recorded, edited, and shipped in a fraction of the time — and it produces a demo that actually proves the thesis instead of just demonstrating the UI.

## Quality Gate

Before delivering the brief, verify:

- [ ] One source artifact selected (Pattern 2 — non-negotiable)
- [ ] Source artifact scored ≥18/25 on selection criteria (otherwise pick a different one)
- [ ] Layout matches canonical hierarchy (Pattern 3 + HK2)
- [ ] Temporal proof beat designed — source playhead VISIBLE when tool completes
- [ ] Reveal narration written verbatim (not paraphrased)
- [ ] Total demo content within 10-20% of video duration
- [ ] Continuation beat planned for SAME source (continuity, not breadth)

**Pass standard**: Can the creator hand this brief to an editor and produce a Matrix Moment without the creator needing to be present? If yes, ship it. If no, the brief is missing structural specificity.
