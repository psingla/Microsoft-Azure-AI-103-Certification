import os

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import MCPTool, PromptAgentDefinition
from azure.identity import DefaultAzureCredential
from openai.types.responses.response_input_param import ResponseInputParam

from azure.identity import DefaultAzureCredential
from azure.ai.textanalytics import TextAnalyticsClient


def setting(variable: str, prompt: str) -> str:
    return os.getenv(variable, "").strip() or input(f"{prompt}: ").strip()


resource_endpoint = setting("FOUNDRY_RESOURCE_ENDPOINT", "Foundry resource endpoint").rstrip("/")
model_deployment = "gpt-6-astra"

# Create client using endpoint and default Azure identity
credential = DefaultAzureCredential()
client = TextAnalyticsClient(endpoint=resource_endpoint, 
                             credential=credential)

# Assumes code to create TextAnalyticsClient is above...

# Example text to analyze
documents = ["Hello World!", "Bonjour le monde!"]

# Detect language
response = client.detect_language(documents=documents)
for doc in response:
    print(f"Document: {doc.id}")
    print(f"\tPrimary Language: {doc.primary_language.name}")
    print(f"\tISO6391 Name: {doc.primary_language.iso6391_name}")
    print(f"\tConfidence Score: {doc.primary_language.confidence_score}")