# Workflow: /riley-brand-asset-scraper

**Tier**: Practitioner  
**Complexity**: Low-Medium  
**Time**: 2-5 minutes  
**Cost**: $0-10 (Firecrawl)  
**APIs**: Firecrawl, Notion  
**Output**: Notion brand kit database (logos, colors, fonts, tone, imagery style)

---

## Pre-Flight Gate

**When to Use**:
- You want to extract brand assets from a competitor's website
- You're building a brand reference library for replication
- You need to identify visual/tone patterns across a competitor ecosystem

**Prerequisites**:
- Firecrawl API key (free tier: 100 pages/month)
- Target company domain(s)
- Notion workspace + integration token

**Don't Use When**:
- Website blocks scraping (robots.txt restriction)
- Brand guide isn't publicly available online (manual fallback needed)
- You need trademarked assets (legal concern; Firecrawl retrieves URLs only)

---

## Skill Acquisition

**Read First**:
1. `genius.md` — Section: "API-First Thinking"
2. `SKILL.md` — Quick Reference: `/riley-brand-asset-scraper`
3. `references/api-integration-guide.md` — Section: "3. Firecrawl API"
4. `references/notion-schema-templates.md` — Section: "Template 1-5: Brand Audit Starter"

**Key Concepts**:
- Firecrawl extracts page HTML + cleaned text + image URLs (not the images themselves)
- CSS parsing can reveal color palettes, font families
- Brand tone is inferred from website copy (homepage, about, value props)
- Notion schema: Logo + Colors + Fonts + Tone + Imagery

---

## Execution

### Step 1: Define Brand Targets

```
Companies to audit:
  1. [Company A] → domain.com
  2. [Company B] → domain.com
  3. [Company C] → domain.com
  ... (up to 5 for thorough audit)
```

### Step 2: Call Firecrawl API to Scrape Brand Website

```bash
curl -H "Authorization: Bearer YOUR_FIRECRAWL_KEY" \
  "https://api.firecrawl.dev/v1/scrape?url=https://domain.com"
```

**Response fields to capture**:
- `html` (full page HTML, for CSS extraction)
- `text` (cleaned page text)
- `images` (list of image URLs)
- `metadata` (title, description, Open Graph tags)

### Step 3: Extract Brand Elements (Python Script)

```python
import firecrawl
import json
import re
from urllib.parse import urljoin

client = firecrawl.Client(api_key="YOUR_FIRECRAWL_KEY")

def extract_brand_assets(domain_url):
    """Scrape domain and extract brand assets."""
    
    # Scrape homepage
    data = client.scrape_url(domain_url)
    
    # Extract colors from CSS
    colors = extract_colors_from_css(data['html'])
    
    # Extract fonts from CSS
    fonts = extract_fonts_from_css(data['html'])
    
    # Extract logo (usually first image in header)
    logo_url = find_logo_in_images(data['images'])
    
    # Extract tone from homepage copy
    tone = infer_tone_from_copy(data['text'])
    
    # Extract imagery style from images
    imagery_style = infer_imagery_style(data['images'])
    
    return {
        "domain": domain_url,
        "logo_url": logo_url,
        "colors": colors,
        "fonts": fonts,
        "tone": tone,
        "imagery_style": imagery_style,
        "metadata": data['metadata']
    }

def extract_colors_from_css(html):
    """Extract color codes from CSS."""
    # Match hex colors (#RRGGBB) and rgb() in CSS
    color_pattern = r'(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}|rgb\([^)]+\))'
    colors = list(set(re.findall(color_pattern, html)))
    
    # Remove duplicates and limit to 5-10 primary colors
    return colors[:10]

def extract_fonts_from_css(html):
    """Extract font families from CSS."""
    font_pattern = r"font-family:\s*([^;}\n]+)"
    fonts = list(set(re.findall(font_pattern, html)))
    
    # Clean up: remove quotes, extract primary font names
    cleaned_fonts = []
    for font in fonts:
        # Extract first font in font-stack (e.g., "'Helvetica Neue', Arial" → "Helvetica Neue")
        primary = font.split(',')[0].strip("\"'")
        if primary and len(primary) > 2:
            cleaned_fonts.append(primary)
    
    return list(set(cleaned_fonts))[:5]

def find_logo_in_images(images):
    """Identify likely logo from images."""
    # Usually logo is in <img> with src="/logo" or "/brand"
    for img_url in images:
        if 'logo' in img_url.lower() or 'brand' in img_url.lower():
            return img_url
    
    # Fallback: assume first image is logo (unreliable, but fallback)
    return images[0] if images else None

def infer_tone_from_copy(text):
    """Infer brand tone from homepage copy."""
    tone_keywords = {
        "Authoritative": ["expert", "leading", "trusted", "industry"],
        "Friendly": ["friendly", "easy", "simple", "help", "love"],
        "Urgent": ["now", "today", "limited", "fast", "immediate"],
        "Inspirational": ["transform", "empower", "believe", "dream", "achieve"]
    }
    
    tone_scores = {}
    text_lower = text.lower()
    
    for tone, keywords in tone_keywords.items():
        score = sum(text_lower.count(kw) for kw in keywords)
        tone_scores[tone] = score
    
    # Return top tone
    if max(tone_scores.values()) > 0:
        return max(tone_scores, key=tone_scores.get)
    return "Professional"

def infer_imagery_style(images):
    """Infer imagery style from image URLs or names."""
    imagery_keywords = {
        "Stock Photos": ["stock", "unsplash", "pexels"],
        "Custom Illustration": ["illustration", "icon", "graphic"],
        "Product Screenshots": ["product", "app", "screenshot"],
        "People/Lifestyle": ["team", "people", "lifestyle", "culture"]
    }
    
    style_scores = {}
    all_image_urls = " ".join(images).lower()
    
    for style, keywords in imagery_keywords.items():
        score = sum(all_image_urls.count(kw) for kw in keywords)
        style_scores[style] = score
    
    # Return top style
    if max(style_scores.values()) > 0:
        return max(style_scores, key=style_scores.get)
    return "Mixed"

# Run extraction for each domain
domains = ["https://domain1.com", "https://domain2.com", "https://domain3.com"]
brand_assets = [extract_brand_assets(domain) for domain in domains]

return brand_assets
```

### Step 4: Create Notion Brand Kit Database

```python
import notion_client

client = notion_client.Client(auth="YOUR_NOTION_TOKEN")

# Create database
db = client.databases.create(
    parent={"page_id": "PARENT_PAGE_ID"},
    title="Brand Asset Database",
    properties={
        "Company": {"title": {}},
        "Domain": {"url": {}},
        "Logo": {"file": {}},
        "Primary Colors": {"rich_text": {}},
        "Secondary Colors": {"rich_text": {}},
        "Font Stack": {"rich_text": {}},
        "Brand Tone": {"select": {"options": [
            {"name": "Authoritative"}, {"name": "Friendly"}, 
            {"name": "Urgent"}, {"name": "Inspirational"}, 
            {"name": "Professional"}, {"name": "Playful"}
        ]}},
        "Imagery Style": {"select": {"options": [
            {"name": "Stock Photos"}, {"name": "Custom Illustration"}, 
            {"name": "Product Screenshots"}, {"name": "People/Lifestyle"}
        ]}},
        "Key Message": {"rich_text": {}},
        "Value Props": {"rich_text": {}},
        "Audit Date": {"date": {}}
    }
)

return db['id']
```

### Step 5: Populate Notion with Brand Assets

```python
import datetime

for brand in brand_assets:
    client.pages.create(
        parent={"database_id": db_id},
        properties={
            "Company": {"title": [{"text": {"content": brand['domain'].replace('https://', '').replace('http://', '')}}]},
            "Domain": {"url": brand['domain']},
            "Primary Colors": {"rich_text": [{"text": {"content": '; '.join(brand['colors'][:3])}}]},
            "Secondary Colors": {"rich_text": [{"text": {"content": '; '.join(brand['colors'][3:])}}]},
            "Font Stack": {"rich_text": [{"text": {"content": ', '.join(brand['fonts'])}}]},
            "Brand Tone": {"select": {"name": brand['tone']}},
            "Imagery Style": {"select": {"name": brand['imagery_style']}},
            "Key Message": {"rich_text": [{"text": {"content": brand['metadata'].get('og:description', 'N/A')[:200]}}]},
            "Audit Date": {"date": {"start": datetime.now().isoformat()}}
        }
    )

print(f"✓ Added {len(brand_assets)} brands to Notion")
```

---

## Content Type Adaptations

### B2B SaaS Brands
- Tone: Authoritative, trustworthy
- Colors: Blues, grays, clean palettes
- Fonts: Sans-serif, modern (e.g., Inter, Montserrat)
- Imagery: Product screenshots, happy customers

### E-commerce / DTC Brands
- Tone: Friendly, urgent
- Colors: Bold, brand-specific (e.g., orange, teal)
- Fonts: Mix of serif (headlines) + sans-serif (body)
- Imagery: Product photos + lifestyle shots

### Creator / Personal Brands
- Tone: Inspirational, relatable
- Colors: Often vibrant, personal preference
- Fonts: Diverse (may mix serif + script)
- Imagery: Headshots, behind-the-scenes content

---

## Output Requirements

**Notion Brand Kit Database**:
- ✓ Logo URLs extracted and validated
- ✓ Primary + secondary colors identified (5-10 colors per brand)
- ✓ Font stack extracted (3-5 fonts per brand)
- ✓ Brand tone inferred from copy
- ✓ Imagery style categorized
- ✓ All fields populated (no gaps)

**Quality Gate**:
- ✓ Logo URL is valid (returns a 200 status)
- ✓ Primary colors are actual brand colors (not random page colors)
- ✓ Fonts are legible + appropriate for industry
- ✓ Brand tone matches perception of brand (sanity check)
- ✓ Imagery style is consistent with brand positioning

**Next Workflows**:
- Feed to design workflows (Satori, Canva)
- Use as reference for brand replication
- Share with creative team for consistency

---

## Quality Gate

**Red Flags** (fail if any):
- [ ] Logo URL is broken or 404
- [ ] Colors include obvious non-brand colors (e.g., white, black only)
- [ ] Font stack is empty or generic (Georgia, Arial only)
- [ ] Brand tone doesn't match actual brand perception
- [ ] Imagery style is misidentified (e.g., saying "illustrations" when it's "stock photos")

**Validation Checklist**:
1. Click logo URL; verify it's the company logo (not a random image)
2. Scan primary colors; are they recognizable as the brand's palette?
3. Visit the actual website; do the extracted fonts match what you see?
4. Read the homepage copy; does inferred tone match your impression?
5. Look at their imagery; is the inferred style accurate?

**Anti-Patterns**:
- Do NOT assume extracted colors are all primary (sort by frequency if possible)
- Do NOT rely solely on CSS (some brands use image-based logos)
- Do NOT confuse tone with industry (a fintech company can be playful)
- Do NOT miss that font-stacks include fallbacks (primary font is first)
- Do NOT scrape brands with robots.txt restrictions (respect robots.txt)

---

## Troubleshooting

**"Firecrawl API returns 403 Forbidden"**
→ Website blocks scraping (robots.txt or firewall). Fallback: manual download of brand guide (often available on company website as PDF).

**"Logo URL is broken"**
→ Firecrawl returns relative URLs. Resolve to absolute: `urljoin(base_url, relative_url)`.

**"Font extraction returns too many fonts"**
→ CSS may include multiple font-stacks. Take top 5 by frequency, then verify against website.

**"Brand tone inference feels wrong"**
→ Homepage copy may not be representative. Try scraping `/about` or `/values` pages for better signal.

---

## Next Steps After Completion

1. **Validate** brand kit in Notion (spot-check 3 brands)
2. **Use** as reference for design work (Satori, Canva)
3. **Compare** brands side-by-side (Notion grouping by Tone or Imagery Style)
4. **Share** with creative team for consistency guidelines
5. **Update** quarterly as brands evolve

**Downstreams**: Design workflows (Satori, Canva), brand replication projects, creative briefs

