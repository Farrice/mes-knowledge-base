---
name: Rank & Rent Asset Generator
description: A complete system for identifying low-competition local niches, generating high-fidelity HTML assets with elevated copy and visuals.
---

# 🏙️ Rank & Rent Asset Generator (v2.0 - Elevated)

> **"Digital Real Estate is the new oil."** – Based on the *Words At Scale* "Locus Pilot" methodology.
> **v2.0 (2026-02-05)**: Engines upgraded with Harry Dry "Concrete Copy" and Oren "Taste Mastery" principles.

This skill upgrades you into a **Digital Landlord**. It provides the intelligence to find "Search Gaps" (weak competitors) and the engineering to instantly build "Asset-Class" websites that conquer those gaps.

## 🧠 The Capabilities

### 1. 🕵️ Market Espionage (The "Spy" Layer)
*Replicates: EMD Striker*
- **Capability**: Analyzes Google SERPs to find "Weak Spots" (forums, directories, outdated sites).
- **Metric**: Uses the **Striker Score** (0-100) to validate if a niche is worth entering.
- **Commands**: `/spy-market`, `/spy-amazon`.

### 2. 🏗️ Asset Construction (The "Locus" Layer)
*Replicates: Locus Pilot*
- **Capability**: Generates "Pure HTML" websites that score 100/100 on Core Web Vitals.
- **Tech**: Zero-JS-Bloat, TailwindCSS, Schema.org LocalBusiness markup.
- **Command**: `/generate-asset`
- **Elevation**: Now accepts researched data for grounded, specific copy.

### 3. 🎨 Visual Packaging (The "Nanobanana" Layer)
*Replicates: Nanobanana / Midjourney*
- **Capability**: Replaces generic stock photos with premium AI-generated imagery.
- **Method**: Agent uses `generate_image` tool with Oren "Taste Mastery" prompts.
- **Elevation**: Prompts optimized for trust signals (uniforms, branded trucks, professional environments).

### 4. ✍️ Copy Engine (The "Harry Dry" Layer)
*Replicates: MarketingExamples.com quality*
- **Capability**: Generates "Concrete Copy" – specific, provable, outcome-focused.
- **Principles**:
  - "On-site in 45 minutes" > "Fast service"
  - "500+ verified reviews" > "Highly rated"
  - "Your pipes fixed" > "Plumbing services"

---

## 🚀 How to Use This Skill

### Phase 1: Reconnaissance
Use the Spy workflows to find a target.
- **Command**: `Run /spy-market`
- **Goal**: Find a keyword where the top result is a Reddit thread or a YellowPages listing.

### Phase 2: Infiltration (Build)
Deploy the asset to capture the flag.
- **Command**: `Run /generate-asset`
- **Input**: "Emergency Plumber", "Seattle", "Seattle Rapid Flow".
- **Elevation**: Add optional research phase for grounded copy.

### Phase 3: Packaging & Deployment
- **Manual Step**: Inspect the `_site/index.html`.
- **Polish**: Ask the Agent to generate AI visuals.
- **Deploy**: Drag and drop to Netlify/Vercel.

## 📂 File Structure
- `generator.py`: The build orchestrator.
- `content_engine.py`: The copywriter (Harry Dry principles).
- `visual_engine.py`: The art director (Oren principles + AI prompts).
- `templates/master_theme.html`: The HTML/Tailwind template.
- `references/genius-patterns.md`: The strategy guide.
