import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate, spring } from "remotion";

export const HelloWorld: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const opacity = interpolate(frame, [0, 30], [0, 1], {
        extrapolateRight: "clamp",
    });

    const scale = spring({
        frame,
        fps,
        config: {
            damping: 200,
        },
    });

    return (
        <AbsoluteFill
            style={{
                justifyContent: "center",
                alignItems: "center",
                backgroundColor: "#0f0f0f",
                fontFamily: "system-ui, sans-serif",
            }}
        >
            <div
                style={{
                    transform: `scale(${scale})`,
                    opacity,
                    fontSize: 100,
                    fontWeight: "bold",
                    background: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                    WebkitBackgroundClip: "text",
                    WebkitTextFillColor: "transparent",
                    textAlign: "center",
                }}
            >
                Hello Remotion!
            </div>
            <div
                style={{
                    opacity: interpolate(frame, [30, 60], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }),
                    fontSize: 32,
                    color: "#888",
                    marginTop: 20,
                }}
            >
                AI-Powered Video Creation
            </div>
        </AbsoluteFill>
    );
};
