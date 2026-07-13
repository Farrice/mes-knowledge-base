#!/usr/bin/env python3
"""Forge queue — wave builder for the born-v2 prompt backfill.

Enumerates skills with NO structure-pure v2 prompts (skills/<s>/references/
prompts-v2/ absent or empty), inventories each skill's forgeable material
(SKILL.md, genius.md, workflows, references), and emits wave-sized batches to
forge-input.json for the fleet. Resume-safe the RIGHT way: a skill leaves the
queue only when its prompts-v2 dir has files that PASS renaissance_audit
checks (existence alone is not done — see docs/solutions/
2026-07-11-concurrent-writer-queue-poisoning-quality-gate.md).

Usage:
  python3 execution/forge_queue.py --status
  python3 execution/forge_queue.py --wave-size 25          # → forge-input.json
  python3 execution/forge_queue.py --wave-size 25 --include-archived
"""
import argparse
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_active", "prompt-wiring-os-2026-07-13", "forge-input.json")

sys.path.insert(0, os.path.join(ROOT, "execution"))
from renaissance_audit import audit_file  # noqa: E402


def is_archived(skill_md_path):
    try:
        head = open(skill_md_path, encoding="utf-8", errors="replace").read(2000)
    except OSError:
        return False
    return bool(re.search(r"^status:\s*archived", head, re.M))


def skill_inventory(skill_dir):
    name = os.path.basename(skill_dir.rstrip("/"))
    skill_md = os.path.join(skill_dir, "SKILL.md")
    if not os.path.exists(skill_md):
        return None
    v2_dir = os.path.join(skill_dir, "references", "prompts-v2")
    v2_files = glob.glob(os.path.join(v2_dir, "*.md"))
    # done = at least one v2 file AND all of them pass the audit gate
    if v2_files and all(not audit_file(f) for f in v2_files):
        return None
    workflows = sorted(
        os.path.relpath(w, ROOT)
        for w in glob.glob(os.path.join(skill_dir, "workflows", "*.md"))
    )
    return {
        "skill": name,
        "skill_md": os.path.relpath(skill_md, ROOT),
        "genius_md": os.path.relpath(os.path.join(skill_dir, "genius.md"), ROOT)
        if os.path.exists(os.path.join(skill_dir, "genius.md")) else None,
        "workflows": workflows,
        "archived": is_archived(skill_md),
        "existing_v2_failing": [os.path.relpath(f, ROOT) for f in v2_files],
    }


def main():
    # One-driver-per-tree guard (orchestration doctrine Law 5)
    import subprocess as _sp
    _lock = _sp.run(["python3", os.path.join(ROOT, "execution", "session_lock.py"), "check",
                     os.environ.get("SESSION_LOCK_TOKEN", "")], capture_output=True, text=True)
    if _lock.returncode != 0:
        print(_lock.stdout.strip() or "BLOCKED by session lock")
        print("claim it first: python3 execution/session_lock.py claim \"<mission>\"  (export SESSION_LOCK_TOKEN=<token>)")
        raise SystemExit(1)
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--wave-size", type=int, default=0, help="number of SKILLS per wave")
    ap.add_argument("--include-archived", action="store_true")
    args = ap.parse_args()

    todo = []
    for d in sorted(glob.glob(os.path.join(ROOT, "skills", "*/"))):
        inv = skill_inventory(d)
        if inv is None:
            continue
        if inv["archived"] and not args.include_archived:
            continue
        todo.append(inv)

    archived_skipped = sum(1 for d in sorted(glob.glob(os.path.join(ROOT, "skills", "*/")))
                           if (i := skill_inventory(d)) and i["archived"]) if not args.include_archived else 0

    if args.status or not args.wave_size:
        print(f"skills needing born-v2 forge: {len(todo)}"
              + (f" (+{archived_skipped} archived excluded — lazy path)" if archived_skipped else ""))
        return

    wave = todo[: args.wave_size]
    payload = {
        "standard": "born-v2 (directives/prompt-forging-spec.md)",
        "total_skills": len(wave),
        "remaining_after_wave": len(todo) - len(wave),
        "skills": wave,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(payload, open(OUT, "w"), indent=1)
    print(f"wave: {len(wave)} skills · remaining after: {len(todo) - len(wave)}")
    print(f"→ {OUT}")


if __name__ == "__main__":
    main()
