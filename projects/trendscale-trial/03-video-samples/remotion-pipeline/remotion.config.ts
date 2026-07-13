import { Config } from "@remotion/cli/config";

// The folder-drop workflow uses `assets/` (not Remotion's default `public/`)
// so manifest paths can read literally as `assets/clips/H3.mp4`.
Config.setPublicDir("assets");
Config.setVideoImageFormat("jpeg");
Config.setOverwriteOutput(true);
