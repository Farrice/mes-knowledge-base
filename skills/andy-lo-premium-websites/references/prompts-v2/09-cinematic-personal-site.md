---
name: "Cinematic Personal Site"
source_prompt: "skills/andy-lo-premium-websites/references/prompts/09-cinematic-personal-site.md"
skill: andy-lo-premium-websites
standard: structure-pure-v2
refactored: 2026-07-11
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

## Output Contract
- Phase 1: starting + ending frame prompts, plus 2-3 supporting section-visual prompts, all sharing one palette
- Phase 2: one motion prompt (gentle, 4-6 second duration) and WebP conversion settings
- Phase 3: a 5-section page structure (Hero, About, Work/Skills, Portfolio-optional, Contact), design specifications, and interaction list
- Phase 4: a deployment target with custom domain and OG meta-tag instructions
- The complete phased output, in order, with no phase skipped

## Output Skeleton
```
PHASE 1 — VISUAL DIRECTION
Starting frame: [prompt — lighting, composition, texture, personal not corporate]
Ending frame: [prompt — same palette, shifted perspective, "introduction → invitation" arc]
Supporting visuals: [about section] / [skills section] / [contact section]

PHASE 2 — MOTION DESIGN
Motion prompt: [gentle/intentional, breathing-or-floating quality, duration in the 4-6s range]
WebP settings: resolution=[original], fps=[closest native], quality=[value], destination=[Supabase]

PHASE 3 — WEBSITE ASSEMBLY
Page structure:
- Hero: [animated, name + title overlay]
- About: [bio + supporting visual, subtle parallax]
- Work/Skills: [grid/list, hover effects]
- Portfolio (optional): [case study cards or thumbnails]
- Contact: [social links + email + CTA]
Design specs: [theme, typography pairing, cursor treatment, scroll behavior, entrance animations, mobile parity]
Interactions: [hover states, social icon treatment, portfolio zoom, scroll indicator, mobile nav pattern]

PHASE 4 — DEPLOYMENT
Platform: [chosen host]
Domain: [custom domain steps if applicable]
OG meta: [sourced from hero starting frame]
```

## Quality Gate
- [ ] All four phases are present in the output, in order, none skipped or merged
- [ ] Starting and ending frame prompts share one color palette
- [ ] The Portfolio section is explicitly marked optional and conditioned on {{PORTFOLIO}} being non-empty
- [ ] Every interaction listed maps to a concrete implementation detail, not a vague "add polish" instruction
- [ ] The OG image instruction explicitly references the hero starting frame, not a generic placeholder

## Deploy When
- Building a personal brand site from scratch
- Refreshing an outdated personal web presence
- Creating a portfolio that positions you as premium

## Genius Patterns Applied
- Visual Direction First (#1)
- Bookend Frame Architecture (#2)
- Tool Specialization Pipeline (#3)
- Progressive Polish Protocol (#6)
