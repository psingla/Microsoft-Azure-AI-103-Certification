import os

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import MCPTool, PromptAgentDefinition
from azure.identity import DefaultAzureCredential
from openai.types.responses.response_input_param import ResponseInputParam


def setting(variable: str, prompt: str) -> str:
    return os.getenv(variable, "").strip() or input(f"{prompt}: ").strip()


project_endpoint = setting("AZURE_AI_PROJECT_ENDPOINT", "Foundry project endpoint").rstrip("/")
search_endpoint = setting("AZURE_SEARCH_ENDPOINT", "Azure AI Search endpoint").rstrip("/")
connection_name = setting("AZURE_SEARCH_CONNECTION_NAME", "Foundry MCP connection name")
model_deployment = "gpt-6-astra"
question = input("Your question: ").strip()

credential = DefaultAzureCredential()
project_client = AIProjectClient(endpoint=project_endpoint, credential=credential)

knowledge_tool = MCPTool(
    server_label="product-docs",
    server_url=(
        f"{search_endpoint}/knowledgebases/product-documentation/mcp"
        "?api-version=2026-08-01-preview"
    ),
    project_connection_id=connection_name,
    allowed_tools=["knowledge_base_retrieve"],
)

agent = project_client.agents.create_version(
    agent_name="product-support-agent",
    definition=PromptAgentDefinition(
        model=model_deployment,
        instructions="Answer product questions using the knowledge base. Always cite your sources.",
        tools=[knowledge_tool],
    ),
)

agent_reference = {
    "agent_reference": {
        "type": "agent_reference",
        "name": agent.name,
        "version": agent.version,
    }
}
with project_client.get_openai_client() as openai_client:
    response = openai_client.responses.create(input=question, extra_body=agent_reference)
    while True:
        if response.status != "completed":
            raise SystemExit("The agent response did not complete successfully.")

        approvals: ResponseInputParam = []
        for item in response.output:
            if item.type == "mcp_approval_request":
                approved = input("Allow querying the knowledge base? [y/N]: ").strip().lower()
                approvals.append(
                    {
                        "type": "mcp_approval_response",
                        "approval_request_id": item.id,
                        "approve": approved in {"y", "yes"},
                    }
                )
            elif item.type == "mcp_call" and item.error:
                raise SystemExit("The knowledge-base MCP call failed.")

        if not approvals:
            break
        response = openai_client.responses.create(
            input=approvals,
            previous_response_id=response.id,
            extra_body=agent_reference,
        )

    print(f"\nAgent: {response.output_text}")
