"""Foundry multi-turn chat with Microsoft Agent Framework.

Install requirements-maf.txt and sign in with `az login`.
Run with the "MAF: Foundry chat" F5 configuration to use the repository .venv.
For terminal runs, activate .venv first; existing terminals may still use system
Python. Keep both Agent Framework packages at the versions in requirements-maf.txt.
Set AZURE_AI_PROJECT_ENDPOINT and AZURE_AI_MODEL_DEPLOYMENT_NAME, or enter them
when prompted. The same session is reused until exit, but not saved for restarts.
Source: https://learn.microsoft.com/en-us/training/modules/develop-ai-agent-with-semantic-kernel/3-create-azure-ai-agent
"""

import asyncio
import os

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity.aio import DefaultAzureCredential


def setting(variable: str, prompt: str) -> str:
    return os.getenv(variable, "").strip() or input(f"{prompt}: ").strip()


async def main() -> None:
    endpoint = setting("AZURE_AI_PROJECT_ENDPOINT", "Foundry project endpoint").rstrip("/")
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
