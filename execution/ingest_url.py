#!/usr/bin/env python3
"""ingest_url.py — one door for "paste anything, get text" (canvas build, 2026-09-10).

The Poppy.ai trick is not intelligence: paste a URL, the transcript appears,
the chat box downstream reads it. This is that door, free-first, cached.

    ingest(source) -> {"kind", "title", "text", "meta", "cache_path"}

Routing by shape of the input:
    youtube.com / youtu.be   → youtube-transcript-api (seconds, no download);
                               falls back to watch_free.py (yt-dlp captions →
                               local whisper.cpp) when captions are off
    tiktok / instagram / any other video URL → watch_free.py
    *.pdf (URL or path)      → pypdf
    any other http(s) URL    → trafilatura (readability-grade article text)
    local .mp4/.mov/.mp3/.m4a/.wav → watch_free.py (video) or whisper-cli (audio)
    anything else            → treated as pasted text, passthrough

Every result is cached under .agent/canvas/cache/<sha>.json so re-adding the
same node costs nothing. No paid API is called anywhere in this file.

CLI:
    python3 execution/ingest_url.py <url-or-path-or-text> [--force] [--json]
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
EXEC = ROOT / "execution"
CACHE_DIR = ROOT / ".agent" / "canvas" / "cache"
_VENV_PY = Path(__file__).resolve().parent.parent / ".venv" / "bin" / "python3"
PY = str(_VENV_PY) if _VENV_PY.exists() else (sys.executable or "python3")  # deps live in the venv


def _env() -> dict:
    """Prefer the repo venv's yt-dlp over a stale brew copy (TikTok broke on
    2026.07.04, works on 2026.08.19 — 2026-09-10). PATH-prepend, nothing global."""
    env = dict(os.environ)
    vbin = str(ROOT / ".venv" / "bin")
    if os.path.isdir(vbin):
        env["PATH"] = vbin + os.pathsep + env.get("PATH", "")
    return env

VIDEO_HOSTS = ("youtube.com", "youtu.be", "tiktok.com", "instagram.com", "vimeo.com",
               "facebook.com", "fb.watch", "x.com", "twitter.com", "loom.com")
YOUTUBE_HOSTS = ("youtube.com", "youtu.be")
MEDIA_EXT = {".mp4", ".mov", ".mkv", ".webm", ".m4v", ".mp3", ".m4a", ".wav", ".aac", ".ogg"}
AUDIO_EXT = {".mp3", ".m4a", ".wav", ".aac", ".ogg"}
WHISPER_MODEL = Path("~/.cache/whisper-cpp/ggml-base.en.bin").expanduser()


# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------

def _is_url(s: str) -> bool:
    try:
        u = urlparse(s.strip())
        return u.scheme in ("http", "https") and bool(u.netloc)
    except ValueError:
        return False


def _host(s: str) -> str:
    return (urlparse(s).netloc or "").lower().removeprefix("www.").removeprefix("m.")


def _key(source: str) -> str:
    return hashlib.sha1(source.strip().encode("utf-8")).hexdigest()[:16]


def est_tokens(text: str) -> int:
    return max(1, len(text) // 4) if text else 0


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def _oembed_meta(url: str) -> dict:
    """Title + channel from YouTube's oEmbed endpoint: ~0.3s, no download.
    (yt-dlp's metadata pass on the same video measured 20+ s — 2026-09-10.)"""
    try:
        import requests  # in .venv, carries its own CA bundle
        r = requests.get("https://www.youtube.com/oembed",
                         params={"url": url, "format": "json"}, timeout=8)
        if r.ok:
            j = r.json()
            return {"title": j.get("title", ""), "channel": j.get("author_name", "")}
    except Exception:
        pass
    return {}


def _ytdlp_meta(url: str) -> dict:
    """Title/channel/duration without downloading. Slow (20 s+); only a fallback."""
    if not shutil.which("yt-dlp"):
        return {}
    try:
        r = subprocess.run(
            ["yt-dlp", "--skip-download", "--no-warnings", "--print",
             "%(title)s\t%(channel)s\t%(duration)s\t%(upload_date)s", "--", url],
            capture_output=True, text=True, timeout=60, env=_env())
        line = (r.stdout or "").strip().splitlines()
        if not line:
            return {}
        parts = (line[0].split("\t") + ["", "", "", ""])[:4]
        return {"title": parts[0], "channel": parts[1],
                "duration_s": _num(parts[2]), "upload_date": parts[3]}
    except (OSError, subprocess.SubprocessError):
        return {}


def _num(s: str):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


# ----------------------------------------------------------------------------
# fetchers — each returns (title, text, meta)
# ----------------------------------------------------------------------------

def _youtube_fast(url: str):
    ft = _load_module(EXEC / "fetch-transcript.py", "fetch_transcript_mod")
    vid = ft.extract_video_id(url)
    text = ft.fetch_transcript(vid)
    meta = _oembed_meta(url) or _ytdlp_meta(url)
    meta.update({"video_id": vid, "transcript_source": "youtube_captions_api"})
    return meta.get("title") or f"YouTube {vid}", text, meta


def _watch_free(source: str, key: str):
    """yt-dlp captions → local whisper.cpp. Writes a source package under the
    cache dir; we lift transcript.txt + metadata.json out of it."""
    out = CACHE_DIR / f"{key}-src"
    if out.exists():
        shutil.rmtree(out)  # acquire() demands an empty dir
    r = subprocess.run([PY, str(EXEC / "watch_free.py"), source, "--out-dir", str(out),
                        "--frames", "0"], capture_output=True, text=True, timeout=2400, env=_env())
    tpath = out / "transcript.txt"
    if r.returncode != 0 or not tpath.exists():
        tail = (r.stderr or r.stdout or "")[-400:]
        host = urlparse(source).netloc.lower()
        if "tiktok.com" in host or "instagram.com" in host:
            raise RuntimeError("TikTok and Instagram videos are login-walled for downloaders, so the words "
                               "can't be pulled for free here. Use the profile card for the listing, or paste "
                               "the caption/transcript as text. (vidIQ 'watch' can transcribe them for credits.)")
        raise RuntimeError(f"video fetch failed: {tail.strip()[-200:]}")
    text = tpath.read_text(encoding="utf-8").strip()
    meta = {}
    mpath = out / "metadata.json"
    if mpath.exists():
        try:
            meta = json.loads(mpath.read_text(encoding="utf-8")) or {}
        except ValueError:
            meta = {}
    try:
        acq = json.loads((out / "acquisition.json").read_text(encoding="utf-8"))
        meta["transcript_source"] = acq.get("transcript_source")
        meta["duration_s"] = acq.get("duration_seconds")
    except (OSError, ValueError):
        pass
    title = meta.get("title") or Path(source).name or source
    return title, text, meta


def _whisper_audio(path: Path, key: str):
    """Audio-only local file: ffmpeg → 16k wav → whisper-cli. Free, local."""
    if not shutil.which("whisper-cli") or not WHISPER_MODEL.is_file():
        raise RuntimeError("whisper-cli or its model is missing; cannot transcribe audio locally")
    out = CACHE_DIR / f"{key}-src"
    out.mkdir(parents=True, exist_ok=True)
    wav = out / "audio.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(path), "-vn", "-ac", "1",
                    "-ar", "16000", "-c:a", "pcm_s16le", str(wav)], check=True, timeout=600)
    base = out / "local-transcript"
    subprocess.run(["whisper-cli", "-ng", "-m", str(WHISPER_MODEL), "-f", str(wav), "-otxt",
                    "-of", str(base), "-np"], capture_output=True, text=True, timeout=3600,
                   check=True)
    text = (out / "local-transcript.txt").read_text(encoding="utf-8").strip()
    return path.name, text, {"transcript_source": "local_whisper_cpp", "path": str(path)}


def _pdf(source: str, key: str):
    from pypdf import PdfReader  # in .venv
    if _is_url(source):
        import requests  # urllib on this python has no CA bundle; requests does
        local = CACHE_DIR / f"{key}.pdf"
        r = requests.get(source, timeout=60)
        r.raise_for_status()
        local.write_bytes(r.content)
    else:
        local = Path(source).expanduser().resolve()
    reader = PdfReader(str(local))
    pages = []
    for i, p in enumerate(reader.pages):
        t = (p.extract_text() or "").strip()
        if t:
            pages.append(f"[page {i + 1}]\n{t}")
    text = "\n\n".join(pages)
    title = ""
    try:
        title = (reader.metadata or {}).get("/Title") or ""
    except Exception:
        title = ""
    return (title or local.name), text, {"pages": len(reader.pages), "path": str(local)}


def _article(url: str):
    import trafilatura  # in .venv
    html = trafilatura.fetch_url(url)
    if not html:
        raise RuntimeError("fetch returned nothing (blocked, login-walled, or JS-only page)")
    text = trafilatura.extract(html, include_comments=False, include_tables=True,
                               favor_recall=True, url=url) or ""
    if not text.strip():
        raise RuntimeError("no article text extracted")
    title, author, date, site = "", "", "", ""
    try:
        md = trafilatura.extract_metadata(html, default_url=url)
        if md:
            title, author, date, site = md.title or "", md.author or "", md.date or "", md.sitename or ""
    except Exception:
        pass
    return (title or url), text.strip(), {"author": author, "date": date, "site": site}


# ----------------------------------------------------------------------------
# router
# ----------------------------------------------------------------------------

def classify(source: str) -> str:
    s = source.strip()
    if _is_url(s):
        path = urlparse(s).path.lower()
        if path.endswith(".pdf"):
            return "pdf"
        h = _host(s)
        if any(h == v or h.endswith("." + v) for v in YOUTUBE_HOSTS):
            return "youtube"
        if any(h == v or h.endswith("." + v) for v in VIDEO_HOSTS):
            return "video_url"
        return "article"
    p = Path(s).expanduser()
    if p.is_file():
        ext = p.suffix.lower()
        if ext == ".pdf":
            return "pdf"
        if ext in AUDIO_EXT:
            return "local_audio"
        if ext in MEDIA_EXT:
            return "local_video"
        if ext in {".txt", ".md", ".markdown", ".vtt", ".srt", ".json", ".csv"}:
            return "local_text"
    return "text"


def ingest(source: str, *, force: bool = False) -> dict:
    source = source.strip()
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    key = _key(source)
    cpath = CACHE_DIR / f"{key}.json"
    if cpath.exists() and not force:
        try:
            cached = json.loads(cpath.read_text(encoding="utf-8"))
            cached["cache_hit"] = True
            return cached
        except ValueError:
            pass

    kind = classify(source)
    t0 = time.time()
    meta: dict = {}
    if kind == "youtube":
        try:
            title, text, meta = _youtube_fast(source)
        except Exception as e:  # captions off / API blocked → free download path
            meta["fast_path_error"] = str(e)[:200]
            title, text, m2 = _watch_free(source, key)
            meta.update(m2)
    elif kind == "video_url" or kind == "local_video":
        title, text, meta = _watch_free(source, key)
    elif kind == "local_audio":
        title, text, meta = _whisper_audio(Path(source).expanduser().resolve(), key)
    elif kind == "pdf":
        title, text, meta = _pdf(source, key)
    elif kind == "article":
        title, text, meta = _article(source)
    elif kind == "local_text":
        p = Path(source).expanduser().resolve()
        title, text, meta = p.name, p.read_text(encoding="utf-8", errors="replace"), {"path": str(p)}
    else:
        first = source.splitlines()[0] if source else "note"
        title, text, meta = (first[:80] or "note"), source, {}

    text = re.sub(r"[ \t]+\n", "\n", text or "").strip()
    rec = {
        "kind": kind,
        "title": (title or "").strip()[:200] or source[:80],
        "text": text,
        "meta": {**meta, "url": source if _is_url(source) else None,
                 "source": source[:500], "chars": len(text), "tokens_est": est_tokens(text),
                 "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
                 "seconds": round(time.time() - t0, 1)},
        "cache_path": str(cpath),
        "cache_hit": False,
    }
    cpath.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
    return rec


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", help="URL, local path, or pasted text")
    ap.add_argument("--force", action="store_true", help="ignore the cache")
    ap.add_argument("--json", action="store_true", help="print the full record")
    a = ap.parse_args()
    try:
        rec = ingest(a.source, force=a.force)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    if a.json:
        print(json.dumps(rec, ensure_ascii=False, indent=1))
        return 0
    m = rec["meta"]
    hit = " (cache)" if rec.get("cache_hit") else f" ({m.get('seconds')}s)"
    print(f"{rec['kind']} · {rec['title']}")
    print(f"{m.get('chars'):,} chars · ~{m.get('tokens_est'):,} tokens · "
          f"{m.get('transcript_source') or m.get('site') or ''}{hit}")
    print(f"cache: {rec['cache_path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
