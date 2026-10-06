"""Foundry multi-turn chat with Microsoft Agent Framework.

Install requirements-maf.txt and sign in with `az login`.
Run with the "MAF: Foundry chat" F5 configuration to use the repository .venv.
For terminal runs, activate .venv first; existing terminals may still use system
Python. Keep both Agent Framework packages at the versions in requirements-maf.txt.
Set AZURE_AI_PROJECT_ENDPOINT and AZURE_AI_MODEL_DEPLOYMENT_NAME, or enter them
when prompted. The same session is reused until exit, but not saved for restarts.
The project endpoint must be https://<resource>.services.ai.azure.com/api/projects/<project>,
not an Azure OpenAI /openai/v1 endpoint. A valid environment value skips the prompt;
an invalid endpoint prints guidance and prompts again. Corrections apply to this run only.
Source: https://learn.microsoft.com/en-us/training/modules/develop-ai-agent-with-semantic-kernel/3-create-azure-ai-agent
"""

import asyncio
import os
import sys
from urllib.parse import urlsplit

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity.aio import DefaultAzureCredential


def setting(variable: str, prompt: str) -> str:
    return os.getenv(variable, "").strip() or input(f"{prompt}: ").strip()


def validate_project_endpoint(endpoint: str) -> str:
    endpoint = endpoint.strip().rstrip("/")
    message = (
        "AZURE_AI_PROJECT_ENDPOINT must be a Foundry project endpoint: "
        "https://<resource>.services.ai.azure.com/api/projects/<project>. "
        "Copy it from your Foundry project's overview, not an Azure OpenAI "
        "model endpoint."
    )
    try:
        url = urlsplit(endpoint)
    except ValueError:
        raise ValueError(message) from None
    segments = url.path.split("/")
    if (
        url.scheme != "https"
        or not url.hostname
        or url.hostname.endswith(".openai.azure.com")
        or url.username is not None
        or url.password is not None
        or url.query
        or url.fragment
        or len(segments) != 4
        or segments[1:3] != ["api", "projects"]
        or not segments[3]
    ):
        raise ValueError(message)
    return endpoint


def read_project_endpoint() -> str:
    endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT", "").strip()
    while True:
        if not endpoint:
            endpoint = input("Foundry project endpoint: ").strip()
        try:
            return validate_project_endpoint(endpoint)
        except ValueError as error:
            print(f"Invalid endpoint configuration. {error}", file=sys.stderr)
            endpoint = ""


async def main() -> None:
    endpoint = read_project_endpoint()
    model = setting("AZURE_AI_MODEL_DEPLOYMENT_NAME", "Model deployment name")

    async with (
        DefaultAzureCredential() as credential,
        AzureAIProjectAgentProvider(
            project_endpoint=endpoint, model=model, credential=credential
        ) as provider,
    ):
        agent = await provider.create_agent(
            name="maf-study-agent",
            instructions="You are a helpful study assistant. Give concise, accurate answers.",
        )
        session = agent.create_session()
        print("Ask a question, then a follow-up to test memory. Type 'exit' to finish.")
        while True:
            question = input("You: ").strip()
            if question.lower() in {"exit", "quit"}:
                break
            response = await agent.run(question, session=session)
            print(f"Agent: {response.text}\n")


if __name__ == "__main__":
    asyncio.run(main())
