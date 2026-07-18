#!/usr/bin/env python3
"""fleet_merge.py — serial conductor merge: fleet quarantine → skills/ through the gate.

Born 2026-07-17 (Wave 3 Lane 3 close) from the third hand-rolled merge_one.sh.
Encodes merge-discipline Law 1 + the carded fleet failure shapes:
  - shape 2 (quarantine path drift): copies ONLY from the contract path; a worker's
    path claim is a claim like any other.
  - shape 5 (hollow delivery): empty/missing delivery dir hard-fails (exit 3) BEFORE
    any file lands — delivery paperwork without payload never reaches skills/.
  - file-not-summary: the deterministic gate (skill_auditor.py check) is the sole
    merge arbiter; exit mirrors the gate.

Usage:
    python3 execution/fleet_merge.py <batch_dir> <skill_id> [--dry-run]
    # e.g. python3 execution/fleet_merge.py .tmp/wave3-batch4 jasmin-alic-linkedin-growth

Copies every file from <batch_dir>/<skill_id>/ into skills/<skill_id>/ EXCEPT the
fleet artifacts (PROVENANCE.md → skills/<id>/references/PROVENANCE-<date>.md;
REPAIR-NOTES.md stays in quarantine), then runs the 6-check heartbeat gate.
Exit: 0 gate-clear · 1 gate-fail (files copied — revert or repair) · 3 no/empty delivery.
Committing remains conductor-owned and manual, on purpose.
"""
import argparse
import datetime
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FLEET_ARTIFACTS = {"REPAIR-NOTES.md", "PROVENANCE.md"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("batch_dir")
    ap.add_argument("skill_id")
    ap.add_argument("--dry-run", action="store_true", help="list actions, copy nothing, still run the gate on the LIVE skill")
    args = ap.parse_args()

    src = (ROOT / args.batch_dir / args.skill_id).resolve()
    dst = ROOT / "skills" / args.skill_id
    if not src.is_dir():
        print(f"NO DELIVERY: {src} missing (shape-2/5 guard)")
        return 3
    # Shape-2 variant (caught 2026-07-17, damon-cart-nlp): worker nests its output
    # under <quarantine>/skills/<ID>/ — normalize to that inner root so the blind
    # copy never plants a stray skills/<ID>/skills/ tree in the live repo.
    nested = src / "skills" / args.skill_id
    if nested.is_dir():
        print(f"NESTED DELIVERY LAYOUT normalized: merging from {nested.relative_to(ROOT)} "
              f"(top-level PROVENANCE/REPAIR-NOTES still honored)")
        for artifact in FLEET_ARTIFACTS:
            top = src / artifact
            if top.exists() and not (nested / artifact).exists():
                shutil.copy2(top, nested / artifact)
        src = nested
    files = [p for p in src.rglob("*") if p.is_file()]
    if not files:
        print(f"EMPTY DELIVERY: {src} has no files (shape-5 hollow-delivery guard)")
        return 3
    if not dst.is_dir():
        print(f"NO TARGET SKILL: {dst} does not exist — fleet repairs existing skills only")
        return 3

    today = datetime.date.today().isoformat()
    copied = 0
    for f in files:
        rel = f.relative_to(src)
        if rel.name == "REPAIR-NOTES.md":
            continue
        if rel.name == "PROVENANCE.md":
            target = dst / "references" / f"PROVENANCE-{today}.md"
        elif rel == Path("source-ledger.md"):
            # Placement quirk (jay-hiette/jonathan-courtney, 2026-07-18): workers
            # sometimes deliver the ledger flat at the root; the auditor only
            # looks in references/.
            target = dst / "references" / "source-ledger.md"
        else:
            target = dst / rel
        if args.dry_run:
            print(f"  would copy {rel} -> {target.relative_to(ROOT)}")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, target)
        copied += 1
    print(f"{'DRY-RUN: ' if args.dry_run else ''}{copied} file(s) from contract path {src.relative_to(ROOT)}")

    gate = subprocess.run(
        [sys.executable, str(ROOT / "execution" / "skill_auditor.py"), "check", "--skill", args.skill_id],
        cwd=ROOT, capture_output=True, text=True,
    )
    print(gate.stdout, end="")
    if gate.stderr:
        print(gate.stderr, end="", file=sys.stderr)
    # Fleet standard is 6/6, stricter than the auditor's own exit code (which
    # clears at ≤1 failure — that latitude let a 5/6 merge slip through on
    # 2026-07-17, deya-business-systems). Any failing check = exit 1.
    if "0/6 failing" not in gate.stdout:
        return 1
    return gate.returncode


if __name__ == "__main__":
    sys.exit(main())
