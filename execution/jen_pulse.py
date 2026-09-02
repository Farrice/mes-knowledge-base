#!/usr/bin/env python3
"""jen_pulse.py — weekly public-numbers pulse for an Instagram grid (default @_jiing).

Deterministic, read-only, $0, no login, no browser automation library. Two moves:
  1. chrome-headless-shell --dump-dom on /<handle>/reels/  → per-reel views / likes / comments (the logged-out
     grid renders the first 12 reels with all three counts) + follower / following counts.
  2. one plain GET per reel page → og:description → date, likes, comments, caption first line (the hook).

Writes  <out>/YYYY-MM-DD.json  (raw rows)  and  <out>/latest.md  (table + medians + deltas vs the previous pulse).
Feeds FUNNEL-MATH.md and the monthly /alyssa-stalker-outlier-audit. Never posts, likes, or logs in
(directives/browser-automation-safety.md Tier 1).

  python3 execution/jen_pulse.py                                  # @_jiing → _active/clients/jen-listings/06-system/pulse/
  python3 execution/jen_pulse.py --handle someone --out .tmp/pulse
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import html
import json
import os
import pathlib
import re
import statistics
import subprocess
import sys
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "_active" / "clients" / "jen-listings" / "06-system" / "pulse"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
      "(KHTML, like Gecko) Version/17.0 Safari/605.1.15")


def chrome_path() -> str:
    cands = sorted(glob.glob(os.path.expanduser(
        "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))
    if not cands:
        sys.exit("chrome-headless-shell not found under ~/Library/Caches/ms-playwright — install a Playwright chromium once")
    return cands[-1]


def to_int(tok: str) -> int:
    t = tok.replace(",", "").strip()
    mult = 1
    if t.endswith("K"):
        mult, t = 1_000, t[:-1]
    elif t.endswith("M"):
        mult, t = 1_000_000, t[:-1]
    return int(float(t) * mult)


def dump_grid(handle: str) -> tuple[int | None, int | None, list[dict]]:
    url = f"https://www.instagram.com/{handle}/reels/"
    dom = subprocess.run(
        [chrome_path(), "--headless", "--disable-gpu", "--no-sandbox", "--virtual-time-budget=8000",
         "--window-size=1200,2000", "--dump-dom", url],
        capture_output=True, text=True, timeout=90).stdout
    hrefs = [(m.start(), m.group(1)) for m in re.finditer(rf'href="/{re.escape(handle)}/reel/([A-Za-z0-9_-]+)/"', dom)]
    nums = [(m.start(), m.group(1)) for m in re.finditer(r">([0-9][0-9,.]*[KM]?)<", dom)]
    followers = following = None
    pre = [n for p, n in nums if not hrefs or p < hrefs[0][0]]
    if len(pre) >= 2:
        followers, following = to_int(pre[0]), to_int(pre[1])
    rows, seen = [], set()
    for i, (pos, code) in enumerate(hrefs):
        if code in seen:
            continue
        seen.add(code)
        end = hrefs[i + 1][0] if i + 1 < len(hrefs) else len(dom)
        trio = [to_int(n) for p, n in nums if pos < p < end][:3]
        row = {"code": code, "url": f"https://www.instagram.com/{handle}/reel/{code}/"}
        if len(trio) == 3:
            row.update(likes=trio[0], comments=trio[1], views=trio[2])
        rows.append(row)
    return followers, following, rows


def fetch_meta(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            page = r.read().decode("utf-8", "ignore")
    except Exception as e:  # network or 429; keep going, mark the row
        return {"meta_error": str(e)[:80]}
    m = re.search(r'property="og:description" content="([^"]*)"', page)
    if not m:
        return {"meta_error": "no og:description"}
    desc = html.unescape(m.group(1))
    out: dict = {}
    head = re.match(r"\s*([\d,]+) likes?, ([\d,]+) comments? - \S+ on ([A-Za-z]+ \d{1,2}, \d{4}):\s*[\"“]?(.*)", desc, re.S)
    if head:
        out["likes_meta"] = to_int(head.group(1))
        out["comments_meta"] = to_int(head.group(2))
        try:
            out["date"] = dt.datetime.strptime(head.group(3), "%B %d, %Y").date().isoformat()
        except ValueError:
            out["date"] = head.group(3)
        cap = head.group(4).strip().rstrip('"”. ')
        out["hook"] = cap.split("\n")[0][:160]
        out["caption"] = cap[:1200]
    else:
        out["hook"] = desc[:160]
    return out


def previous_pulse(out_dir: pathlib.Path, today: str) -> dict | None:
    files = sorted(p for p in out_dir.glob("*.json") if p.stem != today)
    if not files:
        return None
    return json.loads(files[-1].read_text())


def render_md(pulse: dict, prev: dict | None) -> str:
    rows = [r for r in pulse["reels"] if "views" in r]
    prev_rows = {r["code"]: r for r in (prev or {}).get("reels", [])}
    med = lambda k: statistics.median([r[k] for r in rows if k in r]) if rows else 0
    lines = [f"# pulse · @{pulse['handle']} · {pulse['pulled_at'][:10]}", ""]
    f, fo = pulse.get("followers"), pulse.get("following")
    df = f"{f - prev['followers']:+d}" if prev and prev.get("followers") and f else "—"
    lines += [f"followers {f} ({df} since last pulse) · following {fo} · reels read {len(rows)}", ""]
    lines += [f"median views **{int(med('views')):,}** · median likes **{int(med('likes')):,}** · median comments **{int(med('comments')):,}**", ""]
    lines += ["| date | hook | views | likes | comments | Δ views since last pulse | url |", "|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: r.get("date", ""), reverse=True):
        pv = prev_rows.get(r["code"], {}).get("views")
        delta = f"{r['views'] - pv:+,}" if pv is not None else "new" if prev else "—"
        hook = (r.get("hook") or "").replace("|", "/")
        lines.append(f"| {r.get('date','')} | {hook[:70]} | {r['views']:,} | {r['likes']:,} | {r['comments']:,} | {delta} | {r['url']} |")
    if prev:
        new = [r for r in rows if r["code"] not in prev_rows]
        lines += ["", f"new since last pulse: {len(new)}" + (" — " + "; ".join((r.get('hook') or r['code'])[:50] for r in new) if new else "")]
    lines += ["", "Read-only public numbers. Saves, shares, reach, and follows are not public; they come from Jen's Insights or not at all.",
              "Monthly: run `/alyssa-stalker-outlier-audit` on this table; update `../FUNNEL-MATH.md` inputs."]
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--handle", default="_jiing")
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--no-meta", action="store_true", help="skip per-reel page fetches (grid counts only)")
    ap.add_argument("--sleep", type=float, default=1.0, help="seconds between reel page fetches")
    a = ap.parse_args()
    out_dir = pathlib.Path(a.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    today = dt.date.today().isoformat()

    followers, following, rows = dump_grid(a.handle)
    if not rows:
        sys.exit("grid dump returned no reels — Instagram may have changed the logged-out grid or rate-limited this IP")
    if not a.no_meta:
        for r in rows:
            r.update(fetch_meta(r["url"]))
            time.sleep(a.sleep)
    pulse = {"pulled_at": dt.datetime.now().isoformat(timespec="seconds"), "handle": a.handle,
             "followers": followers, "following": following, "reels": rows,
             "note": "public logged-out numbers; first 12 reels only; views/likes/comments from the grid, date/hook from og:description"}
    prev = previous_pulse(out_dir, today)
    (out_dir / f"{today}.json").write_text(json.dumps(pulse, indent=2, ensure_ascii=False))
    md = render_md(pulse, prev)
    (out_dir / "latest.md").write_text(md)
    print(md)


if __name__ == "__main__":
    main()
