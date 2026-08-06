#!/usr/bin/env python3
"""Edit Bay — deterministic video assembly for the video-studio skill.

The ffmpeg execution layer of the in-house studio (skills/video-studio/):
agents decide WHAT (cutlist.json); this script executes HOW. stdlib + ffmpeg
/ffprobe only. Every subcommand prints one JSON object to stdout.
Exit codes: 0 ok · 1 failure · 2 precondition missing (bad input/missing file).

Strategy: normalize-then-concat. Each shot is trimmed AND re-encoded to the
preset's exact fps/size/pixfmt/audio spec as an intermediate, then joined via
the concat demuxer. Mixed-source concat bugs die here, at the cost of
intermediate re-encodes. xfade transitions are applied pairwise afterwards.

Source pattern: Brad Bonanno's agentic edit pipeline (extraction:
extractions/brad-bonanno-edit-bay/). Policy: directives/video-studio-policy.md.
Schema: skills/video-studio/schemas/cutlist.schema.json.

CLI:
  edit_bay.py probe         --in FILE
  edit_bay.py cutlist-apply --project SLUG [--cutlist PATH] [--preset yt-169]
                            [--out PATH] [--dry-run] [--keep-temp]
  edit_bay.py overlay       --in BASE --overlay FILE --at SEC [--end SEC]
                            [--pos PRESET|x,y] --out PATH
  edit_bay.py captions-burn --in FILE --srt FILE [--style yt-default] --out PATH
  edit_bay.py audio-mix     --in FILE [--music FILE] [--music-gain DB]
                            [--duck DB] [--sfx t=SEC:FILE ...] [--lufs -14]
                            --out PATH
  edit_bay.py transcode     --in FILE --preset NAME [--out-dir DIR]
  edit_bay.py qa-probe      --project SLUG --render PATH [--cutlist PATH]
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ffmpeg resolution: the repo's static full build FIRST (tools/bin/ffmpeg — has
# libass/subtitles + drawtext, which the Homebrew formula on this machine lacks),
# then PATH, then Homebrew. ffprobe comes from Homebrew (probing needs no libass).
_ffmpeg_repo = os.path.join(ROOT, "tools", "bin", "ffmpeg")
FFMPEG = _ffmpeg_repo if os.path.exists(_ffmpeg_repo) else (
    shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg")
FFPROBE = shutil.which("ffprobe") or "/opt/homebrew/bin/ffprobe"
CAPTION_STYLES = os.path.join(ROOT, "skills", "video-studio", "caption-styles.json")

PRESETS = {
    # name: (width, height, fps, vbitrate-ish crf, notes)
    "yt-169":   {"w": 1920, "h": 1080, "fps": 30, "crf": 18, "lufs": -14.0},
    "vert-916": {"w": 1080, "h": 1920, "fps": 30, "crf": 18, "lufs": -14.0},
    # linkedin: silent-autoplay-safe — captions must be burned (policy), -14 LUFS
    "linkedin": {"w": 1920, "h": 1080, "fps": 30, "crf": 18, "lufs": -14.0},
}
AUDIO_SPEC = ["-ar", "48000", "-ac", "2", "-c:a", "aac", "-b:a", "192k"]


def out_json(obj, code=0):
    print(json.dumps(obj, indent=2))
    sys.exit(code)


def fail(msg, code=1, **extra):
    out_json({"ok": False, "error": msg, **extra}, code)


def run(cmd, timeout=1800):
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def ffprobe_json(path):
    rc, so, se = run([FFPROBE, "-v", "quiet", "-print_format", "json",
                      "-show_format", "-show_streams", path])
    if rc != 0:
        return None
    return json.loads(so or "{}")


def probe_summary(path):
    info = ffprobe_json(path)
    if not info:
        return None
    v = next((s for s in info.get("streams", []) if s.get("codec_type") == "video"), {})
    a = next((s for s in info.get("streams", []) if s.get("codec_type") == "audio"), {})
    fr = v.get("avg_frame_rate", "0/1")
    try:
        num, den = fr.split("/")
        fps = round(float(num) / float(den), 3) if float(den) else None
    except (ValueError, ZeroDivisionError):
        fps = None
    return {
        "path": path,
        "duration": round(float(info.get("format", {}).get("duration", 0) or 0), 3),
        "w": v.get("width"), "h": v.get("height"), "fps": fps,
        "vcodec": v.get("codec_name"), "pix_fmt": v.get("pix_fmt"),
        "acodec": a.get("codec_name") or None,
        "sample_rate": int(a["sample_rate"]) if a.get("sample_rate") else None,
        "size": int(info.get("format", {}).get("size", 0) or 0),
    }


def video_dir(project):
    return os.path.join(ROOT, "_active", project, "05-assets", "video")


def load_cutlist(project, cutlist_path=None):
    path = cutlist_path or os.path.join(video_dir(project), "cutlist.json")
    if not os.path.exists(path):
        fail(f"cutlist not found: {path}", 2)
    with open(path) as f:
        cl = json.load(f)
    if cl.get("v") != 1 or "shots" not in cl:
        fail(f"cutlist schema invalid (need v:1 + shots[]): {path}", 2)
    return cl, path


def resolve_src(project, src):
    """Cutlist srcs are project-relative (05-assets/video/...) or repo-relative or absolute."""
    if os.path.isabs(src):
        return src
    for base in (video_dir(project), os.path.join(ROOT, "_active", project, "05-assets"), ROOT):
        cand = os.path.join(base, src)
        if os.path.exists(cand):
            return cand
    return os.path.join(video_dir(project), src)  # best guess for error message


def manifest_append(path, project, kind, extra=None):
    """ENGINE CONTRACT append (asset_index.py) + quick board refresh."""
    rel = os.path.relpath(path, ROOT)
    rec = {"v": 1, "path": rel, "type": kind, "ext": os.path.splitext(path)[1].lstrip("."),
           "zone": "active-projects", "project": project, "src": "edit-bay",
           "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "status": "active"}
    if extra:
        rec.update(extra)
    manifest = os.path.join(ROOT, ".agent", "assets", "manifest.jsonl")
    os.makedirs(os.path.dirname(manifest), exist_ok=True)
    with open(manifest, "a") as f:
        f.write(json.dumps(rec) + "\n")
    subprocess.run([sys.executable, os.path.join(ROOT, "execution", "asset_gallery.py"),
                    "--quick"], capture_output=True)


# ---------------------------------------------------------------- subcommands

def cmd_probe(args):
    if not os.path.exists(args.infile):
        fail(f"no such file: {args.infile}", 2)
    s = probe_summary(args.infile)
    if not s:
        fail(f"ffprobe could not read: {args.infile}")
    out_json({"ok": True, **s})


def normalize_shot(shot, src, preset, tmpdir, idx):
    """Trim + re-encode one shot to preset spec. Returns intermediate path."""
    p = PRESETS[preset]
    inter = os.path.join(tmpdir, f"shot_{idx:03d}.mp4")
    vf = (f"scale={p['w']}:{p['h']}:force_original_aspect_ratio=decrease,"
          f"pad={p['w']}:{p['h']}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={p['fps']}")
    cmd = [FFMPEG, "-y", "-hide_banner", "-loglevel", "error"]
    t_in = shot.get("in")
    t_out = shot.get("out")
    if t_in is not None:
        cmd += ["-ss", str(t_in)]
    if t_out is not None and t_in is not None:
        cmd += ["-to", str(t_out)]
    elif shot.get("dur"):
        cmd += ["-t", str(shot["dur"])]
    cmd += ["-i", src]
    audio = shot.get("audio", {})
    gain = audio.get("gain_db", 0)
    has_audio = bool(probe_summary(src) and probe_summary(src).get("acodec"))
    if audio.get("keep", True) and has_audio:
        af = f"volume={gain}dB," if gain else ""
        cmd += ["-vf", vf, "-af", f"{af}aresample=48000", *AUDIO_SPEC]
    else:
        # synthesize silence so concat inputs are uniform
        cmd += ["-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
                "-shortest", "-map", "0:v:0", "-map", "1:a:0", "-vf", vf, *AUDIO_SPEC]
    cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", str(p["crf"]),
            "-pix_fmt", "yuv420p", inter]
    rc, _, se = run(cmd)
    if rc != 0:
        raise RuntimeError(f"shot {shot.get('id', idx)} normalize failed: {se[-400:]}")
    return inter


def cmd_cutlist_apply(args):
    cl, cl_path = load_cutlist(args.project, args.cutlist)
    preset = args.preset or cl.get("preset", "yt-169")
    if preset not in PRESETS:
        fail(f"unknown preset {preset}; options: {list(PRESETS)}", 2)
    shots = [s for s in cl["shots"] if s.get("enabled", True)]
    if not shots:
        fail("cutlist has no enabled shots", 2)

    # resolve sources up front — a graphic shot points at its pre-rendered file
    plan = []
    for i, shot in enumerate(shots):
        src = shot.get("render") or shot.get("src")
        if not src:
            fail(f"shot {shot.get('id', i)} has neither src nor render", 2)
        rsrc = resolve_src(args.project, src)
        if not os.path.exists(rsrc):
            fail(f"shot {shot.get('id', i)} source missing: {rsrc}", 2)
        plan.append((shot, rsrc))

    renders = os.path.join(video_dir(args.project), "renders")
    os.makedirs(renders, exist_ok=True)
    if args.out:
        out = args.out if os.path.isabs(args.out) else os.path.join(ROOT, args.out)
    else:
        existing = [f for f in os.listdir(renders) if re.match(r"v\d+\.mp4$", f)]
        nxt = max([int(f[1:-4]) for f in existing], default=0) + 1
        out = os.path.join(renders, f"v{nxt:02d}.mp4")

    if args.dry_run:
        out_json({"ok": True, "dry_run": True, "preset": preset, "out": out,
                  "shots": [{"id": s.get("id"), "src": os.path.relpath(p, ROOT),
                             "in": s.get("in"), "out": s.get("out"),
                             "transition": s.get("transition", {"type": "cut"})}
                            for s, p in plan]})

    tmpdir = tempfile.mkdtemp(prefix="editbay_")
    try:
        inters = []
        for i, (shot, src) in enumerate(plan):
            inters.append((shot, normalize_shot(shot, src, preset, tmpdir, i)))

        # pairwise xfade where requested, else concat demuxer
        xfades = [s.get("transition", {}) for s, _ in inters[1:]]
        if any(t.get("type") == "xfade" for t in xfades):
            current = inters[0][1]
            elapsed = probe_summary(current)["duration"]
            for i in range(1, len(inters)):
                shot, nxt_path = inters[i]
                tr = shot.get("transition", {"type": "cut"})
                merged = os.path.join(tmpdir, f"merge_{i:03d}.mp4")
                if tr.get("type") == "xfade":
                    d = float(tr.get("dur", 0.25))
                    off = max(elapsed - d, 0)
                    p = PRESETS[preset]
                    rc, _, se = run([FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
                                     "-i", current, "-i", nxt_path, "-filter_complex",
                                     f"[0:v][1:v]xfade=transition=fade:duration={d}:offset={off}[v];"
                                     f"[0:a][1:a]acrossfade=d={d}[a]",
                                     "-map", "[v]", "-map", "[a]",
                                     "-c:v", "libx264", "-preset", "medium",
                                     "-crf", str(p["crf"]), "-pix_fmt", "yuv420p",
                                     *AUDIO_SPEC, merged])
                    if rc != 0:
                        raise RuntimeError(f"xfade into shot {shot.get('id')} failed: {se[-400:]}")
                else:
                    lst = os.path.join(tmpdir, f"pair_{i}.txt")
                    with open(lst, "w") as f:
                        f.write(f"file '{current}'\nfile '{nxt_path}'\n")
                    rc, _, se = run([FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
                                     "-f", "concat", "-safe", "0", "-i", lst,
                                     "-c", "copy", merged])
                    if rc != 0:
                        raise RuntimeError(f"concat at shot {shot.get('id')} failed: {se[-400:]}")
                current = merged
                elapsed = probe_summary(current)["duration"]
            shutil.copy(current, out)
        else:
            lst = os.path.join(tmpdir, "concat.txt")
            with open(lst, "w") as f:
                for _, inter in inters:
                    f.write(f"file '{inter}'\n")
            rc, _, se = run([FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
                             "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", out])
            if rc != 0:
                raise RuntimeError(f"final concat failed: {se[-400:]}")
    except RuntimeError as e:
        fail(str(e))
    finally:
        if not args.keep_temp:
            shutil.rmtree(tmpdir, ignore_errors=True)

    summary = probe_summary(out)
    manifest_append(out, args.project, "video",
                    {"tags": ["render"], "model": None,
                     "prompt": f"cutlist-apply {os.path.relpath(cl_path, ROOT)}",
                     "dur_s": summary["duration"]})
    out_json({"ok": True, "out": os.path.relpath(out, ROOT), "preset": preset,
              "shots": len(plan), "duration": summary["duration"],
              "w": summary["w"], "h": summary["h"]})


def cmd_overlay(args):
    for f in (args.infile, args.overlay):
        if not os.path.exists(f):
            fail(f"no such file: {f}", 2)
    pos_presets = {
        "lower-third": "x=W*0.05:y=H*0.72",
        "center": "x=(W-w)/2:y=(H-h)/2",
        "top-right": "x=W-w-W*0.04:y=H*0.06",
        "bottom-center": "x=(W-w)/2:y=H-h-H*0.06",
    }
    pos = pos_presets.get(args.pos)
    if not pos:
        m = re.match(r"^(-?\d+),(-?\d+)$", args.pos or "")
        pos = f"x={m.group(1)}:y={m.group(2)}" if m else pos_presets["lower-third"]
    enable = f"between(t,{args.at},{args.end})" if args.end else f"gte(t,{args.at})"
    # -itsoffset shifts overlay stream start to --at so animated overlays play from their first frame
    cmd = [FFMPEG, "-y", "-hide_banner", "-loglevel", "error", "-i", args.infile,
           "-itsoffset", str(args.at), "-i", args.overlay, "-filter_complex",
           f"[0:v][1:v]overlay={pos}:enable='{enable}':eof_action=pass[v]",
           "-map", "[v]", "-map", "0:a?", "-c:v", "libx264", "-preset", "medium",
           "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "copy", args.out]
    rc, _, se = run(cmd)
    if rc != 0:
        fail(f"overlay failed: {se[-400:]}")
    out_json({"ok": True, "out": args.out, "at": args.at, "end": args.end, "pos": args.pos})


def load_caption_style(name):
    styles = {}
    if os.path.exists(CAPTION_STYLES):
        with open(CAPTION_STYLES) as f:
            styles = json.load(f).get("styles", {})
    default = ("FontName=Arial,FontSize=13,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
               "BorderStyle=1,Outline=1.4,Shadow=0,Alignment=2,MarginV=42")
    return styles.get(name, {}).get("force_style", default)


def cmd_captions_burn(args):
    for f in (args.infile, args.srt):
        if not os.path.exists(f):
            fail(f"no such file: {f}", 2)
    style = load_caption_style(args.style)
    # ffmpeg's subtitles filter parses its filename arg specially — spaces in the
    # repo path ("Google Antigravity") break it. Stage the SRT at a safe temp path.
    tmp = tempfile.NamedTemporaryFile(suffix=".srt", delete=False)
    tmp.close()
    shutil.copy(args.srt, tmp.name)
    try:
        cmd = [FFMPEG, "-y", "-hide_banner", "-loglevel", "error", "-i", args.infile,
               "-vf", f"subtitles='{tmp.name}':force_style='{style}'",
               "-c:v", "libx264", "-preset", "medium", "-crf", "18",
               "-pix_fmt", "yuv420p", "-c:a", "copy", args.out]
        rc, _, se = run(cmd)
    finally:
        os.unlink(tmp.name)
    if rc != 0:
        fail(f"captions-burn failed: {se[-400:]}")
    out_json({"ok": True, "out": args.out, "style": args.style})


def measure_lufs(path):
    rc, _, se = run([FFMPEG, "-hide_banner", "-i", path, "-af",
                     "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json",
                     "-f", "null", "-"])
    m = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", se, re.S)
    return json.loads(m.group(0)) if m else None


def cmd_audio_mix(args):
    if not os.path.exists(args.infile):
        fail(f"no such file: {args.infile}", 2)
    inputs = ["-i", args.infile]
    filters = []
    amix_labels = ["[0:a]"]
    idx = 1
    if args.music:
        if not os.path.exists(args.music):
            fail(f"music file missing: {args.music}", 2)
        inputs += ["-stream_loop", "-1", "-i", args.music]
        if args.duck:
            # sidechain: VO ducks the music bed
            filters.append(f"[{idx}:a]volume={args.music_gain}dB[m]")
            filters.append(f"[m][0:a]sidechaincompress=threshold=0.03:ratio=8:attack=80:release=400[mduck]")
            amix_labels.append("[mduck]")
        else:
            filters.append(f"[{idx}:a]volume={args.music_gain}dB[m]")
            amix_labels.append("[m]")
        idx += 1
    sfx_entries = []
    for spec in args.sfx or []:
        m = re.match(r"^t=([\d.]+):(.+)$", spec)
        if not m:
            fail(f"bad --sfx spec (want t=SEC:FILE): {spec}", 2)
        t, f = float(m.group(1)), m.group(2)
        if not os.path.exists(f):
            fail(f"sfx file missing: {f}", 2)
        inputs += ["-i", f]
        filters.append(f"[{idx}:a]adelay={int(t*1000)}|{int(t*1000)}[sfx{idx}]")
        amix_labels.append(f"[sfx{idx}]")
        sfx_entries.append({"t": t, "file": f})
        idx += 1
    n = len(amix_labels)
    if n > 1:
        filters.append(f"{''.join(amix_labels)}amix=inputs={n}:duration=first:normalize=0[mix]")
        alabel = "[mix]"
    else:
        alabel = "[0:a]"
    filters.append(f"{alabel}loudnorm=I={args.lufs}:TP=-1.5:LRA=11[aout]")
    cmd = [FFMPEG, "-y", "-hide_banner", "-loglevel", "error", *inputs,
           "-filter_complex", ";".join(filters), "-map", "0:v", "-map", "[aout]",
           "-c:v", "copy", *AUDIO_SPEC, args.out]
    rc, _, se = run(cmd)
    if rc != 0:
        fail(f"audio-mix failed: {se[-400:]}")
    out_json({"ok": True, "out": args.out, "music": args.music,
              "ducking": bool(args.duck), "sfx": sfx_entries, "target_lufs": args.lufs})


def cmd_transcode(args):
    if not os.path.exists(args.infile):
        fail(f"no such file: {args.infile}", 2)
    if args.preset not in PRESETS:
        fail(f"unknown preset {args.preset}; options: {list(PRESETS)}", 2)
    p = PRESETS[args.preset]
    out_dir = args.out_dir or os.path.join(os.path.dirname(os.path.dirname(args.infile)), "exports")
    os.makedirs(out_dir, exist_ok=True)
    stem = os.path.splitext(os.path.basename(args.infile))[0]
    out = os.path.join(out_dir, f"{stem}-{args.preset}.mp4")
    src = probe_summary(args.infile)
    if args.preset == "vert-916" and src["w"] > src["h"]:
        # v1 honest limitation: center-crop 16:9 → 9:16 (subject-aware reframe is Phase 4)
        vf = f"crop=ih*9/16:ih,scale={p['w']}:{p['h']},setsar=1,fps={p['fps']}"
    else:
        vf = (f"scale={p['w']}:{p['h']}:force_original_aspect_ratio=decrease,"
              f"pad={p['w']}:{p['h']}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={p['fps']}")
    cmd = [FFMPEG, "-y", "-hide_banner", "-loglevel", "error", "-i", args.infile,
           "-vf", vf, "-c:v", "libx264", "-preset", "medium", "-crf", str(p["crf"]),
           "-pix_fmt", "yuv420p", "-movflags", "+faststart", *AUDIO_SPEC, out]
    rc, _, se = run(cmd)
    if rc != 0:
        fail(f"transcode failed: {se[-400:]}")
    out_json({"ok": True, "out": os.path.relpath(out, ROOT) if out.startswith(ROOT) else out,
              "preset": args.preset})


def cmd_qa_probe(args):
    render = args.render if os.path.isabs(args.render) else os.path.join(ROOT, args.render)
    if not os.path.exists(render):
        fail(f"render missing: {render}", 2)
    s = probe_summary(render)
    report = {"ok": True, "render": os.path.relpath(render, ROOT), "probe": s, "checks": {}}

    cl_path = args.cutlist or os.path.join(video_dir(args.project), "cutlist.json")
    if os.path.exists(cl_path):
        with open(cl_path) as f:
            cl = json.load(f)
        preset = cl.get("preset", "yt-169")
        p = PRESETS.get(preset, PRESETS["yt-169"])
        report["checks"]["resolution"] = {"pass": (s["w"], s["h"]) == (p["w"], p["h"]),
                                          "expect": f"{p['w']}x{p['h']}", "got": f"{s['w']}x{s['h']}"}
        report["checks"]["fps"] = {"pass": abs((s["fps"] or 0) - p["fps"]) < 0.6,
                                   "expect": p["fps"], "got": s["fps"]}
        expected = 0.0
        for shot in cl.get("shots", []):
            if not shot.get("enabled", True):
                continue
            if shot.get("in") is not None and shot.get("out") is not None:
                expected += float(shot["out"]) - float(shot["in"])
            elif shot.get("dur"):
                expected += float(shot["dur"])
        if expected:
            drift = abs(s["duration"] - expected)
            report["checks"]["duration_vs_cutlist"] = {
                "pass": drift < max(1.0, expected * 0.03),
                "expect_s": round(expected, 2), "got_s": s["duration"],
                "drift_s": round(drift, 2)}

    lufs = measure_lufs(render)
    if lufs:
        got = float(lufs.get("input_i", 0))
        report["checks"]["loudness"] = {"pass": -16.5 <= got <= -11.5,
                                        "expect": "-14 LUFS ±2.5", "got_lufs": got}

    rc, _, se = run([FFMPEG, "-hide_banner", "-i", render, "-vf",
                     "blackdetect=d=0.4:pix_th=0.10", "-an", "-f", "null", "-"])
    blacks = re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", se)
    report["checks"]["black_frames"] = {"pass": len(blacks) == 0,
                                        "segments": [{"start": float(a), "end": float(b)}
                                                     for a, b in blacks]}
    rc, _, se = run([FFMPEG, "-hide_banner", "-i", render, "-af",
                     "silencedetect=noise=-45dB:d=1.5", "-vn", "-f", "null", "-"])
    silences = re.findall(r"silence_start: ([\d.]+)", se)
    report["checks"]["long_silences"] = {"pass": len(silences) == 0,
                                         "starts": [float(x) for x in silences]}
    report["pass"] = all(c.get("pass", True) for c in report["checks"].values())
    out_json(report, 0 if report["pass"] else 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("probe")
    p.add_argument("--in", dest="infile", required=True)

    p = sub.add_parser("cutlist-apply")
    p.add_argument("--project", required=True)
    p.add_argument("--cutlist")
    p.add_argument("--preset", choices=list(PRESETS))
    p.add_argument("--out")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--keep-temp", action="store_true")

    p = sub.add_parser("overlay")
    p.add_argument("--in", dest="infile", required=True)
    p.add_argument("--overlay", required=True)
    p.add_argument("--at", type=float, required=True)
    p.add_argument("--end", type=float)
    p.add_argument("--pos", default="lower-third")
    p.add_argument("--out", required=True)

    p = sub.add_parser("captions-burn")
    p.add_argument("--in", dest="infile", required=True)
    p.add_argument("--srt", required=True)
    p.add_argument("--style", default="yt-default")
    p.add_argument("--out", required=True)

    p = sub.add_parser("audio-mix")
    p.add_argument("--in", dest="infile", required=True)
    p.add_argument("--music")
    p.add_argument("--music-gain", type=float, default=-18.0)
    p.add_argument("--duck", type=float, default=None,
                   help="enable VO→music sidechain ducking (value kept for tuning)")
    p.add_argument("--sfx", action="append")
    p.add_argument("--lufs", type=float, default=-14.0)
    p.add_argument("--out", required=True)

    p = sub.add_parser("transcode")
    p.add_argument("--in", dest="infile", required=True)
    p.add_argument("--preset", required=True)
    p.add_argument("--out-dir", dest="out_dir")

    p = sub.add_parser("qa-probe")
    p.add_argument("--project", required=True)
    p.add_argument("--render", required=True)
    p.add_argument("--cutlist")

    args = ap.parse_args()
    {"probe": cmd_probe, "cutlist-apply": cmd_cutlist_apply, "overlay": cmd_overlay,
     "captions-burn": cmd_captions_burn, "audio-mix": cmd_audio_mix,
     "transcode": cmd_transcode, "qa-probe": cmd_qa_probe}[args.cmd](args)


if __name__ == "__main__":
    main()
