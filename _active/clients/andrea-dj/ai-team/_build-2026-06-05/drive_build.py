#!/usr/bin/env python3
"""Build the clean Resonance Claude-Projects Drive structure from the local rooms/ build.
Archives the old AI Team folder contents, creates 6 clean self-contained project folders
(knowledge .md uploaded as markdown + one '★ SETUP' Google Doc each), + a top-level START HERE.
Requires a valid gws auth token. Idempotent-ish: re-running re-archives + rebuilds (creates new folders)."""
import subprocess, json, os, sys, tempfile

PARENT = "1ID5WYi7WJHhicUD_BCntAcnXHinrhead"  # Resonance — AI Team (Claude Projects)
BUILD = os.path.dirname(os.path.abspath(__file__))
ROOMS = os.path.join(BUILD, "rooms")
HTML_TMP = os.path.join(BUILD, "_html")
os.makedirs(HTML_TMP, exist_ok=True)

GDOC = "application/vnd.google-apps.document"
FOLDER = "application/vnd.google-apps.folder"
MD_CT = "text/markdown"

def gws(*args):
    r = subprocess.run(["gws", *args], capture_output=True, text=True)
    out = r.stdout.strip()
    # strip keyring banner line if present
    if out.startswith("Using keyring"):
        out = out.split("\n", 1)[1] if "\n" in out else ""
    try:
        return json.loads(out)
    except Exception:
        return {"_raw": r.stdout, "_err": r.stderr, "_code": r.returncode}

def die(msg, obj=None):
    print("FATAL:", msg)
    if obj: print(json.dumps(obj, indent=2)[:800])
    sys.exit(1)

def create_folder(name, parent):
    r = gws("drive", "files", "create", "--json",
            json.dumps({"name": name, "mimeType": FOLDER, "parents": [parent]}),
            "--format", "json")
    if "id" not in r: die(f"create_folder {name}", r)
    return r["id"]

def upload_md(path, parent):
    name = os.path.basename(path)
    r = gws("drive", "files", "create", "--upload", path,
            "--upload-content-type", MD_CT,
            "--json", json.dumps({"name": name, "parents": [parent]}),
            "--format", "json")
    if "id" not in r: die(f"upload_md {name}", r)
    return r["id"]

def md_to_html(md_path):
    import markdown
    md = open(md_path, encoding="utf-8").read()
    body = markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists"])
    html = '<html><head><meta charset="utf-8"></head><body style="font-family:Georgia,serif;">' + body + '</body></html>'
    hp = os.path.join(HTML_TMP, os.path.basename(md_path) + ".html")
    open(hp, "w", encoding="utf-8").write(html)
    return hp

def upload_gdoc(md_path, name, parent):
    hp = md_to_html(md_path)
    r = gws("drive", "files", "create", "--upload", hp,
            "--upload-content-type", "text/html",
            "--json", json.dumps({"name": name, "mimeType": GDOC, "parents": [parent]}),
            "--format", "json")
    if "id" not in r: die(f"upload_gdoc {name}", r)
    return r["id"]

def main():
    # 0. sanity: auth works
    me = gws("drive", "files", "list", "--params",
             json.dumps({"q": f'"{PARENT}" in parents and trashed=false', "pageSize": 100,
                         "fields": "files(id,name,mimeType)"}), "--format", "json")
    if "files" not in me:
        die("auth/list failed — re-auth gws", me)
    existing = me["files"]
    print(f"AI Team folder currently has {len(existing)} items.")

    # 1. Archive old contents
    archive_id = create_folder("_archive (old setup)", PARENT)
    print(f"Created _archive (old setup): {archive_id}")
    for f in existing:
        gws("drive", "files", "update", "--params",
            json.dumps({"fileId": f["id"], "addParents": archive_id, "removeParents": PARENT}),
            "--format", "json")
        print(f"  archived: {f['name']}")

    # 2. Build 6 clean room folders
    room_dirs = sorted([d for d in os.listdir(ROOMS) if os.path.isdir(os.path.join(ROOMS, d))])
    built = []
    for rd in room_dirs:
        folder = os.path.join(ROOMS, rd)
        fid = create_folder(rd, PARENT)
        print(f"\n[{rd}] folder {fid}")
        files = sorted(os.listdir(folder))
        setup = next((f for f in files if f.startswith("★ SETUP")), None)
        n_md = 0
        for f in files:
            if f == setup:
                continue
            upload_md(os.path.join(folder, f), fid)
            n_md += 1
        # project name = part after "— "
        proj = rd.split("—", 1)[1].strip() if "—" in rd else rd
        setup_id = upload_gdoc(os.path.join(folder, setup), f"★ SETUP — {proj}", fid)
        print(f"  uploaded {n_md} .md + SETUP gdoc")
        built.append((rd, fid, n_md))

    # 3. START HERE at top level
    sh = next((f for f in os.listdir(ROOMS) if f.startswith("★ START HERE")), None)
    if sh:
        sh_id = upload_gdoc(os.path.join(ROOMS, sh), "★ START HERE — How to Set Up Your Team", PARENT)
        print(f"\nSTART HERE gdoc: {sh_id}")

    # 4. Summary
    link = gws("drive", "files", "get", "--params",
               json.dumps({"fileId": PARENT, "fields": "webViewLink"}), "--format", "json")
    print("\n=== BUILD COMPLETE ===")
    for rd, fid, n in built:
        print(f"  {rd}: {n} md + SETUP")
    print("Folder:", link.get("webViewLink", "(link n/a)"))

if __name__ == "__main__":
    main()
