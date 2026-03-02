---
name: website-assembly-blueprint
description: Assemble animated assets into a complete, deployed website using Firebase Studio or Antigravity
---

# Website Assembly Blueprint

## Purpose
Take all generated visual assets, animation frames, and content and assemble them into a complete, functional, deployable website. This prompt covers both the Firebase Studio (no-code) and Antigravity (agent-assisted) paths.

## System Prompt

You are Andy Lo, a premium AI website creator. You assemble websites like a film editor assembles footage — every cut is intentional, every transition serves the story. You build on professional foundations (never from scratch) and polish progressively. You treat the AI agent as an autonomous engineer.

## User Prompt

```
I need to assemble a premium website from my prepared visual assets.

**Project Details:**
- Project name: {{PROJECT_NAME}}
- Type: {{TYPE}} (personal site / agency site / product landing / portfolio)
- Pages needed: {{PAGES}} (e.g., Home, About, Work, Contact)
- Visual assets ready: {{ASSET_LIST}}
- Supabase frame URLs: {{FRAME_URLS}}
- Target mood: {{MOOD}}

**Choose your build path:**

---

## Path A: Firebase Studio (No-Code, Personal Projects)

### Step 1: Open Firebase Studio
Navigate to Firebase Studio and start a new project.

### Step 2: Assembly Prompt
Paste the following into Firebase Studio:

"Build a premium, modern website with the following specifications:

**Design Language:**
- Dark theme with {{COLOR_PALETTE}}
- Typography: Clean sans-serif (Inter or equivalent) for body, editorial serif for headings
- Full-screen sections with parallax scroll behavior
- Smooth scroll-triggered animations
- Minimal UI chrome — let the visuals do the talking

**Hero Section:**
- Full-viewport animated hero using WebP frame sequence
- Frame URLs: [paste Supabase URLs]
- Trigger: Scroll-linked playback (frame advances as user scrolls)
- Overlay: Brand name + tagline with subtle entrance animation

**Page Structure:**
{{PAGE_STRUCTURE}}

**Interactions:**
- Custom cursor with subtle glow effect
- Smooth page transitions between sections
- Hover states on all interactive elements
- Loading animation for asset-heavy sections

**Performance:**
- Lazy load all images below the fold
- Preload hero animation frames
- Optimize for Core Web Vitals"

### Step 3: Click "Prototype This App"
Let Firebase Studio generate the initial build.

### Step 4: Review + Polish
Iterate with targeted refinement prompts.

---

## Path B: Antigravity / IDE Agent (Agency-Grade, Client Projects)

### Step 1: Foundation
```
Create a professional React website foundation for {{PROJECT_NAME}}.

Requirements:
- React with Vite build system
- CSS modules (no Tailwind)
- Proper routing (React Router)
- Responsive from the start
- Clean component structure
- Dark theme with rich gradients
- Professional viewport handling
```

### Step 2: Install Agent Skills
Install Antigravity agent skills before any creative work — these change the agent's quality floor.

### Step 3: Page Generation
Generate each page with specific section prompts, referencing the visual direction established in Prompt #1.

### Step 4: Asset Integration
Place all generated visual assets and reference Supabase frame URLs for scroll-triggered animations.

### Step 5: Polish Layer
```
Add the following polish to the website:

1. Custom cursor glow effect (subtle, on-brand color)
2. Smooth scroll behavior (CSS scroll-behavior: smooth)
3. Section entrance animations (fade-up, 200ms stagger)
4. Logo carousel for clients/partners (if applicable)
5. Hover states on all cards and links
6. Loading skeleton for dynamic content
7. Mobile-optimized navigation
```

### Step 6: Deploy
- **Option 1**: Netlify — drag-and-drop build folder
- **Option 2**: Netlify + GitHub — connect repo for auto-deploy
- **Option 3**: Export from Firebase Studio — zip download for any host
```

## Expected Output
- Complete, deployable website
- All visual assets integrated
- Scroll-triggered animations functional
- Responsive across devices

## When to Use
- After visual direction (Prompt #1) and motion design (Prompt #2) are complete
- When you have all assets and are ready to build

## Genius Patterns Applied
- Progressive Polish Protocol (#6)
- Boilerplate-First Foundation (#4)
- AI Agent as Autonomous Engineer (#10)
- Export-Ready Architecture (#12)
