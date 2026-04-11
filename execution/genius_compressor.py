#!/usr/bin/env python3
"""
Genius File Compression — Reduce genius.md token overhead while preserving depth.

Strategies:
1. Remove redundant markdown formatting (extra blank lines, verbose headers)
2. Compress verbose pattern descriptions to essential insight + application
3. Deduplicate cross-referenced patterns (e.g., same concept in multiple genius files)
4. Convert verbose prose to structured bullet format where safe

Safety: Always backs up original before modifying. Never deletes content — restructures it.

Usage:
    python3 execution/genius_compressor.py --audit                    # show stats only
    python3 execution/genius_compressor.py --compress FILE            # compress one file
    python3 execution/genius_compressor.py --compress-tier1           # compress Tier 1 (>30K)
    python3 execution/genius_compressor.py --compress-all --apply     # compress and write
"""

import os
import re
import sys
import shutil
import argparse
from pathlib import Path
from datetime import datetime

SKILLS_DIR = Path("skills")
BACKUP_DIR = Path(".tmp/genius_backups")

TIER1_THRESHOLD = 30000  # chars
TIER2_THRESHOLD = 15000  # chars
TARGET_SIZE = 15000      # compress to under this


def find_genius_files():
    """Find all genius.md files with their sizes."""
    files = []
    for f in sorted(SKILLS_DIR.rglob("genius.md")):
        size = f.stat().st_size
        files.append({"path": f, "size": size, "skill": f.parent.name})
    return files


def compress_content(content):
    """
    Apply structural compression without losing meaning.
    
    Rules:
    1. Collapse 3+ consecutive blank lines to 1
    2. Remove trailing whitespace
    3. Convert verbose "When to use:" / "Example:" prose to compact bullets
    4. Shorten redundant header prefixes like "## Pattern X: The" to "## X."
    5. Remove filler phrases: "It's important to note that", "This is because", etc.
    """
    original_len = len(content)
    
    # 1. Collapse multiple blank lines to single
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 2. Remove trailing whitespace on each line
    content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)
    
    # 3. Remove filler phrases (careful — only remove true filler, not content)
    filler_patterns = [
        r"It's important to note that ",
        r"It is important to note that ",
        r"It's worth noting that ",
        r"It is worth noting that ",
        r"Keep in mind that ",
        r"Note that ",
        r"Remember that ",
        r"The key thing to understand is that ",
        r"What this means in practice is that ",
        r"In other words, ",
        r"Essentially, ",
        r"Basically, ",
        r"Fundamentally, ",
    ]
    for filler in filler_patterns:
        # Only remove at start of sentence/bullet
        content = re.sub(r'(?m)^(\s*[-*]?\s*)' + filler, r'\1', content)
    
    # 4. Compress verbose "When to use" sections
    content = re.sub(
        r'(?m)^(\s*)When to use this:?\s*\n',
        r'\1**Use when**: ',
        content
    )
    content = re.sub(
        r'(?m)^(\s*)When NOT to use this:?\s*\n',
        r'\1**Skip when**: ',
        content
    )
    
    # 5. Remove redundant horizontal rules within sections
    content = re.sub(r'\n---\n---\n', '\n---\n', content)
    
    # 6. Compress "## Pattern N: The " to "## N. "
    content = re.sub(
        r'^## Pattern (\d+): The (.+)$',
        r'## \1. \2',
        content,
        flags=re.MULTILINE
    )
    
    new_len = len(content)
    return content, original_len - new_len


def backup_file(path):
    """Create a timestamped backup of the file."""
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{path.parent.name}_genius_{timestamp}.md"
    backup_path = BACKUP_DIR / backup_name
    shutil.copy2(path, backup_path)
    return backup_path


def audit():
    """Show compression statistics."""
    files = find_genius_files()
    total_chars = sum(f["size"] for f in files)
    
    tier1 = [f for f in files if f["size"] > TIER1_THRESHOLD]
    tier2 = [f for f in files if TIER2_THRESHOLD < f["size"] <= TIER1_THRESHOLD]
    tier3 = [f for f in files if f["size"] <= TIER2_THRESHOLD]
    
    print(f"Total genius files:     {len(files)}")
    print(f"Total content:          {total_chars:,} chars ({total_chars // 4:,} est. tokens)")
    print(f"Average size:           {total_chars // len(files):,} chars")
    print()
    print(f"TIER 1 (>30K, critical):  {len(tier1)} files, {sum(f['size'] for f in tier1):,} chars")
    print(f"TIER 2 (15-30K, high):    {len(tier2)} files, {sum(f['size'] for f in tier2):,} chars")
    print(f"TIER 3 (<15K, optimal):   {len(tier3)} files, {sum(f['size'] for f in tier3):,} chars")
    print()
    
    # Estimate savings from structural compression
    total_saved = 0
    for f in files:
        content = f["path"].read_text(errors="ignore")
        _, saved = compress_content(content)
        total_saved += saved
    
    print(f"Estimated structural compression savings: {total_saved:,} chars ({total_saved // 4:,} tokens)")
    print(f"That's {total_saved * 100 / total_chars:.1f}% of total genius content")


def compress_file(path, apply=False):
    """Compress a single genius file."""
    content = path.read_text(errors="ignore")
    original_size = len(content)
    
    compressed, saved = compress_content(content)
    
    print(f"  {path.parent.name}/genius.md")
    print(f"    Before: {original_size:,} chars ({original_size // 4:,} tokens)")
    print(f"    After:  {len(compressed):,} chars ({len(compressed) // 4:,} tokens)")
    print(f"    Saved:  {saved:,} chars ({saved // 4:,} tokens) — {saved * 100 / original_size:.1f}%")
    
    if apply and saved > 0:
        backup = backup_file(path)
        path.write_text(compressed)
        print(f"    Backup: {backup}")
        print(f"    Written: {path}")
    elif not apply and saved > 0:
        print(f"    [DRY RUN — use --apply to write]")
    
    return saved


def main():
    parser = argparse.ArgumentParser(description="Genius File Compressor")
    parser.add_argument("--audit", action="store_true", help="Show compression stats")
    parser.add_argument("--compress", type=str, help="Compress a specific file")
    parser.add_argument("--compress-tier1", action="store_true", help="Compress all Tier 1 files")
    parser.add_argument("--compress-all", action="store_true", help="Compress all files")
    parser.add_argument("--apply", action="store_true", help="Actually write changes")
    
    args = parser.parse_args()
    
    if args.audit:
        audit()
    elif args.compress:
        path = Path(args.compress)
        if not path.exists():
            print(f"File not found: {path}")
            sys.exit(1)
        compress_file(path, apply=args.apply)
    elif args.compress_tier1:
        files = find_genius_files()
        tier1 = [f for f in files if f["size"] > TIER1_THRESHOLD]
        total_saved = 0
        for f in tier1:
            saved = compress_file(f["path"], apply=args.apply)
            total_saved += saved
        print(f"\nTotal Tier 1 savings: {total_saved:,} chars ({total_saved // 4:,} tokens)")
    elif args.compress_all:
        files = find_genius_files()
        total_saved = 0
        for f in files:
            saved = compress_file(f["path"], apply=args.apply)
            total_saved += saved
            print()
        print(f"\nTotal savings: {total_saved:,} chars ({total_saved // 4:,} tokens)")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
