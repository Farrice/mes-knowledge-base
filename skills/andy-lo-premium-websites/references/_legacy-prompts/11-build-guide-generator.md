---
name: build-guide-generator
description: Create a structured prompt document that makes any website workflow repeatable
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

## Expected Output
- Complete, phase-by-phase build guide document
- All prompts pre-written and ready to execute
- Checklists for each phase
- Time estimates per phase

## When to Use
- Before starting any new website project
- When creating a repeatable service offering
- When delegating website builds to team members

## Genius Patterns Applied
- Prompt Document as Build Blueprint (#9)
- Tool Specialization Pipeline (#3)
- Progressive Polish Protocol (#6)
