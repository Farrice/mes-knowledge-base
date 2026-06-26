# Lulu Cheng Meservey — Use Cases & Workflow Routing

> Specific deployment scenarios mapped to the matching workflow. When a request
> sounds like one of the situations below, load `genius.md` first, then invoke
> the named workflow. The 16 workflows are NOT interchangeable — most failures
> are routing failures (running a build engine when you needed a radar, or a
> timing engine when you needed a stance). The "Pick the right one" section at
> the bottom resolves the ambiguous pairs.

## The 16 workflows at a glance

| Workflow | One-line job | Produces |
|---|---|---|
| `lulu-m3-matrix` | The load-bearing campaign engine: Message→Medium→Messenger, in that order | PMF-tested message + medium map + messenger matrix, gravity-welled to one goal |
| `lulu-founder-brand-os` | Stand up an always-on founder comms operating system (not a campaign) | 5-subsystem standing OS: channel map, ship-to-yap cadence, deterrence score, voice spec, slogan engine |
| `lulu-line-in-sand` | Engineer a bold stance gerrymandered around your own people | A polarizing position that lifts loyalty AND recruiting simultaneously |
| `lulu-reality-architect` | Install a new operating truth in a market that believes something limiting | Named reality + mechanism + self-reinforcing loops + installation piece |
| `lulu-strategic-wrongness` | Stake the contrarian position before the crowd arrives | One scored early-but-right position + conviction backing to hold it |
| `lulu-erogenous-zones` | The radar: map an audience's obsession landscape and read each zone | Ranked list of already-open receptors to attach a message to |
| `lulu-viral-trajectory` | The timing engine: which topic to post NOW, wait on, or never touch | GO / WAIT / KILL verdict per topic, netted against your production lead time |
| `lulu-zeitgeist-content` | The production engine: turn charged zones into an ongoing calendar | Content calendar + hooks + ready-to-ship posts that surf the current |
| `lulu-conviction-copy` | Write copy that installs a belief instead of explaining one | Belief-architecture copy with the conviction layer intact |
| `lulu-launch-comms` | Engineer a launch that breaks through AND converts the spike | Launch angle + M3 package + 2-click conversion infra + harvest sequence |
| `lulu-authenticity-engineering` | Make TRUE things FEEL true (the Obama "um", the TikTok-in-the-car) | Truth-gated content with corporate signals stripped, spontaneity injected |
| `founder-narrative-voice-architecture` | Build the founder's uncopyable voice + first-person manifesto | Founder identity + reality-shaping manifesto + behavioral-commitment mechanics |
| `cultural-positioning-differentiation` | Find the cultural hook / draw the line to win market share | Strategic positioning + zeitgeist-entry roadmap |
| `attention-conversion-momentum-management` | Convert a viral/crisis moment into business value | Attention-to-value + crisis response protocol |

---

## Use cases by trigger

### Founder voice, identity & manifesto

| Scenario | Workflow |
|---|---|
| "Our founder needs a public persona / a voice that's unmistakably theirs." | `founder-narrative-voice-architecture` |
| "Write the founder's first-person manifesto declaring our new direction." | `founder-narrative-voice-architecture` |
| "The founder sounds like a VP of marketing — make them sound like a real person." | `founder-narrative-voice-architecture` → `lulu-authenticity-engineering` |
| "Stand up a standing comms system for the founder, not a one-off post." | `lulu-founder-brand-os` |
| "How should the founder show up across social, blog, events, regulators over the next year?" | `lulu-founder-brand-os` |
| "We keep going quiet between launches and the authority never compounds." | `lulu-founder-brand-os` (ship-to-yap + deterrence subsystems) |

### Positioning, stance & market belief

| Scenario | Workflow |
|---|---|
| "We blend in with competitors — give us a position only our tribe will love." | `cultural-positioning-differentiation` or `lulu-line-in-sand` |
| "Take a bold stand without splitting our own customer base." | `lulu-line-in-sand` |
| "Pick the enemy / draw the line in the sand." | `lulu-line-in-sand` |
| "The whole market believes X and we think X is going false — make our view the new truth." | `lulu-reality-architect` |
| "Create a category / name a movement / make our thesis 'the writing on the wall'." | `lulu-reality-architect` |
| "Give us the one contrarian position to plant a flag on before it's safe." | `lulu-strategic-wrongness` |
| "Stress-test industry consensus for where it's quietly cracking." | `lulu-strategic-wrongness` |

### Audience research & timing

| Scenario | Workflow |
|---|---|
| "What is our audience already obsessed with / what are they feeling but not saying?" | `lulu-erogenous-zones` |
| "Which cultural topics are charged right now, and what's their valence?" | `lulu-erogenous-zones` |
| "Of these 8 topics, which do I post this week and which do I skip?" | `lulu-viral-trajectory` |
| "Is 'founder mode' still worth posting about or is it burned?" | `lulu-viral-trajectory` |
| "Will I arrive at the peak or the cringe given how long it takes us to produce?" | `lulu-viral-trajectory` |

### Content production

| Scenario | Workflow |
|---|---|
| "Build us a content calendar that rides the culture instead of fighting it." | `lulu-zeitgeist-content` |
| "Give me hooks + ready-to-ship posts for the next month." | `lulu-zeitgeist-content` |
| "Turn this charged obsession-landscape into a feed-the-beast weekly engine." | `lulu-zeitgeist-content` |
| "Our content bounces off a wall of indifference — fix why." | `lulu-erogenous-zones` first, then `lulu-zeitgeist-content` |

### Copy & persuasion

| Scenario | Workflow |
|---|---|
| "Write copy that changes what the reader believes, not just informs them." | `lulu-conviction-copy` |
| "The reader has to believe X before they'll buy — install that belief." | `lulu-conviction-copy` |
| "This landing page is grammatically perfect and totally dead." | `lulu-conviction-copy` (conviction layer) |
| "Lead with the reader's world, not our offer." | `lulu-conviction-copy` (candy coating layer; supplies belief layer inside `copy-engine`) |

### Launch, attention & crisis

| Scenario | Workflow |
|---|---|
| "We're launching X — make it break through AND convert." | `lulu-launch-comms` |
| "Pre-wire the conversion path before the noise hits." | `lulu-launch-comms` |
| "We went viral — how do we capture it before it dissipates?" | `lulu-launch-comms` or `attention-conversion-momentum-management` |
| "Crisis / outage / data breach — write the response." | `attention-conversion-momentum-management` (emotional-altitude matching, active-voice ownership) |
| "Turn this attention spike into hires / term sheets / sales." | `attention-conversion-momentum-management` |

### Authenticity & realness

| Scenario | Workflow |
|---|---|
| "Make this true thing FEEL true / strip the corporate stiffness." | `lulu-authenticity-engineering` |
| "Engineer the unguarded moment (the car TikTok, the inserted 'um')." | `lulu-authenticity-engineering` |
| "This reads fake even though it's true — close the gap." | `lulu-authenticity-engineering` |

### Foundational campaign (start here when unsure)

| Scenario | Workflow |
|---|---|
| "Run a full comms campaign for us — where do we start?" | `lulu-m3-matrix` (forge the message first; everything else assumes this is done) |
| "Who should say what, where?" | `lulu-m3-matrix` (messenger matrix + medium map) |
| "We have a great message but it's not landing." | Check medium/messenger via `lulu-m3-matrix`; the message may be fine but in the wrong pocket |

---

## Pick the right one (the ambiguous pairs)

These pairs get confused constantly. Resolve before invoking.

- **`lulu-erogenous-zones` vs. `lulu-viral-trajectory` vs. `lulu-zeitgeist-content`** — three stages of one pipeline, not substitutes. Zones = *which* receptors are charged (the radar). Trajectory = *when* to fire on a topic you're already considering (the timing engine). Zeitgeist-content = the *build* (calendar + posts). Order: zones → trajectory → zeitgeist-content. If you're drafting copy in the trajectory workflow, you're in the wrong one.

- **`lulu-reality-architect` vs. `founder-narrative-voice-architecture`** — Reality-architect changes what the *market believes is true* (belief-installation engine for a whole field). Founder-narrative changes what one *founder's audience does* (voice DNA + first-person manifesto + behavioral commitment). Founder-narrative makes you sound like you; reality-architect makes the market think in your terms.

- **`lulu-line-in-sand` vs. `lulu-strategic-wrongness`** — Line-in-sand engineers a *stance gerrymandered around your people* (us-who-believe vs. an external old way). Strategic-wrongness finds the *early contrarian position* before consensus catches up (it's about timing and being right-early, not about uniting a base). A strategic-wrongness position often becomes the content *inside* a line-in-the-sand.

- **`lulu-line-in-sand` vs. `cultural-positioning-differentiation`** — Line-in-sand is the focused stance-engineering primitive. Cultural-positioning is the broader roadmap (positioning + zeitgeist entry) that may *contain* a line-in-the-sand as one component. Use line-in-sand when the deliverable is the stance; use cultural-positioning when it's the whole differentiation strategy.

- **`lulu-launch-comms` vs. `attention-conversion-momentum-management`** — Launch-comms is *proactive* (engineer a planned launch backwards from one business goal, with the 2-click path pre-built). Attention-conversion is *reactive* (a moment already happened — viral spike or crisis — capture or contain it). Launch = before; attention-conversion = during/after, and it's the one that handles crisis.

- **`lulu-m3-matrix` vs. everything** — M3 is the foundation every other workflow assumes is done. If the message itself isn't dialed, run M3 first; a perfect medium and messenger carrying a weak message is "selling encyclopedias nobody wants."

- **`lulu-conviction-copy` vs. `copy-engine` / `luke-iha-*`** — Lulu supplies the *belief-architecture and conviction layer*, not the full offer-and-proof structure. Use `lulu-conviction-copy` to engineer what the reader must believe; wire it INSIDE `copy-engine` / `luke-iha` for the complete piece. Lulu is the architect of belief, not the writer of every line.

---

## Always-on gates (run before any workflow)

Regardless of which workflow you route to, run `genius.md § Decision Framework` first. The three that veto fastest:

1. **Q1 — Business goal:** names exactly one of recruiting / fundraising / sales / regulatory? If the honest answer is "attention," it's a dopamine sugar high — stop.
2. **Q2 — Two comms tests:** (a) Could you say this without the CTA in the next sentence? (b) If your company didn't exist, what could you say that makes the audience feel understood? Pure self-interest = rewrite.
3. **Q7 — Realness:** would this still land if the audience knew exactly how it was made? Manufactured authenticity works once. You get one bullet.

And the cross-cutting honesty spine: **every technique amplifies a claim that is already TRUE.** Point any workflow at a hollow thing and you've built the most efficient possible machine for getting caught.
