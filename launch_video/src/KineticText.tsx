import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring, useVideoConfig } from 'remotion';

// Simple Word-by-Word Kinetic Text Component
export const KineticText: React.FC<{
    text: string;
    startFrame: number;
    color?: string;
    fontSize?: number;
    highlightWords?: string[]; // Words to make RED or accented
}> = ({ text, startFrame, color = 'white', fontSize = 80, highlightWords = [] }) => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    // Split text into words
    const words = text.split(' ');

    // stagger duration per word (e.g. 5 frames per word)
    const stagger = 8;

    return (
        <AbsoluteFill
            style={{
                justifyContent: 'center',
                alignItems: 'center',
                flexDirection: 'row',
                flexWrap: 'wrap',
                padding: '0 100px',
                zIndex: 10
            }}
        >
            {words.map((w, i) => {
                // Calculate when this word should appear
                const delay = startFrame + i * stagger;

                // Spring animation for pop-in
                const progress = spring({
                    frame: frame - delay,
                    fps,
                    config: { damping: 200, stiffness: 200 },
                });

                const opacity = interpolate(frame, [delay, delay + 5], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
                const scale = interpolate(progress, [0, 1], [0.5, 1]);
                const translateY = interpolate(progress, [0, 1], [50, 0]);

                const isHighlight = highlightWords.includes(w.replace(/[^a-zA-Z0-9]/g, '')); // Strip punctuation for check

                return (
                    <span
                        key={i}
                        style={{
                            fontFamily: 'Impact, Helvetica, sans-serif',
                            fontWeight: 'bold',
                            textTransform: 'uppercase',
                            fontSize: fontSize,
                            color: isHighlight ? '#FF3B30' : color, // iOS Red for highlights
                            marginLeft: 15,
                            marginRight: 15,
                            opacity,
                            transform: `scale(${scale}) translateY(${translateY}px)`,
                            textShadow: '0 4px 20px rgba(0,0,0,0.8)'
                        }}
                    >
                        {w}
                    </span>
                );
            })}
        </AbsoluteFill>
    );
};
