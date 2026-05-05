#!/usr/bin/env python3
"""
bos_scaffold.py — Brand Operating System scaffold from template.

Copies templates/brand-operating-system-v1/ to a target project location with
identity-token substitution. Identity tokens (BRAND_NAME, FOUNDER_NAME, CITY,
SPINE_LINE, etc.) are auto-substituted at scaffold time. Brand-specific content
sections (the 12 non-negotiables, voice patterns, ICP profiles) are overwritten
during the build workflow's Phase A-B, not here.

Usage:
    python3 execution/bos_scaffold.py \\
        --template templates/brand-operating-system-v1/ \\
        --output projects/<client-slug>/brand-operating-system/ \\
        --tokens-file scratch/<client>-tokens.json

    # Or interactive mode (prompts for each required token):
    python3 execution/bos_scaffold.py \\
        --template templates/brand-operating-system-v1/ \\
        --output projects/<client-slug>/brand-operating-system/ \\
        --interactive

Token file format (JSON):
    {
        "BRAND_NAME": "Resonance",
        "BRAND_NAME_LOWER": "resonance",
        "FOUNDER_NAME": "Andrea",
        "CITY": "Chicago",
        "SPINE_LINE": "Heart encounters, not head encounters...",
        ...
    }

See templates/brand-operating-system-v1/TOKENS.md for the full token catalog.
"""

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

# Files that should NOT be copied to the target output (template-internal only)
EXCLUDE_FILES = {"TOKENS.md", "README.md"}

# Required identity tokens — scaffold halts if any are missing
REQUIRED_TOKENS = [
    "BRAND_NAME",
    "BRAND_NAME_LOWER",
    "FOUNDER_NAME",
    "SPINE_LINE",
    "ONE_LINER",
    "SUCCESS_METRIC",
]

# Recommended tokens — prompted but allow blank
RECOMMENDED_TOKENS = [
    "FOUNDER_FULL_NAME",
    "CITY",
    "REGION",
    "LAUNCH_DATE",
    "EVENT_TYPE",
    "SPINE_FRAME",
    "SPINE_MECHANISM",
    "KILL_CONDITION",
    "PATIENCE_WINDOW",
    "SUCCESS_RATE_TARGET",
    "ICP_PROFILE_1_NAME",
    "ICP_PROFILE_2_NAME",
    "ICP_PROFILE_3_NAME",
]


def load_tokens(tokens_file: Path | None, interactive: bool) -> dict[str, str]:
    """Load tokens from file, prompt interactively, or both."""
    tokens: dict[str, str] = {}

    if tokens_file and tokens_file.exists():
        with tokens_file.open() as f:
            tokens = json.load(f)
        print(f"Loaded {len(tokens)} tokens from {tokens_file}")

    # Validate required tokens
    missing_required = [t for t in REQUIRED_TOKENS if not tokens.get(t)]

    if missing_required:
        if interactive:
            print(f"\nMissing required tokens: {', '.join(missing_required)}")
            print("Prompting interactively:\n")
            for token in missing_required:
                value = input(f"  {token}: ").strip()
                if not value:
                    print(f"  ERROR: {token} is required.")
                    sys.exit(1)
                tokens[token] = value
        else:
            print(f"ERROR: Missing required tokens: {', '.join(missing_required)}")
            print("Either supply --tokens-file with these set, or use --interactive.")
            sys.exit(1)

    # Prompt for recommended (interactive only)
    if interactive:
        for token in RECOMMENDED_TOKENS:
            if not tokens.get(token):
                value = input(f"  {token} (optional, press Enter to skip): ").strip()
                if value:
                    tokens[token] = value

    return tokens


def substitute(content: str, tokens: dict[str, str]) -> str:
    """Replace {{TOKEN}} occurrences in content."""
    for token, value in tokens.items():
        pattern = "{{" + token + "}}"
        content = content.replace(pattern, value)
    return content


def find_unsubstituted(content: str) -> set[str]:
    """Return set of {{TOKEN}} patterns still in content (warning indicator)."""
    return set(re.findall(r"\{\{([A-Z_][A-Z0-9_]*)\}\}", content))


def scaffold(template_root: Path, output_root: Path, tokens: dict[str, str], force: bool) -> dict:
    """Walk template, substitute, write to output. Return stats."""
    if output_root.exists() and any(output_root.iterdir()) and not force:
        print(f"ERROR: Output {output_root} exists and is not empty. Use --force to overwrite.")
        sys.exit(1)

    stats: dict[str, int | list[str]] = {
        "files_copied": 0,
        "files_skipped": 0,
        "tokens_substituted": 0,
        "unsubstituted_warnings": [],
    }

    for src in template_root.rglob("*"):
        if not src.is_file():
            continue

        rel = src.relative_to(template_root)
        if src.name in EXCLUDE_FILES:
            stats["files_skipped"] += 1
            continue

        dst = output_root / rel
        dst.parent.mkdir(parents=True, exist_ok=True)

        if src.suffix == ".md":
            original = src.read_text(encoding="utf-8")
            transformed = substitute(original, tokens)
            stats["tokens_substituted"] += original.count("{{") - transformed.count("{{")

            unsubstituted = find_unsubstituted(transformed)
            if unsubstituted:
                stats["unsubstituted_warnings"].append(  # type: ignore
                    f"{rel}: {sorted(unsubstituted)}"
                )

            dst.write_text(transformed, encoding="utf-8")
        else:
            shutil.copy2(src, dst)

        stats["files_copied"] += 1

    return stats


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scaffold a Brand Operating System from template",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--template",
        required=True,
        type=Path,
        help="Path to templates/brand-operating-system-v1/",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Target project path (e.g., projects/<client>/brand-operating-system/)",
    )
    parser.add_argument(
        "--tokens-file",
        type=Path,
        help="JSON file with token values",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Prompt for tokens interactively",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite if output directory exists and is non-empty",
    )

    args = parser.parse_args()

    if not args.template.exists():
        print(f"ERROR: Template path {args.template} does not exist.")
        sys.exit(1)

    if not args.tokens_file and not args.interactive:
        print("ERROR: Supply --tokens-file or --interactive.")
        sys.exit(1)

    tokens = load_tokens(args.tokens_file, args.interactive)
    print(f"\nScaffolding from {args.template} → {args.output}")
    print(f"  Tokens to substitute: {len(tokens)}\n")

    stats = scaffold(args.template, args.output, tokens, args.force)

    print(f"\n✓ Scaffold complete.")
    print(f"  Files copied: {stats['files_copied']}")
    print(f"  Files skipped (template-internal): {stats['files_skipped']}")
    print(f"  Tokens substituted: {stats['tokens_substituted']}")

    warnings = stats["unsubstituted_warnings"]
    if warnings:
        print(f"\n⚠ {len(warnings)} files have unsubstituted tokens:")
        for w in warnings[:10]:
            print(f"  • {w}")
        if len(warnings) > 10:
            print(f"  • ... and {len(warnings) - 10} more")
        print("\nUnsubstituted tokens are normal during scaffold — content blocks")
        print("are filled by the workflow during Phase A-B. Review TOKENS.md if unsure.")

    print(f"\nNext step: run the build workflow")
    print(f"  /build-bos --name \"<brand>\" --source <canonical-doc> --output {args.output}")


if __name__ == "__main__":
    main()
