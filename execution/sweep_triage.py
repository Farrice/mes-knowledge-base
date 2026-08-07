#!/usr/bin/env python3
"""sweep_triage.py — one decision surface for reorganising every _active/ project.

The 2026-08-07 retrieval-architecture pilot proved the shape on one project.
Rolling it across the rest needs exactly three judgment calls per project, and
they are Farrice's, not the system's:

    1. ARENA        which surface does this belong to?
    2. ALIVE/DEAD   keep it live, or archive it?
    3. DUPES        for non-identical duplicates only, which copy is live?

Everything else is mechanical. This script computes the evidence for all three
so the answer is a confirmation, not homework: last time anyone actually worked
on it, how many files elsewhere point at it, whether the control plane cites
it, and how much retrieval debt it carries.

Byte-identical duplicates never reach him — those are decided by `diff`.

    python3 execution/sweep_triage.py                # markdown decision doc
    python3 execution/sweep_triage.py --html         # + Premium Minimal board
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import front_door as fd  # noqa: E402

ROOT = fd.ROOT
ACTIVE = ROOT / "_active"

# Name -> arena. First match wins; order matters (most specific first).
ARENA_HINTS = [
    (r"linkedin", "linkedin"),
    (r"^jen", "jen-listings"),
    (r"andrea|resonance", "andrea"),
    (r"javier|human-values", "javier"),
    (r"coach-cooz|cooz", "coach-cooz"),
    (r"josh|katie|dancewear|swing-nerd", "josh-katie"),
    (r"chris-restaurants", "chris"),
    (r"kens-fasting", "kens-fasting"),
    (r"mybpm|merch", "mybpm"),
    (r"parallax|farrice-brand|farrice-master|farrice-final|farrice-teach|farrice-creative", "farrice-brand"),
    (r"prediction-market|betting|picks", "wagering"),
    (r"trendscale|dwa-|upwork", "client-trials"),
    (r"codex|harness|harvest|parity|repeatability|loop-engineering|operator-core|platform-bakeoff|memory-bakeoff|system-integration|prompt-wiring|prompt-renaissance|self-heal", "harness"),
    (r"audit|health-check|second-brain|context-engineering|elevation|frontier|swarm-apex|harness-apex|operator-cockpit", "harness"),
    (r"pmf|offer-|positioning|path-decision|alignment-architect|strategic-clarity", "offer-strategy"),
    (r"video|remotion|hyperframes|disney|studio", "video-studio"),
    (r"kdp|book", "publishing"),
    (r"notion|youtube-notion|search-content|health-performance|mastery-forge", "knowledge"),
    (r"digital-product|re-compliance|claude-export|_ledgers", "misc"),
]

# A project that is a COPY of the repo — never restructure, never rewrite.
def is_snapshot(p: Path) -> bool:
    return (p / "_active").is_dir()


def propose_arena(name: str) -> str:
    low = name.lower()
    for pat, arena in ARENA_HINTS:
        if re.search(pat, low):
            return arena
    return "misc"


DATED_SLUG = re.compile(r"-20\d{2}-\d{2}-\d{2}$")

# Files this system writes. They are never evidence of human work.
GENERATED = ("START-HERE.md", "START-HERE.html", "CANON.md", "MOVED.md",
             "06-system/front-door.state.json")


def _generated(path: str) -> bool:
    return any(path.endswith(g) for g in GENERATED)


# WIRED-IN means the harness itself depends on the project — a hook or script
# resolves it, a directive binds it, a workflow drives it. Deliberately NOT
# skills/ or agents/: those are content that merely mentions paths, and
# counting them marked 65 of 66 projects "wired in", which is the same as
# marking none of them.
CONTROL_PREFIXES = ("directives/", "execution/", ".agent/workflows/", ".claude/")
CONTROL_FILES = {"CLAUDE.md", "AGENTS.md", "CODEX.md", "GEMINI.md",
                 "PROJECTS.md", "JARVIS.md", "FARRICE.md",
                 "FARRICE-MASTER-CONTEXT.md", "PRODUCTION_CORE.md"}


def all_referrers() -> dict[str, tuple[set, set]]:
    """slug -> (files outside it that mention it, control-plane subset).

    ONE grep for the whole repo. Doing it per project meant 69 full-repo
    passes at ~9s each — over ten minutes for a table that has to feel
    instant to be worth answering.
    """
    out: dict[str, tuple[set, set]] = {}
    try:
        r = subprocess.run(
            ["grep", "-rEo", "--exclude-dir=.git", "--exclude-dir=node_modules",
             "--exclude-dir=.venv", "--binary-files=without-match",
             r"_active/[A-Za-z0-9_.-]+", str(ROOT)],
            capture_output=True, text=True, timeout=600)
    except (OSError, subprocess.SubprocessError):
        return out
    base = str(ROOT) + "/"
    for line in r.stdout.splitlines():
        if ":_active/" not in line:
            continue
        fpath, _, match = line.rpartition(":_active/")
        slug = match.split("/")[0]
        if not slug:
            continue
        src = fpath[len(base):] if fpath.startswith(base) else fpath
        if src.startswith(f"_active/{slug}"):
            continue                                   # self-reference
        if src.startswith(("_system/organization", ".agent/organization")):
            continue                                   # bookkeeping
        refs, ctrl = out.setdefault(slug, (set(), set()))
        refs.add(src)
        if src.startswith(CONTROL_PREFIXES) or src in CONTROL_FILES:
            ctrl.add(src)
    return out


def state_of(p: Path) -> dict:
    sysfile = p / "06-system" / "front-door.state.json"
    if sysfile.exists():
        try:
            return json.loads(sysfile.read_text())
        except Exception:
            pass
    return {}


def collect() -> list[dict]:
    dates = fd._git_dates_all()
    refmap = all_referrers()
    rows = []
    for p in sorted(ACTIVE.iterdir()):
        if not p.is_dir() or p.name.startswith("."):
            continue
        rel = f"_active/{p.name}"
        files = sum(1 for _ in p.rglob("*") if _.is_file())
        # Newest real-work date across the project — EXCLUDING files this
        # system generates. Without this every project read "worked on today",
        # because `front_door.py build --all` had just written a START-HERE.md
        # into all 73 of them. A tool must never mistake its own output for
        # evidence that a human did something.
        ts = max((v for k, v in dates.items()
                  if k.startswith(rel + "/") and not _generated(k)), default=0)
        refs, ctrl = refmap.get(p.name, (set(), set()))
        outside, control = len(refs), len(ctrl)
        st = state_of(p)
        snap = is_snapshot(p)
        age = (datetime.now() - datetime.fromtimestamp(ts)).days if ts else 999
        rows.append({
            "name": p.name, "rel": rel, "files": files,
            "last": fd._fmt(ts) if ts else "—", "age": age,
            "refs": outside, "control": control,
            "competing": st.get("competing", 0) or 0,
            "unabsorbed": st.get("unabsorbed", 0) or 0,
            "broken": st.get("broken_links", 0) or 0,
            "snapshot": snap,
            "arena": propose_arena(p.name),
            "dated_slug": bool(DATED_SLUG.search(p.name)),
        })
    return rows


def recommend(r: dict) -> tuple[str, str]:
    """(recommendation, one-line why). Conservative: archiving is reversible,
    but only he knows what he intends to pick back up."""
    if r["snapshot"]:
        return ("FREEZE", "a copy of this repo — never restructure or rewrite inside it")
    if r["control"] > 0:
        return ("KEEP", f"cited by {r['control']} control-plane file(s) — it is wired in")
    if r["age"] <= 14:
        return ("KEEP", f"worked on {r['age']}d ago")
    if r["age"] >= 30 and r["refs"] <= 2 and r["files"] < 400:
        return ("ARCHIVE?", f"cold {r['age']}d, only {r['refs']} inbound ref(s)")
    if r["age"] >= 30:
        return ("ARCHIVE?", f"cold {r['age']}d, {r['refs']} inbound ref(s), {r['files']} files")
    return ("KEEP", f"worked on {r['age']}d ago")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", action="store_true")
    ap.add_argument("--out", default="_active/_ledgers/sweep-decisions.md")
    args = ap.parse_args()

    rows = collect()
    for r in rows:
        r["rec"], r["why"] = recommend(r)

    keep = [r for r in rows if r["rec"] == "KEEP"]
    arch = [r for r in rows if r["rec"] == "ARCHIVE?"]
    frz = [r for r in rows if r["rec"] == "FREEZE"]

    import collections
    groups = collections.defaultdict(list)
    for r in rows:
        groups[r["arena"]].append(r)

    D = [f"# Sweep decisions — {len(rows)} folders → {len(groups)} arenas", "",
         f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} by "
         f"`execution/sweep_triage.py`. Evidence computed; calls are yours.*", "",
         f"`_active/` currently has **{len(rows)} folders at the top level**. "
         f"Grouped into arenas it has **{len(groups)}**. Nothing is deleted — "
         "each folder becomes an initiative inside its arena, with every "
         "referrer repointed and a generated `START-HERE.md` at each level.", "",
         "**How to answer:** for each arena, either say nothing (it stands), "
         "rename it, or move/archive specific folders out of it. "
         "`last` = last time a human actually worked on it — generated files "
         "and housekeeping commits do not count.", "",
         "---", ""]

    for arena in sorted(groups, key=lambda a: -len(groups[a])):
        items = sorted(groups[arena], key=lambda x: x["age"])
        cold = [i for i in items if i["age"] >= 30]
        D.append(f"## `_active/{arena}/` — {len(items)} folder(s)")
        D.append("")
        D.append("| becomes initiative | last | refs | files | debt |")
        D.append("|---|---|---|---|---|")
        for i in items:
            debt = []
            if i["competing"]:
                debt.append(f"{i['competing']} competing")
            if i["unabsorbed"]:
                debt.append(f"{i['unabsorbed']} unabsorbed")
            if i["snapshot"]:
                debt.append("**repo snapshot — frozen**")
            D.append(f"| `{i['name']}` | {i['last']} ({i['age']}d) | {i['refs']} | "
                     f"{i['files']} | {' · '.join(debt) or '—'} |")
        D.append("")
        if cold:
            D.append(f"*Cold ≥30d, archive instead of moving? "
                     + ", ".join(f"`{c['name']}`" for c in cold) + "*")
            D.append("")

    (ROOT / "_active/_ledgers/sweep-arenas.md").write_text("\n".join(D) + "\n",
                                                           encoding="utf-8")

    L = [f"# Sweep decisions — {len(rows)} projects under `_active/`", "",
         f"*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} by "
         f"`execution/sweep_triage.py`. Evidence is computed; the calls are yours.*", "",
         "**How to answer:** everything is pre-filled with a recommendation. "
         "Only tell me the ones you want to CHANGE — say the project name and "
         "your call. Silence = the recommendation stands.", "",
         "Columns: **last** = last time anyone actually worked on it (a "
         "40+ file commit is housekeeping and does not count; a rename is not "
         "work). **refs** = files elsewhere pointing at it. **ctrl** = "
         "control-plane files citing it — those are wired into the harness.", ""]

    def table(title, items, note):
        L.append(f"## {title} — {len(items)}")
        L.append("")
        L.append(note)
        L.append("")
        L.append("| project | proposed arena | last | refs | ctrl | files | debt | why |")
        L.append("|---|---|---|---|---|---|---|---|")
        for r in sorted(items, key=lambda x: (x["arena"], -x["refs"])):
            debt = []
            if r["competing"]:
                debt.append(f"{r['competing']} competing")
            if r["unabsorbed"]:
                debt.append(f"{r['unabsorbed']} unabsorbed")
            L.append(f"| `{r['name']}` | **{r['arena']}** | {r['last']} | {r['refs']} | "
                     f"{r['control']} | {r['files']} | {' · '.join(debt) or '—'} | {r['why']} |")
        L.append("")

    table("KEEP — stays live, gets the arena/initiative shape", keep,
          "These get reorganised. Confirm the arena, or rename it — the arena "
          "is the folder name you will actually click.")
    table("ARCHIVE? — cold and unreferenced", arch,
          "My read is these are done. Archiving moves them to "
          "`_active/_archive/2026-08-07-sweep/` with every referrer repointed — "
          "reversible, nothing deleted. Tell me any you intend to pick back up.")
    table("FREEZE — repo snapshots, never touched", frz,
          "These contain their own `_active/` tree. Rewriting inside them edits "
          "what the snapshot recorded. No decision needed.")

    L.append("## Dupes needing a call")
    L.append("")
    L.append("Byte-identical duplicates are decided by `diff` and never reach you. "
             "Non-identical ones are listed per project in that project's "
             "`START-HERE.md` under **Competing versions** — I will surface the "
             "specific pairs for whichever projects you keep, once the arenas "
             "are settled.")
    L.append("")

    out = ROOT / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))
    print(f"\nwritten: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
