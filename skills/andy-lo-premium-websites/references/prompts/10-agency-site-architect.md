---
name: agency-site-architect
description: Build a complete agency website with case studies, process pages, and CMS
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

## Expected Output
- Complete 7-page agency website
- Full CMS integration for dynamic content
- Responsive, performant, deploy-ready

## When to Use
- Building an agency or consultancy website
- Creating a services-based business site
- Any project that needs case studies + CMS + multiple pages

## Genius Patterns Applied
- Boilerplate-First Foundation (#4)
- Progressive Polish Protocol (#6)
- Headless CMS as Client Independence Layer (#7)
- AI Agent as Autonomous Engineer (#10)
- Security-Conscious API Handling (#11)
