# AI Image-Generation Guardrails

## Appropriate uses

- Quiet paper, fog, or tactile texture fields.
- Nonrepresentational tonal backgrounds.
- Atmosphere that supports typography without becoming the subject.
- Early reference exploration that is never mistaken for a final identity asset.

## Inappropriate uses

- Final typography when an editable layout tool can typeset exact copy.
- Farrice's face, body, clothing, or identity.
- Supplement products or labels presented as real client work.
- Scientific, clinical, legal, or compliance imagery used as credibility theater.
- Decorative imagery added merely to fill open space.

## Positive prompt architecture

Use this structure:

**Container + light + material + spatial behavior + tonal system + mood**

Example:

```text
Wide 4:1 background field.
Soft even studio illumination.
Subtle tactile paper and fog texture with very low tonal variation.
Calm low-information left third and clean central-right typography field.
Near-monochrome warm off-white, soft gray, and graphite atmosphere.
Restrained, contemporary, decisive.
The scene contains only abstract nonrepresentational texture.
```

Hard production constraints should be stated separately:

- typography-free;
- logo-free;
- person-free;
- product-free;
- no imitated brand marks or campaign layouts.

Generate the background layer separately. Typeset exact copy afterward in SVG, PPTX, Figma, Illustrator, or another editable layout environment.

