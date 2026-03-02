# Genius Patterns — Andy Lo Premium Websites (12 patterns)

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
