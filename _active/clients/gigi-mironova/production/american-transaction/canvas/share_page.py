#!/usr/bin/env python3
"""
Build the client-facing share page for the Gigi concept.

BINDING: zero operator language. Nothing here diagnoses her feed, her posting, or her
results. It is a gift with an offer attached — the moment it reads as a teardown, the
relationship it depends on is gone. Diagnosis lives in ../../OPERATOR-NOTES.md.

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


def plate(stem, caption=None, ru=False):
    cap = ('<figcaption%s>%s</figcaption>'
           % (' class="ru"' if ru else "", caption)) if caption else ""
    return ('<figure class="plate"><img src="%s" alt="" loading="lazy">%s</figure>'
            % (img(stem), cap))


CSS = """
:root{
  --paper:#FBF7F6; --ink:#4A1420; --band:#3B0F1A; --muted:#7A5A60;
  --hair:#EADEE0; --accent:#A85A52; --plate:#F3EBEA; --onband:#F6E9E7;
  --bandmuted:rgba(246,233,231,0.72); --bandhair:rgba(246,233,231,0.26);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --paper:#1E0C11; --ink:#F4E7E8; --band:#2C1017; --muted:#BC9A9D;
    --hair:#3E2027; --accent:#D89184; --plate:#261116; --onband:#F6E9E7;
    --bandmuted:rgba(246,233,231,0.72); --bandhair:rgba(246,233,231,0.22);
  }
}
:root[data-theme="dark"]{
  --paper:#1E0C11; --ink:#F4E7E8; --band:#2C1017; --muted:#BC9A9D;
  --hair:#3E2027; --accent:#D89184; --plate:#261116; --onband:#F6E9E7;
  --bandmuted:rgba(246,233,231,0.72); --bandhair:rgba(246,233,231,0.22);
}

*{box-sizing:border-box;}
body{
  margin:0; background:var(--paper); color:var(--ink);
  font-family:'Figtree','Avenir Next',system-ui,sans-serif;
  font-size:18px; line-height:1.62; -webkit-font-smoothing:antialiased;
}
.ru{font-family:'Manrope','Figtree',system-ui,sans-serif;}
.si{font-family:'Playfair Display',Georgia,serif; font-style:italic; font-weight:500;
    color:var(--accent);}
.wrap{max-width:940px; margin:0 auto; padding:0 28px;}
.caps{font-weight:600; letter-spacing:0.22em; text-transform:uppercase; font-size:12px;}

/* --- opening: an oxblood field, the same silence the portrait board uses ------- */
.open{background:var(--band); color:var(--onband); padding:96px 0 88px;}
.open .caps{color:var(--bandmuted);}
.open .rule{border-bottom:1px solid var(--bandhair); padding-bottom:18px;
            margin-bottom:64px; display:flex; justify-content:space-between;
            align-items:baseline; gap:20px; flex-wrap:wrap;}
.open h1{
  font-size:clamp(38px,6.4vw,72px); line-height:1.1; letter-spacing:-0.025em;
  font-weight:600; margin:0 0 40px; text-wrap:balance; max-width:16ch;
}
.open h1 .si{color:#E8C4BE;}
.open p{color:var(--bandmuted); font-size:19px; max-width:62ch; margin:0 0 18px;}
.open p:last-child{margin-bottom:0;}

/* --- sections ------------------------------------------------------------------ */
section{padding:82px 0;}
section + section{border-top:1px solid var(--hair);}
.lede{max-width:64ch;}
.lede h2{
  font-size:clamp(27px,3.6vw,40px); line-height:1.18; letter-spacing:-0.02em;
  font-weight:600; margin:14px 0 20px; text-wrap:balance;
}
.lede p{color:var(--muted); margin:0 0 16px; max-width:62ch;}
.lede p:last-child{margin-bottom:0;}

/* --- plates: the artwork is the hero, shown at the size she'd hold it ---------- */
.plates{display:flex; flex-direction:column; gap:56px; margin-top:52px;}
.pair{display:grid; grid-template-columns:repeat(auto-fit,minmax(268px,1fr)); gap:34px;}
.pair .plate img{border-radius:0;}
figure.plate{margin:0;}
.plate img{
  display:block; width:100%; height:auto;
  border:1px solid var(--hair); background:var(--plate);
}
figcaption{
  margin-top:14px; font-size:15px; line-height:1.55; color:var(--muted);
  max-width:56ch;
}

/* --- the close ----------------------------------------------------------------- */
.close{background:var(--band); color:var(--onband); padding:82px 0;}
.close h2{font-size:clamp(26px,3.4vw,38px); line-height:1.18; font-weight:600;
          letter-spacing:-0.02em; margin:14px 0 22px; max-width:20ch;
          text-wrap:balance;}
.close h2 .si{color:#E8C4BE;}
.close .caps{color:var(--bandmuted);}
.close p{color:var(--bandmuted); max-width:60ch; margin:0 0 16px;}
.close ul{color:var(--bandmuted); max-width:60ch; padding-left:0; list-style:none;
          margin:26px 0 0; display:flex; flex-direction:column; gap:14px;}
.close li{border-top:1px solid var(--bandhair); padding-top:14px;}
.close li b{color:var(--onband); font-weight:600;}

@media (max-width:640px){
  section{padding:58px 0;} .open{padding:64px 0 58px;} .plates{gap:42px;}
}
"""

BODY = """
<div class="open">
  <div class="wrap">
    <div class="rule">
      <span class="caps">For Gigi Mironova</span>
      <span class="caps">A concept, built not pitched</span>
    </div>
    <h1>Everyone can show the house.<br>Almost no one can explain
        <span class="si">the paperwork.</span></h1>
    <p>This is a made thing, not a proposal. One carousel, four reel covers and a
       profile, built around escrow and made to run in English and in Russian.</p>
    <p>Take any piece of it and post it. Nothing here needs my permission.</p>
  </div>
</div>

<section><div class="wrap">
  <div class="lede">
    <span class="caps">The series</span>
    <h2>The American Transaction</h2>
    <p>A buyer's offer gets accepted and three deadlines start running the same day.
       Most people find out what those deadlines were after one of them has passed.</p>
    <p>It is the most expensive gap in the whole process and almost nobody covers it,
       because listings are easier to post. It is also the part where somebody who can
       explain it twice, once in English and once in Russian, is simply the only option
       on the board.</p>
  </div>
  <div class="plates">
    __C1__ __C2__ __C3__ __C4__ __C5__ __C5RU__ __C6__
  </div>
</div></section>

<section><div class="wrap">
  <div class="lede">
    <span class="caps">Reel covers</span>
    <h2>The same argument, in the format that travels</h2>
    <p>Four covers in the same system. Each one is the first frame of a reel that answers
       the question on it. One of them is in Russian, because the lane only counts if it
       actually runs.</p>
  </div>
  <div class="plates">
    <div class="pair">__R1__ __R2__</div>
    <div class="pair">__R3__ __R4__</div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="lede">
    <span class="caps">The profile</span>
    <h2>One promise, one way in</h2>
    <p>A bio that says the specific thing you do, and nine highlight covers that each open
       a different door for whoever just landed on the page.</p>
  </div>
  <div class="plates">
    <div class="pair">__P1__ __P2__</div>
  </div>
</div></section>

<div class="close"><div class="wrap">
  <span class="caps">What happens next</span>
  <h2>If you want it, it becomes <span class="si">yours</span> — and it needs you in it.</h2>
  <p>Three things I need from you before any of this posts, and every one of them is
     something only you can give:</p>
  <ul>
    <li><b>The Russian is a draft.</b> I wrote it to read like a transaction rather than a
        translation. But you are the native speaker and the licensee. Correct it freely.</li>
    <li><b>The line on the fourth cover is yours.</b> You wrote it first. I only pointed
        it at the work. If it does not feel like you, it comes out and nothing breaks.</li>
    <li><b>Photographs of you beat anything I can source.</b> The fourth cover is holding
        an empty field on purpose. It is the shape your portrait drops into.</li>
  </ul>
  <p style="margin-top:26px;">The next listing can arrive as a finished kit: shoot sheet,
     scripts in your own words, captions, stories, and a fair-housing pass before any of
     it goes out. That is the thing I do, and we should talk about it.</p>
</div></div>
"""


def main():
    body = BODY
    for key, stem, cap, ru in [
        ("C1", "01-c1", "1 / 6 — the hook.", False),
        ("C2", "02-c2", "2 / 6 — where the clock actually starts.", False),
        ("C3", "03-c3", "3 / 6 — the three C.A.R. defaults, side by side. "
                        "The white slides are the densest ones on purpose.", False),
        ("C4", "04-c4", "4 / 6 — the deposit, and the thing people most often get wrong "
                        "about it.", False),
        ("C5", "05-c5-three-questions", "5 / 6 — the save-worthy slide.", False),
        ("C5RU", "06-c5-three-questions-ru",
         "5 / 6 — тот же слайд, тот же дизайн, другой язык.", True),
        ("C6", "07-c6", "6 / 6 — the close, with one keyword to reply to.", False),
        ("R1", "08-reel-1", None, False),
        ("R2", "09-reel-2", None, False),
        ("R3", "10-reel-3", None, False),
        ("R4", "11-reel-4", None, False),
        ("P1", "12-profile-bio", None, False),
        ("P2", "13-profile-highlights", None, False),
    ]:
        body = body.replace("__%s__" % key, plate(stem, cap, ru))

    html = ("<title>The American Transaction</title>\n"
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
            "family=Figtree:wght@400;500;600;700"
            "&family=Manrope:wght@400;500;600;700"
            "&family=Playfair+Display:ital,wght@0,400;1,400;1,500"
            '&display=swap">\n'
            "<style>%s</style>\n%s" % (CSS, body))
    OUT.write_text(html)
    print("%s  %.1f MB" % (OUT.name, OUT.stat().st_size / 1e6))


if __name__ == "__main__":
    main()
