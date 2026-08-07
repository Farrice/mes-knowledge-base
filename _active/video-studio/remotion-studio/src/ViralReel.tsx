import React from "react";
import {
    AbsoluteFill,
    Sequence,
    useCurrentFrame,
    useVideoConfig,
    interpolate,
    spring,
    staticFile,
    Easing,
} from "remotion";
import { Video } from "@remotion/media";

// ─── SCENE CONFIG ────────────────────────────────────────────────────
// Each scene is a Setup (action) → Punchline (reaction/face) pair.
// All times are in SECONDS relative to the SOURCE video.
//
// HOW TO TUNE:
//   1. Open Remotion Studio → select ViralReel
//   2. Scrub the source video to find exact cut points
//   3. Update the timestamps below
//   4. The composition auto-calculates durations and frame offsets

interface SceneConfig {
    setupStart: number;    // When the setup action begins in source video
    setupEnd: number;      // When it ends (cut point)
    punchStart: number;    // When the punchline/reaction starts
    punchEnd: number;      // When it ends
    setupText: string;     // Text overlay during setup
    punchText: string;     // Text overlay during punchline
}

const SCENES: SceneConfig[] = [
    {
        setupStart: 0.0,
        setupEnd: 2.0,
        punchStart: 2.0,
        punchEnd: 3.5,
        setupText: "When he asks me to try it...",
        punchText: "I DO 💍",
    },
    {
        setupStart: 3.5,
        setupEnd: 5.5,
        punchStart: 5.5,
        punchEnd: 7.0,
        setupText: "When he says watch this...",
        punchText: "I DO 💍",
    },
    {
        setupStart: 7.0,
        setupEnd: 9.0,
        punchStart: 9.0,
        punchEnd: 10.5,
        setupText: "When he nails it first try...",
        punchText: "I DO 💍",
    },
    {
        setupStart: 10.5,
        setupEnd: 12.5,
        punchStart: 12.5,
        punchEnd: 14.0,
        setupText: "When he doesn't even flinch...",
        punchText: "I DO 💍",
    },
    {
        setupStart: 14.0,
        setupEnd: 16.0,
        punchStart: 16.0,
        punchEnd: 17.5,
        setupText: "When he just keeps going...",
        punchText: "I DO 💍",
    },
];

// ─── PLAYBACK SPEEDS ─────────────────────────────────────────────────
const SETUP_SPEED = 1.3;    // Urgency — removes "waiting" feeling
const PUNCH_SPEED = 1.0;    // Normal — emphasizes the reaction

// ─── CRASH ZOOM ──────────────────────────────────────────────────────
const ZOOM_START_SCALE = 1.05;
const ZOOM_END_SCALE = 1.0;
const ZOOM_DURATION_SEC = 0.2; // 6 frames @ 30fps

// ─── COMPONENT: Setup Text (top 15%) ────────────────────────────────
const SetupText: React.FC<{ text: string }> = ({ text }) => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    // Instant pop-in (scale 0 → 1 in 2 frames)
    const scale = interpolate(frame, [0, 2], [0, 1], {
        extrapolateRight: "clamp",
        easing: Easing.out(Easing.back(1.5)),
    });

    return (
        <div
            style={{
                position: "absolute",
                top: "15%",
                left: 0,
                right: 0,
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                transform: `scale(${scale})`,
                zIndex: 10,
            }}
        >
            <span
                style={{
                    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif",
                    fontWeight: 800,
                    fontSize: 48,
                    color: "#FFFFFF",
                    textShadow:
                        "-2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000, 2px 2px 0 #000, 0 0 8px rgba(0,0,0,0.7)",
                    textAlign: "center",
                    padding: "0 40px",
                    lineHeight: 1.2,
                }}
            >
                {text}
            </span>
        </div>
    );
};

// ─── COMPONENT: Punchline Text (center, "I DO" pop) ─────────────────
const PunchText: React.FC<{ text: string }> = ({ text }) => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    // Spring pop: scale 0 → 1 instantly on cut (no fade-in)
    const scaleSpring = spring({
        frame,
        fps,
        config: {
            damping: 12,
            stiffness: 200,
            mass: 0.8,
        },
    });

    return (
        <div
            style={{
                position: "absolute",
                top: "50%",
                left: 0,
                right: 0,
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                transform: `translateY(-50%) scale(${scaleSpring})`,
                zIndex: 10,
            }}
        >
            <span
                style={{
                    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif",
                    fontWeight: 900,
                    fontSize: 96,
                    color: "#FFFFFF",
                    textShadow:
                        "-4px -4px 0 #000, 4px -4px 0 #000, -4px 4px 0 #000, 4px 4px 0 #000, " +
                        "-3px 0 0 #000, 3px 0 0 #000, 0 -3px 0 #000, 0 3px 0 #000, " +
                        "0 0 20px rgba(0,0,0,0.8)",
                    textAlign: "center",
                    letterSpacing: 4,
                }}
            >
                {text}
            </span>
        </div>
    );
};

// ─── COMPONENT: Crash Zoom Wrapper ───────────────────────────────────
// Scale-in from 1.05 → 1.0 over 0.2s on the first frame of the clip
const CrashZoom: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const zoomFrames = Math.round(ZOOM_DURATION_SEC * fps);
    const scale = interpolate(
        frame,
        [0, zoomFrames],
        [ZOOM_START_SCALE, ZOOM_END_SCALE],
        { extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) }
    );

    return (
        <div style={{ width: "100%", height: "100%", transform: `scale(${scale})`, overflow: "hidden" }}>
            {children}
        </div>
    );
};

// ─── MAIN COMPOSITION ────────────────────────────────────────────────
export interface ViralReelProps {}

export const ViralReel: React.FC<ViralReelProps> = () => {
    const { fps } = useVideoConfig();
    const videoSrc = staticFile("source.mov");

    // Calculate timeline frame offsets for each scene
    // Setup duration is compressed by speed, punchline is 1:1
    let currentFrame = 0;
    const timeline = SCENES.map((scene) => {
        const setupDurationSrc = scene.setupEnd - scene.setupStart;
        const punchDurationSrc = scene.punchEnd - scene.punchStart;

        // Actual frames on the timeline (setup is faster, so fewer frames)
        const setupFrames = Math.round((setupDurationSrc / SETUP_SPEED) * fps);
        const punchFrames = Math.round((punchDurationSrc / PUNCH_SPEED) * fps);

        const entry = {
            ...scene,
            timelineStart: currentFrame,
            setupFrames,
            punchFrames,
            totalFrames: setupFrames + punchFrames,
        };

        currentFrame += entry.totalFrames;
        return entry;
    });

    return (
        <AbsoluteFill style={{ backgroundColor: "#000" }}>
            {timeline.map((scene, i) => (
                <React.Fragment key={i}>
                    {/* ── SETUP SEGMENT ── */}
                    <Sequence
                        from={scene.timelineStart}
                        durationInFrames={scene.setupFrames}
                    >
                        <AbsoluteFill>
                            <Video
                                src={videoSrc}
                                trimBefore={Math.round(scene.setupStart * fps)}
                                trimAfter={Math.round(scene.setupEnd * fps)}
                                playbackRate={SETUP_SPEED}
                                style={{
                                    width: "100%",
                                    height: "100%",
                                    objectFit: "cover",
                                }}
                                volume={1}
                            />
                            <SetupText text={scene.setupText} />
                        </AbsoluteFill>
                    </Sequence>

                    {/* ── PUNCHLINE SEGMENT ── */}
                    <Sequence
                        from={scene.timelineStart + scene.setupFrames}
                        durationInFrames={scene.punchFrames}
                    >
                        <AbsoluteFill>
                            <CrashZoom>
                                <Video
                                    src={videoSrc}
                                    trimBefore={Math.round(scene.punchStart * fps)}
                                    trimAfter={Math.round(scene.punchEnd * fps)}
                                    playbackRate={PUNCH_SPEED}
                                    style={{
                                        width: "100%",
                                        height: "100%",
                                        objectFit: "cover",
                                    }}
                                    volume={1}
                                />
                            </CrashZoom>
                            <PunchText text={scene.punchText} />
                        </AbsoluteFill>
                    </Sequence>
                </React.Fragment>
            ))}
        </AbsoluteFill>
    );
};
