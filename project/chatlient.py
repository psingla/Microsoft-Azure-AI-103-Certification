from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_endpoint = "https://pramodmafprj3-resource.services.ai.azure.com/api/projects/pramodmafprj3"
project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint
)

openai_client = project_client.get_openai_client(api_version="2024-10-21")