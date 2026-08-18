#!/usr/bin/env python3
"""
md_to_gdoc.py — Convert Markdown files to beautifully formatted Google Docs.

Pipeline: Markdown → Styled HTML → Upload to Google Drive as native Google Doc

Usage:
    python execution/md_to_gdoc.py <file.md> [--folder-id <DRIVE_FOLDER_ID>]
    python execution/md_to_gdoc.py <folder/> [--folder-id <DRIVE_FOLDER_ID>]
    python execution/md_to_gdoc.py <folder/> --create-folder "Folder Name" [--parent-id <PARENT_ID>]

Features:
    - Native Google Docs (not .docx import — actual Google Docs)
    - Page breaks at --- dividers and before ## headings
    - Styled tables with borders and header rows
    - Proper heading hierarchy with consistent fonts
    - Bold, italic, inline code, blockquotes
    - Bullet and numbered lists
    - Clean typography and spacing
    - Batch conversion for entire folders

Requirements:
    - gws CLI authenticated: gws auth login -s drive
    - Python markdown library (included in most installs)

Created: 2026-04-12
"""

import sys
import os
import re
import json
import subprocess
import tempfile
from datetime import date
from pathlib import Path

from google_doc_lifecycle import content_hash, lookup, record

try:
    import markdown
    from markdown.extensions.tables import TableExtension
except ImportError:
    print("Error: markdown library not found. Install with: pip install markdown")
    sys.exit(1)


# Google-Docs-optimized HTML template
HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body {{
    font-family: Arial, sans-serif;
    font-size: 11pt;
    color: #333333;
    line-height: 1.5;
    max-width: 7in;
    margin: 0 auto;
    padding: 0;
}}
h1 {{
    font-family: Arial, sans-serif;
    font-size: 22pt;
    font-weight: bold;
    color: #1a1a1a;
    margin-top: 6pt;
    margin-bottom: 6pt;
    page-break-before: auto;
}}
h2 {{
    font-family: Arial, sans-serif;
    font-size: 16pt;
    font-weight: bold;
    color: #2a2a2a;
    margin-top: 18pt;
    margin-bottom: 6pt;
    page-break-before: always;
}}
h3 {{
    font-family: Arial, sans-serif;
    font-size: 13pt;
    font-weight: bold;
    color: #3a3a3a;
    margin-top: 12pt;
    margin-bottom: 4pt;
}}
h4 {{
    font-family: Arial, sans-serif;
    font-size: 11pt;
    font-weight: bold;
    color: #444444;
    margin-top: 10pt;
    margin-bottom: 4pt;
}}
p {{
    margin-top: 4pt;
    margin-bottom: 8pt;
}}
table {{
    border-collapse: collapse;
    width: 100%;
    margin-top: 8pt;
    margin-bottom: 12pt;
    font-size: 10pt;
}}
th {{
    background-color: #f5f5f5;
    font-weight: bold;
    text-align: left;
    padding: 6pt 8pt;
    border: 1px solid #cccccc;
}}
td {{
    padding: 5pt 8pt;
    border: 1px solid #cccccc;
    vertical-align: top;
}}
tr:nth-child(even) {{
    background-color: #fafafa;
}}
blockquote {{
    margin-left: 20pt;
    margin-right: 20pt;
    padding-left: 10pt;
    border-left: 3px solid #cccccc;
    color: #555555;
    font-style: italic;
}}
code {{
    font-family: 'Courier New', monospace;
    font-size: 9pt;
    color: #884400;
    background-color: #f8f4f0;
    padding: 1pt 3pt;
}}
pre {{
    font-family: 'Courier New', monospace;
    font-size: 9pt;
    color: #555555;
    background-color: #f5f5f5;
    padding: 8pt 12pt;
    margin: 8pt 0;
    border: 1px solid #e0e0e0;
    white-space: pre-wrap;
    word-wrap: break-word;
}}
ul, ol {{
    margin-top: 4pt;
    margin-bottom: 8pt;
    padding-left: 24pt;
}}
li {{
    margin-bottom: 3pt;
}}
hr {{
    border: none;
    page-break-before: always;
    margin: 0;
    padding: 0;
    height: 0;
}}
.page-break {{
    page-break-before: always;
}}
</style>
</head>
<body>
{content}
</body>
</html>"""


def preprocess_markdown(md_text):
    """Pre-process markdown to handle edge cases before conversion."""
    lines = md_text.split('\n')
    processed = []
    in_code_block = False

    for line in lines:
        stripped = line.strip()

        # Track code blocks
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            processed.append(line)
            continue

        if in_code_block:
            processed.append(line)
            continue

        # Convert --- horizontal rules to page break divs
        if stripped in ('---', '***', '___') and len(stripped) == 3:
            processed.append('<div style="page-break-before: always;"></div>')
            processed.append('')
            continue

        # Convert checkbox items to bullet-style
        if stripped.startswith('- [x]') or stripped.startswith('- [X]'):
            text = stripped[5:].strip()
            processed.append(f'- ✓ {text}')
            continue
        if stripped.startswith('- [ ]'):
            text = stripped[5:].strip()
            processed.append(f'- ☐ {text}')
            continue

        processed.append(line)

    return '\n'.join(processed)


def md_to_html(md_text):
    """Convert markdown text to styled HTML ready for Google Docs import."""
    # Pre-process
    md_text = preprocess_markdown(md_text)

    # Convert to HTML
    html_content = markdown.markdown(
        md_text,
        extensions=['tables', 'fenced_code', 'nl2br'],
        output_format='html5'
    )

    # Wrap in template
    full_html = HTML_TEMPLATE.format(content=html_content)

    return full_html


def gws_create_folder(name, parent_id=None):
    """Create a Google Drive folder and return its ID."""
    metadata = {
        "name": name,
        "mimeType": "application/vnd.google-apps.folder"
    }
    if parent_id:
        metadata["parents"] = [parent_id]

    cmd = [
        'gws', 'drive', 'files', 'create',
        '--json', json.dumps(metadata),
        '--params', '{"fields": "id,name,webViewLink"}'
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error creating folder: {result.stderr}")
        return None

    data = json.loads(result.stdout)
    print(f"  📁 Created folder: {data.get('name')} → {data.get('webViewLink', 'no link')}")
    return data.get('id')


def upload_html_as_gdoc(html_path, name, folder_id=None):
    """Upload an HTML file to Google Drive as a native Google Doc.

    Uses a two-step approach: upload HTML, then copy as Google Doc.
    This is required because gws CLI doesn't support multipart upload with
    content-type conversion in a single call.
    """
    # Step 1: Upload HTML as-is
    upload_metadata = {"name": f"_temp_{name}.html"}
    if folder_id:
        upload_metadata["parents"] = [folder_id]

    cmd_upload = [
        'gws', 'drive', 'files', 'create',
        '--json', json.dumps(upload_metadata),
        '--upload', str(html_path),
        '--params', '{"fields": "id"}'
    ]

    result = subprocess.run(cmd_upload, capture_output=True, text=True)
    if result.returncode != 0 or 'error' in result.stdout.lower():
        print(f"  ✗ Error uploading {name}: {result.stdout[:200]} {result.stderr[:200]}")
        return None

    try:
        upload_data = json.loads(result.stdout)
        temp_file_id = upload_data.get('id')
    except json.JSONDecodeError:
        print(f"  ✗ Error parsing upload response for {name}")
        return None

    if not temp_file_id:
        print(f"  ✗ No file ID returned for {name}")
        return None

    # Step 2: Copy as native Google Doc
    copy_metadata = {
        "name": name,
        "mimeType": "application/vnd.google-apps.document"
    }
    if folder_id:
        copy_metadata["parents"] = [folder_id]

    cmd_copy = [
        'gws', 'drive', 'files', 'copy',
        '--json', json.dumps(copy_metadata),
        '--params', json.dumps({"fileId": temp_file_id, "fields": "id,name,webViewLink"})
    ]

    result = subprocess.run(cmd_copy, capture_output=True, text=True)

    # Step 3: Delete temp HTML file. gws otherwise leaves an empty
    # download.html response in the working directory for this 204 response.
    delete_response = Path(html_path).with_suffix('.delete-response')
    cmd_delete = [
        'gws', 'drive', 'files', 'delete',
        '--params', json.dumps({"fileId": temp_file_id}),
        '--output', str(delete_response),
    ]
    subprocess.run(cmd_delete, capture_output=True, text=True)
    delete_response.unlink(missing_ok=True)

    if result.returncode != 0 or 'error' in result.stdout.lower():
        print(f"  ✗ Error converting {name}: {result.stdout[:200]}")
        return None

    try:
        data = json.loads(result.stdout)
        link = data.get('webViewLink', 'no link')
        print(f"  ✓ {name} → {link}")
        return data
    except json.JSONDecodeError:
        print(f"  ✗ Error parsing conversion response for {name}")
        return None


def update_html_gdoc(html_path, existing):
    """Replace one living Google Doc while preserving its ID and revisions."""
    doc_id = existing.get('doc_id') or existing.get('id')
    if not doc_id:
        return None
    result = subprocess.run([
        'gws', 'drive', 'files', 'update',
        '--params', json.dumps({"fileId": doc_id, "fields": "id,name,webViewLink"}),
        '--upload', str(html_path), '--upload-content-type', 'text/html',
    ], capture_output=True, text=True)
    if result.returncode != 0 or '"error"' in (result.stdout or '').lower():
        print(f"  ✗ Error updating living Google Doc {doc_id}: {result.stderr[:200]}")
        return None
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None
    data.setdefault('id', doc_id)
    data.setdefault('webViewLink', existing.get('link') or
                    f"https://docs.google.com/document/d/{doc_id}/edit")
    print(f"  ✓ Updated living Google Doc → {data['webViewLink']}")
    return data


def set_pageless(doc_id):
    """Set a Google Doc to pageless rendering. Docs API v1 has no native pageless
    toggle; the documented workaround is a very large pageSize.height. 14400 PT
    (200 inches) is well within accepted bounds — 1,000,000 PT broke the renderer."""
    payload = json.dumps({
        "requests": [{
            "updateDocumentStyle": {
                "documentStyle": {
                    "pageSize": {
                        "height": {"magnitude": 14400, "unit": "PT"}
                    }
                },
                "fields": "pageSize.height",
            }
        }]
    })
    cmd = [
        'gws', 'docs', 'documents', 'batchUpdate',
        '--params', json.dumps({"documentId": doc_id}),
        '--json', payload,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)

    failed = result.returncode != 0 or '"error"' in (result.stdout or '')
    if failed:
        print(f"  ✗ Pageless format FAILED for doc {doc_id}")
        if result.stderr:
            print(f"    stderr: {result.stderr.strip()}")
        if result.stdout:
            print(f"    stdout: {result.stdout.strip()[:500]}")
        return False
    print(f"  ✓ Pageless format applied")
    return True


def convert_and_upload(md_path, folder_id=None, name=None, pageless=True,
                       new_milestone=False, existing_doc_id=None):
    """Convert Markdown to one living Google Doc, updating it on later runs."""
    md_path = Path(md_path)

    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Convert to HTML
    html_content = md_to_html(md_text)

    # gws only uploads files from the active workspace. Keep conversion
    # intermediates inside the repo instead of macOS's private temp directory.
    staging_dir = Path.cwd() / '.tmp'
    staging_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False,
                                     encoding='utf-8', dir=staging_dir) as f:
        f.write(html_content)
        html_path = f.name

    try:
        # Upload as Google Doc
        if name is None:
            doc_name = md_path.stem.replace('-', ' ').title()
            # Keep number prefix for ordering
            if md_path.stem[:2].isdigit():
                doc_name = md_path.stem[:3] + doc_name[3:]
        else:
            doc_name = name

        if new_milestone and not re.match(r'^\d{4}-\d{2}-\d{2}[-_ ]', doc_name):
            doc_name = f"{date.today().isoformat()} — {doc_name}"
        source_hash = content_hash(md_text)
        existing = None if new_milestone else lookup(md_path, folder_id, doc_name)
        if existing_doc_id and not new_milestone:
            existing = {"doc_id": existing_doc_id,
                        "link": f"https://docs.google.com/document/d/{existing_doc_id}/edit"}
        if existing and existing.get('source_hash') == source_hash:
            result = {"id": existing['doc_id'], "name": doc_name,
                      "webViewLink": existing.get('link')}
            print(f"  ✓ Unchanged — reused living Google Doc → {result['webViewLink']}")
        elif existing:
            result = update_html_gdoc(html_path, existing)
        else:
            result = upload_html_as_gdoc(html_path, doc_name, folder_id)
        if result and not new_milestone:
            record(md_path, folder_id, doc_name, result.get('id'), source_hash,
                   result.get('webViewLink'))

        # Apply pageless format
        if result and pageless:
            doc_id = result.get('id')
            if doc_id:
                if not set_pageless(doc_id):
                    print(f"  ⚠ Doc uploaded but pageless not applied — open in Drive "
                          f"and toggle manually, or rerun set_pageless('{doc_id}')")

        return result
    finally:
        os.unlink(html_path)


def batch_convert_and_upload(input_dir, folder_id=None, folder_name=None, parent_id=None):
    """Convert all markdown files in a directory and upload to Drive."""
    input_dir = Path(input_dir)
    md_files = sorted(input_dir.glob('*.md'))

    if not md_files:
        print(f"No .md files found in {input_dir}")
        return []

    # Create folder if requested
    if folder_name and not folder_id:
        folder_id = gws_create_folder(folder_name, parent_id)
        if not folder_id:
            print("Failed to create Drive folder. Aborting.")
            return []

    print(f"\nConverting {len(md_files)} files to Google Docs...\n")

    results = []
    for md_file in md_files:
        result = convert_and_upload(md_file, folder_id)
        if result:
            results.append(result)

    print(f"\n✅ {len(results)}/{len(md_files)} files uploaded as native Google Docs.")

    if folder_id:
        print(f"📁 Folder: https://drive.google.com/drive/folders/{folder_id}")

    return results


def mirror_folders_and_upload(root_dir, drive_parent_id, dated_folder_name=None, exclude_dirs=None):
    """Walk root_dir, mirror its subfolder structure into Drive, upload all .md files as native Google Docs.

    Built for the Brand Operating System (BOS) build pipeline — preserves the 6-layer
    folder structure (00-foundation, 01-visual, etc.) when uploading.

    Args:
        root_dir: Local directory containing the layer subfolders (e.g., projects/<client>/brand-operating-system/)
        drive_parent_id: Drive folder ID where the dated subfolder gets created
        dated_folder_name: If provided, creates an intermediate dated folder; otherwise uploads directly into drive_parent_id
        exclude_dirs: Set of subfolder names to skip (default: {'_working'})
    """
    root_dir = Path(root_dir)
    if exclude_dirs is None:
        exclude_dirs = {'_working'}

    if not root_dir.is_dir():
        print(f"Error: {root_dir} is not a directory")
        return []

    # Step 1: Create the dated folder under drive_parent_id (if requested)
    if dated_folder_name:
        target_root_id = gws_create_folder(dated_folder_name, drive_parent_id)
        if not target_root_id:
            print("Failed to create dated folder. Aborting.")
            return []
    else:
        target_root_id = drive_parent_id

    # Step 2: Discover all subfolders containing .md files
    subfolders = []
    for entry in sorted(root_dir.iterdir()):
        if not entry.is_dir():
            continue
        if entry.name in exclude_dirs:
            print(f"  ⊘ Skipping {entry.name} (excluded)")
            continue
        if any(entry.glob('*.md')):
            subfolders.append(entry)

    # Also check for .md files in the root itself (non-subfolder docs like README.md)
    root_md_files = [f for f in sorted(root_dir.glob('*.md')) if f.is_file()]

    print(f"\nMirroring {len(subfolders)} subfolders + {len(root_md_files)} root files into Drive\n")

    # Step 3: Create matching Drive subfolder + upload .md files for each
    all_results = []
    for subfolder in subfolders:
        print(f"\n→ {subfolder.name}/")
        subfolder_id = gws_create_folder(subfolder.name, target_root_id)
        if not subfolder_id:
            print(f"  ⚠ Failed to create Drive subfolder for {subfolder.name}, skipping uploads")
            continue
        results = batch_convert_and_upload(subfolder, folder_id=subfolder_id)
        all_results.extend(results)

    # Step 4: Upload root-level .md files (if any)
    if root_md_files:
        print(f"\n→ (root)")
        for md_file in root_md_files:
            result = convert_and_upload(md_file, folder_id=target_root_id)
            if result:
                all_results.append(result)

    print(f"\n✅ Mirror complete: {len(all_results)} total files uploaded as native Google Docs")
    print(f"📁 Root folder: https://drive.google.com/drive/folders/{target_root_id}")
    return all_results


def save_html_locally(input_dir, output_dir=None):
    """Convert markdown to HTML and save locally (for testing without Drive)."""
    input_dir = Path(input_dir)
    if output_dir is None:
        output_dir = input_dir / 'html'
    else:
        output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)
    md_files = sorted(input_dir.glob('*.md'))

    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            md_text = f.read()

        html_content = md_to_html(md_text)
        html_path = output_dir / md_file.with_suffix('.html').name

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"  ✓ {md_file.name} → {html_path.name}")

    print(f"\nSaved {len(md_files)} HTML files to {output_dir}/")
    print("Open any .html file in a browser to preview formatting.")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Convert Markdown to native Google Docs')
    parser.add_argument('input', help='Markdown file or folder')
    parser.add_argument('--folder-id', help='Existing Google Drive folder ID to upload into')
    parser.add_argument('--create-folder', help='Create a new Drive folder with this name')
    parser.add_argument('--parent-id', help='Parent folder ID for new folder')
    parser.add_argument('--name', help='Document title (overrides auto-generated name)')
    parser.add_argument('--html-only', action='store_true', help='Save as HTML locally (no upload)')
    parser.add_argument('--mirror-folders', action='store_true',
                        help='Walk input dir and mirror subfolder structure into Drive (BOS build pipeline)')
    parser.add_argument('--drive-parent', help='Drive parent folder ID (alias for --parent-id when used with --mirror-folders)')
    parser.add_argument('--exclude-dirs', help='Comma-separated list of subfolder names to skip when mirroring (default: _working)')
    parser.add_argument('--new-milestone', action='store_true',
                        help='create a separate date-led Doc instead of updating the living Doc')
    parser.add_argument('--doc-id',
                        help='adopt an existing Google Doc as the living export (single-file mode)')

    args = parser.parse_args()
    input_path = Path(args.input)

    if args.mirror_folders:
        if not input_path.is_dir():
            print(f"Error: --mirror-folders requires a directory, got {input_path}")
            sys.exit(1)
        drive_parent = args.drive_parent or args.parent_id or args.folder_id
        if not drive_parent:
            print("Error: --mirror-folders requires --drive-parent (or --parent-id / --folder-id)")
            sys.exit(1)
        exclude = set((args.exclude_dirs or '_working').split(','))
        mirror_folders_and_upload(
            input_path,
            drive_parent_id=drive_parent,
            dated_folder_name=args.create_folder,
            exclude_dirs=exclude,
        )
    elif args.html_only:
        if input_path.is_dir():
            save_html_locally(input_path)
        else:
            # Single file
            with open(input_path, 'r', encoding='utf-8') as f:
                md_text = f.read()
            html = md_to_html(md_text)
            out = input_path.with_suffix('.html')
            with open(out, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"  ✓ {input_path.name} → {out.name}")
    elif input_path.is_dir():
        if args.doc_id or args.new_milestone:
            print("Error: --doc-id and --new-milestone are single-file controls")
            sys.exit(1)
        batch_convert_and_upload(
            input_path,
            folder_id=args.folder_id,
            folder_name=args.create_folder,
            parent_id=args.parent_id
        )
    elif input_path.is_file():
        convert_and_upload(input_path, folder_id=args.folder_id, name=args.name,
                           new_milestone=args.new_milestone, existing_doc_id=args.doc_id)
    else:
        print(f"Error: {input_path} not found")
        sys.exit(1)
