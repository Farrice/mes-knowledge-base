#!/usr/bin/env python3
"""Assemble the Listing Launch Kit landing page with inlined proof images."""
import base64, pathlib

HERE = pathlib.Path(__file__).parent
def b64(name):
    return base64.b64encode((HERE / "img" / name).read_bytes()).decode()

IMGS = {k: b64(f"{k}.jpg") for k in ["day-intro", "twilight", "interior", "hook-text"]}

HTML = '''<title>The Listing Launch Kit</title>
<style>
  :root{
    --canvas:#F3F3F0; --paper:#FAFAF8; --ink:#101010; --graphite:#555553;
    --line:#D8D8D3; --stone:#8C8C82; --white:#FFFFFF;
  }
  *{ box-sizing:border-box; }
  body{ background:var(--canvas); color:var(--ink); margin:0;
    font-family:"Helvetica Neue", Helvetica, Arial, sans-serif; font-size:17px; line-height:1.6; }
  .wrap{ max-width:960px; margin:0 auto; padding:0 24px; }
  .label{ font-size:11px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; }
  header{ border-bottom:1px solid var(--ink); }
  header .wrap{ display:flex; justify-content:space-between; align-items:baseline; padding:20px 24px; flex-wrap:wrap; gap:8px; }
  header .name{ color:var(--ink); }
  header .desc{ color:var(--stone); }
  .hero{ padding:96px 0 72px; }
  h1{ font-weight:700; font-size:clamp(38px,6vw,64px); line-height:1.05; letter-spacing:-.025em; margin:0 0 24px; max-width:16ch; text-wrap:balance; }
  .hero p.sub{ font-size:21px; color:var(--graphite); max-width:52ch; margin:0 0 40px; }
  .cta{ display:inline-block; background:var(--ink); color:var(--paper); text-decoration:none;
    padding:18px 34px; font-weight:700; font-size:16px; letter-spacing:.04em; }
  .cta:hover{ background:#2A2A28; color:var(--paper); }
  .pricehint{ display:inline-block; margin-left:20px; color:var(--graphite); font-size:15px; }
  section{ padding:72px 0; border-top:1px solid var(--line); }
  .sechead{ display:flex; align-items:baseline; gap:16px; margin-bottom:8px; }
  .sechead .idx{ color:var(--stone); font-weight:700; font-size:22px; }
  h2{ font-weight:700; font-size:clamp(26px,4vw,36px); letter-spacing:-.02em; margin:0; text-wrap:balance; }
  .secsub{ color:var(--graphite); margin:6px 0 40px; max-width:60ch; }
  .proofgrid{ display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:20px; }
  .proof{ background:var(--white); border:1px solid var(--line); text-decoration:none; color:var(--ink); display:flex; flex-direction:column; }
  .proof img{ width:100%; display:block; aspect-ratio:9/16; object-fit:cover; }
  .proof .cap{ padding:14px 16px; display:flex; flex-direction:column; gap:4px; }
  .proof .cap b{ font-size:14px; font-weight:700; }
  .proof .cap span{ font-size:12.5px; color:var(--stone); }
  .proofnote{ margin-top:24px; font-size:14px; color:var(--graphite); max-width:70ch; }
  .ledger{ border-top:1px solid var(--line); }
  .row{ display:flex; gap:24px; padding:26px 0; border-bottom:1px solid var(--line); align-items:baseline; }
  .row .n{ color:var(--stone); font-weight:700; font-size:14px; min-width:34px; }
  .row b{ font-size:18px; min-width:220px; }
  .row p{ margin:0; color:var(--graphite); font-size:16px; }
  .steps{ display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:24px; }
  .step{ background:var(--paper); border:1px solid var(--line); padding:32px 28px; }
  .step .n{ color:var(--stone); font-weight:700; font-size:14px; letter-spacing:.16em; display:block; margin-bottom:14px; }
  .step b{ font-size:19px; display:block; margin-bottom:10px; }
  .step p{ margin:0; color:var(--graphite); font-size:15.5px; }
  .std{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:0; border-top:1px solid var(--line); }
  .std div{ padding:28px 24px 28px 0; border-bottom:1px solid var(--line); }
  .std b{ display:block; margin-bottom:8px; font-size:17px; }
  .std p{ margin:0; color:var(--graphite); font-size:15.5px; }
  .offer{ background:var(--ink); color:var(--paper); }
  .offer h2, .offer .sechead .idx{ color:var(--paper); }
  .offer .big{ font-size:clamp(48px,7vw,84px); font-weight:700; letter-spacing:-.025em; line-height:1; margin:24px 0 6px; }
  .offer .strike{ color:#8C8C82; text-decoration:line-through; font-size:26px; font-weight:400; margin-left:14px; letter-spacing:0; }
  .offer p{ color:#C9C9C4; max-width:56ch; }
  .offer .terms{ display:flex; flex-wrap:wrap; gap:10px 28px; margin:28px 0 40px; padding:0; list-style:none; }
  .offer .terms li{ font-size:14px; color:#C9C9C4; border-left:2px solid #3A3A38; padding-left:12px; }
  .cta.inv{ background:var(--paper); color:var(--ink); }
  .cta.inv:hover{ background:#EDEDE8; color:var(--ink); }
  footer{ border-top:1px solid var(--ink); }
  footer .wrap{ display:flex; justify-content:space-between; align-items:baseline; padding:24px; flex-wrap:wrap; gap:8px; color:var(--stone); font-size:13px; }
</style>

<header><div class="wrap">
  <span class="label name">Farrice Cain</span>
  <span class="label desc">Listing content system</span>
</div></header>

<div class="hero"><div class="wrap">
  <h1>Your listing becomes a week of content. You just film.</h1>
  <p class="sub">Shoot sheet, word-for-word reel scripts in your voice, captions, stories, and a DM keyword that turns views into conversations — researched, designed, and compliance-screened. Delivered in 48 hours.</p>
  <a class="cta" href="#offer">Claim a founding spot — $200</a>
  <span class="pricehint">3 spots · then $450</span>
</div></div>

<section><div class="wrap">
  <div class="sechead"><span class="idx">01</span><h2>Live on Jen Santulan's feed right now</h2></div>
  <p class="secsub">This system runs the listing content behind @_jiing and the House Sellers team — the research, scripts, shoot plans, captions, and compliance screens beneath the reels you can watch today. Tap any still to see it live.</p>
  <div class="proofgrid">
    <a class="proof" href="https://www.instagram.com/_jiing/reel/DZvfGfxyVxn/">
      <img src="data:image/jpeg;base64,{DAY}" alt="Jen opening a listing walkthrough at the property exterior">
      <span class="cap"><b>Listing walkthrough</b><span>agent-forward open · watch on Instagram</span></span>
    </a>
    <a class="proof" href="https://www.instagram.com/_jiing/reel/Dcei8M2oZqg/">
      <img src="data:image/jpeg;base64,{TWI}" alt="Twilight exterior showcase of a listed home">
      <span class="cap"><b>Twilight showcase</b><span>blue-hour listing feature · watch on Instagram</span></span>
    </a>
    <a class="proof" href="https://www.instagram.com/_jiing/reel/DZvfGfxyVxn/">
      <img src="data:image/jpeg;base64,{INT}" alt="Interior detail shot from a listing reel">
      <span class="cap"><b>Detail storytelling</b><span>interior reveal sequence · watch on Instagram</span></span>
    </a>
    <a class="proof" href="https://www.instagram.com/_jiing/reel/DYkn2gBPWJq/">
      <img src="data:image/jpeg;base64,{HOOK}" alt="Hook reel with kinetic text overlay">
      <span class="cap"><b>Hook reel</b><span>20-second scripted hook · watch on Instagram</span></span>
    </a>
  </div>
  <p class="proofnote">Stills from published reels on @_jiing. Filming by Jen's videographer; the content system underneath — what to shoot, what to say, what to write, what never to say on camera — is what you're buying here.</p>
</div></section>

<section><div class="wrap">
  <div class="sechead"><span class="idx">02</span><h2>What a kit contains</h2></div>
  <p class="secsub">One active listing in, one forwardable package out. Everything film-ready the day you receive it.</p>
  <div class="ledger">
    <div class="row"><span class="n">1</span><b>Shoot Sheet</b><p>Every shot for the whole kit in one 40-minute phone walkthrough. No videographer required.</p></div>
    <div class="row"><span class="n">2</span><b>Teleprompter Pack</b><p>Three reel scripts written in your voice from your own posts — read them off your phone, word for word.</p></div>
    <div class="row"><span class="n">3</span><b>Caption + Hook Set</b><p>Captions, hooks, and a designed carousel, each with pick-one options. No blank-page moments.</p></div>
    <div class="row"><span class="n">4</span><b>Stories + DM Keyword</b><p>A five-frame story arc ending in a keyword CTA, so views become conversations instead of decoration.</p></div>
    <div class="row"><span class="n">5</span><b>Compliance Pass</b><p>Every line screened against fair-housing language rules, with a don't-say list included. Most agents have never had this.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sechead"><span class="idx">03</span><h2>How it works</h2></div>
  <div class="steps">
    <div class="step"><span class="n">STEP 1</span><b>Text me your listing</b><p>Address, MLS link, five phone photos, your IG handle. Ten minutes, one text.</p></div>
    <div class="step"><span class="n">STEP 2</span><b>48 hours later</b><p>Your complete kit arrives as one forwardable package — scripts in your voice, designs in your brand.</p></div>
    <div class="step"><span class="n">STEP 3</span><b>Film, post, answer DMs</b><p>One walkthrough covers every shot. Day 3, I check in; send me your raw take and I'll tighten it.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sechead"><span class="idx">04</span><h2>Why this beats templates</h2></div>
  <div class="std">
    <div><b>Demand-researched</b><p>Content answers what buyers and sellers in your market are searching this month — not what a template calendar guessed last year.</p></div>
    <div><b>Written in your voice</b><p>Built from your last 15 posts and a 10-minute intake. If it doesn't sound like you, it doesn't ship.</p></div>
    <div><b>Designed, not decorated</b><p>Editorial-grade graphics in your colors and type — no stock photos, no clip art, no template your competitors are also using.</p></div>
    <div><b>Screened before you say it</b><p>Fair-housing compliance on every line, plus a don't-say list for when you improvise. Protection most content services never mention.</p></div>
  </div>
</div></section>

<section class="offer" id="offer"><div class="wrap">
  <div class="sechead"><span class="idx">05</span><h2>Founding rate</h2></div>
  <div class="big">$200<span class="strike">$450</span></div>
  <p>First three agents on the team, in exchange for permission to screenshot results and one sentence of feedback after your first kit posts. Paid up front, Zelle or Venmo. Kit lands within 48 hours of your intake.</p>
  <ul class="terms">
    <li>No active listing? Same price gets the Agent Engine Starter: profile fix + 10 ready-to-film scripts + 2-week calendar</li>
    <li>No subscription, no contract — one kit, then decide</li>
    <li>Posting stays yours; I build, you publish</li>
  </ul>
  <a class="cta inv" href="https://www.instagram.com/[YOUR-HANDLE]/">DM me — or text [YOUR PHONE]</a>
</div></section>

<footer><div class="wrap">
  <span class="label">Farrice Cain · Listing Content System</span>
  <span>Serving the San Fernando Valley &amp; Greater LA</span>
</div></footer>
'''

out = HERE / "listing-launch-kit.html"
out.write_text(HTML.replace("{DAY}", IMGS["day-intro"]).replace("{TWI}", IMGS["twilight"]).replace("{INT}", IMGS["interior"]).replace("{HOOK}", IMGS["hook-text"]))
print("wrote", out, out.stat().st_size, "bytes")
