import { AbsoluteFill, Img, interpolate, useCurrentFrame, Sequence, useVideoConfig, random } from 'remotion';
import { staticFile } from 'remotion';
import { KineticText } from './KineticText';

// Glitch Effect Helper
const GlitchLayer = () => {
    const frame = useCurrentFrame();
    const opacity = random(frame) > 0.8 ? 0.3 : 0; // Random flickers
    const transformX = random(frame + 1) * 20 - 10;

    return (
        <AbsoluteFill style={{
            backgroundColor: 'rgba(255, 0, 0, 0.2)', // Red tint glitch
            opacity: opacity,
            transform: `translateX(${transformX}px)`,
            mixBlendMode: 'overlay'
        }} />
    );
};

// Scene 1: Chaos (0-90 frames) - High Energy, Staccato
const ChaosScene = () => {
    const frame = useCurrentFrame();
    const shakeX = Math.sin(frame * 0.8) * 10; // More aggressive shake
    const scale = interpolate(frame, [0, 90], [1, 1.2]); // Slow creep zoom (anxiety)

    return (
        <AbsoluteFill style={{ backgroundColor: 'black' }}>
            <Img
                src={staticFile("chaos.png")}
                style={{
                    width: '100%',
                    height: '100%',
                    objectFit: 'cover',
                    transform: `translate(${shakeX}px, 0) scale(${scale})`,
                    filter: 'contrast(1.2) saturation(0.8)' // Gritty look
                }}
            />
            <GlitchLayer />

            {/* Rapid Fire Copy */}
            <Sequence from={10} durationInFrames={25}>
                <KineticText text="4 INVOICES" startFrame={0} fontSize={100} color="#FF3B30" />
            </Sequence>
            <Sequence from={35} durationInFrames={25}>
                <KineticText text="12 EMAILS" startFrame={0} fontSize={100} color="#FF3B30" />
            </Sequence>
            <Sequence from={60}>
                <KineticText text="ZERO REAL WORK" startFrame={0} highlightWords={['ZERO']} fontSize={110} />
            </Sequence>
        </AbsoluteFill>
    );
};

// Scene 2: Peace (90-150 frames) - The Relief
const PeaceScene = () => {
    const frame = useCurrentFrame();
    // "Crash Zoom" out - start close, snap to wide
    const scale = interpolate(frame, [0, 5], [1.5, 1], { extrapolateRight: 'clamp' });

    return (
        <AbsoluteFill style={{ backgroundColor: 'white' }}>
            <Img
                src={staticFile("peace.png")}
                style={{
                    width: '100%',
                    height: '100%',
                    objectFit: 'cover',
                    transform: `scale(${scale})`
                }}
            />
            <Sequence from={10}>
                <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
                    <h1 style={{
                        fontFamily: 'Georgia, serif',
                        fontStyle: 'italic',
                        fontSize: 70,
                        color: '#333',
                        backgroundColor: 'rgba(255,255,255,0.9)',
                        padding: '20px 60px',
                        boxShadow: '0 10px 30px rgba(0,0,0,0.1)',
                        opacity: interpolate(frame, [10, 20], [0, 1])
                    }}>
                        The System.
                    </h1>
                </AbsoluteFill>
            </Sequence>
        </AbsoluteFill>
    );
};

// Scene 3: UI (150-300 frames) - The Solution
const UIScene = () => {
    const frame = useCurrentFrame();
    const translateY = interpolate(frame, [0, 20], [200, 0], { extrapolateRight: 'clamp' });

    return (
        <AbsoluteFill style={{ backgroundColor: '#111' }}>
            <Img
                src={staticFile("ui.png")}
                style={{
                    width: '100%',
                    height: '100%',
                    objectFit: 'contain',
                    transform: `translateY(${translateY}px)`
                }}
            />
            <Sequence from={10} durationInFrames={60}>
                <AbsoluteFill style={{ top: 150, alignItems: 'center' }}>
                    <KineticText text="STOP PLAYING JANITOR" startFrame={0} fontSize={70} color="#888" />
                </AbsoluteFill>
            </Sequence>

            <Sequence from={70}>
                <AbsoluteFill style={{ top: 150, alignItems: 'center' }}>
                    <KineticText text="START BEING CEO" startFrame={0} highlightWords={['CEO']} fontSize={90} color="white" />
                </AbsoluteFill>
            </Sequence>
        </AbsoluteFill>
    );
};

export const ViralHook = () => {
    return (
        <AbsoluteFill>
            <Sequence from={0} durationInFrames={90}>
                <ChaosScene />
            </Sequence>
            <Sequence from={90} durationInFrames={60}>
                <PeaceScene />
            </Sequence>
            <Sequence from={150} durationInFrames={150}>
                <UIScene />
            </Sequence>

            {/* Global Vignette for Cinematic Feel */}
            <AbsoluteFill style={{
                background: 'radial-gradient(circle, transparent 40%, rgba(0,0,0,0.4) 100%)',
                pointerEvents: 'none'
            }} />
        </AbsoluteFill>
    );
};
