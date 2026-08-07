# Video Enhancement Processing Summary

**Disclaimer:** Enhanced output is a viewing aid only. It does not prove contact, fault, causation, or responsibility.

## Source
- Input: `/private/var/folders/kz/kfs_j6zs7czgk1_dlwp_p7580000gn/T/TemporaryItems/com.apple.Photos.NSItemProvider/uuid=E86183C1-B5FD-4527-86CB-90E7091B014B&code=001&library=1&type=3&mode=1&loc=true&cap=true.mp4/1000010463.mp4`
- SHA-256 before processing: `a4f821d543dfe1355c19ff6d3bfbc88da4f4cb308c5ef2df3c81156801e7ac7d`
- Size before processing: `16209080` bytes
- Duration: `39.864000` seconds
- Video: `1280x720` at `74750/4983` fps

## Outputs
- Enhanced video: `/Users/farricecain/Codex Antigravity/deliverables/video-enhancement/1000010463-20260511-083917/enhanced.mp4`
- Side-by-side comparison: `/Users/farricecain/Codex Antigravity/deliverables/video-enhancement/1000010463-20260511-083917/comparison.mp4`
- Slow-motion export: `/Users/farricecain/Codex Antigravity/deliverables/video-enhancement/1000010463-20260511-083917/enhanced-slowmo.mp4`

## Processing Settings
- Extracted frames: `598`
- Brightness: `0.03`
- Contrast: `1.2`
- Denoise: `hqdn3d`
- Denoise strength: `1.0`
- Sharpen: `0.8`
- Scale: `1.5`
- Stabilization: `False`
- AI upscaling requested: `True`
- Slow-motion factor: `2.0`

## FFmpeg Filter Chain
`eq=brightness=0.03:contrast=1.2,hqdn3d=1.500:1.500:6.000:6.000,scale=trunc(iw*1.5/2)*2:trunc(ih*1.5/2)*2:flags=lanczos,unsharp=5:5:0.800:5:5:0.0,format=yuv420p`

## Interpretation Boundary
Use these outputs to inspect the clip more comfortably. Do not treat them as proof that any person or object made contact with glass, caused damage, or is responsible for the shattering.
