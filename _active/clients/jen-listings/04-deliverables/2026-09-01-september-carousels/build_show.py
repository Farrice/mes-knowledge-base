#!/usr/bin/env python3
"""The presentation for tonight: one full-screen slideshow page (arrow keys, tap, swipe), built from the rendered PNGs.
Sections: the walkthrough (16 boards) · the first post (condo, 7) · next (rail 7, insurance 7) · her words + the reply.
Press N for Farrice's one-line notes. Writes show/september-for-jen.html (self-contained)."""
import base64, json, pathlib

HERE = pathlib.Path(__file__).parent
PNG = HERE / "png"
OUT = HERE / "show"
OUT.mkdir(exist_ok=True)

SECTIONS = [
    ("tonight", [(f"deck-{i:02d}", n) for i, n in enumerate([
        "start with the feeling: she's the friend who happens to sell real estate, from here.",
        "four words. define them once, then never use another term she doesn't know.",
        "a post is a billboard, a system is a door. this is the 'not posting for posting's sake' board.",
        "three things she already does, said out loud. read the third one in her words.",
        "the month, not the post. point at october: sellers, a $2M listing, a downsizer. the subject and the buyer rotate; her face, the stamp, and the close repeat.",
        "how one post becomes a conversation. the only new work is the minute she talks.",
        "we count replies, not likes. a like is nothing; a message is a person.",
        "the math. do not read numbers; ask for hers. 'you already know your conversation-to-client ratio from referrals.'",
        "ninety days: a series people collect, the stamp, her face, the same close.",
        "about three hours a week. when a post does nothing, nothing happens.",
        "the slow weeks are part of the plan. this is the board that removes the guilt.",
        "who does what. she has the last word on every word.",
        "the valley file: what she hands people who write. evergreen, no gate. the pinned 'start here' post is the doorway.",
        "three photos, one memo, four numbers. ask for these tonight.",
        "if she says yes, this is the rhythm. read 'what you never do' out loud.",
        "the first post is ready. stop here and show the carousel.",
    ], 1)]),
    ("the first post", [(f"dir-d-{i:02d}", "") for i in range(1, 8)]),
    ("next: the train", [(f"rail-{i:02d}", "") for i in range(1, 8)]),
    ("next: the insurance quote", [(f"insurance-{i:02d}", "") for i in range(1, 8)]),
    ("her words + the reply", [("present-05-your-words", "her lines from the voice memos. if one isn't her, it goes."), ("deck-17-dm-reply", "the saved replies. paste, personalize, send.")]),
]

slides = []
for sec, items in SECTIONS:
    for stem, note in items:
        p = PNG / f"{stem}.png"
        if not p.exists():
            continue
        slides.append({"sec": sec, "src": "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode(), "note": note})

html = """<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>September, for Jen</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&family=Playfair+Display:ital@1&display=swap">
<style>
  html,body{margin:0;height:100%;background:#0F1F35;color:#F7F5F2;font-family:Figtree,system-ui,sans-serif;overflow:hidden}
  #stage{position:fixed;inset:0;display:flex;align-items:center;justify-content:center}
  #stage img{max-height:calc(100vh - 96px);max-width:calc(100vw - 48px);box-shadow:0 30px 80px rgba(0,0,0,.45);background:#F7F5F2}
  #top{position:fixed;top:0;left:0;right:0;height:48px;display:flex;align-items:center;justify-content:space-between;padding:0 22px;font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:#9FB4CC}
  #top b{color:#F7F5F2;font-weight:500}
  #bar{position:fixed;bottom:0;left:0;right:0;height:48px;display:flex;align-items:center;gap:6px;padding:0 22px}
  #bar .d{height:4px;flex:1;background:#24436B}
  #bar .d.on{background:#F7F5F2}
  #bar .d.done{background:#4C7CA8}
  #note{position:fixed;left:0;right:0;bottom:48px;padding:16px 26px;background:rgba(15,31,53,.92);border-top:1px solid #3A5578;font-size:18px;line-height:1.5;color:#C9D4E2;display:none}
  #note.on{display:block}
  #note i{font-family:'Playfair Display',serif;color:#9FB4CC;margin-right:10px}
  #help{position:fixed;right:22px;bottom:60px;font-size:12px;letter-spacing:.18em;color:#7E96B4;text-transform:uppercase}
  .hit{position:fixed;top:48px;bottom:48px;width:50%;cursor:pointer}
  #prev{left:0}#next{right:0}
</style></head><body>
<div id="top"><span id="sec"></span><span><b id="num"></b> <span id="tot"></span></span></div>
<div id="stage"><img id="img" alt=""></div>
<div class="hit" id="prev"></div><div class="hit" id="next"></div>
<div id="note"><i>note</i><span id="notetext"></span></div><div id="help">← → · space · n for notes · f fullscreen</div>
<div id="bar"></div>
<script>
const S=__SLIDES__;let i=0,notes=false;
const img=document.getElementById('img'),sec=document.getElementById('sec'),num=document.getElementById('num'),tot=document.getElementById('tot'),note=document.getElementById('note'),notetext=document.getElementById('notetext'),bar=document.getElementById('bar');
S.forEach(()=>{const d=document.createElement('div');d.className='d';bar.appendChild(d)});
function go(n){i=Math.max(0,Math.min(S.length-1,n));img.src=S[i].src;sec.textContent=S[i].sec;num.textContent=String(i+1);tot.textContent='/ '+S.length;
  notetext.textContent=S[i].note||'';note.className=(notes&&S[i].note)?'on':'';
  Array.from(bar.children).forEach((d,k)=>{d.className='d'+(k<i?' done':k===i?' on':'')});
  try{localStorage.setItem('jen-show-i',String(i))}catch(e){}}
document.getElementById('next').onclick=()=>go(i+1);document.getElementById('prev').onclick=()=>go(i-1);
addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'){e.preventDefault();go(i+1)}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();go(i-1)}
  else if(e.key==='n'||e.key==='N'){notes=!notes;go(i)}
  else if(e.key==='f'||e.key==='F'){if(document.documentElement.requestFullscreen)document.documentElement.requestFullscreen()}
  else if(e.key==='Home'){go(0)}});
let x0=null;addEventListener('touchstart',e=>{x0=e.touches[0].clientX},{passive:true});
addEventListener('touchend',e=>{if(x0===null)return;const dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>40)go(dx<0?i+1:i-1);x0=null});
S.slice(1).forEach(s=>{const im=new Image();im.src=s.src});
go(0);
</script></body></html>"""
out = OUT / "september-for-jen.html"
out.write_text(html.replace("__SLIDES__", json.dumps(slides)))
print(f"show: {len(slides)} slides, {out.stat().st_size // 1024} KB -> {out}")
