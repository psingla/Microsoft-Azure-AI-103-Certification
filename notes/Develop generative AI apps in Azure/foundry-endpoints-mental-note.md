# Project Endpoint vs Azure OpenAI Endpoint

> **Project = project features. OpenAI = direct model APIs. Both can generate responses.**

| | Project endpoint | Azure OpenAI endpoint |
| --- | --- | --- |
| Scope | Specific Foundry project | Resource-level OpenAI-compatible APIs |
| Use for | Foundry agents, connections, evaluations, and model calls | Chat, Responses, embeddings, or migrating OpenAI apps |
| When to choose | Your operation needs Foundry project features or project-scoped access | You only need direct model calls, such as simple chat or custom RAG, without project features |
| SDK | Foundry: `AIProjectClient` | OpenAI: `OpenAI` (v1 API) |
| Auth | Microsoft Entra ID + project permissions | Entra ID or API key, if enabled |
| URL | `https://<resource>.services.ai.azure.com/api/projects/<project>` | `https://<resource>.openai.azure.com/openai/v1/` |

[Microsoft Learn: SDKs and endpoints](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview) (source checked: 2026-10-03).
