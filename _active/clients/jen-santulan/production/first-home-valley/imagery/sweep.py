#!/usr/bin/env python3
"""Wide Openverse sweep — real photography only, CC0 / public-domain only.

Batch one had a ~14% hit rate on narrow queries. This casts wide across the
angles the pool actually rewards (California architecture, archival street,
light and hands) so the pool gets judged on its best, not on my first guess.

  sweep.py            # run every query
  sweep.py --dry      # show counts per query, download nothing
"""
import argparse, json, pathlib, re, ssl, sys, urllib.parse, urllib.request

HERE = pathlib.Path(__file__).parent
OUT = HERE / "raw" / "_sweep"
PROV = HERE / "provenance.jsonl"
API = "https://api.openverse.org/v1/images/"
UA = {"User-Agent": "antigravity-jen-imagery/1.0"}

QUERIES = [
    # place — the angle that actually landed in batch one
    "california architecture", "palm trees street", "los angeles street",
    "california sunset houses", "suburban neighborhood aerial", "stucco house",
    "mid century modern house", "apartment building dusk", "california bungalow",
    "spanish revival house", "palm tree sunset city", "suburban houses row",
    # archival — for the 1981 "old map" beat
    "vintage suburban street", "1950s neighborhood", "historic los angeles",
    "vintage house photograph", "archival street scene",
    # entry / threshold
    "front door house", "house key lock", "keys on table", "door handle brass",
    "mailbox suburban", "front porch chairs", "house number address",
    # interiors with actual light
    "empty living room sunlight", "sunlight through window floor",
    "morning light interior", "window light curtain", "balcony plants apartment",
    # human, unposed
    "hands holding paper", "person writing notebook", "woman coffee window morning",
    "man looking out window", "two people walking street", "hands on table talking",
    # objects / texture
    "blueprint drawing", "contract signing pen", "calculator numbers",
    "moving box cardboard", "apartment keys keychain",
]


def _ctx():
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return None


def http(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40, context=_ctx()) as r:
        return json.loads(r.read().decode())


def search(q, n):
    qs = urllib.parse.urlencode({"q": q, "license": "cc0,pdm", "page_size": n, "mature": "false"})
    try:
        return http(API + "?" + qs)
    except Exception as e:
        print("  ! %s: %s" % (q, e), file=sys.stderr)
        return {"results": [], "result_count": 0}


def download(url, dest):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90, context=_ctx()) as r:
        dest.write_bytes(r.read())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--per-query", type=int, default=4)
    ap.add_argument("--min-px", type=int, default=1600)
    a = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    seen = set()
    if PROV.exists():
        seen = {json.loads(l)["id"] for l in PROV.open() if l.strip()}

    total = 0
    prov = None if a.dry else PROV.open("a")
    for q in QUERIES:
        d = search(q, a.per_query * 3)
        results = d.get("results", [])
        if a.dry:
            print("%-34s %5s results" % (q, d.get("result_count")))
            continue
        slug = re.sub(r"[^a-z0-9]+", "-", q.lower()).strip("-")
        got = 0
        for r in results:
            rid = r.get("id")
            if not rid or rid in seen:
                continue
            w, h = r.get("width") or 0, r.get("height") or 0
            if max(w, h) < a.min_px:
                continue
            if (r.get("license") or "").lower() not in ("cc0", "pdm"):
                continue
            url = r.get("url")
            if not url:
                continue
            ext = re.sub(r"[^a-z]", "", (r.get("filetype") or "jpg").lower()) or "jpg"
            ext = "jpg" if ext == "jpeg" else ext
            dest = OUT / ("%s-%02d-%s.%s" % (slug, got, rid[:8], ext))
            try:
                download(url, dest)
            except Exception as e:
                print("  ! dl %s: %s" % (rid[:8], e), file=sys.stderr)
                continue
            seen.add(rid)
            prov.write(json.dumps({
                "id": rid, "role": "_sweep", "purpose": "wide sweep", "query": q,
                "file": str(dest.relative_to(HERE)),
                "license": (r.get("license") or "").lower(),
                "provider": r.get("provider"), "title": r.get("title"),
                "creator": r.get("creator"),
                "source_url": r.get("foreign_landing_url"), "direct_url": url,
                "w": w, "h": h,
            }) + "\n")
            prov.flush()
            got += 1
            total += 1
            if got >= a.per_query:
                break
        print("%-34s +%d" % (q, got))
    if prov:
        prov.close()
    print("\n%d new images -> %s" % (total, OUT))


if __name__ == "__main__":
    main()
