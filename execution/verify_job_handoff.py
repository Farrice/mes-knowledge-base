#!/usr/bin/env python3
"""verify_job_handoff.py — sabotage-both-directions check for the manager loop.

Covers (2026-09-09, verification-spine rule — every new check fires both ways):
  1. Hook fire path: job-shaped prompts emit MODE JOB-HANDOFF (Claude and Codex
     variants) and NO intent-brief / fresh-pen card; near-misses emit nothing of
     the kind; the off switch silences it.
  2. Board: `next` says TURN MUST CONTINUE while a lane is runnable, MAY END when
     every lane is terminal or blocked; `lint` catches an illegal status; `--brief`
     is silent with no jobs; a packet answer flips open→answered.
  3. Stop observer: a transcript ending with runnable lanes and no DECISION PACKET
     logs `job-turn-ended-unblocked`; with all lanes blocked it logs nothing.
  4. Portable packet carries every open lane and packet.

Pinned expectations are hardcoded here, never read from the artifact under test.
Telemetry the hook writes is snapshotted and restored. Exit 0 pass, 1 fail.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
HOOK = REPO / "execution" / "hooks" / "steering_loop_hook.py"
BOARD = REPO / "execution" / "job_board.py"
TELEMETRY = [
    REPO / ".agent" / "steering-loop-state.json",
    REPO / ".agent" / "co-creation-state.json",
    REPO / ".agent" / "sessions" / "steering-observe.jsonl",
    REPO / ".agent" / "active-model.json",
]
PIN_MODE = "MODE JOB-HANDOFF"
PIN_BRIEF = "📋 INTENT BRIEF"
PIN_PEN = ("FRESH PEN", "PEN (Codex)")
PIN_CODEX = "single seat"
PIN_END = "MAY END"
PIN_CONTINUE = "TURN MUST CONTINUE"
PIN_EVENT = "job-turn-ended-unblocked"

JOB = ("I want you to take this whole thing and handle it end to end. Watch the video, extract the concepts "
       "into a skill, then wire it into the harness and Codex so it fires from the hook, then write the recipe "
       "cards and register everything. Cover all the gaps yourself, manage yourself, and only come back to me "
       "for decisions that need me.")
NEG_NO_VERB = ("I was thinking about the video and the concepts in it. Watch the video, extract the concepts into a "
               "skill, then wire it into the harness and Codex so it fires from the hook, then write the recipe cards "
               "and register everything and tell me what you think about the approach.")
NEG_DUMP = ("I keep thinking about how the sessions feel lately and I am not sure the shape is right, the rhythm is "
            "off and I want it to feel like a partner, kind of like a chief of staff, you know, and the harness "
            "should feel calmer than it does right now, that is where my head is at this evening and I wanted to "
            "get it down before I lose it, nothing to do with this yet, just parking the thought here for later "
            "reference so it is on disk somewhere and not in my head anymore tonight.")

PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"  ok  {name}")
    else:
        FAIL += 1
        print(f"FAIL  {name}" + (f" — {detail}" if detail else ""))


def snapshot():
    snap = {}
    for p in TELEMETRY:
        snap[p] = p.read_bytes() if p.exists() else None
    return snap


def restore(snap):
    for p, data in snap.items():
        if data is None:
            if p.exists():
                p.unlink()
        else:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)


def fire(prompt, codex=False, env_extra=None):
    env = dict(os.environ, CLAUDE_PROJECT_DIR=str(REPO))
    env.pop("ANTIGRAVITY_HARNESS", None)
    if codex:
        env["ANTIGRAVITY_HARNESS"] = "codex"
    if env_extra:
        env.update(env_extra)
    payload = {"session_id": "verify-job-handoff", "prompt": prompt, "cwd": str(REPO)}
    r = subprocess.run([sys.executable, str(HOOK), "prompt"], input=json.dumps(payload),
                       capture_output=True, text=True, env=env, cwd=str(REPO), timeout=60)
    return r.stdout


def board(args, root):
    # handoff_store.py roots itself in the repo, not ANTIGRAVITY_ROOT — skip it so a
    # temp job never leaks a handoff file into .agent/handoffs/
    env = dict(os.environ, ANTIGRAVITY_ROOT=str(root), JOB_BOARD_SKIP_HANDOFF_STORE="1")
    r = subprocess.run([sys.executable, str(BOARD)] + args, capture_output=True, text=True,
                       env=env, cwd=str(REPO), timeout=60)
    return r.returncode, r.stdout + r.stderr


def seed_job(root, slug, lanes, status="active"):
    d = root / ".agent" / "missions" / slug
    d.mkdir(parents=True, exist_ok=True)
    state = {"name": slug, "slug": slug, "goal": "verify", "status": status, "mode": "code",
             "created_at": "2026-09-09T00:00:00+00:00", "updated_at": "2026-09-09T00:00:00+00:00",
             "job": {"recipe": "source-to-skill-harvest", "opened_at": "2026-09-09", "opened_by": "claude"},
             "activation_queue": lanes, "handoffs": [], "validation_contract": []}
    (d / "mission.json").write_text(json.dumps(state, indent=2), encoding="utf-8")
    (d / "card.md").write_text("---\njob: source-to-skill-harvest\n---\n## The job\nverify\n", encoding="utf-8")
    (d / "decisions.md").write_text("# Decisions\n", encoding="utf-8")
    return d


def lane(i, status, after=None, blocker=""):
    return {"id": i, "owner": "claude", "workflow": f"lane {i}", "expected_artifact": "x",
            "status": status, "after": after or [], "blocker": blocker, "evidence_path": "",
            "next_action": "", "kind": "lane", "updated_at": ""}


def main():
    snap = snapshot()
    try:
        print("== hook fire path")
        out = fire(JOB)
        check("claude job-shaped → MODE JOB-HANDOFF", PIN_MODE in out, out[:200])
        check("claude job-shaped → no INTENT BRIEF card", PIN_BRIEF not in out)
        check("claude job-shaped → no fresh-pen card", not any(p in out for p in PIN_PEN))
        check("claude job-shaped → card names MAY END", PIN_END in out)
        out_c = fire(JOB, codex=True)
        check("codex job-shaped → MODE JOB-HANDOFF single seat", PIN_MODE in out_c and PIN_CODEX in out_c, out_c[:200])
        check("codex job-shaped → no PEN (Codex) card", "PEN (Codex)" not in out_c)
        check("near-miss (no delegation verb) → no job card", PIN_MODE not in fire(NEG_NO_VERB))
        check("reflective dump → no job card", PIN_MODE not in fire(NEG_DUMP))
        check("slash prompt → no job card", PIN_MODE not in fire("/go " + JOB))
        check("short ask → no job card", PIN_MODE not in fire("handle this end to end then finish"))
        check("approval → no job card", PIN_MODE not in fire("This matches the scope and brief, go ahead and execute it."))
        check("mode override forces it", PIN_MODE in fire("mode job-handoff — " + NEG_NO_VERB))
        check("CO_CREATION_OFF silences the card", PIN_MODE not in fire(JOB, env_extra={"CO_CREATION_OFF": "1"}))
        # Codex path proper: through the runner, which must wrap the card in the hook envelope
        runner = REPO / ".codex" / "tools" / "codex_hook_runner.py"
        if runner.exists():
            env = dict(os.environ)
            env.pop("CLAUDE_PROJECT_DIR", None)
            r = subprocess.run([sys.executable, str(runner), "steering-loop", "prompt"],
                               input=json.dumps({"session_id": "verify-job-handoff", "prompt": JOB, "cwd": str(REPO)}),
                               capture_output=True, text=True, env=env, cwd=str(REPO), timeout=60)
            try:
                data = json.loads(r.stdout or "{}")
            except Exception:
                data = {}
            ctx = str((data.get("hookSpecificOutput") or {}).get("additionalContext") or "")
            check("codex runner wraps the job card in the hook envelope",
                  (data.get("hookSpecificOutput") or {}).get("hookEventName") == "UserPromptSubmit" and PIN_MODE in ctx,
                  (r.stdout or r.stderr)[:200])
            check("codex runner emits the single-seat variant", PIN_CODEX in ctx)

        print("== board")
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rc, out = board(["--brief"], root)
            check("--brief silent with no jobs", out.strip() == "", out[:120])
            seed_job(root, "j-open", [lane("L1", "planned"), lane("L2", "planned", ["L1"])])
            rc, out = board(["next", "j-open"], root)
            check("runnable lane → TURN MUST CONTINUE", PIN_CONTINUE in out and "L1" in out, out[:160])
            check("dep-queued lane listed, not runnable", "queued behind them: L2" in out, out[:160])
            rc, out = board(["--brief"], root)
            check("--brief shows the open job", out.startswith("JOBS: 1 open") and "runnable" in out, out[:160])
            board(["lane", "j-open", "L1", "--status", "blocked", "--blocker", "needs his pick"], root)
            rc, out = board(["next", "j-open"], root)
            check("blocked lane + dep-chained lane → MAY END", out.startswith(PIN_END) and "L1" in out, out[:160])
            rc, out = board(["packet", "j-open", "add", "--lane", "L1", "--choice", "A or B",
                             "--options", "A x / B y", "--recommend", "A — cheaper"], root)
            check("packet add prints a DECISION PACKET", "DECISION PACKET" in out, out[:160])
            rc, out = board(["--brief"], root)
            check("--brief counts the waiting packet", "1 decision packet" in out, out[:160])
            rc, out = board(["packet", "j-open", "answer", "1", "go with B"], root)
            check("packet answer flips open→answered", rc == 0 and "answered" in out, out[:160])
            dec = (root / ".agent" / "missions" / "j-open" / "decisions.md").read_text()
            check("answer recorded verbatim", "go with B" in dec and "· answered ·" in dec)
            rc, out = board(["handoff", "j-open", "--to", "chat"], root)
            pm = root / ".agent" / "missions" / "j-open" / "portable.md"
            check("handoff writes portable.md", pm.exists(), out[:160])
            txt = pm.read_text() if pm.exists() else ""
            check("portable packet carries every lane", "| L1 |" in txt and "| L2 |" in txt)
            check("portable packet carries the answered decision", "go with B" in txt)
            # sabotage: illegal status must fail lint
            sp = root / ".agent" / "missions" / "j-open" / "mission.json"
            st = json.loads(sp.read_text())
            st["activation_queue"][1]["status"] = "wip"
            sp.write_text(json.dumps(st))
            rc, out = board(["lint", "j-open"], root)
            check("lint catches an illegal lane status", rc == 1 and "illegal" in out, out[:160])
            seed_job(root, "j-done", [lane("L1", "complete"), lane("L2", "skipped")])
            rc, out = board(["next", "j-done"], root)
            check("all terminal → MAY END (close it)", out.startswith(PIN_END) and "close" in out, out[:160])

            print("== stop observer")
            obs = REPO / ".agent" / "sessions" / "steering-observe.jsonl"

            def count_tmp_events():
                # count only OUR temp job's events — other open jobs in the repo store
                # (the dogfood job, for one) legitimately log their own lines
                if not obs.exists():
                    return 0
                n = 0
                for ln in obs.read_text().splitlines():
                    if PIN_EVENT in ln and '"verify-job-tmp"' in ln:
                        n += 1
                return n

            before = count_tmp_events()
            # run the Stop hook against a transcript whose last assistant text has no packet,
            # pointing the hook's job scan at the temp root via a symlinked .agent/missions? The
            # observer reads STATE_DIR.parent/missions — the REPO's. Use a temp job in the repo
            # store instead and clean it up.
            tmp_job = REPO / ".agent" / "missions" / "verify-job-tmp"
            try:
                seed_job(REPO, "verify-job-tmp", [lane("L1", "planned")])
                tp = root / "transcript.jsonl"
                tp.write_text(json.dumps({"type": "assistant", "message": {"content": [
                    {"type": "text", "text": "Worked on lane one. " * 40}]}}) + "\n")
                env = dict(os.environ, CLAUDE_PROJECT_DIR=str(REPO))
                subprocess.run([sys.executable, str(HOOK), "stop"], input=json.dumps(
                    {"session_id": "verify-job-handoff", "transcript_path": str(tp)}),
                    capture_output=True, text=True, env=env, cwd=str(REPO), timeout=60)
                after = count_tmp_events()
                check("runnable lane + no packet → job-turn-ended-unblocked logged", after == before + 1,
                      f"before={before} after={after}")
                # now block the lane: nothing new should log
                st = json.loads((tmp_job / "mission.json").read_text())
                st["activation_queue"][0]["status"] = "blocked"
                st["activation_queue"][0]["blocker"] = "his pick"
                (tmp_job / "mission.json").write_text(json.dumps(st))
                subprocess.run([sys.executable, str(HOOK), "stop"], input=json.dumps(
                    {"session_id": "verify-job-handoff", "transcript_path": str(tp)}),
                    capture_output=True, text=True, env=env, cwd=str(REPO), timeout=60)
                after2 = count_tmp_events()
                check("all lanes blocked → nothing logged", after2 == after, f"after={after} after2={after2}")
            finally:
                shutil.rmtree(tmp_job, ignore_errors=True)
    finally:
        restore(snap)
    print(f"\nverify_job_handoff: {PASS} pass, {FAIL} fail")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
