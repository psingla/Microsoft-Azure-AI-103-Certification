# Agent Publishing

**Remember: publish = stable URL + separate identity + controlled access.**

In the **legacy Agent Application publishing model**, publishing creates:

- **Stable invocation URL**: stays the same when you roll out new agent versions.
- **Distinct Microsoft Entra agent identity**: separate from the project's shared identity.
- **Independent access control**: grant callers access without granting project access.

**Identity changes; permissions do not transfer.** Grant the published identity access to downstream resources such as Azure AI Search.

**User-data caveat:** do not assume full end-user isolation. The documented Agent Application Responses endpoint is stateless; conversation APIs are unavailable pending end-user isolation support. The client must keep each user's conversation history separate.

Source: [Microsoft Learn: Agent Applications](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/agent-applications) (checked 2026-10-06; marked legacy).

## Microsoft 365 Agents Toolkit

**Default: Foundry portal. Custom enterprise integration: Agents Toolkit.**

**Toolkit = development tools**, available as a VS Code extension and through the Visual Studio Installer for Visual Studio.

For most scenarios, publish directly from the **Foundry portal** to **Microsoft Teams and Microsoft 365 Copilot**.

Use **Microsoft 365 Agents Toolkit** to build a proxy application connected to your Foundry agent when the integration layer needs:

- Custom single sign-on (SSO) beyond the default Microsoft Entra ID setup.
- Middleware for custom processing, logging, or data transformation between Teams and the Foundry agent.
- Multi-environment deployment pipelines.

The proxy is an extra application to build, host, and maintain, not a requirement for every agent.

Related: [Publish to Microsoft Copilot and Teams](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot).

Toolkit availability: [VS Code](https://learn.microsoft.com/en-us/microsoftteams/platform/toolkit/agents-toolkit-fundamentals) | [Visual Studio](https://learn.microsoft.com/en-us/microsoftteams/platform/toolkit/toolkit-v4/agents-toolkit-fundamentals-vs).
