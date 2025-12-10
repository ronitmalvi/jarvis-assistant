# jarvis/tools/registry.py
from typing import Callable, Dict, Any

class Tool:
    def __init__(self, name: str, description: str, func: Callable[[Dict[str, Any]], str]):
        self.name = name
        self.description = description
        self.func = func

TOOLS: Dict[str, Tool] = {}

def register_tool(tool: Tool):
    TOOLS[tool.name] = tool

def get_tool(name: str) -> Tool | None:
    return TOOLS.get(name)

def list_tools() -> Dict[str, Tool]:
    return TOOLS
