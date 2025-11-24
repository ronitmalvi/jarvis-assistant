from jarvis.audio.microphone import record
from jarvis.audio.stt import transcribe
from jarvis.llm.client import OllamaClient
from jarvis.tts.tts_client import speak

def start_jarvis():
    llm = OllamaClient("qwen2.5")

    print("🤖 Jarvis initialized. Press Enter and speak...")

    while True:
        input("\n👉 Press Enter to talk...")

        audio, sr = record()
        text = transcribe(audio, sr)

        print("🧑 You:", text)

        reply = llm.chat([
            {"role": "system", "content": "You are Jarvis, a friendly conversational AI assistant."},
            {"role": "user", "content": text}
        ])

        print("🤖 Jarvis:", reply)
        speak(reply)
