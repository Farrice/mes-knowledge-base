import { Composition } from "remotion";
import { HelloWorld } from "./HelloWorld";
import { ProductTeaser } from "./ProductTeaser";
import { ViralReel } from "./ViralReel";
import { KittyCaatPitch } from "./KittyCaatPitch";
import { ProteinRecipeUGC } from "./ProteinRecipeUGC";

export const RemotionRoot: React.FC = () => {
    return (
        <>
            <Composition
                id="ProteinRecipeUGC"
                component={ProteinRecipeUGC}
                durationInFrames={1200}
                fps={30}
                width={1080}
                height={1920}
            />
            <Composition
                id="KittyCaatPitch"
                component={KittyCaatPitch}
                durationInFrames={1500}
                fps={30}
                width={1080}
                height={1920}
            />
            <Composition
                id="ViralReel"
                component={ViralReel}
                durationInFrames={450}
                fps={30}
                width={1080}
                height={1920}
            />
            <Composition
                id="HelloWorld"
                component={HelloWorld}
                durationInFrames={150}
                fps={30}
                width={1920}
                height={1080}
            />
            <Composition
                id="ProductTeaser"
                component={ProductTeaser}
                durationInFrames={450}
                fps={30}
                width={1080}
                height={1920}
                defaultProps={{
                    hookText: "Stop wasting 4 hours on content",
                    productName: "AI Authority Architect",
                    featureText: "Turn 1 idea into 30 days of LinkedIn posts in 15 minutes",
                    resultStat: "10x Faster",
                    ctaText: "Try It Free →",
                }}
            />
        </>
    );
};
