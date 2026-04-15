#!/usr/bin/env python3
"""
Creative Design Generator — Art Direction + Nano Banana 2 Pipeline

End-to-end creative asset generation:
1. Takes a concept/brief as input
2. Uses Gemini to apply creative direction intelligence (visual language, art movements,
   composition, color theory, typography) to generate a world-class prompt
3. Feeds that prompt into Nano Banana 2 for actual image generation
4. Optionally iterates with creative review

This bridges the Creative Director agent's knowledge with actual pixel output.

Usage:
    python generate_design.py "streetwear tee graphic for an EDM brand called My.BPM"
    python generate_design.py --style "cyberpunk" --aspect 9:16 "album cover for electronic music"
    python generate_design.py --type logo --aspect 1:1 "minimalist gravity-defying logo"
    python generate_design.py --type apparel --style "vintage-bootleg" "band tee for a DJ collective"
    python generate_design.py --prompt-only "mood board reference for luxury streetwear"
    python generate_design.py --iterate 3 "hero image for product launch campaign"
"""

import asyncio
import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from gemini_client import GeminiClient, load_env

load_env()

OUTPUT_DIR = Path(__file__).parent.parent / "deliverables" / "designs"

# Creative Director system instruction — compressed from genius.md
CREATIVE_DIRECTOR_SYSTEM = """You are an elite creative director generating production-ready AI image prompts.

## Your Decision Framework
1. Clarify the brief — message, audience, medium, emotional target
2. Establish concept — Visual Hook + Emotional Core + Cultural Anchor
3. Choose aesthetic — specific art movement, style, or cultural reference
4. Define visual language — shot types, lighting, color, typography, composition
5. Write the prompt — production-ready with all technical parameters

## Prompt Formula (Nano Banana 2 / Gemini Image Generation)
Structure: [DETAILED SUBJECT], [PRECISE ENVIRONMENT], [SPECIFIC LIGHTING with direction], [CAMERA: lens, aperture], [COLOR TEMPERATURE], [MOOD/ATMOSPHERE], [STYLE REFERENCE]

## Rules
- NEVER use vague words: "beautiful," "nice," "cool," "amazing," "stunning"
- Specificity > length: "85mm f/1.4 lens" > "beautiful blurry background"
- Reference real movements, directors, brands, photographers
- Include technical specs: camera settings, color hex codes, specific fonts
- Front-load the subject — most important element first
- Describe light direction, not mood: "warm golden backlight at 45 degrees" > "beautiful lighting"

## Design Type Frameworks

### For Apparel/Streetwear Graphics:
Apply the 5 Streetwear Graphic Archetypes:
1. Logo Play — minimal, logo-centric, power through recognition
2. Vintage Bootleg — appropriated imagery, distressed, nostalgic
3. Art Piece — original illustration as centerpiece
4. Typography Statement — text-driven, bold, provocative
5. Pattern/All-Over — repeating motif

### For Logos:
Consider geometric sans (Futura, Gotham) for modern, slab serif (Rockwell) for industrial,
modern serif (Didot, Bodoni) for luxury. Include negative space strategy.

### For Campaign/Hero Images:
Apply the Three Anchors: Visual Hook + Emotional Core + Cultural Anchor.
Reference specific art movements (25+ available: Bauhaus, Art Deco, Swiss, Pop Art, Cyberpunk, etc.)

### For Product Photography:
Use photorealistic specs: "Canon EOS R5, 85mm f/1.4, ISO 200, white cyclorama studio"

## Color Psychology Quick Reference
Red = passion/power (Supreme), Black = luxury/mystery (Off-White), Blue = trust/calm,
Yellow = energy/optimism, Green = growth/nature, Purple = royalty/creativity

## The Virgil Test (apply to every prompt)
- Does it have tension? (harmony = boring)
- Is there a specific cultural reference?
- Can you explain the concept in one sentence?
- Would removing any element make it stronger?
"""

PROMPT_GENERATION_TEMPLATE = """Generate a production-ready image prompt for Nano Banana 2 (Gemini image generation).

CONCEPT: {concept}
TYPE: {design_type}
STYLE PREFERENCE: {style}
ASPECT RATIO: {aspect}

Generate EXACTLY this JSON structure:
{{
    "concept_name": "Short creative name for this direction",
    "thesis": "One sentence describing the concept",
    "three_anchors": {{
        "visual_hook": "What grabs attention first",
        "emotional_core": "The feeling it sustains",
        "cultural_anchor": "The reference that creates meaning"
    }},
    "prompt": "The complete, production-ready prompt for image generation. Be extremely specific about subject, environment, lighting (direction + quality), camera/lens, color palette (hex codes), composition, style references, and mood. This prompt will be fed DIRECTLY to the AI image model.",
    "negative_elements": "What to avoid in the generation",
    "art_direction_notes": "Brief creative rationale — why these choices serve the brief"
}}

Remember: The prompt must be specific enough that a different creative director would generate a nearly identical image from it alone. No vague descriptors."""

REVIEW_TEMPLATE = """You generated this image from this prompt. Review it as a senior creative director.

ORIGINAL CONCEPT: {concept}
PROMPT USED: {prompt}

Evaluate against the Virgil Test:
1. Tension — is there visual or conceptual friction?
2. Cultural anchor — is there a specific, nameable reference?
3. One-sentence concept — can you explain what this IS?
4. Subtraction — would removing any element make it stronger?

Then provide a REVISED prompt that addresses any weaknesses. Return JSON:
{{
    "virgil_test": {{
        "tension": "pass/fail + reason",
        "cultural_anchor": "pass/fail + reason",
        "one_sentence": "pass/fail + the sentence",
        "subtraction": "pass/fail + what to remove or keep"
    }},
    "score": 1-10,
    "improvements": ["specific change 1", "specific change 2"],
    "revised_prompt": "The improved prompt incorporating feedback"
}}"""


def _parse_json_response(text: str) -> dict:
    """Parse JSON from model output, handling code blocks and extra whitespace."""
    import re
    text = text.strip()
    # Try direct parse first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Try extracting from markdown code block
    match = re.search(r'```(?:json)?\s*(.*?)\s*```', text, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    # Try finding first { to last }
    start = text.find('{')
    end = text.rfind('}')
    if start != -1 and end != -1 and end > start:
        return json.loads(text[start:end + 1])
    raise ValueError("No valid JSON found in response")


async def generate_design(
    concept: str,
    design_type: str = "general",
    style: str = "auto",
    aspect_ratio: str = "1:1",
    resolution: str = "1K",
    output_path: str = None,
    prompt_only: bool = False,
    iterate: int = 1,
    reference_paths: list = None,
):
    """Full creative design pipeline: concept -> art direction -> image generation."""
    client = GeminiClient()

    print(f"\n{'='*60}")
    print(f"CREATIVE DESIGN GENERATOR")
    print(f"{'='*60}")
    print(f"Concept:    {concept}")
    print(f"Type:       {design_type}")
    print(f"Style:      {style}")
    print(f"Aspect:     {aspect_ratio}")
    print(f"Resolution: {resolution}")
    print(f"Iterations: {iterate}")
    print(f"{'='*60}\n")

    # --- Phase 1: Creative Direction (prompt engineering) ---
    print("[1/3] Generating creative direction...")

    direction_prompt = PROMPT_GENERATION_TEMPLATE.format(
        concept=concept,
        design_type=design_type,
        style=style,
        aspect=aspect_ratio,
    )

    direction_text, dir_meta = await client.generate(
        direction_prompt,
        system_instruction=CREATIVE_DIRECTOR_SYSTEM,
        model="flash",
        temperature=0.8,
        max_output_tokens=4096,
        response_mime_type="application/json",
    )

    try:
        direction = _parse_json_response(direction_text)
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Failed to parse creative direction: {e}")
        print(f"Raw output (first 500 chars):")
        print(direction_text[:500])
        return None

    image_prompt = direction.get("prompt", "")

    print(f"\n  Concept: {direction.get('concept_name', 'N/A')}")
    print(f"  Thesis:  {direction.get('thesis', 'N/A')}")
    anchors = direction.get("three_anchors", {})
    print(f"  Visual Hook:    {anchors.get('visual_hook', 'N/A')}")
    print(f"  Emotional Core: {anchors.get('emotional_core', 'N/A')}")
    print(f"  Cultural Anchor: {anchors.get('cultural_anchor', 'N/A')}")
    print(f"\n  Prompt ({len(image_prompt)} chars):")
    print(f"  {image_prompt[:200]}...")
    print(f"\n  Direction cost: ${dir_meta.estimated_cost_usd:.4f} ({dir_meta.total_tokens:,} tokens)")

    if prompt_only:
        print(f"\n{'='*60}")
        print("PROMPT ONLY MODE — No image generation")
        print(f"{'='*60}")
        print(f"\nFull prompt:\n{image_prompt}")
        print(f"\nNegative: {direction.get('negative_elements', 'N/A')}")
        print(f"\nArt direction: {direction.get('art_direction_notes', 'N/A')}")

        # Save prompt to file
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        slug = concept[:30].lower().replace(" ", "_")
        slug = "".join(c for c in slug if c.isalnum() or c in "_-")
        prompt_path = OUTPUT_DIR / f"{timestamp}_{slug}_prompt.json"
        prompt_path.write_text(json.dumps(direction, indent=2))
        print(f"\nSaved to: {prompt_path}")
        return direction

    # --- Phase 2: Image Generation ---
    current_prompt = image_prompt
    final_path = None

    for iteration in range(iterate):
        iter_label = f"[2/3] Generating image" + (f" (iteration {iteration + 1}/{iterate})" if iterate > 1 else "") + "..."
        print(f"\n{iter_label}")

        images, img_meta = await client.generate_image(
            current_prompt,
            aspect_ratio=aspect_ratio,
            image_size=resolution,
            reference_image_paths=reference_paths,
        )

        if not images:
            print("  No images generated. Model may have declined the prompt.")
            print("  Try adjusting the concept or style.")
            return None

        # Save image
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        slug = concept[:30].lower().replace(" ", "_")
        slug = "".join(c for c in slug if c.isalnum() or c in "_-")

        if output_path and iteration == iterate - 1:
            save_path = Path(output_path)
        else:
            suffix = f"_v{iteration + 1}" if iterate > 1 else ""
            save_path = OUTPUT_DIR / f"{timestamp}_{slug}{suffix}.png"

        save_path.parent.mkdir(parents=True, exist_ok=True)
        save_path.write_bytes(images[0])
        final_path = save_path

        print(f"  Saved: {save_path}")
        print(f"  Generation cost: ${img_meta.estimated_cost_usd:.4f} ({img_meta.total_tokens:,} tokens)")

        # --- Phase 3: Creative Review (if iterating) ---
        if iteration < iterate - 1:
            print(f"\n[3/3] Creative review (iteration {iteration + 1})...")

            review_prompt = REVIEW_TEMPLATE.format(
                concept=concept,
                prompt=current_prompt,
            )

            review_text, rev_meta = await client.generate(
                review_prompt,
                system_instruction=CREATIVE_DIRECTOR_SYSTEM,
                model="flash",
                temperature=0.7,
                max_output_tokens=1024,
                response_mime_type="application/json",
            )

            try:
                review = _parse_json_response(review_text)
            except (json.JSONDecodeError, ValueError):
                print("  Could not parse review. Keeping current prompt.")
                continue

            score = review.get("score", 0)
            print(f"  Score: {score}/10")
            for imp in review.get("improvements", []):
                print(f"    - {imp}")

            if score >= 8:
                print(f"  Score >= 8 — stopping iteration early.")
                break

            revised = review.get("revised_prompt", "")
            if revised:
                current_prompt = revised
                print(f"  Revised prompt applied for next iteration.")
            print(f"  Review cost: ${rev_meta.estimated_cost_usd:.4f}")

    # --- Summary ---
    total_cost = client.total_cost_usd
    print(f"\n{'='*60}")
    print(f"DESIGN COMPLETE")
    print(f"{'='*60}")
    print(f"Final image: {final_path}")
    print(f"Total API calls: {client.call_count}")
    print(f"Total tokens: {client.total_tokens_used:,}")
    print(f"Total cost: ${total_cost:.4f}")
    print(f"{'='*60}")

    # Save metadata alongside the image
    if final_path:
        meta_path = final_path.with_suffix(".json")
        meta_data = {
            "concept": concept,
            "design_type": design_type,
            "style": style,
            "aspect_ratio": aspect_ratio,
            "resolution": resolution,
            "creative_direction": direction,
            "final_prompt": current_prompt,
            "iterations": min(iteration + 1, iterate),
            "total_cost_usd": round(total_cost, 4),
            "total_tokens": client.total_tokens_used,
            "output_path": str(final_path),
        }
        meta_path.write_text(json.dumps(meta_data, indent=2))
        print(f"Metadata:    {meta_path}")

    return final_path


def main():
    parser = argparse.ArgumentParser(
        description="Creative Design Generator — Art Direction + Nano Banana 2",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_design.py "streetwear tee for My.BPM EDM brand"
  python generate_design.py --type logo --aspect 1:1 "minimalist gravity logo"
  python generate_design.py --type apparel --style vintage-bootleg "DJ collective merch"
  python generate_design.py --style cyberpunk --aspect 16:9 "hero banner for AI agency"
  python generate_design.py --prompt-only "luxury streetwear campaign hero"
  python generate_design.py --iterate 3 "album cover for electronic artist"
  python generate_design.py --reference style.png "product in this exact style"

Design Types:
  general     Any creative asset (default)
  logo        Logo / brand mark / icon
  apparel     T-shirt, hoodie, hat graphic (streetwear-optimized)
  campaign    Campaign hero image / key visual
  social      Social media asset (post, story, banner)
  product     Product photography / mockup
  editorial   Editorial / fashion photography
  pattern     Repeating pattern / all-over print
  poster      Poster / print / wall art

Style Presets:
  auto              Let the creative director decide (default)
  cyberpunk         Neon noir, tech dystopian
  swiss             Clean grids, Helvetica, minimal
  streetwear        Bold, high-contrast, edge
  vintage-bootleg   Distressed, nostalgic, appropriated
  brutalist         Raw, anti-beauty, exposed
  luxury            Elegant, restrained, premium
  vaporwave         Retro-futurism, pastels, glitch
  afrofuturism      African heritage + sci-fi, cosmic
        """
    )
    parser.add_argument("concept", help="Description of what to create")
    parser.add_argument("--type", "-t", default="general",
                        choices=["general", "logo", "apparel", "campaign", "social",
                                "product", "editorial", "pattern", "poster"],
                        help="Design type (default: general)")
    parser.add_argument("--style", "-s", default="auto",
                        help="Style preset or custom aesthetic direction")
    parser.add_argument("--aspect", "-a", default="1:1",
                        choices=["1:1", "16:9", "9:16", "4:3", "3:4"],
                        help="Aspect ratio (default: 1:1)")
    parser.add_argument("--resolution", default="1K",
                        choices=["1K", "2K", "4K"],
                        help="Output resolution (default: 1K)")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--prompt-only", action="store_true",
                        help="Generate creative direction and prompt only, no image")
    parser.add_argument("--iterate", "-i", type=int, default=1,
                        help="Number of generate-review-revise iterations (default: 1)")
    parser.add_argument("--reference", "-r", action="append",
                        help="Reference image path(s) for style consistency")

    args = parser.parse_args()

    result = asyncio.run(generate_design(
        args.concept,
        design_type=args.type,
        style=args.style,
        aspect_ratio=args.aspect,
        resolution=args.resolution,
        output_path=args.output,
        prompt_only=args.prompt_only,
        iterate=args.iterate,
        reference_paths=args.reference,
    ))

    if not result:
        sys.exit(1)


if __name__ == "__main__":
    main()
