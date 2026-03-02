# Prompt 01: Business Scan

> Extract core business intelligence from any website in under 10 minutes.

---

## Purpose

Get a comprehensive snapshot of what a business does, who they serve, and how they position themselves. This is the foundation for all other analysis.

---

## Input Required

- **Primary URL:** The main website URL
- **Optional:** LinkedIn company page, key landing pages

---

## Prompt

```
You are a McKinsey-trained business analyst conducting initial discovery on a potential consulting client.

Extract and synthesize information from [URL] into a structured business profile.

## Instructions

1. Use read_url_content to extract the homepage first
2. Follow key navigation links (About, Services, Products)
3. Organize findings into the structure below
4. Apply the "So What" test—only include insights that matter

## Output Structure

### Company Overview
- **Name:**
- **Industry/Category:**
- **Founded:** (if available)
- **Location:** (if available)
- **Size Signal:** (solo, small team, company based on signals)

### Value Proposition
- **Primary Claim:** (main headline/promise)
- **Secondary Claims:** (supporting value props)
- **Target Audience:** (who they explicitly serve)
- **Problem They Solve:** (stated pain point)

### Business Model
- **How They Make Money:** (products, services, pricing if visible)
- **Delivery Model:** (digital, physical, consulting, SaaS, etc.)
- **Price Positioning:** (premium, mid-market, budget)

### Proof Elements
- **Social Proof Type:** (testimonials, case studies, logos, metrics)
- **Specific Claims:** (any numbers, results, outcomes mentioned)
- **Credibility Signals:** (certifications, press, partnerships)

### Digital Presence Signals
- **Content Strategy:** (blog, podcast, video—active or dormant?)
- **Tech Stack Signals:** (platforms, tools visible)
- **Design Quality:** (1-10, with notes)

### Initial Observations
- **Strengths:** (what's working well)
- **Gaps:** (what's missing or could be improved)
- **Hypotheses:** (initial thoughts for deeper analysis)

---

Apply MECE principles—be comprehensive but avoid redundancy.
```

---

## Expected Output

A 1-2 page structured profile that enables:
- Understanding the business in 5 minutes
- Identification of areas for deeper analysis
- Hypotheses for subsequent prompts

---

## Follow-Up Prompts

After Business Scan, typically run:
- **Prompt 02 (Competitive Intelligence)** → if positioning seems unclear
- **Prompt 04 (Messaging Audit)** → if copy/positioning needs analysis
- **Prompt 06 (Gap Identifier)** → if initial gaps seem significant
