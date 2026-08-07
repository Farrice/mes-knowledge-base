---
name: Brief to Finished AI Video Ad, Production-Grade
problem_signature: a written ad brief/script must become launch-ready video with consistent characters and exact product labels across many AI-generated clips — one-model/one-prompt approaches produce inconsistent voices, drifting faces, garbled labels, and burned-in subtitle bugs
domain: creative
tags: [ai-video, multi-model-relay, remotion, storyboard, silent-vo, veo, kling, production-pipeline, trendscale]
date: 2026-07-11
status: active
session: trendscale-trial
---

# Solution Card — Brief → Finished AI Video Ad, Production-Grade (2026-07-11)

**Problem:** A written ad brief/script must become finished, realistic, launch-ready video, with consistent characters and exact product labels across many AI-generated clips, assembled hands-off so the operator only applies taste. One-model/one-prompt approaches produce inconsistent voices, drifting faces, garbled labels, and burned-in subtitle bugs.

**Context it was cracked in:** TrendScale trial (JCKED + Puravita scripts → video samples), session 2026-07-11. Assets: `_active/clients/trendscale-trial/03-video-samples/`.

**The approach (repeatable recipe):**
1. **Research before templates.** One deep-research pass against primary docs produces a CANONICAL LAW file (verified prompt ordering, timestamp syntax per model, subtitle mitigations, model-per-job rankings, flagged unknowns). Every downstream prompt cites it; UNCONFIRMED claims carry ⚠ flags into the prompts instead of being silently trusted. File: `research/AI-VIDEO-REALISM-RESEARCH.md`.
2. **Multi-model relay, not one model.** GPT Image 2 start frames (ALL in-scene text baked into stills), Kling-class for talking humans, Veo 3.1/Flow for cinematic b-roll with bracketed `[00:00-00:0X]` beats, real product photos attached as `<<<image_1>>>` on every product clip.
3. **Silent-VO rule.** Narrated multi-clip ads generate clips silent (SFX only); ONE ElevenLabs voice lays in post — per-clip native audio cannot hold one voice across a sequence.
4. **Consistency backbone first.** Storyboard contact sheets + character/environment/prop sheets generate before any video; panels feed Flow Ingredients / Kling refs / Soul ID.
5. **Per-clip multi-format cards.** Each clip ships as: start-frame prompt + timestamped Veo + Kling (if narrator) + Higgsfield paragraph + portable JSON `{beats[],dialogue,vo_verbatim,negatives[],start_frame_ref}` so any future model gets fed consistently. Machine index `clips.json` names expected asset files.
6. **Manifest-driven Remotion assembly.** `assets/clips/<ID>.mp4` naming contract shared between clips.json and render manifests; one command renders captions (accent-word coloring), music duck, silence-close, safe areas. PoC render is mandatory before claiming the pipeline works.

**Why it works:** every failure mode (voice drift, face drift, label hallucination, subtitle bug, timing mush) is owned by the one layer best at preventing it, and the contracts between layers are files (LAW doc, clips.json, manifests), not memory.

**Reuse trigger:** any "turn this brief/script into finished AI video" request. Orchestration: Fable writes specs and judges; Sonnet builders execute one layer each in parallel; research completes before template builders start.
