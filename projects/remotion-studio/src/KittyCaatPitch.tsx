import {
    AbsoluteFill,
    useCurrentFrame,
    useVideoConfig,
    interpolate,
    spring,
    Sequence,
    Easing,
} from "remotion";
import { loadFont as loadInter } from "@remotion/google-fonts/Inter";
import { loadFont as loadSpaceGrotesk } from "@remotion/google-fonts/SpaceGrotesk";
import { TransitionSeries, linearTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { slide } from "@remotion/transitions/slide";

// @see rules/high-retention-editing.md for pacing and cut strategy
// Structure: Hook (3s) → Stats (4s) → Opportunity (4s) → Paths (12s) → Revenue (6s) → Why Her (6s) → Video Concepts (10s) → CTA (5s)
// Total: ~50 seconds at 30fps = 1500 frames

const { fontFamily: interFont } = loadInter("normal", {
    weights: ["400", "600", "700", "800", "900"],
    subsets: ["latin"],
});
const { fontFamily: spaceFont } = loadSpaceGrotesk("normal", {
    weights: ["400", "600", "700"],
    subsets: ["latin"],
});

// ─── COLOR PALETTE ───
const COLORS = {
    bg: "#0a0a0f",
    bgCard: "#111118",
    accent: "#c084fc", // purple
    accentPink: "#f472b6",
    accentCyan: "#22d3ee",
    accentGold: "#fbbf24",
    white: "#ffffff",
    gray: "#9ca3af",
    dimGray: "#6b7280",
    gradientPurple: "linear-gradient(135deg, #c084fc 0%, #a855f7 50%, #7c3aed 100%)",
    gradientPink: "linear-gradient(135deg, #f472b6 0%, #ec4899 50%, #db2777 100%)",
    gradientGold: "linear-gradient(135deg, #fbbf24 0%, #f59e0b 50%, #d97706 100%)",
    gradientCyan: "linear-gradient(135deg, #22d3ee 0%, #06b6d4 50%, #0891b2 100%)",
};

// ─── MAIN COMPOSITION ───
export const KittyCaatPitch: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    // Subtle ambient animation for the background
    const bgShift = Math.sin(frame * 0.008) * 5;

    return (
        <AbsoluteFill
            style={{
                backgroundColor: COLORS.bg,
                fontFamily: interFont,
                overflow: "hidden",
            }}
        >
            {/* Animated ambient gradient orbs */}
            <div
                style={{
                    position: "absolute",
                    top: `${30 + bgShift}%`,
                    left: "20%",
                    width: 400,
                    height: 400,
                    borderRadius: "50%",
                    background: "radial-gradient(circle, rgba(168,85,247,0.15) 0%, transparent 70%)",
                    filter: "blur(60px)",
                }}
            />
            <div
                style={{
                    position: "absolute",
                    top: `${60 - bgShift}%`,
                    right: "10%",
                    width: 300,
                    height: 300,
                    borderRadius: "50%",
                    background: "radial-gradient(circle, rgba(244,114,182,0.12) 0%, transparent 70%)",
                    filter: "blur(50px)",
                }}
            />

            {/* SCENE 1: HOOK — 0-3s (0-90) */}
            <Sequence from={0} durationInFrames={90} premountFor={fps}>
                <HookScene />
            </Sequence>

            {/* SCENE 2: HER STATS — 3-7s (90-210) */}
            <Sequence from={90} durationInFrames={120} premountFor={fps}>
                <StatsScene />
            </Sequence>

            {/* SCENE 3: THE OPPORTUNITY — 7-11s (210-330) */}
            <Sequence from={210} durationInFrames={120} premountFor={fps}>
                <OpportunityScene />
            </Sequence>

            {/* SCENE 4: 6 PATHS — 11-23s (330-690) */}
            <Sequence from={330} durationInFrames={360} premountFor={fps}>
                <PathsScene />
            </Sequence>

            {/* SCENE 5: REVENUE — 23-29s (690-870) */}
            <Sequence from={690} durationInFrames={180} premountFor={fps}>
                <RevenueScene />
            </Sequence>

            {/* SCENE 6: WHY HER — 29-35s (870-1050) */}
            <Sequence from={870} durationInFrames={180} premountFor={fps}>
                <WhyHerScene />
            </Sequence>

            {/* SCENE 7: VIDEO CONCEPTS — 35-45s (1050-1350) */}
            <Sequence from={1050} durationInFrames={300} premountFor={fps}>
                <VideoConceptsScene />
            </Sequence>

            {/* SCENE 8: CTA — 45-50s (1350-1500) */}
            <Sequence from={1350} durationInFrames={150} premountFor={fps}>
                <CTAScene />
            </Sequence>
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// SCENE 1: HOOK
// ═══════════════════════════════════════════════
const HookScene: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const line1 = "What if your";
    const line2 = "Instagram";
    const line3 = "could pay your bills?";

    const line1Opacity = interpolate(frame, [0, 12], [0, 1], { extrapolateRight: "clamp" });
    const line1Y = interpolate(frame, [0, 12], [40, 0], { extrapolateRight: "clamp", easing: Easing.out(Easing.quad) });

    const line2Scale = spring({ frame: frame - 12, fps, config: { damping: 12, mass: 0.6 } });
    const line2Opacity = interpolate(frame, [12, 20], [0, 1], { extrapolateRight: "clamp" });

    const line3Opacity = interpolate(frame, [30, 42], [0, 1], { extrapolateRight: "clamp" });
    const line3Y = interpolate(frame, [30, 42], [30, 0], { extrapolateRight: "clamp", easing: Easing.out(Easing.quad) });

    // Flash effect at the start
    const flash = interpolate(frame, [0, 4, 8], [0.6, 0, 0], { extrapolateRight: "clamp" });

    return (
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
            {/* Flash */}
            <AbsoluteFill style={{ backgroundColor: COLORS.accent, opacity: flash }} />

            <div style={{ textAlign: "center", padding: 60 }}>
                <div
                    style={{
                        fontSize: 42,
                        fontWeight: 600,
                        color: COLORS.gray,
                        opacity: line1Opacity,
                        transform: `translateY(${line1Y}px)`,
                        marginBottom: 16,
                    }}
                >
                    {line1}
                </div>
                <div
                    style={{
                        fontSize: 96,
                        fontWeight: 900,
                        background: COLORS.gradientPurple,
                        WebkitBackgroundClip: "text",
                        WebkitTextFillColor: "transparent",
                        opacity: line2Opacity,
                        transform: `scale(${Math.max(line2Scale, 0)})`,
                        lineHeight: 1.1,
                        marginBottom: 16,
                    }}
                >
                    {line2}
                </div>
                <div
                    style={{
                        fontSize: 42,
                        fontWeight: 600,
                        color: COLORS.gray,
                        opacity: line3Opacity,
                        transform: `translateY(${line3Y}px)`,
                    }}
                >
                    {line3}
                </div>
            </div>
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// SCENE 2: HER STATS
// ═══════════════════════════════════════════════
const StatsScene: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const stats = [
        { label: "@kittycaatmeow", color: COLORS.accentPink, delay: 0 },
        { label: "18.3K Followers", color: COLORS.accent, delay: 12 },
        { label: "ICU Nurse", color: COLORS.accentCyan, delay: 24 },
        { label: "NPC Athlete", color: COLORS.accentGold, delay: 36 },
        { label: "Cosplayer", color: COLORS.accentPink, delay: 48 },
    ];

    // Header
    const headerOpacity = interpolate(frame, [0, 10], [0, 1], { extrapolateRight: "clamp" });

    return (
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
            <div style={{ textAlign: "center", padding: 50, width: "100%" }}>
                <div
                    style={{
                        fontSize: 28,
                        fontWeight: 600,
                        color: COLORS.dimGray,
                        letterSpacing: 6,
                        textTransform: "uppercase",
                        opacity: headerOpacity,
                        marginBottom: 50,
                    }}
                >
                    Meet Your Brand
                </div>

                {stats.map((stat, i) => {
                    const entrance = spring({
                        frame: frame - stat.delay,
                        fps,
                        config: { damping: 15, mass: 0.5 },
                    });
                    const opacity = interpolate(frame, [stat.delay, stat.delay + 8], [0, 1], {
                        extrapolateLeft: "clamp",
                        extrapolateRight: "clamp",
                    });

                    return (
                        <div
                            key={i}
                            style={{
                                fontSize: i === 0 ? 56 : 48,
                                fontWeight: i === 0 ? 800 : 700,
                                color: stat.color,
                                opacity,
                                transform: `translateX(${(1 - Math.max(entrance, 0)) * 80}px)`,
                                marginBottom: i === 0 ? 40 : 20,
                                fontFamily: i === 0 ? spaceFont : interFont,
                            }}
                        >
                            {stat.label}
                        </div>
                    );
                })}

                {/* Tagline */}
                <div
                    style={{
                        fontSize: 24,
                        fontWeight: 600,
                        color: COLORS.dimGray,
                        opacity: interpolate(frame, [65, 80], [0, 1], { extrapolateRight: "clamp" }),
                        marginTop: 40,
                        fontStyle: "italic",
                    }}
                >
                    Creatine & Cosplay
                </div>
            </div>
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// SCENE 3: THE OPPORTUNITY
// ═══════════════════════════════════════════════
const OpportunityScene: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const line1In = spring({ frame, fps, config: { damping: 20 } });
    const line2In = spring({ frame: frame - 20, fps, config: { damping: 20 } });
    const highlightIn = spring({ frame: frame - 50, fps, config: { damping: 15 } });

    return (
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
            <div style={{ textAlign: "center", padding: 60 }}>
                <div
                    style={{
                        fontSize: 38,
                        fontWeight: 600,
                        color: COLORS.gray,
                        opacity: Math.max(line1In, 0),
                        transform: `translateY(${(1 - Math.max(line1In, 0)) * 30}px)`,
                        marginBottom: 24,
                    }}
                >
                    Most creators with 18K followers
                </div>
                <div
                    style={{
                        fontSize: 72,
                        fontWeight: 900,
                        color: COLORS.white,
                        opacity: Math.max(line2In, 0),
                        transform: `scale(${Math.max(line2In, 0)})`,
                        marginBottom: 40,
                    }}
                >
                    earn $0
                </div>
                <div
                    style={{
                        fontSize: 32,
                        fontWeight: 600,
                        color: COLORS.accentGold,
                        opacity: Math.max(highlightIn, 0),
                        transform: `translateY(${(1 - Math.max(highlightIn, 0)) * 20}px)`,
                    }}
                >
                    You already have a brand deal.{"\n"}
                    <span style={{ color: COLORS.dimGray, fontSize: 24 }}>
                        That means brands already see the value.
                    </span>
                </div>
            </div>
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// SCENE 4: 6 MONETIZATION PATHS
// ═══════════════════════════════════════════════
const PathsScene: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    // Show header, then cycle through paths
    const headerOpacity = interpolate(frame, [0, 15], [0, 1], { extrapolateRight: "clamp" });

    const paths = [
        { icon: "🤝", title: "Brand Partnerships", amount: "$500-$2K/mo", gradient: COLORS.gradientPurple, startFrame: 30 },
        { icon: "📦", title: "Digital Products", amount: "$15-$50 each", gradient: COLORS.gradientPink, startFrame: 80 },
        { icon: "💜", title: "Fan Memberships", amount: "$900+/mo", gradient: COLORS.gradientCyan, startFrame: 130 },
        { icon: "📱", title: "Platform Expansion", amount: "TikTok + YouTube", gradient: COLORS.gradientGold, startFrame: 180 },
        { icon: "🔗", title: "Affiliate Marketing", amount: "$200-$800/mo", gradient: COLORS.gradientPurple, startFrame: 230 },
        { icon: "🎪", title: "Convention Revenue", amount: "$500-$2K/weekend", gradient: COLORS.gradientPink, startFrame: 280 },
    ];

    return (
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
            <div style={{ padding: 50, width: "100%" }}>
                <div
                    style={{
                        fontSize: 28,
                        fontWeight: 600,
                        color: COLORS.dimGray,
                        letterSpacing: 4,
                        textTransform: "uppercase",
                        textAlign: "center",
                        opacity: headerOpacity,
                        marginBottom: 40,
                    }}
                >
                    6 Revenue Paths
                </div>

                <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
                    {paths.map((path, i) => {
                        const entrance = spring({
                            frame: frame - path.startFrame,
                            fps,
                            config: { damping: 18, mass: 0.5 },
                        });
                        const opacity = interpolate(frame, [path.startFrame, path.startFrame + 10], [0, 1], {
                            extrapolateLeft: "clamp",
                            extrapolateRight: "clamp",
                        });
                        // Highlight effect — each card glows briefly
                        const isActive = frame >= path.startFrame && frame < path.startFrame + 50;
                        const glow = isActive ? interpolate(frame, [path.startFrame, path.startFrame + 15, path.startFrame + 50], [0, 1, 0.3], { extrapolateRight: "clamp" }) : interpolate(frame, [path.startFrame + 50, path.startFrame + 60], [0.3, 0.15], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

                        return (
                            <div
                                key={i}
                                style={{
                                    display: "flex",
                                    alignItems: "center",
                                    gap: 20,
                                    padding: "20px 30px",
                                    borderRadius: 16,
                                    backgroundColor: `rgba(255,255,255,${0.03 + glow * 0.07})`,
                                    border: `1px solid rgba(192,132,252,${0.1 + glow * 0.3})`,
                                    opacity,
                                    transform: `translateX(${(1 - Math.max(entrance, 0)) * 60}px)`,
                                }}
                            >
                                <span style={{ fontSize: 36 }}>{path.icon}</span>
                                <div style={{ flex: 1 }}>
                                    <div style={{ fontSize: 28, fontWeight: 700, color: COLORS.white }}>
                                        {path.title}
                                    </div>
                                </div>
                                <div
                                    style={{
                                        fontSize: 22,
                                        fontWeight: 700,
                                        background: path.gradient,
                                        WebkitBackgroundClip: "text",
                                        WebkitTextFillColor: "transparent",
                                    }}
                                >
                                    {path.amount}
                                </div>
                            </div>
                        );
                    })}
                </div>
            </div>
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// SCENE 5: REVENUE PROJECTIONS
// ═══════════════════════════════════════════════
const RevenueScene: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const tiers = [
        { label: "Conservative", amount: "$500-$1K", sub: "per month", color: COLORS.gray, delay: 15 },
        { label: "Moderate", amount: "$2K-$4K", sub: "per month", color: COLORS.accent, delay: 45 },
        { label: "Full Creator", amount: "$5K-$8K", sub: "per month", color: COLORS.accentGold, delay: 75 },
    ];

    // Header
    const headerIn = spring({ frame, fps, config: { damping: 20 } });

    // Annual reveal
    const annualOpacity = interpolate(frame, [120, 140], [0, 1], { extrapolateRight: "clamp" });
    const annualScale = spring({ frame: frame - 120, fps, config: { damping: 12 } });

    return (
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
            <div style={{ textAlign: "center", padding: 50, width: "100%" }}>
                <div
                    style={{
                        fontSize: 28,
                        fontWeight: 600,
                        color: COLORS.dimGray,
                        letterSpacing: 4,
                        textTransform: "uppercase",
                        opacity: Math.max(headerIn, 0),
                        marginBottom: 50,
                    }}
                >
                    Revenue Projections
                </div>

                {tiers.map((tier, i) => {
                    const entrance = spring({
                        frame: frame - tier.delay,
                        fps,
                        config: { damping: 15, mass: 0.6 },
                    });
                    const opacity = interpolate(frame, [tier.delay, tier.delay + 10], [0, 1], {
                        extrapolateLeft: "clamp",
                        extrapolateRight: "clamp",
                    });

                    return (
                        <div
                            key={i}
                            style={{
                                opacity,
                                transform: `scale(${Math.max(entrance, 0)})`,
                                marginBottom: 30,
                            }}
                        >
                            <div style={{ fontSize: 22, fontWeight: 600, color: COLORS.dimGray, marginBottom: 4 }}>
                                {tier.label}
                            </div>
                            <div style={{ fontSize: i === 2 ? 72 : 56, fontWeight: 900, color: tier.color }}>
                                {tier.amount}
                            </div>
                            <div style={{ fontSize: 18, color: COLORS.dimGray }}>{tier.sub}</div>
                        </div>
                    );
                })}

                {/* Annual highlight */}
                <div
                    style={{
                        opacity: annualOpacity,
                        transform: `scale(${Math.max(annualScale, 0)})`,
                        marginTop: 20,
                        padding: "16px 40px",
                        borderRadius: 12,
                        background: "rgba(251,191,36,0.1)",
                        border: "1px solid rgba(251,191,36,0.3)",
                        display: "inline-block",
                    }}
                >
                    <span style={{ fontSize: 24, fontWeight: 700, color: COLORS.accentGold }}>
                        Up to $96K/year
                    </span>
                </div>
            </div>
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// SCENE 6: WHY HER
// ═══════════════════════════════════════════════
const WhyHerScene: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const titleIn = spring({ frame, fps, config: { damping: 20 } });

    const points = [
        { text: "Cosplay", emoji: "🎭", delay: 20 },
        { text: "×", emoji: "", delay: 35 },
        { text: "Bodybuilding", emoji: "💪", delay: 45 },
        { text: "×", emoji: "", delay: 60 },
        { text: "ICU Nursing", emoji: "🏥", delay: 70 },
    ];

    const conclusionOpacity = interpolate(frame, [100, 120], [0, 1], { extrapolateRight: "clamp" });
    const conclusionScale = spring({ frame: frame - 100, fps, config: { damping: 12, mass: 0.8 } });

    return (
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
            <div style={{ textAlign: "center", padding: 60 }}>
                <div
                    style={{
                        fontSize: 28,
                        fontWeight: 600,
                        color: COLORS.dimGray,
                        letterSpacing: 4,
                        textTransform: "uppercase",
                        opacity: Math.max(titleIn, 0),
                        marginBottom: 50,
                    }}
                >
                    Your Unfair Advantage
                </div>

                <div style={{ display: "flex", justifyContent: "center", alignItems: "center", gap: 16, flexWrap: "wrap", marginBottom: 50 }}>
                    {points.map((p, i) => {
                        const entrance = spring({ frame: frame - p.delay, fps, config: { damping: 15 } });
                        const opacity = interpolate(frame, [p.delay, p.delay + 8], [0, 1], {
                            extrapolateLeft: "clamp",
                            extrapolateRight: "clamp",
                        });
                        const isMultiplier = p.text === "×";

                        return (
                            <div
                                key={i}
                                style={{
                                    opacity,
                                    transform: `scale(${Math.max(entrance, 0)})`,
                                }}
                            >
                                {isMultiplier ? (
                                    <span style={{ fontSize: 48, color: COLORS.accent, fontWeight: 300 }}>×</span>
                                ) : (
                                    <div
                                        style={{
                                            padding: "16px 24px",
                                            borderRadius: 12,
                                            backgroundColor: "rgba(255,255,255,0.05)",
                                            border: "1px solid rgba(192,132,252,0.2)",
                                        }}
                                    >
                                        <div style={{ fontSize: 36, marginBottom: 4 }}>{p.emoji}</div>
                                        <div style={{ fontSize: 22, fontWeight: 700, color: COLORS.white }}>{p.text}</div>
                                    </div>
                                )}
                            </div>
                        );
                    })}
                </div>

                <div
                    style={{
                        opacity: conclusionOpacity,
                        transform: `scale(${Math.max(conclusionScale, 0)})`,
                    }}
                >
                    <div style={{ fontSize: 20, color: COLORS.dimGray, marginBottom: 12 }}>
                        = Nobody else occupies this space
                    </div>
                    <div
                        style={{
                            fontSize: 56,
                            fontWeight: 900,
                            background: COLORS.gradientGold,
                            WebkitBackgroundClip: "text",
                            WebkitTextFillColor: "transparent",
                        }}
                    >
                        Category of One
                    </div>
                </div>
            </div>
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// SCENE 7: VIDEO CONCEPTS
// ═══════════════════════════════════════════════
const VideoConceptsScene: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const headerIn = spring({ frame, fps, config: { damping: 20 } });

    const concepts = [
        {
            title: "POV: Your ICU nurse\nis also an NPC competitor",
            difficulty: "EASY",
            format: "15s Reel",
            delay: 20,
        },
        {
            title: "Training like\n[anime character] for 30 days",
            difficulty: "MEDIUM",
            format: "60s Series",
            delay: 75,
        },
        {
            title: "What I eat in a day\n— NPC prep edition",
            difficulty: "EASY",
            format: "30s Reel",
            delay: 130,
        },
        {
            title: "Cosplay build +\nthe workout that powers it",
            difficulty: "MEDIUM",
            format: "45s Reel",
            delay: 185,
        },
        {
            title: "Night shift → morning lift\n→ cosplay shoot",
            difficulty: "EASY",
            format: "30s Reel",
            delay: 240,
        },
    ];

    return (
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
            <div style={{ padding: 50, width: "100%" }}>
                <div
                    style={{
                        fontSize: 24,
                        fontWeight: 600,
                        color: COLORS.dimGray,
                        letterSpacing: 4,
                        textTransform: "uppercase",
                        textAlign: "center",
                        opacity: Math.max(headerIn, 0),
                        marginBottom: 12,
                    }}
                >
                    Ready-to-Film Content
                </div>
                <div
                    style={{
                        fontSize: 18,
                        color: COLORS.dimGray,
                        textAlign: "center",
                        opacity: Math.max(headerIn, 0),
                        marginBottom: 36,
                    }}
                >
                    5 video concepts with full scripts
                </div>

                <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
                    {concepts.map((concept, i) => {
                        const entrance = spring({
                            frame: frame - concept.delay,
                            fps,
                            config: { damping: 18, mass: 0.4 },
                        });
                        const opacity = interpolate(frame, [concept.delay, concept.delay + 10], [0, 1], {
                            extrapolateLeft: "clamp",
                            extrapolateRight: "clamp",
                        });
                        const isActive = frame >= concept.delay && frame < concept.delay + 55;
                        const glow = isActive
                            ? interpolate(frame, [concept.delay, concept.delay + 15, concept.delay + 55], [0, 0.4, 0.1], { extrapolateRight: "clamp" })
                            : 0.05;

                        return (
                            <div
                                key={i}
                                style={{
                                    display: "flex",
                                    alignItems: "center",
                                    gap: 16,
                                    padding: "18px 24px",
                                    borderRadius: 14,
                                    backgroundColor: `rgba(255,255,255,${0.02 + glow * 0.08})`,
                                    border: `1px solid rgba(192,132,252,${0.08 + glow * 0.4})`,
                                    opacity,
                                    transform: `translateY(${(1 - Math.max(entrance, 0)) * 40}px)`,
                                }}
                            >
                                <div
                                    style={{
                                        fontSize: 32,
                                        fontWeight: 800,
                                        color: COLORS.accent,
                                        minWidth: 40,
                                        textAlign: "center",
                                        fontFamily: spaceFont,
                                    }}
                                >
                                    {i + 1}
                                </div>
                                <div style={{ flex: 1 }}>
                                    <div style={{ fontSize: 22, fontWeight: 700, color: COLORS.white, lineHeight: 1.3, whiteSpace: "pre-line" }}>
                                        {concept.title}
                                    </div>
                                </div>
                                <div style={{ textAlign: "right" }}>
                                    <div
                                        style={{
                                            fontSize: 14,
                                            fontWeight: 700,
                                            color: concept.difficulty === "EASY" ? COLORS.accentCyan : COLORS.accentGold,
                                            letterSpacing: 2,
                                        }}
                                    >
                                        {concept.difficulty}
                                    </div>
                                    <div style={{ fontSize: 14, color: COLORS.dimGray }}>{concept.format}</div>
                                </div>
                            </div>
                        );
                    })}
                </div>
            </div>
        </AbsoluteFill>
    );
};

// ═══════════════════════════════════════════════
// SCENE 8: CTA
// ═══════════════════════════════════════════════
const CTAScene: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const mainScale = spring({ frame, fps, config: { damping: 12, mass: 0.8 } });
    const subOpacity = interpolate(frame, [30, 50], [0, 1], { extrapolateRight: "clamp" });
    const buttonBounce = spring({ frame: frame - 50, fps, config: { damping: 8, stiffness: 200, mass: 0.5 } });
    const pulse = Math.sin(frame * 0.1) * 0.03 + 1;

    // Glow effect
    const glow = interpolate(frame, [0, 30], [0, 1], { extrapolateRight: "clamp" });

    return (
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
            {/* Radial glow behind */}
            <div
                style={{
                    position: "absolute",
                    width: 500,
                    height: 500,
                    borderRadius: "50%",
                    background: `radial-gradient(circle, rgba(192,132,252,${0.2 * glow}) 0%, transparent 70%)`,
                    filter: "blur(40px)",
                }}
            />

            <div style={{ textAlign: "center", padding: 60 }}>
                <div
                    style={{
                        fontSize: 64,
                        fontWeight: 900,
                        color: COLORS.white,
                        transform: `scale(${Math.max(mainScale, 0)})`,
                        marginBottom: 20,
                        lineHeight: 1.2,
                    }}
                >
                    Ready to{"\n"}build this?
                </div>
                <div
                    style={{
                        fontSize: 24,
                        color: COLORS.gray,
                        opacity: subOpacity,
                        marginBottom: 50,
                    }}
                >
                    Strategy deck + content playbook included
                </div>
                <div
                    style={{
                        transform: `scale(${Math.max(buttonBounce, 0) * pulse})`,
                        display: "inline-block",
                        padding: "24px 56px",
                        background: COLORS.gradientPurple,
                        borderRadius: 16,
                        boxShadow: `0 20px 60px rgba(192,132,252,${0.4 * glow})`,
                    }}
                >
                    <span
                        style={{
                            fontSize: 36,
                            fontWeight: 700,
                            color: COLORS.white,
                        }}
                    >
                        Let's Talk →
                    </span>
                </div>
            </div>
        </AbsoluteFill>
    );
};
