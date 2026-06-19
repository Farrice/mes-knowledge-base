#!/usr/bin/env python3
"""
brand_radar.py — Weekly named-brand intelligence sweep for the Farrice Engine.

Pulls RAW data (no inference) on the Top-10 target brands via Apify, so the daily
Creative Brief / cook can weave in NAMED specifics (real captions, engagement, formats)
for narrative, tension, and authority. Deterministic; interpretation happens in the cook.

Per directives/apify-usage-policy.md: Apify self-governs budget and NEVER throws — on
`{"fallback": true}` we log the gap and move on (no silent break, no blocking).

Output: `_active/linkedin-launch/daily/brand-radar-YYYY-WW.md`
Config: edit BRANDS below (correct any IG handle that returns no data).

Usage:
  python3 execution/brand_radar.py            # full sweep, write the radar file
  python3 execution/brand_radar.py --limit 8  # posts per brand (default 10)
  python3 execution/brand_radar.py --brands gorgie,bala   # subset by handle
"""
import argparse
import datetime
import json
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(REPO, "_active/linkedin-launch/daily")

# (display name, instagram handle, website) — Top-10 from research/wellness-supplement-brand-niche.md.
# Correct any handle that returns no data (Apify will just report empty + we note it).
BRANDS = [
    ("Create Wellness", "create", "https://createwellness.com"),
    ("Gorgie", "drinkgorgie", "https://drinkgorgie.com"),
    ("Gainful", "gainful", "https://gainful.com"),
    ("Momentous", "livemomentous", "https://www.livemomentous.com"),
    ("Four Sigmatic", "foursigmatic", "https://foursigmatic.com"),
    ("Hilma", "hilma", "https://www.hilma.co"),
    ("Bala", "bala", "https://bala.com"),
    ("Joovv", "joovv", "https://joovv.com"),
    ("Plunge", "plunge", "https://plunge.com"),
    ("Rasa", "wearerasa", "https://wearerasa.com"),
]


def apify(actor, *args):
    cmd = ["python3", "execution/apify_client.py", actor] + list(args)
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO)
    out = (res.stdout or "") + (res.stderr or "")
    a, b = out.find("{"), out.rfind("}")
    s, e2 = out.find("["), out.rfind("]")
    # response may be a JSON object (status/fallback) or a JSON array (items)
    payload = ""
    if a != -1 and b > a:
        payload = out[a:b + 1]
    if s != -1 and e2 > s and (s < a or a == -1):
        payload = out[s:e2 + 1]
    try:
        return json.loads(payload) if payload else None
    except json.JSONDecodeError:
        return None


def items_of(resp):
    if resp is None:
        return [], "no-response"
    if isinstance(resp, dict):
        if resp.get("fallback"):
            return [], "budget-fallback"
        if "items" in resp:
            return resp["items"], "ok"
        return [resp], "ok"
    if isinstance(resp, list):
        return resp, "ok"
    return [], "unknown"


def caption_of(it):
    for k in ("caption", "text", "title", "description"):
        v = it.get(k) if isinstance(it, dict) else None
        if v:
            return re.sub(r"\s+", " ", str(v)).strip()
    return ""


def eng_of(it):
    likes = it.get("likesCount") or it.get("likes") or it.get("likeCount") or "?"
    comments = it.get("commentsCount") or it.get("comments") or it.get("commentCount") or "?"
    return likes, comments


def sweep_brand(name, handle, url, limit):
    block = [f"### {name}  ·  @{handle}  ·  {url}"]
    resp = apify("instagram", handle, "--limit", str(limit))
    posts, status = items_of(resp)
    if not posts:
        block.append(f"- _IG: {status} (correct the handle in brand_radar.py if this brand should have data)_")
    else:
        block.append(f"- **Recent posts ({len(posts)}):**")
        for it in posts[:limit]:
            if not isinstance(it, dict):
                continue
            cap = caption_of(it)
            likes, comments = eng_of(it)
            if cap:
                block.append(f"  - [{likes}❤ / {comments}💬] {cap[:200]}")
    return "\n".join(block)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--brands", help="comma-separated handles to limit the sweep")
    args = ap.parse_args()

    now = datetime.datetime.now()
    iso = now.isocalendar()
    tag = f"{iso[0]}-W{iso[1]:02d}"
    brands = BRANDS
    if args.brands:
        want = {b.strip().lower() for b in args.brands.split(",")}
        brands = [b for b in BRANDS if b[1].lower() in want]

    print(f"🛰  Brand Radar {tag} — sweeping {len(brands)} brands (Apify IG, limit {args.limit}/brand)\n")
    blocks = []
    for name, handle, url in brands:
        print(f"  · {name} (@{handle})")
        blocks.append(sweep_brand(name, handle, url, args.limit))

    header = (
        f"# Brand Radar — {tag}\n\n"
        f"> Raw named-brand intelligence (Apify Instagram). The daily Creative Brief / cook INTERPRETS this — "
        f"format winners, visual/voice sameness, the angle gap, the wedge. Feed named specifics into posts + teardown DMs.\n"
        f"> Generated {now.strftime('%Y-%m-%d %H:%M')}. Budget self-governed (apify-usage-policy). "
        f"Brands with no data = fix the handle in `execution/brand_radar.py`.\n"
    )
    out_path = os.path.join(OUT_DIR, f"brand-radar-{tag}.md")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(out_path, "w") as f:
        f.write(header + "\n" + "\n\n".join(blocks) + "\n")
    print(f"\n✓ Brand Radar written → {os.path.relpath(out_path, REPO)}")
    # budget snapshot
    bs = apify("budget-status")
    if isinstance(bs, dict):
        print(f"  Apify spent this month: ${bs.get('spent_dollars', '?')} / ${bs.get('plan_dollars', '?')} ({bs.get('state','?')})")


if __name__ == "__main__":
    main()
