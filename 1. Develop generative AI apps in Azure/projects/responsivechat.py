import os

from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# The environment variable must contain the full URL, including /openai/v1/.
base_url = os.getenv("AZURE_OPENAI_BASE_URL", "").strip()
if not base_url:
    raise SystemExit("Set AZURE_OPENAI_BASE_URL in your terminal before running Python.")

# Use Microsoft Entra credentials instead of a hardcoded API key.
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)
openai_client = OpenAI(
    base_url=base_url,
    api_key=token_provider,
)

# Streaming returns events incrementally instead of a single completed response.
stream = openai_client.responses.create(
    model="gpt-4.1",
    input="Write a short story about a robot learning to paint.",
    stream=True,
)

for event in stream:
    print(event, end="", flush=True)