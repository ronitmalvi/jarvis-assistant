from jarvis.audio.microphone import record
from jarvis.audio.stt import transcribe
from jarvis.llm.client import OllamaClient
from jarvis.llm.orchestrator import Orchestrator
from jarvis.tts.tts_client import speak
from jarvis.tools.system_tools import register as register_system_tools

def start_jarvis():
    # Register tools
    register_system_tools()

    llm = OllamaClient("qwen2.5")
    orchestrator = Orchestrator(llm)

    print("🤖 Jarvis initialized with tools. Press Enter and speak...")

    while True:
        input("\n👉 Press Enter to talk...")

        audio, sr = record()
        text = transcribe(audio, sr)

        print("🧑 You:", text)

        if not text:
            continue

        reply = orchestrator.handle(text)

        print("🤖 Jarvis:", reply)
        speak(reply)
