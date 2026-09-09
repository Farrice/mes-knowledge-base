#!/usr/bin/env python3
"""build_hook_surface.py: the blind judging surface for HOOK-ROOM-11 (eight finalists + the specimen, shuffled, unlabeled).
  python3 build_hook_surface.py   # writes .tmp/valley-os/hook-room-11.html + HOOK-ROOM-11-KEY.json beside this file
Cards are drawn the way the reel draws them: white Playfair over a dark wash of her two photos (kitchen, exterior), her lockup at the foot.
"""
import base64, html, json, pathlib, random, subprocess

HERE = pathlib.Path(__file__).parent
ROOT = pathlib.Path(__file__).resolve().parents[5]
PH = ROOT / "_active/clients/jen-listings/06-system/valley-editions/photos/jen"
OUT = ROOT / ".tmp/valley-os/hook-room-11.html"
OUT.parent.mkdir(parents=True, exist_ok=True)

ENTRIES = {
    "K1": ("the kitchen you keep<br>screenshotting", "the $860K version<br>exists in tarzana.<br>i found three."),
    "K5": ("you screenshot the kitchen.<br>your person hearts it.<br>nobody says anything.", "$860K says something.<br>tarzana. three of them."),
    "F1": ("the kitchens you save<br>and the kitchens<br>you can afford", "meet in tarzana<br>at $860K."),
    "F4": ("midnight kitchen.<br>morning budget.", "they meet in tarzana<br>at $860K.<br>three times this week."),
    "H2": ("your thumb knows<br>the white oak one<br>by now", "it&#8217;s $860K in tarzana.<br>the door is real."),
    "H3": ("you send the kitchen.<br>the read receipt.<br>nothing.", "tarzana has three<br>under $900K this week.<br>one of them just dropped."),
    "H4": ("the island. the light at 4pm.<br>the house you&#8217;ll never tour.", "the one you will<br>is $860K. tarzana.<br>this week."),
    "L3": ("your person stopped replying<br>to the kitchen screenshots", "send them this instead.<br>$860K, tarzana,<br>three of them."),
    "SPECIMEN": ("&#8220;Sorry, one more<br>question&#8230;&#8221;", "You&#8217;re buying<br>an $800K house.<br>You can ask me<br>whatever you need."),
}

def thumb(name, w=540):
    src = PH / name
    dst = pathlib.Path("/private/tmp/claude-501/-Users-farricecain-Google-Antigravity--claude-worktrees-sweet-chatterjee-785901/fb507082-9a9a-4eef-8f82-1d1363b9f994/scratchpad") / f"{src.stem}-{w}.jpg"
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "70", "--resampleWidth", str(w), str(src), "--out", str(dst)], check=True, capture_output=True)
    b = base64.b64encode(dst.read_bytes()).decode()
    dst.unlink()
    return "data:image/jpeg;base64," + b

KITCHEN, EXTERIOR = thumb("listing-04-kitchen.jpg"), thumb("listing-01-exterior.jpg")
keys = list(ENTRIES)
random.seed(1109)
random.shuffle(keys)
json.dump({"order": keys, "seed": 1109, "note": "open after tapping; entry n = order[n-1]"}, open(HERE / "HOOK-ROOM-11-KEY.json", "w"), indent=2)

def card(n, k):
    b1, b2 = ENTRIES[k]
    return f'''<article class="entry" id="e{n}">
  <div class="num">{n}</div>
  <div class="pair">
    <div class="frame" style="background-image:url({KITCHEN})"><div class="wash"></div><div class="line">{b1}</div><div class="lockup"><span>Jen Santulan</span><small>REALTOR&#174; &#183; SAN FERNANDO VALLEY</small></div></div>
    <div class="frame" style="background-image:url({EXTERIOR})"><div class="wash"></div><div class="line small">{b2}</div><div class="lockup"><span>Jen Santulan</span><small>REALTOR&#174; &#183; SAN FERNANDO VALLEY</small></div></div>
  </div>
</article>'''

CSS = """
:root{--ink:#1E2430;--paper:#F5F6F8;--steel:#1E3A5F;--muted:#6B7684;--line:#DDE3EA}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--ink:#E8ECF1;--paper:#141920;--steel:#C9D4E2;--muted:#9AA6B5;--line:#2A3340}}
:root[data-theme="dark"]{--ink:#E8ECF1;--paper:#141920;--steel:#C9D4E2;--muted:#9AA6B5;--line:#2A3340}
body{background:var(--paper);color:var(--ink);font-family:Jost,system-ui,sans-serif;margin:0}
main{max-width:1180px;margin:0 auto;padding:2rem 1.2rem 5rem}
h1{font-family:'Playfair Display',Georgia,serif;font-weight:400;font-size:2rem;margin:0 0 .3rem}
p.lede{color:var(--muted);max-width:70ch;margin:.2rem 0 1.6rem}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:1.4rem 1.2rem}
.entry{display:grid;grid-template-columns:34px 1fr;gap:.6rem;align-items:start}
.num{font-family:'Playfair Display',Georgia,serif;font-size:1.6rem;color:var(--steel);padding-top:.2rem}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:6px}
.frame{position:relative;aspect-ratio:9/16;background-size:cover;background-position:center;overflow:hidden;border-radius:4px}
.wash{position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,20,30,.18) 0%,rgba(15,20,30,.42) 55%,rgba(15,20,30,.62) 100%)}
.line{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center;padding:0 12px 40px;font-family:'Playfair Display',Georgia,serif;font-size:19px;line-height:1.06;letter-spacing:-.02em;color:#fff;text-shadow:0 2px 14px rgba(0,0,0,.35)}
.line.small{font-size:16px}
.lockup{position:absolute;left:0;right:0;bottom:12px;text-align:center;color:#fff;line-height:1}
.lockup span{font-family:Caveat,cursive;font-size:14px;display:block}
.lockup small{font-family:Jost,sans-serif;font-size:5.5px;letter-spacing:.3em;opacity:.85}
.foot{margin-top:2.4rem;border-top:1px solid var(--line);padding-top:1rem;color:var(--muted);font-size:13px;max-width:70ch}
"""

body = "".join(card(i + 1, k) for i, k in enumerate(keys))
page = f'''<title>Hook Room 11</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@500&family=Jost:wght@400;500&family=Playfair+Display&display=swap">
<style>{CSS}</style>
<main>
<h1>Hook Room 11</h1>
<p class="lede">Nine two-beat pairs for the tuesday reel, drawn the way the reel draws them. One of the nine is the approved specimen, unlabeled. Tap the pair that makes you say "damn, that's me," and name any you hate. The key opens after.</p>
<div class="grid">{body}</div>
<p class="foot">Beat 1 sits over her Bothwell kitchen, beat 2 over her Bothwell exterior, exactly as the render will. The caption under every pair is the same: three real Tarzana houses read on Redfin Sept 9, her "meeting in the middle" line once, a share ask, the number door.</p>
</main>'''
OUT.write_text(page)
print(OUT, len(page) // 1024, "KB; order written to HOOK-ROOM-11-KEY.json")
