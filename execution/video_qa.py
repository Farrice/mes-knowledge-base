#!/usr/bin/env python3
"""Video QA — seam-targeted inspection + fixlist plumbing for the Edit Bay.

The "controllable inspection" layer (Bonanno pattern): extract frames exactly
where defects live — each cut ±0.2s, graphic in/out edges, caption onsets —
never uniform sampling. A picky-editor reviewer (sub-agent or Codex) reads the
frames + skills/video-studio/REVIEW.md and writes a fixlist.json; this script
validates it and logs applied fixes into the cutlist's revisions[].

stdlib + ffmpeg only. JSON to stdout. Exit: 0 ok · 1 fail · 2 bad input.

CLI:
  video_qa.py inspect          --project SLUG --render PATH [--seams] [--graphics]
                               [--captions] [--uniform N] [--window 0.2]
  video_qa.py fixlist-validate --file PATH
  video_qa.py apply-log        --project SLUG --fixlist PATH [--note TEXT]
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_ffmpeg_repo = os.path.join(ROOT, "tools", "bin", "ffmpeg")
FFMPEG = _ffmpeg_repo if os.path.exists(_ffmpeg_repo) else (shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg")

KINDS = {"seam", "caption", "graphic", "pacing", "audio", "color", "content"}
SEVERITIES = {"blocker", "nit"}
REQUIRED_FIX = {"id", "t", "kind", "severity", "observed", "expected", "action"}


def out_json(obj, code=0):
    print(json.dumps(obj, indent=2))
    sys.exit(code)


def fail(msg, code=1, **extra):
    out_json({"ok": False, "error": msg, **extra}, code)


def video_dir(project):
    return os.path.join(ROOT, "_active", project, "05-assets", "video")


def load_cutlist(project):
    path = os.path.join(video_dir(project), "cutlist.json")
    if not os.path.exists(path):
        return None, path
    with open(path) as f:
        return json.load(f), path


def parse_srt_onsets(srt_path, limit=None):
    onsets = []
    if not srt_path or not os.path.exists(srt_path):
        return onsets
    with open(srt_path) as f:
        for m in re.finditer(r"(\d{2}):(\d{2}):(\d{2}),(\d{3}) -->", f.read()):
            h, mi, s, ms = map(int, m.groups())
            onsets.append(h * 3600 + mi * 60 + s + ms / 1000.0)
    return onsets[:limit] if limit else onsets


def grab_frame(render, t, out_path):
    r = subprocess.run([FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
                        "-ss", str(max(t, 0)), "-i", render, "-frames:v", "1",
                        "-q:v", "3", out_path], capture_output=True)
    return r.returncode == 0 and os.path.exists(out_path)


def cmd_inspect(args):
    render = args.render if os.path.isabs(args.render) else os.path.join(ROOT, args.render)
    if not os.path.exists(render):
        # try project-relative
        cand = os.path.join(video_dir(args.project), args.render)
        if os.path.exists(cand):
            render = cand
        else:
            fail(f"render missing: {args.render}", 2)

    stem = os.path.splitext(os.path.basename(render))[0]
    frames_dir = os.path.join(os.path.dirname(render), f"{stem}-frames")
    os.makedirs(frames_dir, exist_ok=True)

    cl, _ = load_cutlist(args.project)
    targets = []  # (t, shot_id, why)
    w = args.window

    everything = not (args.seams or args.graphics or args.captions or args.uniform)

    if cl and (args.seams or everything):
        # cut boundaries in RENDER time = cumulative shot durations
        elapsed = 0.0
        shots = [s for s in cl.get("shots", []) if s.get("enabled", True)]
        for i, shot in enumerate(shots):
            dur = None
            if shot.get("in") is not None and shot.get("out") is not None:
                dur = float(shot["out"]) - float(shot["in"])
            elif shot.get("dur"):
                dur = float(shot["dur"])
            if dur is None:
                continue
            elapsed += dur
            if i < len(shots) - 1:
                nxt = shots[i + 1]
                targets += [(elapsed - w, shot.get("id"), f"pre-cut into {nxt.get('id')}"),
                            (elapsed + w, nxt.get("id"), f"post-cut from {shot.get('id')}")]

    if cl and (args.graphics or everything):
        elapsed = 0.0
        for shot in [s for s in cl.get("shots", []) if s.get("enabled", True)]:
            dur = None
            if shot.get("in") is not None and shot.get("out") is not None:
                dur = float(shot["out"]) - float(shot["in"])
            elif shot.get("dur"):
                dur = float(shot["dur"])
            if dur is None:
                continue
            if shot.get("role") == "graphic":
                targets += [(elapsed + min(w, dur / 4), shot.get("id"), "graphic-in edge"),
                            (elapsed + dur / 2, shot.get("id"), "graphic mid"),
                            (elapsed + dur - min(w, dur / 4), shot.get("id"), "graphic-out edge")]
            elapsed += dur

    if args.captions or everything:
        srt = None
        if cl and cl.get("captions", {}).get("srt"):
            srt = os.path.join(video_dir(args.project), cl["captions"]["srt"]) \
                if not os.path.isabs(cl["captions"]["srt"]) else cl["captions"]["srt"]
            if not os.path.exists(srt):
                srt = None
        if not srt:
            auto = os.path.join(video_dir(args.project), "captions", "auto.srt")
            srt = auto if os.path.exists(auto) else None
        for t in parse_srt_onsets(srt, limit=40):
            targets.append((t + 0.05, None, "caption onset"))

    if args.uniform:
        # duration probe
        r = subprocess.run([FFMPEG, "-hide_banner", "-i", render, "-f", "null", "-"],
                           capture_output=True, text=True)
        m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
        if m:
            dur = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
            step = dur / (args.uniform + 1)
            targets += [(step * (i + 1), None, "uniform sample")
                        for i in range(args.uniform)]

    if not targets:
        fail("no inspection targets — no cutlist found and no --uniform fallback given", 2)

    targets = sorted({(round(max(t, 0), 3), sid, why) for t, sid, why in targets})
    inspection = []
    for i, (t, sid, why) in enumerate(targets, 1):
        fp = os.path.join(frames_dir, f"insp_{i:03d}.jpg")
        if grab_frame(render, t, fp):
            inspection.append({"frame": os.path.relpath(fp, ROOT), "t": t,
                               "shot": sid, "why": why})

    meta = {"v": 1, "render": os.path.relpath(render, ROOT),
            "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "frames": inspection}
    with open(os.path.join(frames_dir, "inspection.json"), "w") as f:
        json.dump(meta, f, indent=1)
    out_json({"ok": True, "frames_dir": os.path.relpath(frames_dir, ROOT),
              "count": len(inspection),
              "inspection": os.path.relpath(os.path.join(frames_dir, "inspection.json"), ROOT)})


def cmd_fixlist_validate(args):
    if not os.path.exists(args.file):
        fail(f"no such file: {args.file}", 2)
    try:
        with open(args.file) as f:
            fx = json.load(f)
    except json.JSONDecodeError as e:
        fail(f"not valid JSON: {e}", 1)
    errors = []
    if fx.get("v") != 1:
        errors.append("v must be 1")
    for k in ("render", "reviewer", "verdict"):
        if not fx.get(k):
            errors.append(f"missing {k}")
    if fx.get("verdict") not in ("pass", "revise"):
        errors.append("verdict must be pass|revise")
    fixes = fx.get("fixes")
    if not isinstance(fixes, list):
        errors.append("fixes must be a list")
        fixes = []
    downgraded = []
    for i, f_ in enumerate(fixes):
        missing = REQUIRED_FIX - set(f_)
        if missing:
            errors.append(f"fix[{i}] missing {sorted(missing)}")
        if f_.get("kind") not in KINDS:
            errors.append(f"fix[{i}] bad kind: {f_.get('kind')}")
        if f_.get("severity") not in SEVERITIES:
            errors.append(f"fix[{i}] bad severity: {f_.get('severity')}")
        if f_.get("severity") == "blocker" and not f_.get("style_rule"):
            downgraded.append(f_.get("id", f"fix[{i}]"))
    if fx.get("verdict") == "revise" and not any(
            f_.get("severity") == "blocker" and f_.get("style_rule") for f_ in fixes):
        errors.append("verdict=revise but no citable blockers (blockers need style_rule)")
    if errors:
        fail("fixlist invalid", 1, errors=errors)
    out_json({"ok": True, "fixes": len(fixes),
              "blockers": sum(1 for f_ in fixes
                              if f_.get("severity") == "blocker" and f_.get("style_rule")),
              "downgrade_to_nit": downgraded,
              "note": "blockers without style_rule are nits (REVIEW.md contract)"})


def cmd_apply_log(args):
    cl, cl_path = load_cutlist(args.project)
    if not cl:
        fail(f"cutlist not found for project {args.project}", 2)
    if not os.path.exists(args.fixlist):
        fail(f"no such fixlist: {args.fixlist}", 2)
    with open(args.fixlist) as f:
        fx = json.load(f)
    cl.setdefault("revisions", []).append({
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "by": fx.get("reviewer", "qa-loop"),
        "render": fx.get("render"),
        "fixes": [f_.get("id") for f_ in fx.get("fixes", [])],
        "note": args.note or f"applied fixlist {os.path.basename(args.fixlist)}"})
    with open(cl_path, "w") as f:
        json.dump(cl, f, indent=1)
    farrice_fixes = [f_ for f_ in fx.get("fixes", [])
                     if fx.get("reviewer") == "farrice"]
    out_json({"ok": True, "revisions": len(cl["revisions"]),
              "promote_to_style_file": bool(farrice_fixes),
              "reminder": ("PROMOTE these into _active/farrice-brand/voice/video-style.md "
                           "Correction Log before close-out" if farrice_fixes else None)})


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("inspect")
    p.add_argument("--project", required=True)
    p.add_argument("--render", required=True)
    p.add_argument("--seams", action="store_true")
    p.add_argument("--graphics", action="store_true")
    p.add_argument("--captions", action="store_true")
    p.add_argument("--uniform", type=int)
    p.add_argument("--window", type=float, default=0.2)

    p = sub.add_parser("fixlist-validate")
    p.add_argument("--file", required=True)

    p = sub.add_parser("apply-log")
    p.add_argument("--project", required=True)
    p.add_argument("--fixlist", required=True)
    p.add_argument("--note")

    args = ap.parse_args()
    {"inspect": cmd_inspect, "fixlist-validate": cmd_fixlist_validate,
     "apply-log": cmd_apply_log}[args.cmd](args)


if __name__ == "__main__":
    main()
