#!/usr/bin/env python3
"""
Client-facing share page for "Same Door".

BINDING: zero operator language. Nothing here diagnoses her feed or her results.
Diagnosis lives in ../../OPERATOR-NOTES.md.

    python3 share_page.py    # -> concept.html
"""
import base64
import pathlib
import subprocess

HERE = pathlib.Path(__file__).parent
PNG = HERE / "png"
OUT = HERE / "concept.html"
TMP = HERE / ".sharethumbs"


def img(stem, width=1180, q=80):
    src = next(PNG.glob(stem + "*.png"))
    TMP.mkdir(exist_ok=True)
    dst = TMP / (src.stem + ".jpg")
    subprocess.run(["sips", "-Z", str(width), "-s", "format", "jpeg",
                    "-s", "formatOptions", str(q), str(src), "--out", str(dst)],
                   check=True, capture_output=True)
    return "data:image/jpeg;base64," + base64.b64encode(dst.read_bytes()).decode()


def plate(stem, caption=None):
    cap = '<figcaption>%s</figcaption>' % caption if caption else ""
    return ('<figure class="plate"><img src="%s" alt="" loading="lazy">%s</figure>'
            % (img(stem), cap))


CSS = """
:root{
  --paper:#FBFCFD; --ink:#174579; --band:#0F2D4F; --muted:#687994;
  --hair:#DCE3EC; --accent:#4A6E96; --plate:#EFF3F8; --onband:#EAF0F7;
  --bandmuted:rgba(234,240,247,0.74); --bandhair:rgba(234,240,247,0.26);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --paper:#0B1926; --ink:#E4EDF6; --band:#102636; --muted:#9FB3C8;
    --hair:#22364B; --accent:#9BB8D6; --plate:#132434; --onband:#EAF0F7;
    --bandmuted:rgba(234,240,247,0.74); --bandhair:rgba(234,240,247,0.22);
  }
}
:root[data-theme="dark"]{
  --paper:#0B1926; --ink:#E4EDF6; --band:#102636; --muted:#9FB3C8;
  --hair:#22364B; --accent:#9BB8D6; --plate:#132434; --onband:#EAF0F7;
  --bandmuted:rgba(234,240,247,0.74); --bandhair:rgba(234,240,247,0.22);
}

*{box-sizing:border-box;}
body{
  margin:0; background:var(--paper); color:var(--ink);
  font-family:'Jost','Futura','Avenir Next',system-ui,sans-serif;
  font-size:18px; line-height:1.62; -webkit-font-smoothing:antialiased;
}
.si{font-family:'Bodoni Moda',Didot,Georgia,serif; font-style:italic; font-weight:500;
    color:var(--accent);}
.wrap{max-width:940px; margin:0 auto; padding:0 28px;}
.caps{font-weight:500; letter-spacing:0.24em; text-transform:uppercase; font-size:12px;}
.num{font-family:'Bodoni Moda',Didot,Georgia,serif; font-weight:500;
     font-variant-numeric:tabular-nums;}

.open{background:var(--band); color:var(--onband); padding:92px 0 84px;}
.open .caps{color:var(--bandmuted);}
.open .rule{border-bottom:1px solid var(--bandhair); padding-bottom:18px;
            margin-bottom:60px; display:flex; justify-content:space-between;
            align-items:baseline; gap:20px; flex-wrap:wrap;}
.open h1{font-size:clamp(36px,6vw,66px); line-height:1.11; letter-spacing:-0.02em;
         font-weight:600; margin:0 0 36px; text-wrap:balance; max-width:17ch;}
.open h1 .si{color:#AFC5DC;}
.open p{color:var(--bandmuted); font-size:19px; max-width:62ch; margin:0 0 18px;}
.open p:last-child{margin-bottom:0;}
.pricebar{display:flex; gap:56px; flex-wrap:wrap; margin:44px 0 8px;}
.pricebar div{border-top:2px solid var(--bandhair); padding-top:14px;}
.pricebar .num{font-size:clamp(38px,6vw,64px); line-height:1; display:block;
               color:var(--onband);}
.pricebar span.caps{color:var(--bandmuted); display:block; margin-top:12px;}

section{padding:78px 0;}
section + section{border-top:1px solid var(--hair);}
.lede{max-width:64ch;}
.lede h2{font-size:clamp(26px,3.5vw,38px); line-height:1.18; letter-spacing:-0.015em;
         font-weight:600; margin:14px 0 20px; text-wrap:balance;}
.lede p{color:var(--muted); margin:0 0 16px; max-width:62ch;}
.lede p:last-child{margin-bottom:0;}

.plates{display:flex; flex-direction:column; gap:54px; margin-top:50px;}
.pair{display:grid; grid-template-columns:repeat(auto-fit,minmax(268px,1fr)); gap:34px;}
figure.plate{margin:0;}
.plate img{display:block; width:100%; height:auto;
           border:1px solid var(--hair); background:var(--plate);}
figcaption{margin-top:14px; font-size:15px; line-height:1.55; color:var(--muted);
           max-width:56ch;}

.close{background:var(--band); color:var(--onband); padding:78px 0;}
.close h2{font-size:clamp(25px,3.3vw,36px); line-height:1.18; font-weight:600;
          letter-spacing:-0.015em; margin:14px 0 22px; max-width:21ch;
          text-wrap:balance;}
.close h2 .si{color:#AFC5DC;}
.close .caps{color:var(--bandmuted);}
.close p{color:var(--bandmuted); max-width:60ch; margin:0 0 16px;}
.close ul{color:var(--bandmuted); max-width:60ch; padding-left:0; list-style:none;
          margin:26px 0 0; display:flex; flex-direction:column; gap:14px;}
.close li{border-top:1px solid var(--bandhair); padding-top:14px;}
.close li b{color:var(--onband); font-weight:600;}

@media (max-width:640px){
  section{padding:56px 0;} .open{padding:60px 0 56px;} .plates{gap:40px;}
}
"""

BODY = """
<div class="open">
  <div class="wrap">
    <div class="rule">
      <span class="caps">For Gigi Mironova</span>
      <span class="caps">A concept, built not pitched</span>
    </div>
    <h1>The best story on your feed is already
        <span class="si">in your own listings.</span></h1>
    <div class="pricebar">
      <div><span class="num">$2,500</span><span class="caps">a month to rent unit 124</span></div>
      <div><span class="num">$319,999</span><span class="caps">to own unit 124</span></div>
    </div>
    <p>Same unit at 19350 Sherman Way, and both sides of it are yours — the lease and the
       sale. Nobody else in the Valley can post this.</p>
    <p>Here is a six-slide carousel, four reel covers and a profile built around it.
       Take any piece and post it. Nothing here needs my permission.</p>
  </div>
</div>

<section><div class="wrap">
  <div class="lede">
    <span class="caps">The series</span>
    <h2>Same Door</h2>
    <p>Every renter in that building already knows what rent costs. Almost none of them
       know what the unit down the hall sells for, or which number actually decides
       whether owning it costs them less.</p>
    <p>It is not the price. It is the association dues, and they are the one figure that
       is not on the listing — which is the part of this that happens to be your
       professional home ground.</p>
  </div>
  <div class="plates">
    __C1__ __C2__ __C3__ __C4__ __C5__ __C5RU__ __C6__
  </div>
</div></section>

<section><div class="wrap">
  <div class="lede">
    <span class="caps">Reel covers</span>
    <h2>The same argument, in the format that travels</h2>
    <p>Four first frames. One of them is in Russian, because a second language is only
       an advantage when something is actually published in it.</p>
  </div>
  <div class="plates">
    <div class="pair">__R1__ __R2__</div>
    <div class="pair">__R3__ __R4__</div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="lede">
    <span class="caps">The photograph</span>
    <h2>One slot, and it has to be yours</h2>
    <p>There is no stock image worth putting here. The only photograph this series wants
       is the one of the actual door, and you already own it.</p>
  </div>
  <div class="plates">__L1__</div>
</div></section>

<section><div class="wrap">
  <div class="lede">
    <span class="caps">The profile</span>
    <h2>Sixteen years, moved out of the last paragraph</h2>
    <p>Sixteen years in litigation support before real estate — research, analysis,
       negotiation, reading documents for a living. That line is already in the brokerage
       bio. It is the most valuable sentence on the page, and it sits at the bottom of
       one nobody scrolls to.</p>
  </div>
  <div class="plates">
    <div class="pair">__P1__ __P2__</div>
  </div>
</div></section>

<div class="close"><div class="wrap">
  <span class="caps">What happens next</span>
  <h2>Three things only you can <span class="si">give it</span>.</h2>
  <ul>
    <li><b>The dues figure.</b> I deliberately did not put a number on it. You can pull
        the actual association financials on unit 124, and once you have them the carousel
        gets a real figure instead of a question.</li>
    <li><b>The Russian is a draft.</b> I wrote it to read like a transaction rather than a
        translation. Between us, only one person here is a native speaker and a licensee. Correct it
        freely.</li>
    <li><b>Photographs of the unit.</b> The slot is holding an empty frame on purpose.
        Send the set and it drops straight in.</li>
  </ul>
  <p style="margin-top:26px;">If you want your next listing to arrive as a finished kit:
     shoot sheet, scripts in your own words, captions, stories, and a fair-housing pass
     before any of it goes out. That is the thing I do, and we should talk about it.</p>
</div></div>
"""


def main():
    body = BODY
    for key, stem, cap in [
        ("C1", "01-c1", "1 / 6 — the whole argument, and it is already true."),
        ("C2", "02-c2", "2 / 6 — three of these are public. The fourth is not."),
        ("C3", "03-c3", "3 / 6 — where the deciding number actually lives."),
        ("C4", "04-c4", "4 / 6 — the building against the Valley it sits in."),
        ("C5", "05-c5-three-documents", "5 / 6 — the slide people save."),
        ("C5RU", "06-c5-three-documents-ru",
         "5 / 6 — тот же слайд, тот же дизайн, другой язык."),
        ("C6", "07-c6", "6 / 6 — the close, with one keyword to reply to."),
        ("R1", "08-reel-1", None), ("R2", "09-reel-2", None),
        ("R3", "10-reel-3", None), ("R4", "11-reel-4", None),
        ("L1", "12-listing", None),
        ("P1", "13-profile-bio", None), ("P2", "14-profile-highlights", None),
    ]:
        body = body.replace("__%s__" % key, plate(stem, cap))

    html = ("<title>Same Door</title>\n"
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
            "family=Jost:wght@400;500;600;700"
            "&family=Bodoni+Moda:ital,opsz,wght@0,6..96,500;1,6..96,500"
            '&display=swap">\n'
            "<style>%s</style>\n%s" % (CSS, body))
    OUT.write_text(html)
    print("%s  %.1f MB" % (OUT.name, OUT.stat().st_size / 1e6))


if __name__ == "__main__":
    main()
