import os
import sys
import json
from pathlib import Path
from google import genai
from google.genai import types

# Load env
ENV_PATH = Path("/Users/farricecain/Google Antigravity/.env")
if ENV_PATH.exists():
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())

API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
if not API_KEY:
    print("Error: GEMINI_API_KEY not found in .env")
    exit(1)

def call_gemini(prompt: str, transcript: str):
    client = genai.Client(api_key=API_KEY)
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=[
                prompt,
                f"TRANSCRIPT START\n\n{transcript}\n\nTRANSCRIPT END"
            ],
            config=types.GenerateContentConfig(
                temperature=0.2,
                system_instruction="You are a master knowledge extractor specializing in the MES 3.0 methodology. VIRTUOSO MANDATE: Optimize for extreme Information Density and precision, not just length. Do not output surface-level content. ANTI-PATTERN LOCK: Absorb the mechanics of the requested frameworks but do not lazily mimic structural templates or metaphors. Apply true creative intuition, taste, and paradigm-shifting nuance."
            )
        )
        return response.text
    except Exception as e:
        print(f"Error calling Gemini via SDK: {e}")
        return None

def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_mes_extraction.py <expert_name> <transcript_filepath>")
        sys.exit(1)
        
    expert_name = sys.argv[1]
    transcript_path = Path(sys.argv[2])
    
    # Deriving output path in the same dir
    output_path = transcript_path.parent / "extraction-report.md"
    
    if not transcript_path.exists():
        print(f"Transcript not found at {transcript_path}")
        return
        
    transcript = transcript_path.read_text()
    print(f"Transcript loaded: {len(transcript.split())} words.")
    
    prompt = f"""
Perform a Standard Tier Master Extraction (MES 3.0) on the provided transcript of {expert_name}.
Output your response completely as a Markdown document ready to save as extraction-report.md.

**VIRTUOSO MANDATE & ANTI-PATTERN LOCK**: 
1. Optimize for exact, lethal precision and extreme information density. Do not use 1,000 words if 200 words of profound insight will suffice, but NEVER cut corners to save tokens. **Formatting for Density**: Dense text requires high-contrast formatting. You MUST aggressively use bullet points, bolding, and whitespace so the density remains readable.
2. Beware of "pattern lock". Extract the underlying physics and mental models of the expert, but do not lazily map them to generic consulting frameworks. Demonstrate true creative taste and intuition in your analysis.
3. **The Gravedigger Safeguard (Feeling Density)**: When discarding the skin of an example to invent a new scenario or explain a framework, you must explicitly build a human-centric "gravedigger" detail. Density cannot mean sterile. Concrete emotional resonance must scale with information density.

Analyze the transcript using the 5-layer methodology:
1. Surface Meaning (What are they saying?)
2. Contextual Flow (How is the argument constructed?)
3. Subtextual Motivations (Why do they care/What are the unspoken assumptions?)
4. Hidden Knowledge (What tacit expertise are they using casually?)
5. Deep Meaning/Genius Patterns (What is the core replicable mental model?)

Structure the extraction report exactly following this template:

# {expert_name} — Mastery Extraction

## Content Assessment
Source: Transcript
Expert: {expert_name}
Domain: Marketing, Copywriting, Entrepreneurship
Depth Tier: Standard
Genius Patterns: [Number] identified
Hidden Knowledge: [Number] tacit insights detected
Existing Overlap: [Any existing Antigravity skills in this domain?]

## Executive Summary
- **Core Genius**: [1-2 sentence essence of their unique approach]
- **What Makes Them Different**: [Specific differentiation, not generic praise]
- **Deployable Skills**: [What the user can now execute after this extraction]
- **Hidden Knowledge Captured**: [Tacit insights made explicit]

## Genius Patterns
For each pattern identified:
### [Pattern Name]
- **What They Do Unconsciously**: [The behavior]
- **Executable Behavior**: [Concrete action to replicate]
- **Deployment Context**: [When and where to apply]
- **Success Metric**: [How to know it's working]

## Hidden Knowledge
- **[Insight Name]**: [What they know but don't explain — now made deployable]

## Methodology
[Core methodology organized by progression, focused on what the user will PRODUCE at each level]

## Applied Intelligence
### Capability Unlocks
- **[Capability 1]**: [What you can now build/do that you couldn't before]
- **[Capability 2]**: [New decision-making ability or framework]
- **[Capability 3]**: [Product, agent, or workflow this enables]

## Implementation Pathway
- **24-Hour Quickstart**: [First deployment activities]
- **7-Day Sprint**: [Core capability milestones]
- **30-Day Integration**: [Full system deployment]

Emphasize a practitioner-first mode. This extraction must yield production-grade frameworks that can be directly mapped to an AI agent and skill repository. Focus on copywriting, persuasion, high-status positioning, and NLP. Do not write anything outside of the markdown document (e.g., no conversational intro/outro).
"""
    
    print("Calling Gemini API...")
    report = call_gemini(prompt, transcript)
    
    if report:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        # Clean up any wrapping markdown code blocks from the API response
        if report.startswith("```md") or report.startswith("```markdown"):
            lines = report.splitlines()
            if lines[0].startswith("```"):
                report = "\n".join(lines[1:])
            if report.endswith("```"):
                report = report[:-3]
        elif report.startswith("```"):
            lines = report.splitlines()
            if lines[0].startswith("```"):
                report = "\n".join(lines[1:])
            if report.endswith("```"):
                report = report[:-3]
                
        output_path.write_text(report.strip() + "\n")
        print(f"Successfully generated extraction report at {output_path}")

if __name__ == "__main__":
    main()
