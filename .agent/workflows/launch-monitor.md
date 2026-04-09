---
description: Seena Rez "Early Adopter" Innovation Strategy
---

# 🚀 Seena Rez Launch Monitor

> **Goal**: Replicate the exact process of identifying an "Early Adopter" supply-demand gap from YouTube vlogs.
> **Skill**: `skills/seena_rez_early_adopter`

## Phase 1: Market Selection (The "Growing" Check)
1. **User Input**: Niche (e.g., "Pilates", "Pickleball", "Home Coffee Brewing").
2. **Validation**:
   - Check Google Trends (Must be upward trending 12mo).
   - Check CAGR reports (Is the market growing YoY?).

## Phase 2: The "Day in the Life" Extraction
**Agent Action**:

1. **Pull YouTube videos + transcripts via Apify** (PRIMARY — replaces manual transcript extraction):

   ```bash
   python execution/apify_client.py youtube "[Niche] day in the life" --limit 5 --transcript
   python execution/apify_client.py youtube "[Niche] morning routine" --limit 5 --transcript
   python execution/apify_client.py youtube "[Niche] vlog" --limit 5 --transcript
   ```

   The actor returns video metadata (channel name, sub count, view count) AND the transcript in a single call. Filter for **micro-influencers (10k-100k subs)** — NOT mega celebs.

   **Fallback Contract**: If response contains `{"fallback": true}`, Apify cap is hit. Reroute to:
   - Manual YouTube search via web interface
   - OR `perplexity_ask`: "Find 5 day-in-the-life vlogs from micro-influencers (10k-100k subs) in [Niche]. List video URLs, channel names, and key product mentions."

2. **Analyze the transcripts** (LLM call on the data Apify returned):
   - Prompt: "Identify products mentioned that are being used daily but called by generic names (e.g., 'grippy socks' not 'BrandX'). Look for pain points like 'I wish I had' or 'I finally found'. Cross-reference across all 15 transcripts to find recurring generic-product mentions — those are your supply-demand gap signals."

## Phase 3: Identity & Aesthetics Match
**Agent Action**:
1. Identify the "Avatar" from the videos (e.g., "Clean Girl Aesthetic", "Biohacker Dad").
2. Identify 3 "Love Brands" outside the niche (e.g., "They wear Alo, drink Erewhon, use Dyson").
3. **Visual Strategy**: Define the "Visual API" to copy (Lighting, Colors, Fonts).

## Phase 4: Product Source & Viral Hook
**Agent Action**:
1. Generate the **Manufacturing Spec**: Defines the "Premium" version of the generic product (Materials, Branding placement).
2. Script the **Viral Video** using the 3-Second Rule:
   - 0:00-0:03: Context/Hook.
   - 0:03: Beat Drop + Product Reveal.

## Output
Generate a **Launch Dossier**:
- **The Gap**: "Generic Product" opportunity found.
- **The Evidence**: Verbatim quotes from vloggers.
- **The Avatar**: Identity profile.
- **The Visual Strategy**: Which non-competitor to mirror.
- **The Viral Script**: Second-by-second breakdown.
