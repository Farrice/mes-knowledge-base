"""Jen's lifestyle layout, using local licensed photographs and the existing renderer."""
from pathlib import Path
import importlib.util,shutil,json,zipfile,re
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'execution').is_dir())
HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'kitchen-101'
IMG=ROOT/'_active/clients/jen-listings/04-deliverables/2026-09-01-september-carousels/img'
PH=ROOT/'_active/clients/jen-listings/06-system/valley-editions/photos/jen'
for source,name in [(PH/'listing-04-kitchen.jpg','kitchen.jpg'),(IMG/'vannuys-blvd-2024.jpg','street.jpg'),(IMG/'vannuys-valerio-2024.jpg','street2.jpg'),(PH/'listing-01-exterior.jpg','house.jpg')]:shutil.copyfile(source,HERE/'assets'/name)
spec=importlib.util.spec_from_file_location('valley',ROOT/'_active/clients/jen-listings/06-system/valley-editions/editions.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
v.OUT=HERE/'renders';v.OUT.mkdir(exist_ok=True)
css=(OLD/'fonts/fonts.css').read_text()+f'@font-face{{font-family:Pinyon;src:url("{(HERE/"assets/script.woff2").as_uri()}")}}'+'''
*{box-sizing:border-box}html,body{margin:0;background:#1E3A5F}.page{width:1080px;height:1350px;position:relative;overflow:hidden;color:#F7F5F2;background:#1E3A5F}.abs{position:absolute}.serif{font:400 90px/1.10 'Playfair Display',Georgia;letter-spacing:-3px}.script{font:400 124px/1.2 Pinyon,cursive;letter-spacing:0;color:#C9D4E2}.sans{font:400 38px/1.4 Jost,Arial;letter-spacing:0}.top{left:86px;right:86px;top:73px;display:flex;justify-content:space-between;font:400 23px Jost;letter-spacing:1px}.footer{left:70px;right:70px;bottom:35px;display:flex;justify-content:space-between;font:400 22px Jost;letter-spacing:.2px}.arrow{left:490px;bottom:110px;color:#C9D4E2}.photo{width:100%;height:100%;object-fit:cover}.navy{color:#1E3A5F}.story{height:1920px}.story .top{top:135px}.story .footer{bottom:170px}.center{text-align:center}
'''
v.HEAD='<!doctype html><meta charset="utf-8"><style>'+css+'</style>'
def txt(s,y,size=90,x=86,w=908,cls='serif'):
 return f'<div class="abs {cls}" data-text style="left:{x}px;top:{y}px;width:{w}px;font-size:{size}px">{s}</div>'
def photo(name,y=0,h=1350,pos='center',wash=.28):
 return f'<div class="abs" style="left:0;top:{y}px;width:1080px;height:{h}px"><img class="photo" src="{(HERE/"assets"/name).as_uri()}" style="object-position:{pos}"><div class="abs" style="inset:0;background:rgba(9,23,39,{wash})"></div></div>'
def shade():return '<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(7,19,30,.40),transparent 30%,transparent 67%,rgba(7,19,30,.58))"></div>'
def wrap(s,n,light=False,story=False):
 return '<div class="page '+('navy ' if light else '')+('story' if story else '')+'">'+s+f'<div class="abs top"><span>JEN SANTULAN · THE VALLEY</span><span>@_jiing</span></div>'+('<svg class="abs arrow" width="100" height="40" viewBox="0 0 100 40"><path d="M5 20 H92 M73 2 L92 20 L73 38" fill="none" stroke="currentColor" stroke-width="3"/></svg>' if n<6 and not story else '')+f'<div class="abs footer"><span>Jennifer Santulan · Equity Union · DRE #01914509</span><span>{n:02d} / {"03" if story else "06"}</span></div></div>'
pages=[]
# Reference 1: three photographic bands, oversized editorial headline, script connective.
pages.append(wrap(photo('101.jpg',0,440,'50% 43%',.20)+photo('kitchen.jpg',440,480,'50% 54%',.48)+photo('street2.jpg',920,430,'50% 57%',.34)+shade()+txt('you don’t take the 101.',240,66,x=45,w=990,cls='serif center')+txt('but you really like',490,94,x=45,w=990,cls='script center')+txt('that kitchen.',625,126,x=45,w=990,cls='serif center'),1))
# Reference 2: full-bleed street, left headline, separated lower narrative.
pages.append(wrap(photo('street.jpg',pos='50% 50%',wash=.43)+shade()+txt('right now,',250,99)+txt('you take<br>the streets.',375,109)+txt('you know the turns.<br>you know when to leave.',925,43,cls='sans'),2))
# Keep the 101 marker visible as the photograph's own proof of the subject.
pages.append(wrap(photo('101.jpg',pos='46% 50%',wash=.33)+shade()+txt('“i could get used<br>to the freeway.”',165,91,x=58,w=964,cls='serif center')+txt('maybe.',905,116,x=50,w=980,cls='script center')+txt('let’s try that part too.',1060,43,x=50,w=980,cls='sans center'),3))
# Reference's cafe detail becomes an actual home-coffee vignette.
pages.append(wrap(photo('coffee.jpg',pos='62% 50%',wash=.41)+shade()+txt('before you plan where<br>the coffee maker goes…',220,69)+txt('try the drive.',415,103,cls='script')+txt('from that street to work.<br>at the time you actually leave.<br>then check the way home.',925,39,cls='sans'),4))
# A second street perspective gives the narrative its return trip.
pages.append(wrap(photo('street2.jpg',pos='50% 50%',wash=.43)+shade()+txt('would you still<br>pick this house',245,93,x=50,w=980,cls='serif center')+txt('after that drive?',490,110,x=50,w=980,cls='script center')+txt('the kitchen.<br>the weekday that comes with it.',965,41,x=50,w=980,cls='sans center'),5))
# Reference 5: scene-led closing beat with spacious centered invitation.
pages.append(wrap(photo('kitchen.jpg',pos='60% 50%',wash=.49)+shade()+txt('send this to the<br>person who already<br>picked the kitchen.',310,84,x=60,w=960,cls='serif center')+txt('you know who.',785,114,x=50,w=980,cls='script center')+txt('SAVE IT FOR YOUR NEXT HOUSE TOUR',1183,25,x=40,w=1000,cls='sans center'),6))
for i,s in enumerate(pages,1):v.render(s,str(v.OUT/f'{i:02d}.png'))
v.H=1920
stories=[photo('kitchen.jpg',h=1920,pos='57% 50%',wash=.54)+txt('be honest.',380,135,cls='script')+txt('have you started<br>rearranging the furniture<br>before checking<br>the drive?',625,82)+txt('which one are you?',1400,39,cls='sans'),photo('101.jpg',h=1920,pos='46% 50%',wash=.40)+txt('“i could get used<br>to the freeway.”',370,96)+txt('the 101 gets<br>a vote too.',1240,118,cls='script')+txt('the drive check is in my latest post.',1540,37,cls='sans'),photo('street2.jpg',h=1920,wash=.47)+txt('still love the house<br>after that drive?',395,97)+txt('try the weekday version<br>before you decide.',1250,51,cls='sans')+txt('send this to your house-hunting person.',1540,35,cls='sans')]
for i,s in enumerate(stories,1):v.render(wrap(s,i,story=True),str(v.OUT/f'story-{i:02d}.png'))
from PIL import Image,ImageDraw
for prefix,count,height in [('',6,1350),('story-',3,1920)]:
 cols=3;tw=360;th=round(tw*height/1080);rows=(count+2)//3
 sheet=Image.new('RGB',(1140,rows*(th+44)+24),'#ecebe7')
 for i in range(count):
  im=Image.open(v.OUT/f'{prefix}{i+1:02d}.png').convert('RGB');im.thumbnail((tw,th));sheet.paste(im,(20+(i%3)*380,20+(i//3)*(th+44)))
 sheet.save(HERE/('stories-preview.jpg' if prefix else 'contact-sheet.jpg'),quality=95)
(HERE/'PUBLIC-COPY.txt').write_text('\n\n'.join(re.sub('<[^>]+>',' ',s) for s in pages+stories))
print('Rendered six feed slides and three Stories in the new lifestyle treatment.')
