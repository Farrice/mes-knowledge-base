---
name: "Headless CMS Wiring"
source_prompt: "skills/andy-lo-premium-websites/references/prompts/05-headless-cms-wiring.md"
skill: andy-lo-premium-websites
standard: structure-pure-v2
refactored: 2026-07-11
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

## Output Contract
- A CMS schema definition for every content type listed in {{CONTENT_TYPES}}, with correctly typed fields (text, rich text, slug, date, asset, relation)
- An authentication setup using a permanent (non-session) auth token, with endpoint URL and token captured
- An .env file created BEFORE any secret is pasted in — no API key ever appears in code, prompts, or version control
- Per content type: a list-fetch GraphQL query (paginated), a single-item-by-slug query, a rendering component, loading and error states
- Page-level wiring connecting each CMS-backed page to its query
- A completed verification checklist

## Output Skeleton
```
CMS SCHEMA
[content type name]: [field name]:[field type], [field name]:[field type], ...
[repeat per content type in {{CONTENT_TYPES}}]

AUTHENTICATION
Token type: Permanent (non-session)
Endpoint: [captured, not hardcoded into prompts]
Token storage: .env only

FRONTEND INTEGRATION (per content type)
- List query: [paginated, fetches all items]
- Single query: [fetches by slug]
- Component: [renders content, has loading state, has error state]

PAGE WIRING
- [page]: [query it consumes]
[repeat per page]

VERIFICATION CHECKLIST RESULT
- [ ] CMS schemas created with all fields
- [ ] Permanent auth token generated
- [ ] .env file created (secret added manually)
- [ ] GraphQL queries working for all content types
- [ ] Content renders correctly on the frontend
- [ ] Non-technical user can publish new content through CMS
- [ ] No API keys visible in code or version control
```

## Quality Gate
- [ ] Every content type in {{CONTENT_TYPES}} has a complete schema with correctly typed fields — none left generic
- [ ] The auth token is permanent, not session-based, and is never pasted into a prompt or code file
- [ ] The .env file is created before the token is added, in that order
- [ ] Every content type has both a list query and a single-item query, each with loading and error states
- [ ] The verification checklist is fully checked, not partially, before the integration is considered done

## Deploy When
- Any client website where content will change over time
- Agency sites with blog/case studies
- Any project requiring non-developer content updates

## Genius Patterns Applied
- Headless CMS as Client Independence Layer (#7)
- Security-Conscious API Handling (#11)
- AI Agent as Autonomous Engineer (#10)
