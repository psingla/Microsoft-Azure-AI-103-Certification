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

## Foundry chat uses the OpenAI SDK

**Foundry connects to the project; the OpenAI SDK provides the chat client.**

- Install `openai` alongside `azure-ai-projects` and `azure-identity` for this workflow.
- `project.get_openai_client()` returns an OpenAI SDK client. Import OpenAI classes or types when used explicitly; obtaining the client through Foundry does not itself require an `import openai` statement.
- **Combine them:** use `AIProjectClient` for project features and its OpenAI client for supported model APIs. Let `get_openai_client()` configure the project's OpenAI route; the bare project URL is not an OpenAI `base_url`.

## Choosing MAF, Foundry SDK, or OpenAI SDK

**Microsoft Agent Framework (MAF) = agent behavior; Foundry SDK = platform access; endpoint = where requests go.**

| Choose | When |
| --- | --- |
| MAF | Building agents with tools, conversation state, or multi-agent workflows; use its reusable orchestration. |
| Foundry SDK | Foundry Agent Service, hosted tools and approval workflows, cloud evaluations, project connections and metadata, and tracing integration. Choose for Foundry-specific platform features. |
| OpenAI SDK | Direct inference with maximum OpenAI API compatibility and minimal Foundry coupling: Chat Completions, Responses, embeddings, or Images where supported. Useful for moving existing OpenAI code to Azure. |

- **Compatibility is not universal:** API support depends on the endpoint and deployed model. Supported non-OpenAI models can also use the OpenAI SDK; model vendor alone does not determine SDK choice.
- **OpenAI SDK is not a project-management SDK:** it does not replace Foundry's connections or cloud evaluation APIs, even when used through the project.
- **They work together:** MAF's Foundry integration uses the Foundry SDK underneath; it does not replace all Foundry SDK capabilities.
- **MAF does not remove the endpoint choice:** its Foundry integration uses the project endpoint; its Azure OpenAI integration uses the corresponding model endpoint.

[Microsoft Learn: SDKs and endpoints](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview) (source checked: 2026-10-04).
