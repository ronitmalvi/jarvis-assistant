# jarvis/tools/system_tools.py
import webbrowser
import subprocess
import os
import sys

from jarvis.tools.registry import Tool, register_tool

def open_url(args):
    url = args.get("url")
    if not url:
        return "No URL provided."
    webbrowser.open(url)
    return f"Opening {url}"

def open_app(args):
    """
    Args:
      name: executable name or path, e.g. 'notepad.exe', 'chrome.exe'
    """
    name = args.get("name")
    if not name:
        return "No application name provided."

    try:
        if sys.platform.startswith("win"):
            # On Windows, os.startfile can open apps by path or associated programs
            os.startfile(name)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", "-a", name])
        else:
            subprocess.Popen([name])
        return f"Opening application: {name}"
    except Exception as e:
        return f"Failed to open {name}: {e}"

def register():
    register_tool(Tool(
        name="open_url",
        description="Open a URL in the default browser. Args: {\"url\": \"https://...\"}",
        func=open_url,
    ))
    register_tool(Tool(
        name="open_app",
        description="Open a local application by name or path. Args: {\"name\": \"notepad.exe\"}",
        func=open_app,
    ))
