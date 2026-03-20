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

---

## Hall of Fame Exemplars

**1. "Aura Smart Lamp" Product Launch Page**
*   **Description**: A single-page product launch site for a new smart home device. The hero section features a full-screen, scroll-triggered animation of the lamp rotating and transitioning between different lighting moods (e.g., "Sunrise Glow" to "Midnight Serenity"). The animation is buttery smooth, leveraging WebP sequences hosted on Supabase, and maintains a consistent, high-end visual aesthetic throughout. Product specifications and testimonials below are managed via a Hygraph CMS, allowing the marketing team to update content without developer intervention.
*   **What makes this excellent**: Exemplifies the "Millisecond Judgment" problem solution (Hidden Knowledge 1) by immediately captivating the user with a premium, performant visual. The animation perfectly executes "Bookend Frame Architecture" (Pattern 2) and "Visual Arc Theory" (Hidden Knowledge 3), with the starting frame showing the lamp off and the ending frame highlighting its ambient effect. The "WebP Sequence Scroll Animation Hack" (Pattern 8) ensures desktop-level visual quality at mobile-friendly speeds.

**2. "Apex Adventures" Interactive Travel Portal**
*   **Description**: A dynamic travel website showcasing exotic destinations. Each destination page features a hero section with a subtle, parallax-driven background animation of the landscape, smoothly transitioning as the user scrolls. The visual identity (color palette, mood, composition) for each destination is distinct yet cohesive with the overall brand, established through initial AI-generated visual direction. Travel packages and blog posts are managed through a headless CMS, allowing for rapid updates and new content publication.
*   **What makes this excellent**: Demonstrates "Visual Direction First" (Pattern 1) by establishing unique aesthetics for each destination while maintaining brand consistency. The subtle parallax animations showcase "Tool Specialization Pipeline" (Pattern 3) and "Progressive Polish Protocol" (Pattern 6), adding a premium feel without sacrificing performance. The "Headless CMS as Client Independence Layer" (Pattern 7) is crucial for a content-rich site, leveraging "Schema as Content Contract" (Hidden Knowledge 6) for robust data structuring.

**Anti-Exemplar: "Generic AI Build Co." Landing Page**
*   **Description**: A landing page ostensibly built with AI, featuring a stock video in the hero section that loops abruptly. The visual style is inconsistent across sections, mixing different fonts and color palettes. Basic content is hardcoded, requiring a developer to update a single headline. Animation quality is low, with visible stuttering and artifacts, and page load times are sluggish.
*   **What makes this mediocre**: Fails on "Millisecond Judgment" (Hidden Knowledge 1) due to poor first impression. Lacks any "Visual Arc Theory" (Hidden Knowledge 3) or "Bookend Frame Architecture" (Pattern 2), resulting in jarring, non-narrative motion. Ignores "Tool Specialization Pipeline" (Pattern 3) by trying to force a single AI tool to do everything, leading to generic output and poor performance. No "Headless CMS as Client Independence Layer" (Pattern 7), creating client dependency.

## Signature Moves

*   **The Aesthetic Blueprint First**: Always initiates a project by defining the complete visual identity—color palette, lighting, mood, composition—through AI image generation and reference images *before* any layout or coding begins. → **Deploy when**: Starting any new website, landing page, or visual asset creation.
*   **The Motion Arc Definition**: Crafts all complex animations by first establishing a distinct "starting frame" and "ending frame" in an AI video generator, then prompts the AI to interpolate the motion, ensuring a controlled visual narrative. → **Deploy when**: Any section requires a high-quality, narrative-driven animation or parallax effect.
*   **The Client Content Autonomy Layer**: Implements a headless CMS (like Hygraph) with GraphQL endpoints from day one, explicitly framing it as the mechanism for clients to manage all dynamic content independently, removing future developer dependency. → **Deploy when**: Building any client-facing website with dynamic content (blogs, case studies, product listings).
*   **The Scroll-Optimized Visual Stream**: Converts all generated video animations into high-performance WebP frame sequences at a specific quality (85) and native FPS, then hosts them on a public bucket (e.g., Supabase) for scroll-triggered playback. → **Deploy when**: Implementing any visually rich, scroll-driven animation that must maintain performance and quality.
*   **The Autonomous Engineer Brief**: Provides the AI agent with a comprehensive, multi-step implementation plan for the entire project, allowing it to autonomously execute the build, intervening only to review and approve major milestones, rather than micromanaging code. → **Deploy when**: Delegating complex, multi-file, or multi-API development tasks to an AI agent.

## Expert-Specific Quality Rubric

| Criterion                           | Score 4 (Acceptable)                                                                         | Score 7 (Good)                                                                                                   | Score 10 (Savant)                                                                                                                                                                         |
| :---------------------------------- | :------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **First Impression Coherence**      | Visuals are pleasant but lack a strong, unified brand identity; feels somewhat generic.      | Visuals are consistent and professional, clearly communicating the brand's aesthetic.                            | The site instantly communicates a distinct, premium brand identity within milliseconds; every visual element reinforces the core aesthetic and mood.                                       |
| **Visual Arc Integrity**            | Animations are present but may have abrupt transitions or inconsistent pacing; lacks narrative. | Animations transition smoothly between sections with good pacing, though the overall visual story is subtle.     | Animations tell a clear visual story, flowing seamlessly between distinct "bookend" states, guiding the user through a deliberate, cinematic experience without artifacts.                |
| **Performance-Optimized Visuals**   | Animations are heavy video files or low-quality GIFs, impacting page load significantly.      | Animations use WebP, but file sizes are larger than necessary or frame rates are slightly off, causing minor delays. | All complex animations are perfectly optimized WebP sequences (quality 85, native FPS) hosted on a performant CDN (Supabase), ensuring sub-second load times and flawless playback.           |
| **Content Autonomy & Scalability**  | Content is hardcoded or relies on a basic editor, requiring developer intervention for updates. | A headless CMS is integrated, but the schema could be more robust, or content updates require minor technical guidance. | A robust headless CMS with a well-defined GraphQL schema allows non-technical clients to update all dynamic content autonomously, supporting future content expansion with ease.           |
| **Aesthetic Uniqueness**            | The site resembles a common template, despite some custom elements.                          | The site has a custom feel, differentiating it from typical templates, showing creative application of tools.     | The site's aesthetic is entirely unique, defying common templates and reflecting a bespoke visual direction, demonstrating the "Anti-Template Paradox" in action.                           |
| **Progressive Polish Layering**     | Core functionality is present, but micro-interactions and subtle polish are missing.         | Basic micro-interactions and finishing touches are present, adding a good level of polish.                       | The site features subtle, intentional micro-interactions, cursor effects, and layered animations that feel like final, integrated touches, not afterthoughts, enhancing user delight.       |
| **Toolchain Handover Precision**    | Outputs from one tool require manual cleanup or adjustments before the next tool can use them. | Handoffs between tools are mostly clean, with minimal friction or rework required.                                | Each tool's output is perfectly formatted and optimized for the next stage in the pipeline, demonstrating a seamless, zero-friction handoff across the specialized toolchain.             |
