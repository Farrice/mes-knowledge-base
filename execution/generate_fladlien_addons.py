#!/usr/bin/env python3
"""
Generate Crown Jewel prompts for Jason Fladlien's marketing skill.

Uses the shared GeminiClient for consistent API access with thinking mode
enabled for deep extraction analysis.
"""

import asyncio
import sys
from dataclasses import dataclass
from pathlib import Path

# Shared client
sys.path.insert(0, str(Path(__file__).parent))
from gemini_client import GeminiClient, load_env

load_env()

BASE_PATH = Path(__file__).parent.parent


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


def strip_code_fences(text: str) -> str:
    """Remove markdown code block wrappers from API response."""
    lines = text.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines)


async def generate_prompt(prompt_def: PromptDef, extraction_content: str,
                          client: GeminiClient):
    print(f"  ⏳ Generating {prompt_def.slug}...")
    prompt_text = USER_PROMPT_TEMPLATE.format(
        prompt_slug=prompt_def.slug,
        prompt_desc=prompt_def.description,
        extraction_content=extraction_content
    )

    try:
        text, meta = await client.generate(
            prompt_text,
            temperature=0.7,
            max_output_tokens=16384,
            thinking_budget=2048,
        )
        content = strip_code_fences(text)

        output_path = BASE_PATH / "skills" / "jason-fladlien-marketing" / "references" / "prompts" / f"{prompt_def.slug}.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content.strip() + "\n")
        print(f"  ✅ Saved {prompt_def.slug} ({meta.total_tokens} tokens, ${meta.estimated_cost_usd:.4f})")
    except Exception as e:
        print(f"  ❌ Failed {prompt_def.slug}: {e}")


async def main():
    client = GeminiClient()

    extraction_path = BASE_PATH / "extractions" / "Jason Fladlien" / "extraction-report.md"
    if not extraction_path.exists():
        print(f"❌ Extraction not found: {extraction_path}")
        sys.exit(1)
    extraction_content = extraction_path.read_text()

    if len(sys.argv) > 1:
        batch_id = int(sys.argv[1])
        batch = PROMPTS[0:5] if batch_id == 0 else PROMPTS[5:10]
    else:
        batch = PROMPTS

    print(f"Running generation for {len(batch)} prompts (model: {client.default_model})...")
    tasks = [generate_prompt(p, extraction_content, client) for p in batch]
    await asyncio.gather(*tasks)

    usage = client.usage_summary()
    print(f"\nDone! {usage['api_calls']} calls, {usage['total_tokens']} tokens, ${usage['total_cost_usd']:.4f}")


if __name__ == "__main__":
    asyncio.run(main())
