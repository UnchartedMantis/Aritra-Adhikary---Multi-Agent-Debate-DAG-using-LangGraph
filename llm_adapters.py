"""llm_adapters.py

Provides a pluggable adapter interface for multiple LLM providers.
Adapters implement a common `generate` method: generate(prompt, max_tokens, temperature)
This file includes:
- OpenAIAdapter (uses openai package; requires OPENAI_API_KEY)
- AnthropicAdapter (stub showing how to integrate; requires ANTHROPIC_API_KEY)
- AzureOpenAIAdapter (stub showing Azure usage; requires AZURE credentials)
- FallbackAdapter (deterministic local fallback)
Each adapter raises RuntimeError if required credentials or packages are missing.
"""

import os

class AdapterError(Exception):
    pass

class BaseAdapter:
    def generate(self, prompt: str, max_tokens: int = 200, temperature: float = 0.7) -> str:
        raise NotImplementedError()

class OpenAIAdapter(BaseAdapter):
    def __init__(self, model: str = None):
        try:
            import openai
            self.openai = openai
        except Exception as e:
            raise AdapterError('openai package not installed') from e
        self.api_key = os.environ.get('OPENAI_API_KEY')
        if not self.api_key:
            raise AdapterError('OPENAI_API_KEY not set')
        self.openai.api_key = self.api_key
        self.model = model or os.environ.get('OPENAI_MODEL', 'gpt-4o-mini')

    def generate(self, prompt: str, max_tokens: int = 200, temperature: float = 0.7) -> str:
        resp = self.openai.ChatCompletion.create(
            model=self.model,
            messages=[{'role':'user','content':prompt}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return resp['choices'][0]['message']['content'].strip()

class AnthropicAdapter(BaseAdapter):
    def __init__(self):
        # This is a stub. To enable, install `anthropic` package and set ANTHROPIC_API_KEY.
        self.api_key = os.environ.get('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise AdapterError('ANTHROPIC_API_KEY not set')
        # Normally you'd set up client here; omitted to keep repo offline-friendly.

    def generate(self, prompt: str, max_tokens: int = 200, temperature: float = 0.7) -> str:
        raise AdapterError('AnthropicAdapter is a stub in this repo. Implement API calls to Anthropic.')

class AzureOpenAIAdapter(BaseAdapter):
    def __init__(self, deployment_name: str = None):
        # Stub demonstrating required env vars for Azure OpenAI
        self.endpoint = os.environ.get('AZURE_OPENAI_ENDPOINT')
        self.key = os.environ.get('AZURE_OPENAI_KEY')
        self.deployment = deployment_name or os.environ.get('AZURE_OPENAI_DEPLOYMENT')
        if not (self.endpoint and self.key and self.deployment):
            raise AdapterError('Azure OpenAI environment variables not fully configured.')
        # Real implementation would use azure.ai.openai package.

    def generate(self, prompt: str, max_tokens: int = 200, temperature: float = 0.7) -> str:
        raise AdapterError('AzureOpenAIAdapter is a stub. Implement Azure OpenAI SDK calls here.')

class FallbackAdapter(BaseAdapter):
    def generate(self, prompt: str, max_tokens: int = 200, temperature: float = 0.7) -> str:
        # Simple deterministic echo with truncation
        return prompt.strip()[:max_tokens] + "\n\n[local fallback]"
