#!/usr/bin/env python3
"""Assemble self-contained per-room folders from the reformatted _pool + name-swapped _instructions.
Run AFTER the reformat workflow completes and the pool is verified. Idempotent (rebuilds rooms/)."""
import json, os, shutil, sys

BUILD = os.path.dirname(os.path.abspath(__file__))
POOL = os.path.join(BUILD, "_pool")
INSTR = os.path.join(BUILD, "_instructions")
ROOMS = os.path.join(BUILD, "rooms")
manifest = json.load(open(os.path.join(BUILD, "manifest.json")))

# new-project-number -> instruction filename (already name-swapped)
INSTR_FILE = {
    1: "1-planning-strategy.md",
    2: "2-content-social.md",
    3: "3-applications-vetting.md",
    4: "4-partners-outreach.md",
    5: "5-music-and-the-floor.md",
    6: "6-event-memory.md",
}
MODEL_WHY = {
    "Opus": "Opus — this one needs careful judgment and strategy.",
    "Sonnet": "Sonnet — fast and great for everyday volume.",
}

def setup_doc(room, knowledge_files, instructions_text):
    """Build the '★ SETUP' sheet markdown for a room. Instructions embedded in a fenced block for clean copy."""
    name = room["folder"].split("—", 1)[1].strip() if "—" in room["folder"] else room["folder"]
    lines = []
    lines.append(f"# ★ SETUP — {name}")
    lines.append("")
    lines.append(f"*Everything for your **{name}** Claude project is in this folder. Setup takes about 3 minutes — just follow the three steps.*")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## What this project is for")
    lines.append("")
    lines.append(room["purpose"])
    lines.append("")
    lines.append(f"**Model to pick:** {MODEL_WHY[room['model']]}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Step 1 — Make the project")
    lines.append("")
    lines.append(f"In Claude, create a new Project and name it **{name}**.")
    lines.append("")
    lines.append("## Step 2 — Paste the custom instructions")
    lines.append("")
    lines.append("Copy **everything** in the box below and paste it into the project's *Custom instructions* field. Don't change it. (It's also saved next to this sheet as `CUSTOM-INSTRUCTIONS.md` if you'd rather copy from there.)")
    lines.append("")
    lines.append("```")
    lines.append(instructions_text.rstrip())
    lines.append("```")
    lines.append("")
    lines.append("## Step 3 — Add the knowledge files")
    lines.append("")
    lines.append("Upload these files from this folder into the project's knowledge (drag them in, or use *Add content*):")
    lines.append("")
    for f in knowledge_files:
        lines.append(f"- `{f}`")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("That's it. Open the project and just talk to it the way you'd talk to a teammate — it already knows the brand, your voice, and the twelve lines.")
    lines.append("")
    return "\n".join(lines)

def main():
    if os.path.isdir(ROOMS):
        shutil.rmtree(ROOMS)
    os.makedirs(ROOMS)
    summary = []
    for room in manifest["rooms"]:
        folder = os.path.join(ROOMS, room["folder"])
        os.makedirs(folder)
        # 1. instructions (name-swapped) -> CUSTOM-INSTRUCTIONS.md
        instr_src = os.path.join(INSTR, INSTR_FILE[room["num"]])
        instr_text = open(instr_src, encoding="utf-8").read()
        open(os.path.join(folder, "CUSTOM-INSTRUCTIONS.md"), "w", encoding="utf-8").write(instr_text)
        # 2. knowledge files from pool
        knowledge = []
        docs = list(room["docs"])
        # team-map only belongs in Planning & Strategy (room 1)
        if room["num"] == 1 and "team-map" not in docs:
            docs.append("team-map")
        # dedupe, preserve order
        seen = set(); docs = [d for d in docs if not (d in seen or seen.add(d))]
        for doc_id in docs:
            src = os.path.join(POOL, doc_id + ".md")
            if not os.path.isfile(src):
                print(f"  !! MISSING pool doc: {doc_id} (room {room['num']})", file=sys.stderr)
                continue
            fname = doc_id + ".md"
            shutil.copyfile(src, os.path.join(folder, fname))
            knowledge.append(fname)
        # 3. SETUP sheet
        setup_md = setup_doc(room, knowledge, instr_text)
        open(os.path.join(folder, f"★ SETUP - open me first.md"), "w", encoding="utf-8").write(setup_md)
        summary.append((room["folder"], len(knowledge)))
        print(f"  built {room['folder']}: {len(knowledge)} knowledge files + instructions + SETUP")
    # START HERE at rooms root
    start = []
    start.append("# ★ START HERE — Setting Up Your Resonance AI Team")
    start.append("")
    start.append("*Six small AI projects that hold the brand for you — so you can stay in your zone (the music, the curating, the room) and hand off the rest.*")
    start.append("")
    start.append("---")
    start.append("")
    start.append("You're setting up six Claude Projects. Each one lives in its own folder here. Open the folders in order — each has a **★ SETUP** sheet that walks you through it in about three minutes.")
    start.append("")
    start.append("## The six projects")
    start.append("")
    start.append("| # | Project | Use it for | Model |")
    start.append("|---|---------|-----------|-------|")
    rows = {
        1: ("Planning & Strategy", "Thinking, planning, deciding what's next. Your front door — start here when unsure.", "Opus"),
        2: ("Content & Social", "Anything the world reads: IG posts, reels, stories, captions, emails.", "Sonnet"),
        3: ("Applications & Vetting", "Who gets in: DMs, applications, accept/decline, sponsor offers.", "Opus"),
        4: ("Partners & Outreach", "Venues, press, DJs, sponsors, outreach.", "Sonnet"),
        5: ("Music & The Floor", "The set, tempo, the floor, day-of flow.", "Sonnet"),
        6: ("Event Memory", "*(After July 18.)* Couples who met, voice corrections, lessons.", "Sonnet"),
    }
    for n in range(1, 7):
        nm, use, mdl = rows[n]
        start.append(f"| {n} | **{nm}** | {use} | {mdl} |")
    start.append("")
    start.append("## Set them up in this order")
    start.append("")
    start.append("1. **Planning & Strategy** — your front door")
    start.append("2. **Content & Social**")
    start.append("3. **Applications & Vetting**")
    start.append("4. **Partners & Outreach**")
    start.append("5. **Music & The Floor**")
    start.append("6. **Event Memory** — wait until after July 18")
    start.append("")
    start.append("## How each folder works")
    start.append("")
    start.append("Inside every project folder you'll find:")
    start.append("")
    start.append("- **★ SETUP - open me first** — open this first. Three steps.")
    start.append("- **CUSTOM-INSTRUCTIONS.md** — the text you paste into the project's instructions (also shown inside the SETUP sheet).")
    start.append("- **the rest of the `.md` files** — the project's knowledge. Upload all of them.")
    start.append("")
    start.append("## The one thing that matters")
    start.append("")
    start.append("Every project carries the same heart — daytime, sober, curated, your twelve lines, your voice. You never have to remember the system. When in doubt, open **Planning & Strategy** and it'll point you to the right room.")
    start.append("")
    open(os.path.join(ROOMS, "★ START HERE - how to set up your team.md"), "w", encoding="utf-8").write("\n".join(start))
    print(f"\nAssembled {len(summary)} rooms + START HERE into {ROOMS}")

if __name__ == "__main__":
    main()
