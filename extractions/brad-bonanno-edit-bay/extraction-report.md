# Brad Bonanno — Agentic Edit Bay: Virtuoso Mastery Extraction Report

**Source**: https://www.youtube.com/watch?v=mlhhZSHIS-w — "My Claude Code Edits FULL Videos in One Shot (Here's How)"
**Extraction**: MES 3.0 wf-01, multi-modal (518-segment caption transcript + 54 frames), 2026-08-06
**Corpus note**: SECOND Bonanno extraction — composes with `extractions/brad-bonanno/` (explainer architecture, 2026-05-03) and `skills/brad-bonanno-explainer-architecture/`. This one decodes the *editing pipeline*, not the explainer format.
**Target application**: the Antigravity Edit Bay build (skills/video-studio) — Farrice's in-house VOX-explainer studio.

---

🔍 MES 3.0 CONTENT ASSESSMENT
Type: YouTube tutorial + live demo, 17:00, 1280×720, published 2026-08-06 (extracted day-of)
Expert: Brad Bonanno — AI/automation YouTuber & indie maker; built the claude-video `/watch` skill (the tool this extraction ran on); claims every video on his channel for the past month was edited by this pipeline; prior extraction in corpus verified his explainer craft
Domain: agentic video editing (primary) + agent-loop design, capability decomposition, motion-graphics-as-code, editorial QA systems (hidden: front-end design taste transfer, persistent-memory compounding)
Depth: Master — he is demonstrating a production system he operates daily, not teaching theory
Virtuoso Patterns: 12 unconscious mastery behaviors detected
Extraction Value: VIRTUOSO — this is the exact missing spine of the Antigravity media arsenal (assembly/edit layer); every stage maps to tools already owned or free
Proceeding with ultra-resolution virtuoso extraction...

## Executive Summary

- **Core Genius**: He treats "Claude can't edit video" as a *sensory* problem, not a capability problem — give the agent ears (word-level timestamps) and eyes (frame extraction of its own render), decompose the craft at the boundaries of what the agent can actually execute, and editing becomes a closed feedback loop instead of a blind generation task.
- **Unique Value**: The only public pipeline where the agent *reviews its own render* with controllable inspection (choose where to look) rather than passive video-understanding — and where human corrections compound into a persistent style file instead of evaporating.
- **Replication Priority**: (1) the render→watch→fixlist→re-render loop, (2) transcript-driven cutting via word timestamps, (3) style-file correction compounding.
- **Virtuoso Elements**: capability-boundary decomposition, seam-targeted inspection, solved-vs-fails stage triage, annotation-as-direction pre-work, graphics-as-front-end taste transfer.
- **Time to Mastery**: 30 days (pipeline runs day 1; one-shot quality by week 4).
- **Surpassing Potential**: HIGH — he has no direction/craft layer (we have 18 craft-map masters), no cost governance (we have budget guards), no provenance (we have manifest.jsonl), and his B-roll runs through a paid aggregator we've already replaced with fal-direct.

## Genius Patterns Decoded

### 1. Give the Agent the Missing Sense
He never asks a bigger model to "understand video." Claude can't hear → WhisperX word-level timestamps ("Claude has no idea where a cut lands without sub-second timing of every spoken word"). Claude can't see → frame extraction of the render.
**Why It Works**: instrumentation closes sensory gaps at near-zero cost; model upgrades don't add senses, they add reasoning over the same missing data.
**How to Apply**: before any "the agent can't do X" conclusion, name the missing input and build the cheapest deterministic feeder for it (Edit Bay: `transcribe_local.py`, `video_qa.py inspect`).
**Success Metric**: zero pipeline stages that require the agent to perceive something it was never given; cut accuracy at word boundaries (±1 word).

### 2. Controllable Inspection > Passive Comprehension
He explicitly rejects Gemini-style video understanding: with `/watch`, Claude "controls exactly where it looks" — e.g., inspecting the seams between graphics and scenes.
**Why It Works**: review value concentrates at transition points; uniform comprehension dilutes attention across mostly-fine footage. Directed attention is a queryable microscope, not a summary.
**How to Apply**: extract frames at cut points ±0.2s, graphic in/outs, caption onsets — never uniform sampling (Edit Bay: seam-targeted `inspect`).
**Success Metric**: >80% of extracted review frames land within 0.5s of an edit event; defects caught per frame reviewed.

### 3. Capability-Boundary Decomposition
"Claude Code cannot log into Premiere Pro" — so the pipeline splits the human editor's craft at the boundaries of what the agent can execute (read text, run CLIs, write code), not at the boundaries of an NLE's menus. Six stages, each agent-runnable: transcription → rough cut → B-roll → graphics → SFX → export (frame t=02:50).
**Why It Works**: every stage is either deterministic (ffmpeg) or text-reasoning (cut decisions from transcript) — the two things LLM agents are actually reliable at.
**How to Apply**: when porting any human craft to an agent, list the human's sub-tasks, then re-partition them by agent capability class, not by traditional tool workflow.
**Success Metric**: each stage completable by one agent turn + one CLI invocation; no stage requires GUI interaction.

### 4. Solved-vs-Fails Stage Triage
He states plainly which stages always work and which always fail: rough cuts "succeed every time" (pure transcript problem); anything visual "fails by default" (captions on faces, spacing) and *requires* the loop.
**Why It Works**: review effort budgeted where failure lives; no QA spend on solved stages.
**How to Apply**: classify every pipeline stage as SOLVED (spot-check only) or FAILS-BY-DEFAULT (mandatory loop). Edit Bay: cutlist-apply = solved; overlay/captions/graphics = loop-mandatory.
**Success Metric**: QA iterations concentrated on visual stages; rough-cut revisions ≈ 0 per video.

### 5. The Picky-Editor Fix List
Sub-agents review the render "like a picky editor" and return a **structured fix list**, not a score or vibe ("visual glitches, spacing, alignment, general feel" → concrete items Claude then fixes).
**Why It Works**: a fix list is executable; a score is not. Severity-tagged defects convert judgment into a work queue.
**How to Apply**: reviewer contract requires: timestamp, shot ID, observed vs expected, proposed action (Edit Bay `fixlist.json`). "By the time I sit down for final review it's been through half a dozen reviews."
**Success Metric**: ≥90% of fixlist items actionable without clarification; human final-review notes ≤3 per video by week 4.

### 6. Corrections Compound or You Pay Forever
Secret #3: every note from final review is written back into the style file **before the edit is closed out** — "every note you give in final review is a note you'll give again next week."
**Why It Works**: converts episodic feedback into persistent policy; the marginal video approaches zero-correction asymptotically. This is the compounding term in the system.
**How to Apply**: close-out gate: no edit is "done" until human fixlist items are promoted to the style file's Correction Log (Edit Bay: `_active/farrice-brand/video-style.md`).
**Success Metric**: repeat-correction rate → 0; style file grows every video for the first month.

### 7. Annotation-as-Direction Pre-Work (his #1 lever, "not a tool")
Script lives in a commentable doc; inline comments carry direction: which music, camera behavior ("start zoomed in, then rapidly zoom out"), graphic types, reference-image links. "10 minutes of comments will literally save you hours of back and forth." Frame t=10:32 shows his agent planning "graphics from the 15 doc comments."
**Why It Works**: converts the agent from *guessing* taste to *reading* direction; ambiguity is resolved at authoring time when it's cheapest.
**How to Apply**: Edit Bay `script-annotation.md` grammar: `[music:] [broll:] [graphic:] [camera:] [ref:]` inline tags in the script markdown — same semantics, file-native instead of Word.
**Success Metric**: ≥1 annotation per script beat; first-render acceptance rate rises with annotation density.

### 8. Graphics-as-Code ⇒ Taste = Front-End Design
Secret #1: every HyperFrames graphic is HTML, so "anything that makes Claude better at front-end design makes your graphics better." His taste skill gives "a design approach, not a preset — so it improves graphics in any style."
**Why It Works**: reduces motion-graphics quality to a domain (front-end craft) where agent tooling is mature and improvable; approach-level rules generalize across styles where presets lock one look.
**How to Apply**: route graphic generation through the existing design stack (frontend-design skill, satori brain, Premium Minimal brand system) — we already own a deeper "taste skill" than his.
**Success Metric**: zero "AI slop" default-styled graphics; graphics pass the brand's design-taste gate.

### 9. Generated Assets Mid-Edit (breaking the HTML ceiling)
Secret #2: the generator is called *during* the edit to produce an icon/image/clip that HTML can't build, dropped straight into a HyperFrames composite.
**Why It Works**: keeps one assembly path (graphics engine composites everything) while unbounding the visual vocabulary.
**How to Apply**: cutlist graphic shots may declare a generated asset dependency → `/generate` (fal) → file → composite. Never a second assembly path.
**Success Metric**: generated-asset shots carry full provenance (prompt+cost in manifest) and land in one render pass.

### 10. One Working Folder, One Prompt, One Reminder
The live edit starts with: a single folder (footage + script), a short prompt naming the target clip, "go check the comments," and always the reminder "use the watch skill for that self-improvement loop."
**Why It Works**: the pipeline's intelligence lives in skills/config, not in prompt engineering; the invocation stays constant so the system is operable by anyone (the handoff test).
**How to Apply**: Edit Bay front door = `/video-studio <project>` with the same three elements: workspace path, annotated script, QA-loop mandate baked into the workflow (not retyped).
**Success Metric**: invocation prompt ≤4 sentences, stable across videos.

### 11. Async Overlap of Slow Lanes
B-roll render is kicked off, then "Claude keeps working during the render" — generation latency masked behind graphics planning.
**Why It Works**: the pipeline's slowest stage (video generation) has zero data dependency on graphics planning; overlapping them cuts wall-clock ~in half.
**How to Apply**: cutlist stages ordered so generation fires early and assembly consumes results late (Edit Bay: fire fal jobs before graphics build).
**Success Metric**: wall-clock ≈ max(lane) not sum(lanes); his intro: ~40 min autonomous.

### 12. Version-Stamped Render Discipline
Renders are versioned and reviewed as versions ("Version 1" burned into review frames t=12:29–13:47); he ships after "two passes of technical QA and composition fidelity."
**Why It Works**: versioning makes the QA loop legible — every fixlist binds to a specific render, regressions are diffable.
**How to Apply**: `renders/v01.mp4, v01-frames/, v01-fixlist.json` (Edit Bay convention); cap loop at 3 iterations to prevent churn.
**Success Metric**: every shipped video has a full v-chain audit trail; ≤3 versions to pass.

## Hidden Knowledge Revealed (Layer 2 — never explicitly taught)

1. **The caption auto-correction wordlist** (frame t=08:01, on-screen only, never spoken): his style file carries a "Brand / product wordlist (caption auto-corrections)" — Claude/ClaudeKit/etc. spelled canonically — so ASR misspellings of brand terms are auto-fixed at caption time. Steal verbatim: Farrice's wordlist = Parallax, Antigravity, Farrice, My.BPM, Proof-to-Market, LinkedIn…
2. **Typography is pinned in config, not chosen per-video** (same frame): "Display font: Instrument Serif (regular + italic, or *apostrophes*) for title cards, editorial statements…" — font decisions are style-file law, which is why his graphics never drift. Also visible: "Hook style (TikTok/raw front card)" — the cold-open card is a *named, configured* graphic type.
3. **The agent's own edit plan is a todo list** (frame t=10:32): the edit run is decomposed into tracked todos ("Study the rough cut frames to find gesture timings" → "Plan graphics from the 15 doc comments" → "Generate B-roll" → "Build the graphics in HyperFrames" → merge). Editing is run as a *project*, not a prompt.
4. **Gesture-timing sync**: that first todo — studying rough-cut frames to find *gesture timings* — means graphics are timed to his hand movements/body language, not just to words. This is why his overlays feel motivated. (Transcript never mentions it.)
5. **The B-roll model is Seedance 2.5 at 1080p** (frame t=12:04; ASR garbled it as "Cance 2"). VERIFIED visually. Direct consequence for us: our fal stack runs Seedance natively — same model family, no aggregator needed; our seedance-1080p hard-block means we ship 720p B-roll (fine at overlay scale) or A/B kling-v3.
6. **Sub-second cutting needs alignment, not just ASR**: he names WhisperX specifically (wav2vec2 forced alignment), not Whisper — the distinction between "transcript" and "cut-accurate transcript" is load-bearing and unstated.
7. **Review persona is adversarial by design**: "picky editor" is a deliberate persona choice — same mechanism as our adversarial-reviewer/blind-bar doctrine: agreeable reviewers produce nothing actionable.
8. **His demo footage economics**: ~$90/video in tokens absorbed by a Max plan (marginal cash $0), B-roll "a few dollars per segment," vs. $150–$3,000 human editor — the pipeline's pitch is cash-flow shape, not just speed. (~3 hr turnaround; intro segment: ~40 min autonomous with ONE human intervention — choosing between two B-roll takes.)

## Complete Methodology (4-level progression)

### Week 1 — Foundation (mental models + the solved stage)
Install the senses: WhisperX local, frame extraction. Learn the capability-boundary decomposition. Ship transcript-driven rough cuts only (the SOLVED stage) — cut silences/filler from one real recording. Domain language: cutlist, beat, seam, fixlist, style file.
**Checkpoint**: a watchable rough cut from raw footage, zero visual layers, zero paid calls.

### Week 2 — Professional (the loop)
Add captions + music + the QA loop. Run render→inspect→fixlist→re-render on every output. Style file v1 exists (typography, caption style, wordlist). Human corrections start promoting to the Correction Log.
**Checkpoint**: a captioned, music-bedded video that passed ≥1 self-review cycle; ≥3 corrections banked.

### Week 3 — Contextual (direction + B-roll)
Annotated-script pre-work becomes mandatory. B-roll ladder live (own footage → stock → graphics → generated). Graphics-as-code with the design stack loaded. Async overlap of generation and planning.
**Checkpoint**: a full VOX-grammar explainer: annotations honored, ≥2 B-roll sources, ≥2 graphics, one-shot acceptance of ≥70% of beats.

### Week 4 — Virtuoso (compounding + surpassing)
Style file dense enough that first renders need ≤3 human notes. Derive shorts from the long-form cutlist. Package releases. Innovate past the source: seam-targeted inspection, provenance, cost governance, blind-bar QA vs. a named VOX reference.
**Checkpoint**: publish-ready 3-format package Farrice would actually post; repeat-correction rate ≈ 0.

## Implementation Pathway

### 24-Hour Quickstart
- H0–2: WhisperX into `.venv`; transcribe one real recording (word-level JSON + SRT).
- H2–5: hand-write a 6–8 shot cutlist from the transcript; `edit_bay.py cutlist-apply` → rough cut.
- H5–7: burn captions (platform preset); qa-probe clean.
- H7–8: watch it. **First result: a real cut of real footage, inside one day, $0.**

### 7-Day Sprint
- D1: quickstart. D2: QA loop live (inspect→fixlist→re-render). D3: style file v1 + wordlist. D4: annotated script grammar + first full explainer beat-map. D5: B-roll ladder (stock keys + graphics). D6: full P1 pilot production. D7: human review → corrections promoted → v2 render → package.

### 30-Day Transformation
- W1: foundation + P1 pilot (Parallax explainer, VO-only). W2: P2 pilot (AI teaching, screen-recording B-roll) + shorts derivation. W3: P3 pilot (Proof-to-Market asset) + cadence rehearsal (1 long + shorts inside one week). W4: style file audit, loop-iteration count trending down, publish cadence sustained. **Success criteria**: 3 pilots shipped, ≤3 human notes per video, weekly cadence proven.

## Transcendence Opportunities (preview)

- **Hidden Virtuoso Patterns**: gesture-timing sync (see Hidden Knowledge #4) formalized as a cutlist field — graphics keyed to motion, not just words. He does it implicitly; we can make it a schema property.
- **Cross-Domain**: the render→inspect→fixlist loop is a general artifact-QA pattern — apply to poster generation (fantastic-studio critique stage already exists; unify contracts) and to web-artifact review.
- **Technology Amplification**: he pays an aggregator for Seedance; we run it fal-direct with budget guards, provenance manifest, and craft-map grammar he doesn't have (cinema-worldbuilder M1–M5, PJ pacing tables, Dave Clark flatness audit). Our direction layer is the surpass vector: his pipeline executes edits; ours can *direct* them.
- **Constraint Removal**: his pipeline assumes his talking-head footage exists; our three-mode design (talking-head / VO-only / zero-camera with Farrice VO) removes the camera as a prerequisite — VOX grammar from a laptop and AirPods.

Full Five-Pillar treatment: fold into the Edit Bay build (plan: `run-the-watch-watch-and-replicated-corbato.md`) — the build IS the transcendence path.

---

*Factual grounding: pipeline stages, tools, costs, quotes = VERIFIED (transcript + frames). Seedance 2.5 = VERIFIED (frame t=12:04). "Every video for the past month" = his claim, UNCONFIRMED. HyperFrames repo verified independently (github.com/heygen-com/hyperframes, Apache 2.0).*
