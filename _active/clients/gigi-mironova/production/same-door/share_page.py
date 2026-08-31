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
  --paper:#FDFDFC; --ink:#2C4A68; --band:#243D56; --muted:#75879C;
  --hair:#E3E9F0; --accent:#5E86AC; --plate:#F2F5F8; --onband:#ECF1F6;
  --bandmuted:rgba(234,240,247,0.74); --bandhair:rgba(234,240,247,0.26);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --paper:#101D2C; --ink:#E6EDF4; --band:#1B2E42; --muted:#9FB3C8;
    --hair:#22364B; --accent:#9BB8D6; --plate:#132434; --onband:#EAF0F7;
    --bandmuted:rgba(234,240,247,0.74); --bandhair:rgba(234,240,247,0.22);
  }
}
:root[data-theme="dark"]{
  --paper:#101D2C; --ink:#E6EDF4; --band:#1B2E42; --muted:#9FB3C8;
  --hair:#22364B; --accent:#9BB8D6; --plate:#132434; --onband:#EAF0F7;
  --bandmuted:rgba(234,240,247,0.74); --bandhair:rgba(234,240,247,0.22);
}

*{box-sizing:border-box;}
body{
  margin:0; background:var(--paper); color:var(--ink);
  font-family:'Figtree','Avenir Next',system-ui,sans-serif;
  font-size:18px; line-height:1.62; -webkit-font-smoothing:antialiased;
}
.si{font-family:'Playfair Display',Georgia,serif; font-style:italic; font-weight:500;
    color:var(--accent);}
.wrap{max-width:940px; margin:0 auto; padding:0 28px;}
.caps{font-weight:500; letter-spacing:0.24em; text-transform:uppercase; font-size:12px;}
.num{font-weight:600; letter-spacing:-0.02em;
     font-variant-numeric:tabular-nums;}

.open{background:var(--band); color:var(--onband); padding:92px 0 84px;}
.open .caps{color:var(--bandmuted);}
.open .rule{border-bottom:1px solid var(--bandhair); padding-bottom:18px;
            margin-bottom:60px; display:flex; justify-content:space-between;
            align-items:baseline; gap:20px; flex-wrap:wrap;}
.open h1{font-size:clamp(36px,6vw,66px); line-height:1.11; letter-spacing:-0.02em;
         font-weight:600; margin:0 0 36px; text-wrap:balance; max-width:17ch;}
.open h1 .si{color:#C3D4E5;}
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

.script{border:1px solid var(--hair); padding:26px 30px; margin-top:22px;}
.script .caps{color:var(--muted); display:block; margin-bottom:12px;}
.script p{margin:0; font-size:17.5px; line-height:1.7; color:var(--ink);}
.opts{display:flex; flex-direction:column; gap:14px; margin-top:22px;}
.opt{background:var(--plate); padding:20px 24px; font-size:16.5px; line-height:1.65;
     color:var(--ink);}
.opt b{color:var(--accent); font-weight:600; letter-spacing:0.08em;}
.framelist{display:flex; flex-direction:column; gap:0; margin-top:22px;
           border-top:1px solid var(--hair);}
.framelist div{display:flex; gap:22px; padding:16px 0; border-bottom:1px solid var(--hair);
               font-size:16.5px; line-height:1.6; color:var(--ink);}
.framelist span{color:var(--accent); font-weight:600; min-width:70px;
                letter-spacing:0.06em;}
.covergrid{display:grid; grid-template-columns:repeat(3,1fr); gap:18px; margin-top:26px;}
.covergrid img{width:100%; display:block; border:1px solid var(--hair);}
.dont{list-style:none; padding:0; margin:22px 0 0; display:flex; flex-direction:column;
      gap:12px;}
.dont li{border-left:2px solid var(--accent); padding:2px 0 2px 18px; font-size:16.5px;
         line-height:1.6; color:var(--ink);}
.close{background:var(--band); color:var(--onband); padding:78px 0;}
.close h2{font-size:clamp(25px,3.3vw,36px); line-height:1.18; font-weight:600;
          letter-spacing:-0.015em; margin:14px 0 22px; max-width:21ch;
          text-wrap:balance;}
.close h2 .si{color:#C3D4E5;}
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
      <span class="caps">A finished kit, not a pitch</span>
    </div>
    <h1>Unit 124, ready to <span class="si">post.</span></h1>
    <div class="pricebar">
      <div><span class="num">$2,500</span><span class="caps">a month to rent it</span></div>
      <div><span class="num">$2,515</span><span class="caps">a month to own it (estimate)</span></div>
    </div>
    <p>You are the agent on both sides of the same unit, and the real monthly math lands
       fifteen dollars from the rent. Nobody else in the Valley can post that.</p>
    <p>Below is the whole package: a six-slide carousel, three reel scripts written to be
       read off your phone, captions with pick-one options, a five-frame story sequence,
       nine highlight covers, and a short don&#8217;t-say list so every line is
       fair-housing clean. Post any of it today, change anything. Nothing here needs my
       permission.</p>
  </div>
</div>

<section><div class="wrap">
  <div class="lede">
    <span class="caps">Post this today · the carousel</span>
    <h2>Same Door</h2>
    <p>The math is computed, sourced and labeled: 20% down at 6.66% (Freddie Mac average,
       Aug 27), taxes estimated at 1.25%, the building&#8217;s recorded $477 dues, and
       HO-6 insurance. Slide two does the work most agents leave as homework.</p>
  </div>
  <div class="plates">
    __C1__ __C2__ __C3__ __C4__ __C5__ __C5RU__ __C6__
  </div>
  <div class="lede" style="margin-top:44px;">
    <span class="caps">Caption · pick one</span>
    <div class="opts">
      <div class="opt"><b>A</b> · Same unit. Two listings. Both mine. Renting it runs
      $2,500 a month. Do the actual math on owning it and the answer is closer than
      almost anyone guesses. The figure that decides it isn&#8217;t the price, and it
      isn&#8217;t on the listing. Full math in the slides. Estimate, not a quote;
      your numbers will differ. DM me &#8220;124&#8221; for the complete breakdown.</div>
      <div class="opt"><b>B</b> · One Reseda unit, two of my listings: the lease and the
      sale. That makes this rent-vs-own math real, line by line, sources included. If
      you&#8217;ve been assuming owning is out of reach, slide two is worth thirty
      seconds. Message me &#8220;124&#8221; and
      I&#8217;ll send the full breakdown.</div>
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="lede">
    <span class="caps">Film these · three reels</span>
    <h2>Scripts you can read off the phone</h2>
    <p>Written to your register: clear plan, honest numbers, no sugarcoating. Each is
       one continuous take, about thirty seconds. The cover is the first frame.</p>
  </div>
  <div class="plates">
    <div class="pair">__R1__ __R2__</div>
  </div>
  <div class="script"><span class="caps">Reel 01 · Same Door · ~30s</span>
    <p>&#8220;I&#8217;m the agent on both listings for the same unit at 19350 Sherman Way.
    Renting it: twenty-five hundred a month. Buying it: just under three hundred twenty
    thousand. Most people assume owning costs far more. Run the actual numbers. Twenty
    percent down at today&#8217;s average rate, taxes, insurance, and the dues: about
    twenty-five fifteen a month. Fifteen dollars apart. And about two
    hundred twenty of that first payment is principal. Money that stays yours. Want the
    full breakdown? Message me the number 124.&#8221;</p>
  </div>
  <div class="opts">
    <div class="opt"><b>Caption A</b> · The full math is in my Same Door carousel, sources
    and assumptions included. Estimate, not a quote. DM &#8220;124&#8221; for the breakdown.</div>
    <div class="opt"><b>Caption B</b> · Fifteen dollars. That&#8217;s the real gap between
    renting and owning this unit, before equity. Numbers in the carousel. Send me
    &#8220;124&#8221; for the breakdown.</div>
  </div>
  <div class="script"><span class="caps">Reel 02 · The $477 · ~30s</span>
    <p>&#8220;Here&#8217;s the number nobody quotes you when you&#8217;re shopping for a
    condo: the association dues. In this building the recorded figure is four hundred
    seventy-seven dollars a month. It covers the pool, the spa, the gym, water, trash and
    the building&#8217;s insurance. And it isn&#8217;t on the listing. It lives in the
    HOA documents. I spent sixteen years in litigation support before I got my license,
    so reading those documents is the part of this job I&#8217;m built for. Looking at any condo, mine included: ask for the financials before you write. Message me 124 and
    I&#8217;ll send you the exact list to ask for.&#8221;</p>
  </div>
  <div class="plates" style="margin-top:34px;">
    <div class="pair">__R3__ __R4__</div>
  </div>
  <div class="script"><span class="caps">Reel 03 · по-русски · ~25s (your pass first; I
  wrote it to read like a transaction, you&#8217;re the native speaker)</span>
    <p>&#8220;Одна и та же квартира на Шерман Уэй. Снять — две тысячи пятьсот в месяц.
    Купить — чуть меньше трёхсот двадцати тысяч. Посчитаем честно: взнос двадцать
    процентов, сегодняшняя ставка, налоги, страховка и взносы ассоциации — выходит около
    двух тысяч пятисот в месяц. Почти как аренда. Разница в том, что часть платежа
    остаётся вашей. Хотите полный расчёт по-русски — напишите мне «124».&#8221;</p>
  </div>
  <div class="script"><span class="caps">Reel 04 · the portrait cover</span>
    <p>This one is for a talking-head reel about how you work: the sixteen years, the
    documents, the honest-numbers approach your clients already describe in reviews.
    When you send a current portrait you like, I&#8217;ll set it into the cover the same
    day; your brokerage headshot is holding the frame for now.</p>
  </div>
</div></section>

<section><div class="wrap">
  <div class="lede">
    <span class="caps">Stories · five frames, one keyword</span>
    <h2>The story sequence</h2>
    <div class="framelist">
      <div><span>1</span>Poll sticker: &#8220;Renting in the Valley: do you know what the
      unit next door sells for?&#8221; Yes / No idea</div>
      <div><span>2</span>Slide 1 of the carousel (the two prices), no added text</div>
      <div><span>3</span>Slide 2 (the math), with &#8220;estimate; your numbers will
      differ&#8221; typed on top</div>
      <div><span>4</span>Slide 3 (the $477), caption: &#8220;the number that isn&#8217;t
      on the listing&#8221;</div>
      <div><span>5</span>Close-up of you or the building; text: &#8220;full breakdown, in
      English or по-русски. DM &#8216;124&#8217;&#8221;</div>
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="lede">
    <span class="caps">Profile · bio and covers</span>
    <h2>The bio, one line stronger</h2>
    <div class="opts">
      <div class="opt"><b>Bio</b> · Real estate, read carefully. 16 years in litigation
      support before my license; now the fine print works for you.<br>
      English · Русский&nbsp; |&nbsp; SFV + Conejo Valley<br>
      DM &#8220;HOME&#8221; to start</div>
    </div>
    <p style="margin-top:18px;">Your background is the one credential no other agent in
       the Valley can copy, and it belongs in the first line, in your own words. The nine
       covers below are finished files. Save them and upload straight to your highlights.</p>
  </div>
  <div class="covergrid">
    __COVERS__
  </div>
</div></section>

<section><div class="wrap">
  <div class="lede">
    <span class="caps">Before anything posts</span>
    <h2>The don&#8217;t-say list</h2>
    <ul class="dont">
      <li>Never describe a neighborhood or building by who lives there. Speaking Russian
      is a service you offer, never a description of an area, in either language.</li>
      <li>Keep &#8220;estimate, not a quote&#8221; wherever the $2,515 appears. Rate,
      credit and the unit&#8217;s actual dues all move it.</li>
      <li>Don&#8217;t say owning is cheaper than renting. Say &#8220;about the same before
      equity. Run your numbers.&#8221;</li>
      <li>The $477 is the building&#8217;s recorded figure for a two-bedroom. Say
      &#8220;recorded for this building,&#8221; never &#8220;unit 124&#8217;s dues.&#8221;</li>
      <li>No &#8220;guaranteed,&#8221; no &#8220;always appreciates,&#8221; no
      &#8220;can&#8217;t lose.&#8221;</li>
      <li>If you boost any of it, never target by language or demographics. Housing ads
      follow special rules on every platform.</li>
    </ul>
  </div>
</div></section>

<div class="close"><div class="wrap">
  <span class="caps">Two upgrades, when you&#8217;re ready</span>
  <h2>What makes this even <span class="si">sharper</span>.</h2>
  <ul>
    <li><b>Unit 124&#8217;s own dues figure.</b> Pull the association&#8217;s financials
    and the math slide gets the exact number instead of the building&#8217;s recorded one.
    Send it over and I&#8217;ll have the updated slide back same day.</li>
    <li><b>Your photos of the unit.</b> The moment you send the listing set, slide one
    carries the actual door instead of the Valley at dusk.</li>
  </ul>
  <p style="margin-top:26px;">This one&#8217;s on me. It&#8217;s the same kit I build for
     Jen&#8217;s listings. If it works, all I&#8217;d ask is a screenshot of the results
     and one sentence of feedback. And if you want the next listing to arrive like this automatically (shoot sheet,
     scripts, captions, compliance pass, done in 48 hours), that&#8217;s the thing I do.
     Text me.</p>
</div></div>
"""


def main():
    body = BODY
    for key, stem, cap in [
        ("C1", "01-c1", "1 / 6 — the two prices, already true."),
        ("C2", "02-c2", "2 / 6 — the math, done and labeled. This is the slide that gets saved."),
        ("C3", "03-c3", "3 / 6 — the $477, and what it actually buys."),
        ("C4", "04-c4", "4 / 6 — the part rent never does."),
        ("C5", "05-c5-three-documents", "5 / 6 — the checklist."),
        ("C5RU", "06-c5-three-documents-ru",
         "5 / 6 — тот же слайд, другой язык (your pass first)."),
        ("C6", "07-c6", "6 / 6 — the close. One keyword: 124."),
        ("R1", "08-reel-1", None), ("R2", "09-reel-2", None),
        ("R3", "10-reel-3", None), ("R4", "11-reel-4", None),
    ]:
        body = body.replace("__%s__" % key, plate(stem, cap))

    covers = sorted((HERE / "covers").glob("cover-*.png"),
                    key=lambda f: int(f.name.split("-")[1]))
    tags = []
    for f in covers:
        TMP.mkdir(exist_ok=True)
        dst = TMP / (f.stem + ".jpg")
        subprocess.run(["sips", "-Z", "540", "-s", "format", "jpeg",
                        "-s", "formatOptions", "82", str(f), "--out", str(dst)],
                       check=True, capture_output=True)
        b = base64.b64encode(dst.read_bytes()).decode()
        tags.append('<img src="data:image/jpeg;base64,%s" alt="">' % b)
    body = body.replace("__COVERS__", "".join(tags))

    html = ("<title>Same Door</title>\n"
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
            "family=Figtree:wght@400;500;600;700"
            "&family=Playfair+Display:ital,wght@1,400;1,500"
            '&display=swap">\n'
            "<style>%s</style>\n%s" % (CSS, body))
    OUT.write_text(html)
    print("%s  %.1f MB" % (OUT.name, OUT.stat().st_size / 1e6))


if __name__ == "__main__":
    main()
