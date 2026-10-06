# Agent-to-Agent (A2A) protocol

**Remember: A2A = how agents collaborate; Skills = what an agent does; Card = how clients discover it.**

- **A2A protocol:** standardizes communication between agents across vendors/frameworks so they can exchange messages, share task context, and delegate work.
- **Agent Skills:** advertised tasks an agent can perform, described with names, descriptions, and examples. These describe capabilities, not their implementation.
- **Agent Card:** a JSON description containing the agent's identity, service endpoint, skills, supported protocol features, and authentication requirements.

**Discovery flow:** find the Agent Card -> select a suitable skill -> satisfy authentication requirements -> send an A2A request.

- Cards can be discovered through a well-known URL, a registry, or direct configuration; they need not be publicly accessible.
- **Security caveat:** interoperability does not automatically establish trust or grant access. Enforce authentication/authorization; never embed credentials in a card.

**Example:** a travel agent discovers a booking agent's card, sees its flight-booking skill, and delegates a booking request through A2A.

Source: [A2A agent discovery and Agent Cards](https://a2a-protocol.org/latest/topics/agent-discovery/).
