#!/usr/bin/env python3
"""B-roll sourcing — free-first stock search/fetch for the Edit Bay.

Ladder rung 2 (broll-ladder.md). Enforces free-first IN CODE: `search` greps
the asset manifest for already-owned matching clips before touching any API.
Providers: Pexels (primary — free, monetization-safe, ~200 req/hr) and
Pixabay (secondary — free, no attribution). Keys in .env:
  PEXELS_API_KEY=...   PIXABAY_API_KEY=...   (both free signups)

Every download appends a manifest line (asset_index ENGINE CONTRACT) with
`license` + `source_url` — the provenance audit trail is non-negotiable
(directives/video-studio-policy.md #3).

stdlib only. JSON to stdout. Exit: 0 ok · 1 fail · 2 missing key/input.

CLI:
  broll_source.py search --query "server room" [--provider pexels|pixabay|all]
                         [--orientation landscape|portrait] [--min-duration 5]
                         [--per-page 8] [--skip-owned]
  broll_source.py fetch  --id pexels:12345 --project SLUG [--tags a,b] [--quality hd]
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, ".agent", "assets", "manifest.jsonl")


def load_env():
    env = {}
    path = os.path.join(ROOT, ".env")
    if os.path.exists(path):
        for line in open(path):
            m = re.match(r"^([A-Z0-9_]+)=(.*)$", line.strip())
            if m:
                env[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    env.update({k: v for k, v in os.environ.items() if k.endswith("_API_KEY")})
    return env


def out_json(obj, code=0):
    print(json.dumps(obj, indent=2))
    sys.exit(code)


def fail(msg, code=1, **extra):
    out_json({"ok": False, "error": msg, **extra}, code)


def http_json(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    try:
        import certifi
        import ssl
        ctx = ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        ctx = None
    with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
        return json.loads(r.read().decode())


def owned_matches(query):
    """Grep the manifest for already-indexed video assets matching the query terms."""
    if not os.path.exists(MANIFEST):
        return []
    terms = [t.lower() for t in re.findall(r"\w+", query) if len(t) > 2]
    latest = {}
    with open(MANIFEST) as f:
        for line in f:
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if rec.get("path"):
                latest[rec["path"]] = rec
    hits = []
    for rec in latest.values():
        if rec.get("type") != "video" or rec.get("status") == "missing":
            continue
        hay = " ".join([rec.get("path", ""), rec.get("prompt") or "",
                        " ".join(rec.get("tags") or [])]).lower()
        score = sum(1 for t in terms if t in hay)
        if score:
            hits.append({"path": rec["path"], "score": score,
                         "tags": rec.get("tags"), "dur_s": rec.get("dur_s"),
                         "src": rec.get("src")})
    return sorted(hits, key=lambda h: -h["score"])[:10]


def search_pexels(env, q, orientation, per_page):
    key = env.get("PEXELS_API_KEY")
    if not key:
        return None, "PEXELS_API_KEY missing from .env (free signup: pexels.com/api)"
    url = ("https://api.pexels.com/videos/search?"
           + urllib.parse.urlencode({"query": q, "per_page": per_page,
                                     **({"orientation": orientation} if orientation else {})}))
    data = http_json(url, {"Authorization": key})
    results = []
    for v in data.get("videos", []):
        files = sorted(v.get("video_files", []),
                       key=lambda f: abs((f.get("height") or 0) - 1080))
        best = files[0] if files else {}
        results.append({"id": f"pexels:{v['id']}", "provider": "pexels",
                        "duration": v.get("duration"),
                        "w": v.get("width"), "h": v.get("height"),
                        "preview": v.get("image"),
                        "url": v.get("url"),
                        "download": best.get("link"),
                        "by": (v.get("user") or {}).get("name")})
    return results, None


def search_pixabay(env, q, orientation, per_page):
    key = env.get("PIXABAY_API_KEY")
    if not key:
        return None, "PIXABAY_API_KEY missing from .env (free signup: pixabay.com/api/docs)"
    url = ("https://pixabay.com/api/videos/?"
           + urllib.parse.urlencode({"key": key, "q": q, "per_page": per_page}))
    data = http_json(url)
    results = []
    for v in data.get("hits", []):
        vids = v.get("videos", {})
        best = vids.get("large") or vids.get("medium") or vids.get("small") or {}
        w, h = best.get("width"), best.get("height")
        if orientation == "landscape" and w and h and w < h:
            continue
        if orientation == "portrait" and w and h and w > h:
            continue
        results.append({"id": f"pixabay:{v['id']}", "provider": "pixabay",
                        "duration": v.get("duration"), "w": w, "h": h,
                        "preview": None, "url": v.get("pageURL"),
                        "download": best.get("url"), "by": v.get("user")})
    return results, None


def cmd_search(args):
    env = load_env()
    owned = [] if args.skip_owned else owned_matches(args.query)
    providers = ["pexels", "pixabay"] if args.provider == "all" else [args.provider]
    results, warnings = [], []
    for p in providers:
        fn = search_pexels if p == "pexels" else search_pixabay
        try:
            res, err = fn(env, args.query, args.orientation, args.per_page)
        except Exception as e:  # network/API failure shouldn't kill the ladder
            res, err = None, f"{p} search failed: {e}"
        if err:
            warnings.append(err)
        elif res is not None:
            results += res
    if args.min_duration:
        results = [r for r in results
                   if not r.get("duration") or r["duration"] >= args.min_duration]
    out_json({"ok": True, "query": args.query,
              "owned_first": owned,
              "owned_note": ("MANIFEST HITS ABOVE — free-first ladder says use owned "
                             "footage before fetching stock" if owned else None),
              "results": results, "warnings": warnings or None},
             0 if (results or owned or not warnings) else 2)


def cmd_fetch(args):
    env = load_env()
    m = re.match(r"^(pexels|pixabay):(\d+)$", args.id)
    if not m:
        fail("--id must be pexels:<id> or pixabay:<id>", 2)
    provider, vid = m.groups()

    if provider == "pexels":
        key = env.get("PEXELS_API_KEY")
        if not key:
            fail("PEXELS_API_KEY missing from .env", 2)
        v = http_json(f"https://api.pexels.com/videos/videos/{vid}",
                      {"Authorization": key})
        files = sorted(v.get("video_files", []),
                       key=lambda f: abs((f.get("height") or 0)
                                         - (1080 if args.quality == "hd" else 720)))
        dl = files[0].get("link") if files else None
        meta = {"license": "pexels", "source_url": v.get("url"),
                "by": (v.get("user") or {}).get("name"),
                "dur_s": v.get("duration")}
    else:
        key = env.get("PIXABAY_API_KEY")
        if not key:
            fail("PIXABAY_API_KEY missing from .env", 2)
        data = http_json("https://pixabay.com/api/videos/?"
                         + urllib.parse.urlencode({"key": key, "id": vid}))
        hits = data.get("hits", [])
        if not hits:
            fail(f"pixabay id {vid} not found")
        v = hits[0]
        vids = v.get("videos", {})
        best = vids.get("large") if args.quality == "hd" else None
        best = best or vids.get("medium") or vids.get("small") or {}
        dl = best.get("url")
        meta = {"license": "pixabay", "source_url": v.get("pageURL"),
                "by": v.get("user"), "dur_s": v.get("duration")}

    if not dl:
        fail("no downloadable file found")

    dest_dir = os.path.join(ROOT, "_active", args.project, "05-assets", "video",
                            "broll", "stock")
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, f"{provider}-{vid}.mp4")
    try:
        import certifi
        import ssl
        ctx = ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        ctx = None
    with urllib.request.urlopen(dl, timeout=120, context=ctx) as r, open(dest, "wb") as f:
        f.write(r.read())

    tags = [t.strip() for t in (args.tags or "").split(",") if t.strip()]
    rec = {"v": 1, "path": os.path.relpath(dest, ROOT), "type": "video",
           "ext": "mp4", "zone": "active-projects", "project": args.project,
           "src": provider, "prompt": None, "tags": tags or None,
           "license": meta["license"], "source_url": meta["source_url"],
           "dur_s": meta.get("dur_s"), "cost_usd": 0.0,
           "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "status": "active"}
    os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
    with open(MANIFEST, "a") as f:
        f.write(json.dumps(rec) + "\n")
    subprocess.run([sys.executable, os.path.join(ROOT, "execution", "asset_gallery.py"),
                    "--quick"], capture_output=True)
    out_json({"ok": True, "path": rec["path"], "license": meta["license"],
              "source_url": meta["source_url"], "by": meta.get("by"),
              "dur_s": meta.get("dur_s"), "cost_usd": 0.0})


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("search")
    p.add_argument("--query", required=True)
    p.add_argument("--provider", default="all", choices=["pexels", "pixabay", "all"])
    p.add_argument("--orientation", choices=["landscape", "portrait"])
    p.add_argument("--min-duration", type=float)
    p.add_argument("--per-page", type=int, default=8)
    p.add_argument("--skip-owned", action="store_true")

    p = sub.add_parser("fetch")
    p.add_argument("--id", required=True)
    p.add_argument("--project", required=True)
    p.add_argument("--tags")
    p.add_argument("--quality", default="hd", choices=["hd", "sd"])

    args = ap.parse_args()
    {"search": cmd_search, "fetch": cmd_fetch}[args.cmd](args)


if __name__ == "__main__":
    main()
