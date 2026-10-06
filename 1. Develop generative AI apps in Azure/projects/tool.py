from openai import OpenAI
import os
from pathlib import Path

from azure.identity import DefaultAzureCredential, get_bearer_token_provider


# The environment variable must contain the full URL, including /openai/v1/.
base_url = os.getenv("AZURE_OPENAI_BASE_URL", "").strip()
if not base_url:
    raise SystemExit("Set AZURE_OPENAI_BASE_URL in your terminal before running Python.")

# Resolve the document beside this script, regardless of the terminal's folder.
policy_path = Path(__file__).resolve().with_name("center_of_mass.pdf")
if not policy_path.is_file():
    raise SystemExit("Place center_of_mass.pdf in the same folder as tool.py before running.")

# Use Microsoft Entra credentials instead of a hardcoded API key.
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)
openai_client = OpenAI(
    base_url=base_url,
    api_key=token_provider,
)

# Get response using the code_interpreter tool
'''response = openai_client.responses.create(
    model="gpt-6-astra",
    instructions="You are an AI assistant that provides information. Use the python tool to run code for math problems.",
    input="30 people in room. how many handshakes occur?",
    tools=[{"type": "code_interpreter",
            "container": {"type": "auto"}}]
)
print(response.output_text)'''


# Create vector store and upload a file
with policy_path.open("rb") as policy_file:
    vector_store = openai_client.vector_stores.create(name="policy-docs")
    openai_client.vector_stores.files.upload_and_poll(
        vector_store_id=vector_store.id,
        file=policy_file,
    )

# Get response using the file_search tool
stream = openai_client.responses.create(
    model="gpt-6-astra",
    instructions="You are an AI assistant that provides related information to center of mass.",
    input="Explain the concept of center of mass in physics in layman terms.",
    stream=True,
    tools=[{
        "type": "file_search",
        "vector_store_ids": [vector_store.id]
    }],
    include=["file_search_call.results"]
)
completed = False
with stream:
    for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)
        elif event.type == "response.completed":
            completed = True
        elif event.type in ("error", "response.failed", "response.incomplete"):
            raise SystemExit(f"\nResponse did not complete: {event.type}")
if not completed:
    raise SystemExit("\nResponse stream ended before completion.")
print()