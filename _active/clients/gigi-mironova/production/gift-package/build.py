#!/usr/bin/env python3
"""Build the final three-board Gigi gift, client close, and internal overview."""
import base64,json
from pathlib import Path

HERE=Path(__file__).parent
PROD=HERE.parent
RECOVERY=PROD/'editorial-recovery'
SAFE=PROD/'same-door'
PAPER='#F3F0E9'; INK='#163A52'; SLATE='#607887'; CLAY='#C47C63'; LINE='#C8D4D9'
FONTS="""@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');"""

def enc(path):
    mime='image/png' if path.suffix=='.png' else 'image/jpeg'
    return f'data:{mime};base64,'+base64.b64encode(path.read_bytes()).decode()

def board(photo,number,kicker,headline,marker,marker_label,caption,detail):
    return f'''<!doctype html><meta charset=utf-8><style>{FONTS}*{{box-sizing:border-box}}body{{margin:0}}.b{{width:1080px;height:1350px;background:{PAPER};color:{INK};font-family:Manrope,Arial,sans-serif;overflow:hidden;position:relative}}.caps{{font-size:13px;font-weight:800;letter-spacing:.2em;text-transform:uppercase}}</style><div class=b>
    <div style="position:absolute;left:0;top:0;bottom:0;width:10px;background:{CLAY};z-index:8"></div>
    <header style="height:88px;padding:31px 48px 0 58px;display:flex;justify-content:space-between;border-bottom:1px solid {LINE}"><span class=caps>The Calm Closer · Property File 124</span><span class=caps style="color:{SLATE}">Gigi Mironova</span></header>
    <section style="height:760px;position:relative;overflow:hidden"><img src="{photo}" style="width:100%;height:100%;object-fit:cover;object-position:50% 50%;filter:saturate(.82) contrast(1.035)"><div style="position:absolute;left:48px;bottom:34px;background:{PAPER};color:{INK};padding:13px 16px" class=caps>{caption}</div></section>
    <main style="height:502px;padding:38px 48px 34px 58px;position:relative"><div style="display:grid;grid-template-columns:1fr 214px;gap:36px;align-items:start"><div><div class=caps style="color:{CLAY}">{kicker} · 0{number}</div><div style="font-size:68px;font-weight:700;letter-spacing:-.058em;line-height:.91;margin-top:18px">{headline}</div></div><div style="border-left:1px solid {LINE};padding-left:27px;padding-top:22px"><div style="font-size:48px;font-weight:800;letter-spacing:-.06em;line-height:.9;color:{SLATE}">{marker}</div><div class=caps style="margin-top:16px;color:{SLATE}">{marker_label}</div></div></div>
    <div style="margin-top:30px;border-top:1px solid {LINE};padding-top:22px;display:grid;grid-template-columns:1.22fr .78fr;gap:46px"><div style="font-size:19px;line-height:1.5;color:{SLATE}">{detail}</div><div><div class=caps>19350 Sherman Way</div><div style="font-size:18px;line-height:1.5;color:{SLATE};margin-top:8px">Unit 124 · Reseda<br>$319,999</div></div></div>
    <footer style="position:absolute;left:58px;right:48px;bottom:28px;display:flex;justify-content:space-between;align-items:end"><span class=caps>Gigi Mironova · DRE 02025393 · Equity Union</span><span style="font-size:25px;font-weight:700">DM <span style="color:{CLAY}">“124”</span></span></footer></main></div>'''

def overview():
    dossier=enc(RECOVERY/'final-pass.png')
    return f'''<!doctype html><meta charset=utf-8><style>{FONTS}*{{box-sizing:border-box}}body{{margin:0}}.b{{width:1080px;height:1350px;background:{PAPER};color:{INK};font-family:Manrope,Arial,sans-serif;padding:58px;overflow:hidden}}.caps{{font-size:13px;font-weight:800;letter-spacing:.2em;text-transform:uppercase}}</style><div class=b>
    <div class=caps style="color:{CLAY}">A content identity for Gigi Mironova</div><div style="font-size:70px;font-weight:700;letter-spacing:-.06em;line-height:.92;margin-top:22px">One voice.<br>Two useful modes.</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:48px"><section><div style="width:100%;height:570px;background:{INK};color:{PAPER};padding:48px;display:flex;flex-direction:column;justify-content:space-between"><div class=caps style="color:#C9D7DE">The Calm Closer</div><div><div style="font-size:49px;font-weight:700;letter-spacing:-.05em;line-height:.95">Documents.<br>Markets.<br>Decisions.</div><div style="width:74px;height:5px;background:{CLAY};margin-top:32px"></div></div><div class=caps style="color:#C9D7DE">Plain English · Exact details</div></div><div class=caps style="color:{CLAY};margin-top:24px">01 · The Calm Closer</div><div style="font-size:31px;font-weight:700;letter-spacing:-.035em;margin-top:11px">Explain the decision.</div><div style="font-size:18px;line-height:1.5;color:{SLATE};margin-top:12px">Education, documents and market intelligence—clear enough to act on.</div></section>
    <section><img src="{dossier}" style="width:100%;height:570px;object-fit:cover;object-position:50% 40%;border:1px solid {LINE}"><div class=caps style="color:{CLAY};margin-top:24px">02 · Property Dossier</div><div style="font-size:31px;font-weight:700;letter-spacing:-.035em;margin-top:11px">Show the property.</div><div style="font-size:18px;line-height:1.5;color:{SLATE};margin-top:12px">One image, one useful detail and one clear next step for each listing moment.</div></section></div>
    <div style="margin-top:48px;border-top:5px solid {CLAY};padding-top:25px;display:flex;justify-content:space-between;align-items:end"><div style="font-size:24px;font-weight:600;max-width:690px">The same practical authority—adapted to the job the content needs to do.</div><div class=caps>House Sellers · Equity Union</div></div></div>'''

def close_page(theme):
    navy=theme=='navy'
    bg=INK if navy else '#FFFFFF'
    text='#FFFFFF' if navy else INK
    muted='#C8D8E1' if navy else SLATE
    panel='#FFFFFF' if navy else '#F4F7F8'
    panel_text=INK
    rule='#547184' if navy else LINE
    return f'''<!doctype html><meta charset=utf-8><style>{FONTS}*{{box-sizing:border-box}}body{{margin:0}}.b{{width:1080px;height:1350px;background:{bg};color:{text};font-family:Manrope,Arial,sans-serif;overflow:hidden;position:relative}}.caps{{font-size:13px;font-weight:800;letter-spacing:.2em;text-transform:uppercase}}</style><div class=b>
    <div style="position:absolute;left:0;top:0;bottom:0;width:12px;background:{CLAY}"></div>
    <header style="height:108px;margin:0 58px 0 70px;padding-top:42px;display:flex;justify-content:space-between;border-bottom:1px solid {rule}"><span class=caps>Gigi Mironova · House Sellers</span><span class=caps style="color:{muted}">A gift for Gigi</span></header>
    <main style="padding:76px 76px 62px 70px">
      <div class=caps style="color:{CLAY}">Built from Unit 124 · Ready for the next address</div>
      <h1 style="font-size:92px;line-height:.91;letter-spacing:-.068em;margin:27px 0 0;font-weight:700;max-width:900px">The next listing can look unmistakably Gigi.</h1>
      <p style="font-size:25px;line-height:1.48;color:{muted};max-width:790px;margin:38px 0 0">The Unit 124 boards and captions are yours to use. If you want to continue, I’d love to build your next listing launch with you.</p>
      <section style="margin-top:64px;background:{panel};color:{panel_text};padding:42px 46px 40px;display:grid;grid-template-columns:235px 1fr;gap:42px;min-height:262px">
        <div><div class=caps style="color:{CLAY}">One-listing pilot</div><div style="font-size:56px;line-height:.9;font-weight:800;letter-spacing:-.06em;margin-top:20px">4–6<br>assets</div></div>
        <div style="border-left:1px solid {LINE};padding-left:39px;font-size:22px;line-height:1.65;font-weight:600"><div>Property-photo selection</div><div>Custom boards and captions</div><div>Posting sequence and one revision</div></div>
      </section>
      <div style="margin-top:58px;border-top:1px solid {rule};padding-top:31px"><div class=caps style="color:{muted}">If this feels right</div><div style="font-size:32px;font-weight:700;letter-spacing:-.035em;margin-top:9px">Reply <span style="color:{CLAY}">“NEXT LISTING”</span></div></div>
    </main>
    <footer style="position:absolute;left:70px;right:58px;bottom:42px;display:flex;justify-content:space-between" class=caps><span>Made for Gigi</span><span style="color:{muted}">No pressure · Yours to use</span></footer>
    </div>'''

def main():
    (HERE/'01-remodel-date.html').write_text((RECOVERY/'final-pass.html').read_text())
    laundry=enc(RECOVERY/'source-photos'/'14.jpg'); building=enc(RECOVERY/'source-photos'/'1.jpg')
    (HERE/'02-in-unit-laundry.html').write_text(board(laundry,2,"Gigi's listing note",'The laundry<br>stays in the unit.','IN','UNIT','In-unit laundry · Washer + dryer included','The stacked washer and dryer are included and were purchased in December 2023.'))
    (HERE/'03-private-showing.html').write_text(board(building,3,"Gigi's invitation",'See Unit 124<br>in person.','BY','APPT.','Building exterior · 19350 Sherman Way','Private showings are available by appointment. Message “124” to coordinate a time.'))
    (HERE/'identity-overview.html').write_text(overview())
    (HERE/'04-close-white.html').write_text(close_page('white'))
    (HERE/'04-close-navy.html').write_text(close_page('navy'))
    manifest={'assets':{name:{'width':1080,'height':1350} for name in ['01-remodel-date','02-in-unit-laundry','03-private-showing','04-close-white','04-close-navy','identity-overview']}}
    (HERE/'manifest.json').write_text(json.dumps(manifest,indent=2))
    print('gift package built')

if __name__=='__main__': main()
