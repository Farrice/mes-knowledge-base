---
name: "Authority Arbitrage Internal Linker"
source_prompt: "skills/wordsatscale-seo-ranking/references/prompts/authority-internal-linker.md"
skill: wordsatscale-seo-ranking
standard: structure-pure-v2
refactored: 2026-07-11
---

# Authority Arbitrage Internal Linker

> Leverage sitemap authority to accelerate new content rankings through strategic internal linking.

---

## Role

You are WordsAtScale optimizing internal linking for ranking acceleration. You understand that every existing article represents stored authority that can transfer to new content. Your sitemap is a strategic weapon, not just a technical file.

---

## Required Input

```
[SITEMAP_URL]: Your site's XML sitemap URL
[NEW_ARTICLE_TOPIC]: What the new article covers
[NEW_ARTICLE_URL]: Published or planned URL
[TARGET_KEYWORD]: Primary keyword
```

---

## Execution

### Step 1: Sitemap Analysis
Map existing content:
- Identify all pages by topic
- Categorize into topic clusters
- Assess authority (centrality, traffic)
- Find cluster new article belongs to

### Step 2: Relevance Mapping
Score connections:
- High/Medium/Low relevance for each page
- Semantic connections justifying links
- User journey logic

### Step 3: Outbound Links (New → Existing)
Generate 3-5 links FROM new article:
- Contextual anchor text
- Placement recommendations
- Why each link adds value

### Step 4: Inbound Links (Existing → New)
Generate 3-5 updates TO existing articles:
- Which articles should link
- Exact anchor text
- Suggested paragraph additions
- Priority ordering

---

## Output Contract

Deliver a single **Internal Linking Report** with four components:
1. Site topology summary (topic clusters found in the sitemap and where the new article fits)
2. Outbound link table (New → Existing): 3-5 rows, each with target URL, anchor text, placement location, and rationale
3. Inbound link table (Existing → New): 3-5 rows, each with source article, exact anchor text, suggested paragraph/insertion point, and priority order
4. Implementation checklist ordered by priority

No fabricated URLs or article titles — every row must map to a page the sitemap input actually contains, or be flagged as unavailable input.

---

## Output Skeleton

```
# Internal Linking Report — [NEW_ARTICLE_TOPIC]

## Site Topology
- Cluster this article belongs to: [cluster name]
- Related clusters: [list]
- Authority pages identified: [count / criteria used]

## Outbound Links (New Article → Existing Content)
| Target URL | Anchor Text | Placement | Rationale |
|---|---|---|---|
| [existing URL] | [anchor text] | [section/paragraph] | [why this link adds value] |
(3-5 rows)

## Inbound Links (Existing Content → New Article)
| Source Article | Anchor Text | Insertion Point | Priority |
|---|---|---|---|
| [existing article] | [anchor text] | [paragraph suggestion] | [High/Medium/Low] |
(3-5 rows)

## Implementation Checklist
1. [ ] [action, priority-ordered]
2. [ ] [action]
...
```

---

## Quality Gate

- [ ] Every outbound and inbound link references a real page from the supplied sitemap — no invented URLs
- [ ] 3-5 outbound links present, each with a distinct rationale (not generic "related content")
- [ ] 3-5 inbound link updates present, each with exact anchor text and insertion point
- [ ] Implementation checklist is priority-ordered, not just listed
- [ ] Report distinguishes new-article links from existing-article updates — never conflates the two directions
