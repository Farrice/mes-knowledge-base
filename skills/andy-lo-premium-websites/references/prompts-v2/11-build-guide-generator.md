---
name: "Build Guide Generator"
source_prompt: "skills/andy-lo-premium-websites/references/prompts/11-build-guide-generator.md"
skill: andy-lo-premium-websites
standard: structure-pure-v2
refactored: 2026-07-11
---

# Build Guide Generator

## Purpose
Create a structured "build guide" — a prompt document containing every prompt needed for an entire website project, organized by phase. This eliminates improvisation and makes the workflow repeatable by anyone.

## System Prompt

You are Andy Lo. You know that the difference between a one-time project and a scalable service is documentation. A build guide is your project blueprint — anyone with access to the same tools should be able to follow it and produce a comparable result.

## User Prompt

```
Create a comprehensive build guide for a website project.

**Project:** {{PROJECT_NAME}}
**Type:** {{PROJECT_TYPE}} (personal site / agency site / product landing / portfolio)
**Visual mood:** {{MOOD}}
**Pages:** {{PAGES}}
**CMS needed:** {{YES_NO}}
**Target timeline:** {{TIMELINE}}

**Generate a build guide with the following structure:**

---
# Build Guide: {{PROJECT_NAME}}
## Created: {{DATE}}
## Estimated Time: {{TIMELINE}}
---

### Phase 1: Visual Direction (Time: ~30 min)
**Tool: Nano Banana / Whisk**

**Prompt 1.1 — Starting Frame:**
[Generated prompt for opening visual]

**Prompt 1.2 — Ending Frame:**
[Generated prompt for closing visual]

**Prompt 1.3 — Supporting Assets:**
[Generated prompts for section backgrounds and product shots]

**Checklist:**
- [ ] Starting frame generated and approved
- [ ] Ending frame generated and approved
- [ ] Supporting assets generated
- [ ] All assets downloaded to local folder

---

### Phase 2: Motion Design (Time: ~30 min)
**Tool: Google Flow (Veo 3.1)**

**Prompt 2.1 — Hero Animation:**
[Generated motion prompt]

**Prompt 2.2 — Section Animations (if needed):**
[Generated motion prompts for additional sections]

**Conversion Settings:**
- Resolution: Original
- FPS: Closest native
- Quality: 85
- Format: WebP
- Loop: Forever

**Checklist:**
- [ ] Hero animation generated and reviewed
- [ ] Converted to WebP
- [ ] Frames split and uploaded to Supabase
- [ ] Frame URLs documented

---

### Phase 3: Website Assembly (Time: ~1-2 hours)
**Tool: Firebase Studio / Antigravity**

**Prompt 3.1 — Foundation:**
[Generated boilerplate prompt]

**Prompt 3.2 — Page Assembly:**
[Generated prompts for each page]

**Prompt 3.3 — Polish:**
[Generated polish prompts — cursor, animations, hover states]

**Checklist:**
- [ ] Boilerplate renders clean in preview
- [ ] All pages built and linked
- [ ] Assets integrated from Supabase
- [ ] Polish applied
- [ ] Responsive on mobile

---

### Phase 4: CMS Integration (if applicable, Time: ~1 hour)
**Tool: Hygraph + Agent**

**Prompt 4.1 — CMS Wiring:**
[Generated CMS integration prompt]

**Prompt 4.2 — Content Migration:**
[Generated migration prompt]

**Checklist:**
- [ ] Schemas created
- [ ] Auth token generated and stored in .env
- [ ] Content migrated from hardcoded to CMS
- [ ] CMS publishing verified

---

### Phase 5: Deployment (Time: ~15 min)
**Tool: Netlify / Vercel**

**Steps:**
1. Build production bundle
2. Deploy to hosting
3. Configure custom domain
4. Set up OG meta tags for social sharing
5. Test all pages live

**Checklist:**
- [ ] Site deployed and accessible
- [ ] Custom domain configured (if applicable)
- [ ] Social sharing preview looks correct
- [ ] All animations render on production

---

**This build guide should be complete enough that a different person could follow it and produce a comparable result to the original. Every prompt should be specific and actionable — no vague instructions.**
```

## Output Contract
- A single build-guide document, header (project, date, estimated time) plus five sequential phases
- Each phase carries: named tool, numbered sub-prompts (populated, not left as "[Generated prompt]" placeholders), and a completion checklist
- Phase 4 (CMS) explicitly marked conditional on {{YES_NO}}
- Every checklist item from the source protocol present and unmodified

## Output Skeleton
```
BUILD GUIDE: {{PROJECT_NAME}}
Created: [date] | Estimated Time: {{TIMELINE}}

PHASE 1 — VISUAL DIRECTION (Tool: Nano Banana / Whisk)
1.1 Starting Frame: [populated prompt]
1.2 Ending Frame: [populated prompt]
1.3 Supporting Assets: [populated prompt(s)]
Checklist: [ ] starting frame approved [ ] ending frame approved [ ] supporting assets generated [ ] assets downloaded

PHASE 2 — MOTION DESIGN (Tool: Google Flow)
2.1 Hero Animation: [populated prompt]
2.2 Section Animations: [populated prompt(s), if needed]
Conversion settings: resolution=[original], fps=[closest native], quality=[value], format=WebP, loop=[forever]
Checklist: [ ] animation reviewed [ ] converted to WebP [ ] frames uploaded to Supabase [ ] URLs documented

PHASE 3 — WEBSITE ASSEMBLY (Tool: Firebase Studio / Antigravity)
3.1 Foundation: [populated prompt]
3.2 Page Assembly: [populated prompt per page]
3.3 Polish: [populated prompt]
Checklist: [ ] boilerplate clean [ ] pages built+linked [ ] assets integrated [ ] polish applied [ ] mobile responsive

PHASE 4 — CMS INTEGRATION (conditional on {{YES_NO}}; Tool: Hygraph + Agent)
4.1 CMS Wiring: [populated prompt]
4.2 Content Migration: [populated prompt]
Checklist: [ ] schemas created [ ] token in .env [ ] content migrated [ ] publishing verified

PHASE 5 — DEPLOYMENT (Tool: Netlify / Vercel)
Steps: [build] → [deploy] → [domain] → [OG tags] → [live test]
Checklist: [ ] deployed+accessible [ ] domain configured [ ] social preview correct [ ] animations render in production
```

## Quality Gate
- [ ] All five phases are present, each with its named tool and populated (not placeholder) sub-prompts
- [ ] Phase 4 is explicitly marked conditional and is omitted or included based on {{YES_NO}}, not always present
- [ ] Every checklist item from the source protocol appears verbatim — none dropped or reworded
- [ ] The guide is specific enough that someone unfamiliar with the project could execute it without asking clarifying questions

## Deploy When
- Before starting any new website project
- When creating a repeatable service offering
- When delegating website builds to team members

## Genius Patterns Applied
- Prompt Document as Build Blueprint (#9)
- Tool Specialization Pipeline (#3)
- Progressive Polish Protocol (#6)
