---
name: content-migration-agent
description: Migrate hardcoded website content to CMS schema programmatically
---

# Content Migration Agent

## Purpose
Take hardcoded content currently embedded in React components or HTML files and migrate it to a headless CMS, replacing static content with dynamic CMS queries. This is the step that transforms a "static site" into a "living site."

## System Prompt

You are Andy Lo. You treat content migration not as tedious manual work but as a systematic transformation. You give the AI agent a clear migration plan, let it execute autonomously, and verify the result. Every piece of hardcoded content becomes a CMS-managed entry.

## User Prompt

```
I need to migrate hardcoded content from my website to the CMS.

**Current State:**
- Project: {{PROJECT_NAME}}
- CMS: {{CMS_CHOICE}} (already integrated via Prompt #5)
- Content currently hardcoded in: {{FILE_LOCATIONS}}

**Migration Plan:**

### Phase 1: Content Audit
Scan all component files and identify every piece of hardcoded content:
- Page headings and subheadings
- Body text / descriptions
- Image URLs and alt text
- Testimonial quotes and attributions
- Case study details
- Blog post content
- Team member bios
- FAQ entries

### Phase 2: Schema Mapping
Map each content item to its CMS schema:
| Hardcoded Content | CMS Model | CMS Field |
|---|---|---|
| (auto-populate from audit) | | |

### Phase 3: CMS Population
For each content item:
1. Create the entry in {{CMS_CHOICE}} with all fields populated
2. Ensure slugs are URL-friendly
3. Upload any associated images to the CMS asset library
4. Publish each entry

### Phase 4: Frontend Swap
For each component containing hardcoded content:
1. Replace static text with CMS query results
2. Add proper loading states
3. Add error fallbacks (show placeholder if CMS is unreachable)
4. Maintain all existing styling and layout

### Phase 5: Verification
- [ ] All hardcoded content identified and mapped
- [ ] CMS entries created with correct data
- [ ] Frontend components fetch from CMS
- [ ] Site renders identically to before migration
- [ ] New content can be added through CMS without code changes
- [ ] Error states work correctly if CMS is temporarily unavailable

**Important:** The site should look EXACTLY the same after migration. The only difference is that content now comes from the CMS instead of being hardcoded. Any visual regression is a bug.
```

## Expected Output
- Content audit spreadsheet
- Complete CMS population
- Updated frontend components
- Zero visual regression

## When to Use
- After CMS integration (Prompt #5) when existing content is hardcoded
- When converting a static site to CMS-managed

## Genius Patterns Applied
- AI Agent as Autonomous Engineer (#10)
- Headless CMS as Client Independence Layer (#7)
