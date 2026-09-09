#!/usr/bin/env python3
"""Read-only verifier for the preservation-first duplicate deletion manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def files_under(root: Path) -> dict[str, Path]:
    return {
        str(path.relative_to(root)): path
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def verify_file(item: dict, candidate: Path, canonical: Path) -> list[str]:
    errors: list[str] = []
    expected_hash = item["sha256"]
    for label, path in (("candidate", candidate), ("canonical", canonical)):
        if not path.is_file():
            errors.append(f"{item['id']}: missing {label} file: {path}")
            continue
        if path.stat().st_size != item["logical_bytes"]:
            errors.append(f"{item['id']}: {label} size mismatch: {path}")
        observed_hash = sha256(path)
        if observed_hash != expected_hash:
            errors.append(
                f"{item['id']}: {label} SHA-256 mismatch: "
                f"expected {expected_hash}, got {observed_hash}"
            )
    return errors


def verify_tree(item: dict, candidate: Path, canonical: Path) -> list[str]:
    errors: list[str] = []
    if not candidate.is_dir():
        errors.append(f"{item['id']}: missing candidate directory: {candidate}")
        return errors
    if not canonical.is_dir():
        errors.append(f"{item['id']}: missing canonical directory: {canonical}")
        return errors

    candidate_files = files_under(candidate)
    canonical_files = files_under(canonical)
    expected_hashes = {entry["relative_path"]: entry["sha256"] for entry in item["file_hashes"]}

    if set(candidate_files) != set(canonical_files):
        errors.append(f"{item['id']}: candidate and canonical relative paths differ")
    if set(candidate_files) != set(expected_hashes):
        errors.append(f"{item['id']}: observed and manifest relative paths differ")
    if len(candidate_files) != item["file_count"]:
        errors.append(f"{item['id']}: file-count mismatch")

    candidate_total = sum(path.stat().st_size for path in candidate_files.values())
    if candidate_total != item["logical_bytes"]:
        errors.append(f"{item['id']}: logical-byte total mismatch")

    for relative_path, expected_hash in expected_hashes.items():
        for label, collection in (("candidate", candidate_files), ("canonical", canonical_files)):
            path = collection.get(relative_path)
            if path is None:
                continue
            observed_hash = sha256(path)
            if observed_hash != expected_hash:
                errors.append(
                    f"{item['id']}: {label} hash mismatch for {relative_path}: "
                    f"expected {expected_hash}, got {observed_hash}"
                )
    return errors


def verify_negative_control(control: dict) -> list[str]:
    errors: list[str] = []
    canonical = Path(control["canonical_root"])
    review = Path(control["review_root"])
    extra = Path(control["extra_file"])
    if not canonical.is_dir() or not review.is_dir():
        return ["negative control: one or both Hoodie roots are missing"]
    if len(files_under(canonical)) != control["canonical_file_count"]:
        errors.append("negative control: canonical Hoodie file count changed")
    if len(files_under(review)) != control["review_file_count"]:
        errors.append("negative control: review Hoodie file count changed")
    if not extra.is_file():
        errors.append("negative control: unique Hoodie file is missing")
    elif sha256(extra) != control["extra_file_sha256"]:
        errors.append("negative control: unique Hoodie file hash changed")
    if set(files_under(canonical)) == set(files_under(review)):
        errors.append("negative control: Hoodie roots unexpectedly appear identical")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--phase", choices=("pre-move", "in-trash", "post-empty"), default="pre-move")
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text())
    errors: list[str] = []

    for item in manifest["items"]:
        source = Path(item["source_path"])
        trash = Path(item["trash_path"])
        canonical = Path(item["retained_canonical"])
        if args.phase == "pre-move":
            candidate = source
            if trash.exists():
                errors.append(f"{item['id']}: trash destination already exists: {trash}")
        elif args.phase == "in-trash":
            candidate = trash
            if source.exists():
                errors.append(f"{item['id']}: source still exists after move: {source}")
        else:
            candidate = source
            if source.exists() or trash.exists():
                errors.append(f"{item['id']}: source or Trash candidate still exists after emptying")
            if not canonical.exists():
                errors.append(f"{item['id']}: retained canonical is missing after emptying")
            continue

        if item["item_type"] == "file":
            errors.extend(verify_file(item, candidate, canonical))
        else:
            errors.extend(verify_tree(item, candidate, canonical))

    for control in manifest["negative_controls"]:
        errors.extend(verify_negative_control(control))

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "PASS "
        f"phase={args.phase} "
        f"items={len(manifest['items'])} "
        f"allocated_bytes={manifest['expected_reclaim_allocated_bytes']} "
        "negative_controls=1"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
