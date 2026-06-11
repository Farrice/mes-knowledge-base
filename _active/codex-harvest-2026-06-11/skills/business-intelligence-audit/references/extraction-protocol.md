# Web Extraction Protocol

> Systematic approach to extracting business intelligence from any website.

---

## Tool Selection

| Site Type | Primary Tool | Backup |
|-----------|--------------|--------|
| Text-heavy (blogs, about pages) | `read_url_content` | - |
| JS-heavy (SPAs, interactive) | `browser_subagent` | - |
| Social media | `browser_subagent` | `search_web` |
| Reviews (G2, Trustpilot) | `read_url_content` | `browser_subagent` |
| LinkedIn | `search_web` | `browser_subagent` (if logged in) |

---

## Standard Extraction Sequence

### 1. Core Website Pages

Extract in this order:

```
1. Homepage (/)
2. About page (/about, /about-us, /our-story)
3. Services/Products (/services, /products, /what-we-do)
4. Pricing (/pricing, if public)
5. Case Studies/Results (/case-studies, /results, /testimonials)
6. Blog (first 3-5 posts for content strategy)
7. Team (/team, /about/team)
8. Contact (/contact)
```

### 2. External Sources

After core website:

```
1. LinkedIn company page
2. LinkedIn founder/CEO profiles
3. Google reviews
4. Industry-specific reviews (G2, Capterra, Trustpilot)
5. Social media (Instagram, Twitter/X, TikTok)
6. Press mentions (search: "company name" + news)
```

---

## Extraction Template

For each URL, extract:

```markdown
## [Page Name] - [URL]

### Key Messages
- Main headline
- Sub-headlines
- Primary CTA

### Claims Made
- What do they promise?
- What results do they cite?
- What proof do they offer?

### Target Audience Signals
- Who do they speak to?
- What problems do they address?
- What language/jargon do they use?

### Gaps/Observations
- What's missing?
- What's confusing?
- What seems weak?
```

---

## Using read_url_content

Best for text extraction:

```
Tool: read_url_content
URL: [target URL]

Returns: Markdown-formatted content with headers, links, and text
```

**Pro tip:** If the content is truncated, use `view_content_chunk` to get additional positions.

---

## Using browser_subagent

Best for visual/interactive sites:

```
Task: Navigate to [URL]. 
1. Wait for page to fully load
2. Extract all visible text content
3. Note the visual layout and design quality
4. Identify key CTAs and their placement
5. Take note of any interactive elements
Return: Summary of page content, design observations, and any conversion elements.
```

**Pro tip:** Use for screenshots, video sales letters, and any page that requires scrolling.

---

## Using search_web

Best for external intelligence:

```
Query: "[company name]" + [modifier]

Modifiers:
- reviews
- complaints
- founder interview
- funding
- competitors
- news
- employee reviews
```

---

## Data Organization

Store extracted data in structured format:

```
.tmp/audit_[company_name]/
├── core_website/
│   ├── homepage.md
│   ├── about.md
│   ├── services.md
│   └── pricing.md
├── social/
│   ├── linkedin.md
│   ├── instagram.md
│   └── twitter.md
├── reviews/
│   ├── google_reviews.md
│   └── g2_reviews.md
└── synthesis/
    ├── key_findings.md
    └── recommendations.md
```

---

## Quality Checks

Before analysis, verify:

- [ ] Homepage extracted
- [ ] Core value proposition identified
- [ ] Target audience clear
- [ ] At least 3 external sources checked
- [ ] Competitor context established

---

*Protocol for business-intelligence-audit skill*
