# Foundry: Endpoints, SDKs, and Responses

> **Project = project features. OpenAI = direct model APIs. Both can generate responses.**

## 1. Choose the endpoint

| | Project endpoint | Azure OpenAI endpoint |
| --- | --- | --- |
| Scope | Specific Foundry project | Resource-level OpenAI-compatible APIs |
| Use for | Foundry agents, connections, evaluations, and model calls | Chat, Responses, embeddings, or migrating OpenAI apps |
| When to choose | Your operation needs Foundry project features or project-scoped access | You only need direct model calls, such as simple chat or custom RAG, without project features |
| Direct SDK client | Foundry: `AIProjectClient` | OpenAI: `OpenAI` (v1 API) |
| Auth | Microsoft Entra ID + project permissions | Entra ID or API key, if enabled |
| URL | `https://<resource>.services.ai.azure.com/api/projects/<project>` | `https://<resource>.openai.azure.com/openai/v1/` |

## 2. Choose MAF, Foundry SDK, or OpenAI SDK

**Microsoft Agent Framework (MAF) = agent behavior; Foundry SDK = platform access; endpoint = where requests go.**

| | MAF | Foundry SDK | OpenAI SDK |
| --- | --- | --- | --- |
| **Features** | Agent loops, tools, conversation state, multi-agent workflows, and model-provider integrations | Foundry Agent Service, hosted tools and approvals, connections, metadata, cloud evaluations, tracing integration, and model access through the project's OpenAI client | Chat Completions, Responses, embeddings, Images, and model tool calls where supported; your app supplies orchestration |
| **When to use** | Build agents or multi-agent workflows with reusable orchestration | Access Foundry-specific project and service features | Make direct model calls or move existing OpenAI code to Azure with minimal changes and Foundry coupling |

- **Compatibility is not universal:** API support depends on the endpoint and deployed model. Supported non-OpenAI models can also use the OpenAI SDK; model vendor alone does not determine SDK choice.
- **OpenAI SDK is not a project-management SDK:** it does not replace Foundry's connections or cloud evaluation APIs, even when used through the project.
- **They work together:** MAF's Foundry integration uses the Foundry SDK underneath; it does not replace all Foundry SDK capabilities.
- **MAF does not remove the endpoint choice:** its Foundry integration uses the project endpoint; its Azure OpenAI integration uses the corresponding model endpoint.

## 3. Connect the Foundry and OpenAI clients

**Foundry connects to the project; the OpenAI SDK provides the chat client.**

- Install `openai` alongside `azure-ai-projects` and `azure-identity` for this workflow.
- `project.get_openai_client()` returns an OpenAI SDK client. Import OpenAI classes or types when used explicitly; obtaining the client through Foundry does not itself require an `import openai` statement.
- **Combine them:** use `AIProjectClient` for project features and its OpenAI client for supported model APIs. Let `get_openai_client()` configure the project's OpenAI route; the bare project URL is not an OpenAI `base_url`.

## 4. Generate responses and maintain conversation context

**Prefer Responses for new Foundry response-generation workflows where supported; Chat Completions is not universally replaced.**

- **Stateful turns:** link requests with `previous_response_id` or use a supported conversation mechanism; unrelated requests do not automatically share context.
- **Unified experience:** combines Chat Completions and Assistants-style capabilities, including tool use.
- **Simple integration:** call `client.responses.create(...)` through the OpenAI-compatible client.
- **Check model support:** Foundry catalog availability or OpenAI compatibility alone does not guarantee Responses support, including for non-OpenAI models. Check the model, endpoint, and region; use Chat Completions when required for compatibility.

## Sources

[Microsoft Learn: SDKs and endpoints](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview) (source checked: 2026-10-04).

[Microsoft Learn: Responses API](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses) (source checked: 2026-10-04).
