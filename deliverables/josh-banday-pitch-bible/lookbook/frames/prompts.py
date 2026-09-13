"""Scene-plate prompts for the In-Betweener lookbook frames.

Written in banana-pro-director Mode 3B prose (pure environment; cinema stack folded into the
closing paragraph). Run by run_frames.py — never edit prompts at the command line.
"""

STACK = (
    "Photographed on a real cinema camera on a real studio lot by a real cinematographer, "
    "vintage two-times anamorphic optical character with oval bokeh, gentle horizontal streak "
    "flares only on the practical light sources, soft frame-edge falloff, atmospheric perspective "
    "with visible haze and air density between planes so the far background sits softer and lower "
    "in contrast than the foreground, highlights rolled off gently in a filmic curve never clipping "
    "to pure white, a true black point in the deepest shadows with detail held just above it, "
    "tungsten-balanced color negative motion-picture stock with fine theatrical 35mm grain across "
    "the whole frame, the palette a near-black neutral base with a single warm amber-gold accent "
    "family and a desaturated cream on paper and cups and nothing orange and nothing teal. "
    "Real photographic frame, no legible text or signage anywhere, no readable faces, no CGI, no "
    "plastic, no AI smoothness."
)

FRAMES = {
    "01-hero-key-art": (
        "A wide eye-level static frame across a dark empty soundstage where a single tungsten stage "
        "unit high camera-left throws one hard cone of light down onto a small X of gaffer tape on "
        "the painted floor, the mark sitting a little right of center with empty dark stage around it, "
        "the mood quiet and expectant like the moment before someone steps into a light that was "
        "aimed for somebody else. "
        "Hazer smoke hangs in the beam so the cone reads as a solid shape in the air, and far behind "
        "the mark, out of focus and two stops under, the glossy living-room set of a streaming sitcom "
        "waits with its couch and bookshelf and practical lamps switched off, the flag stands and "
        "cable runs of the stage floor catching only the edge of the spill. "
        "Nothing else is lit; the ceiling grid, the black drapes and the distant stage door dissolve "
        "into the dark with only the faintest amber rim on the grid pipes. "
        + STACK
    ),
    "02-stage-7": (
        "A medium-wide frame from slightly below eye level looking past video village toward a "
        "sitcom living-room set lit for a take, the set bright and glossy and warm in the middle "
        "distance while the near foreground stays dark, a director's chair and two crew members seen "
        "only from behind as silhouettes against the set light, the mood of a room holding its breath "
        "between action and cut. "
        "Two monitors glow on a cart camera-right and paint the nearest silhouette's shoulder in cool "
        "grey, set light spills across the stage floor in a warm pool, hazer smoke makes the key light "
        "beams visible, cable ramps and apple boxes and a C-stand cross the foreground in shadow. "
        "The set itself is a comfortable fake apartment with a couch, a kitchen island and a window "
        "backed by a painted skyline, every practical lamp on it switched on. "
        + STACK
    ),
    "03-craft-services": (
        "A three-quarter medium frame at eye level of a craft services table under a white pop-up "
        "tent on a studio lot in the morning, sunlight coming through the tent fabric as one soft "
        "overhead source, the mood of a place where small deals get made over bad coffee. "
        "Two steel coffee urns, a tray of bagels under cling film, a stack of paper cups, a crumpled "
        "call sheet and a sharpie sit on the folding table in the foreground with the cream of the "
        "paper and cups the only bright tones; behind the table and well out of focus two crew members "
        "in dark work clothes stand mid-conversation with their backs half turned, and beyond them the "
        "beige wall of a soundstage rises into soft haze with a numbered stage door catching the light. "
        + STACK
    ),
    "04-trailer-village": (
        "A wide low frame looking straight down a row of production trailers on a studio lot in late "
        "afternoon, the sun low from camera-right throwing long shadows across the asphalt, the mood "
        "of a street where the size of your door tells everyone what you are worth. "
        "The nearest trailers are enormous and gleaming with their steps down and awnings out, and the "
        "row descends trailer by trailer to a small dented shared unit at the far end with a sheet of "
        "paper taped to its door and a folding chair outside it, the whole line receding into warm "
        "haze with the palm tops and a water tower faint against the sky. "
        + STACK
    ),
    "05-writers-room": (
        "A medium eye-level frame from a dim office corridor toward a closed door with a frosted "
        "glass window, warm light from inside the room spilling through the glass and across the "
        "polished hallway floor toward camera, the mood of a room you are not invited into. "
        "Through the frosted pane the shapes of index cards pinned in rows on a corkboard and a "
        "whiteboard covered in a grid are just legible as shapes and never as words, a coat hangs "
        "on a hook beside the door, and the corridor around the door stays two stops under with a "
        "fire-exit sign glowing faintly far down the hall and a water cooler in near-black shadow. "
        + STACK
    ),
    "06-parking-lot": (
        "A wide static eye-level frame of a studio lot parking structure at night, sodium lamps "
        "overhead throwing amber pools onto wet-looking concrete, marine-layer haze thick enough "
        "that each lamp wears a soft halo, the mood of the only place on the lot where nobody is "
        "performing. "
        "One car parked alone in the middle distance has its interior dome light on and its "
        "driver-side window fogged so nothing inside is readable, the rest of the level is empty "
        "bays and painted lines receding into haze, a stairwell door far camera-left leaks a "
        "sliver of cooler light, and the concrete pillars step away in diminishing contrast. "
        + STACK
    ),
    "07-production-offices": (
        "A medium-wide frame shot through the glass wall of a production office bullpen at night, "
        "fluorescent ceiling panels giving a flat even light across desks stacked with binders and "
        "call sheets and a single warm desk lamp still on in the foreground, the mood of the place "
        "where decisions about people are made without them in the room. "
        "Behind the bullpen a conference room sits behind its own glass with the blinds half "
        "closed, a large whiteboard schedule grid visible only as a pattern of boxes, chairs pushed "
        "back from the table, and the reflection of the corridor lights lies faintly on the near glass "
        "so the whole scene is seen slightly through a layer. "
        + STACK
    ),
}
