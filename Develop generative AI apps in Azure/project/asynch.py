import asyncio
import os

from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider
from openai import AsyncOpenAI

async def ask(client: AsyncOpenAI, prompt: str) -> str:
    response = await client.responses.create(
        model="gpt-4.1",
        input=prompt,
        stream=False
    )
    return response.output_text

async def main() -> None:
    # The environment variable must contain the full URL, including /openai/v1/.
    base_url = os.getenv("AZURE_OPENAI_BASE_URL", "").strip()
    if not base_url:
        raise SystemExit("Set AZURE_OPENAI_BASE_URL in your terminal before running Python.")

    # Issue three requests concurrently instead of one after another
    prompts = [
        "Explain quantum computing briefly.",
        "Summarize the benefits of async I/O.",
        "Give a one-sentence definition of machine learning."
    ]
    async with DefaultAzureCredential() as credential:
        token_provider = get_bearer_token_provider(
            credential, "https://ai.azure.com/.default"
        )
        async with AsyncOpenAI(
            base_url=base_url,
            api_key=token_provider,
        ) as client:
            results = await asyncio.gather(*(ask(client, p) for p in prompts))
    for prompt, output in zip(prompts, results):
        print(f"Q: {prompt}\nA: {output}\n")

if __name__ == "__main__":
    asyncio.run(main())