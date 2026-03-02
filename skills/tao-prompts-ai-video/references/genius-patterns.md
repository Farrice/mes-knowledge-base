# Genius Patterns: Tao Prompts AI Video Architecture

## 1. The Cinematic Formula (Structured Control)
**What They Do**: Instead of intuitively describing scenes like a novelist, they write prompts like an architectural blueprint or a JSON data structure.
**Executable Behavior**: Assemble prompts strictly using the formula: [Visual Style] + [Camera Shot] + [Subject] + [Action] + [Environment] + [Camera Motion]. Never leave framing or styling up to the AI's interpretation.
**Deploy When**: Generating precise B-Roll, product shots, or specific cinematic compositions where serendipity is not desired.
**Success Metric**: The output strictly follows the requested framing (e.g., "Close-up", "Low Angle") and completely obeys the directed camera movement.

## 2. Multi-Shot Sequential Prompting
**What They Do**: They don't generate single clips in isolation. They generate editing cuts natively within the prompter.
**Executable Behavior**: Write a single unified prompt that defines multiple distinct shots sequentially (e.g., Shot 1: Wide shot establishing base. Shot 2: Close up on hacker's fingers. Shot 3: Over the shoulder looking at screen).
**Deploy When**: Constructing cohesive B-roll sequences or continuous scenes that need to maintain stylistic and character continuity across different cuts.
**Success Metric**: The AI delivers a seamless edit of multiple camera angles within one output video without hallucinating the primary setup.

## 3. The "Lazy Teacher" Prompt Translator
**What They Do**: They refuse to hand-write prompts that comply with the intricate syntax of every new video model that drops.
**Executable Behavior**: Feed the official prompt guideline PDF of the target tool (e.g., Cling AI) into a Custom GPT. Instruct the GPT to act strictly as a syntax translator. Supply your narrative intent or storyboard beat to the GPT, and let it generate the mathematically precise prompt required for the target tool.
**Deploy When**: Swapping between AI video generators, utilizing newly released models, or standardizing team output.
**Success Metric**: A raw, unformatted idea is instantly converted into a high-fidelity, tool-optimized prompt that works perfectly on the first pass.

## 4. Modular Pipeline Orchestration
**What They Do**: They treat AI video as an assembly line, not a magic box. They never expect one model to do everything.
**Executable Behavior**: Isolate tasks. Generate the visual scene using a dedicated video model (Runway/Cling). Generate audio tracks with specific emotional tone bracketing using specialized voice tools (11Labs). Stitch the final lip-sync together using specialized face-animation tools (Creatify/SyncLabs). 
**Deploy When**: Orchestrating dialogue-heavy scenes, complex human interactions, or sophisticated narratives.
**Success Metric**: Character movements don't warp or glitch when they speak, because action and lip-sync are generated in separate parallel environments.
