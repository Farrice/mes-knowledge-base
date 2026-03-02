# Andy Lo — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## Genius Patterns

## 1. Visual Direction First
Before touching any code or layout tool, establish a complete visual identity — color palette, lighting, mood, composition — using reference images and AI image generators. Never build without knowing the final aesthetic.

## 2. Bookend Frame Architecture
Create exactly two frames — a starting frame and an ending frame — that serve as visual anchors. The AI generates all motion in between. These bookends define the visual arc's start state and destination.

## 3. Tool Specialization Pipeline
Each tool handles exactly one job: Nano Banana/Whisk = image generation + style definition → Google Flow/Veo 3.1 = frame-to-video animation → EasyGIF = video-to-WebP conversion → Firebase Studio/Antigravity = website assembly + deployment. Never force one tool to do two jobs.

## 4. Boilerplate-First Foundation
Never start from zero. Begin with a professionally structured boilerplate — document structure, viewport handling, styling defaults, responsive foundations. This eliminates 90% of setup time.

## 5. Reference Image Anchoring
Always upload a reference image alongside generation prompts. This anchors AI output to your intended color palette, texture quality, and product style — preventing generic, off-brand results.

## 6. Progressive Polish Protocol
Build in layers: foundation → pages → content → CMS → polish. Each layer is complete before the next begins. Polish comes last — cursor glow, animations, micro-interactions are finishing touches, not foundations.

## 7. Headless CMS as Client Independence Layer
Position the CMS as a client independence layer — the mechanism that means clients never call you to update a headline or publish a blog post. Wire up GraphQL endpoints so non-technical users manage dynamic content without touching code.

## 8. WebP Sequence Scroll Animation Hack
Convert animations to WebP frame sequences triggered on scroll. This keeps visual quality while maintaining page performance. Export at original resolution, closest native FPS, quality 85, forever loop. Split into frames, store in Supabase, reference URLs for scroll-triggered playback.

## 9. Prompt Document as Build Blueprint
Create a structured prompt document containing every prompt needed for the entire project, organized by phase. This eliminates improvisation and makes the workflow repeatable by anyone.

## 10. AI Agent as Autonomous Engineer
Treat the AI agent as an autonomous front-end engineer: give it an implementation plan → review the plan it returns → approve or adjust → let it execute autonomously → verify output. Don't micromanage individual lines.

## 11. Security-Conscious API Handling
Separate API key handling — never paste secrets into agent prompts. Wait for the agent to create an .env file, then paste secrets only there. No API keys visible in code files, prompts, or version control.

## 12. Export-Ready Architecture
Build with portability — projects can be exported from Firebase Studio and deployed anywhere (Netlify, Vercel, custom hosting) without restructuring. Use code editor to select all → zip → download → deploy.

## Hidden Knowledge

## 1. The "Millisecond Judgment" Problem
Website visitors judge a site in milliseconds. Andy's entire pipeline is built around winning that neurological reaction through motion, depth, and visual coherence. Most builders optimize for features; Andy optimizes for the first impression. Every tool choice and animation decision serves this single moment.

## 2. The FPS/Quality Sweet Spot
When converting video to WebP: original resolution, closest frame rate to native (NOT maximum), quality 85. Going higher adds file size without perceptible quality gain. Going lower creates visible degradation. This number (85) only comes from testing dozens of projects — you won't find it in documentation.

## 3. Visual Arc Theory
The first and last frames aren't just "two images" — they define a visual arc. Opening frame = first impression. Closing frame = permanence. Everything in between = controlled interpolation. This is cinematic directing applied to web design — something film directors do intuitively but web designers almost never consider.

## 4. Supabase as Visual CDN
Andy uses Supabase not as a database but as a public bucket for visual assets — essentially a free, high-performance CDN for WebP frame sequences. This solves the "where do I host 50+ animation frames" problem without paid CDN services.

## 5. The Anti-Template Paradox
By following a systematic workflow (which sounds like templating), Andy produces sites that look nothing like templates. The system is rigid; the outputs are unique. This works because the visual direction step produces completely different aesthetic foundations every time, while the structural pipeline ensures professional execution.

## 6. Schema as Content Contract
When setting up Hygraph schemas, Andy creates a content contract — a structural agreement between CMS and frontend about what data looks like. Once the schema is set, content can be migrated programmatically. This is enterprise-grade architecture presented as "just drag and drop."

## 7. The "Agent Skills" Meta-Layer
Installing Antigravity agent skills as a pre-build step isn't optional decoration — these skills fundamentally change how the agent approaches the project. They provide best practices, design patterns, and quality standards that inform every subsequent decision. Skip this step and you get a mediocre site.

## 8. Permanent Auth Token Strategy
By creating a permanent OAuth token for Hygraph (rather than session-based), Andy enables content automation through AI agents — new blog posts and case studies can be published by simply pasting content into the agent. This is content automation infrastructure hiding in plain sight.

