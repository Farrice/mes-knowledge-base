#!/usr/bin/env python3
"""Senior art-director pass: preserve the fixture, sharpen crop, type, and Gigi POV."""
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
    *{{box-sizing:border-box}}body{{margin:0}}.b{{width:1080px;height:1350px;background:{PAPER};color:{INK};font-family:Manrope,Arial,sans-serif;overflow:hidden;position:relative}}.caps{{font-size:13px;font-weight:800;letter-spacing:.2em;text-transform:uppercase}}
    </style><div class=b>
      <div style="position:absolute;left:0;top:0;bottom:0;width:12px;background:{CLAY};z-index:8"></div>
      <header style="height:88px;padding:31px 48px 0 58px;display:flex;justify-content:space-between;border-bottom:1px solid {LINE}">
        <span class=caps>The Calm Closer · Property File 124</span><span class=caps style="color:{SLATE}">Gigi Mironova</span>
      </header>
      <section style="height:754px;position:relative;background:{INK}">
        <div style="position:absolute;left:0;top:0;width:73%;height:100%;overflow:hidden"><img src="{living}" style="width:100%;height:100%;object-fit:cover;object-position:58% 54%;filter:saturate(.82) contrast(1.035)"></div>
        <div style="position:absolute;right:0;top:68px;width:29%;height:686px;overflow:hidden;border-left:9px solid {PAPER}"><img src="{kitchen}" style="width:100%;height:100%;object-fit:cover;object-position:52% 50%;filter:saturate(.80) contrast(1.035)"></div>
        <div style="position:absolute;right:0;top:0;width:29%;height:68px;background:{INK};color:white;padding:23px 24px" class=caps>Property file · Detail 01</div>
        <div style="position:absolute;left:44px;bottom:36px;background:{PAPER};color:{INK};padding:12px 15px" class=caps>Living / dining</div>
        <div style="position:absolute;right:23px;bottom:36px;background:{CLAY};color:white;padding:12px 15px" class=caps>Updated kitchen</div>
      </section>
      <main style="height:508px;padding:39px 48px 36px 58px;position:relative">
        <div style="display:grid;grid-template-columns:1fr 214px;gap:36px;align-items:start">
          <div>
            <div class=caps style="color:{CLAY}">Gigi's listing note · 01</div>
            <div style="font-size:68px;font-weight:700;letter-spacing:-.058em;line-height:.91;margin-top:18px">The remodel<br>has a date.</div>
          </div>
          <div style="border-left:1px solid {LINE};padding-left:27px;padding-top:22px">
            <div style="font-size:54px;font-weight:800;letter-spacing:-.06em;line-height:.88;color:{SLATE}">12<span style="color:{CLAY}">.</span>23</div>
            <div class=caps style="margin-top:16px;color:{SLATE}">Completed</div>
          </div>
        </div>
        <div style="margin-top:30px;border-top:1px solid {LINE};padding-top:22px;display:grid;grid-template-columns:1.22fr .78fr;gap:46px">
          <div style="font-size:19px;line-height:1.5;color:{SLATE}">The entire unit was remodeled in December 2023. Kitchen appliances and the in-unit washer and dryer were purchased that month.</div>
          <div><div class=caps>19350 Sherman Way</div><div style="font-size:18px;line-height:1.5;color:{SLATE};margin-top:8px">Unit 124 · Reseda<br>$319,999</div></div>
        </div>
        <footer style="position:absolute;left:58px;right:48px;bottom:30px;display:flex;justify-content:space-between;align-items:end"><span class=caps>Gigi Mironova · DRE 02025393 · Equity Union</span><span style="font-size:25px;font-weight:700">DM <span style="color:{CLAY}">“124”</span></span></footer>
      </main>
    </div>'''
    (HERE/'senior-pass.html').write_text(html)
    print('senior pass built')

if __name__=='__main__': main()
