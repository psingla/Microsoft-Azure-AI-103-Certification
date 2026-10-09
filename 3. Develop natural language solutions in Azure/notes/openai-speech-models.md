# OpenAI Speech Models

**TTS: text -> audio; STT: audio -> text; diarization: who spoke when.**

| Task | Model | Remember |
|---|---|---|
| Text-to-speech | `gpt-4o-mini-tts` | Generate speech from text; supports instructions for speaking style |
| Speech-to-text | `gpt-4o-transcribe` | Transcribe spoken audio |
| Speech-to-text | `gpt-4o-mini-transcribe` | Smaller transcription model |
| Speech-to-text with speaker diarization | `gpt-4o-transcribe-diarize` | Transcription with speaker labels; not proof of a speaker's real identity |

**Model-name caveat:** The supplied `gpt-4o-tts` name was not confirmed in the Azure model catalog consulted. Verify it before using it as a deployment/model ID; the documented GPT-4o TTS model is `gpt-4o-mini-tts`.

Availability depends on region, deployment type, and model version. In Azure API calls, use your deployment name where required, which may differ from the model ID.

[Microsoft Learn: Audio models](https://learn.microsoft.com/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure#audio-models) | [Microsoft Learn: Azure OpenAI updates](https://learn.microsoft.com/azure/foundry-classic/openai/whats-new)
