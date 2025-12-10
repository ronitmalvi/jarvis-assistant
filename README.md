# Jarvis Assistant
An audio-first multimodal AI assistant built using **completely free** and **local** models — Whisper (STT), Ollama (LLM), and pyttsx3 (TTS).

## Features
- 🎤 Voice input (microphone)
- 🧠 Local reasoning with free LLMs via Ollama
- 🗣 Offline TTS using pyttsx3
- 🛠 Extensible tool system (coming soon)
- 👁️ Optional vision features (coming soon)

## Tech Stack
- Python 3.10+
- Faster-Whisper (local STT)
- Ollama (local LLM engine)
- pyttsx3 (offline TTS)
- sounddevice, numpy, requests

## Running Locally
1. Clone the repo  
2. Create venv  
3. Install requirements  
4. Install Ollama and pull a model  
5. Run `python main.py`

---

## Roadmap
- [x] Phase 1: Voice → LLM → Voice
- [ ] Phase 2: Tool layer (system automation)
- [ ] Phase 3: Wake word
- [ ] Phase 4: Vision support
- [ ] Phase 5: MCP tool servers


## Phase 1 — Voice Assistant (Completed)

JARVIS now supports basic voice interaction:
- Records your voice  
- Converts speech to text using Faster-Whisper  
- Generates replies using the local Qwen2.5 model (Ollama)  
- Responds back using offline TTS (pyttsx3)

Fully offline, free, and functional.

## Phase 2 — Tool Layer (In Progress)
Jarvis can now decide when to call tools using a simple JSON protocol and can open apps and URLs on the system (e.g., "open YouTube", "open notepad").

