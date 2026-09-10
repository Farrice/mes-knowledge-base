#!/usr/bin/env python3
"""Build the single acceptance fixture for Gigi's editorial recovery."""
import base64
from pathlib import Path

HERE=Path(__file__).parent
ASSETS=HERE.parent/'same-door'/'canvas-assets'
PAPER='#F3F0E9'; INK='#163A52'; SLATE='#607887'; CLAY='#C47C63'; LINE='#C8D4D9'

def enc(name):
    return 'data:image/jpeg;base64,'+base64.b64encode((ASSETS/name).read_bytes()).decode()

def main():
    living=enc('unit-124-open-plan.jpg'); kitchen=enc('unit-124-kitchen.jpg')
    html=f'''<!doctype html><meta charset=utf-8><style>
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');
    *{{box-sizing:border-box}}body{{margin:0}}.b{{width:1080px;height:1350px;background:{PAPER};color:{INK};font-family:Manrope,Arial,sans-serif;overflow:hidden}}.caps{{font-size:15px;font-weight:800;letter-spacing:.19em;text-transform:uppercase}}
    </style><div class=b>
      <header style="height:116px;padding:40px 52px 0;display:flex;justify-content:space-between;border-bottom:1px solid {LINE}">
        <span class=caps>Gigi Mironova · DRE 02025393</span><span class=caps style="color:{SLATE}">Unit 124 / Reseda</span>
      </header>
      <section style="height:724px;display:grid;grid-template-columns:2.18fr 1fr;gap:10px;background:{PAPER};padding-top:10px">
        <div style="position:relative;overflow:hidden"><img src="{living}" style="width:100%;height:100%;object-fit:cover;object-position:54% 50%;filter:saturate(.86) contrast(1.025)"><div style="position:absolute;left:34px;bottom:32px;background:{INK};color:white;padding:13px 16px" class=caps>Living / dining</div></div>
        <div style="position:relative;overflow:hidden"><img src="{kitchen}" style="width:100%;height:100%;object-fit:cover;object-position:48% 50%;filter:saturate(.84) contrast(1.025)"><div style="position:absolute;left:22px;bottom:32px;background:{CLAY};color:white;padding:13px 16px" class=caps>Kitchen</div></div>
      </section>
      <main style="height:510px;padding:44px 52px 40px;position:relative">
        <div style="display:grid;grid-template-columns:208px 1fr;gap:38px;align-items:start">
          <div><div class=caps style="color:{CLAY}">Listing note 01</div><div style="height:4px;background:{CLAY};width:66px;margin-top:18px"></div></div>
          <div style="font-size:72px;font-weight:800;letter-spacing:-.055em;line-height:.91;text-transform:uppercase">Remodeled.<br><span style="color:{SLATE}">December 2023.</span></div>
        </div>
        <div style="margin-top:38px;border-top:1px solid {LINE};padding-top:26px;display:grid;grid-template-columns:1.28fr .72fr;gap:50px">
          <div style="font-size:22px;line-height:1.45;color:{SLATE}">The entire unit was remodeled in December 2023—including the kitchen appliances and in-unit washer and dryer.</div>
          <div><div class=caps style="color:{INK}">19350 Sherman Way</div><div style="font-size:20px;line-height:1.55;color:{SLATE};margin-top:10px">Unit 124 · Reseda<br>$319,999</div></div>
        </div>
        <footer style="position:absolute;left:52px;right:52px;bottom:34px;display:flex;justify-content:space-between;align-items:end"><span class=caps>House Sellers · Equity Union</span><span style="font-size:28px;font-weight:700">DM <span style="color:{CLAY}">“124”</span></span></footer>
      </main>
    </div>'''
    (HERE/'recovery-proof.html').write_text(html)
    print('recovery proof built')

if __name__=='__main__': main()

