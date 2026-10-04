# AI-103 Certification Context: Must-Know Decisions

> **Purpose:** A selective revision companion, not another full set of notes. Keep what helps choose, implement, troubleshoot, or secure an exam scenario.
> **Verified against:** [Official AI-103 study guide](https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-103), accessed 2026-10-04.
> **Related:** [Full exam objectives](https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-103) | [SDK and endpoint notes](./notes/Develop%20generative%20AI%20apps%20in%20Azure/foundry-endpoints-mental-note.md)
> **Study order:** Priorities -> architecture -> connections -> retrieval -> agents -> other modalities -> evaluation and operations -> troubleshooting.

## 1. Priorities, Not Predictions

| Exam Area | Weight | What You Must Be Able to Do |
|-----------|--------|----------------------------|
| Plan and manage | 25-30% | Select models/services, deploy, secure, govern, monitor, and control cost |
| Generative AI and agents | 30-35% | Connect apps, implement RAG and tools, orchestrate agents, evaluate and optimize |
| Computer vision | 10-15% | Generate/edit images and video; understand visual content safely |
| Text analysis | 10-15% | Extract, summarize, translate, and integrate speech |
| Information extraction | 10-15% | Extract structured content and build retrieval/grounding pipelines |

Planning plus generative AI/agents account for **55-65%** of the published weighting. Start there, but do not skip the other three domains. "Must-know" below is a study prioritization, not a guarantee of particular exam questions or complete syllabus coverage.

## 2. Must Know: Choose the Simplest Suitable Architecture

| Requirement | Starting Choice |
|-------------|-----------------|
| Transform or summarize supplied content | Direct model call |
| Answer from private or frequently changing knowledge | RAG |
| Follow prescribed steps with explicit business controls | Workflow |
| Dynamically choose tools or next steps | Agent |
| Combine controlled business steps with flexible reasoning | Workflow plus agents/models |
| Use managed agent behavior with instructions and supported tools | Prompt agent |
| Run custom orchestration or runtime code | Hosted agent or an agent framework in your application |

- Select a model by task capability, modalities, context length, quality, latency, cost, regional availability, and deployment constraints.
- Choose a smaller model when evaluation shows it meets requirements; do not assume the largest model is necessary.
- **Prompting** changes task instructions/examples. **RAG** supplies external knowledge. **Fine-tuning** can specialize learned behavior; it is not a substitute for retrieving current facts.
- Benchmark results narrow candidates; evaluate finalists on representative application data.

> Exam insight: RAG can be conversational and can be used inside an agent. A predefined workflow can contain nondeterministic model calls. These are composable patterns, not mutually exclusive categories.

## 3. Must Know: Endpoint, SDK, Authentication, Authorization

| Need | Use |
|------|-----|
| Project connections and project-scoped capabilities | Project endpoint + `AIProjectClient` from `azure-ai-projects` |
| Direct supported model calls | Azure OpenAI endpoint + `openai` |
| Project access plus model inference | Project client + `get_openai_client()`; the model calls use the OpenAI client |
| Microsoft Entra authentication in Python | `azure-identity`, commonly `DefaultAzureCredential` |
| Select which deployed model receives a request | Model deployment name |

- An **endpoint** identifies the service/project API; an **SDK** makes requests; a **credential** establishes identity; **RBAC** determines permitted actions.
- Successful authentication does not grant every permission. Match the role and scope to the required operation.
- Prefer managed identity for Azure-hosted production applications. Do not hardcode keys.
- Match client configuration to the API generation. Do not mix connection-string examples, project endpoints, and OpenAI base URLs indiscriminately.

> Exam insight: Know how to read and complete client/credential/model-call patterns. Do not rely on claims that SDK implementation details cannot appear on the exam.

For the SDK comparison, client setup, and Responses API, read the [SDK and endpoint notes](./notes/Develop%20generative%20AI%20apps%20in%20Azure/foundry-endpoints-mental-note.md), then continue below.

## 4. Must Know: Retrieval and Extraction End to End

```text
Ingest -> OCR/layout/field extraction -> Enrich/chunk -> Embed -> Index
Query -> Retrieve -> Optional semantic reranking -> Supply context -> Generate
```

| Distinction | Remember |
|-------------|----------|
| Keyword search | Lexical matching; useful for exact terms and identifiers |
| Vector search | Similarity using embeddings |
| Hybrid search | Combines keyword and vector retrieval |
| Semantic ranking | Reranks retrieved results; not the definition of hybrid search |
| OCR | Extracts text; does not by itself supply all layout/field semantics |
| Document Intelligence | Document-focused extraction, including prebuilt and custom models |
| Content Understanding | Analyzers for structured information from documents and other modalities |

- Preserve source identifiers and useful structure for citations, filtering, and downstream reasoning.
- Understand built-in/custom enrichment skills, chunking, embedding compatibility, and index updates.
- Configure Content Understanding analyzers for required fields and structured or Markdown outputs.
- Enforce document permissions during retrieval; an instruction such as "do not reveal confidential data" is insufficient.

> Exam insight: Grounding reduces unsupported generation but does not guarantee correctness. Evaluate retrieval quality separately from answer quality.

## 5. Must Know: Tools, Memory, and Orchestration

| Scenario | Appropriate Capability |
|----------|------------------------|
| Search uploaded files | File Search |
| Ground answers in an existing enterprise search index | Azure AI Search |
| Calculate or analyze data using sandboxed code | Code Interpreter |
| Execute an application-specific operation | Function calling |
| Integrate an API described by a supported OpenAPI schema | OpenAPI tool |
| Connect to a server exposing standardized tools/context | MCP |
| Retain conversation context | Conversation state / memory |

**Custom function-calling loop:**

```text
Define tool schema -> Model requests call -> App/framework validates and executes
                   -> Return result with matching call ID -> Model continues
```

- A tool description/schema helps the model select a tool; it is not an authorization boundary.
- Validate arguments, enforce permissions, handle failures, and require approval for sensitive actions.
- **Memory** retains interaction state; **retrieval** supplies relevant knowledge. Both need access and retention controls.
- **Sequential** orchestration fits dependent stages; **parallel** fits independent work; **orchestrator/subagent** fits delegation to specialists.
- Use explicit completion criteria, step limits, and controlled retries. More agents add coordination, latency, and cost.
- MCP standardizes integration; it does not automatically host a remote server or make its outputs trustworthy.

## 6. Must Know: The Other Three Domains

| Domain | Minimum Revision Checklist |
|--------|----------------------------|
| Vision | Generation versus analysis; reference-image inputs; inpainting/masks and editing controls; video generation/editing/analysis; captions, visual Q&A, accessibility descriptions; object/region identification |
| Multimodal understanding and safety | Content Understanding analyzers and the guide's single-task/pro-mode objectives; unsafe visual content; image-based indirect prompt injection; watermarking and visual policy requirements |
| Text | Entities, topics, sentiment/tone, summaries, sensitive-content detection; domain-specific extraction; structured JSON outputs; Translator versus LLM-powered translation |
| Speech | Speech-to-text versus text-to-speech; custom speech; speech translation; audio reasoning; speech as an agent input/output modality |
| Extraction | OCR plus layout and field extraction; multimodal ingestion; enrichment/indexing; structured or Markdown output feeding RAG and tools |

**Do not memorize a model name as proof of capability.** Verify that the selected model/API supports the required operation, such as image editing or audio input.

## 7. Must Know: Evaluation, Safety, and Operations

| Measure / Control | What It Establishes |
|-------------------|---------------------|
| Groundedness | Whether claims are supported by supplied context |
| Relevance | Whether the answer addresses the request |
| Coherence and fluency | Logical organization and readable language |
| Safety evaluation | Harmful content or behavior under normal and adversarial inputs |
| Task success and tool correctness | Whether the agent performed the intended task appropriately |
| Traces | Where time, errors, and tool/model decisions occurred |
| Token usage, latency, error rate | Operational cost, responsiveness, and reliability |

- Use representative datasets and clear acceptance criteria; evaluate changes before release and monitor after deployment.
- Reflection/self-critique can help refine an answer, but a model reviewing itself is not independent proof. Check evidence and observable outcomes.
- Engagement matters when the experience requires it, not for every workload. Determinism alone proves neither relevance nor correctness.
- Combine safety filters with least-privilege tools, input validation, approval gates, and auditing.
- Treat retrieved text, tool results, and embedded image text as potentially untrusted instructions.
- Private endpoints control network exposure; identity/RBAC control access. Neither replaces the other.
- Understand quotas, request/token rate limits, deployment capacity, and scaling. More application instances do not automatically increase model quota.
- Version prompts, tool schemas, model/deployment configuration, and infrastructure. Use evaluation gates, environment separation, and rollback in CI/CD.

> Exam insight: Content filtering is not authorization. A harmless-looking request to transfer money still requires access checks and appropriate approval.

## 8. High-Value Additions: Diagnose Before Changing the Model

These are practical reasoning aids mapped to the objectives, not separately weighted exam topics.

| Symptom | First Checks |
|---------|--------------|
| Fluent answer, wrong facts | Retrieved evidence, groundedness, source freshness, prompt constraints |
| Correct facts, wrong question answered | Relevance, query interpretation, conversation context |
| Required information never retrieved | OCR/extraction quality, chunking, filters/permissions, index freshness, retrieval mode |
| Tool selected but operation failed | Schema/arguments, credentials and role scope, service response, timeout |
| Slow or expensive agent | Trace model/tool latency, repeated calls, oversized context, unnecessary agent stages |
| Rate-limit errors | Deployment quota/capacity, request and token rates, concurrency, retry guidance |
| Valid JSON, incorrect values | Semantic validation and source evidence; schema compliance is not factual correctness |
| Repeated external action after retry | Idempotency, persisted execution state, approval scope |

**Highest-value practice:** Build one small grounded assistant that retrieves documents, calls one custom tool, uses appropriate authentication, records traces, and is evaluated for relevance, groundedness, safety, and task success. Then explain where each failure would be diagnosed.

## 9. Deliberately Left Out

- Exact quota counts, subnet sizes, container ports, and preview-version strings.
- Fixed "best model" tables, prices, and model context-window figures.
- Historical SDK migration details and exhaustive framework class names.
- Broad claims such as "RAG cannot remember," "managed means free," or "all model APIs support every model."

Look up changing implementation details when needed. For final preparation, use the [official objectives](https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-103) as the coverage checklist; use this file for decisions and distinctions worth retaining.
