import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
import logging

logger = logging.getLogger(__name__)

class AzureClient:
    def __init__(self):
        self.api_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4")
        
        if not self.api_key or not self.endpoint:
            logger.warning("Azure OpenAI API Key or Endpoint not found in environment variables.")
            # Mocking for scaffolding if credentials are missing
            self.client = None
        else:
            self.client = AzureOpenAI(
                api_key=self.api_key,
                api_version="2023-05-15",
                azure_endpoint=self.endpoint
            )

    def get_completion(self, prompt, temperature=0.0):
        if self.client is None:
            logger.info("Mocking Azure OpenAI response.")
            return "Score: 5\nReasoning: The response is accurate and follows the instructions perfectly."

        try:
            response = self.client.chat.completions.create(
                model=self.deployment_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error calling Azure OpenAI: {e}")
            return None
