# Mental Note: Project Endpoint vs Azure OpenAI Endpoint

## Remember this

> **Project endpoint = work with the AI project.**
> **Azure OpenAI endpoint = call models directly using OpenAI APIs.**

Think of Foundry as a workplace:

- **Project endpoint: the project office.** Access project connections, agents, evaluations, and models in the project context.
- **Azure OpenAI endpoint: the direct model counter.** Send requests to deployed models without using the Foundry project API.

**Important:** Both paths can generate AI responses. The project endpoint is not just for administration, and the Azure OpenAI endpoint is not a different model.

## Side-by-side comparison

| Question | Project endpoint | Azure OpenAI endpoint |
| --- | --- | --- |
| What does it address? | A specific Foundry project. | The resource's OpenAI-compatible API surface; it is not a project-management endpoint. |
| Typical URL | `https://<resource>.services.ai.azure.com/api/projects/<project>` | `https://<resource>.openai.azure.com/openai/v1/` |
| Usual SDK | Microsoft Foundry SDK; in Python, `azure-ai-projects` and `AIProjectClient`. | OpenAI SDK; for the v1 API in Python, `OpenAI`. |
| Main purpose | Combine model calls with Foundry-specific project capabilities. | Direct model calls and compatibility with OpenAI-based applications and libraries. |
| Typical uses | Project connections, Foundry agents, evaluations, and supported platform tools. | Chat Completions, Responses, embeddings, and other supported OpenAI APIs. |
| Authentication | Use Microsoft Entra ID and the appropriate project permissions. | Microsoft Entra ID or an API key, subject to resource configuration. |
| Main selection rule | "My app needs the project and its features." | "My app primarily needs the model API." |

The Azure OpenAI endpoint can be displayed as the resource URL without `/openai/v1/`. The table shows the base URL used by the modern OpenAI v1 client. Copy the endpoint from your resource and follow the configuration for your SDK/API version.

## Why do both SDKs have an OpenAI-compatible client?

**OpenAI-compatible describes the client interface, not necessarily the endpoint or all available features.**

- With the Foundry SDK, initialize `AIProjectClient` with the **project endpoint**. Its `get_openai_client()` helper provides an OpenAI-compatible client for supported calls in the project context.
- With the OpenAI SDK, configure the client directly with the **Azure OpenAI API base URL**.
- Similar method names do not mean identical API coverage. Check support for the endpoint, model, and SDK version you use.
- In the current Foundry API, the project OpenAI-compatible client uses the project's `/openai` route. Let the SDK construct it rather than replacing the project URL with the resource-level `/openai/v1/` URL.

## When should I use which?

| Scenario | Choose | Why |
| --- | --- | --- |
| A simple chatbot that sends a prompt and displays a model response. | Azure OpenAI endpoint + OpenAI SDK. | Direct model access is enough. The project endpoint can also support chat if you already use Foundry features. |
| Migrate an existing OpenAI-based app to Azure. | Azure OpenAI endpoint + OpenAI SDK. | Retain familiar OpenAI interfaces, while checking Azure/model-specific support. |
| Generate embeddings for a vector search index. | Azure OpenAI endpoint + OpenAI SDK. | Direct access to the embeddings API. |
| Use Foundry-managed agents, project connections, or Foundry evaluation capabilities. | Project endpoint + Foundry SDK. | These require project-specific functionality beyond ordinary model calls. |
| Build a custom RAG app that queries Azure AI Search itself and passes retrieved text to a model. | Azure OpenAI endpoint can be sufficient for the model call. | RAG alone does not require the Foundry project endpoint; Search has its own client and endpoint. |
| Combine Foundry project operations with an API available through the direct model endpoint. | Both, where needed. | Endpoint choice is per operation, not necessarily one exclusive choice for the entire app. |

## Exam traps

- **Not "management vs inference":** the project path can also invoke models.
- **Not "OpenAI SDK means public OpenAI":** configuring an Azure endpoint sends requests to Azure.
- **Not "Azure OpenAI endpoint means only OpenAI-branded models":** supported Foundry models sold by Azure can also be exposed through OpenAI-compatible APIs.
- **Not "endpoint selects the model":** the request's `model` value normally identifies your deployment name; use that name rather than assuming the catalog model name.
- **Not "every endpoint supports every feature":** model and API support vary. Do not mix older `AzureOpenAI` configuration examples with modern `OpenAI` v1 configuration.

## One-line recall

> **Need project features? Project endpoint. Need direct model APIs? Azure OpenAI endpoint. Need both? Use both.**

## Official reference

- [Microsoft Learn: Get started with Microsoft Foundry SDKs and endpoints](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/sdk-overview)

Based on documentation checked on 2026-10-03. Foundry SDKs and API coverage evolve; match examples to your installed SDK version.
