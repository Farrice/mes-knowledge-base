#!/usr/bin/env python3
"""Jen Engine v2, weeks 1 and 2 (delivery Sun 2026-09-06 and Sun 2026-09-13).
Six finished posts in the Valley Native · Photo look: attract / position / convert each week.
Extends (imports) the September builders; never forks them:
  gen_photo.py  -> photo(), lockup(), serif(), hand(), body(), HEAD_PHOTO   (cards, 1080x1350)
  build_reel.py -> photo-motion reels (1080x1920, silent, serif over a moving photo)
Photos are placeholders from the cleared pool until her listing shoots land in Drive folder 01;
PHOTO-SWAP.md maps every frame to the shot that replaces it.

  python3 build_weeks.py            # cards + reels + captions + replies + swap map
  python3 build_weeks.py --no-video # skip ffmpeg (fast copy/QA loop)
"""
import glob, json, os, pathlib, shutil, subprocess, sys

HERE = pathlib.Path(__file__).parent
SEPT = HERE.parent / "2026-09-01-september-carousels"
sys.path.insert(0, str(SEPT))
from gen_photo import HEAD_PHOTO, FRAME, photo, lockup, serif, hand, body  # noqa: E402

IMG = SEPT / "img"
CHROME = sorted(glob.glob(os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]
NO_VIDEO = "--no-video" in sys.argv

# ------------------------------------------------------------------ the posts
# Every fact is dated in FACTS.md. Copy rules: her lowercase register, ellipses, one job per post,
# the door open at the end, her verbatim close. Luxury listing = Title Case hook, authority POV.

WEEKS = [
    {
        "folder": "week-of-2026-09-07",
        "message": (
            "hey babe, week 1 is in the folder: three posts, tue / thu / sat. open, post, done.\n"
            "if a line isn't you, reply here and it changes before it posts. nothing else to do 🤍"
        ),
        "posts": [
            {
                "id": "01-attract-what-850k-buys",
                "kind": "reel",
                "job": "attract",
                "day": "tue sept 8 · 7:30am",
                "beats": [
                    {"photo": "valley-street-01.jpg", "line": "what $850K actually<br>buys in the valley<br>this week.", "size": 96, "secs": 4, "zoom": "in",
                     "swap": "a valley-floor street or a front elevation from any listing shoot (folder 01)"},
                    {"photo": "california-bungalow-00.jpg", "line": "$869,000. tarzana.<br>3 bed. a 7,296 sq ft lot<br>with room for an ADU.", "size": 92, "secs": 4.5, "zoom": "out",
                     "swap": "an exterior from a listing shoot, single story"},
                    {"photo": "suburban-neighborhood-aerial-02.jpg", "line": "$850,000. lake balboa.<br>3 bed... a few blocks<br>from the lake.", "size": 92, "secs": 4.5, "zoom": "in",
                     "swap": "a drone frame from any listing shoot"},
                    {"photo": "front-door-house-00.jpg", "line": "$815,000. van nuys.<br>4 bed... and a pool.", "size": 96, "secs": 4, "zoom": "out",
                     "swap": "a backyard or pool frame from a listing shoot"},
                    {"photo": "jen-porch-vannuys.jpg", "line": "send me your number.<br>i&#8217;ll send you the three<br>i&#8217;d actually go see.", "size": 88, "hand": "my DMs are open &#8594;", "secs": 5, "zoom": "in",
                     "swap": "her at a front door (folder 03)"},
                ],
                "caption": (
                    "what $850K actually buys in the valley this week. three homes on the market right now (none of them mine):\n"
                    "\n"
                    "tarzana... $869,000. 3 bed, 1.5 bath, 1,136 sq ft on a 7,296 sq ft lot. room in the back for an ADU, that's a small second home you can build later.\n"
                    "lake balboa... $850,000. 3 bed, 1 bath, 1,126 sq ft, a few blocks from the lake.\n"
                    "van nuys... $815,000. 4 bed, 1.5 bath, 1,390 sq ft, and a pool.\n"
                    "\n"
                    "none of them are the finished, soft, modern house from the listing photos you keep saving. all three are a real front door at a real number... and the number is the part nobody posts.\n"
                    "\n"
                    "send me your number, buying or selling. i'll send you the three i'd actually go see this weekend, and what i'd check first at each one. or just say hi.\n"
                    "\n"
                    "i'm here for you. that's my job. i do this to protect you and your best interest.\n"
                    "\n"
                    "prices from the MLS, sept 2, 2026. they move.\n"
                    "#sanfernandovalley #tarzana #vannuys #lakebalboa #valleyrealestate #SFV"
                ),
                "reply": "a number arrives → saved reply 3 (looking / a number). an address arrives → saved reply 1.",
            },
            {
                "id": "02-position-not-the-number-that-matters",
                "kind": "card",
                "job": "position",
                "day": "thu sept 10 · 6:30pm",
                "slides": [
                    {"photo": "vannuys-blvd-2024.jpg", "pos": "50% 50%", "wash": 0.46,
                     "swap": "the boulevard at golden hour, or any wide valley frame (folder 01 or 02)",
                     "html": lambda: f'''{serif("6.66% this week.<br><em>not the number<br>that matters.</em>", size=88)}
    {hand("the one i ask for instead &#8594;", size=48)}'''},
                    {"photo": "sunlight-through-window-floor-00.jpg", "pos": "50% 50%", "wash": 0.52,
                     "swap": "an interior with light on the floor, from a listing shoot",
                     "html": lambda: f'''{hand("the question", size=52)}
    {serif("what rate did<br>your lender<br><em>actually</em> quote you?", size=84)}
    {body("not the one on the news. yours. the news number is an average of the whole country... your number is your credit, your down payment, your loan.", size=31)}
    {body("<b style='font-weight: 500;'>those two can sit half a point apart. half a point on $850,000 with 20% down is about $220 a month.</b>", size=29, width=720)}'''},
                    {"photo": "jen-porch-vannuys.jpg", "pos": "50% 0%", "wash": 0.44,
                     "swap": "her at a front door (folder 03)",
                     "html": lambda: f'''{serif("send me your<br>lender&#8217;s quote.", size=88)}
    {body("and we&#8217;ll look at a buydown together... that&#8217;s someone paying a little now so your rate is lower, for good or just the first couple of years.", size=31, width=720)}
    {body("i&#8217;m here for you. that&#8217;s my job.<br>i do this to protect you and your best interest.", size=29, width=720)}
    {hand("my DMs are open &#8594;", size=50)}'''},
                ],
                "caption": (
                    "6.66% is this week's 30-year average (freddie mac, aug 27). it's a headline, not your rate.\n"
                    "\n"
                    "what i ask for instead: the quote your lender actually gave you... your credit, your down payment, your loan. yours and the headline can sit half a point apart, and half a point on an $850,000 home with 20% down is about $220 a month, every month.\n"
                    "\n"
                    "then two questions. have you looked at a buydown... someone pays a little upfront so your rate is lower, either for good or just the first couple of years. and how we structure the loan so it works for you now, not for a version of you who makes more later.\n"
                    "\n"
                    "send me your lender's quote, or just the number you're working with. buying or selling, it's the same conversation.\n"
                    "\n"
                    "i'm here for you. that's my job. i do this to protect you and your best interest.\n"
                    "everything works out exactly the way it's supposed to.\n"
                    "\n"
                    "#mortgagerates #sanfernandovalley #SFV #valleyrealestate #shermanoaks"
                ),
                "reply": "a quote or a number arrives → saved reply 3. a 'hi' → saved reply 4.",
            },
            {
                "id": "03-convert-5421-bothwell",
                "kind": "reel",
                "job": "convert",
                "day": "sat sept 12 · 9:00am",
                "beats": [
                    {"photo": "sfv-aerial-nara.jpg", "line": "Three Structures.<br>One Lot. Tarzana.", "size": 100, "secs": 4, "zoom": "in",
                     "swap": "the Bothwell drone frame over the whole lot (folder 01)"},
                    {"photo": "sunlight-through-window-floor-00.jpg", "line": "The Living Room Opens<br>to the Pool<br>on Pocket Doors.", "size": 92, "secs": 4.5, "zoom": "out",
                     "swap": "Bothwell living room, pocket doors open"},
                    {"photo": "california-bungalow-00.jpg", "line": "882 Sq Ft Guest House.<br>Its Own Kitchen.<br>Not a Converted Garage.", "size": 84, "secs": 4.5, "zoom": "in",
                     "swap": "the Bothwell ADU exterior or its kitchen"},
                    {"photo": "jen-frontdoor.jpg", "line": "5421 Bothwell Rd.<br>$5,695,000.", "size": 100, "hand": "DM for a private showing &#8594;", "secs": 5, "zoom": "out",
                     "swap": "her at the Bothwell front door (folder 01 or 03)"},
                ],
                "caption": (
                    "Most New Construction in the Valley Is One Big Box. This Is Three Buildings on One Lot.\n"
                    "\n"
                    "5421 bothwell rd, tarzana. a 5,468 sq ft main house, an 882 sq ft guest house with its own kitchen, and a 238 sq ft rec room. 6,588 sq ft in total.\n"
                    "\n"
                    "white oak floors and real white oak cabinetry. taj mahal quartzite in the kitchen, thermador and sub-zero. venetian plaster in the office, the theater, and the primary bath. pocket doors from the living room straight out to the pool and a half basketball court. eleven-foot ceilings downstairs.\n"
                    "\n"
                    "$5,695,000. co-listed with marty azoulay, equity union.\n"
                    "\n"
                    "DM for a private showing.\n"
                    "\n"
                    "#tarzana #newconstruction #sanfernandovalley #luxuryrealestate #losangelesrealestate"
                ),
                "reply": "a showing request → reply in her own words, same evening; no saved reply needed (she does this daily).",
            },
        ],
    },
    {
        "folder": "week-of-2026-09-14",
        "message": (
            "week 2 is in the folder: three posts, tue / thu / sat. same as last week... open, post, done.\n"
            "the thursday one is about the october 15 insurance change, so it goes out on time. reply here if a line isn't you 🤍"
        ),
        "posts": [
            {
                "id": "04-attract-900k-two-zips",
                "kind": "reel",
                "job": "attract",
                "day": "tue sept 15 · 7:30am",
                "beats": [
                    {"photo": "vannuys-blvd-2024.jpg", "line": "$900K in sherman oaks.<br>$900K in van nuys.<br>same week.", "size": 90, "secs": 4.5, "zoom": "in",
                     "swap": "a wide valley frame from the drive (folder 02) or a drone frame (01)"},
                    {"photo": "california-bungalow-00.jpg", "line": "sherman oaks. $899,900.<br>1 bed. 1 bath.<br>a big lot and a plan.", "size": 88, "secs": 4.5, "zoom": "out",
                     "swap": "a small cottage exterior from any shoot"},
                    {"photo": "front-door-house-00.jpg", "line": "van nuys. $888,000.<br>4 bed. 2 bath.<br>1,576 square feet.", "size": 90, "secs": 4.5, "zoom": "in",
                     "swap": "a front elevation from a listing shoot"},
                    {"photo": "suburban-neighborhood-aerial-02.jpg", "line": "neither one is wrong.<br>they&#8217;re two different<br>ten-year plans.", "size": 90, "secs": 4.5, "zoom": "out",
                     "swap": "a drone frame from any shoot"},
                    {"photo": "jen-porch-vannuys.jpg", "line": "tell me the zip you<br>keep coming back to.<br>i&#8217;ll tell you what it costs.", "size": 84, "hand": "my DMs are open &#8594;", "secs": 5, "zoom": "in",
                     "swap": "her at a front door (folder 03)"},
                ],
                "caption": (
                    "$900K in sherman oaks vs. $900K in van nuys, same week, both on the market right now:\n"
                    "\n"
                    "sherman oaks... $899,900. 1 bed, 1 bath, on a big lot. you're buying the dirt and the zip, and building the house later.\n"
                    "van nuys... $888,000. 4 bed, 2 bath, 1,576 sq ft. you're buying the house, and the zip most people scroll past.\n"
                    "\n"
                    "neither one is wrong. they're two different ten-year plans. three things i'd want to know before you pick:\n"
                    "how long you're staying (under five years, the zip matters less than you think).\n"
                    "whether you'd ever build or add on (a lot is a plan, not a house).\n"
                    "what the insurance quote looks like at each address (i get it before we write, not in escrow).\n"
                    "\n"
                    "tell me the zip you keep coming back to. i'll tell you what it actually costs this month, buying or selling.\n"
                    "\n"
                    "i'm here for you. that's my job. i do this to protect you and your best interest.\n"
                    "\n"
                    "prices from the MLS, sept 2, 2026. they move.\n"
                    "#shermanoaks #vannuys #sanfernandovalley #valleyrealestate #SFV"
                ),
                "reply": "a zip or a number arrives → saved reply 3. an address → saved reply 1.",
            },
            {
                "id": "05-position-insurance-before-the-offer",
                "kind": "reel",
                "job": "position",
                "day": "thu sept 17 · 6:30pm",
                "beats": [
                    {"photo": "vannuys-blvd-2024.jpg", "line": "fully approved...<br>and the insurance quote<br>still moves your payment.", "size": 92, "secs": 4.5, "zoom": "in",
                     "swap": "a hillside or canyon street from the drive (folder 02)"},
                    {"photo": "california-bungalow-00.jpg", "line": "in the hills, i get<br>the quote <em>before</em><br>we write the offer.", "size": 96, "secs": 4.5, "zoom": "out",
                     "swap": "a hillside listing exterior (folder 01)"},
                    {"photo": "house-key-lock-00.jpg", "line": "october 15: the state&#8217;s<br>backup fire policy<br>goes up 29.1%.", "size": 92, "secs": 4.5, "zoom": "in",
                     "swap": "a front door or key frame from any shoot"},
                    {"photo": "jen-porch-vannuys.jpg", "line": "send me the street.<br>i&#8217;ll tell you what<br>i&#8217;d check first.", "size": 92, "hand": "my DMs are open &#8594;", "secs": 5, "zoom": "in",
                     "swap": "her at a front door (folder 03)"},
                ],
                "caption": (
                    "the insurance quote now comes before the offer, not once we're in escrow with the clock already running.\n"
                    "\n"
                    "on october 15, 2026 the california FAIR plan rises 29.1% on average. it's the state's backup fire policy, what you get when no regular company will cover the house. the increase is weighted to wildfire risk... hillside and canyon homes can see far more.\n"
                    "\n"
                    "the day your policy starts decides the rate. start before the 15th and you generally keep today's rate for the whole term.\n"
                    "\n"
                    "valley floor? most homes still get a regular company.\n"
                    "\n"
                    "selling a hillside home this fall? the same quote is the first thing your buyer's lender will ask about. worth knowing before the sign goes up.\n"
                    "\n"
                    "source: california dept of insurance, oct 15, 2026.\n"
                    "\n"
                    "my DMs are open... send me the address. or just the street, if that's as far as you've gotten. i'll tell you which paper i'd read first.\n"
                    "\n"
                    "i'm here for you. that's my job. i do this to protect you and your best interest.\n"
                    "approved and insured are two different yeses.\n"
                    "\n"
                    "#SFV #sanfernandovalleyrealtor #losangelesrealestate #shermanoaks #woodlandhills"
                ),
                "reply": "an address → saved reply 1, then 2 the next day. 'is this true for my house' → saved reply 2 shape.",
            },
            {
                "id": "06-position-tarzana-median-sellers",
                "kind": "card",
                "job": "position (seller side)",
                "day": "sat sept 19 · 9:00am",
                "slides": [
                    {"photo": "sfv-aerial-nara.jpg", "pos": "50% 50%", "wash": 0.46,
                     "swap": "a drone frame over tarzana or the valley floor (folder 01)",
                     "html": lambda: f'''{serif("tarzana sold for<br>14.5% less this july<br>than last july.", size=86)}
    {hand("and that&#8217;s still not your number &#8594;", size=46)}'''},
                    {"photo": "valley-street-01.jpg", "pos": "50% 50%", "wash": 0.50,
                     "swap": "a residential street from the drive (folder 02)",
                     "html": lambda: f'''{hand("why the median lies to sellers", size=50)}
    {serif("the median is<br>half the valley.<br>your house is one street.", size=80)}
    {body("a median is the middle of every sale, from a $650,000 fixer to a $19,999,000 estate. one big month at the top and the whole number moves.", size=31)}
    {body("<b style='font-weight: 500;'>what a home like yours closed for this summer, three streets over, is the number that decides your list price.</b>", size=29, width=720)}'''},
                    {"photo": "jen-frontdoor.jpg", "pos": "50% 20%", "wash": 0.42,
                     "swap": "her at a front door (folder 03)",
                     "html": lambda: f'''{serif("send me the street.<br>not the address...<br>just the street.", size=84)}
    {body("i&#8217;ll tell you what homes like yours actually closed for this summer, and what i&#8217;d list at. no pitch, no pressure.", size=31, width=720)}
    {body("i&#8217;m here for you. that&#8217;s my job.<br>i do this to protect you and your best interest.", size=29, width=720)}
    {hand("my DMs are open &#8594;", size=50)}'''},
                ],
                "caption": (
                    "tarzana's median sale price was $949,676 in july... 14.5% below last july. if you own here, that headline hit your phone too. it's still not your number.\n"
                    "\n"
                    "a median is the middle of every sale, from a $650,000 fixer to a $19,999,000 estate. a few big closings at the top one month and the whole number moves. your house didn't.\n"
                    "\n"
                    "the number that actually decides your list price: what homes like yours closed for this summer, three streets in every direction. same bed count, same era, same condition. that's a list of five or six addresses, not a percentage.\n"
                    "\n"
                    "send me the street. not the address, just the street. i'll pull what closed around you this summer and tell you what i'd list at. no pitch, no pressure... and if the honest answer is \"wait,\" i'll say that too.\n"
                    "\n"
                    "i'm here for you. that's my job. i do this to protect you and your best interest.\n"
                    "\n"
                    "source: redfin, all home types, july 2026 vs july 2025.\n"
                    "#tarzana #sanfernandovalley #valleyrealestate #homevalue #SFV"
                ),
                "reply": "a street or 'what's mine worth' → saved reply 2 (the seller one).",
            },
        ],
    },
]

SAVED_REPLIES = """saved replies · paste, add their name, send the same evening
(save these in instagram: profile → settings → business tools → saved replies)

1 · an address came in
got it... give me a day with the numbers and i'll come back with what i'd read first, what i'd ask the listing agent, and what we do next. we'll go from there.

1b · the next day, with the numbers
okay, i read it. here's what i'd read first, here's the one question i'd ask the listing agent, and here's what i'd do next. are you actually looking this fall, or just keeping an eye on things? either is fine... i just want to point you the right way.

2 · "what's mine worth" / a street came in
got it... give me a day. i'll pull what homes like yours actually closed for this summer, three streets in every direction, and come back with a range and what i'd list at. are you thinking this fall, or just curious? either is fine.

3 · "we're looking this fall" / a number or a zip came in
love that. two things so i point you the right way: the number you're working with, and the zip you keep coming back to. i'll send you the three i'd actually go see this weekend, and what i'd check first at each one. we'll go from there.

4 · just "hi"
hi! so glad you wrote. buying, selling, or just keeping an eye on things? any of those is a good reason to say hi. tell me where you're at and we'll go from there 🏡
"""

# ------------------------------------------------------------------ builders

def card_html(slide):
    src = (IMG / slide["photo"]).resolve().as_uri()
    return f'''<div style="{FRAME} background: #1E2430;">
{photo(src, pos=slide.get("pos", "50% 50%"), wash=slide.get("wash", 0.44))}
  <div style="position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 34px; padding: 120px 100px 200px;">
    {slide["html"]()}
  </div>
{lockup()}
</div>'''


def render_card(html_body, png):
    tmp = HERE / ".render_tmp"
    tmp.mkdir(exist_ok=True)
    page = HEAD_PHOTO.format(body=html_body)
    for tag in ('<script src="./support.js"></script>', "<x-dc>", "</x-dc>", "<helmet>", "</helmet>"):
        page = page.replace(tag, "")
    shim = tmp / (png.stem + ".html")
    shim.write_text(page)
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--window-size=1080,1350", "--virtual-time-budget=4000", f"--screenshot={png}", shim.as_uri()],
                   check=True, capture_output=True)


def build_reel(post, out_dir):
    spec = {"out": post["id"], "lockup": True, "out_dir": str(out_dir),
            "beats": [{k: v for k, v in b.items() if k != "swap"} for b in post["beats"]]}
    for b in spec["beats"]:
        b["size"] = fit(b["line"], b.get("size", 104))
    for b in spec["beats"]:
        b["photo"] = str((IMG / b["photo"]).resolve())
    spec_path = HERE / "reels" / f"{post['id']}.json"
    spec_path.parent.mkdir(exist_ok=True)
    spec_path.write_text(json.dumps(spec, indent=2))
    if NO_VIDEO:
        return
    r = subprocess.run([sys.executable, str(SEPT / "build_reel.py"), str(spec_path)], capture_output=True, text=True, cwd=SEPT)
    if r.returncode:
        print(r.stderr[-2000:]); raise SystemExit(f"reel failed: {post['id']}")
    print("  " + r.stdout.strip())


def main():
    swap_rows, copy_md = [], ["# jen engine v2 · weeks 1 and 2 · the copy\n",
                              "Operator file. Same words as the Drive folders; here so the fair-housing lint and the classifier can read them in one pass.\n"]
    for wk in WEEKS:
        wdir = HERE / wk["folder"]
        if wdir.exists() and not NO_VIDEO:
            shutil.rmtree(wdir)
        wdir.mkdir(parents=True, exist_ok=True)
        (wdir / "MESSAGE-to-jen.txt").write_text(wk["message"] + "\n")
        (wdir / "saved-replies.txt").write_text(SAVED_REPLIES)
        plan, captions = [], []
        copy_md.append(f"\n## {wk['folder']}\n\n> message: {wk['message']}\n")
        for p in wk["posts"]:
            print(f"{wk['folder']} / {p['id']}")
            plan.append(f"{p['day']} · {p['id'].split('-', 1)[1].replace('-', ' ')} · {p['kind']}")
            captions.append(f"=== {p['id']} · {p['day']} ===\n\n{p['caption']}\n")
            copy_md.append(f"\n### {p['id']} · {p['kind']} · {p['job']} · {p['day']}\n")
            if p["kind"] == "card":
                for i, s in enumerate(p["slides"], 1):
                    png = wdir / f"{p['id']}-{i}.png"
                    render_card(card_html(s), png)
                    print(f"  {png.name} ({png.stat().st_size // 1024} KB)")
                    swap_rows.append((wk["folder"], png.name, s["photo"], s["swap"]))
                    copy_md.append(f"- slide {i}: {_strip(s['html']())}")
            else:
                build_reel(p, wdir)
                for i, b in enumerate(p["beats"], 1):
                    swap_rows.append((wk["folder"], f"{p['id']}.mp4 · beat {i}", b["photo"], b["swap"]))
                    copy_md.append(f"- beat {i}: {_strip(b['line'])}" + (f" · *{_strip(b['hand'])}*" if b.get("hand") else ""))
            copy_md.append(f"\n**caption**\n\n{p['caption']}\n\n*reply routing: {p['reply']}*\n")
        (wdir / "day-plan.txt").write_text("\n".join(plan) + "\n")
        (wdir / "captions.txt").write_text("\n".join(captions))
    (HERE / "COPY-weeks-1-2.md").write_text("\n".join(copy_md))
    lines = ["# photo swap map\n",
             "Every frame below is a placeholder from the cleared pool. When her shoots land in Drive folder 01 (and her portraits in 03), drop the named shot into `img/` under the placeholder's filename, or point the beat at the new file, and re-run `python3 build_weeks.py`. Nothing else changes.\n",
             "| week | frame | placeholder now | what replaces it |", "|---|---|---|---|"]
    lines += [f"| {w} | {f} | `{ph}` | {sw} |" for w, f, ph, sw in swap_rows]
    (HERE / "PHOTO-SWAP.md").write_text("\n".join(lines) + "\n")
    shutil.rmtree(HERE / ".render_tmp", ignore_errors=True)
    print("done:", ", ".join(w["folder"] for w in WEEKS))


def fit(line, size, usable=880, em=0.46):
    """Largest size (<= requested) at which the longest copy-broken line fits the frame."""
    import html, re
    longest = max(len(html.unescape(re.sub(r"<[^>]+>", "", seg))) for seg in line.split("<br>"))
    return min(size, int(usable / (longest * em)))


def _strip(h):
    import html, re
    return html.unescape(re.sub(r"<[^>]+>", " ", h.replace("<br>", " "))).replace("  ", " ").strip()


if __name__ == "__main__":
    main()
