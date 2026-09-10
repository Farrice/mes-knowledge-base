#!/usr/bin/env python3
"""Build four listing boards, a six-page gift deck, and an image-direction board."""
import base64, json
from pathlib import Path

HERE=Path(__file__).parent
ROOT=HERE.parent
SAFE=ROOT/'same-door'
PAPER='#F4F0E8'; INK='#173A54'; NAVY='#244C68'; CLAY='#BD765E'; MUTED='#657783'; LINE='#CBD6DB'; WHITE='#FCFBF7'
FONTS="""@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&display=swap');"""

def enc(name):
    p=SAFE/'canvas-assets'/name
    return 'data:image/jpeg;base64,'+base64.b64encode(p.read_bytes()).decode()

def shell(body, extra=''):
    css=f"""{FONTS}*{{box-sizing:border-box}}body{{margin:0;background:#ddd}}.b{{width:1080px;height:1350px;background:{PAPER};color:{INK};font-family:Manrope,Arial,sans-serif;overflow:hidden;position:relative}}.serif{{font-family:Newsreader,Georgia,serif;letter-spacing:-.042em}}.caps{{font-size:15px;font-weight:700;letter-spacing:.18em;text-transform:uppercase}}{extra}"""
    return f'<!doctype html><meta charset=utf-8><style>{css}</style><div class=b>{body}</div>'

def topbar(number,light=False):
    c='white' if light else INK
    return f'<div class="caps" style="position:absolute;z-index:4;left:48px;right:48px;top:42px;color:{c};display:flex;justify-content:space-between;text-shadow:{"0 2px 14px rgba(0,0,0,.35)" if light else "none"}"><span>Gigi Mironova</span><span>Property Dossier · {number}</span></div>'

def reveal():
    p=enc('unit-124-open-plan.jpg')
    return shell(f'''{topbar('01',True)}<img src="{p}" style="width:100%;height:850px;object-fit:cover;filter:saturate(.84) contrast(1.03)"><section style="height:500px;padding:48px 58px"><div class=caps style="color:{CLAY}">Now presenting · Reseda</div><div class=serif style="font-size:78px;line-height:.94;margin-top:18px">A calmer way<br>to come home.</div><div style="margin-top:30px;border-top:1px solid {LINE};padding-top:22px;display:flex;justify-content:space-between;font-size:20px;color:{MUTED}"><span>19350 Sherman Way · Unit 124</span><span>$319,999</span></div></section>''')

def feature():
    p=enc('unit-124-kitchen.jpg')
    return shell(f'''{topbar('02')}<section style="padding:112px 58px 38px"><div class=caps style="color:{CLAY}">Feature story · Everyday ease</div><div class=serif style="font-size:76px;line-height:.95;margin-top:20px">The upgrade you use<br>three times a day.</div></section><img src="{p}" style="width:100%;height:715px;object-fit:cover;object-position:50% 46%;filter:saturate(.82)"><section style="padding:34px 58px;display:grid;grid-template-columns:1fr 1fr;gap:44px;font-size:20px;line-height:1.45;color:{MUTED}"><div>Modern kitchen, updated appliances and storage that keeps the counters clear.</div><div style="border-left:1px solid {LINE};padding-left:38px"><span class=caps style="color:{INK}">The detail</span><br>Appliances purchased December 2023.</div></section>''')

def finance():
    p=enc('unit-124-living.jpg')
    return shell(f'''{topbar('03',True)}<div style="height:785px;position:relative"><img src="{p}" style="width:100%;height:100%;object-fit:cover;filter:saturate(.82) contrast(1.02)"></div><section style="height:565px;padding:48px 58px;display:flex;flex-direction:column"><div class=caps style="color:{CLAY}">The first-month ledger</div><div class=serif style="font-size:82px;line-height:.95;margin-top:20px">$158 more leaves.<br><span style="color:{CLAY}">$224</span> remains yours.</div><div style="height:1px;background:{INK};opacity:.25;margin:28px 0 20px"></div><div style="display:grid;grid-template-columns:1.25fr .75fr;gap:44px;font-size:20px;line-height:1.45;color:{MUTED}"><div>Same apartment. The ownership payment is higher—but part becomes principal instead of disappearing as rent.</div><div>Estimate, not a quote.<br>Full breakdown available.</div></div><div style="margin-top:auto;display:flex;justify-content:space-between;align-items:end"><span class=caps>DRE 02025393 · Equity Union</span><span class=serif style="font-size:43px">DM <b style="color:{CLAY};font-weight:500">“124”</b></span></div></section>''')

def openhouse():
    p=enc('unit-124-building.jpg')
    return shell(f'''{topbar('04',True)}<div style="height:770px;position:relative"><img src="{p}" style="width:100%;height:100%;object-fit:cover;filter:saturate(.78) contrast(1.04)"><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,34,49,.04),rgba(10,34,49,.58))"></div><div style="position:absolute;left:58px;bottom:52px;color:white"><div class=caps>Open house invitation</div><div class=serif style="font-size:90px;line-height:.9;margin-top:18px">Come see<br>what fits.</div></div></div><section style="padding:48px 58px"><div style="display:grid;grid-template-columns:1fr 1fr;gap:55px"><div><div class=caps style="color:{CLAY}">Showing schedule</div><div class=serif style="font-size:48px;margin-top:10px">By appointment</div></div><div><div class=caps style="color:{CLAY}">Address</div><div style="font-size:22px;line-height:1.45;margin-top:13px">19350 Sherman Way<br>Unit 124 · Reseda</div></div></div><div style="border-top:1px solid {LINE};margin-top:38px;padding-top:28px;display:flex;justify-content:space-between;align-items:end"><div style="font-size:20px;line-height:1.5;color:{MUTED}">Tour the open plan, updated kitchen<br>and private balcony in person.</div><div class=serif style="font-size:45px">DM <span style="color:{CLAY}">“TOUR”</span></div></div></section>''')

def deck_page(kicker,title,body,visual='',footer='Gigi Mironova · Identity gift'):
    return shell(f'''<div style="padding:64px 70px;height:100%;display:flex;flex-direction:column"><div class=caps style="color:{CLAY}">{kicker}</div><div class=serif style="font-size:82px;line-height:.93;margin-top:24px;max-width:900px">{title}</div>{visual}<div style="font-size:23px;line-height:1.55;color:{MUTED};max-width:820px;margin-top:34px">{body}</div><div class=caps style="margin-top:auto;border-top:1px solid {LINE};padding-top:22px;display:flex;justify-content:space-between"><span>{footer}</span><span>House Sellers · Equity Union</span></div></div>''')

def deck():
    calm=base64.b64encode((SAFE/'png'/'01-c1-same-door.png').read_bytes()).decode()
    hero=base64.b64encode((ROOT/'editorial-refinement'/'png'/'hero.png').read_bytes()).decode()
    pages={}
    pages['gift-01']=deck_page('A considered gift','A recognizable<br>way to show up.','A two-mode content identity built around the work you already do well: helping people understand the decision, then helping them see the property.','<div style="margin-top:58px;height:520px;background:'+NAVY+';display:flex;align-items:center;justify-content:center;color:'+PAPER+'"><div class=serif style="font-size:104px;text-align:center;line-height:.88">The Calm Closer<br><span style="color:#DCA38E">meets</span><br>Property Dossier</div></div>')
    pages['gift-02']=deck_page('The recurring identity','The Calm Closer','For education, market intelligence and document authority. Calm, direct and repeatable enough to become recognizable over time.','<img src="data:image/png;base64,'+calm+'" style="margin-top:48px;width:500px;height:625px;object-fit:cover;align-self:center;border:1px solid '+LINE+'">')
    pages['gift-03']=deck_page('The campaign mode','The Property Dossier','For listing reveals, feature stories, open houses and seller moments. The photography earns attention; the information design earns trust.','<img src="data:image/png;base64,'+hero+'" style="margin-top:48px;width:500px;height:625px;object-fit:cover;align-self:center;border:1px solid '+LINE+'">')
    pages['gift-04']=deck_page('How the system works','One identity.<br>Two distinct jobs.','The systems share color, restraint and point of view. They do not share every layout. That separation keeps educational content recognizable and listing content visually desirable.','<div style="margin-top:70px;display:grid;grid-template-columns:1fr 1fr;gap:26px"><div style="background:'+NAVY+';color:'+PAPER+';padding:42px"><div class=caps>Always on</div><div class=serif style="font-size:54px;margin-top:20px">Explain the decision.</div></div><div style="border:2px solid '+NAVY+';padding:40px"><div class=caps>When listing</div><div class=serif style="font-size:54px;margin-top:20px">Show the property.</div></div></div>')
    pages['gift-05']=deck_page('Ready to use','Four launch moments,<br>already designed.','Reveal the listing. Tell one feature story. Make the economics understandable. Invite the next action. Each board has one job and one dominant visual.','<div style="margin-top:65px;display:grid;grid-template-columns:repeat(4,1fr);gap:16px">'+''.join(f'<div><div class=caps style="color:{CLAY}">0{i}</div><div style="font-size:22px;margin-top:12px">{x}</div></div>' for i,x in enumerate(['Reveal','Feature','Finance','Open house'],1))+'</div>')
    pages['gift-06']=deck_page('The invitation','Keep what feels like you.<br>Use what helps.','This is not a demand to rebrand. It is a working demonstration of what your content could become when the information, photography and packaging receive the same care you give your clients.','<div style="margin-top:72px;border-top:5px solid '+CLAY+';padding-top:38px"><div class=serif style="font-size:57px">Built as a gift.<br>Designed to be useful now.</div></div>')
    return pages

def image_standard():
    imgs=[('HERO',enc('unit-124-open-plan.jpg'),'Depth + spatial promise'),('FEATURE',enc('unit-124-kitchen.jpg'),'One subject, clean proof'),('INVITE',enc('unit-124-building.jpg'),'Exterior establishes arrival')]
    cards=''.join(f'<div><img src="{p}" style="width:100%;height:245px;object-fit:cover"><div class=caps style="margin-top:15px;color:{CLAY}">{k}</div><div style="font-size:18px;margin-top:8px">{t}</div></div>' for k,p,t in imgs)
    return shell(f'''<div style="padding:60px"><div class=caps style="color:{CLAY}">Property Dossier · Image standard</div><div class=serif style="font-size:70px;line-height:.95;margin-top:20px">Let the photograph<br>do one clear job.</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:46px">{cards}</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:50px;margin-top:48px;border-top:1px solid {LINE};padding-top:36px"><div><div class=caps>Choose</div><div style="font-size:19px;line-height:1.55;color:{MUTED};margin-top:15px">Spatial depth · natural light · clean verticals · one focal point · room destination visible · useful negative space</div></div><div><div class=caps>Reject</div><div style="font-size:19px;line-height:1.55;color:{MUTED};margin-top:15px">Equal-photo grids · cluttered overlays · severe wide-angle distortion · tight room crops · decorative filler · generic stock</div></div></div><div style="margin-top:42px;background:{NAVY};color:{PAPER};padding:28px 32px;display:flex;justify-content:space-between;align-items:center"><div><div class=caps>Mobile rule</div><div style="font-size:20px;margin-top:8px">If image and headline compete, remove copy before shrinking it.</div></div><div class=serif style="font-size:54px">56%+</div></div></div>''')

def main():
    assets={'01-reveal':reveal(),'02-feature':feature(),'03-financial':finance(),'04-open-house':openhouse(),'image-standard':image_standard()}
    assets.update(deck())
    manifest={'concept':'Property Dossier launch system','assets':{}}
    for name,html in assets.items():
        (HERE/f'{name}.html').write_text(html)
        manifest['assets'][name]={'width':1080,'height':1350}
    (HERE/'manifest.json').write_text(json.dumps(manifest,indent=2))
    print(f'built {len(assets)} assets')

if __name__=='__main__': main()
