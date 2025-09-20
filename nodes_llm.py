import os, time, hashlib
from llm_adapters import BaseAdapter, FallbackAdapter

class LLMAgent:
    def __init__(self, name: str, persona: str, system_prompt: str, fallback_keywords=[], adapter: BaseAdapter = None):
        self.name = name
        self.persona = persona
        self.system_prompt = system_prompt
        self.adapter = adapter if adapter is not None else FallbackAdapter()
        self.fallback_keywords = fallback_keywords

    def generate(self, topic: str, round_number:int, memory:dict):
        prompt = self._build_prompt(topic, round_number, memory)
        try:
            return f"[Round {round_number}] {self.name}: " + self.adapter.generate(prompt)
        except Exception as e:
            return f"[Round {round_number}] {self.name}: (fallback) As a {self.persona}, I argue about {topic}."

    def _build_prompt(self, topic, round_number, memory):
        lines = [f"You are {self.name} — {self.persona}.", f"Topic: {topic}", f"Round: {round_number}"]
        if memory.get('self_summary'):
            lines.append('Recent: ' + ' | '.join(memory.get('self_summary')))
        if memory.get('last_opponent'):
            lines.append('Last opponent: ' + memory.get('last_opponent'))
        lines.append('Respond concisely in 2-4 sentences.')
        return '\n'.join(lines)
