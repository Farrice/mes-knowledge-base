import { Composition, registerRoot } from 'remotion';
import { ViralHook } from './Composition';
import './style.css'; // Optional global styles

export const RemotionRoot: React.FC = () => {
    return (
        <>
            <Composition
                id="ViralHook"
                component={ViralHook}
                durationInFrames={300} // 10 Seconds total
                fps={30}
                width={1080}
                height={1920}
            />
        </>
    );
};


