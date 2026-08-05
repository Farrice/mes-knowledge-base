#!/usr/bin/env python3
"""Asset index — unified manifest for every visual/media asset in the tree.

Feeds the Asset Command Center (execution/asset_gallery.py → /assets-board).
Deterministic, stdlib-only, never moves or deletes files.

Manifest: .agent/assets/manifest.jsonl — append-only JSONL, reduced by
`path` with latest-line-wins (same pattern as pulse_dashboard.open_missions).
Idempotence is structural: a sweep appends a line only for paths that are new
or whose mtime/size changed; re-sweeps append nothing. Records for files that
vanish from disk get a tombstone line (status "missing"), never deletion.

Record schema v1 (all fields optional except v/path/type/zone/ts):
  {"v":1, "path":"<repo-relative>", "type":"image|video|audio|doc", "ext":"png",
   "zone":"fantastic-posters", "project":null, "src":"fal", "model":null,
   "style":"brutalist-broadcast", "prompt":"...", "refs":[], "cost_usd":0.04,
   "ts":"2026-05-02T08:07:02Z", "mtime":1777662417, "size":812345,
   "w":1024, "h":1536, "dur_s":null, "tags":[], "keep":null, "status":"active"}

ENGINE CONTRACT (generate_media.py and any future generator): after writing an
asset, append ONE line in this schema with src/model/prompt/refs/style/cost_usd
/ts populated; mtime/size/w/h may be omitted — the next sweep fills them and
carries your metadata forward (append-only + reduce means nothing is lost).
Then call `python3 execution/asset_gallery.py --quick` so the board updates.

CLI:
  python3 execution/asset_index.py            # sweep (default)
  python3 execution/asset_index.py --status   # counts per zone
  python3 execution/asset_index.py --verify   # every active path exists
  python3 execution/asset_index.py --compact  # rewrite manifest to reduced form
"""
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, ".agent", "assets", "manifest.jsonl")

# zone name → list of repo-relative root dirs (walked recursively)
STATIC_ZONES = [
    ("fantastic-posters", ["skills/fantastic-posters/out"]),
    ("deliverables-generations", ["deliverables/generations"]),
    ("deliverables-images", ["deliverables/images"]),
    ("deliverables-designs", ["deliverables/designs"]),
    ("deliverables-carousel", ["deliverables/carousel-images"]),
    ("deliverables-video", ["deliverables/video-enhancement"]),
    ("research-briefs", ["deliverables/research-briefs"]),
]
# _active/*/05-assets and _active/*/visuals are discovered dynamically
ACTIVE_DIR_NAMES = {"05-assets", "visuals"}

TYPE_BY_EXT = {
    "png": "image", "jpg": "image", "jpeg": "image", "webp": "image", "gif": "image",
    "mp4": "video", "mov": "video", "webm": "video",
    "mp3": "audio", "wav": "audio", "m4a": "audio",
    "pdf": "doc",
}
# zone-scoped extension allowances — html is a card type ONLY where a zone opts in
# (a global html→doc mapping would sweep every stray template in every zone)
ZONE_EXTRA_EXTS = {
    "research-briefs": {"html": "doc"},
}
SKIP_BASENAMES = {".DS_Store"}


def jsonl(path):
    rows = []
    try:
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except ValueError:
                    pass
    except OSError:
        pass
    return rows


def reduced_manifest():
    latest = {}
    for r in jsonl(MANIFEST):
        p = r.get("path")
        if p:
            latest[p] = r
    return latest


def iso(epoch):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(epoch))


# ---------------------------------------------------------------- discovery

def discover_files():
    """Yield (zone, project, abs_path) for every media file in every zone."""
    for zone, roots in STATIC_ZONES:
        for rel_root in roots:
            base = os.path.join(ROOT, rel_root)
            if not os.path.isdir(base):
                continue
            for dirpath, dirnames, filenames in os.walk(base):
                dirnames[:] = [d for d in dirnames if not d.startswith(".")]
                for name in filenames:
                    if name in SKIP_BASENAMES or name.startswith("."):
                        continue
                    ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
                    if ext not in TYPE_BY_EXT and ext not in ZONE_EXTRA_EXTS.get(zone, {}):
                        continue
                    # project = first subdir under the zone root, if any
                    sub = os.path.relpath(dirpath, base)
                    project = None if sub == "." else sub.split(os.sep)[0]
                    yield zone, project, os.path.join(dirpath, name)

    active_root = os.path.join(ROOT, "_active")
    if os.path.isdir(active_root):
        for dirpath, dirnames, filenames in os.walk(active_root):
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            parts = os.path.relpath(dirpath, active_root).split(os.sep)
            if not any(p in ACTIVE_DIR_NAMES for p in parts):
                continue
            for name in filenames:
                if name in SKIP_BASENAMES or name.startswith("."):
                    continue
                ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
                if ext not in TYPE_BY_EXT:
                    continue
                # project = component right after the LAST "_active" in the path
                # (handles nested _active/codex-harvest-*/_active/<proj>/05-assets)
                full_parts = os.path.join(dirpath, name).split(os.sep)
                idxs = [i for i, p in enumerate(full_parts) if p == "_active"]
                project = full_parts[idxs[-1] + 1] if idxs and idxs[-1] + 1 < len(full_parts) else None
                yield "active-projects", project, os.path.join(dirpath, name)


# ---------------------------------------------------------------- backfill

FANTASTIC_RE = re.compile(r"^(?P<style>.+)_(?P<ms>\d{13})_v(?P<n>\d+)(?P<alpha>_alpha)?$")
DELIV_TS_RE = re.compile(r"^(?P<d>\d{8})_(?P<t>\d{6})_(?P<slug>.+)$")


def parse_filename(zone, stem, rec):
    m = FANTASTIC_RE.match(stem)
    if zone == "fantastic-posters" and m:
        rec.setdefault("style", m.group("style"))
        rec.setdefault("src", "fal")
        rec["ts"] = iso(int(m.group("ms")) / 1000.0)
        if m.group("alpha"):
            rec.setdefault("tags", []).append("alpha")
        return
    m = DELIV_TS_RE.match(stem)
    if zone in ("deliverables-images", "deliverables-designs") and m:
        try:
            rec["ts"] = iso(time.mktime(time.strptime(m.group("d") + m.group("t"), "%Y%m%d%H%M%S")))
        except ValueError:
            pass
        if not rec.get("prompt"):
            rec["prompt"] = m.group("slug").replace("_", " ")
        rec.setdefault("src", "gemini-image" if zone == "deliverables-images" else "gemini-design")


def sidecar_for(abs_path):
    """Find a metadata sidecar JSON next to an asset. Two known shapes:
    {stem}.json / {stem}_prompt.json / {stem}_with_prompt.json."""
    base, _ = os.path.splitext(abs_path)
    for cand in (base + ".json", base + "_prompt.json", base + "_with_prompt.json"):
        if os.path.isfile(cand):
            try:
                return json.load(open(cand, encoding="utf-8"))
            except (OSError, ValueError):
                return None
    return None


def apply_sidecar(abs_path, rec):
    sc = sidecar_for(abs_path)
    if not isinstance(sc, dict):
        return
    cd = sc.get("creative_direction") if isinstance(sc.get("creative_direction"), dict) else {}
    prompt = sc.get("final_prompt") or sc.get("prompt") or cd.get("prompt")
    if prompt and not rec.get("prompt"):
        rec["prompt"] = prompt
    style = sc.get("concept_name") or cd.get("concept_name") or (
        sc.get("style") if sc.get("style") not in (None, "auto") else None)
    if style and not rec.get("style"):
        rec["style"] = style
    if sc.get("total_cost_usd") is not None and rec.get("cost_usd") is None:
        rec["cost_usd"] = sc["total_cost_usd"]
    rec.setdefault("src", "gemini-design")


def fal_log_index():
    """output_path → log entry, for entries that recorded a path."""
    try:
        data = json.load(open(os.path.join(ROOT, ".agent", "fal-usage.json")))
    except (OSError, ValueError):
        return {}
    out = {}
    for e in data.get("log", []):
        p = (e.get("output_path") or "").strip()
        if p:
            out[os.path.normpath(p)] = e
    return out


def higgsfield_runs_index():
    """basename(output_url/path) → run, for runs with a recorded output."""
    try:
        data = json.load(open(os.path.join(ROOT, ".agent", "higgsfield-usage.json")))
    except (OSError, ValueError):
        return {}
    out = {}
    for r in data.get("runs", []):
        u = r.get("output_url")
        if u:
            out[os.path.basename(str(u))] = r
    return out


# ---------------------------------------------------------------- media probes

def probe_image(abs_path, rec):
    try:
        p = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", abs_path],
                           capture_output=True, text=True, timeout=15)
        for line in p.stdout.splitlines():
            line = line.strip()
            if line.startswith("pixelWidth:"):
                rec["w"] = int(line.split(":")[1])
            elif line.startswith("pixelHeight:"):
                rec["h"] = int(line.split(":")[1])
    except Exception:
        pass


def probe_video(abs_path, rec):
    try:
        p = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=width,height:format=duration", "-of", "json", abs_path],
            capture_output=True, text=True, timeout=20)
        info = json.loads(p.stdout or "{}")
        streams = info.get("streams") or [{}]
        rec["w"] = streams[0].get("width")
        rec["h"] = streams[0].get("height")
        dur = (info.get("format") or {}).get("duration")
        rec["dur_s"] = round(float(dur), 2) if dur else None
    except Exception:
        pass


# ---------------------------------------------------------------- commands

CARRY = ("prompt", "style", "refs", "cost_usd", "tags", "keep", "src", "model", "project")


def sweep(verbose=True):
    latest = reduced_manifest()
    fal_log = fal_log_index()
    hf_runs = higgsfield_runs_index()
    seen, added = set(), 0
    os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
    with open(MANIFEST, "a", encoding="utf-8") as out:
        for zone, project, abs_path in discover_files():
            rel = os.path.relpath(abs_path, ROOT)
            seen.add(rel)
            try:
                st = os.stat(abs_path)
            except OSError:
                continue
            prev = latest.get(rel)
            if prev and prev.get("mtime") == int(st.st_mtime) and prev.get("size") == st.st_size \
                    and prev.get("status") == "active":
                continue
            name = os.path.basename(abs_path)
            ext = name.rsplit(".", 1)[-1].lower()
            ftype = TYPE_BY_EXT.get(ext) or ZONE_EXTRA_EXTS.get(zone, {}).get(ext, "doc")
            rec = {"v": 1, "path": rel, "type": ftype, "ext": ext,
                   "zone": zone, "project": project, "src": None, "model": None,
                   "style": None, "prompt": None, "refs": [], "cost_usd": None,
                   "ts": None, "mtime": int(st.st_mtime), "size": st.st_size,
                   "w": None, "h": None, "dur_s": None, "tags": [], "keep": None,
                   "status": "active"}
            if prev:  # carry provenance forward across re-exports
                for k in CARRY:
                    if prev.get(k) not in (None, [], "") and rec.get(k) in (None, [], ""):
                        rec[k] = prev[k]
            stem = os.path.splitext(name)[0]
            parse_filename(zone, stem, rec)
            apply_sidecar(abs_path, rec)
            fe = fal_log.get(os.path.normpath(rel))
            if fe:
                rec["src"] = rec["src"] or "fal"
                if rec.get("cost_usd") is None:
                    rec["cost_usd"] = fe.get("actual_cost_usd") or fe.get("estimated_cost_usd")
                if not rec.get("prompt") and fe.get("brief"):
                    rec["prompt"] = fe["brief"]
                if not rec.get("style") and fe.get("style"):
                    rec["style"] = fe["style"]
            hr = hf_runs.get(name)
            if hr:
                rec["src"] = rec["src"] or "higgsfield"
                rec["model"] = rec["model"] or hr.get("operation")
            if rec["type"] == "image" and rec.get("w") is None:
                probe_image(abs_path, rec)
            elif rec["type"] == "video" and (rec.get("w") is None or rec.get("dur_s") is None):
                probe_video(abs_path, rec)
            if not rec.get("ts"):
                rec["ts"] = iso(st.st_mtime)
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            added += 1
        # tombstones
        gone = 0
        for rel, prev in latest.items():
            if rel not in seen and prev.get("status") == "active":
                t = dict(prev)
                t["status"] = "missing"
                out.write(json.dumps(t, ensure_ascii=False) + "\n")
                gone += 1
    if verbose:
        print(f"sweep: {added} added/updated, {gone} tombstoned, "
              f"{len(seen)} media files on disk → {os.path.relpath(MANIFEST, ROOT)}")
    return added


def status():
    latest = reduced_manifest()
    active = [r for r in latest.values() if r.get("status") == "active"]
    by_zone, by_type = {}, {}
    with_prompt = with_cost = 0
    for r in active:
        by_zone[r.get("zone")] = by_zone.get(r.get("zone"), 0) + 1
        by_type[r.get("type")] = by_type.get(r.get("type"), 0) + 1
        if r.get("prompt"):
            with_prompt += 1
        if r.get("cost_usd") is not None:
            with_cost += 1
    print(f"ASSET INDEX: {len(active)} active ({len(latest) - len(active)} missing)")
    for z in sorted(by_zone):
        print(f"  {z:26} {by_zone[z]}")
    print("  types: " + ", ".join(f"{k}={v}" for k, v in sorted(by_type.items())))
    print(f"  provenance: {with_prompt} with prompt, {with_cost} with cost")


def verify():
    latest = reduced_manifest()
    bad = [p for p, r in latest.items()
           if r.get("status") == "active" and not os.path.isfile(os.path.join(ROOT, p))]
    if bad:
        print(f"VERIFY FAIL: {len(bad)} active record(s) missing on disk (run a sweep to tombstone):")
        for p in bad[:20]:
            print(f"  {p}")
        return 1
    print(f"verify: clean ({len(latest)} records)")
    return 0


def compact():
    latest = reduced_manifest()
    tmp = MANIFEST + ".tmp"
    with open(tmp, "w", encoding="utf-8") as out:
        for rel in sorted(latest):
            out.write(json.dumps(latest[rel], ensure_ascii=False) + "\n")
    os.replace(tmp, MANIFEST)
    print(f"compact: {len(latest)} records")


def main():
    if "--status" in sys.argv:
        status()
    elif "--verify" in sys.argv:
        raise SystemExit(verify())
    elif "--compact" in sys.argv:
        compact()
    else:
        sweep()


if __name__ == "__main__":
    main()
