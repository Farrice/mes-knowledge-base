import asyncio
import os
import sys
import json
from dataclasses import dataclass
from typing import List
from google import genai
def load_env_file(filepath=".env"):
    try:
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                key, val = line.split("=", 1)
                key = key.strip()
                val = val.strip().strip("'").strip('"')
                os.environ[key] = val
    except Exception as e:
        print(f"Warning: Could not load {filepath} - {e}")

load_env_file()

@dataclass
class PromptDef:
    slug: str
    description: str

PROMPTS = [
    PromptDef("micro-commitment-funnel-architecture", "Using \"ridiculously small\" behavioral steps to engineer high-ticket sales transitions without friction."),
    PromptDef("invisible-identity-recoding", "Writing content that bypasses behavior change and directly attacks and re-codes the reader's \"I am\" identity."),
    PromptDef("biological-survival-pitching", "Tying the offer to the \"Deepest Truth\" (survival/safety mechanisms) rather than superficial features or benefits."),
    PromptDef("guru-to-the-guru-branding", "Positioning frameworks to artificially detach from the sale, elevating status by serving a \"Higher Purpose\"."),
    PromptDef("frictionless-onboarding-design", "Utilizing \"Success by Subtraction\" to remove every possible point of inertia in the post-purchase experience."),
    PromptDef("conversational-hypnosis-sales-letter", "Writing a long-form VSL/Sales Letter using NLP principles of nested stories to bypass conscious resistance."),
    PromptDef("stoic-marketer-content-pillars", "Content generation framework blending high-level spiritual/stoic detachment with aggressive direct response."),
    PromptDef("procrastination-alchemy-emails", "An email sequence designed to transmute the \"Utility of the Negative\" (anger/shame) into product adoption."),
    PromptDef("radical-candor-launch-strategy", "Launch strategy that uses \"Radical Candor\" on Day 1 to dismantle the \"Con-Man\" frame and build unmatched trust."),
    PromptDef("future-pull-offer-creation", "Designing an offer that builds a \"Future-Pull\" so vivid that the prospect's current identity must shift to attain it.")
]

USER_PROMPT_TEMPLATE = """You are a virtuoso prompt engineer and expert system designer for the Antigravity AI framework.

Based on the complete extraction of Jason Fladlien below, analyze his most powerful methodologies and create a single Crown Jewel virtuoso-level prompt for the following topic:

Topic: {prompt_slug}
Description: {prompt_desc}

YOUR ANALYSIS TASK:
Identify Jason Fladlien's most valuable and unique contributions from the extraction. Intuitively determine what type of prompt would best harness his genius for maximum real-world impact for this specific topic. Consider:
- What made him revolutionary in his field?
- Which methodologies produce the most consistent results?
- What frameworks would be most valuable to replicate and enhance?
- How can we systematize his intuitive genius?
- What would create the biggest competitive advantage when deployed?

FOR THIS CROWN JEWEL PROMPT CREATE THE FOLLOWING SECTIONS:
1. Powerful activation statement that instantly triggers his mindset
2. Core methodologies and frameworks that encode his secret sauce
3. Step-by-step deployment protocol for real-world application
4. Quantified performance metrics (X% improvement, ROI, speed gains)
5. Enhancement layer that surpasses the original expert's limitations
6. Practical use cases for business, personal, and client applications
7. 2 concrete examples (500+ words each) showing viral methodology creating measurable success with specific metrics, templates, and replicable formulas.

Make sure the prompt is 100% self-contained and zero-shot deployable with consistent remarkable and exceptional outcomes and results.

**ULTRA-THINK and Remember to maintain MES 3.0 virtuoso level of excellence with sophisticated depth and nuanced expertise embedded throughout.**
**Formatting for Density**: Dense text requires high-contrast formatting. You MUST aggressively use bullet points, bolding, and whitespace so the density remains readable.
**Anti-Pattern Lock & Gravedigger Safeguard**: Do not lazily map examples to generic consulting frameworks. Demonstrate true creative taste and intuition in your analysis. When discarding the skin of an example to invent a new scenario, explicitly build a human-centric "gravedigger" detail so emotional resonance scales with information density.

Output ONLY the final Markdown content that will be saved to the .md file. Do NOT wrap it in Markdown code fences (```markdown).

EXTRACTION REPORT CONTEXT:
======================================================
{extraction_content}
======================================================
"""

async def generate_prompt(prompt_def: PromptDef, extraction_content: str, model_name: str, client: genai.Client):
    print(f"⏳ Generating {prompt_def.slug}...")
    prompt_text = USER_PROMPT_TEMPLATE.format(
        prompt_slug=prompt_def.slug,
        prompt_desc=prompt_def.description,
        extraction_content=extraction_content
    )
    
    try:
        response = await asyncio.to_thread(
            client.models.generate_content,
            model=model_name,
            contents=prompt_text,
            config=genai.types.GenerateContentConfig(
                temperature=0.7,
            )
        )
        content = response.text
        if content.startswith("```markdown"):
            content = content[11:]
        elif content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]
            
        output_path = f"/Users/farricecain/Google Antigravity/skills/jason-fladlien-marketing/references/prompts/{prompt_def.slug}.md"
        with open(output_path, "w") as f:
            f.write(content.strip() + "\\n")
        print(f"✅ Saved {prompt_def.slug}")
    except Exception as e:
        print(f"❌ Failed {prompt_def.slug}: {e}")

async def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Missing GEMINI_API_KEY")
        sys.exit(1)
        
    client = genai.Client(api_key=api_key)
    model_name = os.environ.get("GEMINI_MODEL", "gemini-3-flash-preview")
    
    with open("/Users/farricecain/Google Antigravity/extractions/Jason Fladlien/extraction-report.md", "r") as f:
        extraction_content = f.read()

    if len(sys.argv) > 1:
        batch_id = int(sys.argv[1])
        if batch_id == 0:
            batch = PROMPTS[0:5]
        else:
            batch = PROMPTS[5:10]
    else:
        batch = PROMPTS
        
    print(f"Running generation for {len(batch)} prompts...")
    tasks = [generate_prompt(p, extraction_content, model_name, client) for p in batch]
    await asyncio.gather(*tasks)
    
    print("Done!")

if __name__ == "__main__":
    asyncio.run(main())
