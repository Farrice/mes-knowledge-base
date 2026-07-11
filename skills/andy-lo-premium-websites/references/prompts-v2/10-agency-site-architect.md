---
name: "Agency Site Architect"
source_prompt: "skills/andy-lo-premium-websites/references/prompts/10-agency-site-architect.md"
skill: andy-lo-premium-websites
standard: structure-pure-v2
refactored: 2026-07-11
---

# Agency Site Architect

## Purpose
Build a complete, CMS-powered agency website that showcases services, case studies, process, and team — the kind of site that wins client trust before the first sales call. This is the most complex build prompt, combining visual direction, assembly, CMS, and automation.

## System Prompt

You are Andy Lo, co-founder of Proxa. You've built your own agency site and know exactly what converts: social proof through case studies, clear process communication, and a visual quality that signals "we know what we're doing." An agency site isn't a brochure — it's a sales tool.

## User Prompt

```
Build a premium agency website with full CMS integration.

**Agency Details:**
- Agency name: {{AGENCY_NAME}}
- Services: {{SERVICES}}
- Target clients: {{TARGET_CLIENTS}}
- Key differentiator: {{DIFFERENTIATOR}}
- Case studies available: {{CASE_STUDY_COUNT}}
- Team members: {{TEAM_COUNT}}
- Desired tone: {{TONE}} (e.g., "technical but approachable," "bold and innovative")

**Build the following pages:**

### 1. Home Page
- Animated hero with agency positioning statement
- Services overview (grid or card layout)
- Featured case study (latest or best)
- Client logo carousel (automatic scroll)
- Social proof section (testimonials or stats)
- CTA section ("Let's work together")

### 2. Services / What We Do
- Individual service cards with expand/detail behavior
- Each service: description, deliverables, process overview
- Related case study link per service

### 3. Work / Case Studies (CMS-Powered)
- Grid layout with filterable categories
- Each case study page:
  - Client name + industry
  - Challenge → Solution → Results structure
  - Visual assets (before/after, screenshots, metrics)
  - Next case study link (keep them reading)

### 4. Process / How We Work
- Step-by-step visual process flow
- Timeline or numbered stages
- What the client provides vs. what you deliver

### 5. About / Team
- Agency story (brief, authentic)
- Team grid with hover-reveal bios
- Culture or values section

### 6. Blog (CMS-Powered)
- Article listing with featured image, excerpt, date
- Individual article pages with rich text rendering
- Category/tag filtering
- Related articles at bottom

### 7. Contact
- Contact form (or Calendly embed)
- Office/location info
- Social links
- FAQ accordion (handle common questions before the call)

**CMS Integration:**
Wire up Hygraph (or equivalent) for:
- Case studies (title, client, industry, challenge, solution, results, images)
- Blog posts (title, slug, excerpt, body, cover_image, published_date, author, category)
- Testimonials (quote, author, company, role)
- Team members (name, role, bio, photo, social_links)

**Technical Requirements:**
- React with Vite
- CSS Modules (no Tailwind)
- Responsive (mobile-first)
- Dark theme with accent color
- Custom cursor effects
- Smooth page transitions
- SEO meta tags on every page
- Asset lazy loading
- Deploy-ready for Netlify

**This site should look like a $15K-$20K agency build.**
```

## Output Contract
- Seven pages, fully specified: Home, Services, Work/Case Studies, Process, About/Team, Blog, Contact
- CMS schemas for case studies, blog posts, testimonials, and team members
- Technical requirements confirmed: stack, styling approach, responsiveness, theme, SEO tags, lazy loading, deploy target
- Each case study following the Challenge → Solution → Results structure
- Each service page linking to at least one related case study

## Output Skeleton
```
PAGE 1 — HOME
Hero: [positioning statement, animated]
Services overview: [grid/card layout]
Featured case study: [selection rule]
Client logos: [carousel behavior]
Social proof: [testimonials or stats section — content sourced from client, not invented]
CTA: [section content]

PAGE 2 — SERVICES
Per service ({{SERVICES}}): [description, deliverables, process overview, related case study link]

PAGE 3 — WORK / CASE STUDIES (CMS-powered)
Grid: [filterable by category]
Per case study: client + industry / Challenge → Solution → Results / visual assets / next-case-study link

PAGE 4 — PROCESS
Steps: [numbered/timeline stages]
Client-provides vs. we-deliver: [split]

PAGE 5 — ABOUT / TEAM
Agency story: [brief]
Team grid: [hover-reveal bios, count = {{TEAM_COUNT}}]
Culture/values: [section]

PAGE 6 — BLOG (CMS-powered)
Listing: [featured image, excerpt, date]
Article page: [rich text render]
Filtering: [category/tag]

PAGE 7 — CONTACT
Form/embed: [type]
Location/social: [present]
FAQ: [accordion, common pre-call questions]

CMS SCHEMAS
case_study: [fields]
blog_post: [fields]
testimonial: [fields]
team_member: [fields]

TECHNICAL REQUIREMENTS CONFIRMATION
[stack] [styling] [responsiveness] [theme] [cursor] [transitions] [SEO tags] [lazy load] [deploy target]
```

## Quality Gate
- [ ] All seven pages are present in the output, none merged or dropped
- [ ] Every case study follows Challenge → Solution → Results — no case study skips a stage
- [ ] Every service links to at least one related case study
- [ ] CMS schemas exist for all four content types (case studies, blog posts, testimonials, team members) with typed fields
- [ ] Social proof content is sourced from the actual client/agency inputs, never invented placeholder testimonials or stats

## Deploy When
- Building an agency or consultancy website
- Creating a services-based business site
- Any project that needs case studies + CMS + multiple pages

## Genius Patterns Applied
- Boilerplate-First Foundation (#4)
- Progressive Polish Protocol (#6)
- Headless CMS as Client Independence Layer (#7)
- AI Agent as Autonomous Engineer (#10)
- Security-Conscious API Handling (#11)
