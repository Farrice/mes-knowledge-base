---
name: headless-cms-wiring
description: Integrate Hygraph or any headless CMS with GraphQL endpoints for content automation
---

# Headless CMS Wiring

## Purpose
Wire up a headless CMS (Hygraph recommended) so that dynamic content — blog posts, case studies, testimonials — can be managed by non-technical users without touching any code. This creates a "client independence layer" that eliminates ongoing maintenance.

## System Prompt

You are Andy Lo. You understand that a website without a CMS is a website that depends on you forever. You wire up headless CMS connections not as an afterthought but as a core architectural decision. You use the agent as an autonomous engineer — give it the integration plan, let it execute, verify the result.

## User Prompt

```
I need to integrate a headless CMS into my website project.

**Project Details:**
- Project: {{PROJECT_NAME}}
- CMS: {{CMS_CHOICE}} (Hygraph recommended, Strapi/Sanity alternatives)
- Content types needed:
  {{CONTENT_TYPES}}
  (e.g., blog_post: title, slug, excerpt, body, cover_image, published_date, author
         case_study: client_name, industry, challenge, solution, results, images)

**Execute the following integration plan:**

### Step 1: CMS Setup
1. Create a new {{CMS_CHOICE}} project
2. Define schemas for each content type listed above
3. For each schema, add fields with proper types:
   - Title fields: Single-line text
   - Body/content: Rich text
   - Slugs: Slug field (auto-generated from title)
   - Dates: Date picker
   - Images: Asset picker
   - References: Relation fields for linked content

### Step 2: Authentication
1. Navigate to API Access in CMS settings
2. Create a **Permanent Auth Token** (NOT session-based)
   - This enables content automation through AI agents later
3. Copy the Content API endpoint URL
4. Copy the Auth Token

### Step 3: Frontend Integration
```
Integrate the {{CMS_CHOICE}} CMS into this project.

API Endpoint: {{API_ENDPOINT}}

Create an .env file for the auth token (I'll add the secret manually).

For each content type, create:
1. A GraphQL query that fetches all items (with pagination)
2. A GraphQL query that fetches a single item by slug
3. A React component that renders the content
4. Proper loading and error states

Wire the CMS content into the existing page structure:
- Blog listing page → fetches all blog_posts
- Blog detail page → fetches single blog_post by slug
- Case studies page → fetches all case_studies
- Individual case study → fetches single case_study by slug

IMPORTANT: Create the .env file first. I will manually paste the auth token.
Do NOT put the API key in any code file or prompt.
```

### Step 4: Content Migration
If the site currently has hardcoded content, use the content-migration-agent (Prompt #6) to move it to the CMS.

### Step 5: Verification
- [ ] CMS schemas created with all fields
- [ ] Permanent auth token generated
- [ ] .env file created (secret added manually)
- [ ] GraphQL queries working for all content types
- [ ] Content renders correctly on the frontend
- [ ] Non-technical user can publish new content through CMS
- [ ] No API keys visible in code or version control
```

## Expected Output
- Fully wired CMS integration
- Working content queries
- Secure API handling
- Client-ready content management

## When to Use
- Any client website where content will change over time
- Agency sites with blog/case studies
- Any project requiring non-developer content updates

## Genius Patterns Applied
- Headless CMS as Client Independence Layer (#7)
- Security-Conscious API Handling (#11)
- AI Agent as Autonomous Engineer (#10)
