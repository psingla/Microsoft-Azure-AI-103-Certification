# Why tools matter

**Tools connect AI reasoning to external data and real-world actions.**

- **Fetch current data:** weather, prices, or live API results beyond training data.
- **Take actions:** send emails, create records, or trigger workflows.
- **Ground answers:** retrieve authoritative information to reduce factual errors.
- **Extend capabilities:** connect existing systems, databases, and business logic.
- **Coordinate workflows:** combine tool calls into multi-step tasks.

**Remember:** tools improve access, not guaranteed accuracy. Validate results and require appropriate permissions for actions.

## Who chooses the tool?

**The model chooses; instructions guide; tool-selection settings constrain.**

- **Default (automatic selection):** the model decides whether to call an available tool and which one, based on the prompt and context.
- **Instructions (system prompt):** guide when and how tools should be used.
- **Tool-selection rules:** configure allowed or required choices; instructions alone do not enforce these constraints.
