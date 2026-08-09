#!/usr/bin/env python3
"""Build a self-contained Briefing Room bundle for use outside this repo.

Private exports preserve the human brief, Markdown mirror, provenance JSON,
portable context pack, and safely copyable local evidence. Share exports use
render_brief's existing outward-safe renderer and contain HTML only.

Examples:
    python3 execution/brief_export.py jordan-crawford-gtm-intelligence-os \
      --output /path/to/jordan-briefs --zip

    python3 execution/brief_export.py angle-map-god-agent-gtm-decision \
      --audience share --output /path/to/client-review

    python3 execution/brief_export.py client-working-brief \
      --brief-root /path/to/curated-brief-root --output /path/to/private-room
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parent.parent
BRIEFS = ROOT / "deliverables" / "research-briefs"
VERIFY_SOURCE = ROOT / "execution" / "verify_brief_export.py"
SCHEMA_VERSION = "portable-briefing-room/v1"
DEFAULT_MAX_FILE_MB = 25
DEFAULT_MAX_TOTAL_MB = 100

BRAND_CONTRACT = {
    "schema_version": "farrice-cain-premium-minimal/report-portable-v1",
    "name": "Farrice Cain Premium Minimal",
    "mode": "master-brand · report dialect",
    "masthead": "FARRICE CAIN",
    "mood": ["restrained", "contemporary", "decisive"],
    "color": {
        "canvas": "#F3F3F0", "paper": "#FAFAF8", "ink": "#101010",
        "graphite": "#555553", "line": "#D8D8D3", "stone": "#8C8C82",
        "white": "#FFFFFF", "report_steel": "#3D5A94",
    },
    "typography": {
        "primary": "Helvetica Neue",
        "weights": [400, 500, 700],
        "display_tracking": "-0.025em",
        "functional_label_tracking": "+0.16em",
        "report_exception": "One Source Serif 4 italic accent per display or section heading",
    },
    "layout": {
        "columns": 12, "minimum_open_space_fraction": "1/3",
        "maximum_hierarchy_levels": 3, "dominant_ideas_per_surface": 1,
    },
    "prohibited": [
        "gradients", "shadows", "black-and-gold luxury theater",
        "ornamental icons", "decorative route colors", "unearned logos",
    ],
    "source_provenance": [
        "_active/farrice-brand/premium-minimal/package/02-DESIGN-CONTRACT.md",
        "_active/farrice-brand/premium-minimal/REPORT-DIALECT.md",
        "templates/research-brief/template.html",
    ],
}

DENIED_NAMES = {
    ".env", ".netrc", ".htpasswd", "credentials", "credentials.json",
    "id_rsa", "id_ed25519",
}
DENIED_SUFFIXES = (".pem", ".key", ".p12", ".pfx", ".keystore")
HARD_DENIED_DIRS = {".git"}


def fail(message: str) -> "None":
    raise SystemExit(f"[brief_export] ERROR — {message}")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def canonical_repo_root() -> Path:
    dotgit = ROOT / ".git"
    if dotgit.is_dir():
        return ROOT
    if dotgit.is_file():
        try:
            marker = dotgit.read_text(encoding="utf-8").strip()
            if marker.startswith("gitdir:"):
                gitdir = Path(marker.split(":", 1)[1].strip()).resolve()
                for parent in gitdir.parents:
                    if parent.name == ".git":
                        return parent.parent
        except OSError:
            pass
    return ROOT


CANONICAL_ROOT = canonical_repo_root()


def source_commit() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def list_slugs(brief_root: Path = BRIEFS) -> list[str]:
    slugs = []
    if not brief_root.exists():
        return slugs
    for directory in sorted(brief_root.iterdir()):
        if directory.is_dir() and (directory / f"{directory.name}-brief.json").exists():
            slugs.append(directory.name)
    return slugs


def validate_slug(slug: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", slug or ""):
        fail(f"invalid brief slug: {slug!r}")
    return slug


def brief_files(slug: str, brief_root: Path = BRIEFS, audience: str = "private") -> dict[str, Path | None]:
    slug = validate_slug(slug)
    directory = (brief_root / slug).resolve()
    if not _inside(directory, brief_root.resolve()) or not directory.is_dir():
        fail(f"brief not found: {slug}")
    paths: dict[str, Path | None] = {
        "dir": directory,
        "html": directory / f"{slug}-brief.html",
        "md": directory / f"{slug}-brief.md",
        "json": directory / f"{slug}-brief.json",
        "context": directory / f"{slug}-context.json",
    }
    required = ("json",) if audience == "share" else ("html", "md", "json")
    for key in required:
        path = paths[key]
        if not path or not path.is_file():
            fail(f"{slug} is missing required {key} artifact")
    if paths["context"] and not paths["context"].is_file():
        paths["context"] = None
    return paths


def safe_dependency_reason(rel: str, include_hidden: bool) -> str | None:
    parts = PurePosixPath(rel).parts
    if not parts or any(part in ("", ".", "..") for part in parts):
        return "unsafe repository-relative path"
    for part in parts:
        low = part.lower()
        if part in HARD_DENIED_DIRS:
            return "Git internals are never exportable"
        if low in DENIED_NAMES or low.startswith(".env"):
            return "credential-shaped file is never exportable"
        if low.endswith(DENIED_SUFFIXES):
            return "key material is never exportable"
        if part.startswith(".") and not include_hidden:
            return "hidden path requires --include-hidden"
    return None


def resolve_dependency(item: dict, include_hidden: bool) -> tuple[Path | None, str | None, str | None]:
    raw = str(item.get("path") or item.get("abs") or "").strip()
    if not raw:
        return None, None, "empty context path"
    if raw.startswith("file://"):
        raw = urllib.parse.unquote(raw[len("file://"):])

    candidate = Path(raw)
    roots = tuple(dict.fromkeys((ROOT.resolve(), CANONICAL_ROOT.resolve())))
    rel: str | None = None
    source: Path | None = None

    if candidate.is_absolute():
        resolved = candidate.resolve()
        for base in roots:
            if _inside(resolved, base):
                rel = resolved.relative_to(base).as_posix()
                source = resolved
                break
        if rel is None:
            return None, None, "absolute path is outside the repository"
    else:
        rel = PurePosixPath(raw).as_posix()
        if safe_dependency_reason(rel, include_hidden):
            return None, rel, safe_dependency_reason(rel, include_hidden)
        for base in roots:
            resolved = (base / rel).resolve()
            if _inside(resolved, base) and resolved.is_file():
                source = resolved
                break

    reason = safe_dependency_reason(rel, include_hidden) if rel else "unresolvable path"
    if reason:
        return None, rel, reason
    if source is None or not source.is_file():
        return None, rel, "referenced file is missing"
    resolved = source.resolve()
    if not any(_inside(resolved, base) for base in roots):
        return None, rel, "symlink resolves outside the repository"
    return resolved, rel, None


def load_context_pack(meta: dict, paths: dict[str, Path | None]) -> tuple[dict, Path | None]:
    context_path = paths.get("context")
    if context_path:
        try:
            return json.loads(context_path.read_text(encoding="utf-8")), context_path
        except (OSError, ValueError) as exc:
            fail(f"{meta.get('slug')} context pack is unreadable: {exc}")
    try:
        import render_brief
        return render_brief.build_context_pack(meta), None
    except Exception as exc:
        fail(f"could not derive context pack for {meta.get('slug')}: {exc}")


def sanitize_source_roots(text: str) -> str:
    for base in dict.fromkeys((ROOT.resolve(), CANONICAL_ROOT.resolve())):
        uri = base.as_uri()
        text = text.replace(uri + "/", "source-repo://")
        text = text.replace(uri, "source-repo://")
        text = text.replace(str(base) + os.sep, "source-repo://")
        text = text.replace(str(base), "source-repo://")
    # Older authored ledgers sometimes use file://repo/relative/path as a
    # provenance label rather than a valid absolute URI. Preserve the identity
    # without leaving a misleading local-file scheme in the portable copy.
    return re.sub(r"file://(?=[A-Za-z0-9_.-]+/)", "source-repo://", text)


def _relative_url(target_rel: str, page_dir_rel: str) -> str:
    raw = posixpath.relpath(target_rel, start=page_dir_rel)
    return urllib.parse.quote(raw, safe="/._-")


def rewrite_private_html(
    source_html: str,
    slug: str,
    portable_md: str,
    original_pack: dict,
    portable_pack: dict,
    dependency_map: dict[str, Path],
) -> str:
    page_dir = f"briefs/{slug}"
    text = source_html

    artifact_names = {
        f"deliverables/research-briefs/{slug}/{slug}-brief.html": f"{slug}-brief.html",
        f"deliverables/research-briefs/{slug}/{slug}-brief.md": f"{slug}-brief.md",
        f"deliverables/research-briefs/{slug}/{slug}-context.json": f"{slug}-context.json",
        f"deliverables/research-briefs/{slug}/{slug}-brief.json": f"{slug}-brief.json",
    }
    roots = tuple(dict.fromkeys((ROOT.resolve(), CANONICAL_ROOT.resolve())))
    for source_rel, target in artifact_names.items():
        for base in roots:
            source = base / source_rel
            text = text.replace(source.as_uri(), target)
            text = text.replace(str(source), target)

    for source_rel, destination in dependency_map.items():
        target_rel = destination.as_posix()
        href = _relative_url(target_rel, page_dir)
        raw_rel = posixpath.relpath(target_rel, start=page_dir)
        for base in roots:
            source = base / source_rel
            text = text.replace(source.as_uri(), href)
            text = text.replace(str(source), raw_rel)
        text = text.replace(f"file://{source_rel}", href)

    old_pack = html.escape(json.dumps(original_pack, indent=2, ensure_ascii=False), quote=True)
    new_pack = html.escape(json.dumps(portable_pack, indent=2, ensure_ascii=False), quote=True)
    if old_pack in text:
        text = text.replace(old_pack, new_pack, 1)

    pagepack = {
        "path": f"{slug}-brief.md",
        "brief": (
            f"SOURCE: {slug}-brief.md  (portable research brief)\n"
            f"HTML: {slug}-brief.html\nCONTEXT PACK: {slug}-context.json\n\n"
            + portable_md
        ),
    }
    pagepack_json = json.dumps(pagepack, ensure_ascii=False).replace("</", "<\\/")
    text = re.sub(
        r'<script id="pagepack" type="application/json">.*?</script>',
        f'<script id="pagepack" type="application/json">{pagepack_json}</script>',
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = re.sub(r'var REPO_ROOT = ".*?";', 'var REPO_ROOT = "";', text, count=1)
    text = text.replace(
        "For repo-scoped files, <strong>path</strong> is canonical and resolves from the active Antigravity root; <strong>abs</strong> is only a render-time hint.",
        "In this portable copy, <strong>path</strong> resolves from the bundle root; <strong>source_repo_path</strong> preserves provenance.",
    )
    text = apply_portable_brand_chrome(text, "PRIVATE WORKING COPY")
    return sanitize_source_roots(text)


def apply_portable_brand_chrome(document: str, edition: str) -> str:
    """Add portable identity without introducing a competing visual system."""
    css = '''<style id="portable-brand-chrome">
.portable-brandbar{border-bottom:1px solid #D8D8D3;background:#F3F3F0;color:#101010;padding:10px max(20px,4vw);display:flex;justify-content:space-between;gap:18px;align-items:center;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:9px;font-weight:700;letter-spacing:.16em;line-height:1.3;text-transform:uppercase}
.portable-brandbar .edition{color:#8C8C82;font-weight:500}@media(max-width:560px){.portable-brandbar{align-items:flex-start;flex-direction:column;gap:4px}}
</style>'''
    bar = (
        '<div class="portable-brandbar"><span>FARRICE CAIN</span>'
        f'<span class="edition">PORTABLE BRIEF · {html.escape(edition)}</span></div>'
    )
    document = document.replace("</head>", css + "</head>", 1)
    document = document.replace("<body>", "<body>" + bar, 1)
    return re.sub(
        r'<footer class="brief">.*?</footer>',
        '<footer class="brief"><span>FARRICE CAIN</span><span>PORTABLE BRIEFING ROOM</span></footer>',
        document,
        count=1,
        flags=re.DOTALL,
    )


def render_share_html(meta: dict) -> str:
    try:
        import render_brief
        output = render_brief.render(meta, share=True)
    except Exception as exc:
        fail(f"share render failed for {meta.get('slug')}: {exc}")
    return sanitize_share_html(apply_portable_brand_chrome(output, "CLIENT EDITION"))


def sanitize_share_html(document: str) -> str:
    """Remove internal implementation commentary and reject local provenance."""
    document = sanitize_source_roots(document)
    document = re.sub(r"<!--.*?-->", "", document, flags=re.DOTALL)
    document = re.sub(r"/\*.*?\*/", "", document, flags=re.DOTALL)
    # Client briefs are static reading surfaces. Removing the template runtime
    # eliminates repository link-rewrite code and nonessential copy controls.
    document = re.sub(r"<script\b[^>]*>.*?</script>", "", document,
                      flags=re.DOTALL | re.IGNORECASE)
    document = re.sub(r'<button\b[^>]*class="[^"]*copybtn[^"]*"[^>]*>.*?</button>', "", document,
                      flags=re.DOTALL | re.IGNORECASE)
    document = re.sub(
        r"<tr>.*?(?:source-repo://|file://).*?</tr>", "", document,
        flags=re.DOTALL | re.IGNORECASE,
    )
    forbidden = ("source-repo://", "file://", str(ROOT), str(CANONICAL_ROOT))
    leaked = [token for token in forbidden if token and token in document]
    if leaked:
        fail(f"share HTML retained local provenance token(s): {', '.join(leaked)}")
    return document


def client_brand_contract() -> dict:
    """Return the client-visible brand law without repository provenance."""
    return {key: value for key, value in BRAND_CONTRACT.items() if key != "source_provenance"}


def accent_text(value: str, fallback_last: bool = False) -> str:
    """Render one report-dialect serif accent without trusting authored HTML."""
    raw = str(value or "").strip()
    match = re.search(r"\*([^*]+)\*", raw)
    if match:
        before = html.escape(raw[:match.start()].replace("*", ""))
        marked = html.escape(match.group(1))
        after = html.escape(raw[match.end():].replace("*", ""))
        return f"{before}<em>{marked}</em>{after}"
    clean = re.sub(r"\*", "", raw)
    if fallback_last and " " in clean:
        before, last = clean.rsplit(" ", 1)
        return f"{html.escape(before)} <em>{html.escape(last)}</em>"
    return html.escape(clean)


def build_index(title: str, audience: str, briefs: list[dict]) -> str:
    rows = []
    for index, brief in enumerate(briefs, 1):
        slug = brief["slug"]
        meta = brief["meta"]
        title_text = re.sub(r"\*", "", str(meta.get("title") or slug))
        chip = str(meta.get("chip") or "RESEARCH BRIEF")
        dek = str(meta.get("dek") or "")
        links = [f'<a href="briefs/{slug}/{slug}-brief.html">open brief</a>']
        if audience == "private":
            links.extend([
                f'<a href="briefs/{slug}/{slug}-brief.md">markdown</a>',
                f'<a href="briefs/{slug}/{slug}-context.json">context</a>',
            ])
        rows.append(
            f'<article class="brief-row" data-search="{html.escape((title_text + " " + chip + " " + dek).lower())}">'
            f'<span class="field">{index:02d}</span><div class="brief-copy">'
            f'<span class="chip">{html.escape(chip)}</span>'
            f'<h2>{accent_text(str(meta.get("title") or slug))}</h2><p>{html.escape(dek)}</p></div>'
            f'<div class="links">{"".join(links)}</div></article>'
        )
    private = audience == "private"
    mode_value = "Private working library" if private else "Client edition"
    context_value = "Included · agent-ready" if private else "Curated · presentation ready"
    note = (
        "Private internal export. It may contain candid strategy and source documents; use a client edition for outward sharing."
        if private else
        "A focused collection of source-grounded GTM methods and decisions, with proof boundaries kept visible."
    )
    edition_label = "PRIVATE" if private else "CLIENT EDITION"
    tool_links = (
        '<a href="README.md">Read me</a><a href="manifest.json">Manifest</a>'
        '<a href="brand-contract.json">Brand contract</a>'
        if private else '<a href="README.md">About this room</a>'
    )
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><style>
:root{{--canvas:#F3F3F0;--paper:#FAFAF8;--ink:#101010;--graphite:#555553;--line:#D8D8D3;--stone:#8C8C82;--white:#FFFFFF;--steel:#3D5A94;--sans:'Helvetica Neue',Helvetica,Arial,sans-serif;--serif:'Source Serif 4',Georgia,'Times New Roman',serif;--mono:'JetBrains Mono','SF Mono',Menlo,monospace}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth;max-width:100%}}body{{margin:0;max-width:100%;overflow-x:hidden;background:var(--canvas);color:var(--ink);font-family:var(--sans);-webkit-font-smoothing:antialiased}}
.shell{{width:calc(100% - 48px);max-width:1120px;margin:0 auto}}.masthead{{display:flex;justify-content:space-between;gap:20px;padding:18px 0 12px;border-bottom:2px solid var(--ink);font:700 9px/1.35 var(--sans);letter-spacing:.16em;text-transform:uppercase}}
.masthead .mode{{color:var(--stone);font-weight:500}}header{{padding:72px 0 48px;display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:18px}}.hero{{grid-column:1/10}}
.eyebrow,.chip,.field,.proof .k{{font:700 9px/1.35 var(--sans);letter-spacing:.16em;text-transform:uppercase}}.eyebrow{{color:var(--steel)}}
h1{{font:700 clamp(42px,6.2vw,76px)/.98 var(--sans);letter-spacing:-.025em;max-width:960px;margin:16px 0 0}}h1,h2{{overflow-wrap:anywhere}}h1 em,h2 em{{font-family:var(--serif);font-style:italic;font-weight:400;color:var(--steel)}}
.dek{{font-size:15px;line-height:1.6;color:var(--graphite);max-width:60ch;margin:22px 0 0}}.proof{{grid-column:1/-1;display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--ink);border-bottom:1px solid var(--line);margin-top:48px}}
.proof>div{{min-width:0;padding:13px 16px 13px 0}}.proof>div+div{{border-left:1px solid var(--line);padding-left:16px}}.proof .k{{display:block;color:var(--stone);margin-bottom:5px}}.proof .v{{font-size:12px;font-weight:500;overflow-wrap:anywhere}}
main{{padding:0 0 84px}}.notice{{border-left:2px solid var(--steel);color:var(--graphite);font-size:12px;line-height:1.55;padding:2px 0 2px 14px;margin:0 0 36px;max-width:72ch}}
.tools{{display:grid;grid-template-columns:repeat(12,1fr);column-gap:18px;align-items:end;border-bottom:1px solid var(--ink);padding-bottom:10px}}.search{{grid-column:1/9}}input{{width:100%;border:0;background:transparent;color:var(--ink);font:500 14px/1.4 var(--sans);padding:8px 0;outline:none}}input::placeholder{{color:var(--stone)}}
.tool-links{{grid-column:9/-1;display:flex;justify-content:flex-end;gap:16px}}a{{color:var(--steel)}}.tool-links a,.links a{{font:700 9px/1.35 var(--sans);letter-spacing:.12em;text-transform:uppercase;text-decoration:none;border-bottom:1px solid var(--line);padding-bottom:3px}}.tool-links a:hover,.links a:hover{{border-color:var(--steel)}}
.brief-list{{border-bottom:1px solid var(--ink)}}.brief-row{{display:grid;grid-template-columns:72px minmax(0,1fr) 260px;gap:24px;padding:28px 0;border-top:1px solid var(--line);align-items:start}}.hero,.brief-copy{{min-width:0}}.field{{font-family:var(--serif);font-style:italic;font-weight:400;color:var(--steel);font-size:15px;letter-spacing:0}}
.chip{{display:block;color:var(--stone);margin-bottom:9px}}h2{{font:700 25px/1.12 var(--sans);letter-spacing:-.018em;margin:0;max-width:30ch}}.brief-copy p{{font-size:12.5px;line-height:1.55;color:var(--graphite);max-width:64ch;margin:9px 0 0}}.links{{display:flex;justify-content:flex-end;gap:14px;flex-wrap:wrap;padding-top:24px}}
footer{{display:flex;justify-content:space-between;gap:18px;border-top:2px solid var(--ink);padding:14px 0 42px;color:var(--stone);font:700 9px/1.35 var(--sans);letter-spacing:.16em;text-transform:uppercase}}
@media(max-width:760px){{.shell{{width:calc(100% - 32px)}}header{{padding:52px 0 36px}}.hero{{grid-column:1/-1}}.proof{{grid-template-columns:1fr}}.proof>div+div{{border-left:0;border-top:1px solid var(--line);padding-left:0}}.tools{{display:flex;gap:12px;flex-direction:column;align-items:stretch}}.search{{width:100%}}.tool-links{{justify-content:flex-start}}.brief-row{{grid-template-columns:44px minmax(0,1fr);gap:14px}}.links{{grid-column:2;justify-content:flex-start;padding-top:4px}}.masthead{{align-items:flex-start;flex-direction:column;gap:5px}}}}
</style></head><body><div class="shell"><div class="masthead"><span>FARRICE CAIN</span><span class="mode">PORTABLE BRIEFING ROOM · {edition_label}</span></div>
<header><div class="hero"><div class="eyebrow">CURATED INTELLIGENCE · PORTABLE LIBRARY</div><h1>{accent_text(title, fallback_last=True)}</h1>
<p class="dek">A self-contained decision library built to travel without visual or evidentiary drift.</p></div>
<div class="proof"><div><span class="k">Mode</span><span class="v">{html.escape(mode_value)}</span></div><div><span class="k">Context</span><span class="v">{html.escape(context_value)}</span></div><div><span class="k">Portability</span><span class="v">Verified · repository independent</span></div></div></header><main>
<p class="notice">{html.escape(note)}</p><div class="tools"><div class="search"><input id="q" placeholder="Search the room" aria-label="Search briefs"></div>
<div class="tool-links">{tool_links}</div></div><section class="brief-list">{''.join(rows)}</section></main>
<footer><span>FARRICE CAIN · PORTABLE BRIEFING ROOM</span><span>PREMIUM MINIMAL · REPORT DIALECT</span></footer></div>
<script>const q=document.getElementById('q');q.addEventListener('input',()=>{{const v=q.value.toLowerCase();document.querySelectorAll('.brief-row').forEach(c=>c.hidden=!c.dataset.search.includes(v));}});</script>
</body></html>'''


def build_readme(title: str, audience: str, slugs: list[str], omissions: list[dict]) -> str:
    if audience == "private":
        warning = (
            "This is a PRIVATE INTERNAL export. It may include candid strategy, prompts, "
            "research notes, and source documents. Do not send the folder or ZIP to a client "
            "or prospect. Use a `--audience share` export for that."
        )
        ai_use = (
            "Give an AI `manifest.json`, then the selected brief's "
            "`briefs/<slug>/<slug>-context.json`. Every context `path` starts at this bundle root."
        )
    else:
        warning = (
            "This client edition contains presentation HTML and public source links only. "
            "Each brief keeps its evidence status and proof boundary visible."
        )
        ai_use = "This edition is designed for reading and review, not as an AI context package."
    omitted_line = (
        f"The manifest records {len(omissions)} omitted context item(s) with reasons."
        if omissions else "No requested context items were omitted."
    )
    slug_lines = "\n".join(f"- `{slug}`" for slug in slugs)
    return f"""# {title}

{warning}

## Open

Open `index.html` in any browser. It works directly from disk and through any static file host.

The visual source of truth travels with the bundle as `brand-contract.json`.
It records the approved Farrice Cain Premium Minimal palette, Helvetica Neue
typography, report-dialect exception, grid law, and prohibited visual signals.

## File integrity

The included `verify.py` can check every manifest hash and local link. This step
is optional for normal reading.

## Use with an AI

{ai_use}

{("`source-repo://...` labels preserve the original repository identity; they are provenance labels, not required local paths." if audience == "private" else "Every source link retained in the briefs points to a public webpage.")}

## Included briefs

{slug_lines}

## Evidence boundary

{omitted_line} External URLs remain URLs and require internet access. File hashes prove bundle integrity, not truth or market validity.
"""


def make_zip(bundle: Path) -> tuple[Path, str]:
    zip_path = bundle.with_suffix(".zip")
    if zip_path.exists():
        fail(f"ZIP already exists: {zip_path}")
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(bundle.rglob("*")):
            if path.is_file():
                archive.write(path, (Path(bundle.name) / path.relative_to(bundle)).as_posix())
    return zip_path, sha256_file(zip_path)


def export_bundle(args: argparse.Namespace) -> tuple[Path, Path | None]:
    brief_root = Path(args.brief_root).expanduser().resolve() if args.brief_root else BRIEFS
    if not brief_root.is_dir():
        fail(f"brief source directory not found: {brief_root}")
    slugs = list_slugs(brief_root) if args.all else [validate_slug(slug) for slug in args.slugs]
    slugs = list(dict.fromkeys(slugs))
    if not slugs:
        fail("choose one or more brief slugs, or pass --all")

    output = Path(args.output).expanduser() if args.output else (
        ROOT / "_exports" / "briefing-room" / ("portable-" + "-".join(slugs[:2]))
    )
    output = output.resolve()
    if output.exists():
        fail(f"output already exists; choose a new path: {output}")
    if output == ROOT.resolve():
        fail("output cannot be the repository root")
    output.parent.mkdir(parents=True, exist_ok=True)

    stage = Path(tempfile.mkdtemp(prefix=f".{output.name}.tmp-", dir=output.parent))
    records: dict[str, dict] = {}
    omissions: list[dict] = []
    brief_records: list[dict] = []
    dependency_destinations: dict[str, Path] = {}
    total_dependency_bytes = 0
    max_file = int(args.max_file_mb * 1024 * 1024)
    max_total = int(args.max_total_mb * 1024 * 1024)

    def source_identity(source: Path) -> str | None:
        """Return repository provenance when the source actually lives there.

        Curated brief roots may be generated in a temporary directory. Their
        bytes remain hashed, but they must not be mislabeled as repository
        paths or crash a private export.
        """
        resolved = source.resolve()
        for base in dict.fromkeys((ROOT.resolve(), CANONICAL_ROOT.resolve())):
            if _inside(resolved, base):
                return resolved.relative_to(base).as_posix()
        return None

    def record_file(path: Path, kind: str, source: Path | None = None, source_rel: str | None = None) -> None:
        rel = path.relative_to(stage).as_posix()
        row = {"path": rel, "kind": kind, "bytes": path.stat().st_size, "sha256": sha256_file(path)}
        if source is not None:
            if source_rel:
                row["source_repo_path"] = source_rel
            row["source_sha256"] = sha256_file(source)
        records[rel] = row

    try:
        loaded: list[dict] = []
        for slug in slugs:
            paths = brief_files(slug, brief_root, args.audience)
            try:
                meta = json.loads(paths["json"].read_text(encoding="utf-8"))
            except (OSError, ValueError) as exc:
                fail(f"{slug} brief JSON is unreadable: {exc}")
            meta.setdefault("slug", slug)
            pack, pack_source = load_context_pack(meta, paths) if args.audience == "private" else ({}, None)
            loaded.append({"slug": slug, "paths": paths, "meta": meta, "pack": pack, "pack_source": pack_source})

        if args.audience == "private":
            for brief in loaded:
                for item in brief["pack"].get("paths", []):
                    source, source_rel, reason = resolve_dependency(item, args.include_hidden)
                    if reason:
                        omission = {
                            "brief": brief["slug"], "source_path": source_rel or item.get("path") or item.get("abs"),
                            "role": item.get("role") or "context", "reason": reason,
                        }
                        omissions.append(omission)
                        continue
                    assert source is not None and source_rel is not None
                    if source_rel in dependency_destinations:
                        continue
                    size = source.stat().st_size
                    if size > max_file:
                        omissions.append({
                            "brief": brief["slug"], "source_path": source_rel,
                            "role": item.get("role") or "context",
                            "reason": f"file exceeds --max-file-mb ({args.max_file_mb:g} MiB)",
                        })
                        continue
                    if total_dependency_bytes + size > max_total:
                        omissions.append({
                            "brief": brief["slug"], "source_path": source_rel,
                            "role": item.get("role") or "context",
                            "reason": f"bundle context exceeds --max-total-mb ({args.max_total_mb:g} MiB)",
                        })
                        continue
                    destination_rel = Path("context") / "repo" / PurePosixPath(source_rel)
                    destination = stage / destination_rel
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source, destination)
                    dependency_destinations[source_rel] = destination_rel
                    total_dependency_bytes += size
                    record_file(destination, "context-source", source, source_rel)

        for brief in loaded:
            slug, meta, paths = brief["slug"], brief["meta"], brief["paths"]
            brief_dir = stage / "briefs" / slug
            brief_dir.mkdir(parents=True, exist_ok=True)
            artifacts = {"html": f"{slug}-brief.html"}
            portable_pack = None

            if args.audience == "share":
                out_html = brief_dir / artifacts["html"]
                out_html.write_text(render_share_html(meta), encoding="utf-8")
                record_file(out_html, "share-html")
            else:
                out_md = brief_dir / f"{slug}-brief.md"
                out_json = brief_dir / f"{slug}-brief.json"
                out_context = brief_dir / f"{slug}-context.json"
                out_html = brief_dir / artifacts["html"]
                portable_md = sanitize_source_roots(paths["md"].read_text(encoding="utf-8"))
                portable_json = sanitize_source_roots(paths["json"].read_text(encoding="utf-8"))
                out_md.write_text(portable_md, encoding="utf-8")
                out_json.write_text(portable_json, encoding="utf-8")

                portable_paths = []
                brief_omissions = []
                for item in brief["pack"].get("paths", []):
                    source, source_rel, reason = resolve_dependency(item, args.include_hidden)
                    destination_rel = dependency_destinations.get(source_rel or "")
                    if reason or destination_rel is None:
                        matched = next((o for o in omissions if o["brief"] == slug and o["source_path"] == (source_rel or item.get("path") or item.get("abs"))), None)
                        row = matched or {
                            "brief": slug, "source_path": source_rel or item.get("path") or item.get("abs"),
                            "role": item.get("role") or "context", "reason": reason or "not included",
                        }
                        brief_omissions.append({k: v for k, v in row.items() if k != "brief"})
                        if matched is None:
                            omissions.append(row)
                        continue
                    portable_paths.append({
                        "path": destination_rel.as_posix(),
                        "source_repo_path": source_rel,
                        "scope": "bundle",
                        "role": item.get("role") or "context",
                        "sha256": sha256_file(stage / destination_rel),
                    })
                portable_pack = {
                    "schema_version": SCHEMA_VERSION,
                    "slug": slug,
                    "title": re.sub(r"\*", "", str(meta.get("title") or slug)),
                    "compiled": meta.get("compiled"),
                    "generated_by": "execution/brief_export.py",
                    "audience": "private",
                    "path_policy": {
                        "canonical_field": "path",
                        "semantics": "resolve from the portable bundle root",
                        "provenance_field": "source_repo_path",
                        "absolute_paths": "intentionally removed",
                    },
                    "brief_html": f"briefs/{slug}/{slug}-brief.html",
                    "brief_md": f"briefs/{slug}/{slug}-brief.md",
                    "paths": portable_paths,
                    "urls": brief["pack"].get("urls", []),
                    "omissions": brief_omissions,
                }
                out_context.write_text(json.dumps(portable_pack, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
                source_html = paths["html"].read_text(encoding="utf-8")
                out_html.write_text(
                    rewrite_private_html(source_html, slug, portable_md, brief["pack"], portable_pack, dependency_destinations),
                    encoding="utf-8",
                )
                for key, out_path, kind in (
                    ("html", out_html, "brief-html"), ("md", out_md, "brief-markdown"),
                    ("json", out_json, "brief-provenance"),
                ):
                    source = paths[key]
                    record_file(out_path, kind, source, source_identity(source))
                if brief["pack_source"]:
                    source = brief["pack_source"]
                    record_file(out_context, "portable-context", source, source_identity(source))
                else:
                    record_file(out_context, "portable-context")
                artifacts.update({
                    "md": f"{slug}-brief.md", "json": f"{slug}-brief.json", "context": f"{slug}-context.json",
                })

            brief_records.append({
                "slug": slug, "meta": meta, "artifacts": artifacts,
                "context_files": len(portable_pack.get("paths", [])) if portable_pack else 0,
                "omissions": len(portable_pack.get("omissions", [])) if portable_pack else 0,
            })

        title = args.title or "Portable Briefing Room"
        index_path = stage / "index.html"
        readme_path = stage / "README.md"
        brand_path = stage / "brand-contract.json"
        index_path.write_text(build_index(title, args.audience, brief_records), encoding="utf-8")
        readme_path.write_text(build_readme(title, args.audience, slugs, omissions), encoding="utf-8")
        brand_contract = BRAND_CONTRACT if args.audience == "private" else client_brand_contract()
        brand_path.write_text(json.dumps(brand_contract, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        shutil.copy2(VERIFY_SOURCE, stage / "verify.py")
        record_file(index_path, "bundle-index")
        record_file(readme_path, "bundle-readme")
        record_file(brand_path, "brand-contract")
        if args.audience == "private":
            record_file(stage / "verify.py", "bundle-verifier", VERIFY_SOURCE, "execution/verify_brief_export.py")
        else:
            record_file(stage / "verify.py", "bundle-verifier")

        commit = source_commit() if args.audience == "private" else None
        identity_seed = json.dumps({"slugs": slugs, "audience": args.audience, "commit": commit}, sort_keys=True)
        manifest = {
            "schema_version": SCHEMA_VERSION,
            "bundle_id": hashlib.sha256(identity_seed.encode("utf-8")).hexdigest()[:16],
            "title": title,
            "audience": args.audience,
            "warning": (
                "PRIVATE INTERNAL EXPORT — do not send as-is" if args.audience == "private"
                else "CLIENT EDITION — presentation-only; proof boundaries remain explicit"
            ),
            "brand": {
                "name": BRAND_CONTRACT["name"],
                "mode": BRAND_CONTRACT["mode"],
                "contract": "brand-contract.json",
            },
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "briefs": [{k: v for k, v in row.items() if k != "meta"} for row in brief_records],
            "files": [records[key] for key in sorted(records)],
            "omissions": omissions,
            "limits": {"max_file_mb": args.max_file_mb, "max_total_context_mb": args.max_total_mb},
            "integrity_note": "SHA-256 proves file integrity only; it does not validate authored claims.",
        }
        if commit:
            manifest["source_commit"] = commit
        (stage / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        os.replace(stage, output)
        stage = None
        zip_path = make_zip(output)[0] if args.zip else None
        print(
            f"[brief_export] OK → {output} "
            f"({len(slugs)} brief(s) · {len(records)} hashed file(s) · {len(omissions)} omission(s))"
        )
        if zip_path:
            print(f"[brief_export] ZIP → {zip_path} · sha256 {sha256_file(zip_path)}")
        print(f"[brief_export] VERIFY → python3 {output / 'verify.py'} {output}")
        return output, zip_path
    finally:
        if stage is not None and stage.exists():
            shutil.rmtree(stage)


def main() -> int:
    parser = argparse.ArgumentParser(description="Export selected Briefing Room briefs as a portable folder/ZIP.")
    parser.add_argument("slugs", nargs="*", help="brief directory slug(s)")
    parser.add_argument("--all", action="store_true", help="export every brief in the library")
    parser.add_argument("--list", action="store_true", help="list exportable brief slugs and exit")
    parser.add_argument("--output", help="new bundle directory (must not already exist)")
    parser.add_argument("--title", help="title shown on the portable index")
    parser.add_argument("--audience", choices=("private", "share"), default="private",
                        help="private includes context; share renders stripped HTML only")
    parser.add_argument("--brief-root",
                        help="alternate directory of curated <slug>/<slug>-brief artifacts")
    parser.add_argument("--zip", action="store_true", help="also create <output>.zip")
    parser.add_argument("--include-hidden", action="store_true",
                        help="private mode only: allow hidden repo paths except secrets and .git")
    parser.add_argument("--max-file-mb", type=float, default=DEFAULT_MAX_FILE_MB)
    parser.add_argument("--max-total-mb", type=float, default=DEFAULT_MAX_TOTAL_MB)
    args = parser.parse_args()

    if args.list:
        print("\n".join(list_slugs()))
        return 0
    if args.all and args.slugs:
        fail("use explicit slugs or --all, not both")
    if args.include_hidden and args.audience != "private":
        fail("--include-hidden is only valid for private exports")
    if args.max_file_mb <= 0 or args.max_total_mb <= 0:
        fail("size limits must be positive")
    export_bundle(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
