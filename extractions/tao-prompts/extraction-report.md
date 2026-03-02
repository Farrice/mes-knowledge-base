# Tao Prompts — Mastery Extraction

## Content Assessment
Source: YouTube Video Transcript (~15 mins)
Expert: Tao Prompts (AI Video Production and Prompt Architecture)
Domain: AI Video Generation workflows, Prompt Engineering, Modular Content Creation
Depth Tier: Standard — Single deep dive covering a comprehensive 5-level mastery framework.
Genius Patterns: 4 identified
Hidden Knowledge: 3 tacit insights detected
Existing Overlap: Compliments PJ Accetturo (AI Video Production) by adding granular prompt-level control and multi-tool pipeline architecture.

## Executive Summary
- **Core Genius**: Tao Prompts transitions AI video creation from "slot machine" experimentation into deterministic film direction through structured syntax, reference control, and modular pipelines. 
- **What Makes Them Different**: He focuses on *control and consistency* rather than just aesthetic quality. He recognizes that basic prompts produce high-quality output now; the true skill is maintaining narrative continuity and precision across multiple shots.
- **Deployable Skills**: Designing JSON and Multi-Shot prompt structures, building "Lazy Teacher" Custom GPTs for prompt translation, and executing a modular (Storyboard -> Video -> Audio -> Lip Sync) pipeline.
- **Hidden Knowledge Captured**: The "Action vs. Lip Sync Decoupling", the "Storyboard Bridge", and "Pipeline Agnosticism".

## Genius Patterns

### 1. The Cinematic Formula (Structured Control)
- **What They Do Unconsciously**: They don't write generic descriptions. They modularize scenes into variables.
- **Executable Behavior**: Write prompts using strict syntax: [Visual Style] + [Camera Shot] + [Subject] + [Action] + [Environment] + [Camera Motion]. Never leave camera or style to the AI's discretion.
- **Deployment Context**: When transitioning from single-clip tests to cohesive scene generation.
- **Success Metric**: The generated video matches the exact framing and camera movement intended, rather than random cinematic pans.

### 2. Multi-Shot Sequential Prompting
- **What They Do Unconsciously**: They think in editing cuts, not single clips. 
- **Executable Behavior**: Write a single prompt that defines multiple sequential shots (e.g., Shot 1: Wide shot establishing scene. Shot 2: Close up on face. Shot 3: Over the shoulder). 
- **Deployment Context**: When generating cohesive B-roll sequences or continuous scenes from a single generation trigger.
- **Success Metric**: The AI returns a continuous scene with distinct, logical camera angle changes without losing character consistency.

### 3. The "Lazy Teacher" Prompt Translator
- **What They Do Unconsciously**: They refuse to memorize tool-specific syntax. They outsource tool compliance to LLMs.
- **Executable Behavior**: Feed the official prompt guide PDFs of new AI video tools (like Cling AI or Sora) into a Custom GPT. Add a section of "What to Avoid" based on testing. Then, feed narrative ideas to the GPT to translate them into tool-optimized prompts.
- **Deployment Context**: When adopting new AI video models or switching between tools (Runway to Cling to Luma).
- **Success Metric**: Prompts work flawlessly on the first try on a new platform without needing to manually read the syntax documentation.

### 4. Modular Pipeline Orchestration
- **What They Do Unconsciously**: They separate complex generations into single-variable tasks across multiple tools.
- **Executable Behavior**: Generate the visual scene first (Cling/Runway). Generate the character voice second (11Labs), specifying tone in brackets `[angry, whispering]`. Generate the lip sync third (Creatify Aurora/SyncLabs) using static or low-movement facial clips.
- **Deployment Context**: When creating dialogue-heavy or narratively complex cinematic scenes.
- **Success Metric**: Character speaks naturally without the video warping or melting, which occurs when asking a single AI model to handle complex action *and* lip sync simultaneously.

## Hidden Knowledge
- **The Decoupling Law**: Never prompt for intense physical action and dialogue lip-sync in the same generation. Create the action shots as B-roll, and create "low-movement" close-ups specifically for lip-syncing, cutting between the two in the edit.
- **The Storyboard Bridge**: When generating complex scenes for multiple tools, first prompt an LLM/Midjourney for a "3x3 Storyboard Grid". Use this grid as the architectural blueprint to ensure all subsequent video generations align perfectly with the narrative arc.
- **Prompt Complexity ≠ Aesthetic Quality**: Adding more words to a prompt does not make the video look "better" (a 1-sentence prompt can generate hyper-realistic footage). Prompt complexity only controls *specificity*. Stop describing aesthetics when what you need is blocking control.

## Methodology
The 5 Levels of Prompting:
1. **Idea Prompting**: Simple intuition for B-roll.
2. **Structured Prompting**: Formulas, JSON, and Multi-shot syntax.
3. **Reference Control**: Directing with image, video, and audio reference inputs to force consistency.
4. **Leverage & Scaling**: Using Custom GPTs loaded with documentation to generate prompts at scale.
5. **Full Pipeline Orchestration**: Using multiple specialized tools (Storyboard -> Video Gen -> Voice Gen -> Voice Sync) instead of one "god tool".

## Applied Intelligence

### Capability Unlocks
- **Deterministic AI Video Architecting**: The ability to plan and execute a short film or ad with guaranteed consistency rather than generating 100 random clips and hoping they match.
- **Tool-Agnostic Prompt Translation**: A system to instantly adopt any new video AI model (Sora, Veo, Cling) by feeding its user manual into a Custom GPT, avoiding the learning curve.
- **Automated Storyboard-to-Scene Workflow**: Connecting text-to-image storyboards directly to video generation prompts for high-efficiency client pitching or content planning.

### Market Signals
The market is shifting from "AI video is a slot machine" to "AI video is a predictable production pipeline." Clients and brands are no longer impressed by generic "beautiful AI clips"; they demand narrative control and specific character continuity. The demand for modular orchestrators (people who stitch Cling + 11Labs + SyncLabs) is eclipsing the demand for single-tool "prompt engineers."

### System Enhancements
Antigravity can utilize the "Lazy Teacher" Custom GPT behavior as an internal sub-agent protocol. We can create an `AIVideoTranslator` agent that takes Farrice's raw script ideas and auto-formats them into perfect multi-shot JSON prompts for whatever the current best-in-class video model is.

## Implementation Pathway
- **24-Hour Quickstart**: Create a Custom GPT (or Antigravity Agent) loaded with the Cling AI or current video model PDF guide to serve as the prompt translator.
- **7-Day Sprint**: Execute a full pipeline test (generate storyboard → translate to multi-shot prompts → generate video → generate 11Labs audio → lip-sync).
- **30-Day Integration**: Build standard operating procedures (SOPs) for generating B-roll vs. dialogue shots, solidifying the Decoupling Law.

## Prompt Inventory
| # | Prompt Name | Category | Status |
|---|-------------|----------|--------|
| 1 | `ai-video-translator-gpt` | leverage-scaling | [ ] |
| 2 | `cinematic-scene-architect` | structured-control | [ ] |
| 3 | `storyboard-grid-bridge` | pipeline-orchestration | [ ] |
| 4 | `modular-dialogue-director` | pipeline-orchestration | [ ] |
