#!/usr/bin/env python3
"""export_growth_package.py — standalone + full-package export for Growth Blueprint OS.

Every artifact ships in three forms (SKILL.md Output Contracts); this script owns
form 3: PDF portability + the assembled package.

    pdf <file.html> [--out <file.pdf>]
        One HTML -> PDF via local headless Chrome ($0, no network).

    package --niche <slug> [--no-zip]
        For growth-lab/<slug>/: PDF every export HTML, assemble
        exports/package/ (HTML + PDF + lead magnet + MANIFEST.md), zip it.

Chrome renders with a virtual-time budget so load animations in the interactive
artifacts settle before print; interactivity is inherently lost in PDF — the
MANIFEST says so per file (PDF = portability form, HTML = premium form).
"""

import argparse
import datetime as dt
import json
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def html_to_pdf(src: Path, out: Path) -> bool:
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = [CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
           "--virtual-time-budget=8000", f"--print-to-pdf={out}", src.resolve().as_uri()]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    ok = out.exists() and out.stat().st_size > 1024
    if not ok:
        print(f"  FAIL {src.name}: {r.stderr.strip().splitlines()[-1] if r.stderr.strip() else 'no output'}",
              file=sys.stderr)
    return ok


def cmd_pdf(args):
    src = Path(args.html)
    out = Path(args.out) if args.out else src.with_suffix(".pdf")
    ok = html_to_pdf(src, out)
    print(json.dumps({"cmd": "pdf", "src": str(src), "out": str(out), "ok": ok}))
    return 0 if ok else 1


def cmd_package(args):
    lab = ROOT / "growth-lab" / args.niche
    exports = lab / "exports"
    if not exports.is_dir():
        print(json.dumps({"cmd": "package", "ok": False,
                          "error": f"no exports dir at {exports} — run the gb-* chain first"}))
        return 1
    pkg = exports / "package"
    if pkg.exists():
        shutil.rmtree(pkg)
    pkg.mkdir(parents=True)

    rows, failures = [], 0
    for html in sorted(exports.glob("*.html")):
        dest_html = pkg / html.name
        shutil.copy2(html, dest_html)
        pdf = pkg / (html.stem + ".pdf")
        ok = html_to_pdf(html, pdf)
        failures += 0 if ok else 1
        interactive = "-client" not in html.stem
        rows.append((html.name, pdf.name if ok else "PDF FAILED", interactive))

    # Client-facing manifest: reader language only (Reader-Purity Rule 2026-08-27 —
    # no paths, commands, or system names; operator detail goes in the notes file
    # which stays OUT of the shipped package).
    manifest = pkg / "CONTENTS.md"
    lines = [f"# What's inside — {dt.date.today().strftime('%B %d, %Y')}", "",
             "Suggested reading order: the positioning dossier first, then the whitespace map, "
             "the bullseye, the topic scan, the format playbook, and the growth blueprint last — "
             "it assembles the other five. The mini-report stands alone.", ""]
    for name, pdf_name, interactive in rows:
        tag = ("interactive — open this one in your browser for the full experience"
               if interactive else "document")
        lines.append(f"- **{name}** ({tag}) · print version: {pdf_name}")
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")

    op_notes = exports / "OPERATOR-NOTES.md"
    op_lines = [f"# Operator notes — {args.niche} package (NOT shipped)",
                f"Assembled {dt.date.today().isoformat()} from {exports.relative_to(ROOT)}"]
    src_manifest = lab / "manifest.json"
    if src_manifest.exists():
        op_lines.append(f"State ledger at assembly: `{src_manifest.relative_to(ROOT)}`")
    op_lines.append(f"PDF failures this run: {failures}")
    op_notes.write_text("\n".join(op_lines) + "\n", encoding="utf-8")

    zip_path = None
    if not args.no_zip:
        zip_path = exports / f"{args.niche}-growth-blueprint-package.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(pkg.iterdir()):
                z.write(f, arcname=f"{args.niche}-package/{f.name}")

    print(json.dumps({"cmd": "package", "niche": args.niche, "files": len(rows),
                      "pdf_failures": failures, "package_dir": str(pkg),
                      "zip": str(zip_path) if zip_path else None, "ok": failures == 0}))
    return 0 if failures == 0 else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pdf", help="one HTML -> PDF")
    p.add_argument("html")
    p.add_argument("--out")
    p.set_defaults(fn=cmd_pdf)
    p = sub.add_parser("package", help="assemble the full niche package")
    p.add_argument("--niche", required=True)
    p.add_argument("--no-zip", action="store_true")
    p.set_defaults(fn=cmd_package)
    args = ap.parse_args()
    if not Path(CHROME).exists():
        print(json.dumps({"ok": False, "error": "Google Chrome not found — PDF export needs it"}))
        return 1
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
