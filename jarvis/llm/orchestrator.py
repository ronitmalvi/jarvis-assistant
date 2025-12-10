# jarvis/llm/orchestrator.py
import json
from typing import List, Dict

from jarvis.llm.client import OllamaClient
from jarvis.tools.registry import get_tool, list_tools

def build_system_prompt() -> str:
    """
    Tell the model what tools it has and how to call them using JSON.
    """
    tools = list_tools()
    tool_descriptions = []
    for name, tool in tools.items():
        tool_descriptions.append(f"- {name}: {tool.description}")
    tools_text = "\n".join(tool_descriptions)

    prompt = f"""
You are Jarvis, an AI assistant that can either:
1) Answer the user directly in natural language, OR
2) Call one of the available tools to perform an action.

Available tools:
{tools_text}

If the user asks you to perform an action that matches one of the tools
(e.g. "open YouTube", "open Chrome", "open google.com"), you MUST respond
with a JSON object ONLY, with this exact structure:

{{
  "type": "tool_call",
  "tool": "<tool_name>",
  "args": {{ ... }}
}}

Rules:
- Do NOT add any extra keys.
- Do NOT add comments or explanations.
- Do NOT wrap JSON in backticks.
- Do NOT include natural language outside of JSON when calling a tool.
- If no tool is needed, respond with normal natural language (no JSON).

Examples:
User: "Open YouTube"
Assistant:
{{"type": "tool_call", "tool": "open_url", "args": {{"url": "https://www.youtube.com"}}}}

User: "Open notepad"
Assistant:
{{"type": "tool_call", "tool": "open_app", "args": {{"name": "notepad.exe"}}}}
"""
    return prompt.strip()

class Orchestrator:
    def __init__(self, llm_client: OllamaClient):
        self.llm = llm_client

    def handle(self, user_text: str) -> str:
        system_prompt = build_system_prompt()

        response = self.llm.chat([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ])

        # Try to interpret response as JSON tool call
        try:
            data = json.loads(response)
            if isinstance(data, dict) and data.get("type") == "tool_call":
                tool_name = data.get("tool")
                args = data.get("args", {}) or {}

                tool = get_tool(tool_name)
                if not tool:
                    return f"I tried to call tool '{tool_name}', but it is not registered."

                # Execute the tool
                result = tool.func(args)

                # For low latency, just return the tool result directly
                # (You can later add another LLM call to 'explain' the result nicely)
                return str(result)
        except json.JSONDecodeError:
            # Not a JSON tool call – treat as normal assistant text
            pass

        # Normal assistant response
        return response
