#!/usr/bin/env python3
"""
Workflow Consolidator — Merges duplicate workflows by keeping the better version
and converting the inferior to a redirect stub.
"""

import os
import sys
import shutil
from datetime import datetime

WORKFLOWS_DIR = os.path.join(os.path.dirname(__file__), '..', '.agent', 'workflows')
BACKUP_DIR = os.path.join(os.path.dirname(__file__), '..', '.tmp', 'consolidated_backups')

# Consolidation map: (deprecated_file, canonical_file)
# The canonical is the one we keep; the deprecated becomes a redirect.
CONSOLIDATIONS = [
    ("competitor-content-spy.md", "competitor-intel.md"),
    ("design-offer.md", "design-digital-product-offer.md"),
    ("swarm-research.md", "research-swarm.md"),
    ("content-series.md", "content-series-plan.md"),
]


def create_redirect_stub(deprecated_path, canonical_name):
    """Replace deprecated workflow with a redirect stub."""
    canonical_cmd = "/" + canonical_name.replace(".md", "")
    deprecated_cmd = "/" + os.path.basename(deprecated_path).replace(".md", "")

    # Read the original description
    desc = ""
    with open(deprecated_path) as f:
        for line in f:
            if line.strip().startswith("description:"):
                desc = line.strip().replace("description:", "").strip()
                break

    stub = f"""---
description: "{desc} (→ use {canonical_cmd})"
---

# {deprecated_cmd} — Redirected

> This workflow has been consolidated into **{canonical_cmd}**.
> Run `{canonical_cmd}` instead.
"""
    with open(deprecated_path, 'w') as f:
        f.write(stub)


def consolidate(dry_run=False):
    os.makedirs(BACKUP_DIR, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d")

    results = []
    for deprecated_file, canonical_file in CONSOLIDATIONS:
        dep_path = os.path.join(WORKFLOWS_DIR, deprecated_file)
        can_path = os.path.join(WORKFLOWS_DIR, canonical_file)

        if not os.path.exists(dep_path):
            results.append(f"SKIP: {deprecated_file} not found")
            continue
        if not os.path.exists(can_path):
            results.append(f"SKIP: {canonical_file} not found")
            continue

        dep_size = os.path.getsize(dep_path)
        can_size = os.path.getsize(can_path)

        if dry_run:
            results.append(
                f"WOULD MERGE: {deprecated_file} ({dep_size}b) → redirect to {canonical_file} ({can_size}b)"
            )
        else:
            # Backup deprecated
            backup_path = os.path.join(BACKUP_DIR, f"{deprecated_file}.{stamp}")
            shutil.copy2(dep_path, backup_path)

            # Create redirect stub
            create_redirect_stub(dep_path, canonical_file)
            results.append(
                f"MERGED: {deprecated_file} → redirect to {canonical_file} (backup: {backup_path})"
            )

    return results


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("=== DRY RUN ===\n")

    results = consolidate(dry_run=dry_run)
    for r in results:
        print(r)

    if not dry_run:
        print(f"\nConsolidated {len([r for r in results if r.startswith('MERGED')])} workflows.")
        print(f"Backups saved to: {BACKUP_DIR}")
