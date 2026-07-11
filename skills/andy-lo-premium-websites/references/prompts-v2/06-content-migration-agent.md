---
name: "Content Migration Agent"
source_prompt: "skills/andy-lo-premium-websites/references/prompts/06-content-migration-agent.md"
skill: andy-lo-premium-websites
standard: structure-pure-v2
refactored: 2026-07-11
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

## Output Contract
- A content audit record (spreadsheet or table) enumerating every hardcoded content item found, one row per item, with its source file/location
- A schema mapping table linking each audited item to its target CMS model + field
- A populated CMS instance: one entry per audited content item, all fields filled, slugs URL-friendly, images uploaded to the CMS asset library, entries published
- Updated frontend components: static text/markup replaced with CMS queries, each with a loading state and an error fallback
- A verification pass confirming zero visual regression against the pre-migration site

## Output Skeleton
```
CONTENT AUDIT
| Location (file/component) | Content Type | Current Value (reference only, not reproduced) |
|---|---|---|
[one row per hardcoded content item found — headings, body text, image URLs/alt text, testimonials, case studies, blog posts, bios, FAQ entries]

SCHEMA MAPPING
| Hardcoded Content | CMS Model | CMS Field |
|---|---|---|
[one row per audited item, mapped to its destination model/field]

CMS POPULATION LOG
- [Model/Entry name]: created, fields populated, slug set, images uploaded, published — [pass/fail]
[repeat per entry]

FRONTEND SWAP LOG
- [Component/file]: static content replaced with CMS query, loading state added, error fallback added — [pass/fail]
[repeat per component]

VERIFICATION CHECKLIST RESULT
- [ ] All hardcoded content identified and mapped
- [ ] CMS entries created with correct data
- [ ] Frontend components fetch from CMS
- [ ] Site renders identically to before migration
- [ ] New content can be added through CMS without code changes
- [ ] Error states work correctly if CMS is temporarily unavailable
```

## Quality Gate
- [ ] Every hardcoded content item found in {{FILE_LOCATIONS}} appears in the audit — none skipped
- [ ] Every audited item has a corresponding CMS model/field mapping before population begins
- [ ] Every CMS entry is published (not left as draft) and has a URL-friendly slug
- [ ] Every swapped component has both a loading state and an error fallback for CMS unavailability
- [ ] The site renders identically pre- and post-migration — any visual difference is treated as a bug, not an acceptable tradeoff
- [ ] New content can subsequently be added through the CMS alone, with zero code changes required

## Deploy When
- After CMS integration (Prompt #5) when existing content is hardcoded
- When converting a static site to CMS-managed

## Genius Patterns Applied
- AI Agent as Autonomous Engineer (#10)
- Headless CMS as Client Independence Layer (#7)
