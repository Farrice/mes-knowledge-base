import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate, spring, Sequence } from "remotion";

// Viral Product Teaser - 15 seconds
// Framework: Hook → Feature → Result → CTA

export const ProductTeaser: React.FC<{
    hookText: string;
    productName: string;
    featureText: string;
    resultStat: string;
    ctaText: string;
}> = ({ hookText, productName, featureText, resultStat, ctaText }) => {
    const frame = useCurrentFrame();
    const { fps, width, height } = useVideoConfig();

    return (
        <AbsoluteFill
            style={{
                backgroundColor: "#0a0a0a",
                fontFamily: "'Inter', system-ui, sans-serif",
            }}
        >
            {/* HOOK - Frames 0-90 (0-3 seconds) */}
            <Sequence from={0} durationInFrames={90}>
                <Hook text={hookText} />
            </Sequence>

            {/* FEATURE - Frames 90-210 (3-7 seconds) */}
            <Sequence from={90} durationInFrames={120}>
                <Feature productName={productName} featureText={featureText} />
            </Sequence>

            {/* RESULT - Frames 210-360 (7-12 seconds) */}
            <Sequence from={210} durationInFrames={150}>
                <Result stat={resultStat} />
            </Sequence>

            {/* CTA - Frames 360-450 (12-15 seconds) */}
            <Sequence from={360} durationInFrames={90}>
                <CTA text={ctaText} />
            </Sequence>
        </AbsoluteFill>
    );
};

// HOOK Component - Pattern interrupt
const Hook: React.FC<{ text: string }> = ({ text }) => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const scale = spring({ frame, fps, config: { damping: 15, mass: 0.5 } });
    const opacity = interpolate(frame, [0, 15], [0, 1], { extrapolateRight: "clamp" });

    // Text reveal animation
    const words = text.split(" ");

    return (
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
            <div
                style={{
                    transform: `scale(${scale})`,
                    opacity,
                    display: "flex",
                    flexWrap: "wrap",
                    justifyContent: "center",
                    gap: 20,
                    padding: 60,
                }}
            >
                {words.map((word, i) => {
                    const delay = i * 5;
                    const wordOpacity = interpolate(frame, [delay, delay + 10], [0, 1], {
                        extrapolateLeft: "clamp",
                        extrapolateRight: "clamp",
                    });
                    const wordY = interpolate(frame, [delay, delay + 10], [30, 0], {
                        extrapolateLeft: "clamp",
                        extrapolateRight: "clamp",
                    });

                    return (
                        <span
                            key={i}
                            style={{
                                fontSize: 72,
                                fontWeight: 800,
                                color: "#fff",
                                opacity: wordOpacity,
                                transform: `translateY(${wordY}px)`,
                            }}
                        >
                            {word}
                        </span>
                    );
                })}
            </div>
        </AbsoluteFill>
    );
};

// FEATURE Component
const Feature: React.FC<{ productName: string; featureText: string }> = ({
    productName,
    featureText,
}) => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const slideIn = spring({ frame, fps, config: { damping: 20 } });
    const textOpacity = interpolate(frame, [20, 40], [0, 1], { extrapolateRight: "clamp" });

    return (
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
            {/* Gradient accent bar */}
            <div
                style={{
                    position: "absolute",
                    top: 0,
                    left: 0,
                    right: 0,
                    height: 6,
                    background: "linear-gradient(90deg, #667eea 0%, #764ba2 50%, #f093fb 100%)",
                    transform: `scaleX(${slideIn})`,
                    transformOrigin: "left",
                }}
            />

            <div style={{ textAlign: "center", padding: 80 }}>
                <div
                    style={{
                        fontSize: 48,
                        fontWeight: 600,
                        background: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                        WebkitBackgroundClip: "text",
                        WebkitTextFillColor: "transparent",
                        marginBottom: 30,
                        transform: `translateX(${(1 - slideIn) * -100}px)`,
                    }}
                >
                    {productName}
                </div>
                <div
                    style={{
                        fontSize: 56,
                        fontWeight: 700,
                        color: "#fff",
                        opacity: textOpacity,
                        lineHeight: 1.3,
                        maxWidth: 1200,
                    }}
                >
                    {featureText}
                </div>
            </div>
        </AbsoluteFill>
    );
};

// RESULT Component - Big stat
const Result: React.FC<{ stat: string }> = ({ stat }) => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const scale = spring({ frame, fps, config: { damping: 12, mass: 0.8 } });
    const glow = interpolate(frame, [0, 60, 90], [0, 1, 0.6], { extrapolateRight: "clamp" });

    return (
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
            <div
                style={{
                    transform: `scale(${scale})`,
                    textAlign: "center",
                }}
            >
                <div
                    style={{
                        fontSize: 120,
                        fontWeight: 900,
                        background: "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
                        WebkitBackgroundClip: "text",
                        WebkitTextFillColor: "transparent",
                        textShadow: `0 0 ${glow * 60}px rgba(240, 147, 251, 0.5)`,
                    }}
                >
                    {stat}
                </div>
                <div
                    style={{
                        fontSize: 32,
                        color: "#888",
                        marginTop: 20,
                        opacity: interpolate(frame, [30, 50], [0, 1], { extrapolateRight: "clamp" }),
                    }}
                >
                    Real results. Real users.
                </div>
            </div>
        </AbsoluteFill>
    );
};

// CTA Component
const CTA: React.FC<{ text: string }> = ({ text }) => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const bounce = spring({ frame, fps, config: { damping: 8, mass: 0.5, stiffness: 200 } });
    const pulse = Math.sin(frame / 8) * 0.05 + 1;

    return (
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
            <div
                style={{
                    transform: `scale(${bounce * pulse})`,
                    padding: "30px 60px",
                    background: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                    borderRadius: 16,
                    boxShadow: "0 20px 60px rgba(102, 126, 234, 0.4)",
                }}
            >
                <span
                    style={{
                        fontSize: 48,
                        fontWeight: 700,
                        color: "#fff",
                    }}
                >
                    {text}
                </span>
            </div>
        </AbsoluteFill>
    );
};
