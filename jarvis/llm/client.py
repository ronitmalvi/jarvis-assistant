import requests
import json

class OllamaClient:
    def __init__(self, model="qwen2.5"):
        self.model = model

    def chat(self, messages):
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={"model": self.model, "messages": messages},
            stream=True   # IMPORTANT: enable streaming
        )

        full_text = ""

        for line in response.iter_lines():
            if not line:
                continue

            try:
                data = json.loads(line.decode("utf-8"))
            except json.JSONDecodeError:
                    continue   # skip bad lines

            # Each chunk is like: {"message": {"content": "..."}}
            if "message" in data and "content" in data["message"]:
                full_text += data["message"]["content"]

        return full_text.strip()
