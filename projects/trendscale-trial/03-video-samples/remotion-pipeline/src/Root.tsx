import React from "react";
import { Composition } from "remotion";
import { Ad, AdManifestSchema, calculateAdMetadata, WIDTH, HEIGHT, FPS } from "./Ad";

// Placeholder defaultProps — real renders always pass a manifest via
// `--props` (see scripts/render.mjs / scripts/still.mjs). This only exists so
// the composition is valid when opened cold in Remotion Studio.
const PLACEHOLDER_PROPS = {
  adName: "placeholder",
  crossfadeFrames: 0,
  clips: [
    {
      id: "placeholder",
      path: "assets/clips/placeholder.mp4",
      label: "Drop a manifest with --props to preview a real ad",
      trimInSeconds: 0,
      trimOutSeconds: null,
      targetDurationSeconds: 5,
      resolvedExists: false,
    },
  ],
  vo: [],
  captions: [],
  accentWords: [],
  theme: {
    fontFamily: "'Inter Tight','Inter',-apple-system,'Segoe UI',sans-serif",
    fontFileExists: false,
    textColor: "#F2F1EC",
    accentColor: "#D9A441",
    backgroundColor: "#0B111C",
    captionBottomOffset: 420,
  },
  endCard: {
    productImage: "assets/images/placeholder.png",
    productImageExists: false,
    offerLine: "Offer line",
    guaranteeLine: "Guarantee line",
    holdSeconds: 3,
  },
};

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="Ad"
        component={Ad}
        durationInFrames={FPS * 5}
        fps={FPS}
        width={WIDTH}
        height={HEIGHT}
        schema={AdManifestSchema}
        defaultProps={PLACEHOLDER_PROPS}
        calculateMetadata={calculateAdMetadata}
      />
    </>
  );
};
