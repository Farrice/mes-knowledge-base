# Banana Squad — Image Agent Team

> This project uses Claude Code's experimental "Agent Teams" feature to orchestrate a multi-agent image generation pipeline powered by the Gemini 3 Pro Image API (Nano Banana Pro).

## Quick Start

1. Ensure `GEMINI_API_KEY` is set in `.env`
2. Open Claude Code with experimental agent teams enabled
3. Copy the contents of `spawn-team-prompt.md` and paste it as your first message
4. The Lead agent will ask you clarifying questions about your image needs
5. Images are saved to `outputs/`

## Project Structure

```
banana-squad/
├── CLAUDE.md                 # You are here
├── .env.template             # Copy to .env with your API key
├── spawn-team-prompt.md      # The master spawn prompt — paste to create the team
├── gemini-3-image-api-guide.md  # API reference for the Generator agent
├── paperbanana.md            # Research paper — foundational framework
├── diagrams/                 # Visual workflow diagrams from the methodology
├── reference-images/         # Drop reference images here for the team
│   ├── style/                # Color palettes, aesthetic references
│   ├── composition/          # Layout and framing references
│   ├── subject/              # Subject matter references
│   ├── brand/                # Brand assets, logos, fonts
│   └── output-examples/      # Examples of desired output quality
└── outputs/                  # Generated images land here
```

## Agent Architecture (Banana Squad)

| Agent | Role | What It Does |
|-------|------|-------------|
| **Lead** | Orchestrator | Asks clarifying questions, delegates tasks, presents final results |
| **Research Agent** | Reference Analyzer | Analyzes reference images, extracts visual DNA (style, composition, color) |
| **Prompt Architect** | Prompt Engineer | Creates 5 narrative prompts per brief using photography terminology |
| **Generator Agent** | Image Creator | Calls Gemini 3 Pro API with prompts + references, saves to outputs/ |
| **Critic Agent** | Quality Reviewer | Scores images on composition, color, detail, brand alignment, impact |

## Prompting Best Practices

From the methodology, these principles produce the best results:

1. **Narrative over keywords** — Write prompts as descriptive paragraphs, not comma-separated tags
2. **Photography terms** — Use lens types, lighting setups, film stocks for realism
3. **Specificity wins** — "golden hour light filtering through venetian blinds" > "warm lighting"
4. **Conversational iteration** — Edit images through natural follow-up requests
5. **Reference images matter** — Drop 3-5 reference images for style-matching (up to 14 supported)

## Dependencies

```bash
pip install google-genai Pillow python-dotenv
```

## Key Specs

- **Model**: `gemini-2.0-flash-preview-image-generation` (or latest)
- **Max resolution**: ~4K
- **Max reference images**: 14
- **Supported formats**: PNG, JPEG, WebP
- **Aspect ratios**: Landscape, portrait, square all supported
