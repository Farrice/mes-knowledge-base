#!/usr/bin/env python3
"""Real-photography bank for First Home Valley v2.

Source: Openverse (keyless). Filter: CC0 + Public Domain Mark ONLY — no
attribution obligation, commercial use cleared, safe to put on a client's
Instagram. No generated images. Every download writes a provenance row.

  fetch_bank.py pull                    # every role
  fetch_bank.py pull --role doorway-keys
"""
import argparse, json, pathlib, re, ssl, sys, urllib.parse, urllib.request

HERE = pathlib.Path(__file__).parent
RAW = HERE / "raw"
PROV = HERE / "provenance.jsonl"
API = "https://api.openverse.org/v1/images/"
UA = {"User-Agent": "antigravity-jen-imagery/1.0"}

# role -> (queries, what it is for in the design)
ROLES = {
    "doorway-keys":   (["house keys hand", "new home keys", "front door key"], "R5 cover - the handoff moment"),
    "renter-window":  (["woman looking out apartment window", "person window apartment", "apartment window light"], "R1 cover - 40 and renting"),
    "interior-warm":  (["modern home interior", "living room natural light", "sunlit living room"], "A1 hook - warm ground"),
    "table-math":     (["calculator paperwork desk", "documents coffee table", "signing papers desk"], "R2/R4 - the honest math"),
    "two-people":     (["couple home together", "two friends kitchen", "family kitchen morning"], "R3 - co-buying"),
    "moving-boxes":   (["moving boxes new home", "cardboard boxes apartment", "unpacking boxes"], "R5 alt - moving in"),
    "valley-street":  (["suburban street california", "residential street palm trees", "california bungalow street"], "A2 old map - place"),
    "la-landscape":   (["los angeles hills view", "san fernando valley", "california suburb aerial"], "A6 CTA - the Valley"),
    "porch-exterior": (["small house exterior", "bungalow front porch", "single family home exterior"], "texture - entry homes"),
    "paper-sheet":    (["paper document desk", "notebook pen desk", "printed sheet table"], "M1 magnet promo"),
}


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


def search(q, n=8):
    qs = urllib.parse.urlencode({
        "q": q, "license": "cc0,pdm", "page_size": n, "mature": "false",
    })
    try:
        return http(API + "?" + qs).get("results", [])
    except Exception as e:
        print("    ! search failed (%s): %s" % (q, e), file=sys.stderr)
        return []


def download(url, dest):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90, context=_ctx()) as r:
        dest.write_bytes(r.read())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["pull"])
    ap.add_argument("--role")
    ap.add_argument("--per-query", type=int, default=6)
    ap.add_argument("--min-px", type=int, default=1400)
    a = ap.parse_args()

    RAW.mkdir(parents=True, exist_ok=True)
    seen = set()
    if PROV.exists():
        seen = {json.loads(l)["id"] for l in PROV.open() if l.strip()}

    roles = {a.role: ROLES[a.role]} if a.role else ROLES
    total = 0
    with PROV.open("a") as prov:
        for role, (queries, purpose) in roles.items():
            print("\n[%s] %s" % (role, purpose))
            (RAW / role).mkdir(exist_ok=True)
            got = 0
            for q in queries:
                if got >= a.per_query:
                    break
                for r in search(q, a.per_query * 2):
                    rid = r.get("id")
                    if not rid or rid in seen:
                        continue
                    w, h = r.get("width") or 0, r.get("height") or 0
                    if max(w, h) < a.min_px:
                        continue
                    lic = (r.get("license") or "").lower()
                    if lic not in ("cc0", "pdm"):
                        continue
                    url = r.get("url")
                    if not url:
                        continue
                    ext = re.sub(r"[^a-z]", "", (r.get("filetype") or "jpg").lower()) or "jpg"
                    if ext == "jpeg":
                        ext = "jpg"
                    name = "%s-%02d-%s.%s" % (role, got, rid[:8], ext)
                    dest = RAW / role / name
                    try:
                        download(url, dest)
                    except Exception as e:
                        print("    ! dl %s: %s" % (rid[:8], e), file=sys.stderr)
                        continue
                    seen.add(rid)
                    prov.write(json.dumps({
                        "id": rid, "role": role, "purpose": purpose, "query": q,
                        "file": str(dest.relative_to(HERE)), "license": lic,
                        "provider": r.get("provider"), "title": r.get("title"),
                        "creator": r.get("creator"),
                        "source_url": r.get("foreign_landing_url"), "direct_url": url,
                        "w": w, "h": h,
                    }) + "\n")
                    prov.flush()
                    got += 1
                    total += 1
                    print("    + %s  %sx%s  %s  %s" % (name, w, h, lic, r.get("provider")))
                    if got >= a.per_query:
                        break
    print("\n%d images -> %s\nprovenance -> %s" % (total, RAW, PROV))


if __name__ == "__main__":
    main()
