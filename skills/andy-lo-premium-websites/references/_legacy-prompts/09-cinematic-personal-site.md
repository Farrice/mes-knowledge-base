---
name: cinematic-personal-site
description: Create a premium personal/portfolio website with cinematic transitions and parallax effects
---

# Cinematic Personal Site

## Purpose
Build a complete personal website that positions you as premium before a single word is read. This is an end-to-end prompt that combines visual direction, motion design, and website assembly into a single workflow for personal/portfolio sites.

## System Prompt

You are Andy Lo. A personal website isn't a résumé — it's a first impression that compounds. You build personal sites that feel like stepping into a film — every scroll reveals something intentional. The motion, depth, and visual coherence create the feeling of someone who takes their craft seriously.

## User Prompt

```
Build a cinematic personal website for me.

**Personal Details:**
- Name: {{NAME}}
- Title/Role: {{TITLE}}
- Brief bio (1-2 sentences): {{BIO}}
- Key skills/expertise: {{SKILLS}}
- Social links: {{SOCIALS}}
- Portfolio pieces (if any): {{PORTFOLIO}}
- Desired mood: {{MOOD}} (e.g., "dark and cinematic," "minimal and architectural," "warm and creative")
- Color preferences: {{COLORS}} (or "surprise me")
- Reference sites I admire: {{REFERENCES}}

**Build the complete site following this workflow:**

### Phase 1: Visual Direction (10 min)
1. Generate a starting frame prompt for Nano Banana/Whisk:
   - Based on my mood and color preferences
   - Should feel personal, not corporate
   - Include lighting, composition, texture specs

2. Generate an ending frame prompt:
   - Same palette, shifted perspective
   - Creates a visual arc from "introduction" to "invitation"

3. Generate 2-3 supporting section visuals:
   - About section background
   - Skills/expertise section atmosphere
   - Contact section mood

### Phase 2: Motion Design (10 min)
4. Motion prompt for Google Flow:
   - Gentle, intentional movement (not flashy)
   - Should feel like breathing or floating
   - 4-6 second duration

5. WebP conversion settings:
   - Original resolution
   - Closest native FPS
   - Quality 85
   - Upload to Supabase

### Phase 3: Website Assembly (30-45 min)
6. Build the site using Firebase Studio or Antigravity:

**Page Structure:**
- **Hero**: Full-viewport animated section with name + title overlay
- **About**: Brief bio with supporting visual, subtle parallax
- **Work/Skills**: Grid or list of expertise areas with hover effects
- **Portfolio** (optional): Case study cards or project thumbnails
- **Contact**: Minimal — social links + email with tasteful CTA

**Design Specifications:**
- Dark theme (deep charcoal/navy, NOT pure black)
- Typography: Editorial serif for name/headings, clean sans for body
- Custom cursor with subtle glow matching brand color
- Smooth scroll between sections
- Section entrance animations (fade-up, stagger)
- Responsive: looks premium on mobile too
- Page load: subtle logo/name animation before content appears

**Interactions:**
- Hover effects on all links and cards
- Social icons with hover color shift
- Portfolio cards with image zoom on hover
- Smooth scroll indicator in hero section
- Mobile: hamburger nav with full-screen overlay

### Phase 4: Deployment
7. Deploy to preferred platform:
   - Netlify (drag-and-drop or GitHub connected)
   - Custom domain setup instructions
   - Meta tags for social sharing (OG image from hero frame)

**The site should make someone think "this person is serious about what they do" within 2 seconds of landing.**
```

## Expected Output
- Complete visual direction (frame prompts + motion prompt)
- Fully assembled personal website
- Deployed and live
- Custom domain ready

## When to Use
- Building a personal brand site from scratch
- Refreshing an outdated personal web presence
- Creating a portfolio that positions you as premium

## Genius Patterns Applied
- Visual Direction First (#1)
- Bookend Frame Architecture (#2)
- Tool Specialization Pipeline (#3)
- Progressive Polish Protocol (#6)
