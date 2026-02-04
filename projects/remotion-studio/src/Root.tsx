import { Composition } from "remotion";
import { HelloWorld } from "./HelloWorld";
import { ProductTeaser } from "./ProductTeaser";

export const RemotionRoot: React.FC = () => {
    return (
        <>
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
