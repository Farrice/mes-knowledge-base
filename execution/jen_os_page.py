"""jen_os_page.py: regenerate The Valley OS artifact page (one-page readout of Jen's content system).
  python3 execution/jen_os_page_thumbs.py .tmp/valley-os/thumbs && python3 execution/jen_os_page.py .tmp/valley-os/thumbs .tmp/valley-os/the-valley-os.html
Then publish with the Artifact tool (url of the existing page keeps the link). Edit POSTS/MEMOS/HERS/OTHER tables as weeks ship.
"""
import base64, html, json, pathlib, re, sys

T = pathlib.Path(sys.argv[1])
LANE = pathlib.Path(__file__).resolve().parents[1]
WEEKS = LANE / "_active/clients/jen-listings/04-deliverables/2026-09-06-engine-v2-weeks-1-2"
OUT = pathlib.Path(sys.argv[2])

MISSING = []

def img(name):
    p = T / (name + ".jpg")
    if not p.exists():
        # a render that is not on this tree (e.g. edition-01 lives in a gitignored out/); show a labeled blank, never crash
        MISSING.append(name)
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4 5"><rect width="4" height="5" fill="#C9D4E2"/><text x="2" y="2.6" font-size=".35" text-anchor="middle" fill="#1E3A5F">not rendered</text></svg>'
        return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()
    return "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode()

def esc(s): return html.escape(s)

def captions(week):
    txt = (WEEKS / week / "captions.txt").read_text()
    out = {}
    for block in re.split(r"^=== ", txt, flags=re.M):
        if not block.strip(): continue
        head, _, body = block.partition(" ===\n")
        pid = head.split(" · ")[0].strip()
        out[pid] = body.strip()
    return out

def beats(pid):
    p = WEEKS / "reels" / f"{pid}.json"
    if not p.exists(): return []
    d = json.load(open(p))
    rows = []
    for b in d["beats"]:
        line = re.sub(r"<[^>]+>", " ", b["line"].replace("<br>", " / ")).replace("&#8217;", "’")
        hand = b.get("hand", "").replace("&#8594;", "→").replace("&#8217;", "’")
        rows.append((line, hand, b["secs"], b["zoom"], b["photo"]))
    return rows

CAP = {}
for w in ["week-of-2026-09-07", "week-of-2026-09-14", "week-of-2026-09-21"]:
    CAP.update(captions(w))
MSG = {w: (WEEKS / w / "MESSAGE-to-jen.txt").read_text().strip() for w in ["week-of-2026-09-07", "week-of-2026-09-14", "week-of-2026-09-21"]}
SAVED = (WEEKS / "week-of-2026-09-21" / "saved-replies.txt").read_text().strip()

POSTS = [
 ("week-of-2026-09-07", "Week 1 · drop Sun Sept 6 · re-run 9/2 through /jen (hook rule, voice bank, attract / connect / convert)", [
   ("01-attract-what-850k-buys", "attract", "reel · 25.5 s", "tue sept 8 · 7:30am", "you keep saving the finished ones.", "01-attract-what-850k-buys", ["sunlight-through-window-floor-00","valley-street-01","california-bungalow-00","suburban-neighborhood-aerial-02","front-door-house-00","jen-porch-vannuys"], "a number → saved reply 3 · an address → saved reply 1 · 'same' → her words"),
   ("02-connect-just-breathe", "connect", "card · 3 slides · her photos", "thu sept 10 · 6:30pm", "just breathe.", "02-connect-just-breathe-1", ["listing-03-pool (hers)","listing-02-living (hers)","jen-headshot-studio (hers, no type)"], "a number → saved reply 3 · 'same' → her words: 'send me the number when you're up'"),
   ("03-convert-5421-bothwell", "convert", "reel · 22 s", "sat sept 12 · 9:00am", "Most New Construction in the Valley Is One Big Box.", "03-convert-5421-bothwell", ["sfv-aerial-nara","california-bungalow-00","sunlight-through-window-floor-00","front-door-house-00","jen-frontdoor"], "a showing request → her own words, same evening · collab tag @myhousesellers"),
 ]),
 ("week-of-2026-09-14", "Week 2 · drop Sun Sept 13", [
   ("04-attract-900k-two-zips", "attract", "reel · 23 s", "tue sept 15 · 7:30am", "$900K in sherman oaks. $900K in van nuys. same week.", "04-attract-900k-two-zips", ["vannuys-blvd-2024","california-bungalow-00","front-door-house-00","suburban-neighborhood-aerial-02","jen-porch-vannuys"], "a zip or a number → saved reply 3 · an address → saved reply 1"),
   ("05-position-insurance-before-the-offer", "position", "reel · 18.5 s", "thu sept 17 · 6:30pm", "fully approved... and the insurance quote still moves your payment.", "05-position-insurance-before-the-offer", ["vannuys-blvd-2024","california-bungalow-00","house-key-lock-00","jen-porch-vannuys"], "an address → saved reply 1, then 2 the next day"),
   ("06-position-tarzana-median-sellers", "position", "card · 3 slides", "sat sept 19 · 9:00am", "tarzana sold for 14.5% less this july than last july.", "06-position-tarzana-median-sellers-1", ["sfv-aerial-nara","valley-street-01","jen-frontdoor"], "a street or 'what's mine worth' → saved reply 2"),
 ]),
 ("week-of-2026-09-21", "Week 3 · drop Sun Sept 20 · first full OS run", [
   ("07-attract-900k-woodland-hills-vs-reseda", "attract", "reel · 23 s", "tue sept 22 · 7:30am", "$900K in woodland hills. $900K in reseda. same week.", "07-attract-900k-woodland-hills-vs-reseda", ["suburban-neighborhood-aerial-02","california-bungalow-00","front-door-house-00","valley-street-01","jen-porch-vannuys"], "a zip or a number → saved reply 3 · an address → saved reply 1"),
   ("08-position-two-markets-one-street", "position", "card · 3 slides", "thu sept 24 · 6:30pm", "two markets on the same tarzana street.", "08-position-two-markets-one-street-1", ["sfv-aerial-nara","valley-street-01","jen-porch-vannuys"], "buyer's street → saved reply 3 shape · owner's street → saved reply 2"),
   ("09-connect-just-breathe", "connect", "card · 2 slides", "sat sept 26 · 9:00am", "just breathe.", "09-connect-just-breathe-1", ["palm-tree-sunset-city-02","jen-porch-vannuys"], "a number → saved reply 3 · 'same' → her words: 'send me the number when you're up'"),
 ]),
]

CARD_SLIDES = {
 "02-connect-just-breathe": 3, "06-position-tarzana-median-sellers": 3,
 "08-position-two-markets-one-street": 3, "09-connect-just-breathe": 2,
}

def post_card(pid, district, fmt, day, hook, thumb, photos, routing):
    cap = CAP.get(pid, "")
    b = beats(pid)
    slides = CARD_SLIDES.get(pid)
    gallery = ""
    if slides:
        gallery = '<div class="slides">' + "".join(f'<img src="{img(pid + "-" + str(i))}" alt="{esc(pid)} slide {i}">' for i in range(1, slides + 1)) + "</div>"
    else:
        gallery = f'<div class="slides"><img class="reelframe" src="{img(thumb)}" alt="{esc(pid)} first frame"><div class="reelnote">reel, first frame at 1.2 s · full file in the week folder</div></div>'
    beat_html = ""
    if b:
        beat_html = '<h4>the reel, beat by beat</h4><table class="beats"><thead><tr><th>on screen</th><th>hand line</th><th>secs</th><th>move</th></tr></thead><tbody>' + \
            "".join(f"<tr><td>{esc(l)}</td><td>{esc(h)}</td><td class=num>{s}</td><td>{z}</td></tr>" for l, h, s, z, _ in b) + "</tbody></table>"
    ph = "".join(f'<span class="ph">{esc(p)}</span>' for p in dict.fromkeys(photos))
    return f'''
<article class="post" id="{pid}">
  <div class="post-head">
    <span class="chip {district}">{district}</span>
    <span class="mono">{esc(day)}</span>
    <span class="mono dim">{esc(fmt)}</span>
    <span class="badge placeholder">placeholder photos</span>
  </div>
  <h3 class="hook">{esc(hook)}</h3>
  {gallery}
  <details>
    <summary>caption, script, routing</summary>
    <h4>caption, as it posts</h4>
    <pre class="caption">{esc(cap)}</pre>
    {beat_html}
    <h4>when someone writes back</h4>
    <p class="routing">{esc(routing)}</p>
    <h4>photos on these frames</h4>
    <p class="phlist">{ph}</p>
  </details>
</article>'''

weeks_html = ""
for folder, label, posts in POSTS:
    weeks_html += f'''
<section class="week">
  <div class="week-head"><h3>{esc(label)}</h3><span class="mono dim">{folder}</span></div>
  <blockquote class="msg"><span class="lbl">the text she gets</span>{esc(MSG[folder])}</blockquote>
  <div class="posts">{"".join(post_card(*p) for p in posts)}</div>
</section>'''

# ---------- her assets
MEMOS = [
 ("1 · a house you couldn't stop thinking about", "“lipstick remodel” · “you could feel the quality... the stone, the handles, the doors and the windows”", "Connect post 02 (copy ready, not built)", "unused on the grid"),
 ("2 · a buyer who panics at night", "“just breathe. take a step back. let's sleep on it” · lender quote · buydowns, “how we structure the loan”", "Week 1 post 02 (Connect) · Week 3 post 09 (the same post; week 3 gets a different Connect when it re-runs)", "used"),
 ("3 · what people tease you about saying", "“i'm here for you. that's my job. i do this to protect you and your best interest.” · “everything works out exactly the way it's supposed to” · “this, this, and this, and we'll go from there”", "the close: week 1 once (post 02) · weeks 2–3 still 6 of 6 until re-run · recap habit: saved replies", "bank, drawn once a week (stamp-lint enforces)"),
 ("4 · what makes you cringe", "“top producer” · “30 years in business” · credentials on camera", "rule: no credentials anywhere", "used as a rule"),
 ("5 · the most impressive home", "“i've sold an $80 million home... a regular three-bedroom on malibu beach” · “i am a sucker for a view of skylines”", "Connect post 04 (copy ready) · photo taste for the look", "unused on the grid"),
]
HERS = [
 ("jen-headshot-studio", "studio headshot 2048²", "Edition 01 cover"),
 ("jen-closing-day-selfie", "closing day, three faces", "none: no type-safe crop"),
 ("jen-client-kitchen-sold", "kitchen, family, SOLD sign", "none: faces in the type zone"),
 ("jen-client-couple-dogs-selfie", "clients + dogs, 414px", "none: inset only"),
 ("jen-client-family-selfie", "clients, 414px", "none: inset only"),
 ("jen-client-newhomeowner-kid", "new homeowner, 414px", "none: inset only"),
 ("jen-client-pool-house", "pool house, 414px", "none: inset only"),
 ("listing-01-exterior", "5421 Bothwell exterior", "Edition 01 frame 3"),
 ("listing-02-living", "Bothwell living, pocket doors", "Edition 01 frame 3 inset"),
 ("listing-03-pool", "Bothwell pool at dusk", "Edition 01 frames 3, 5"),
 ("listing-04-kitchen", "Bothwell kitchen", "Connect 02 plan"),
 ("listing-home-gym-pool", "older listing gym/pool", "none: would mislead"),
]
POOL_USED = {
 "vannuys-blvd-2024": "posts 02, 04, 05", "sunlight-through-window-floor-00": "posts 02, 03", "jen-porch-vannuys": "posts 01, 02, 04, 05, 07, 08, 09 (her, 2025 grid)",
 "sfv-aerial-nara": "posts 03, 06, 08 (1930s archive aerial)", "california-bungalow-00": "posts 01, 03, 04, 05, 07", "front-door-house-00": "posts 01, 04, 07",
 "valley-street-01": "posts 01, 06, 07, 08", "suburban-neighborhood-aerial-02": "posts 01, 04, 07", "jen-frontdoor": "posts 03, 06 (360px, her reel cover)",
 "house-key-lock-00": "post 05", "palm-tree-sunset-city-02": "post 09", "jen-portrait": "none (280px)", "apartment-building-dusk-03": "none",
 "vannuys-street-scene": "none", "vannuys-valerio-2024": "none",
}

hers_html = "".join(f'<figure><img src="{img("hers-"+f)}" alt="{esc(d)}"><figcaption><b>{esc(d)}</b><span class="{ "ok" if not u.startswith("none") else "no"}">{esc(u)}</span></figcaption></figure>' for f, d, u in HERS)
pool_html = "".join(f'<figure><img src="{img("pool-"+f)}" alt="{esc(f)}"><figcaption><b>{esc(f)}</b><span class="{ "ok" if not u.startswith("none") else "no"}">{esc(u)}</span></figcaption></figure>' for f, u in POOL_USED.items())
memo_rows = "".join(f"<tr><td>{esc(a)}</td><td>{esc(b)}</td><td>{esc(c)}</td><td><span class='state'>{esc(d)}</span></td></tr>" for a, b, c, d in MEMOS)

OTHER = [
 ("Register ladder (calm-warm lowercase · Quiet Flex Title Case on luxury)", "used", "post 03 runs Title Case; every other caption lowercase"),
 ("Palette navy / steel / cream, no orange", "used", "cards and editions both hold it"),
 ("Her listings: 5421 Bothwell", "used", "post 03 + Edition 01 frame 3"),
 ("Her listings: 5200 Armida · 1654 Moonseed · 6853 Willis", "banked", "shoot sheets exist; Armida status unconfirmed"),
 ("Saved replies (4)", "built, unmeasured", "in every week folder; no DM count has come back yet"),
 ("Bio line “Your Valley agent. $800K and up, buying or selling.”", "not done", "her bio still reads “raver vibes, boy mom life”"),
 ("Pinned post + the valley file (three one-pagers)", "not done", "ENGINE-V2 §9 names it; nothing rendered"),
 ("Stories", "none", "Coffee & Contracts runs stories daily; we have zero"),
 ("Her Insights (saves, reach, follows)", "none", "pulse reads public views/likes/comments only"),
 ("Scheduling access (Meta Business Suite)", "none", "she posts the files by hand until then"),
 ("Her listing photography → Drive folder 01", "none", "the single biggest reason the cards look generic"),
 ("A thumbs-up from Jen on anything since Sept 2", "none", "two rebuilds without her in the loop"),
]
other_rows = "".join(f"<tr><td>{esc(a)}</td><td><span class='state {b.split(',')[0].replace(' ','-')}'>{esc(b)}</span></td><td>{esc(c)}</td></tr>" for a, b, c in OTHER)

ED = [("ed01-01-cover","cover"),("ed01-02-laidrey","Laidrey, 7am"),("ed01-03-bothwell","Three Buildings. One Lot."),("ed01-04-what-869k-buys","What $869K Buys Here."),("ed01-05-close","Send Me the Street.")]
EDS = [("ed01-S2-moment-cover","moment"),("ed01-S3-stack-cover","stack"),("ed01-S4-guide-cover","guide"),("ed01-S5-urban-cover","urban"),("ed01-S6-initial-cover","big initial")]
ed_html = "".join(f'<figure><img src="{img(f)}" alt="{esc(c)}"><figcaption>{esc(c)}</figcaption></figure>' for f, c in ED)
eds_html = "".join(f'<figure><img src="{img(f)}" alt="{esc(c)}"><figcaption>{esc(c)}</figcaption></figure>' for f, c in EDS)

STAGES = [
 ("0 · Load", "Seven files, in order, before a word is written: the operating doc, the mix, the vault, her voice profile, the calibration log, the client card, the last pulse.", "/jen step 0 · LOAD: 7/7", "us"),
 ("1 · Read", "What the account moved on last month decides this week's three slots. Shares come from the extractions, never from taste.", "CONTENT-MIX.md · pulse · outlier audit", "us"),
 ("2 · Research", "Redfin comps and market pages, Freddie Mac rates, CA Dept of Insurance. Read the day of the build, dated, labeled. The realism gate on every topic.", "FACTS.md · RESEARCH-PACK.md", "us"),
 ("3 · Write", "One pen, her seat first. Every hook opens on her or the reader; the number or the house is beat 2. Her verbatim lines are a bank drawn once a week, never a stamp.", "build_weeks.py WEEKS list", "us"),
 ("4 · Amplify", "Six seats critique, one pen integrates: Alyssa, Luke Iha, Sam Parr, Kallaway, Georgi, then Jen-as-herself with the veto. Plain words with punch.", "AMPLIFY.md in the week folder", "us"),
 ("5 · Check", "Fair-housing lint (hard). Prose classifier (nudge). Stamp-lint: a sentence in two posts of one week fails the week (hard).", "fair_housing_lint.py · prose_classifier.py · jen_stamp_lint.py", "script"),
 ("6 · Render", "Cards and photo-motion reels from one generator family. Photos are placeholders until hers arrive.", "week-of-YYYY-MM-DD/ · PHOTO-SWAP.md", "script"),
 ("7 · Deliver", "This page, then the Sunday folder: files, one text to her, captions, the day plan with story slide, collab tag and first comment, the saved replies.", "Drive · Jen · Content Drop / 04", "us"),
 ("Her two moves", "A thumbs-up on the preview (30 seconds). Same-evening replies from the saved replies. Nothing else.", "iMessage · Instagram", "Jen"),
 ("8 · Learn", "Monday pulse of public numbers. First of the month: outlier audit, her four numbers into the funnel, vault rows, one line back to her.", "jen_pulse.py · jen-outlier-audit.md · FUNNEL-MATH.md", "us"),
]
stages_html = "".join(f'''<li><span class="who {w.replace(" ","-")}">{esc(w)}</span><h4>{esc(n)}</h4><p>{esc(d)}</p><code>{esc(f)}</code></li>''' for n, d, f, w in STAGES)

PAGE = f'''<title>The Valley OS</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Jost:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root{{--ink:#1E3A5F;--steel:#4C7CA8;--cream:#F7F5F2;--paper:#FFFFFF;--rule:#C9D4E2;--slate:#5B6472;--text:#1B2431;--good:#2F7D5B;--warn:#9A6B1F;--bad:#9B3F3F;--chip-attract:#DCE7F2;--chip-position:#E7EEF5;--chip-convert:#EAE5DA;--chip-connect:#E4EDE6;--shadow:0 1px 2px rgba(30,58,95,.08),0 8px 24px rgba(30,58,95,.06)}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--ink:#DCE6F2;--steel:#8FB3D6;--cream:#141B26;--paper:#1C2532;--rule:#2B3746;--slate:#9AA7B8;--text:#E9EEF4;--good:#6FBF95;--warn:#D8A54A;--bad:#E07A7A;--chip-attract:#243A52;--chip-position:#22313F;--chip-convert:#3A3428;--chip-connect:#22382C;--shadow:none}}}}
:root[data-theme="dark"]{{--ink:#DCE6F2;--steel:#8FB3D6;--cream:#141B26;--paper:#1C2532;--rule:#2B3746;--slate:#9AA7B8;--text:#E9EEF4;--good:#6FBF95;--warn:#D8A54A;--bad:#E07A7A;--chip-attract:#243A52;--chip-position:#22313F;--chip-convert:#3A3428;--chip-connect:#22382C;--shadow:none}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--cream);color:var(--text);font-family:Jost,system-ui,sans-serif;font-weight:400;line-height:1.5;font-size:16px}}
a{{color:var(--steel)}}
.mono{{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:.82rem;color:var(--ink)}}
.dim{{color:var(--slate)}}
h1,h2,h3{{font-family:"Playfair Display",Georgia,serif;font-weight:400;color:var(--ink);text-wrap:balance;margin:0}}
h1{{font-size:clamp(2.2rem,4.5vw,3.4rem);line-height:1.05}}
h2{{font-size:1.9rem;line-height:1.15}}
h3{{font-size:1.25rem}}
h4{{font-family:Jost,sans-serif;font-weight:600;font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--slate);margin:1.4rem 0 .5rem}}
nav{{position:sticky;top:0;z-index:5;background:var(--cream);border-bottom:1px solid var(--rule);display:flex;gap:1.4rem;padding:.8rem 1.4rem;overflow-x:auto;font-size:.85rem;font-weight:500;letter-spacing:.04em}}
nav a{{color:var(--ink);text-decoration:none;white-space:nowrap}} nav a:hover,nav a:focus-visible{{color:var(--steel);outline:none;text-decoration:underline}}
main{{max-width:1120px;margin:0 auto;padding:2.5rem 1.4rem 5rem}}
header.hero{{display:grid;grid-template-columns:1.2fr .8fr;gap:2.5rem;align-items:end;padding:1rem 0 2.5rem;border-bottom:1px solid var(--rule)}}
.hero p{{max-width:62ch;font-size:1.05rem;color:var(--slate)}}
.hero .stat{{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}}
.stat div{{background:var(--paper);border:1px solid var(--rule);padding:.9rem 1rem;box-shadow:var(--shadow)}}
.stat b{{display:block;font-family:"Playfair Display",serif;font-weight:400;font-size:1.7rem;color:var(--ink);font-variant-numeric:tabular-nums}}
.stat span{{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:var(--slate)}}
section.block{{padding:3rem 0;border-bottom:1px solid var(--rule)}}
.lede{{max-width:66ch;color:var(--slate);margin:.6rem 0 1.6rem}}
ol.read{{margin:0;padding:0;list-style:none;display:grid;gap:1rem;max-width:78ch}}
ol.read li{{background:var(--paper);border-left:3px solid var(--steel);padding:1rem 1.2rem;box-shadow:var(--shadow)}}
ol.read b{{color:var(--ink)}}
ul.stages{{list-style:none;margin:0;padding:.5rem 0 1rem;display:grid;grid-auto-flow:column;grid-auto-columns:minmax(230px,1fr);gap:.9rem;overflow-x:auto}}
ul.stages li{{background:var(--paper);border:1px solid var(--rule);padding:1rem 1rem 1.1rem;position:relative;box-shadow:var(--shadow)}}
ul.stages li::after{{content:"→";position:absolute;right:-.85rem;top:1rem;color:var(--steel);font-size:1.1rem}}
ul.stages li:last-child::after{{content:"↺";right:.8rem;top:.6rem}}
ul.stages h4{{margin:.4rem 0 .3rem;color:var(--ink);letter-spacing:0;text-transform:none;font-family:"Playfair Display",serif;font-weight:400;font-size:1.15rem}}
ul.stages p{{font-size:.9rem;margin:0 0 .6rem;color:var(--text)}}
ul.stages code{{font-family:"IBM Plex Mono",monospace;font-size:.72rem;color:var(--slate);display:block}}
.who{{font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;padding:.15rem .45rem;border:1px solid var(--rule);color:var(--slate)}}
.who.Jen{{border-color:var(--steel);color:var(--steel)}}
.week{{margin-top:2.2rem}}
.week-head{{display:flex;align-items:baseline;gap:1rem;flex-wrap:wrap;margin-bottom:.6rem}}
.msg{{margin:0 0 1.2rem;background:var(--paper);border:1px solid var(--rule);padding:.9rem 1.1rem;font-size:.95rem;max-width:70ch;position:relative}}
.msg .lbl{{display:block;font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;color:var(--slate);margin-bottom:.3rem}}
.posts{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.2rem}}
.post{{background:var(--paper);border:1px solid var(--rule);padding:1rem 1rem 1.1rem;box-shadow:var(--shadow);display:flex;flex-direction:column;gap:.6rem}}
.post-head{{display:flex;flex-wrap:wrap;gap:.5rem .8rem;align-items:center}}
.chip{{font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;padding:.2rem .55rem;color:var(--ink);font-weight:600}}
.chip.attract{{background:var(--chip-attract)}} .chip.position{{background:var(--chip-position)}} .chip.convert{{background:var(--chip-convert)}} .chip.connect{{background:var(--chip-connect)}}
.badge{{font-size:.68rem;letter-spacing:.06em;padding:.15rem .45rem;border:1px dashed var(--warn);color:var(--warn);margin-left:auto}}
.hook{{font-size:1.15rem;line-height:1.3}}
.slides{{display:grid;grid-template-columns:repeat(3,1fr);gap:.4rem}}
.slides img{{width:100%;aspect-ratio:4/5;object-fit:cover;display:block;border:1px solid var(--rule)}}
.slides .reelframe{{grid-column:1/2;aspect-ratio:9/16}}
.reelnote{{grid-column:2/4;font-size:.8rem;color:var(--slate);align-self:end}}
details{{border-top:1px solid var(--rule);padding-top:.5rem}}
summary{{cursor:pointer;font-weight:500;color:var(--steel);font-size:.9rem;list-style:none}} summary::-webkit-details-marker{{display:none}} summary::before{{content:"+ ";}} details[open] summary::before{{content:"– ";}}
summary:focus-visible{{outline:2px solid var(--steel);outline-offset:2px}}
pre.caption{{white-space:pre-wrap;font-family:Jost,sans-serif;font-size:.92rem;line-height:1.5;margin:0;background:var(--cream);padding:.9rem 1rem;border:1px solid var(--rule);max-width:64ch}}
table{{border-collapse:collapse;width:100%;font-size:.88rem}}
th{{text-align:left;font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--slate);font-weight:600;padding:.4rem .5rem;border-bottom:1px solid var(--rule)}}
td{{padding:.5rem .5rem;border-bottom:1px solid var(--rule);vertical-align:top}}
td.num{{font-variant-numeric:tabular-nums;font-family:"IBM Plex Mono",monospace;font-size:.8rem}}
.routing{{margin:0;font-size:.9rem}}
.ph{{font-family:"IBM Plex Mono",monospace;font-size:.72rem;background:var(--cream);border:1px solid var(--rule);padding:.1rem .4rem;margin:0 .3rem .3rem 0;display:inline-block}}
.tablewrap{{overflow-x:auto}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:.8rem;margin-top:.8rem}}
figure{{margin:0}} figure img{{width:100%;aspect-ratio:1;object-fit:cover;display:block;border:1px solid var(--rule)}}
.ed figure img{{aspect-ratio:4/5}}
figcaption{{font-size:.76rem;line-height:1.35;margin-top:.35rem;color:var(--slate)}} figcaption b{{display:block;color:var(--text);font-weight:500}}
figcaption .ok{{color:var(--good)}} figcaption .no{{color:var(--bad)}}
.state{{font-size:.7rem;letter-spacing:.08em;text-transform:uppercase;padding:.15rem .45rem;border:1px solid var(--rule);white-space:nowrap}}
.state.used{{color:var(--good);border-color:var(--good)}} .state.none,.state.not-done{{color:var(--bad);border-color:var(--bad)}} .state.banked,.state.built{{color:var(--warn);border-color:var(--warn)}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:2rem}}
.filemap{{font-family:"IBM Plex Mono",monospace;font-size:.78rem;line-height:1.7;color:var(--slate);background:var(--paper);border:1px solid var(--rule);padding:1rem 1.2rem;overflow-x:auto}}
.filemap b{{color:var(--ink);font-weight:500}}
@media (max-width:820px){{header.hero,.two{{grid-template-columns:1fr}} .slides{{grid-template-columns:repeat(3,1fr)}}}}
@media (prefers-reduced-motion:no-preference){{summary{{transition:color .15s}}}}
</style>

<nav>
  <a href="#read">The honest read</a><a href="#machine">The machine</a><a href="#month">The month</a><a href="#edition">Edition 01</a><a href="#assets">Her assets</a><a href="#gates">Gates</a><a href="#gaps">Against Coffee &amp; Contracts</a><a href="#files">Files</a>
</nav>
<main>
<header class="hero">
  <div>
    <h1>The Valley OS</h1>
    <p>Jen's content system as of Sept 2, 2026, after the reset to one spine: how it runs, the nine posts it has produced (week 1 re-run through the new order), which of her own assets it uses, and the places it is not working yet. Every frame on this page is the actual render.</p>
  </div>
  <div class="stat">
    <div><b>9</b><span>posts built, 3 weeks</span></div>
    <div><b>0</b><span>posted or approved by Jen</span></div>
    <div><b>5 / 12</b><span>of her photos in use</span></div>
  </div>
</header>

<section class="block" id="read">
  <h2>The honest read</h2>
  <p class="lede">Why it doesn't feel like a system that works, even though every gate passes.</p>
  <ol class="read">
    <li><b>We ship the system, not the posts.</b> Coffee &amp; Contracts shows a post, then a calendar, then a price. Tonight produced funnel math, amendments, a vault, and a contract before anything you could flick through. This page is the first place the posts sit side by side.</li>
    <li><b>The cards cannot look like her yet.</b> Every weekly frame runs on a CC0 pool photo or a 360-pixel image of Jen from her old grid. Her twelve real photos are only in Edition 01. Drive folder 01 is still empty. The generator is not the ceiling; the inputs are.</li>
    <li><b>Two generators, two looks.</b> The weekly cards (centered serif over a full-bleed photo) and the editions (six Canva grammars) are not one wardrobe. Whichever you prefer from the other session should become the only one.</li>
    <li><b>Her close was in nine of nine captions.</b> “i'm here for you. that's my job.” is her best line, and it had become a template. Fixed Sept 2 for week 1 (it appears once, on the Connect post; the attract post closes “i've got you,” the listing closes on the showing); a stamp-lint now fails any week where a sentence repeats across posts. Weeks 2 and 3 still carry the old stamp until they go through the same door.</li>
    <li><b>Every week-1 hook now opens on her or on you, not on the house.</b> Her account's own numbers: life-first hooks beat property-first two to one; every bottom-quartile post led with the property. “you keep saving the finished ones” before the three prices; “just breathe” before the buydown; the one-big-box thesis before the address.</li>
    <li><b>Three of five voice memos are unused on the grid.</b> Lipstick remodel, the $80M beach house, the skyline: written, not built. The two memos that are used carry the same two lines.</li>
    <li><b>No Jen since “hated it.”</b> Two rebuilds, zero thumbs-up. The system is optimized for operator legibility, not for the two humans who decide: your verdict and her yes.</li>
    <li><b>Zero stories, zero bio change, zero pinned post, zero Insights.</b> Those are the parts of Coffee &amp; Contracts that make the feed feel alive and measurable. We built the feed posts and the reply layer and stopped.</li>
  </ol>
</section>

<section class="block" id="machine">
  <h2>The machine</h2>
  <p class="lede">One front door, <code>/jen</code>, nine steps in a fixed order with a receipt after each. Jen appears in exactly one of them. Reset Sept 2: the three competing engines are archived; this is the only order.</p>
  <ul class="stages">{stages_html}</ul>
</section>

<section class="block" id="month">
  <h2>The month, as she would see it</h2>
  <p class="lede">Three drops, nine posts. Open any card for the caption as it posts, the reel beat by beat, and what happens when someone writes back. The dashed badge means the photos are placeholders from the cleared pool.</p>
  {weeks_html}
  <h4>the saved replies she pastes</h4>
  <pre class="caption">{esc(SAVED)}</pre>
</section>

<section class="block" id="edition">
  <h2>Edition 01, the other lane's surface</h2>
  <p class="lede">The Valley · Tarzana · Edition 01 on the Local Gem grammar, plus one cover per other grammar. Her headshot and her Bothwell photos, researched Tarzana facts, awaiting your verdict.</p>
  <div class="grid ed">{ed_html}</div>
  <h4>the other five grammars</h4>
  <div class="grid ed">{eds_html}</div>
</section>

<section class="block" id="assets">
  <h2>Her assets: used, unused</h2>
  <p class="lede">What we have of hers, and where each piece actually landed.</p>
  <h4>her five voice memos (2026-09-01)</h4>
  <div class="tablewrap"><table><thead><tr><th>memo</th><th>her lines</th><th>where it went</th><th>state</th></tr></thead><tbody>{memo_rows}</tbody></table></div>
  <h4>her twelve photos</h4>
  <div class="grid">{hers_html}</div>
  <h4>the placeholder pool the weekly cards actually run on</h4>
  <div class="grid">{pool_html}</div>
  <h4>everything else of hers</h4>
  <div class="tablewrap"><table><thead><tr><th>asset</th><th>state</th><th>note</th></tr></thead><tbody>{other_rows}</tbody></table></div>
</section>

<section class="block" id="gates">
  <h2>Gates and receipts</h2>
  <div class="tablewrap"><table><thead><tr><th>check</th><th>result</th><th>what it means</th></tr></thead><tbody>
  <tr><td>Fair-housing lint, all nine captions and frames</td><td><span class="state used">pass</span></td><td>no steering language, no protected-class targeting</td></tr>
  <tr><td>Stamp-lint, week 1 (re-run)</td><td><span class="state used">pass</span></td><td>no sentence appears in two posts; the close once, “i've got you” once, no “my DMs are open” tail</td></tr>
  <tr><td>Stamp-lint, weeks 2–3 (not yet re-run)</td><td><span class="state none">fail</span></td><td>the close in 6 of 6; “my DMs are open” in 6 of 6; queued for the same door</td></tr>
  <tr><td>Prose classifier, week 3 captions</td><td><span class="state used">clean 0/10</span></td><td>after removing three “here's what” lead-ins and two repeated ask tails</td></tr>
  <tr><td>Facts ledger</td><td><span class="state used">17 rows</span></td><td>every number read from Redfin, Freddie Mac, or CDI on the build day, with a re-check date</td></tr>
  <tr><td>Realism gate</td><td><span class="state used">applied</span></td><td>condo and light-rail topics dead; insurance, rates, “just breathe” pass</td></tr>
  <tr><td>Type on a face</td><td><span class="state banked">1 fixed</span></td><td>week 3 card 08-3 re-pointed after the headline landed on her face</td></tr>
  <tr><td>Jen-as-herself seat</td><td><span class="state banked">3 lines flagged</span></td><td>the 11pm scene, “touch three things,” the $80M line: need her thumbs-up</td></tr>
  <tr><td>Public pulse, Sept 2</td><td><span class="state used">2,660 followers</span></td><td>median 2,642 views · 125 likes · 15 comments across her last 12 reels</td></tr>
  <tr><td>Outlier audit</td><td><span class="state used">done</span></td><td>life-first hooks 2× property-first; the one real-estate breakout was comfort-shaped; zero local content</td></tr>
  <tr><td>Finalize composite</td><td><span class="state banked">7.33 marginal</span></td><td>honest: placeholders and unverified funnel rates cap it</td></tr>
  </tbody></table></div>
</section>

<section class="block" id="gaps">
  <h2>Against Coffee &amp; Contracts</h2>
  <div class="two">
    <div><h4>they have, we match or beat</h4>
      <div class="tablewrap"><table><tbody>
      <tr><td>Weekly template drop</td><td>Sunday folder, finished posts, her streets, dated facts</td></tr>
      <tr><td>Captions with local nouns</td><td>captions with verified local numbers and her words</td></tr>
      <tr><td>Reel scripts</td><td>photo-motion reels, beats written, rendered</td></tr>
      <tr><td>“5 minutes to post”</td><td>thumbs-up + reply DMs; we post for her once we have access</td></tr>
      <tr><td>Analytics dashboard</td><td>Monday pulse, monthly outlier audit</td></tr>
      </tbody></table></div>
    </div>
    <div><h4>they have, we have not built</h4>
      <div class="tablewrap"><table><tbody>
      <tr><td>Stories, daily</td><td><span class="state none">none</span></td></tr>
      <tr><td>Lead magnet / the valley file</td><td><span class="state none">not rendered</span></td></tr>
      <tr><td>Bio and link-in-bio</td><td><span class="state none">untouched</span></td></tr>
      <tr><td>Two style options shown to her</td><td><span class="state none">not yet</span></td></tr>
      <tr><td>Insights-based numbers</td><td><span class="state none">no access</span></td></tr>
      <tr><td>Trending audio at post time</td><td><span class="state banked">optional</span></td></tr>
      </tbody></table></div>
    </div>
  </div>
</section>

<section class="block" id="files">
  <h2>Where everything lives</h2>
  <div class="filemap">
<b>_active/clients/jen-listings/</b><br>
&nbsp;&nbsp;06-system/ENGINE-V2.md &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the operating doc (four districts, rhythm, scoreboard)<br>
&nbsp;&nbsp;06-system/VAULT.md &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;every asset by district, with status<br>
&nbsp;&nbsp;06-system/FUNNEL-MATH.md &nbsp;&nbsp;&nbsp;&nbsp;operator only; placeholders until her four numbers<br>
&nbsp;&nbsp;06-system/pulse/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weekly public numbers (jen_pulse.py)<br>
&nbsp;&nbsp;06-system/valley-editions/ &nbsp;&nbsp;DESIGN.md · CANVA-GRAMMAR.md · editions.py · photos/jen/<br>
&nbsp;&nbsp;04-deliverables/2026-09-06-engine-v2-weeks-1-2/ &nbsp;build_weeks.py · FACTS.md · PHOTO-SWAP.md · week-of-*/<br>
&nbsp;&nbsp;04-deliverables/connect-posts-01/COPY.md &nbsp;four Connect posts, three still unbuilt<br>
&nbsp;&nbsp;04-deliverables/jen-outlier-audit.md<br>
<b>skills/alyssa-stalker-agent-content-playbook/</b> &nbsp;/alyssa-stalker-outlier-audit · -hook-reframe · -comfort-content-engine · -content-mix-planner<br>
<b>execution/jen_pulse.py</b>
  </div>
</section>
</main>'''

OUT.write_text(PAGE)
print(len(PAGE) // 1024, "KB")
