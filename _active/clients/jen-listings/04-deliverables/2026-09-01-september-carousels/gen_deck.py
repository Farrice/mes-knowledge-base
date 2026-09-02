#!/usr/bin/env python3
"""The presentation for Jen: seven boards that make the whole thing make sense, plus the saved DM reply card.
Same look as the carousels (Valley Native furniture), her words where they belong, nothing she has to study.
Writes S1..S7 and DM next to itself."""
import pathlib
from gen_valley import (HEAD, SERIF, SIGN, FRAME, INK, STEEL, SOFT, CREAM, HAIR, GREY, DIMC, DIMD, GHOSTD, RULED,
                        svg, valley_map, stamp_mark, it)

OUT = pathlib.Path(__file__).parent


def mast(dark=False, right="SEPTEMBER 2026"):
    ink = CREAM if dark else INK
    rule = RULED if dark else HAIR
    dim = DIMD if dark else DIMC
    dim2 = "#7E96B4" if dark else GREY
    return f'''  <div style="position: relative; display: flex; flex-direction: column; gap: 26px;">
    <div style="display: flex; justify-content: space-between; align-items: baseline;">
      <span style="font-size: 28px; font-weight: 500; letter-spacing: 0.24em; color: {ink};">@_JIING</span>
      <span style="font-size: 25px; letter-spacing: 0.24em; color: {dim};">{right}</span>
    </div>
    <div style="height: 1px; background: {rule};"></div>
    <div style="display: flex; align-items: center; gap: 18px; padding-top: 4px;">
      {stamp_mark(44, ink)}
      <div style="display: flex; flex-direction: column; gap: 3px;">
        <span style="{SIGN} font-size: 22px; font-weight: 600; letter-spacing: 0.2em; color: {ink};">SAN FERNANDO VALLEY</span>
        <span style="{SIGN} font-size: 15px; font-weight: 400; letter-spacing: 0.28em; color: {dim2};">FROM THE VALLEY</span>
      </div>
    </div>
  </div>'''


def foot(label, n, dark=False):
    c = DIMD if dark else DIMC
    return f'''  <div style="position: relative; display: flex; justify-content: space-between; align-items: baseline;">
    <span style="font-size: 25px; letter-spacing: 0.22em; color: {c};">{label}</span>
    <span style="{SERIF} font-style: italic; font-size: 30px; color: {c};">{n}&#8202;/&#8202;10</span>
  </div>'''


def board(inner, label, n, dark=False, absolute=""):
    bg = INK if dark else CREAM
    return f'''<div style="{FRAME} background: {bg}; display: flex; flex-direction: column; justify-content: space-between; padding: 100px;">
{absolute}
{mast(dark)}
  <div style="position: relative; display: flex; flex-direction: column; gap: 40px;">
{inner}
  </div>
{foot(label, n, dark)}
</div>'''


def h1(html, dark=False, size=80):
    return f'<div style="font-size: {size}px; font-weight: 600; line-height: 1.12; color: {CREAM if dark else INK}; letter-spacing: -0.015em;">{html}</div>'


def p(html, dark=False, size=32, width=820):
    return f'<div style="font-size: {size}px; line-height: 1.55; color: {SOFT if dark else GREY}; max-width: {width}px;">{html}</div>'


def rows(items, dark=False, size=25):
    ink = CREAM if dark else INK
    rule = RULED if dark else "#D9D3C8"
    out = ""
    for k, (lead, rest) in enumerate(items):
        out += f'''      <div style="display: flex; gap: 28px; padding: 20px 0; border-top: 1px solid {rule};">
        <span style="{SERIF} font-style: italic; font-size: 38px; line-height: 1; color: {STEEL}; width: 60px; flex: none;">{k + 1}</span>
        <div style="display: flex; flex-direction: column; gap: 6px;">
          <span style="font-size: 31px; font-weight: 600; color: {ink};">{lead}</span>
          <span style="font-size: {size}px; line-height: 1.45; color: {SOFT if dark else GREY};">{rest}</span>
        </div>
      </div>'''
    return f'<div style="display: flex; flex-direction: column;">{out}</div>'


def flywheel(size=520):
    """Six stops on a drawn loop. Labels are placed by hand."""
    stops = [
        (250, 40, "LOCAL SIGNAL", "what's actually happening on your streets"),
        (440, 150, "YOUR TAKE", "a 60-second voice memo"),
        (440, 350, "REEL + CAROUSEL", "in the valley native look"),
        (250, 460, "THE ASK", "\"send me the address\""),
        (60, 350, "YOUR REPLY", "the saved DM"),
        (60, 150, "WHAT WE LEARN", "who wrote, what they asked"),
    ]
    circle = svg(size, size, "0 0 500 500", [
        "M250 40 C 366 40 460 134 460 250 C 460 366 366 460 250 460 C 134 460 40 366 40 250 C 40 134 134 40 250 40",
        "M250 40 L262 30 M250 40 L262 50",
        "M460 250 L450 238 M460 250 L470 238",
        "M250 460 L238 450 M250 460 L238 470",
        "M40 250 L50 262 M40 250 L30 262",
    ], stroke=INK, sw=2)
    dots = "".join(f'<div style="position: absolute; left: {x * size / 500 - 11}px; top: {y * size / 500 - 11}px; width: 22px; height: 22px; background: {CREAM}; border: 2px solid {INK}; box-sizing: border-box;"></div>' for x, y, _, _ in stops)
    return f'<div style="position: relative; width: {size}px; height: {size}px; flex: none;">{circle}{dots}</div>', stops


slides = {}

# S1 · cover / the why
slides["S1"] = f'''<div style="{FRAME} background: {CREAM}; display: flex; flex-direction: column; justify-content: space-between; padding: 100px;">
  <div style="position: absolute; right: -200px; top: 152px;">{valley_map(660, 660, SOFT, 2)}</div>
{mast()}
  <div style="position: relative; display: flex; flex-direction: column; gap: 44px;">
    {h1(f'the friend who happens<br>to sell real estate...<br>{it("from here.")}', size=84)}
    <div style="display: flex; align-items: center; gap: 32px;">
      <div style="width: 76px; height: 1px; background: {INK}; flex: none;"></div>
      {p("what we built for september, why it looks the way it does, and what it does for your business.", width=640)}
    </div>
  </div>
{foot("A WALKTHROUGH &#183; ABOUT FIFTEEN MINUTES", 1)}
</div>'''

# S2 · the ethos
slides["S2"] = board(f'''{h1(f'people don&#8217;t follow an agent.<br>they follow {it("a person who knows the block.")}', size=58)}
{rows([
    ("you&#8217;re from here.", "van nuys, sherman oaks, the boulevard, the stations. every post is stamped with a neighborhood and a zip, so the grid slowly becomes a map of the valley with you on it."),
    ("you translate the scary parts.", "reserve studies, buydowns, backup insurance. in your posts they become the savings account, paying a little now, the state&#8217;s fire policy. nobody has to feel dumb to follow you."),
    ("you protect people.", "your own words: &#8220;i&#8217;m here for you. that&#8217;s my job. i do this to protect you and your best interest.&#8221; that line ends everything now."),
])}''', "THE ETHOS", 2)

# S3 · the flywheel
wheel, stops = flywheel(400)
labels = "".join(f'''      <div style="display: flex; flex-direction: column; gap: 4px; padding: 12px 0; border-top: 1px solid #D9D3C8;">
        <span style="{SIGN} font-size: 16px; font-weight: 600; letter-spacing: 0.2em; color: {INK};">0{k + 1} &#183; {name}</span>
        <span style="font-size: 25px; line-height: 1.35; color: {GREY};">{sub}</span>
      </div>''' for k, (_, _, name, sub) in enumerate(stops))
slides["S3"] = board(f'''{h1(f'the {it("flywheel.")}', size=70)}
    <div style="display: flex; gap: 44px; align-items: center;">
      {wheel}
      <div style="display: flex; flex-direction: column; flex: 1;">{labels}</div>
    </div>
{p("one loop, every week. the signal gives you something real to say, the memo makes it yours, the reel earns attention, the carousel earns saves, the ask starts a conversation, your reply keeps it human... and what people write back tells us what to make next.", size=25, width=880)}''', "ONE LOOP, EVERY WEEK", 3)

# S4 · what go-to looks like in 90 days
slides["S4"] = board(f'''{h1(f'what &#8220;go-to agent in the valley&#8221;<br>looks like {it("on your grid.", dark=True)}', dark=True, size=62)}
{rows([
    ("a numbered series.", "first-time buyer file, no. 01, 02, 03... people collect a series. they scroll past a post."),
    ("a stamp on every post.", "the neighborhood and the zip, same spot every time. recognizable at thumbnail size before anyone reads a word."),
    ("your face on the cover, real valley places inside.", "no stock, no orange, no serif-over-a-warm-photo like the other sixteen agents. your navy line drawings are the identity."),
    ("the same close, every time.", "&#8220;i&#8217;m here for you. that&#8217;s my job.&#8221; in 90 days it&#8217;s the thing people quote back to you."),
], dark=True)}''', "IN 90 DAYS", 4, dark=True)

# S5 · your week
slides["S5"] = board(f'''{h1(f'your week, {it("about three hours.")}', size=76)}
{rows([
    ("one voice memo.", "sixty seconds on the topic, in your words. everything gets written from it, never before it."),
    ("two reels, one carousel.", "film both reels in one sitting. the carousel goes out the day after its reel and does the saving-and-sending work."),
    ("reply the same evening.", "comments and DMs are where the pipeline starts. the saved reply is written; you paste and personalize."),
    ("that&#8217;s it.", "no daily posting. no trends. the right pace is the one you can hold without becoming a worse agent."),
])}''', "THE RHYTHM", 5)

# S6 · what we need from you
slides["S6"] = board(f'''{h1(f'what we need {it("from you.")}', size=76)}
{rows([
    ("three phone photos.", "you on a van nuys sidewalk. you at a condo building&#8217;s front door. you holding an HOA packet. they replace the grid grabs on the covers."),
    ("your real take on the train.", "the light-rail reel has an opinion drafted for you. say it your way on a voice memo and it gets rebuilt around that."),
    ("how many you can film in a sitting.", "the plan assumes two reels and one carousel a week. if that&#8217;s too many, say so and it shrinks."),
    ("if a line isn&#8217;t you, say so.", "every script ends on your words. if any of them don&#8217;t sound like you, it&#8217;s gone."),
])}''', "THREE PHOTOS, ONE MEMO, ONE NUMBER", 6)

# S7 · the lead magnet (evergreen)
slides["S7"] = board(f'''{h1(f'what they get when they write: {it("the valley file.")}', size=58)}
{p("content brings strangers to your DMs. this is what you hand them. three one-page guides in this look, your number at the bottom, good for a year. no keyword, no form... you send it because they wrote.", size=27)}
{rows([
    ("the four things i read before you write.", "the condo guide. the savings account, the meeting notes, the building&#8217;s insurance, who&#8217;s behind on dues. one page, plain words."),
    ("the insurance question before the offer.", "the hillside guide. what the october 15 change means, the date detail, what the backup policy actually covers."),
    ("the 11pm rate note.", "the calm one. just breathe, the three morning questions, what a buydown is in one sentence."),
    ("pinned to your profile: start here.", "a permanent post that says who you help and hands out the file. the first thing a new visitor sees."),
])}''', "EVERGREEN &#183; SEND IT, DON&#8217;T GATE IT", 7)

# S8 · the referral loop
slides["S8"] = board(f'''{h1(f'the people who {it("already love you.", dark=True)}', dark=True, size=68)}
{p("you show up for everyone and you never ask. that&#8217;s why they love you, and it&#8217;s why the referrals stopped. the fix isn&#8217;t asking harder. it&#8217;s giving them a reason and a moment.", dark=True, size=27)}
{rows([
    ("the quarterly valley note.", "one text to every past client and close friend, four times a year. what actually changed in the valley this quarter, in your words, useful whether they&#8217;re moving or not. last line, every time: &#8220;if someone you love is thinking about buying, i&#8217;d love to be the first call.&#8221;"),
    ("the one-year text.", "a year after every closing: &#8220;one year in the house. how&#8217;s it treating you?&#8221; the easiest conversation you&#8217;ll ever restart."),
    ("the who-do-you-know moment.", "after every thank-you, one specific ask: &#8220;who&#8217;s the one friend who keeps saying they&#8217;ll never afford LA? send them my way, i&#8217;ve got them.&#8221;"),
    ("the referral reply.", "when a name comes in, the reply is written: &#8220;thank you for trusting me with them. i&#8217;m here for them the way i was here for you.&#8221;"),
], dark=True, size=24)}''', "FOUR TEXTS A YEAR, ONE ASK EACH", 8, dark=True)

# S9 · if you say yes: how it runs
slides["S9"] = board(f'''{h1(f'if you say yes, {it("this is how it runs.")}', size=68)}
{rows([
    ("this week.", "three photos, one voice memo on the train, one number for how many you can film. we swap your photos in and post reel 1 and the condo carousel."),
    ("every week after.", "one voice memo from you, two reels and one carousel from us, in the look. you reply the same evening with the saved replies."),
    ("every quarter.", "the valley note goes to your list. a new neighborhood gets its own stamp. the file gets a new page."),
    ("what you never do.", "post daily. chase trends. say &#8220;top producer.&#8221; write a caption from scratch. explain a lender word without a plain one next to it."),
])}''', "THE RHYTHM, IF YOU WANT IT", 9)

# S10 · the first post
slides["S10"] = board(f'''{h1(f'the first post is {it("ready.", dark=True)}', dark=True, size=76)}
{rows([
    ("reel 1: the building has to qualify too.", "&#8220;your credit can be perfect... and the condo still falls through.&#8221; forty seconds, kitchen or car."),
    ("then the condo carousel, the next day.", "seven slides in the valley native look, you on the cover and the close."),
    ("then the reply.", "when the first address arrives, the DM is already written in your recap voice. paste, personalize, send."),
], dark=True)}
    <div style="display: flex; gap: 32px; padding-top: 10px;">
      <div style="width: 1px; background: {RULED}; flex: none;"></div>
      <div style="{SERIF} font-style: italic; font-size: 44px; line-height: 1.3; color: {SOFT};">everything works out exactly the way it&#8217;s supposed to.</div>
    </div>''', "JEN SANTULAN &#183; SFV &amp; LOS ANGELES", 10, dark=True)

# DM · the saved reply
slides["DM"] = board(f'''{h1(f'the saved reply, {it("when an address arrives.")}', size=54)}
{p("save both in instagram under saved replies. paste, add their name, send within the hour. the routing question goes second, never first.", size=26)}
    <div style="display: flex; flex-direction: column; gap: 16px; background: #FFFFFF; border: 2px solid {INK}; padding: 32px 40px;">
      <div style="{SIGN} font-size: 16px; font-weight: 600; letter-spacing: 0.2em; color: {STEEL};">REPLY 1 &#183; THE ADDRESS CAME IN</div>
      <div style="font-size: 29px; line-height: 1.5; color: {INK};">got it... give me a day with the numbers and i&#8217;ll come back with what i&#8217;d read first, what i&#8217;d ask the listing agent, and what we do next. we&#8217;ll go from there.</div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 16px; background: {CREAM}; border: 1px solid {HAIR}; padding: 32px 40px;">
      <div style="{SIGN} font-size: 16px; font-weight: 600; letter-spacing: 0.2em; color: {STEEL};">REPLY 2 &#183; THE NEXT DAY, WITH THE NUMBERS</div>
      <div style="font-size: 26px; line-height: 1.5; color: {INK};">okay, i read it. here&#8217;s what i&#8217;d read first, here&#8217;s the one question i&#8217;d ask the listing agent, and here&#8217;s what i&#8217;d do next. are you actually looking this fall, or just keeping an eye on things? either is fine... i just want to point you the right way.</div>
    </div>''', "SAVED REPLIES &#183; PASTE, PERSONALIZE, SEND", 10)

for name, html in slides.items():
    (OUT / f"{name}.dc.html").write_text(HEAD.format(body=html))
print("wrote", len(slides), "deck artboards:", ", ".join(slides))
