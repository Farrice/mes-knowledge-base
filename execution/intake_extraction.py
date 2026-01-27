#!/usr/bin/env python3
"""
Intake Extraction - Move new extraction to inbox and run initial assessment.

Usage:
    python intake_extraction.py /path/to/extraction.md
    python intake_extraction.py /path/to/extraction.md --assess
    python intake_extraction.py --scan  # Scan Downloads for extractions

This script follows the extraction-workflow.md directive.
"""

import os
import re
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple


# Base paths
BASE_PATH = Path(__file__).parent.parent
EXTRACTIONS_INBOX = BASE_PATH / "knowledge" / "extractions" / "inbox"
DOWNLOADS_PATH = Path.home() / "Downloads"
DESKTOP_PATH = Path.home() / "Desktop"


# Expert detection patterns
EXPERT_PATTERNS = {
    'jeremy-miner': ['jeremy miner', 'nepq', 'sales skill', 'identity persuasion'],
    'michael-bernoff': ['michael bernoff', 'identity engineering', 'reset frame'],
    'harry-dry': ['harry dry', 'marketing examples', 'copywriting'],
    'cardinal-mason': ['cardinal mason', 'ai copywriting', 'conversion'],
    'shaan-puri': ['shaan puri', 'storytelling', 'content strategy'],
    'caleb-ralston': ['caleb ralston', 'personal brand', 'stand out'],
    'dai-media': ['dai media', 'consumer posture', 'identity persona'],
    'mitch-albom': ['mitch albom', 'writing', 'best-seller', 'tuesdays with morrie'],
    'dan-wang': ['dan wang', 'china', 'annual letter'],
    'oscar-hoglund': ['oscar hoglund', 'epidemic sound', 'sound storytelling'],
    'futurepedia': ['futurepedia', 'prompt engineering', 'ai prompting'],
    'nate-b-jones': ['nate b jones', 'jarvis', 'ai failure', 'intent'],
    'darrel-wilson': ['darrel wilson', 'jing', 'ai automation', 'freelancer'],
    'kittl': ['kittl', 'graphic design', 'typography'],
    'erica-mallet': ['erica mallet', 'brand magnetism', 'stop scrolling'],
    'seena-rez': ['seena rez', 'tiktok', 'dropshipping', 'viral'],
    'samuel-thompson': ['samuel thompson', 'info product', 'launch'],
    'jim-oshaughnessy': ["jim o'shaughnessy", 'oshaughnessy', 'philosophy', 'finance'],
    'lulu-cheng-meservey': ['lulu cheng', 'meservey', 'communications', 'pr strategy'],
}


# Tier assignments
TIER_MAPPING = {
    'jeremy-miner': 'Revenue',
    'michael-bernoff': 'Revenue',
    'harry-dry': 'Revenue',
    'cardinal-mason': 'Revenue',
    'samuel-thompson': 'Revenue',
    'shaan-puri': 'Content',
    'caleb-ralston': 'Content',
    'dai-media': 'Content',
    'seena-rez': 'Content',
    'mitch-albom': 'Craft',
    'dan-wang': 'Craft',
    'oscar-hoglund': 'Craft',
    'futurepedia': 'AI',
    'nate-b-jones': 'AI',
    'darrel-wilson': 'AI',
    'kittl': 'Design',
    'erica-mallet': 'Design',
    'jim-oshaughnessy': 'Strategy',
    'lulu-cheng-meservey': 'Strategy',
}


def detect_expert(content: str, filename: str) -> Tuple[str, float]:
    """Detect which expert this extraction is for."""
    combined = (content + filename).lower()

    best_match = None
    best_score = 0

    for expert, patterns in EXPERT_PATTERNS.items():
        score = sum(1 for p in patterns if p in combined)
        if score > best_score:
            best_score = score
            best_match = expert

    confidence = min(best_score / 3.0, 1.0)  # Normalize to 0-1
    return best_match, confidence


def check_extraction_quality(content: str) -> Dict:
    """Check if extraction has expected MES 3.0 components."""
    quality = {
        'has_executive_summary': 'executive summary' in content.lower(),
        'has_genius_patterns': 'genius pattern' in content.lower() or 'pattern' in content.lower(),
        'has_hidden_knowledge': 'hidden knowledge' in content.lower() or 'tacit' in content.lower(),
        'has_methodology': 'methodology' in content.lower() or 'implementation' in content.lower(),
        'has_prompts': 'crown jewel' in content.lower() or 'prompt' in content.lower(),
        'word_count': len(content.split()),
    }

    # Calculate overall quality score
    checks = [quality['has_executive_summary'], quality['has_genius_patterns'],
              quality['has_hidden_knowledge'], quality['has_methodology'], quality['has_prompts']]
    quality['components_found'] = sum(checks)
    quality['quality_score'] = quality['components_found'] / len(checks)

    # Length check
    quality['is_substantial'] = quality['word_count'] > 5000

    return quality


def assess_extraction(filepath: Path) -> Dict:
    """Run full assessment on an extraction file."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    expert, confidence = detect_expert(content, filepath.name)
    quality = check_extraction_quality(content)

    tier = TIER_MAPPING.get(expert, 'Unknown')

    # Determine if agent-worthy
    agent_worthy = (
        quality['quality_score'] >= 0.6 and
        quality['is_substantial'] and
        confidence >= 0.5
    )

    return {
        'filepath': str(filepath),
        'filename': filepath.name,
        'expert_detected': expert,
        'expert_confidence': confidence,
        'tier': tier,
        'quality': quality,
        'agent_worthy': agent_worthy,
        'recommendation': 'Build agent + skill' if agent_worthy else 'Skill only or reference',
    }


def format_assessment_report(assessment: Dict) -> str:
    """Format assessment as readable report."""
    lines = [
        "=" * 60,
        "EXTRACTION ASSESSMENT REPORT",
        "=" * 60,
        f"\nFile: {assessment['filename']}",
        f"Expert Detected: {assessment['expert_detected'] or 'Unknown'}",
        f"Confidence: {assessment['expert_confidence']:.0%}",
        f"Tier: {assessment['tier']}",
        "\n--- Quality Check ---",
        f"Word Count: {assessment['quality']['word_count']:,}",
        f"Is Substantial (>5000 words): {'✅' if assessment['quality']['is_substantial'] else '❌'}",
        f"Has Executive Summary: {'✅' if assessment['quality']['has_executive_summary'] else '❌'}",
        f"Has Genius Patterns: {'✅' if assessment['quality']['has_genius_patterns'] else '❌'}",
        f"Has Hidden Knowledge: {'✅' if assessment['quality']['has_hidden_knowledge'] else '❌'}",
        f"Has Methodology: {'✅' if assessment['quality']['has_methodology'] else '❌'}",
        f"Has Prompts: {'✅' if assessment['quality']['has_prompts'] else '❌'}",
        f"Quality Score: {assessment['quality']['quality_score']:.0%}",
        "\n--- Recommendation ---",
        f"Agent Worthy: {'✅ YES' if assessment['agent_worthy'] else '❌ NO'}",
        f"Action: {assessment['recommendation']}",
        "=" * 60,
    ]
    return '\n'.join(lines)


def scan_for_extractions(directory: Path) -> List[Path]:
    """Scan directory for potential extraction files."""
    extractions = []

    if not directory.exists():
        return extractions

    for file in directory.glob('*.md'):
        # Look for files that appear to be Claude extractions
        if 'claude' in file.name.lower() or 'extraction' in file.name.lower():
            extractions.append(file)
        else:
            # Check content for MES markers
            try:
                with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(1000)  # Read first 1000 chars
                if 'mes 3.0' in content.lower() or 'genius pattern' in content.lower():
                    extractions.append(file)
            except:
                pass

    return extractions


def move_to_inbox(source: Path) -> Path:
    """Move extraction file to inbox."""
    EXTRACTIONS_INBOX.mkdir(parents=True, exist_ok=True)

    dest = EXTRACTIONS_INBOX / source.name

    # Handle duplicates
    if dest.exists():
        stem = source.stem
        suffix = source.suffix
        counter = 1
        while dest.exists():
            dest = EXTRACTIONS_INBOX / f"{stem}_{counter}{suffix}"
            counter += 1

    shutil.copy2(source, dest)
    return dest


def main():
    parser = argparse.ArgumentParser(description='Intake and assess extraction files')
    parser.add_argument('filepath', nargs='?', help='Path to extraction file')
    parser.add_argument('--assess', '-a', action='store_true', help='Run assessment only (no move)')
    parser.add_argument('--scan', '-s', action='store_true', help='Scan Downloads/Desktop for extractions')
    parser.add_argument('--move-all', '-m', action='store_true', help='Move all found extractions to inbox')

    args = parser.parse_args()

    if args.scan:
        print("🔍 Scanning for extraction files...")
        print()

        for directory, name in [(DOWNLOADS_PATH, 'Downloads'), (DESKTOP_PATH, 'Desktop')]:
            extractions = scan_for_extractions(directory)
            if extractions:
                print(f"📁 {name}: {len(extractions)} potential extractions found")
                for ext in extractions:
                    print(f"   📄 {ext.name}")
            else:
                print(f"📁 {name}: No extractions found")

        print("\n💡 Use: python intake_extraction.py /path/to/file.md")
        return

    if not args.filepath:
        print("❌ Please provide a file path or use --scan")
        print("\nUsage:")
        print("  python intake_extraction.py /path/to/extraction.md")
        print("  python intake_extraction.py /path/to/extraction.md --assess")
        print("  python intake_extraction.py --scan")
        return

    filepath = Path(args.filepath)

    if not filepath.exists():
        print(f"❌ File not found: {filepath}")
        return

    print(f"📄 Processing: {filepath.name}")
    print()

    # Run assessment
    assessment = assess_extraction(filepath)
    print(format_assessment_report(assessment))

    # Move to inbox unless assess-only
    if not args.assess:
        dest = move_to_inbox(filepath)
        print(f"\n✅ Moved to inbox: {dest}")

        print("\n📝 Next steps (per extraction-workflow.md):")
        print(f"   1. Review assessment above")
        print(f"   2. If agent-worthy: Build using agents/_framework/AGENT_TEMPLATE.md")
        print(f"   3. Register in COUNCIL.md")
        print(f"   4. Move to knowledge/extractions/processed/ when done")


if __name__ == '__main__':
    main()
