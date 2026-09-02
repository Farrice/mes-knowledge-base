#!/usr/bin/env python3
"""The presentation for Jen, v2 (2026-09-02): sixteen boards that lead with what she knows, walk broad to specific,
and answer her pushbacks inside the flow without ever labelling them. Plus the saved DM reply card.
Same look as the carousels (Valley Native furniture), her words where they belong, nothing she has to study.
Writes S1..S16 and DM next to itself."""
import pathlib
from gen_valley import (HEAD, SERIF, SIGN, FRAME, INK, STEEL, SOFT, CREAM, HAIR, GREY, DIMC, DIMD, GHOSTD, RULED,
                        svg, valley_map, stamp_mark, it)

OUT = pathlib.Path(__file__).parent
N = 16


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
    <span style="{SERIF} font-style: italic; font-size: 30px; color: {c};">{n}&#8202;/&#8202;{N}</span>
  </div>'''


def board(inner, label, n, dark=False, absolute="", gap=40):
    bg = INK if dark else CREAM
    return f'''<div style="{FRAME} background: {bg}; display: flex; flex-direction: column; justify-content: space-between; padding: 100px;">
{absolute}
{mast(dark)}
  <div style="position: relative; display: flex; flex-direction: column; gap: {gap}px;">
{inner}
  </div>
{foot(label, n, dark)}
</div>'''


def h1(html, dark=False, size=80):
    return f'<div style="font-size: {size}px; font-weight: 600; line-height: 1.12; color: {CREAM if dark else INK}; letter-spacing: -0.015em;">{html}</div>'


def p(html, dark=False, size=32, width=820):
    return f'<div style="font-size: {size}px; line-height: 1.55; color: {SOFT if dark else GREY}; max-width: {width}px;">{html}</div>'


def rows(items, dark=False, size=25, lead=31, pad=20):
    ink = CREAM if dark else INK
    rule = RULED if dark else "#D9D3C8"
    out = ""
    for k, (lead_txt, rest) in enumerate(items):
        out += f'''      <div style="display: flex; gap: 28px; padding: {pad}px 0; border-top: 1px solid {rule};">
        <span style="{SERIF} font-style: italic; font-size: 38px; line-height: 1; color: {STEEL}; width: 60px; flex: none;">{k + 1}</span>
        <div style="display: flex; flex-direction: column; gap: 6px;">
          <span style="font-size: {lead}px; font-weight: 600; color: {ink};">{lead_txt}</span>
          <span style="font-size: {size}px; line-height: 1.45; color: {SOFT if dark else GREY};">{rest}</span>
        </div>
      </div>'''
    return f'<div style="display: flex; flex-direction: column;">{out}</div>'


def panel(title, lines, dark=False, fill=False, size=25):
    """A bordered column: small caps title, then lines."""
    ink = CREAM if dark else INK
    border = RULED if dark else INK
    bg = "rgba(255,255,255,0.06)" if dark else ("#FFFFFF" if fill else "transparent")
    body = "".join(f'<div style="font-size: {size}px; line-height: 1.45; color: {SOFT if dark else GREY};">{l}</div>' for l in lines)
    return f'''<div style="flex: 1; display: flex; flex-direction: column; gap: 16px; border: 2px solid {border}; background: {bg}; padding: 30px 32px;">
      <div style="{SIGN} font-size: 16px; font-weight: 600; letter-spacing: 0.2em; color: {STEEL};">{title}</div>
      {body}
    </div>'''


def loop(size=400):
    """Six stops on a drawn loop. Labels placed by hand."""
    stops = [
        (250, 40, "SOMETHING REAL HAPPENS", "on your streets, this week"),
        (440, 150, "YOU TALK FOR A MINUTE", "one voice memo, your words"),
        (440, 350, "WE BUILD IT", "one video, one slideshow, in the look"),
        (250, 460, "IT OPENS THE DOOR", "an address, a question, or just &#8220;hi&#8221;"),
        (60, 350, "YOU ANSWER", "the reply is already written"),
        (60, 150, "WE LISTEN", "what they wrote decides what&#8217;s next"),
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

# ---------------------------------------------------------------- 1 · cover
slides["S1"] = f'''<div style="{FRAME} background: {CREAM}; display: flex; flex-direction: column; justify-content: space-between; padding: 100px;">
  <div style="position: absolute; right: -200px; top: 152px;">{valley_map(660, 660, SOFT, 2)}</div>
{mast()}
  <div style="position: relative; display: flex; flex-direction: column; gap: 44px;">
    {h1(f'the friend who happens<br>to sell real estate...<br>{it("from here.")}', size=84)}
    <div style="display: flex; align-items: center; gap: 32px;">
      <div style="width: 76px; height: 1px; background: {INK}; flex: none;"></div>
      {p("what i built for you, how it works, what it asks of you, and how it turns into clients.", width=640)}
    </div>
  </div>
{foot("A WALKTHROUGH &#183; ABOUT TWENTY MINUTES", 1)}
</div>'''

# ---------------------------------------------------------------- 2 · four words
slides["S2"] = board(f'''{h1(f'four words, then {it("plain english.")}', size=76)}
{p("everything tonight uses these four. nothing else needs a definition.", size=28)}
{rows([
    ("a reel.", "a forty-second video of you talking, filmed on your phone. it&#8217;s how strangers find you."),
    ("a carousel.", "a post you swipe through, seven slides. people save these and send them to a friend. it&#8217;s how strangers trust you."),
    ("the stamp.", "a small mark on every post: the neighborhood and the zip. over time your grid becomes a map of the valley with you on it."),
    ("the file.", "three one-page guides in your look. you send them to anyone who writes. no form, no catch."),
])}''', "FOUR WORDS, THEN NO MORE JARGON", 2)

# ---------------------------------------------------------------- 3 · posting vs a system
slides["S3"] = board(f'''{h1(f'a post is a billboard.<br>a system is {it("a door.")}', size=70)}
{p("most agents post and hope. this is built so every post has a reason, a job, and a next step.", size=28)}
{rows([
    ("every post starts with something real.", "a rule that changed, a train that&#8217;s coming, a quote that moved. on your streets, this week. never a trend."),
    ("every post has one job.", "one person writes to you. not likes, not views. an address, a question, or just &#8220;hi, i&#8217;ve been meaning to reach out.&#8221; the door is open on every post, and people learn that."),
    ("every reply is already written.", "when they write, you answer the same evening from a saved reply, in your voice. paste, add their name, send."),
    ("what they write back decides what&#8217;s next.", "the questions in your DMs are the plan for next month. nothing is made in a vacuum."),
])}''', "NOT POSTING FOR POSTING&#8217;S SAKE", 3)

# ---------------------------------------------------------------- 4 · the ethos
slides["S4"] = board(f'''{h1(f'people don&#8217;t follow an agent.<br>they follow {it("a person who knows the block.")}', size=58)}
{rows([
    ("you&#8217;re from here.", "van nuys, sherman oaks, the boulevard, the stations. every post is stamped with a neighborhood and a zip. nobody else on your feed can say that honestly."),
    ("you translate the scary parts.", "reserve studies, buydowns, backup insurance. in your posts they become the savings account, paying a little now, the state&#8217;s fire policy. nobody has to feel dumb to follow you."),
    ("you protect people.", "your own words: &#8220;i&#8217;m here for you. that&#8217;s my job. i do this to protect you and your best interest.&#8221; that line ends everything now."),
])}''', "THE ETHOS", 4)

# ---------------------------------------------------------------- 5 · the month, not the post
def month_table():
    hdr = f'''<div style="display: grid; grid-template-columns: 110px 1fr 200px 250px; gap: 0 20px; padding: 0 0 12px; border-bottom: 2px solid {INK};">
      {"".join(f'<span style="{SIGN} font-size: 15px; font-weight: 600; letter-spacing: 0.22em; color: {STEEL};">{h}</span>' for h in ("WEEK", "THE PIECE", "THE SUBJECT", "WHO IT&#8217;S FOR"))}
    </div>'''
    data = [
        ("SEPT 1", "the building has to qualify too", "money", "anyone buying a condo", True),
        ("SEPT 2", "the train down van nuys blvd", "the neighborhood", "everyone who lives here", True),
        ("SEPT 3", "the insurance quote before the offer", "the process", "hillside and move-up buyers", True),
        ("SEPT 4", "just breathe", "you", "anyone awake at 11pm", True),
        ("OCT 1", "when the move-up seller should list", "timing", "sellers", False),
        ("OCT 2", "a $2M listing, in your other voice", "a home", "luxury buyers", False),
        ("OCT 3", "the downsizer&#8217;s story", "a life change", "empty-nesters", False),
        ("OCT 4", "a client&#8217;s first year in the house", "a win", "everyone", False),
    ]
    body = ""
    for wk, piece, subj, who, done in data:
        c = INK if done else GREY
        tag = "" if done else f' <span style="{SIGN} font-size: 13px; letter-spacing: 0.2em; color: {DIMC};">SKETCH</span>'
        body += f'''<div style="display: grid; grid-template-columns: 110px 1fr 200px 250px; gap: 0 20px; padding: 13px 0; border-bottom: 1px solid #D9D3C8; align-items: baseline;">
      <span style="{SIGN} font-size: 15px; font-weight: 600; letter-spacing: 0.2em; color: {STEEL};">{wk}</span>
      <span style="font-size: 25px; font-weight: 600; color: {c};">{piece}{tag}</span>
      <span style="font-size: 23px; color: {GREY};">{subj}</span>
      <span style="font-size: 23px; color: {GREY};">{who}</span>
    </div>'''
    return f'<div style="display: flex; flex-direction: column;">{hdr}{body}</div>'

slides["S5"] = board(f'''{h1(f'the month, {it("not the post.")}', size=70)}
{month_table()}
{p("what repeats: your face, the stamp, the close. what never repeats: the subject, or who it&#8217;s for. first-time buyers are the door people know you by. the whole valley walks through it.", size=23, width=880)}''', "SEPTEMBER IS WRITTEN &#183; OCTOBER IS SKETCHED", 5, gap=32)

# ---------------------------------------------------------------- 6 · how one post becomes a conversation
wheel, stops = loop(400)
labels = "".join(f'''      <div style="display: flex; flex-direction: column; gap: 4px; padding: 12px 0; border-top: 1px solid #D9D3C8;">
        <span style="{SIGN} font-size: 16px; font-weight: 600; letter-spacing: 0.2em; color: {INK};">0{k + 1} &#183; {name}</span>
        <span style="font-size: 25px; line-height: 1.35; color: {GREY};">{sub}</span>
      </div>''' for k, (_, _, name, sub) in enumerate(stops))
slides["S6"] = board(f'''{h1(f'how one post becomes {it("a conversation.")}', size=62)}
    <div style="display: flex; gap: 44px; align-items: center;">
      {wheel}
      <div style="display: flex; flex-direction: column; flex: 1;">{labels}</div>
    </div>
{p("six steps, once a week, paced to your month. the only new work is the minute you talk. everything else is built from it, never before it.", size=25, width=880)}''', "PACED TO YOUR MONTH, NOT A STREAK", 6)

# ---------------------------------------------------------------- 7 · what counts
slides["S7"] = board(f'''{h1(f'we count replies, {it("not likes.")}', size=76)}
{p("most posts get looked at and that&#8217;s it. that&#8217;s fine. only one kind of response counts, and the system already knows the difference.", size=27)}
    <div style="display: flex; gap: 28px;">
      {panel("DOESN&#8217;T COUNT", ["a like.", "a &#128293;.", "&#8220;love this!&#8221;", "a new follower.", "a view from someone in ohio.", "<br>nice. we don&#8217;t chase it. it doesn&#8217;t change the plan."], size=26)}
      {panel("COUNTS", ["a DM with an address.", "&#8220;is this true for my building?&#8221;", "&#8220;we&#8217;re looking this fall.&#8221;", "&#8220;hi, i&#8217;ve been meaning to reach out.&#8221;", "a friend tagged with a question.", "<br>that&#8217;s a person. saved reply, same evening, from you."], fill=True, size=26)}
    </div>''', "A FILTER, NOT A MACHINE", 7)

# ---------------------------------------------------------------- 8 · how this turns into clients (the number board)
def stage(k, name, sub, note):
    return f'''<div style="display: grid; grid-template-columns: 60px 1fr 250px; gap: 0 24px; padding: 18px 0; border-top: 1px solid {RULED}; align-items: center;">
      <span style="{SERIF} font-style: italic; font-size: 38px; line-height: 1; color: {STEEL};">{k}</span>
      <div style="display: flex; flex-direction: column; gap: 4px;">
        <span style="font-size: 30px; font-weight: 600; color: {CREAM};">{name}</span>
        <span style="font-size: 23px; line-height: 1.4; color: {SOFT};">{sub}</span>
      </div>
      <div style="border: 1px solid {RULED}; padding: 12px 16px; display: flex; flex-direction: column; gap: 4px;">
        <span style="{SIGN} font-size: 13px; letter-spacing: 0.22em; color: #7E96B4;">YOUR NUMBER</span>
        <span style="font-size: 22px; color: {SOFT};">{note}</span>
      </div>
    </div>'''

slides["S8"] = board(f'''{h1(f'how this turns {it("into clients.", dark=True)}', dark=True, size=70)}
{p("four stages. the shape is the same as your referral business, pointed at strangers. the numbers are yours to fill in after the first month; until then nothing is promised.", dark=True, size=26)}
    <div style="display: flex; flex-direction: column;">
      {stage(1, "people who see it", "reels bring the strangers. this is the only number that isn&#8217;t about you.", "we&#8217;ll read it off instagram")}
      {stage(2, "people who write", "an address, a question, a &#8220;hi.&#8221; every post ends with the door open, so the people who&#8217;ve been meaning to reach out finally do.", "how many write now, per post?")}
      {stage(3, "real conversations", "you replied the same evening. they replied back. a showing, a lender call, a &#8220;let&#8217;s talk friday.&#8221;", "you already know this from referrals")}
      {stage(4, "closings", "same as always. the conversation is the pipeline; nothing here changes how you close.", "what a normal month looks like")}
    </div>
{p("the honest version: if ten people write in a month and three become real conversations, you&#8217;ve added a second referral source that never sleeps. we&#8217;ll know the real ratio in thirty days.", dark=True, size=23, width=880)}''', "YOUR NUMBERS &#183; NOTHING PROMISED", 8, dark=True, gap=26)

# ---------------------------------------------------------------- 9 · 90 days
slides["S9"] = board(f'''{h1(f'what &#8220;the go-to in the valley&#8221;<br>looks like {it("on your grid.")}', size=62)}
{rows([
    ("a series people collect.", "condos this month, the train next, a $2M listing in your other voice. people collect a series. they scroll past a post."),
    ("a stamp on every post.", "the neighborhood and the zip, same spot every time. recognizable at thumbnail size before anyone reads a word."),
    ("your face on the cover, real valley places inside.", "no stock, no orange, no serif-over-a-warm-photo like the other sixteen agents. the navy line drawings are yours alone."),
    ("the same close, every time.", "&#8220;i&#8217;m here for you. that&#8217;s my job.&#8221; in 90 days it&#8217;s the thing people quote back to you, and nobody wonders whether you have time for them."),
])}''', "IN 90 DAYS", 9)

# ---------------------------------------------------------------- 10 · your week
slides["S10"] = board(f'''{h1(f'your week, {it("about three hours.")}', size=76)}
{rows([
    ("one voice memo.", "sixty seconds on the topic, in your words. everything gets written from it, never before it."),
    ("one filming sitting.", "both reels in one go, kitchen or car. the carousel goes out the day after its reel and does the saving-and-sending work."),
    ("reply the same evening.", "comments and DMs are where the pipeline starts. the reply is written; you paste and add a name. minutes, not writing. people learn you answer, and that becomes the reputation."),
    ("when a post does nothing, nothing happens.", "it&#8217;s not a report card. we read the month, not the tuesday. one quiet post changes no plan."),
])}''', "THE RHYTHM", 10)

# ---------------------------------------------------------------- 11 · slow weeks
slides["S11"] = board(f'''{h1(f'the slow weeks are {it("part of the plan.", dark=True)}', dark=True, size=68)}
{p("three closings and a sick kid is most months. the system is built for that month, not the perfect one.", dark=True, size=27)}
{rows([
    ("there is no streak to protect.", "no post is ever &#8220;late.&#8221; a week you can&#8217;t film is a week that goes quiet, and nobody notices but us."),
    ("the file keeps working.", "anyone who writes still gets the three guides and a reply. that part never needs you on camera."),
    ("a good reel reruns.", "the one that worked in september goes out again in november with a new stamp. nobody remembers; new people see it."),
    ("it resumes when you&#8217;re back.", "one voice memo restarts the whole thing. no makeup posts, no guilt, same rhythm."),
], dark=True)}''', "BUILT FOR THE BUSY MONTH", 11, dark=True)

# ---------------------------------------------------------------- 12 · who does what
slides["S12"] = board(f'''{h1(f'who does {it("what.")}', size=76)}
    <div style="display: flex; gap: 28px;">
      {panel("YOU", ["talk for a minute.", "film in one sitting.", "answer the same evening.", "say &#8220;that&#8217;s not me&#8221; and it&#8217;s gone.", "<br>nothing posts you haven&#8217;t read."], fill=True, size=27)}
      {panel("US", ["find what&#8217;s real this week.", "write it from your memo.", "build the look.", "post it, on schedule.", "read every reply that comes back.", "adjust next month from what people asked.", "<br>you never write a caption from scratch."], size=27)}
    </div>
{p("this is your business. every word is yours before it&#8217;s anyone&#8217;s.", size=28)}''', "YOU HAVE THE LAST WORD ON EVERY WORD", 12)

# ---------------------------------------------------------------- 13 · the file
slides["S13"] = board(f'''{h1(f'what they get when they write: {it("the valley file.")}', size=58)}
{p("content brings strangers to your DMs. this is what you hand them. three one-page guides in this look, your number at the bottom, good for a year. you send it because they wrote. no form, no catch.", size=26)}
{rows([
    ("the four things i read before you write.", "the condo guide. the savings account, the meeting notes, the building&#8217;s insurance, who&#8217;s behind on dues. one page, plain words."),
    ("the insurance question before the offer.", "the hillside guide. what the october 15 change means, the date detail, what the backup policy actually covers."),
    ("the 11pm rate note.", "the calm one. just breathe, the three morning questions, what a buydown is in one sentence."),
    ("pinned to your profile: start here.", "the first thing a stranger sees after a reel makes them curious. who you help, and the file. a bio line that says it in ten words."),
], size=24)}''', "EVERGREEN &#183; SEND IT, DON&#8217;T GATE IT", 13)

# ---------------------------------------------------------------- 14 · what we need from you
slides["S14"] = board(f'''{h1(f'what we need {it("from you.")}', size=76)}
{rows([
    ("three phone photos.", "you on a van nuys sidewalk. you at a condo building&#8217;s front door. you holding an HOA packet. they replace the placeholders on the covers."),
    ("your real take on the train.", "the light-rail piece has an opinion drafted for you. say it your way on a voice memo and it gets rebuilt around that."),
    ("how many you can film in a sitting.", "the plan assumes two reels and one carousel a week. if that&#8217;s too many, say so and it shrinks."),
    ("your three numbers.", "how many people write when you post now. how many warm conversations become clients. what a normal month looks like. that fills in board 8."),
])}''', "THREE PHOTOS, ONE MEMO, FOUR NUMBERS", 14)

# ---------------------------------------------------------------- 15 · if you say yes
slides["S15"] = board(f'''{h1(f'if you say yes, {it("this is how it runs.")}', size=68)}
{rows([
    ("this week.", "three photos, one voice memo on the train, your three numbers. we swap your photos in and post reel 1 and the condo carousel."),
    ("every week after.", "one voice memo from you, two reels and one carousel from us, in the look. you reply the same evening with the saved replies."),
    ("every quarter.", "a short note goes to the people who already know you, in your words, about what changed in the valley. a new neighborhood gets its own stamp. the file gets a new page."),
    ("what you never do.", "post daily. chase trends. say &#8220;top producer.&#8221; write a caption from scratch. explain a lender word without a plain one next to it."),
])}''', "THE RHYTHM, IF YOU WANT IT", 15)

# ---------------------------------------------------------------- 16 · the first post
slides["S16"] = board(f'''{h1(f'the first post is {it("ready.", dark=True)}', dark=True, size=76)}
{rows([
    ("reel 1: the building has to qualify too.", "&#8220;your credit can be perfect... and the condo still falls through.&#8221; forty seconds, kitchen or car."),
    ("then the condo carousel, the next day.", "seven slides in your look, you on the cover and the close."),
    ("then the reply.", "when the first address arrives, the DM is already written in your recap voice. paste, personalize, send."),
], dark=True)}
    <div style="display: flex; gap: 32px; padding-top: 10px;">
      <div style="width: 1px; background: {RULED}; flex: none;"></div>
      <div style="{SERIF} font-style: italic; font-size: 44px; line-height: 1.3; color: {SOFT};">everything works out exactly the way it&#8217;s supposed to.</div>
    </div>''', "JEN SANTULAN &#183; SFV &amp; LOS ANGELES", 16, dark=True)

# ---------------------------------------------------------------- DM · the saved reply
slides["DM"] = board(f'''{h1(f'the saved reply, {it("when an address arrives.")}', size=54)}
{p("save both in instagram under saved replies. paste, add their name, send within the hour. the routing question goes second, never first.", size=26)}
    <div style="display: flex; flex-direction: column; gap: 16px; background: #FFFFFF; border: 2px solid {INK}; padding: 32px 40px;">
      <div style="{SIGN} font-size: 16px; font-weight: 600; letter-spacing: 0.2em; color: {STEEL};">REPLY 1 &#183; THE ADDRESS CAME IN</div>
      <div style="font-size: 29px; line-height: 1.5; color: {INK};">got it... give me a day with the numbers and i&#8217;ll come back with what i&#8217;d read first, what i&#8217;d ask the listing agent, and what we do next. we&#8217;ll go from there.</div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 16px; background: {CREAM}; border: 1px solid {HAIR}; padding: 32px 40px;">
      <div style="{SIGN} font-size: 16px; font-weight: 600; letter-spacing: 0.2em; color: {STEEL};">REPLY 2 &#183; THE NEXT DAY, WITH THE NUMBERS</div>
      <div style="font-size: 26px; line-height: 1.5; color: {INK};">okay, i read it. here&#8217;s what i&#8217;d read first, here&#8217;s the one question i&#8217;d ask the listing agent, and here&#8217;s what i&#8217;d do next. are you actually looking this fall, or just keeping an eye on things? either is fine... i just want to point you the right way.</div>
    </div>''', "SAVED REPLIES &#183; PASTE, PERSONALIZE, SEND", N)

for name, html in slides.items():
    (OUT / f"{name}.dc.html").write_text(HEAD.format(body=html))
print("wrote", len(slides), "deck artboards:", ", ".join(slides))
