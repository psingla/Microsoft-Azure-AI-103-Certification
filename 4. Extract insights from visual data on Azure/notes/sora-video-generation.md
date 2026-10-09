# Sora 2: Video Generation

**Generate video -> deploy Sora 2; analyze existing video -> choose a video analysis capability.**

- **Sora 2 (preview)** is an OpenAI video generation model available in Microsoft Foundry.
- Inputs: **text prompts**, **reference images**, or **previously generated videos** for remixing. Do not assume support for arbitrary uploaded videos.
- Outputs: generated video scenes, including animation and effects; supports audio generation and targeted remix edits.
- In Foundry: **Models + endpoints -> Deploy model -> Sora 2 -> Video playground**.
- API generation is **asynchronous**: submit a job -> check status -> retrieve the completed video.

## Sora 2 capabilities

| Feature | Description |
|---|---|
| **Text to video** | Generate video from natural language prompts |
| **Image to video** | Use a reference image to guide video generation |
| **Video remix** | Make targeted adjustments to a previously generated video without starting from scratch |
| **Audio generation** | Generate audio in output videos |
| **Multiple resolutions** | Portrait: `720x1280`; landscape: `1280x720` (width x height) |
| **Variable duration** | Generate clips of **4, 8, or 12 seconds** |

**Remember: two orientations; three durations (4 / 8 / 12).** Documented defaults: portrait `720x1280`, **4 seconds**.

**Caveats:** Availability depends on supported regions and access. Content filters and responsible AI restrictions apply; model capabilities do not guarantee that every prompt or realistic scene is permitted.

[Microsoft Learn: Video generation with Sora 2](https://learn.microsoft.com/azure/foundry/openai/concepts/video-generation)
