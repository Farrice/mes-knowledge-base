#!/usr/bin/env python3
"""
Verifier for the `persona_team.py critique` / `digest` subcommands.

Runs the real CLI (subprocess) against a scratch temp dir with fake fixtures — never
the real repo's agents/_framework/seats or skills/ — via --seat-prompts-dir and
--skills-root overrides. Also exercises critique_digest()/render_ledger() directly
as importable functions.

CLI: python3 execution/verify_persona_critique.py
Prints "N pass / M fail" and exits 1 on any failure.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PERSONA_TEAM = ROOT / "execution" / "persona_team.py"

sys.path.insert(0, str(ROOT / "execution"))
from persona_team import critique_digest, render_ledger  # noqa: E402

PASS = 0
FAIL = 0
FAILURES = []


def check(name: str, condition: bool, detail: str = ""):
    global PASS, FAIL
    if condition:
        PASS += 1
    else:
        FAIL += 1
        FAILURES.append(f"{name}: {detail}")


def run_cli(args, cwd=None):
    result = subprocess.run(
        [sys.executable, str(PERSONA_TEAM)] + args,
        capture_output=True, text=True, cwd=cwd or str(ROOT),
    )
    return result


def main():
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)

        # ── Fixtures: never the real repo ──
        artifact = base / "artifact.md"
        artifact.write_text("\n".join(f"artifact line {i} — some claim about the launch" for i in range(1, 31)) + "\n")

        bar = base / "bar.md"
        bar.write_text("\n".join(f"bar line {i} — a standard the artifact must meet" for i in range(1, 21)) + "\n")

        seats_dir = base / "agents" / "_framework" / "seats"
        seats_dir.mkdir(parents=True)
        (seats_dir / "x.md").write_text("# Seat X\nYou are lens X. Judge structural soundness only.\n")

        skills_dir = base / "skills"
        (skills_dir / "y").mkdir(parents=True)
        (skills_dir / "y" / "SKILL.md").write_text("# Skill Y\nSKILL.md body for lens y — the bench is the skill library.\n")
        (skills_dir / "y" / "genius.md").write_text("# Genius Y\nGenius excerpt for lens y — voice, not summary.\n")

        # ── Test 1: 2 READY seats (one via seat file, one via skill fallback) ──
        out1 = base / "out1"
        r1 = run_cli([
            "critique", "--artifact", str(artifact), "--bar", str(bar),
            "--lenses", "x,y", "--run", "test", "--platform", "claude",
            "--out", str(out1), "--seat-prompts-dir", str(seats_dir),
            "--skills-root", str(skills_dir),
        ])
        check("test1: exit code 0 (>=1 READY)", r1.returncode == 0, f"stderr={r1.stderr}")
        try:
            plan1 = json.loads(r1.stdout)
        except Exception as exc:
            plan1 = {}
            check("test1: valid JSON on stdout", False, str(exc))
        else:
            check("test1: valid JSON on stdout", True)

        seats1 = plan1.get("seats", [])
        check("test1: 2 seats returned", len(seats1) == 2, str(seats1))
        ready1 = [s for s in seats1 if s.get("status") == "READY"]
        check("test1: both seats READY", len(ready1) == 2, str(seats1))

        for s in seats1:
            bp = s.get("brief_path")
            if not bp or not Path(bp).exists():
                check(f"test1: brief file exists for {s.get('lens')}", False, str(s))
                continue
            text = Path(bp).read_text(encoding="utf-8")
            first_line = text.splitlines()[0] if text.splitlines() else ""
            check(f"test1: [swarm:test] header line 1 for {s['lens']}",
                  first_line == f"[swarm:test] {s['lens']}", first_line)
            check(f"test1: artifact text present for {s['lens']}",
                  "artifact line 1 " in text, "artifact text missing")
            check(f"test1: bar text present for {s['lens']}",
                  "bar line 1 " in text, "bar text missing")

        # ── Test 2: oversized (7 KB) artifact -> INPUT_GAP ──
        big_artifact = base / "big_artifact.md"
        big_artifact.write_text("x" * 7168)
        out2 = base / "out2"
        r2 = run_cli([
            "critique", "--artifact", str(big_artifact), "--bar", str(bar),
            "--lenses", "x", "--run", "test2", "--platform", "codex",
            "--out", str(out2), "--seat-prompts-dir", str(seats_dir),
            "--skills-root", str(skills_dir),
        ])
        check("test2: exit code 1 (0 READY)", r2.returncode == 1, f"stderr={r2.stderr}")
        try:
            plan2 = json.loads(r2.stdout)
        except Exception as exc:
            plan2 = {}
            check("test2: valid JSON on stdout", False, str(exc))
        seats2 = plan2.get("seats", [])
        check("test2: 1 seat returned", len(seats2) == 1, str(seats2))
        if seats2:
            check("test2: status INPUT_GAP", seats2[0].get("status") == "INPUT_GAP", str(seats2[0]))
            check("test2: bytes > 6144", (seats2[0].get("bytes") or 0) > 6144, str(seats2[0]))
            check("test2: no brief file written", not (out2 / "x-brief.md").exists(),
                  "brief file should not exist for INPUT_GAP seat")

        # ── Test 3: 5 lenses -> the 5th is SEAT_CAP ──
        out3 = base / "out3"
        r3 = run_cli([
            "critique", "--artifact", str(artifact), "--bar", str(bar),
            "--lenses", "x,y,x,y,x", "--run", "test3", "--platform", "claude",
            "--out", str(out3), "--seat-prompts-dir", str(seats_dir),
            "--skills-root", str(skills_dir),
        ])
        try:
            plan3 = json.loads(r3.stdout)
        except Exception as exc:
            plan3 = {}
            check("test3: valid JSON on stdout", False, str(exc))
        seats3 = plan3.get("seats", [])
        check("test3: 5 seats returned", len(seats3) == 5, str(seats3))
        if len(seats3) == 5:
            check("test3: seats 1-4 not SEAT_CAP",
                  all(s.get("status") != "SEAT_CAP" for s in seats3[:4]), str(seats3[:4]))
            check("test3: 5th seat is SEAT_CAP", seats3[4].get("status") == "SEAT_CAP", str(seats3[4]))
            check("test3: 5th seat has no brief_path", seats3[4].get("brief_path") is None, str(seats3[4]))

        # ── Test 4: critique_digest() on 3 fixtures (direct import) ──
        fixtures = [
            {"lens": "a", "biggest_gap": "Missing proof the price beats the comp set",
             "evidence_lines": ["artifact:L5 \"$620/mo\"", "bar:L3 \"cite comparable pricing\""],
             "proposed_fix": "add a comp table", "dissent": "none because the bar is satisfied elsewhere"},
            {"lens": "b", "biggest_gap": "Missing proof the price beats the comp set",
             "evidence_lines": ["artifact:L6 \"no comps shown\"", "bar:L4 \"comp table required\""],
             "proposed_fix": "cite 3 comps with dates", "dissent": "I disagree the bar's comp count of 3 is necessary; 1 suffices"},
            {"lens": "c", "biggest_gap": None, "evidence_lines": [], "proposed_fix": None,
             "dissent": "none because no gap found against the bar"},
        ]
        digest = critique_digest(fixtures)
        check("test4: crux is the shared gap",
              digest.get("crux") == "Missing proof the price beats the comp set", str(digest))
        check("test4: dissent_log has exactly 1 entry", len(digest.get("dissent_log", [])) == 1, str(digest))
        if digest.get("dissent_log"):
            check("test4: dissent entry is verbatim from lens b",
                  digest["dissent_log"][0] == {"lens": "b", "dissent": fixtures[1]["dissent"]},
                  str(digest["dissent_log"]))
        check("test4: null_seats has exactly 1 (lens c)",
              digest.get("null_seats") == ["c"], str(digest))
        check("test4: gaps has 2 entries", len(digest.get("gaps", [])) == 2, str(digest))

        # ── Test 5: render_ledger has one row per gap ──
        ledger = render_ledger(digest)
        data_rows = [ln for ln in ledger.splitlines() if ln.startswith("|") and "---" not in ln][1:]
        check("test5: header present (lens/gap/disposition/evidence)",
              "lens" in ledger and "gap" in ledger and "disposition" in ledger and "evidence" in ledger,
              ledger.splitlines()[0] if ledger else "")
        check("test5: one row per gap (2 gaps -> 2 rows)",
              len(data_rows) == len(digest.get("gaps", [])), f"rows={data_rows}")

        # ── Test 6: digest subcommand reads --outputs <dir> of <lens>.json files ──
        outputs_dir = base / "seat_outputs"
        outputs_dir.mkdir()
        for fx in fixtures:
            (outputs_dir / f"{fx['lens']}.json").write_text(json.dumps(fx), encoding="utf-8")
        r6 = run_cli(["digest", "--outputs", str(outputs_dir)])
        try:
            digest_cli = json.loads(r6.stdout)
        except Exception as exc:
            digest_cli = {}
            check("test6: digest subcommand valid JSON", False, str(exc))
        else:
            check("test6: digest subcommand valid JSON", True)
        check("test6: digest subcommand matches direct call",
              digest_cli.get("crux") == digest.get("crux") and
              digest_cli.get("null_seats") == digest.get("null_seats") and
              len(digest_cli.get("dissent_log", [])) == len(digest.get("dissent_log", [])),
              str(digest_cli))

    print(f"{PASS} pass / {FAIL} fail")
    if FAILURES:
        for f in FAILURES:
            print(f"  FAIL: {f}")
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
