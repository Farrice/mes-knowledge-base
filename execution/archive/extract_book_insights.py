#!/usr/bin/env python3
"""
Extract Book Insights - Process book PDFs into summary files.

Usage:
    python extract_book_insights.py /path/to/book.pdf
    python extract_book_insights.py /path/to/book.pdf --output custom_name.md
    python extract_book_insights.py --list  # List books directory

Note: This script creates a template for AI-assisted extraction.
      Full PDF parsing requires additional dependencies (PyPDF2, pdfplumber).
"""

import os
import argparse
from pathlib import Path
from datetime import datetime


# Base paths
BASE_PATH = Path(__file__).parent.parent
BOOKS_PATH = BASE_PATH / "knowledge" / "books"
EBOOKS_PATH = Path.home() / "Ebook-PDFs"


def create_book_template(book_name: str, pdf_path: str = None) -> str:
    """Create a template for book insights extraction."""
    return f"""# {book_name} - Key Insights

*Extracted: {datetime.now().strftime('%Y-%m-%d')}*
*Source: {pdf_path or 'Unknown'}*

---

## Overview

**Author:** [Author Name]
**Category:** [Marketing/Sales/Writing/Psychology/Business/etc.]
**Core Premise:** [One sentence summary of the book's main argument]

---

## Key Frameworks

### Framework 1: [Name]
**What it is:** [Description]
**How to use it:** [Actionable steps]
**When to apply:** [Context for deployment]

### Framework 2: [Name]
**What it is:** [Description]
**How to use it:** [Actionable steps]
**When to apply:** [Context for deployment]

### Framework 3: [Name]
**What it is:** [Description]
**How to use it:** [Actionable steps]
**When to apply:** [Context for deployment]

---

## Mental Models

1. **[Model Name]:** [Brief explanation and application]
2. **[Model Name]:** [Brief explanation and application]
3. **[Model Name]:** [Brief explanation and application]

---

## Actionable Insights

### Immediate Actions (Today)
- [ ] [Action 1]
- [ ] [Action 2]
- [ ] [Action 3]

### Short-term Actions (This Week)
- [ ] [Action 1]
- [ ] [Action 2]

### Long-term Applications (This Month+)
- [ ] [Action 1]
- [ ] [Action 2]

---

## Notable Quotes

> "[Quote 1]" - p.XX

> "[Quote 2]" - p.XX

> "[Quote 3]" - p.XX

---

## Connection to Expert Council

**Relevant Experts:**
- @[expert-name]: How this connects to their frameworks
- @[expert-name]: How this connects to their frameworks

**Integration Ideas:**
- [How to combine this book's insights with existing expert frameworks]

---

## Personal Application Notes

[Space for your notes on how to apply this to your specific situation]

---

*Last updated: {datetime.now().strftime('%Y-%m-%d')}*
"""


def list_ebooks():
    """List available ebooks in the Ebook-PDFs directory."""
    if not EBOOKS_PATH.exists():
        print(f"❌ Ebooks directory not found: {EBOOKS_PATH}")
        return

    pdfs = list(EBOOKS_PATH.glob('*.pdf'))

    print(f"\n📚 Available Ebooks ({len(pdfs)} found):")
    print("=" * 60)

    for pdf in sorted(pdfs):
        size_mb = pdf.stat().st_size / (1024 * 1024)
        print(f"  📖 {pdf.name} ({size_mb:.1f} MB)")

    print("\n💡 Usage: python extract_book_insights.py '/path/to/book.pdf'")


def list_existing_summaries():
    """List existing book summaries."""
    if not BOOKS_PATH.exists():
        print(f"📁 Creating books directory: {BOOKS_PATH}")
        BOOKS_PATH.mkdir(parents=True, exist_ok=True)
        return

    summaries = list(BOOKS_PATH.glob('*.md'))

    if summaries:
        print(f"\n📝 Existing Summaries ({len(summaries)}):")
        for summary in sorted(summaries):
            print(f"  ✅ {summary.stem}")
    else:
        print("\n📝 No existing summaries yet.")


def create_summary_file(pdf_path: Path, output_name: str = None) -> Path:
    """Create a summary file for a book."""
    # Ensure books directory exists
    BOOKS_PATH.mkdir(parents=True, exist_ok=True)

    # Generate output filename
    if output_name:
        output_file = BOOKS_PATH / f"{output_name}.md"
    else:
        # Clean up the PDF filename
        clean_name = pdf_path.stem.lower()
        clean_name = clean_name.replace(' ', '-')
        clean_name = ''.join(c for c in clean_name if c.isalnum() or c == '-')
        output_file = BOOKS_PATH / f"{clean_name}.md"

    # Create template
    book_name = pdf_path.stem.replace('-', ' ').replace('_', ' ').title()
    template = create_book_template(book_name, str(pdf_path))

    # Write file
    with open(output_file, 'w') as f:
        f.write(template)

    return output_file


def main():
    parser = argparse.ArgumentParser(description='Extract book insights into summary files')
    parser.add_argument('pdf_path', nargs='?', help='Path to the PDF book')
    parser.add_argument('--output', '-o', help='Custom output filename (without .md)')
    parser.add_argument('--list', '-l', action='store_true', help='List available ebooks')
    parser.add_argument('--summaries', '-s', action='store_true', help='List existing summaries')

    args = parser.parse_args()

    if args.list:
        list_ebooks()
        return

    if args.summaries:
        list_existing_summaries()
        return

    if not args.pdf_path:
        print("❌ Please provide a PDF path or use --list to see available books")
        print("\nUsage:")
        print("  python extract_book_insights.py /path/to/book.pdf")
        print("  python extract_book_insights.py --list")
        print("  python extract_book_insights.py --summaries")
        return

    pdf_path = Path(args.pdf_path)

    if not pdf_path.exists():
        print(f"❌ File not found: {pdf_path}")
        return

    if not pdf_path.suffix.lower() == '.pdf':
        print(f"⚠️ Warning: File may not be a PDF: {pdf_path}")

    print(f"📖 Processing: {pdf_path.name}")

    output_file = create_summary_file(pdf_path, args.output)

    print(f"✅ Template created: {output_file}")
    print(f"\n📝 Next steps:")
    print(f"   1. Open the book and read/skim key sections")
    print(f"   2. Fill in the template with key frameworks and insights")
    print(f"   3. Or use AI to help extract insights from the PDF")
    print(f"\n💡 Tip: Ask Claude to help fill in the template:")
    print(f'   "Help me extract key insights from [book name] into this template"')


if __name__ == '__main__':
    main()
