#!/usr/bin/env python3
"""
export_to_drive.py — Deterministic export of the Farrice LinkedIn Engine assets
to a Google Drive folder as CLEAN Google Docs (markdown -> Doc), via the `gws` CLI.

Why a script (not "Claude runs gws by hand"): standing rule — never ship infra that
depends on manual AI invocation. `/farrice-engine export` and the daily/weekly close call this.

What it does:
  - Find-or-creates the Drive folder by name (re-runs reuse it).
  - Exports a CURATED core set (strategy/research/voice-gate/workflows) + an AUTO GLOB of
    `daily/*.md` (so every future post + briefing lands automatically).
  - CLEANS each file before upload: strips internal provenance blockquotes, descriptor-laden
    heading parentheticals, trailing gate-note QA, and (for posts) the ```code fences``` so the
    post reads as clean body text — no system overhead in the portable Docs.
  - Updates existing Docs in place (stable links); creates new ones; trashes stale "Farrice —"
    Docs no longer in the set (no duplicates as content rotates).
  - Writes links to `_active/linkedin-launch/90-exports/drive-export-manifest.json`.
  - Auth-expiry aware: on a gws token error, prints the re-auth command and exits non-zero.

Usage:
  python3 execution/export_to_drive.py                # export (core + daily glob), cleaned
  python3 execution/export_to_drive.py --preview <relpath>   # print cleaned output, no upload
  python3 execution/export_to_drive.py --dry-run      # list what would export
  python3 execution/export_to_drive.py --folder "X"   # override folder name
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_FOLDER = "Farrice LinkedIn Engine — Content & Strategy OS"
MANIFEST_OUT = os.path.join(REPO, "_active/linkedin-launch/90-exports/drive-export-manifest.json")
DAILY_DIR = os.path.join(REPO, "_active/linkedin-launch/99-archive/2026-08-07-dupe-trees/daily-pre-0623-snapshot")
FOLDER_MIME = "application/vnd.google-apps.folder"
DOC_MIME = "application/vnd.google-apps.document"
REAUTH = "gws auth login -s drive,gmail,calendar,sheets,docs"
AUTH_HINTS = ("invalid_grant", "token", "unauthorized", "401", "credential", "expired")

# Curated, non-daily assets: (relative path, Doc name, kind). kind: doc | system | content
CORE = [
    ("_active/linkedin-launch/99-archive/2026-08-07-dead-front-doors/00-start-here-june-era/CREATIVE-BOOK.md", "Farrice — The Creative Book (Daily)", "doc"),
    ("_active/linkedin-launch/01-research/MASTER-STRATEGY.md", "Farrice — Master Strategy", "doc"),
    ("_active/linkedin-launch/content-os.md", "Farrice — Content OS", "doc"),
    ("_active/linkedin-launch/01-research/icp-emotional-map.md", "Farrice — ICP Emotional Map", "doc"),
    ("_active/linkedin-launch/01-research/wellness-supplement-brand-niche.md", "Farrice — Wellness & Supplement Brand Niche Research", "doc"),
    ("_active/linkedin-launch/02-offer/OFFER-LADDER.md", "Farrice — Offer Ladder", "doc"),
    ("_active/linkedin-launch/02-offer/teardown-system.md", "Farrice — Teardown System", "doc"),
    ("_active/linkedin-launch/05-lead-gen/pipeline.md", "Farrice — Pipeline Tracker", "doc"),
    ("_active/linkedin-launch/05-lead-gen/proof-tracker.md", "Farrice — Proof Tracker", "doc"),
    ("_active/linkedin-launch/04-deliverables/content-os/voice-gate.md", "Farrice — Voice Gate", "doc"),
    (".agent/workflows/farrice-engine.md", "Farrice Engine — Master Workflow", "system"),
    (".agent/workflows/linkedin-daily.md", "Farrice — LinkedIn Daily Workflow", "system"),
]


# ---------- markdown cleaning ----------
def clean_heading(line):
    # drop a trailing descriptor parenthetical, e.g. "(verified world-class)", "(Mon)"
    return re.sub(r"\s*\([^)]*\)\s*$", "", line).rstrip()


def clean_markdown(text, kind):
    lines = text.split("\n")
    # 1) strip leading metadata: keep the first H1 (descriptor-cleaned), drop leading
    #    blockquotes / horizontal rules / blanks before the first real content line.
    out, seen, kept_h1 = [], False, False
    for ln in lines:
        s = ln.strip()
        if not seen:
            if s.startswith("# ") and not kept_h1:
                out.append(clean_heading(ln)); kept_h1 = True; continue
            if s == "" or s.startswith(">") or s == "---":
                continue
            seen = True
            out.append(ln)
        else:
            out.append(ln)
    lines = out

    if kind == "content":
        # 2) unwrap fenced code blocks so the post is clean prose, not a monospace block
        lines = [ln for ln in lines if not ln.lstrip().startswith("```")]
        body = "\n".join(lines)
        # 3) cut a trailing internal QA section (gate notes / why-it-clears / receipts)
        body = re.split(
            r"\n\s*(?:\*\*|#+\s*)(?:Gate notes|Why it clears|Gate-passed|Receipts? &|Cost & Receipts)",
            body, maxsplit=1, flags=re.I)[0]
        lines = body.split("\n")

    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip() + "\n"


def derive_name(filename):
    stem = filename[:-3] if filename.endswith(".md") else filename
    m = re.match(r"^(\d{4}-\d{2}-\d{2})[-_]?(.*)$", stem)
    if m and m.group(2):
        return f"Farrice — {m.group(2).replace('-', ' ').replace('_', ' ').strip().title()} {m.group(1)}"
    m = re.match(r"^(.*?)[-_](\d{4}-\d{2}-\d{2})$", stem)
    if m:
        return f"Farrice — {m.group(1).replace('-', ' ').replace('_', ' ').strip().title()} {m.group(2)}"
    return f"Farrice — {stem.replace('-', ' ').replace('_', ' ').strip().title()}"


def build_asset_list():
    assets = list(CORE)
    for path in sorted(glob.glob(os.path.join(DAILY_DIR, "*.md"))):
        fn = os.path.basename(path)
        rel = os.path.relpath(path, REPO)
        kind = "doc" if ("briefing" in fn or "performance" in fn) else "content"
        assets.append((rel, derive_name(fn), kind))
    return assets


# ---------- gws ----------
def gws(args, upload=None, content_type=None, body=None):
    cmd = ["gws"] + args
    if body is not None:
        cmd += ["--json", json.dumps(body)]
    if upload:
        cmd += ["--upload", upload]
        if content_type:
            cmd += ["--upload-content-type", content_type]
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO)
    out = (res.stdout or "") + (res.stderr or "")
    a, b = out.find("{"), out.rfind("}")
    payload = out[a:b + 1] if a != -1 and b != -1 else ""
    if res.returncode != 0 or not payload:
        low = out.lower()
        if any(h in low for h in AUTH_HINTS):
            print(f"\n  ✗ gws auth expired/invalid. Re-authenticate, then re-run:\n      {REAUTH}\n", file=sys.stderr)
            sys.exit(2)
        print(f"  ✗ gws error: {out.strip()[:400]}", file=sys.stderr); sys.exit(1)
    try:
        return json.loads(payload)
    except json.JSONDecodeError:
        print(f"  ✗ unparseable gws output: {payload[:300]}", file=sys.stderr); sys.exit(1)


def find_one(query, fields="files(id,name)"):
    r = gws(["drive", "files", "list", "--params", json.dumps({"q": query, "fields": fields, "pageSize": 1})])
    return (r.get("files") or [None])[0]


def list_all(query, fields="files(id,name)"):
    r = gws(["drive", "files", "list", "--params", json.dumps({"q": query, "fields": fields, "pageSize": 100})])
    return r.get("files", [])


def find_or_create_folder(name):
    hit = find_one(f"name = '{name}' and mimeType = '{FOLDER_MIME}' and trashed = false", "files(id,name,webViewLink)")
    return hit or gws(["drive", "files", "create",
                       "--json", json.dumps({"name": name, "mimeType": FOLDER_MIME}),
                       "--params", json.dumps({"fields": "id,name,webViewLink"})])


def upsert_doc(local_path, doc_name, kind, folder_id):
    abs_path = os.path.join(REPO, local_path)
    if not os.path.exists(abs_path):
        return {"name": doc_name, "status": "missing-source", "source": local_path}
    with open(abs_path) as f:
        cleaned = clean_markdown(f.read(), kind)
    # gws only accepts uploads inside its cwd (REPO) — stage cleaned content under .tmp/
    tmp_dir = os.path.join(REPO, ".tmp", "drive-export")
    os.makedirs(tmp_dir, exist_ok=True)
    tmp_path = os.path.join(tmp_dir, re.sub(r"[^A-Za-z0-9]+", "_", doc_name) + ".md")
    with open(tmp_path, "w") as f:
        f.write(cleaned)
    rel = os.path.relpath(tmp_path, REPO)
    try:
        existing = find_one(f"name = '{doc_name}' and '{folder_id}' in parents and trashed = false")
        if existing:
            r = gws(["drive", "files", "update", "--params", json.dumps({"fileId": existing["id"], "fields": "id,name,webViewLink"})],
                    upload=rel, content_type="text/markdown"); r["status"] = "updated"
        else:
            r = gws(["drive", "files", "create",
                     "--json", json.dumps({"name": doc_name, "parents": [folder_id], "mimeType": DOC_MIME}),
                     "--params", json.dumps({"fields": "id,name,webViewLink"})],
                    upload=rel, content_type="text/markdown"); r["status"] = "created"
        return r
    finally:
        os.unlink(tmp_path)


def reconcile(folder_id, keep_names):
    """Trash 'Farrice —' Docs in the folder that are no longer in the export set."""
    trashed = []
    for f in list_all(f"'{folder_id}' in parents and trashed = false and mimeType = '{DOC_MIME}'"):
        if f["name"].startswith("Farrice") and f["name"] not in keep_names:
            gws(["drive", "files", "update", "--params", json.dumps({"fileId": f["id"], "fields": "id"})], body={"trashed": True})
            trashed.append(f["name"])
    return trashed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", default=DEFAULT_FOLDER)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--preview", metavar="RELPATH")
    args = ap.parse_args()

    if args.preview:
        p = os.path.join(REPO, args.preview)
        kind = "content" if ("daily/2026" in args.preview and "briefing" not in args.preview) else "doc"
        with open(p) as f:
            print(clean_markdown(f.read(), kind))
        return

    assets = build_asset_list()
    if args.dry_run:
        print(f"Folder: {args.folder}")
        for path, name, kind in assets:
            ok = "ok" if os.path.exists(os.path.join(REPO, path)) else "MISSING"
            print(f"  [{ok}] ({kind}) {path}  ->  {name}")
        return

    folder = find_or_create_folder(args.folder)
    fid = folder["id"]
    flink = folder.get("webViewLink", f"https://drive.google.com/drive/folders/{fid}")
    print(f"📁 {args.folder}\n   {flink}\n")

    results, keep = [], set()
    for path, name, kind in assets:
        r = upsert_doc(path, name, kind, fid)
        keep.add(name)
        results.append({"name": name, "source": path, "kind": kind,
                        **{k: r.get(k) for k in ("id", "webViewLink", "status")}})
        mark = {"created": "＋", "updated": "↻", "missing-source": "⚠"}.get(r.get("status"), "?")
        print(f"  {mark} {r.get('status','?'):14} {name}")

    trashed = reconcile(fid, keep)
    for t in trashed:
        print(f"  🗑  trashed stale     {t}")

    manifest = {"folder": {"name": args.folder, "id": fid, "link": flink}, "docs": results, "trashed": trashed}
    os.makedirs(os.path.dirname(MANIFEST_OUT), exist_ok=True)
    with open(MANIFEST_OUT, "w") as f:
        json.dump(manifest, f, indent=2)
    ok = sum(1 for r in results if r["status"] in ("created", "updated"))
    print(f"\n✓ {ok}/{len(assets)} docs exported, {len(trashed)} stale trashed. Links → {os.path.relpath(MANIFEST_OUT, REPO)}")


if __name__ == "__main__":
    main()
