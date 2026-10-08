# Agent Hosting: Foundry Agent Service vs. Azure Container Apps

**Remember: ACA manages containers; FAS adds an agent-specific runtime. MAF defines agent behavior on either.**

This comparison covers **code-first hosted agents** in Foundry Agent Service (FAS), not prompt-only agents or the legacy Agent Application publishing model.

## What FAS adds

Both platforms manage infrastructure. FAS's advantage is less agent-platform integration to build yourself.

| Concern | FAS hosted agents | Agent deployed directly to ACA |
| --- | --- | --- |
| **Agent API** | Supported agent protocols; Responses integrates conversational streaming and session lifecycle. | ACA provides ingress; your application supplies the agent API and streaming behavior. |
| **Conversation state** | Responses supports managed history and conversation-ID threading. | Your application/framework manages history, session routing, and persistence. |
| **Session isolation** | Current hosted-agent runtime provides per-session isolated sandboxes, persistent files, and stateful resume. | Container replicas are not isolated agent sessions; design user/session isolation and durable storage. |
| **Identity** | Dedicated agent identity; you still grant downstream permissions. | Managed identities are available; configure their use and application-level authorization. |
| **Operations** | Agent lifecycle, versions, and observability integration. | Container revisions, scaling, and logs; add agent-specific instrumentation and management. |
| **Teams integration** | Supported publishing path with managed channel integration. | Host your own integration, or use ACA as an adapter to a Foundry-hosted agent. |

**Platform-managed state is not a substitute for authorization:** enforce session ownership and permissions for tool calls. Capabilities depend on the protocol, supported region, and runtime version.

## When to choose each

- **Choose FAS** when you want a managed agent runtime with integrated conversations, identity, lifecycle, and Foundry publishing.
- **Choose ACA** when you need a general application host for agents, APIs, jobs, and microservices, with direct control over ingress, revisions, traffic splitting, and scaling triggers.
- **Reuse existing infrastructure:** ACA is attractive if your application already handles agent state, security, and observability.
- **They are not exclusive:** an agent on ACA can still call Foundry models and services.

## How both fit the architecture

**Teams -> custom adapter on ACA -> agent hosted in FAS**

- **ACA:** hosts the custom Teams integration.
- **FAS:** hosts the agent and supplies its managed runtime.
- **MAF:** defines the agent's behavior and orchestration.

Use this split when a custom adapter is needed. Otherwise, consider supported direct Foundry publishing. Backend streaming alone does not guarantee progressive text in Teams; validate the full delivery path.

## Avoid these assumptions

- FAS is not automatically faster, cheaper, or more accurate.
- Managed hosting and autoscaling are not exclusive to FAS; ACA provides both.
- Neither platform removes responsibility for authorization, tool safety, evaluation, or application correctness.

Related: [MAF](microsoft-agent-framework.md) | [Publishing and legacy-model caveats](agent-publishing.md) | [Teams + Foundry architecture](../../architecture/teams-foundry-agent-architecture.html).

Sources: [Foundry hosted agents](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents) | [Azure Container Apps overview](https://learn.microsoft.com/en-us/azure/container-apps/overview).

*Sources checked: 2026-10-07. Hosting capabilities and protocol support can change.*
