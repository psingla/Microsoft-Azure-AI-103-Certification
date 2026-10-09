# Azure Speech: Capabilities

**Recognize input, synthesize output, translate speech, or converse live.**

Azure Speech in Foundry Tools provides APIs for speech-enabled applications:

| Need | Capability | Remember |
|---|---|---|
| Accept spoken input as text | **Speech to text** | Speech recognition: audio -> text |
| Provide spoken output | **Text to speech** | Speech synthesis: text -> audio |
| Translate spoken input into target languages | **Speech Translation** | Spoken input -> translated text or speech; supports multiple target languages |
| Build agents for real-time voice conversations | **Voice Live** | Interactive, low-latency conversations, not just one-way transcription or synthesis |

![Azure Speech feature tiles.](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/media/overview/speech-features-highlight.png)

*Image: Microsoft Learn.*

## Important: SpeechConfig vs. AudioConfig

**SpeechConfig = how the service behaves; AudioConfig = where audio comes from or goes.**

| Configuration | Controls | Examples |
|---|---|---|
| `SpeechConfig` | Service connection, authentication, and recognition/synthesis settings | Key or token, region/endpoint, recognition language, synthesis voice, custom speech endpoint where supported |
| `AudioConfig` | Audio input source or output destination | Microphone, speaker, audio file, or stream |

**Exam cue:** Change the language or voice -> `SpeechConfig`; switch from microphone input to a file -> `AudioConfig`.

[SpeechConfig reference](https://learn.microsoft.com/python/api/azure-cognitiveservices-speech/azure.cognitiveservices.speech.speechconfig?view=azure-python) | [AudioConfig reference](https://learn.microsoft.com/python/api/azure-cognitiveservices-speech/azure.cognitiveservices.speech.audio.audioconfig?view=azure-python)

## Very important: Voice Live API

**WebSocket = real-time conversation events; WebRTC = avatar video streaming.**

- Combines speech recognition, speech synthesis, avatar streaming, and audio processing for real-time voice applications.
- **JSON events over WebSocket** manage conversations, audio streams, and responses:
  - **Client events:** client -> server.
  - **Server events:** server -> client.

| Feature | Remember |
|---|---|
| Real-time audio | Supports PCM16 at supported sample rates and G.711 codecs |
| Voice options | Includes OpenAI voices and Azure custom voices |
| Avatar integration | WebRTC-based video streaming and animation |
| Audio enhancement | Built-in noise reduction and echo cancellation |

**Exam cue:** Do not confuse the WebSocket conversation channel with the WebRTC avatar stream. Feature availability and configuration depend on API version and selected model/voice.

[Microsoft Learn: Voice Live API reference (2025-10-01)](https://learn.microsoft.com/azure/ai-services/speech-service/voice-live-api-reference-2025-10-01)

[Microsoft Learn: Azure Speech overview](https://learn.microsoft.com/azure/ai-services/speech-service/overview) | [Voice Live](https://learn.microsoft.com/azure/ai-services/speech-service/voice-live)
