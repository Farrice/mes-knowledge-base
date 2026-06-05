#!/usr/bin/env python3
"""
Build seamless Claude-Project upload bundles for the Resonance AI Team.

For each of the 5 projects, produces a folder under claude-project-uploads/ containing:
  - CUSTOM-INSTRUCTIONS.txt  (the Constitution-Core block + that project's ROLE block,
    concatenated — paste this ONE file into the project's Custom Instructions)
  - all of that project's knowledge files, copied in (drag the whole folder into the
    project's knowledge)
  - _UPLOAD-ME.txt  (2-line provisioning instruction)

Re-run this any time the Core or a role block changes. Idempotent.
"""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # projects/andrea-dj/
AI_TEAM = ROOT / "ai-team"
BOS = ROOT / "brand-operating-system"
OUT = AI_TEAM / "claude-project-uploads"

CORE_FILE = AI_TEAM / "shared" / "CONSTITUTION-CORE.md"

# (basename-in-bundle, source-path-relative-to-projects/andrea-dj)
FOUNDATION = {
    "00-master-index.md": "brand-operating-system/00-foundation/00-master-index.md",
    "01-brand-bible.md": "brand-operating-system/00-foundation/01-brand-bible.md",
    "02-icp-master.md": "brand-operating-system/00-foundation/02-icp-master.md",
    "03-voice-document.md": "brand-operating-system/00-foundation/03-voice-document.md",
    "04-positioning-one-pager.md": "brand-operating-system/00-foundation/04-positioning-one-pager.md",
    "05-non-negotiables.md": "brand-operating-system/00-foundation/05-non-negotiables.md",
}
SHARED = {
    "CONSTITUTION-CORE.md": "ai-team/shared/CONSTITUTION-CORE.md",
    "TEAM-MAP.md": "ai-team/shared/TEAM-MAP.md",
    "wrong-ai-ledger.md": "ai-team/shared/wrong-ai-ledger.md",
}
# Sourced Audience & Set Intelligence brief (2026-06-04 deep-research swarm)
BRIEF = "research/2026-06-04-audience-set-intelligence-brief.md"

PROJECTS = {
    "1-front-of-house": {
        "role_src": "ai-team/projects/01-front-of-house.md",
        "knowledge": [
            SHARED["CONSTITUTION-CORE.md"], SHARED["TEAM-MAP.md"],
            FOUNDATION["00-master-index.md"], FOUNDATION["01-brand-bible.md"],
            FOUNDATION["02-icp-master.md"], FOUNDATION["03-voice-document.md"],
            FOUNDATION["04-positioning-one-pager.md"], FOUNDATION["05-non-negotiables.md"],
            "brand-operating-system/03-marketing/03-channel-architecture.md",
            "brand-operating-system/03-marketing/07-funnel.md",
            BRIEF,
        ],
    },
    "2-the-crowd": {
        "role_src": "ai-team/projects/02-the-crowd.md",
        "knowledge": [
            SHARED["CONSTITUTION-CORE.md"], SHARED["wrong-ai-ledger.md"],
            FOUNDATION["03-voice-document.md"], FOUNDATION["02-icp-master.md"],
            FOUNDATION["05-non-negotiables.md"],
            "brand-operating-system/02-briefs/ig-feed-post.md",
            "brand-operating-system/02-briefs/ig-reel.md",
            "brand-operating-system/02-briefs/ig-story.md",
            "brand-operating-system/02-briefs/email-newsletter.md",
            "brand-operating-system/03-marketing/01-content-pillars.md",
            "brand-operating-system/03-marketing/02-hook-library.md",
            "brand-operating-system/04-ai-handoff/03-image-prompt-formulas.md",
            BRIEF,
        ],
    },
    "3-the-doorkeeper": {
        "role_src": "ai-team/projects/03-the-doorkeeper.md",
        "knowledge": [
            SHARED["CONSTITUTION-CORE.md"],
            FOUNDATION["02-icp-master.md"], FOUNDATION["05-non-negotiables.md"],
            FOUNDATION["03-voice-document.md"],
            "brand-operating-system/03-marketing/06-why-gate-mechanics.md",
            "brand-operating-system/05-ops/03-drift-signals.md",
            BRIEF,
        ],
    },
    "4-the-green-room": {
        "role_src": "ai-team/projects/04-the-green-room.md",
        "knowledge": [
            SHARED["CONSTITUTION-CORE.md"],
            FOUNDATION["04-positioning-one-pager.md"], FOUNDATION["05-non-negotiables.md"],
            FOUNDATION["03-voice-document.md"],
            "brand-operating-system/02-briefs/venue-pitch.md",
            "brand-operating-system/02-briefs/press-one-sheeter.md",
            "brand-operating-system/02-briefs/dj-booking-pack.md",
            ("brand-operating-system/../launch/02-outreach-playbook/README.md", "outreach-playbook.md"),
        ],
    },
    "5-the-logbook": {
        "role_src": "ai-team/projects/05-the-logbook.md",
        "knowledge": [
            SHARED["CONSTITUTION-CORE.md"], SHARED["wrong-ai-ledger.md"],
            FOUNDATION["02-icp-master.md"], FOUNDATION["03-voice-document.md"],
            "brand-operating-system/05-ops/04-success-metrics.md",
            "brand-operating-system/05-ops/05-exit-interview-protocol.md",
        ],
    },
    "6-the-booth": {
        "role_src": "ai-team/projects/06-the-booth.md",
        "knowledge": [
            SHARED["CONSTITUTION-CORE.md"], BRIEF,
            FOUNDATION["05-non-negotiables.md"], FOUNDATION["03-voice-document.md"],
            "brand-operating-system/05-ops/06-run-of-show.md",
            "brand-operating-system/02-briefs/dj-booking-pack.md",
        ],
    },
}


def extract_core() -> str:
    # Pull the REAL block from inside the ``` code fence, not the prose mention of the tag.
    text = CORE_FILE.read_text()
    m = re.search(r"```\n(<resonance_core\b.*?</resonance_core>)\n```", text, re.DOTALL)
    if not m:
        raise SystemExit("Core block not found inside a code fence in CONSTITUTION-CORE.md")
    return m.group(1).strip()


def extract_role(role_src: str) -> str:
    # Pull the fenced role block, not the inline prose mention of the tag.
    text = (ROOT / role_src).read_text()
    m = re.search(r"```\n(<role_\w+>.*?</role_\w+>)\n```", text, re.DOTALL)
    if not m:
        raise SystemExit(f"ROLE block not found inside a code fence in {role_src}")
    return m.group(1).strip()


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    core = extract_core()
    summary = []
    for name, spec in PROJECTS.items():
        folder = OUT / name
        folder.mkdir()
        role = extract_role(spec["role_src"])
        pretty = name.split("-", 1)[1].replace("-", " ").title()
        (folder / "CUSTOM-INSTRUCTIONS.txt").write_text(
            f"{core}\n\n\n{role}\n"
        )
        copied = 0
        for entry in spec["knowledge"]:
            if isinstance(entry, tuple):
                src_rel, dest_name = entry
            else:
                src_rel, dest_name = entry, Path(entry).name
            src = (ROOT / src_rel).resolve()
            if not src.exists():
                print(f"  !! MISSING {src_rel}")
                continue
            shutil.copy2(src, folder / dest_name)
            copied += 1
        (folder / "_UPLOAD-ME.txt").write_text(
            f"PROJECT: {pretty}\n\n"
            f"1. Paste ALL of CUSTOM-INSTRUCTIONS.txt into this project's Custom Instructions.\n"
            f"2. Upload every OTHER file in this folder into the project's Knowledge.\n"
            f"   (Skip CUSTOM-INSTRUCTIONS.txt and this file when uploading knowledge.)\n"
            f"3. Test with one example line from the project's guide. Ship only when it flinches.\n"
        )
        summary.append((pretty, copied))
    print("Built bundles:")
    for pretty, copied in summary:
        print(f"  {pretty}: 1 instructions file + {copied} knowledge files")


if __name__ == "__main__":
    main()
