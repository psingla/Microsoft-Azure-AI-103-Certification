# Project Endpoint vs Azure OpenAI Endpoint

> **Project = project features. OpenAI = direct model APIs. Both can generate responses.**

| | Project endpoint | Azure OpenAI endpoint |
| --- | --- | --- |
| Scope | Specific Foundry project | Resource-level OpenAI-compatible APIs |
| Use for | Foundry agents, connections, evaluations, and model calls | Chat, Responses, embeddings, or migrating OpenAI apps |
| When to choose | Your operation needs Foundry project features or project-scoped access | You only need direct model calls, such as simple chat or custom RAG, without project features |
| Direct SDK client | Foundry: `AIProjectClient` | OpenAI: `OpenAI` (v1 API) |
| Auth | Microsoft Entra ID + project permissions | Entra ID or API key, if enabled |
| URL | `https://<resource>.services.ai.azure.com/api/projects/<project>` | `https://<resource>.openai.azure.com/openai/v1/` |

## MAF vs Foundry SDK

**Microsoft Agent Framework (MAF) = agent behavior; Foundry SDK = platform access; endpoint = where requests go.**

| Choose | When |
| --- | --- |
| MAF | Building agents with tools, conversation state, or multi-agent workflows; use its reusable orchestration. |
| Foundry SDK | Calling Foundry project APIs directly for agents, connections, evaluations, or project configuration, without framework abstractions. |
| OpenAI SDK | Making direct model calls, such as chat or embeddings, without agent orchestration. |

- **They work together:** MAF's Foundry integration uses the Foundry SDK underneath; it does not replace all Foundry SDK capabilities.
- **MAF does not remove the endpoint choice:** its Foundry integration uses the project endpoint; its Azure OpenAI integration uses the corresponding model endpoint.

[Microsoft Learn: SDKs and endpoints](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview) (source checked: 2026-10-03).
