# Aritra-Adhikary---Multi-Agent-Debate-DAG-using-LangGraph

# Multi-Agent Debate DAG (LLM-Backed)

This project implements a **LangGraph-style DAG** where two agents (Scientist & Philosopher) debate a user-defined topic for 8 rounds.  
It supports **pluggable LLM adapters**, automated logging, diagram generation, and demo video creation.

---

## 🚀 Features
- **Multi-Agent Debate**:  
  - Scientist (risk & safety focused)  
  - Philosopher (ethics & autonomy focused)  
  - Judge node decides winner after 8 rounds
- **Pluggable LLM Adapters** (`llm_adapters.py`)  
  - `OpenAIAdapter` – works with `OPENAI_API_KEY`  
  - `AnthropicAdapter` – stub (to extend)  
  - `AzureOpenAIAdapter` – stub (to extend)  
  - `FallbackAdapter` – deterministic offline mode
- **Visualization**: Generates DAG diagram in DOT, PNG, SVG, and PDF.  
- **Demo Output**: Transcript logs, GIF, MP4 video, captioned video.  
- **CI/CD**: GitHub Actions workflow runs the demo and uploads artifacts. 
## 📂 Project Structure
