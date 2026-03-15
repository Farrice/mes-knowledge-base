import {
    AbsoluteFill,
    useCurrentFrame,
    useVideoConfig,
    interpolate,
    spring,
    Sequence,
    Img,
    Easing,
    staticFile,
} from "remotion";
import { loadFont as loadInter } from "@remotion/google-fonts/Inter";
import { loadFont as loadSpaceGrotesk } from "@remotion/google-fonts/SpaceGrotesk";

// @see rules/high-retention-editing.md — staccato hook, measured demo, accelerate to CTA
// Structure: Hook (2s) → Ingredients (4s) → Steps (11s) → Blend (3s) → Reveal (5s) → Macros (5s) → Recipe Card (5s) → CTA (5s)
// Total: 40 seconds = 1200 frames at 30fps

const { fontFamily: interFont } = loadInter("normal", {
    weights: ["400", "600", "700", "800", "900"],
    subsets: ["latin"],
});
const { fontFamily: spaceFont } = loadSpaceGrotesk("normal", {
    weights: ["400", "600", "700"],
    subsets: ["latin"],
});

// ─── IMAGES ───
const IMAGES = {
    hero: staticFile("recipe/hero-smoothie.png"),
    flatlay: staticFile("recipe/ingredients-flatlay.png"),
    scoop: staticFile("recipe/action-scoop.png"),
    blender: staticFile("recipe/blender-action.png"),
    lifestyle: staticFile("recipe/lifestyle-holding.png"),
};

// ─── COLORS ───
const C = {
    bg: "#0f0f14",
    card: "#1a1a24",
    accent: "#a855f7",
    accentLight: "#c084fc",
    pink: "#f472b6",
    cyan: "#22d3ee",
    gold: "#fbbf24",
    white: "#ffffff",
    gray: "#9ca3af",
    dimGray: "#6b7280",
    warmBg: "#1c1917",
};

// ─── MAIN COMPOSITION ───
export const ProteinRecipeUGC: React.FC = () => {
    return (
        <AbsoluteFill style={{ backgroundColor: C.bg, fontFamily: interFont, overflow: "hidden" }}>
            {/* HOOK — 0-2s (0-60) */}
            <Sequence from={0} durationInFrames={60} premountFor={30}>
                <HookScene />
            </Sequence>

            {/* INGREDIENTS — 2-6s (60-180) */}
            <Sequence from={60} durationInFrames={120} premountFor={30}>
                <IngredientsScene />
            </Sequence>

            {/* STEP 1: Protein Powder — 6-10s (180-300) */}
            <Sequence from={180} durationInFrames={120} premountFor={30}>
                <StepScene
                    image={IMAGES.scoop}
                    stepNumber={1}
                    caption="1 scoop protein powder"
                    subCaption="(vanilla or chocolate — your choice)"
                />
            </Sequence>

            {/* STEP 2: Berries + Banana — 10-14s (300-420) */}
            <Sequence from={300} durationInFrames={120} premountFor={30}>
                <StepScene
                    image={IMAGES.blender}
                    stepNumber={2}
                    caption="Frozen berries + banana"
                    subCaption="the color comes from HERE"
                />
            </Sequence>

            {/* STEP 3: Yogurt + Milk — 14-17s (420-510) */}
            <Sequence from={420} durationInFrames={90} premountFor={30}>
                <StepScene
                    image={IMAGES.blender}
                    stepNumber={3}
                    caption="Greek yogurt + almond milk"
                    subCaption="this is the creamy texture hack"
                    zoomStart={1.15}
                />
            </Sequence>

            {/* BLEND — 17-20s (510-600) */}
            <Sequence from={510} durationInFrames={90} premountFor={30}>
                <BlendScene />
            </Sequence>

            {/* REVEAL — 20-25s (600-750) */}
            <Sequence from={600} durationInFrames={150} premountFor={30}>
                <RevealScene />
            </Sequence>

            {/* MACROS — 25-30s (750-900) */}
            <Sequence from={750} durationInFrames={150} premountFor={30}>
                <MacroScene />
            </Sequence>

            {/* RECIPE CARD — 30-35s (900-1050) */}
            <Sequence from={900} durationInFrames={150} premountFor={30}>
                <RecipeCardScene />
            </Sequence>

            {/* CTA — 35-40s (1050-1200) */}
            <Sequence from={1050} durationInFrames={150} premountFor={30}>
                <CTAScene />
            </Sequence>
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// Dynamic Caption Component (word-by-word reveal)
// ═══════════════════════════════════════════════
const DynamicCaption: React.FC<{
    text: string;
    startFrame?: number;
    fontSize?: number;
    color?: string;
    bold?: boolean;
}> = ({ text, startFrame = 0, fontSize = 42, color = C.white, bold = true }) => {
    const frame = useCurrentFrame();
    const words = text.split(" ");

    return (
        <div
            style={{
                display: "flex",
                flexWrap: "wrap",
                justifyContent: "center",
                gap: 10,
                padding: "0 40px",
            }}
        >
            {words.map((word, i) => {
                const delay = startFrame + i * 4;
                const opacity = interpolate(frame, [delay, delay + 6], [0, 1], {
                    extrapolateLeft: "clamp",
                    extrapolateRight: "clamp",
                });
                const y = interpolate(frame, [delay, delay + 6], [20, 0], {
                    extrapolateLeft: "clamp",
                    extrapolateRight: "clamp",
                    easing: Easing.out(Easing.quad),
                });

                return (
                    <span
                        key={i}
                        style={{
                            fontSize,
                            fontWeight: bold ? 800 : 600,
                            color,
                            opacity,
                            transform: `translateY(${y}px)`,
                            textShadow: "0 4px 20px rgba(0,0,0,0.8), 0 2px 4px rgba(0,0,0,0.9)",
                        }}
                    >
                        {word}
                    </span>
                );
            })}
        </div>
    );
};

// ═══════════════════════════════════════════════
// Ken Burns image with zoom/pan
// ═══════════════════════════════════════════════
const KenBurnsImage: React.FC<{
    src: string;
    zoomStart?: number;
    zoomEnd?: number;
    panX?: number;
    panY?: number;
    brightness?: number;
}> = ({ src, zoomStart = 1.0, zoomEnd = 1.1, panX = 0, panY = 0, brightness = 0.7 }) => {
    const frame = useCurrentFrame();
    const { durationInFrames } = useVideoConfig();

    const zoom = interpolate(frame, [0, durationInFrames], [zoomStart, zoomEnd], {
        extrapolateRight: "clamp",
    });
    const px = interpolate(frame, [0, durationInFrames], [0, panX], { extrapolateRight: "clamp" });
    const py = interpolate(frame, [0, durationInFrames], [0, panY], { extrapolateRight: "clamp" });

    return (
        <AbsoluteFill>
            <Img
                src={src}
                style={{
                    width: "100%",
                    height: "100%",
                    objectFit: "cover",
                    transform: `scale(${zoom}) translate(${px}px, ${py}px)`,
                    filter: `brightness(${brightness})`,
                }}
            />
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// SCENE 1: HOOK
// ═══════════════════════════════════════════════
const HookScene: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const flash = interpolate(frame, [0, 3, 6], [0.7, 0, 0], { extrapolateRight: "clamp" });
    const lineScale = spring({ frame, fps, config: { damping: 12, mass: 0.5 } });

    return (
        <AbsoluteFill>
            {/* Dark with subtle hero image behind */}
            <KenBurnsImage src={IMAGES.hero} brightness={0.25} zoomStart={1.2} zoomEnd={1.3} />

            {/* Flash */}
            <AbsoluteFill style={{ backgroundColor: C.accent, opacity: flash }} />

            <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
                <div
                    style={{
                        transform: `scale(${Math.max(lineScale, 0)})`,
                        textAlign: "center",
                        padding: 60,
                    }}
                >
                    <div
                        style={{
                            fontSize: 52,
                            fontWeight: 900,
                            color: C.white,
                            textShadow: "0 4px 30px rgba(0,0,0,0.8)",
                            lineHeight: 1.3,
                        }}
                    >
                        The only protein shake{"\n"}
                        <span
                            style={{
                                background: "linear-gradient(135deg, #c084fc, #f472b6)",
                                WebkitBackgroundClip: "text",
                                WebkitTextFillColor: "transparent",
                            }}
                        >
                            I actually crave
                        </span>
                    </div>
                </div>
            </AbsoluteFill>
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// SCENE 2: INGREDIENTS
// ═══════════════════════════════════════════════
const IngredientsScene: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const ingredients = [
        { name: "Protein Powder", emoji: "🥄", delay: 10 },
        { name: "Frozen Berries", emoji: "🫐", delay: 22 },
        { name: "Banana", emoji: "🍌", delay: 34 },
        { name: "Greek Yogurt", emoji: "🥛", delay: 46 },
        { name: "Almond Milk", emoji: "🥜", delay: 58 },
    ];

    return (
        <AbsoluteFill>
            <KenBurnsImage src={IMAGES.flatlay} brightness={0.5} zoomStart={1.0} zoomEnd={1.08} panY={-15} />

            {/* Gradient overlay for readability */}
            <AbsoluteFill
                style={{
                    background: "linear-gradient(180deg, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.7) 100%)",
                }}
            />

            <AbsoluteFill style={{ justifyContent: "flex-end", padding: 50, paddingBottom: 200 }}>
                <div
                    style={{
                        fontSize: 22,
                        fontWeight: 600,
                        color: C.dimGray,
                        letterSpacing: 4,
                        textTransform: "uppercase",
                        marginBottom: 24,
                        opacity: interpolate(frame, [0, 10], [0, 1], { extrapolateRight: "clamp" }),
                    }}
                >
                    5 INGREDIENTS
                </div>

                {ingredients.map((ing, i) => {
                    const entrance = spring({
                        frame: frame - ing.delay,
                        fps,
                        config: { damping: 18, mass: 0.4 },
                    });
                    const opacity = interpolate(frame, [ing.delay, ing.delay + 8], [0, 1], {
                        extrapolateLeft: "clamp",
                        extrapolateRight: "clamp",
                    });

                    return (
                        <div
                            key={i}
                            style={{
                                display: "flex",
                                alignItems: "center",
                                gap: 16,
                                opacity,
                                transform: `translateX(${(1 - Math.max(entrance, 0)) * 50}px)`,
                                marginBottom: 12,
                            }}
                        >
                            <span style={{ fontSize: 32 }}>{ing.emoji}</span>
                            <span
                                style={{
                                    fontSize: 32,
                                    fontWeight: 700,
                                    color: C.white,
                                    textShadow: "0 2px 10px rgba(0,0,0,0.8)",
                                }}
                            >
                                {ing.name}
                            </span>
                        </div>
                    );
                })}
            </AbsoluteFill>
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// STEP SCENE (reusable for steps 1-3)
// ═══════════════════════════════════════════════
const StepScene: React.FC<{
    image: string;
    stepNumber: number;
    caption: string;
    subCaption: string;
    zoomStart?: number;
}> = ({ image, stepNumber, caption, subCaption, zoomStart = 1.0 }) => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const badgeScale = spring({ frame, fps, config: { damping: 12, mass: 0.5 } });

    return (
        <AbsoluteFill>
            <KenBurnsImage src={image} brightness={0.55} zoomStart={zoomStart} zoomEnd={zoomStart + 0.1} panX={10} />

            {/* Bottom gradient for text */}
            <AbsoluteFill
                style={{
                    background: "linear-gradient(180deg, transparent 40%, rgba(0,0,0,0.85) 100%)",
                }}
            />

            {/* Step badge */}
            <div
                style={{
                    position: "absolute",
                    top: 80,
                    left: 50,
                    transform: `scale(${Math.max(badgeScale, 0)})`,
                }}
            >
                <div
                    style={{
                        width: 64,
                        height: 64,
                        borderRadius: 16,
                        background: "linear-gradient(135deg, #a855f7, #7c3aed)",
                        display: "flex",
                        justifyContent: "center",
                        alignItems: "center",
                        boxShadow: "0 8px 30px rgba(168,85,247,0.4)",
                    }}
                >
                    <span style={{ fontSize: 32, fontWeight: 900, color: C.white, fontFamily: spaceFont }}>
                        {stepNumber}
                    </span>
                </div>
            </div>

            {/* Caption */}
            <AbsoluteFill style={{ justifyContent: "flex-end", padding: 50, paddingBottom: 200 }}>
                <DynamicCaption text={caption} startFrame={10} fontSize={46} />
                <div style={{ height: 12 }} />
                <DynamicCaption text={subCaption} startFrame={30} fontSize={24} color={C.gray} bold={false} />
            </AbsoluteFill>
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// BLEND SCENE
// ═══════════════════════════════════════════════
const BlendScene: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    // Shake effect to simulate blending
    const shakeX = frame > 15 && frame < 70 ? Math.sin(frame * 1.5) * 4 : 0;
    const shakeY = frame > 15 && frame < 70 ? Math.cos(frame * 2) * 3 : 0;

    const textScale = spring({ frame: frame - 10, fps, config: { damping: 12 } });

    return (
        <AbsoluteFill style={{ transform: `translate(${shakeX}px, ${shakeY}px)` }}>
            <KenBurnsImage src={IMAGES.blender} brightness={0.5} zoomStart={1.1} zoomEnd={1.2} />

            <AbsoluteFill
                style={{
                    background: "linear-gradient(180deg, transparent 30%, rgba(0,0,0,0.8) 100%)",
                }}
            />

            <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
                <div
                    style={{
                        transform: `scale(${Math.max(textScale, 0)})`,
                        textAlign: "center",
                    }}
                >
                    <div
                        style={{
                            fontSize: 64,
                            fontWeight: 900,
                            color: C.white,
                            textShadow: "0 4px 30px rgba(0,0,0,0.8)",
                        }}
                    >
                        BLEND
                    </div>
                    <div
                        style={{
                            fontSize: 28,
                            fontWeight: 600,
                            color: C.accentLight,
                            marginTop: 8,
                            opacity: interpolate(frame, [25, 40], [0, 1], { extrapolateRight: "clamp" }),
                        }}
                    >
                        30 seconds
                    </div>
                </div>
            </AbsoluteFill>
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// REVEAL SCENE
// ═══════════════════════════════════════════════
const RevealScene: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    // Start zoomed in, slow zoom out for dramatic reveal
    const zoom = interpolate(frame, [0, 150], [1.3, 1.0], {
        extrapolateRight: "clamp",
        easing: Easing.out(Easing.quad),
    });
    const brightness = interpolate(frame, [0, 40], [0.3, 0.75], { extrapolateRight: "clamp" });

    return (
        <AbsoluteFill>
            <Img
                src={IMAGES.hero}
                style={{
                    width: "100%",
                    height: "100%",
                    objectFit: "cover",
                    transform: `scale(${zoom})`,
                    filter: `brightness(${brightness})`,
                }}
            />

            <AbsoluteFill
                style={{
                    background: "linear-gradient(180deg, transparent 50%, rgba(0,0,0,0.7) 100%)",
                }}
            />

            <AbsoluteFill style={{ justifyContent: "flex-end", padding: 50, paddingBottom: 220 }}>
                <DynamicCaption text="That's it." startFrame={30} fontSize={52} />
                <div style={{ height: 8 }} />
                <DynamicCaption text="That's the recipe." startFrame={45} fontSize={52} />
            </AbsoluteFill>
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// MACRO BREAKDOWN
// ═══════════════════════════════════════════════
const MacroScene: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const macros = [
        { label: "Calories", value: 210, unit: "cal", color: C.accentLight, delay: 10 },
        { label: "Protein", value: 40, unit: "g", color: C.cyan, delay: 25 },
        { label: "Carbs", value: 25, unit: "g", color: C.gold, delay: 40 },
        { label: "Fat", value: 5, unit: "g", color: C.pink, delay: 55 },
    ];

    const headerOpacity = interpolate(frame, [0, 10], [0, 1], { extrapolateRight: "clamp" });

    return (
        <AbsoluteFill>
            <KenBurnsImage src={IMAGES.hero} brightness={0.2} zoomStart={1.1} zoomEnd={1.15} />

            <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
                <div style={{ textAlign: "center", width: "100%", padding: 50 }}>
                    <div
                        style={{
                            fontSize: 22,
                            fontWeight: 600,
                            color: C.dimGray,
                            letterSpacing: 4,
                            textTransform: "uppercase",
                            opacity: headerOpacity,
                            marginBottom: 50,
                        }}
                    >
                        Per Serving
                    </div>

                    <div style={{ display: "flex", justifyContent: "center", gap: 20, flexWrap: "wrap" }}>
                        {macros.map((macro, i) => {
                            const entrance = spring({
                                frame: frame - macro.delay,
                                fps,
                                config: { damping: 15, mass: 0.6 },
                            });
                            // Animated counter
                            const count = Math.round(
                                interpolate(frame, [macro.delay, macro.delay + 30], [0, macro.value], {
                                    extrapolateLeft: "clamp",
                                    extrapolateRight: "clamp",
                                    easing: Easing.out(Easing.quad),
                                })
                            );

                            return (
                                <div
                                    key={i}
                                    style={{
                                        width: 220,
                                        padding: "30px 20px",
                                        borderRadius: 20,
                                        backgroundColor: "rgba(255,255,255,0.05)",
                                        border: `1px solid ${macro.color}33`,
                                        transform: `scale(${Math.max(entrance, 0)})`,
                                    }}
                                >
                                    <div style={{ fontSize: 52, fontWeight: 900, color: macro.color, fontFamily: spaceFont }}>
                                        {count}
                                        <span style={{ fontSize: 24, fontWeight: 600 }}>{macro.unit}</span>
                                    </div>
                                    <div style={{ fontSize: 18, color: C.dimGray, marginTop: 8, fontWeight: 600 }}>
                                        {macro.label}
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                </div>
            </AbsoluteFill>
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// RECIPE CARD (save-worthy)
// ═══════════════════════════════════════════════
const RecipeCardScene: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const cardEntrance = spring({ frame, fps, config: { damping: 18, mass: 0.8 } });

    const ingredients = [
        "1 scoop vanilla protein powder",
        "1/2 cup frozen mixed berries",
        "1 banana",
        "1/2 cup Greek yogurt",
        "1 cup almond milk",
    ];

    return (
        <AbsoluteFill>
            <KenBurnsImage src={IMAGES.lifestyle} brightness={0.2} zoomStart={1.05} zoomEnd={1.1} />

            <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
                <div
                    style={{
                        transform: `scale(${Math.max(cardEntrance, 0)}) translateY(${(1 - Math.max(cardEntrance, 0)) * 60}px)`,
                        width: 900,
                        padding: 50,
                        borderRadius: 24,
                        backgroundColor: "rgba(15,15,20,0.92)",
                        border: "1px solid rgba(168,85,247,0.3)",
                        boxShadow: "0 30px 80px rgba(0,0,0,0.6)",
                    }}
                >
                    {/* Header */}
                    <div
                        style={{
                            fontSize: 16,
                            fontWeight: 600,
                            color: C.accentLight,
                            letterSpacing: 3,
                            textTransform: "uppercase",
                            marginBottom: 8,
                        }}
                    >
                        SAVE THIS RECIPE
                    </div>
                    <div
                        style={{
                            fontSize: 36,
                            fontWeight: 900,
                            color: C.white,
                            marginBottom: 30,
                        }}
                    >
                        Cosplay Gains Smoothie
                    </div>

                    {/* Divider */}
                    <div
                        style={{
                            height: 2,
                            background: "linear-gradient(90deg, #a855f7, transparent)",
                            marginBottom: 24,
                            transform: `scaleX(${Math.max(cardEntrance, 0)})`,
                            transformOrigin: "left",
                        }}
                    />

                    {/* Ingredients */}
                    {ingredients.map((ing, i) => {
                        const itemOpacity = interpolate(frame, [20 + i * 8, 28 + i * 8], [0, 1], {
                            extrapolateLeft: "clamp",
                            extrapolateRight: "clamp",
                        });
                        return (
                            <div
                                key={i}
                                style={{
                                    display: "flex",
                                    alignItems: "center",
                                    gap: 12,
                                    marginBottom: 14,
                                    opacity: itemOpacity,
                                }}
                            >
                                <div
                                    style={{
                                        width: 8,
                                        height: 8,
                                        borderRadius: 4,
                                        backgroundColor: C.accentLight,
                                        flexShrink: 0,
                                    }}
                                />
                                <span style={{ fontSize: 24, color: C.white, fontWeight: 500 }}>{ing}</span>
                            </div>
                        );
                    })}

                    {/* Instructions */}
                    <div
                        style={{
                            marginTop: 24,
                            padding: "16px 20px",
                            borderRadius: 12,
                            backgroundColor: "rgba(168,85,247,0.1)",
                            opacity: interpolate(frame, [70, 85], [0, 1], { extrapolateRight: "clamp" }),
                        }}
                    >
                        <span style={{ fontSize: 20, color: C.gray, fontWeight: 600 }}>
                            Blend everything for 30 seconds. Pour & enjoy.
                        </span>
                    </div>

                    {/* Macros bar */}
                    <div
                        style={{
                            display: "flex",
                            justifyContent: "space-between",
                            marginTop: 24,
                            opacity: interpolate(frame, [85, 100], [0, 1], { extrapolateRight: "clamp" }),
                        }}
                    >
                        {[
                            { label: "210 cal", color: C.accentLight },
                            { label: "40g protein", color: C.cyan },
                            { label: "25g carbs", color: C.gold },
                            { label: "5g fat", color: C.pink },
                        ].map((m, i) => (
                            <span key={i} style={{ fontSize: 18, fontWeight: 700, color: m.color }}>
                                {m.label}
                            </span>
                        ))}
                    </div>
                </div>
            </AbsoluteFill>
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// CTA SCENE
// ═══════════════════════════════════════════════
const CTAScene: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const mainScale = spring({ frame, fps, config: { damping: 12, mass: 0.8 } });
    const handleScale = spring({ frame: frame - 30, fps, config: { damping: 15 } });
    const saveScale = spring({ frame: frame - 60, fps, config: { damping: 8, stiffness: 200, mass: 0.5 } });
    const pulse = Math.sin(frame * 0.12) * 0.04 + 1;

    return (
        <AbsoluteFill>
            <KenBurnsImage src={IMAGES.lifestyle} brightness={0.3} zoomStart={1.0} zoomEnd={1.08} />

            <AbsoluteFill
                style={{
                    background: "radial-gradient(circle at center, rgba(168,85,247,0.15) 0%, transparent 60%)",
                }}
            />

            <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
                <div style={{ textAlign: "center", padding: 60 }}>
                    <div
                        style={{
                            fontSize: 48,
                            fontWeight: 900,
                            color: C.white,
                            transform: `scale(${Math.max(mainScale, 0)})`,
                            marginBottom: 16,
                            textShadow: "0 4px 30px rgba(0,0,0,0.8)",
                            lineHeight: 1.3,
                        }}
                    >
                        Save this.
                    </div>
                    <div
                        style={{
                            fontSize: 32,
                            fontWeight: 600,
                            color: C.gray,
                            transform: `scale(${Math.max(handleScale, 0)})`,
                            marginBottom: 40,
                            textShadow: "0 2px 10px rgba(0,0,0,0.8)",
                        }}
                    >
                        Tag someone who needs{"\n"}this recipe.
                    </div>

                    {/* Handle */}
                    <div
                        style={{
                            transform: `scale(${Math.max(handleScale, 0)})`,
                            marginBottom: 30,
                        }}
                    >
                        <span
                            style={{
                                fontSize: 36,
                                fontWeight: 800,
                                background: "linear-gradient(135deg, #c084fc, #f472b6)",
                                WebkitBackgroundClip: "text",
                                WebkitTextFillColor: "transparent",
                                fontFamily: spaceFont,
                            }}
                        >
                            @kittycaatmeow
                        </span>
                    </div>

                    {/* Save button */}
                    <div
                        style={{
                            transform: `scale(${Math.max(saveScale, 0) * pulse})`,
                            display: "inline-block",
                            padding: "20px 48px",
                            background: "linear-gradient(135deg, #a855f7, #7c3aed)",
                            borderRadius: 14,
                            boxShadow: "0 16px 50px rgba(168,85,247,0.4)",
                        }}
                    >
                        <span style={{ fontSize: 28, fontWeight: 700, color: C.white }}>
                            🔖 Save Recipe
                        </span>
                    </div>

                    <div
                        style={{
                            marginTop: 30,
                            fontSize: 18,
                            color: C.dimGray,
                            opacity: interpolate(frame, [90, 110], [0, 1], { extrapolateRight: "clamp" }),
                        }}
                    >
                        Creatine & Cosplay
                    </div>
                </div>
            </AbsoluteFill>
        </AbsoluteFill>
    );
};
