# Microsoft Agent Framework (MAF)

**Remember: AutoGen simplicity + Semantic Kernel enterprise features + explicit workflows.**

- **Successor to both Semantic Kernel and AutoGen**, built by the same engineering teams.
- **AutoGen contribution:** intuitive single- and multi-agent abstractions.
- **Semantic Kernel contribution:** session-based state management, type safety, execution filters/middleware, and telemetry.
- **Graph-based workflows:** explicit control over multi-agent execution paths, including long-running and human-in-the-loop processes.
- **Consistent agent interface across model providers:** Python uses `Agent` for standard model-backed agents; .NET uses the `AIAgent` base abstraction. Avoid assuming every SDK's base class is named `Agent`.

## Core building blocks

| Feature | Remember |
| --- | --- |
| **Model clients** | Common interfaces for connecting to different AI providers. |
| **Agent session** | Maintains conversation state across turns; durable persistence depends on configured storage. |
| **Context providers** | Pluggable memory/context components that dynamically supply relevant information. |
| **Function tools** | Custom functions you expose to the agent; the framework generates tool schemas. |
| **MCP clients** | Connect to MCP servers and discover available tools at runtime. |
| **Middleware** | Intercept, log, or modify execution before/after agent, model, or tool calls. |
| **Workflow orchestration** | Explicit graphs for sequential, concurrent, group-chat, and handoff patterns. |

**Distinction:** sessions retain conversation state; context providers supply relevant context; middleware controls execution.

## Multi-agent orchestration and workflows

**Remember: specialize, combine, sequence, route.**

Compared with one agent handling every responsibility, orchestration lets you:

- **Specialize:** give agents distinct skills, roles, or perspectives.
- **Combine:** merge or cross-check outputs to support better decisions.
- **Sequence:** make each step build on earlier results.
- **Route:** hand off control dynamically using context or rules.

**MAF workflows** define structured execution paths that combine agents with code and other components. They are not limited to multiple agents or a linear sequence: they can branch, run concurrently, and include human input.

**Use when:** a task benefits from collaboration, specialization, or redundancy. More agents do not guarantee better accuracy or efficiency; coordination adds complexity, latency, and cost.

### Workflow components

**Remember: executors work, edges route, events report, checkpoints resume.**

- **Executors:** receive messages, run an agent or custom logic, and emit results.
- **Edges:** control message flow between executors.
- **Events:** expose progress, outputs, errors, and requests for observability/debugging.
- **Checkpoints:** save workflow state so execution can resume. Configure checkpoint storage; in-memory storage does not survive restarts. This is workflow progress, not just chat history.

| Edge | Remember | Travel example |
| --- | --- | --- |
| **Direct** | A to B | Gather request, then process it. |
| **Conditional** | Follow an edge only if its condition matches. | No rooms? Suggest other dates. |
| **Switch-case** | Choose a branch using conditions. | VIP vs. standard service. |
| **Fan-out** | Send work to multiple executors in parallel. | Check flights and hotels. |
| **Fan-in** | Collect branch results for a downstream executor. | Build an itinerary from both results. |

### Workflow events

Event APIs vary by language/version. Current Python documentation uses **`WorkflowEvent.type`**; .NET uses named event classes.

| Meaning | .NET event | Current Python type |
| --- | --- | --- |
| Workflow begins | `WorkflowStartedEvent` | `"started"` |
| Final output produced | `WorkflowOutputEvent` | `"output"` |
| Workflow fails | `WorkflowErrorEvent` | `"failed"` |
| Executor starts | `ExecutorInvokeEvent` | `"executor_invoked"` |
| Executor finishes | `ExecutorCompleteEvent` | `"executor_completed"` |
| External input/approval requested | `RequestInfoEvent` | `"request_info"` |

**Caveats:** Python also distinguishes non-fatal `"error"` events. Request-info events ask for a response (for example, human approval); they are not logs of every outbound API call.

### Orchestration patterns

| Pattern | Control flow | Use when |
| --- | --- | --- |
| **Sequential** | Fixed order; output feeds the next agent. | Pipelines and progressive refinement. |
| **Concurrent** | Same task to multiple agents; collect independent results. | Parallel analysis and diverse perspectives. |
| **Handoff** | Transfer control dynamically to another agent. | Expert routing, escalation, or fallback. |
| **Group chat** | Shared conversation; a manager selects the next speaker. | Brainstorming and collaborative discussion. |
| **Magentic** | Manager plans, delegates, tracks progress, and adapts. | Complex, open-ended tasks with an evolving solution path. |

**Contrast:** group chat manages **who speaks next**; Magentic manages an **evolving plan**. A human can participate where configured.

### Concurrent workflow: implementation sequence

**Remember: client -> specialists -> parallel workflow -> run -> collect.**

1. Configure a chat client and credentials.
2. Create named agents with distinct instructions.
3. Build with `ConcurrentBuilder(participants=[...]).build()`.
4. Run with `events = await workflow.run(task)`.
5. Extract final outputs with `events.get_outputs()`.
6. In the current documented default, `outputs[0]` is an `AgentResponse`; iterate its `.messages` and read each message's `.author_name` and `.text`.

**Version trap:** older training examples use `create_agent()` and `.participants(...)`; the current concurrent tutorial uses `chat_client.as_agent()` and constructor `participants=...`. Match examples to installed SDK versions. A custom aggregator can change the output shape; collecting responses does not automatically synthesize consensus.

Workflow sources: [Edges](https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/edges) | [Events](https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/events) | [Checkpoints](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints) | [Patterns](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/) | [Concurrent tutorial](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/concurrent) (verified 2026-10-06).

## Foundry integration and service-side history

**Remember: the service stores history; your app keeps the session reference.**

- Connect to a **Foundry project** using Azure credentials (Microsoft Entra ID) to create/use agents with managed conversation history and tool/service integration.
- **Service-side chat history:** the service retains conversation messages, so your app need not manually resend the full history each turn.

| Provider/API | Service-managed chat history |
| --- | --- |
| Foundry Agent Service | Yes |
| Azure OpenAI Responses | Yes |
| OpenAI Responses | Yes |

**Caveats:** reuse the same session across turns and save/restore its reference across app restarts. Support depends on API/options; Responses support does not imply Chat Completions support. In multi-user apps, enforce session ownership.

Foundry is a strong fit for managed production agents, but service-side history is **not unique to Foundry** and is not, by itself, a reason to prefer it over every other provider.

Related: [Foundry Workflows retirement and migration](foundry-workflows.md).

Sources: [Framework overview](https://learn.microsoft.com/en-us/agent-framework/overview/) | [Agent concepts](https://learn.microsoft.com/en-us/agent-framework/concepts/agents/).

Details: [Function tools](https://learn.microsoft.com/en-us/agent-framework/agents/tools/function-tools) | [Workflows](https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/).

History: [Provider comparison](https://learn.microsoft.com/en-us/agent-framework/integrations/by-component/model-providers/) | [Agent sessions](https://learn.microsoft.com/en-us/agent-framework/concepts/agents/conversations/session).
