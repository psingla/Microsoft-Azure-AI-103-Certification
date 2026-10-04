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

# Pass the previous response ID to retain context across chat turns.
last_response_id = None

print("Assistant: Enter a prompt (or type 'quit' to exit)")
while True:
    input_text = input("\nYou: ")
    if input_text.lower() == "quit":
        print("Assistant: Goodbye!")
        break

    response = openai_client.responses.create(
        model="gpt-4.1",
        instructions="You are a helpful AI assistant that explains technology concepts clearly.",
        input=input_text,
        previous_response_id=last_response_id,
    )
    print("\nAssistant:", response.output_text)
    last_response_id = response.id