import React, { useEffect, useState } from "react";
import {
  AbsoluteFill,
  Img,
  Sequence,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
  useDelayRender,
  interpolate,
  Easing,
  CalculateMetadataFunction,
} from "remotion";
import { Video, Audio } from "@remotion/media";
import { TransitionSeries, linearTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { loadFont as loadLocalFont } from "@remotion/fonts";
import { z } from "zod";

// ---------------------------------------------------------------------------
// Fixed spec constants (not manifest-editable — these are the format, not the
// creative). Rendering a different ad means writing a different manifest;
// these three never change.
// ---------------------------------------------------------------------------
export const WIDTH = 1080;
export const HEIGHT = 1920;
export const FPS = 30;

// Meta safe-area: bottom ~250px is reserved for platform UI (like/comment/
// share rail + caption/username block). Captions must clear it. Default sits
// mid-way in the 350-500px-from-bottom zone the brief calls for.
const DEFAULT_CAPTION_BOTTOM_OFFSET = 420;

// ---------------------------------------------------------------------------
// Manifest schema — this is the entire contract. A different ad is a
// different JSON file against this same schema, never a code change.
// ---------------------------------------------------------------------------

const ClipSchema = z.object({
  id: z.string(),
  path: z.string(), // e.g. "assets/clips/H3.mp4" — see normalizeAssetPath()
  label: z.string(), // shown on the slate if the file is missing
  trimInSeconds: z.number().default(0),
  trimOutSeconds: z.number().nullable().default(null),
  targetDurationSeconds: z.number().positive(),
  // Set by scripts/render.mjs + scripts/still.mjs after a real fs.existsSync
  // check. Defaults to true so Remotion Studio preview (which skips that
  // preprocessing step) behaves like a normal Remotion project.
  resolvedExists: z.boolean().default(true),
});

const VoTrackSchema = z.object({
  path: z.string(),
  offsetSeconds: z.number().default(0),
  volumeDb: z.number().default(0),
  resolvedExists: z.boolean().default(true),
});

const VolumeWindowSchema = z.object({
  startSeconds: z.number(),
  endSeconds: z.number(),
  volumeDb: z.number().optional(), // omitted on silenceWindows (implied -Infinity)
});

const MusicSchema = z.object({
  path: z.string(),
  volumeDb: z.number().default(-18),
  duckWindows: z.array(VolumeWindowSchema).default([]),
  silenceWindows: z
    .array(VolumeWindowSchema.omit({ volumeDb: true }))
    .default([]),
  resolvedExists: z.boolean().default(true),
});

const CaptionCueSchema = z.object({
  text: z.string(), // max 6 words per the brief — enforced by convention, not code
  startSeconds: z.number(),
  endSeconds: z.number(),
});

const ThemeSchema = z.object({
  fontFamily: z
    .string()
    .default("'Inter Tight','Inter',-apple-system,'Segoe UI',sans-serif"),
  // Optional local woff2 for pixel-exact Inter Tight (no network call — see
  // README "Fonts" section). Skipped silently if the file isn't present.
  fontFilePath: z.string().optional(),
  fontFileExists: z.boolean().default(false),
  textColor: z.string().default("#F2F1EC"),
  accentColor: z.string(),
  backgroundColor: z.string(),
  brandLabel: z.string().optional(),
  captionBottomOffset: z.number().default(DEFAULT_CAPTION_BOTTOM_OFFSET),
});

const EndCardSchema = z.object({
  productImage: z.string(),
  productImageExists: z.boolean().default(true),
  offerLine: z.string(),
  guaranteeLine: z.string(),
  holdSeconds: z.number().default(4),
  backgroundColor: z.string().optional(),
});

// Image composited ABOVE the clip track for a time window — built for the
// one thing generative video cannot be trusted with: the real product (label
// must be pixel-exact, so it comes from a real PNG, never from the model).
const OverlaySchema = z.object({
  path: z.string(),
  startSeconds: z.number(),
  endSeconds: z.number(),
  xPercent: z.number().default(50), // overlay center, % of frame width
  yPercent: z.number().default(50), // overlay center, % of frame height
  widthPercent: z.number().default(26), // image width, % of frame width
  glow: z.boolean().default(true), // accent radial behind the image — also masks the covered region's edges
  fadeInSeconds: z.number().default(0.4),
  resolvedExists: z.boolean().default(true),
});

export const AdManifestSchema = z.object({
  adName: z.string(),
  crossfadeFrames: z.number().int().min(0).default(0),
  clips: z.array(ClipSchema).min(1),
  overlays: z.array(OverlaySchema).default([]),
  vo: z.array(VoTrackSchema).default([]),
  captions: z.array(CaptionCueSchema).default([]),
  accentWords: z.array(z.string()).default([]),
  music: MusicSchema.optional(),
  theme: ThemeSchema,
  endCard: EndCardSchema,
});

export type AdManifest = z.infer<typeof AdManifestSchema>;
type Clip = z.infer<typeof ClipSchema>;
type Theme = z.infer<typeof ThemeSchema>;

// ---------------------------------------------------------------------------
// Small pure helpers (shared by calculateMetadata and the component tree —
// keep them pure so both sides always agree on the timeline).
// ---------------------------------------------------------------------------

/**
 * Our public dir IS the assets/ folder (see remotion.config.ts), but manifest
 * paths are written as "assets/clips/H3.mp4" so the folder-drop convention
 * reads literally in the JSON. Strip the leading segment before staticFile().
 */
export const normalizeAssetPath = (p: string): string =>
  p.replace(/^assets\//, "");

export const dbToGain = (db: number): number => Math.pow(10, db / 20);

export type TimelineEntry = { startFrame: number; durationInFrames: number };

/** Cumulative clip start/duration in frames, accounting for crossfade overlap. */
export const computeClipTimeline = (
  clips: Pick<Clip, "targetDurationSeconds">[],
  crossfadeFrames: number,
  fps: number
): TimelineEntry[] => {
  const entries: TimelineEntry[] = [];
  let cursor = 0;
  clips.forEach((clip, i) => {
    const durationInFrames = Math.round(clip.targetDurationSeconds * fps);
    const startFrame = i === 0 ? 0 : cursor - crossfadeFrames;
    entries.push({ startFrame, durationInFrames });
    cursor = startFrame + durationInFrames;
  });
  return entries;
};

export const computeEndCardStartFrame = (
  clips: Pick<Clip, "targetDurationSeconds">[],
  crossfadeFrames: number,
  fps: number
): number => {
  const timeline = computeClipTimeline(clips, crossfadeFrames, fps);
  if (timeline.length === 0) return 0;
  const last = timeline[timeline.length - 1];
  return last.startFrame + last.durationInFrames;
};

export const computeTotalDurationInFrames = (
  manifest: Pick<AdManifest, "clips" | "crossfadeFrames" | "endCard">,
  fps: number
): number => {
  const endCardStart = computeEndCardStartFrame(
    manifest.clips,
    manifest.crossfadeFrames,
    fps
  );
  return endCardStart + Math.round(manifest.endCard.holdSeconds * fps);
};

/**
 * Splits `text` on every occurrence of any accentWords entry (case-
 * insensitive, longest match first so phrases like "over 600 reactions"
 * aren't shadowed by a shorter "600" entry) and colors the matched runs with
 * the brand accent, everything else with the base text color.
 */
const renderAccentedText = (
  text: string,
  accentWords: string[],
  accentColor: string,
  baseColor: string
): React.ReactNode => {
  if (accentWords.length === 0) {
    return <span style={{ color: baseColor }}>{text}</span>;
  }
  const escaped = [...accentWords]
    .sort((a, b) => b.length - a.length)
    .map((w) => w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"));
  const regex = new RegExp(`(${escaped.join("|")})`, "gi");
  const parts = text.split(regex);
  const accentSet = new Set(accentWords.map((w) => w.toLowerCase()));
  return parts
    .filter((part) => part.length > 0)
    .map((part, i) => (
      <span
        key={i}
        style={{ color: accentSet.has(part.toLowerCase()) ? accentColor : baseColor }}
      >
        {part}
      </span>
    ));
};

// ---------------------------------------------------------------------------
// calculateMetadata — pure arithmetic over the manifest (no fs/fetch), so it
// behaves identically in Remotion Studio preview and in `remotion render`.
// ---------------------------------------------------------------------------

export const calculateAdMetadata: CalculateMetadataFunction<AdManifest> = async ({
  props,
}) => {
  const durationInFrames = computeTotalDurationInFrames(props, FPS);
  return {
    durationInFrames: Math.max(durationInFrames, FPS), // never render a 0-frame video
    width: WIDTH,
    height: HEIGHT,
    fps: FPS,
    defaultOutName: `${props.adName}.mp4`,
  };
};

// ---------------------------------------------------------------------------
// Visual building blocks
// ---------------------------------------------------------------------------

const Slate: React.FC<{ clip: Clip; theme: Theme }> = ({ clip, theme }) => (
  <AbsoluteFill
    style={{
      backgroundColor: theme.backgroundColor,
      alignItems: "center",
      justifyContent: "center",
      flexDirection: "column",
      gap: 18,
    }}
  >
    <div
      style={{
        fontFamily: theme.fontFamily,
        fontSize: 46,
        fontWeight: 700,
        color: theme.textColor,
        textAlign: "center",
        padding: "0 90px",
      }}
    >
      {clip.label}
    </div>
    <div
      style={{
        fontFamily: theme.fontFamily,
        fontSize: 24,
        color: theme.accentColor,
        opacity: 0.85,
        textAlign: "center",
        padding: "0 90px",
      }}
    >
      MISSING CLIP — drop the file at {clip.path}
    </div>
  </AbsoluteFill>
);

const ClipVisual: React.FC<{ clip: Clip; theme: Theme }> = ({ clip, theme }) => {
  const { fps } = useVideoConfig();
  // Defensive fallback: even if a file passed the pre-render existence check
  // but fails to decode (corrupt/partial upload), fail over to the slate
  // instead of crashing the whole render.
  const [decodeFailed, setDecodeFailed] = useState(false);

  if (!clip.resolvedExists || decodeFailed) {
    return <Slate clip={clip} theme={theme} />;
  }

  // NOTE: despite what the "videos" skill rule text says, @remotion/media's
  // trimBefore/trimAfter are in FRAMES, not seconds (confirmed against the
  // package source: `(trimBefore ?? 0) / fps`). Convert here, once.
  const trimBefore = Math.round(clip.trimInSeconds * fps);
  const trimAfter =
    clip.trimOutSeconds != null
      ? Math.round(clip.trimOutSeconds * fps)
      : Math.round((clip.trimInSeconds + clip.targetDurationSeconds) * fps);

  return (
    <Video
      src={staticFile(normalizeAssetPath(clip.path))}
      trimBefore={trimBefore}
      trimAfter={trimAfter}
      muted // native clip audio is never used — the VO track is the single source of truth
      style={{ width: "100%", height: "100%", objectFit: "cover" }}
      onError={() => {
        setDecodeFailed(true);
        return "fail"; // we render our own Slate fallback; don't let @remotion/media retry internally
      }}
    />
  );
};

const OverlayImage: React.FC<{
  overlay: z.infer<typeof OverlaySchema>;
  theme: Theme;
}> = ({ overlay, theme }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const fadeFrames = Math.max(1, Math.round(overlay.fadeInSeconds * fps));
  const opacity = interpolate(frame, [0, fadeFrames], [0, 1], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const scale = interpolate(frame, [0, fadeFrames], [0.92, 1], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const imgWidth = WIDTH * (overlay.widthPercent / 100);

  return (
    <AbsoluteFill>
      <div
        style={{
          position: "absolute",
          left: `${overlay.xPercent}%`,
          top: `${overlay.yPercent}%`,
          transform: `translate(-50%, -50%) scale(${scale})`,
          opacity,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        {overlay.glow && (
          <div
            style={{
              position: "absolute",
              width: imgWidth * 2.4,
              height: imgWidth * 2.4,
              borderRadius: "50%",
              background: `radial-gradient(circle, ${theme.accentColor}40 0%, ${theme.accentColor}18 40%, transparent 68%)`,
            }}
          />
        )}
        <Img
          src={staticFile(normalizeAssetPath(overlay.path))}
          style={{
            width: imgWidth,
            position: "relative",
            filter: "drop-shadow(0 18px 40px rgba(0,0,0,0.55))",
          }}
        />
      </div>
    </AbsoluteFill>
  );
};

const CaptionCard: React.FC<{
  text: string;
  accentWords: string[];
  theme: Theme;
}> = ({ text, accentWords, theme }) => (
  <AbsoluteFill style={{ justifyContent: "flex-end", alignItems: "center" }}>
    <div
      style={{
        position: "absolute",
        bottom: theme.captionBottomOffset,
        maxWidth: "86%",
        textAlign: "center",
        fontFamily: theme.fontFamily,
        fontSize: 58,
        fontWeight: 700,
        lineHeight: 1.25,
        textShadow: "0 2px 16px rgba(0,0,0,0.6), 0 0 2px rgba(0,0,0,0.4)",
        whiteSpace: "pre-wrap",
      }}
    >
      {renderAccentedText(text, accentWords, theme.accentColor, theme.textColor)}
    </div>
  </AbsoluteFill>
);

const EndCard: React.FC<{
  endCard: AdManifest["endCard"];
  accentWords: string[];
  theme: Theme;
}> = ({ endCard, accentWords, theme }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 12], [0, 1], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: endCard.backgroundColor ?? theme.backgroundColor,
        alignItems: "center",
        justifyContent: "center",
        flexDirection: "column",
        gap: 36,
        opacity,
      }}
    >
      {endCard.productImageExists ? (
        <div
          style={{
            position: "relative",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            width: "100%",
            maxHeight: "48%",
          }}
        >
          <div
            style={{
              position: "absolute",
              width: 720,
              height: 720,
              borderRadius: "50%",
              background: `radial-gradient(circle, ${theme.accentColor}33 0%, ${theme.accentColor}14 40%, transparent 70%)`,
            }}
          />
          <Img
            src={staticFile(normalizeAssetPath(endCard.productImage))}
            style={{ maxWidth: "52%", maxHeight: "100%", objectFit: "contain", position: "relative" }}
          />
        </div>
      ) : (
        <div
          style={{
            width: "52%",
            aspectRatio: "3 / 4",
            border: `2px dashed ${theme.accentColor}`,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            textAlign: "center",
            padding: 24,
            fontFamily: theme.fontFamily,
            color: theme.accentColor,
            fontSize: 22,
          }}
        >
          MISSING PRODUCT IMAGE — {endCard.productImage}
        </div>
      )}
      <div
        style={{
          fontFamily: theme.fontFamily,
          fontSize: 64,
          fontWeight: 800,
          color: theme.textColor,
          textAlign: "center",
          padding: "0 80px",
        }}
      >
        {renderAccentedText(endCard.offerLine, accentWords, theme.accentColor, theme.textColor)}
      </div>
      <div
        style={{
          fontFamily: theme.fontFamily,
          fontSize: 34,
          fontWeight: 500,
          color: theme.textColor,
          opacity: 0.85,
          textAlign: "center",
          padding: "0 90px",
        }}
      >
        {renderAccentedText(endCard.guaranteeLine, accentWords, theme.accentColor, theme.textColor)}
      </div>
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------
// Music bed: base dB, with duck windows (temporary reduction) and silence
// windows (hard mute) layered on top. Both kits close on true silence under
// the final CTA line, so silence always wins and ramps in over ~5 frames
// rather than cutting instantly (avoids an audible pop).
// ---------------------------------------------------------------------------

const RAMP_FRAMES = 5;

const MusicBed: React.FC<{ music: NonNullable<AdManifest["music"]> }> = ({
  music,
}) => {
  const { fps } = useVideoConfig();

  const volume = (frame: number): number => {
    const t = frame / fps;
    const baseGain = dbToGain(music.volumeDb);

    for (const w of music.silenceWindows) {
      if (t >= w.startSeconds - RAMP_FRAMES / fps && t <= w.endSeconds) {
        const rampIn = interpolate(
          t,
          [w.startSeconds - RAMP_FRAMES / fps, w.startSeconds],
          [baseGain, 0],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );
        return t >= w.startSeconds ? 0 : rampIn;
      }
    }

    for (const w of music.duckWindows) {
      if (t >= w.startSeconds && t <= w.endSeconds) {
        return dbToGain(w.volumeDb ?? music.volumeDb);
      }
    }

    return baseGain;
  };

  return (
    <Audio
      src={staticFile(normalizeAssetPath(music.path))}
      volume={(f) => volume(f)}
    />
  );
};

/**
 * Loads a local Inter Tight woff2 if the manifest points at one and
 * scripts/render.mjs confirmed it exists on disk. Zero network calls either
 * way: when absent, the CSS fallback chain in theme.fontFamily silently
 * takes over (Inter, then system sans) — no crash, no fetch.
 */
const useLocalFont = (theme: Theme) => {
  const { delayRender, continueRender } = useDelayRender();
  const [handle] = useState<number | null>(() =>
    theme.fontFileExists && theme.fontFilePath ? delayRender("Loading local Inter Tight font") : null
  );

  useEffect(() => {
    if (handle === null || !theme.fontFilePath) return;
    loadLocalFont({ family: "Inter Tight", url: staticFile(normalizeAssetPath(theme.fontFilePath)) })
      .then(() => continueRender(handle))
      .catch(() => continueRender(handle)); // never block the render over a font
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [handle]);
};

// ---------------------------------------------------------------------------
// Root composition
// ---------------------------------------------------------------------------

export const Ad: React.FC<AdManifest> = (props) => {
  const { fps } = useVideoConfig();
  useLocalFont(props.theme);
  const clipTimeline = computeClipTimeline(props.clips, props.crossfadeFrames, fps);
  const endCardStart = computeEndCardStartFrame(props.clips, props.crossfadeFrames, fps);
  const endCardDuration = Math.round(props.endCard.holdSeconds * fps);

  return (
    <AbsoluteFill style={{ backgroundColor: props.theme.backgroundColor }}>
      {/* --- Clips track --- */}
      {props.crossfadeFrames === 0 ? (
        props.clips.map((clip, i) => (
          <Sequence
            key={clip.id}
            from={clipTimeline[i].startFrame}
            durationInFrames={clipTimeline[i].durationInFrames}
            premountFor={fps}
          >
            <ClipVisual clip={clip} theme={props.theme} />
          </Sequence>
        ))
      ) : (
        <TransitionSeries>
          {props.clips.map((clip, i) => (
            <React.Fragment key={clip.id}>
              {i > 0 && (
                <TransitionSeries.Transition
                  presentation={fade()}
                  timing={linearTiming({ durationInFrames: props.crossfadeFrames })}
                />
              )}
              <TransitionSeries.Sequence
                durationInFrames={clipTimeline[i].durationInFrames}
              >
                <ClipVisual clip={clip} theme={props.theme} />
              </TransitionSeries.Sequence>
            </React.Fragment>
          ))}
        </TransitionSeries>
      )}

      {/* --- Overlay track (real product image over generated footage) --- */}
      {props.overlays
        .filter((o) => o.resolvedExists)
        .map((o, i) => (
          <Sequence
            key={`overlay-${i}`}
            from={Math.round(o.startSeconds * fps)}
            durationInFrames={Math.max(
              1,
              Math.round((o.endSeconds - o.startSeconds) * fps)
            )}
            premountFor={fps}
          >
            <OverlayImage overlay={o} theme={props.theme} />
          </Sequence>
        ))}

      {/* --- Captions track (burned-in, bottom-third, safe-area aware) --- */}
      {props.captions.map((cue, i) => {
        const startFrame = Math.round(cue.startSeconds * fps);
        const durationInFrames = Math.max(
          1,
          Math.round((cue.endSeconds - cue.startSeconds) * fps)
        );
        return (
          <Sequence
            key={i}
            from={startFrame}
            durationInFrames={durationInFrames}
            premountFor={fps}
          >
            <CaptionCard text={cue.text} accentWords={props.accentWords} theme={props.theme} />
          </Sequence>
        );
      })}

      {/* --- VO track(s) --- */}
      {props.vo
        .filter((v) => v.resolvedExists)
        .map((v, i) => (
          <Sequence key={i} from={Math.round(v.offsetSeconds * fps)} premountFor={fps}>
            <Audio src={staticFile(normalizeAssetPath(v.path))} volume={dbToGain(v.volumeDb)} />
          </Sequence>
        ))}

      {/* --- Music bed --- */}
      {props.music && props.music.resolvedExists ? <MusicBed music={props.music} /> : null}

      {/* --- End card --- */}
      <Sequence from={endCardStart} durationInFrames={endCardDuration} premountFor={fps}>
        <EndCard endCard={props.endCard} accentWords={props.accentWords} theme={props.theme} />
      </Sequence>
    </AbsoluteFill>
  );
};
